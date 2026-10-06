"""Check the runtime shader contract independently of Blender preview shading."""
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

from PIL import Image

SOURCE = Path(__file__).parents[1] / "pack_pdx_material.py"
SPEC = importlib.util.spec_from_file_location("pack_pdx_material", SOURCE)
PACK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PACK)


class PdxGlossinessTests(unittest.TestCase):
    def test_explicit_class_recipes_bound_gloss_while_provider_bytes_stay_unchanged(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            roughness = Image.new("L", (4, 1))
            roughness.putdata([0, 64, 128, 255])
            roughness.save(root / "roughness.png")
            Image.new("L", (4, 1), 73).save(root / "metallic.png")
            cloth = Image.new('L', (4, 1)); cloth.putdata([0, 0, 255, 255]); cloth.save(root / 'cloth.png')
            steel = Image.new('L', (4, 1)); steel.putdata([255, 255, 0, 0]); steel.save(root / 'steel.png')
            Image.new('L', (4, 1), 255).save(root / 'occupancy.png')
            (root / 'material_classes.json').write_text(json.dumps({'classes': {'cloth': 'cloth.png', 'steel': 'steel.png'}, 'occupancy': 'occupancy.png'}))
            originals = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in root.glob("*.png")}
            PACK.ensure_gltf_metallic_roughness_map(root, "metallic_roughness.png")
            with Image.open(root / "metallic_roughness.png") as gltf:
                self.assertEqual(list(gltf.getchannel("G").getdata()), [0, 64, 128, 255])
            reports = [PACK.pack_pdx_specular_map(root, "metallic_roughness.png"),
                       PACK.pack_pdx_specular_channels(root, "metallic.png", "roughness.png", "separate.png")]
            for report in reports:
                self.assertEqual(report["layout"]["alpha"], "glossiness_255_minus_roughness")
                with Image.open(root / report["output"]["path"]) as result:
                    self.assertEqual(list(result.getchannel("A").getdata()), [180, 180, 100, 60])
                    green = list(result.getchannel('G').getdata())
                    self.assertTrue(all(180 <= value <= 255 for value in green[:2]))
                    self.assertTrue(all(40 <= value <= 90 for value in green[2:]))
                    blue = list(result.getchannel('B').getdata())
                    self.assertTrue(all(value >= 200 for value in blue[:2]))
                    self.assertEqual(blue[2:], [0, 0])
            for filename, digest in originals.items():
                self.assertEqual(hashlib.sha256((root / filename).read_bytes()).hexdigest(), digest)

    def test_unknown_material_coverage_refuses_pack(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            Image.new('L', (4, 1), 128).save(root / 'roughness.png')
            Image.new('L', (4, 1), 0).save(root / 'metallic.png')
            with self.assertRaisesRegex(ValueError, 'material_classes.json'):
                PACK.pack_pdx_specular_channels(root, 'metallic.png', 'roughness.png', 'out.png')
            self.assertFalse((root / 'out.png').exists())


if __name__ == "__main__":
    unittest.main()
