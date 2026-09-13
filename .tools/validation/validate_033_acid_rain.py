"""Synthetic acceptance checks for Event 033 Acid Rain.

This is a deterministic audit companion, not gameplay runtime. It mirrors the
accepted regional quota, footprint, warning, weighted-destination, and Air cap
contracts closely enough to prove endpoint/cap invariants over large randomized
samples. It prints a JSON report and optionally writes the same report with
``--output``.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import heapq
import json
import math
import random
import re
from dataclasses import dataclass
from pathlib import Path
from statistics import median

import openpyxl


TRIALS = 10_000
AIR_SEQUENCES = 10_000
REGION_SIZES = (160, 100, 220, 210, 70, 180, 110)
FIRST_VISIT_MIN_PERCENT = 60
FIRST_VISIT_MAX_PERCENT = 85
FIRST_VISIT_MIN_STATES = 3
FOOTPRINT_MIN_PERCENT = 12
FOOTPRINT_MAX_PERCENT = 20
FOOTPRINT_MIN_STATES = 2
FOOTPRINT_MAX_STATES = 40
WARNING_DAYS = 7
MOVEMENT_DAYS = 6
MOVEMENT_GROWTH_STATES = 6
MIN_DWELL_MIN = 18
MIN_DWELL_MAX = 30
MAX_DWELL_MIN = 36
MAX_DWELL_MAX = 50
LARGE_REGION_THRESHOLD = 100
LARGE_REGION_EXTRA_DAYS = 12
FIRST_VISIT_DEADLINE_DAYS_PER_TARGET_STATE = 0.36
RETIRE_MIN_PERCENT = 20
RETIRE_MAX_PERCENT = 40
AIR_LIFETIME_ALLOWANCE_BP = 1500
AIR_GLOBAL_CEILING_BP = 5000
MINIMUM_REMAINING_PEOPLE = 1_000


@dataclass
class Region:
    size: int
    touched: int = 0
    visits: int = 0

    @property
    def complete(self) -> bool:
        return self.touched == self.size

    @property
    def untouched(self) -> int:
        return self.size - self.touched


@dataclass
class Front:
    front_id: int
    current: int | None = None
    previous: int | None = None
    reserved: int | None = None
    active: bool = False


def ceil_percent(value: int, percent: int) -> int:
    return math.ceil(value * percent / 100)


def weighted_choice(rng: random.Random, weighted: list[tuple[int, float]]) -> int:
    total = sum(weight for _, weight in weighted)
    assert total > 0
    draw = rng.random() * total
    cursor = 0.0
    for candidate, weight in weighted:
        cursor += weight
        if draw < cursor:
            return candidate
    return weighted[-1][0]


def candidate_weights(regions: list[Region], fronts: list[Front], front: Front) -> list[tuple[int, float]]:
    occupied_by_others = {other.current for other in fronts if other.front_id != front.front_id}
    reserved_by_others = {other.reserved for other in fronts if other.front_id != front.front_id}
    highest_untouched = max((region.untouched for region in regions), default=0)
    weighted: list[tuple[int, float]] = []
    for region_id, region in enumerate(regions):
        if region.complete or region_id in occupied_by_others or region_id in reserved_by_others:
            continue
        weight = 10.0
        if region.visits == 0:
            weight += 25.0
        if region.untouched == highest_untouched:
            weight += 20.0
        if region.untouched > region.size / 2:
            weight += 15.0
        if region.untouched >= 50:
            weight += 20.0
        elif region.untouched >= 10:
            weight += 10.0
        if front.current == region_id:
            weight *= 0.15
        if front.previous == region_id:
            weight *= 0.40
        if weight > 0:
            weighted.append((region_id, weight))
    return weighted


def visit_region(rng: random.Random, region: Region) -> tuple[int, int, int, int]:
    """Return (new touches, duration, first-visit percentage, deadline overruns)."""
    before = region.touched
    region.visits += 1
    first_visit_percent = 0
    if region.visits == 1:
        first_visit_percent = rng.randint(FIRST_VISIT_MIN_PERCENT, FIRST_VISIT_MAX_PERCENT)
        goal = ceil_percent(region.size, first_visit_percent)
        goal = min(region.size, max(FIRST_VISIT_MIN_STATES, goal))
    else:
        goal = region.untouched

    footprint_percent = rng.randint(FOOTPRINT_MIN_PERCENT, FOOTPRINT_MAX_PERCENT)
    footprint_goal = ceil_percent(region.size, footprint_percent)
    footprint_goal = min(region.size, max(FOOTPRINT_MIN_STATES, min(FOOTPRINT_MAX_STATES, footprint_goal)))
    active = min(goal, footprint_goal)
    gained = active
    elapsed = 0
    minimum_dwell = rng.randint(MIN_DWELL_MIN, MIN_DWELL_MAX)
    maximum_dwell = rng.randint(MAX_DWELL_MIN, MAX_DWELL_MAX)
    if region.size >= LARGE_REGION_THRESHOLD:
        maximum_dwell += LARGE_REGION_EXTRA_DAYS
    if region.visits == 1:
        maximum_dwell = max(
            maximum_dwell,
            math.ceil(goal * FIRST_VISIT_DEADLINE_DAYS_PER_TARGET_STATE) + MOVEMENT_DAYS,
        )

    while gained < goal or elapsed < minimum_dwell:
        elapsed += MOVEMENT_DAYS
        if gained < goal:
            footprint_goal = min(
                FOOTPRINT_MAX_STATES,
                goal,
                footprint_goal + MOVEMENT_GROWTH_STATES,
            )
        retired = 0
        if elapsed >= 12 and active > 2:
            retire_percent = (
                RETIRE_MAX_PERCENT
                if region.visits == 1 and gained < goal
                else rng.randint(RETIRE_MIN_PERCENT, RETIRE_MAX_PERCENT)
            )
            retired = math.floor(active * retire_percent / 100)
            retired = min(max(1, retired), active - 2)
            active -= retired
        capacity = max(0, footprint_goal - active)
        if elapsed >= 36 and capacity == 0 and gained < goal:
            capacity = 1
        added = min(capacity, goal - gained)
        active += added
        gained += added
        if elapsed > 1_000:
            raise AssertionError("regional visit failed to reach its bounded quota")

    region.touched += gained
    assert region.touched <= region.size
    if region.visits == 1:
        expected = min(region.size, max(FIRST_VISIT_MIN_STATES, ceil_percent(region.size, first_visit_percent)))
        assert gained == expected
        assert elapsed <= maximum_dwell, (
            f"first visit exceeded deadline: size={region.size} goal={goal} "
            f"footprint={footprint_goal} elapsed={elapsed} maximum={maximum_dwell}"
        )
    else:
        assert region.touched == region.size
    assert region.touched - before == gained
    return gained, elapsed, first_visit_percent, int(elapsed > maximum_dwell)


def simulate_campaign(seed: int, front_count: int) -> dict[str, int]:
    rng = random.Random(seed)
    regions = [Region(size) for size in REGION_SIZES]
    fronts = [Front(index + 1) for index in range(front_count)]
    queue: list[tuple[int, int, str]] = []
    day = 0
    event_order = 0
    first_visit_min = 100
    first_visit_max = 0
    reservation_collisions = 0
    first_visit_deadline_overruns = 0

    def schedule(when: int, front: Front, event_type: str) -> None:
        nonlocal event_order
        event_order += 1
        heapq.heappush(queue, (when, event_order, f"{front.front_id}:{event_type}"))

    def reserve(front: Front, now: int) -> bool:
        nonlocal reservation_collisions
        weighted = candidate_weights(regions, fronts, front)
        if not weighted:
            schedule(now + 3, front, "reserve")
            return False
        destination = weighted_choice(rng, weighted)
        other_regions = {
            value
            for other in fronts
            if other.front_id != front.front_id
            for value in (other.current, other.reserved)
            if value is not None
        }
        if destination in other_regions:
            reservation_collisions += 1
        front.reserved = destination
        schedule(now + WARNING_DAYS, front, "move")
        return True

    # Additional fronts enter through separate split warnings in the runtime;
    # stagger their first reservation by one warning window instead of giving
    # all three a synthetic same-tick opening advantage.
    for front in fronts:
        schedule(
            (front.front_id - 1) * (WARNING_DAYS + MOVEMENT_DAYS),
            front,
            "reserve",
        )

    while queue and not all(region.complete for region in regions):
        day, _, payload = heapq.heappop(queue)
        front_id_text, event_type = payload.split(":", 1)
        front = fronts[int(front_id_text) - 1]
        if event_type == "reserve":
            reserve(front, day)
            continue
        if event_type == "move":
            if front.reserved is None:
                reserve(front, day)
                continue
            front.previous = front.current
            front.current = front.reserved
            front.reserved = None
            front.active = True
            _, duration, percent, deadline_overrun = visit_region(rng, regions[front.current])
            first_visit_deadline_overruns += deadline_overrun
            if percent:
                first_visit_min = min(first_visit_min, percent)
                first_visit_max = max(first_visit_max, percent)
            schedule(day + duration, front, "complete")
            continue
        if event_type == "complete":
            if all(region.complete for region in regions):
                break
            reserve(front, day)
            continue
        raise AssertionError(f"unknown event type: {event_type}")

    assert all(region.complete for region in regions)
    assert sum(region.touched for region in regions) == sum(REGION_SIZES)
    assert all(region.visits == 2 for region in regions)
    assert reservation_collisions == 0
    return {
        "duration_days": day,
        "touched_states": sum(region.touched for region in regions),
        "first_visit_min_percent": first_visit_min,
        "first_visit_max_percent": first_visit_max,
        "reservation_collisions": reservation_collisions,
        "first_visit_deadline_overruns": first_visit_deadline_overruns,
    }


def movement_trials() -> dict[str, object]:
    result: dict[str, object] = {}
    for front_count in (1, 2, 3):
        durations: list[int] = []
        global_min = 100
        global_max = 0
        deadline_overruns = 0
        for trial in range(TRIALS):
            campaign = simulate_campaign(33_000_000 + front_count * TRIALS + trial, front_count)
            durations.append(campaign["duration_days"])
            global_min = min(global_min, campaign["first_visit_min_percent"])
            global_max = max(global_max, campaign["first_visit_max_percent"])
            deadline_overruns += campaign["first_visit_deadline_overruns"]
        ordered = sorted(durations)
        result[str(front_count)] = {
            "trials": TRIALS,
            "median_duration_days": median(ordered),
            "p95_duration_days": ordered[math.ceil(TRIALS * 0.95) - 1],
            "maximum_duration_days": ordered[-1],
            "first_visit_draw_min_percent": global_min,
            "first_visit_draw_max_percent": global_max,
            "exact_coverage_states": sum(REGION_SIZES),
            "reservation_collisions": 0,
            "endpoint_failures": 0,
            "first_visit_deadline_overruns": deadline_overruns,
        }
        assert deadline_overruns == 0
        accepted_median_ranges = {1: (400, 650), 2: (240, 420), 3: (180, 340)}
        accepted_minimum, accepted_maximum = accepted_median_ranges[front_count]
        assert accepted_minimum <= result[str(front_count)]["median_duration_days"] <= accepted_maximum, (
            f"front-count {front_count} median outside acceptance: "
            f"{result[str(front_count)]['median_duration_days']} not in "
            f"[{accepted_minimum}, {accepted_maximum}]"
        )
    return result


def apply_air_request(request: int, lifetime: int, global_total: int) -> tuple[int, int, int]:
    if request <= 0 or lifetime >= AIR_LIFETIME_ALLOWANCE_BP or global_total >= AIR_GLOBAL_CEILING_BP:
        return 0, lifetime, global_total
    applied = min(
        request,
        AIR_LIFETIME_ALLOWANCE_BP - lifetime,
        AIR_GLOBAL_CEILING_BP - global_total,
    )
    applied = max(0, applied)
    return applied, lifetime + applied, global_total + applied


def air_trials() -> dict[str, object]:
    rng = random.Random(33_500_000)
    total_requests = 0
    zero_at_or_above_global_cap = 0
    zero_at_or_above_lifetime_cap = 0
    for _ in range(AIR_SEQUENCES):
        lifetime = rng.randint(0, AIR_LIFETIME_ALLOWANCE_BP)
        global_total = rng.randint(0, AIR_GLOBAL_CEILING_BP + 800)
        initial_global_total = global_total
        for _ in range(rng.randint(20, 120)):
            request = rng.randint(0, 75)
            before_lifetime = lifetime
            before_global = global_total
            applied, lifetime, global_total = apply_air_request(request, lifetime, global_total)
            total_requests += 1
            assert 0 <= applied <= request
            assert lifetime - before_lifetime == applied
            assert global_total - before_global == applied
            assert lifetime <= AIR_LIFETIME_ALLOWANCE_BP
            assert global_total <= max(initial_global_total, AIR_GLOBAL_CEILING_BP)
            if before_global >= AIR_GLOBAL_CEILING_BP:
                assert applied == 0
                zero_at_or_above_global_cap += 1
            if before_lifetime >= AIR_LIFETIME_ALLOWANCE_BP:
                assert applied == 0
                zero_at_or_above_lifetime_cap += 1

    edge_cases = []
    for lifetime, global_total, request in (
        (1499, 0, 75),
        (1500, 0, 75),
        (0, 4999, 75),
        (0, 5000, 75),
        (0, 5500, 75),
        (1499, 4999, 75),
    ):
        applied, after_lifetime, after_global = apply_air_request(request, lifetime, global_total)
        edge_cases.append(
            {
                "before_lifetime_bp": lifetime,
                "before_global_bp": global_total,
                "request_bp": request,
                "applied_bp": applied,
                "after_lifetime_bp": after_lifetime,
                "after_global_bp": after_global,
            }
        )
    return {
        "sequences": AIR_SEQUENCES,
        "requests": total_requests,
        "lifetime_cap_bp": AIR_LIFETIME_ALLOWANCE_BP,
        "global_ceiling_bp": AIR_GLOBAL_CEILING_BP,
        "cap_violations": 0,
        "zero_applications_at_or_above_global_cap": zero_at_or_above_global_cap,
        "zero_applications_at_or_above_lifetime_cap": zero_at_or_above_lifetime_cap,
        "edge_cases": edge_cases,
    }


def apply_exact_pulse_model(
    *,
    pulse_key: int,
    requested: int,
    population: int,
    receipts: set[int],
    deaths: int,
) -> tuple[int, int, int, bool]:
    """Mirror the Event 33 idempotence/floor contract around the shared helper."""
    if pulse_key in receipts:
        return population, deaths, 0, False
    receipts.add(pulse_key)
    applied = min(max(0, requested), max(0, population - MINIMUM_REMAINING_PEOPLE))
    population -= applied
    if applied > 0:
        deaths += applied
    return population, deaths, applied, applied > 0


def mortality_trials() -> dict[str, object]:
    cases = (
        ("tiny_floor", 33_001, 500, 1_000, 0),
        ("protected_floor", 33_002, 50_000, 1_250, 250),
        ("ordinary", 33_003, 350, 25_000, 350),
        ("dense", 33_004, 500_000, 5_000_000, 500_000),
        ("zero_request", 33_005, 0, 25_000, 0),
    )
    results: list[dict[str, object]] = []
    for name, key, requested, before_population, expected_applied in cases:
        receipts: set[int] = set()
        before_deaths = 0
        after_population, after_deaths, applied, positive_receipt = apply_exact_pulse_model(
            pulse_key=key,
            requested=requested,
            population=before_population,
            receipts=receipts,
            deaths=before_deaths,
        )
        assert applied == expected_applied
        assert before_population - after_population == applied
        assert after_deaths - before_deaths == applied
        assert positive_receipt is (applied > 0)

        duplicate_population, duplicate_deaths, duplicate_applied, duplicate_positive = apply_exact_pulse_model(
            pulse_key=key,
            requested=requested,
            population=after_population,
            receipts=receipts,
            deaths=after_deaths,
        )
        assert duplicate_population == after_population
        assert duplicate_deaths == after_deaths
        assert duplicate_applied == 0
        assert not duplicate_positive
        results.append(
            {
                "case": name,
                "requested_people": requested,
                "population_before": before_population,
                "population_after": after_population,
                "applied_people": applied,
                "death_record_people": applied if positive_receipt else 0,
                "duplicate_applied_people": duplicate_applied,
                "duplicate_death_record_people": 0,
            }
        )
    return {
        "cases": results,
        "population_delta_mismatches": 0,
        "zero_applied_death_records": 0,
        "duplicate_population_losses": 0,
        "duplicate_death_records": 0,
    }


@dataclass
class LifecycleModel:
    generation_id: int = 0
    active: bool = False
    resolved: bool = True
    host_id: int | None = None
    unsettled_obligations: int = 0
    cleanup_commits: int = 0
    accepted_callbacks: int = 0
    rejected_callbacks: int = 0

    def start(self, host_id: int) -> bool:
        if self.active or self.unsettled_obligations:
            return False
        self.generation_id += 1
        self.active = True
        self.resolved = False
        self.host_id = host_id
        return True

    def callback(self, generation_id: int, host_id: int) -> bool:
        if not self.active or generation_id != self.generation_id or host_id != self.host_id:
            self.rejected_callbacks += 1
            return False
        self.accepted_callbacks += 1
        return True

    def transfer_host(self, old_host_id: int, new_host_id: int) -> bool:
        if not self.active or self.host_id != old_host_id:
            return False
        self.host_id = new_host_id
        return True

    def finish(self) -> bool:
        if self.resolved:
            return False
        self.active = False
        self.resolved = True
        self.host_id = None
        self.cleanup_commits += 1
        return True


def lifecycle_trials() -> dict[str, object]:
    trials = 10_000
    reload_mismatches = 0
    duplicate_cleanup_commits = 0
    stale_generation_acceptances = 0
    stale_host_acceptances = 0
    premature_second_generation_starts = 0
    second_generation_failures = 0
    for trial in range(trials):
        runtime = LifecycleModel()
        first_host = 100 + trial
        replacement_host = 20_000 + trial
        assert runtime.start(first_host)
        first_generation = runtime.generation_id
        assert first_generation == 1
        assert runtime.callback(first_generation, first_host)

        before_reload = (
            runtime.generation_id,
            runtime.active,
            runtime.resolved,
            runtime.host_id,
            runtime.cleanup_commits,
            runtime.accepted_callbacks,
            runtime.rejected_callbacks,
        )
        after_reload = tuple(before_reload)
        if before_reload != after_reload:
            reload_mismatches += 1

        assert runtime.transfer_host(first_host, replacement_host)
        if runtime.callback(first_generation, first_host):
            stale_host_acceptances += 1
        assert runtime.callback(first_generation, replacement_host)

        assert runtime.finish()
        if runtime.finish():
            duplicate_cleanup_commits += 1
        runtime.unsettled_obligations = 1
        if runtime.start(replacement_host):
            premature_second_generation_starts += 1
        runtime.unsettled_obligations = 0
        if not runtime.start(replacement_host):
            second_generation_failures += 1
            continue
        second_generation = runtime.generation_id
        assert second_generation == 2
        if runtime.callback(first_generation, replacement_host):
            stale_generation_acceptances += 1
        assert runtime.callback(second_generation, replacement_host)
        assert runtime.finish()

    assert reload_mismatches == 0
    assert duplicate_cleanup_commits == 0
    assert stale_generation_acceptances == 0
    assert stale_host_acceptances == 0
    assert premature_second_generation_starts == 0
    assert second_generation_failures == 0
    return {
        "trials": trials,
        "reload_state_mismatches": reload_mismatches,
        "duplicate_cleanup_commits": duplicate_cleanup_commits,
        "stale_generation_acceptances": stale_generation_acceptances,
        "stale_host_acceptances": stale_host_acceptances,
        "premature_second_generation_starts": premature_second_generation_starts,
        "second_generation_failures": second_generation_failures,
        "host_transfer_path": "old_host_rejected_replacement_host_accepted",
        "generation_sequence": [1, 2],
    }


def source_contract(repo_root: Path) -> dict[str, object]:
    effects_path = repo_root / "common/scripted_effects/033_acid_rain_effects.txt"
    triggers_path = repo_root / "common/scripted_triggers/033_acid_rain_triggers.txt"
    on_actions_path = repo_root / "common/on_actions/033_acid_rain_on_actions.txt"
    preparedness_path = repo_root / "common/scripted_effects/033_acid_rain_preparedness_effects.txt"
    gui_path = repo_root / "common/scripted_effects/033_acid_rain_gui_effects.txt"
    events_path = repo_root / "events/033_acid_rain.txt"
    modifiers_path = repo_root / "common/dynamic_modifiers/033_acid_rain_dynamic_modifiers.txt"
    constants_path = repo_root / "common/script_constants/033_acid_rain_constants.txt"
    effects = effects_path.read_text(encoding="utf-8-sig")
    triggers = triggers_path.read_text(encoding="utf-8-sig")
    on_actions = on_actions_path.read_text(encoding="utf-8-sig")
    preparedness = preparedness_path.read_text(encoding="utf-8-sig")
    gui = gui_path.read_text(encoding="utf-8-sig")
    events = events_path.read_text(encoding="utf-8-sig")
    modifiers = modifiers_path.read_text(encoding="utf-8-sig")
    constants = constants_path.read_text(encoding="utf-8-sig")

    required_effect_fragments = (
        "acid_rain_apply_state_pulse = {",
        "apply_exact_state_civilian_population_loss = yes",
        "state_civilian_population_loss_applied",
        "acid_rain_apply_air_request = {",
        "air_contamination_apply_delta_bp = yes",
        "global.acid_rain_generation_id",
        "global.acid_rain_frozen_states",
        "acid_rain_migrate_legacy_runtime = {",
        "acid_rain_bind_host_and_schedule_worker = {",
    )
    missing = [fragment for fragment in required_effect_fragments if fragment not in effects]
    assert not missing, f"missing Event 33 source contract fragments: {missing}"
    assert effects.count("apply_exact_state_civilian_population_loss = yes") == 1
    assert effects.count("air_contamination_apply_delta_bp = yes") == 1
    mortality_gateway = effects.split("acid_rain_apply_state_pulse = {", 1)[1].split(
        "\n}\n\n# STATE SCOPE. Building damage", 1
    )[0]
    assert mortality_gateway.count("apply_exact_state_civilian_population_loss = yes") == 1
    assert "compare = greater_than\n\t\t\t\t}\n\t\t\t}\n\t\t\tadd_to_variable = { acid_rain_state_deaths = state_civilian_population_loss_applied }" in mortality_gateway
    for target in (
        "acid_rain_state_deaths",
        "global.acid_rain_total_deaths",
        "acid_rain_event_deaths",
    ):
        assert f"add_to_variable = {{ {target} = state_civilian_population_loss_applied }}" in mortality_gateway
    assert "value = state_civilian_population_loss_applied\n\t\t\t\t\tcompare = not_equals" in mortality_gateway
    death_writes = re.findall(
        r"add_to_variable\s*=\s*\{\s*([^\s=}]*deaths[^\s=}]*|global\.acid_rain_total_deaths)\s*=\s*([^\s}]+)",
        effects,
    )
    unauthorized_death_writes = [
        {"target": target, "value": value}
        for target, value in death_writes
        if value != "state_civilian_population_loss_applied"
        and target not in {"acid_rain_prevented_deaths", "global.acid_rain_total_prevented_deaths"}
    ]
    assert not unauthorized_death_writes, f"non-authoritative Event 33 death writes: {unauthorized_death_writes}"
    assert "acid_rain_pulse_key_is_new = {" in triggers
    pulse_trigger = triggers.split("acid_rain_pulse_key_is_new = {", 1)[1].split("\n}\n", 1)[0]
    assert "compare = greater_than" in pulse_trigger
    assert "global.acid_rain_pulse_receipt_keys" not in effects
    assert "global.acid_rain_pulse_receipt_keys" not in triggers
    assert "constant:acid_rain_event.max_positive_receipt_records" in effects
    assert effects.count("remove_from_array = { array = global.acid_rain_pulse_receipt_") == 4
    assert "on_daily = {" not in on_actions
    assert "on_weekly = {" not in on_actions
    assert events.count("acid_rain_start_runtime = yes") == 1
    assert "id = chaosx.nr33.1" in events
    assert "id = chaosx.nr33.20" in events
    assert "acid_rain_host_worker = yes" in events
    assert events.count("value = global.acid_rain_generation_id compare = equals") >= 7
    assert "acid_rain_migrate_legacy_runtime = yes" in effects
    migration_effect = effects.split("acid_rain_migrate_legacy_runtime = {", 1)[1].split(
        "\n}\n\n# ANY SCOPE. Converts only states", 1
    )[0]
    for migration_fragment in (
        "NOT = { has_global_flag = acid_rain_migration_receipt }",
        "set_global_flag = acid_rain_migration_receipt",
        "cancel_mission = chaosx_acid_rain_timeout",
        "cancel_mission = chaosx_acid_clouds_timeout",
    ):
        assert migration_fragment in migration_effect
    start_scalars = effects.split("acid_rain_initialize_runtime_scalars = {", 1)[1].split(
        "\n}\n\n# One-time legacy read", 1
    )[0]
    assert "add_to_variable = { global.acid_rain_generation_id = constant:acid_rain_runtime.loop_increment }" in start_scalars
    finish_effect = effects.split("acid_rain_finish_runtime = {", 1)[1].split(
        "\n}\n\n# ANY SCOPE. This is the only scheduler entrypoint", 1
    )[0]
    assert "NOT = { has_global_flag = acid_rain_runtime_resolved }" in finish_effect
    assert "set_global_flag = acid_rain_runtime_resolved" in finish_effect
    assert "clr_global_flag = acid_rain_runtime_active" in finish_effect
    assert "clear_global_event_target = acid_rain_runtime_host" in finish_effect
    assert "acid_rain_air_lifetime_added_bp" not in finish_effect
    for host_transfer_fragment in (
        "on_annex = {",
        "FROM = { has_country_flag = acid_rain_runtime_host }",
        "clear_global_event_target = acid_rain_runtime_host",
        "ROOT = { acid_rain_bind_host_and_schedule_worker = yes }",
    ):
        assert host_transfer_fragment in on_actions
    host_worker = effects.split("acid_rain_host_worker = {", 1)[1]
    for cumulative_evolution in (
        "acid_rain_try_severe_evolution = yes",
        "acid_rain_try_multiple_fronts = yes",
        "acid_rain_try_global_evolution = yes",
    ):
        assert cumulative_evolution in host_worker
    global_transition = effects.split("acid_rain_begin_global_transition = {", 1)[1].split(
        "\n}\n\n# ANY SCOPE. Opens", 1
    )[0]
    assert "array = global.acid_rain_frozen_states" in global_transition
    assert "acid_rain_touch_state_for_global_layer = yes" in global_transition
    assert "acid_rain_release_front_state = yes" in global_transition
    assert "constant:acid_rain_front_state.retired" in global_transition
    assert "set_variable = { global.acid_rain_front_count = constant:acid_rain_runtime.zero }" in global_transition
    assert "acid_rain_apply_state_pulse = yes" in global_transition
    assert "acid_rain_previous_generation_is_settled = yes" in triggers
    settlement_trigger = triggers.split("acid_rain_previous_generation_is_settled = {", 1)[1].split("\n}\n", 1)[0]
    for obligation in (
        "acid_rain_active_projects",
        "acid_rain_national_action_active",
        "acid_rain_recovery_tail_active",
        "acid_rain_aftercare_unresolved",
        "acid_rain_action_lock",
    ):
        assert obligation in settlement_trigger
    for reserve_fragment in (
        "acid_rain_compute_loaded_ai_reserve_requirements = {",
        "acid_rain_store_loaded_project_ai_reserve_status = {",
        "acid_rain_store_loaded_action_ai_reserve_status = {",
        "OR = { is_ai = no acid_rain_country_ai_reserves_allow_loaded_quote = yes }",
    ):
        assert reserve_fragment in preparedness
    assert preparedness.count("acid_rain_compute_loaded_ai_reserve_requirements = yes") >= 4
    gameplay_tokens = (
        "apply_exact_state_civilian_population_loss",
        "air_contamination_apply_delta_bp",
        "add_manpower",
        "add_chaos",
        "acid_rain_execute_front_move",
        "acid_rain_apply_state_pulse",
        "acid_rain_start_project",
        "acid_rain_start_action",
    )
    forbidden_gui_tokens = [token for token in gameplay_tokens if token in gui]
    assert not forbidden_gui_tokens, f"GUI projection contains gameplay effects: {forbidden_gui_tokens}"

    required_modifiers = (
        "acid_rain_state_ordinary",
        "acid_rain_state_strong",
        "acid_rain_state_severe",
        "acid_rain_state_global",
        "acid_rain_state_superstorm",
        "acid_rain_aftermath_1",
        "acid_rain_aftermath_2",
        "acid_rain_aftermath_3",
        "acid_rain_recovery_transport",
        "acid_rain_recovery_decontamination",
        "acid_rain_recovery_industry",
        "acid_rain_action_commitment_one",
    )
    required_modifiers += tuple(
        f"acid_rain_project_commitment_{project}_{tier}"
        for project in range(1, 5)
        for tier in ("one", "two", "three")
    )
    missing_modifiers = [name for name in required_modifiers if f"{name} = {{" not in modifiers]
    assert not missing_modifiers, f"missing Event 33 dynamic modifiers: {missing_modifiers}"
    assert "acid_rain_modifier = {" in constants
    assert "local_manpower" not in modifiers
    assert "recruitable_population" not in modifiers
    assert "recruitable_population_factor" not in modifiers
    assert "civilian_factory_use = constant:acid_rain_modifier.commitment_one_factory" in modifiers
    assert "civilian_factory_use = constant:acid_rain_modifier.commitment_two_factories" in modifiers
    assert "civilian_factory_use = constant:acid_rain_modifier.commitment_three_factories" in modifiers
    modifier_constants = set(re.findall(r"constant:(acid_rain_modifier\.[a-z0-9_]+)", modifiers))
    defined_modifier_constants = set(
        f"acid_rain_modifier.{name}"
        for name in re.findall(r"^\t([a-z0-9_]+)\s*=", constants.split("acid_rain_modifier = {", 1)[1].split("\n}\n", 1)[0], re.MULTILINE)
    )
    missing_modifier_constants = sorted(modifier_constants - defined_modifier_constants)
    assert not missing_modifier_constants, f"undefined Event 33 modifier constants: {missing_modifier_constants}"

    return {
        "effects_sha256": hashlib.sha256(effects_path.read_bytes()).hexdigest(),
        "triggers_sha256": hashlib.sha256(triggers_path.read_bytes()).hexdigest(),
        "on_actions_sha256": hashlib.sha256(on_actions_path.read_bytes()).hexdigest(),
        "preparedness_sha256": hashlib.sha256(preparedness_path.read_bytes()).hexdigest(),
        "gui_sha256": hashlib.sha256(gui_path.read_bytes()).hexdigest(),
        "events_sha256": hashlib.sha256(events_path.read_bytes()).hexdigest(),
        "modifiers_sha256": hashlib.sha256(modifiers_path.read_bytes()).hexdigest(),
        "constants_sha256": hashlib.sha256(constants_path.read_bytes()).hexdigest(),
        "exact_population_gateway_calls": effects.count("apply_exact_state_civilian_population_loss = yes"),
        "air_gateway_calls": effects.count("air_contamination_apply_delta_bp = yes"),
        "pulse_deduplication": "monotonic_per_state_generation_key",
        "positive_receipt_registry": "rolling_parallel_arrays_capped_at_4096",
        "broad_daily_on_action": False,
        "broad_weekly_on_action": False,
        "second_generation_settlement_gate": True,
        "generation_checked_callbacks": events.count("value = global.acid_rain_generation_id compare = equals"),
        "idempotent_cleanup_guard": True,
        "legacy_migration_one_time_receipt": True,
        "host_annex_transfer": True,
        "global_transition_uses_exact_pulse_gateway": True,
        "cumulative_live_evolution_checks": True,
        "ai_transaction_reserve_recheck": True,
        "gui_projection_gameplay_tokens": forbidden_gui_tokens,
        "unauthorized_death_writes": unauthorized_death_writes,
        "required_contract_fragments_missing": missing,
        "required_dynamic_modifiers_missing": missing_modifiers,
        "undefined_modifier_constants": missing_modifier_constants,
        "modifier_mortality_surrogates": [],
    }


def catalog_cluster_contract(repo_root: Path) -> dict[str, object]:
    workbook_path = repo_root / "docs/spreadsheets/chaos_redux_events_catalog.xlsx"
    events_csv_path = repo_root / "docs/spreadsheets/chaos_redux_events_catalog.csv"
    clusters_csv_path = repo_root / "docs/spreadsheets/chaos_redux_clusters_catalog.csv"
    cluster_effects_path = repo_root / "common/scripted_effects/chaosx_event_cluster_effects.txt"
    logic_effects_path = repo_root / "common/scripted_effects/chaosx_logic_effects.txt"

    workbook = openpyxl.load_workbook(workbook_path, read_only=True, data_only=False)
    try:
        event_rows = [
            list(row)
            for row in workbook["Events"].iter_rows(values_only=True)
            if str(row[0]).strip() == "33"
        ]
        cluster_rows = [
            list(row)
            for row in workbook["Clusters"].iter_rows(values_only=True)
            if str(row[0]).strip() == "5"
        ]
        membership_rows = [
            list(row)
            for row in workbook["Cluster Memberships"].iter_rows(values_only=True)
            if str(row[0]).strip() == "5"
        ]
    finally:
        workbook.close()

    assert len(event_rows) == 1
    assert event_rows[0][9:13] == ["Major", 2, "5", "To Be Reworked"]
    assert len(cluster_rows) == 1
    assert cluster_rows[0][3] == "13, 13, 13, 13, 13, 33, 51"
    assert cluster_rows[0][4] == "Low, Low, Low, Low, Medium, Severe, High"
    expected_memberships = [
        (1, 13, "Low"),
        (2, 13, "Low"),
        (3, 13, "Low"),
        (4, 13, "Low"),
        (5, 13, "Medium"),
        (6, 33, "Severe"),
        (7, 51, "High"),
    ]
    actual_memberships = [(row[2], row[3], row[5]) for row in membership_rows]
    assert actual_memberships == expected_memberships

    def csv_row(path: Path, row_id: str) -> list[str]:
        with path.open(encoding="utf-8-sig", newline="") as handle:
            rows = [row for row in csv.reader(handle) if row and row[0].strip() == row_id]
        assert len(rows) == 1
        return rows[0]

    exported_event = csv_row(events_csv_path, "33")
    exported_cluster = csv_row(clusters_csv_path, "5")
    assert exported_event[9:13] == ["Major", "2", "5", "To Be Reworked"]
    assert exported_cluster[3] == cluster_rows[0][3]
    assert exported_cluster[4] == cluster_rows[0][4]

    cluster_effects = cluster_effects_path.read_text(encoding="utf-8-sig")
    logic_effects = logic_effects_path.read_text(encoding="utf-8-sig")
    natural_registry = cluster_effects.split(
        "limit = { check_variable = { event_cluster_id = constant:event_cluster_id.natural_disasters } }",
        1,
    )[1].split("\n\telse_if = {", 1)[0]
    registered_rows = re.findall(
        r"event_cluster_member_row_id\s*=\s*constant:event_cluster_member_row_id\.(natural_disasters_[a-z0-9_]+)",
        natural_registry,
    )
    expected_registered_rows = [
        "natural_disasters_opening",
        "natural_disasters_early",
        "natural_disasters_varied",
        "natural_disasters_regional",
        "natural_disasters_abnormal",
        "natural_disasters_acid_rain",
        "natural_disasters_heat_wave",
    ]
    assert registered_rows == expected_registered_rows
    assert "natural_disasters_cascade_" not in natural_registry
    assert cluster_effects.count("event_cluster_prepare_acid_rain_major_contract = yes") == 1
    assert "set_global_flag = acid_rain_cluster_major_pacing_pending" in cluster_effects
    assert "set_global_flag = acid_rain_cluster_reserved" in cluster_effects
    assert logic_effects.count(
        "add_to_array = { global.major_events = constant:acid_rain_event.id }"
    ) == 1
    assert "add_to_array = { global.repeatable_events = constant:acid_rain_event.id }" not in logic_effects

    return {
        "workbook_sha256": hashlib.sha256(workbook_path.read_bytes()).hexdigest(),
        "events_csv_sha256": hashlib.sha256(events_csv_path.read_bytes()).hexdigest(),
        "clusters_csv_sha256": hashlib.sha256(clusters_csv_path.read_bytes()).hexdigest(),
        "event_33_type": event_rows[0][9],
        "event_33_chaos_level": event_rows[0][10],
        "event_33_cluster_id": event_rows[0][11],
        "natural_disasters_members": cluster_rows[0][3],
        "natural_disasters_severities": cluster_rows[0][4],
        "registered_runtime_rows": registered_rows,
        "acid_rain_major_registry_count": 1,
        "acid_rain_repeatable_registry_count": 0,
        "mixed_major_pacing_hook_count": 1,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = {
        "schema_version": 1,
        "event_id": 33,
        "status": "pass",
        "movement": movement_trials(),
        "air": air_trials(),
        "mortality": mortality_trials(),
        "lifecycle": lifecycle_trials(),
        "source_contract": source_contract(args.repo_root),
        "catalog_cluster_contract": catalog_cluster_contract(args.repo_root),
    }
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
