# Relief-obstruction receipt audit

Date: 2026-08-26.

Scope: Audit the current famine-relief and humanitarian-corridor lifecycle for a truthful caller of `famine_condemn_relief_obstruction`.

Verdict: No accepted owner currently exposes an exact people-denominated relief-obstruction receipt at a successful verified obstruction boundary.

No gameplay file was patched.

The wrapper remains definition-only and fail-closed.

## Required wrapper contract

`common\scripted_effects\famine_adapter_effects.txt:299-319` defines `famine_validate_condemnation_receipt_exact`.

The validator requires the country scope to carry `famine_condemnation_state` and `famine_condemnation_actor` event targets, with a valid state and existing actor.

It also requires positive `famine_condemnation_state_proven`, `famine_condemnation_food_proven`, `famine_condemnation_environment_proven`, `famine_condemnation_transport_proven`, `famine_condemnation_policy_proven`, `famine_condemnation_actor_proven`, `famine_condemnation_cause_proven`, `famine_condemnation_people_amount`, `famine_condemnation_generation`, `famine_condemnation_revision`, and `famine_condemnation_request_id`.

`common\scripted_effects\famine_adapter_effects.txt:338-350` then defines `famine_condemn_relief_obstruction` as a downstream Condemnation source only.

The wrapper adds no population loss, Deaths call, movement, reserve transfer, event, pacing, scan, or player-facing value.

The existing adapter documentation states the same contract at `common\scripted_effects\famine_adapter_effects.md:41-45` and records that no exact relief-obstruction caller exists at `:24`.

## Candidate owner audit

| Candidate | Exact facts available | Why it cannot author this receipt |
| --- | --- | --- |
| Foreign relief contract (`famine_relief_select_donor`, `famine_relief_create_contract`, `famine_relief_deliver_contract`) | `common\scripted_effects\famine_relief_effects.txt:243-519` persists recipient, donor, actor, route mode, contract date/generation, and measured delivery debit/credit. | `famine_relief_requested_amount`, `famine_relief_contract_amount`, and `famine_relief_last_delivery_debit/credit` are food-reserve units. A valid result is successful relief, not verified obstruction. The path has no people amount or five-dimensional condemnation proof and therefore cannot call the wrapper. |
| Local reserve release (`famine_release_reserves` -> `famine_consume_reserve_for_relief`) | `common\decisions\famine_decisions.txt:182-242` requests a reserve release, and `common\scripted_effects\famine_core_effects.txt:2201-2260,2378-2385` returns exact reserve debit and relief projection. | The amount is reserve/food units, not affected people. Success is local relief consumption, not a responsible actor's blocked operation. There is no state/actor target bundle, causal proof bundle, or obstruction boundary. |
| Corridor offer rejection (`humanitarian_corridor_reject_offer`) | `common\scripted_effects\humanitarian_corridor_effects.txt:367-394` validates the exact origin, front, requester, counterpart, operation, cohort, route generation, and response deadline through `common\scripted_triggers\humanitarian_corridor_triggers.txt:257-289`. | The rejection only changes contract status and performs cleanup. It carries no affected-people receipt, no relief-reserve amount, no revision or request identity, and no independent food/environment/transport/policy/cause proof. An evacuation offer rejection is not verified relief obstruction. The only current decision caller is `common\decisions\migration_decisions.txt:1239`. |
| Accepted corridor relief (`humanitarian_corridor_execute_relief` -> `famine_relief_deliver_contract` -> `humanitarian_corridor_record_relief`) | `common\scripted_effects\humanitarian_corridor_effects.txt:503-528,579-600` records valid route operation and exact reserve debit/credit after successful delivery. | The path proves delivered relief, not blocked relief. `humanitarian_corridor_relief_source_debit` and `humanitarian_corridor_relief_destination_credit` remain reserve units, not people. It lacks the condemnation actor, five causal dimensions, revision, and request identity. |
| Accepted corridor evacuation (`humanitarian_corridor_execute_evacuation` -> `humanitarian_corridor_record_evacuation`) | `common\scripted_effects\humanitarian_corridor_effects.txt:474-575` records positive exact origin debit, route deaths, survivor credit, cohort, and route generation after successful movement. | This is a movement owner, not a relief-obstruction owner. The fallback `humanitarian_corridor_transfer_people = migration_trapped_population` at `:77-90` is an aggregate and is explicitly not a valid affected-people receipt. The current evacuation decision supplies `migration_state_live_cohort_amount`, but that still describes a successful evacuation rather than a blocked relief operation. No condemnation call is valid here. |
| Famine mortality (`famine_record_exact_mortality_condemnation`) | `common\scripted_effects\famine_core_effects.txt:2401-2516,2643-2707` receives exact applied civilian loss, state, owner actor, food/environment/transport/policy/cause, generation, revision, and request date. | This is the sole famine mortality owner and already feeds deliberate-starvation or concealment Condemnation. Reusing its people amount as relief obstruction would relabel deaths and create duplicate condemnation evidence. |
| Migration trapped/reception demand (`migration_publish_reception_demand`) | `common\scripted_effects\migration_core_effects.txt:964-980` has a positive amount plus migration generation/revision and trapped-population cause. | The amount is trapped aggregate demand, not people affected by a verified relief obstruction. It has no responsible actor target or food/relief obstruction proof. |
| Generic route, war, peace, control, or policy callbacks | Existing corridor/reassessment helpers preserve exact IDs or relation changes in their narrow owner scope. | They do not expose an affected people amount, verified relief refusal/blocking operation, all condemnation dimensions, or a replay identity. Relation denial, route invalidation, and policy intensity cannot be promoted into a people receipt. |

## Callsite and namespace census

`famine_condemn_relief_obstruction` has no gameplay callsite in the current source tree.

The only source references are its definition and validator in `common\scripted_effects\famine_adapter_effects.txt`, the adapter documentation, existing constants, and audit documents.

`famine_relief_deliver_contract` is called by the three foreign-relief decision lanes at `common\decisions\famine_decisions.txt:418,645,807` and by the corridor relief adapter at `common\scripted_effects\humanitarian_corridor_effects.txt:587`.

None of those callers has a verified obstruction result or the required people/proof bundle.

`humanitarian_corridor_reject_offer` is called by `common\decisions\migration_decisions.txt:1239`.

No decision or helper calls `famine_condemn_relief_obstruction` after rejection, delivery failure, route expiry, relation invalidation, or cleanup.

All current runtime names remain separated into `famine_*`, `migration_*`, and `humanitarian_*` namespaces.

No new identifier, alias, wrapper, or combined namespace was introduced.

## State, actor, and replay analysis

The famine relief contract stores scope-valued donor and actor variables and uses regular chain-local event targets at `common\scripted_effects\famine_relief_effects.txt:373-421` and `:423-519`.

Its `famine_relief_contract_generation = global.date` is a contract timestamp, not the condemnation receipt's independently supplied generation, revision, and request identity.

Successful delivery writes reserve debit/credit history and clears the active contract; failed or stale delivery runs cleanup without creating an obstruction receipt.

The corridor offer mirror validates exact route identity and generation, but it does not mirror transfer people, reserve amount, causal dimensions, revision, or request identity.

`humanitarian_corridor_reject_offer` enters the persisted origin only long enough to set a rejected status and call cleanup, then clears the response mirrors at `common\scripted_effects\humanitarian_corridor_effects.txt:367-394`.

The corridor route generation is a route identity and cannot substitute for the condemnation generation/revision/request contract.

`humanitarian_corridor_cleanup` clears active route IDs, proof fields, operation, cohort, transfer people, relief reserve debit/credit, and transaction receipts at `common\scripted_effects\humanitarian_corridor_effects.txt:900-1034`.

There is no durable, replay-safe obstruction receipt surviving that cleanup boundary.

The documented event-target rules in `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md:254-312` and `paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md:231-264` confirm that regular targets are chain-lifetime pointers and global targets would require explicit cleanup.

The current lifecycle therefore cannot safely reconstruct a responsible actor or exact affected people after rejection or expiry.

## Helper map and implementation decision

| Helper | Scope | Inputs | Output and side effects | Decision |
| --- | --- | --- | --- | --- |
| `famine_validate_condemnation_receipt_exact` | Country | Explicit state and actor event targets plus the complete proof bundle and positive people amount. | Temporary validity only. | Reuse unchanged; no new helper is justified. |
| `famine_condemn_relief_obstruction` | Country | The validator's exact receipt. | Existing Condemnation source only. | Leave unchanged and fail-closed. |
| Potential relief-obstruction producer | Unknown current owner | Would need a real successful verified obstruction transaction with exact state, responsible actor, positive affected people, five causal dimensions, generation, revision, and request identity. | One call to the existing wrapper after validation, with a one-shot/replay guard owned by the producer. | No accepted producer exists, so no helper or callsite is proposed. |

No scripted effect, scripted trigger, decision, event, GUI, map, population, Deaths, transfer, or localisation change was made.

## Constants and tuning table plan

No constants were added or changed.

`famine_condemnation_gain.relief_obstruction` already exists as a Condemnation gain constant, but its existence does not supply an owner or an affected-people conversion.

The relief constants and fields describe reserve units, and no documented reserve-to-people conversion contract exists.

No fixed, arbitrary, inferred, survivor-credit, trapped-aggregate, death, or food-unit amount is proposed.

## Event-target and cleanup plan

No new event target is proposed.

The existing relief targets (`famine_relief_selection_recipient`, `famine_relief_selection_actor`, `famine_relief_delivery_donor_state`, `famine_relief_delivery_donor_country`, and `famine_food_reserve_destination`) remain chain-local and are cleared by their existing contract cleanup.

The existing corridor origin target and response mirrors remain route identity only and are cleared by corridor cleanup.

Only a future accepted obstruction owner may create the validator's `famine_condemnation_state` and `famine_condemnation_actor` targets, and that owner must clear its one-shot receipt after the wrapper returns.

A future owner must persist a producer-owned replay guard keyed to its own generation/revision/request identity until the terminal cleanup policy is defined.

No global event target is warranted by the current evidence.

## Migration plan for a future exact owner

There is no migration to perform in this audit.

If a real relief owner is recovered, it must write a positive affected-people value at the successful verified obstruction boundary rather than at offer preparation, ordinary rejection, reserve delivery, route expiry, or generic policy reassessment.

That owner must provide explicit state and responsible-actor targets, food/environment/transport/policy/cause proof, generation, revision, request identity, and an idempotent one-shot guard before calling `famine_condemn_relief_obstruction` once.

Reserve debit/credit, trapped population, evacuation debit, survivor credit, and deaths must remain separate ledgers and must not be used as substitutes.

## Risks, unsupported analysis, and follow-up

The current source has no generic verified-relief-obstruction callback or exact refusal transaction that exposes affected people.

Vanilla and current source provide no people conversion from famine reserve units, so a conversion would be an unauthorized inference.

The existing historical handoff `docs\plans\famine_and_migration_system_plans\subagent_handoffs\condemnation_owner_scaling_map.md` contains older combined-namespace discussion and is not current implementation evidence; the current split source census and `remaining_owner_receipts.md` are authoritative for this audit.

No focus, GUI, map, or event surface is in scope, so no read-only MCP surface inspection or render/compare artifact applies.

No weighted or probability-bearing helper was changed or proposed, so `hoi4.probability_inspect` and the `chaosx_ai_probability_auditor` evidence pass were not applicable.

The required audit route remains blocked only by the missing owner receipt, not by a tooling substitution.

Parent-owned follow-up is to recover a concrete relief transaction owner or keep this API definition-only and fail-closed.

## References and validation

Required repository guidance and skills used: `AGENTS.md`, `.agents\skills\chaos-redux-state-ledgers\SKILL.md`, and `.agents\skills\chaos-redux-subagents\SKILL.md`.

Offline references consulted: `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md`, `Effects - Hearts of Iron 4 Wiki.md`, `Triggers - Hearts of Iron 4 Wiki.md`, `Scopes - Hearts of Iron 4 Wiki.md`, `Modifiers - Hearts of Iron 4 Wiki.md`, `Localisation - Hearts of Iron 4 Wiki.md`, `On actions - Hearts of Iron 4 Wiki.md`, `Event modding - Hearts of Iron 4 Wiki.md`, `Decision modding - Hearts of Iron 4 Wiki.md`, `Idea modding - Hearts of Iron 4 Wiki.md`, and `AI modding - Hearts of Iron 4 Wiki.md`.

Vanilla references consulted: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, and `common\script_constants\documentation.md`.

Required current-status artifacts consulted: `completion_report.md`, `source_of_truth_map.md`, `improvement_review_addendum.md` for FM-R25, `remaining_owner_receipts.md`, `owner_receipts_0826.md`, and `current_owner_blocker_reaudit.md`.

Task-specific checks run were source-range inspections and `rg` callsite/identifier censuses for the wrapper, relief delivery/release paths, corridor acceptance/rejection/relief/evacuation paths, mortality owner, migration demand/cohort paths, and condemnation sink.

No gameplay lint or live game run was performed because no gameplay file changed, and live HOI4 execution is outside the agent boundary.

No new MCP artifact exists for this audit because no supported focus, GUI, map, event, or weighted surface was in scope.

Known limitation: source inspection cannot prove a future runtime owner that is absent from the current repository; the missing exact receipt is therefore an explicit blocker rather than a synthesized fallback.

## Completion statement

Files changed: `docs\plans\famine_and_migration_system_plans\subagent_handoffs\relief_obstruction_receipt_0826.md` only.

Gameplay helpers, callsites, constants, cleanup, and player-facing surfaces changed: none.

The requested exact caller was not implemented because no truthful caller exists in the current accepted lifecycle.

No simplification or fallback was used.
