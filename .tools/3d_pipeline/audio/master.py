"""Auditable, source-only mastering for installed unit recordings.

The CLI measures existing audio and writes derivatives only beneath an
explicit evidence/output directory. It never edits runtime inputs.
"""

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import json
import math
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from typing import Any, Dict, List, Optional, Sequence, Tuple

try:
    from .inventory import (
        build_sound_coverage,
        flatten_runtime_inventory,
        load_json,
        source_lineage,
        summarize_duplicates,
    )
    from .metrics import (
        AudioToolError,
        analyze_audio,
        binary_version,
        decode_mono_f32,
        find_recorded_loop_crossfade,
        measure_max_gain_reduction_db,
        resolve_binary,
        sha256_file,
    )
except ImportError:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from audio.inventory import (
        build_sound_coverage,
        flatten_runtime_inventory,
        load_json,
        source_lineage,
        summarize_duplicates,
    )
    from audio.metrics import (
        AudioToolError,
        analyze_audio,
        binary_version,
        decode_mono_f32,
        find_recorded_loop_crossfade,
        measure_max_gain_reduction_db,
        resolve_binary,
        sha256_file,
    )


SAMPLE_RATE = 44100
FADE_IN_SECONDS = 0.008
FADE_OUT_SECONDS = 0.050
MAX_LIMITER_REDUCTION_DB = 6.5
LIMITER_STEPS_DB = (0.0, 1.5, 3.0, 4.5, 6.0, 6.5)
SUPPORTED_AUDIO = {".wav", ".ogg", ".flac", ".mp3", ".aiff", ".aif"}


def _json_write(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _is_under(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def _run_ffmpeg(ffmpeg: str, source: Path, output: Path, audio_filter: str,
                codec: str = "pcm_s16le", extra_input_args: Optional[Sequence[str]] = None) -> List[str]:
    output.parent.mkdir(parents=True, exist_ok=True)
    command = [ffmpeg, "-hide_banner", "-nostats", "-v", "error", "-y"]
    if extra_input_args:
        command.extend(extra_input_args)
    command.extend(["-i", str(source), "-map", "0:a:0", "-vn", "-af", audio_filter,
                    "-ar", str(SAMPLE_RATE), "-ac", "1", "-c:a", codec, str(output)])
    process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    if process.returncode != 0:
        raise AudioToolError("ffmpeg processing failed: {}".format(
            process.stderr.decode("utf-8", errors="replace")[-2500:]))
    return command


def _render_preprocessed(ffmpeg: str, source: Path, output: Path, start_seconds: float,
                         duration_seconds: float) -> List[str]:
    start_seconds = max(0.0, start_seconds)
    remaining = max(0.05, duration_seconds - start_seconds)
    fade_out_start = max(0.0, remaining - FADE_OUT_SECONDS)
    audio_filter = (
        "highpass=f=30,atrim=start={:.9f},asetpts=PTS-STARTPTS,"
        "afade=t=in:st=0:d={:.6f},afade=t=out:st={:.6f}:d={:.6f}"
    ).format(start_seconds, FADE_IN_SECONDS, fade_out_start, FADE_OUT_SECONDS)
    return _run_ffmpeg(ffmpeg, source, output, audio_filter, "pcm_f32le")


def _postmaster_trim(ffmpeg: str, source: Path, output: Path, lead_ms: float,
                     evidence: Optional[List[Dict[str, Any]]] = None) -> Tuple[float, List[str]]:
    """Remove measured excess lead while retaining 10 ms of recorded pre-roll.

    A quiet first transient can fall below the onset detector after the fade-in
    is applied. Remeasure and trim only the newly observed lead, for at most
    three passes, rather than assuming the first measurement survived mastering.
    """
    commands: List[str] = []
    current = source
    total_trim = 0.0
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="postmaster_trim_", dir=str(output.parent)) as temp_name:
        temp_root = Path(temp_name)
        for attempt in range(3):
            current_analysis = analyze_audio(current, ffmpeg)
            measured = current_analysis["direct_sample_metrics"].get("leading_silence_ms_at_minus55db")
            if measured is None or measured <= 20.0:
                break
            trim_start = max(0.0, float(measured) / 1000.0 - 0.010)
            total_trim += trim_start
            duration = float(current_analysis["ffprobe"]["duration_seconds"])
            target = output if attempt == 2 else temp_root / "trim_pass_{}.wav".format(attempt + 1)
            input_sha = sha256_file(current)
            pass_commands = _render_preprocessed(ffmpeg, current, target, trim_start, duration)
            commands.extend(pass_commands)
            pass_analysis = analyze_audio(target, ffmpeg)
            if evidence is not None:
                evidence.append({
                    "pass": attempt + 1,
                    "input_sha256": input_sha,
                    "measured_leading_silence_ms": measured,
                    "trim_start_seconds": trim_start,
                    "output_sha256": sha256_file(target),
                    "output_leading_silence_ms": pass_analysis["direct_sample_metrics"].get("leading_silence_ms_at_minus55db"),
                    "command": pass_commands,
                })
            current = target
        if current != output:
            shutil.copy2(current, output)
    return total_trim, commands


def _default_output_path(output_root: Path, unit_id: str, soundeffect: str, source: str) -> Path:
    import hashlib
    digest = hashlib.sha256(source.replace("\\", "/").encode("utf-8")).hexdigest()[:8]
    basename = Path(source.replace("\\", "/")).name
    stem = Path(basename).stem
    suffix = Path(basename).suffix or ".wav"
    cue = str(soundeffect or "unassigned_cue").replace("/", "_").replace("\\", "_")
    unit = str(unit_id or "unknown_unit").replace("/", "_").replace("\\", "_")
    return output_root / unit / (cue + "_" + stem + "_" + digest + suffix)


def _source_gate(analysis: Dict[str, Any], role: str, subsonic: bool) -> List[str]:
    blockers: List[str] = []
    clipping = analysis.get("clipping", {})
    direct = analysis.get("direct_sample_metrics", {})
    if clipping.get("probable_flat_top") is True or direct.get("probable_flat_top") is True:
        blockers.append("source_has_probable_clipped_flat_tops")
    if direct.get("nonfinite_sample_count") not in (None, 0):
        blockers.append("source_contains_nonfinite_samples")
    if analysis.get("long_form_exempt_from_unit_sfx_centroid_gate"):
        blockers.append("source_exceeds_unit_sfx_duration_scope")
    centroid = analysis.get("spectral", {}).get("centroid_hz_median")
    if centroid is None and not subsonic:
        blockers.append("source_spectral_centroid_unavailable")
    elif centroid is not None and centroid <= 200.0 and not subsonic:
        blockers.append("source_centroid_at_or_below_200_hz_without_subsonic_declaration")
    return blockers


def _gain_filter(gain_db: float) -> str:
    return "volume={:.6f}dB".format(gain_db)


def _write_recorded_float(ffmpeg: str, samples: Sequence[float], output: Path) -> List[str]:
    import array
    output.parent.mkdir(parents=True, exist_ok=True)
    values = array.array("f", (float(value) for value in samples))
    if sys.byteorder != "little":
        values.byteswap()
    command = [ffmpeg, "-hide_banner", "-nostats", "-v", "error", "-y", "-f", "f32le",
               "-ar", str(SAMPLE_RATE), "-ac", "1", "-i", "pipe:0", "-c:a", "pcm_f32le", str(output)]
    process = subprocess.run(command, input=values.tobytes(), stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE, check=False)
    if process.returncode != 0:
        raise AudioToolError("could not write recorded-sample intermediate: {}".format(
            process.stderr.decode("utf-8", errors="replace")[-2000:]))
    return command


def _limiter_stage(ffmpeg: str, base: Path, limiter_path: Path, requested_reduction_db: float,
                   base_peak_dbfs: float) -> Dict[str, Any]:
    """Push recorded peaks by a bounded amount into a sample-peak limiter."""
    gain_db = max(0.0, -base_peak_dbfs) + requested_reduction_db
    gained_path = limiter_path.with_name(limiter_path.stem + "_gain.wav")
    gain_command = _run_ffmpeg(ffmpeg, base, gained_path, _gain_filter(gain_db), "pcm_f32le")
    gained = decode_mono_f32(gained_path, ffmpeg)
    limiter_filter = "alimiter=limit=1:attack=5:release=50:level=false:latency=true"
    limiter_command = _run_ffmpeg(ffmpeg, gained_path, limiter_path, limiter_filter, "pcm_f32le")
    limited = decode_mono_f32(limiter_path, ffmpeg)
    reduction = measure_max_gain_reduction_db(gained, limited)
    reduction["requested_peak_push_db"] = requested_reduction_db
    reduction["normalizing_gain_before_limiter_db"] = gain_db
    reduction["ceiling"] = "0 dBFS sample peak before EBU true-peak loudness normalization"
    reduction["maximum_allowed_db"] = MAX_LIMITER_REDUCTION_DB
    # FFmpeg float output adds sub-micro-dB arithmetic noise at this exact
    # ceiling, so allow only that measured precision at 6.5 dB.
    reduction["within_bounded_policy"] = reduction["max_sample_gain_reduction_db"] <= MAX_LIMITER_REDUCTION_DB + 0.0001
    return {"gain_command": gain_command, "limiter_command": limiter_command,
            "gain_stage_sha256": sha256_file(gained_path), "limiter_stage_sha256": sha256_file(limiter_path),
            "gain_reduction": reduction, "gained_path": gained_path}


def _peak_guard(ffmpeg: str, source: Path, output: Path, target_peak_dbfs: float) -> Dict[str, Any]:
    analysis = analyze_audio(source, ffmpeg)
    peak = analysis["direct_sample_metrics"].get("sample_peak_dbfs")
    true_peak = analysis["ebur128"].get("true_peak_dbtp")
    if peak is None or true_peak is None:
        return {"applied": False, "reason": "peak measurement unavailable"}
    requested_gain = target_peak_dbfs - peak
    safe_gain = min(requested_gain, -1.05 - true_peak)
    # Only boost when it preserves the sample-peak band. Attenuation is always
    # retained to prevent a clip overshoot.
    if requested_gain < 0.0:
        safe_gain = requested_gain
    if abs(safe_gain) < 0.03:
        shutil.copy2(source, output)
        return {"applied": False, "gain_db": 0.0, "source_peak_dbfs": peak,
                "source_true_peak_dbtp": true_peak}
    command = _run_ffmpeg(ffmpeg, source, output, _gain_filter(safe_gain), "pcm_s16le")
    return {"applied": True, "gain_db": safe_gain, "requested_gain_db": requested_gain,
            "source_peak_dbfs": peak, "source_true_peak_dbtp": true_peak, "command": command}


def _role_checks(analysis: Dict[str, Any], role: str, subsonic: bool,
                 expected_loop_delta: Optional[float] = None) -> Dict[str, bool]:
    direct = analysis["direct_sample_metrics"]
    probe = analysis["ffprobe"]
    ebur = analysis["ebur128"]
    peak = direct.get("sample_peak_dbfs")
    rms = direct.get("sample_rms_dbfs")
    true_peak = ebur.get("true_peak_dbtp")
    loudness = ebur.get("integrated_lufs")
    checks = {
        "runtime_codec_pcm_s16le": probe.get("codec_name") == "pcm_s16le",
        "runtime_sample_rate_44100": probe.get("sample_rate") == SAMPLE_RATE,
        "runtime_mono": probe.get("channels") == 1,
        "runtime_16_bit": probe.get("bits_per_sample") == 16,
        "lead_silence_at_most_20ms": direct.get("leading_silence_ms_at_minus55db") is not None
        and direct["leading_silence_ms_at_minus55db"] <= 20.0,
        "astats_flat_factor_observed": analysis.get("astats", {}).get("flat_factor") is not None,
        "no_direct_flat_top": direct.get("probable_flat_top") is False,
        "spectral_centroid_above_200_hz_or_explicit_subsonic": (
            subsonic or (analysis["spectral"].get("centroid_hz_median") is not None
                         and analysis["spectral"]["centroid_hz_median"] > 200.0)
        ),
        "true_peak_at_or_below_minus_1_dbtp": true_peak is not None and true_peak <= -1.0,
    }
    lowered = role.lower()
    if lowered in ("loop", "idle_loop", "movement_loop"):
        checks["loop_loudness_minus20_plusminus1"] = loudness is not None and abs(loudness + 20.0) <= 1.0
        checks["loop_inner_edge_rms_within3db"] = expected_loop_delta is not None and expected_loop_delta <= 3.0
    elif lowered in ("step", "steps", "footstep"):
        checks["step_peak_target_minus6_plusminus0_8"] = peak is not None and abs(peak + 6.0) <= 0.8
        checks["step_loudness_minus23_plusminus5_when_gated"] = (
            float(probe.get("duration_seconds") or 0.0) < 0.4 or loudness is None
            or abs(loudness + 23.0) <= 5.0
        )
    else:
        checks["shot_peak_target_minus3_plusminus0_8"] = peak is not None and abs(peak + 3.0) <= 0.8
        checks["shot_rms_minus18_plusminus4"] = rms is not None and abs(rms + 18.0) <= 4.0
    return checks


def _failed_checks(checks: Dict[str, bool]) -> List[str]:
    return [name for name, passed in checks.items() if not passed]


def _prepare_base(ffmpeg: str, source: Path, before: Dict[str, Any], work: Path) -> Tuple[Path, Dict[str, Any]]:
    direct = before["direct_sample_metrics"]
    lead_ms = float(direct.get("leading_silence_ms_at_minus55db") or 0.0)
    duration = float(before["ffprobe"]["duration_seconds"])
    trim_start = max(0.0, lead_ms / 1000.0 - 0.010)
    base = work / "recorded_preprocessed_float.wav"
    command = _render_preprocessed(resolve_binary("ffmpeg"), source, base, trim_start, duration)
    return base, {"trim_start_seconds": trim_start, "retained_pre_roll_ms": min(10.0, lead_ms),
                  "fade_in_seconds": FADE_IN_SECONDS, "fade_out_seconds": FADE_OUT_SECONDS,
                  "highpass_hz": 30, "command": command, "sha256": sha256_file(base)}


def _candidate_for_role(ffmpeg: str, base: Path, role: str, output: Path,
                        work: Path, subsonic: bool = False) -> Tuple[Optional[Path], Dict[str, Any], Dict[str, Any], List[Dict[str, Any]]]:
    """Return a passing derived candidate plus full processing evidence."""
    role_name = role.lower()
    base_analysis = analyze_audio(base, ffmpeg)
    base_peak = float(base_analysis["direct_sample_metrics"].get("sample_peak_dbfs") or -120.0)
    attempts: List[Dict[str, Any]] = []
    chosen: Optional[Path] = None
    selected_analysis: Dict[str, Any] = {}
    selected_checks: Dict[str, Any] = {}
    selected_edge: Optional[float] = None
    limiter_info: Optional[Dict[str, Any]] = None

    loop_samples = None
    crossfade_evidence: Dict[str, Any] = {"attempted": False}
    if role_name in ("loop", "idle_loop", "movement_loop"):
        loop_samples = decode_mono_f32(base, ffmpeg)
        edge = base_analysis["direct_sample_metrics"].get("loop_inner_edge_rms", {})
        edge_delta = edge.get("delta_db")
        if edge_delta is None or edge_delta > 3.0:
            mixed, overlap, overlap_attempts = find_recorded_loop_crossfade(loop_samples, SAMPLE_RATE)
            crossfade_evidence = {
                "attempted": True,
                "method": "bounded equal-power mix of recorded head and tail samples",
                "source_base_sha256": sha256_file(base),
                "overlap_frames": overlap,
                "overlap_ms": overlap * 1000.0 / SAMPLE_RATE if overlap else None,
                "attempts": overlap_attempts,
                "passed": mixed is not None,
            }
            if mixed is None:
                return None, {}, {}, [{"status": "unresolved", "blockers": ["recorded_loop_crossfade_could_not_meet_3db_gate"],
                                       "crossfade": crossfade_evidence}]
            crossfaded_path = work / "recorded_equal_power_loop.wav"
            crossfade_command = _write_recorded_float(ffmpeg, mixed, crossfaded_path)
            faded_path = work / "recorded_equal_power_loop_faded.wav"
            # The outer fades protect the wrap; all samples come from the
            # crossfaded real recording.
            fade_command = _run_ffmpeg(ffmpeg, crossfaded_path, faded_path,
                                       "afade=t=in:st=0:d={:.6f},afade=t=out:st={:.6f}:d={:.6f}".format(
                                           FADE_IN_SECONDS,
                                           max(0.0, float(analyze_audio(crossfaded_path, ffmpeg)["ffprobe"]["duration_seconds"]) - FADE_OUT_SECONDS),
                                           FADE_OUT_SECONDS), "pcm_f32le")
            base = faded_path
            base_analysis = analyze_audio(base, ffmpeg)
            base_peak = float(base_analysis["direct_sample_metrics"].get("sample_peak_dbfs") or -120.0)
            crossfade_evidence["recorded_mix_sha256"] = sha256_file(crossfaded_path)
            crossfade_evidence["crossfade_command"] = crossfade_command
            crossfade_evidence["endpoint_fade_command"] = fade_command
            crossfade_evidence["post_fade_edge_metrics"] = base_analysis["direct_sample_metrics"].get("loop_inner_edge_rms")

    is_loop = role_name in ("loop", "idle_loop", "movement_loop")
    is_step = role_name in ("step", "steps", "footstep")
    for requested_reduction in LIMITER_STEPS_DB:
        trial = work / ("limiter_{:.1f}db.wav".format(requested_reduction))
        limiter_info = _limiter_stage(ffmpeg, base, trial, requested_reduction, base_peak)
        limiter_gain = limiter_info["gain_reduction"].get("max_sample_gain_reduction_db")
        if limiter_gain is None or limiter_gain > MAX_LIMITER_REDUCTION_DB + 0.0001:
            attempts.append({"requested_peak_push_db": requested_reduction,
                             "measured_max_gain_reduction_db": limiter_gain,
                             "status": "outside_bounded_limiter_policy"})
            continue
        if is_loop:
            loudness_target, tp_target = -20.0, -1.0
        elif is_step:
            loudness_target, tp_target = -23.0, -6.0
        else:
            loudness_target, tp_target = -18.0, -3.0
        normalized = work / ("normalized_{:.1f}db.wav".format(requested_reduction))
        norm_filter = "loudnorm=I={:.1f}:TP={:.1f}:LRA=11:linear=false".format(loudness_target, tp_target)
        norm_command = _run_ffmpeg(ffmpeg, trial, normalized, norm_filter, "pcm_s16le")
        guard = {"applied": False}
        finalized = normalized
        if not is_loop:
            guarded = work / ("peak_guard_{:.1f}db.wav".format(requested_reduction))
            target_peak = -6.0 if is_step else -3.0
            guard = _peak_guard(ffmpeg, normalized, guarded, target_peak)
            finalized = guarded
        analysis = analyze_audio(finalized, ffmpeg)
        edge_delta = None
        if is_loop:
            edge_delta = analysis["direct_sample_metrics"].get("loop_inner_edge_rms", {}).get("delta_db")
        checks = _role_checks(analysis, role, subsonic, edge_delta)
        check_failures = _failed_checks(checks)
        attempt = {
            "requested_peak_push_db": requested_reduction,
            "max_limiter_gain_reduction_db": limiter_gain,
            "gain_reduction_measurement": limiter_info["gain_reduction"],
            "limiter_stage_sha256": limiter_info["limiter_stage_sha256"],
            "normalization_target": {"integrated_lufs": loudness_target, "true_peak_dbtp": tp_target},
            "normalization_command": norm_command,
            "peak_guard": guard,
            "after_sha256": sha256_file(finalized),
            "after_metrics": analysis,
            "checks": checks,
            "blockers": check_failures,
            "status": "passes_all_gates" if not check_failures else "does_not_pass_all_gates",
        }
        attempts.append(attempt)
        selected_analysis, selected_checks = analysis, checks
        selected_edge = edge_delta
        if not check_failures:
            chosen = finalized
            break

    crossfade_evidence["final_edge_delta_db"] = selected_edge
    selected_processing = {
        "pipeline": "recorded source highpass/trim/fades; bounded real-sample alimiter; EBU loudnorm; measured final gates",
        "limiter": limiter_info["gain_reduction"] if limiter_info else None,
        "crossfade": crossfade_evidence,
        "limit_ceiling_dbfs": 0.0,
        "maximum_allowed_gain_reduction_db": MAX_LIMITER_REDUCTION_DB,
    }
    return chosen, selected_analysis, selected_processing, attempts


def _simple_candidate(ffmpeg: str, base: Path, role: str, output: Path, work: Path,
                      subsonic: bool) -> Tuple[Optional[Path], Dict[str, Any], Dict[str, Any], Dict[str, bool]]:
    lowered = role.lower()
    base_analysis = analyze_audio(base, ffmpeg)
    peak = base_analysis["direct_sample_metrics"].get("sample_peak_dbfs")
    if peak is None:
        return None, {}, {"method": "peak normalization", "error": "sample peak unavailable"}, {}
    target = -6.0 if lowered in ("step", "steps", "footstep") else -3.0
    output_filter = _gain_filter(target - peak)
    command = _run_ffmpeg(ffmpeg, base, output, output_filter, "pcm_s16le")
    analysis = analyze_audio(output, ffmpeg)
    checks = _role_checks(analysis, role, subsonic)
    return output, analysis, {"method": "source peak gain plus PCM conversion", "target_peak_dbfs": target,
                              "gain_db": target - peak, "command": command}, checks


def _process_entry(index: int, entry: Dict[str, Any], repo_root: Path, source_root: Path,
                   inventory_records: Dict[str, Dict[str, Any]], output_root: Path,
                   ffmpeg: str) -> Dict[str, Any]:
    source_value = str(entry.get("source", ""))
    base_result: Dict[str, Any] = {"index": index, "source": source_value,
                                   "unit_id": entry.get("unit_id"), "soundeffect": entry.get("soundeffect"),
                                   "role": entry.get("role"), "license_statement":
                                   "Existing attribution reference is preserved; derivative license has not been re-evaluated."}
    try:
        source = (source_root / source_value).resolve()
        if not _is_under(source, source_root):
            raise ValueError("source path escapes the explicit source root")
        if not source.is_file():
            raise ValueError("source file does not exist")
        normalized_source = source_value.replace("\\", "/").lower()
        if any(token in normalized_source for token in ("super_event", "super-event", "superevent", "super_events/")):
            raise ValueError("super-event audio is outside unit-sound mastering scope")
        actual_sha = sha256_file(source)
        expected_sha = str(entry.get("sha256", "")).lower()
        if not expected_sha or actual_sha.lower() != expected_sha:
            raise ValueError("source SHA-256 does not match the allowlist")
        before = analyze_audio(source, ffmpeg)
        base_result["before"] = before
        base_result["lineage"] = source_lineage(repo_root, source, entry, inventory_records.get(source_value))
        base_result["installed_source_sha256"] = actual_sha
        base_result["installed_source_sha256_basis"] = "current runtime input bytes before processing"
        blockers = _source_gate(before, str(entry.get("role", "shot")), bool(entry.get("subsonic", False)))
        attribution = base_result["lineage"].get("attribution", {})
        if attribution.get("status") != "row_matched":
            blockers.append("existing_attribution_source_row_unresolved")
        if blockers:
            base_result.update({"status": "unresolved", "blockers": blockers})
            return base_result

        output = Path(entry.get("output") or _default_output_path(output_root, str(entry.get("unit_id", "unknown")),
                                                                  str(entry.get("soundeffect", "cue")), source_value))
        if not output.is_absolute():
            output = output_root / output
        output = output.resolve()
        if not _is_under(output, output_root):
            raise ValueError("destination path escapes output root")
        if _is_under(output, repo_root / "sound"):
            raise ValueError("output must remain outside active runtime sound tree")
        if output.exists():
            raise ValueError("destination_already_exists")

        work_parent = output_root / ".audio_work"
        work_parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix="entry_{:03d}_".format(index), dir=str(work_parent)) as temp_name:
            work = Path(temp_name)
            duration = float(before["ffprobe"]["duration_seconds"])
            lead_ms = float(before["direct_sample_metrics"].get("leading_silence_ms_at_minus55db") or 0.0)
            trim_start = max(0.0, lead_ms / 1000.0 - 0.010)
            preprocessed = work / "preprocessed.wav"
            prep_commands = _render_preprocessed(ffmpeg, source, preprocessed, trim_start, duration)
            processing: Dict[str, Any] = {
                "highpass_hz": 30,
                "initial_measured_lead_ms": lead_ms,
                "trim_start_seconds": trim_start,
                "retained_pre_roll_ms": min(10.0, lead_ms),
                "fade_in_ms": FADE_IN_SECONDS * 1000.0,
                "fade_out_ms": FADE_OUT_SECONDS * 1000.0,
                "preprocessed_sha256": sha256_file(preprocessed),
                "preprocessing_command": prep_commands,
            }
            loop_role = str(entry.get("role", "")).lower() in ("loop", "idle_loop", "movement_loop")
            if loop_role:
                staged, after, limiter_processing, attempts = _candidate_for_role(
                    ffmpeg, preprocessed, str(entry.get("role", "loop")), output, work,
                    bool(entry.get("subsonic", False)))
                processing["limiter_and_loop_correction"] = limiter_processing
                base_result["attempts"] = attempts
                if staged is None:
                    latest = attempts[-1] if attempts else {}
                    base_result.update({"status": "unresolved", "blockers": latest.get("blockers", ["loop_mastering_failed"]),
                                        "after_last_candidate": latest.get("after_metrics"),
                                        "processing": processing})
                    return base_result
                shutil.copy2(staged, output)
                checks = _role_checks(after, str(entry.get("role", "loop")), bool(entry.get("subsonic", False)),
                                      after["direct_sample_metrics"].get("loop_inner_edge_rms", {}).get("delta_db"))
            else:
                pre_analysis = analyze_audio(preprocessed, ffmpeg)
                lead = pre_analysis["direct_sample_metrics"].get("leading_silence_ms_at_minus55db")
                if lead is not None and lead > 20.0:
                    post_trim = work / "postmaster_trimmed.wav"
                    trim_passes: List[Dict[str, Any]] = []
                    trim_seconds, post_commands = _postmaster_trim(ffmpeg, preprocessed, post_trim, lead, trim_passes)
                    processing["postmaster_lead_correction"] = {
                        "measured_lead_ms": lead, "trim_start_seconds": trim_seconds,
                        "retained_pre_roll_ms": 10.0, "fade_in_ms": FADE_IN_SECONDS * 1000.0,
                        "input_sha256": sha256_file(preprocessed), "passes": trim_passes,
                        "command": post_commands, "output_sha256": sha256_file(post_trim),
                    }
                    preprocessed = post_trim
                candidate_path = work / "candidate.wav"
                candidate, after, simple_processing, checks = _simple_candidate(
                    ffmpeg, preprocessed, str(entry.get("role", "shot")), candidate_path, work,
                    bool(entry.get("subsonic", False)))
                processing["initial_peak_normalization"] = simple_processing
                failures = _failed_checks(checks)
                if failures and any(name in failures for name in (
                        "shot_rms_minus18_plusminus4", "loop_loudness_minus20_plusminus1")):
                    candidate, after, limiter_processing, attempts = _candidate_for_role(
                        ffmpeg, preprocessed, str(entry.get("role", "shot")), output, work,
                        bool(entry.get("subsonic", False)))
                    processing["limiter_and_loudness_recovery"] = limiter_processing
                    base_result["attempts"] = attempts
                    if candidate is not None:
                        shutil.copy2(candidate, output)
                        checks = _role_checks(after, str(entry.get("role", "shot")), bool(entry.get("subsonic", False)))
                    else:
                        latest = attempts[-1] if attempts else {}
                        base_result.update({"status": "needs_review", "blockers": latest.get("blockers", failures),
                                            "after_last_candidate": latest.get("after_metrics"),
                                            "processing": processing})
                        return base_result
                else:
                    if candidate is None:
                        base_result.update({"status": "unresolved", "blockers": ["no_candidate_created"]})
                        return base_result
                    shutil.copy2(candidate, output)
            after = analyze_audio(output, ffmpeg)
            checks = _role_checks(after, str(entry.get("role", "shot")), bool(entry.get("subsonic", False)),
                                  after["direct_sample_metrics"].get("loop_inner_edge_rms", {}).get("delta_db") if loop_role else None)
            failures = _failed_checks(checks)
            if failures:
                try:
                    output.unlink()
                except OSError:
                    pass
                base_result.update({"status": "needs_review", "blockers": failures, "after": after,
                                    "checks": checks, "processing": processing})
                return base_result
            base_result.update({"status": "staged", "destination_path": str(output), "output_sha256": sha256_file(output),
                                "after": after, "checks": checks, "blockers": [], "processing": processing})
            return base_result
    except (AudioToolError, OSError, ValueError, KeyError) as exc:
        base_result.update({"status": "unresolved", "blockers": [str(exc)]})
        return base_result


def _load_manifest(path: Path) -> Tuple[Dict[str, Any], str]:
    manifest, digest = load_json(path)
    if manifest.get("schema") != 1 or not isinstance(manifest.get("entries"), list):
        raise ValueError("allowlist must have schema=1 and an entries array")
    return manifest, digest


def _batch(args: argparse.Namespace) -> int:
    repo_root = Path.cwd().resolve()
    manifest_path = Path(args.manifest).resolve()
    manifest, manifest_sha = _load_manifest(manifest_path)
    source_root = Path(args.source_root).resolve()
    output_root = Path(args.output_root).resolve()
    report_path = Path(args.report).resolve()
    if _is_under(output_root, repo_root / "sound") or _is_under(report_path, repo_root / "sound"):
        raise ValueError("batch output and report must remain outside the active sound tree")
    ffmpeg = resolve_binary("ffmpeg")
    ffprobe = resolve_binary("ffprobe")
    inventory_records: Dict[str, Dict[str, Any]] = {}
    inventory_sha = None
    inventory_path = manifest.get("inventory_path")
    if inventory_path:
        inv_path = (repo_root / inventory_path).resolve()
        if inv_path.is_file():
            inventory, inventory_sha = load_json(inv_path)
            inventory_records, _ = flatten_runtime_inventory(inventory)
    output_root.mkdir(parents=True, exist_ok=True)
    results = []
    for index, entry in enumerate(manifest["entries"]):
        if not isinstance(entry, dict):
            results.append({"index": index, "status": "unresolved", "blockers": ["entry is not an object"]})
            continue
        result = _process_entry(index, entry, repo_root, source_root, inventory_records, output_root, ffmpeg)
        results.append(result)
    report = {
        "schema": 1,
        "tool": "Chaos Redux auditable unit audio master",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "status": "complete_with_review" if any(row.get("status") != "staged" for row in results) else "complete",
        "manifest_path": str(manifest_path),
        "manifest_sha256": manifest_sha,
        "source_root": str(source_root),
        "output_root": str(output_root),
        "report_path": str(report_path),
        "inventory_path": str((repo_root / inventory_path).resolve()) if inventory_path else None,
        "inventory_sha256": inventory_sha,
        "ffmpeg_version": binary_version(ffmpeg),
        "ffprobe_version": binary_version(ffprobe),
        "entry_count": len(results),
        "staged_count": sum(1 for row in results if row.get("status") == "staged"),
        "needs_review_count": sum(1 for row in results if row.get("status") == "needs_review"),
        "unresolved_count": sum(1 for row in results if row.get("status") == "unresolved"),
        "blocked_count": sum(1 for row in results if row.get("status") == "blocked"),
        "lineage_policy": "preserves installed preimage hash and existing attribution row; derivative license has not been reassessed",
        "processing_recipe": {
            "delivery": "PCM signed 16-bit little-endian, 44.1 kHz, mono",
            "highpass_hz": 30,
            "fade_in_ms": 8,
            "fade_out_ms": 50,
            "loop_target": {"integrated_lufs": -20, "tolerance_lu": 1, "true_peak_max_dbtp": -1, "edge_delta_max_db": 3},
            "shot_target": {"sample_peak_dbfs": -3, "peak_tolerance_db": 0.8, "rms_dbfs": -18, "rms_tolerance_db": 4},
            "step_target": {"sample_peak_dbfs": -6, "peak_tolerance_db": 0.8, "integrated_lufs": -23, "tolerance_lu": 5},
            "limiter": {"filter": "alimiter plus EBU loudnorm true-peak normalization", "max_measured_gain_reduction_db": MAX_LIMITER_REDUCTION_DB,
                        "bounded_peak_push_trials_db": list(LIMITER_STEPS_DB)},
        },
        "results": results,
    }
    _json_write(report_path, report)
    print(json.dumps({"report": str(report_path), "staged": report["staged_count"],
                      "needs_review": report["needs_review_count"], "unresolved": report["unresolved_count"]}, indent=2))
    return 0


def _inspect(args: argparse.Namespace) -> int:
    ffmpeg = resolve_binary("ffmpeg")
    supplied = [value for value in (args.input, args.path) if value]
    if not supplied:
        raise ValueError("inspect requires --input <path> or a positional input path")
    if len(supplied) > 1:
        raise ValueError("inspect accepts one input path")
    source = Path(supplied[0]).resolve()
    if not source.is_file():
        raise ValueError("input audio file does not exist: {}".format(source))
    report_path = Path(args.output).resolve()
    repo_root = Path.cwd().resolve()
    if _is_under(report_path, repo_root / "sound"):
        raise ValueError("inspect report must remain outside the active sound tree")
    if report_path.exists() and not args.force:
        raise ValueError("inspect report already exists; pass --force to replace it")
    analysis = analyze_audio(source, ffmpeg)
    role = str(args.role)
    edge = analysis.get("direct_sample_metrics", {}).get("loop_inner_edge_rms", {}).get("delta_db")
    checks = _role_checks(analysis, role, bool(args.subsonic), edge if role.lower() in ("loop", "idle_loop", "movement_loop") else None)
    source_blockers = _source_gate(analysis, role, bool(args.subsonic))
    blockers = source_blockers + _failed_checks(checks)
    try:
        source_relative = source.relative_to(repo_root).as_posix()
    except ValueError:
        source_relative = str(source)
    report = {
        "schema": 1,
        "tool": "Chaos Redux read-only unit audio inspector",
        "status": "passes_role_checks" if not blockers else "needs_review",
        "source_relative_path": source_relative,
        "source_sha256": analysis["sha256"],
        "role": role,
        "subsonic_declared": bool(args.subsonic),
        "force_overwrite_requested": bool(args.force),
        "destination_path": None,
        "output_sha256": None,
        "before": analysis,
        "after": None,
        "checks": checks,
        "source_blockers": source_blockers,
        "blockers": blockers,
        "processing": {"read_only": True, "audio_transformed": False},
    }
    _json_write(report_path, report)
    print(json.dumps({"report": str(report_path), "status": report["status"], "checks": checks,
                      "blockers": blockers, "source_sha256": report["source_sha256"]}, indent=2))
    return 0


def _compatible_result(row: Dict[str, Any]) -> Dict[str, Any]:
    """Add the established batch-result aliases without dropping new evidence."""
    compatible = dict(row)
    compatible["source_relative_path"] = row.get("source_relative_path", row.get("source"))
    compatible["source_sha256"] = row.get("source_sha256", row.get("installed_source_sha256"))
    compatible["destination_path"] = row.get("destination_path")
    compatible["output_sha256"] = row.get("output_sha256")
    compatible["before"] = row.get("before")
    compatible["after"] = row.get("after")
    compatible["checks"] = row.get("checks", {})
    compatible["processing"] = row.get("processing", {})
    return compatible


def _compat_report(args: argparse.Namespace) -> int:
    source_path = Path(args.input_report).resolve()
    source_report, source_sha = load_json(source_path)
    output_path = Path(args.output).resolve()
    if _is_under(output_path, Path.cwd().resolve() / "sound"):
        raise ValueError("compatibility report must remain outside the active sound tree")
    if output_path.exists() and not args.force:
        raise ValueError("compatibility report already exists; pass --force to replace it")
    source_rows = source_report.get("results", [])
    install_rows = [_compatible_result(row) for row in source_rows if row.get("status") == "staged"]
    excluded_rows = [_compatible_result(row) for row in source_rows if row.get("status") != "staged"]
    report = {
        "schema": 1,
        "tool": "Chaos Redux batch-result compatibility view",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "source_report_path": str(source_path),
        "source_report_sha256": source_sha,
        "report_path": str(output_path),
        "result_schema": ["source_relative_path", "source_sha256", "destination_path", "output_sha256",
                          "before", "after", "checks", "processing"],
        "result_count": len(install_rows),
        "excluded_count": len(excluded_rows),
        "results": install_rows,
        "excluded_results": excluded_rows,
    }
    _json_write(output_path, report)
    print(json.dumps({"report": str(output_path), "results": len(install_rows),
                      "excluded": len(excluded_rows), "source_report_sha256": source_sha}, indent=2))
    return 0


def _audit_tree(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    inventory_path = Path(args.inventory).resolve() if args.inventory else None
    inventory_records: Dict[str, Dict[str, Any]] = {}
    cue_rows: List[Dict[str, Any]] = []
    inventory_sha = None
    if inventory_path and inventory_path.is_file():
        inventory, inventory_sha = load_json(inventory_path)
        inventory_records, cue_rows = flatten_runtime_inventory(inventory)
    family_pools: List[Dict[str, Any]] = []
    if args.family_pools:
        family_payload, _ = load_json(Path(args.family_pools))
        family_pools = family_payload.get("family_pools", family_payload.get("pools", []))
    attribution_map: Dict[str, Any] = {}
    if args.attribution_map:
        attr_payload, _ = load_json(Path(args.attribution_map))
        attribution_map = attr_payload.get("entries", attr_payload)
    ffmpeg = resolve_binary("ffmpeg")
    ffprobe = resolve_binary("ffprobe")
    audio_paths = [path for path in root.rglob("*") if path.is_file() and path.suffix.lower() in SUPPORTED_AUDIO]
    hashes: Dict[str, str] = {}
    reports: Dict[str, Any] = {}
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = {executor.submit(analyze_audio, path, ffmpeg): path for path in audio_paths}
        for future in as_completed(futures):
            path = futures[future]
            rel = path.relative_to(root.parent).as_posix()
            try:
                row = future.result()
                reports[rel] = row
                hashes[rel] = row["sha256"]
            except Exception as exc:
                reports[rel] = {"path": str(path), "status": "analysis_error", "error": str(exc)}
                hashes[rel] = sha256_file(path)
    coverage = build_sound_coverage(root, cue_rows, attribution_map, Path.cwd(), inventory_records)
    duplicates = summarize_duplicates(inventory_records, hashes, family_pools)
    report = {
        "schema": 1,
        "tool": "Chaos Redux read-only unit sound tree audit",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "root": str(root),
        "inventory_path": str(inventory_path) if inventory_path else None,
        "inventory_sha256": inventory_sha,
        "ffmpeg_version": binary_version(ffmpeg),
        "ffprobe_version": binary_version(ffprobe),
        "audio_file_count": len(audio_paths),
        "family_pool_and_duplicate_audit": duplicates,
        "single_sample_and_coverage_audit": coverage,
        "files": reports,
    }
    _json_write(Path(args.output).resolve(), report)
    print(json.dumps({"output": str(Path(args.output).resolve()), "audio_files": len(audio_paths),
                      "single_sample_cues": len(coverage["single_sample_cues"]),
                      "undeclared_cross_unit_duplicates": len(duplicates["undeclared_cross_unit_duplicates"])}, indent=2))
    return 0


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Audit and master existing Chaos Redux unit recordings")
    subparsers = parser.add_subparsers(dest="command", required=True)
    inspect_parser = subparsers.add_parser("inspect", help="read-only audio analysis")
    inspect_parser.add_argument("path", nargs="?", help="input audio path (positional compatibility form)")
    inspect_parser.add_argument("--input", help="input audio path")
    inspect_parser.add_argument("--role", required=True, choices=("shot", "loop", "step", "steps", "footstep"))
    inspect_parser.add_argument("--output", required=True, help="JSON inspection report destination")
    inspect_parser.add_argument("--subsonic", action="store_true", help="explicitly permit centroid at/below 200 Hz")
    inspect_parser.add_argument("--force", action="store_true", help="allow replacing an existing JSON report")
    inspect_parser.set_defaults(func=_inspect)
    compat_parser = subparsers.add_parser("compat-report", help="write established batch aliases for a new batch report")
    compat_parser.add_argument("--input-report", required=True)
    compat_parser.add_argument("--output", required=True)
    compat_parser.add_argument("--force", action="store_true")
    compat_parser.set_defaults(func=_compat_report)
    batch_parser = subparsers.add_parser("batch", help="stage only explicit allowlisted derivatives")
    batch_parser.add_argument("--manifest", required=True)
    batch_parser.add_argument("--source-root", default=".")
    batch_parser.add_argument("--output-root", required=True)
    batch_parser.add_argument("--report", required=True)
    batch_parser.set_defaults(func=_batch)
    tree_parser = subparsers.add_parser("audit-tree", help="read-only full sound-tree audit")
    tree_parser.add_argument("--root", required=True)
    tree_parser.add_argument("--inventory")
    tree_parser.add_argument("--family-pools")
    tree_parser.add_argument("--attribution-map")
    tree_parser.add_argument("--output", required=True)
    tree_parser.add_argument("--workers", type=int, default=4)
    tree_parser.set_defaults(func=_audit_tree)
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except (AudioToolError, OSError, ValueError, json.JSONDecodeError) as exc:
        print("audio master error: {}".format(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
