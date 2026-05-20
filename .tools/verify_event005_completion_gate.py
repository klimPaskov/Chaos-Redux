#!/usr/bin/env python3
"""Deterministic Event 005 surface checks.

This verifier is intentionally conservative: it proves selected implementation
surfaces that are easy to regress in script, while docs and live play still own
the full design judgement.

Exit codes:
- 0: checked gates passed.
- 1: one or more checked gates failed.
- 2: checked gates passed, but required source inputs are missing.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_INPUTS = [
	"tmp/005_soviet_union_collapse_serious_completion_audit_spec.md",
	"tmp/005_soviet_union_collapse_terminal_release_league_threat_correction_spec.md",
	"tmp/soviet_collapse_republic_focus_tree_mandatory_package/soviet_collapse_republic_focus_tree_mandatory_package/specs/005_soviet_union_collapse_republic_focus_tree_part_1_universal_rules.md",
	"tmp/soviet_collapse_republic_focus_tree_mandatory_package/soviet_collapse_republic_focus_tree_mandatory_package/specs/005_soviet_union_collapse_republic_focus_tree_part_2_ukraine_belarus.md",
	"tmp/soviet_collapse_republic_focus_tree_mandatory_package/soviet_collapse_republic_focus_tree_mandatory_package/specs/005_soviet_union_collapse_republic_focus_tree_part_3_kazakhstan_central_asia.md",
	"tmp/soviet_collapse_republic_focus_tree_mandatory_package/soviet_collapse_republic_focus_tree_mandatory_package/specs/005_soviet_union_collapse_republic_focus_tree_part_4_baltic_caucasus_moldova_karelia_fallback.md",
	"tmp/soviet_collapse_republic_focus_tree_mandatory_package/soviet_collapse_republic_focus_tree_mandatory_package/matrices/005_soviet_union_collapse_republic_focus_tree_route_matrix.md",
	"tmp/soviet_collapse_republic_focus_tree_mandatory_package/soviet_collapse_republic_focus_tree_mandatory_package/prompts/coding_prompt.md",
	"tmp/soviet_collapse_republic_focus_tree_mandatory_package/soviet_collapse_republic_focus_tree_mandatory_package/prompts/goal_prompt.md",
	"tmp/soviet_collapse_republic_focus_tree_mandatory_package/soviet_collapse_republic_focus_tree_mandatory_package/research/005_soviet_union_collapse_republic_focus_tree_research_notes.md",
	"tmp/005_soviet_union_collapse_final_clean_spec_part_1_core_crisis.md",
	"tmp/005_soviet_union_collapse_final_clean_spec_part_2_objectives_missions_intervention.md",
	"tmp/005_soviet_union_collapse_final_clean_spec_part_3_republics_focus_trees.md",
	"tmp/005_soviet_union_collapse_final_clean_spec_part_4_custom_countries_evolutions_assets_achievements.md",
	"AGENTS.md",
	".agents/skills/chaos-redux-events/SKILL.md",
	".agents/skills/chaos-redux-event-assets/SKILL.md",
	".agents/skills/chaos-redux-super-events/SKILL.md",
]

ORDINARY_TERMINAL_TAGS = {
	"UKR", "BLR", "KAZ", "MOL", "LIT", "LAT", "EST", "GEO", "ARM", "AZR",
	"UZB", "KYR", "TAJ", "TMS",
}

INTERNAL_TERMINAL_TAGS = {
	"KAR", "KOM", "CRI", "TAT", "BSK", "FER", "YAK", "BYA", "TAN",
}

FREE_LEAGUE_TERMINAL_TAGS = ORDINARY_TERMINAL_TAGS | INTERNAL_TERMINAL_TAGS | {
	"FEV", "SZA", "IUL", "UWD", "BAC",
}

REGIONAL_LEAGUE_FUNCTIONS = [
	"soviet_collapse_found_terminal_baltic_restoration_pact",
	"soviet_collapse_found_terminal_caucasus_defense_compact",
	"soviet_collapse_found_terminal_central_asian_league",
	"soviet_collapse_refresh_baltic_regional_faction",
	"soviet_collapse_refresh_caucasus_regional_faction",
	"soviet_collapse_refresh_central_asian_regional_faction",
	"soviet_collapse_form_terminal_regional_leagues",
]

FOCUS_FILES = [
	"common/national_focus/005_soviet_collapse_republics.txt",
	"common/national_focus/005_soviet_collapse_custom_splinters.txt",
	"common/national_focus/005_soviet_collapse_factory_successors.txt",
]

INTERNAL_REPUBLIC_FOCUS_IDS = {
	"internal_soviet_collapse_convene_republic_presidium",
	"internal_soviet_collapse_secure_autonomous_capital",
	"internal_soviet_collapse_map_union_property",
	"internal_soviet_collapse_form_republic_guard",
	"internal_soviet_collapse_write_the_autonomy_statute",
	"internal_soviet_collapse_legal_autonomy_congress",
	"internal_soviet_collapse_security_council",
	"internal_soviet_collapse_border_and_rail_liaisons",
	"internal_soviet_collapse_forest_republic_committees",
	"internal_soviet_collapse_white_sea_rail_watch",
	"internal_soviet_collapse_volga_oil_and_workshops",
	"internal_soviet_collapse_ural_cavalry_roads",
	"internal_soviet_collapse_black_sea_peninsula_guard",
	"internal_soviet_collapse_crimean_tatar_councils",
	"internal_soviet_collapse_siberian_rail_authorities",
	"internal_soviet_collapse_taiga_steppe_self_rule",
	"internal_soviet_collapse_trade_oaths_with_neighbors",
	"internal_soviet_collapse_free_republics_wire",
	"internal_soviet_collapse_terminal_survival_plan",
	"internal_soviet_collapse_no_return_to_oblast_rule",
}


def read(rel: str) -> str:
	path = ROOT / rel
	return path.read_text(encoding="utf-8-sig")


def block_after(text: str, name: str) -> str:
	match = re.search(rf"(?m)^\s*{re.escape(name)}\s*=\s*\{{", text)
	if not match:
		return ""
	return block_from_match(text, match)


def block_from_match(text: str, match: re.Match[str]) -> str:
	start = match.end()
	depth = 1
	i = start
	while i < len(text) and depth:
		if text[i] == "{":
			depth += 1
		elif text[i] == "}":
			depth -= 1
		i += 1
	return text[start:i - 1] if depth == 0 else ""


def focus_tree_block(text: str, tree_id: str) -> str:
	match = re.search(rf"(?m)^\s*id\s*=\s*{re.escape(tree_id)}\b", text)
	if not match:
		return ""
	tree_start = text.rfind("focus_tree = {", 0, match.start())
	if tree_start < 0:
		return ""
	start = text.find("{", tree_start) + 1
	depth = 1
	i = start
	while i < len(text) and depth:
		if text[i] == "{":
			depth += 1
		elif text[i] == "}":
			depth -= 1
		i += 1
	return text[start:i - 1] if depth == 0 else ""


def tags_in(block: str) -> set[str]:
	return set(re.findall(r"\btag\s*=\s*([A-Z][A-Z0-9]{2})\b", block))


def mission_blocks(text: str) -> dict[str, str]:
	blocks: dict[str, str] = {}
	for match in re.finditer(r"(?m)^\s*(soviet_collapse_soviet_mission_\d+_[A-Za-z0-9_]+)\s*=\s*\{", text):
		blocks[match.group(1)] = block_from_match(text, match)
	return blocks


def loc_keys(text: str) -> set[str]:
	return set(re.findall(r"(?m)^([A-Za-z0-9_]+):\s*\"", text))


def check(name: str, ok: bool, details: str = "") -> bool:
	status = "PASS" if ok else "FAIL"
	print(f"{status} {name}{': ' + details if details else ''}")
	return ok


def main() -> int:
	parser = argparse.ArgumentParser()
	parser.add_argument("--allow-missing-continuation-spec", action="store_true")
	args = parser.parse_args()

	failed = False
	missing_inputs = [rel for rel in REQUIRED_INPUTS if not (ROOT / rel).exists()]
	if missing_inputs:
		for rel in missing_inputs:
			print(f"MISSING input: {rel}")
		if not args.allow_missing_continuation_spec:
			return 2

	effects = read("common/scripted_effects/005_soviet_collapse_effects.txt")
	triggers = read("common/scripted_triggers/005_soviet_collapse_triggers.txt")
	decisions = read("common/decisions/005_soviet_collapse_decisions.txt")
	focus = read("common/national_focus/005_soviet_collapse_republics.txt")
	all_focus = "\n".join(read(rel) for rel in FOCUS_FILES)
	loc_paths = sorted((ROOT / "localisation/english").glob("005_soviet_collapse*_l_english.yml"))
	localisation = "\n".join(path.read_text(encoding="utf-8-sig") for path in loc_paths)

	failed |= not check(
		"unsupported_operators",
		"<=" not in effects and ">=" not in effects and "<=" not in triggers and ">=" not in triggers,
		"no <= or >= in edited core script surfaces",
	)

	recalc = block_after(effects, "soviet_collapse_recalculate_total_threat")
	progressive = block_after(effects, "soviet_collapse_maybe_release_threat_breakaway")
	failed |= not check(
		"union_unmade_guarded_ceiling",
		"soviet_collapse_maybe_show_union_unmade_super_event = yes" in recalc
		and "soviet_collapse_show_union_unmade_super_event = yes" not in recalc
		and "soviet_collapse_maybe_show_union_unmade_super_event = yes" in progressive,
		"threat ceiling uses guarded helper",
	)

	terminal_release = block_after(effects, "soviet_collapse_release_terminal_ordinary_republics")
	release_tags = tags_in(terminal_release)
	required_terminal = ORDINARY_TERMINAL_TAGS | INTERNAL_TERMINAL_TAGS
	failed |= not check(
		"terminal_release_tags",
		required_terminal <= release_tags,
		"missing=" + ",".join(sorted(required_terminal - release_tags)),
	)
	failed |= not check(
		"terminal_subject_freeing",
		all(f"tag = {tag}" in terminal_release for tag in required_terminal)
		and "set_autonomy = { target = PREV autonomy_state = autonomy_free }" in terminal_release,
		"ordinary and internal tags share release/freeing surface",
	)

	terminal = block_after(effects, "soviet_collapse_apply_terminal_collapse")
	sequence = [
		"soviet_collapse_release_terminal_ordinary_republics = yes",
		"soviet_collapse_spawn_terminal_high_chaos_successors = yes",
		"soviet_collapse_form_terminal_leagues = yes",
		"soviet_collapse_start_terminal_anti_soviet_war = yes",
		"soviet_collapse_cleanup_terminal_collapse_missions = yes",
	]
	positions = [terminal.find(item) for item in sequence]
	failed |= not check(
		"terminal_sequence",
		all(pos >= 0 for pos in positions) and positions == sorted(positions),
		"release -> spawn -> leagues -> war -> cleanup",
	)

	failed |= not check(
		"terminal_regional_leagues",
		all(block_after(effects, fn) for fn in REGIONAL_LEAGUE_FUNCTIONS)
		and "soviet_collapse_found_terminal_regional_faction_common" in effects
		and "add_political_power" not in block_after(effects, "soviet_collapse_found_terminal_regional_faction_common")
		and "add_command_power" not in block_after(effects, "soviet_collapse_found_terminal_regional_faction_common"),
		"terminal local league helpers present and no-cost",
	)

	free_invite = block_after(effects, "soviet_collapse_invite_free_republics_league_partners")
	failed |= not check(
		"terminal_free_league_members",
		FREE_LEAGUE_TERMINAL_TAGS <= set(re.findall(r"\b([A-Z][A-Z0-9]{2})\s*=\s*\{[^{}]*exists\s*=\s*yes", free_invite)),
		"missing=" + ",".join(sorted(FREE_LEAGUE_TERMINAL_TAGS - set(re.findall(r"\b([A-Z][A-Z0-9]{2})\s*=\s*\{[^{}]*exists\s*=\s*yes", free_invite)))),
	)

	failed |= not check(
		"local_league_quorums",
		all(name in triggers for name in [
			"has_soviet_collapse_baltic_league_quorum",
			"has_soviet_collapse_caucasus_league_quorum",
			"has_soviet_collapse_central_asian_league_quorum",
		]),
		"quorum triggers exist",
	)

	loader = block_after(effects, "soviet_collapse_load_event_created_focus_tree")
	internal_tree_pos = loader.find("load_focus_tree = { tree = soviet_collapse_internal_republic_focus_tree }")
	internal_loader_context = loader[max(0, internal_tree_pos - 700):internal_tree_pos] if internal_tree_pos >= 0 else ""
	failed |= not check(
		"internal_republic_focus_loader",
		internal_tree_pos >= 0 and INTERNAL_TERMINAL_TAGS <= tags_in(internal_loader_context),
		"missing=" + ",".join(sorted(INTERNAL_TERMINAL_TAGS - tags_in(internal_loader_context))),
	)

	internal_tree = focus_tree_block(focus, "soviet_collapse_internal_republic_focus_tree")
	internal_focus_ids = set(re.findall(r"(?m)^\s*id\s*=\s*(internal_soviet_collapse_[A-Za-z0-9_]+)", internal_tree))
	failed |= not check(
		"internal_republic_focus_tree",
		INTERNAL_REPUBLIC_FOCUS_IDS <= internal_focus_ids
		and all(f"tag = {tag}" in internal_tree for tag in INTERNAL_TERMINAL_TAGS)
		and "soviet_collapse_apply_focus_league_preparation = yes" in internal_tree
		and "soviet_collapse_apply_focus_high_chaos_identity = yes" in internal_tree,
		"missing=" + ",".join(sorted(INTERNAL_REPUBLIC_FOCUS_IDS - internal_focus_ids)),
	)
	failed |= not check(
		"internal_republic_focus_localisation",
		"soviet_collapse_internal_republic_focus_tree:" in localisation
		and all(f"{focus_id}:" in localisation and f"{focus_id}_desc:" in localisation for focus_id in INTERNAL_REPUBLIC_FOCUS_IDS),
		"tree and focus keys are localised",
	)

	missions = mission_blocks(decisions)
	mission_names = set(missions)
	localisation_keys = loc_keys(localisation)
	missing_mission_loc = sorted(
		key
		for mission in mission_names
		for key in [mission, f"{mission}_desc", f"{mission}_req_tt", f"{mission}_success_tt", f"{mission}_failure_tt"]
		if key not in localisation_keys
	)
	missing_shape = sorted(
		mission for mission, block in missions.items()
		if "selectable_mission = no" not in block
		or "is_good = yes" not in block
		or "days_mission_timeout =" not in block
		or "custom_trigger_tooltip" not in block
		or f"tooltip = {mission}_req_tt" not in block
		or "hidden_trigger = {" not in block
		or "complete_effect = {" not in block
		or "timeout_effect = {" not in block
	)
	identical_outcomes = []
	for mission, block in missions.items():
		complete = re.search(r"(?m)^\s*complete_effect\s*=\s*\{(.*)\}\s*$", block)
		timeout = re.search(r"(?m)^\s*timeout_effect\s*=\s*\{(.*)\}\s*$", block)
		if complete and timeout and complete.group(1) == timeout.group(1):
			identical_outcomes.append(mission)
	weak_requirement_loc = sorted(
		key[:-7]
		for key in localisation_keys
		if key.endswith("_req_tt")
		and key[:-7] in mission_names
		and re.search(
			r"required states|border states|todo|tbd|placeholder|unknown",
			re.search(rf"(?m)^{re.escape(key)}:\s*\"(.*)\"", localisation).group(1),
			re.IGNORECASE,
		)
	)

	mission_count = len(missions)
	activation_refs = len(re.findall(r"\bactivate_mission\s*=\s*soviet_collapse_soviet_mission_\d+_", effects))
	removal_refs = len(re.findall(r"\bremove_mission\s*=\s*soviet_collapse_soviet_mission_\d+_", effects))
	failed |= not check(
		"mission_wiring_counts",
		mission_count > 0 and mission_count == activation_refs == removal_refs,
		f"missions={mission_count} activation={activation_refs} cleanup={removal_refs}",
	)
	failed |= not check(
		"mission_objective_shape",
		not missing_shape and not identical_outcomes,
		"bad_shape=" + ",".join(missing_shape[:10]) + " identical=" + ",".join(identical_outcomes[:10]),
	)
	failed |= not check(
		"mission_localisation_surface",
		not missing_mission_loc and not weak_requirement_loc,
		"missing=" + ",".join(missing_mission_loc[:10]) + " weak_req=" + ",".join(weak_requirement_loc[:10]),
	)

	focus_ids = re.findall(r"(?m)^\s*id\s*=\s*([A-Za-z0-9_]+)", all_focus)
	duplicate_focuses = sorted({focus_id for focus_id in focus_ids if focus_ids.count(focus_id) > 1})
	failed |= not check(
		"event005_focus_unique_ids",
		not duplicate_focuses,
		"duplicates=" + ",".join(duplicate_focuses[:20]),
	)
	missing_focus_loc = sorted(focus_id for focus_id in focus_ids if focus_id not in localisation_keys)
	missing_focus_desc = sorted(
		focus_id for focus_id in focus_ids
		if not focus_id.endswith("_focus_tree") and f"{focus_id}_desc" not in localisation_keys
	)
	bad_bom = sorted(str(path.relative_to(ROOT)) for path in loc_paths if not path.read_bytes().startswith(b"\xef\xbb\xbf"))
	failed |= not check(
		"event005_focus_localisation",
		not missing_focus_loc and not missing_focus_desc,
		"missing=" + ",".join(missing_focus_loc[:10]) + " missing_desc=" + ",".join(missing_focus_desc[:10]),
	)
	failed |= not check(
		"event005_localisation_format",
		not bad_bom and not re.search(r"(?m)^[A-Za-z0-9_]+:0\s*\"", localisation),
		"bad_bom=" + ",".join(bad_bom[:10]),
	)

	if failed:
		return 1
	if missing_inputs:
		return 2
	return 0


if __name__ == "__main__":
	sys.exit(main())
