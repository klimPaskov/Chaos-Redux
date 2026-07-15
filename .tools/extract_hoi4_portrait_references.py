#!/usr/bin/env python3
"""Extract the approved vanilla HOI4 portrait references as review PNGs.

The files under the event-assets skill's canonical ``assets/vanilla_reference``
portrait folders are style references only. They are never runtime mod assets
and must not be wired through a Chaos Redux ``.gfx`` file.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


LEADER_REFERENCES = (
	("den_thorvald_stauning", "gfx/leaders/DEN/Portrait_Denmark_Thorvald_Stauning.dds"),
	("ire_eamon_de_valera", "gfx/leaders/IRE/Portrait_Ireland_Eamon_de_Valera.dds"),
	("fin_carl_mannerheim", "gfx/leaders/FIN/portrait_fin_carl_mannerheim.dds"),
)

ADVISOR_REFERENCES = (
	("generic_europe_1", "gfx/interface/ideas/idea_generic_political_advisor_europe_1.dds"),
	("generic_female_europe", "gfx/interface/ideas/idea_generic_political_advisor_female_europe.dds"),
	("generic_asia_1", "gfx/interface/ideas/idea_generic_political_advisor_asia_1.dds"),
)

REFERENCE_ROOT = Path(
	".agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits"
)


def extract_set(game_root: Path, output: Path, entries: tuple[tuple[str, str], ...]) -> None:
	output.mkdir(parents=True, exist_ok=True)
	for stem, relative_path in entries:
		source = game_root / relative_path
		if not source.is_file():
			raise FileNotFoundError(f"Missing vanilla reference: {source}")
		with Image.open(source) as image:
			image.convert("RGBA").save(output / f"{stem}.png")


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument(
		"--game-root",
		type=Path,
		default=Path(r"C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV"),
	)
	parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
	return parser.parse_args()


def main() -> None:
	args = parse_args()
	extract_set(args.game_root, args.repo_root / REFERENCE_ROOT / "leaders", LEADER_REFERENCES)
	extract_set(args.game_root, args.repo_root / REFERENCE_ROOT / "advisors", ADVISOR_REFERENCES)


if __name__ == "__main__":
	main()
