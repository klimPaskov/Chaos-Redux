# Humanitarian Corridor Contract Architecture Handoff

Status: design-only handoff for the bounded replacement of `fm_negotiate_corridor`.

Scope: this handoff proposes the smallest authoritative contract that can prove an exact origin state, adjacent cross-front state, counterpart country, route geometry, response, operation, expiry, and cleanup without adding an event, event-pool entry, third mapmode, global target registry, or global periodic scan.

No gameplay files were edited.

## Decision

`fm_negotiate_corridor` should remain an ordinary state-targeted decision in `common/decisions/famine_migration_decisions.txt`, but its completion should create a pending offer and never debit trapped population, credit destination manpower, set a successful border policy, or arm the old mission directly.

The selected `FROM` state is the authoritative origin scope.

The counterpart is derived only from an exact adjacent front state whose controller is at the allowed relation with `ROOT`.

If the current UI leaves more than one valid adjacent front candidate, the helper must fail closed with a selection-ambiguity flag instead of choosing a random neighbor or an arbitrary country.

Acceptance is represented by two ordinary country decisions in the existing `chaosx_famine_migration_category`: `fm_accept_corridor_offer` and `fm_reject_corridor_offer`.

Acceptance changes contract state only; relief and evacuation are separate exact transactions after acceptance.

The existing `famine_migration_transfer_civilians_exact` contract remains the only population movement endpoint, and `famine_migration_transfer_food_reserves` remains the only reserve movement endpoint.

The old quarter-relief arithmetic in `fm_negotiate_corridor.remove_effect` must be removed by the parent implementation because it is an unproven debit that can be lost or duplicated.

The existing weighted destination selector remains valid for non-corridor evacuation and fallback decisions, but it must not override an accepted corridor's persisted exact front destination.

Exactly two mapmodes remain in scope: `famine_state_map_mode` and `migration_state_map_mode`.

## Authoritative data model

Persistent pointers should be normal variables containing database IDs, not global event targets.

The offline Data structures page documents variables holding database IDs and `var:` scope/target use, while global event targets are one globally shared name that persists until manually cleared.

This avoids collisions when more than one requester creates a corridor and keeps regular event targets limited to one exact transfer chain.

### Origin state scope

The origin state selected by `FROM` owns the contract and stores these normal variables:

- `famine_migration_corridor_status`.
- `famine_migration_corridor_origin_state_id`.
- `famine_migration_corridor_front_state_id`.
- `famine_migration_corridor_counterpart_country_id`.
- `famine_migration_corridor_requester_country_id`.
- `famine_migration_corridor_cohort_id`.
- `famine_migration_corridor_operation`.
- `famine_migration_corridor_relation`.
- `famine_migration_corridor_offer_deadline`.
- `famine_migration_corridor_mission_deadline`.
- `famine_migration_corridor_route_generation`.
- `famine_migration_corridor_origin_controller_id`.
- `famine_migration_corridor_front_controller_id`.
- `famine_migration_corridor_route_proof_generation`.
- `famine_migration_corridor_route_border_proof`.
- `famine_migration_corridor_route_transport_proof`.
- `famine_migration_corridor_route_safety_proof`.
- `famine_migration_corridor_route_actor_proof`.
- `famine_migration_corridor_route_ceasefire_proof`.
- `famine_migration_corridor_food_proof`.
- `famine_migration_corridor_reception_proof`.
- `famine_migration_corridor_actual_origin_debit`.
- `famine_migration_corridor_route_deaths`.
- `famine_migration_corridor_survivor_credit`.
- `famine_migration_corridor_relief_source_debit`.
- `famine_migration_corridor_relief_destination_credit`.
- `famine_migration_corridor_cleanup_reason`.
- `famine_migration_corridor_attack_reason`.
- `famine_migration_corridor_attack_date`.

The state owns the following flags for visibility and proof rather than using numeric booleans:

- `famine_migration_corridor_contract_active`.
- `famine_migration_corridor_offer_pending`.
- `famine_migration_corridor_accepted`.
- `famine_migration_corridor_operation_pending`.
- `famine_migration_corridor_mission_active`.
- `famine_migration_corridor_relief_proven`.
- `famine_migration_corridor_evacuation_proven`.
- `famine_migration_corridor_attack_disqualified`.
- `famine_migration_corridor_route_invalid`.
- `famine_migration_corridor_selection_ambiguous`.

The origin state remains the single source of truth for trapped population and the aligned cohort row.

The requester country may mirror `famine_migration_corridor_origin_state_id`, `famine_migration_corridor_front_state_id`, and `famine_migration_corridor_cohort_id` only to support sparse existing-country hooks and its mission-slot flag.

### Counterpart country scope

The counterpart country scope `var:famine_migration_corridor_counterpart_country_id` stores one bounded pending-offer mirror:

- `famine_migration_corridor_offer_pending`.
- `famine_migration_corridor_offer_origin_state_id`.
- `famine_migration_corridor_offer_front_state_id`.
- `famine_migration_corridor_offer_requester_country_id`.
- `famine_migration_corridor_offer_cohort_id`.
- `famine_migration_corridor_offer_operation`.
- `famine_migration_corridor_offer_deadline`.

The one-pending-offer-per-counterpart limit is intentional for the smallest implementation and prevents an unkeyed country decision from accepting the wrong origin.

Submitting a second offer to a counterpart with an active pending mirror must fail closed.

If the engine cannot resolve `var:<database_id>` as a state or country scope after save/reload, that is an implementation blocker and must not be bypassed with a static global target name.

### Transaction-local targets

During an exact movement chain, save the origin as regular `famine_migration_transfer_origin` and the persisted front state as regular `famine_migration_route_destination` before calling the existing transfer helper.

Regular event targets must be cleared by the existing route-request cleanup path and must never be the durable corridor registry.

No `save_global_event_target_as` is needed for this contract.

## Lifecycle state machine

`idle` -> `prepared` -> `offer_pending` -> `accepted` -> `operation_pending` -> `mission_active` -> `completed`.

`offer_pending` -> `rejected` on an explicit counterpart rejection.

`offer_pending` -> `expired` when its response deadline elapses without a response.

`prepared`, `offer_pending`, or `accepted` -> `invalidated` when exact state, controller, adjacency, relation, route proof, destination safety, or counterpart validity fails.

`accepted`, `operation_pending`, or `mission_active` -> `disqualified` only when an authoritative attack owner supplies an exact corridor attack receipt.

`accepted`, `operation_pending`, or `mission_active` -> `expired` on the operation or hold deadline.

Every terminal branch calls one idempotent cleanup effect.

Pending rejection, expiry, and invalidation leave trapped population and reserves unchanged.

After a valid exact movement, cleanup leaves the transferred cohort at its actual credited host and leaves any untransferred trapped remainder in the origin state.

Cleanup must never restore a debit or subtract a second arrival merely because a later route or control proof fails.

## Helper map

The following names are the proposed narrow contracts and their intended call sites.

| Helper | Scope | Inputs | Outputs | Side effects | Call sites |
|---|---|---|---|---|---|
| `famine_migration_corridor_origin_is_valid` | origin state | current cohort, trapped amount, controller, active flags | trigger | none | `fm_negotiate_corridor`, response/operation guards |
| `famine_migration_corridor_front_candidate_is_valid` | candidate neighbor state | origin ID, requester ID, relation mode | trigger | none | preparation enumeration |
| `famine_migration_corridor_front_state_is_valid` | origin state | stored front and counterpart IDs, route generation | trigger | none | every response, mission, transaction, and hook revalidation |
| `famine_migration_corridor_route_geometry_is_valid` | origin state | exact front, adjacency, controller snapshots, border/transport/safety/actor proofs | trigger | none | preparation, acceptance, operation, hold mission |
| `famine_migration_corridor_offer_is_valid` | counterpart country | mirrored IDs, deadline, relation, route proofs | trigger | none | `fm_accept_corridor_offer`, `fm_reject_corridor_offer` |
| `famine_migration_prepare_corridor_contract` | origin state | optional explicit front-state ID, operation, relation | preparation result and persisted IDs/proofs | sets `prepared` data only; no population/resource mutation | `fm_negotiate_corridor.complete_effect` |
| `famine_migration_submit_corridor_offer` | origin state then counterpart country | prepared IDs, response deadline | offer result | sets pending flags and country mirror; no population/resource mutation | `fm_negotiate_corridor.complete_effect` |
| `famine_migration_corridor_accept_offer` | counterpart country | pending mirror and exact origin/front IDs | acceptance result | marks origin accepted and counterpart response; no population/resource mutation | `fm_accept_corridor_offer.complete_effect` |
| `famine_migration_corridor_reject_offer` | counterpart country | pending mirror and exact origin/front IDs | rejection result | marks rejection and calls cleanup; no population/resource mutation | `fm_reject_corridor_offer.complete_effect`, guarded timeout removal |
| `famine_migration_execute_corridor_relief` | origin state with front-state source | accepted contract, exact reserve source, route proofs | source debit, destination credit, result | calls existing exact reserve transfer and marks relief proof only on balanced success | relief/convoy operation branch |
| `famine_migration_execute_corridor_evacuation` | origin state | accepted contract, exact cohort, front destination, requested amount, route proofs | actual debit, deaths, survivor credit, conservation result | calls `famine_migration_transfer_civilians_exact` once; subtracts trapped only after valid return | accepted branches of `fm_famine_evacuation`, `fm_evacuate_vulnerable`, and `fm_evacuate_workers` |
| `famine_migration_mark_corridor_attack_disqualified` | origin state | exact origin/front, attacker, attack reason/date, authoritative attack receipt | disqualification result | owns status/flag transition and cleanup; does not infer the attack | combat/front/air/nuclear owner callback, once available |
| `famine_migration_corridor_finalize` | origin state | completed operation and hold proof | completion result | outcome/achievement effects and cleanup | `fm_mission_hold_humanitarian_corridor.complete_effect` |
| `famine_migration_corridor_expire` | origin state | current status and deadline reason | expiry result | terminal status and cleanup; preserves completed transfers | mission timeout/cancel and sparse invalidation hooks |
| `famine_migration_corridor_cleanup` | origin state or counterpart country | IDs, terminal reason, transaction outputs | cleanup result | clears flags, mirrors, slot/legacy mission fields, deadlines, proofs, and one-shot route variables idempotently | every terminal path and control-change handler |

The private scripted source belongs in `common/scripted_effects/chaosx_famine_migration_effects.txt` and `common/scripted_triggers/chaosx_famine_migration_triggers.txt`.

The new helpers must be documented in the matching section of `common/scripted_effects/chaosx_dynamic_effects.md` only if a helper becomes a cross-subsystem dynamic contract; corridor-private helpers should be documented in a famine/migration helper document rather than added to the shared dynamic namespace.

## Exact preparation and counterpart proof

`famine_migration_prepare_corridor_contract` runs in the selected origin state and first requires `famine_migration_corridor_origin_is_valid`.

When an explicit front-state ID is supplied, it must pass `famine_migration_corridor_front_candidate_is_valid` and the stored route proof must be generated from that exact state.

For the current state-targeted UI, enumerate valid adjacent candidates with `every_neighbor_state` and count them using the existing ambiguity pattern used by cohort reconciliation.

Exactly one candidate persists `famine_migration_corridor_front_state_id` and its controller ID.

Zero candidates set `famine_migration_corridor_route_invalid` and return invalid.

More than one candidate sets `famine_migration_corridor_selection_ambiguous` and returns invalid rather than using `random_neighbor_state`, an arbitrary `any_neighbor_state`, or a hidden weighted route.

The front state must be distinct from the origin state, adjacent to it, controlled by the persisted counterpart, and still satisfy the selected relation mode.

The route proof bundle must include state validity, adjacency, controller snapshot, border opening/permission, transport or rail/port capacity, route safety, actor/ceasefire proof, and destination food/reception proof as required by the selected operation.

`has_war_with` is only a relation input and is not sufficient proof of exact geometry, acceptance, route safety, or attack.

The helper records the route generation and controller snapshots so a later control or route change invalidates the contract without searching the world.

## Response and operation contracts

`fm_accept_corridor_offer` and `fm_reject_corridor_offer` are ordinary country decisions in the existing category and have no event IDs, event targets, event-pool entries, or dedicated GUI.

Both decisions must require the same mirrored pending offer, exact IDs, deadline, and route proof.

The acceptance decision sets `accepted` on the origin and leaves trapped population, reserve stockpiles, and cohort rows untouched.

The rejection decision leaves trapped population and reserves untouched, records a rejection reason, and cleans all pending mirrors.

The pending response timeout is guarded by status so the decision's `remove_effect` cannot delete an already accepted contract.

If the category requires a famine phase flag before a child decision can surface, the offer submission helper may set a counterpart-only emerging/active visibility flag and cleanup must restore the prior phase; this requires engine validation and must not be assumed from source syntax alone.

The accepted mission `fm_mission_hold_humanitarian_corridor` should activate only for the exact accepted origin and requester contract.

Its available, cancel, complete, and timeout paths should call the exact front/route validators and the corridor finalize/expire helpers instead of the current generic subject plus any-enemy checks.

The mission is an operational hold objective, not the acceptance response.

`famine_migration_execute_corridor_evacuation` saves the exact front state as `famine_migration_route_destination`, sets a bounded request from the current trapped cohort, and calls `famine_migration_transfer_civilians_exact` exactly once.

Only a valid transfer result may subtract `famine_migration_transfer_actual_origin_debit` from both trapped variables, clamp at zero, clear the trapped flag at zero, update the cohort host/destination using existing bind helpers, and record corridor evacuation proof.

The corridor branch must bypass generic weighted destination selection and the generic evacuation mission for that transfer, while all non-corridor branches retain their existing weighted destination contract.

Route deaths remain outputs of the exact transfer helper and must be logged once by its existing death ledger path.

`famine_migration_execute_corridor_relief` uses the exact front/counterpart reserve source and the origin reserve destination through `famine_migration_transfer_food_reserves`.

It records relief proof only when source debit and destination credit are both positive and balanced under the existing reserve contract.

If an enemy front has no authoritative reserve donor or transport proof, relief fails closed rather than inventing a second stockpile or crediting the origin.

## Attack disqualifier ownership

The corridor helper owns the contract state transition, reason, cleanup, and preservation of already completed transfers.

The combat, front, strategic-bombing, or nuclear subsystem that has the authoritative attack receipt must own detection and call `famine_migration_mark_corridor_attack_disqualified` with exact origin state, exact front state, attacker, date, and reason.

The current `common/on_actions/chaosx_famine_migration_on_actions.txt` exposes state-control change and country war/peace reassessment hooks but no exact battle/front/attack callback.

`has_war_with`, `on_war_relation_added`, or generic state control loss must not be used as an attack substitute.

State-control loss can invalidate the route through `famine_migration_handle_state_control_change`, but it is not an attack death proof.

If no authoritative attack owner can be wired, the contract must fail closed on missing attack proof and the handoff must remain marked blocked for that acceptance criterion.

## Sparse hooks and cleanup

Extend `famine_migration_handle_state_control_change` and `famine_migration_cleanup_mission_subjects_after_control_change` to inspect only the exact state and its stored counterpart/front IDs.

Extend the existing `on_war_relation_added`, `on_peace`, and `on_peaceconference_ended` country reassessment paths to revalidate only a country whose stored corridor IDs match the changed relation.

Use the existing active displacement state/country registries for bounded deadline and revalidation jobs if an engine-supported scheduled job is required.

Do not add `on_daily`, `on_weekly`, `on_monthly`, or any other whole-world corridor scan.

`famine_migration_corridor_cleanup` must clear origin contract flags and IDs, counterpart mirrored flags and IDs, requester mission-slot/legacy corridor subject fields, deadlines, route proofs, attack/rejection reasons, and one-shot transfer targets.

Cleanup must be safe when called twice, when the counterpart is invalid, and when only one side of the mirror remains.

Cleanup must not clear aligned cohort rows or reverse actual population/reserve transactions.

The existing mission cleanup currently clears `famine_migration_mission_corridor_subject`, success, cohort, and slot fields; the new centralized cleanup must subsume that behavior rather than create a parallel stale-flag path.

## Constants and tuning table

Add a corridor-specific constants category in `common/script_constants/famine_migration_constants.txt` for status, operation, relation, and terminal reason IDs.

Add response and operation timing constants with explicit offer-response and accepted-hold deadlines.

Reuse `constant:famine_migration_decision_timing.decision_short` for the initial response timeout only if the acceptance audit confirms it is appropriate; otherwise add a named corridor response constant.

Reuse `constant:famine_migration_mission_timing.secure_corridor_timeout` for the hold window only if the existing mission semantics remain correct.

Retain `negotiate_corridor_base`, `negotiate_corridor_factor_1`, and `negotiate_corridor_factor_2` as the requester baseline until the mandatory probability audit supplies a balance decision.

Add named accept/reject AI base and factor constants for civilian danger, condemnation/observers, route value, military advantage/cost, food/reception capacity, ideology, route safety, and deadline pressure.

Do not put raw relief-quarter or arbitrary counterpart weights into the replacement; exact operation amounts must come from the existing transfer contracts and state/cohort variables.

## Probability surfaces and audit scenarios

The named baseline surface is `prob_corridor_acceptance` from `docs/specs/famine_and_migration_system_specs/famine_and_migration_system_probability_scenarios.csv`.

The candidate pool must include `fm_accept_corridor_offer` and `fm_reject_corridor_offer`, with `fm_negotiate_corridor` audited separately as the requester surface.

Required scenario inputs are requester country, origin state, exact front state, counterpart country, relation/war state, trapped amount, cohort cause, famine severity, route adjacency, route border/transport/safety/actor/ceasefire proofs, destination food/reception/capacity, observers, condemnation, war goals, military advantage/cost, ideology/relations, pending flags, and deadlines.

Expected result: both response weights are zero when geometry, counterpart, or deadline validity fails.

Expected result: acceptance exceeds rejection under high civilian danger, high condemnation/observer pressure, valid reception, and low military cost.

Expected result: rejection exceeds acceptance under high military advantage/cost, inadequate reception, unsafe route, or invalid policy.

Direct persecution and civilian safety must outrank ideology when both are present, following the ordering in Part 8.

Also sweep `prob_famine_relief_blocked_island`, `prob_humanitarian_border`, `prob_genocide_escape`, and `prob_cleanup` where the operation or invalidation path shares those existing factors.

The required evidence sequence is baseline `hoi4.probability_inspect`, scenario evaluation/sweep, owner-applied tuning, then `hoi4.probability_compare` using the same named scenarios through `chaosx_ai_probability_auditor`.

No probability completion claim is supported by this handoff because the current auditor tool was unavailable and the direct MCP calls timed out.

## Migration plan

1. Add the corridor constants and private triggers/effects with documentation before changing the decision call sites.

2. Change `fm_negotiate_corridor.complete_effect` to prepare and submit the exact offer, preserving its existing cost and target UI but removing immediate border mutation and quarter relief.

3. Add `fm_accept_corridor_offer` and `fm_reject_corridor_offer` with shared exact-offer guards and AI blocks.

4. Replace the current generic corridor mission activation checks with the accepted origin/front contract and route proofs.

5. Add the accepted corridor branch to the three existing civilian evacuation decisions and call the exact transfer helper once per operation.

6. Add the exact reserve relief branch only where an existing relief/convoy operation supplies a proven donor and route.

7. Centralize invalidation, attack disqualification, mission timeout, control-change, peace, and country-invalid cleanup.

8. Keep non-corridor evacuation on the existing weighted destination path and preserve both existing mapmodes without a GUI or third mapmode.

9. Run source lint and the required MCP inspect/compare/auditor workflow before any completion claim.

## Evidence, blockers, and unsupported analysis

The required offline wiki and vanilla documentation were consulted, including `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`, `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`, `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`, `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`, and the vanilla `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, `documentation/script_concept_documentation.md`, `documentation/dynamic_variables_documentation.md`, and `common/script_constants/documentation.md`.

The current source defect is visible in `common/decisions/famine_migration_decisions.txt:2004-2113`: `fm_negotiate_corridor` only proves an origin-side trapped crisis plus some enemy neighbor, accepts any other country, debits `relief_quarter` in `remove_effect`, and arms a mission without a durable exact front/counterpart or acceptance response.

The existing exact transfer endpoint is `common/scripted_effects/chaosx_famine_migration_effects.txt:famine_migration_transfer_civilians_exact` around line 1382, and the existing reserve endpoint is the `famine_migration_transfer_food_reserves` contract in the same file.

The current state-control hook is `common/on_actions/chaosx_famine_migration_on_actions.txt:33-38`, which calls `famine_migration_handle_state_control_change` and is suitable for exact route invalidation but not attack attribution.

The historical probability artifact is recorded in `docs/plans/famine_and_migration_system_plans/completion_report.md:50` as `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5712c1607f325cf31162964e8cb82dd3eb03738ad7633287adb8b11f96bf5759/fcc46d28fb1c766e9e9adc702d44cbb5941a3ee378d85687be77a778680e4ee5/probability-inspect-62b30cfcbe48.json`.

The historical decision audit records the additional inspect artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/824fbca7673608e8cb019c3b25d4101d8497c6109d0f66246bfd20785efd8189/537a4970ef837d99c949ab697a3506b9d027bff51f3c72d3fb6d2d2e0c543f87/probability-inspect-59e1d1ff03fa.json` in `docs/plans/famine_and_migration_system_plans/subagent_handoffs/decision_mission_audit.md:50-55`.

The historical map evidence is recorded as `map-inspect.de30e4f6849d41e0.json` in `docs/plans/famine_and_migration_system_plans/handoff_dispositions.md:38` and in the mapmode validation handoffs.

Fresh mandatory MCP calls in this turn were made against the `chaos_redux` workspace for `hoi4.probability_inspect` on `common/decisions/famine_migration_decisions.txt`, `hoi4.map_inspect` on the relevant state set, and the available read-only `hoi4.event_inspect` lint route for the decision source.

Each fresh call failed with the exact blocker `tool call error: tool call failed for hoi4_agent_tools/hoi4.<route>; Caused by: timed out awaiting tools/call after 180s`.

The callable tool inventory did not expose `chaosx_ai_probability_auditor`, so the required evidence pass and same-scenario probability comparison could not be performed here.

The current source contains no exact combat/front/strategic-bombing/nuclear attack callback that supplies an origin/front/attacker receipt, so attack-disqualifier ownership remains an explicit integration blocker.

The engine behavior of child ordinary decisions surfacing for a counterpart with only a pending offer, and the save/reload behavior of `var:<state_or_country_id>` scope resolution, remain runtime questions and require MCP or parent-owned live consumer validation.

No source-only inspection in this handoff is presented as a substitute for those MCP or engine checks.

## Completion boundary

This handoff is complete as an architecture proposal and intentionally contains no gameplay implementation.

Parent implementation is blocked only on the listed exact attack-owner hook, MCP/auditor availability, and engine validation of dynamic ID scopes and counterpart decision visibility; those blockers must be carried into the final report if they remain unresolved.
