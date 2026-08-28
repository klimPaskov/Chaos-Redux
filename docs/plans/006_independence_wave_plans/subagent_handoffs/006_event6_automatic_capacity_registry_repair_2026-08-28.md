# Event 006 automatic capacity registry repair

Date: 2026-08-28.

## Scope

This bounded repair addresses the confirmed automatic Event 006 selection regression in the Liberations cluster. It does not change package admission, readiness predicates, weights, reservation groups, target counts, collision rules, direct event execution, or the no-pre-event surface.

## Confirmed defect

The generic event-pool capacity check evaluated the thirty-two runtime automatic package wrappers before `independence_wave_begin_plan_contribution` populated `global.independence_wave_plan_possible_countries`. Because those wrappers searched an empty registry, the Event 006 candidate was marked unavailable before `chaosx.nr6.1` could fire automatically.

## Source changes

- `common/scripted_effects/006_independence_wave_package_planner_effects.txt` adds `independence_wave_prepare_runtime_possible_country_registry`, populates `independence_wave_runtime_possible_countries` alongside the durable plan registry during contribution setup, and clears the temporary registry during contribution cleanup.
- `common/scripted_triggers/006_independence_wave_triggers.txt` routes all thirty-two runtime automatic readiness wrappers through `independence_wave_runtime_possible_countries`, preserving each existing exact-package, preflight, anchor, and host check.
- `common/scripted_effects/chaosx_logic_effects.txt` seeds the temporary registry before the Event 006 capacity branch in `evaluate_event_pool_candidate_unavailability` when the chaos requirement and reset gate are valid, then clears it after the probe.

## Validation

The allocator audit reports 149 publishers, 126 automatic/high-chaos selectable packages, 32 content attestations, 29 compatible groups, 40 runtime adapters, 161 unattested rows, and the unchanged 3/4/5/7/10 ladder. Country API, strict flag-family, FORM-16, and SCN-008 scenario-matrix audits pass. A source assertion confirms that all thirty-two automatic wrappers use the temporary registry, contribution setup populates it, and pre-selection prepares and clears it.

The required Event MCP inspect/render retry remains blocked by `ARTIFACT_MANIFEST_INTEGRITY_FAILED` with zero scanned files and zero artifacts. No engine, live save, or non-empty runtime transaction receipt is claimed.

## Remaining risk

Direct `event chaosx.nr6.1` still correctly fails closed when its runtime terminal receipt records an empty eligible pool or a later lock, release, transfer, or finalization failure. This patch only repairs automatic pre-selection; it does not bypass those safeguards.
