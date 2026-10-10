"""anim_signs removes exporter-level quaternion sign flips without changing any orientation."""
import sys
import tempfile
import unittest
from pathlib import Path
from xml.etree.ElementTree import Element, SubElement

PIPELINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE / "review"))
sys.path.insert(0, str(PIPELINE / "runtime"))
import anim_signs  # noqa: E402
import pdx_reader  # noqa: E402


def build(path, samples):
    module, _ = pdx_reader.parser()
    root = Element("File", {"pdxasset": [1, 0]})
    info = SubElement(root, "info", {"fps": [30.0], "sa": [len(samples)], "j": [2]})
    for name in ("Hips", "Spine"):
        SubElement(info, name, {"sa": ["tqs"], "t": [0.0, 1.0, 0.0], "q": [0.0, 0.0, 0.0, 1.0], "s": [1.0]})
    flat_q = []
    for frame in samples:
        for q in frame:
            flat_q.extend(float(v) for v in q)
    SubElement(root, "samples", {"t": [0.0] * (3 * 2 * len(samples)), "q": flat_q, "s": [1.0] * (2 * len(samples))})
    module.write_animfile(str(path), root)


class AnimSigns(unittest.TestCase):
    def test_flipped_samples_are_negated_and_orientation_is_unchanged(self):
        # bone 0 flips sign on frame 2 (same orientation), bone 1 is continuous
        frames = [[(0, 0, 0, 1.0), (0.0, 0.1, 0.0, 0.995)],
                  [(0, 0.05, 0, 0.9987), (0.0, 0.2, 0.0, 0.98)],
                  [(0, -0.1, 0, -0.995), (0.0, 0.3, 0.0, 0.954)],
                  [(0, -0.15, 0, -0.9887), (0.0, 0.4, 0.0, 0.9165)]]
        with tempfile.TemporaryDirectory() as folder:
            src = Path(folder) / "a.anim"
            build(src, frames)
            receipt = anim_signs.fix(src)
            self.assertEqual(receipt["negative_dots_before"], 1)
            self.assertEqual(receipt["negative_dots_after"], 0)
            module, _ = pdx_reader.parser()
            tree = module.read_meshfile(str(src))
            q = tree.find("samples").get("q")
            # frame 2 / frame 3 of bone 0 are now the negation of what was written (same rotation)
            self.assertAlmostEqual(q[2 * 8 + 3], 0.995, places=5)
            self.assertAlmostEqual(q[3 * 8 + 3], 0.9887, places=4)
            self.assertTrue(Path(str(src) + ".signs_orig").exists())


if __name__ == "__main__":
    unittest.main()
