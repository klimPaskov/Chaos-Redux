"""FFmpeg-backed WAV probing and signal measurements.

The analyzer decodes existing recordings to float samples for direct flat-top
measurement and also records FFmpeg astats, EBU R128, and spectral centroid
evidence. It never writes or changes the analyzed input.
"""

import array
from collections import deque
import hashlib
import json
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple


class AudioToolError(RuntimeError):
    """Raised when an external audio tool cannot provide reliable evidence."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def resolve_binary(name: str) -> str:
    binary = shutil.which(name)
    if not binary:
        raise AudioToolError("required executable is unavailable on PATH: {}".format(name))
    return binary


def binary_version(binary: str, argument: str = "-version") -> str:
    result = subprocess.run(
        [binary, argument],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
        universal_newlines=True,
    )
    if result.returncode != 0 or not result.stdout.strip():
        raise AudioToolError("could not read version from {}".format(binary))
    return result.stdout.splitlines()[0].strip()


def _run_json(command: Sequence[str]) -> Dict[str, Any]:
    result = subprocess.run(
        list(command),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        universal_newlines=True,
    )
    if result.returncode != 0:
        raise AudioToolError("command failed ({}): {}".format(result.returncode, result.stderr.strip()))
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise AudioToolError("tool returned invalid JSON: {}".format(exc))


def probe_audio(path: Path, ffprobe: Optional[str] = None) -> Dict[str, Any]:
    ffprobe = ffprobe or resolve_binary("ffprobe")
    payload = _run_json(
        [
            ffprobe,
            "-v",
            "error",
            "-show_streams",
            "-show_format",
            "-of",
            "json",
            str(path),
        ]
    )
    streams = [stream for stream in payload.get("streams", []) if stream.get("codec_type") == "audio"]
    if not streams:
        raise AudioToolError("ffprobe found no audio stream: {}".format(path))
    stream = streams[0]
    audio_format = payload.get("format", {})
    duration = _number(stream.get("duration"))
    if duration is None:
        duration = _number(audio_format.get("duration"))
    result = {
        "codec_name": stream.get("codec_name"),
        "codec_long_name": stream.get("codec_long_name"),
        "sample_fmt": stream.get("sample_fmt"),
        "sample_rate": _integer(stream.get("sample_rate")),
        "channels": _integer(stream.get("channels")),
        "channel_layout": stream.get("channel_layout"),
        "bits_per_sample": _integer(stream.get("bits_per_sample")),
        "bits_per_raw_sample": _integer(stream.get("bits_per_raw_sample")),
        "duration_seconds": duration,
        "file_format": audio_format.get("format_name"),
        "file_bytes": _integer(audio_format.get("size")),
    }
    if not result["sample_rate"] or not result["channels"] or duration is None:
        raise AudioToolError("ffprobe omitted required stream fields: {}".format(path))
    return result


def _number(value: Any) -> Optional[float]:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number if math.isfinite(number) else None


def _integer(value: Any) -> Optional[int]:
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


class _SampleAccumulator:
    def __init__(self, sample_rate: int, channels: int) -> None:
        self.sample_rate = sample_rate
        self.channels = max(1, channels)
        self.frame_count = 0
        self.sample_count = 0
        self.sum_squares = 0.0
        self.sum_values = 0.0
        self.peak = 0.0
        self.nonfinite_count = 0
        self.over_full_scale_count = 0
        self.rail_count = 0
        self.rail_run_max = 0
        self.rail_runs_by_channel = [0 for _ in range(self.channels)]
        self.last_rail_values_by_channel: List[Optional[float]] = [None for _ in range(self.channels)]
        self.first_active_frame: Optional[int] = None
        self._active_bin_sum = 0.0
        self._active_bin_frames = 0
        self._active_bin_start = 0
        self.edge_capacity_frames = max(1, int(sample_rate * 0.22))
        self.head_values: List[float] = []
        self.tail_values = deque(maxlen=self.edge_capacity_frames * self.channels)
        self.loop_inner_edges: List[float] = []

    def consume(self, values: array.array) -> None:
        if sys.byteorder != "little":
            values.byteswap()
        channel_count = self.channels
        for value in values:
            if not math.isfinite(value):
                self.nonfinite_count += 1
                continue
            absolute = abs(value)
            self.sample_count += 1
            channel = (self.sample_count - 1) % channel_count
            self.sum_values += value
            self.sum_squares += value * value
            if absolute > self.peak:
                self.peak = absolute
            if absolute > 1.000001:
                self.over_full_scale_count += 1
            if absolute >= 0.999:
                self.rail_count += 1
                previous = self.last_rail_values_by_channel[channel]
                if previous is not None and abs(value - previous) <= 1e-7:
                    self.rail_runs_by_channel[channel] += 1
                else:
                    self.rail_runs_by_channel[channel] = 1
                self.last_rail_values_by_channel[channel] = value
                if self.rail_runs_by_channel[channel] > self.rail_run_max:
                    self.rail_run_max = self.rail_runs_by_channel[channel]
            else:
                self.rail_runs_by_channel[channel] = 0
                self.last_rail_values_by_channel[channel] = None

            if len(self.head_values) < self.edge_capacity_frames * channel_count:
                self.head_values.append(value)
            self.tail_values.append(value)

            # Use 5 ms windows and all channels to identify the first audible
            # onset. This is evidence for trim placement, not a silence editor.
            self._active_bin_sum += value * value
            self._active_bin_frames += 1
            if self._active_bin_frames >= max(1, int(self.sample_rate * channel_count * 0.005)):
                if self.first_active_frame is None:
                    rms = math.sqrt(self._active_bin_sum / self._active_bin_frames)
                    if rms > 10.0 ** (-55.0 / 20.0):
                        self.first_active_frame = self._active_bin_start
                self._active_bin_start += self._active_bin_frames // channel_count
                self._active_bin_sum = 0.0
                self._active_bin_frames = 0
        self.frame_count = self.sample_count // channel_count

    def result(self) -> Dict[str, Any]:
        rms = math.sqrt(self.sum_squares / self.sample_count) if self.sample_count else 0.0
        mean = self.sum_values / self.sample_count if self.sample_count else 0.0
        peak_db = _dbfs(self.peak)
        rms_db = _dbfs(rms)
        first_active_ms = None
        if self.first_active_frame is not None:
            first_active_ms = self.first_active_frame * 1000.0 / self.sample_rate
        if self.first_active_frame is None and self.frame_count:
            first_active_ms = self.frame_count * 1000.0 / self.sample_rate
        tail_values = list(self.tail_values)
        edge_rms = _edge_rms(self.head_values, tail_values, self.channels, self.sample_rate)
        loop_edge_rms = _loop_inner_edge_rms(
            self.head_values, tail_values, self.channels, self.sample_rate
        )
        rail_fraction = self.rail_count / float(self.sample_count or 1)
        probable_flat_top = self.rail_run_max >= 3 and self.rail_count >= 6
        return {
            "decoded_frames": self.frame_count,
            "decoded_samples": self.sample_count,
            "sample_peak_linear": self.peak,
            "sample_peak_dbfs": peak_db,
            "sample_rms_linear": rms,
            "sample_rms_dbfs": rms_db,
            "mean_dc_offset_linear": mean,
            "leading_silence_ms_at_minus55db": first_active_ms,
            "nonfinite_sample_count": self.nonfinite_count,
            "over_full_scale_sample_count": self.over_full_scale_count,
            "near_rail_sample_count": self.rail_count,
            "near_rail_sample_fraction": rail_fraction,
            "longest_exact_near_rail_run_samples": self.rail_run_max,
            "probable_flat_top": probable_flat_top,
            "edge_rms": edge_rms,
            "loop_inner_edge_rms": loop_edge_rms,
        }


def _dbfs(linear: float) -> Optional[float]:
    if linear <= 0.0:
        return None
    return 20.0 * math.log10(linear)


def _rms(values: Sequence[float]) -> Optional[float]:
    if not values:
        return None
    return math.sqrt(sum(value * value for value in values) / len(values))


def _edge_rms(head: Sequence[float], tail: Sequence[float], channels: int, rate: int) -> Dict[str, Any]:
    window = max(1, int(rate * 0.1) * channels)
    head_value = _dbfs(_rms(head[:window]) or 0.0)
    tail_value = _dbfs(_rms(tail[-window:]) or 0.0)
    return {"window_ms": 100, "head_rms_dbfs": head_value, "tail_rms_dbfs": tail_value}


def _loop_inner_edge_rms(head: Sequence[float], tail: Sequence[float], channels: int, rate: int) -> Dict[str, Any]:
    # Ignore the deliberately applied endpoint fades and compare 100 ms slices
    # immediately after/before those fades. Short clips cannot be certified as
    # seamless because they provide no stable interior comparison window.
    fade = max(1, int(rate * 0.06) * channels)
    window = max(1, int(rate * 0.1) * channels)
    if len(head) < fade + window or len(tail) < fade + window:
        return {"window_ms": 100, "fade_excluded_ms": 60, "head_rms_dbfs": None, "tail_rms_dbfs": None}
    head_value = _dbfs(_rms(head[fade:fade + window]) or 0.0)
    tail_value = _dbfs(_rms(tail[-(fade + window):-fade]) or 0.0)
    delta = None
    if head_value is not None and tail_value is not None:
        delta = abs(head_value - tail_value)
    return {
        "window_ms": 100,
        "fade_excluded_ms": 60,
        "head_rms_dbfs": head_value,
        "tail_rms_dbfs": tail_value,
        "delta_db": delta,
    }


def decode_mono_f32(path: Path, ffmpeg: Optional[str] = None, sample_rate: int = 44100) -> array.array:
    """Decode an existing recording to mono float samples for recorded-sample editing."""
    ffmpeg = ffmpeg or resolve_binary("ffmpeg")
    command = [
        ffmpeg,
        "-hide_banner",
        "-nostats",
        "-v",
        "error",
        "-i",
        str(path),
        "-map",
        "0:a:0",
        "-vn",
        "-ar",
        str(sample_rate),
        "-ac",
        "1",
        "-c:a",
        "pcm_f32le",
        "-f",
        "f32le",
        "pipe:1",
    ]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    if result.returncode != 0:
        raise AudioToolError("ffmpeg loop-source decode failed: {}".format(result.stderr.decode("utf-8", errors="replace")[-2000:]))
    if len(result.stdout) % 4:
        raise AudioToolError("decoded recording ended with a partial float sample")
    samples = array.array("f")
    samples.frombytes(result.stdout)
    if sys.byteorder != "little":
        samples.byteswap()
    return samples


def equal_power_recorded_loop(samples: Sequence[float], overlap_frames: int) -> array.array:
    """Make a cyclic bridge only by mixing the recording's tail and head samples."""
    if overlap_frames < 2 or len(samples) <= overlap_frames * 2:
        raise ValueError("loop crossfade overlap is invalid for the source length")
    middle = array.array("f", samples[overlap_frames:-overlap_frames])
    blend = array.array("f")
    denominator = float(overlap_frames - 1)
    for index in range(overlap_frames):
        angle = (math.pi * 0.5) * index / denominator
        tail_sample = float(samples[len(samples) - overlap_frames + index])
        head_sample = float(samples[index])
        blend.append(tail_sample * math.cos(angle) + head_sample * math.sin(angle))
    middle.extend(blend)
    return middle


def loop_inner_edge_metrics(samples: Sequence[float], sample_rate: int = 44100) -> Dict[str, Any]:
    edge_capacity = max(1, int(sample_rate * 0.22))
    if len(samples) < edge_capacity * 2:
        return {"window_ms": 100, "fade_excluded_ms": 60, "head_rms_dbfs": None, "tail_rms_dbfs": None, "delta_db": None}
    return _loop_inner_edge_rms(samples[:edge_capacity], samples[-edge_capacity:], 1, sample_rate)


def measure_max_gain_reduction_db(
    dry_samples: Sequence[float],
    limited_samples: Sequence[float],
    active_floor: float = 0.03,
) -> Dict[str, Any]:
    """Estimate the maximum aligned sample gain reduction of a limiter pass."""
    if len(dry_samples) != len(limited_samples):
        raise AudioToolError("limiter input/output sample counts differ; gain reduction is unverified")
    maximum_db = 0.0
    measured_samples = 0
    for dry, wet in zip(dry_samples, limited_samples):
        dry_abs = abs(float(dry))
        wet_abs = abs(float(wet))
        if dry_abs < active_floor or wet_abs <= 0.0 or not math.isfinite(dry_abs + wet_abs):
            continue
        measured_samples += 1
        if wet_abs < dry_abs:
            reduction_db = 20.0 * math.log10(dry_abs / wet_abs)
            if reduction_db > maximum_db:
                maximum_db = reduction_db
    return {
        "max_sample_gain_reduction_db": maximum_db,
        "active_sample_floor_linear": active_floor,
        "compared_sample_count": measured_samples,
        "alignment": "same-rate mono samples; alimiter latency compensation enabled",
        "method": "maximum aligned abs(dry)/abs(wet) ratio above active floor",
    }


def find_recorded_loop_crossfade(
    samples: Sequence[float],
    sample_rate: int = 44100,
    max_edge_delta_db: float = 3.0,
) -> Tuple[Optional[array.array], Optional[int], List[Dict[str, Any]]]:
    """Try short, bounded equal-power bridges and return the shortest passing one."""
    length = len(samples)
    max_overlap = min(int(sample_rate * 1.0), int(length * 0.45), length - int(sample_rate * 0.32))
    overlap_candidates = [
        int(sample_rate * milliseconds / 1000.0)
        for milliseconds in (80, 100, 125, 150, 200, 250, 300, 400, 500, 650, 750, 850, 900, 950, 1000)
    ]
    attempts: List[Dict[str, Any]] = []
    seen = set()
    for overlap in overlap_candidates:
        overlap = min(overlap, max_overlap)
        if overlap in seen or overlap < int(sample_rate * 0.06):
            continue
        seen.add(overlap)
        candidate = equal_power_recorded_loop(samples, overlap)
        metrics = loop_inner_edge_metrics(candidate, sample_rate)
        delta = metrics.get("delta_db")
        attempts.append(
            {
                "overlap_frames": overlap,
                "overlap_ms": overlap * 1000.0 / sample_rate,
                "head_rms_dbfs": metrics.get("head_rms_dbfs"),
                "tail_rms_dbfs": metrics.get("tail_rms_dbfs"),
                "delta_db": delta,
                "passes_edge_gate": delta is not None and delta <= max_edge_delta_db,
            }
        )
        if delta is not None and delta <= max_edge_delta_db:
            return candidate, overlap, attempts
    return None, None, attempts


def _parse_ebur128(log_text: str) -> Dict[str, Optional[float]]:
    integrated = None
    true_peak = None
    lra = None
    integrated_sections = re.findall(
        r"Integrated loudness:\s*(.*?)(?=\n\s*(?:Loudness range:|True peak:)|\Z)",
        log_text,
        flags=re.DOTALL,
    )
    if integrated_sections:
        match = re.search(r"\bI:\s*(-?[0-9]+(?:\.[0-9]+)?)\s*LUFS", integrated_sections[-1])
        if match:
            integrated = float(match.group(1))
    lra_match = re.search(r"\bLRA:\s*([0-9]+(?:\.[0-9]+)?)\s*LU", log_text)
    if lra_match:
        lra = float(lra_match.group(1))
    peak_sections = re.findall(r"True peak:\s*(.*?)(?=\n\s*\n|\Z)", log_text, flags=re.DOTALL)
    if peak_sections:
        match = re.search(r"\bPeak:\s*(-?[0-9]+(?:\.[0-9]+)?)\s*dB", peak_sections[-1])
        if match:
            true_peak = float(match.group(1))
    return {"integrated_lufs": integrated, "true_peak_dbtp": true_peak, "loudness_range_lu": lra}


def _parse_astats_flat_factor(log_text: str) -> Optional[float]:
    # FFmpeg astats prints the overall final report as well as per-channel
    # reports. The direct PCM scan below remains authoritative for flat tops.
    matches = re.findall(r"Flat factor:\s*([0-9]+(?:\.[0-9]+)?)", log_text)
    values = [float(value) for value in matches if math.isfinite(float(value))]
    return max(values) if values else None


def _parse_centroids(log_text: str, active_dbfs: float = -55.0) -> List[float]:
    frames = re.split(r"(?=frame:\s*\d+)", log_text)
    values: List[float] = []
    rms_pattern = re.compile(r"lavfi\.astats\.(\d+)\.RMS_level=([-+0-9.eE]+)")
    centroid_pattern = re.compile(r"lavfi\.aspectralstats\.(\d+)\.centroid=([-+0-9.eE]+)")
    for frame in frames:
        rms_by_channel: Dict[str, float] = {}
        for channel, value in rms_pattern.findall(frame):
            try:
                rms_by_channel[channel] = float(value)
            except ValueError:
                continue
        for channel, value in centroid_pattern.findall(frame):
            try:
                centroid = float(value)
            except ValueError:
                continue
            if not math.isfinite(centroid) or centroid < 0.0:
                continue
            if rms_by_channel.get(channel, -120.0) > active_dbfs:
                values.append(centroid)
    return values


def _parse_astats_value(log_text: str, label: str) -> Optional[float]:
    matches = re.findall(r"{}:\s*(-?[0-9]+(?:\.[0-9]+)?)".format(re.escape(label)), log_text)
    return float(matches[-1]) if matches else None


def _analyze_long_form(
    path: Path,
    probe: Dict[str, Any],
    ffmpeg: str,
    analysis_filter: str,
) -> Dict[str, Any]:
    """Audit long-form tracks without treating them as unit-SFX candidates."""
    command = [
        ffmpeg,
        "-hide_banner",
        "-nostats",
        "-loglevel",
        "info",
        "-i",
        str(path),
        "-map",
        "0:a:0",
        "-vn",
        "-af",
        analysis_filter,
        "-ar",
        "44100",
        "-f",
        "null",
        "NUL",
    ]
    with tempfile.TemporaryFile(mode="w+b") as error_stream:
        process = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=error_stream, check=False)
        error_stream.seek(0)
        log_text = error_stream.read().decode("utf-8", errors="replace")
    if process.returncode != 0:
        raise AudioToolError("ffmpeg long-form audit failed: {}".format(log_text[-2000:]))
    peak_db = _parse_astats_value(log_text, "Peak level dB")
    rms_db = _parse_astats_value(log_text, "RMS level dB")
    dc_offset = _parse_astats_value(log_text, "DC offset")
    flat_factor = _parse_astats_flat_factor(log_text)
    direct = {
        "decoded_frames": None,
        "decoded_samples": None,
        "sample_peak_linear": 10.0 ** (peak_db / 20.0) if peak_db is not None else None,
        "sample_peak_dbfs": peak_db,
        "sample_rms_linear": 10.0 ** (rms_db / 20.0) if rms_db is not None else None,
        "sample_rms_dbfs": rms_db,
        "mean_dc_offset_linear": dc_offset,
        "leading_silence_ms_at_minus55db": None,
        "nonfinite_sample_count": None,
        "over_full_scale_sample_count": None,
        "near_rail_sample_count": None,
        "near_rail_sample_fraction": None,
        "longest_exact_near_rail_run_samples": None,
        "probable_flat_top": None,
        "edge_rms": None,
        "loop_inner_edge_rms": None,
        "measurement_source": "whole-stream astats only; direct sample scan exempt for long-form audio",
    }
    ebur = _parse_ebur128(log_text)
    return {
        "path": str(path),
        "sha256": sha256_file(path),
        "ffprobe": probe,
        "direct_sample_metrics": direct,
        "astats": {
            "flat_factor": flat_factor,
            "flat_factor_zero": flat_factor is not None and flat_factor == 0.0,
            "source": "ffmpeg whole-stream astats; direct rail/centroid/onset checks are out of scope for >60 second audio",
        },
        "ebur128": ebur,
        "spectral": {
            "analysis_mode": "long_form_exempt",
            "centroid_active_window_count": 0,
            "centroid_hz_median": None,
            "centroid_hz_p10": None,
            "centroid_hz_p90": None,
            "active_window_threshold_dbfs": -55.0,
        },
        "clipping": {
            "probable_flat_top": None,
            "astats_zero_but_direct_flat_top": None,
            "over_full_scale_samples_are_not_automatically_clipping": True,
            "assessment": "not_directly_sample_scanned_long_form",
        },
        "long_form_exempt_from_unit_sfx_centroid_gate": True,
        "analysis_command": command,
    }


def analyze_audio(path: Path, ffmpeg: Optional[str] = None, ffprobe: Optional[str] = None) -> Dict[str, Any]:
    path = path.resolve()
    ffmpeg = ffmpeg or resolve_binary("ffmpeg")
    probe = probe_audio(path, ffprobe)
    channels = int(probe["channels"])
    is_long_form = float(probe["duration_seconds"]) > 60.0
    if is_long_form:
        # Long music/super-event tracks are included in the tree audit, but
        # they are never candidates for unit-SFX mastering. Avoid high-volume
        # per-frame centroid/astats logs while retaining full-stream EBU,
        # final astats, and direct decoded-sample evidence.
        analysis_filter = "aresample=44100,astats=metadata=1:reset=0,ebur128=peak=true:framelog=40"
    else:
        analysis_filter = (
            "aresample=44100,"
            # 4,096-sample frames reduce metadata I/O while retaining useful
            # active-window centroid resolution for unit cues.
            "asetnsamples=n=4096:p=0,"
            "astats=metadata=1:reset=1:"
            "measure_perchannel=Peak_level+RMS_level+Flat_factor+DC_offset:"
            "measure_overall=Peak_level+RMS_level+Flat_factor+DC_offset,"
            "ebur128=peak=true:framelog=40,"
            "aspectralstats=win_size=2048:overlap=0.5:measure=centroid,"
            "ametadata=print,"
            "astats=metadata=1:reset=0"
        )
    if is_long_form:
        return _analyze_long_form(path, probe, ffmpeg, analysis_filter)
    command = [
        ffmpeg,
        "-hide_banner",
        "-nostats",
        "-loglevel",
        "info",
        "-i",
        str(path),
        "-map",
        "0:a:0",
        "-vn",
        "-af",
        analysis_filter,
        "-ar",
        "44100",
        "-c:a",
        "pcm_f32le",
        "-f",
        "f32le",
        "pipe:1",
    ]
    accumulator = _SampleAccumulator(44100, channels)
    with tempfile.TemporaryFile(mode="w+b") as error_stream:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=error_stream)
        pending = bytearray()
        if process.stdout is None:
            process.kill()
            raise AudioToolError("ffmpeg sample output pipe was unavailable")
        while True:
            block = process.stdout.read(65536)
            if not block:
                break
            pending.extend(block)
            usable = len(pending) - (len(pending) % 4)
            if usable:
                values = array.array("f")
                values.frombytes(pending[:usable])
                accumulator.consume(values)
                del pending[:usable]
        process.stdout.close()
        return_code = process.wait()
        error_stream.seek(0)
        log_text = error_stream.read().decode("utf-8", errors="replace")
    if return_code != 0:
        raise AudioToolError("ffmpeg analysis failed: {}".format(log_text[-2000:]))
    if pending:
        raise AudioToolError("ffmpeg returned an incomplete float sample at end of stream")
    if accumulator.sample_count == 0:
        raise AudioToolError("ffmpeg returned no decoded audio samples")

    centroids = [] if is_long_form else _parse_centroids(log_text)
    sorted_centroids = sorted(centroids)
    median_centroid = None
    p10_centroid = None
    p90_centroid = None
    if sorted_centroids:
        median_centroid = _percentile(sorted_centroids, 0.5)
        p10_centroid = _percentile(sorted_centroids, 0.1)
        p90_centroid = _percentile(sorted_centroids, 0.9)
    direct = accumulator.result()
    astats_flat = _parse_astats_flat_factor(log_text)
    ebur = _parse_ebur128(log_text)
    flat_top_detected = bool(direct["probable_flat_top"])
    astats_zero = astats_flat is not None and astats_flat == 0.0
    return {
        "path": str(path),
        "sha256": sha256_file(path),
        "ffprobe": probe,
        "direct_sample_metrics": direct,
        "astats": {
            "flat_factor": astats_flat,
            "flat_factor_zero": astats_zero,
            "source": "ffmpeg astats; checked against direct decoded samples",
        },
        "ebur128": ebur,
        "spectral": {
            "analysis_mode": "long_form_exempt" if is_long_form else "active_windows",
            "centroid_active_window_count": len(sorted_centroids),
            "centroid_hz_median": median_centroid,
            "centroid_hz_p10": p10_centroid,
            "centroid_hz_p90": p90_centroid,
            "active_window_threshold_dbfs": -55.0,
        },
        "clipping": {
            "probable_flat_top": flat_top_detected,
            "astats_zero_but_direct_flat_top": bool(astats_zero and flat_top_detected),
            "over_full_scale_samples_are_not_automatically_clipping": True,
            "assessment": "probable_clipped" if flat_top_detected else "no_direct_flat_top_detected",
        },
        "long_form_exempt_from_unit_sfx_centroid_gate": is_long_form,
        "analysis_command": command,
    }


def _percentile(sorted_values: Sequence[float], fraction: float) -> float:
    if not sorted_values:
        raise ValueError("percentile requires at least one value")
    position = fraction * (len(sorted_values) - 1)
    low = int(math.floor(position))
    high = int(math.ceil(position))
    if low == high:
        return sorted_values[low]
    weight = position - low
    return sorted_values[low] * (1.0 - weight) + sorted_values[high] * weight
