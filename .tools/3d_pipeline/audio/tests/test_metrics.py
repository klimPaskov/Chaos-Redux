import unittest
from pathlib import Path
import sys
import subprocess
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from audio.metrics import (
    _parse_astats_flat_factor,
    _parse_centroids,
    _parse_ebur128,
    analyze_audio,
    decode_mono_f32,
    find_recorded_loop_crossfade,
    loop_inner_edge_metrics,
    measure_max_gain_reduction_db,
    resolve_binary,
)


class MetricsTests(unittest.TestCase):
    def test_ebur128_parser_uses_final_summary(self):
        log = """
Integrated loudness:
  I: -21.4 LUFS
  Threshold: -31.4 LUFS
Loudness range:
  LRA: 2.1 LU
True peak:
  Peak: -1.2 dBFS
"""
        parsed = _parse_ebur128(log)
        self.assertEqual(-21.4, parsed["integrated_lufs"])
        self.assertEqual(-1.2, parsed["true_peak_dbtp"])
        self.assertEqual(2.1, parsed["loudness_range_lu"])

    def test_astats_flat_factor_and_active_centroids_parse(self):
        self.assertEqual(0.0, _parse_astats_flat_factor("[Parsed_astats] Flat factor: 0.000000"))
        log = """
frame:0 pts:0 pts_time:0
lavfi.astats.1.RMS_level=-120.0
lavfi.aspectralstats.1.centroid=105.0
frame:1 pts:1024 pts_time:0.02
lavfi.astats.1.RMS_level=-30.0
lavfi.aspectralstats.1.centroid=410.0
"""
        self.assertEqual([410.0], _parse_centroids(log))

    @unittest.skipUnless(
        Path("C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/sound/animations/infantry_move_animation_01.wav").is_file(),
        "installed vanilla HOI4 audio reference is not present",
    )
    def test_real_installed_infantry_clip_has_expected_pcm_delivery(self):
        path = Path("C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/sound/animations/infantry_move_animation_01.wav")
        report = analyze_audio(path)
        self.assertEqual("pcm_s16le", report["ffprobe"]["codec_name"])
        self.assertEqual(44100, report["ffprobe"]["sample_rate"])
        self.assertEqual(1, report["ffprobe"]["channels"])
        self.assertGreater(report["spectral"]["centroid_hz_median"], 200.0)
        self.assertEqual("no_direct_flat_top_detected", report["clipping"]["assessment"])

    @unittest.skipUnless(
        Path("sound/012_africa/units/gorilla_heavy_infantry/chaosx_gorilla_heavy_infantry_idle.wav").is_file(),
        "recorded unit loop is not present",
    )
    def test_real_gorilla_loop_uses_a_recorded_equal_power_crossfade(self):
        path = Path("sound/012_africa/units/gorilla_heavy_infantry/chaosx_gorilla_heavy_infantry_idle.wav")
        original = decode_mono_f32(path)
        result, overlap, attempts = find_recorded_loop_crossfade(original)
        self.assertIsNotNone(result)
        self.assertIsNotNone(overlap)
        self.assertEqual(len(original) - overlap, len(result))
        self.assertLessEqual(loop_inner_edge_metrics(result)["delta_db"], 3.0)
        self.assertTrue(any(item["passes_edge_gate"] for item in attempts))

    @unittest.skipUnless(
        Path("sound/002_zombie_outbreak/zombies/zombie_idle_moan_03.wav").is_file(),
        "recorded unit sample is not present",
    )
    def test_unrepairable_short_recording_remains_unresolved(self):
        original = decode_mono_f32(Path("sound/002_zombie_outbreak/zombies/zombie_idle_moan_03.wav"))
        result, overlap, attempts = find_recorded_loop_crossfade(original)
        self.assertIsNone(result)
        self.assertIsNone(overlap)
        self.assertTrue(attempts)
        self.assertFalse(any(item["passes_edge_gate"] for item in attempts))

    @unittest.skipUnless(
        Path("sound/012_africa/units/forest_giants/chaosx_forest_giants_attack.wav").is_file(),
        "recorded forest-giant attack sample is not present",
    )
    def test_real_recording_limiter_reports_maximum_gain_reduction(self):
        source = Path("sound/012_africa/units/forest_giants/chaosx_forest_giants_attack.wav")
        ffmpeg = resolve_binary("ffmpeg")
        dry = decode_mono_f32(source, ffmpeg)
        with tempfile.TemporaryDirectory(prefix="chaosx_audio_limiter_") as temp_dir:
            limited_path = Path(temp_dir) / "recorded_limited.wav"
            command = [
                ffmpeg,
                "-hide_banner",
                "-nostats",
                "-y",
                "-i",
                str(source),
                "-map",
                "0:a:0",
                "-vn",
                "-af",
                "alimiter=limit=0.5:attack=5:release=50:level=false:latency=true",
                "-ar",
                "44100",
                "-ac",
                "1",
                "-c:a",
                "pcm_f32le",
                str(limited_path),
            ]
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
            self.assertEqual(0, result.returncode, result.stderr.decode("utf-8", errors="replace"))
            wet = decode_mono_f32(limited_path, ffmpeg)
        measured = measure_max_gain_reduction_db(dry, wet)
        self.assertGreater(measured["max_sample_gain_reduction_db"], 0.1)
        self.assertGreater(measured["compared_sample_count"], 0)


if __name__ == "__main__":
    unittest.main()
