#!/usr/bin/env python3
"""Audit the Event 006 anchor-first frozen-plan contract.

This is a mechanical source audit. It does not simulate HOI4, package readiness,
or live map ownership; those remain separate gameplay and scenario tests.
"""

from __future__ import annotations

import re
import sys
import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLISHER_GLOB = "006_independence_wave_packages_region_*_effects.txt"
OVERLAY_ONLY_IDS = {5, 22, 25, 35, 59, 85, 101, 102, 105, 156, 196, 197, 204}


def read(relative: str) -> str:
	return (ROOT / relative).read_text(encoding="utf-8-sig")


def strip_comments(text: str) -> str:
	return re.sub(r"#.*", "", text)


def brace_problem(text: str) -> str | None:
	stack: list[int] = []
	quoted = False
	escaped = False
	comment = False
	line = 1
	for char in text:
		if char == "\n":
			line += 1
			comment = False
			continue
		if comment:
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
			stack.append(line)
		elif char == "}":
			if not stack:
				return f"extra closing brace at line {line}"
			stack.pop()
	if quoted:
		return "unterminated quoted string"
	if stack:
		return f"unclosed brace opened at line {stack[-1]}"
	return None


def extract_named_blocks(text: str, prefix: str) -> dict[int, str]:
	pattern = re.compile(rf"(?m)^{re.escape(prefix)}(\d{{3}})\s*=\s*\{{")
	blocks: dict[int, str] = {}
	for match in pattern.finditer(text):
		package_id = int(match.group(1))
		depth = 0
		quoted = False
		escaped = False
		comment = False
		end = None
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
					end = index + 1
					break
		if end is None:
			raise ValueError(f"unterminated publisher IW{package_id:03d}")
		if package_id in blocks:
			raise ValueError(f"duplicate publisher IW{package_id:03d}")
		blocks[package_id] = text[match.start() : end]
	return blocks


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


def require(condition: bool, message: str, errors: list[str]) -> None:
	if not condition:
		errors.append(message)


def require_order(text: str, labels: list[tuple[str, str]], context: str, errors: list[str]) -> None:
	positions: list[int] = []
	for label, needle in labels:
		position = text.find(needle)
		if position < 0:
			errors.append(f"{context}: missing {label} ({needle})")
			return
		positions.append(position)
	if positions != sorted(positions):
		errors.append(f"{context}: wrong order: " + " -> ".join(label for label, _ in labels))


def main() -> int:
	errors: list[str] = []
	for relative in (
		"common/script_constants/006_independence_wave_package_constants.txt",
		"common/scripted_effects/005_006_liberations_collision_effects.txt",
		"common/scripted_effects/006_independence_wave_execution_effects.txt",
		"common/scripted_effects/006_independence_wave_package_planner_effects.txt",
		"common/scripted_effects/006_independence_wave_scenario_effects.txt",
		"common/scripted_effects/chaosx_liberation_release_effects.txt",
	):
		problem = brace_problem(read(relative))
		require(problem is None, f"{relative}: {problem}", errors)
	for path in sorted((ROOT / "common/scripted_effects").glob(PUBLISHER_GLOB)):
		problem = brace_problem(path.read_text(encoding="utf-8-sig"))
		require(problem is None, f"{path.relative_to(ROOT)}: {problem}", errors)

	constants = strip_comments(read("common/script_constants/006_independence_wave_constants.txt"))
	for key, expected in {
		"calm_world": 3,
		"gathering_storm": 4,
		"rising_chaos": 5,
		"chaos_tier": 7,
		"totalen_chaos": 10,
		"world_collapse": 10,
	}.items():
		require(
			bool(re.search(rf"(?m)^\s*{key}\s*=\s*{expected}\s*$", constants)),
			f"wave count {key} is not {expected}",
			errors,
		)

	planner_constants = strip_comments(read("common/script_constants/006_independence_wave_package_constants.txt"))
	for phase, expected in {"anchors": 1, "compact": 2, "extended": 3}.items():
		require(
			bool(re.search(rf"(?m)^\s*{phase}\s*=\s*{expected}\s*$", planner_constants)),
			f"reservation phase {phase} is not {expected}",
			errors,
		)

	publishers: dict[int, str] = {}
	for path in sorted((ROOT / "common/scripted_effects").glob(PUBLISHER_GLOB)):
		try:
			blocks = extract_named_blocks(path.read_text(encoding="utf-8-sig"), "independence_wave_reserve_package_iw_")
		except ValueError as exc:
			errors.append(f"{path.name}: {exc}")
			continue
		for package_id, block in blocks.items():
			if package_id in publishers:
				errors.append(f"IW{package_id:03d} has more than one publisher")
			publishers[package_id] = block

	require(len(publishers) == 149, f"expected 149 package publishers, found {len(publishers)}", errors)
	for package_id, block in sorted(publishers.items()):
		for token, expected in {
			"independence_wave_begin_package_reservation = yes": 1,
			"independence_wave_reserve_candidate_anchor = yes": 1,
			"independence_wave_finish_package_reservation = yes": 1,
		}.items():
			actual = block.count(token)
			require(actual == expected, f"IW{package_id:03d}: {token!r} occurs {actual} times", errors)

	binding_path = ROOT / "docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv"
	with binding_path.open(encoding="utf-8-sig", newline="") as handle:
		binding_rows = list(csv.DictReader(handle))

	# The accepted v10 closure keeps the RHI/AJX reservation group intact and
	# requires one distinct grounded package before the ten-country band can
	# open. Keep that disposition source-audited so a tempting map rebind cannot
	# silently manufacture capacity.
	dispatch = read("common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt")
	attestation = extract_script_block(
		dispatch,
		"has_independence_wave_runtime_package_content_attestation_for_execution_id",
	)
	attested_ids = sorted(
		{
			int(value)
			for value in re.findall(
				r"constant:independence_wave_package_id\.iw_(\d{3})", attestation
			)
		}
	)
	expected_attested_ids = {1, 4, 6, 7, 8, 9, 10, 17, 19, 184}
	require(
		set(attested_ids) == expected_attested_ids,
		"content-attestation set changed without updating the accepted Event 006 closure: "
		+ f"expected={sorted(expected_attested_ids)} found={attested_ids}",
		errors,
	)
	loaders: dict[int, str] = {}
	for path in sorted((ROOT / "common/scripted_effects").glob(PUBLISHER_GLOB)):
		try:
			blocks = extract_named_blocks(path.read_text(encoding="utf-8-sig"), "independence_wave_load_package_iw_")
		except ValueError as exc:
			errors.append(f"{path.name}: {exc}")
			continue
		for package_id, block in blocks.items():
			if package_id in loaders:
				errors.append(f"IW{package_id:03d} has more than one package loader")
			loaders[package_id] = block
	attested_groups: dict[int, str] = {}
	attested_anchors: dict[int, int] = {}
	for package_id in attested_ids:
		block = loaders.get(package_id)
		require(block is not None, f"IW{package_id:03d} is attested but has no package loader", errors)
		if block is None:
			continue
		group_match = re.search(
			r"independence_wave_candidate_reservation_group\s*=\s*constant:"
			r"independence_wave_reservation_group_id\.([a-z0-9_]+)",
			block,
		)
		anchor_match = re.search(
			r"(?ms)^\s*(\d+)\s*=\s*\{.*?save_event_target_as\s*=\s*liberation_candidate_anchor",
			block,
		)
		require(group_match is not None, f"IW{package_id:03d} loader has no reservation group", errors)
		require(anchor_match is not None, f"IW{package_id:03d} loader has no anchor", errors)
		if group_match:
			attested_groups[package_id] = group_match.group(1)
		if anchor_match:
			attested_anchors[package_id] = int(anchor_match.group(1))
	if len(attested_groups) == len(expected_attested_ids):
		require(
		len(set(attested_groups.values())) == 9,
		"accepted ten-package closure no longer exposes exactly nine compatible reservation groups: "
		+ repr(attested_groups),
		errors,
		)
		require(
		attested_groups.get(8) == "rg_rhine_saar" and attested_groups.get(10) == "rg_rhine_saar",
		"accepted RHI/AJX shared RG-RHINE-SAAR disposition changed without a new closure: "
		+ repr({8: attested_groups.get(8), 10: attested_groups.get(10)}),
		errors,
		)
		require(
		len(set(attested_anchors.values())) == 10,
		"attested package anchors are not pairwise unique: " + repr(attested_anchors),
		errors,
	)
	expected_automatic_ids = {
		int(row["package_id"].split("-")[1])
		for row in binding_rows
		if row["readiness_verdict"]
		in {
			"ready_automatic",
			"ready_high_chaos",
			"ready_if_tag_not_living",
			"ready_unique_state_confirmed",
		}
	}
	automatic_ids: set[int] = set()
	for path in sorted((ROOT / "common/scripted_effects").glob(PUBLISHER_GLOB)):
		text = path.read_text(encoding="utf-8-sig")
		automatic_ids.update(
			int(value)
			for value in re.findall(
				r"independence_wave_weight_iw_(\d{3})\s*=\s*\{\s*independence_wave_reserve_package_iw_\1\s*=\s*yes\s*\}",
				text,
			)
		)
	require(
		automatic_ids == expected_automatic_ids,
		"automatic selector set differs from the 126 bound automatic/high-chaos rows: "
		+ f"missing={sorted(expected_automatic_ids - automatic_ids)} extra={sorted(automatic_ids - expected_automatic_ids)}",
		errors,
	)
	require(not (automatic_ids & OVERLAY_ONLY_IDS), f"automatic selectors contain overlay-only packages {sorted(automatic_ids & OVERLAY_ONLY_IDS)}", errors)

	planner = read("common/scripted_effects/006_independence_wave_package_planner_effects.txt")
	require_order(
		planner,
		[
			("compact phase", "independence_wave_reservation_phase.compact"),
			("extended phase", "independence_wave_reservation_phase.extended"),
		],
		"Event 006 optional expansion",
		errors,
	)
	for helper, phase in {
		"independence_wave_reserve_candidate_anchor": "anchors",
		"independence_wave_try_candidate_compact_state": "compact",
		"independence_wave_try_candidate_extended_state": "extended",
	}.items():
		match = re.search(rf"(?ms)^{helper}\s*=\s*\{{(.*?)(?=^[a-z0-9_]+\s*=\s*\{{)", planner)
		require(match is not None, f"missing helper {helper}", errors)
		if match:
			require(
				f"constant:independence_wave_reservation_phase.{phase}" in match.group(1),
				f"{helper} is not gated to {phase}",
				errors,
			)

	execution = read("common/scripted_effects/006_independence_wave_execution_effects.txt")
	require_order(
		execution,
		[
			("automatic anchor allocation", "independence_wave_allocate_automatic_packages = yes"),
			("automatic optional expansion", "independence_wave_expand_selected_optional_territory = yes"),
			("automatic frozen execution", "independence_wave_execute_standalone_frozen_plan = yes"),
		],
		"standalone flow",
		errors,
	)
	require("set_capital = event_target:" not in execution, "Event 006 uses undocumented set_capital shorthand", errors)
	for needle in (
		"is_owned_by = event_target:independence_wave_execution_state_target",
		"is_controlled_by = event_target:independence_wave_execution_state_target",
		"independence_wave_execution_transfer_failure = constant:liberation_plan_reject_reason.unsafe_instantiation",
	):
		require(needle in execution, f"Event 006 transfer verification is missing {needle}", errors)

	scenario = read("common/scripted_effects/006_independence_wave_scenario_effects.txt")
	require_order(
		scenario,
		[
			("scenario ranked anchor attempts", "independence_wave_scenario_attempt_ranked_packages = yes"),
			("scenario optional expansion", "independence_wave_expand_selected_optional_territory = yes"),
			("scenario exact selected count", "global.independence_wave_plan_target_count = global.independence_wave_plan_selected_count"),
		],
		"SCN-008 flow",
		errors,
	)
	ranked_ids = {
		int(value)
		for value in re.findall(
			r"independence_wave_scenario_ranked_package_ids\s+value\s*=\s*constant:independence_wave_package_id\.iw_(\d{3})",
			scenario,
		)
	}
	require(len(ranked_ids) == 138, f"SCN-008 expected 138 distinct ranked packages, found {len(ranked_ids)}", errors)
	require(not (ranked_ids & OVERLAY_ONLY_IDS), f"SCN-008 contains overlay-only packages {sorted(ranked_ids & OVERLAY_ONLY_IDS)}", errors)
	require(
		scenario.count("independence_wave_scenario_clear_belligerence_target_marks = yes") == 3,
		"SCN-008 belligerence target marks are not cleared on reset and around target selection",
		errors,
	)
	require(
		"global.independence_wave_scenario_belligerence_targets" in scenario,
		"SCN-008 does not keep a bounded belligerence-target cleanup ledger",
		errors,
	)
	try:
		intensity_tuning = extract_script_block(scenario, "independence_wave_scenario_set_intensity_tuning")
		type_application = extract_script_block(scenario, "independence_wave_scenario_apply_type")
		ranked_attempts = extract_script_block(scenario, "independence_wave_scenario_attempt_ranked_packages")
	except ValueError as exc:
		errors.append(str(exc))
		intensity_tuning = ""
		type_application = ""
		ranked_attempts = ""

	for label, territory, force in (
		("low", "anchor", "fragile"),
		("medium", "compact", "viable"),
		("high", "extended", "armed"),
		("maximum", "extended", "high_chaos"),
	):
		require(
			f"constant:liberation_territory_level.{territory}" in intensity_tuning
			and f"constant:liberation_force_level.{force}" in intensity_tuning,
			f"SCN-008 {label} intensity is missing territory={territory} force={force}",
			errors,
		)
	require(
		"constant:independence_wave_scenario_registry.bound_package_count" in intensity_tuning,
		"SCN-008 intensity tuning does not keep the all-bound-package target count",
		errors,
	)
	require(
		"independence_wave_scenario_last_intensity" not in ranked_attempts,
		"SCN-008 ranked candidate attempts vary by intensity",
		errors,
	)
	for scenario_type, required_effect in {
		"common_congress": "independence_wave_scenario_form_common_congress = yes",
		"wars_of_separation": "independence_wave_scenario_start_all_host_wars = yes",
		"universal_belligerence": "independence_wave_scenario_start_universal_belligerence = yes",
		"patron_worlds": "independence_wave_scenario_assign_patrons = yes",
	}.items():
		require(
			f"constant:independence_wave_scenario_type.{scenario_type}" in type_application
			and required_effect in type_application,
			f"SCN-008 type {scenario_type} is missing {required_effect}",
			errors,
		)
	for scenario_type in ("sovereign_scatter", "great_partition"):
		require(
			f"constant:independence_wave_scenario_type.{scenario_type}" in scenario,
			f"SCN-008 type {scenario_type} is not registered in scenario behavior",
			errors,
		)
	require(
		"constant:independence_wave_scenario_type.great_partition" in intensity_tuning,
		"SCN-008 Great Partition does not alter pre-reservation partition setup",
		errors,
	)

	joint = read("common/scripted_effects/005_006_liberations_collision_effects.txt")
	require_order(
		joint,
		[
			("Event 005 anchors", "soviet_collapse_joint_allocate_opening_republics = yes"),
			("Event 006 anchors", "independence_wave_allocate_automatic_packages = yes"),
			("Event 005 compact pass", "soviet_collapse_joint_expand_selected_compact_territory = yes"),
			("Event 006 optional passes", "independence_wave_expand_selected_optional_territory = yes"),
			("shared lock", "liberation_release_lock_plan = yes"),
		],
		"joint Event 005/Event 006 flow",
		errors,
	)
	require("set_capital = event_target:" not in joint, "joint Event 005 uses undocumented set_capital shorthand", errors)
	for needle in (
		"is_owned_by = event_target:soviet_collapse_joint_execution_state_target",
		"is_controlled_by = event_target:soviet_collapse_joint_execution_state_target",
		"soviet_collapse_joint_execution_transfer_failure = constant:liberation_plan_reject_reason.unsafe_instantiation",
	):
		require(needle in joint, f"joint Event 005 transfer verification is missing {needle}", errors)

	shared = read("common/scripted_effects/chaosx_liberation_release_effects.txt")
	require("random_owned_state" not in shared, "host-survival selection still contains random_owned_state", errors)
	for needle in (
		"capital_scope =",
		"is_core_of = PREV",
		"is_controlled_by = PREV",
		"liberation_release_select_first_host_state_candidate = yes",
	):
		require(needle in shared, f"host-survival priority is missing {needle}", errors)

	if errors:
		print("Event 006 allocator audit FAILED")
		for error in errors:
			print(f"- {error}")
		return 1

	print("Event 006 allocator audit passed")
	print(f"- publishers: {len(publishers)}")
	print(f"- automatic/high-chaos selectable packages: {len(automatic_ids)}")
	print(f"- SCN-008 ranked selectable packages: {len(ranked_ids)}")
	print(f"- attested packages: {len(attested_ids)}; compatible reservation groups: {len(set(attested_groups.values()))}")
	print("- automatic counts: 3 / 4 / 5 / 7 / 10 (World Collapse 10)")
	print("- scenario intensities: low anchor/fragile; medium compact/viable; high extended/armed; maximum extended/high-chaos")
	print("- scenario types: scatter; congress; host wars; universal belligerence; patrons; partition")
	print("- order: all anchors -> compact -> extended -> lock")
	print("- joint order: Event 005 anchors -> Event 006 anchors -> optional territory -> lock")
	return 0


if __name__ == "__main__":
	sys.exit(main())
