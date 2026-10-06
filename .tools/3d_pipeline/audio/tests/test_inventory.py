import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from audio.inventory import _extract_blocks, _matching_pool, build_sound_coverage, flatten_runtime_inventory, parse_soundeffect_assets


class InventoryTests(unittest.TestCase):
    def test_balanced_soundeffect_blocks_keep_nested_sample_lists(self):
        text = '''
soundeffect = {
    name = "example_step"
    sounds = {
        sound = "take_01"
        sound = "take_02"
    }
    prevent_random_repetition = yes
}
'''
        blocks = list(_extract_blocks(text, "soundeffect"))
        self.assertEqual(1, len(blocks))
        self.assertIn("take_01", blocks[0][1])
        self.assertIn("take_02", blocks[0][1])

    def test_runtime_inventory_retains_each_consumer_and_source_hash(self):
        inventory = {
            "models": [
                {
                    "pdxmesh": "sample_unit_mesh",
                    "sound_cues": [
                        {
                            "name": "sample_step",
                            "loop": "no",
                            "samples": [{"name": "step_01", "file": {"path": "sound/sample/step.wav", "sha256": "a" * 64, "bytes": 12}}],
                        }
                    ],
                }
            ]
        }
        files, cues = flatten_runtime_inventory(inventory)
        self.assertEqual(["sample_unit"], files["sound/sample/step.wav"]["consumer_units"])
        self.assertEqual("a" * 64, files["sound/sample/step.wav"]["sha256"])
        self.assertEqual(1, cues[0]["sample_count"])

    def test_null_sample_file_is_reported_as_unresolved_not_crashing(self):
        inventory = {
            "models": [
                {
                    "pdxmesh": "sample_unit_mesh",
                    "sound_cues": [
                        {
                            "name": "sample_step",
                            "loop": "no",
                            "samples": [{"name": "step_01", "file": None}],
                        }
                    ],
                }
            ]
        }
        files, cues = flatten_runtime_inventory(inventory)
        self.assertEqual({}, files)
        self.assertEqual(1, cues[0]["unresolved_sample_count"])

    def test_additional_sound_files_are_consumer_owned_inventory_rows(self):
        inventory = {
            "models": [
                {
                    "pdxmesh": "selection_unit_mesh",
                    "sound_cues": [],
                    "additional_sound_files": [
                        {
                            "path": "sound/selection_unit/select_01.wav",
                            "sha256": "c" * 64,
                            "bytes": 99,
                        }
                    ],
                }
            ]
        }
        files, cues = flatten_runtime_inventory(inventory)
        record = files["sound/selection_unit/select_01.wav"]
        self.assertEqual("c" * 64, record["sha256"])
        self.assertEqual(["selection_unit"], record["consumer_units"])
        self.assertTrue(record["additional_sound_file"])
        self.assertEqual([], cues)

    def test_installed_vanilla_sound_path_is_not_a_missing_mod_attribution_row(self):
        vanilla_path = "C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/sound/animations/infantry_move_animation_01.wav"
        coverage = build_sound_coverage(
            Path("sound"),
            [{"unit_id": "sample_unit", "soundeffect": "sample_move", "loop": False, "sample_count": 1, "sample_names": ["vanilla"], "paths": [vanilla_path]}],
            {},
            Path("."),
            {vanilla_path: {"path": vanilla_path, "sha256": "d" * 64}},
        )
        self.assertEqual(0, coverage["attribution_coverage_count"])

    def test_family_pool_must_cover_exact_hash_and_observed_paths(self):
        pool = {
            "id": "shared_steps",
            "sha256": ["b" * 64],
            "unit_ids": ["unit_a", "unit_b"],
            "paths": ["sound/a/step.wav", "sound/b/step.wav"],
            "rationale": "accepted same-family footstep pool",
        }
        self.assertIsNotNone(_matching_pool([pool], "b" * 64, ["unit_a", "unit_b"], ["sound/a/step.wav", "sound/b/step.wav"]))
        self.assertIsNone(_matching_pool([pool], "b" * 64, ["unit_a", "unit_c"], ["sound/a/step.wav", "sound/c/step.wav"]))


if __name__ == "__main__":
    unittest.main()
