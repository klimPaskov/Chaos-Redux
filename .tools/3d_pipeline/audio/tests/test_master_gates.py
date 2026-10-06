import json
import subprocess
import unittest
from pathlib import Path
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from audio.master import _default_output_path, _limiter_stage, _postmaster_trim, _source_gate
from audio.metrics import analyze_audio, resolve_binary


def _analysis(flat_top, astats_flat_factor):
    return {
        "clipping": {"probable_flat_top": flat_top},
        "direct_sample_metrics": {"nonfinite_sample_count": 0},
        "astats": {"flat_factor": astats_flat_factor},
        "spectral": {"centroid_hz_median": 1000.0},
    }


class MasterGateTests(unittest.TestCase):
    def test_astats_zero_does_not_override_direct_flat_top_evidence(self):
        blockers = _source_gate(_analysis(True, 0.0), "shot", False)
        self.assertIn("source_has_probable_clipped_flat_tops", blockers)

    def test_nonzero_astats_alone_does_not_reject_unclipped_source(self):
        blockers = _source_gate(_analysis(False, 4.4), "shot", False)
        self.assertEqual([], blockers)

    def test_default_destinations_are_unique_for_samples_in_one_cue(self):
        root = Path("docs/plans/unit_fix_2026-10/audio_evidence/staged")
        first = _default_output_path(root, "unit", "unit_steps", "sound/unit/step_01.wav")
        second = _default_output_path(root, "unit", "unit_steps", "sound/unit/step_02.wav")
        self.assertNotEqual(first, second)
        self.assertIn("step_01_", first.name)
        self.assertIn("step_02_", second.name)

    @unittest.skipUnless(
        Path("sound/012_africa/units/plague_carriers/chaosx_plague_carriers_select.wav").is_file(),
        "recorded plague-carrier selection sample is not present",
    )
    def test_postmaster_lead_trim_uses_a_real_recording_and_measures_again(self):
        source = Path("sound/012_africa/units/plague_carriers/chaosx_plague_carriers_select.wav")
        before = analyze_audio(source)
        lead_ms = before["direct_sample_metrics"]["leading_silence_ms_at_minus55db"]
        self.assertGreater(lead_ms, 20.0)
        with tempfile.TemporaryDirectory(prefix="chaosx_audio_posttrim_") as temp_dir:
            output = Path(temp_dir) / "derived_recording.wav"
            trim_start, _ = _postmaster_trim(resolve_binary("ffmpeg"), source, output, lead_ms)
            after = analyze_audio(output)
        self.assertGreater(trim_start, 0.0)
        self.assertLessEqual(after["direct_sample_metrics"]["leading_silence_ms_at_minus55db"], 20.0)

    @unittest.skipUnless(
        Path("sound/012_africa/units/forest_giants/chaosx_forest_giants_attack.wav").is_file(),
        "recorded forest-giant attack sample is not present",
    )
    def test_bounded_limiter_records_reduction_from_real_source_samples(self):
        source = Path("sound/012_africa/units/forest_giants/chaosx_forest_giants_attack.wav")
        before = analyze_audio(source)
        peak = before["direct_sample_metrics"]["sample_peak_dbfs"]
        with tempfile.TemporaryDirectory(prefix="chaosx_audio_bounded_limiter_") as temp_dir:
            work = Path(temp_dir)
            evidence = _limiter_stage(resolve_binary("ffmpeg"), source, work / "limited.wav", 3.0, peak)
        reduction = evidence["gain_reduction"]
        self.assertGreater(reduction["max_sample_gain_reduction_db"], 2.5)
        self.assertLessEqual(reduction["max_sample_gain_reduction_db"], 6.5001)
        self.assertGreater(reduction["compared_sample_count"], 0)
        self.assertTrue(reduction["within_bounded_policy"])

    @unittest.skipUnless(
        Path("sound/012_africa/units/forest_giants/chaosx_forest_giants_attack.wav").is_file(),
        "recorded forest-giant attack sample is not present",
    )
    def test_inspect_cli_accepts_parent_flag_interface_and_writes_role_report(self):
        repo = Path.cwd()
        source = Path("sound/012_africa/units/forest_giants/chaosx_forest_giants_attack.wav")
        cli = Path(".tools/3d_pipeline/audio/master.py")
        with tempfile.TemporaryDirectory(prefix="chaosx_audio_inspect_cli_") as temp_dir:
            report_path = Path(temp_dir) / "source_probe.json"
            result = subprocess.run(
                [sys.executable, str(cli), "inspect", "--input", str(source), "--role", "shot",
                 "--output", str(report_path), "--force"],
                cwd=str(repo), stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
                universal_newlines=True,
            )
            self.assertEqual(0, result.returncode, result.stderr)
            report = json.loads(report_path.read_text(encoding="utf-8"))
        self.assertEqual("shot", report["role"])
        self.assertEqual(report["before"]["sha256"], report["source_sha256"])
        self.assertTrue(report["processing"]["read_only"])
        self.assertIn("shot_peak_target_minus3_plusminus0_8", report["checks"])

    @unittest.skipUnless(
        Path("docs/plans/unit_fix_2026-10/audio_evidence/recovery2_evidence/recovery2_batch.json").is_file(),
        "recovery2 batch evidence is not present",
    )
    def test_compat_report_cli_emits_established_install_result_aliases(self):
        repo = Path.cwd()
        source_report = Path("docs/plans/unit_fix_2026-10/audio_evidence/recovery2_evidence/recovery2_batch.json")
        cli = Path(".tools/3d_pipeline/audio/master.py")
        with tempfile.TemporaryDirectory(prefix="chaosx_audio_compat_cli_") as temp_dir:
            report_path = Path(temp_dir) / "compatible.json"
            result = subprocess.run(
                [sys.executable, str(cli), "compat-report", "--input-report", str(source_report),
                 "--output", str(report_path), "--force"],
                cwd=str(repo), stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
                universal_newlines=True,
            )
            self.assertEqual(0, result.returncode, result.stderr)
            report = json.loads(report_path.read_text(encoding="utf-8"))
        self.assertEqual(17, report["result_count"])
        self.assertEqual(2, report["excluded_count"])
        required = {"source_relative_path", "source_sha256", "destination_path", "output_sha256",
                    "before", "after", "checks", "processing"}
        self.assertTrue(all(required.issubset(row) for row in report["results"]))
        self.assertTrue(all(row["status"] == "staged" for row in report["results"]))


if __name__ == "__main__":
    unittest.main()
