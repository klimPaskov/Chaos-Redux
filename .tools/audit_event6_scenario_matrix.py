#!/usr/bin/env python3
"""Audit the non-live SCN-008 mode and collision acceptance receipts.

This validator checks source witnesses and documentation cardinality. It does
not execute Clausewitz, allocate a live map, or promote an Event 006 package.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "docs/plans/006_independence_wave_plans/subagent_handoffs/006_scn008_32_cell_static_acceptance_2026_08_02.md"
EDGE_MATRIX = ROOT / "docs/plans/006_independence_wave_plans/006_event6_scn008_edge_case_source_matrix_current_2026-09-25.md"


def read(relative: str) -> str:
	return (ROOT / relative).read_text(encoding="utf-8-sig")


def require(condition: bool, message: str, errors: list[str]) -> None:
	if not condition:
		errors.append(message)


def extract_block_at(text: str, start: int) -> tuple[str, int]:
	opening = text.find("{", start)
	if opening < 0:
		raise ValueError("missing opening brace")
	depth = 0
	quoted = False
	escaped = False
	comment = False
	for index in range(opening, len(text)):
		char = text[index]
		if comment:
			if char in "\r\n":
				comment = False
			continue
		if quoted:
			if escaped:
				escaped = False
			elif char == "\\":
				escaped = True
			elif char == '"':
				quoted = False
			continue
		if char == "#":
			comment = True
		elif char == '"':
			quoted = True
		elif char == "{":
			depth += 1
		elif char == "}":
			depth -= 1
			if depth == 0:
				return text[start : index + 1], index + 1
	raise ValueError("unterminated block")


def extract_script_block(text: str, name: str) -> str:
	match = re.search(rf"(?m)^{re.escape(name)}\s*=\s*\{{", text)
	if match is None:
		raise ValueError(f"missing scripted block {name}")
	try:
		return extract_block_at(text, match.start())[0]
	except ValueError as exc:
		raise ValueError(f"unterminated scripted block {name}") from exc


def extract_named_block(text: str, name: str) -> str:
	match = re.search(rf"(?m)^[ \t]*{re.escape(name)}\s*=\s*\{{", text)
	if match is None:
		raise ValueError(f"missing named block {name}")
	try:
		return extract_block_at(text, match.start())[0]
	except ValueError as exc:
		raise ValueError(f"unterminated named block {name}") from exc


def extract_block_containing(text: str, needle: str, opener: str) -> str:
	marker = text.find(needle)
	if marker < 0:
		raise ValueError(f"missing marker {needle}")
	start = text.rfind(opener, 0, marker)
	if start < 0:
		raise ValueError(f"missing enclosing block for {needle}")
	try:
		return extract_block_at(text, start)[0]
	except ValueError as exc:
		raise ValueError(f"unterminated enclosing block for {needle}") from exc


def extract_block_containing_with_end(text: str, needle: str, opener: str) -> tuple[str, int]:
	marker = text.find(needle)
	if marker < 0:
		raise ValueError(f"missing marker {needle}")
	start = text.rfind(opener, 0, marker)
	if start < 0:
		raise ValueError(f"missing enclosing block for {needle}")
	try:
		return extract_block_at(text, start)
	except ValueError as exc:
		raise ValueError(f"unterminated enclosing block for {needle}") from exc


def main() -> int:
	errors: list[str] = []
	matrix = MATRIX.read_text(encoding="utf-8-sig")
	edges = EDGE_MATRIX.read_text(encoding="utf-8-sig")
	scenario = read("common/scripted_effects/006_independence_wave_scenario_effects.txt")
	scenario_triggers = read("common/scripted_triggers/006_independence_wave_triggers.txt")
	scenario_event = read("events/006_independence_wave.txt")
	scenario_localisation = read("common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt")
	planner = read("common/scripted_effects/006_independence_wave_package_planner_effects.txt")
	shared = read("common/scripted_effects/chaosx_liberation_release_effects.txt")
	joint = read("common/scripted_effects/005_006_liberations_collision_effects.txt")
	collision_triggers = read("common/scripted_triggers/005_006_liberations_collision_triggers.txt")
	soviet_triggers = read("common/scripted_triggers/005_soviet_collapse_triggers.txt")
	soviet_effects = read("common/scripted_effects/005_soviet_collapse_effects.txt")
	region_triggers = read("common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt")
	dispatch = read("common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt")
	decisions = read("common/decisions/006_independence_wave_decisions.txt")
	categories = read("common/decisions/categories/006_independence_wave_categories.txt")
	try:
		scenario_summary = extract_script_block(scenario, "independence_wave_scenario_freeze_summary")
	except ValueError as exc:
		errors.append(str(exc))
		scenario_summary = ""

	# SCN-008 publication is a single receipt boundary. Keep this census
	# explicit so a future caller cannot accidentally publish a stale or failed
	# generation through a second setter or event dispatch.
	try:
		scenario_trigger = extract_script_block(scenario, "independence_wave_trigger_scenario")
		success_branch, success_end = extract_block_containing_with_end(
			scenario_trigger,
			"set_global_flag = independence_wave_scenario_committed",
			"\tif = {",
		)
		failure_start = scenario_trigger.find("\n\telse = {", success_end)
		if failure_start < 0:
			raise ValueError("missing failure branch after SCN-008 success branch")
		failure_branch = extract_block_at(scenario_trigger, failure_start + 1)[0]
	except ValueError as exc:
		errors.append(str(exc))
		scenario_trigger = ""
		success_branch = ""
		failure_branch = ""

	gameplay_sources: list[str] = []
	for source_root in (ROOT / "common", ROOT / "events"):
		for source_path in source_root.rglob("*.txt"):
			try:
				gameplay_sources.append(source_path.read_text(encoding="utf-8-sig"))
			except UnicodeDecodeError as exc:
				errors.append(f"could not decode gameplay source {source_path}: {exc}")
	gameplay = "\n".join(gameplay_sources)
	commit_setters = re.findall(
		r"(?m)^[ \t]*set_global_flag = independence_wave_scenario_committed[ \t]*$",
		gameplay,
	)
	ledger_setters = re.findall(
		r"(?m)^[ \t]*set_country_flag = independence_wave_scenario_ledger_visible[ \t]*$",
		gameplay,
	)
	result_pending_setters = re.findall(
		r"(?m)^[ \t]*set_global_flag = independence_wave_scenario_result_pending[ \t]*$",
		gameplay,
	)
	result_pending_clearers = re.findall(
		r"(?m)^[ \t]*clr_global_flag = independence_wave_scenario_result_pending[ \t]*$",
		gameplay,
	)
	scenario_result_dispatches = re.findall(
		r"(?m)^[ \t]*country_event = \{ id = chaosx\.triggerable_scenarios\.80\b[^}\r\n]*\}[ \t]*$",
		gameplay,
	)
	scenario_2_dispatches = re.findall(
		r"(?m)^[ \t]*country_event = \{ id = chaosx\.nr6\.2\b[^}\r\n]*\}[ \t]*$",
		scenario_trigger,
	)
	scenario_80_dispatches = re.findall(
		r"(?m)^[ \t]*country_event = \{ id = chaosx\.triggerable_scenarios\.80\b[^}\r\n]*\}[ \t]*$",
		scenario_trigger,
	)
	success_2 = success_branch.find("country_event = { id = chaosx.nr6.2")
	success_80 = success_branch.find("country_event = { id = chaosx.triggerable_scenarios.80")
	require(len(commit_setters) == 1, f"SCN-008 publication receipt has {len(commit_setters)} global setters; expected one", errors)
	require(len(ledger_setters) == 1, f"SCN-008 ledger visibility has {len(ledger_setters)} country setters; expected one", errors)
	require(len(result_pending_setters) == 1, f"SCN-008 queued result has {len(result_pending_setters)} pending setters; expected one", errors)
	require(len(result_pending_clearers) == 2, f"SCN-008 queued result has {len(result_pending_clearers)} pending clearers; expected report acknowledgement plus summary reset", errors)
	require(len(scenario_result_dispatches) == 1, f"SCN-008 result event has {len(scenario_result_dispatches)} dispatch call sites; expected one", errors)
	require(len(scenario_2_dispatches) == 1, f"SCN-008 Event 006 log has {len(scenario_2_dispatches)} dispatches in its trigger; expected one", errors)
	require(len(scenario_80_dispatches) == 1, f"SCN-008 result dispatch has {len(scenario_80_dispatches)} trigger-local call sites; expected one", errors)
	require(success_2 >= 0 and success_80 > success_2, "SCN-008 success branch does not dispatch chaosx.nr6.2 before triggerable_scenarios.80", errors)
	require(
		failure_branch
		and "clr_global_flag = independence_wave_scenario_committed" in failure_branch
		and "country_event = { id = chaosx.nr6.2" not in failure_branch
		and "country_event = { id = chaosx.triggerable_scenarios.80" not in failure_branch
		and "independence_wave_scenario_reset_summary = yes" in failure_branch,
		"SCN-008 failure/rollback branch can publish a result or leave the summary surface visible",
		errors,
	)
	try:
		result_event = extract_block_containing(
			scenario_event,
			"id = chaosx.triggerable_scenarios.80",
			"country_event = {",
		)
	except ValueError as exc:
		errors.append(str(exc))
		result_event = ""
	require(
		result_event
		and "has_global_flag = independence_wave_scenario_committed" in result_event
		and "has_global_flag = independence_wave_scenario_result_pending" in result_event
		and "NOT = { has_global_flag = independence_wave_scenario_failed }" in result_event
		and "NOT = { has_global_flag = independence_wave_scenario_finalization_failed }" in result_event
		and result_event.count("set_country_flag = independence_wave_scenario_ledger_visible") == 1,
		"SCN-008 result event does not require the current commit receipt before exposing the ledger",
		errors,
	)
	try:
		result_option = extract_block_containing(
			result_event,
			"name = chaosx.triggerable_scenarios.80.a",
			"option = {",
		)
		summary_reset = extract_script_block(scenario, "independence_wave_scenario_reset_summary")
		transaction_barrier = extract_script_block(scenario_triggers, "independence_wave_scenario_transaction_barrier_is_open")
		busy_status = extract_block_containing(
			scenario_localisation,
			"localization_key = chaosx.scenarios.launch_status.independence_wave.transaction_busy",
			"text = {",
		)
	except ValueError as exc:
		errors.append(str(exc))
		result_option = ""
		summary_reset = ""
		transaction_barrier = ""
		busy_status = ""
	require(
		result_option
		and "has_global_flag = independence_wave_scenario_result_pending" in result_option
		and result_option.find("set_country_flag = independence_wave_scenario_ledger_visible")
			< result_option.find("clr_global_flag = independence_wave_scenario_result_pending"),
		"SCN-008 report acknowledgement does not publish the ledger before releasing the result lock",
		errors,
	)
	require(
		"NOT = { has_global_flag = independence_wave_scenario_result_pending }" in transaction_barrier
		and "clr_global_flag = independence_wave_scenario_result_pending" in summary_reset,
		"SCN-008 launch barrier or summary reset does not manage the queued-result lock",
		errors,
	)
	require(
		"has_global_flag = independence_wave_scenario_result_pending" in busy_status,
		"SCN-008 launch status does not explain the queued-result transaction lock",
		errors,
	)
	publication_visibility = (
		"has_global_flag = independence_wave_scenario_committed",
		"NOT = { has_global_flag = independence_wave_scenario_failed }",
		"NOT = { has_global_flag = independence_wave_scenario_finalization_failed }",
		"has_country_flag = independence_wave_scenario_ledger_visible",
	)
	try:
		scenario_category = extract_script_block(categories, "independence_wave_scenario_ledger_category")
	except ValueError as exc:
		errors.append(str(exc))
		scenario_category = ""
	for needle in publication_visibility:
		require(needle in scenario_category, f"SCN-008 category is missing publication gate: {needle}", errors)
	for decision_name in (
		"independence_wave_scenario_ledger_previous",
		"independence_wave_scenario_ledger_next",
		"independence_wave_scenario_ledger_close",
	):
		try:
			control = extract_named_block(decisions, decision_name)
		except ValueError as exc:
			errors.append(str(exc))
			control = ""
		for needle in publication_visibility:
			require(needle in control, f"{decision_name} is missing publication gate: {needle}", errors)

	cell_ids = re.findall(r"`(SCN-008/[^`]+)`", matrix)
	require(len(cell_ids) == 32 and len(set(cell_ids)) == 32, f"expected 32 unique SCN-008 cells, found {len(set(cell_ids))}", errors)
	for label in (
		"Sovereign Scatter",
		"Common Congress",
		"Wars of Separation",
		"Universal Belligerence: former hosts",
		"Universal Belligerence: neighboring releases",
		"Universal Belligerence: nearby non-league",
		"Patron Worlds",
		"Great Partition",
	):
		require(label in matrix, f"32-cell receipt is missing {label}", errors)
	for intensity in ("low", "medium", "high", "maximum"):
		intensity_cells = [cell for cell in cell_ids if cell.rsplit("/", 1)[-1] == intensity]
		require(len(intensity_cells) == 8, f"32-cell receipt does not contain eight {intensity} cells", errors)

	edge_ids = re.findall(r"(?m)^\|\s*`(EDGE-SCN-\d{3})`", edges)
	require(len(edge_ids) == 8 and len(set(edge_ids)) == 8, f"expected eight unique SCN-008 edge cases, found {len(set(edge_ids))}", errors)
	for case_id in (f"EDGE-SCN-{index:03d}" for index in range(1, 9)):
		require(case_id in edges, f"edge receipt is missing {case_id}", errors)

	witnesses = {
		"zero-ready rejection ledger": "independence_wave_scenario_attempt_ranked_packages",
		"mixed readiness ranked registry": "independence_wave_scenario_rebuild_ranked_registry",
		"anchor collision": "is_liberation_release_current_reserved_state",
		"protected-host remnant": "is_liberation_release_host_protection_candidate",
		"optional trim rollback": "independence_wave_record_optional_state_trim",
		"Event 005 ordering": "soviet_collapse_joint_allocate_opening_republics = yes",
		"DON/DHC cross-event exclusion": "is_don_dhc_cross_event_collision_clear",
		"single shared lock": "liberation_release_lock_plan = yes",
		"repeat-launch barrier": "independence_wave_scenario_transaction_barrier_is_open",
		"repeat-launch reset": "independence_wave_scenario_reset_summary",
		"former-host uniqueness": "independence_wave_scenario_former_host_unique_policy",
		"former-host target ledger": "global.independence_wave_scenario_belligerence_targets",
		"neighboring-release target": "independence_wave_scenario_start_neighbor_release_war",
		"nearby non-league target": "independence_wave_scenario_start_nearby_nonleague_war",
		"summary released array": "global.independence_wave_scenario_released_package_ids",
		"summary blocked array": "global.independence_wave_scenario_blocked_package_ids",
		"summary rejection array": "global.independence_wave_scenario_blocked_reasons",
		"bounded ledger cursor": "independence_wave_scenario_ledger_index",
		"origin and attestation gate": "is_independence_wave_iw093_fixed_origin_preflight = yes",
	}
	for label, needle in witnesses.items():
		require(
			any(needle in source for source in (scenario, scenario_triggers, scenario_event, planner, shared, joint, collision_triggers, soviet_triggers, soviet_effects, region_triggers, dispatch, decisions)),
			f"missing static witness: {label} ({needle})",
			errors,
		)

	try:
		don_dhc_guard = extract_script_block(collision_triggers, "is_don_dhc_cross_event_collision_clear")
		dhc_creation_guard = extract_script_block(collision_triggers, "is_soviet_collapse_dhc_creation_clear")
		dhc_runtime_preflight = extract_script_block(collision_triggers, "is_iw039_dhc_runtime_preflight_clear")
		dhc_spawn_trigger = extract_script_block(soviet_triggers, "can_soviet_collapse_spawn_dhc")
		dhc_spawn_effect = extract_script_block(soviet_effects, "soviet_collapse_spawn_dhc_if_enabled")
		don_plan_trigger = extract_script_block(region_triggers, "can_plan_independence_wave_package_iw_039")
		package_runtime_preflight = extract_script_block(dispatch, "is_independence_wave_runtime_package_preflight_ready")
	except ValueError as exc:
		errors.append(str(exc))
		don_dhc_guard = ""
		dhc_creation_guard = ""
		dhc_runtime_preflight = ""
		dhc_spawn_trigger = ""
		dhc_spawn_effect = ""
		don_plan_trigger = ""
		package_runtime_preflight = ""
	require("DHC = { exists = no }" in don_dhc_guard, "DON/DHC exclusion does not reject an existing DHC", errors)
	require("has_country_flag = soviet_collapse_don_host_successor" in don_dhc_guard, "IW-039 candidate gate does not reject the DHC successor receipt", errors)
	for state_id in (218, 238):
		try:
			candidate_state = extract_named_block(don_dhc_guard, str(state_id))
		except ValueError as exc:
			errors.append(str(exc))
			candidate_state = ""
		require(
			"is_liberation_release_current_reserved_state = yes" in candidate_state
			and "liberation_plan_owner.soviet_collapse" in candidate_state,
			f"DON/DHC exclusion does not reject an Event 005 state-{state_id} reservation",
			errors,
		)
		require("is_owned_by = DHC" in candidate_state and "is_controlled_by = DHC" in candidate_state, f"IW-039 candidate gate does not check DHC ownership/control of state {state_id}", errors)
	require(
		"owner = { is_soviet_collapse_active_origin_country = yes }" in don_dhc_guard
		and "controller = { is_soviet_collapse_active_origin_country = yes }" in don_dhc_guard,
		"IW-039 candidate gate does not check active Event 005 ownership/control of the conflict states",
		errors,
	)
	require(
		"DHC = { exists = no }" in dhc_creation_guard
		and "has_country_flag = soviet_collapse_don_host_successor" in dhc_creation_guard,
		"Event 005 DHC creation guard does not reject an existing or previously tagged DHC",
		errors,
	)
	for marker in (
		"has_country_flag = liberation_release_reserved_country",
		"has_country_flag = independence_wave_pending_package",
		"has_country_flag = independence_wave_origin_prepared",
		"is_independence_wave_active_country = yes",
	):
		require(marker in dhc_creation_guard, f"Event 005 DHC creation guard does not protect pending/active DON marker {marker}", errors)
	require(
		"owner = { is_soviet_collapse_active_origin_country = yes }" not in dhc_creation_guard
		and "controller = { is_soviet_collapse_active_origin_country = yes }" not in dhc_creation_guard
		and "is_liberation_release_current_reserved_state = yes" not in dhc_creation_guard,
		"Event 005 DHC creation guard is blocked by the normal active SOV host owner",
		errors,
	)
	for marker in (
		"has_country_flag = liberation_release_reserved_country",
		"has_country_flag = independence_wave_pending_package",
		"has_country_flag = independence_wave_origin_prepared",
		"is_independence_wave_active_country = yes",
	):
		require(marker in don_dhc_guard, f"DON/DHC exclusion does not test pending/active DON marker {marker}", errors)
	require(
		"has_country_flag = independence_wave_origin_committed" not in don_dhc_guard,
		"DON/DHC exclusion can remain latched after Event 006 marks the origin ended",
		errors,
	)
	require(
		"is_soviet_collapse_dhc_creation_clear = yes" in dhc_spawn_trigger,
		"ordinary Event 005 DHC eligibility bypasses the shared collision guard",
		errors,
	)
	require(
		"is_don_dhc_cross_event_collision_clear = yes" in don_plan_trigger,
		"Event 006 IW-039 eligibility bypasses the shared DHC collision guard",
		errors,
	)
	force_all_position = dhc_spawn_effect.find("has_global_flag = soviet_collapse_force_all_chaos_successors")
	force_all_guard = dhc_spawn_effect.find("is_soviet_collapse_dhc_creation_clear = yes", force_all_position)
	require(
		force_all_position >= 0 and force_all_guard > force_all_position,
		"Event 005 force-all DHC path bypasses the shared DON collision guard",
		errors,
	)
	for state_id in (218, 238):
		try:
			preflight_state = extract_named_block(dhc_runtime_preflight, str(state_id))
		except ValueError as exc:
			errors.append(str(exc))
			preflight_state = ""
		require("is_owned_by = DHC" in preflight_state and "is_controlled_by = DHC" in preflight_state, f"IW-039 final preflight does not check DHC ownership/control of state {state_id}", errors)
		require(
			"owner = { is_soviet_collapse_active_origin_country = yes }" in preflight_state
			and "controller = { is_soviet_collapse_active_origin_country = yes }" in preflight_state,
			f"IW-039 final preflight does not reject active Event 005 ownership/control of state {state_id}",
			errors,
		)
	require("has_country_flag = soviet_collapse_don_host_successor" in dhc_runtime_preflight, "IW-039 final preflight misses the DHC successor receipt", errors)
	try:
		preflight_218 = extract_named_block(dhc_runtime_preflight, "218")
		preflight_238 = extract_named_block(dhc_runtime_preflight, "238")
	except ValueError as exc:
		errors.append(str(exc))
		preflight_218 = ""
		preflight_238 = ""
	require(
		"is_liberation_release_current_reserved_state = yes" in preflight_218
		and "liberation_plan_owner.soviet_collapse" in preflight_218
		and "liberation_release_package_id" in preflight_218
		and "independence_wave_package_id.iw_039" in preflight_218,
		"IW-039 final preflight permits an Event 005 reservation or an IW-039 reservation of excluded state 218",
		errors,
	)
	require(
		"is_liberation_release_current_reserved_state = yes" in preflight_238
		and "liberation_plan_owner.soviet_collapse" in preflight_238,
		"IW-039 final preflight does not distinguish Event 005 state-238 reservations from trim-eligible compact reservations",
		errors,
	)
	require(
		"check_variable = { var = liberation_release_package_id value = constant:independence_wave_package_id.iw_039 compare = equals }" in dhc_runtime_preflight,
		"IW-039 final preflight does not distinguish its optional 238 reservation from Event 005 reservations",
		errors,
	)
	require(
		"is_iw039_dhc_runtime_preflight_clear = yes" in package_runtime_preflight
		and "independence_wave_execution_package_id = constant:independence_wave_package_id.iw_039" in package_runtime_preflight,
		"Event 006 final package preflight does not run the IW-039 DHC collision proof",
		errors,
	)
	edge_005_rows = [line for line in edges.splitlines() if "EDGE-SCN-005" in line]
	require(
		len(edge_005_rows) == 1
		and "both event orders" in edge_005_rows[0]
		and "force-all DHC creation" in edge_005_rows[0],
		"current EDGE-SCN-005 does not document both-order normal and force-all DHC exclusion",
		errors,
	)
	committed_gate = scenario_summary.find("has_global_flag = independence_wave_scenario_committed")
	released_append = scenario_summary.find(
		"add_to_array = { array = global.independence_wave_scenario_released_package_ids"
	)
	require(
		committed_gate >= 0 and released_append > committed_gate,
		"failed SCN-008 summary can publish selected rows as released without the committed flag",
		errors,
	)
	require(
		"add_to_array = { array = global.independence_wave_scenario_blocked_package_ids value = independence_wave_scenario_summary_package_id }" in scenario_summary
		and "add_to_array = { array = global.independence_wave_scenario_blocked_reasons value = global.independence_wave_scenario_last_failure }" in scenario_summary,
		"failed SCN-008 summary does not retain selected rows and failure reason in blocked arrays",
		errors,
	)
	failure_match = re.search(r"(?m)^\telse = \{\n\t\t# A plan that failed", scenario_summary)
	failure_summary = scenario_summary[failure_match.start() :] if failure_match else ""
	selected_ids = failure_summary.find("array = global.independence_wave_plan_selected_package_ids")
	rejected_ids = failure_summary.find("array = global.liberation_plan_rejected_package_ids")
	selected_rows = failure_summary.find("array = global.independence_wave_plan_country_row_indices")
	selected_country_scope = failure_summary.find("var:global.liberation_plan_countries^independence_wave_scenario_summary_country_row")
	selected_failure_reason = failure_summary.rfind("global.independence_wave_scenario_last_failure")
	require(
		rejected_ids >= 0 and selected_ids > rejected_ids and selected_rows > selected_ids and selected_country_scope > selected_rows and selected_failure_reason > selected_country_scope,
		"failed SCN-008 summary does not preserve rejected-prefix then selected country/reason array alignment",
		errors,
	)

	# Target selection must clear marks both before target selection and after the
	# rule-specific dispatch. This is the source-level repeated-launch guarantee.
	require(
		scenario.count("independence_wave_scenario_clear_belligerence_target_marks = yes") == 3,
		"belligerence target marks are not cleared at reset, dispatch boundary, and completion",
		errors,
	)
	require(
		"independence_wave_scenario_freeze_summary = yes" in scenario
		and "independence_wave_scenario_append_unbound_registry_rows = yes" in scenario,
		"scenario summary does not freeze released/blocked rows with the unbound registry projection",
		errors,
	)

	rows = [
		{"id": case_id, "source_receipt": "006_event6_scn008_edge_case_source_matrix_current_2026-09-25.md"}
		for case_id in edge_ids
	]
	if errors:
		print("SCN-008 scenario matrix audit FAILED")
		for error in errors:
			print(f"- {error}")
		return 1
	print("SCN-008 scenario matrix audit passed")
	publication_census = {
		"commit_setter_count": len(commit_setters),
		"ledger_visible_setter_count": len(ledger_setters),
		"result_pending_setter_count": len(result_pending_setters),
		"result_pending_clearer_count": len(result_pending_clearers),
		"scenario_result_dispatch_count": len(scenario_result_dispatches),
		"scenario_log_dispatch_count": len(scenario_2_dispatches),
		"scenario_result_dispatch_order": "chaosx.nr6.2 -> chaosx.triggerable_scenarios.80",
		"failed_branch_log_dispatch_count": failure_branch.count("country_event = { id = chaosx.nr6.2"),
		"failed_branch_result_dispatch_count": failure_branch.count("country_event = { id = chaosx.triggerable_scenarios.80"),
	}
	print(json.dumps({"cells": sorted(set(cell_ids)), "edge_cases": rows, "publication": publication_census}, ensure_ascii=False))
	return 0


if __name__ == "__main__":
	sys.exit(main())
