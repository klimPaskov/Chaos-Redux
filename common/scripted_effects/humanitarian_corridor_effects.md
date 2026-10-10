# Humanitarian corridor contract helpers

This package owns an exact, non-event humanitarian-corridor contract. The origin state persists the origin, adjacent front state, requester, counterpart controller, cohort, operation, deadlines, route-proof bundle, and transaction outputs in normal variables. Regular event targets are used only during one exact transfer chain. The helpers add no event ID, event pool, GUI, or mapmode, and use the two existing owner mapmodes only as presentation consumers.

## Files and identifiers

- `common/script_constants/humanitarian_corridor_constants.txt` defines `humanitarian_corridor_status`, `humanitarian_corridor_operation`, `humanitarian_corridor_relation`, `humanitarian_corridor_reason`, `humanitarian_corridor_result`, `humanitarian_corridor_timing`, and `humanitarian_corridor_runtime`.
- `common/scripted_triggers/humanitarian_corridor_triggers.txt` defines `humanitarian_corridor_origin_is_valid`, `humanitarian_corridor_front_candidate_is_valid`, `humanitarian_corridor_counterpart_is_valid`, `humanitarian_corridor_front_destination_is_safe`, `humanitarian_corridor_front_state_is_valid`, `humanitarian_corridor_route_geometry_is_valid`, `humanitarian_corridor_offer_request_is_valid`, `humanitarian_corridor_acceptance_is_valid`, `humanitarian_corridor_offer_is_valid`, `humanitarian_corridor_operation_is_valid`, `humanitarian_corridor_mission_is_valid`, `humanitarian_corridor_route_binding_is_valid`, `humanitarian_corridor_attack_receipt_is_valid`, `humanitarian_corridor_country_pulse_is_valid`, and `humanitarian_corridor_cleanup_needed`.
- `common/scripted_effects/humanitarian_corridor_effects.txt` defines proof-copy/preparation, offer submission, acceptance/rejection, route binding, exact evacuation/relief adapters, mission arm/finalize/expiry, attack disqualification, cleanup, and sparse pulse helpers. Public response effects are `humanitarian_corridor_accept_offer` and `humanitarian_corridor_reject_offer`.

## Lifecycle

`humanitarian_corridor_prepare_contract` runs on the exact origin STATE, persists origin/requester identity and counts valid adjacent fronts.
Ordinary decision callers default to ROOT as requester; sparse spontaneous callers explicitly bind their actual origin OWNER through `humanitarian_corridor_requester` and a validated temporary override.
An explicit front ID still passes the same adjacency/actor/food/native-hazard predicate; default manual discovery retains its zero/multiple-candidate rejection.
Preparable fronts need current food and native route/hazard proof but not yet-paid reception services/capacity.
Every new contract allocates a fresh monotonic generation, including retries of the same retained cohort.

`humanitarian_corridor_submit_offer` writes the response deadline and mirrors one pending offer on the exact counterpart country, registers that real issue and schedules the existing sparse country pulse.
Each distinct valid evacuation generation increments the existing incident count exactly once.
Private last-generation/fresh-until receipts retain a real prior incoming episode across dormant incident cleanup for `cooldown_days + offer_response_days`; a second fresh generation can reconstruct exactly one prior episode before incrementing the new one, while an expired receipt cannot reveal ancient history.
No incoming metadata is an arrival or reception-load receipt.
Acceptance reobserves current food/capacity, resolves the actual live row and requires full offered amount equality and exact current headroom before acknowledging success and clearing the matching host mirror.
Rejection and expiry preserve the unmoved origin cohort/flight/trapped obligation.
Country mirrors clear only on matching origin/generation, so stale cleanup cannot erase a later request or the counterpart's independent outgoing contract.
Sparse pulses also bind positive mirror generation and actual counterpart/requester before expiring an origin.
`humanitarian_corridor_clear_stale_incoming_mirror` runs only on a valid COUNTRY whose incoming mirror no longer matches a live origin contract; it clears only that local incoming identity and rearms the existing outgoing pulse when necessary.
It returns no output, moves no people and leaves every origin/newer contract and permanent transfer receipt unchanged.

`humanitarian_corridor_rearm_surviving_country_identity` runs in COUNTRY scope after matching terminal or stale-local mirror cleanup.
It checks an active incoming mirror's exact origin/counterpart/generation, or the outgoing mirror's exact active origin/requester/generation, without treating identity as operational admission proof.
Either surviving identity rearms only the existing `humanitarian_corridor_country_pulse_pending` and `humanitarian_corridor_country_pulse_due` at `global.date + humanitarian_corridor_timing.pulse_cooldown_days`.
No surviving identity clears those two scheduling fields.
Matching receiver terminal cleanup invokes it after removing the incoming mirror, and matching requester terminal cleanup invokes it after removing the outgoing mirror, so independent opposing contexts retain scheduled revalidation after expiry, rejection or completion.
Nonmatching stale-generation terminal callbacks do not enter either cleanup branch or mutate another context's scheduling.
This helper has no input/output envelope, resource/ledger mutation, new timer, new scheduler or world scan.

`humanitarian_corridor_bind_route_destination` saves the persisted front as regular exact route targets.
Evacuation reobserves food/capacity and resolves the entire current origin row; stored offer, live row and actual requested transaction must agree, and live protected population/flight reservations plus full receiver headroom must cover that amount.
The shared exact transaction remains the only population/reception/cohort mutation owner.
Post-finalizer evacuation recording validates measured full debit, zero deaths, equal survivor/destination credit, zero conservation residual, exact cohort/current transfer projection and unchanged contract generation, not pre-move row/headroom.
The durable current transfer-generation receipt is `humanitarian_corridor_evacuation_transfer_generation`.
Relief retains its existing destination safety/capacity branch and reserve-transfer owner; evacuation preparation does not grant relief services or route authorization.

On valid acceptance, the receiving country emits one achievement gate request containing the prepared route generation, exact origin state ID, exact front state ID, counterpart country ID, and offered cohort ID. `humanitarian_achievement_record_gate_crisis` then derives the qualifying cohort set from the authoritative global cohort IDs, host states, live statuses, amounts, and approved camp/genocide/exterminatory source ledger (or catastrophic origin proof); it never uses aggregate trapped population as a cohort identity. Before terminal route IDs are cleared, `humanitarian_corridor_cleanup` calls `humanitarian_achievement_record_gate_terminal_cleanup` on that exact counterpart country, preserving the terminal cohort/protection/resolution arrays and clearing the active arrays for idempotent replay failure.

Manual corridor missions arm only when the requester has a free existing mission slot and retain their prior finalize/expiry behavior.
The private ordinary spontaneous lane does not arm a manual mission or start a manual full-term famine achievement attempt; its existing sparse origin owner consumes accepted requests and immediately completes a measured successful passage.
Actual receiving-country protection evidence is recorded before cleanup archives terminal achievement arrays.
Consent alone grants no protection or completion.
Cleanup is idempotent, clears only matching country mirrors/mission fields, recounts existing mission slots, and never reverses a committed transfer or erases the authoritative moved cohort/reception/projection ledgers.

## Mapmode operation provenance

The corridor origin state owns the presentation pair `humanitarian_corridor_last_terminal_status` and `humanitarian_corridor_last_terminal_operation`.
Preparation clears both fields when starting a new contract so an earlier terminal operation cannot override the new live offer or operation.
Cleanup records the current status and copies the current operation only when it is the recognized evacuation or relief constant, then clears the live contract fields.
A missing or invalid operation leaves the terminal operation absent, and mapmode consumers must not infer it from a status, cohort, owner, or route alone.
Repeated cleanup after the live status has been cleared preserves the existing terminal pair.

Migration mapmode borders and corridor, route, generation, and preparation selectors require explicit evacuation operation provenance.
Terminal migration corridor selectors require the recorded terminal evacuation operation because cleanup removes the live operation.
Famine mapmode presentation continues to consume famine-owned route and delivered-relief receipts.
These fields change presentation only and never authorize movement, relief, rewards, mission completion, or any population change.

For example, a relief offer records `humanitarian_corridor_operation = constant:humanitarian_corridor_operation.relief` while active and records that same token in `humanitarian_corridor_last_terminal_operation` when cleaned up.
Neither stage qualifies a migration corridor display.

## Route-proof and replay contract

`humanitarian_corridor_front_is_preparable` requires current food, native rail/bombing/infrastructure and all supported live hazard channels clear, including trapped population.
`humanitarian_corridor_front_destination_is_safe` adds valid current capacity, while exact evacuation admission/transfer separately checks `load + whole amount <= capacity`.
It also retains the existing relief spare-capacity condition, load absent or load strictly below capacity; full relief capacity is not admission-ready.
A completed exact-fit passage remains recordable because post-finalizer recording does not demand spare capacity after the people arrived.
A missing or orphaned generic unsafe marker is never treated as safety evidence.

Preparation's transport proof mirrors the established destination selector: both exact adjacent endpoints must exceed `constant:migration_destination_selection_threshold.minimum_route_infrastructure` and expose the live `famine_component_transport` field. The field is availability evidence, not a fabricated throughput value; a missing field fails closed.

`humanitarian_corridor_front_state_is_valid` additionally requires the origin's current owner/controller, the stored counterpart's current ownership/control of the exact adjacent front, and the persisted relation to remain valid. Enemy-front relations require the current war relation, while neutral, faction-partner, and ordinary-neighbor relations require the corresponding current non-war/faction requirements. `humanitarian_corridor_route_geometry_is_valid` adds the positive accepted ceasefire proof for an operating route and requires positive cohort, route-generation, and proof-generation identity, with proof generation equal to route generation.

The counterpart mirror persists `humanitarian_corridor_offer_cohort_id` and `humanitarian_corridor_offer_route_generation` alongside the exact origin/front/requester/operation fields. Acceptance compares every mirrored identity against the origin before setting safety, ceasefire, and reception proofs. Terminal cleanup clears the mirror generation with the other offer fields.

## Sparse callback helpers

`humanitarian_corridor_handle_state_control_change` is called in the documented `on_state_control_changed` state scope. It checks the exact changed state against the persisted origin ID, then checks only `global.migration_active_countries` for mirrored front-state IDs. Matching origins are invalidated with `control_change`; the callback never writes an attack receipt.

The same callback first calls `migration_reception_front_intent_handle_control_change` on the changed state, so a front that changed hands drops the reception intent of any receiver that no longer owns and controls it.

## Relief-obstruction hooks

`humanitarian_corridor_reject_offer` and the response-deadline branch of `humanitarian_corridor_expire` call `famine_condemn_corridor_obstruction` on the origin before cleanup clears the corridor identity. Expiry condemns only a genuine unanswered lapse: the deadline has passed while the origin, counterpart and offered route were otherwise still acceptable. Both paths condemn only a receiver that could have accepted, meaning its safe front and current reception capacity had room for the whole request (`humanitarian_corridor_full_request_headroom_is_valid`). Only an evacuation corridor from a famine or catastrophic famine state with measured people condemns the receiving country, once per route generation.

## Receiver-front reception intent hooks

Evacuation corridors publish an identity-only intent row on their front state through [migration_reception_front_intent_effects.md](migration_reception_front_intent_effects.md).
`humanitarian_corridor_submit_offer` publishes `requested` after a valid submission, and `humanitarian_corridor_accept_offer` publishes `agreed` inside its successful inner acceptance, using a reveal snapshot taken while the offer was still pending.
`humanitarian_corridor_record_evacuation` retires the row after the measured, conserved passage, and `humanitarian_corridor_cleanup` retires it for every other terminal before the live contract fields are cleared.
These calls are presentation only; a failed publication or retirement never changes the corridor result, moves people or grants capacity.

`humanitarian_corridor_revalidate_sparse_country` is called only on countries named by war, peace, and peace-conference callbacks that carry the existing registered-country flag. It resolves one pending-offer or active-contract origin ID and validates the persisted relation, front controller, and adjacency. A route that no longer satisfies its stored relation is invalidated with `route_closed`; no country or state scan is performed.

The offline on-actions reference defines `on_peace` with `THIS` as the country that is no longer at war, while `on_war_relation_added` and `on_peaceconference_ended` provide paired country scopes. The hook wiring follows those scopes exactly.

`humanitarian_corridor_handle_exact_state_attack` accepts only a saved exact attacker and the current exact state. An origin match submits the attacker ID directly. A second pass through `global.migration_active_countries` resolves an exact persisted `front_state_id` and current contract generation before submitting the same receipt on the origin. `on_naval_invasion` supplies the invaded `THIS` state and invading `ROOT` country, while the once-per-operation `on_units_paradropped_in_state` callback supplies the exact `ROOT` state and dropping `FROM` country. `humanitarian_corridor_handle_nuke_drop` adapts the documented launcher and nuked-state scopes into this shared path. Missing or stale identity fails closed.

## Current canonical decision consumers: 2026-10-03

The parent authorized this bounded documentation reconciliation after accepting the separate famine/migration implementation and the current corridor presentation correction.
Current source callsites are in `common/decisions/famine_decisions.txt` and `common/decisions/migration_decisions.txt`, rather than the historical `common/decisions/humanitarian_decisions.txt` path quoted below.

| Current consumer | Source evidence | Boundary |
| --- | --- | --- |
| `migration_negotiate_corridor` | Migration decision source calls `humanitarian_corridor_prepare_contract`, then `humanitarian_corridor_submit_offer` only when preparation reports valid. | Existing route/capacity/cohort requirements remain authoritative; no new negotiation wiring is requested by the historical instructions. |
| `migration_accept_corridor_offer`, `migration_reject_corridor_offer` | Migration decision source invokes the respective corridor response effect. | Acceptance/rejection changes the exact contract; it does not itself move population. |
| `famine_evacuation`, `migration_evacuate_civilians` | One famine and one migration decision lane call `humanitarian_corridor_execute_evacuation` in their accepted corridor branch. | Exact transaction and generation-bound receipt remain the sole movement authority. |
| `migration_mission_hold_humanitarian_corridor` | Migration mission calls `humanitarian_corridor_finalize` on successful completion and `humanitarian_corridor_expire` on cancellation/timeout. | Existing exact subject/operation guards and mission-owner outcomes remain unchanged. |

This table is current source evidence, not live execution, numeric AI validation, or final completion.
The current probability specialist handoff is `docs/plans/famine_and_migration_system_plans/subagent_handoffs/probability_capability_reaudit_20261003.md`; its country-target same-case comparison remains outstanding.
Food assessment is integrated separately in commit `52b2e7cfe`, with `normal_food_observation_probability_20261003.md` retaining the pre-integration destination baseline and `normal_food_observation_completion_audit_20261003.md` recording final source corrections.
The internal/persecution same-scenario eligibility compare and native helper execution remain unresolved.
Food assessment supplies no shelter/medical service or host-activation receipt.
The accepted prospective runtime now supplies the first-host exact request and paid preparation lifecycle described above, without inferring free service from food observation.
Current source cases, parent-owned integration and still-unresolved probability/native execution evidence are recorded in `docs/plans/famine_and_migration_system_plans/subagent_handoffs/prospective_reception_implementation_20261003.md`.

## Historical required-wiring instructions

The instructions below describe the original owner handoff before the separate decision consumers above were integrated.
They are retained as implementation history, not a current instruction to rewire those consumers or recreate the old decision file.

The parent must wire the corridor negotiation decision in the parent-owned decision file to submit route-proof request variables, call `humanitarian_corridor_prepare_contract`, then `humanitarian_corridor_submit_offer`, and remove immediate humanitarian-policy/quarter-relief mutation. It must add ordinary counterpart response decisions with the same offer trigger and AI surface, and route accepted branches of the three evacuation decisions through `humanitarian_corridor_execute_evacuation` rather than weighted destination selection. Any relief branch must supply a proven donor and `humanitarian_corridor_relief_amount_request` before `humanitarian_corridor_execute_relief`.

The parent must replace generic `any_neighbor_state` mission activation/availability/cancellation checks for the humanitarian-corridor hold mission with the exact origin/front validators and call finalize/expire. The parent should add sparse calls from the parent-owned humanitarian on-actions file and the existing registered country/state hooks only for stored IDs; no `on_daily`, `on_weekly`, `on_monthly`, global periodic scan, event target registry, event, GUI, or third mapmode belongs here.

Attack disqualification is wired through the authoritative nuclear, naval-invasion, and once-per-operation paradrop receipts described above. The live core safety projection separately refreshes `civilian_transfer_route_damaged` from positive native rail damage and `migration_bombing_active` from the current strategic-bombing recency window; the corridor reads those producers only as hazard exclusions and also checks their native current values. Ordinary land-combat and strategic-bombing callbacks that provide exact corridor origin/front/attacker identity remain unavailable in the engine/source surface; those paths stay fail-closed and are not inferred from `has_war_with`, peace, control loss, or a bombing date.

The engine still needs runtime validation for counterpart ordinary-decision visibility from a country-only pending mirror and for save/reload `var:<database_id>` state/country scope resolution. These are recorded blockers, not source fallbacks.

## Replay-safe evacuation receipt

The receipt contract below remains source-level documentation; references to the former `humanitarian_decisions.txt` file describe the historical repair snapshot.
Current evacuation consumers are the three separate decision IDs in the table above.

The canonical one-shot receipt is the origin-state normal variable `humanitarian_corridor_evacuation_proven = 1`, scoped to the active `humanitarian_corridor_route_generation`. The three exact evacuation lanes in `common/decisions/humanitarian_decisions.txt` and `humanitarian_corridor_execute_evacuation` require that generation and all fail closed when this variable exists, so an already-consumed generation cannot debit the origin again.

Before this repair, all three lanes tested `NOT = { has_state_flag = humanitarian_corridor_evacuation_proven }`, although the producer persisted only the normal variable and no state-flag producer existed. The execution helper also had no receipt guard, and terminal cleanup cleared the dead flag name separately from the durable variable.

After this repair, each lane requires `has_variable = humanitarian_corridor_route_generation` and tests `NOT = { has_variable = humanitarian_corridor_evacuation_proven }`, the execution helper repeats both guards, and `humanitarian_corridor_record_evacuation` repeats them while requiring a valid exact result, positive origin debit, and positive survivor credit. The receipt is written only after the exact endpoint has returned both measured movement values; cohort binding and reception recording remain part of that same accepted transaction chain.

The first valid caller therefore owns one origin debit, one route-death amount, one survivor destination credit, one cohort/reception record, and one mission proof. A second same-generation lane is unavailable, and a direct helper call returns the initialized invalid transaction result without entering the exact-transfer endpoint. Mission continuation and `humanitarian_corridor_finalize` still use the durable proof variable and mission-active state, so replay prevention does not cancel or re-run the mission.

`humanitarian_corridor_prepare_contract` clears the receipt only while fully resetting the state for a new route generation. `humanitarian_corridor_cleanup` clears the normal-variable receipt only on terminal, expiry, or full reset paths; it no longer clears the dead state-flag name. The normal variable survives save/reload, and repeated terminal cleanup remains idempotent without reversing a committed transfer or clearing cohort metadata.

## Historical probability and MCP evidence

The no-auditor and required-future-wiring statements below belong to the original helper tranche and its tool inventory.
They do not describe current specialist availability or certify October source.
All artifact URIs and original per-request limits remain unchanged for provenance; current scenario limitations are recorded in the dated probability handoff and `docs/plans/famine_and_migration_system_plans/ai_probability_current.md`.

No weighted helper or AI factor was added in this tranche, so no probability compare was applicable. The required initial `hoi4.probability_inspect` returned `discoveryReason=no_weighted_surfaces`, with zero candidates and zero unresolved inputs, for the owned effect source. The named `chaosx_ai_probability_auditor` route was not available in the enabled tool set, so no auditor evidence pass was possible; no weights were changed. If the parent adds accept/reject AI weights, it must run `hoi4.probability_inspect` first and the `chaosx_ai_probability_auditor` baseline/compare workflow for `prob_corridor_acceptance` and the named scenarios in the architecture handoff.

Read-only MCP evidence used for this helper boundary:

- Decision lint: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d4d07833c1b269b47049aa9871a1a73bfc5ed2515d4727b531c263c4c6791933/18cfc541a40928807c83e481f5ea81797180a9748d5782d07c54a23297e4c221/event-lint-2ff7afa1197e.json` (`EVENT_INSPECTED_PARTIAL`; deferred helper projections explain the partial result).
- Probability inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/195cb52e80ca347642a3afb702a1ed6264c3bdcb433667a8e6cece8faabf2f37/0bba180908fa37b57e45304c86fe3a8a8dedf24c12061d9d3e0de4c22d1a9f78/probability-inspect-c716751f7dfb.json` (`PROBABILITY_SOURCE_DISCOVERED`; no weighted surfaces, zero candidates, zero unresolved inputs; no probability weights changed).
- Fresh helper-file lint: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b5b92527ff31d4733b93f622db8c38a022790728065322ce280046d3b1d952e2/467fe718d9a3e0a9a3598201d8e939afd1793392533d6c9eb380de9d9543a120/event-lint-2ff7afa1197e.json` (`EVENT_INSPECTED_PARTIAL`; no blocking diagnostics, workspace-wide helper/lifecycle projection deferred).
- Fresh post-repair decision lint was attempted against `common/decisions/humanitarian_decisions.txt` and blocked by the exact MCP error `tool call error: tool call failed for hoi4_agent_tools/hoi4.event_inspect; Caused by: timed out awaiting tools/call after 180s`.
- Relevant map inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e9f85bd2d3ac500120678a26f41ddd47c02cef8119f0bb057a9e8ff131faeb9e/31a8fa3f3d59e0871e4027ca23c6ad0d0916070b754285a4bf57bce8c5e8dff3/map-inspect.76240d67ca053497.json` (`MAP_INSPECTED`; adjacency/state membership passed, while unrelated existing building/port locator diagnostics kept the overall validation flag false).
- Fresh bounded map inspection for the adjacency surface: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/978cb238e3fce6632d213c546888d2d03a79a70a1351c7ce9ad5c54aff726f22/f9dde0560c9c44c561c0f73c4d4723394dd8d3c044acc44f1fa3417a4a5472bd/map-inspect.11f81b8704b94497.json` (`MAP_INSPECTED`; state/region membership and network/adjacency checks passed, while unrelated map-building/port locator diagnostics kept the overall validation flag false).

The offline wiki, vanilla documentation, existing Chaos Redux famine/migration helpers, exact transfer/reserve contracts, and vanilla adjacency/variable-scope precedents were consulted before writing these package-owned files.
