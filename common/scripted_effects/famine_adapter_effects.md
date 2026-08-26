# Famine owner adapters

This file documents `famine_adapter_effects.txt`. These helpers accept only a state-local food receipt from an owner that has already proven the affected state, food consequence, environmental context, transport consequence, policy context, responsible actor, causal generation, revision, and one-shot request identity.

Famine adapters register food pressure only. They never set a flight channel, create a migration cohort, transfer civilians, apply a population loss, or record route deaths.

## Helper map

| Helper | Scope and required inputs | Output and side effects | Owner call sites and status |
| --- | --- | --- | --- |
| `famine_publish_migration_food_safety` | State scope with initialized famine stage, pressure, production, transport, and governance facts. | Publishes a proven schema, monotonic generation/revision, and bounded `famine_to_migration_*` fields. It never initializes an untracked state; missing facts call the invalidator and fail closed. | Called after famine evaluation and by bounded migration consumers for registered states or adjacent destination candidates. |
| `famine_invalidate_migration_food_safety` | State scope when famine facts are absent or retired. | Clears the projected fields, clears proof, and dirties an already-registered migration reception candidate. It does not clear migration obligations. | Famine cleanup and rejected publisher attempts. |
| `famine_validate_state_local_food_receipt_exact` | State scope; valid civilian state; positive `famine_adapter_amount`; positive `famine_adapter_state_proven`, `famine_adapter_food_proven`, `famine_adapter_environment_proven`, `famine_adapter_transport_proven`, `famine_adapter_policy_proven`, `famine_adapter_actor_proven`, `famine_adapter_cause_proven`, `famine_adapter_source_proven`, `famine_adapter_generation`, `famine_adapter_revision`, and `famine_adapter_request_id`; live `famine_adapter_actor` event target. | Sets only temporary `famine_adapter_contract_valid`. It discovers no state, owner, amount, or actor. | Shared validator called by every famine pressure adapter. |
| `famine_clear_state_local_food_receipt` | State scope; no inputs. | Resets every one-shot temporary famine adapter proof, amount, generation, revision, request identity, and validation result after an adapter attempt. It leaves the regular chain-local actor event target to engine cleanup. | Called by every famine food/death adapter on both accepted and rejected paths. |
| `famine_apply_related_state_deaths_exact` | State scope; complete famine proof bundle plus a positive not-yet-applied occupation-repression or forced-labor request. | Calls the exact state population-loss primitive once and returns temporary `famine_related_deaths_applied`; it never accepts route deaths. | API-only until an upstream owner supplies all proof fields. |
| `famine_apply_occupation_repression_deaths_exact` | Famine-owned exact death request with occupation-repression reason. | Delegates to the famine direct-death receipt. | API-only. |
| `famine_apply_forced_labor_deaths_exact` | Famine-owned exact death request with forced-labor reason. | Delegates to the famine direct-death receipt. | API-only. |
| `famine_adapt_air_winter_state` | State scope; positive exact Air Winter loss plus the complete famine proof bundle. | Calls either `famine_request_fallout_pressure` or `famine_request_air_cleanliness_pressure` and returns temporary `famine_adapter_result`; no movement. | `fallout_consolidated_effects.txt`, `air_winter_apply_state_population_loss`; caller now supplies cycle, ledger, actor-target, and source proof from the accepted Air Winter loss. |
| `famine_adapt_camp_state` | State scope; positive `camp_site_last_month_deaths`, site type, responsible owner, and the complete famine proof bundle. | Calls `famine_request_camp_pressure`, `famine_request_gulag_pressure`, or `famine_request_forced_labor_pressure`; it never repeats Camp Deaths. | `camp_repression_rework_effects.txt`, `camp_rework_record_latest_state_deaths`; caller now supplies site, pool, control, actor-target, and dated receipt proof. |
| `famine_adapt_chemical_state` | State scope; positive accepted chemical civilian loss and the complete famine proof bundle. | Calls `famine_request_chemical_aftermath_pressure`; it never creates flight from chemical deaths. | `cbrn_occupation_effects.txt`, `cbrn_occupation_apply_accepted_operation_state`; caller now supplies accepted-operation route, severity, contamination, attribution, actor-target, and dated receipt proof. |
| `famine_adapt_black_plague_state` | State scope; established human Black Plague, positive exact loss, non-rat provenance, and the complete famine proof bundle. | Calls `famine_request_outbreak_pressure`; it never turns plague deaths into live movement. | `020_black_plague_effects.txt`, `black_plague_apply_current_state_mortality_once`; caller now supplies non-rat pulse, outbreak ledgers, actor-target, and dated receipt proof. |
| `famine_adapt_natural_disaster_state` | State scope; positive Event 013 loss and the complete famine proof bundle. | Calls `famine_request_disaster_pressure`; it never creates evacuation or route deaths. | `013_natural_disasters_effects.txt`, `natural_disaster_apply_population_loss`; caller now supplies sequence, family, severity, driver, actor-target, and dated receipt proof. |
| `famine_validate_condemnation_receipt_exact` | Country scope with explicit `famine_condemnation_state` and `famine_condemnation_actor` targets; positive food, environment, transport, policy, actor, cause, people amount, generation, revision, and request identity proof. | Sets only temporary `famine_condemnation_valid`. | Shared by famine-owned condemnation wrappers; current famine decision surfaces contain no stale combined condemnation caller and remain fail-closed until an exact proof-owning decision route exists. |
| `famine_condemn_deliberate_starvation` | Exact famine condemnation receipt. | Adds the existing Condemnation source with `famine_condemnation_gain.deliberate_starvation`; no Deaths or migration effect. | Called once per state from `famine_record_exact_mortality_condemnation` only after exact famine deaths occur while extraction remains active. |
| `famine_condemn_relief_obstruction` | Exact famine relief-obstruction receipt. | Adds the existing Condemnation source with `famine_condemnation_gain.relief_obstruction`; no Deaths or migration effect. | No current exact caller census entry; API remains available and fail-closed. |
| `famine_condemn_concealment` | Exact hidden mortality/food-crisis concealment receipt. | Adds the existing hidden Condemnation source with `famine_condemnation_gain.concealment` and sets `famine_achievement_blockade_concealed_mortality` only after proof. | Called once per state from `famine_record_exact_mortality_condemnation` only after exact famine deaths occur while the crisis is concealed. |

## Famine proof contract

The owner must set the proof fields in the same state scope as the resolved food consequence or pass them into that state scope through explicit event targets and one-shot variables.

`famine_adapter_amount` is a positive people-denominated food consequence or the owner-approved nuclear estimate, never a route amount and never an already-applied death request for a second Deaths debit.

`famine_adapter_state_proven` identifies the exact state and must equal the current state ID; `famine_adapter_food_proven` identifies the food or food-route fact; `famine_adapter_environment_proven` identifies the environmental or contamination fact; `famine_adapter_transport_proven` identifies the transport or route-food fact; `famine_adapter_policy_proven` identifies the policy or relief-access fact; and `famine_adapter_actor_proven` must equal the ID of the valid `famine_adapter_actor` event target.

`famine_adapter_cause_proven`, `famine_adapter_source_proven`, `famine_adapter_generation`, `famine_adapter_revision`, and `famine_adapter_request_id` are mandatory owner-supplied receipt identity fields. The validator does not infer them from a modifier, country flag, stale amount, or evaluator date, and the adapter does not persist a generic consumed composite because the current Camp and CBRN owners use date-based fields that are not guaranteed unique for distinct same-date operations.

## Replay boundary

The exact owner consumes or rejects its source transaction before calling a famine adapter. Air Winter guards one state loss per `air_winter_cycle_id`, Black Plague guards one mortality pulse per `global.black_plague_pulse_sequence`, and the Natural Disaster, Camp, and CBRN callsites submit only their current accepted source transaction. The adapter validates state/actor binding and clears the complete temporary proof envelope after every attempt, but it is not a substitute for an owner transaction guard or a durable unique request identity.

The bounded `on_nuke_drop` callback is a chain-local direct pressure owner and does not cross the exact external adapter boundary. It supplies its own callback-local amount and actor proof to the famine and migration endpoints once per engine callback; no persisted adapter receipt is fabricated for it.

The source-specific `famine_request_*` operations are intentionally food-only public endpoints. The adapter file does not set `apply_food`, `apply_flight`, or any equivalent combined flag. If the current shared core exposes only a combined transitional endpoint, the parent must split that core endpoint before wiring these adapters.

The direct-death helpers are famine-owned only when the upstream owner proves an unapplied occupation-repression or forced-labor cause together with the same state-local famine proof bundle. A post-owner callback must not call them after a Deaths debit.

## Condemnation proof contract

Famine condemnation wrappers require `famine_condemnation_state` and `famine_condemnation_actor` event targets, a positive people-denominated affected amount, and independent state, food, environment, transport, policy, actor, cause, generation, revision, and request proofs.

The wrapper records evidence only after `famine_validate_condemnation_receipt_exact` succeeds. It does not infer a state from the country scope, a food stage from a flag, or a responsible actor from `ROOT`.

## Cleanup and ownership

The adapters create no recurring action, world scan, cohort row, or global event target. The direct-death helpers apply only the explicitly requested unapplied transaction; all other helpers create no population transaction. Every source-specific endpoint calls `famine_clear_state_local_food_receipt` after its success or rejection branch, which resets temporary inputs so a later call in the same parent effect block cannot inherit a stale proof bundle. The regular `famine_adapter_actor` target remains chain-local because the engine clears regular event targets at effect-chain end.

The famine achievement concealment flag is durable evidence and must not be cleared by famine recovery or migration cleanup.

## Unsupported owner seams

Air Winter, Camp, CBRN, Black Plague, and Event 013 now pass source-owned proof bundles at their exact applied-loss callbacks. Any callback that cannot provide a positive source ledger or actor target still fails closed in the shared validator; no death amount is promoted into proof by itself.

Generic occupation-law changes, strategic-bombing recency, war declarations, peace callbacks, event roots, cluster dispatch, and scenario intensity remain API-only until an owner supplies an exact state-local food receipt.
