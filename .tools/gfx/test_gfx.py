"""Unit tests for the bounded Chaos Redux sprite QA helpers."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import struct
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import numpy as np
from PIL import Image


ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("chaosx_gfx", Path(__file__).with_name("gfx.py"))
gfx = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(gfx)

VANILLA = Path(r"C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\gfx\interface\counters")


class GfxHelpersTests(unittest.TestCase):
    def test_canonical_dds_round_trip_keeps_bgra_pixels_and_header(self):
        pixels = np.array([
            [[240, 10, 20, 255], [7, 80, 190, 37]],
            [[5, 6, 7, 0], [255, 255, 255, 128]],
        ], dtype=np.uint8)
        image = Image.fromarray(pixels, "RGBA")
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "roundtrip.dds"
            gfx.write_dds(image, output)
            raw = output.read_bytes()
            self.assertEqual(raw[:4], b"DDS ")
            self.assertEqual(struct.unpack_from("<I", raw, 4)[0], 124)
            self.assertEqual(struct.unpack_from("<II", raw, 12), (2, 2))
            self.assertEqual(len(raw), 128 + 2 * 2 * 4)
            self.assertEqual(np.asarray(gfx.strict_dds(output)).tobytes(), pixels.tobytes())
            self.assertEqual(np.asarray(gfx.load(output)).tobytes(), pixels.tobytes())

    def test_strict_dds_rejects_truncated_payload_and_moved_pixel_format(self):
        image = Image.new("RGBA", (2, 2), (11, 22, 33, 255))
        with tempfile.TemporaryDirectory() as directory:
            valid = Path(directory) / "valid.dds"
            gfx.write_dds(image, valid)
            truncated = Path(directory) / "truncated.dds"
            truncated.write_bytes(valid.read_bytes()[:-1])
            moved = Path(directory) / "moved.dds"
            raw = bytearray(valid.read_bytes())
            raw[76:80], raw[80:84] = raw[80:84], raw[76:80]
            moved.write_bytes(raw)
            for bad in (truncated, moved):
                with self.subTest(path=bad.name), self.assertRaises(ValueError):
                    gfx.strict_dds(bad)

    def test_defringe_removes_one_alpha_pixel_and_replaces_chroma_from_core(self):
        image = Image.new("RGBA", (9, 9), (0, 255, 0, 0))
        # Large uncontaminated region makes the intended nearest interior unambiguous.
        for y in range(2, 7):
            for x in range(2, 7):
                image.putpixel((x, y), (30, 80, 120, 255))
        image.putpixel((1, 4), (0, 255, 0, 255))
        image.putpixel((3, 4), (0, 255, 0, 180))
        repaired = gfx.defringe(image, erosion=1)
        self.assertEqual(repaired.getpixel((1, 4))[3], 0)
        self.assertEqual(repaired.getpixel((3, 4))[:3], (30, 80, 120))
        self.assertEqual(repaired.getpixel((3, 4))[3], 180)
        self.assertEqual(repaired.getpixel((5, 4))[3], 255)
        self.assertEqual(repaired.getpixel((0, 0))[3], 0)

    def test_defringe_fails_closed_for_empty_or_fully_opaque_canvases(self):
        with self.assertRaisesRegex(ValueError, "Empty subject"):
            gfx.defringe(Image.new("RGBA", (7, 7), (1, 2, 3, 0)))
        with self.assertRaisesRegex(ValueError, "No transparent canvas"):
            gfx.defringe(Image.new("RGBA", (7, 7), (1, 2, 3, 255)))

    def test_frames_are_repaired_independently_without_cross_frame_rgb_bleed(self):
        sheet = Image.new("RGBA", (16, 8), (0, 0, 0, 0))
        for y in range(2, 6):
            for x in range(2, 6):
                sheet.putpixel((x, y), (220, 20, 20, 255))
            for x in range(10, 14):
                sheet.putpixel((x, y), (20, 20, 220, 255))
        left, right = gfx.frames(sheet, 2)
        repaired = [gfx.defringe(frame) for frame in (left, right)]
        self.assertTrue(all(repaired[0].getpixel((x, y))[2] < 100
                            for y in range(8) for x in range(8)
                            if repaired[0].getpixel((x, y))[3] > 0))
        self.assertTrue(all(repaired[1].getpixel((x, y))[0] < 100
                            for y in range(8) for x in range(8)
                            if repaired[1].getpixel((x, y))[3] > 0))

    def test_alpha_ghost_threshold_and_opaque_normal_image_are_explicit(self):
        ghost = Image.new("RGBA", (5, 5), (0, 0, 0, 0))
        ghost.putpixel((2, 2), (20, 30, 40, 100))
        normal = Image.new("RGBA", (5, 5), (20, 30, 40, 255))
        self.assertTrue(gfx.alpha_stats(ghost)["ghosted"])
        self.assertFalse(gfx.alpha_stats(normal)["ghosted"])
        self.assertEqual(gfx.alpha_stats(normal)["subject_alpha_mean"], 255)

    def test_size_profiles_report_wrong_canvas_and_three_pixel_margin(self):
        wrong = Image.new("RGBA", (93, 86), (0, 0, 0, 0))
        self.assertTrue(any("canvas" in finding for finding in gfx.size_check(wrong, "focus")))
        tight = Image.new("RGBA", (34, 34), (0, 0, 0, 0))
        for y in range(2, 32):
            for x in range(2, 32):
                tight.putpixel((x, y), (120, 120, 120, 255))
        findings = gfx.size_check(tight, "decision", margin=3)
        self.assertTrue(any("minimum 3" in finding for finding in findings))
        self.assertEqual(gfx.PROFILES["report"][:2], (210, 176))
        self.assertEqual(gfx.PROFILES["news"][:2], (397, 153))

    def test_output_refusal_does_not_modify_input_even_with_force(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source.png"
            original = Image.new("RGBA", (5, 5), (40, 80, 120, 255))
            original.save(source)
            before = source.read_bytes()
            result = subprocess.run(
                [sys.executable, str(Path(__file__).with_name("gfx.py")), "defringe",
                 str(source), "--root", str(root), "--out", str(root), "--force"],
                capture_output=True, text=True, check=False)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Input overwrite forbidden", result.stdout)
            self.assertEqual(source.read_bytes(), before)

    def test_non_force_output_install_preserves_competing_writer(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "review.png"
            competitor_bytes = b"created by competing worker"
            install = gfx.install_output

            def competitor_wins(scratch, path, overwrite):
                path.write_bytes(competitor_bytes)
                return install(scratch, path, overwrite)

            image = Image.new("RGBA", (4, 4), (20, 40, 60, 255))
            with patch.object(gfx, "install_output", side_effect=competitor_wins):
                with self.assertRaises(FileExistsError):
                    gfx.write_png(image, target, overwrite=False)
            self.assertEqual(target.read_bytes(), competitor_bytes)
            self.assertEqual(list(Path(directory).iterdir()), [target])

    def test_json_report_refuses_to_replace_a_selected_input(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.png"
            Image.new("RGBA", (5, 5), (40, 80, 120, 255)).save(source)
            before = source.read_bytes()
            result = subprocess.run(
                [sys.executable, str(Path(__file__).with_name("gfx.py")), "alpha",
                 str(source), "--json", str(source)],
                capture_output=True, text=True, check=False)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(source.read_bytes(), before)

    def test_json_report_refuses_input_list_and_planned_output_collisions(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source.png"
            Image.new("RGBA", (9, 9), (40, 80, 120, 255)).save(source)
            manifest = root / "inputs.json"
            manifest.write_text('[{"path":"source.png","frames":1}]', encoding="utf-8")
            list_before = manifest.read_bytes()
            list_result = subprocess.run(
                [sys.executable, str(Path(__file__).with_name("gfx.py")), "alpha",
                 "--list", str(manifest), "--json", str(manifest)],
                capture_output=True, text=True, check=False)
            self.assertNotEqual(list_result.returncode, 0)
            self.assertEqual(manifest.read_bytes(), list_before)

            planned_png = root / "output" / "source.png"
            output_result = subprocess.run(
                [sys.executable, str(Path(__file__).with_name("gfx.py")), "defringe",
                 str(source), "--root", str(root), "--out", str(root / "output"),
                 "--json", str(planned_png)],
                capture_output=True, text=True, check=False)
            self.assertNotEqual(output_result.returncode, 0)
            self.assertFalse(planned_png.exists())

    def test_manifest_can_declare_mixed_frame_counts(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            single = root / "single.png"
            strip = root / "strip.png"
            Image.new("RGBA", (8, 8), (10, 20, 30, 255)).save(single)
            Image.new("RGBA", (16, 8), (10, 20, 30, 255)).save(strip)
            manifest = root / "inputs.json"
            manifest.write_text(json.dumps([
                {"path": str(single), "frames": 1},
                {"texture": str(strip), "frames": 2},
            ]), encoding="utf-8")
            report = root / "report.json"
            result = subprocess.run(
                [sys.executable, str(Path(__file__).with_name("gfx.py")), "alpha",
                 "--list", str(manifest), "--json", str(report)],
                capture_output=True, text=True, check=False)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            rows = json.loads(report.read_text(encoding="utf-8"))
            self.assertEqual([len(row["frames"]) for row in rows], [1, 2])


class InstalledVanillaCounterTests(unittest.TestCase):
    @unittest.skipUnless((VANILLA / "divisions_large" / "unit_infantry_icon.dds").is_file()
                         and (VANILLA / "divisions_small" / "onmap_unit_infantry_icon.dds").is_file(),
                         "Installed vanilla counter DDS files unavailable")
    def test_exact_vanilla_reference_surfaces_are_valid_inputs_and_expose_threshold_baseline(self):
        large = gfx.load(VANILLA / "divisions_large" / "unit_infantry_icon.dds")
        small = gfx.load(VANILLA / "divisions_small" / "onmap_unit_infantry_icon.dds")
        self.assertEqual(large.size, (152, 42))
        self.assertEqual(small.size, (60, 12))
        # These are precise baselines: legacy normal frames have translucent pixels,
        # so a universal <200 subject-alpha rule would reject the vanilla templates.
        self.assertLess(gfx.alpha_stats(gfx.frames(large, 2)[0])["subject_alpha_mean"], 200)
        self.assertLess(gfx.alpha_stats(gfx.frames(small, 2)[0])["subject_alpha_mean"], 200)
        large_findings = gfx.counter_check(large, "large", large)
        small_findings = gfx.counter_check(small, "small", small)
        # The reference itself must not be presented as a defective candidate.
        self.assertEqual(large_findings, [])
        self.assertEqual(small_findings, [])


if __name__ == "__main__":
    unittest.main()
