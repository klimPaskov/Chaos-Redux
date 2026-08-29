# Policy Consumer and Closed-Border Rejection Handoff

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

## Scope and ownership

This bounded patch updates only the destination-selection, relief, and spontaneous-movement helper surfaces owned by this subagent. It does not edit decisions, the shared core famine/migration effects or triggers, capacity, corridor, persecution, presentation, mapmode, GUI, localisation, workbook, assets, or on-actions.

Changed source files:

- `common/scripted_triggers/famine_migration_destination_selection_triggers.txt`
- `common/scripted_effects/famine_migration_destination_selection_effects.txt`
- `common/scripted_triggers/famine_migration_relief_triggers.txt`
- `common/scripted_effects/famine_migration_relief_effects.txt`
- `common/scripted_effects/famine_migration_spontaneous_movement_effects.txt`

Documentation files:

- `common/scripted_effects/famine_migration_destination_selection_effects.md`
- `common/scripted_effects/famine_migration_spontaneous_movement_effects.md`
- `common/scripted_effects/famine_migration_relief_effects.md`
- This handoff.

No new script constants were needed. Existing `famine_migration_destination_selection_runtime.zero/one`, `famine_migration_runtime.zero/one`, policy enum values, and source enum values are used.

## Helper map

| Identifier | Scope | Inputs | Outputs | Side effects | Call sites |
| --- | --- | --- | --- | --- | --- |
| `famine_migration_destination_selection_border_admissible` | State trigger | Candidate owner reception policy and forced-return pending flag | Foreign admission boolean | None | All foreign destination candidate branches |
| `famine_migration_destination_selection_reception_policy_blocks_admission` | State trigger | Candidate owner `famine_migration_reception_policy` | Exact blocking-policy boolean | None | Closed-border prepass and receipt revalidation |
| `famine_migration_destination_selection_foreign_policy_rejection_candidate_is_valid` | State trigger | Adjacent state, saved origin, actor target, normal safety, route, owner/controller, war, capacity, and policy facts | Otherwise-valid foreign blocker candidate boolean | None | The bounded prepass |
| `famine_migration_destination_selection_preflight_closed_border_rejection` | State effect | Origin state and chain-local actor target | Temporary candidate count/result and regular destination/actor targets only for exactly one candidate | Adjacent `every_neighbor_state` proof pass only | `famine_migration_process_spontaneous_movement_owner` before normal selection |
| `famine_migration_spontaneous_movement_record_closed_border_rejection` | State effect | Failed selector result, unique prepass proof, request, flight generation, and regular targets | Durable exact rejection receipt | Writes receipt variables once per generation; no population/death/Condemnation side effect | Spontaneous owner after the trap path |
| `famine_migration_relief_recipient_is_valid` policy gate | State trigger | Recipient owner reception policy | Recipient admission boolean | None | Existing relief donor candidate and availability contracts |

## Authoritative policy behavior

Foreign destination admission now calls the existing decision-owner trigger `famine_migration_decision_reception_policy_allows_admission`, which requires a valid `famine_migration_reception_policy` and accepts only humanitarian-open, controlled, transit-only, or quarantine values. Missing or malformed reception policy therefore fails closed. The derived `famine_migration_border_policy` is not consumed by destination admission or relief policy gates.

The three existing persecution humanitarian overrides in relief relation/route/selection predicates now validate the authoritative reception variable and require `humanitarian_open`. Recipient relief validity also requires `famine_migration_decision_reception_policy_allows_admission`. This is a recipient admission gate. Donor state registration remains a supply-side stock contract and does not use a receiving-policy gate, so a donor's own border posture cannot silently suppress its stock from the relief registry.

The existing decision-owner initialization helper remains responsible for legacy backfill. This patch does not infer an open policy from an absent value and does not change the initialization contract.

## Closed-border prepass formula and gates

The prepass runs only from the spontaneous movement origin state and only through `every_neighbor_state`. It does not use `every_state`, `every_country`, distant geometry, or a mapmode.

For each adjacent candidate, `famine_migration_destination_selection_foreign_policy_rejection_candidate_is_valid` requires:

- valid state and safe food stage;
- live transport, undamaged railway threshold, and recent-bombing threshold;
- no food-security, famine, catastrophic, persecution, bombing, trapped-population, camp, contamination, fallout, or plague hazard;
- candidate infrastructure and saved-origin infrastructure above the existing route threshold;
- a valid foreign owner, owner control of the candidate, and controller not at war with the actor;
- candidate reception capacity and load headroom;
- no forced-return pending flag;
- a valid authoritative reception policy whose value is `closed`, `violent`, or `forced_return`.

The effect initializes a temporary count at `constant:famine_migration_destination_selection_runtime.zero`, adds one per qualifying adjacent candidate, and saves the exact candidate state and owner only when the count equals `constant:famine_migration_destination_selection_runtime.one`. The prepass has no weight or random draw.

The normal selector runs immediately after the prepass. A successful internal or foreign selection suppresses rejection attribution. If it returns no destination, the owner calls the existing trap helper and then records attribution only when the unique prepass proof and target revalidation still hold.

## Receipt, conservation, and no-debit proof

`famine_migration_spontaneous_movement_record_closed_border_rejection` writes:

- `famine_migration_spontaneous_rejection_receipt_proven = one`;
- source `constant:famine_migration_pressure_source.cross_border_flight`;
- blocker policy value copied from the exact rejecting owner's `famine_migration_reception_policy`;
- blocker-policy proof flag;
- exact requested people amount;
- origin state id, rejecting destination state id, rejecting owner id, and origin owner id;
- `famine_migration_flight_request_generation` as the receipt generation;
- `global.date` as the transaction id.

The helper first checks the prepass result, regular targets, positive request, positive generation, candidate validity, policy blocker, and destination-owner/actor identity. It does not call `famine_migration_transfer_civilians_exact`, `add_manpower`, a Deaths writer, or a Condemnation adapter. The existing `famine_migration_spontaneous_movement_trap_request` remains the only failed-selection effect and adds only `max(request - existing_trapped_population, 0)` to the trapped ledger. Population authority, cohort history, survivor credit, and deaths are untouched.

If the same state is replayed for the same flight generation, the receipt remains unchanged. A later generation may write a replacement exact receipt. Multiple, zero, malformed, or independently invalid candidates remain trapped but unattributed. No synthetic hosted-cohort trap is created, and no rejection receipt is written for an ordinary transfer failure after a destination was selected.

## Event-target and cleanup plan

The prepass uses regular chain-local targets `famine_migration_spontaneous_closed_border_destination` and `famine_migration_spontaneous_closed_border_actor`. They are saved only for the unique-candidate branch and clear with the effect chain. They are not global targets and are not stored as durable scope-valued variables.

The existing spontaneous cleanup still clears destination-local selector proof variables through `famine_migration_route_destination` on every owner exit. The selector actor override is reset after the prepass and normal selection. No new recurring hook or whole-world cleanup is added. The durable receipt stores ids and scalar facts only, so stale event-target pointers cannot survive a save/reload.

## Weighted surfaces and balance preservation

No numeric weight or balance target was changed. The destination weight effect retains the existing terms and uses the reception-policy value for valid foreign candidates. The prepass is unweighted. The relief weight effect retains all terms and only changes the persecution override's source variable to reception policy.

Weighted surfaces touched or gated for later same-scenario baseline/post-change auditing:

- `prob_destination_selection_internal`;
- `prob_destination_selection_persecution`;
- `prob_destination_selection_donor`;
- `prob_cleanup`;
- `prob_relief_donor`.

The required first `hoi4.probability_inspect` call was made before weighted analysis. A current source inspection was also run against `common/scripted_effects/famine_migration_destination_selection_effects.txt` with adapter `custom_weighted_pool` and the five named surfaces. It returned `PROBABILITY_SOURCE_INSPECTED`, `poolComplete=false`, `candidates=0`, `unresolved=5`, source revision `9892314c0125886aae1c1146181d8c6f850adb162ecfb5fff317935e0a5572a7`, source hash `81e52df99ba485ecca76587fcc74db6d019b96165a02e7fcbc239f84e43668fd`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f93b5147e3b1de01d2db893f3b6563d784bccd663e65d21f1ee8fbff9c86294e/438ddffce1d3eb63fd165aec60b503241eb889cb85a2f86c6032c4570c686cfa/probability-inspect-81e52df99ba4.json`. The named `chaosx_ai_probability_auditor` route is not exposed in the current callable tool registry. Therefore the independent baseline/post-change auditor comparison, scenario evaluation, sweep, sequence, and rendered evidence remain blocked and are not claimed here. Existing pre-override source artifacts in the spontaneous and relief handoffs are not post-change engine evidence.

The existing destination-selection handoff also records a prior narrow map-inspection artifact and its `ARTIFACT_STORAGE_LIMIT` blocker. This patch does not modify map data or mapmodes, so no new map route was required.

## Condemnation adapter boundary

The current Condemnation adapter accepts fixed source type, gain, visibility, severity, optional deaths, contamination, victim country, and context fields. It does not accept this patch's exact actor, policy-cause, generation, and transaction receipt contract. No Condemnation wrapper is called. The durable receipt is the owner handoff for a future compatible adapter, and existing humanitarian, diplomatic, security, and political consequences remain with their current owners.

## Validation and remaining risks

Targeted source checks covered helper-name references, policy-variable consumers, `check_variable` forms in touched blocks, balanced Clausewitz braces, and the final diff. The required offline wiki pages, vanilla effect/trigger/script-constant documentation, repository skills, and current owned source were reviewed. No live Hearts of Iron IV process was launched.

Remaining risks are the unavailable independent probability-auditor route, the lack of a compatible Condemnation exact-receipt adapter, and the need for parent-owned final integration/live consumer validation. The prepass intentionally duplicates the normal candidate safety boundary. If future destination safety gates change, both predicates must be reviewed together.
