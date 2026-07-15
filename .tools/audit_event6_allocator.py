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
	print("- automatic counts: 3 / 4 / 5 / 7 / 10 (World Collapse 10)")
	print("- order: all anchors -> compact -> extended -> lock")
	print("- joint order: Event 005 anchors -> Event 006 anchors -> optional territory -> lock")
	return 0


if __name__ == "__main__":
	sys.exit(main())
