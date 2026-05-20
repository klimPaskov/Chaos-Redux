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


def focus_blocks(text: str) -> dict[str, str]:
	blocks: dict[str, str] = {}
	for match in re.finditer(r"(?m)^\s*focus\s*=\s*\{", text):
		block = block_from_match(text, match)
		id_match = re.search(r"(?m)^\s*id\s*=\s*([A-Za-z0-9_]+)", block)
		if id_match:
			blocks[id_match.group(1)] = block
	return blocks


def loc_keys(text: str) -> set[str]:
	return set(re.findall(r"(?m)^([A-Za-z0-9_]+):\s*\"", text))


def constant_values(text: str, section: str) -> dict[str, float]:
	block = block_after(text, section)
	return {
		match.group(1): float(match.group(2))
		for match in re.finditer(r"(?m)^\s*([A-Za-z0-9_]+)\s*=\s*(-?\d+(?:\.\d+)?)\s*$", block)
	}


def threat_value(components: dict[str, float], baseline: dict[str, float]) -> float:
	raw = (
		components["republic_confidence"]
		+ components["depot_vulnerability"]
		+ components["foreign_appetite"]
		+ components["league_cohesion"]
		+ components["old_movement_pressure"]
		+ baseline["total_threat_offset"]
		- components["moscow_authority"]
		- components["military_obedience"]
	)
	threat = raw * baseline["total_threat_multiplier"]
	return max(baseline["total_threat_floor"], min(baseline["total_threat_ceiling"], threat))


def pressure_deltas(pressure: dict[str, float], outcome: str, multiplier: float) -> dict[str, float]:
	deltas: dict[str, float] = {}
	marker = f"_{outcome}_"
	for key, value in pressure.items():
		if marker not in key:
			continue
		family, component = key.split(marker, 1)
		sign = -1 if component in {"authority", "obedience"} else 1
		deltas[family] = deltas.get(family, 0.0) + sign * value * multiplier
	return deltas


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
	constants = read("common/script_constants/005_soviet_collapse_constants.txt")
	focus = read("common/national_focus/005_soviet_collapse_republics.txt")
	all_focus = "\n".join(read(rel) for rel in FOCUS_FILES)
	mission_audit = read("docs/events/005_soviet_union_collapse_mission_audit.md")
	loc_paths = sorted((ROOT / "localisation/english").glob("005_soviet_collapse*_l_english.yml"))
	localisation = "\n".join(path.read_text(encoding="utf-8-sig") for path in loc_paths)

	failed |= not check(
		"unsupported_operators",
		"<=" not in effects and ">=" not in effects and "<=" not in triggers and ">=" not in triggers,
		"no <= or >= in edited core script surfaces",
	)

	recalc = block_after(effects, "soviet_collapse_recalculate_total_threat")
	progressive = block_after(effects, "soviet_collapse_maybe_release_threat_breakaway")
	init = block_after(effects, "soviet_collapse_initialize_crisis_values")
	maybe_union_unmade = block_after(effects, "soviet_collapse_maybe_show_union_unmade_super_event")
	monthly_guard = block_after(effects, "soviet_collapse_apply_monthly_threat_guard")
	baseline = constant_values(constants, "soviet_collapse_baseline")
	threat_guard = constant_values(constants, "soviet_collapse_threat_guard")
	progressive_release = constant_values(constants, "soviet_collapse_progressive_release")
	opening_pressure = constant_values(constants, "soviet_collapse_opening_pressure")
	soviet_objective = constant_values(constants, "soviet_collapse_soviet_objective")
	objective_pressure = constant_values(constants, "soviet_collapse_objective_pressure")
	super_event = constant_values(constants, "soviet_collapse_super_event")
	release_mtth = constant_values(constants, "soviet_collapse_release_mtth")
	calm_components = {
		key: baseline[key]
		for key in [
			"moscow_authority",
			"republic_confidence",
			"military_obedience",
			"depot_vulnerability",
			"foreign_appetite",
			"league_cohesion",
			"old_movement_pressure",
		]
	}
	calm_threat = threat_value(calm_components, baseline)
	severe_components = dict(calm_components)
	severe_components["republic_confidence"] += (
		opening_pressure["chaos_tier_final"]
		+ opening_pressure["low_stability"]
		+ opening_pressure["low_war_support"]
		+ opening_pressure["capital_lost"]
	)
	severe_components["depot_vulnerability"] += opening_pressure["chaos_tier_final"] + opening_pressure["active_war"]
	severe_components["foreign_appetite"] += opening_pressure["chaos_tier_final_foreign_appetite"] + opening_pressure["active_war"]
	severe_components["old_movement_pressure"] += opening_pressure["chaos_tier_final_old_movement_pressure"]
	severe_components["moscow_authority"] += opening_pressure["low_stability_authority"] + opening_pressure["capital_lost_authority"]
	severe_components["military_obedience"] += opening_pressure["low_war_support_obedience"]
	severe_threat = threat_value(severe_components, baseline)
	success_deltas = pressure_deltas(objective_pressure, "success", baseline["total_threat_multiplier"])
	failure_deltas = pressure_deltas(objective_pressure, "failure", baseline["total_threat_multiplier"])
	max_success_delta = max(success_deltas.values())
	max_failure_delta = max(failure_deltas.values())
	active_cap = int(soviet_objective["active_cap"])
	first_wave_failure_pressure = calm_threat + active_cap * max_failure_delta
	failed |= not check(
		"crisis_balance_surface",
		calm_threat < threat_guard["calm_threat_ceiling"]
		and severe_threat < super_event["union_unmade_high_threat"]
		and severe_threat < progressive_release["severe_threat"],
		f"calm={calm_threat:.2f} severe={severe_threat:.2f}",
	)
	failed |= not check(
		"crisis_monthly_guard_surface",
		"constant:soviet_collapse_threat_guard.calm_success_month_cap" in monthly_guard
		and "constant:soviet_collapse_threat_guard.moderate_success_month_cap" in monthly_guard
		and "soviet_collapse_monthly_successful_objectives" in monthly_guard
		and "soviet_collapse_monthly_failed_objectives" in monthly_guard
		and "set_variable = { soviet_collapse_last_month_total_threat = soviet_collapse_total_collapse_threat }" in monthly_guard,
		"calm and moderate success-month caps present",
	)
	failed |= not check(
		"mission_success_pressure_surface",
		max_success_delta <= 0,
		f"least_stabilizing={max_success_delta:.2f} strongest={min(success_deltas.values()):.2f}",
	)
	failed |= not check(
		"mission_failure_pressure_surface",
		max_failure_delta <= 4.25
		and first_wave_failure_pressure < super_event["union_unmade_high_threat"],
		f"max_failure={max_failure_delta:.2f} active_cap={active_cap} first_wave={first_wave_failure_pressure:.2f}",
	)
	failed |= not check(
		"union_unmade_first_month_guard_surface",
		"soviet_collapse_union_unmade_first_month_lock" in init
		and "days = 31" in init
		and "NOT = { has_global_flag = soviet_collapse_union_unmade_first_month_lock }" in maybe_union_unmade
		and "constant:soviet_collapse_super_event.min_breakaways_for_union_unmade" in maybe_union_unmade
		and "constant:soviet_collapse_super_event.union_unmade_high_threat" in maybe_union_unmade
		and "constant:soviet_collapse_super_event.union_unmade_critical_authority" in maybe_union_unmade,
		"31-day lock and severe ingredient gates present",
	)
	failed |= not check(
		"union_unmade_pacing",
		super_event["min_breakaways_for_union_unmade"] >= 5
		and super_event["union_unmade_high_threat"] >= 60
		and super_event["union_unmade_critical_authority"] <= 25
		and super_event["union_unmade_contested_authority"] <= 45
		and "constant:soviet_collapse_super_event.min_breakaways_for_union_unmade" in maybe_union_unmade
		and "constant:soviet_collapse_super_event.union_unmade_high_threat" in maybe_union_unmade
		and "constant:soviet_collapse_super_event.union_unmade_critical_authority" in maybe_union_unmade
		and "constant:soviet_collapse_super_event.union_unmade_contested_authority" in maybe_union_unmade,
		"breakaways=5 high_threat=60 critical_authority=25 contested_authority=45",
	)
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
	failed |= not check(
		"terminal_ordinary_republic_release_surface",
		required_terminal <= release_tags
		and "release = PREV" in terminal_release
		and "set_autonomy = { target = PREV autonomy_state = autonomy_free }" in terminal_release
		and "soviet_collapse_setup_breakaway_country = yes" in terminal_release,
		"ordinary and internal release/setup paths present",
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
	baltic_quorum = block_after(triggers, "has_soviet_collapse_baltic_league_quorum")
	caucasus_quorum = block_after(triggers, "has_soviet_collapse_caucasus_league_quorum")
	central_asian_quorum = block_after(triggers, "has_soviet_collapse_central_asian_league_quorum")
	failed |= not check(
		"local_league_surface",
		all(tag in baltic_quorum for tag in ["LIT", "LAT", "EST"])
		and all(tag in caucasus_quorum for tag in ["GEO", "ARM", "AZR"])
		and all(tag in central_asian_quorum for tag in ["UZB", "KYR", "TAJ", "TMS", "KAZ"])
		and not any(tag in caucasus_quorum for tag in ["MRC"])
		and not any(tag in central_asian_quorum for tag in ["BSC", "TNC", "ALA"])
		and "has_soviet_collapse_baltic_league_quorum = yes" in block_after(triggers, "can_found_soviet_collapse_baltic_league")
		and "has_soviet_collapse_caucasus_league_quorum = yes" in block_after(triggers, "can_found_soviet_collapse_caucasus_league")
		and "has_soviet_collapse_central_asian_league_quorum = yes" in block_after(triggers, "can_found_soviet_collapse_central_asian_league"),
		"founding triggers require regional quorums",
	)

	progressive_release_effect = block_after(effects, "soviet_collapse_maybe_release_threat_breakaway")
	progressive_release_event = block_after(effects, "soviet_collapse_fire_progressive_release_event")
	release_cause_ids = {f"chaosx.nr5.{event_id}" for event_id in range(130, 138)}
	release_causes = [
		"ministry", "rail", "border", "party", "foreign", "depot", "old_movement", "league",
	]
	failed |= not check(
		"mtth_release_surface",
		release_mtth["release_base"] < release_mtth["miss_base"]
		and all(f"constant:soviet_collapse_release_mtth.cause_{cause}_weight" in progressive_release_event for cause in release_causes)
		and all(event_id in progressive_release_event for event_id in release_cause_ids)
		and "mtth:soviet_collapse_progressive_release_weight" in progressive_release_effect
		and "mtth:soviet_collapse_progressive_release_miss_weight" in progressive_release_effect
		and "soviet_collapse_progressive_release_cooldown" in block_after(effects, "soviet_collapse_release_one_threat_breakaway_republic"),
		"8 cause events, MTTH release/miss weights, and cooldown present",
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
	terminal_cleanup = block_after(effects, "soviet_collapse_cleanup_terminal_collapse_missions")
	terminal_cleanup_refs = len(re.findall(r"\bremove_mission\s*=\s*soviet_collapse_soviet_mission_\d+_", terminal_cleanup))
	failed |= not check(
		"mission_wiring_counts",
		mission_count > 0 and mission_count == activation_refs == removal_refs,
		f"missions={mission_count} activation={activation_refs} cleanup={removal_refs}",
	)
	failed |= not check(
		"terminal_mission_cleanup",
		mission_count > 0
		and terminal_cleanup_refs == mission_count
		and "soviet_collapse_cleanup_terminal_collapse_missions = yes" in terminal,
		f"cleanup={terminal_cleanup_refs} missions={mission_count}",
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
	mission_audit_header = (
		"| Mission | Owner | Category | Region | Target states or capitals | Duration | Success condition | "
		"Failure condition | Success effect | Failure effect | Duplicate check |"
	)
	mission_audit_rows = re.findall(r"(?m)^\| \d{3} `soviet_collapse_soviet_mission_\d+_", mission_audit)
	failed |= not check(
		"mission_audit_table_surface",
		mission_audit_header in mission_audit
		and len(mission_audit_rows) == mission_count
		and "mission_quality_surface" not in mission_audit
		and "mission_requirement_surface" not in mission_audit,
		f"rows={len(mission_audit_rows)} missions={mission_count}",
	)

	focus_ids = re.findall(r"(?m)^\s*id\s*=\s*([A-Za-z0-9_]+)", all_focus)
	duplicate_focuses = sorted({focus_id for focus_id in focus_ids if focus_ids.count(focus_id) > 1})
	failed |= not check(
		"event005_focus_unique_ids",
		not duplicate_focuses,
		"duplicates=" + ",".join(duplicate_focuses[:20]),
	)
	focus_map = focus_blocks(all_focus)
	missing_focus_shape = sorted(
		focus_id for focus_id, block in focus_map.items()
		if not all(re.search(rf"(?m)^\s*{field}\s*=", block) for field in ["icon", "x", "y", "completion_reward", "ai_will_do"])
	)
	focus_ref_pairs = [
		(focus_id, ref)
		for focus_id, block in focus_map.items()
		for ref in re.findall(r"\bfocus\s*=\s*([A-Za-z0-9_]+)", block)
	]
	missing_focus_refs = sorted(f"{focus_id}->{ref}" for focus_id, ref in focus_ref_pairs if ref not in focus_map)
	failed |= not check(
		"event005_focus_integrity_surface",
		len(focus_map) >= 775 and not missing_focus_shape and not missing_focus_refs,
		f"focuses={len(focus_map)} bad_shape=" + ",".join(missing_focus_shape[:10]) + " missing_refs=" + ",".join(missing_focus_refs[:10]),
	)
	material_reward_pattern = (
		r"\b(add_building_construction|add_extra_state_shared_building_slots|add_equipment_to_stockpile|"
		r"add_manpower|add_political_power|add_stability|add_war_support|add_command_power|army_experience|add_to_faction)\b"
	)
	focus_helper_pattern = r"\bsoviet_collapse_apply_focus_[A-Za-z0-9_]+\b"
	material_reward_focuses = sum(1 for block in focus_map.values() if re.search(material_reward_pattern, block))
	focus_helper_reward_focuses = sum(1 for block in focus_map.values() if re.search(focus_helper_pattern, block))
	idea_only_focuses = sum(
		1 for block in focus_map.values()
		if "add_ideas" in block
		and not re.search(material_reward_pattern, block)
		and not re.search(focus_helper_pattern, block)
	)
	ai_contextual_focuses = sum(1 for block in focus_map.values() if "ai_will_do" in block and "modifier =" in block)
	failed |= not check(
		"focus_reward_variety_surface",
		material_reward_focuses >= 500
		and focus_helper_reward_focuses >= 250
		and idea_only_focuses <= 40,
		f"material={material_reward_focuses} focus_helpers={focus_helper_reward_focuses} idea_only={idea_only_focuses}",
	)
	failed |= not check(
		"focus_ai_surface",
		ai_contextual_focuses >= 190,
		f"contextual_ai={ai_contextual_focuses}",
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
