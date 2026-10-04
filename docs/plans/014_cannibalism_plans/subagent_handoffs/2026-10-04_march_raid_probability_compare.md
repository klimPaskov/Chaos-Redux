# Event 014 March raid same-scenario probability comparison

Date: 2026-10-04.
Disposition: `implemented` for the comparison step of the March raid change; candidate-pool coverage remains `unresolved`.

## Request

- Route: `hoi4.probability_compare`, adapter `decision_ai_will_do`, candidate `cannibalism_march_raid_supply_depot`.
- Before: frozen snapshot `subagent_handoffs/2026-10-04_actual_raid_target_owner_proposal/evidence/current_source_snapshot/common/decisions/014_cannibalism_decisions.txt`, SHA-256 `ad356db7875965262a049bcdc858499193ee5c2163dc1c736aa066c063d279d3`, byte-identical to the pre-change working copy.
- After: the live `common/decisions/014_cannibalism_decisions.txt` with the state-targeted decision.
- Scenario set `event014_march_raid_supply_depot_costs_satisfied` with the baseline scenario IDs `event014_march_raid_supply_depot_peace_costs_satisfied` and `event014_march_raid_supply_depot_war_costs_satisfied` (actor `CBA`, March origin, March actions and event-created warlord flags, `has_war` false and true).

## Result

`PROBABILITY_ANALYZED_PARTIAL`, analysis `probability-9d7b70c3ca9313c55ca0e3e3`, scenario hash `41db2792b632c3c0564faf21cac0027441b6c29ba8b1072339b68488f7cea3e7`, source revision `83220c2457caefaa3e05666f5e6d3f288392a9721bac337e9c70dd7829d75d16`.
`comparisonChanges = 0`, no regressions, adapter and assumptions unchanged.
Both sides report the candidate ineligible because the scenario cannot declare `exists`, `has_capitulated` and the other command-gate inputs (7 unresolved items), the same input-binding gap the pre-change baseline attempt recorded.
The AI expression (base `constant:cannibalism_decision_ai.high`, `urgent_factor` at war) is unchanged, so the prior raw scores 60 in peace and 150 at war still describe the willingness score.

## Limits

The adapter does not enumerate the new per-state target pool, so no statement about which states the AI picks is made.
The Host-wide cooldown keeps the number of strikes per period at the pre-change cadence; AI target choice among valid hubs is engine-native and needs live observation.
