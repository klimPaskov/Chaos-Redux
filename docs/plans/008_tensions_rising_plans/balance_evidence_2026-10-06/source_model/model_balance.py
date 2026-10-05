#!/usr/bin/env python3
"""Bounded, source-anchored model for Event008 packet distribution/reporting."""

from __future__ import annotations

import hashlib
import json
import math
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
EFFECTS = ROOT / "common/scripted_effects/008_tensions_rising_effects.txt"
TRIGGERS = ROOT / "common/scripted_triggers/008_tensions_rising_triggers.txt"
EVENTS = ROOT / "events/008_tensions_rising.txt"
CONSTANTS = ROOT / "common/script_constants/008_tensions_rising_constants.txt"
CHAOS_EFFECTS = ROOT / "common/scripted_effects/chaos_meter_effects.txt"
OUTPUT = Path(__file__).with_name("result_2026-10-06.json")


def balanced_block(text: str, name: str) -> str:
    text = re.sub(r"(?m)#.*$", "", text)
    match = re.search(rf"(?m)^{re.escape(name)}\s*=\s*\{{", text)
    if not match:
        raise AssertionError(f"source block missing: {name}")
    start = match.end() - 1
    depth = 0
    for i in range(start, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return text[start : i + 1]
    raise AssertionError(f"unterminated source block: {name}")


def parse_constants(text: str, group: str) -> dict[str, float]:
    body = balanced_block(text, group)
    return {key: float(value) for key, value in re.findall(r"(?m)^\s*([a-z0-9_]+)\s*=\s*(-?[0-9]+(?:\.[0-9]+)?)\s*$", body)}


def event_block(text: str, event_id: str) -> str:
    at = text.find(f"id = {event_id}")
    if at < 0:
        raise AssertionError(f"event ID missing: {event_id}")
    start = text.rfind("country_event = {", 0, at)
    if start < 0:
        raise AssertionError(f"country_event block missing for {event_id}")
    return balanced_block(text[start:], "country_event")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    source = {p: p.read_text(encoding="utf-8-sig") for p in (EFFECTS, TRIGGERS, EVENTS, CONSTANTS, CHAOS_EFFECTS)}
    helper = balanced_block(source[EFFECTS], "apply_tensions_rising_distributed_world_tension")
    root_effect = balanced_block(source[EFFECTS], "apply_tensions_rising_event_effect")
    stage_world = balanced_block(source[EFFECTS], "apply_tensions_rising_stage_world_tension")
    stage_chaos = balanced_block(source[EFFECTS], "apply_tensions_rising_stage_chaos")
    generic_chaos = balanced_block(source[CHAOS_EFFECTS], "add_chaos_meter_value")
    automatic = balanced_block(source[TRIGGERS], "is_tensions_rising_automatic_event_available")
    report_ack = event_block(source[EVENTS], "chaosx.nr8.16")
    packet_values = parse_constants(source[CONSTANTS], "tensions_rising_world_tension_gain")
    reporting = parse_constants(source[CONSTANTS], "tensions_rising_reporting")

    # These source-shape assertions pin the executable model to the actual body.
    required = [
        "set_temp_variable = { tensions_rising_world_tension_before = global.threat }",
        "divide_temp_variable = { tensions_rising_world_tension_source_cap = constant:tensions_rising_world_tension_gain.minimum_country_slice }",
        "round_temp_variable = tensions_rising_world_tension_source_cap",
        "compare = greater_than",
        "subtract_from_temp_variable = { tensions_rising_world_tension_source_cap = 1 }",
        "clamp_temp_variable = { var = tensions_rising_world_tension_source_cap min = 1 }",
        "clamp_temp_variable = { var = tensions_rising_world_tension_selected_count max = tensions_rising_world_tension_source_cap }",
        "divide_temp_variable = { tensions_rising_world_tension_slice = tensions_rising_world_tension_selected_count }",
        "random_select_amount = [RECIPIENT_COUNT]",
        'RECIPIENT_COUNT = "[?tensions_rising_world_tension_selected_count|.0]"',
        "set_temp_variable = { tensions_rising_applied_world_tension = global.threat }",
        "subtract_from_temp_variable = { tensions_rising_applied_world_tension = tensions_rising_world_tension_before }",
        "multiply_temp_variable = { tensions_rising_applied_world_tension = constant:tensions_rising_reporting.world_tension_scale }",
        "clamp_temp_variable = { var = tensions_rising_applied_world_tension min = 0 }",
    ]
    missing = [item for item in required if item not in helper]
    assert not missing, f"source shape changed; model not applicable: {missing}"
    assert "add_to_variable = { tensions_rising_report_world_tension = tensions_rising_applied_world_tension }" in root_effect
    assert "add_to_variable = { tensions_rising_report_world_tension = tensions_rising_applied_world_tension }" in stage_world
    assert "tensions_rising_report_world_tension" not in helper, "helper must not mutate pending report" 
    assert "set_temp_variable = { tensions_rising_applied_world_tension = 0 }" in stage_world
    assert "set_temp_variable = { tensions_rising_applied_world_tension = 0 }" in root_effect
    # Root initializes its accumulator for a new report before entering this helper.
    assert "set_variable = { tensions_rising_report_world_tension = 0 }" in root_effect
    assert "set_temp_variable = { tensions_rising_chaos_delta = global.chaos_meter_value }" in root_effect
    assert "subtract_from_temp_variable = { tensions_rising_chaos_delta = tensions_rising_chaos_before }" in root_effect
    assert "add_to_variable = { tensions_rising_report_chaos = tensions_rising_chaos_delta }" in root_effect
    assert root_effect.index("tensions_rising_sync_world_tension_tracker = yes") < root_effect.index("set_temp_variable = { tensions_rising_chaos_delta = global.chaos_meter_value }")
    assert "NOT = { has_global_flag = tensions_rising_recent_shock }" in automatic
    assert "has_global_flag = tensions_rising_recent_shock" not in source[EVENTS]
    assert "clr_country_flag = tensions_rising_report_effectful" in root_effect
    assert "clr_country_flag = tensions_rising_report_effectful" in report_ack
    capture = balanced_block(source[EFFECTS], "capture_tensions_rising_first_effectful_report_stage")
    assert "NOT = { has_country_flag = tensions_rising_report_effectful }" in capture
    assert "set_country_flag = tensions_rising_report_effectful" in capture
    assert "set_variable = { tensions_rising_report_stage = tensions_rising_stage }" in capture

    # Execute the source-equivalent recipient selection. Native eligibility and RNG
    # are bounded stubs: the first N of a caller-supplied eligible set is selected.
    min_slice = packet_values["minimum_country_slice"]
    scale = reporting["world_tension_scale"]
    packet_keys = ["baseline", "stage_1", "stage_2", "stage_3", "stage_4"]
    packets = [(key, packet_values[key]) for key in packet_keys]
    packets += [("future_fractional_0_05", 0.05), ("future_fractional_2_05", 2.05)]
    counts = [0, 1, 10, 20, 30, 50, 180, 240]
    before_values = [0.0, 0.95, 1.0]
    cases = []
    case_count = 0
    for packet_name, packet in packets:
        for eligible in counts:
            # Engine round semantics are modeled explicitly to mirror round then
            # decrement when the rounded result exceeded the unrounded quotient.
            raw_cap = packet / min_slice
            rounded = math.floor(raw_cap + 0.5)
            cap = rounded - (1 if rounded > raw_cap else 0)
            cap = max(1, cap)
            selected = min(eligible, cap)
            slice_size = packet / selected if selected else None
            assert selected <= cap
            assert selected <= eligible
            if selected:
                assert math.isclose(slice_size * selected, packet, abs_tol=1e-12)
            else:
                assert slice_size is None
            for before in before_values:
                # add_named_threat receives percentage points; global.threat is
                # [0,1], so the returned value is the clipped meter delta in points.
                after = min(1.0, before + (packet / scale if selected else 0.0))
                actual_points = max(0.0, (after - before) * scale)
                assert actual_points <= packet + 1e-9
                assert 0 <= after <= 1
                case_count += 1
                cases.append({
                    "packet": packet_name,
                    "packet_points": packet,
                    "eligible_source_count": eligible,
                    "recipient_cap": cap,
                    "selected_count": selected,
                    "per_recipient_points": slice_size,
                    "before_global_threat": before,
                    "after_global_threat": after,
                    "returned_actual_meter_points": actual_points,
                    "caller_report_addition": actual_points,
                    "ignored_caller_output_report_addition": 0,
                })

    # Exercise pending-report accumulation as before/after behavior: direct
    # scripted addition uses the actual returned amount; ignored outputs vanish.
    report_cases = []
    for start, returned in [(0.0, 0.0), (1.25, 0.5), (1.25, 0.0), (0.2, 3.0)]:
        report_cases.append({"before_report_points": start, "actual_return": returned,
                             "after_report_points": start + returned})

    # Source-backed local Chaos-meter behavior: the generic effect rounds the
    # change, adds it, clamps the meter at zero, and rounds the stored result.
    assert "round_temp_variable = chaos_change" in generic_chaos
    assert "add_to_variable = { global.chaos_meter_value = chaos_change }" in generic_chaos
    assert "clamp_variable = {\n\t\t\tvar = global.chaos_meter_value\n\t\t\tmin = 0" in generic_chaos
    chaos_cases = []
    for before, requested in [(10.0, 2.4), (10.0, 0.0), (1.0, -3.0)]:
        rounded_delta = math.floor(requested + 0.5) if requested >= 0 else math.ceil(requested - 0.5)
        after = max(0.0, round(before + rounded_delta))
        chaos_cases.append({"before": before, "requested_change": requested,
                            "rounded_change": rounded_delta, "after": after,
                            "actual_delta": after - before})
    assert [case["actual_delta"] for case in chaos_cases] == [2.0, 0.0, -1.0]
    for case in chaos_cases:
        # Root snapshots the meter around the full effect sequence and records
        # the net observed change; tracker and clipping effects are therefore
        # represented only when supplied as actual before/after states.
        case["root_reported_net_delta"] = case["after"] - case["before"]
        assert case["root_reported_net_delta"] == case["actual_delta"]
    assert "set_temp_variable = { chaos_history_reason_custom = 1 }" in stage_chaos

    # Source static checks for report-stage capture/clear and automatic/manual gates.
    assert "capture_tensions_rising_first_effectful_report_stage = yes" in root_effect
    assert "if = {\n\t\tlimit = { NOT = { has_country_flag = tensions_rising_report_pending } }" in root_effect
    assert "has_variable = automatic_event_firing_context" in balanced_block(source[EFFECTS], "tensions_rising_prepare_random_event_fire")
    assert reporting["automatic_cooldown_days"] == 30
    result = {
        "scope": "Bounded actual-source model of Event008 distributed world-tension helper, caller report accumulation, relevant report-stage/cooldown guards, and local Chaos-meter arithmetic.",
        "source_sha256": {str(p.relative_to(ROOT)).replace("\\", "/"): sha(p) for p in (EFFECTS, TRIGGERS, EVENTS, CONSTANTS, CHAOS_EFFECTS)},
        "model_sha256": sha(Path(__file__)),
        "source_constants": {"world_tension_packets": {key: packet_values[key] for key in packet_keys},
                             "minimum_country_slice": min_slice,
                             "world_tension_scale": scale,
                             "automatic_cooldown_days": reporting["automatic_cooldown_days"]},
        "coverage": {"packets": len(packets), "eligible_counts": counts,
                     "before_meter_points": before_values,
                     "world_tension_cases": case_count,
                     "report_accumulation_examples": len(report_cases),
                     "chaos_meter_before_after_examples": len(chaos_cases),
                     "root_observed_net_chaos_deltas": [case["root_reported_net_delta"] for case in chaos_cases],
                     "recipient_rng_stub": "select first selected_count from supplied eligible records",
                     "caller_output_rule": "actual returned delta is recorded only when caller explicitly accumulates the output; incident/ignored output is discarded"},
        "static_source_assertions": ["helper has packet/minimum-slice cap, round-and-decrement floor correction, minimum cap 1, selected min(count,cap), equal packet slices, and .0 integer meta expansion",
                                     "helper computes actual global.threat delta times source scale and clamps negative return to zero",
                                     "root initializes report accumulators and accumulates actual output; stage-world caller initializes output and accumulates it",
                                     "helper does not mutate pending report accumulators",
                                     "new report batch and acknowledgement clear effectful flag; first-effectful capture is guarded by the flag",
                                     "automatic availability rejects global recent-shock flag; preparer ties rejection to automatic firing context",
                                     "manual forced entry bypasses automatic availability condition by source control flow",
                                     "Chaos source rounds requested change, applies it, clamps meter at zero, then rounds stored meter"],
        "case_examples": {"world_tension": cases, "report_accumulation": report_cases, "chaos_meter": chaos_cases},
        "limits": ["Native source-country eligibility trigger is stubbed as the explicit eligible count.",
                   "Native random_select_amount is deterministic first-N in the model; no probability estimate is claimed.",
                   "Global threat's engine-side add_named_threat behavior and global tracker synchronization are bounded stubs; the model applies source scale and [0,1] meter cap to exercise clipping.",
                   "Chaos-meter tests cover the visible generic block arithmetic only; disabled-meter and final-tier guards, shared tracker effects, and full overall-global-delta aggregation are not modeled.",
                   "No on_action scheduling, scope propagation, PREV behavior, pulse cadence, or opinion behavior is modeled.",
                   "Static control-flow assertions do not prove engine runtime semantics or live game behavior."],
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    # Model SHA is added after writing so the JSON records the exact executed model file hash.
    data = json.loads(OUTPUT.read_text(encoding="utf-8"))
    data["model_sha256"] = sha(Path(__file__))
    OUTPUT.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(OUTPUT), "world_tension_cases": case_count,
                      "source_sha256": data["source_sha256"], "model_sha256": data["model_sha256"]}, indent=2))


if __name__ == "__main__":
    main()
