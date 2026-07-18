#!/usr/bin/env python3
"""Process and validate the generated raster tranche for Event 019."""

from __future__ import annotations

import hashlib
import math
import struct
import subprocess
import sys
import textwrap
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageOps


ROOT = Path(__file__).resolve().parents[4]
PACKAGE = ROOT / "docs" / "assets" / "019_infantry_spawn"
SOURCE = PACKAGE / "source_png"
PROCESSED = PACKAGE / "processed_png"
CONTACT = PACKAGE / "contact_sheets"
ANIMATIONS = PACKAGE / "animations"

REPORT_RUNTIME = ROOT / "gfx" / "event_pictures" / "019_infantry_spawn"
LEADER_RUNTIME = ROOT / "gfx" / "leaders" / "019_infantry_spawn"
UI_RUNTIME = ROOT / "gfx" / "interface" / "019_infantry_spawn"
ACHIEVEMENT_RUNTIME = ROOT / "gfx" / "achievements"
FOCUS_RUNTIME = ROOT / "gfx" / "interface" / "goals" / "019_infantry_spawn"
DECISION_RUNTIME = ROOT / "gfx" / "interface" / "decisions" / "019_infantry_spawn"
IDEA_RUNTIME = ROOT / "gfx" / "interface" / "ideas" / "019_infantry_spawn"
FLAG_RUNTIME = ROOT / "gfx" / "flags"

REPORT_PROCESSOR = ROOT / ".agents" / "skills" / "chaos-redux-event-assets" / "tools" / "process_report_event_image.py"
REPORT_PROCESSOR_SHA256 = "5b51613f391934960a8310268041c66b00fdd31bc12da2393eb02c8f3dc87bd9"
CHROMA_REMOVER = Path("C:/Users/klimp/.codex/skills/.system/imagegen/scripts/remove_chroma_key.py")
CONVERTER = ROOT / ".agents" / "skills" / "chaos-redux-event-assets" / "tools" / "convert_to_dds.py"
ACHIEVEMENT_OVERLAY = ROOT / ".agents" / "skills" / "chaos-redux-event-assets" / "assets" / "vanilla_reference" / "icons" / "achievements" / "overlay.png"

REPORT_STEMS = (
	"report_event_019_infantry_spawn_manifestation",
	"report_event_019_infantry_spawn_organized",
	"report_event_019_infantry_spawn_arsenal",
	"report_event_019_infantry_spawn_claimant",
	"report_event_019_infantry_spawn_anomalous",
	"report_event_019_infantry_spawn_zombie_release",
	"report_event_019_infantry_spawn_zombie_defeat",
	"report_event_019_infantry_spawn_ghost_release",
	"report_event_019_infantry_spawn_ghost_defeat",
	"report_event_019_infantry_spawn_golem_release",
	"report_event_019_infantry_spawn_golem_defeat",
)

CLAIMANT_STEMS = tuple(f"portrait_019_claimant_{index:02d}" for index in range(1, 21))
DERIVATIVE_STEMS = (
	"portrait_019_zombie_host_commander",
	"portrait_019_zombie_host_council",
	"portrait_019_ghost_host_commander",
	"portrait_019_ghost_host_council",
	"portrait_019_golem_master_builder",
	"portrait_019_golem_pattern_council",
)
TECHNICAL_STEMS = ("portrait_019_unassigned_muster",)
PORTRAIT_STEMS = CLAIMANT_STEMS + DERIVATIVE_STEMS + TECHNICAL_STEMS

ACHIEVEMENT_STEMS = (
	"019_infantry_spawn_every_rifle_accounted_for",
	"019_infantry_spawn_one_battalion_wonder",
	"019_infantry_spawn_the_army_has_voted",
	"019_infantry_spawn_order_from_noise",
	"019_infantry_spawn_combined_arms_accident",
	"019_infantry_spawn_no_room_on_the_train",
	"019_infantry_spawn_borrowed_future",
	"019_infantry_spawn_three_false_apocalypses",
	"019_infantry_spawn_barracks_of_babel",
	"019_infantry_spawn_quiet_demobilisation",
	"019_infantry_spawn_every_barracks_a_front",
)
ACHIEVEMENT_CONTACT_LABELS = {
	"019_infantry_spawn_every_rifle_accounted_for": "01 rifle_accounted",
	"019_infantry_spawn_one_battalion_wonder": "02 one_battalion",
	"019_infantry_spawn_the_army_has_voted": "03 army_voted",
	"019_infantry_spawn_order_from_noise": "04 order_from_noise",
	"019_infantry_spawn_combined_arms_accident": "05 combined_arms",
	"019_infantry_spawn_no_room_on_the_train": "06 train",
	"019_infantry_spawn_borrowed_future": "07 borrowed_future",
	"019_infantry_spawn_three_false_apocalypses": "08 false_apocalypses",
	"019_infantry_spawn_barracks_of_babel": "09 barracks_babel",
	"019_infantry_spawn_quiet_demobilisation": "10 demobilisation",
	"019_infantry_spawn_every_barracks_a_front": "11 barracks_front",
}

ANIMATION_SPECS = {
	"muster_seal_pulse": {"frames": 8, "size": (64, 64), "fps": 8, "atlas_grid": (4, 2)},
	"critical_command_border": {"frames": 8, "size": (156, 210), "fps": 6, "atlas_grid": (4, 2)},
	"anomalous_registry_emblem": {"frames": 10, "size": (64, 64), "fps": 5, "atlas_grid": (5, 2)},
}

FOCUS_ATLASES = (
	(
		"focus_atlas_a_foundation_source.png",
		(
			"infantry_spawn_derivative_hold_the_first_ground",
			"infantry_spawn_derivative_count_the_surviving_host",
			"infantry_spawn_derivative_inventory_the_seized_districts",
			"infantry_spawn_derivative_restore_a_chain_of_orders",
			"infantry_spawn_derivative_name_the_future_host",
			"infantry_spawn_derivative_mark_the_muster_depots",
			"infantry_spawn_derivative_reopen_captured_workshops",
			"infantry_spawn_derivative_open_the_living_corridor",
			"infantry_spawn_derivative_count_every_obligation",
		),
	),
	(
		"focus_atlas_b_hierarchy_source.png",
		(
			"infantry_spawn_derivative_crown_the_claimant",
			"infantry_spawn_derivative_assign_command_estates",
			"infantry_spawn_derivative_one_voice_over_the_host",
			"infantry_spawn_derivative_convene_the_host_council",
			"infantry_spawn_derivative_bind_the_district_councils",
			"infantry_spawn_derivative_no_host_abandoned",
			"infantry_spawn_derivative_obey_the_family_instinct",
			"infantry_spawn_derivative_mark_the_family_domain",
			"infantry_spawn_derivative_end_the_old_chain_of_rule",
		),
	),
	(
		"focus_atlas_c_army_expansion_source.png",
		(
			"infantry_spawn_derivative_quiet_the_fragmented_columns",
			"infantry_spawn_derivative_outlast_the_former_state",
			"infantry_spawn_derivative_make_an_army_of_the_host",
			"infantry_spawn_derivative_concentrate_the_host",
			"infantry_spawn_derivative_scatter_the_bands",
			"infantry_spawn_derivative_arm_the_captured_auxiliaries",
			"infantry_spawn_derivative_a_method_fit_for_the_host",
			"infantry_spawn_derivative_read_the_neighboring_frontiers",
			"infantry_spawn_derivative_issue_the_submission_terms",
		),
	),
	(
		"focus_atlas_d_predator_zombie_source.png",
		(
			"infantry_spawn_derivative_absorb_the_conquered_districts",
			"infantry_spawn_derivative_turn_the_host_outward",
			"infantry_spawn_derivative_become_the_regional_predator",
			"infantry_spawn_derivative_zombie_scavenge_the_abandoned_barracks",
			"infantry_spawn_derivative_zombie_number_the_devouring_bands",
			"infantry_spawn_derivative_zombie_teach_the_base_dead_to_muster",
			"infantry_spawn_derivative_zombie_keep_the_hunger_in_column",
			"infantry_spawn_derivative_zombie_a_realm_of_base_dead",
			"infantry_spawn_derivative_ghost_mark_the_first_anchors",
		),
	),
	(
		"focus_atlas_e_ghost_golem_source.png",
		(
			"infantry_spawn_derivative_ghost_call_a_second_procession",
			"infantry_spawn_derivative_ghost_bind_the_procession_to_place",
			"infantry_spawn_derivative_ghost_thin_the_hunger_for_life",
			"infantry_spawn_derivative_ghost_a_pale_dominion",
			"infantry_spawn_derivative_golem_recover_the_broken_coal",
			"infantry_spawn_derivative_golem_reconstruct_the_binding_marks",
			"infantry_spawn_derivative_golem_turn_workshops_into_foundries",
			"infantry_spawn_derivative_golem_share_the_living_pattern",
			"infantry_spawn_derivative_golem_a_march_of_living_stone",
		),
	),
)

DECISION_ATLASES = (
	(
		"decision_atlas_a_core_source.png",
		(
			"board_open",
			"lot_cycle",
			"audit",
			"territorial_roles",
			"standardization",
			"demobilization",
			"emergency_integration",
			"muster_district",
			"integration_staff",
		),
	),
	(
		"decision_atlas_b_requests_source.png",
		(
			"specialist_preservation",
			"emergency_reserve",
			"training_cycle",
			"rail_corridor",
			"request_field",
			"request_mobile",
			"request_territorial",
			"request_firepower",
			"request_numbers",
		),
	),
	(
		"decision_atlas_c_anomalous_claimant_source.png",
		(
			"request_discipline",
			"request_anything",
			"request_anomalous",
			"cantonment",
			"liaison",
			"restricted_deployment",
			"family_sustainment",
			"breach_sealing",
			"anomalous_disperse",
		),
	),
	(
		"decision_atlas_d_claimants_derivatives_source.png",
		(
			"claimant_recognize",
			"claimant_accept",
			"claimant_refuse",
			"claimant_counter_command",
			"claimant_discredit",
			"claimant_arrest",
			"derivative_zombie_training",
			"derivative_zombie_rally",
			"derivative_ghost_manifest",
		),
	),
	(
		"decision_atlas_e_derivative_ops_source.png",
		(
			"derivative_golem_bind",
			"derivative_sustainment_site",
			"derivative_integrate_district",
			"derivative_suppress_fragmentation",
			"derivative_break_command_net",
			"derivative_demand_submission",
			"derivative_preserve_claimant",
			"derivative_replace_claimant",
			"derivative_survive_front",
		),
	),
)

STANDALONE_DECISION_STEMS = (
	"prototype_preservation",
	"prototype_cannibalization",
)

IDEA_STEMS = (
	"muster_control",
	"army_congestion",
	"claimant_command",
	"anomalous_saturation",
	"supply_strain",
	"command_confusion",
	"training_saturation",
	"equipment_debt",
	"family_registry",
)

UI_STEMS = (
	"formation_management_category",
	"claimant_command_category",
	"derivative_operations_category",
	"formation_quality_marker",
	"formation_coherence_marker",
	"dynamic_cost_marker",
	"warning_marker",
	"cooldown_marker",
	"invalid_target_marker",
)

FLAG_ATLASES = (
	(
		"zombie_flags_atlas_source.png",
		(
			"INFANTRY_SPAWN_ZOMBIE_BASE",
			"INFANTRY_SPAWN_ZOMBIE_CLAIMANT",
			"INFANTRY_SPAWN_ZOMBIE_COLLECTIVE",
			"INFANTRY_SPAWN_ZOMBIE_SPECIES",
		),
	),
	(
		"ghost_flags_atlas_source.png",
		(
			"INFANTRY_SPAWN_GHOST_BASE",
			"INFANTRY_SPAWN_GHOST_CLAIMANT",
			"INFANTRY_SPAWN_GHOST_COLLECTIVE",
			"INFANTRY_SPAWN_GHOST_SPECIES",
		),
	),
	(
		"golem_flags_atlas_source.png",
		(
			"INFANTRY_SPAWN_GOLEM_BASE",
			"INFANTRY_SPAWN_GOLEM_CLAIMANT",
			"INFANTRY_SPAWN_GOLEM_COLLECTIVE",
			"INFANTRY_SPAWN_GOLEM_SPECIES",
		),
	),
)

CLAIMANT_FLAG_TAG = "INFANTRY_SPAWN_CLAIMANT_BREAKAWAY"
FLAG_TAGS = (CLAIMANT_FLAG_TAG,) + tuple(tag for _, tags in FLAG_ATLASES for tag in tags)
FLAG_SIZES = {"normal": (82, 52), "medium": (41, 26), "small": (10, 7)}


def sha256(path: Path) -> str:
	return hashlib.sha256(path.read_bytes()).hexdigest()


def ensure_prerequisites() -> None:
	if not REPORT_PROCESSOR.is_file() or sha256(REPORT_PROCESSOR) != REPORT_PROCESSOR_SHA256:
		raise RuntimeError("Verified report-card processor is missing or changed")
	if not CHROMA_REMOVER.is_file():
		raise RuntimeError(f"Official imagegen chroma remover is missing: {CHROMA_REMOVER}")
	if not CONVERTER.is_file():
		raise RuntimeError(f"Repository DDS converter is missing: {CONVERTER}")
	if not ACHIEVEMENT_OVERLAY.is_file():
		raise RuntimeError(f"Achievement not-eligible overlay is missing: {ACHIEVEMENT_OVERLAY}")


def ensure_dirs() -> None:
	for path in (
		PROCESSED / "report",
		PROCESSED / "portraits" / "claimants",
		PROCESSED / "portraits" / "derivatives",
		PROCESSED / "portraits" / "technical",
		PROCESSED / "achievements",
		PROCESSED / "focuses",
		PROCESSED / "decisions",
		PROCESSED / "ideas",
		PROCESSED / "ui",
		PROCESSED / "gui",
		PROCESSED / "flags",
		SOURCE / "focuses" / "split_sources",
		SOURCE / "decisions" / "split_sources",
		SOURCE / "ideas" / "split_sources",
		SOURCE / "ui" / "split_sources",
		SOURCE / "flags" / "split_sources",
		CONTACT,
		REPORT_RUNTIME,
		LEADER_RUNTIME,
		UI_RUNTIME,
		ACHIEVEMENT_RUNTIME,
		FOCUS_RUNTIME,
		DECISION_RUNTIME,
		IDEA_RUNTIME,
		FLAG_RUNTIME,
		FLAG_RUNTIME / "medium",
		FLAG_RUNTIME / "small",
	):
		path.mkdir(parents=True, exist_ok=True)
	for slug in ANIMATION_SPECS:
		for child in ("keyed_frames", "processed_frames", "sheets", "previews"):
			(ANIMATIONS / slug / child).mkdir(parents=True, exist_ok=True)


def cover_crop(image: Image.Image, target_size: tuple[int, int]) -> Image.Image:
	target_width, target_height = target_size
	scale = max(target_width / image.width, target_height / image.height)
	resized = image.resize(
		(int(round(image.width * scale)), int(round(image.height * scale))),
		Image.Resampling.LANCZOS,
	)
	left = (resized.width - target_width) // 2
	top = (resized.height - target_height) // 2
	return resized.crop((left, top, left + target_width, top + target_height))


def process_reports() -> None:
	for index, stem in enumerate(REPORT_STEMS):
		source = SOURCE / "report" / f"{stem}_source.png"
		output = PROCESSED / "report" / f"{stem}.png"
		command = [
			sys.executable,
			str(REPORT_PROCESSOR),
			str(source),
			str(output),
			"--canvas-size", "210x176",
			"--card-size", "192x153",
			"--border", "0",
			"--angle", "4.0",
			"--shadow-offset", "4", "5",
			"--shadow-blur", "4.5",
			"--shadow-opacity", "0.50",
			"--grain", "7",
			"--paper-grain", "0",
			"--seed", str(19001 + index),
			"--rotate-supersample", "4",
			"--edge-soften", "0.35",
		]
		subprocess.run(command, cwd=ROOT, check=True)


def portrait_treatment(source: Path) -> Image.Image:
	image = Image.open(source).convert("RGB")
	image = cover_crop(image, (156, 210))
	image = ImageEnhance.Contrast(image).enhance(1.04)
	image = ImageEnhance.Color(image).enhance(0.90)
	image = ImageEnhance.Sharpness(image).enhance(1.04)
	return image


def process_portraits() -> None:
	for stem in CLAIMANT_STEMS:
		portrait_treatment(SOURCE / "portraits" / "claimants" / f"{stem}_source.png").save(
			PROCESSED / "portraits" / "claimants" / f"{stem}.png"
		)
	for stem in DERIVATIVE_STEMS:
		portrait_treatment(SOURCE / "portraits" / "derivatives" / f"{stem}_source.png").save(
			PROCESSED / "portraits" / "derivatives" / f"{stem}.png"
		)
	for stem in TECHNICAL_STEMS:
		portrait_treatment(SOURCE / "portraits" / "technical" / f"{stem}_source.png").save(
			PROCESSED / "portraits" / "technical" / f"{stem}.png"
		)


def process_achievements() -> None:
	overlay = Image.open(ACHIEVEMENT_OVERLAY).convert("RGBA")
	for stem in ACHIEVEMENT_STEMS:
		source = Image.open(SOURCE / "achievements" / f"{stem}_source.png").convert("RGBA")
		completed = ImageOps.fit(source, (64, 64), method=Image.Resampling.LANCZOS)
		grey_channel = ImageOps.grayscale(completed.convert("RGB"))
		grey = Image.merge("RGBA", (grey_channel, grey_channel, grey_channel, completed.getchannel("A")))
		not_eligible = grey.copy()
		not_eligible.alpha_composite(overlay)
		completed.save(PROCESSED / "achievements" / f"{stem}.png")
		grey.save(PROCESSED / "achievements" / f"{stem}_grey.png")
		not_eligible.save(PROCESSED / "achievements" / f"{stem}_not_eligible.png")


def remove_chroma(source: Path, output: Path) -> None:
	command = [
		sys.executable,
		str(CHROMA_REMOVER),
		"--input", str(source),
		"--out", str(output),
		"--auto-key", "border",
		"--soft-matte",
		"--transparent-threshold", "12",
		"--opaque-threshold", "220",
		"--despill",
		"--edge-contract", "1",
		"--force",
	]
	subprocess.run(command, cwd=ROOT, check=True)


def normalize_alpha_subject(image: Image.Image, target: tuple[int, int], padding: int) -> Image.Image:
	image = image.convert("RGBA")
	bbox = image.getchannel("A").getbbox()
	if bbox is None:
		raise RuntimeError("Chroma removal produced an empty frame")
	subject = image.crop(bbox)
	available_width = target[0] - (padding * 2)
	available_height = target[1] - (padding * 2)
	scale = min(available_width / subject.width, available_height / subject.height)
	subject = subject.resize(
		(max(1, int(round(subject.width * scale))), max(1, int(round(subject.height * scale)))),
		Image.Resampling.LANCZOS,
	)
	canvas = Image.new("RGBA", target, (0, 0, 0, 0))
	x = (target[0] - subject.width) // 2
	y = (target[1] - subject.height) // 2
	canvas.alpha_composite(subject, (x, y))
	return canvas


def normalize_alpha_sequence(
	images: list[Image.Image],
	target: tuple[int, int],
	padding: int,
) -> list[Image.Image]:
	converted = [image.convert("RGBA") for image in images]
	bounds = [image.getchannel("A").getbbox() for image in converted]
	if any(bound is None for bound in bounds):
		raise RuntimeError("Chroma removal produced an empty animation frame")
	valid_bounds = [bound for bound in bounds if bound is not None]
	maximum_width = max(right - left for left, top, right, bottom in valid_bounds)
	maximum_height = max(bottom - top for left, top, right, bottom in valid_bounds)
	available_width = target[0] - (padding * 2)
	available_height = target[1] - (padding * 2)
	shared_scale = min(available_width / maximum_width, available_height / maximum_height)
	frames: list[Image.Image] = []
	for image, bound in zip(converted, valid_bounds):
		subject = image.crop(bound)
		subject = subject.resize(
			(
				max(1, int(round(subject.width * shared_scale))),
				max(1, int(round(subject.height * shared_scale))),
			),
			Image.Resampling.LANCZOS,
		)
		canvas = Image.new("RGBA", target, (0, 0, 0, 0))
		x = (target[0] - subject.width) // 2
		y = (target[1] - subject.height) // 2
		canvas.alpha_composite(subject, (x, y))
		canvas.putdata(
			[(0, 0, 0, 0) if alpha <= 5 else (red, green, blue, alpha) for red, green, blue, alpha in canvas.getdata()]
		)
		frames.append(canvas)
	return frames


def keep_largest_alpha_component(image: Image.Image, threshold: int = 12) -> Image.Image:
	image = image.convert("RGBA")
	alpha = image.getchannel("A")
	width, height = image.size
	opaque = bytearray(1 if value > threshold else 0 for value in alpha.getdata())
	visited = bytearray(width * height)
	largest: list[int] = []
	for start, is_opaque in enumerate(opaque):
		if not is_opaque or visited[start]:
			continue
		visited[start] = 1
		stack = [start]
		component: list[int] = []
		while stack:
			pixel = stack.pop()
			component.append(pixel)
			x = pixel % width
			y = pixel // width
			neighbors = []
			if x:
				neighbors.append(pixel - 1)
			if x + 1 < width:
				neighbors.append(pixel + 1)
			if y:
				neighbors.append(pixel - width)
			if y + 1 < height:
				neighbors.append(pixel + width)
			for neighbor in neighbors:
				if opaque[neighbor] and not visited[neighbor]:
					visited[neighbor] = 1
					stack.append(neighbor)
		if len(component) > len(largest):
			largest = component
	if not largest:
		raise RuntimeError("Animation frame has no opaque subject component")
	keep = bytearray(width * height)
	for pixel in largest:
		keep[pixel] = 255
	keep_mask = Image.frombytes("L", image.size, bytes(keep))
	image.putalpha(ImageChops.multiply(alpha, keep_mask))
	return image


def split_grid(image: Image.Image, columns: int, rows: int) -> list[Image.Image]:
	cells: list[Image.Image] = []
	for row in range(rows):
		for column in range(columns):
			left = round(column * image.width / columns)
			top = round(row * image.height / rows)
			right = round((column + 1) * image.width / columns)
			bottom = round((row + 1) * image.height / rows)
			cells.append(image.crop((left, top, right, bottom)))
	return cells


def split_animation_source_atlases() -> None:
	for slug, spec in ANIMATION_SPECS.items():
		animation = ANIMATIONS / slug
		atlas = Image.open(
			animation / "source_atlas" / f"{slug}_animation_source_atlas.png"
		).convert("RGB")
		columns, rows = spec["atlas_grid"]
		cells = split_grid(atlas, columns, rows)
		if len(cells) != spec["frames"]:
			raise RuntimeError(f"Animation atlas mapping mismatch: {slug}")
		for index, cell in enumerate(cells):
			cell.save(animation / "source_frames" / f"{slug}_{index:03d}_source.png")


def process_icon_atlas(
	atlas: Path,
	stems: tuple[str, ...],
	source_split_dir: Path,
	processed_dir: Path,
	target: tuple[int, int],
	padding: int,
) -> None:
	image = Image.open(atlas).convert("RGB")
	cells = split_grid(image, 3, 3)
	if len(cells) != len(stems):
		raise RuntimeError(f"Atlas mapping mismatch: {atlas}")
	keyed_dir = processed_dir / "keyed"
	keyed_dir.mkdir(parents=True, exist_ok=True)
	for stem, cell in zip(stems, cells):
		source = source_split_dir / f"{stem}_source.png"
		keyed = keyed_dir / f"{stem}_keyed.png"
		output = processed_dir / f"{stem}.png"
		cell.save(source)
		remove_chroma(source, keyed)
		normalize_alpha_subject(Image.open(keyed), target, padding).save(output)


def process_icons() -> None:
	for atlas_name, stems in FOCUS_ATLASES:
		process_icon_atlas(
			SOURCE / "focuses" / atlas_name,
			stems,
			SOURCE / "focuses" / "split_sources",
			PROCESSED / "focuses",
			(100, 88),
			2,
		)
	for atlas_name, stems in DECISION_ATLASES:
		process_icon_atlas(
			SOURCE / "decisions" / atlas_name,
			stems,
			SOURCE / "decisions" / "split_sources",
			PROCESSED / "decisions",
			(33, 32),
			1,
		)
	for stem in STANDALONE_DECISION_STEMS:
		source = SOURCE / "decisions" / f"{stem}_source.png"
		keyed = PROCESSED / "decisions" / "keyed" / f"{stem}_keyed.png"
		output = PROCESSED / "decisions" / f"{stem}.png"
		remove_chroma(source, keyed)
		normalize_alpha_subject(Image.open(keyed), (33, 32), 1).save(output)
	process_icon_atlas(
		SOURCE / "ideas" / "idea_ui_atlas_source.png",
		IDEA_STEMS,
		SOURCE / "ideas" / "split_sources",
		PROCESSED / "ideas",
		(64, 64),
		2,
	)
	process_icon_atlas(
		SOURCE / "ui" / "decision_category_ui_atlas_source.png",
		UI_STEMS,
		SOURCE / "ui" / "split_sources",
		PROCESSED / "ui" / "source_sized",
		(64, 64),
		2,
	)
	for index, stem in enumerate(UI_STEMS):
		source = PROCESSED / "ui" / "source_sized" / f"{stem}.png"
		target = (50, 40) if index < 3 else (32, 32)
		padding = 0 if index < 3 else 1
		normalize_alpha_subject(Image.open(source), target, padding).save(PROCESSED / "ui" / f"{stem}.png")


def process_gui_background() -> None:
	source = Image.open(SOURCE / "gui" / "infantry_spawn_muster_board_background_source.png").convert("RGBA")
	background = ImageOps.fit(source, (1120, 760), method=Image.Resampling.LANCZOS)
	background.save(PROCESSED / "gui" / "infantry_spawn_muster_board_background.png")


def extract_flag_rectangle(source: Path, keyed: Path) -> Image.Image:
	remove_chroma(source, keyed)
	keyed_image = Image.open(keyed).convert("RGBA")
	thresholded = keyed_image.getchannel("A").point(lambda value: 255 if value > 220 else 0)
	bbox = thresholded.getbbox()
	if bbox is None:
		raise RuntimeError(f"Flag chroma removal produced no opaque rectangle: {source}")
	left, top, right, bottom = bbox
	if right - left < 32 or bottom - top < 20:
		raise RuntimeError(f"Flag rectangle is unexpectedly small: {source} -> {bbox}")
	flag = Image.open(source).convert("RGBA").crop((left, top, right, bottom))

	def key_green(pixel: tuple[int, int, int, int]) -> bool:
		red, green, blue, _ = pixel
		return green > 140 and green > red * 1.45 and green > blue * 1.45

	def column_is_key_green(x: int) -> bool:
		return sum(key_green(flag.getpixel((x, y))) for y in range(flag.height)) / flag.height > 0.35

	def row_is_key_green(y: int) -> bool:
		return sum(key_green(flag.getpixel((x, y))) for x in range(flag.width)) / flag.width > 0.35

	trim_left = 0
	trim_top = 0
	trim_right = flag.width
	trim_bottom = flag.height
	while trim_left < trim_right - 32 and column_is_key_green(trim_left):
		trim_left += 1
	while trim_right > trim_left + 32 and column_is_key_green(trim_right - 1):
		trim_right -= 1
	while trim_top < trim_bottom - 20 and row_is_key_green(trim_top):
		trim_top += 1
	while trim_bottom > trim_top + 20 and row_is_key_green(trim_bottom - 1):
		trim_bottom -= 1
	outer_columns = max(1, flag.width // 10)
	outer_rows = max(1, flag.height // 10)
	left_gutter = [x for x in range(outer_columns) if column_is_key_green(x)]
	right_gutter = [x for x in range(flag.width - outer_columns, flag.width) if column_is_key_green(x)]
	top_gutter = [y for y in range(outer_rows) if row_is_key_green(y)]
	bottom_gutter = [y for y in range(flag.height - outer_rows, flag.height) if row_is_key_green(y)]
	if left_gutter:
		trim_left = max(trim_left, max(left_gutter) + 1)
	if right_gutter:
		trim_right = min(trim_right, min(right_gutter))
	if top_gutter:
		trim_top = max(trim_top, max(top_gutter) + 1)
	if bottom_gutter:
		trim_bottom = min(trim_bottom, min(bottom_gutter))
	if trim_right - trim_left < 32 or trim_bottom - trim_top < 20:
		raise RuntimeError(f"Flag gutter trim removed too much artwork: {source}")
	return flag.crop((trim_left, trim_top, trim_right, trim_bottom))


def save_tga(image: Image.Image, output: Path) -> None:
	image.convert("RGBA").save(output, format="TGA", compression=None)


def process_flags() -> None:
	split_dir = SOURCE / "flags" / "split_sources"
	keyed_dir = PROCESSED / "flags" / "keyed"
	keyed_dir.mkdir(parents=True, exist_ok=True)
	for atlas_name, tags in FLAG_ATLASES:
		atlas = Image.open(SOURCE / "flags" / atlas_name).convert("RGB")
		for tag, cell in zip(tags, split_grid(atlas, 2, 2)):
			source = split_dir / f"{tag}_source.png"
			keyed = keyed_dir / f"{tag}_keyed.png"
			cell.save(source)
			flag = extract_flag_rectangle(source, keyed)
			normal = ImageOps.fit(flag, FLAG_SIZES["normal"], method=Image.Resampling.LANCZOS)
			normal.save(PROCESSED / "flags" / f"{tag}.png")
	claimant_keyed = keyed_dir / f"{CLAIMANT_FLAG_TAG}_keyed.png"
	claimant = extract_flag_rectangle(SOURCE / "flags" / "claimant_flag_source.png", claimant_keyed)
	ImageOps.fit(claimant, FLAG_SIZES["normal"], method=Image.Resampling.LANCZOS).save(
		PROCESSED / "flags" / f"{CLAIMANT_FLAG_TAG}.png"
	)
	for tag in FLAG_TAGS:
		normal = Image.open(PROCESSED / "flags" / f"{tag}.png").convert("RGBA")
		for size_name, size in FLAG_SIZES.items():
			resized = normal if size_name == "normal" else normal.resize(size, Image.Resampling.LANCZOS)
			processed = PROCESSED / "flags" / f"{tag}_{size_name}.png"
			resized.save(processed)
			runtime_dir = FLAG_RUNTIME if size_name == "normal" else FLAG_RUNTIME / size_name
			save_tga(resized, runtime_dir / f"{tag}.tga")


def process_animations() -> None:
	split_animation_source_atlases()
	for slug, spec in ANIMATION_SPECS.items():
		animation = ANIMATIONS / slug
		keyed_frames: list[Image.Image] = []
		for index in range(spec["frames"]):
			source = animation / "source_frames" / f"{slug}_{index:03d}_source.png"
			keyed = animation / "keyed_frames" / f"{slug}_{index:03d}_keyed.png"
			remove_chroma(source, keyed)
			cleaned = keep_largest_alpha_component(Image.open(keyed))
			cleaned.save(keyed)
			keyed_frames.append(cleaned)
		padding = 1 if slug == "critical_command_border" else 3
		frames = normalize_alpha_sequence(keyed_frames, spec["size"], padding)
		for index, frame in enumerate(frames):
			processed = animation / "processed_frames" / f"{slug}_{index:03d}.png"
			frame.save(processed)

		sheet = Image.new("RGBA", (spec["size"][0] * spec["frames"], spec["size"][1]), (0, 0, 0, 0))
		for index, frame in enumerate(frames):
			sheet.alpha_composite(frame, (index * spec["size"][0], 0))
		sheet.save(animation / "sheets" / f"{slug}_sheet.png")
		frames[0].save(animation / "sheets" / f"{slug}_static.png")
		frames[0].save(
			animation / "previews" / f"{slug}_preview.gif",
			save_all=True,
			append_images=frames[1:],
			duration=int(round(1000 / spec["fps"])),
			loop=0,
			disposal=2,
		)


def checker_preview(image: Image.Image) -> Image.Image:
	image = image.convert("RGBA")
	checker = Image.new("RGB", image.size, (54, 54, 54))
	draw = ImageDraw.Draw(checker)
	cell = 8
	for y in range(0, image.height, cell):
		for x in range(0, image.width, cell):
			if ((x // cell) + (y // cell)) % 2:
				draw.rectangle((x, y, x + cell - 1, y + cell - 1), fill=(94, 94, 94))
	checker.paste(image, mask=image.getchannel("A"))
	return checker


def make_contact_sheet(
	items: list[tuple[str, Path]],
	output: Path,
	columns: int,
	preview_size: tuple[int, int],
	checker: bool = False,
	upscale: bool = False,
	label_wrap: int = 0,
	minimum_cell_width: int = 0,
) -> None:
	rows = math.ceil(len(items) / columns)
	cell_width = max(preview_size[0] + 24, minimum_cell_width)
	cell_height = preview_size[1] + 48
	sheet = Image.new("RGB", (columns * cell_width, rows * cell_height), (24, 24, 24))
	draw = ImageDraw.Draw(sheet)
	for index, (label, path) in enumerate(items):
		image = Image.open(path).convert("RGBA")
		if upscale:
			image = ImageOps.contain(image, preview_size, Image.Resampling.LANCZOS)
		else:
			image.thumbnail(preview_size, Image.Resampling.LANCZOS)
		if checker:
			preview = checker_preview(image)
		else:
			preview = Image.new("RGB", image.size, (18, 18, 18))
			preview.paste(image, mask=image.getchannel("A"))
		x0 = (index % columns) * cell_width + (cell_width - preview.width) // 2
		y0 = (index // columns) * cell_height + 8
		sheet.paste(preview, (x0, y0))
		if label_wrap:
			label = "\n".join(textwrap.wrap(label, width=label_wrap))
		draw.multiline_text(((index % columns) * cell_width + 8, y0 + preview.height + 8), label, fill=(235, 235, 235), spacing=2)
	output.parent.mkdir(parents=True, exist_ok=True)
	sheet.save(output)


def make_contacts() -> None:
	make_contact_sheet(
		[(stem, SOURCE / "report" / f"{stem}_source.png") for stem in REPORT_STEMS],
		CONTACT / "event_019_report_source_contact_sheet.png",
		columns=3,
		preview_size=(384, 256),
	)
	make_contact_sheet(
		[(stem, PROCESSED / "report" / f"{stem}.png") for stem in REPORT_STEMS],
		CONTACT / "event_019_report_processed_contact_sheet.png",
		columns=4,
		preview_size=(315, 264),
		checker=True,
	)
	make_contact_sheet(
		[(stem, SOURCE / "portraits" / "claimants" / f"{stem}_source.png") for stem in CLAIMANT_STEMS],
		CONTACT / "event_019_claimant_source_contact_sheet.png",
		columns=5,
		preview_size=(234, 315),
	)
	make_contact_sheet(
		[(stem, PROCESSED / "portraits" / "claimants" / f"{stem}.png") for stem in CLAIMANT_STEMS],
		CONTACT / "event_019_claimant_processed_contact_sheet.png",
		columns=5,
		preview_size=(156, 210),
	)
	make_contact_sheet(
		[(stem, PROCESSED / "portraits" / "derivatives" / f"{stem}.png") for stem in DERIVATIVE_STEMS],
		CONTACT / "event_019_derivative_portrait_contact_sheet.png",
		columns=3,
		preview_size=(234, 315),
	)
	make_contact_sheet(
		[(stem, SOURCE / "portraits" / "technical" / f"{stem}_source.png") for stem in TECHNICAL_STEMS],
		CONTACT / "event_019_unassigned_muster_source_contact_sheet.png",
		columns=1,
		preview_size=(468, 630),
	)
	make_contact_sheet(
		[(stem, PROCESSED / "portraits" / "technical" / f"{stem}.png") for stem in TECHNICAL_STEMS],
		CONTACT / "event_019_unassigned_muster_processed_contact_sheet.png",
		columns=1,
		preview_size=(312, 420),
		upscale=True,
	)
	make_contact_sheet(
		[(ACHIEVEMENT_CONTACT_LABELS[stem], PROCESSED / "achievements" / f"{stem}.png") for stem in ACHIEVEMENT_STEMS],
		CONTACT / "event_019_achievement_completed_contact_sheet.png",
		columns=3,
		preview_size=(128, 128),
		upscale=True,
		label_wrap=24,
		minimum_cell_width=240,
	)
	make_contact_sheet(
		[
			(f"{ACHIEVEMENT_CONTACT_LABELS[stem]} [not eligible]", PROCESSED / "achievements" / f"{stem}_not_eligible.png")
			for stem in ACHIEVEMENT_STEMS
		],
		CONTACT / "event_019_achievement_not_eligible_contact_sheet.png",
		columns=3,
		preview_size=(128, 128),
		upscale=True,
		label_wrap=24,
		minimum_cell_width=240,
	)
	focus_stems = [stem for _, stems in FOCUS_ATLASES for stem in stems]
	make_contact_sheet(
		[(stem.removeprefix("infantry_spawn_derivative_"), PROCESSED / "focuses" / f"{stem}.png") for stem in focus_stems],
		CONTACT / "event_019_focus_icon_contact_sheet.png",
		columns=5,
		preview_size=(150, 132),
		checker=True,
		upscale=True,
		label_wrap=24,
		minimum_cell_width=190,
	)
	decision_stems = [stem for _, stems in DECISION_ATLASES for stem in stems] + list(STANDALONE_DECISION_STEMS)
	make_contact_sheet(
		[(stem, PROCESSED / "decisions" / f"{stem}.png") for stem in decision_stems],
		CONTACT / "event_019_decision_icon_contact_sheet.png",
		columns=5,
		preview_size=(99, 96),
		checker=True,
		upscale=True,
		label_wrap=23,
		minimum_cell_width=180,
	)
	make_contact_sheet(
		[(stem, PROCESSED / "ideas" / f"{stem}.png") for stem in IDEA_STEMS],
		CONTACT / "event_019_idea_icon_contact_sheet.png",
		columns=3,
		preview_size=(128, 128),
		checker=True,
		upscale=True,
		label_wrap=24,
		minimum_cell_width=220,
	)
	make_contact_sheet(
		[(stem, PROCESSED / "ui" / f"{stem}.png") for stem in UI_STEMS],
		CONTACT / "event_019_ui_icon_contact_sheet.png",
		columns=3,
		preview_size=(128, 96),
		checker=True,
		upscale=True,
		label_wrap=24,
		minimum_cell_width=220,
	)
	make_contact_sheet(
		[(tag.removeprefix("INFANTRY_SPAWN_"), PROCESSED / "flags" / f"{tag}.png") for tag in FLAG_TAGS],
		CONTACT / "event_019_flag_contact_sheet.png",
		columns=4,
		preview_size=(246, 156),
		upscale=True,
		label_wrap=26,
		minimum_cell_width=290,
	)
	make_contact_sheet(
		[("muster_board_background", PROCESSED / "gui" / "infantry_spawn_muster_board_background.png")],
		CONTACT / "event_019_gui_background_contact_sheet.png",
		columns=1,
		preview_size=(560, 380),
		minimum_cell_width=600,
	)
	for slug, spec in ANIMATION_SPECS.items():
		items = [
			(f"{slug}_{index:03d}", ANIMATIONS / slug / "processed_frames" / f"{slug}_{index:03d}.png")
			for index in range(spec["frames"])
		]
		make_contact_sheet(
			items,
			ANIMATIONS / slug / "previews" / f"{slug}_contact.png",
			columns=5 if spec["frames"] == 10 else 4,
			preview_size=spec["size"],
			checker=True,
		)


def convert_dds(source: Path, output: Path, size: tuple[int, int]) -> None:
	command = [
		sys.executable,
		str(CONVERTER),
		"--input", str(source),
		"--output", str(output),
		"--width", str(size[0]),
		"--height", str(size[1]),
	]
	subprocess.run(command, cwd=ROOT, check=True)


def convert_all() -> None:
	for stem in REPORT_STEMS:
		convert_dds(PROCESSED / "report" / f"{stem}.png", REPORT_RUNTIME / f"{stem}.dds", (210, 176))
	for stem in CLAIMANT_STEMS:
		convert_dds(
			PROCESSED / "portraits" / "claimants" / f"{stem}.png",
			LEADER_RUNTIME / f"{stem}.dds",
			(156, 210),
		)
	for stem in DERIVATIVE_STEMS:
		convert_dds(
			PROCESSED / "portraits" / "derivatives" / f"{stem}.png",
			LEADER_RUNTIME / f"{stem}.dds",
			(156, 210),
		)
	for stem in TECHNICAL_STEMS:
		convert_dds(
			PROCESSED / "portraits" / "technical" / f"{stem}.png",
			LEADER_RUNTIME / f"{stem}.dds",
			(156, 210),
		)
	for slug, spec in ANIMATION_SPECS.items():
		convert_dds(
			ANIMATIONS / slug / "sheets" / f"{slug}_sheet.png",
			UI_RUNTIME / f"{slug}_sheet.dds",
			(spec["size"][0] * spec["frames"], spec["size"][1]),
		)
		convert_dds(
			ANIMATIONS / slug / "sheets" / f"{slug}_static.png",
			UI_RUNTIME / f"{slug}_static.dds",
			spec["size"],
		)
	for stem in ACHIEVEMENT_STEMS:
		for suffix in ("", "_grey", "_not_eligible"):
			convert_dds(
				PROCESSED / "achievements" / f"{stem}{suffix}.png",
				ACHIEVEMENT_RUNTIME / f"{stem}{suffix}.dds",
				(64, 64),
			)
	for _, stems in FOCUS_ATLASES:
		for stem in stems:
			convert_dds(PROCESSED / "focuses" / f"{stem}.png", FOCUS_RUNTIME / f"{stem}.dds", (100, 88))
	for _, stems in DECISION_ATLASES:
		for stem in stems:
			convert_dds(PROCESSED / "decisions" / f"{stem}.png", DECISION_RUNTIME / f"{stem}.dds", (33, 32))
	for stem in STANDALONE_DECISION_STEMS:
		convert_dds(PROCESSED / "decisions" / f"{stem}.png", DECISION_RUNTIME / f"{stem}.dds", (33, 32))
	for stem in IDEA_STEMS:
		convert_dds(PROCESSED / "ideas" / f"{stem}.png", IDEA_RUNTIME / f"infantry_spawn_{stem}.dds", (64, 64))
	for index, stem in enumerate(UI_STEMS):
		size = (50, 40) if index < 3 else (32, 32)
		convert_dds(PROCESSED / "ui" / f"{stem}.png", UI_RUNTIME / f"{stem}.dds", size)
	convert_dds(
		PROCESSED / "gui" / "infantry_spawn_muster_board_background.png",
		UI_RUNTIME / "infantry_spawn_muster_board_background.dds",
		(1120, 760),
	)


def parse_dds(path: Path) -> tuple[int, int, int, int, int, tuple[int, int, int, int], int]:
	data = path.read_bytes()
	if len(data) < 128 or data[:4] != b"DDS ":
		raise RuntimeError(f"Invalid DDS header: {path}")
	values = struct.unpack("<31I", data[4:128])
	return (
		values[3],
		values[2],
		values[6],
		values[19],
		values[21],
		(values[22], values[23], values[24], values[25]),
		len(data),
	)


def validate_dds_pair(png: Path, dds: Path, expected: tuple[int, int]) -> None:
	image = Image.open(png).convert("RGBA")
	if image.size != expected:
		raise RuntimeError(f"Wrong PNG size: {png} -> {image.size}; expected {expected}")
	width, height, mip_count, pixel_flags, bits, masks, file_length = parse_dds(dds)
	if (width, height) != expected:
		raise RuntimeError(f"Wrong DDS size: {dds} -> {(width, height)}; expected {expected}")
	if mip_count not in (0, 1):
		raise RuntimeError(f"Unexpected DDS mip count: {dds} -> {mip_count}")
	if pixel_flags != 65 or bits != 32:
		raise RuntimeError(f"Unexpected DDS pixel format: {dds} -> flags={pixel_flags}, bits={bits}")
	if masks != (0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000):
		raise RuntimeError(f"Unexpected DDS masks: {dds} -> {masks}")
	if file_length != 128 + expected[0] * expected[1] * 4:
		raise RuntimeError(f"Unexpected DDS file length: {dds} -> {file_length}")
	dds_image = Image.open(dds).convert("RGBA")
	if ImageChops.difference(image, dds_image).getbbox() is not None:
		raise RuntimeError(f"DDS pixels differ from processed PNG: {dds}")


def validate_transparent_dds_pair(png: Path, dds: Path, expected: tuple[int, int]) -> None:
	validate_dds_pair(png, dds, expected)
	alpha = Image.open(png).convert("RGBA").getchannel("A")
	minimum, maximum = alpha.getextrema()
	if minimum != 0 or maximum == 0:
		raise RuntimeError(f"Icon lacks useful transparency: {png} -> {(minimum, maximum)}")


def parse_tga(path: Path) -> tuple[int, int, int, int, int, int]:
	data = path.read_bytes()
	if len(data) < 18:
		raise RuntimeError(f"Invalid TGA header: {path}")
	fields = struct.unpack("<BBBHHBHHHHBB", data[:18])
	return fields[2], fields[8], fields[9], fields[10], fields[11], len(data)


def validate_tga_pair(png: Path, tga: Path, expected: tuple[int, int]) -> None:
	image = Image.open(png).convert("RGBA")
	if image.size != expected:
		raise RuntimeError(f"Wrong processed flag size: {png} -> {image.size}; expected {expected}")
	image_type, width, height, depth, descriptor, file_length = parse_tga(tga)
	if image_type != 2:
		raise RuntimeError(f"Flag TGA is not uncompressed true-colour: {tga} -> type {image_type}")
	if (width, height) != expected or depth != 32:
		raise RuntimeError(f"Wrong TGA format: {tga} -> {(width, height, depth)}; expected {expected}x32")
	if descriptor & 0x20:
		raise RuntimeError(f"Flag TGA is top-origin rather than bottom-origin: {tga} -> descriptor {descriptor}")
	if descriptor & 0x0F != 8:
		raise RuntimeError(f"Flag TGA does not declare eight alpha bits: {tga} -> descriptor {descriptor}")
	if file_length < 18 + expected[0] * expected[1] * 4:
		raise RuntimeError(f"Flag TGA pixel payload is truncated: {tga} -> {file_length}")
	tga_image = Image.open(tga).convert("RGBA")
	if ImageChops.difference(image, tga_image).getbbox() is not None:
		raise RuntimeError(f"TGA pixels differ from processed PNG: {tga}")
	border = (
		[image.getpixel((x, 0)) for x in range(image.width)]
		+ [image.getpixel((x, image.height - 1)) for x in range(image.width)]
		+ [image.getpixel((0, y)) for y in range(image.height)]
		+ [image.getpixel((image.width - 1, y)) for y in range(image.height)]
	)
	key_green_count = sum(
		green > 140 and green > red * 1.45 and green > blue * 1.45
		for red, green, blue, _ in border
	)
	if key_green_count / len(border) > 0.01:
		raise RuntimeError(f"Flag retains chroma green along its border: {png} -> {key_green_count}/{len(border)}")


def validate() -> None:
	for stem in REPORT_STEMS:
		png = PROCESSED / "report" / f"{stem}.png"
		image = Image.open(png).convert("RGBA")
		corners = [image.getpixel(point)[3] for point in ((0, 0), (209, 0), (0, 175), (209, 175))]
		if any(corners):
			raise RuntimeError(f"Report corners are not transparent: {png} -> {corners}")
		validate_dds_pair(png, REPORT_RUNTIME / f"{stem}.dds", (210, 176))

	for stem in CLAIMANT_STEMS:
		validate_dds_pair(
			PROCESSED / "portraits" / "claimants" / f"{stem}.png",
			LEADER_RUNTIME / f"{stem}.dds",
			(156, 210),
		)
	for stem in DERIVATIVE_STEMS:
		validate_dds_pair(
			PROCESSED / "portraits" / "derivatives" / f"{stem}.png",
			LEADER_RUNTIME / f"{stem}.dds",
			(156, 210),
		)
	for stem in TECHNICAL_STEMS:
		validate_dds_pair(
			PROCESSED / "portraits" / "technical" / f"{stem}.png",
			LEADER_RUNTIME / f"{stem}.dds",
			(156, 210),
		)

	if len({sha256(SOURCE / "portraits" / "claimants" / f"{stem}_source.png") for stem in CLAIMANT_STEMS}) != 20:
		raise RuntimeError("Claimant source portraits are not all distinct")
	portrait_source_hashes = {
		*(sha256(SOURCE / "portraits" / "claimants" / f"{stem}_source.png") for stem in CLAIMANT_STEMS),
		*(sha256(SOURCE / "portraits" / "derivatives" / f"{stem}_source.png") for stem in DERIVATIVE_STEMS),
		*(sha256(SOURCE / "portraits" / "technical" / f"{stem}_source.png") for stem in TECHNICAL_STEMS),
	}
	if len(portrait_source_hashes) != len(PORTRAIT_STEMS):
		raise RuntimeError("Army, host, and technical muster source scenes are not all distinct")
	if len({sha256(SOURCE / "report" / f"{stem}_source.png") for stem in REPORT_STEMS}) != len(REPORT_STEMS):
		raise RuntimeError("Report sources are not all distinct")

	for slug, spec in ANIMATION_SPECS.items():
		source_frames = [ANIMATIONS / slug / "source_frames" / f"{slug}_{index:03d}_source.png" for index in range(spec["frames"])]
		processed_frames = [ANIMATIONS / slug / "processed_frames" / f"{slug}_{index:03d}.png" for index in range(spec["frames"])]
		if len({sha256(path) for path in source_frames}) != spec["frames"]:
			raise RuntimeError(f"Animation source frames are not distinct: {slug}")
		if len({sha256(path) for path in processed_frames}) != spec["frames"]:
			raise RuntimeError(f"Animation processed frames are not distinct: {slug}")
		for path in processed_frames:
			image = Image.open(path).convert("RGBA")
			if image.size != spec["size"]:
				raise RuntimeError(f"Wrong frame size: {path} -> {image.size}")
			alpha = image.getchannel("A")
			if alpha.getextrema()[0] != 0 or alpha.getextrema()[1] == 0:
				raise RuntimeError(f"Animation frame lacks useful transparency: {path} -> {alpha.getextrema()}")
		sheet_size = (spec["size"][0] * spec["frames"], spec["size"][1])
		validate_dds_pair(
			ANIMATIONS / slug / "sheets" / f"{slug}_sheet.png",
			UI_RUNTIME / f"{slug}_sheet.dds",
			sheet_size,
		)
		validate_dds_pair(
			ANIMATIONS / slug / "sheets" / f"{slug}_static.png",
			UI_RUNTIME / f"{slug}_static.dds",
			spec["size"],
		)
		gif = Image.open(ANIMATIONS / slug / "previews" / f"{slug}_preview.gif")
		if getattr(gif, "n_frames", 1) != spec["frames"]:
			raise RuntimeError(f"Wrong preview frame count: {slug}")

	if len({sha256(SOURCE / "achievements" / f"{stem}_source.png") for stem in ACHIEVEMENT_STEMS}) != len(ACHIEVEMENT_STEMS):
		raise RuntimeError("Achievement source icons are not all distinct")
	if len({sha256(SOURCE / "decisions" / f"{stem}_source.png") for stem in STANDALONE_DECISION_STEMS}) != len(STANDALONE_DECISION_STEMS):
		raise RuntimeError("Standalone decision source icons are not all distinct")
	for stem in ACHIEVEMENT_STEMS:
		completed = PROCESSED / "achievements" / f"{stem}.png"
		grey = PROCESSED / "achievements" / f"{stem}_grey.png"
		not_eligible = PROCESSED / "achievements" / f"{stem}_not_eligible.png"
		validate_dds_pair(completed, ACHIEVEMENT_RUNTIME / f"{stem}.dds", (64, 64))
		validate_dds_pair(grey, ACHIEVEMENT_RUNTIME / f"{stem}_grey.dds", (64, 64))
		validate_dds_pair(not_eligible, ACHIEVEMENT_RUNTIME / f"{stem}_not_eligible.dds", (64, 64))
		if ImageChops.difference(Image.open(grey).convert("RGB"), Image.open(not_eligible).convert("RGB")).getbbox() is None:
			raise RuntimeError(f"Not-eligible overlay did not change achievement icon: {stem}")

	focus_stems = [stem for _, stems in FOCUS_ATLASES for stem in stems]
	decision_stems = [stem for _, stems in DECISION_ATLASES for stem in stems] + list(STANDALONE_DECISION_STEMS)
	for stem in focus_stems:
		validate_transparent_dds_pair(
			PROCESSED / "focuses" / f"{stem}.png",
			FOCUS_RUNTIME / f"{stem}.dds",
			(100, 88),
		)
	for stem in decision_stems:
		validate_transparent_dds_pair(
			PROCESSED / "decisions" / f"{stem}.png",
			DECISION_RUNTIME / f"{stem}.dds",
			(33, 32),
		)
	for stem in IDEA_STEMS:
		validate_transparent_dds_pair(
			PROCESSED / "ideas" / f"{stem}.png",
			IDEA_RUNTIME / f"infantry_spawn_{stem}.dds",
			(64, 64),
		)
	for index, stem in enumerate(UI_STEMS):
		size = (50, 40) if index < 3 else (32, 32)
		validate_transparent_dds_pair(
			PROCESSED / "ui" / f"{stem}.png",
			UI_RUNTIME / f"{stem}.dds",
			size,
		)
	if len({sha256(PROCESSED / "focuses" / f"{stem}.png") for stem in focus_stems}) != len(focus_stems):
		raise RuntimeError("Focus icons are not all distinct")
	if len({sha256(PROCESSED / "decisions" / f"{stem}.png") for stem in decision_stems}) != len(decision_stems):
		raise RuntimeError("Decision icons are not all distinct")
	if len({sha256(PROCESSED / "ideas" / f"{stem}.png") for stem in IDEA_STEMS}) != len(IDEA_STEMS):
		raise RuntimeError("Idea icons are not all distinct")
	if len({sha256(PROCESSED / "ui" / f"{stem}.png") for stem in UI_STEMS}) != len(UI_STEMS):
		raise RuntimeError("Decision-category and UI icons are not all distinct")

	validate_dds_pair(
		PROCESSED / "gui" / "infantry_spawn_muster_board_background.png",
		UI_RUNTIME / "infantry_spawn_muster_board_background.dds",
		(1120, 760),
	)
	if len({sha256(PROCESSED / "flags" / f"{tag}.png") for tag in FLAG_TAGS}) != len(FLAG_TAGS):
		raise RuntimeError("Cosmetic flags are not all distinct")
	for tag in FLAG_TAGS:
		for size_name, size in FLAG_SIZES.items():
			runtime_dir = FLAG_RUNTIME if size_name == "normal" else FLAG_RUNTIME / size_name
			validate_tga_pair(
				PROCESSED / "flags" / f"{tag}_{size_name}.png",
				runtime_dir / f"{tag}.tga",
				size,
			)

	print(f"validated {len(REPORT_STEMS)} report-event images")
	print(
		f"validated {len(CLAIMANT_STEMS)} claimant army scenes, "
		f"{len(DERIVATIVE_STEMS)} derivative host scenes, and "
		f"{len(TECHNICAL_STEMS)} identity-neutral muster scene"
	)
	print("validated three real-source-frame animations, static fallbacks, sheets, GIFs, alpha, and DDS headers")
	print(f"validated {len(ACHIEVEMENT_STEMS)} achievement icon triplets")
	print(f"validated {len(focus_stems)} focus icons, {len(decision_stems)} decision icons, {len(IDEA_STEMS)} idea icons, and {len(UI_STEMS)} category/UI icons")
	print(f"validated one GUI background and {len(FLAG_TAGS)} three-size cosmetic flag sets")


def main() -> None:
	ensure_prerequisites()
	ensure_dirs()
	process_reports()
	process_portraits()
	process_achievements()
	process_animations()
	process_icons()
	process_gui_background()
	process_flags()
	make_contacts()
	convert_all()
	validate()


if __name__ == "__main__":
	main()
