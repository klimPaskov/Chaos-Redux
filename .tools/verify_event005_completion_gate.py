#!/usr/bin/env python3
"""Verify the Event 005 Soviet Collapse completion gates.

This is a repository-state verifier for the current correction pass. It does
not replace the design review in the completion audit; it preserves the
repeatable parser and surface checks that prove the implementation gates.

Exit codes:
- 0: all implementation gates passed and all required inputs are present.
- 2: implementation gates passed, but a required active source input is still missing.
- 1: one or more implementation gates failed.
"""

from __future__ import annotations

import argparse
import fnmatch
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
	ROOT / "common/mtth/005_soviet_collapse_mtth.txt",
	ROOT / "events/005_soviet_collapse.txt",
]

REQUIRED_INPUTS = [
	"tmp/005_soviet_union_collapse_influence_threat_focus_rework_spec.md",
	"tmp/005_soviet_union_collapse_final_clean_spec_part_1_core_crisis.md",
	"tmp/005_soviet_union_collapse_final_clean_spec_part_2_objectives_missions_intervention.md",
	"tmp/005_soviet_union_collapse_final_clean_spec_part_3_republics_focus_trees.md",
	"tmp/005_soviet_union_collapse_final_clean_spec_part_4_custom_countries_evolutions_assets_achievements.md",
]

ADDITIONAL_CONSULTED_INPUTS = [
	"tmp/005_soviet_union_collapse_threat_mission_focus_rebalance_spec.md",
	"tmp/005_soviet_union_collapse_comprehensive_correction_spec.md",
	"tmp/005_soviet_union_collapse_spawn_balance_collapse_pacing_cleanup_spec.md",
]

REQUIRED_CONTEXT_INPUTS = [
	"AGENTS.md",
	".agents/skills/chaos-redux-events/SKILL.md",
	".agents/skills/chaos-redux-event-assets/SKILL.md",
	".agents/skills/chaos-redux-super-events/SKILL.md",
]

REQUIRED_REFERENCE_INPUTS = [
	"paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md",
	"paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md",
	"paradox_wiki/Effect - Hearts of Iron 4 Wiki.md",
	"paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md",
	"paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md",
	"paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md",
	"paradox_wiki/On actions - Hearts of Iron 4 Wiki.md",
	"paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md",
	"paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md",
	"paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md",
	"paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md",
	"paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md",
	"/home/klim/projects/Hearts of Iron IV/documentation/effects_documentation.md",
	"/home/klim/projects/Hearts of Iron IV/documentation/triggers_documentation.md",
	"/home/klim/projects/Hearts of Iron IV/documentation/modifiers_documentation.md",
	"/home/klim/projects/Hearts of Iron IV/documentation/script_concept_documentation.md",
]

REQUIRED_SOURCE_ORDER = [
	"tmp/005_soviet_union_collapse_influence_threat_focus_rework_spec.md",
	"tmp/005_soviet_union_collapse_final_clean_spec_part_1_core_crisis.md",
	"tmp/005_soviet_union_collapse_final_clean_spec_part_2_objectives_missions_intervention.md",
	"tmp/005_soviet_union_collapse_final_clean_spec_part_3_republics_focus_trees.md",
	"tmp/005_soviet_union_collapse_final_clean_spec_part_4_custom_countries_evolutions_assets_achievements.md",
	"AGENTS.md",
	"chaos-redux-events",
	"chaos-redux-event-assets",
	"chaos-redux-super-events",
]

RECOVERY_SEARCH_PATTERNS = [
	"005_soviet_union_collapse_event_log_mission_balance_focus_cleanup_spec.md",
	"*event_log*mission*balance*focus*cleanup*",
	"*mission_balance_focus*",
	"*focus_cleanup*spec.md",
]

CUSTOM_TAGS = [
	"CFR", "MFR", "KRS", "FTH", "BBH", "BSC", "TNC", "ALA", "UDC", "SDZ",
	"GAC", "DHC", "KHC", "FEV", "SZA", "UWD", "MRC", "IUL", "BAC", "ARD",
	"NLC",
]

DISABLED_CUSTOM_TAGS = [
	"OGB", "ICD", "RMC", "RCD", "ILU", "PRA", "TSC", "BLT", "NRF", "TRS",
	"SEP", "DSC", "COU", "BEC", "RLD", "LID", "IRA",
]

DISABLED_SOVIET_OBJECTIVE_MISSIONS = {
	"soviet_collapse_soviet_mission_090_contain_the_grave_registers",
	"soviet_collapse_soviet_mission_109_classify_the_impossible_reports",
	"soviet_collapse_soviet_mission_110_guard_the_hospitals_from_politics",
	"soviet_collapse_soviet_mission_112_deny_the_star_iron_rumor",
	"soviet_collapse_soviet_mission_113_break_the_funeral_train_schedule",
	"soviet_collapse_soviet_mission_114_prevent_the_crown_from_leaving_the_archive",
	"soviet_collapse_soviet_mission_115_silence_the_wrong_resurrection_committee",
	"soviet_collapse_soviet_mission_116_seal_the_northern_fleet_signals",
	"soviet_collapse_soviet_mission_117_keep_the_priests_out_of_the_war_room",
	"soviet_collapse_soviet_mission_118_order_the_graves_counted_by_the_living",
}

DISABLED_OBJECTIVE_TRIGGERS = {
	"can_contain_soviet_collapse_grave_registers",
	"can_classify_soviet_collapse_impossible_reports",
	"can_guard_soviet_collapse_hospitals_from_politics",
	"can_deny_soviet_collapse_star_iron_rumor",
	"can_break_soviet_collapse_funeral_train_schedule",
	"can_prevent_soviet_collapse_crown_leaving_archive",
	"can_silence_soviet_collapse_wrong_resurrection_committee",
	"can_seal_soviet_collapse_northern_fleet_signals",
	"can_keep_soviet_collapse_priests_out_of_war_room",
	"can_order_soviet_collapse_graves_counted_by_living",
}

DISABLED_OBJECTIVE_FLAGS = {
	"soviet_collapse_grave_registers_failed",
	"soviet_collapse_impossible_reports_classified",
	"soviet_collapse_hospital_records_guarded",
	"soviet_collapse_star_iron_rumor_denied",
	"soviet_collapse_crown_kept_in_archive",
	"soviet_collapse_northern_fleet_signals_unsealed",
	"soviet_collapse_graves_counted_by_living_offices",
}

DISABLED_ACHIEVEMENT_IDS = {
	"chaosx_ach_pale_timetable",
	"chaosx_ach_dead_are_citizens",
	"chaosx_ach_no_discharge_from_grave",
	"chaosx_ach_star_iron_over_tunguska",
	"chaosx_ach_last_tsar_in_snow",
	"chaosx_ach_bulgaria_on_volga",
	"chaosx_ach_bolghar_on_the_volga",
}

ORDINARY_REPUBLIC_TAGS = ["UKR", "BLR", "MOL", "LIT", "LAT", "EST", "GEO", "ARM", "AZR", "UZB", "KYR", "TAJ", "TMS", "KAZ"]
FIRST_WAVE_WESTERN_TAGS = ["UKR", "BLR", "MOL", "LIT", "LAT", "EST"]
FIRST_WAVE_CAUCASUS_TAGS = ["GEO", "ARM", "AZR"]
FIRST_WAVE_CENTRAL_ASIA_TAGS = ["UZB", "KYR", "TAJ", "TMS"]
IDEOLOGIES = ["communism", "democratic", "fascism", "neutrality"]
BANNED_PHRASE = "starts from a low dynamic baseline in calm conditions"
XLSX_NS = {"a": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
EVENT005_ACHIEVEMENT_COUNT = 40

DISABLED_TAG_REGISTRATION_TAGS = [tag for tag in DISABLED_CUSTOM_TAGS if tag != "OGB"]

DISABLED_DECISION_CATEGORIES = {
	"soviet_collapse_volga_restoration",
	"soviet_collapse_iron_commissariat",
	"soviet_collapse_red_martyrs_resurrection_cult",
	"soviet_collapse_red_cosmist_directorate",
	"soviet_collapse_iron_liturgy_of_the_urals",
	"soviet_collapse_pale_railway_authority",
	"soviet_collapse_tunguska_star_committee",
	"soviet_collapse_brotherhood_of_the_last_tsar",
	"soviet_collapse_northern_revenant_fleet",
	"soviet_collapse_third_rome_emergency_synod",
	"soviet_collapse_sepulchre_soviet",
	"soviet_collapse_dead_soldiers_congress",
	"soviet_collapse_commissariat_of_the_unburied",
	"soviet_collapse_black_earth_resurrection_cult",
	"soviet_collapse_red_lazarus_directorate",
	"soviet_collapse_last_international_of_the_dead",
	"soviet_collapse_iron_resurrection_army",
}

DISABLED_EFFECT_BLOCKS = {
	"soviet_collapse_show_dead_are_citizens_super_event",
	"soviet_collapse_apply_ogb_claim_volga_crossings",
	"soviet_collapse_apply_ogb_convene_bolghar_scholars",
	"soviet_collapse_apply_ogb_focus_legitimacy_gain",
	"soviet_collapse_apply_ogb_focus_river_trade",
	"soviet_collapse_apply_ogb_focus_patrols",
	"soviet_collapse_apply_ogb_focus_foreign_contacts",
	"soviet_collapse_apply_ogb_focus_sacred_restoration",
	"soviet_collapse_complete_dead_state_endgame",
	"soviet_collapse_complete_red_martyrs_endgame",
	"soviet_collapse_complete_red_cosmist_endgame",
	"soviet_collapse_complete_iron_liturgy_endgame",
	"soviet_collapse_complete_pale_railway_endgame",
	"soviet_collapse_complete_tunguska_endgame",
	"soviet_collapse_complete_last_tsar_endgame",
	"soviet_collapse_complete_northern_revenant_endgame",
	"soviet_collapse_complete_third_rome_endgame",
	"soviet_collapse_complete_sepulchre_endgame",
	"soviet_collapse_complete_dead_soldiers_endgame",
	"soviet_collapse_complete_unburied_endgame",
	"soviet_collapse_complete_black_earth_endgame",
	"soviet_collapse_complete_red_lazarus_endgame",
	"soviet_collapse_complete_last_international_dead_endgame",
	"soviet_collapse_complete_iron_resurrection_endgame",
}

for _disabled_tag in DISABLED_CUSTOM_TAGS:
	DISABLED_EFFECT_BLOCKS.add(f"soviet_collapse_setup_{_disabled_tag.lower()}_successor")
	DISABLED_EFFECT_BLOCKS.add(f"soviet_collapse_spawn_{_disabled_tag.lower()}_if_enabled")


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


def segments_cross(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int], d: tuple[int, int]) -> bool:
	if len({a, b, c, d}) < 4:
		return False
	def ccw(p: tuple[int, int], q: tuple[int, int], r: tuple[int, int]) -> bool:
		return (r[1] - p[1]) * (q[0] - p[0]) > (q[1] - p[1]) * (r[0] - p[0])
	return ccw(a, c, d) != ccw(b, c, d) and ccw(a, b, c) != ccw(a, b, d)


def verify_focuses() -> list[Check]:
	focuses = []
	layout_rows = []
	reward_bodies = []
	max_visual_prereq_dx = 44
	for path in EVENT005_FOCUS_FILES:
		toks = tokens(read_text(path))
		for block in named_blocks(toks, "focus"):
			ids = top_level_values(block, "id")
			if ids:
				focuses.append((path, ids[0], block))
				rewards = top_level_block_bodies(block, "completion_reward")
				if rewards:
					reward_bodies.append((ids[0], " ".join(rewards[0])))
		for tree_body in named_blocks(toks, "focus_tree"):
			tree_ids = top_level_values(tree_body, "id")
			tree_id = tree_ids[0] if tree_ids else "<missing>"
			continuous_blocks = top_level_block_bodies(tree_body, "continuous_focus_position")
			continuous_x = None
			continuous_y = None
			if continuous_blocks:
				xs = top_level_values(continuous_blocks[0], "x")
				ys = top_level_values(continuous_blocks[0], "y")
				continuous_x = xs[0] if xs else None
				continuous_y = ys[0] if ys else None
			tree_focuses = []
			tree_prereq_edges = []
			tree_mutual_edges = []
			for focus_body in top_level_block_bodies(tree_body, "focus"):
				ids = top_level_values(focus_body, "id")
				xs = top_level_values(focus_body, "x")
				ys = top_level_values(focus_body, "y")
				if ids and xs and ys and xs[0].lstrip("-").isdigit() and ys[0].lstrip("-").isdigit():
					tree_focuses.append((ids[0], int(xs[0]), int(ys[0])))
					for prereq_body in top_level_block_bodies(focus_body, "prerequisite"):
						block_refs = collect_focus_refs([prereq_body])
						for ref in block_refs:
							tree_prereq_edges.append((ref, ids[0], len(block_refs) > 1))
					for ref in collect_focus_refs(top_level_block_bodies(focus_body, "mutually_exclusive")):
						tree_mutual_edges.append((ids[0], ref))
			if tree_focuses:
				x_values = [x for _, x, _ in tree_focuses]
				y_values = [y for _, _, y in tree_focuses]
				coords = [(x, y) for _, x, y in tree_focuses]
				coord_by_id = {focus_id: (x, y) for focus_id, x, y in tree_focuses}
				edges = [(src, dst) for src, dst, _ in tree_prereq_edges if src in coord_by_id and dst in coord_by_id]
				hard_edges = [(src, dst) for src, dst, is_or in tree_prereq_edges if not is_or and src in coord_by_id and dst in coord_by_id]
				mutual_edges = [(src, dst) for src, dst in tree_mutual_edges if src in coord_by_id and dst in coord_by_id]
				mutual_distances = [
					abs(coord_by_id[src][0] - coord_by_id[dst][0]) + abs(coord_by_id[src][1] - coord_by_id[dst][1])
					for src, dst in mutual_edges
				]
				connected_focuses = {focus_id for edge in edges for focus_id in edge}
				graph = {focus_id: set() for focus_id, _, _ in tree_focuses}
				for src, dst in edges:
					graph[src].add(dst)
					graph[dst].add(src)
				parents = {focus_id: set() for focus_id, _, _ in tree_focuses}
				children = {focus_id: set() for focus_id, _, _ in tree_focuses}
				for src, dst in edges:
					parents[dst].add(src)
					children[src].add(dst)
				seen_components = set()
				component_count = 0
				for focus_id, _, _ in tree_focuses:
					if focus_id in seen_components:
						continue
					component_count += 1
					stack = [focus_id]
					seen_components.add(focus_id)
					while stack:
						current = stack.pop()
						for neighbor in graph[current]:
							if neighbor not in seen_components:
								seen_components.add(neighbor)
								stack.append(neighbor)
				edge_crossings = 0
				for edge_index, first_edge in enumerate(hard_edges):
					for second_edge in hard_edges[edge_index + 1:]:
						if segments_cross(coord_by_id[first_edge[0]], coord_by_id[first_edge[1]], coord_by_id[second_edge[0]], coord_by_id[second_edge[1]]):
							edge_crossings += 1
				edge_dx_values = [
					abs(coord_by_id[src][0] - coord_by_id[dst][0])
					for src, dst in edges
				]
				visual_detached_edges = sum(1 for edge_dx in edge_dx_values if edge_dx > max_visual_prereq_dx)
				shallow_dead_end_focuses = sum(
					1
					for focus_id, (_, y) in coord_by_id.items()
					if not children[focus_id] and y < max(y_values)
				)
				layout_rows.append(
					{
						"path": path,
						"tree_id": tree_id,
						"count": len(tree_focuses),
						"min_x": min(x_values),
						"max_x": max(x_values),
						"min_y": min(y_values),
						"max_y": max(y_values),
						"x_span": max(x_values) - min(x_values),
						"y_span": max(y_values) - min(y_values),
						"duplicate_coords": len(coords) - len(set(coords)),
						"max_col": max(x_values.count(x) for x in set(x_values)),
						"max_row": max(y_values.count(y) for y in set(y_values)),
						"edge_crossings": edge_crossings,
						"max_edge_dx": max(edge_dx_values) if edge_dx_values else 0,
						"visual_detached_edges": visual_detached_edges,
						"isolated_focuses": len(tree_focuses) - len(connected_focuses),
						"root_count": sum(1 for focus_id in coord_by_id if not parents[focus_id]),
						"terminal_leaf_count": sum(1 for focus_id in coord_by_id if not children[focus_id]),
						"shallow_dead_end_focuses": shallow_dead_end_focuses,
						"component_count": component_count,
						"min_mutual_distance": min(mutual_distances) if mutual_distances else 99,
						"continuous_x": continuous_x,
						"continuous_y": continuous_y,
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
	republic_multi_focus_prerequisites = []
	republic_hidden_focus_gates_without_visible_links = []
	republic_hidden_focus_gates_requiring_visible_links = {
		"blr_soviet_collapse_which_road_is_belarus",
		"kaz_soviet_collapse_the_congress_chooses_a_past",
	}
	allowed_republic_or_prerequisite_focuses = {
		"ukr_soviet_collapse_last_harvest_plan",
		"blr_soviet_collapse_which_road_is_belarus",
		"central_asia_soviet_collapse_the_southern_shield",
		"kaz_soviet_collapse_the_congress_chooses_a_past",
		"kaz_soviet_collapse_the_steppe_arsenal",
		"kaz_soviet_collapse_the_steppe_keeps_many_memories",
		"kaz_soviet_collapse_the_steppe_outlives_the_union",
	}
	ai_block_count = 0
	dynamic_ai = 0
	mutual_focus_count = 0
	dynamic_mutual_ai = 0
	flat_mutual_ai = 0

	for path, focus_id, block in focuses:
		prereq_refs = collect_focus_refs(top_level_block_bodies(block, "prerequisite"))
		if path.name == "005_soviet_collapse_republics.txt":
			for prereq_block in top_level_block_bodies(block, "prerequisite"):
				block_refs = collect_focus_refs([prereq_block])
				if len(block_refs) > 1 and focus_id not in allowed_republic_or_prerequisite_focuses:
					republic_multi_focus_prerequisites.append((focus_id, len(block_refs)))
		mutual_blocks = top_level_block_bodies(block, "mutually_exclusive")
		mutual_refs = collect_focus_refs(mutual_blocks)
		completed_refs = re.findall(r"\bhas_completed_focus\s*=\s*([A-Za-z0-9_]+)", " ".join(block))
		if path.name == "005_soviet_collapse_republics.txt" and focus_id in republic_hidden_focus_gates_requiring_visible_links:
			for ref in completed_refs:
				if ref not in prereq_refs:
					republic_hidden_focus_gates_without_visible_links.append((focus_id, ref))
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
		for ref in prereq_refs + mutual_refs + completed_refs:
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

	continuous_bad = []
	for row in layout_rows:
		x = row["continuous_x"]
		y = row["continuous_y"]
		if x is None or y is None or not x.lstrip("-").isdigit() or not y.lstrip("-").isdigit():
			continuous_bad.append((row["tree_id"], x, y, "missing_or_non_numeric"))
			continue
		x_int = int(x)
		y_int = int(y)
		min_right_panel_x = (row["max_x"] + 4) * 96
		if x_int < min_right_panel_x or y_int < 120 or y_int > 300:
			continuous_bad.append((row["tree_id"], x, y, f"expected_right_panel_x_at_least_{min_right_panel_x}_and_y_120_300"))
	layout_bad = [
		row
		for row in layout_rows
		if row["duplicate_coords"] != 0
		or row["edge_crossings"] != 0
		or row["visual_detached_edges"] != 0
		or row["isolated_focuses"] != 0
		or row["root_count"] != 1
		or row["terminal_leaf_count"] != 1
		or row["shallow_dead_end_focuses"] != 0
		or row["component_count"] != 1
		or row["y_span"] > 14
		or row["min_mutual_distance"] < 7
		or row["max_row"] > 22
		or row["max_col"] > 14
	]
	crossing_free_count = sum(1 for row in layout_rows if row["edge_crossings"] == 0)
	continuous_positions = sum(1 for row in layout_rows if row["continuous_x"] is not None and row["continuous_y"] is not None)
	reward_counts: dict[str, int] = {}
	for _, reward_body in reward_bodies:
		reward_counts[reward_body] = reward_counts.get(reward_body, 0) + 1
	duplicate_reward_groups = sum(1 for count in reward_counts.values() if count > 1)
	duplicate_reward_focuses = sum(count for count in reward_counts.values() if count > 1)
	reward_category_markers = [
		"add_ideas",
		"add_building_construction",
		"create_unit",
		"division_template",
		"add_equipment_to_stockpile",
		"add_manpower",
		"set_country_flag",
		"add_to_variable",
		"country_event",
		"add_political_power",
		"add_stability",
		"add_war_support",
	]
	reward_categories = sum(1 for marker in reward_category_markers if any(marker in body for _, body in reward_bodies))
	add_idea_rewards = sum(1 for _, body in reward_bodies if "add_ideas" in body)
	ok = not any([
		duplicates, missing_refs, self_refs, nonreciprocal, repeated_mutual_blocks,
		missing_ai, missing_reward, missing_icon, missing_coords,
		republic_multi_focus_prerequisites,
		republic_hidden_focus_gates_without_visible_links,
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
				f"missing_coords={len(missing_coords)} republic_multi_focus_prerequisites={len(republic_multi_focus_prerequisites)} "
				f"hidden_focus_gates_without_visible_links={len(republic_hidden_focus_gates_without_visible_links)} "
				f"continuous_positions={continuous_positions} "
				f"continuous_bad={len(continuous_bad)}"
			),
		),
		Check(
			"focus_layout_surface",
			not layout_bad and not continuous_bad and continuous_positions == len(layout_rows) and crossing_free_count == len(layout_rows),
			(
				f"focus_trees={len(layout_rows)} continuous_positions={continuous_positions} "
				f"layout_bad={len(layout_bad)} duplicate_coord_trees={sum(1 for row in layout_rows if row['duplicate_coords'])} "
				f"continuous_side_bad={len(continuous_bad)} crossing_free={crossing_free_count} "
				f"edge_crossings={sum(row['edge_crossings'] for row in layout_rows)} "
				f"visual_detached_edges={sum(row['visual_detached_edges'] for row in layout_rows)} "
				f"max_edge_dx={max((row['max_edge_dx'] for row in layout_rows), default=0)} "
				f"isolated_focuses={sum(row['isolated_focuses'] for row in layout_rows)} "
				f"single_root_trees={sum(1 for row in layout_rows if row['root_count'] == 1)}/{len(layout_rows)} "
				f"terminal_leaf_trees={sum(1 for row in layout_rows if row['terminal_leaf_count'] == 1)}/{len(layout_rows)} "
				f"shallow_dead_end_focuses={sum(row['shallow_dead_end_focuses'] for row in layout_rows)} "
				f"disconnected_trees={sum(1 for row in layout_rows if row['component_count'] != 1)} "
				f"deep_trees={sum(1 for row in layout_rows if row['y_span'] > 18)} "
				f"tight_mutual_trees={sum(1 for row in layout_rows if row['min_mutual_distance'] < 7)} "
				f"min_x_span={min((row['x_span'] for row in layout_rows), default=0)} "
				f"min_y_span={min((row['y_span'] for row in layout_rows), default=0)} "
				f"max_y_span={max((row['y_span'] for row in layout_rows), default=0)} "
				f"min_mutual_distance={min((row['min_mutual_distance'] for row in layout_rows), default=99)} "
				f"max_col={max((row['max_col'] for row in layout_rows), default=0)} "
				f"max_row={max((row['max_row'] for row in layout_rows), default=0)}"
			),
		),
		Check(
			"focus_reward_variety_surface",
			duplicate_reward_groups == 0 and reward_categories >= 8 and add_idea_rewards <= len(focuses) // 4,
			(
				f"focuses={len(focuses)} duplicate_reward_groups={duplicate_reward_groups} "
				f"duplicate_reward_focuses={duplicate_reward_focuses} reward_categories={reward_categories} "
				f"add_idea_rewards={add_idea_rewards}"
			),
		),
		Check(
			"focus_ai_surface",
			(
				ai_block_count == len(focuses)
				and dynamic_ai >= max(180, len(focuses) // 4)
				and mutual_focus_count >= 70
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


def event005_focus_tree_counts() -> dict[str, int]:
	tree_counts: dict[str, int] = {}
	for path in EVENT005_FOCUS_FILES:
		for tree_body in named_blocks(tokens(read_text(path)), "focus_tree"):
			tree_ids = top_level_values(tree_body, "id")
			if tree_ids:
				tree_counts[tree_ids[0]] = len(top_level_block_bodies(tree_body, "focus"))
	return tree_counts


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
	gfx_compact = " ".join(tokens("\n".join(read_text(gfx_path) for gfx_path in (ROOT / "interface").glob("*.gfx"))))
	idea_sprites = {
		match.group(1): match.group(2)
		for match in re.finditer(r'name\s*=\s*"?(GFX_idea_[A-Za-z0-9_]+)"?\s*texturefile\s*=\s*"?([^"\s]+)"?', gfx_compact)
	}
	localisation_text = "\n".join(
		read_text(loc_path)
		for loc_path in (ROOT / "localisation/english").glob("*.yml")
		if loc_path.exists()
	)
	localisation_keys = set(re.findall(r"^\s*([A-Za-z0-9_.-]+):\s*\"", localisation_text, re.MULTILINE))
	idea_blocks: list[tuple[str, list[str]]] = []
	for ideas_body in named_blocks(toks, "ideas"):
		for group_name, group_body in direct_child_blocks(ideas_body):
			if group_name in {"country", "country_leader", "army_chief", "navy_chief", "air_chief"}:
				idea_blocks.extend(direct_child_blocks(group_body))

	no_modifier = []
	weak_lt3 = []
	tiny_only = []
	modifier_counts = []
	total_modifier_entries = 0
	tiny_components = 0
	unresolved_constants = 0
	missing_picture = []
	missing_sprite = []
	missing_dds = []
	missing_name = []
	missing_desc = []
	for idea_id, block in idea_blocks:
		pictures = top_level_values(block, "picture")
		if not pictures:
			missing_picture.append(idea_id)
		else:
			sprite = f"GFX_idea_{pictures[0]}"
			dds = idea_sprites.get(sprite)
			if not dds:
				missing_sprite.append(idea_id)
			elif not (ROOT / dds).exists():
				missing_dds.append(idea_id)
		if idea_id not in localisation_keys:
			missing_name.append(idea_id)
		if f"{idea_id}_desc" not in localisation_keys:
			missing_desc.append(idea_id)
		values = modifier_values(block, constants)
		if not values:
			no_modifier.append(idea_id)
			continue
		total_modifier_entries += len(values)
		modifier_counts.append(len(values))
		if len(values) < 3:
			weak_lt3.append(idea_id)
		numeric = [abs(value) for value in values if value is not None]
		tiny_components += sum(1 for value in numeric if value <= 0.03)
		unresolved_constants += sum(1 for value in values if value is None)
		if numeric and all(value <= 0.03 for value in numeric):
			tiny_only.append(idea_id)

	ok = not no_modifier and not weak_lt3 and not tiny_only and len(idea_blocks) >= 90
	package_ok = (
		ok
		and total_modifier_entries >= 300
		and tiny_components <= 25
		and unresolved_constants == 0
		and not missing_picture
		and not missing_sprite
		and not missing_dds
		and not missing_name
		and not missing_desc
	)
	return [
		Check(
			"idea_strength",
			ok,
			(
				f"ideas={len(idea_blocks)} no_modifier={len(no_modifier)} weak_lt3={len(weak_lt3)} "
				f"tiny_only={len(tiny_only)} min_modifiers={min(modifier_counts) if modifier_counts else 0} "
				f"max_modifiers={max(modifier_counts) if modifier_counts else 0}"
			),
		),
		Check(
			"idea_package_surface",
			package_ok,
			(
				f"ideas={len(idea_blocks)} modifier_entries={total_modifier_entries} "
				f"tiny_components={tiny_components} unresolved_constants={unresolved_constants} "
				f"missing_picture={len(missing_picture)} missing_sprite={len(missing_sprite)} "
				f"missing_dds={len(missing_dds)} missing_name={len(missing_name)} "
				f"missing_desc={len(missing_desc)}"
			),
		),
	]


def verify_breakaway_recovery_surface() -> list[Check]:
	effects_text = read_text(ROOT / "common/scripted_effects/005_soviet_collapse_effects.txt")
	decisions_text = read_text(ROOT / "common/decisions/005_soviet_collapse_decisions.txt")
	docs_text = read_text(ROOT / "docs/events/005_soviet_union_collapse.md")
	constants = parse_script_constants(read_text(ROOT / "common/script_constants/005_soviet_collapse_constants.txt"))
	effect_tokens = tokens(effects_text)
	setup_blocks = named_blocks(effect_tokens, "soviet_collapse_apply_breakaway_setup_package")
	recovery_blocks = named_blocks(effect_tokens, "soviet_collapse_check_republic_recovery")
	starting_ideas = []
	if setup_blocks:
		setup_text = " ".join(setup_blocks[0])
		starting_ideas = re.findall(r"\badd_ideas?\s*=\s*([A-Za-z0-9_]+)", setup_text)
	recovery_text = " ".join(recovery_blocks[0]) if recovery_blocks else ""
	breakaway_decision_block = ""
	for category_name, category_body in direct_child_blocks(tokens(decisions_text)):
		if category_name == "soviet_collapse_breakaway_category":
			breakaway_decision_block = " ".join(category_body)
			break
	breakaway_decisions = re.findall(r"\bsoviet_collapse_(?:request_foreign_recognition|mobilize_defense_units|seize_depots|coordinate_fronts)\s*=", breakaway_decision_block)
	decision_progress_refs = effects_text.count("soviet_collapse_add_republic_decision_recovery_progress = yes")
	focus_progress_refs = effects_text.count("soviet_collapse_add_republic_focus_recovery_progress = yes")
	recovery_constants = {
		"partial": constants.get("soviet_collapse_breakaway_recovery.partial_recovery"),
		"complete": constants.get("soviet_collapse_breakaway_recovery.recovery_complete"),
		"decision": constants.get("soviet_collapse_breakaway_recovery.decision_progress"),
		"focus": constants.get("soviet_collapse_breakaway_recovery.focus_progress"),
	}
	setup_ok = starting_ideas == ["soviet_collapse_republican_startup_disorder"]
	recovery_ok = all(
		marker in recovery_text
		for marker in [
			"swap_ideas",
			"remove_idea = soviet_collapse_republican_startup_disorder",
			"add_idea = soviet_collapse_republican_startup_disorder_mitigated",
			"remove_ideas = soviet_collapse_republican_startup_disorder",
			"remove_ideas = soviet_collapse_republican_startup_disorder_mitigated",
			"add_ideas = soviet_collapse_emergency_administration_stabilized",
			"soviet_collapse_republic_startup_disorder_resolved",
		]
	)
	progress_ok = (
		len(breakaway_decisions) == 4
		and decision_progress_refs >= 4
		and focus_progress_refs >= 6
		and recovery_constants == {"partial": 2.0, "complete": 4.0, "decision": 1.0, "focus": 1.0}
	)
	docs_ok = all(
		marker in docs_text
		for marker in [
			"A newly released republic starts with `soviet_collapse_republican_startup_disorder`",
			"remove it and add `soviet_collapse_emergency_administration_stabilized`",
		]
	)
	return [
		Check(
			"breakaway_recovery_surface",
			setup_ok and recovery_ok and progress_ok and docs_ok,
			(
				f"starting_ideas={len(starting_ideas)} setup_only_disorder={setup_ok} "
				f"recovery_swap_remove={recovery_ok} breakaway_decisions={len(breakaway_decisions)} "
				f"decision_progress_refs={decision_progress_refs} focus_progress_refs={focus_progress_refs} "
				f"constants={recovery_constants} docs={docs_ok}"
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


def verify_source_context_files() -> list[Check]:
	missing = []
	details = []
	for rel in REQUIRED_CONTEXT_INPUTS:
		path = ROOT / rel
		if not path.exists():
			missing.append(rel)
			continue
		text = read_text(path)
		details.append(f"{rel}:{len(text.splitlines())}l:{path.stat().st_size}b:{sha256(path)[:12]}")
	return [
		Check(
			"source_context_files",
			not missing and len(details) == len(REQUIRED_CONTEXT_INPUTS),
			f"files={len(details)}/{len(REQUIRED_CONTEXT_INPUTS)} missing={len(missing)} {' '.join(details)}",
		)
	]


def verify_reference_context_surface() -> list[Check]:
	completion_audit = read_text(ROOT / "docs/events/005_soviet_union_collapse_completion_audit.md")
	missing_files = []
	for rel in REQUIRED_REFERENCE_INPUTS:
		path = Path(rel) if rel.startswith("/") else ROOT / rel
		if not path.exists():
			missing_files.append(rel)
	required_markers = [
		"Reference context surface",
		"offline Paradox wiki snapshot",
		"Vanilla documentation",
		"Data structures",
		"Triggers",
		"Effects",
		"Modifiers",
		"Localisation",
		"Scopes",
		"On actions",
		"Event modding",
		"Decision modding",
		"Idea modding",
		"AI modding",
		"National focus modding",
		"effects_documentation.md",
		"triggers_documentation.md",
		"modifiers_documentation.md",
		"script_concept_documentation.md",
	]
	missing_markers = [marker for marker in required_markers if marker not in completion_audit]
	return [
		Check(
			"reference_context_surface",
			not missing_files and not missing_markers,
			(
				f"files={len(REQUIRED_REFERENCE_INPUTS) - len(missing_files)}/{len(REQUIRED_REFERENCE_INPUTS)} "
				f"markers={len(required_markers) - len(missing_markers)}/{len(required_markers)}"
			),
		)
	]


def verify_source_order_surface() -> list[Check]:
	completion_audit = read_text(ROOT / "docs/events/005_soviet_union_collapse_completion_audit.md")
	try:
		source_order = completion_audit.split("## Source Order", 1)[1].split("## Input File Audit", 1)[0]
	except IndexError:
		return [Check("source_order_surface", False, "source_order_section=False")]
	missing = [item for item in REQUIRED_SOURCE_ORDER if item not in source_order]
	positions = [source_order.find(item) for item in REQUIRED_SOURCE_ORDER]
	ordered = positions == sorted(positions)
	numbered = all(f"{index}. " in source_order for index in range(1, len(REQUIRED_SOURCE_ORDER) + 1))
	return [
		Check(
			"source_order_surface",
			not missing and ordered and numbered,
			f"items={len(REQUIRED_SOURCE_ORDER) - len(missing)}/{len(REQUIRED_SOURCE_ORDER)} ordered={ordered} numbered={numbered}",
		)
	]


def verify_input_audit_surface() -> list[Check]:
	input_audit = read_text(ROOT / "docs/events/005_soviet_union_collapse_input_audit.md")
	expected_rows = []
	for rel in REQUIRED_INPUTS + ADDITIONAL_CONSULTED_INPUTS + REQUIRED_CONTEXT_INPUTS:
		path = ROOT / rel
		if path.exists():
			text = read_text(path)
			expected_rows.append(f"| `{rel}` | present | {len(text.splitlines())} | {path.stat().st_size} | `{sha256(path)}` |")
		else:
			expected_rows.append(f"| `{rel}` | missing | 0 | 0 | n/a |")
	for rel in ["tmp/error.log", "tmp/text.log"]:
		expected_rows.append(f"| `{rel}` | intentionally removed after fixed errors | 0 | 0 | n/a |")
	missing_rows = [row for row in expected_rows if row not in input_audit]
	return [
		Check(
			"input_audit_surface",
			not missing_rows,
			f"rows={len(expected_rows) - len(missing_rows)}/{len(expected_rows)} mismatches={len(missing_rows)}",
		)
	]


def verify_recovery_search_surface() -> list[Check]:
	matches = []
	for path in ROOT.rglob("*"):
		if not path.is_file():
			continue
		relative = path.relative_to(ROOT)
		if ".git" in relative.parts:
			continue
		relative_text = relative.as_posix().lower()
		name = path.name.lower()
		if any(fnmatch.fnmatch(name, pattern) or fnmatch.fnmatch(relative_text, pattern) for pattern in RECOVERY_SEARCH_PATTERNS):
			matches.append(relative.as_posix())
	log_hits = [rel for rel in ["tmp/error.log", "tmp/text.log"] if (ROOT / rel).exists()]
	return [
		Check(
			"recovery_search_surface",
			not matches and not log_hits,
			f"continuation_matches={len(matches)} removed_log_hits={len(log_hits)}",
		)
	]


def verify_final_completion_report_surface() -> list[Check]:
	completion_audit = read_text(ROOT / "docs/events/005_soviet_union_collapse_completion_audit.md")
	required_markers = [
		"## Final Completion Report",
		"## Resume Packet",
		"The requested final completion report categories are closed by current repository evidence.",
		"Historical missing continuation context",
		"not part of the active required source order",
		"`tmp/error.log` and `tmp/text.log` runtime logs were intentionally removed",
		"strict verifier exits 0",
	]
	missing = [marker for marker in required_markers if marker not in completion_audit]
	return [
		Check(
			"final_completion_report_surface",
			not missing,
			f"markers={len(required_markers) - len(missing)}/{len(required_markers)} missing={len(missing)}",
		)
	]


def verify_strict_verifier_documentation_surface() -> list[Check]:
	completion_audit = read_text(ROOT / "docs/events/005_soviet_union_collapse_completion_audit.md")
	try:
		strict_result = completion_audit.split("Strict verifier result:", 1)[1].split("Current prompt-to-artifact spot audit", 1)[0]
	except IndexError:
		return [Check("strict_verifier_documentation_surface", False, "strict_section=False")]
	required_markers = [
		"python3 .tools/verify_event005_completion_gate.py",
		"result: exit 0; all implementation gates and active required-input gates passed",
	]
	forbidden_markers = [
		"result: exit 2",
		"Missing input blocker was waived",
	]
	missing = [marker for marker in required_markers if marker not in strict_result]
	forbidden = [marker for marker in forbidden_markers if marker in strict_result]
	return [
		Check(
			"strict_verifier_documentation_surface",
			not missing and not forbidden,
			f"markers={len(required_markers) - len(missing)}/{len(required_markers)} forbidden={len(forbidden)}",
		)
	]


def verify_missing_continuation_direct_coverage_surface() -> list[Check]:
	completion_audit = read_text(ROOT / "docs/events/005_soviet_union_collapse_completion_audit.md")
	required_markers = [
		"Missing continuation direct coverage",
		"event-log",
		"mission-balance",
		"focus-cleanup",
		"event_log_detail_surface",
		"event_log_mapping_surface",
		"soviet_objective_board_surface",
		"terminal_mission_cleanup",
		"focus_integrity",
		"focus_layout_surface",
		"focus_ai_surface",
		"focus_tree_map_surface",
		"not part of the active required source order",
	]
	missing = [marker for marker in required_markers if marker not in completion_audit]
	return [
		Check(
			"missing_continuation_direct_coverage_surface",
			not missing,
			f"markers={len(required_markers) - len(missing)}/{len(required_markers)} missing={len(missing)}",
		)
	]


def verify_resume_validation_commands_surface() -> list[Check]:
	completion_audit = read_text(ROOT / "docs/events/005_soviet_union_collapse_completion_audit.md")
	try:
		resume_packet = completion_audit.split("## Resume Packet", 1)[1]
	except IndexError:
		return [Check("resume_validation_commands_surface", False, "resume_packet=False")]
	required_markers = [
		"Resume validation commands:",
		"python3 -m py_compile .tools/verify_event005_completion_gate.py",
		"git diff --check",
		"python3 .tools/verify_event005_completion_gate.py",
		"git status --short",
		"The strict verifier must exit 0 before marking the active Event 005 correction goal complete",
	]
	missing = [marker for marker in required_markers if marker not in resume_packet]
	return [
		Check(
			"resume_validation_commands_surface",
			not missing,
			f"markers={len(required_markers) - len(missing)}/{len(required_markers)} missing={len(missing)}",
		)
	]


def verify_success_criteria_surface() -> list[Check]:
	completion_audit = read_text(ROOT / "docs/events/005_soviet_union_collapse_completion_audit.md")
	try:
		criteria = completion_audit.split("## Concrete Success Criteria", 1)[1].split("## Prompt To Artifact Checklist", 1)[0]
	except IndexError:
		return [Check("success_criteria_surface", False, "criteria_section=False")]
	required_markers = [
		"weak Event 005 ideas and spirits",
		"opening release wave is randomized",
		"Kazakhstan is separately gated",
		"dynamically scaled manpower, equipment, templates, and units",
		"Union Crisis Threat and Moscow Authority",
		"Union Unmade cannot fire during the ordinary first month",
		"unreleased ordinary Soviet republics are released",
		"full-collapse cleanup cancels or hides obsolete Soviet Collapse intervention categories and active missions",
		"runtime focus trees have clean layout",
		"Soviet Collapse flags are orientation-audited",
		"player-facing localisation contains no removed design-language baseline wording",
		"AI, docs, spreadsheet status, event log details, evolutions, super-events, assets",
		"every active source input is present and audited",
	]
	missing = [marker for marker in required_markers if marker not in criteria]
	return [
		Check(
			"success_criteria_surface",
			not missing,
			f"markers={len(required_markers) - len(missing)}/{len(required_markers)} missing={len(missing)}",
		)
	]


def verify_available_source_acceptance_surface() -> list[Check]:
	spawn_spec = read_text(ROOT / "tmp/005_soviet_union_collapse_spawn_balance_collapse_pacing_cleanup_spec.md")
	completion_audit = read_text(ROOT / "docs/events/005_soviet_union_collapse_completion_audit.md")
	source_markers = [
		"Soviet Collapse ideas have meaningful effect packages and are not mostly tiny modifiers",
		"the first wave is randomized across structured pools",
		"the first wave includes at least one western or eastern European actor, one Caucasus republic, and one Central Asian republic when map state allows",
		"Kazakhstan is not a normal first-wave default and is tied to southern cascade logic",
		"first-wave size scales with chaos and Soviet condition",
		"released republics spawn with dynamically scaled units",
		"Union Crisis Threat no longer reaches 100 too easily",
		"Moscow Authority does not start at 0 in calm or modest crisis conditions",
		"Union Unmade cannot fire in the first month in ordinary play",
		"Union Unmade releases all ordinary Soviet republics still under Moscow control",
		"high chaos adds special chaos countries on top of ordinary republic releases",
		"highest chaos terminal failure releases all eligible special chaos countries",
		"final collapse releases each republic with dynamically scaled units",
		"Soviet Collapse intervention categories and active missions are canceled or converted after terminal collapse",
		"continuous focus boxes are moved to a cleaner location",
		"focus trees are more visually readable",
		"duplicate focuses are removed or rewritten",
		"upside-down flags are fixed",
		"removed design-language localisation is replaced with in-world text",
		"AI behavior, docs, event log, achievements, and completion report reflect these corrections",
	]
	audit_markers = [
		"Available source acceptance criteria coverage",
		"available_source_acceptance_surface",
		"idea_package_surface",
		"first_wave_release_surface",
		"force_scaling_surface",
		"crisis_balance_surface",
		"union_unmade_pacing",
		"terminal_ordinary_republic_release_surface",
		"terminal_high_chaos_successor_surface",
		"terminal_mission_cleanup",
		"focus_layout_surface",
		"focus_tree_map_surface",
		"flag_orientation_surface",
		"banned_phrase_cleanup",
		"event_log_mapping_surface",
		"achievement_surface",
		"docs_completion_surface",
	]
	missing_source = [marker for marker in source_markers if marker not in spawn_spec]
	missing_audit = [marker for marker in audit_markers if marker not in completion_audit]
	return [
		Check(
			"available_source_acceptance_surface",
			not missing_source and not missing_audit,
			(
				f"source_markers={len(source_markers) - len(missing_source)}/{len(source_markers)} "
				f"audit_markers={len(audit_markers) - len(missing_audit)}/{len(audit_markers)}"
			),
		)
	]


def verify_comprehensive_source_acceptance_surface() -> list[Check]:
	comprehensive_spec = read_text(ROOT / "tmp/005_soviet_union_collapse_comprehensive_correction_spec.md")
	completion_audit = read_text(ROOT / "docs/events/005_soviet_union_collapse_completion_audit.md")
	source_markers = [
		"This file is the source of truth for the next correction pass",
		"Event log window details are mandatory",
		"Evolutions are not baseline stages",
		"Mission duration correction",
		"Decision cost corrections",
		"Blocked decision and cost localisation",
		"Remove design-language localisation",
		"Threat balance correction",
		"Moscow Authority correction",
		"Stronger Soviet Collapse ideas",
		"Random first-wave release rules",
		"Chaos-scaled opening size and support",
		"Starting divisions and release force scaling",
		"Union Unmade pacing",
		"Union Unmade release rule",
		"Terminal collapse unit packages",
		"Cleanup after full Soviet collapse",
		"Focus tree cleanup",
		"Flag orientation fix",
		"Acceptance criteria",
	]
	audit_markers = [
		"Comprehensive source-of-truth coverage",
		"comprehensive_source_acceptance_surface",
		"event_log_detail_surface",
		"evolution_logging_surface",
		"soviet_objective_board_surface",
		"decision cost corrections",
		"banned_phrase_cleanup",
		"crisis_balance_surface",
		"crisis_cause_surface",
		"idea_package_surface",
		"first_wave_release_surface",
		"force_scaling_surface",
		"union_unmade_pacing",
		"terminal_mission_cleanup",
		"focus_layout_surface",
		"flag_orientation_surface",
		"docs_completion_surface",
	]
	missing_source = [marker for marker in source_markers if marker not in comprehensive_spec]
	missing_audit = [marker for marker in audit_markers if marker not in completion_audit]
	return [
		Check(
			"comprehensive_source_acceptance_surface",
			not missing_source and not missing_audit,
			(
				f"source_markers={len(source_markers) - len(missing_source)}/{len(source_markers)} "
				f"audit_markers={len(audit_markers) - len(missing_audit)}/{len(audit_markers)}"
			),
		)
	]


def verify_prompt_artifact_checklist_surface() -> list[Check]:
	completion_audit = read_text(ROOT / "docs/events/005_soviet_union_collapse_completion_audit.md")
	try:
		checklist = completion_audit.split("## Prompt To Artifact Checklist", 1)[1].split("## Current Focus Counts", 1)[0]
	except IndexError:
		return [Check("prompt_artifact_checklist_surface", False, "checklist_section=False")]
	required_rows = [
		"Missing continuation direct coverage",
		"Comprehensive source-of-truth coverage",
		"Available source acceptance criteria coverage",
		"Stronger Soviet Collapse ideas and spirits",
		"Random first wave from structured pools",
		"Kazakhstan first-wave restraint",
		"Dynamic starting force packages",
		"Union Crisis Threat and Moscow Authority pacing",
		"Soviet goal-style objectives with capacity limits",
		"Longer varied Soviet mission deadlines",
		"Decision cost corrections",
		"Foreign intervention categories and action-based aid",
		"Crisis decision AI behavior",
		"Runtime focus trees for republics and breakaways",
		"High-chaos successor focus trees",
		"Non-linear focus structure, route locks, branch zones, focus filters, AI behavior",
		"Focus tree map documentation",
		"Starting divisions for appearing republics and serious splinters",
		"Union Unmade first-month lock",
		"Terminal ordinary republic release",
		"Terminal high-chaos successor activation",
		"Terminal mission and category cleanup",
		"Event log details",
		"Evolution logging",
		"Super-events",
		"Asset reuse and created assets",
		"Flag orientation audit",
		"Localisation design-language cleanup",
		"Spreadsheet updates",
		"Completion readiness",
	]
	missing = [row for row in required_rows if f"| {row} |" not in checklist]
	implemented_rows = checklist.count("| Implemented")
	blocked_rows = checklist.count("| Not closed")
	return [
		Check(
			"prompt_artifact_checklist_surface",
			not missing and implemented_rows >= 25 and blocked_rows == 0,
			f"rows={len(required_rows) - len(missing)}/{len(required_rows)} implemented_rows={implemented_rows} blocked_rows={blocked_rows}",
		)
	]


def verify_verifier_command_documentation_surface() -> list[Check]:
	completion_audit = read_text(ROOT / "docs/events/005_soviet_union_collapse_completion_audit.md")
	required_markers = [
		"Verifier exit meanings:",
		"`0`: all implementation gates passed and every required input is present.",
		"`2`: implementation gates passed but one or more required active source inputs are missing.",
		"`1`: one or more implementation gates failed.",
		"python3 .tools/verify_event005_completion_gate.py",
		"result: exit 0; all implementation gates and active required-input gates passed",
	]
	missing = [marker for marker in required_markers if marker not in completion_audit]
	return [
		Check(
			"verifier_command_documentation_surface",
			not missing,
			f"markers={len(required_markers) - len(missing)}/{len(required_markers)} missing={len(missing)}",
		)
	]


def verify_focus_tree_map_documentation_surface() -> list[Check]:
	event_doc = read_text(ROOT / "docs/events/005_soviet_union_collapse.md")
	completion_audit = read_text(ROOT / "docs/events/005_soviet_union_collapse_completion_audit.md")
	actual_counts = event005_focus_tree_counts()
	required_markers = [
		"## Republic Focus Trees",
		"The implemented trees are:",
		"soviet_collapse_ukraine_focus_tree",
		"soviet_collapse_belarus_focus_tree",
		"soviet_collapse_kazakhstan_focus_tree",
		"soviet_collapse_breakaway_focus_tree",
		"CFR_soviet_collapse_focus_tree",
		"NLC_soviet_collapse_focus_tree",
		"Continuous focus windows",
	]
	missing = [marker for marker in required_markers if marker not in event_doc]
	audit_markers = [
		"Focus tree map documentation",
		"focus_tree_map_surface",
		"post-cleanup focus-tree map",
	]
	missing_audit = [marker for marker in audit_markers if marker not in completion_audit]
	event_count_mismatches = []
	audit_count_mismatches = []
	for tree_id, actual_count in actual_counts.items():
		event_counts = [
			int(match)
			for match in re.findall(rf"`{re.escape(tree_id)}`[^\n]*?:\s*(\d+)\s+focuses", event_doc)
		]
		if len(event_counts) != 1 or event_counts[0] != actual_count:
			event_count_mismatches.append((tree_id, actual_count, event_counts))
		audit_counts = [
			int(match)
			for match in re.findall(rf"^{re.escape(tree_id)}\s+(\d+)\s*$", completion_audit, re.MULTILINE)
		]
		if len(audit_counts) != 1 or audit_counts[0] != actual_count:
			audit_count_mismatches.append((tree_id, actual_count, audit_counts))
	return [
		Check(
			"focus_tree_map_surface",
			not missing and not missing_audit and not event_count_mismatches and not audit_count_mismatches,
			(
				f"event_markers={len(required_markers) - len(missing)}/{len(required_markers)} "
				f"audit_markers={len(audit_markers) - len(missing_audit)}/{len(audit_markers)} "
				f"counted_trees={len(actual_counts)} event_count_mismatches={len(event_count_mismatches)} "
				f"audit_count_mismatches={len(audit_count_mismatches)}"
			),
		)
	]


def verify_mission_audit_documentation_surface() -> list[Check]:
	decisions = read_text(ROOT / "common/decisions/005_soviet_collapse_decisions.txt")
	event_doc = read_text(ROOT / "docs/events/005_soviet_union_collapse.md")
	completion_audit = read_text(ROOT / "docs/events/005_soviet_union_collapse_completion_audit.md")
	audit_path = ROOT / "docs/events/005_soviet_union_collapse_mission_audit.md"
	if not audit_path.exists():
		return [Check("mission_audit_documentation_surface", False, "doc_exists=False")]
	audit_doc = read_text(audit_path)
	mission_ids = set(re.findall(r"^\s*(soviet_collapse_soviet_mission_\d{3}_[A-Za-z0-9_]+)\s*=\s*\{", decisions, re.MULTILINE))
	table_ids = set(re.findall(r"\bsoviet_collapse_soviet_mission_\d{3}_[A-Za-z0-9_]+\b", audit_doc))
	table_rows = len(re.findall(r"^\| \d{3} `soviet_collapse_soviet_mission_", audit_doc, re.MULTILINE))
	expected_rows = len(mission_ids)
	header = "| Mission | Owner | Purpose | Requirement | Success effect | Failure effect | Duplicate risk |"
	required_markers = [
		header,
		"Trivial passive missions",
		"Division-state and map requirements",
		"Long trigger details",
		"soviet_objective_board_surface",
		"mission_quality_surface",
		"localisation_surface",
		"terminal_mission_cleanup",
	]
	validation_markers = [
		"mission_audit_documentation_surface",
		f"rows {expected_rows}",
		f"mission_ids {expected_rows}/{expected_rows}",
		"validation_markers 4/4",
	]
	missing_markers = [marker for marker in required_markers if marker not in audit_doc]
	missing_validation = [marker for marker in validation_markers if marker not in completion_audit]
	ok = (
		not missing_markers
		and not missing_validation
		and table_rows == expected_rows
		and mission_ids
		and mission_ids <= table_ids
		and "005_soviet_union_collapse_mission_audit.md" in event_doc
		and "Mission audit table" in completion_audit
	)
	return [
		Check(
			"mission_audit_documentation_surface",
			ok,
			(
				f"rows={table_rows} mission_ids={len(mission_ids & table_ids)}/{len(mission_ids)} "
				f"header={header in audit_doc} validation_markers={len(validation_markers) - len(missing_validation)}/{len(validation_markers)} "
				f"missing_markers={len(missing_markers)}"
			),
		)
	]


def verify_validation_snapshot_freshness_surface() -> list[Check]:
	completion_audit = read_text(ROOT / "docs/events/005_soviet_union_collapse_completion_audit.md")
	required_markers = [
		"validation_snapshot_freshness_surface",
		"terminal_high_chaos_successor_surface prepare_flags 18 spawn_calls 21/21 ready_trigger_refs 21",
		"highest_chaos_prepare_flags 18",
	]
	stale_markers = [
		"terminal_high_chaos_spawn_gates_with_required_flags 35",
	]
	missing = [marker for marker in required_markers if marker not in completion_audit]
	stale = [marker for marker in stale_markers if marker in completion_audit]
	return [
		Check(
			"validation_snapshot_freshness_surface",
			not missing and not stale,
			f"markers={len(required_markers) - len(missing)}/{len(required_markers)} stale={len(stale)}",
		)
	]


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
	constants = parse_script_constants(read_text(ROOT / "common/script_constants/005_soviet_collapse_constants.txt"))
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
	force_package_vars = [
		"soviet_collapse_breakaway_manpower_package",
		"soviet_collapse_breakaway_infantry_equipment_package",
		"soviet_collapse_breakaway_support_equipment_package",
		"soviet_collapse_breakaway_artillery_equipment_package",
		"soviet_collapse_breakaway_guard_unit_count",
		"soviet_collapse_breakaway_field_unit_count",
	]
	base_scaling = all(
		f"set_temp_variable = {{ {var} = constant:soviet_collapse_breakaway_support.base_" in package_body
		for var in force_package_vars
	)
	major_scaling = (
		"tag = UKR" in package_body
		and "tag = KAZ" in package_body
		and all(f"constant:soviet_collapse_breakaway_support.major_{suffix}" in package_body for suffix in ["manpower_bonus", "infantry_equipment_bonus", "support_equipment_bonus", "artillery_equipment_bonus", "guard_units_bonus", "field_units_bonus"])
	)
	regional_scaling = (
		all(f"tag = {tag}" in package_body for tag in ["BLR", "GEO", "AZR", "UZB", "LIT", "LAT", "EST"])
		and all(f"constant:soviet_collapse_breakaway_support.regional_{suffix}" in package_body for suffix in ["manpower_bonus", "infantry_equipment_bonus", "support_equipment_bonus", "artillery_equipment_bonus", "field_units_bonus"])
	)
	chaos_scaling = (
		package_body.count("extra_manpower_per_chaos_band") == 4
		and package_body.count("extra_infantry_equipment_per_chaos_band") == 4
		and package_body.count("extra_field_units_per_chaos_band") == 4
		and all(f"has_global_flag = {{ flag = chaos_tier value = {tier} }}" in package_body for tier in [2, 3, 4, 5])
	)
	condition_scaling = all(
		item in package_body
		for item in [
			"SOV = { exists = yes has_war = yes }",
			"constant:soviet_collapse_breakaway_support.soviet_war_manpower_bonus",
			"check_variable = { var = soviet_collapse_moscow_authority value = constant:soviet_collapse_soviet_objective.contested_authority compare = less_than }",
			"check_variable = { var = soviet_collapse_total_collapse_threat value = constant:soviet_collapse_soviet_objective.deep_collapse_threat compare = greater_than }",
			"constant:soviet_collapse_breakaway_support.weak_center_manpower_bonus",
			"check_variable = { var = soviet_collapse_depot_vulnerability value = constant:soviet_collapse_breakaway_support.high_depot_vulnerability_gate compare = greater_than }",
			"constant:soviet_collapse_breakaway_support.depot_pressure_manpower_bonus",
			"check_variable = { var = soviet_collapse_foreign_appetite value = constant:soviet_collapse_breakaway_support.high_foreign_appetite_gate compare = greater_than }",
			"constant:soviet_collapse_breakaway_support.foreign_access_manpower_bonus",
			"has_global_flag = soviet_collapse_terminal_collapse_in_progress",
			"constant:soviet_collapse_breakaway_support.terminal_manpower_bonus",
		]
	)
	declaration_scaling = all(
		item in package_body
		for item in [
			"soviet_collapse_next_declaration_unarmed",
			"soviet_collapse_next_declaration_armed",
			"constant:soviet_collapse_breakaway_support.preempted_declaration_manpower",
			"constant:soviet_collapse_breakaway_support.emboldened_declaration_manpower",
			"clr_country_flag = soviet_collapse_next_declaration_unarmed",
			"clr_country_flag = soviet_collapse_next_declaration_armed",
		]
	)
	unit_delivery = all(
		item in package_body
		for item in [
			"clamp_temp_variable = { var = soviet_collapse_breakaway_field_unit_count min = 0 max = 12 }",
			"add_manpower = var:soviet_collapse_breakaway_manpower_package",
			"amount = var:soviet_collapse_breakaway_infantry_equipment_package",
			"amount = var:soviet_collapse_breakaway_support_equipment_package",
			"amount = var:soviet_collapse_breakaway_artillery_equipment_package",
			"Emergency Republican Guard",
			"Emergency Republican Field Brigade",
			"GUARD_UNIT_COUNT = \"[?soviet_collapse_breakaway_guard_unit_count|.0]\"",
			"FIELD_UNIT_COUNT = \"[?soviet_collapse_breakaway_field_unit_count|.0]\"",
		]
	)
	constant_surface = all(
		f"soviet_collapse_breakaway_support.{key}" in constants
		for key in [
			"base_manpower",
			"base_infantry_equipment",
			"base_guard_units",
			"regional_manpower_bonus",
			"major_manpower_bonus",
			"extra_manpower_per_chaos_band",
			"soviet_war_manpower_bonus",
			"weak_center_manpower_bonus",
			"high_depot_vulnerability_gate",
			"depot_pressure_manpower_bonus",
			"high_foreign_appetite_gate",
			"foreign_access_manpower_bonus",
			"terminal_manpower_bonus",
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
	scaling_ok = all([
		base_scaling, major_scaling, regional_scaling, chaos_scaling,
		condition_scaling, declaration_scaling, unit_delivery, constant_surface,
	])
	return [
		Check(
			"dynamic_force_coverage",
			ok,
			(
				f"setup_helpers={len(setup_blocks)} package_helpers={len(package_blocks)} southern_helpers={len(southern_blocks)} "
				f"custom_successor_setup_refs={custom_setup_refs}/{len(CUSTOM_TAGS)} "
				f"ordinary_release_paths={ordinary_release_paths} package_dynamic={package_dynamic_ok}"
			),
		),
		Check(
			"force_scaling_surface",
			scaling_ok,
			(
				f"base={base_scaling} major={major_scaling} regional={regional_scaling} "
				f"chaos_bands={chaos_scaling} conditions={condition_scaling} "
				f"declarations={declaration_scaling} unit_delivery={unit_delivery} constants={constant_surface}"
			),
		),
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


def verify_mtth_release_surface() -> list[Check]:
	mtth_path = ROOT / "common/mtth/005_soviet_collapse_mtth.txt"
	mtth = read_text(mtth_path) if mtth_path.exists() else ""
	effects = read_text(ROOT / "common/scripted_effects/005_soviet_collapse_effects.txt")
	events = read_text(ROOT / "events/005_soviet_collapse.txt")
	loc = read_text(ROOT / "localisation/english/005_soviet_collapse_l_english.yml")
	docs = read_text(ROOT / "docs/events/005_soviet_union_collapse.md")
	mtth_doc_path = ROOT / "docs/events/005_soviet_union_collapse_mtth_releases.md"
	mtth_doc = read_text(mtth_doc_path) if mtth_doc_path.exists() else ""
	constants = read_text(ROOT / "common/script_constants/005_soviet_collapse_constants.txt")
	event_tokens = tokens(events)
	event_blocks = {}
	for block in named_blocks(event_tokens, "country_event"):
		ids = top_level_values(block, "id")
		if ids:
			event_blocks[ids[0]] = " ".join(block)

	mtth_entries_ok = all(
		entry in mtth
		for entry in [
			"soviet_collapse_progressive_release_weight",
			"soviet_collapse_progressive_release_miss_weight",
			"base = constant:soviet_collapse_release_mtth.release_base",
			"base = constant:soviet_collapse_release_mtth.miss_base",
		]
	)
	mtth_factor_markers = [
		"soviet_collapse_total_collapse_threat",
		"soviet_collapse_moscow_authority",
		"soviet_collapse_military_obedience",
		"soviet_collapse_breakaway_count",
		"soviet_collapse_depot_vulnerability",
		"soviet_collapse_foreign_appetite",
		"soviet_collapse_league_cohesion",
		"soviet_collapse_evolution_weirdness",
		"is_soviet_collapse_southern_breakaway_active",
		"soviet_collapse_union_archives_failed",
		"has_global_flag = { flag = chaos_tier value = 5 }",
	]
	mtth_factors_ok = all(marker in mtth for marker in mtth_factor_markers)
	effect_surface_ok = all(
		marker in effects
		for marker in [
			"set_temp_variable = { soviet_collapse_progressive_release_weight = mtth:soviet_collapse_progressive_release_weight }",
			"set_temp_variable = { soviet_collapse_progressive_release_miss_weight = mtth:soviet_collapse_progressive_release_miss_weight }",
			"soviet_collapse_fire_progressive_release_event",
			"country_event = { id = chaosx.nr5.130 }",
			"country_event = { id = chaosx.nr5.137 }",
			"has_soviet_collapse_three_smaller_central_asian_republics_free = yes",
		]
	) and "constant:soviet_collapse_progressive_release.critical_release_weight" not in effects
	event_ids = [f"chaosx.nr5.{event_id}" for event_id in range(130, 138)]
	event_surface_ok = all(
		event_id in event_blocks
		and "is_triggered_only = yes" in event_blocks[event_id]
		and "soviet_collapse_release_one_threat_breakaway_republic = yes" in event_blocks[event_id]
		and "picture = GFX_report_union_crisis" in event_blocks[event_id]
		for event_id in event_ids
	)
	loc_surface_ok = all(
		f"{event_id}.t:" in loc and f"{event_id}.d:" in loc and f"{event_id}.a:" in loc
		for event_id in event_ids
	)
	constant_surface_ok = all(
		marker in constants
		for marker in [
			"soviet_collapse_release_mtth",
			"release_base",
			"miss_base",
			"weak_authority_add",
			"weak_obedience_add",
			"failed_mission_add",
			"cause_league_weight",
		]
	)
	doc_surface_ok = all(
		marker in docs + "\n" + mtth_doc
		for marker in [
			"common/mtth/005_soviet_collapse_mtth.txt",
			"MTTH",
			"chaosx.nr5.130",
			"chaosx.nr5.137",
			"GFX_report_union_crisis",
			"has_soviet_collapse_three_smaller_central_asian_republics_free",
		]
	)
	ok = (
		mtth_path.exists()
		and mtth_entries_ok
		and mtth_factors_ok
		and effect_surface_ok
		and event_surface_ok
		and loc_surface_ok
		and constant_surface_ok
		and doc_surface_ok
	)
	return [
		Check(
			"mtth_release_surface",
			ok,
			(
				f"mtth_file={mtth_path.exists()} entries={mtth_entries_ok} factors={mtth_factors_ok} "
				f"effects={effect_surface_ok} events={sum(1 for event_id in event_ids if event_id in event_blocks)}/8 "
				f"loc={loc_surface_ok} constants={constant_surface_ok} docs={doc_surface_ok}"
			),
		)
	]


def crisis_scenario(constants: dict[str, float], *, tier: int = 0, low_stability: bool = False, low_war_support: bool = False, active_war: bool = False, capital_lost: bool = False, fired_major_events: int = 0, world_threat_sources: int = 0) -> tuple[float, float]:
	authority = constants["soviet_collapse_baseline.moscow_authority"]
	confidence = constants["soviet_collapse_baseline.republic_confidence"]
	obedience = constants["soviet_collapse_baseline.military_obedience"]
	depot = constants["soviet_collapse_baseline.depot_vulnerability"]
	foreign = constants["soviet_collapse_baseline.foreign_appetite"]
	league = constants["soviet_collapse_baseline.league_cohesion"]
	weirdness = constants["soviet_collapse_baseline.evolution_weirdness"]

	if fired_major_events > 0:
		confidence += fired_major_events * constants["soviet_collapse_opening_pressure.prior_major_event_republic_confidence"]
		authority += fired_major_events * constants["soviet_collapse_opening_pressure.prior_major_event_authority"]
	if world_threat_sources > 0:
		authority += constants["soviet_collapse_opening_pressure.active_world_threat_authority"]
		obedience += constants["soviet_collapse_opening_pressure.active_world_threat_obedience"]
		foreign += constants["soviet_collapse_opening_pressure.active_world_threat_foreign_appetite"]
		foreign += world_threat_sources * constants["soviet_collapse_opening_pressure.active_world_threat_source_foreign_appetite"]

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


THREAT_COMPONENT_WEIGHTS = {
	"soviet_collapse_moscow_authority": -1,
	"soviet_collapse_military_obedience": -1,
	"soviet_collapse_republic_confidence": 1,
	"soviet_collapse_depot_vulnerability": 1,
	"soviet_collapse_foreign_appetite": 1,
	"soviet_collapse_league_cohesion": 1,
	"soviet_collapse_evolution_weirdness": 1,
}


def resolve_numeric_token(token: str, constants: dict[str, float]) -> float | None:
	if token.startswith("constant:"):
		return constants.get(token.removeprefix("constant:"))
	try:
		return float(token)
	except ValueError:
		return None


def effect_variable_deltas(body: list[str], constants: dict[str, float]) -> dict[str, float]:
	deltas: dict[str, float] = {}
	for block in top_level_block_bodies(body, "add_to_variable"):
		if len(block) >= 3 and block[1] == "=":
			var = block[0]
			value = resolve_numeric_token(block[2], constants)
		else:
			vars_ = top_level_values(block, "var")
			values = top_level_values(block, "value")
			var = vars_[0] if vars_ else ""
			value = resolve_numeric_token(values[0], constants) if values else None
		if var and value is not None:
			deltas[var] = deltas.get(var, 0) + value
	for block in top_level_block_bodies(body, "subtract_from_variable"):
		if len(block) >= 3 and block[1] == "=":
			var = block[0]
			value = resolve_numeric_token(block[2], constants)
		else:
			vars_ = top_level_values(block, "var")
			values = top_level_values(block, "value")
			var = vars_[0] if vars_ else ""
			value = resolve_numeric_token(values[0], constants) if values else None
		if var and value is not None:
			deltas[var] = deltas.get(var, 0) - value
	return deltas


def objective_pressure_success_audit(effect_tokens: list[str], constants: dict[str, float]) -> tuple[int, int, int, float, list[str]]:
	success_names = sorted(
		{
			token
			for token in effect_tokens
			if re.fullmatch(r"soviet_collapse_apply_successful(?:_[A-Za-z0-9]+)*_objective_pressure", token)
		}
	)
	non_increasing = 0
	bad_component_changes = 0
	max_net_delta = -999.0
	missing_or_unresolved: list[str] = []
	multiplier = constants.get("soviet_collapse_baseline.total_threat_multiplier", 1)
	for name in success_names:
		blocks = named_blocks(effect_tokens, name)
		if len(blocks) != 1:
			missing_or_unresolved.append(name)
			continue
		deltas = effect_variable_deltas(blocks[0], constants)
		if not deltas:
			missing_or_unresolved.append(name)
			continue
		net_delta = 0.0
		for var, delta in deltas.items():
			if var not in THREAT_COMPONENT_WEIGHTS:
				continue
			component_delta = THREAT_COMPONENT_WEIGHTS[var] * delta
			net_delta += component_delta
			if component_delta > 0:
				bad_component_changes += 1
		net_delta *= multiplier
		max_net_delta = max(max_net_delta, net_delta)
		if net_delta <= 0:
			non_increasing += 1
	return len(success_names), non_increasing, bad_component_changes, max_net_delta, missing_or_unresolved


def objective_pressure_failure_pacing_audit(effect_tokens: list[str], constants: dict[str, float], calm_threat: float) -> tuple[int, float, float, list[str]]:
	ordinary_failure_names = [
		"soviet_collapse_apply_failed_authority_objective_pressure",
		"soviet_collapse_apply_failed_legal_objective_pressure",
		"soviet_collapse_apply_failed_command_objective_pressure",
		"soviet_collapse_apply_failed_rail_objective_pressure",
		"soviet_collapse_apply_failed_depot_objective_pressure",
		"soviet_collapse_apply_failed_cleanup_objective_pressure",
	]
	max_net_delta = 0.0
	missing_or_unresolved: list[str] = []
	multiplier = constants.get("soviet_collapse_baseline.total_threat_multiplier", 1)
	for name in ordinary_failure_names:
		blocks = named_blocks(effect_tokens, name)
		if len(blocks) != 1:
			missing_or_unresolved.append(name)
			continue
		deltas = effect_variable_deltas(blocks[0], constants)
		if not deltas:
			missing_or_unresolved.append(name)
			continue
		net_delta = sum(THREAT_COMPONENT_WEIGHTS.get(var, 0) * delta for var, delta in deltas.items())
		net_delta *= multiplier
		max_net_delta = max(max_net_delta, net_delta)
	months_to_eighty = (80 - calm_threat) / max_net_delta if max_net_delta > 0 else 99.0
	return len(ordinary_failure_names), max_net_delta, months_to_eighty, missing_or_unresolved


def verify_crisis_balance() -> list[Check]:
	constants = parse_script_constants(read_text(ROOT / "common/script_constants/005_soviet_collapse_constants.txt"))
	effects = read_text(ROOT / "common/scripted_effects/005_soviet_collapse_effects.txt")
	events = read_text(ROOT / "events/005_soviet_collapse.txt")
	effect_tokens = tokens(effects)
	calm_authority, calm_threat = crisis_scenario(constants)
	tier1_authority, tier1_threat = crisis_scenario(constants, tier=1)
	severe_authority, severe_threat = crisis_scenario(constants, tier=5, low_stability=True, low_war_support=True, active_war=True, capital_lost=True)
	prior_memory_authority, prior_memory_threat = crisis_scenario(constants, fired_major_events=4, world_threat_sources=2)
	recalculate_blocks = named_blocks(effect_tokens, "soviet_collapse_recalculate_total_threat")
	initialize_blocks = named_blocks(effect_tokens, "soviet_collapse_initialize_crisis_values")
	monthly_guard_blocks = named_blocks(effect_tokens, "soviet_collapse_apply_monthly_threat_guard")
	recalculate_body = " ".join(recalculate_blocks[0]) if recalculate_blocks else ""
	initialize_body = " ".join(initialize_blocks[0]) if initialize_blocks else ""
	monthly_guard_body = " ".join(monthly_guard_blocks[0]) if monthly_guard_blocks else ""
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
		and "refresh_world_threat_state = yes" in initialize_body
		and "count_fired_major_events = yes" in initialize_body
		and "set_temp_variable = { soviet_collapse_current_event_id = constant:soviet_collapse_high_chaos_event_log.event_id }" in initialize_body
		and "is_in_array = { global.fired_events = soviet_collapse_current_event_id }" in initialize_body
		and "subtract_from_temp_variable = { major_events_count = 1 }" in initialize_body
		and "check_variable = { major_events_count > 0 }" in initialize_body
		and all(f"soviet_collapse_opening_pressure.{marker}" in constants and marker in initialize_body for marker in [
			"prior_major_event_republic_confidence",
			"prior_major_event_authority",
			"active_world_threat_authority",
			"active_world_threat_obedience",
			"active_world_threat_foreign_appetite",
			"active_world_threat_source_foreign_appetite",
		])
		and all(marker in initialize_body for marker in [
			"has_global_flag = world_in_threat",
			"global.world_threat_source_count",
			"soviet_collapse_active_world_threat_sources",
		])
		and not re.search(r"\bworld_threat_source_(?!count\b)[A-Za-z0-9_]+", initialize_body)
		and all(f"has_global_flag = {{ flag = chaos_tier value = {tier} }}" in initialize_body for tier in [1, 2, 3, 4, 5])
		and "has_stability < constant:soviet_collapse_soviet_objective.good_stability" in initialize_body
		and "has_war_support < constant:soviet_collapse_soviet_objective.good_war_support" in initialize_body
		and "has_war = yes" in initialize_body
		and "NOT = { capital_scope = { is_controlled_by = ROOT } }" in initialize_body
		and "soviet_collapse_recalculate_total_threat = yes" in initialize_body
	)
	first_wave_pressure_surface = all(
		marker in effects
		for marker in [
			"first_wave_breakaway_republic_confidence",
			"first_wave_breakaway_depot_vulnerability",
			"first_wave_breakaway_foreign_appetite",
			"first_wave_major_republic_confidence",
			"first_wave_regional_republic_confidence",
			"clr_global_flag = soviet_collapse_opening_wave_active",
		]
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
			and "soviet_collapse_register_monthly_threat_success = yes" in success_body
			and "soviet_collapse_register_monthly_threat_failure = yes" in failure_body
			and "soviet_collapse_recalculate_total_threat = yes" in success_body
			and "soviet_collapse_recalculate_total_threat = yes" in failure_body
		):
			covered_pressure_families += 1
	monthly_success_regs = effects.count("soviet_collapse_register_monthly_threat_success = yes")
	monthly_failure_regs = effects.count("soviet_collapse_register_monthly_threat_failure = yes")
	success_helper_count, non_increasing_success_helpers, bad_success_component_changes, max_success_delta, unresolved_success_helpers = objective_pressure_success_audit(effect_tokens, constants)
	ordinary_failure_helper_count, max_ordinary_failure_delta, ordinary_failure_months_to_eighty, unresolved_ordinary_failure_helpers = objective_pressure_failure_pacing_audit(effect_tokens, constants, calm_threat)
	event129_guard = bool(re.search(r"id\s*=\s*chaosx\.nr5\.129[\s\S]*?soviet_collapse_apply_monthly_threat_guard\s*=\s*yes[\s\S]*?soviet_collapse_maybe_release_threat_breakaway\s*=\s*yes", events))
	monthly_guard_ok = (
		constants.get("soviet_collapse_threat_guard.calm_threat_ceiling", 100) <= 40
		and constants.get("soviet_collapse_threat_guard.moderate_threat_ceiling", 100) <= 60
		and constants.get("soviet_collapse_threat_guard.calm_success_month_cap", 100) <= 1
		and constants.get("soviet_collapse_threat_guard.moderate_success_month_cap", 100) <= 4
		and "set_variable = { soviet_collapse_last_month_total_threat = soviet_collapse_total_collapse_threat }" in initialize_body
		and "set_variable = { soviet_collapse_monthly_successful_objectives = 0 }" in initialize_body
		and "set_variable = { soviet_collapse_monthly_failed_objectives = 0 }" in initialize_body
		and monthly_success_regs >= len(pressure_families) + 1
		and monthly_failure_regs >= len(pressure_families) + 1
		and len(monthly_guard_blocks) == 1
		and "soviet_collapse_monthly_threat_delta" in monthly_guard_body
		and "soviet_collapse_last_month_total_threat" in monthly_guard_body
		and "soviet_collapse_monthly_successful_objectives" in monthly_guard_body
		and "soviet_collapse_monthly_failed_objectives" in monthly_guard_body
		and "constant:soviet_collapse_threat_guard.calm_success_month_cap" in monthly_guard_body
		and "constant:soviet_collapse_threat_guard.moderate_success_month_cap" in monthly_guard_body
		and "constant:soviet_collapse_baseline.foreign_appetite" in monthly_guard_body
		and "constant:soviet_collapse_baseline.league_cohesion" in monthly_guard_body
		and "has_war = no" in monthly_guard_body
		and "set_variable = { soviet_collapse_monthly_successful_objectives = 0 }" in monthly_guard_body
		and "set_variable = { soviet_collapse_monthly_failed_objectives = 0 }" in monthly_guard_body
		and event129_guard
	)
	ok = (
		calm_authority >= 50
		and 5 <= calm_threat <= 10
		and tier1_authority >= 50
		and tier1_threat <= 15
		and severe_authority > 0
		and 35 <= severe_threat < 80
		and prior_memory_authority < calm_authority
		and prior_memory_threat > calm_threat
		and prior_memory_threat < 20
		and visible_causes
		and pressure_helpers >= 20
		and constants.get("soviet_collapse_baseline.total_threat_multiplier", 1) <= 0.25
		and constants.get("soviet_collapse_baseline.total_threat_floor", 1) == 0
	)
	ordinary_failure_pacing_ok = (
		ordinary_failure_helper_count == 6
		and not unresolved_ordinary_failure_helpers
		and max_ordinary_failure_delta <= 3
		and ordinary_failure_months_to_eighty >= 24
	)
	cause_ok = recalculate_surface and opening_surface and first_wave_pressure_surface and covered_pressure_families == len(pressure_families)
	return [
		Check(
			"crisis_balance_surface",
			ok,
			(
				f"calm_authority={calm_authority:.0f} calm_threat={calm_threat:.2f} "
				f"tier1_authority={tier1_authority:.0f} tier1_threat={tier1_threat:.2f} "
				f"severe_authority={severe_authority:.0f} severe_threat={severe_threat:.2f} "
				f"prior_memory_authority={prior_memory_authority:.0f} prior_memory_threat={prior_memory_threat:.2f} "
				f"visible_causes={visible_causes} pressure_helpers={pressure_helpers} "
				f"floor={constants.get('soviet_collapse_baseline.total_threat_floor', 0):.0f}"
			),
		),
		Check(
			"crisis_monthly_guard_surface",
			monthly_guard_ok and ordinary_failure_pacing_ok,
			(
				f"guard_constants={constants.get('soviet_collapse_threat_guard.calm_success_month_cap', '')}/"
				f"{constants.get('soviet_collapse_threat_guard.moderate_success_month_cap', '')} "
				f"success_regs={monthly_success_regs} failure_regs={monthly_failure_regs} "
				f"guard_blocks={len(monthly_guard_blocks)} event129={event129_guard} "
				f"ordinary_failure_max_delta={max_ordinary_failure_delta:.2f} "
				f"ordinary_failure_months_to_80={ordinary_failure_months_to_eighty:.2f} "
				f"ordinary_failure_unresolved={len(unresolved_ordinary_failure_helpers)}"
			),
		),
		Check(
			"crisis_cause_surface",
			cause_ok and monthly_guard_ok,
			(
				f"recalculate_surface={recalculate_surface} opening_surface={opening_surface} "
				f"first_wave_pressure_surface={first_wave_pressure_surface} "
				f"pressure_families={covered_pressure_families}/{len(pressure_families)} "
				f"monthly_guard={monthly_guard_ok} "
				f"multiplier={constants.get('soviet_collapse_baseline.total_threat_multiplier', 0):.2f}"
			),
		),
		Check(
			"mission_success_pressure_surface",
			(
				success_helper_count >= len(pressure_families) + 1
				and non_increasing_success_helpers == success_helper_count
				and bad_success_component_changes == 0
				and not unresolved_success_helpers
				and max_success_delta <= 0
			),
			(
				f"success_helpers={success_helper_count} non_increasing={non_increasing_success_helpers} "
				f"bad_component_changes={bad_success_component_changes} max_net_delta={max_success_delta:.2f} "
				f"unresolved={len(unresolved_success_helpers)}"
			),
		),
	]


def verify_foreign_influence_surface() -> list[Check]:
	constants = read_text(ROOT / "common/script_constants/005_soviet_collapse_constants.txt")
	decisions = read_text(ROOT / "common/decisions/005_soviet_collapse_decisions.txt")
	effects = read_text(ROOT / "common/scripted_effects/005_soviet_collapse_effects.txt")
	triggers = read_text(ROOT / "common/scripted_triggers/005_soviet_collapse_triggers.txt")
	ideas = read_text(ROOT / "common/ideas/005_soviet_collapse_ideas.txt")
	loc = read_text(ROOT / "localisation/english/005_soviet_collapse_l_english.yml")
	docs = read_text(ROOT / "docs/events/005_soviet_union_collapse.md")
	required_constants = [
		"soviet_collapse_influence_war",
		"recognition_influence",
		"liaison_ideology_influence",
		"armaments_arms_influence",
		"advisers_volunteer_influence",
		"intelligence_influence",
		"volunteers_influence",
		"trade_industry_influence",
		"civilian_construction_industry_influence",
		"military_construction_arms_influence",
		"press_network_ideology_influence",
		"aid_corridor_logistics_influence",
		"conference_independence_resilience",
		"league_logistics_influence",
		"league_logistics_independence_resilience",
		"league_logistics_patronage_risk",
		"anti_puppet_clause_independence_resilience",
		"balanced_sponsor_floor",
		"balanced_two_resilience",
		"balanced_three_resilience",
		"dominant_warning_gap",
		"dominant_lock_gap",
		"target_acceptance_equipment_floor",
		"target_acceptance_patronage_ceiling",
		"target_acceptance_recognition_floor",
		"target_acceptance_resilience_need_ceiling",
		"stage_3_threshold",
	]
	category_vars = [
		"soviet_collapse_influence_recognition_total",
		"soviet_collapse_influence_arms_total",
		"soviet_collapse_influence_volunteers_total",
		"soviet_collapse_influence_advisers_total",
		"soviet_collapse_influence_industry_total",
		"soviet_collapse_influence_intelligence_total",
		"soviet_collapse_influence_ideology_total",
		"soviet_collapse_influence_logistics_total",
		"soviet_collapse_influence_patronage_risk",
	]
	sponsor_vars = [
		"soviet_collapse_influence_germany",
		"soviet_collapse_influence_britain",
		"soviet_collapse_influence_japan",
		"soviet_collapse_influence_france",
		"soviet_collapse_influence_usa",
		"soviet_collapse_influence_turkey",
		"soviet_collapse_influence_iran",
		"soviet_collapse_influence_poland",
		"soviet_collapse_influence_romania",
		"soviet_collapse_influence_finland",
		"soviet_collapse_influence_sweden",
		"soviet_collapse_influence_italy",
	]
	stage_ideas = [
		"soviet_collapse_foreign_diplomatic_contacts",
		"soviet_collapse_foreign_diplomatic_mission",
		"soviet_collapse_foreign_treaty_backing",
		"soviet_collapse_foreign_supply_contacts",
		"soviet_collapse_foreign_supply_corridors",
		"soviet_collapse_foreign_supply_network",
		"soviet_collapse_foreign_reconstruction_offers",
		"soviet_collapse_sponsored_civil_works",
		"soviet_collapse_sovereign_reconstruction_board",
		"soviet_collapse_foreign_volunteer_cadres",
		"soviet_collapse_foreign_volunteer_brigades",
		"soviet_collapse_international_defense_corps",
		"soviet_collapse_foreign_military_observers",
		"soviet_collapse_foreign_training_mission",
		"soviet_collapse_joint_staff_mission",
		"soviet_collapse_foreign_patron_contacts",
		"soviet_collapse_foreign_patron_liaison",
		"soviet_collapse_foreign_patron_network",
		"soviet_collapse_foreign_patron_burden",
	]
	aid_effects = [
		"soviet_collapse_apply_foreign_recognition_aid",
		"soviet_collapse_apply_foreign_liaison_aid",
		"soviet_collapse_apply_foreign_armaments_aid",
		"soviet_collapse_apply_foreign_adviser_aid",
		"soviet_collapse_apply_foreign_intelligence_aid",
		"soviet_collapse_apply_foreign_volunteer_aid",
		"soviet_collapse_apply_foreign_trade_aid",
	]
	expanded_decisions = [
		"soviet_collapse_fund_civilian_construction_mission",
		"soviet_collapse_fund_military_construction_mission",
		"soviet_collapse_sponsor_press_and_radio_network",
		"soviet_collapse_secure_republican_aid_corridor",
		"soviet_collapse_build_republics_league_conference",
		"soviet_collapse_route_aid_through_league_logistics",
		"soviet_collapse_demand_anti_puppet_clause",
	]
	expanded_effects = [
		"soviet_collapse_apply_foreign_civilian_construction_aid",
		"soviet_collapse_apply_foreign_military_construction_aid",
		"soviet_collapse_apply_foreign_press_network_aid",
		"soviet_collapse_apply_foreign_aid_corridor",
		"soviet_collapse_apply_foreign_league_conference",
		"soviet_collapse_apply_foreign_league_logistics_aid",
		"soviet_collapse_apply_anti_puppet_clause",
	]
	constants_ok = all(marker in constants for marker in required_constants)
	category_ok = all(var in effects for var in category_vars)
	sponsor_ok = all(var in effects for var in sponsor_vars)
	stage_idea_defs_ok = all(idea in ideas for idea in stage_ideas)
	stage_loc_ok = all(f"{idea}:" in loc and f"{idea}_desc:" in loc for idea in stage_ideas)
	aid_effect_ok = all(
		re.search(rf"{effect}\s*=\s*{{.*?soviet_collapse_apply_foreign_influence_delta\s*=\s*yes.*?soviet_collapse_update_foreign_investment_stage_ideas\s*=\s*yes", effects, re.S)
		for effect in aid_effects
	)
	expanded_decisions_ok = all(decision in decisions and f"{decision}:" in loc and f"{decision}_desc:" in loc for decision in expanded_decisions)
	expanded_effects_ok = all(effect in effects for effect in expanded_effects) and all(trigger in decisions for trigger in [
		"can_pay_soviet_collapse_foreign_civilian_construction_cost",
		"can_pay_soviet_collapse_foreign_military_construction_cost",
		"can_pay_soviet_collapse_foreign_press_network_cost",
		"can_pay_soviet_collapse_foreign_aid_corridor_cost",
		"can_pay_soviet_collapse_foreign_conference_cost",
		"can_pay_soviet_collapse_foreign_league_logistics_cost",
		"can_pay_soviet_collapse_anti_puppet_clause_cost",
	])
	dynamic_expanded_costs = [
		("soviet_collapse_foreign_civilian_construction_cost_text", "GetSovietCollapseForeignAidCivilianConstructionPPCost", "civilian_construction_major_fuel_extra_spend"),
		("soviet_collapse_foreign_military_construction_cost_text", "GetSovietCollapseForeignAidMilitaryConstructionCPCost", "military_construction_major_support_equipment_extra_spend"),
		("soviet_collapse_foreign_press_network_cost_text", "GetSovietCollapseForeignAidPressNetworkPPCost", "press_network_major_stability_extra_spend"),
		("soviet_collapse_foreign_aid_corridor_cost_text", "GetSovietCollapseForeignAidCorridorFuelCost", "aid_corridor_major_train_extra_spend"),
		("soviet_collapse_foreign_conference_cost_text", "GetSovietCollapseForeignAidConferencePPCost", "conference_major_command_power_extra_spend"),
		("soviet_collapse_foreign_league_logistics_cost_text", "GetSovietCollapseForeignAidLeagueLogisticsPPCost", "league_logistics_major_fuel_extra_spend"),
		("soviet_collapse_anti_puppet_clause_cost_text", "GetSovietCollapseAntiPuppetClausePPCost", "anti_puppet_clause_major_command_power_extra_spend"),
	]
	dynamic_expanded_cost_ok = (
		all(re.search(rf"{re.escape(cost_key)}:\s*\"[^\"]*FROM\.{loc_func}", loc) for cost_key, loc_func, _ in dynamic_expanded_costs)
		and all(loc_func in read_text(ROOT / "common/scripted_localisation/005_soviet_collapse_scripted_localisation.txt") for _, loc_func, _ in dynamic_expanded_costs)
		and all(extra_marker in constants and extra_marker in effects for _, _, extra_marker in dynamic_expanded_costs)
		and all(marker in triggers for marker in [
			"civilian_construction_major_political_power",
			"military_construction_major_command_power",
			"press_network_major_stability_floor",
			"aid_corridor_major_fuel",
			"conference_major_political_power",
			"league_logistics_major_political_power",
			"anti_puppet_clause_major_political_power",
		])
	)
	investment_surface_ok = all(marker in effects for marker in [
		"add_building_construction = { type = industrial_complex",
		"add_building_construction = { type = arms_factory",
		"add_building_construction = { type = anti_air_building",
		"create_unit",
		"soviet_collapse_foreign_aid_corridor_open",
		"soviet_collapse_independence_resilience",
		"soviet_collapse_influence_patronage_risk",
		"add_timed_idea = { idea = soviet_collapse_foreign_patron_burden",
	])
	sponsor_balance_markers = [
		"soviet_collapse_update_sponsor_balance_pressure",
		"soviet_collapse_active_foreign_sponsor_count",
		"soviet_collapse_top_foreign_sponsor_influence",
		"soviet_collapse_second_foreign_sponsor_influence",
		"soviet_collapse_foreign_sponsor_gap",
		"soviet_collapse_balanced_sponsors_two",
		"soviet_collapse_balanced_sponsors_three",
		"soviet_collapse_dominant_sponsor_warning",
		"soviet_collapse_dominant_sponsor_lock",
	]
	sponsor_balance_ok = (
		all(marker in effects for marker in sponsor_balance_markers)
		and all(marker in constants for marker in [
			"balanced_sponsor_floor",
			"balanced_two_resilience",
			"balanced_three_resilience",
			"dominant_warning_influence",
			"dominant_warning_gap",
			"dominant_lock_influence",
			"dominant_lock_gap",
		])
		and re.search(r"soviet_collapse_apply_foreign_influence_delta\s*=\s*{.*?soviet_collapse_update_sponsor_balance_pressure\s*=\s*yes", effects, re.S)
	)
	sponsor_style_triggers = [
		"is_soviet_collapse_military_patron_style",
		"is_soviet_collapse_relief_patron_style",
		"is_soviet_collapse_client_patron_style",
		"is_soviet_collapse_border_patron_style",
		"is_soviet_collapse_league_conference_patron_style",
		"is_soviet_collapse_reconstruction_patron_style",
		"is_soviet_collapse_caucasus_central_asia_patron_style",
		"is_soviet_collapse_caucasus_or_central_asia_breakaway",
	]
	sponsor_style_decision_pairs = [
		("soviet_collapse_recognize_breakaway_government", "is_soviet_collapse_relief_patron_style"),
		("soviet_collapse_fund_ideological_liaison_offices", "is_soviet_collapse_client_patron_style"),
		("soviet_collapse_ship_border_armaments", "is_soviet_collapse_military_patron_style"),
		("soviet_collapse_dispatch_military_advisers", "is_soviet_collapse_caucasus_central_asia_patron_style"),
		("soviet_collapse_open_republican_intelligence_channel", "tag = JAP"),
		("soviet_collapse_sponsor_volunteer_corps", "is_soviet_collapse_border_patron_style"),
		("soviet_collapse_negotiate_republican_trade_mission", "is_soviet_collapse_reconstruction_patron_style"),
		("soviet_collapse_fund_civilian_construction_mission", "is_soviet_collapse_reconstruction_patron_style"),
		("soviet_collapse_fund_military_construction_mission", "is_soviet_collapse_military_patron_style"),
		("soviet_collapse_sponsor_press_and_radio_network", "is_soviet_collapse_client_patron_style"),
		("soviet_collapse_secure_republican_aid_corridor", "is_soviet_collapse_caucasus_or_central_asia_breakaway"),
		("soviet_collapse_build_republics_league_conference", "is_soviet_collapse_league_conference_patron_style"),
		("soviet_collapse_route_aid_through_league_logistics", "is_soviet_collapse_league_conference_patron_style"),
		("soviet_collapse_demand_anti_puppet_clause", "is_soviet_collapse_relief_patron_style"),
		("soviet_collapse_offer_protection_treaty", "is_soviet_collapse_client_patron_style"),
		("soviet_collapse_demand_adviser_privileges", "is_soviet_collapse_client_patron_style"),
		("soviet_collapse_install_client_cabinet", "is_soviet_collapse_client_patron_style"),
	]
	sponsor_style_ok = (
		all(marker in triggers for marker in sponsor_style_triggers)
		and all(
			re.search(rf"{decision}\s*=\s*{{.*?{re.escape(marker)}", decisions, re.S)
			for decision, marker in sponsor_style_decision_pairs
		)
	)
	access_route_ok = all(marker in triggers for marker in [
		"has_soviet_collapse_foreign_aid_route_to_from",
		"has_war_with = SOV",
		"NOT = { has_war_with = ROOT }",
		"is_in_faction_with = FROM",
		"any_neighbor_state",
		"is_owned_by = FROM",
		"any_owned_state = { is_coastal = yes }",
		"FROM = { any_owned_state = { is_coastal = yes } }",
		"soviet_collapse_foreign_aid_corridor_open",
		"soviet_collapse_free_republics_league_member",
		"is_soviet_collapse_league_conference_patron_style = yes",
	]) and triggers.count("has_soviet_collapse_foreign_aid_route_to_from = yes") >= 4
	target_aid_block = re.search(r"can_target_soviet_collapse_breakaway_for_aid\s*=\s*{.*?^}", triggers, re.S | re.M)
	target_acceptance_ok = (
		"has_soviet_collapse_target_acceptance_for_foreign_aid_from_root = yes" in triggers
		and all(marker in triggers for marker in [
			"has_soviet_collapse_target_acceptance_for_foreign_aid_from_root",
			"target_acceptance_equipment_floor",
			"target_acceptance_patronage_ceiling",
			"target_acceptance_recognition_floor",
			"target_acceptance_resilience_need_ceiling",
			"has_country_flag = soviet_collapse_balanced_sponsors_two",
			"has_country_flag = soviet_collapse_balanced_sponsors_three",
			"has_country_flag = soviet_collapse_dominant_sponsor_lock",
			"is_soviet_collapse_republic_protected_from_external_dependency = yes",
			"is_soviet_collapse_client_patron_style = yes",
			"is_soviet_collapse_relief_patron_style = yes",
			"is_soviet_collapse_league_conference_patron_style = yes",
		])
		and bool(target_aid_block)
		and "has_soviet_collapse_target_acceptance_for_foreign_aid_from_root = yes" in target_aid_block.group(0)
	)
	league_mediated_aid_ok = all(marker in triggers + decisions + effects + loc + docs for marker in [
		"can_target_soviet_collapse_breakaway_for_league_aid",
		"has_soviet_collapse_league_aid_channel_to_from",
		"can_pay_soviet_collapse_foreign_league_logistics_cost",
		"soviet_collapse_route_aid_through_league_logistics",
		"soviet_collapse_apply_foreign_league_logistics_aid",
		"soviet_collapse_league_logistics_channel_open",
		"soviet_collapse_foreign_league_logistics_cost_text",
		"League-mediated logistics aid",
	]) and all(marker in read_text(ROOT / "docs/events/005_soviet_union_collapse_league_mediated_aid.md") for marker in [
		"soviet_collapse_route_aid_through_league_logistics",
		"less target dependency",
		"No new icon is required",
	])
	docs_ok = "## Foreign Influence Tracking" in docs and all(marker in docs for marker in [
		"category totals",
		"sponsor totals",
		"staged spirit tracks",
		"Recognition grows",
		"Investment grows",
		"Volunteer support grows",
		"Adviser support grows",
		"civilian construction",
		"anti-puppet clause",
		"active sponsor count",
		"top sponsor",
		"sponsor gap",
		"sponsor-style triggers",
		"Germany, Japan, Italy, Poland, Romania, and Finland",
		"Turkey and Iran",
		"Expanded patron action costs scale by target tier",
		"real access route",
		"target-side acceptance gate",
		"rifle shortage",
		"dominant sponsor lock",
		"League-mediated logistics aid",
	])
	return [
		Check(
			"foreign_influence_surface",
			constants_ok and category_ok and sponsor_ok and stage_idea_defs_ok and stage_loc_ok and aid_effect_ok and expanded_decisions_ok and expanded_effects_ok and dynamic_expanded_cost_ok and investment_surface_ok and sponsor_balance_ok and sponsor_style_ok and access_route_ok and target_acceptance_ok and league_mediated_aid_ok and docs_ok,
			(
				f"constants={constants_ok} category_vars={category_ok} sponsor_vars={sponsor_ok} "
				f"stage_ideas={stage_idea_defs_ok} stage_loc={stage_loc_ok} "
				f"aid_effects={aid_effect_ok} expanded_decisions={expanded_decisions_ok} "
				f"expanded_effects={expanded_effects_ok} dynamic_expanded_costs={dynamic_expanded_cost_ok} "
				f"investment_surface={investment_surface_ok} "
				f"sponsor_balance={bool(sponsor_balance_ok)} sponsor_styles={sponsor_style_ok} "
				f"access_routes={access_route_ok} target_acceptance={target_acceptance_ok} "
				f"league_mediated_aid={league_mediated_aid_ok} docs={docs_ok}"
			),
		)
	]


def verify_reintegration_puppet_surface() -> list[Check]:
	constants = read_text(ROOT / "common/script_constants/005_soviet_collapse_constants.txt")
	triggers = read_text(ROOT / "common/scripted_triggers/005_soviet_collapse_triggers.txt")
	decisions = read_text(ROOT / "common/decisions/005_soviet_collapse_decisions.txt")
	effects = read_text(ROOT / "common/scripted_effects/005_soviet_collapse_effects.txt")
	loc = read_text(ROOT / "localisation/english/005_soviet_collapse_l_english.yml")
	docs = read_text(ROOT / "docs/events/005_soviet_union_collapse.md")
	mechanic_docs = read_text(ROOT / "docs/events/005_soviet_union_collapse_reintegration_dependency.md")
	constant_markers = [
		"soviet_collapse_moscow_reintegration",
		"soviet_collapse_puppet_pressure",
		"moscow_union_treaty_influence",
		"moscow_federal_compact_influence",
		"protection_treaty_influence",
		"adviser_privileges_influence",
		"client_cabinet_influence",
		"dominant_sponsor_influence",
		"total_influence_floor",
	]
	moscow_decisions = [
		"soviet_collapse_offer_new_union_treaty",
		"soviet_collapse_offer_federal_reintegration_compact",
	]
	puppet_decisions = [
		"soviet_collapse_offer_protection_treaty",
		"soviet_collapse_demand_adviser_privileges",
		"soviet_collapse_install_client_cabinet",
	]
	required_triggers = [
		"can_pay_soviet_collapse_moscow_union_treaty_cost",
		"can_pay_soviet_collapse_moscow_federal_compact_cost",
		"can_pay_soviet_collapse_foreign_protection_treaty_cost",
		"can_pay_soviet_collapse_foreign_adviser_privileges_cost",
		"can_pay_soviet_collapse_foreign_client_cabinet_cost",
		"is_soviet_collapse_moscow_dominant_influence_for_from",
		"is_soviet_collapse_root_dominant_sponsor_for_from",
		"can_target_soviet_collapse_breakaway_for_moscow_union_treaty",
		"can_target_soviet_collapse_breakaway_for_moscow_federal_compact",
		"can_target_soviet_collapse_breakaway_for_foreign_protection_treaty",
		"can_target_soviet_collapse_breakaway_for_foreign_adviser_privileges",
		"can_target_soviet_collapse_breakaway_for_foreign_client_cabinet",
		"has_soviet_collapse_foreign_aid_route_to_from",
	]
	required_effects = [
		"soviet_collapse_apply_moscow_union_treaty_offer",
		"soviet_collapse_apply_moscow_federal_compact",
		"soviet_collapse_apply_foreign_protection_treaty",
		"soviet_collapse_apply_foreign_adviser_privileges",
		"soviet_collapse_apply_foreign_client_cabinet",
	]
	decision_loc_ok = all(
		f"{decision}:" in loc and f"{decision}_desc:" in loc and f"{decision}_tt:" in loc
		for decision in moscow_decisions + puppet_decisions
	)
	cost_loc_ok = all(
		f"{key}_cost_text:" in loc and f"{key}_cost_text_blocked:" in loc
		for key in [
			"soviet_collapse_moscow_union_treaty",
			"soviet_collapse_moscow_federal_compact",
			"soviet_collapse_foreign_protection_treaty",
			"soviet_collapse_foreign_adviser_privileges",
			"soviet_collapse_foreign_client_cabinet",
		]
	)
	highest_influence_ok = all(marker in triggers for marker in [
		"soviet_collapse_influence_moscow",
		"soviet_collapse_influence_germany value = soviet_collapse_influence_britain",
		"soviet_collapse_influence_britain value = soviet_collapse_influence_germany",
		"soviet_collapse_influence_italy value = soviet_collapse_influence_moscow",
		"NOT = { is_soviet_collapse_republic_protected_from_external_dependency = yes }",
		"NOT = { has_war_with = SOV }",
	])
	autonomy_ok = all(marker in effects for marker in [
		"set_autonomy = { target = FROM autonomy_state = autonomy_puppet freedom_level = 0.6 end_wars = no }",
		"set_autonomy = { target = FROM autonomy_state = autonomy_puppet freedom_level = 0.3 end_wars = no }",
		"soviet_collapse_moscow_union_treaty_offered",
		"soviet_collapse_moscow_federated_subject",
		"soviet_collapse_foreign_protection_treaty_signed",
		"soviet_collapse_foreign_adviser_privileges_granted",
		"soviet_collapse_foreign_client_cabinet_installed",
	])
	docs_ok = "## Reintegration And Dependency Pressure" in docs and all(marker in docs for marker in [
		"dominant Moscow influence",
		"three-step dependency chain",
		"Install Client Cabinet",
		"strong League or faction protection",
	]) and all(marker in mechanic_docs for marker in [
		"## Moscow Path",
		"## Foreign Sponsor Path",
		"## Icons",
		"reintegration_puppet_surface",
	])
	return [
		Check(
			"reintegration_puppet_surface",
			(
				all(marker in constants for marker in constant_markers)
				and all(decision in decisions for decision in moscow_decisions + puppet_decisions)
				and all(trigger in triggers for trigger in required_triggers)
				and all(effect in effects for effect in required_effects)
				and decision_loc_ok
				and cost_loc_ok
				and highest_influence_ok
				and autonomy_ok
				and docs_ok
			),
			(
				f"constants={all(marker in constants for marker in constant_markers)} "
				f"decisions={all(decision in decisions for decision in moscow_decisions + puppet_decisions)} "
				f"triggers={all(trigger in triggers for trigger in required_triggers)} "
				f"effects={all(effect in effects for effect in required_effects)} "
				f"decision_loc={decision_loc_ok} cost_loc={cost_loc_ok} "
				f"highest_influence={highest_influence_ok} autonomy={autonomy_ok} docs={docs_ok}"
			),
		)
	]


def verify_local_league_surface() -> list[Check]:
	constants = read_text(ROOT / "common/script_constants/005_soviet_collapse_constants.txt")
	triggers = read_text(ROOT / "common/scripted_triggers/005_soviet_collapse_triggers.txt")
	effects = read_text(ROOT / "common/scripted_effects/005_soviet_collapse_effects.txt")
	decisions = read_text(ROOT / "common/decisions/005_soviet_collapse_decisions.txt")
	categories = read_text(ROOT / "common/decisions/categories/005_soviet_collapse_categories.txt")
	events = read_text(ROOT / "events/005_soviet_collapse.txt")
	loc = read_text(ROOT / "localisation/english/005_soviet_collapse_l_english.yml")
	docs = read_text(ROOT / "docs/events/005_soviet_union_collapse.md")
	league_docs = read_text(ROOT / "docs/events/005_soviet_union_collapse_local_leagues.md")
	completion_audit = read_text(ROOT / "docs/events/005_soviet_union_collapse_completion_audit.md")
	constants_ok = all(marker in constants for marker in [
		"soviet_collapse_regional_faction",
		"found_political_power",
		"soviet_release_pressure",
		"war_equipment_reward",
	])
	triggers_ok = all(marker in triggers for marker in [
		"can_found_soviet_collapse_baltic_league",
		"can_found_soviet_collapse_caucasus_league",
		"can_found_soviet_collapse_central_asian_league",
		"can_soviet_collapse_call_regional_league_defensive_war",
		"has_soviet_collapse_three_smaller_central_asian_republics_free = yes",
	])
	visibility_ok = all(marker in categories for marker in [
		"can_found_soviet_collapse_baltic_league = yes",
		"can_found_soviet_collapse_caucasus_league = yes",
		"can_found_soviet_collapse_central_asian_league = yes",
	])
	decisions_ok = all(marker in decisions for marker in [
		"soviet_collapse_found_baltic_restoration_pact",
		"soviet_collapse_found_caucasus_defense_compact",
		"soviet_collapse_found_steppe_federation",
		"soviet_collapse_invite_regional_partners",
		"soviet_collapse_coordinate_regional_faction",
		"soviet_collapse_set_regional_defense_goal",
		"soviet_collapse_call_regional_league_defensive_war",
		"soviet_collapse_withdraw_from_regional_faction",
	])
	effects_ok = all(marker in effects for marker in [
		"soviet_collapse_found_baltic_restoration_pact",
		"soviet_collapse_found_caucasus_defense_compact",
		"soviet_collapse_found_central_asian_league",
		"create_faction = soviet_collapse_baltic_restoration_pact_faction",
		"create_faction = soviet_collapse_caucasus_defense_compact_faction",
		"create_faction = soviet_collapse_central_asian_league_faction",
		"add_to_faction = LIT",
		"add_to_faction = MRC",
		"add_to_faction = KAZ",
		"has_soviet_collapse_three_smaller_central_asian_republics_free = yes",
		"declare_war_on =",
		"add_to_war =",
		"clr_global_flag = soviet_collapse_progressive_release_cooldown",
		"soviet_collapse_maybe_release_threat_breakaway = yes",
	])
	events_ok = all(marker in events for marker in [
		"id = chaosx.nr5.30",
		"id = chaosx.nr5.31",
		"id = chaosx.nr5.32",
		"id = chaosx.nr5.43",
	])
	loc_ok = all(marker in loc for marker in [
		"soviet_collapse_free_republics_league_faction: \"Free Republics' League\"",
		"soviet_collapse_baltic_restoration_pact_faction: \"Baltic League\"",
		"soviet_collapse_caucasus_defense_compact_faction: \"Caucasus League\"",
		"soviet_collapse_central_asian_league_faction: \"Central Asian League\"",
		"soviet_collapse_found_baltic_restoration_pact: \"Found the Baltic League\"",
		"soviet_collapse_found_caucasus_defense_compact: \"Found the Caucasus League\"",
		"soviet_collapse_found_steppe_federation: \"Found the Central Asian League\"",
		"super_event.25.t: \"The Baltic League\"",
		"super_event.26.t: \"The Caucasus League\"",
		"soviet_collapse_call_regional_league_defensive_war:",
		"soviet_collapse_regional_faction_found_cost_text: \"£pol_power 55  £command_power 20\"",
	])
	docs_ok = "Local leagues now operate as the regional layer" in docs and all(marker in league_docs for marker in [
		"## Overview",
		"The Baltic League, Caucasus League, and Central Asian League",
		"Free Republics' League",
		"player-facing text uses league names throughout",
		"Central Asian League",
		"Kazakhstan is restricted",
		"## Icons",
	]) and all(marker in completion_audit for marker in [
		"Local leagues and high-threat coordination",
		"exact player-facing league names",
		"MTTH release acceleration",
	])
	return [
		Check(
			"local_league_surface",
			constants_ok and triggers_ok and visibility_ok and decisions_ok and effects_ok and events_ok and loc_ok and docs_ok,
			(
				f"constants={constants_ok} triggers={triggers_ok} visibility={visibility_ok} "
				f"decisions={decisions_ok} effects={effects_ok} events={events_ok} "
				f"loc={loc_ok} docs={docs_ok}"
			),
		)
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
		cleanup_helper_ok
		and missions <= activate_refs
		and not (DISABLED_SOVIET_OBJECTIVE_MISSIONS & activate_refs)
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
	triggers = read_text(ROOT / "common/scripted_triggers/005_soviet_collapse_triggers.txt")
	effects = read_text(ROOT / "common/scripted_effects/005_soviet_collapse_effects.txt")
	loc = read_text(ROOT / "localisation/english/005_soviet_collapse_l_english.yml")
	constants = parse_script_constants(read_text(ROOT / "common/script_constants/005_soviet_collapse_constants.txt"))
	decision_blocks: list[tuple[str, list[str]]] = []
	for _, category_body in direct_child_blocks(tokens(decisions)):
		decision_blocks.extend(direct_child_blocks(category_body))

	mission_re = re.compile(r"^soviet_collapse_soviet_mission_(\d{3})_")
	missions = [(name, body) for name, body in decision_blocks if mission_re.match(name)]
	mission_ids = {name for name, _ in missions}
	trigger_tokens = tokens(triggers)
	scripted_triggers = dict(direct_child_blocks(trigger_tokens))
	loc_keys = set(re.findall(r"^\s*([A-Za-z0-9_.-]+):\s*\"", loc, re.MULTILINE))
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
	available_bodies = []
	weak_available = []
	identical_outcomes = []
	map_or_state_available = 0
	raw_division_state_available = []
	long_inline_available = []
	missing_scripted_requirement = []
	thin_scripted_requirement = []
	meter_only_requirement = []
	passive_scripted_requirement = []
	division_tooltip_keys = []
	division_tooltip_missing_loc = []
	forbidden_trivial_literals = []
	requirement_family_counts = []
	requirement_families = {
		"stockpile": ["has_equipment", "has_fuel", "has_manpower", "has_army_experience", "command_power"],
		"political": ["has_stability", "has_war_support"],
		"map_control": ["is_controlled_by", "is_owned_by", "capital_scope", "any_owned_state"],
		"division_position": ["num_divisions_in_states"],
		"crisis_variable": ["check_variable"],
		"flag_or_prior_action": ["has_country_flag", "has_global_flag", "has_recovered_", "has_idea"],
		"war_or_diplomacy": ["has_war_with", "is_in_faction", "is_faction_leader"],
		"special_spawn_gate": ["can_soviet_collapse_spawn_"],
	}
	for name, body in missions:
		number = mission_re.match(name).group(1)
		body_text = " ".join(body)
		allowed_text = " ".join(" ".join(block) for block in top_level_block_bodies(body, "allowed"))
		visible_text = " ".join(" ".join(block) for block in top_level_block_bodies(body, "visible"))
		available_blocks = top_level_block_bodies(body, "available")
		available_text = " ".join(" ".join(block) for block in available_blocks)
		complete_text = " ".join(" ".join(block) for block in top_level_block_bodies(body, "complete_effect"))
		timeout_text = " ".join(" ".join(block) for block in top_level_block_bodies(body, "timeout_effect"))
		available_bodies.append(available_text)
		requirement_refs = [
			block[0]
			for block in available_blocks
			if len(block) == 3 and block[1] == "=" and block[2] == "yes"
		]
		requirement_text = " ".join(" ".join(scripted_triggers[ref]) for ref in requirement_refs if ref in scripted_triggers)
		if len(requirement_refs) != 1 or any(ref not in scripted_triggers for ref in requirement_refs):
			missing_scripted_requirement.append(name)
		families = {
			family
			for family, markers in requirement_families.items()
			if any(marker in requirement_text for marker in markers)
		}
		requirement_family_counts.append(len(families))
		if len(families) < 2:
			thin_scripted_requirement.append(name)
		if families == {"crisis_variable"}:
			meter_only_requirement.append(name)
		passive_family_markers = ["has_manpower", "has_equipment", "has_stability", "has_war_support", "has_army_experience", "command_power", "has_fuel"]
		active_family_markers = ["is_controlled_by", "is_owned_by", "capital_scope", "any_owned_state", "num_divisions_in_states", "has_country_flag", "has_global_flag", "has_recovered_", "has_idea", "has_war_with", "is_in_faction", "can_soviet_collapse_spawn_", "check_variable"]
		if any(marker in requirement_text for marker in passive_family_markers) and not any(marker in requirement_text for marker in active_family_markers):
			passive_scripted_requirement.append(name)
		if re.search(r"\b20000\b|\b0\.35\b|35\s*percent", requirement_text):
			forbidden_trivial_literals.append(name)
		if "num_divisions_in_states" in requirement_text:
			keys = re.findall(r"tooltip\s*=\s*([A-Za-z0-9_]+)", requirement_text)
			division_tooltip_keys.extend(keys)
			division_tooltip_missing_loc.extend(key for key in keys if key not in loc_keys)
			if not keys or "custom_trigger_tooltip" not in requirement_text or "hidden_trigger" not in requirement_text:
				raw_division_state_available.append(name)
		if complete_text == timeout_text:
			identical_outcomes.append(name)
		if any(marker in available_text for marker in ["can_", "has_recovered_", "is_controlled_by", "is_owned_by", "capital_scope", "num_divisions_in_states", "any_owned_state"]):
			map_or_state_available += 1
		if "num_divisions_in_states" in available_text:
			raw_division_state_available.append(name)
		if any(
			len(block) > 8
			or not (
				len(block) == 3
				and block[1] == "="
				and block[2] == "yes"
				and (block[0].startswith("can_") or block[0].startswith("has_") or block[0].startswith("is_"))
			)
			for block in available_blocks
		):
			long_inline_available.append(name)
		passive_markers = ["has_manpower", "has_equipment", "has_stability", "has_war_support", "has_army_experience", "command_power", "has_fuel"]
		active_markers = ["can_", "has_recovered_", "is_controlled_by", "is_owned_by", "capital_scope", "num_divisions_in_states", "any_owned_state", "has_country_flag", "check_variable", "has_idea"]
		if any(marker in available_text for marker in passive_markers) and not any(marker in available_text for marker in active_markers):
			weak_available.append(name)
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
		and activate_body.count("constant:soviet_collapse_soviet_objective.active_cap") >= len(mission_ids)
		and activate_body.count("compare = less_than") >= len(mission_ids)
		and activate_body.count("add_to_temp_variable = { soviet_collapse_active_objectives = 1 }") >= len(mission_ids)
	)
	ok = (
		len(count_blocks) == 1
		and len(activate_blocks) == 1
		and count_refs == mission_ids
		and activate_refs == mission_ids
		and manual_only == len(missions)
		and visible_gated == len(missions)
		and mission_payloads == len(missions)
		and queue_restarts == len(missions)
		and done_flag_refs == len(mission_ids)
		and len(mission_timeouts) >= 8
		and queue_cap_ok
	)
	quality_ok = (
		len(set(available_bodies)) == len(available_bodies)
		and not weak_available
		and not identical_outcomes
		and not raw_division_state_available
		and not long_inline_available
		and map_or_state_available >= len(missions) * 9 // 10
	)
	requirements_ok = (
		not missing_scripted_requirement
		and not thin_scripted_requirement
		and not meter_only_requirement
		and not passive_scripted_requirement
		and not forbidden_trivial_literals
		and len(division_tooltip_keys) >= 4
		and not division_tooltip_missing_loc
		and min(requirement_family_counts or [0]) >= 2
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
		,
		Check(
			"mission_quality_surface",
			quality_ok,
			(
				f"missions={len(missions)} unique_available={len(set(available_bodies))}/{len(available_bodies)} "
				f"weak_available={len(weak_available)} identical_outcomes={len(identical_outcomes)} "
				f"raw_division_state_available={len(raw_division_state_available)} "
				f"long_inline_available={len(long_inline_available)} "
				f"map_or_state_available={map_or_state_available}"
			),
		),
		Check(
			"mission_requirement_surface",
			requirements_ok,
			(
				f"scripted_requirement_refs={len(missions) - len(missing_scripted_requirement)}/{len(missions)} "
				f"thin_requirements={len(thin_scripted_requirement)} meter_only={len(meter_only_requirement)} "
				f"passive_only={len(passive_scripted_requirement)} forbidden_trivial_literals={len(forbidden_trivial_literals)} "
				f"division_tooltips={len(division_tooltip_keys)} missing_division_tooltip_loc={len(division_tooltip_missing_loc)} "
				f"min_requirement_families={min(requirement_family_counts or [0])}"
			),
		),
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
	disabled_spawn_calls = {f"soviet_collapse_spawn_{tag.lower()}_if_enabled" for tag in DISABLED_CUSTOM_TAGS}
	disabled_calls_present = {call for call in disabled_spawn_calls if call in maybe_body}
	ready_trigger_count = 0
	for tag in CUSTOM_TAGS:
		blocks = named_blocks(tokens(triggers), f"can_soviet_collapse_spawn_{tag.lower()}")
		body = " ".join(blocks[0]) if blocks else ""
		if "is_soviet_collapse_high_chaos_successor_spawn_ready = yes" in body:
			ready_trigger_count += 1
	ok = (
		"has_global_flag = { flag = chaos_tier value = 5 }" in terminal_body
		and "soviet_collapse_prepare_highest_chaos_terminal_successors" in terminal_body
		and "soviet_collapse_maybe_spawn_high_chaos_successors" in terminal_body
		and prepare_flags >= 18
		and spawn_calls == expected_spawn_calls
		and not disabled_calls_present
		and ready_trigger_count == len(CUSTOM_TAGS)
	)
	return [
		Check(
			"terminal_high_chaos_successor_surface",
			ok,
			(
				f"prepare_flags={prepare_flags} spawn_calls={len(spawn_calls)}/{len(expected_spawn_calls)} "
				f"ready_trigger_refs={ready_trigger_count} disabled_spawn_calls={len(disabled_calls_present)}"
			),
		)
	]


def verify_disabled_weird_successor_surface() -> list[Check]:
	effects_text = read_text(ROOT / "common/scripted_effects/005_soviet_collapse_effects.txt")
	triggers_text = read_text(ROOT / "common/scripted_triggers/005_soviet_collapse_triggers.txt")
	decisions_text = read_text(ROOT / "common/decisions/005_soviet_collapse_decisions.txt")
	categories_text = read_text(ROOT / "common/decisions/categories/005_soviet_collapse_categories.txt")
	mtth_text = read_text(ROOT / "common/mtth/005_soviet_collapse_mtth.txt")
	event005_gfx_text = "\n".join(
		read_text(path)
		for path in [
			ROOT / "interface/005_soviet_collapse_icons.gfx",
			ROOT / "interface/005_soviet_collapse_custom_icons.gfx",
			ROOT / "interface/chaosx_achievements.gfx",
			ROOT / "interface/chaosx_super_events.gfx",
		]
		if path.exists()
	)
	event005_doc_text = "\n".join(
		read_text(path)
		for path in [
			ROOT / "docs/assets/005_soviet_union_collapse/manifest.md",
			ROOT / "docs/assets/005_soviet_union_collapse/republic_focus_and_influence/manifest.md",
			ROOT / "docs/assets/005_soviet_union_collapse/achievement_icon_manifest.md",
			ROOT / "docs/assets/005_soviet_union_collapse/contact_sheets/soviet_collapse_asset_records.tsv",
			ROOT / "docs/super_events/005_soviet_union_collapse_super_event_research.md",
			ROOT / "docs/super_events/super_event_audio_packages.md",
			ROOT / "localisation/english/005_soviet_collapse_l_english.yml",
			ROOT / "localisation/english/chaosx_achievements_l_english.yml",
		]
		if path.exists()
	)
	focus_counts = event005_focus_tree_counts()
	effect_tokens = tokens(effects_text)
	trigger_tokens = tokens(triggers_text)
	decision_tokens = tokens(decisions_text)
	category_tokens = tokens(categories_text)

	disabled_focus_trees = [
		f"{tag}_soviet_collapse_focus_tree"
		for tag in DISABLED_CUSTOM_TAGS
		if f"{tag}_soviet_collapse_focus_tree" in focus_counts
	]
	disabled_load_refs = [
		tag
		for tag in DISABLED_CUSTOM_TAGS
		if f"load_focus_tree = {{ tree = {tag}_soviet_collapse_focus_tree" in effects_text
	]
	disabled_effects = [
		name
		for name in DISABLED_EFFECT_BLOCKS
		if named_blocks(effect_tokens, name)
	]
	disabled_triggers = [
		name
		for name in [f"can_soviet_collapse_spawn_{tag.lower()}" for tag in DISABLED_CUSTOM_TAGS]
		if named_blocks(trigger_tokens, name)
	]
	disabled_decision_categories = [
		name
		for name in DISABLED_DECISION_CATEGORIES
		if named_blocks(decision_tokens, name)
	]
	disabled_category_defs = [
		name
		for name in DISABLED_DECISION_CATEGORIES
		if named_blocks(category_tokens, name)
	]
	disabled_objective_missions = [
		name
		for name in DISABLED_SOVIET_OBJECTIVE_MISSIONS
		if name in decisions_text or name in effects_text
	]
	disabled_objective_triggers = [
		name
		for name in DISABLED_OBJECTIVE_TRIGGERS
		if named_blocks(trigger_tokens, name)
	]
	disabled_objective_flags = [
		name
		for name in DISABLED_OBJECTIVE_FLAGS
		if name in effects_text or name in triggers_text or name in decisions_text or name in mtth_text
	]
	disabled_gfx_refs = []
	for tag in DISABLED_CUSTOM_TAGS:
		tag_lower = tag.lower()
		for marker in [
			f"GFX_portrait_{tag}_",
			f"GFX_focus_{tag}_",
			f"GFX_idea_{tag_lower}_",
			f"GFX_decision_{tag_lower}_",
			f"005_{tag_lower}_custom_splinter",
			f"/{tag}_leader.dds",
		]:
			if marker in event005_gfx_text:
				disabled_gfx_refs.append(marker)
	for achievement_id in DISABLED_ACHIEVEMENT_IDS:
		if f"GFX_achievement_{achievement_id}" in event005_gfx_text or f"gfx/achievements/{achievement_id}" in event005_gfx_text:
			disabled_gfx_refs.append(achievement_id)
	disabled_doc_refs = []
	for marker in [
		"Dead International",
		"The Dead Are Citizens",
		"dead_are_citizens",
		"Iron Commissariat",
		"Red Martyrs",
		"Red Cosmist",
		"Iron Liturgy",
		"Pale Railway",
		"Tunguska",
		"Last Tsar",
		"Revenant",
		"Third Rome",
		"Sepulchre",
		"Unburied",
		"Black Earth",
		"Red Lazarus",
		"Last International",
		"Iron Resurrection",
	]:
		if marker in event005_doc_text:
			disabled_doc_refs.append(marker)
	for tag in DISABLED_TAG_REGISTRATION_TAGS:
		if f"`{tag}`" in event005_doc_text or f"/{tag}_" in event005_doc_text or f"/{tag}.tga" in event005_doc_text:
			disabled_doc_refs.append(tag)
	disabled_tag_regs = []
	country_tags_text = read_text(ROOT / "common/country_tags/chaosx_countries.txt")
	for tag in DISABLED_TAG_REGISTRATION_TAGS:
		if re.search(rf"^{tag}\s*=", country_tags_text, re.MULTILINE):
			disabled_tag_regs.append(tag)
	disabled_idea_prefixes = [
		tag.lower()
		for tag in DISABLED_CUSTOM_TAGS
		if any(idea_id.startswith(f"{tag.lower()}_") for idea_id in event005_idea_ids())
	]
	disabled_country_files = []
	for tag in DISABLED_TAG_REGISTRATION_TAGS:
		for path in (ROOT / "common/countries").glob(f"*{tag}*.txt"):
			disabled_country_files.append(str(path.relative_to(ROOT)))
		for path in (ROOT / "history/countries").glob(f"{tag} - *.txt"):
			disabled_country_files.append(str(path.relative_to(ROOT)))
	ok = not any([
		disabled_focus_trees,
		disabled_load_refs,
		disabled_effects,
		disabled_triggers,
		disabled_decision_categories,
		disabled_category_defs,
		disabled_objective_missions,
		disabled_objective_triggers,
		disabled_objective_flags,
		disabled_gfx_refs,
		disabled_doc_refs,
		disabled_tag_regs,
		disabled_idea_prefixes,
		disabled_country_files,
	])
	return [
		Check(
			"disabled_weird_successor_surface",
			ok,
			(
				f"disabled_focus_trees={len(disabled_focus_trees)} disabled_load_refs={len(disabled_load_refs)} "
				f"disabled_effect_blocks={len(disabled_effects)} disabled_spawn_triggers={len(disabled_triggers)} "
				f"disabled_decision_categories={len(disabled_decision_categories)} "
				f"disabled_category_defs={len(disabled_category_defs)} "
				f"disabled_objective_missions={len(disabled_objective_missions)} "
				f"disabled_objective_triggers={len(disabled_objective_triggers)} "
				f"disabled_objective_flags={len(disabled_objective_flags)} "
				f"disabled_gfx_refs={len(disabled_gfx_refs)} "
				f"disabled_doc_refs={len(disabled_doc_refs)} "
				f"disabled_tag_regs={len(disabled_tag_regs)} disabled_idea_prefixes={len(disabled_idea_prefixes)} "
				f"disabled_country_files={len(disabled_country_files)}"
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
	decoded = {}
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
				try:
					decoded[path] = read_tga_rgb_rows(path)
				except ValueError:
					decode_errors.append(str(path.relative_to(ROOT)))
	orientation_mismatches = []
	comparisons = 0
	source_dims = set()
	for tag in CUSTOM_TAGS:
		for variant in [""] + ["_" + ideology for ideology in IDEOLOGIES]:
			large_path = ROOT / "gfx/flags" / f"{tag}{variant}.tga"
			if large_path not in decoded:
				continue
			large_width, large_height, large_rows = decoded[large_path]
			source_dims.add(f"{large_width}x{large_height}")
			for folder in [ROOT / "gfx/flags/medium", ROOT / "gfx/flags/small"]:
				path = folder / f"{tag}{variant}.tga"
				if path not in decoded:
					continue
				width, height, rows = decoded[path]
				normal_rows = downsample_rgb_rows(large_rows, width, height)
				flipped_rows = downsample_rgb_rows(large_rows, width, height, flip_vertical=True)
				normal_diff = mean_abs_rgb_diff(normal_rows, rows)
				flipped_diff = mean_abs_rgb_diff(flipped_rows, rows)
				if flipped_diff + 0.5 < normal_diff:
					orientation_mismatches.append(f"{tag}{variant}:{folder.name}")
				comparisons += 1
	expected_checked = len(CUSTOM_TAGS) * (len(IDEOLOGIES) + 1) * 3
	expected_comparisons = len(CUSTOM_TAGS) * (len(IDEOLOGIES) + 1) * 2
	ok = checked == expected_checked and not missing and not decode_errors and top_origin == expected_checked and bottom_origin == 0
	surface_ok = ok and comparisons == expected_comparisons and not orientation_mismatches
	return [
		Check("flag_orientation_headers", ok, f"flags_checked={checked} missing={len(missing)} decode_errors={len(decode_errors)} top_origin={top_origin} bottom_origin={bottom_origin}"),
		Check(
			"flag_orientation_surface",
			surface_ok,
			(
				f"comparisons={comparisons} expected={expected_comparisons} orientation_mismatches={len(orientation_mismatches)} "
				f"source_dims={','.join(sorted(source_dims))}"
			),
		),
	]


def read_tga_rgb_rows(path: Path) -> tuple[int, int, list[list[tuple[int, int, int]]]]:
	data = path.read_bytes()
	if len(data) < 18:
		raise ValueError("short TGA header")
	image_type = data[2]
	if image_type != 2:
		raise ValueError(f"unsupported TGA type {image_type}")
	width = data[12] | (data[13] << 8)
	height = data[14] | (data[15] << 8)
	bpp = data[16]
	if width <= 0 or height <= 0 or bpp != 32:
		raise ValueError(f"unsupported TGA geometry {width}x{height}x{bpp}")
	step = bpp // 8
	offset = 18 + data[0]
	expected = offset + width * height * step
	if len(data) < expected:
		raise ValueError("truncated TGA pixel data")
	rows = []
	index = offset
	for _ in range(height):
		row = []
		for _ in range(width):
			blue, green, red = data[index], data[index + 1], data[index + 2]
			row.append((red, green, blue))
			index += step
		rows.append(row)
	descriptor = data[17]
	if not descriptor & 0x20:
		rows.reverse()
	if descriptor & 0x10:
		rows = [list(reversed(row)) for row in rows]
	return width, height, rows


def downsample_rgb_rows(rows: list[list[tuple[int, int, int]]], width: int, height: int, flip_vertical: bool = False) -> list[list[tuple[int, int, int]]]:
	source = list(reversed(rows)) if flip_vertical else rows
	source_height = len(source)
	source_width = len(source[0])
	output = []
	for target_y in range(height):
		source_y0 = int(target_y * source_height / height)
		source_y1 = max(source_y0 + 1, int((target_y + 1) * source_height / height))
		row = []
		for target_x in range(width):
			source_x0 = int(target_x * source_width / width)
			source_x1 = max(source_x0 + 1, int((target_x + 1) * source_width / width))
			red_total = 0
			green_total = 0
			blue_total = 0
			count = 0
			for source_y in range(source_y0, source_y1):
				for source_x in range(source_x0, source_x1):
					red, green, blue = source[source_y][source_x]
					red_total += red
					green_total += green
					blue_total += blue
					count += 1
			row.append((red_total // count, green_total // count, blue_total // count))
		output.append(row)
	return output


def mean_abs_rgb_diff(left: list[list[tuple[int, int, int]]], right: list[list[tuple[int, int, int]]]) -> float:
	total = 0
	count = 0
	for left_row, right_row in zip(left, right):
		for left_rgb, right_rgb in zip(left_row, right_row):
			total += abs(left_rgb[0] - right_rgb[0])
			total += abs(left_rgb[1] - right_rgb[1])
			total += abs(left_rgb[2] - right_rgb[2])
			count += 3
	return total / count


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
	achievements = read_text(ROOT / "common/achievements/chaos_redux_achievements.txt")
	marker = "# EVENT 005 - SOVIET UNION COLLAPSE"
	if marker not in achievements:
		return []
	section = achievements[achievements.index(marker):]
	end_match = re.search(r"^\d+_[A-Za-z0-9_]+_achievement\s*=", section, re.MULTILINE)
	if end_match:
		section = section[:end_match.start()]
	return re.findall(r"^(chaosx_ach_[A-Za-z0-9_]+)\s*=\s*\{", section, re.MULTILINE)


def verify_evolution_logging_surface() -> list[Check]:
	effects = read_text(ROOT / "common/scripted_effects/005_soviet_collapse_effects.txt")
	event_log_loc = read_text(ROOT / "common/scripted_localisation/chaosx_scripted_localisation_events_log.txt")
	custom_loc = read_text(ROOT / "localisation/english/005_soviet_collapse_custom_countries_l_english.yml")
	effect_tokens = tokens(effects)
	record_blocks = named_blocks(effect_tokens, "soviet_collapse_record_high_chaos_successor_evolution")
	record_body = " ".join(record_blocks[0]) if record_blocks else ""
	writer_count = len(re.findall(r"\brecord_events_log_evolution_entry\s*=\s*yes\b", effects))
	helper_calls = sum(
		1
		for tag in CUSTOM_TAGS
		if named_blocks(effect_tokens, f"soviet_collapse_setup_{tag.lower()}_successor")
		and "soviet_collapse_record_high_chaos_successor_evolution = yes" in " ".join(named_blocks(effect_tokens, f"soviet_collapse_setup_{tag.lower()}_successor")[0])
	)
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
		and record_lines >= 90
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
	ok = len(regular) >= 90 and not missing_ai and len(dynamic_ai) >= 90
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
		"## Final Completion Report",
		".tools/verify_event005_completion_gate.py",
		"Strict verifier result",
		"soviet_objective_board_surface",
		"event_log_mapping_surface",
		"focus_layout_surface",
		"first_wave_release_surface",
		"focus_ai_surface",
		"crisis_cause_surface",
		"force_scaling_surface",
		"idea_package_surface",
		"flag_orientation_surface",
		"source_context_files",
		"reference_context_surface",
		"source_order_surface",
		"input_audit_surface",
		"recovery_search_surface",
		"final_completion_report_surface",
		"strict_verifier_documentation_surface",
		"missing_continuation_direct_coverage_surface",
		"resume_validation_commands_surface",
		"success_criteria_surface",
		"available_source_acceptance_surface",
		"comprehensive_source_acceptance_surface",
		"prompt_artifact_checklist_surface",
		"verifier_command_documentation_surface",
		"focus_tree_map_surface",
		"validation_snapshot_freshness_surface",
	]
	event_markers = [
		"Event Logs event-detail entry for Event 005",
		"soviet_collapse_cleanup_terminal_collapse_missions",
		"Event 005 active custom country flags were audited",
		"315 active TGA files",
	]
	input_markers = [
		"tmp/005_soviet_union_collapse_event_log_mission_balance_focus_cleanup_spec.md",
		"historical missing continuation context",
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
		and row_values.get("L6") == "Implemented - Verified"
		and row_values.get("R6") == "Complete"
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
	bad_at_days = []
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
		if re.search(r"\bdays\s*=\s*@", text):
			bad_at_days.append(str(path.relative_to(ROOT)))
	return [
		Check("brace_depth", not bad_braces, f"bad_files={len(bad_braces)}"),
		Check("unsupported_operator_scan", not bad_operator, f"files_with_unsupported_operator={len(bad_operator)}"),
		Check("scoped_temp_variable_scan", not bad_scoped_temp, f"files_with_scoped_temp_variables={len(bad_scoped_temp)}"),
		Check("at_days_token_scan", not bad_at_days, f"files_with_at_days_tokens={len(bad_at_days)}"),
	]


def run_checks() -> list[Check]:
	checks: list[Check] = []
	checks.extend(verify_input_files())
	checks.extend(verify_source_context_files())
	checks.extend(verify_reference_context_surface())
	checks.extend(verify_source_order_surface())
	checks.extend(verify_input_audit_surface())
	checks.extend(verify_recovery_search_surface())
	checks.extend(verify_final_completion_report_surface())
	checks.extend(verify_strict_verifier_documentation_surface())
	checks.extend(verify_missing_continuation_direct_coverage_surface())
	checks.extend(verify_resume_validation_commands_surface())
	checks.extend(verify_success_criteria_surface())
	checks.extend(verify_available_source_acceptance_surface())
	checks.extend(verify_comprehensive_source_acceptance_surface())
	checks.extend(verify_prompt_artifact_checklist_surface())
	checks.extend(verify_verifier_command_documentation_surface())
	checks.extend(verify_focus_tree_map_documentation_surface())
	checks.extend(verify_mission_audit_documentation_surface())
	checks.extend(verify_validation_snapshot_freshness_surface())
	checks.extend(verify_braces_and_unsupported())
	checks.extend(verify_focuses())
	checks.extend(verify_ideas())
	checks.extend(verify_breakaway_recovery_surface())
	checks.extend(verify_first_wave_and_forces())
	checks.extend(verify_dynamic_force_coverage())
	checks.extend(verify_crisis_balance())
	checks.extend(verify_foreign_influence_surface())
	checks.extend(verify_reintegration_puppet_surface())
	checks.extend(verify_local_league_surface())
	checks.extend(verify_union_unmade_and_cleanup())
	checks.extend(verify_soviet_objective_board())
	checks.extend(verify_terminal_ordinary_republics())
	checks.extend(verify_mtth_release_surface())
	checks.extend(verify_terminal_high_chaos_successors())
	checks.extend(verify_disabled_weird_successor_surface())
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
	parser.add_argument("--allow-missing-continuation-spec", action="store_true", help="legacy no-op; the old continuation spec is not part of the active required source order")
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
		print("Missing required active input blocker was waived for this verifier run.")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
