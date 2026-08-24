#!/usr/bin/env python3
"""Audit the Event 006 anchor-first frozen-plan contract.

This is a mechanical source audit. It does not simulate HOI4 or live map
ownership; the static twenty-package witness checks only the current source
bindings, attestation gate, and vanilla history needed for that witness.
"""

from __future__ import annotations

import re
import sys
import csv
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLISHER_GLOB = "006_independence_wave_package_region_effects_registry.txt"
OVERLAY_ONLY_IDS = {5, 22, 25, 35, 59, 85, 101, 102, 105, 156, 196, 197, 204}
STATIC_20_WITNESS_IDS = {
	1,
	2,
	4,
	6,
	7,
	8,
	9,
	10,
	14,
	17,
	18,
	19,
	23,
	33,
	41,
	70,
	71,
	72,
	173,
	184,
}


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


def parse_state_ids(raw: str) -> set[int]:
	return {int(value) for value in re.findall(r"\d+", raw or "")}


def parse_state_owner_map(raw: str) -> dict[int, str]:
	return {
		int(state_id): owner
		for state_id, owner in re.findall(r"(\d+)\s*=\s*([A-Z0-9_]+)", raw or "")
	}


def parse_capital_map(raw: str) -> dict[str, int]:
	return {
		owner: int(state_id)
		for owner, state_id in re.findall(r"([A-Z0-9_]+)\s*=\s*(\d+)", raw or "")
	}


def load_vanilla_owned_states(errors: list[str]) -> dict[str, set[int]]:
	vanilla_root = Path(
		os.environ.get(
			"HOI4_ROOT",
			r"C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV",
		)
	)
	state_root = vanilla_root / "history" / "states"
	if not state_root.is_dir():
		errors.append(
			"20-country static witness requires the installed vanilla history/states root: "
			+ str(state_root)
		)
		return {}
	owned: dict[str, set[int]] = {}
	for path in state_root.glob("*.txt"):
		match = re.match(r"^(\d+)", path.stem)
		if match is None:
			continue
		state_id = int(match.group(1))
		text = path.read_text(encoding="utf-8-sig", errors="ignore")
		owner_match = re.search(r"(?m)^\s*owner\s*=\s*([A-Z0-9_]+)", text)
		if owner_match is not None:
			owned.setdefault(owner_match.group(1), set()).add(state_id)
	return owned


def validate_static_20_witness(
	binding_rows: list[dict[str, str]],
	installed_reservation_rows: list[dict[str, str]],
	attested_ids: list[int],
	loaders: dict[int, str],
	dispatch: str,
	errors: list[str],
) -> dict[str, int]:
	"""Validate one source-backed twenty-package standalone allocation.

	This is deliberately a static acceptance witness, not a live-game
	simulation. It proves that the currently admitted packages can be frozen
	together from the installed bindings while retaining at least one vanilla
	state for every former host and preserving the capital-preference rule.
	"""
	binding_by_id = {
		int(row["package_id"].split("-")[1]): row
		for row in binding_rows
		if row.get("package_id")
	}
	reservation_by_group = {
		row["reservation_group"]: row
		for row in installed_reservation_rows
		if row.get("reservation_group")
	}
	allowed_readiness = {
		"ready_automatic",
		"ready_high_chaos",
		"ready_if_tag_not_living",
		"ready_unique_state_confirmed",
	}
	owned_states = load_vanilla_owned_states(errors)
	selected_group_counts: dict[str, int] = {}
	selected_footprints: dict[str, set[int]] = {}
	selected_anchors: set[int] = set()
	selected_states: set[int] = set()
	selected_tags: set[str] = set()
	for package_id in sorted(STATIC_20_WITNESS_IDS):
		row = binding_by_id.get(package_id)
		require(row is not None, f"IW{package_id:03d} static witness row is missing", errors)
		if row is None:
			continue
		require(
			package_id in attested_ids,
			f"IW{package_id:03d} static witness is not content-attested",
			errors,
		)
		require(
			package_id in loaders,
			f"IW{package_id:03d} static witness has no package loader",
			errors,
		)
		require(
			row["readiness_verdict"] in allowed_readiness,
			f"IW{package_id:03d} static witness has non-admitted readiness {row['readiness_verdict']!r}",
			errors,
		)
		require(
			not row["missing_current_state_ids"].strip(),
			f"IW{package_id:03d} static witness still has missing current state ids",
			errors,
		)
		anchor_ids = parse_state_ids(row["anchor_state_ids"])
		require(
			len(anchor_ids) == 1,
			f"IW{package_id:03d} static witness must have exactly one anchor",
			errors,
		)
		if len(anchor_ids) != 1:
			continue
		anchor = next(iter(anchor_ids))
		require(anchor not in selected_anchors, f"static witness anchor {anchor} is reused", errors)
		selected_anchors.add(anchor)
		tag = row["resolved_tag"]
		require(tag and tag not in selected_tags, f"static witness tag {tag!r} is reused", errors)
		selected_tags.add(tag)
		group = row["reservation_group"]
		selected_group_counts[group] = selected_group_counts.get(group, 0) + 1
		reservation = reservation_by_group.get(group)
		require(reservation is not None, f"IW{package_id:03d} static witness group {group!r} is missing", errors)
		if reservation is not None:
			require(
				selected_group_counts[group] <= int(reservation["maximum_automatic_packages_per_wave"]),
				f"static witness exceeds {group} capacity",
				errors,
			)
		owner_map = parse_state_owner_map(row["initial_owner_by_state"])
		host = owner_map.get(anchor)
		require(host is not None, f"IW{package_id:03d} static witness anchor has no former host", errors)
		if host is None:
			continue
		compact_states = parse_state_ids(row["compact_state_ids"])
		require(anchor in compact_states, f"IW{package_id:03d} compact footprint omits its anchor", errors)
		require(
			not (compact_states & selected_states),
			f"IW{package_id:03d} compact footprint overlaps an earlier witness footprint",
			errors,
		)
		selected_states.update(compact_states)
		for state_id in compact_states:
			require(
				owner_map.get(state_id) == host,
				f"IW{package_id:03d} compact state {state_id} is not owned by former host {host}",
				errors,
			)
		selected_footprints.setdefault(host, set()).update(compact_states)
		require(
			f"constant:independence_wave_package_id.iw_{package_id:03d}" in dispatch,
			f"IW{package_id:03d} static witness is not present in the package dispatch surface",
			errors,
		)
		require(
			f"is_independence_wave_exact_package_iw_{package_id:03d}_tag_available = yes" in dispatch,
			f"IW{package_id:03d} static witness has no exact tag-availability guard",
			errors,
		)

	protected_states: dict[str, int] = {}
	for host, footprint in sorted(selected_footprints.items()):
		vanilla_owned = owned_states.get(host, set())
		require(vanilla_owned, f"static witness former host {host} is absent from vanilla history", errors)
		require(
			footprint <= vanilla_owned,
			f"static witness footprint for {host} contains non-host vanilla states",
			errors,
		)
		remaining = vanilla_owned - footprint
		require(remaining, f"static witness would erase former host {host}", errors)
		capital_candidates = [
			int(state_id)
			for row in binding_rows
			if host in parse_capital_map(row.get("initial_owner_capitals", ""))
			for state_id in [parse_capital_map(row["initial_owner_capitals"])[host]]
		]
		capital = capital_candidates[0] if capital_candidates else None
		protected = capital if capital in remaining else min(remaining)
		protected_states[host] = protected
		require(
			capital is not None,
			f"static witness former host {host} has no documented capital",
			errors,
		)
		if capital is not None and capital in remaining:
			require(
				protected == capital,
				f"static witness did not prefer surviving capital {capital} for {host}",
				errors,
			)
	require(len(selected_anchors) == 20, f"static witness contains {len(selected_anchors)} anchors instead of 20", errors)
	require(len(selected_tags) == 20, f"static witness contains {len(selected_tags)} tags instead of 20", errors)
	return protected_states


def main() -> int:
	errors: list[str] = []
	for relative in (
		"common/script_constants/006_independence_wave_constants_registry.txt",
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

	constants = strip_comments(read("common/script_constants/006_independence_wave_constants_registry.txt"))
	for key, expected in {
		"calm_world": 3,
		"gathering_storm": 4,
		"rising_chaos": 5,
		"chaos_tier": 7,
		"totalen_chaos": 10,
		"world_collapse": 10,
	}.items():
		require(
			bool(re.search(rf"(?m)^\s*{key}\s*=\s*{expected}\s*$", constants))
			or bool(re.search(rf"(?ms)^\s*independence_wave_count\s*=\s*\{{.*?^\s*{key}\s*=\s*{expected}\s*$", constants)),
			f"wave count {key} is not {expected}",
			errors,
		)

	planner_constants = strip_comments(read("common/script_constants/006_independence_wave_constants_registry.txt"))
	for phase, expected in {"anchors": 1, "compact": 2, "extended": 3}.items():
		require(
			bool(re.search(rf"(?ms)^\s*independence_wave_reservation_phase\s*=\s*\{{.*?^\s*{phase}\s*=\s*{expected}\s*$", planner_constants)),
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
	matrix_path = ROOT / "docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv"
	with matrix_path.open(encoding="utf-8-sig", newline="") as handle:
		reservation_rows = list(csv.DictReader(handle))
	rhine_rows = [row for row in reservation_rows if row["reservation_group"] == "RG-RHINE-SAAR"]
	require(
		len(rhine_rows) == 1
		and rhine_rows[0]["maximum_automatic_packages_per_wave"] == "2"
		and rhine_rows[0]["package_ids"] == "IW-008 | IW-010"
		and rhine_rows[0]["baseline_state_ids"] == "51 | 42",
		"canonical RG-RHINE-SAAR matrix row must document the exact two-package 51/42 exception",
		errors,
	)
	installed_matrix_path = ROOT / "docs/plans/006_independence_wave_plans/package_bindings/006_current_map_reservation_groups.csv"
	with installed_matrix_path.open(encoding="utf-8-sig", newline="") as handle:
		installed_reservation_rows = list(csv.DictReader(handle))
	installed_rhine_rows = [row for row in installed_reservation_rows if row["reservation_group"] == "RG-RHINE-SAAR"]
	require(
		len(installed_rhine_rows) == 1
		and installed_rhine_rows[0]["maximum_automatic_packages_per_wave"] == "2"
		and installed_rhine_rows[0]["package_ids"] == "IW-008|IW-010"
		and installed_rhine_rows[0]["current_claimed_state_ids"] == "42|51",
		"installed RG-RHINE-SAAR matrix row must mirror the exact two-package 42/51 exception",
		errors,
	)

	# The accepted closure keeps the RHI/AJX reservation group intact and admits
	# exactly that pair through a documented two-slot exception. IW-045 adds its
	# independently audited RG-651 carrier without changing that exception. Keep
	# the canonical matrix and runtime consumers source-audited so a tempting map
	# rebind cannot silently manufacture capacity.
	dispatch = read("common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt")
	adapter = extract_script_block(
		dispatch,
		"has_independence_wave_runtime_package_adapter_for_execution_id",
	)
	attestation = extract_script_block(
		dispatch,
		"has_independence_wave_runtime_package_content_attestation_for_execution_id",
	)
	adapter_ids = sorted(
		{
			int(value)
			for value in re.findall(
				r"constant:independence_wave_package_id\.iw_(\d{3})", adapter
			)
		}
	)
	attested_ids = sorted(
		{
			int(value)
			for value in re.findall(
				r"constant:independence_wave_package_id\.iw_(\d{3})", attestation
			)
		}
	)
	expected_adapter_ids = {
		1, 2, 4, 6, 7, 8, 9, 10, 12, 13, 14, 15, 17, 18, 19,
		23, 24, 26, 27, 28, 29, 30, 31, 33, 38, 40, 41, 43, 44, 45, 58, 70,
		71, 72, 93, 98, 173, 177, 179, 184,
	}
	expected_attested_ids = {1, 2, 4, 6, 7, 8, 9, 10, 12, 14, 17, 18, 19, 23, 24, 26, 27, 28, 29, 30, 31, 33, 38, 40, 41, 44, 45, 70, 71, 72, 173, 184}
	require(
		set(adapter_ids) == expected_adapter_ids,
		"runtime adapter set changed without updating the accepted Event 006 closure: "
		+ f"expected={sorted(expected_adapter_ids)} found={adapter_ids}",
		errors,
	)
	require(
		set(attested_ids) == expected_attested_ids,
		"content-attestation set changed without updating the accepted Event 006 closure: "
		+ f"expected={sorted(expected_attested_ids)} found={attested_ids}",
		errors,
	)
	expected_adapter_only_ids = expected_adapter_ids - expected_attested_ids
	require(
		set(adapter_ids) - set(attested_ids) == expected_adapter_only_ids,
		"adapter-only fail-closed set changed without an accepted package promotion: "
		+ f"expected={sorted(expected_adapter_only_ids)} found={sorted(set(adapter_ids) - set(attested_ids))}",
		errors,
	)
	require(
		"has_independence_wave_runtime_package_adapter_for_execution_id = yes" in extract_script_block(
			dispatch,
			"is_independence_wave_runtime_package_preflight_ready",
		)
		and "has_independence_wave_runtime_package_content_attestation_for_execution_id = yes" in extract_script_block(
			dispatch,
			"is_independence_wave_runtime_package_preflight_ready",
		),
		"runtime preflight no longer requires both adapter and content-attestation gates",
		errors,
	)
	dispatch_effects = read("common/scripted_effects/006_independence_wave_package_dispatch_effects.txt")
	phase_families: dict[str, set[str]] = {}
	for call, phase in re.findall(
		r"(?m)^\t(independence_wave_dispatch_.+_package_(setup|final_validation|cleanup))\s*=\s*yes$",
		dispatch_effects,
	):
		family = re.sub(r"_package_(?:setup|final_validation|cleanup)$", "", call)
		phase_families.setdefault(family, set()).add(phase)
	require(
		len(phase_families) == 26,
		"central package dispatcher family count changed: " + repr(sorted(phase_families)),
		errors,
	)
	missing_phases = {
		family: sorted({"setup", "final_validation", "cleanup"} - phases)
		for family, phases in phase_families.items()
		if phases != {"setup", "final_validation", "cleanup"}
	}
	require(
		not missing_phases,
		"central package dispatcher has incomplete setup/final-validation/cleanup parity: "
		+ repr(missing_phases),
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
			len(set(attested_groups.values())) == 29,
			"accepted thirty-two-package closure no longer exposes exactly twenty-nine compatible reservation groups: "
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
			len(set(attested_anchors.values())) == 32,
			"attested package anchors are not pairwise unique: " + repr(attested_anchors),
			errors,
		)
		reservation_effects = read("common/scripted_effects/chaosx_liberation_release_effects.txt")
		reservation_triggers = read("common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt")
		capacity_triggers = read("common/scripted_triggers/006_independence_wave_triggers.txt")
		require(
			"independence_wave_reservation_group_id.rg_rhine_saar" in reservation_effects
			and "independence_wave_package_id.iw_008" in reservation_effects
			and "independence_wave_package_id.iw_010" in reservation_effects,
			"RG-RHINE-SAAR pair-capacity exception is missing from the central reservation effect",
			errors,
		)
		require(
			"can_plan_independence_wave_package_iw_008" in reservation_triggers
			and "can_plan_independence_wave_package_iw_010" in reservation_triggers,
			"RG-RHINE-SAAR pair-capacity package triggers are missing",
			errors,
		)
		require(
			capacity_triggers.count("independence_wave_capacity_selected_packages value = constant:independence_wave_package_id.iw_010") >= 1
			and capacity_triggers.count("independence_wave_capacity_selected_packages value = constant:independence_wave_package_id.iw_008") >= 1,
			"RG-RHINE-SAAR pair-capacity witness does not admit both sibling packages",
			errors,
		)
		require(
			"liberation_validation_row_package = constant:independence_wave_package_id.iw_008" in reservation_effects
			and "liberation_validation_inner_package = constant:independence_wave_package_id.iw_010" in reservation_effects,
			"RG-RHINE-SAAR pair-capacity lock invariant exception is missing",
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
	try:
		standalone = extract_script_block(execution, "independence_wave_prepare_and_execute_standalone_incident")
		receipt = extract_script_block(execution, "independence_wave_snapshot_standalone_terminal_receipt")
	except ValueError as exc:
		errors.append(str(exc))
		standalone = ""
		receipt = ""
	for needle, label in (
		("independence_wave_clear_standalone_terminal_receipt = yes", "standalone receipt reset"),
		("independence_wave_snapshot_standalone_terminal_receipt = yes", "standalone terminal receipt snapshot"),
		("liberation_release_begin_plan = yes", "standalone plan begin"),
		("independence_wave_allocate_automatic_packages = yes", "standalone automatic allocation"),
		("independence_wave_expand_selected_optional_territory = yes", "standalone optional territory pass"),
		("independence_wave_execute_standalone_frozen_plan = yes", "standalone frozen execution"),
	):
		require(needle in standalone, f"standalone flow is missing {label}", errors)
	if standalone:
		require_order(
			standalone,
			[
				("receipt reset", "independence_wave_clear_standalone_terminal_receipt = yes"),
				("plan begin", "liberation_release_begin_plan = yes"),
				("terminal receipt", "independence_wave_snapshot_standalone_terminal_receipt = yes"),
			],
			"standalone terminal receipt flow",
			errors,
		)
	for needle, label in (
		("global.independence_wave_terminal_receipt_plan_id", "plan id"),
		("global.independence_wave_terminal_receipt_started_date", "started date"),
		("global.independence_wave_terminal_receipt_committed_date", "committed date"),
		("global.independence_wave_terminal_receipt_phase", "terminal phase"),
		("global.independence_wave_terminal_receipt_last_failure", "last failure"),
		("global.independence_wave_terminal_receipt_finalization_failure", "finalization failure"),
		("global.independence_wave_terminal_receipt_rollback_failure", "rollback failure"),
		("global.independence_wave_terminal_receipt_selected_count", "selected count"),
		("global.independence_wave_terminal_receipt_target_count", "target count"),
		("global.independence_wave_terminal_receipt_instantiated_count", "instantiated count"),
		("global.independence_wave_terminal_receipt_transferred_state_count", "transferred state count"),
		("global.independence_wave_terminal_receipt_prepared_count", "prepared count"),
		("global.independence_wave_terminal_receipt_activated_count", "activated count"),
		("global.independence_wave_terminal_receipt_validated_count", "validated count"),
		("global.independence_wave_terminal_receipt_initialized_count", "initialized count"),
	):
		require(needle in receipt, f"terminal receipt is missing {label}", errors)
	for needle, label in (
		("set_global_flag = independence_wave_terminal_receipt_ready", "receipt-ready flag"),
		("set_global_flag = independence_wave_terminal_receipt_committed", "committed outcome receipt"),
		("set_global_flag = independence_wave_terminal_receipt_cancelled_before_mutation", "pre-mutation cancellation receipt"),
		("set_global_flag = independence_wave_terminal_receipt_failed_after_mutation", "post-mutation failure receipt"),
		("set_global_flag = independence_wave_terminal_receipt_failed_during_finalization", "finalization failure receipt"),
		("set_global_flag = independence_wave_terminal_receipt_rolled_back_after_mutation", "compensating rollback receipt"),
	):
		require(needle in receipt, f"terminal receipt is missing {label}", errors)
	for needle, label in (
		("independence_wave_transfer_frozen_states = yes", "planned state transfer"),
		("set_capital = {", "capital finalization"),
		("is_independence_wave_dormant_country_scope = yes", "dormant-shell validation"),
		("independence_wave_clear_plan_contribution = yes", "contribution cleanup"),
	):
		require(needle in execution, f"Event 006 execution is missing {label}", errors)
	event_root = read("events/006_independence_wave.txt")
	try:
		root_entry = extract_script_block(event_root, "country_event")
	except ValueError as exc:
		errors.append(str(exc))
		root_entry = ""
	for needle, label in (
		("independence_wave_joint_presentation_pending", "joint-delivery marker guard"),
		("independence_wave_prepare_and_execute_standalone_incident = yes", "standalone fallback entry"),
		("has_global_flag = independence_wave_standalone_incident_committed", "committed-only presentation gate"),
		("country_event = { id = chaosx.nr6.2 }", "public report dispatch"),
	):
		require(needle in root_entry, f"Event 006 root is missing {label}", errors)
	static_witness_protected_states = validate_static_20_witness(
		binding_rows,
		installed_reservation_rows,
		attested_ids,
		loaders,
		dispatch,
		errors,
	)
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
	for needle, label in (
		("independence_wave_rollback_reversible_frozen_country_packages = {", "reversible Event 006 cleanup helper"),
		("liberation_release_execute_compensating_rollback = yes", "compensating ownership rollback"),
	):
		require(needle in execution, f"Event 006 execution is missing {label}", errors)
	for needle in (
		"is_owned_by = event_target:independence_wave_execution_state_target",
		"is_controlled_by = event_target:independence_wave_execution_state_target",
		"independence_wave_execution_transfer_failure = constant:liberation_plan_reject_reason.unsafe_instantiation",
	):
		require(needle in execution, f"Event 006 transfer verification is missing {needle}", errors)
	try:
		execution_metadata = extract_script_block(execution, "independence_wave_validate_execution_metadata")
	except ValueError as exc:
		errors.append(str(exc))
		execution_metadata = ""
	for target, first_readiness_trigger in (
		("independence_wave_execution_country", "is_liberation_release_current_reserved_country = yes"),
		("independence_wave_execution_sponsorship_country", "is_liberation_release_current_reserved_country = yes"),
	):
		if target == "independence_wave_execution_country":
			# Event 006 validates the reserved carrier before the release effect
			# activates it. The target is normally absent, but an empty startup
			# carrier shell is also valid; the sponsorship country is the already-
			# existing side of the ledger.
			dormant_target_validation = (
				rf"event_target:{re.escape(target)}\s*=\s*\{{"
				rf"(?:(?:\s*#.*\n)*)"
				rf"\s*(?:exists\s*=\s*no|is_independence_wave_dormant_country_scope\s*=\s*yes)"
				rf"\s*{re.escape(first_readiness_trigger)}"
			)
			require(
				re.search(dormant_target_validation, execution_metadata) is not None,
				f"Event 006 execution metadata does not validate dormant {target} before release",
				errors,
			)
			continue
		positive_target_validation = (
			rf"event_target:{re.escape(target)}\s*=\s*\{{"
			rf"\s*exists\s*=\s*yes"
			rf"\s*{re.escape(first_readiness_trigger)}"
		)
		inverted_target_validation = (
			rf"event_target:{re.escape(target)}\s*=\s*\{{"
			rf"\s*exists\s*=\s*no"
		)
		require(
			re.search(positive_target_validation, execution_metadata) is not None,
			f"Event 006 execution metadata does not positively validate existing {target}",
			errors,
		)
		require(
			re.search(inverted_target_validation, execution_metadata) is None,
			f"Event 006 execution metadata inverts the existence test for {target}",
			errors,
		)

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
	scenario_matrix = read(
		"docs/plans/006_independence_wave_plans/subagent_handoffs/006_scn008_32_cell_static_acceptance_2026_08_02.md"
	)
	cell_ids = re.findall(r"`SCN-008/[^`]+`", scenario_matrix)
	require(
		len(cell_ids) == 32 and len(set(cell_ids)) == 32,
		f"SCN-008 static acceptance matrix must contain 32 unique cells, found {len(set(cell_ids))}",
		errors,
	)
	require(
		all(label in scenario_matrix for label in ("Sovereign Scatter", "Common Congress", "Wars of Separation", "Universal Belligerence: former hosts", "Universal Belligerence: neighboring releases", "Universal Belligerence: nearby non-league", "Patron Worlds", "Great Partition")),
		"SCN-008 static acceptance matrix is missing one or more of the eight player-facing modes",
		errors,
	)
	edge_matrix = read(
		"docs/plans/006_independence_wave_plans/subagent_handoffs/006_scn008_edge_case_static_matrix_2026_08_02.md"
	)
	edge_ids = re.findall(r"`EDGE-SCN-\d{3}`", edge_matrix)
	require(
		len(edge_ids) == 8 and len(set(edge_ids)) == 8,
		f"SCN-008 edge-case static receipt must contain 8 unique cases, found {len(set(edge_ids))}",
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
	try:
		former_host_type = extract_script_block(scenario, "independence_wave_scenario_start_universal_belligerence")
		separation_type = extract_script_block(scenario, "independence_wave_scenario_apply_type")
		host_war = extract_script_block(scenario, "independence_wave_scenario_start_host_war")
		scenario_summary = extract_script_block(scenario, "independence_wave_scenario_freeze_summary")
	except ValueError as exc:
		errors.append(str(exc))
		former_host_type = ""
		separation_type = ""
		host_war = ""
		scenario_summary = ""
	# Universal Former Hosts consumes a distinct-host ledger, but Wars of
	# Separation deliberately keeps one viable host war per release. Guard this
	# boundary so a future refactor cannot leak the temporary uniqueness policy
	# into the ordinary per-release host-war rule.
	require(
		"set_variable = { global.independence_wave_scenario_former_host_unique_policy = constant:independence_wave_scenario_registry.one }" in former_host_type
		and "independence_wave_scenario_clear_belligerence_target_marks = yes" in former_host_type,
		"SCN-008 Universal Former Hosts does not enable and clear its bounded target ledger",
		errors,
	)
	separation_position = separation_type.find("constant:independence_wave_scenario_type.wars_of_separation")
	if separation_position >= 0:
		separation_branch = separation_type[separation_position:]
		require(
			"clear_variable = global.independence_wave_scenario_former_host_unique_policy" in separation_branch
			and "independence_wave_scenario_start_all_host_wars = yes" in separation_branch,
			"SCN-008 Wars of Separation does not clear former-host uniqueness before per-release host wars",
			errors,
		)
	require(
		"check_variable = { global.independence_wave_scenario_former_host_unique_policy" in host_war
		and "global.independence_wave_scenario_belligerence_targets" in host_war
		and "remove_from_array = { array = global.independence_wave_scenario_belligerence_targets" in host_war,
		"SCN-008 host-war helper lacks bounded former-host target reservation/rollback",
		errors,
	)
	committed_gate = scenario_summary.find("has_global_flag = independence_wave_scenario_committed")
	released_append = scenario_summary.find(
		"add_to_array = { array = global.independence_wave_scenario_released_package_ids"
	)
	require(
		committed_gate >= 0 and released_append > committed_gate,
		"SCN-008 summary can publish selected rows as released without the committed flag",
		errors,
	)
	require(
		"add_to_array = { array = global.independence_wave_scenario_blocked_package_ids value = independence_wave_scenario_summary_package_id }" in scenario_summary
		and "add_to_array = { array = global.independence_wave_scenario_blocked_reasons value = global.independence_wave_scenario_last_failure }" in scenario_summary,
		"SCN-008 failed summary does not preserve selected rows as blocked with the failure reason",
		errors,
	)

	joint = read("common/scripted_effects/005_006_liberations_collision_effects.txt")
	for needle, label in (
		("liberations_joint_cancel_before_ownership_mutation = yes", "pre-mutation joint cancellation"),
		("liberations_joint_record_failure_after_ownership_mutation = yes", "post-mutation joint rollback"),
	):
		require(needle in joint, f"joint Event 005/Event 006 flow is missing {label}", errors)
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
	try:
		joint_execution_metadata = extract_script_block(joint, "soviet_collapse_joint_validate_execution_metadata")
	except ValueError as exc:
		errors.append(str(exc))
		joint_execution_metadata = ""
	joint_country_validation = (
		r"event_target:soviet_collapse_joint_execution_country\s*=\s*\{"
		r"\s*exists\s*=\s*yes"
		r"\s*has_country_flag\s*=\s*soviet_collapse_joint_pending_origin"
	)
	joint_country_inversion = (
		r"event_target:soviet_collapse_joint_execution_country\s*=\s*\{"
		r"\s*exists\s*=\s*no"
	)
	require(
		re.search(joint_country_validation, joint_execution_metadata) is not None,
		"joint Event 005 execution metadata does not positively validate the existing reserved country",
		errors,
	)
	require(
		re.search(joint_country_inversion, joint_execution_metadata) is None,
		"joint Event 005 execution metadata inverts the reserved-country existence test",
		errors,
	)

	shared = read("common/scripted_effects/chaosx_liberation_release_effects.txt")
	require("random_owned_state" not in shared, "host-survival selection still contains random_owned_state", errors)
	for needle in (
		"capital_scope =",
		"is_core_of = PREV",
		"is_controlled_by = PREV",
		"liberation_release_select_first_host_state_candidate = yes",
	):
		require(needle in shared, f"host-survival priority is missing {needle}", errors)

	# The pre-event crisis surface is intentionally retired. Event 006 must not
	# expose a pressure category, mission, cost, or queue before its public event.
	compatibility_triggers = read("common/scripted_triggers/006_independence_wave_compatibility_triggers.txt")
	require("can_independence_wave_open_crisis = {" in compatibility_triggers, "retired crisis trigger is missing", errors)
	retired_crisis_trigger = extract_script_block(compatibility_triggers, "can_independence_wave_open_crisis")
	require("always = no" in retired_crisis_trigger, "pre-event crisis trigger is not hard-disabled", errors)
	require(not (ROOT / "common/decisions/006_independence_wave_crisis_decisions.txt").exists(), "retired crisis decision file still exposes a player surface", errors)
	require(not (ROOT / "common/decisions/categories/006_independence_wave_crisis_categories.txt").exists(), "retired crisis category file still exposes a player surface", errors)
	crisis_on_actions = ROOT / "common/on_actions/006_independence_wave_crisis_on_actions.txt"
	require(not crisis_on_actions.exists(), "retired crisis on_annex callback still registers an active on_action file", errors)
	for relative_path in ("common", "events", "history", "interface"):
		for path in (ROOT / relative_path).rglob("*.txt"):
			if path in (crisis_on_actions, ROOT / "common/scripted_effects/006_independence_wave_compatibility_effects.txt"):
				continue
			text = path.read_text(encoding="utf-8-sig")
			require(
				"independence_wave_recover_crisis_requester_loss" not in text,
				f"retired crisis requester-loss callback is still called from {path.relative_to(ROOT)}",
				errors,
			)

	# Dormant Event 006 carriers must be checked through their fixed anchor
	# state, never through capital_scope. A dormant carrier has no valid capital
	# by design, so capital_scope here produces the runtime error reported for
	# BBX, BAX, and AXX and can suppress the package pool before allocation.
	for relative_path, anchor_state, host_tag in (
		("common/scripted_triggers/006_independence_wave_epirus_package_triggers.txt", "185", "GRE"),
		("common/scripted_triggers/006_independence_wave_thrace_package_triggers.txt", "184", "GRE"),
		("common/scripted_triggers/006_independence_wave_banat_package_triggers.txt", "82", "ROM"),
	):
		package_triggers = read(relative_path)
		require(
			"capital_scope" not in package_triggers,
			f"dormant package trigger {relative_path} still dereferences capital_scope",
			errors,
		)
		require(
			re.search(rf"(?m)^\s*{anchor_state}\s*=\s*\{{", package_triggers) is not None,
			f"dormant package trigger {relative_path} lost fixed anchor state {anchor_state}",
			errors,
		)
		require(
			f"owner = {{ exists = yes tag = {host_tag} }}" in package_triggers,
			f"dormant package trigger {relative_path} lost host-owner proof for {host_tag}",
			errors,
		)

	dormant_triggers = read("common/scripted_triggers/006_independence_wave_package_triggers.txt")
	require(
		"num_controlled_states" not in dormant_triggers,
		"dormant-carrier trigger still uses the invalid num_controlled_states variable",
		errors,
	)
	require(
		"NOT = { num_of_controlled_states > 0 }" in dormant_triggers,
		"dormant-carrier trigger lost the documented zero-controlled-state guard",
		errors,
	)

	if errors:
		print("Event 006 allocator audit FAILED")
		for error in errors:
			print(f"- {error}")
		return 1

	print("Event 006 allocator audit passed")
	print(f"- publishers: {len(publishers)}")
	print(f"- automatic/high-chaos selectable packages: {len(automatic_ids)}")
	print(f"- SCN-008 ranked selectable packages: {len(ranked_ids)}")
	print(f"- runtime adapters: {len(adapter_ids)}; adapter-only fail-closed IDs: " + ", ".join(f"IW{package_id:03d}" for package_id in sorted(expected_adapter_only_ids)))
	print(f"- attested packages: {len(attested_ids)}; compatible reservation groups: {len(set(attested_groups.values()))}")
	print(
		"- static standalone witness: 20 admitted packages; protected former-host states "
		+ ", ".join(f"{host}={state_id}" for host, state_id in sorted(static_witness_protected_states.items()))
	)
	print("- RG-RHINE-SAAR pair capacity: 2 distinct packages (IW-008 anchor 51; IW-010 anchor 42)")
	print("- automatic counts: 3 / 4 / 5 / 7 / 10 (World Collapse 10)")
	print("- scenario intensities: low anchor/fragile; medium compact/viable; high extended/armed; maximum extended/high-chaos")
	print("- scenario types: scatter; congress; host wars; universal belligerence; patrons; partition")
	print("- pre-event crisis surface: retired; no category, mission, cost, or queue")
	print("- order: all anchors -> compact -> extended -> lock")
	print("- joint order: Event 005 anchors -> Event 006 anchors -> optional territory -> lock")
	return 0


if __name__ == "__main__":
	sys.exit(main())
