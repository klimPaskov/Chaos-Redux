#!/usr/bin/env python3
"""Verify the Event 005 Soviet Collapse completion gates.

This is a repository-state verifier for the current correction pass. It does
not replace the design review in the completion audit; it preserves the
repeatable parser and surface checks that prove the implementation gates.

Exit codes:
- 0: all implementation gates passed and all required inputs are present.
- 2: implementation gates passed, but a required source input is still missing.
- 1: one or more implementation gates failed.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
import xml.etree.ElementTree as ET
from zipfile import ZipFile
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

EVENT005_FOCUS_FILES = [
	ROOT / "common/national_focus/005_soviet_collapse_republics.txt",
	ROOT / "common/national_focus/005_soviet_collapse_factory_successors.txt",
	ROOT / "common/national_focus/005_soviet_collapse_custom_splinters.txt",
]

EVENT005_SCRIPT_FILES = [
	ROOT / "common/scripted_effects/005_soviet_collapse_effects.txt",
	ROOT / "common/scripted_triggers/005_soviet_collapse_triggers.txt",
	ROOT / "common/decisions/005_soviet_collapse_decisions.txt",
	ROOT / "common/decisions/categories/005_soviet_collapse_categories.txt",
	ROOT / "common/ideas/005_soviet_collapse_ideas.txt",
	ROOT / "common/script_constants/005_soviet_collapse_constants.txt",
	ROOT / "events/005_soviet_collapse.txt",
]

REQUIRED_INPUTS = [
	"tmp/005_soviet_union_collapse_spawn_balance_collapse_pacing_cleanup_spec.md",
	"tmp/005_soviet_union_collapse_event_log_mission_balance_focus_cleanup_spec.md",
	"tmp/005_soviet_union_collapse_final_clean_spec_part_1_core_crisis.md",
	"tmp/005_soviet_union_collapse_final_clean_spec_part_2_objectives_missions_intervention.md",
	"tmp/005_soviet_union_collapse_final_clean_spec_part_3_republics_focus_trees.md",
	"tmp/005_soviet_union_collapse_final_clean_spec_part_4_custom_countries_evolutions_assets_achievements.md",
]

CUSTOM_TAGS = [
	"CFR", "MFR", "OGB", "ICD", "KRS", "FTH", "BBH", "BSC", "TNC", "ALA",
	"UDC", "SDZ", "RMC", "RCD", "ILU", "PRA", "TSC", "BLT", "NRF", "GAC",
	"DHC", "KHC", "FEV", "SZA", "UWD", "MRC", "IUL", "BAC", "ARD", "TRS",
	"NLC", "SEP", "DSC", "COU", "BEC", "RLD", "LID", "IRA",
]

ORDINARY_REPUBLIC_TAGS = ["UKR", "BLR", "MOL", "LIT", "LAT", "EST", "GEO", "ARM", "AZR", "UZB", "KYR", "TAJ", "TMS", "KAZ"]
FIRST_WAVE_WESTERN_TAGS = ["UKR", "BLR", "MOL", "LIT", "LAT", "EST"]
FIRST_WAVE_CAUCASUS_TAGS = ["GEO", "ARM", "AZR"]
FIRST_WAVE_CENTRAL_ASIA_TAGS = ["UZB", "KYR", "TAJ", "TMS"]
IDEOLOGIES = ["communism", "democratic", "fascism", "neutrality"]
BANNED_PHRASE = "starts from a low dynamic baseline in calm conditions"
XLSX_NS = {"a": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
EVENT005_ACHIEVEMENT_COUNT = 47


@dataclass
class Check:
	name: str
	ok: bool
	detail: str
	blocker: bool = False


def read_text(path: Path) -> str:
	return path.read_text(encoding="utf-8-sig", errors="replace")


def sha256(path: Path) -> str:
	return hashlib.sha256(path.read_bytes()).hexdigest()


def strip_comments(text: str) -> str:
	lines = []
	for line in text.splitlines():
		in_quote = False
		out = []
		i = 0
		while i < len(line):
			ch = line[i]
			if ch == '"' and (i == 0 or line[i - 1] != "\\"):
				in_quote = not in_quote
			if ch == "#" and not in_quote:
				break
			out.append(ch)
			i += 1
		lines.append("".join(out))
	return "\n".join(lines)


def tokens(text: str) -> list[str]:
	return re.findall(r'"[^"]*"|[{}=]|[^\s{}=]+', strip_comments(text))


def matching_brace(toks: list[str], open_index: int) -> int:
	depth = 0
	for i in range(open_index, len(toks)):
		if toks[i] == "{":
			depth += 1
		elif toks[i] == "}":
			depth -= 1
			if depth == 0:
				return i
	raise ValueError("unmatched brace")


def top_level_values(body: list[str], key: str) -> list[str]:
	values = []
	depth = 0
	i = 0
	while i < len(body):
		tok = body[i]
		if tok == "{":
			depth += 1
		elif tok == "}":
			depth -= 1
		elif depth == 0 and tok == key and i + 2 < len(body) and body[i + 1] == "=":
			values.append(body[i + 2])
		i += 1
	return values


def top_level_block_bodies(body: list[str], key: str) -> list[list[str]]:
	blocks = []
	depth = 0
	i = 0
	while i < len(body):
		tok = body[i]
		if tok == "{":
			depth += 1
			i += 1
			continue
		if tok == "}":
			depth -= 1
			i += 1
			continue
		if depth == 0 and tok == key and i + 2 < len(body) and body[i + 1] == "=" and body[i + 2] == "{":
			end = matching_brace(body, i + 2)
			blocks.append(body[i + 3:end])
			i = end + 1
			continue
		i += 1
	return blocks


def direct_child_blocks(body: list[str]) -> list[tuple[str, list[str]]]:
	blocks = []
	depth = 0
	i = 0
	while i < len(body):
		tok = body[i]
		if tok == "{":
			depth += 1
			i += 1
			continue
		if tok == "}":
			depth -= 1
			i += 1
			continue
		if depth == 0 and i + 2 < len(body) and body[i + 1] == "=" and body[i + 2] == "{":
			end = matching_brace(body, i + 2)
			blocks.append((tok, body[i + 3:end]))
			i = end + 1
			continue
		i += 1
	return blocks


def named_blocks(toks: list[str], key: str) -> list[list[str]]:
	blocks = []
	i = 0
	while i < len(toks) - 2:
		if toks[i] == key and toks[i + 1] == "=" and toks[i + 2] == "{":
			end = matching_brace(toks, i + 2)
			blocks.append(toks[i + 3:end])
			i = end + 1
			continue
		i += 1
	return blocks


def collect_focus_refs(blocks: list[list[str]]) -> list[str]:
	refs = []
	for block in blocks:
		for i, tok in enumerate(block[:-2]):
			if tok == "focus" and block[i + 1] == "=":
				refs.append(block[i + 2])
	return refs


def count_top_level_key(body: list[str], key: str) -> int:
	depth = 0
	count = 0
	for i, tok in enumerate(body[:-1]):
		if tok == "{":
			depth += 1
		elif tok == "}":
			depth -= 1
		elif depth == 0 and tok == key and body[i + 1] == "=":
			count += 1
	return count


def verify_focuses() -> list[Check]:
	focuses = []
	continuous = []
	layout_rows = []
	for path in EVENT005_FOCUS_FILES:
		toks = tokens(read_text(path))
		for block in named_blocks(toks, "focus"):
			ids = top_level_values(block, "id")
			if ids:
				focuses.append((path, ids[0], block))
		for block in named_blocks(toks, "continuous_focus_position"):
			xs = top_level_values(block, "x")
			ys = top_level_values(block, "y")
			continuous.append((path, xs[0] if xs else None, ys[0] if ys else None))
		for tree_body in named_blocks(toks, "focus_tree"):
			tree_ids = top_level_values(tree_body, "id")
			tree_id = tree_ids[0] if tree_ids else "<missing>"
			tree_focuses = []
			for focus_body in top_level_block_bodies(tree_body, "focus"):
				ids = top_level_values(focus_body, "id")
				xs = top_level_values(focus_body, "x")
				ys = top_level_values(focus_body, "y")
				if ids and xs and ys and xs[0].lstrip("-").isdigit() and ys[0].lstrip("-").isdigit():
					tree_focuses.append((ids[0], int(xs[0]), int(ys[0])))
			if tree_focuses:
				x_values = [x for _, x, _ in tree_focuses]
				y_values = [y for _, _, y in tree_focuses]
				coords = [(x, y) for _, x, y in tree_focuses]
				layout_rows.append(
					{
						"path": path,
						"tree_id": tree_id,
						"count": len(tree_focuses),
						"x_span": max(x_values) - min(x_values),
						"y_span": max(y_values) - min(y_values),
						"duplicate_coords": len(coords) - len(set(coords)),
						"max_col": max(x_values.count(x) for x in set(x_values)),
						"max_row": max(y_values.count(y) for y in set(y_values)),
					}
				)

	ids = [focus_id for _, focus_id, _ in focuses]
	id_set = set(ids)
	duplicates = sorted({focus_id for focus_id in ids if ids.count(focus_id) > 1})
	missing_refs = []
	self_refs = []
	nonreciprocal = []
	repeated_mutual_blocks = 0
	mutuals: dict[str, set[str]] = {}
	missing_ai = []
	missing_reward = []
	missing_icon = []
	missing_coords = []
	ai_block_count = 0
	dynamic_ai = 0
	mutual_focus_count = 0
	dynamic_mutual_ai = 0
	flat_mutual_ai = 0

	for path, focus_id, block in focuses:
		prereq_refs = collect_focus_refs(top_level_block_bodies(block, "prerequisite"))
		mutual_blocks = top_level_block_bodies(block, "mutually_exclusive")
		mutual_refs = collect_focus_refs(mutual_blocks)
		ai_blocks = top_level_block_bodies(block, "ai_will_do")
		ai_block_count += len(ai_blocks)
		has_dynamic_ai = any("modifier" in ai_body for ai_body in ai_blocks)
		if has_dynamic_ai:
			dynamic_ai += 1
		if mutual_refs:
			mutual_focus_count += 1
			if has_dynamic_ai:
				dynamic_mutual_ai += 1
			else:
				flat_mutual_ai += 1
		if len(mutual_blocks) > 1:
			repeated_mutual_blocks += 1
		for ref in prereq_refs + mutual_refs:
			if ref not in id_set:
				missing_refs.append((focus_id, ref))
			if ref == focus_id:
				self_refs.append(focus_id)
		mutuals[focus_id] = set(mutual_refs)
		if not top_level_values(block, "ai_will_do") and not top_level_block_bodies(block, "ai_will_do"):
			missing_ai.append(focus_id)
		if count_top_level_key(block, "completion_reward") != 1:
			missing_reward.append(focus_id)
		if not top_level_values(block, "icon"):
			missing_icon.append(focus_id)
		xs = top_level_values(block, "x")
		ys = top_level_values(block, "y")
		if not xs or not ys:
			missing_coords.append(focus_id)
	for focus_id, refs in mutuals.items():
		for ref in refs:
			if ref in mutuals and focus_id not in mutuals[ref]:
				nonreciprocal.append((focus_id, ref))

	continuous_bad = [
		(path.name, x, y)
		for path, x, y in continuous
		if x != "50" or y is None or not y.lstrip("-").isdigit() or int(y) < 1500
	]
	layout_bad = [
		row
		for row in layout_rows
		if row["duplicate_coords"] != 0
		or row["x_span"] < 14
		or row["y_span"] < 9
		or row["max_col"] > 12
		or row["max_row"] > 14
	]
	wide_tree_count = sum(1 for row in layout_rows if row["x_span"] >= 20)
	ok = not any([
		duplicates, missing_refs, self_refs, nonreciprocal, repeated_mutual_blocks,
		missing_ai, missing_reward, missing_icon, missing_coords,
		continuous_bad,
	])
	return [
		Check(
			"focus_integrity",
			ok,
			(
				f"focuses={len(focuses)} duplicates={len(duplicates)} missing_refs={len(missing_refs)} "
				f"self_refs={len(self_refs)} nonreciprocal_mutual={len(nonreciprocal)} "
				f"repeated_mutual_blocks={repeated_mutual_blocks} missing_ai={len(missing_ai)} "
				f"missing_reward={len(missing_reward)} missing_icon={len(missing_icon)} "
				f"missing_coords={len(missing_coords)} continuous_positions={len(continuous)} "
				f"continuous_bad={len(continuous_bad)}"
			),
		),
		Check(
			"focus_layout_surface",
			not layout_bad and len(layout_rows) == len(continuous) and wide_tree_count >= 9,
			(
				f"focus_trees={len(layout_rows)} continuous_positions={len(continuous)} "
				f"layout_bad={len(layout_bad)} duplicate_coord_trees={sum(1 for row in layout_rows if row['duplicate_coords'])} "
				f"wide_trees={wide_tree_count} min_x_span={min((row['x_span'] for row in layout_rows), default=0)} "
				f"min_y_span={min((row['y_span'] for row in layout_rows), default=0)} "
				f"max_col={max((row['max_col'] for row in layout_rows), default=0)} "
				f"max_row={max((row['max_row'] for row in layout_rows), default=0)}"
			),
		),
		Check(
			"focus_ai_surface",
			(
				ai_block_count == len(focuses)
				and dynamic_ai >= 300
				and mutual_focus_count >= 170
				and dynamic_mutual_ai == mutual_focus_count
				and flat_mutual_ai == 0
			),
			(
				f"focuses={len(focuses)} ai_blocks={ai_block_count} dynamic_ai={dynamic_ai} "
				f"mutual_route_choices={mutual_focus_count} dynamic_mutual_ai={dynamic_mutual_ai} "
				f"flat_mutual_ai={flat_mutual_ai}"
			),
		),
	]


def event005_focus_ids() -> list[str]:
	focus_ids = []
	for path in EVENT005_FOCUS_FILES:
		for block in named_blocks(tokens(read_text(path)), "focus"):
			ids = top_level_values(block, "id")
			if ids:
				focus_ids.append(ids[0])
	return focus_ids


def event005_idea_ids() -> list[str]:
	idea_ids = []
	toks = tokens(read_text(ROOT / "common/ideas/005_soviet_collapse_ideas.txt"))
	for ideas_body in named_blocks(toks, "ideas"):
		for group_name, group_body in direct_child_blocks(ideas_body):
			if group_name in {"country", "country_leader", "army_chief", "navy_chief", "air_chief"}:
				idea_ids.extend(name for name, _ in direct_child_blocks(group_body))
	return idea_ids


def event005_decision_ids() -> list[str]:
	decision_ids = []
	toks = tokens(read_text(ROOT / "common/decisions/005_soviet_collapse_decisions.txt"))
	for _, category_body in direct_child_blocks(toks):
		decision_ids.extend(name for name, _ in direct_child_blocks(category_body))
	return decision_ids


def parse_constants(text: str) -> dict[str, float]:
	constants = {}
	for match in re.finditer(r"^\s*(@[A-Za-z0-9_]+)\s*=\s*(-?\d+(?:\.\d+)?)\s*$", text, re.MULTILINE):
		constants[match.group(1)] = float(match.group(2))
	return constants


def parse_script_constants(text: str) -> dict[str, float]:
	values: dict[str, float] = {}
	for category, body in direct_child_blocks(tokens(text)):
		depth = 0
		i = 0
		while i < len(body) - 2:
			if body[i] == "{":
				depth += 1
			elif body[i] == "}":
				depth -= 1
			elif depth == 0 and body[i + 1] == "=":
				try:
					values[f"{category}.{body[i]}"] = float(body[i + 2])
				except ValueError:
					pass
			i += 1
	return values


def clamp(value: float, low: float, high: float) -> float:
	return max(low, min(high, value))


def modifier_values(block: list[str], constants: dict[str, float]) -> list[float | None]:
	values: list[float | None] = []
	for modifier in top_level_block_bodies(block, "modifier"):
		depth = 0
		i = 0
		while i < len(modifier) - 2:
			if modifier[i] == "{":
				depth += 1
			elif modifier[i] == "}":
				depth -= 1
			elif depth == 0 and modifier[i + 1] == "=":
				raw = modifier[i + 2]
				if raw in constants:
					values.append(constants[raw])
				else:
					try:
						values.append(float(raw))
					except ValueError:
						values.append(None)
			i += 1
	return values


def verify_ideas() -> list[Check]:
	path = ROOT / "common/ideas/005_soviet_collapse_ideas.txt"
	text = read_text(path)
	constants = parse_constants(text)
	toks = tokens(text)
	idea_blocks: list[tuple[str, list[str]]] = []
	for ideas_body in named_blocks(toks, "ideas"):
		for group_name, group_body in direct_child_blocks(ideas_body):
			if group_name in {"country", "country_leader", "army_chief", "navy_chief", "air_chief"}:
				idea_blocks.extend(direct_child_blocks(group_body))

	no_modifier = []
	weak_lt3 = []
	tiny_only = []
	modifier_counts = []
	for idea_id, block in idea_blocks:
		values = modifier_values(block, constants)
		if not values:
			no_modifier.append(idea_id)
			continue
		modifier_counts.append(len(values))
		if len(values) < 3:
			weak_lt3.append(idea_id)
		numeric = [abs(value) for value in values if value is not None]
		if numeric and all(value <= 0.03 for value in numeric):
			tiny_only.append(idea_id)

	ok = not no_modifier and not weak_lt3 and not tiny_only and len(idea_blocks) >= 120
	return [
		Check(
			"idea_strength",
			ok,
			(
				f"ideas={len(idea_blocks)} no_modifier={len(no_modifier)} weak_lt3={len(weak_lt3)} "
				f"tiny_only={len(tiny_only)} min_modifiers={min(modifier_counts) if modifier_counts else 0} "
				f"max_modifiers={max(modifier_counts) if modifier_counts else 0}"
			),
		)
	]


def verify_input_files() -> list[Check]:
	checks = []
	for rel in REQUIRED_INPUTS:
		path = ROOT / rel
		if path.exists():
			text = read_text(path)
			checks.append(Check("input:" + rel, True, f"present lines={len(text.splitlines())} bytes={path.stat().st_size} sha256={sha256(path)}"))
		else:
			checks.append(Check("input:" + rel, False, "missing", blocker=True))
	return checks


def verify_first_wave_and_forces() -> list[Check]:
	effects = read_text(ROOT / "common/scripted_effects/005_soviet_collapse_effects.txt")
	triggers = read_text(ROOT / "common/scripted_triggers/005_soviet_collapse_triggers.txt")
	effect_tokens = tokens(effects)
	trigger_tokens = tokens(triggers)
	release_blocks = named_blocks(effect_tokens, "soviet_collapse_release_initial_republics")
	setup_blocks = named_blocks(effect_tokens, "soviet_collapse_apply_breakaway_setup_package")
	western_blocks = named_blocks(effect_tokens, "soviet_collapse_add_random_first_wave_western_republic")
	caucasus_blocks = named_blocks(effect_tokens, "soviet_collapse_add_random_first_wave_caucasus_republic")
	central_blocks = named_blocks(effect_tokens, "soviet_collapse_add_random_first_wave_central_asian_republic")
	extra_blocks = named_blocks(effect_tokens, "soviet_collapse_add_random_extra_first_wave_republic")
	selected_blocks = named_blocks(effect_tokens, "soviet_collapse_release_selected_first_wave_republics")
	kaz_blocks = named_blocks(trigger_tokens, "can_soviet_collapse_open_kazakhstan_first_wave")
	release_body = " ".join(release_blocks[0]) if release_blocks else ""
	setup_body = " ".join(setup_blocks[0]) if setup_blocks else ""
	western_body = " ".join(western_blocks[0]) if western_blocks else ""
	caucasus_body = " ".join(caucasus_blocks[0]) if caucasus_blocks else ""
	central_body = " ".join(central_blocks[0]) if central_blocks else ""
	extra_body = " ".join(extra_blocks[0]) if extra_blocks else ""
	selected_body = " ".join(selected_blocks[0]) if selected_blocks else ""
	kaz_body = " ".join(kaz_blocks[0]) if kaz_blocks else ""

	first_wave_ok = all(
		item in release_body
		for item in [
			"soviet_collapse_add_random_first_wave_western_republic",
			"soviet_collapse_add_random_first_wave_caucasus_republic",
			"soviet_collapse_add_random_first_wave_central_asian_republic",
			"soviet_collapse_add_random_extra_first_wave_republic",
			"soviet_collapse_release_selected_first_wave_republics",
			"global.soviet_collapse_first_wave_republics",
		]
	) and "can_soviet_collapse_open_kazakhstan_first_wave" in release_body
	pool_ok = (
		all(f"tag = {tag}" in western_body for tag in FIRST_WAVE_WESTERN_TAGS)
		and all(f"tag = {tag}" in caucasus_body for tag in FIRST_WAVE_CAUCASUS_TAGS)
		and all(f"tag = {tag}" in central_body for tag in FIRST_WAVE_CENTRAL_ASIA_TAGS)
		and all(f"tag = {tag}" in extra_body for tag in FIRST_WAVE_WESTERN_TAGS + FIRST_WAVE_CAUCASUS_TAGS + FIRST_WAVE_CENTRAL_ASIA_TAGS)
		and "tag = KAZ" not in western_body + caucasus_body + central_body + extra_body
		and western_body.count("random_select_amount = 1") == 1
		and caucasus_body.count("random_select_amount = 1") == 1
		and central_body.count("random_select_amount = 1") == 1
		and "add_to_array = { array = global.soviet_collapse_first_wave_republics value = THIS }" in western_body
		and "add_to_array = { array = global.soviet_collapse_first_wave_republics value = THIS }" in caucasus_body
		and "add_to_array = { array = global.soviet_collapse_first_wave_republics value = THIS }" in central_body
	)
	kaz_ok = "is_soviet_collapse_southern_breakaway_active" in kaz_body and "chaos_tier" in kaz_body
	pool_requirements = [
		"every_possible_country",
		"NOT = { is_in_array = { array = global.soviet_collapse_first_wave_republics value = THIS } }",
		"exists = no",
		"any_state",
		"is_core_of = PREV",
		"is_owned_by = SOV",
		"is_controlled_by = SOV",
		"exists = yes",
		"is_subject_of = SOV",
		"random_select_amount = 1",
		"add_to_array = { array = global.soviet_collapse_first_wave_republics value = THIS }",
	]
	pool_surface_ok = all(
		all(item in body for item in pool_requirements)
		for body in [western_body, caucasus_body, central_body, extra_body]
	)
	extra_scaling_ok = (
		release_body.count("soviet_collapse_add_random_extra_first_wave_republic = yes") == 3
		and all(f"has_global_flag = {{ flag = chaos_tier value = {tier} }}" in release_body for tier in [2, 3, 4, 5])
		and "has_war = yes" in release_body
		and "has_stability < constant:soviet_collapse_soviet_objective.good_stability" in release_body
		and "has_war_support < constant:soviet_collapse_soviet_objective.good_war_support" in release_body
		and "has_stability < constant:soviet_collapse_soviet_objective.min_stability" in release_body
	)
	selected_release_ok = all(
		item in selected_body
		for item in [
			"for_each_scope_loop",
			"array = global.soviet_collapse_first_wave_republics",
			"SOV = { release = PREV }",
			"SOV = { set_autonomy = { target = PREV autonomy_state = autonomy_free } }",
			"set_country_flag = soviet_collapse_event_created_republic",
			"soviet_collapse_setup_breakaway_country = yes",
			"soviet_collapse_load_event_created_focus_tree = yes",
		]
	)
	kaz_release_ok = all(
		item in release_body
		for item in [
			"limit = { can_soviet_collapse_open_kazakhstan_first_wave = yes }",
			"release = KAZ",
			"set_autonomy = { target = KAZ autonomy_state = autonomy_free }",
			"KAZ = { soviet_collapse_setup_breakaway_country = yes }",
			"KAZ = { soviet_collapse_load_event_created_focus_tree = yes }",
		]
	)
	southern_cascade_ok = all(
		item in release_body
		for item in [
			"release = UZB",
			"release = KYR",
			"release = TAJ",
			"release = TMS",
			"UZB = { soviet_collapse_setup_southern_republic_if_valid = yes }",
			"KYR = { soviet_collapse_setup_southern_republic_if_valid = yes }",
			"TAJ = { soviet_collapse_setup_southern_republic_if_valid = yes }",
			"TMS = { soviet_collapse_setup_southern_republic_if_valid = yes }",
		]
	) and release_body.count("soviet_collapse_setup_southern_republic_if_valid = yes") >= 8
	force_ok = all(
		item in setup_body
		for item in [
			"add_manpower",
			"add_equipment_to_stockpile",
			"division_template",
			"create_unit",
			"soviet_collapse_breakaway_manpower_package",
			"soviet_collapse_breakaway_guard_unit_count",
			"soviet_collapse_breakaway_field_unit_count",
			"soviet_collapse_terminal_collapse",
		]
	)
	return [
		Check("first_wave_structure", first_wave_ok and pool_ok and kaz_ok, f"structured_pools={first_wave_ok} randomized_pool_tags={pool_ok} kazakhstan_gate={kaz_ok}"),
		Check(
			"first_wave_release_surface",
			pool_surface_ok and extra_scaling_ok and selected_release_ok and kaz_release_ok and southern_cascade_ok,
			(
				f"pool_helpers={len(western_blocks) + len(caucasus_blocks) + len(central_blocks) + len(extra_blocks)} "
				f"western_tags={len(FIRST_WAVE_WESTERN_TAGS)} caucasus_tags={len(FIRST_WAVE_CAUCASUS_TAGS)} "
				f"central_tags={len(FIRST_WAVE_CENTRAL_ASIA_TAGS)} map_support_gates={pool_surface_ok} "
				f"extra_scaling={extra_scaling_ok} selected_release={selected_release_ok} "
				f"kazakhstan_release={kaz_release_ok} southern_cascade={southern_cascade_ok}"
			),
		),
		Check("dynamic_force_package", force_ok, f"manpower_equipment_templates_units_terminal_scaling={force_ok}"),
	]


def verify_dynamic_force_coverage() -> list[Check]:
	effects = read_text(ROOT / "common/scripted_effects/005_soviet_collapse_effects.txt")
	effect_tokens = tokens(effects)
	setup_blocks = named_blocks(effect_tokens, "soviet_collapse_setup_breakaway_country")
	package_blocks = named_blocks(effect_tokens, "soviet_collapse_apply_breakaway_setup_package")
	southern_blocks = named_blocks(effect_tokens, "soviet_collapse_setup_southern_republic_if_valid")
	setup_body = " ".join(setup_blocks[0]) if setup_blocks else ""
	package_body = " ".join(package_blocks[0]) if package_blocks else ""
	southern_body = " ".join(southern_blocks[0]) if southern_blocks else ""
	custom_setup_refs = 0
	missing_custom_setup_refs = []
	for tag in CUSTOM_TAGS:
		blocks = named_blocks(effect_tokens, f"soviet_collapse_setup_{tag.lower()}_successor")
		body = " ".join(blocks[0]) if blocks else ""
		if "soviet_collapse_setup_breakaway_country" in body:
			custom_setup_refs += 1
		else:
			missing_custom_setup_refs.append(tag)
	ordinary_release_paths = all(
		item in effects
		for item in [
			"soviet_collapse_release_selected_first_wave_republics",
			"soviet_collapse_release_terminal_ordinary_republics",
			"soviet_collapse_setup_breakaway_country = yes",
			"soviet_collapse_setup_southern_republic_if_valid = yes",
			"KAZ = { soviet_collapse_setup_breakaway_country = yes }",
		]
	)
	package_dynamic_ok = all(
		item in package_body
		for item in [
			"soviet_collapse_breakaway_manpower_package",
			"soviet_collapse_breakaway_infantry_equipment_package",
			"soviet_collapse_breakaway_support_equipment_package",
			"soviet_collapse_breakaway_artillery_equipment_package",
			"soviet_collapse_breakaway_guard_unit_count",
			"soviet_collapse_breakaway_field_unit_count",
			"soviet_collapse_total_collapse_threat",
			"soviet_collapse_moscow_authority",
			"soviet_collapse_depot_vulnerability",
			"soviet_collapse_foreign_appetite",
			"soviet_collapse_terminal_collapse",
			"has_global_flag = { flag = chaos_tier value = 5 }",
			"add_manpower",
			"add_equipment_to_stockpile",
			"division_template",
			"create_unit",
		]
	)
	ok = (
		len(setup_blocks) == 1
		and len(package_blocks) == 1
		and len(southern_blocks) == 1
		and "soviet_collapse_apply_breakaway_setup_package = yes" in setup_body
		and "soviet_collapse_setup_breakaway_country = yes" in southern_body
		and custom_setup_refs == len(CUSTOM_TAGS)
		and ordinary_release_paths
		and package_dynamic_ok
	)
	return [
		Check(
			"dynamic_force_coverage",
			ok,
			(
				f"setup_helpers={len(setup_blocks)} package_helpers={len(package_blocks)} southern_helpers={len(southern_blocks)} "
				f"custom_successor_setup_refs={custom_setup_refs}/{len(CUSTOM_TAGS)} "
				f"ordinary_release_paths={ordinary_release_paths} package_dynamic={package_dynamic_ok}"
			),
		)
	]


def verify_terminal_ordinary_republics() -> list[Check]:
	effects = read_text(ROOT / "common/scripted_effects/005_soviet_collapse_effects.txt")
	effect_tokens = tokens(effects)
	terminal_blocks = named_blocks(effect_tokens, "soviet_collapse_release_terminal_ordinary_republics")
	terminal_body = " ".join(terminal_blocks[0]) if terminal_blocks else ""
	missing_tags = [tag for tag in ORDINARY_REPUBLIC_TAGS if f"tag = {tag}" not in terminal_body]
	release_and_subject_ok = all(
		item in terminal_body
		for item in [
			"every_possible_country",
			"exists = no",
			"is_owned_by = SOV",
			"is_controlled_by = SOV",
			"SOV = { release = PREV }",
			"exists = yes",
			"is_subject_of = SOV",
			"SOV = { set_autonomy = { target = PREV autonomy_state = autonomy_free } }",
			"soviet_collapse_setup_breakaway_country",
			"soviet_collapse_load_event_created_focus_tree",
		]
	)
	terminal_collapse_ok = all(
		item in effects
		for item in [
			"soviet_collapse_apply_terminal_collapse",
			"soviet_collapse_release_terminal_ordinary_republics = yes",
			"soviet_collapse_spawn_terminal_high_chaos_successors = yes",
			"soviet_collapse_cleanup_terminal_collapse_missions = yes",
		]
	)
	ok = len(terminal_blocks) == 1 and not missing_tags and release_and_subject_ok and terminal_collapse_ok
	return [
		Check(
			"terminal_ordinary_republic_release_surface",
			ok,
			(
				f"helpers={len(terminal_blocks)} ordinary_tags={len(ORDINARY_REPUBLIC_TAGS) - len(missing_tags)}/{len(ORDINARY_REPUBLIC_TAGS)} "
				f"release_and_subject_paths={release_and_subject_ok} terminal_collapse_calls={terminal_collapse_ok}"
			),
		)
	]


def crisis_scenario(constants: dict[str, float], *, tier: int = 0, low_stability: bool = False, low_war_support: bool = False, active_war: bool = False, capital_lost: bool = False) -> tuple[float, float]:
	authority = constants["soviet_collapse_baseline.moscow_authority"]
	confidence = constants["soviet_collapse_baseline.republic_confidence"]
	obedience = constants["soviet_collapse_baseline.military_obedience"]
	depot = constants["soviet_collapse_baseline.depot_vulnerability"]
	foreign = constants["soviet_collapse_baseline.foreign_appetite"]
	league = constants["soviet_collapse_baseline.league_cohesion"]
	weirdness = constants["soviet_collapse_baseline.evolution_weirdness"]

	if tier == 1:
		confidence += constants["soviet_collapse_opening_pressure.chaos_tier_1"]
		depot += constants["soviet_collapse_opening_pressure.chaos_tier_1"]
	elif tier == 2:
		confidence += constants["soviet_collapse_opening_pressure.chaos_tier_2"]
		depot += constants["soviet_collapse_opening_pressure.chaos_tier_2"]
		foreign += constants["soviet_collapse_opening_pressure.chaos_tier_2_foreign_appetite"]
	elif tier == 3:
		confidence += constants["soviet_collapse_opening_pressure.chaos_tier_3"]
		depot += constants["soviet_collapse_opening_pressure.chaos_tier_3"]
		foreign += constants["soviet_collapse_opening_pressure.chaos_tier_3_foreign_appetite"]
		weirdness += constants["soviet_collapse_opening_pressure.chaos_tier_3_weirdness"]
	elif tier == 4:
		confidence += constants["soviet_collapse_opening_pressure.chaos_tier_4"]
		depot += constants["soviet_collapse_opening_pressure.chaos_tier_4"]
		foreign += constants["soviet_collapse_opening_pressure.chaos_tier_4_foreign_appetite"]
		weirdness += constants["soviet_collapse_opening_pressure.chaos_tier_4_weirdness"]
	elif tier == 5:
		confidence += constants["soviet_collapse_opening_pressure.chaos_tier_final"]
		depot += constants["soviet_collapse_opening_pressure.chaos_tier_final"]
		foreign += constants["soviet_collapse_opening_pressure.chaos_tier_final_foreign_appetite"]
		weirdness += constants["soviet_collapse_opening_pressure.chaos_tier_final_weirdness"]

	if low_stability:
		confidence += constants["soviet_collapse_opening_pressure.low_stability"]
		authority += constants["soviet_collapse_opening_pressure.low_stability_authority"]
	if low_war_support:
		obedience += constants["soviet_collapse_opening_pressure.low_war_support_obedience"]
		confidence += constants["soviet_collapse_opening_pressure.low_war_support"]
	if active_war:
		depot += constants["soviet_collapse_opening_pressure.active_war"]
		foreign += constants["soviet_collapse_opening_pressure.active_war"]
	if capital_lost:
		authority += constants["soviet_collapse_opening_pressure.capital_lost_authority"]
		confidence += constants["soviet_collapse_opening_pressure.capital_lost"]

	component_min = constants["soviet_collapse_baseline.component_min"]
	component_max = constants["soviet_collapse_baseline.component_max"]
	authority = clamp(authority, component_min, component_max)
	confidence = clamp(confidence, component_min, component_max)
	obedience = clamp(obedience, component_min, component_max)
	depot = clamp(depot, component_min, component_max)
	foreign = clamp(foreign, component_min, component_max)
	league = clamp(league, component_min, component_max)
	weirdness = clamp(weirdness, component_min, component_max)
	threat = confidence + depot + foreign + league + weirdness
	threat += constants["soviet_collapse_baseline.total_threat_offset"]
	threat -= authority
	threat -= obedience
	threat *= constants["soviet_collapse_baseline.total_threat_multiplier"]
	threat = clamp(threat, constants["soviet_collapse_baseline.total_threat_floor"], constants["soviet_collapse_baseline.total_threat_ceiling"])
	return authority, threat


def verify_crisis_balance() -> list[Check]:
	constants = parse_script_constants(read_text(ROOT / "common/script_constants/005_soviet_collapse_constants.txt"))
	effects = read_text(ROOT / "common/scripted_effects/005_soviet_collapse_effects.txt")
	effect_tokens = tokens(effects)
	calm_authority, calm_threat = crisis_scenario(constants)
	tier1_authority, tier1_threat = crisis_scenario(constants, tier=1)
	severe_authority, severe_threat = crisis_scenario(constants, tier=5, low_stability=True, low_war_support=True, active_war=True, capital_lost=True)
	recalculate_blocks = named_blocks(effect_tokens, "soviet_collapse_recalculate_total_threat")
	initialize_blocks = named_blocks(effect_tokens, "soviet_collapse_initialize_crisis_values")
	recalculate_body = " ".join(recalculate_blocks[0]) if recalculate_blocks else ""
	initialize_body = " ".join(initialize_blocks[0]) if initialize_blocks else ""
	visible_causes = all(
		item in effects
		for item in [
			"soviet_collapse_republic_confidence",
			"soviet_collapse_depot_vulnerability",
			"soviet_collapse_foreign_appetite",
			"soviet_collapse_league_cohesion",
			"soviet_collapse_evolution_weirdness",
			"soviet_collapse_moscow_authority",
			"soviet_collapse_military_obedience",
			"total_threat_multiplier",
			"clamp_variable = { var = soviet_collapse_total_collapse_threat",
		]
	)
	pressure_helpers = len(re.findall(r"soviet_collapse_apply_(?:successful|failed)_[A-Za-z0-9_]*objective_pressure\s*=", effects))
	component_variables = [
		"soviet_collapse_moscow_authority",
		"soviet_collapse_republic_confidence",
		"soviet_collapse_military_obedience",
		"soviet_collapse_depot_vulnerability",
		"soviet_collapse_foreign_appetite",
		"soviet_collapse_league_cohesion",
		"soviet_collapse_evolution_weirdness",
	]
	recalculate_surface = (
		len(recalculate_blocks) == 1
		and "soviet_collapse_clamp_crisis_components = yes" in recalculate_body
		and all(var in recalculate_body for var in component_variables)
		and "subtract_from_variable = { soviet_collapse_total_collapse_threat = soviet_collapse_moscow_authority }" in recalculate_body
		and "subtract_from_variable = { soviet_collapse_total_collapse_threat = soviet_collapse_military_obedience }" in recalculate_body
		and "multiply_variable = { var = soviet_collapse_total_collapse_threat value = constant:soviet_collapse_baseline.total_threat_multiplier }" in recalculate_body
		and "clamp_variable = { var = soviet_collapse_total_collapse_threat min = constant:soviet_collapse_baseline.total_threat_floor max = constant:soviet_collapse_baseline.total_threat_ceiling }" in recalculate_body
		and constants.get("soviet_collapse_baseline.total_threat_multiplier", 1) < 1
	)
	opening_surface = (
		len(initialize_blocks) == 1
		and all(f"set_variable = {{ {var} = constant:soviet_collapse_baseline.{var.removeprefix('soviet_collapse_')} }}" in initialize_body for var in component_variables)
		and all(f"has_global_flag = {{ flag = chaos_tier value = {tier} }}" in initialize_body for tier in [1, 2, 3, 4, 5])
		and "has_stability < constant:soviet_collapse_soviet_objective.good_stability" in initialize_body
		and "has_war_support < constant:soviet_collapse_soviet_objective.good_war_support" in initialize_body
		and "has_war = yes" in initialize_body
		and "NOT = { capital_scope = { is_controlled_by = ROOT } }" in initialize_body
		and "soviet_collapse_recalculate_total_threat = yes" in initialize_body
	)
	pressure_families = {
		"authority": ["soviet_collapse_moscow_authority", "soviet_collapse_republic_confidence", "soviet_collapse_foreign_appetite"],
		"legal": ["soviet_collapse_moscow_authority", "soviet_collapse_republic_confidence", "soviet_collapse_evolution_weirdness"],
		"command": ["soviet_collapse_moscow_authority", "soviet_collapse_military_obedience", "soviet_collapse_republic_confidence"],
		"rail": ["soviet_collapse_military_obedience", "soviet_collapse_depot_vulnerability", "soviet_collapse_foreign_appetite"],
		"depot": ["soviet_collapse_republic_confidence", "soviet_collapse_depot_vulnerability"],
		"old_movement": ["soviet_collapse_moscow_authority", "soviet_collapse_depot_vulnerability", "soviet_collapse_evolution_weirdness"],
		"foreign": ["soviet_collapse_moscow_authority", "soviet_collapse_republic_confidence", "soviet_collapse_foreign_appetite"],
		"cleanup": ["soviet_collapse_moscow_authority", "soviet_collapse_military_obedience", "soviet_collapse_depot_vulnerability"],
		"settlement": ["soviet_collapse_moscow_authority", "soviet_collapse_republic_confidence", "soviet_collapse_foreign_appetite", "soviet_collapse_league_cohesion"],
		"league": ["soviet_collapse_republic_confidence", "soviet_collapse_foreign_appetite", "soviet_collapse_league_cohesion"],
	}
	covered_pressure_families = 0
	for family, variables in pressure_families.items():
		success_blocks = named_blocks(effect_tokens, f"soviet_collapse_apply_successful_{family}_objective_pressure")
		failure_blocks = named_blocks(effect_tokens, f"soviet_collapse_apply_failed_{family}_objective_pressure")
		success_body = " ".join(success_blocks[0]) if success_blocks else ""
		failure_body = " ".join(failure_blocks[0]) if failure_blocks else ""
		if (
			len(success_blocks) == 1
			and len(failure_blocks) == 1
			and all(var in success_body + failure_body for var in variables)
			and "soviet_collapse_recalculate_total_threat = yes" in success_body
			and "soviet_collapse_recalculate_total_threat = yes" in failure_body
		):
			covered_pressure_families += 1
	ok = (
		calm_authority >= 50
		and calm_threat < 25
		and tier1_authority >= 50
		and tier1_threat < 30
		and severe_authority > 0
		and severe_threat < 100
		and visible_causes
		and pressure_helpers >= 20
	)
	cause_ok = recalculate_surface and opening_surface and covered_pressure_families == len(pressure_families)
	return [
		Check(
			"crisis_balance_surface",
			ok,
			(
				f"calm_authority={calm_authority:.0f} calm_threat={calm_threat:.2f} "
				f"tier1_authority={tier1_authority:.0f} tier1_threat={tier1_threat:.2f} "
				f"severe_authority={severe_authority:.0f} severe_threat={severe_threat:.2f} "
				f"visible_causes={visible_causes} pressure_helpers={pressure_helpers}"
			),
		),
		Check(
			"crisis_cause_surface",
			cause_ok,
			(
				f"recalculate_surface={recalculate_surface} opening_surface={opening_surface} "
				f"pressure_families={covered_pressure_families}/{len(pressure_families)} "
				f"multiplier={constants.get('soviet_collapse_baseline.total_threat_multiplier', 0):.2f}"
			),
		),
	]


def verify_union_unmade_and_cleanup() -> list[Check]:
	effects = read_text(ROOT / "common/scripted_effects/005_soviet_collapse_effects.txt")
	triggers = read_text(ROOT / "common/scripted_triggers/005_soviet_collapse_triggers.txt")
	decisions = read_text(ROOT / "common/decisions/005_soviet_collapse_decisions.txt")
	categories = read_text(ROOT / "common/decisions/categories/005_soviet_collapse_categories.txt")
	constants = parse_script_constants(read_text(ROOT / "common/script_constants/005_soviet_collapse_constants.txt"))
	effect_tokens = tokens(effects)
	maybe_blocks = named_blocks(effect_tokens, "soviet_collapse_maybe_show_union_unmade_super_event")
	maybe_body = " ".join(maybe_blocks[0]) if maybe_blocks else ""

	union_ok = all(
		item in effects + triggers
		for item in [
			"soviet_collapse_union_unmade_first_month_lock",
			"days = 31",
			"soviet_collapse_maybe_show_union_unmade_super_event",
			"soviet_collapse_apply_terminal_collapse",
			"soviet_collapse_release_terminal_ordinary_republics",
			"soviet_collapse_spawn_terminal_high_chaos_successors",
		]
	)
	union_pacing_ok = (
		len(maybe_blocks) == 1
		and constants.get("soviet_collapse_super_event.min_breakaways_for_union_unmade", 0) >= 5
		and constants.get("soviet_collapse_super_event.union_unmade_high_threat", 0) >= 60
		and constants.get("soviet_collapse_super_event.union_unmade_critical_authority", 100) <= 25
		and constants.get("soviet_collapse_super_event.union_unmade_contested_authority", 100) <= 45
		and "NOT = { has_global_flag = soviet_collapse_super_event_union_unmade_fired }" in maybe_body
		and "NOT = { has_global_flag = soviet_collapse_union_unmade_first_month_lock }" in maybe_body
		and "compare = greater_than_or_equals" in maybe_body
		and "constant:soviet_collapse_super_event.min_breakaways_for_union_unmade" in maybe_body
		and "soviet_collapse_total_collapse_threat" in maybe_body
		and "constant:soviet_collapse_super_event.union_unmade_high_threat" in maybe_body
		and "soviet_collapse_moscow_authority" in maybe_body
		and "constant:soviet_collapse_super_event.union_unmade_critical_authority" in maybe_body
		and "constant:soviet_collapse_super_event.union_unmade_contested_authority" in maybe_body
		and "soviet_collapse_free_republics_league_announced" in maybe_body
		and "soviet_collapse_kazakhstan_first_wave_failed" in maybe_body
		and "has_global_flag = { flag = chaos_tier value = 4 }" in maybe_body
		and "has_global_flag = { flag = chaos_tier value = 5 }" in maybe_body
		and "constant:soviet_collapse_soviet_objective.deep_collapse_threat" in maybe_body
		and "soviet_collapse_show_union_unmade_super_event = yes" in maybe_body
	)
	missions = set(re.findall(r"^\s*(soviet_collapse_soviet_mission_\d{3}_[A-Za-z0-9_]+)\s*=\s*\{", decisions, re.MULTILINE))
	cleanup_blocks = named_blocks(effect_tokens, "soviet_collapse_cleanup_terminal_collapse_missions")
	cleanup_body = " ".join(cleanup_blocks[0]) if cleanup_blocks else ""
	cleanup_remove_refs = set(re.findall(r"remove_mission\s*=\s*(soviet_collapse_soviet_mission_\d{3}_[A-Za-z0-9_]+)", cleanup_body))
	activate_refs = set(re.findall(r"activate_mission\s*=\s*(soviet_collapse_soviet_mission_\d{3}_[A-Za-z0-9_]+)", effects))
	required_cleanup_flags = [
		"clr_global_flag = soviet_collapse_active",
		"clr_global_flag = soviet_collapse_opening_wave_active",
		"clr_global_flag = soviet_collapse_union_unmade_first_month_lock",
		"clr_country_flag = soviet_collapse_next_declaration_unarmed",
		"clr_country_flag = soviet_collapse_next_declaration_armed",
		"clr_country_flag = soviet_collapse_loyal_units_moved",
		"clr_country_flag = soviet_collapse_district_war_rooms_reopened",
		"set_temp_variable = { soviet_collapse_active_objectives = 0 }",
	]
	cleanup_flag_clear_ok = all(flag in cleanup_body for flag in required_cleanup_flags)
	cleanup_helper_ok = (
		len(cleanup_blocks) == 1
		and missions <= cleanup_remove_refs
		and not (cleanup_remove_refs - missions)
		and cleanup_flag_clear_ok
		and "soviet_collapse_cleanup_terminal_collapse_missions = yes" in effects
		and "set_global_flag = soviet_collapse_terminal_collapse" in effects
	)
	cleanup_ok = (
		len(missions) == 128
		and cleanup_helper_ok
		and missions <= activate_refs
		and "NOT = { has_global_flag = soviet_collapse_terminal_collapse }" in triggers
	)
	category_blocks = direct_child_blocks(tokens(categories))
	decision_category_blocks = dict(direct_child_blocks(tokens(decisions)))
	decision_blocks: list[tuple[str, list[str]]] = []
	for _, decision_category_body in decision_category_blocks.items():
		decision_blocks.extend(direct_child_blocks(decision_category_body))
	categories_gated = True
	categories_with_visible = 0
	for _, category_body in category_blocks:
		visible_blocks = top_level_block_bodies(category_body, "visible")
		if visible_blocks:
			categories_with_visible += 1
		if not visible_blocks or "is_soviet_collapse_active = yes" not in " ".join(" ".join(block) for block in visible_blocks):
			categories_gated = False
	decision_categories_gated = all(
		"is_soviet_collapse_active = yes" in " ".join(" ".join(block) for block in top_level_block_bodies(decision_body, "visible"))
		for decision_name, decision_body in decision_blocks
		if not decision_name.startswith("soviet_collapse_soviet_mission_")
	)
	return [
		Check(
			"union_unmade_pacing",
			union_ok and union_pacing_ok,
			(
				f"first_month_lock_and_terminal_release_gates={union_ok} "
				f"trigger_ingredients={union_pacing_ok} min_breakaways={constants.get('soviet_collapse_super_event.min_breakaways_for_union_unmade', '')} "
				f"high_threat={constants.get('soviet_collapse_super_event.union_unmade_high_threat', '')} "
				f"critical_authority={constants.get('soviet_collapse_super_event.union_unmade_critical_authority', '')}"
			),
		),
		Check(
			"terminal_mission_cleanup",
			cleanup_ok and categories_gated and decision_categories_gated,
			(
				f"cleanup_helpers={len(cleanup_blocks)} missions={len(missions)} "
				f"cleanup_remove_refs={len(cleanup_remove_refs & missions)} "
				f"activate_refs={len(activate_refs & missions)} "
				f"category_defs={len(category_blocks)} visible_category_defs={categories_with_visible} "
				f"categories_gated={categories_gated} decision_categories={len(decision_category_blocks)} "
				f"regular_decisions_gated={decision_categories_gated} cleanup_flags={cleanup_flag_clear_ok}"
			),
		),
	]


def verify_soviet_objective_board() -> list[Check]:
	decisions = read_text(ROOT / "common/decisions/005_soviet_collapse_decisions.txt")
	effects = read_text(ROOT / "common/scripted_effects/005_soviet_collapse_effects.txt")
	constants = parse_script_constants(read_text(ROOT / "common/script_constants/005_soviet_collapse_constants.txt"))
	decision_blocks: list[tuple[str, list[str]]] = []
	for _, category_body in direct_child_blocks(tokens(decisions)):
		decision_blocks.extend(direct_child_blocks(category_body))

	mission_re = re.compile(r"^soviet_collapse_soviet_mission_(\d{3})_")
	missions = [(name, body) for name, body in decision_blocks if mission_re.match(name)]
	mission_ids = {name for name, _ in missions}
	effect_tokens = tokens(effects)
	count_blocks = named_blocks(effect_tokens, "soviet_collapse_count_active_soviet_objectives")
	activate_blocks = named_blocks(effect_tokens, "soviet_collapse_activate_opening_objectives")
	count_body = " ".join(count_blocks[0]) if count_blocks else ""
	activate_body = " ".join(activate_blocks[0]) if activate_blocks else ""
	count_refs = set(re.findall(r"has_active_mission\s*=\s*(soviet_collapse_soviet_mission_\d{3}_[A-Za-z0-9_]+)", count_body))
	activate_refs = set(re.findall(r"activate_mission\s*=\s*(soviet_collapse_soviet_mission_\d{3}_[A-Za-z0-9_]+)", activate_body))

	manual_only = 0
	visible_gated = 0
	mission_payloads = 0
	queue_restarts = 0
	done_flag_refs = 0
	mission_timeouts = set()
	for name, body in missions:
		number = mission_re.match(name).group(1)
		body_text = " ".join(body)
		allowed_text = " ".join(" ".join(block) for block in top_level_block_bodies(body, "allowed"))
		visible_text = " ".join(" ".join(block) for block in top_level_block_bodies(body, "visible"))
		complete_text = " ".join(" ".join(block) for block in top_level_block_bodies(body, "complete_effect"))
		timeout_text = " ".join(" ".join(block) for block in top_level_block_bodies(body, "timeout_effect"))
		if (
			"always = no" in allowed_text
			and top_level_values(body, "selectable_mission") == ["no"]
			and top_level_values(body, "is_good") == ["yes"]
			and "activation" not in body_text
		):
			manual_only += 1
		if "tag = SOV" in visible_text and "is_soviet_collapse_active = yes" in visible_text:
			visible_gated += 1
		if (
			top_level_values(body, "days_mission_timeout")
			and "custom_effect_tooltip" in complete_text
			and "custom_effect_tooltip" in timeout_text
			and f"soviet_collapse_mission_{number}_done" in complete_text
			and f"soviet_collapse_mission_{number}_done" in timeout_text
			and "soviet_collapse_apply_successful_" in complete_text
			and "soviet_collapse_apply_failed_" in timeout_text
		):
			mission_payloads += 1
		if (
			"soviet_collapse_activate_opening_objectives = yes" in complete_text
			or "soviet_collapse_activate_opening_objectives = yes" in timeout_text
			or "clr_global_flag = soviet_collapse_active" in complete_text
		):
			queue_restarts += 1
		if f"soviet_collapse_mission_{number}_done" in activate_body:
			done_flag_refs += 1
		mission_timeouts.update(top_level_values(body, "days_mission_timeout"))

	queue_cap_ok = (
		constants.get("soviet_collapse_soviet_objective.active_cap") == 10
		and activate_body.count("constant:soviet_collapse_soviet_objective.active_cap") >= 128
		and activate_body.count("compare = less_than") >= 128
		and activate_body.count("add_to_temp_variable = { soviet_collapse_active_objectives = 1 }") >= 128
	)
	ok = (
		len(missions) == 128
		and len(count_blocks) == 1
		and len(activate_blocks) == 1
		and count_refs == mission_ids
		and activate_refs == mission_ids
		and manual_only == len(missions)
		and visible_gated == len(missions)
		and mission_payloads == len(missions)
		and queue_restarts == len(missions)
		and done_flag_refs == len(missions)
		and len(mission_timeouts) >= 8
		and queue_cap_ok
	)
	return [
		Check(
			"soviet_objective_board_surface",
			ok,
			(
				f"missions={len(missions)} count_helpers={len(count_blocks)} activation_helpers={len(activate_blocks)} "
				f"count_refs={len(count_refs & mission_ids)} activate_refs={len(activate_refs & mission_ids)} "
				f"manual_only={manual_only} visible_gated={visible_gated} payloads={mission_payloads} "
				f"queue_restarts={queue_restarts} done_flag_refs={done_flag_refs} "
				f"timeout_bands={len(mission_timeouts)} active_cap={constants.get('soviet_collapse_soviet_objective.active_cap', '')} "
				f"queue_cap={queue_cap_ok}"
			),
		)
	]


def verify_terminal_high_chaos_successors() -> list[Check]:
	effects = read_text(ROOT / "common/scripted_effects/005_soviet_collapse_effects.txt")
	triggers = read_text(ROOT / "common/scripted_triggers/005_soviet_collapse_triggers.txt")
	effect_tokens = tokens(effects)
	prepare_blocks = named_blocks(effect_tokens, "soviet_collapse_prepare_highest_chaos_terminal_successors")
	maybe_blocks = named_blocks(effect_tokens, "soviet_collapse_maybe_spawn_high_chaos_successors")
	terminal_blocks = named_blocks(effect_tokens, "soviet_collapse_spawn_terminal_high_chaos_successors")
	prepare_body = " ".join(prepare_blocks[0]) if prepare_blocks else ""
	maybe_body = " ".join(maybe_blocks[0]) if maybe_blocks else ""
	terminal_body = " ".join(terminal_blocks[0]) if terminal_blocks else ""

	prepare_flags = len(re.findall(r"\bset_country_flag\b", prepare_body))
	expected_spawn_calls = {f"soviet_collapse_spawn_{tag.lower()}_if_enabled" for tag in CUSTOM_TAGS}
	spawn_calls = {call for call in expected_spawn_calls if call in maybe_body}
	ready_trigger_count = len(re.findall(r"is_soviet_collapse_high_chaos_successor_spawn_ready\s*=\s*yes", triggers))
	ok = (
		"has_global_flag = { flag = chaos_tier value = 5 }" in terminal_body
		and "soviet_collapse_prepare_highest_chaos_terminal_successors" in terminal_body
		and "soviet_collapse_maybe_spawn_high_chaos_successors" in terminal_body
		and prepare_flags >= 25
		and spawn_calls == expected_spawn_calls
		and ready_trigger_count >= 35
	)
	return [
		Check(
			"terminal_high_chaos_successor_surface",
			ok,
			(
				f"prepare_flags={prepare_flags} spawn_calls={len(spawn_calls)}/{len(expected_spawn_calls)} "
				f"ready_trigger_refs={ready_trigger_count}"
			),
		)
	]


def verify_localisation_and_event_log() -> list[Check]:
	search_roots = ["common", "events", "interface", "localisation"]
	hits = []
	for root in search_roots:
		for path in (ROOT / root).rglob("*"):
			if path.is_file() and path.suffix.lower() in {".txt", ".yml", ".gui", ".md"}:
				if BANNED_PHRASE in read_text(path):
					hits.append(str(path.relative_to(ROOT)))
	event_log = read_text(ROOT / "common/scripted_localisation/chaosx_scripted_localisation_events_log.txt")
	debug_loc = read_text(ROOT / "common/scripted_localisation/chaosx_scripted_localisation_debug.txt")
	settings_loc = read_text(ROOT / "common/scripted_localisation/chaosx_scripted_localisation_settings.txt")
	event_names = read_text(ROOT / "localisation/english/chaosx_event_names_l_english.yml")
	gui_loc = read_text(ROOT / "localisation/english/chaosx_gui_l_english.yml")
	logic_effects = read_text(ROOT / "common/scripted_effects/chaosx_logic_effects.txt")
	event_file = read_text(ROOT / "events/005_soviet_collapse.txt")
	event_log_tokens = tokens(event_log)
	event_log_blocks = named_blocks(event_log_tokens, "defined_text")
	defined_texts = {
		values[0]: block
		for block in event_log_blocks
		if (values := top_level_values(block, "name"))
	}
	detail_function_names = [
		"GetEventsLogSovietCollapseDetailCrisisState",
		"GetEventsLogSovietCollapseDetailFirstWave",
		"GetEventsLogSovietCollapseDetailLeague",
		"GetEventsLogSovietCollapseDetailAuthority",
		"GetEventsLogSovietCollapseDetailThreat",
		"GetEventsLogSovietCollapseDetailForeign",
		"GetEventsLogSovietCollapseDetailMutation",
	]
	detail_function_keys = sorted({
		match.group(1)
		for name in detail_function_names
		for match in re.finditer(r"localization_key\s*=\s*(chaosx\.events_log\.window\.event_details\.soviet_collapse\.[A-Za-z0-9_.-]+)", " ".join(defined_texts.get(name, [])))
	})
	detail_ok = all(
		name in defined_texts
		and "always = yes" in " ".join(defined_texts[name])
		and f"[{name}]" in gui_loc
		for name in detail_function_names
	) and all(
		re.search(r"^" + re.escape(key) + r"\s*:", gui_loc, re.MULTILINE)
		for key in detail_function_keys
	) and len(detail_function_keys) == 25
	event_detail_block = " ".join(defined_texts.get("GetEventsLogEventDetailDescription", []))
	logic_compact = " ".join(tokens(logic_effects))
	event_compact = " ".join(tokens(event_file))
	debug_compact = " ".join(tokens(debug_loc))
	settings_compact = " ".join(tokens(settings_loc))
	event_name_ok = bool(re.search(r"^chaosx\.event_name\.5\s*:\s*\"Soviet Union Collapse\"", event_names, re.MULTILINE))
	debug_name_ok = "check_variable = { event_id = 5 }" in debug_compact and "localization_key = chaosx.event_name.5" in debug_compact
	settings_name_ok = "check_variable = { settings_event_id = 5 }" in settings_compact and "localization_key = chaosx.event_name.5" in settings_compact
	default_actor_ok = "check_variable = { event_id = 5 }" in logic_compact and "SOV = { ROOT = { set_temp_variable = { events_log_default_actor = PREV } } }" in logic_compact
	detail_mapping_ok = "check_variable = { var = event_id value = 5 compare = equals }" in event_detail_block and "localization_key = chaosx.events_log.window.event_details.soviet_collapse" in event_detail_block
	entry_event_ok = all(item in event_compact for item in ["add_namespace = chaosx.nr5", "id = chaosx.nr5.1", "id = chaosx.nr5.2", "news_event = { id = chaosx.news.5 days = 2 }"])
	mapping_ok = all([
		event_name_ok,
		debug_name_ok,
		settings_name_ok,
		default_actor_ok,
		detail_mapping_ok,
		entry_event_ok,
		"chaosx.events_log.window.event_details.soviet_collapse:" in gui_loc,
		"Moscow Authority" in gui_loc,
		"Union Crisis Threat" in gui_loc,
	])
	return [
		Check("banned_phrase_cleanup", not hits, f"hits={len(hits)}"),
		Check("event_log_detail_surface", detail_ok, f"detail_functions={sum(1 for name in detail_function_names if name in defined_texts)}/{len(detail_function_names)} detail_output_keys={len(detail_function_keys)}"),
		Check(
			"event_log_mapping_surface",
			mapping_ok,
			(
				f"event_name={event_name_ok} "
				f"debug_name={debug_name_ok} "
				f"settings_name={settings_name_ok} "
				f"default_actor={default_actor_ok} "
				f"detail_mapping={detail_mapping_ok} "
				f"entry_event={entry_event_ok}"
			),
		),
	]


def verify_localisation_surface() -> list[Check]:
	localisation_files = sorted((ROOT / "localisation/english").glob("*005_soviet*.yml")) + [
		ROOT / "localisation/english/chaosx_achievements_l_english.yml",
		ROOT / "localisation/english/chaosx_event_names_l_english.yml",
		ROOT / "localisation/english/chaosx_gui_l_english.yml",
	]
	existing_files = [path for path in localisation_files if path.exists()]
	bom_missing = [str(path.relative_to(ROOT)) for path in existing_files if not path.read_bytes().startswith(b"\xef\xbb\xbf")]
	colon_zero = []
	localisation_text = []
	for path in existing_files:
		text = read_text(path)
		localisation_text.append(text)
		for line_number, line in enumerate(text.splitlines(), start=1):
			if re.search(r"^\s*[A-Za-z0-9_.-]+:0\s*\"", line):
				colon_zero.append(f"{path.relative_to(ROOT)}:{line_number}")
	combined = "\n".join(localisation_text)
	keys = set(re.findall(r"^\s*([A-Za-z0-9_.-]+):\s*\"", combined, re.MULTILINE))
	focus_ids = event005_focus_ids()
	idea_ids = event005_idea_ids()
	decision_ids = event005_decision_ids()
	missing_focus_name = [focus_id for focus_id in focus_ids if focus_id not in keys]
	missing_focus_desc = [focus_id for focus_id in focus_ids if f"{focus_id}_desc" not in keys]
	missing_idea_name = [idea_id for idea_id in idea_ids if idea_id not in keys]
	missing_idea_desc = [idea_id for idea_id in idea_ids if f"{idea_id}_desc" not in keys]
	missing_decision_name = [decision_id for decision_id in decision_ids if decision_id not in keys]
	missing_decision_desc = [decision_id for decision_id in decision_ids if f"{decision_id}_desc" not in keys]
	ok = not any([
		bom_missing,
		colon_zero,
		missing_focus_name,
		missing_focus_desc,
		missing_idea_name,
		missing_idea_desc,
		missing_decision_name,
		missing_decision_desc,
	])
	return [
		Check(
			"localisation_surface",
			ok,
			(
				f"files={len(existing_files)} bom_missing={len(bom_missing)} colon_zero={len(colon_zero)} "
				f"focus_name_missing={len(missing_focus_name)}/{len(focus_ids)} "
				f"focus_desc_missing={len(missing_focus_desc)}/{len(focus_ids)} "
				f"idea_name_missing={len(missing_idea_name)}/{len(idea_ids)} "
				f"idea_desc_missing={len(missing_idea_desc)}/{len(idea_ids)} "
				f"decision_name_missing={len(missing_decision_name)}/{len(decision_ids)} "
				f"decision_desc_missing={len(missing_decision_desc)}/{len(decision_ids)}"
			),
		)
	]


def verify_flags() -> list[Check]:
	missing = []
	decode_errors = []
	top_origin = 0
	bottom_origin = 0
	checked = 0
	for tag in CUSTOM_TAGS:
		for variant in [""] + ["_" + ideology for ideology in IDEOLOGIES]:
			for folder in [ROOT / "gfx/flags", ROOT / "gfx/flags/medium", ROOT / "gfx/flags/small"]:
				path = folder / f"{tag}{variant}.tga"
				if not path.exists():
					missing.append(str(path.relative_to(ROOT)))
					continue
				data = path.read_bytes()
				if len(data) < 18:
					decode_errors.append(str(path.relative_to(ROOT)))
					continue
				descriptor = data[17]
				if descriptor & 0x20:
					top_origin += 1
				else:
					bottom_origin += 1
				checked += 1
	ok = checked == 570 and not missing and not decode_errors and top_origin == 0
	return [Check("flag_orientation_headers", ok, f"flags_checked={checked} missing={len(missing)} decode_errors={len(decode_errors)} bottom_origin={bottom_origin} top_origin={top_origin}")]


def verify_super_events_and_assets() -> list[Check]:
	effects = read_text(ROOT / "common/scripted_effects/005_soviet_collapse_effects.txt")
	super_loc = read_text(ROOT / "localisation/english/005_soviet_collapse_l_english.yml")
	gfx = "\n".join(read_text(path) for path in (ROOT / "interface").glob("*.gfx"))
	union_unmade_ok = all(
		item in effects + super_loc + gfx
		for item in [
			"soviet_collapse_show_union_unmade_super_event",
			"super_event.14.t",
			"super_event.14.d",
			"super_event.14.a",
			"super_event.14.q",
			"GFX_super_event_union_unmade",
		]
	)
	slot_keys = sorted(set(int(match.group(1)) for match in re.finditer(r"super_event\.(1[4-9]|2[0-7])\.t", super_loc)))
	return [Check("super_event_surface", union_unmade_ok and len(slot_keys) == 14, f"union_unmade_package={union_unmade_ok} event005_slots={slot_keys}")]


def event005_achievement_ids() -> list[str]:
	gfx = read_text(ROOT / "interface/chaosx_achievements.gfx")
	marker = "# EVENT 005 - SOVIET UNION COLLAPSE ACHIEVEMENTS"
	if marker not in gfx:
		return []
	section = gfx[gfx.index(marker):]
	ids = []
	for match in re.finditer(r'name\s*=\s*"GFX_achievement_(chaosx_ach_[A-Za-z0-9_]+)"', section):
		achievement_id = match.group(1)
		if achievement_id.endswith("_grey") or achievement_id.endswith("_not_eligible"):
			continue
		ids.append(achievement_id)
	return ids


def verify_evolution_logging_surface() -> list[Check]:
	effects = read_text(ROOT / "common/scripted_effects/005_soviet_collapse_effects.txt")
	event_log_loc = read_text(ROOT / "common/scripted_localisation/chaosx_scripted_localisation_events_log.txt")
	custom_loc = read_text(ROOT / "localisation/english/005_soviet_collapse_custom_countries_l_english.yml")
	effect_tokens = tokens(effects)
	record_blocks = named_blocks(effect_tokens, "soviet_collapse_record_high_chaos_successor_evolution")
	record_body = " ".join(record_blocks[0]) if record_blocks else ""
	writer_count = len(re.findall(r"\brecord_events_log_evolution_entry\s*=\s*yes\b", effects))
	helper_calls = len(re.findall(r"\bsoviet_collapse_record_high_chaos_successor_evolution\s*=\s*yes\b", effects))
	record_context_ok = all(
		item in record_body
		for item in [
			"events_log_evolution_event_id",
			"events_log_evolution_type",
			"events_log_evolution_tier",
			"events_log_evolution_actor",
		]
	)
	spawn_context_ok = all(
		all(item in " ".join(named_blocks(effect_tokens, f"soviet_collapse_spawn_{tag.lower()}_if_enabled")[0]) for item in ["events_log_evolution_stage", "is_current_evolution_enabled"])
		for tag in CUSTOM_TAGS
		if named_blocks(effect_tokens, f"soviet_collapse_spawn_{tag.lower()}_if_enabled")
	)
	spawn_context_count = sum(
		1
		for tag in CUSTOM_TAGS
		if named_blocks(effect_tokens, f"soviet_collapse_spawn_{tag.lower()}_if_enabled")
		and all(item in " ".join(named_blocks(effect_tokens, f"soviet_collapse_spawn_{tag.lower()}_if_enabled")[0]) for item in ["events_log_evolution_stage", "is_current_evolution_enabled"])
	)
	duplicate_flags_ok = all(
		item in record_body
		for item in [
			"soviet_collapse_high_chaos_evolution_tier_5_recorded",
			"soviet_collapse_high_chaos_evolution_tier_4_recorded",
		]
	)
	localisation_ok = all(
		item in event_log_loc + custom_loc
		for item in [
			"chaosx.events_log.evolution.type.soviet_collapse_high_chaos",
			"chaosx.events_log.window.evolution_details.soviet_collapse_high_chaos.title",
			"chaosx.events_log.window.evolution_details.soviet_collapse_high_chaos.body",
		]
	)
	ok = len(record_blocks) == 1 and writer_count == 1 and helper_calls == len(CUSTOM_TAGS) and record_context_ok and spawn_context_ok and duplicate_flags_ok and localisation_ok
	return [
		Check(
			"evolution_logging_surface",
			ok,
			(
				f"record_helpers={len(record_blocks)} writer_count={writer_count} "
				f"successor_calls={helper_calls}/{len(CUSTOM_TAGS)} record_context={record_context_ok} "
				f"spawn_context={spawn_context_count}/{len(CUSTOM_TAGS)} "
				f"duplicate_flags={duplicate_flags_ok} localisation={localisation_ok}"
			),
		)
	]


def verify_achievement_surface() -> list[Check]:
	achievement_ids = event005_achievement_ids()
	achievements = read_text(ROOT / "common/achievements/chaos_redux_achievements.txt")
	localisation = read_text(ROOT / "localisation/english/chaosx_achievements_l_english.yml")
	gfx = read_text(ROOT / "interface/chaosx_achievements.gfx")
	manifest = read_text(ROOT / "docs/assets/005_soviet_union_collapse/achievement_icon_manifest.md")

	missing_definitions = [
		achievement_id for achievement_id in achievement_ids
		if not re.search(r"^" + re.escape(achievement_id) + r"\s*=\s*\{", achievements, re.MULTILINE)
	]
	missing_possible = [
		achievement_id for achievement_id in achievement_ids
		if re.search(r"^" + re.escape(achievement_id) + r"\s*=\s*\{(?P<body>.*?)(?=^chaosx_ach_|\Z)", achievements, re.MULTILINE | re.DOTALL)
		and "chaosx_ach_soviet_collapse_eligible_tooltip" not in re.search(
			r"^" + re.escape(achievement_id) + r"\s*=\s*\{(?P<body>.*?)(?=^chaosx_ach_|\Z)",
			achievements,
			re.MULTILINE | re.DOTALL,
		).group("body")
	]
	missing_name = [achievement_id for achievement_id in achievement_ids if not re.search(r"^" + re.escape(achievement_id) + r"_NAME\s*:", localisation, re.MULTILINE)]
	missing_desc = [achievement_id for achievement_id in achievement_ids if not re.search(r"^" + re.escape(achievement_id) + r"_DESC\s*:", localisation, re.MULTILINE)]
	missing_tooltip = [achievement_id for achievement_id in achievement_ids if not re.search(r"^" + re.escape(achievement_id) + r"_tooltip\s*:", localisation, re.MULTILINE)]
	missing_gfx = []
	missing_dds = []
	missing_manifest = []
	for achievement_id in achievement_ids:
		for suffix in ["", "_grey", "_not_eligible"]:
			sprite = f'GFX_achievement_{achievement_id}{suffix}'
			dds_rel = f"gfx/achievements/{achievement_id}{suffix}.dds"
			if sprite not in gfx or dds_rel not in gfx:
				missing_gfx.append(f"{achievement_id}{suffix}")
			if not (ROOT / dds_rel).exists():
				missing_dds.append(dds_rel)
		if f"`{achievement_id}`" not in manifest:
			missing_manifest.append(achievement_id)

	ok = (
		len(achievement_ids) == EVENT005_ACHIEVEMENT_COUNT
		and not missing_definitions
		and not missing_possible
		and not missing_name
		and not missing_desc
		and not missing_tooltip
		and not missing_gfx
		and not missing_dds
		and not missing_manifest
	)
	return [
		Check(
			"achievement_surface",
			ok,
			(
				f"ids={len(achievement_ids)} definitions_missing={len(missing_definitions)} "
				f"missing_possible={len(missing_possible)} missing_name={len(missing_name)} "
				f"missing_desc={len(missing_desc)} missing_tooltip={len(missing_tooltip)} "
				f"missing_gfx={len(missing_gfx)} missing_dds={len(missing_dds)} "
				f"missing_manifest={len(missing_manifest)}"
			),
		)
	]


def verify_asset_manifest_surface() -> list[Check]:
	manifest_paths = [
		ROOT / "docs/assets/005_soviet_union_collapse/manifest.md",
		ROOT / "docs/assets/005_soviet_union_collapse/achievement_icon_manifest.md",
		ROOT / "docs/assets/005_soviet_union_collapse/republic_focus_and_influence/manifest.md",
		ROOT / "docs/assets/005_soviet_union_collapse/contact_sheets/soviet_collapse_asset_records.tsv",
		ROOT / "docs/super_events/005_soviet_union_collapse_super_event_research.md",
	]
	missing_manifests = [str(path.relative_to(ROOT)) for path in manifest_paths if not path.exists()]
	base_manifest = read_text(manifest_paths[0]) if manifest_paths[0].exists() else ""
	achievement_manifest = read_text(manifest_paths[1]) if manifest_paths[1].exists() else ""
	republic_manifest = read_text(manifest_paths[2]) if manifest_paths[2].exists() else ""
	records = read_text(manifest_paths[3]) if manifest_paths[3].exists() else ""
	super_doc = read_text(manifest_paths[4]) if manifest_paths[4].exists() else ""

	manifest_terms_ok = all(term in base_manifest for term in ["Source PNG", "Processed PNG", "Final DDS", "GFX file", "sourced"])
	achievement_terms_ok = all(term in achievement_manifest for term in ["Source art", "Processed PNG", "Completed DDS", "Grey DDS", "Not eligible DDS"])
	republic_terms_ok = all(term in republic_manifest for term in ["Source PNG", "Processed PNG", "Final DDS", "Sprite", "GFX file"])
	record_lines = len([line for line in records.splitlines() if line.strip()])
	record_header_ok = records.lstrip("\ufeff").startswith("name\tsource_png\tprocessed_png\tfinal_dds")
	super_dds_paths = sorted(set(re.findall(r"Final DDS:\s*`([^`]+\.dds)`", super_doc)))
	missing_super_dds = [path for path in super_dds_paths if not (ROOT / path).exists()]
	representative_assets = [
		"gfx/super_events/super_event_union_unmade.dds",
		"gfx/event_pictures/report_union_crisis.dds",
		"gfx/interface/ideas/soviet_collapse/idea_union_crisis.dds",
		"gfx/achievements/chaosx_ach_soviet_unbroken_signal.dds",
		"docs/assets/005_soviet_union_collapse/contact_sheets/event005_achievement_icons_complete.png",
		"docs/assets/005_soviet_union_collapse/contact_sheets/event005_achievement_icons_not_eligible.png",
	]
	missing_representative = [path for path in representative_assets if not (ROOT / path).exists()]
	ok = (
		not missing_manifests
		and manifest_terms_ok
		and achievement_terms_ok
		and republic_terms_ok
		and record_header_ok
		and record_lines >= 100
		and len(super_dds_paths) >= 10
		and not missing_super_dds
		and not missing_representative
	)
	return [
		Check(
			"asset_manifest_surface",
			ok,
			(
				f"missing_manifests={len(missing_manifests)} base_terms={manifest_terms_ok} "
				f"achievement_terms={achievement_terms_ok} republic_terms={republic_terms_ok} "
				f"record_lines={record_lines} super_dds={len(super_dds_paths)} "
				f"missing_super_dds={len(missing_super_dds)} missing_representative={len(missing_representative)}"
			),
		)
	]


def verify_ai_surface() -> list[Check]:
	decisions = read_text(ROOT / "common/decisions/005_soviet_collapse_decisions.txt")
	decision_blocks: list[tuple[str, list[str]]] = []
	for _, category_body in direct_child_blocks(tokens(decisions)):
		decision_blocks.extend(direct_child_blocks(category_body))

	mission_re = re.compile(r"^soviet_collapse_soviet_mission_\d{3}_")
	regular = [(name, body) for name, body in decision_blocks if not mission_re.match(name)]
	missing_ai = [name for name, body in regular if not top_level_block_bodies(body, "ai_will_do")]
	dynamic_ai = [
		name
		for name, body in regular
		if top_level_block_bodies(body, "ai_will_do")
		and any(token in " ".join(top_level_block_bodies(body, "ai_will_do")[0]) for token in ["modifier", "check_variable", "has_war", "has_country_flag", "has_global_flag"])
	]
	ok = len(regular) >= 120 and not missing_ai and len(dynamic_ai) >= 100
	return [
		Check(
			"decision_ai_surface",
			ok,
			f"regular_decisions={len(regular)} missing_ai={len(missing_ai)} dynamic_ai={len(dynamic_ai)}",
		)
	]


def verify_docs_surface() -> list[Check]:
	event_doc = read_text(ROOT / "docs/events/005_soviet_union_collapse.md")
	completion_audit = read_text(ROOT / "docs/events/005_soviet_union_collapse_completion_audit.md")
	input_audit = read_text(ROOT / "docs/events/005_soviet_union_collapse_input_audit.md")
	required_markers = [
		"## Concrete Success Criteria",
		"## Prompt To Artifact Checklist",
		"## Remaining Blockers",
		"## Blocked Completion Report",
		".tools/verify_event005_completion_gate.py",
		"Strict verifier result",
		"Implementation-gate verifier result",
		"soviet_objective_board_surface",
		"event_log_mapping_surface",
		"focus_layout_surface",
		"first_wave_release_surface",
		"focus_ai_surface",
		"crisis_cause_surface",
	]
	event_markers = [
		"Event Logs event-detail entry for Event 005",
		"soviet_collapse_cleanup_terminal_collapse_missions",
		"Event 005 custom country flags were audited",
		"570 TGA files",
	]
	input_markers = [
		"tmp/005_soviet_union_collapse_event_log_mission_balance_focus_cleanup_spec.md",
		"missing",
		"intentionally removed after fixed errors",
	]
	missing_completion = [marker for marker in required_markers if marker not in completion_audit]
	missing_event = [marker for marker in event_markers if marker not in event_doc]
	missing_input = [marker for marker in input_markers if marker not in input_audit]
	ok = not missing_completion and not missing_event and not missing_input
	return [
		Check(
			"docs_completion_surface",
			ok,
			f"missing_completion={len(missing_completion)} missing_event_doc={len(missing_event)} missing_input_audit={len(missing_input)}",
		)
	]


def xlsx_shared_strings(zip_file: ZipFile) -> list[str]:
	try:
		root = ET.fromstring(zip_file.read("xl/sharedStrings.xml"))
	except KeyError:
		return []
	return [
		"".join((text.text or "") for text in item.findall(".//a:t", XLSX_NS))
		for item in root.findall("a:si", XLSX_NS)
	]


def xlsx_cell_value(cell: ET.Element, shared: list[str]) -> str:
	inline = cell.find("a:is", XLSX_NS)
	if inline is not None:
		return "".join((text.text or "") for text in inline.findall(".//a:t", XLSX_NS))
	value = cell.find("a:v", XLSX_NS)
	if value is None or value.text is None:
		return ""
	raw = value.text
	if cell.attrib.get("t") == "s":
		return shared[int(raw)]
	return raw


def verify_spreadsheet_surface() -> list[Check]:
	path = ROOT / "docs/spreadsheets/chaos_redux_events_catalog.xlsx"
	row_values: dict[str, str] = {}
	formula_count = 0
	with ZipFile(path) as zip_file:
		shared = xlsx_shared_strings(zip_file)
		for sheet_name in [name for name in zip_file.namelist() if name.startswith("xl/worksheets/sheet") and name.endswith(".xml")]:
			root = ET.fromstring(zip_file.read(sheet_name))
			formula_count += len(root.findall(".//a:f", XLSX_NS))
			for row in root.findall(".//a:row", XLSX_NS):
				if row.attrib.get("r") != "6":
					continue
				for cell in row.findall("a:c", XLSX_NS):
					ref = cell.attrib.get("r", "")
					value = xlsx_cell_value(cell, shared)
					if value:
						row_values[ref] = value
	stale_hits = [value for value in row_values.values() if "Missing continuation spec/logs" in value or "Missing logs" in value]
	ok = (
		row_values.get("B6") == "Soviet Union Collapse"
		and row_values.get("L6") == "Implemented - Final Closure Blocked"
		and row_values.get("R6") == "Blocked - Missing continuation spec"
		and not stale_hits
	)
	return [
		Check(
			"spreadsheet_status_surface",
			ok,
			(
				f"B6={row_values.get('B6', '')!r} L6={row_values.get('L6', '')!r} "
				f"R6={row_values.get('R6', '')!r} formula_count={formula_count} stale_status_hits={len(stale_hits)}"
			),
		)
	]


def verify_braces_and_unsupported() -> list[Check]:
	bad_braces = []
	bad_operator = []
	bad_scoped_temp = []
	for path in EVENT005_SCRIPT_FILES + EVENT005_FOCUS_FILES:
		text = read_text(path)
		depth = 0
		min_depth = 0
		for ch in strip_comments(text):
			if ch == "{":
				depth += 1
			elif ch == "}":
				depth -= 1
				min_depth = min(min_depth, depth)
		if depth != 0 or min_depth != 0:
			bad_braces.append(f"{path.relative_to(ROOT)} depth={depth} min={min_depth}")
		if re.search(r"(?<![A-Za-z0-9_])(?:<=|>=)(?![A-Za-z0-9_])", text):
			bad_operator.append(str(path.relative_to(ROOT)))
		if re.search(r"\b(?:ROOT|PREV|FROM|THIS)\.[A-Za-z0-9_]*temp[A-Za-z0-9_]*", text):
			bad_scoped_temp.append(str(path.relative_to(ROOT)))
	return [
		Check("brace_depth", not bad_braces, f"bad_files={len(bad_braces)}"),
		Check("unsupported_operator_scan", not bad_operator, f"files_with_unsupported_operator={len(bad_operator)}"),
		Check("scoped_temp_variable_scan", not bad_scoped_temp, f"files_with_scoped_temp_variables={len(bad_scoped_temp)}"),
	]


def run_checks() -> list[Check]:
	checks: list[Check] = []
	checks.extend(verify_input_files())
	checks.extend(verify_braces_and_unsupported())
	checks.extend(verify_focuses())
	checks.extend(verify_ideas())
	checks.extend(verify_first_wave_and_forces())
	checks.extend(verify_dynamic_force_coverage())
	checks.extend(verify_crisis_balance())
	checks.extend(verify_union_unmade_and_cleanup())
	checks.extend(verify_soviet_objective_board())
	checks.extend(verify_terminal_ordinary_republics())
	checks.extend(verify_terminal_high_chaos_successors())
	checks.extend(verify_localisation_and_event_log())
	checks.extend(verify_localisation_surface())
	checks.extend(verify_flags())
	checks.extend(verify_super_events_and_assets())
	checks.extend(verify_evolution_logging_surface())
	checks.extend(verify_achievement_surface())
	checks.extend(verify_asset_manifest_surface())
	checks.extend(verify_ai_surface())
	checks.extend(verify_docs_surface())
	checks.extend(verify_spreadsheet_surface())
	return checks


def main() -> int:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--allow-missing-continuation-spec", action="store_true", help="return 0 when only the named continuation spec is missing")
	args = parser.parse_args()

	checks = run_checks()
	failures = [check for check in checks if not check.ok and not check.blocker]
	blockers = [check for check in checks if not check.ok and check.blocker]

	for check in checks:
		if check.ok:
			status = "PASS"
		elif check.blocker:
			status = "BLOCKED"
		else:
			status = "FAIL"
		print(f"{status} {check.name}: {check.detail}")

	if failures:
		print(f"\nFAILED implementation checks: {len(failures)}", file=sys.stderr)
		return 1
	if blockers and not args.allow_missing_continuation_spec:
		print(f"\nBLOCKED required inputs: {len(blockers)}", file=sys.stderr)
		return 2
	print("\nEvent 005 implementation gates passed.")
	if blockers:
		print("Missing input blocker was waived for this verifier run.")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
