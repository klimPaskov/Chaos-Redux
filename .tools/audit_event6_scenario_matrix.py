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
EDGE_MATRIX = ROOT / "docs/plans/006_independence_wave_plans/subagent_handoffs/006_scn008_edge_case_static_matrix_2026_08_02.md"


def read(relative: str) -> str:
	return (ROOT / relative).read_text(encoding="utf-8-sig")


def require(condition: bool, message: str, errors: list[str]) -> None:
	if not condition:
		errors.append(message)


def extract_script_block(text: str, name: str) -> str:
	match = re.search(rf"(?m)^{re.escape(name)}\s*=\s*\{{", text)
	if match is None:
		raise ValueError(f"missing scripted block {name}")
	depth = 0
	quoted = False
	escaped = False
	comment = False
	for index in range(match.end() - 1, len(text)):
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
				return text[match.start() : index + 1]
	raise ValueError(f"unterminated scripted block {name}")


def main() -> int:
	errors: list[str] = []
	matrix = MATRIX.read_text(encoding="utf-8-sig")
	edges = EDGE_MATRIX.read_text(encoding="utf-8-sig")
	scenario = read("common/scripted_effects/006_independence_wave_scenario_effects.txt")
	scenario_triggers = read("common/scripted_triggers/006_independence_wave_scenario_triggers.txt")
	scenario_event = read("events/006_independence_wave_scenario.txt")
	planner = read("common/scripted_effects/006_independence_wave_package_planner_effects.txt")
	shared = read("common/scripted_effects/chaosx_liberation_release_effects.txt")
	joint = read("common/scripted_effects/005_006_liberations_collision_effects.txt")
	dispatch = read("common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt")
	decisions = read("common/decisions/006_independence_wave_scenario_decisions.txt")
	try:
		scenario_summary = extract_script_block(scenario, "independence_wave_scenario_freeze_summary")
	except ValueError as exc:
		errors.append(str(exc))
		scenario_summary = ""

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

	edge_ids = re.findall(r"`(EDGE-SCN-\d{3})`", edges)
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
			any(needle in source for source in (scenario, scenario_triggers, scenario_event, planner, shared, joint, dispatch, decisions)),
			f"missing static witness: {label} ({needle})",
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
		{"id": case_id, "source_receipt": "006_scn008_edge_case_static_matrix_2026_08_02.md"}
		for case_id in edge_ids
	]
	if errors:
		print("SCN-008 scenario matrix audit FAILED")
		for error in errors:
			print(f"- {error}")
		return 1
	print("SCN-008 scenario matrix audit passed")
	print(json.dumps({"cells": sorted(set(cell_ids)), "edge_cases": rows}, ensure_ascii=False))
	return 0


if __name__ == "__main__":
	sys.exit(main())
