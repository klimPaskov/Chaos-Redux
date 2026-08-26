# Pressure API replay-boundary audit

Date: 2026-08-26

## Verdict

The live source has one proven bounded defect and no causally safe generic persisted-dedupe patch. `famine_validate_state_local_food_receipt_exact` previously accepted any positive generation, revision, and request identity and did not bind the state proof to the current state or the actor token to the saved actor target. The famine adapters also reset only `famine_adapter_amount`, leaving the remaining temporary proof fields available to a later call in the same parent effect block.

The patch adds `famine_clear_state_local_food_receipt` in `common/scripted_effects/famine_adapter_effects.txt` and calls it from the direct-death adapter and all five source-specific food adapters on both accepted and rejected paths. The helper resets every temporary `famine_adapter_*` contract input and `famine_adapter_contract_valid` to its documented zero or unknown value while preserving the public `famine_adapter_result` output. The validator now requires `famine_adapter_state_proven = THIS.id` and `famine_adapter_actor_proven = event_target:famine_adapter_actor.id`.

The patch deliberately does not add a persisted consumed composite. A generic state-local receipt keyed only by the current fields would be unsafe because current Camp and CBRN receipts use date-based generation/request fields, and distinct same-date operations are not proven to have unique identities. The existing exact owner guards and source transaction boundaries must remain the owners of a future stable receipt; an adapter-wide memory would either be decorative or risk suppressing a legitimate operation.

## Files changed

| File | Change |
| --- | --- |
| `common/scripted_effects/famine_adapter_effects.txt` | Added temporary-envelope cleanup helper, wired cleanup to the direct-death, Air Winter, Camp, CBRN, Black Plague, and Event 013 adapters, and added state/actor identity equality checks. |
| `common/scripted_effects/famine_adapter_effects.md` | Documented helper inputs/outputs, cleanup behavior, identity binding, replay boundary, and the reason generic persisted dedupe is deferred. |
| `docs/plans/famine_and_migration_system_plans/subagent_handoffs/pressure_api_replay_boundary_0826.md` | This audit and handoff. |

## Definitions and callsites inspected

The famine low-level trigger `famine_pressure_request_is_valid` at `common/scripted_triggers/famine_core_triggers.txt:50-58` checks only valid state, positive chain-local proof, positive people amount, non-unknown source, and actor proof. `famine_apply_pressure_request` at `common/scripted_effects/famine_core_effects.txt:446-471` owns famine pressure mutation and resets its four chain-local pressure inputs after every attempt.

The migration low-level trigger `migration_pressure_request_is_valid` at `common/scripted_triggers/migration_core_triggers.txt:17-25` has the corresponding smaller chain-local contract. `migration_apply_flight_request` at `common/scripted_effects/migration_core_effects.txt:734-782` resets its pressure envelope, and `migration_accept_famine_survivor_request` at `:683-731` also resets the envelope when validation fails before the apply helper.

The exact famine validator and adapters are in `common/scripted_effects/famine_adapter_effects.txt:68-317`. The current external owner callsites are `fallout_consolidated_effects.txt:3948-4049`, `camp_repression_rework_effects.txt:1958-1983`, `cbrn_occupation_effects.txt:459-538`, `020_black_plague_effects.txt:1332-1463`, and `013_natural_disasters_effects.txt:5244-5363`. Each source callsite has one adapter invocation in the inspected owner operation; no second current callsite replays the same adapter from another dispatcher.

The only current direct low-level external-looking callback is `common/on_actions/humanitarian_runtime_on_actions.txt:125-152`, where `on_nuke_drop` computes separate famine and migration amounts and calls the source-specific nuclear endpoints in one documented callback-local chain. It intentionally has no generation, revision, or request identity because it is not an exact external adapter receipt and does not cross the famine adapter file. Save/reload does not re-run an on-action, but a future owner-specific replay identity is still needed if that callback is ever replayed manually or routed through a persistent queue.

The migration pressure wrappers at `common/scripted_effects/migration_core_effects.txt:785-823` have no current external adapter callers. The two additional calls at `:1911` and `:1950` are owner-local organized-evacuation and deportation flows inside migration core, where the source owner stages the cohort and then submits the pressure envelope in the same chain. They are not cross-system adapter calls.

## Definition-only source census

The following helpers are defined but have no live caller outside their own definition or wrapper declaration in the current `common` source census:

| Surface | Definition | Exact owner facts absent from current callers |
| --- | --- | --- |
| Famine occupation | `famine_request_occupation_pressure` at `famine_core_effects.txt:506` | No generic occupation-law transition receipt with positive people amount, responsible actor, generation, revision, and request identity. |
| Famine strategic bombing | `famine_request_bombing_pressure` at `famine_core_effects.txt:514` | No exact bombing owner receipt carrying affected state, positive people amount, attacker/actor, cause, and unique replay identity. |
| Famine war / peace | `famine_request_war_pressure` and `famine_request_peace_pressure` at `famine_core_effects.txt:524-526` | Relation callbacks expose no affected state/cohort and people-denominated impact receipt. |
| Famine cluster / scenario | `famine_request_cluster_pressure` and `famine_request_scenario_pressure` at `famine_core_effects.txt:536-538` | Dispatch metadata has no authoritative affected people and replay-safe source identity. |
| Migration occupation | `migration_request_occupation_pressure` at `migration_core_effects.txt:789` | No exact hostile occupation displacement receipt. |
| Migration strategic bombing | `migration_request_bombing_pressure` at `migration_core_effects.txt:799` | No exact live cohort/people/route/actor receipt. |
| Migration war / peace | `migration_request_war_pressure` and `migration_request_peace_pressure` at `migration_core_effects.txt:809-811` | No state/cohort and positive people receipt from relation callbacks. |
| Migration cluster / scenario | `migration_request_cluster_pressure` and `migration_request_scenario_pressure` at `migration_core_effects.txt:821-823` | No exact live cohort/route/actor/generation/revision/request receipt. |
| Famine relief obstruction | `famine_condemn_relief_obstruction` at `famine_adapter_effects.txt:361-373` | Current relief contracts expose reserve debit/credit, route identity, or rejection context, not a verified affected-people obstruction transaction with a stable replay identity. |

No normalized pressure, food reserve units, trapped aggregate, route deaths, survivor credit, or dispatch metadata was converted into a people receipt. No event, event-pool, log, pacing, decision, localization, asset, mapmode, or probability surface was touched.

## Before and after behavior

Before this patch, a source owner could set a new positive `famine_adapter_amount` in the same parent effect block while omitted proof fields remained positive from an earlier adapter call; the validator also accepted a positive state or actor token even when it referred to a different current state or saved actor target. The pressure endpoint would then mutate famine pressure using the new amount and inherited proof.

After this patch, every famine adapter resets all temporary proof, amount, generation, revision, request identity, and validator-result inputs after its attempt. A state or actor mismatch fails validation before pressure mutation, and a later call must set a fresh complete bundle. The public result remains readable by the owner in the same chain.

Identical complete proof re-supply across separate effect chains remains an owner-level responsibility. The adapter does not claim generic idempotence because current source request fields are not uniformly unique, and no current caller provides a safe adapter-owned consumed composite.

## Validation

The endpoint census used `rg` across all `common` script files and found only the five exact famine owner adapters, the bounded nuclear callback, and the two migration-core owner-local flows as live pressure callsites. The definition-only census confirmed no accepted occupation, bombing, war, peace, cluster, scenario, or relief-obstruction owner now supplies the complete exact contract.

The patched file was reviewed for one cleanup call on each famine adapter path and for absence of `clear_variable = famine_adapter_*`; temporary inputs use `set_temp_variable` resets consistently with the core envelope pattern. `git diff --check` is run before commit. No game launch or live save/reload test was performed because runtime validation belongs to the parent/user workflow.

## Rejected alternatives and remaining blockers

Rejected a three-field or full-field persisted dedupe inside the shared famine adapter because date-based and amount-based fields are not proven unique for all source owners, and suppressing a legitimate same-date operation would be worse than leaving owner replay unresolved. Rejected fabricating generation/request IDs in the adapter because identity must be supplied by the authoritative owner. Rejected a global registry or recurring scan because the task requires owner-local cleanup and sparse processing.

Remaining blockers are the generic source-owner receipts documented in the completion report and current completion re-audit, including occupation-law, bombing, war/peace, cluster/scenario, and relief-obstruction owners. A future owner that exposes a stable unique transaction identity must persist and consume that identity in its own scope before calling the exact adapter; this handoff does not invent that source fact.
