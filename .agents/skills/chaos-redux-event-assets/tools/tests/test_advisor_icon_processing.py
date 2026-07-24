from __future__ import annotations

import importlib.util
import inspect
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


TOOL_PATH = Path(__file__).resolve().parents[1] / "advisor_icon_processing.py"
SPEC = importlib.util.spec_from_file_location("advisor_icon_processing", TOOL_PATH)
if SPEC is None or SPEC.loader is None:
	raise RuntimeError(f"Unable to load processor module: {TOOL_PATH}")
PROCESSOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PROCESSOR)


class RoleFamilyProcessorTests(unittest.TestCase):
	def test_cli_defaults_to_leader_family(self) -> None:
		with patch.object(
			sys,
			"argv",
			[
				str(TOOL_PATH),
				"leader",
				"source.png",
				"candidate.png",
				"--crop",
				"0",
				"0",
				"10",
				"10",
				"--source-kind",
				"fictional",
				"--review-sheet",
				"review.png",
			],
		):
			args = PROCESSOR.parse_args()
		self.assertEqual(args.role_family, "leader")

	def test_cli_accepts_explicit_commander_family(self) -> None:
		with patch.object(
			sys,
			"argv",
			[
				str(TOOL_PATH),
				"leader",
				"source.png",
				"candidate.png",
				"--role-family",
				"commander",
				"--crop",
				"0",
				"0",
				"10",
				"10",
				"--source-kind",
				"real",
				"--review-sheet",
				"review.png",
			],
		):
			args = PROCESSOR.parse_args()
		self.assertEqual(args.role_family, "commander")

	def test_commander_defaults_use_montgomery_and_witzleben(self) -> None:
		reference_dir, references = PROCESSOR.resolve_full_size_references(
			"commander"
		)
		self.assertEqual(
			reference_dir,
			(
				PROCESSOR.REFERENCE_ROOT / "commanders"
			).resolve(),
		)
		self.assertEqual(
			[record["name"] for record in references],
			[
				"eng_bernard_montgomery.png",
				"ger_erwin_von_witzleben.png",
			],
		)
		for record in references:
			self.assertEqual(len(record["sha256"]), 64)

	def test_normalized_command_records_family_and_reference_hashes(self) -> None:
		reference_dir, references = PROCESSOR.resolve_full_size_references(
			"commander"
		)
		args = SimpleNamespace(
			mode="leader",
			source=PROCESSOR.REPO_ROOT / "source.png",
			output=PROCESSOR.REPO_ROOT / "candidate.png",
			crop=[0, 0, 10, 10],
			source_kind="real",
			face_box=None,
			review_sheet=PROCESSOR.REPO_ROOT / "review.png",
			reference_dir=None,
			advisor_overlay_manifest=None,
			portrait_provenance_manifest=None,
			advisor_frame_overlay=None,
			advisor_frame_source=None,
			advisor_paper_overlay=None,
			advisor_paper_source=None,
			force=False,
		)
		command = PROCESSOR.normalized_command_record(
			args,
			PROCESSOR.REPO_ROOT / "metadata.json",
			"commander",
			reference_dir,
			references,
		)
		self.assertEqual(command["role_family"], "commander")
		self.assertEqual(command["selected_references"], references)
		self.assertEqual(
			command["arguments"]["selected_references"],
			references,
		)

	def test_review_sheet_uses_processor_input_crop_label(self) -> None:
		source = inspect.getsource(PROCESSOR.make_review_sheet)
		self.assertIn("PROCESSOR_INPUT_CROP_LABEL", source)
		self.assertNotIn('"explicit source crop"', source)
		self.assertEqual(
			PROCESSOR.PROCESSOR_INPUT_CROP_LABEL,
			"processor input crop",
		)


if __name__ == "__main__":
	unittest.main()
