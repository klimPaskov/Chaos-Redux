#!/usr/bin/env python3
"""Extract the approved vanilla HOI4 portrait references as review PNGs.

The files under ``assets/leader_portraits`` and ``assets/advisor_icons`` are
style references only. They are never runtime mod assets and must not be wired
through a Chaos Redux ``.gfx`` file.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw


LEADER_REFERENCES = (
	("vanilla_den_thorvald_stauning", "gfx/leaders/DEN/Portrait_Denmark_Thorvald_Stauning.dds"),
	("vanilla_ire_eamon_de_valera", "gfx/leaders/IRE/Portrait_Ireland_Eamon_de_Valera.dds"),
	("vanilla_fin_carl_mannerheim", "gfx/leaders/FIN/portrait_fin_carl_mannerheim.dds"),
	("vanilla_lux_charlotte", "gfx/leaders/LUX/portrait_LUX_charlotte_wilhelmine.dds"),
	("vanilla_ice_sveinn_bjornsson", "gfx/leaders/ICE/portrait_ice_sveinn_bjornsson.dds"),
	("vanilla_eth_haile_selassie", "gfx/leaders/ETH/Portrait_Ethiopia_Haile_Selassie.dds"),
)

ADVISOR_REFERENCES = (
	("vanilla_advisor_europe_1", "gfx/interface/ideas/idea_generic_political_advisor_europe_1.dds"),
	("vanilla_advisor_europe_6", "gfx/interface/ideas/idea_generic_political_advisor_europe_6.dds"),
	("vanilla_advisor_female_europe", "gfx/interface/ideas/idea_generic_political_advisor_female_europe.dds"),
	("vanilla_advisor_africa_1", "gfx/interface/ideas/idea_generic_political_advisor_africa_1.dds"),
	("vanilla_advisor_asia_1", "gfx/interface/ideas/idea_generic_political_advisor_asia_1.dds"),
	("vanilla_high_command_fevzi_cakmak", "gfx/interface/ideas/idea_tur_fevzi_cakmak_high_command.dds"),
)


def extract_set(game_root: Path, output: Path, entries: tuple[tuple[str, str], ...], scale: int) -> None:
	output.mkdir(parents=True, exist_ok=True)
	decoded: list[tuple[str, Image.Image]] = []
	for stem, relative_path in entries:
		source = game_root / relative_path
		if not source.is_file():
			raise FileNotFoundError(f"Missing vanilla reference: {source}")
		with Image.open(source) as image:
			rgba = image.convert("RGBA")
		rgba.save(output / f"{stem}.png")
		decoded.append((stem, rgba))

	cell_width = max(image.width for _, image in decoded) * scale + 24
	cell_height = max(image.height for _, image in decoded) * scale + 42
	columns = 3
	rows = (len(decoded) + columns - 1) // columns
	sheet = Image.new("RGBA", (cell_width * columns, cell_height * rows), (32, 34, 36, 255))
	draw = ImageDraw.Draw(sheet)
	for index, (stem, image) in enumerate(decoded):
		resample = Image.Resampling.NEAREST if scale > 1 else Image.Resampling.LANCZOS
		preview = image.resize((image.width * scale, image.height * scale), resample)
		x = (index % columns) * cell_width + (cell_width - preview.width) // 2
		y = (index // columns) * cell_height + 8
		checker = Image.new("RGBA", preview.size, (92, 92, 92, 255))
		checker_draw = ImageDraw.Draw(checker)
		tile = 8
		for check_y in range(0, preview.height, tile):
			for check_x in range(0, preview.width, tile):
				if (check_x // tile + check_y // tile) % 2:
					checker_draw.rectangle(
						(check_x, check_y, min(check_x + tile - 1, preview.width - 1), min(check_y + tile - 1, preview.height - 1)),
						fill=(132, 132, 132, 255),
					)
		checker.alpha_composite(preview)
		sheet.alpha_composite(checker, (x, y))
		draw.text(
			((index % columns) * cell_width + 8, y + preview.height + 8),
			stem.removeprefix("vanilla_"),
			fill=(235, 235, 235, 255),
		)
	sheet.save(output / "contact_sheet.png")


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
	extract_set(args.game_root, args.repo_root / "assets/leader_portraits", LEADER_REFERENCES, scale=1)
	extract_set(args.game_root, args.repo_root / "assets/advisor_icons", ADVISOR_REFERENCES, scale=2)


if __name__ == "__main__":
	main()
