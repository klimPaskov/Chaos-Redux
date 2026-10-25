"""Source binding and DDS dimension checks; not an in-game render test."""
from pathlib import Path
import re
import struct
import unittest

ROOT = Path(__file__).resolve().parents[2]
EVENTS = (ROOT / "events/025_alien_technology_in_antarctica.txt").read_text(encoding="utf-8-sig")
GFX = (ROOT / "interface/025_alien_technology_in_antarctica.gfx").read_text(encoding="utf-8-sig")
# The forerunner craft report and news pictures live with the shared event pictures.
GFX += (ROOT / "interface/chaosx_pictures.gfx").read_text(encoding="utf-8-sig")
SPRITES = dict(re.findall(r'name\s*=\s*"([^"]+)"\s+texturefile\s*=\s*"([^"]+)"', GFX))


class ReportAssetTests(unittest.TestCase):
    def test_event025_picture_aliases_are_defined(self):
        for alias in re.findall(r"\bpicture\s*=\s*(GFX_\w+)", EVENTS):
            with self.subTest(alias=alias):
                self.assertIn(alias, SPRITES)

    def test_registered_texture_paths_exist(self):
        for texture in re.findall(r'texturefile\s*=\s*"([^"]+)"', GFX):
            with self.subTest(texture=texture):
                self.assertTrue((ROOT / texture).is_file())

    def test_failure_report_uses_its_native_dds(self):
        alias = "GFX_report_event_025_antarctic_sabotage"
        texture = "gfx/event_pictures/025_alien_technology_in_antarctica/report_event_025_sabotage.dds"
        self.assertEqual(SPRITES[alias], texture)
        header = (ROOT / texture).read_bytes()[:128]
        self.assertEqual(header[:4], b"DDS ")
        height, width = struct.unpack_from("<II", header, 12)
        self.assertEqual((width, height), (210, 176))
        self.assertRegex(EVENTS, r"id\s*=\s*chaosx\.nr25\.86[\s\S]*?picture\s*=\s*" + alias)


if __name__ == "__main__":
    unittest.main()
