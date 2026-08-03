#!/usr/bin/env python3
"""Build the Chaos Redux map/buildings override from the installed vanilla table."""

from __future__ import annotations

import argparse
import math
from collections import Counter
from pathlib import Path

from PIL import Image


FACILITY_SPAWN_LAYOUT = (
	("chaosx_biowarfare_facility_spawn", (-12, 0), 0.35),
	("chaosx_cw_facility_spawn", (12, 0), 1.40),
)

CAMP_SPAWN_LAYOUT = (
	("chaosx_concentration_camp_visual_anchor_spawn", (0, -12), 2.10),
	("chaosx_concentration_camp_visual_anchor_spawn", (9, -9), 2.45),
	("chaosx_concentration_camp_visual_anchor_spawn", (9, 9), 2.80),
	("chaosx_concentration_camp_visual_anchor_spawn", (0, 12), 3.15),
	("chaosx_concentration_camp_visual_anchor_spawn", (-9, 9), 3.50),
	("chaosx_extermination_camp_visual_anchor_spawn", (-9, -9), 3.85),
	("chaosx_extermination_camp_visual_anchor_spawn", (-16, -8), 4.20),
	("chaosx_extermination_camp_visual_anchor_spawn", (-16, 8), 4.55),
	("chaosx_extermination_camp_visual_anchor_spawn", (16, -8), 4.90),
	("chaosx_extermination_camp_visual_anchor_spawn", (16, 8), 5.25),
)

SPAWN_LAYOUT = FACILITY_SPAWN_LAYOUT + CAMP_SPAWN_LAYOUT

STATIC_ROWS = (
	"64;anomaly_signal_beacon_pilot_spawn;2995.00;9.70;1556.00;0.00;0",
)


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser()
	parser.add_argument("--vanilla-map", type=Path, required=True)
	parser.add_argument("--output", type=Path, required=True)
	parser.add_argument("--force", action="store_true")
	return parser.parse_args()


def load_land_colours(definition_path: Path) -> set[tuple[int, int, int]]:
	colours: set[tuple[int, int, int]] = set()
	for raw_line in definition_path.read_text(encoding="utf-8-sig").splitlines():
		parts = raw_line.split(";")
		if len(parts) >= 5 and parts[4] == "land":
			colours.add((int(parts[1]), int(parts[2]), int(parts[3])))
	return colours


def select_positions(
	province_pixels: Image.Image,
	base_x: float,
	base_z: float,
	layout: tuple[tuple[str, tuple[int, int], float], ...],
) -> list[tuple[float, float]]:
	width, height = province_pixels.size
	base_px = max(0, min(width - 1, round(base_x)))
	base_py = max(0, min(height - 1, height - 1 - round(base_z)))
	province_colour = province_pixels.getpixel((base_px, base_py))
	candidates: list[tuple[float, float]] = []

	for radius in (16, 32, 64):
		candidates.clear()
		for py in range(max(0, base_py - radius), min(height, base_py + radius + 1)):
			for px in range(max(0, base_px - radius), min(width, base_px + radius + 1)):
				if province_pixels.getpixel((px, py)) == province_colour:
					candidates.append((px, py))
		if len(candidates) >= len(layout):
			break

	if len(candidates) < len(layout):
		subpixel_offsets = (-0.375, -0.125, 0.125, 0.375)
		candidates = [
			(px + subpixel_x, py + subpixel_y)
			for px, py in candidates
			for subpixel_y in subpixel_offsets
			for subpixel_x in subpixel_offsets
		]

	selected: list[tuple[float, float]] = []
	for _, (target_dx, target_dy), _ in layout:
		def score(point: tuple[float, float]) -> tuple[float, float]:
			dx = point[0] - base_px
			dy = point[1] - base_py
			ideal_distance = (dx - target_dx) ** 2 + (dy - target_dy) ** 2
			separation = min(
				((point[0] - other[0]) ** 2 + (point[1] - other[1]) ** 2 for other in selected),
				default=math.inf,
			)
			return ideal_distance, -separation

		chosen = min((point for point in candidates if point not in selected), key=score)
		selected.append(chosen)

	return selected


def main() -> None:
	args = parse_args()
	vanilla_buildings = args.vanilla_map / "buildings.txt"
	province_path = args.vanilla_map / "provinces.bmp"
	definition_path = args.vanilla_map / "definition.csv"

	if args.output.exists() and not args.force:
		raise FileExistsError(f"Refusing to overwrite {args.output}; pass --force")

	vanilla_lines = vanilla_buildings.read_text(encoding="utf-8-sig").splitlines()
	facility_rows = [line for line in vanilla_lines if ";special_project_facility_spawn;" in line]
	if not facility_rows:
		raise RuntimeError("Installed vanilla buildings.txt has no special-project facility spawn rows")

	land_colours = load_land_colours(definition_path)
	province_pixels = Image.open(province_path).convert("RGB")
	width, height = province_pixels.size
	custom_rows: list[str] = []
	counts = {spawn_type: 0 for spawn_type, _, _ in SPAWN_LAYOUT}
	facility_multipliers = Counter(spawn_type for spawn_type, _, _ in FACILITY_SPAWN_LAYOUT)
	camp_multipliers = Counter(spawn_type for spawn_type, _, _ in CAMP_SPAWN_LAYOUT)
	anchored_states: set[str] = set()

	for line in facility_rows:
		parts = line.split(";")
		if len(parts) != 7:
			raise RuntimeError(f"Unexpected buildings row: {line}")
		state_id, _, x_text, y_text, z_text, rotation_text, adjacent_sea = parts
		base_x = float(x_text)
		base_z = float(z_text)
		base_px = max(0, min(width - 1, round(base_x)))
		base_py = max(0, min(height - 1, height - 1 - round(base_z)))
		if province_pixels.getpixel((base_px, base_py)) not in land_colours:
			raise RuntimeError(f"Facility row does not resolve to a land province: {line}")

		layout = FACILITY_SPAWN_LAYOUT
		if state_id not in anchored_states:
			layout += CAMP_SPAWN_LAYOUT
			anchored_states.add(state_id)

		positions = select_positions(province_pixels, base_x, base_z, layout)
		base_rotation = float(rotation_text)
		for (spawn_type, _, rotation_offset), (px, py) in zip(layout, positions):
			x = float(px)
			z = float(height - 1 - py)
			rotation = ((base_rotation + rotation_offset + math.pi) % (2 * math.pi)) - math.pi
			custom_rows.append(
				f"{state_id};{spawn_type};{x:.2f};{y_text};{z:.2f};{rotation:.2f};{adjacent_sea}"
			)
			counts[spawn_type] += 1

	expected_counts = {
		**{spawn_type: len(facility_rows) * multiplier for spawn_type, multiplier in facility_multipliers.items()},
		**{spawn_type: len(anchored_states) * multiplier for spawn_type, multiplier in camp_multipliers.items()},
	}
	if any(counts[spawn_type] != expected for spawn_type, expected in expected_counts.items()):
		raise RuntimeError(f"Incomplete generated spawn coverage: {counts}")

	args.output.parent.mkdir(parents=True, exist_ok=True)
	with args.output.open("w", encoding="utf-8", newline="\n") as output_file:
		output_file.write("\n".join((*vanilla_lines, *STATIC_ROWS, *custom_rows)) + "\n")
	print(f"Preserved {len(vanilla_lines)} vanilla rows")
	print(f"Preserved {len(STATIC_ROWS)} Chaos Redux static showcase rows")
	print(
		f"Generated {len(custom_rows)} custom rows from {len(facility_rows)} facility anchors "
		f"and {len(anchored_states)} unique state anchors"
	)
	for spawn_type, count in counts.items():
		print(f"{spawn_type}: {count}")


if __name__ == "__main__":
	main()
