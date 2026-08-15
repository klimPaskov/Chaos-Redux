# Event 006 DM-62 factory-aware availability gate

Date: 2026-08-15

## Disposition

Implemented a bounded source-backed repair for DM-62, `independence_wave_request_charter_war_mandate`.

The accepted decision matrix requires a diplomatic-standard commitment plus one civilian factory for DM-62 (`docs/specs/006_independence_wave_specs/matrices/006_decision_mission_map.csv:63`). The decision already reserved the light factory with `civilian_factory_use`, but its availability and custom-cost trigger checked only the diplomatic portion. DM-62 now uses a factory-aware affordability trigger for both checks.

This repair does not widen package admission, content attestation, scenario preflight, deterministic Join, reservation groups, or the Event 006 authority boundary.

## Changed files and identifiers

- `common/scripted_triggers/006_independence_wave_decision_triggers.txt:257-264`
  - Added `can_pay_independence_wave_diplomatic_standard_factory_cost`.
  - The helper requires spare civilian factories above the existing `independence_wave_decision_cost.civilian_factory_light` threshold, standard command power, and the existing convoy-or-train diplomatic material branch.
- `common/decisions/006_independence_wave_decisions.txt:2923-2924`
  - DM-62 now uses the new helper for both `available` and `custom_cost_trigger`.

The existing `independence_wave_cost_diplomatic_standard_factory` base, tooltip, and blocked localisation triplet remains the player-facing cost contract. It was added by the prior DM-62 cost-disclosure repair and already reads the same light-factory constant used by the modifier.

## Before and after behavior

Before this repair, DM-62 displayed and reserved one civilian factory but its availability/custom-cost trigger was `can_pay_independence_wave_diplomatic_standard_cost`, which did not test factory capacity.

After this repair, the decision cannot be selected or shown as affordable unless the existing light factory threshold, command-power threshold, and convoy-or-train material branch all pass. The decision still reserves the same light factory, pays the same diplomatic helper, runs for the accepted 45-day rapid duration, and issues the same target-specific 365-day authorization.

No duration, target, success, failure, cleanup, AI score, or authorization-consumption behavior changed.

## Threshold rationale

The helper uses the repository's established strict factory convention: `num_of_civilian_factories_available_for_projects > constant:independence_wave_decision_cost.civilian_factory_light`. Existing Event 006 administration helpers and FORM-03 project helpers use the same strict comparison for factory reservations. The decision modifier remains the existing light tier; no new tuning literal was introduced.

The strict comparison protects the reserved factory burden rather than allowing the decision to start with no spare project capacity. The dynamic localisation still reports the configured light factory quantity.

## Localisation and lifecycle

The existing factory-aware triplet is present in `localisation/english/006_independence_wave_decisions_l_english.yml`:

- `independence_wave_cost_diplomatic_standard_factory`
- `independence_wave_cost_diplomatic_standard_factory_tooltip`
- `independence_wave_cost_diplomatic_standard_factory_blocked`

The DM-62 target root, 45-day timer, 365-day authorization, cancellation deltas, active-target cleanup, matching-declaration consumption, and unrelated-offensive-war breach behavior are unchanged.

## MCP and probability evidence

Post-change `hoi4.probability_inspect` with adapter `decision_ai_will_do` returned `PROBABILITY_SOURCE_INSPECTED`:

- source revision: `69674fca1fad30844861043bc0ca520b6ce4dbcb035fccbf58ab23e89761cf06`
- source hash: `6d43da33d1620d5ae334684e850c2a46009885608141cba83ddbd491aed7d02f`
- 10 candidates, 0 available under the empty fixture, 78 required inputs, 0 inspect-unresolved rows, `poolComplete=false`
- artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a9f9b206391ef70343bd6071088c5a36c02ee241b32e987164d0d37e211e7589/c640678fc47d755c59764b0f46f8bd42051db60780626c86a872250ff6e173c8/probability-inspect-6d43da33d162.json`

A same-path current/current capability comparison was also produced with named scenario `E6_DM62_EMPTY_2026_08_15`:

- analysis: `probability-e7af4ba63b6e6e0ca7027185`
- scenario hash: `7b1244ff13201703f142dfc1afbafe318be09055a26f2361a6f25c4f4aacf351`
- 1 scenario, 10 candidates, 2,830 unresolved items, 8 empty-fixture diagnostics, `comparisonChanges=0`
- JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/66ab0174108f99bacf5097270d4db0f896685cc9913cf18553f46cc2cd82f52b/4aabcc743e934f20e9098e47f576b4fb78c56b48a7482b4f41346c0f0896ad42/probability-e7af4ba63b6e6e0ca7027185.json`

The MCP input schema rejected the pre-change inspect artifact URI as `before` (`expected object, received string at before`). Therefore no true snapshot-backed pre/post probability delta is claimed. The current/current receipt is capability evidence only; the empty fixture cannot prove ranking, timing, starvation, or balance.

## Validation

- The new scripted trigger definition appears once.
- DM-62 references the factory-aware helper in both `available` and `custom_cost_trigger`.
- The light factory modifier and factory-aware localisation selector remain in the same DM-62 block.
- `git diff --check` is clean for both changed source files.
- The scoped diff contains only the two DM-62 selector replacements and the new helper block.

## Remaining limits

Event 006 remains HOLD / PARTIAL at 40 adapters, 32 content attestations, 29 compatible reservation groups, and 161 unattested selectable rows. This repair changes no admission or Join surface. Live campaign/save-load validation and a fully typed probability fixture remain outside the available MCP evidence boundary.
