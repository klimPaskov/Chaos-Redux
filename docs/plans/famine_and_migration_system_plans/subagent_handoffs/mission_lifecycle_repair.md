# Famine and migration mission lifecycle repair handoff

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

## Scope and outcome

This handoff covers the decision-owner repair of the famine and migration mission surface. The owned decision source now defines exactly six non-selectable missions, each tied to one exact state subject and one owner-country active flag. The former immediate-success `uses_normal_civilian_systems = yes`-only behavior is removed from every mission; `available` now requires an earned proof, a live subject, and a bounded deadline.

No event ID, event-pool registration, pacing pulse, recurring world scan, shared scripted GUI, fake route selector, fixed historical total, third mapmode, or ordinary-decision AI-weight change was added.

## Files owned by this handoff

- `common/decisions/famine_migration_decisions.txt`
- `common/script_constants/famine_migration_mission_constants.txt`
- `localisation/english/famine_migration_missions_l_english.yml`
- `docs/plans/famine_and_migration_system_plans/subagent_handoffs/mission_lifecycle_repair.md`

The existing category, shared scripted effects and triggers, mapmodes, report effects, GUI sources, workbook, on-actions, and existing `famine_migration_l_english.yml` were not edited by this owner. The reserve-ledger implementation remains parent-owned at commit `9627b8bad` and is consumed only through its published APIs.

## Lifecycle proof table

| Mission | Exact activation subject and producer | Earned success proof and available gate | Timeout and cleanup |
| --- | --- | --- | --- |
| `fm_mission_secure_relief_route` | A successful `fm_repair_relief_route` transaction marks one owned and controlled state with `famine_migration_mission_route_subject`, a hold deadline, and the owner flag `famine_migration_mission_route_active`. | A later accepted reserve relief transaction marks `famine_migration_mission_route_success_proven`. The route must no longer be damaged and the global date must reach the hold deadline. | `repair_route_timeout` is bounded in `famine_migration_mission_timing`; success and timeout use `famine_migration_mission_outcome`. Completion, timeout, and cancellation clear the subject, proof, deadline, and owner flag. |
| `fm_mission_hold_humanitarian_corridor` | `fm_negotiate_corridor` requires a trapped cohort, a non-ambiguous cohort id, and a controlled state adjacent to a controller at war with ROOT. Its successful corridor transaction persists the exact state subject, cohort id, and owner flag `famine_migration_mission_corridor_active`. | One of the existing exact civilian-transfer decisions must return a valid transfer and positive survivor credit. The same origin subject then consumes the actual debit, clears the trapped cohort population, and sets `famine_migration_mission_corridor_success_proven`. Available also requires live hostile-front adjacency and a safe route. | `secure_corridor_timeout` is bounded. Success alone calls `famine_migration_achievement_record_corridor_completed`; timeout/cancel do not. Every terminal path clears the subject, proof, cohort id, and owner flag. An authoritative attack/control callback is still required; see blockers. |
| `fm_mission_protect_evacuation_transport` | `fm_famine_evacuation`, `fm_evacuate_vulnerable`, and `fm_evacuate_workers` arm one exact origin state only after `famine_migration_record_displaced_cohort` and the exact transfer return a valid result with positive survivor credit. The state stores the cohort id, deadline, subject flag, and owner flag `famine_migration_mission_evacuation_active`. | `fm_distribute_arrivals` must return a valid positive reception delta. The origin subject then receives `famine_migration_mission_evacuation_success_proven`; the route must remain safe through the deadline. | `protect_evacuation_timeout` is bounded. All terminal paths clear subject, proof, cohort id, deadline, and owner flag. No second civilian movement is performed by the mission. |
| `fm_mission_deliver_relief_before_reserves_fail` | The first accepted release, import, convoy, airlift, or requisition reserve transaction creates one named state subject, deadline, reserve amount proof, and owner flag `famine_migration_mission_relief_active`; a later accepted transaction on that same subject marks success. | The transaction must return the valid result code and an accepted output above `minimum_relief_grant`. Available requires the success proof, date at or after the deadline, remaining reserve above `minimum_reserve_after_relief`, and food pressure below `maximum_success_food_pressure`. No fabricated starting reserve is used. | `deliver_relief_timeout` is bounded. Success and timeout outcomes come from constants. Subject, success proof, deadline, and owner flag are cleared on completion, timeout, and cancellation. |
| `fm_mission_prevent_reception_collapse` | `fm_controlled_medical_reception` only establishes the controlled quarantine/capacity policy flag. It does not record the medical achievement. After an exact positive reception delta, `fm_distribute_arrivals` requires `event_target:famine_migration_cohort_origin = { black_plague_state_is_infected = yes }`, then creates the exact destination state/cohort subject, observation-pending flag, deadline, and owner flag. Only this positive exposed-cohort reception path calls `famine_migration_achievement_record_medical_reception`. | Available requires the same owned/controlled subject, pending observation, reception context, capacity and load values, no overload, no observation breach, no state infection, load below capacity, and date at or after the observation deadline. A breach or current infection/overload cancels rather than merely hiding the success predicate. | `prevent_reception_timeout` is bounded. The breach cancel path permanently sets `famine_migration_mission_reception_observation_breach`, applies the timeout consequence, calls `famine_migration_achievement_record_medical_reception_failure`, clears all subject/pending/breach/cohort/deadline state, and clears the owner flag. The timeout path applies the same outcome and cleanup. The parent still needs to add the timeout callback line if the live decisions file remains write-locked when this handoff is committed. |
| `fm_mission_prepare_safe_return_route` | After `fm_voluntary_return` completes one valid exact civilian transfer, validates the state return projection, and returns positive survivor credit, the destination state stores the return subject and deadline with `famine_migration_return_context_active` and owner flag `famine_migration_mission_return_active`. | Available requires the exact return context, live safe route, no active food-security failure, and date at or after the observation deadline. The subject is therefore evidence of a real return transaction, not a selectable checklist. | `prepare_return_timeout` is bounded. Completion, timeout, and cancellation clear subject/deadline and owner flag. The existing exact return transaction remains the only movement; the mission observes its post-return safety window. |

## Reserve and transaction APIs consumed

The decision source consumes the parent ledger contracts `famine_migration_release_food_reserves`, `famine_migration_import_food_reserves`, and `famine_migration_requisition_food_reserves`. Release and convoy/airlift paths gate relief and mission proof on `famine_migration_food_reserve_consume_result = constant:famine_migration_route_result.valid` plus `famine_migration_food_reserve_consume_relief_granted_output > constant:famine_migration_mission_contract.minimum_relief_grant`. Import gates on the corresponding add result and accepted output. Requisition gates on `famine_migration_food_reserve_transfer_result` and `famine_migration_food_reserve_transfer_destination_credit_output`, while the donor pressure adjustment uses the actual accepted destination credit divided by the saved requested amount.

Movement paths call the existing exact civilian transfer once and use its returned actual origin debit, survivor credit, and result. Reception and return mission arming additionally require valid reception-delta and state-return-projection results. No movement path treats route deaths as a second population debit.

The parent report selectors are called only after their qualifying proof: closed-border after a valid trapped-cohort registration, wartime evacuation after a valid organized transfer, relief arrival after an accepted reserve result, and return after a valid voluntary return and projection.

## Parent callbacks and unresolved contracts

1. The parent should expose a bounded `famine_migration_mark_reception_observation_breach` contract in the authoritative infection/reception owner. Its state input is the exact state carrying `famine_migration_mission_reception_subject`; it should set `famine_migration_mission_reception_observation_breach` when `black_plague_state_is_infected` becomes true or reception load reaches/exceeds capacity while `famine_migration_mission_reception_observation_pending` is set. The contract must call or lead to `famine_migration_achievement_record_medical_reception_failure` and must not clear the breach when infection or overload later recedes. The mission also has a direct cancel trigger for a persistent current infection/overload as a fail-closed safety net.

2. The parent needs an authoritative `on_state_control_changed` or equivalent route-owner callback for corridor invalidation. When the exact corridor state loses ROOT ownership/control, loses the hostile-front adjacency proof, or suffers an authoritative route attack, the callback must set the corridor failure/disqualifier and clear the owner/state subject. No corridor attack evidence is fabricated by this decision owner. The same callback family should clear or invalidate state subjects when ownership/control is lost outside the mission tick.

3. `famine_migration_achievement_record_medical_reception_failure` is a parent-owned country-scope API already present in the shared achievement effects. This owner calls it from the reception breach cancellation path. If the final parent merge retains a separate timeout path without the new failure call, add that exact call before timeout cleanup; otherwise stale exposed/controlled proof could survive into an unrelated durable-outcome check.

## AI, probability, and route-lock disposition

All 26 ordinary decision IDs remain present. Their existing `ai_will_do` blocks and weights were preserved; no mission AI block, weight, factor, MTTH, random pool, or weighted target was changed. The mandatory probability auditor baseline/compare route was therefore not invoked for this patch, because no weighted surface changed. Parent review must still use the existing probability artifacts for any later AI-weight edit.

Player and AI use the same ordinary decisions to create mission subjects. Front adjacency, ownership/control, cohort ambiguity, route safety, reserve result codes, and actual accepted amounts are shared validity gates. No human-only mission gate was added.

## GUI, cognitive load, costs, and localisation

The mandatory read-only GUI inspection used `decision_view` with scenario `famine_migration_category` at workspace `mod_chaos_redux_ea3b2d67c2c0`. It returned `GUI_INSPECTED` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0ae8754d323a796d44bc82ba59d6e218943a743918e00c29c87d47b9a13123e1/7fe6be1556d94c699cd60071d0009ddb8dcc8de334e78862021b5fe7428690ac/gui-inspect.92e67796f2fc1c0b.json`. The source graph was complete but the aggregate result was dominated by unrelated repository-wide symbol collisions/truncation; the decision window itself was approximated with zero modeled elements. The required read-only render was attempted for normal, active, warning, long-text, and missing-localisation states at 1920x1080 and 1280x720 and returned `INTERNAL_ERROR` with no artifact. These are tooling/fidelity blockers, not evidence of a GUI rewrite or a new decision GUI. No GUI rewrite was performed.

Six simultaneous non-selectable missions are the maximum primary objective count, with one persistent exact subject per family and no extra mission tab or category. Their values have clear significance: named subject state/cohort, earned transaction proof, deadline, route/control lock, reserve output, reception load/capacity, and outcome consequence. Existing ordinary decision costs were not changed and no mission cost was introduced. New player-facing names, descriptions, success/failure text, and concise requirement tooltips are in the new BOM-encoded localisation file; the original localisation file remains untouched.

## Validation performed

- The six mission IDs are exactly `fm_mission_secure_relief_route`, `fm_mission_hold_humanitarian_corridor`, `fm_mission_protect_evacuation_transport`, `fm_mission_deliver_relief_before_reserves_fail`, `fm_mission_prevent_reception_collapse`, and `fm_mission_prepare_safe_return_route`.
- The ordinary decision ID comparison is 26 before and 26 after, with no ID removed.
- The decision source has balanced braces and no event declaration, event ID, pacing on-action, scripted GUI binding, or third mapmode addition in this patch.
- The mapmode source still contains exactly `famine_state_map_mode` and `migration_state_map_mode`.
- All six mission base names/descriptions/success/failure keys resolve across the existing and new localisation files. The new localisation is UTF-8 with BOM and contains no `:0` keys.
- Reserve call sites gate on the published result codes and accepted output variables rather than decision selection or fixed historical totals.
- No `ai_will_do` block changed in the owned decision diff.

Live gameplay, save/load, and user consumer validation were not run under repository policy. The GUI render blocker and the parent callbacks above remain open; this handoff does not claim overall famine/migration system completion.

## Simplifications, omissions, and blockers

- The authoritative corridor attack invalidation producer is not available to this owner and is deliberately not fabricated.
- The durable reception breach callback is parent-owned. The decision surface has a persistent breach flag, direct fail-closed cancellation, country achievement failure call, and exact cleanup, but the authoritative infection/reception transition must still call the parent contract.
- The return objective is armed by the existing exact voluntary-return transaction and then observes its safe settlement window; no separate pre-return route-construction decision was invented because ownership is limited to the existing 26 ordinary decisions.
- The current decisions-file write lock prevented adding one final duplicate failure call to the reception `timeout_effect` after the cancellation call was applied. The parent should add that one line before final merge if it is not already present.
- GUI render produced no current artifact, and the inspect artifact reports repository-wide graph collisions/truncation; no visual acceptance claim is made.
- No other simplification, fallback, hardcoded historical total, event carrier, recurring world scan, or probability change was introduced.

## Parent review disposition

The parent accepted all six mission families and retained all 26 ordinary decisions. The parent added the missing medical-reception timeout failure call, wired an exact registered-state observation breach for infected-or-worse Black Plague phases and reception overload, registered exact receiving states for that bounded observation, and added state-control subject cleanup without treating control change as proof that a corridor was attacked.

The parent also rejected the handoff's statement that six missions could be simultaneous because Part 6 caps urgent missions at three. A centralized country slot ledger now permits no more than three active family flags, and every terminal mission path recounts the live flags. The authoritative corridor-attack producer remains unresolved and is not fabricated.
