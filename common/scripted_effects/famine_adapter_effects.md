# Famine owner adapters

This file documents `famine_adapter_effects.txt`. These helpers accept only a state-local food receipt from an owner that has already proven the affected state, food consequence, environmental context, transport consequence, policy context, responsible actor, causal generation, revision, and one-shot request identity.

Food-pressure adapters register only their proven food consequences.
Food-observation helpers assess the existing pressure model for explicit state candidates and publish famine-owned facts without granting food, reception services or route authority.
Neither family sets a flight channel, creates a migration cohort, transfers civilians or records route deaths.

## Helper map

| Helper | Scope and required inputs | Output and side effects | Owner call sites and status |
| --- | --- | --- | --- |
| `famine_observe_migration_food_context` | Exact valid civilian state with positive native population, valid present model fields, complete declared owner contexts and complete durable inputs for a known crisis. | Returns temporary `famine_food_observation_result`. Uses missing neutral normal-model defaults, current context and the shared calculation helpers. Preserves existing stock, pressure, stage, clocks and exposure. A newly material stable-stage assessment fails destination proof and queues only this state without simulation-active or category flags. | Called by `migration_consume_famine_food_safety` for explicit origin, adjacent destination and registered reception candidates. No free service, reserve stock or route proof is supplied. |
| `famine_record_food_assessment` | State after the current shared component/score calculation. | Sets `famine_food_assessment_current` and records or clears `famine_food_observation_pending_material` from stable stage plus the existing supply-strain score threshold. | Assessment provenance only. Does not commit stages or change stock, clocks, population, categories or reports. |
| `famine_publish_migration_food_safety` | State scope with a current real assessment, no pending-material stable-stage assessment, and initialized famine stage, pressure, production, transport, and governance facts. | Publishes a proven schema, monotonic generation/revision, and bounded `famine_to_migration_*` fields. It never initializes an untracked state. Missing assessment or facts call the invalidator and fail closed. | Called after famine evaluation and by bounded migration consumers only after accepted observation. |
| `famine_invalidate_migration_food_safety` | State scope when facts or assessment are absent, changed, invalid or retired. | Clears current assessment and projection proof/fields, then dirties an already-registered migration reception candidate. It does not clear migration obligations or a pending simulation-stage assessment. | Famine cleanup/control changes and rejected observer/publisher attempts. |
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
| `famine_adapt_acid_rain_state` | State scope; positive temporary `acid_rain_humanitarian_amount` from an exact applied Acid Rain loss, a newly reached tier-2 or tier-3 aftermath, or a completed large evacuation, plus the complete famine proof bundle with Acid Rain source and generation identities. | Calls `famine_request_disaster_pressure` once per accepted source transaction; it never creates a migration cohort, route deaths, or population movement. | `033_acid_rain_aftermath_effects.txt`, `acid_rain_register_humanitarian_pressure`, called from the exact pulse gateway, the aftermath tier assessment, and evacuation completion. |
| `famine_validate_condemnation_receipt_exact` | Country scope with explicit `famine_condemnation_state` and `famine_condemnation_actor` targets; positive food, environment, transport, policy, actor, cause, people amount, generation, revision, and request identity proof. | Sets only temporary `famine_condemnation_valid`. | Shared by famine-owned condemnation wrappers; current famine decision surfaces contain no stale combined condemnation caller and remain fail-closed until an exact proof-owning decision route exists. |
| `famine_condemn_deliberate_starvation` | Exact famine condemnation receipt. | Adds the existing Condemnation source with `famine_condemnation_gain.deliberate_starvation`; no Deaths or migration effect. | Called once per state from `famine_record_exact_mortality_condemnation` only after exact famine deaths occur while extraction remains active. |
| `famine_condemn_relief_obstruction` | Exact famine relief-obstruction receipt. | Adds the existing Condemnation source with `famine_condemnation_gain.relief_obstruction`; no Deaths or migration effect. | Called by `famine_condemn_corridor_obstruction` and `famine_condemn_relief_contract_interruption`. |
| `famine_condemn_corridor_obstruction` | Origin STATE of an evacuation corridor that its receiving country rejected or let expire, before corridor cleanup; the state must be at the famine or catastrophic stage, and `humanitarian_corridor_full_request_headroom_is_valid` must hold, so the receiver's safe front and current reception capacity had room for the whole request. | Condemns the receiving country once per corridor generation with the measured `humanitarian_corridor_transfer_people` as the affected people, the origin state, the route generation and the cohort as identity, then clears the envelope. | `humanitarian_corridor_reject_offer` and the response-deadline branch of `humanitarian_corridor_expire`. |
| `famine_condemn_relief_contract_interruption` | Famine STATE whose foreign relief contract just failed before delivery, with its contract fields still present; the donor state must now be held by a country at war with the relief actor. | Condemns that capturing country once per contract generation; the affected people are the live population scaled by the contract amount against the reserve import it was sized for, and the donor state is the request identity. Clears the envelope. | The failure branches of `famine_relief_deliver_contract`, and the four relief decisions when their paid contract is no longer current at removal. |
| `famine_apply_hunger_lines_scenario_pressure` | Any scope, after a successful Hunger Lines launch; reads `global.cannibalism_node_states` and `global.cannibalism_scenario_last_intensity`. | For each live node state (`cannibalism_active_node`, valid civilian state) whose `famine_scenario_food_context_until_date` has passed or is absent: writes `famine_scenario_food_context_pressure` and a new expiry `context_days` ahead, submits `famine_request_scenario_pressure` for `food_share` of the population, and submits `migration_request_scenario_pressure` for `flight_share` of the population capped above `protected_origin_share` when it reaches `minimum_flight_people`. Returns temporary `famine_hunger_lines_state_count`; clears the request envelopes. No map scan, no Event 014 write, no population change. | The Event 014 branch of `trigger_selected_chaosx_scenario` in `chaosx_triggerable_scenarios_effects.txt`, gated on the caller-declared `cannibalism_scenario_setup_result`. Tuning: `famine_hunger_lines_scenario` in `famine_adapter_constants.txt`. |
| `famine_clear_condemnation_envelope` | Any scope. | Resets every `famine_condemnation_*` proof value and the shared death and contamination inputs. | Called after every obstruction wrapper attempt. |
| `famine_condemn_concealment` | Exact hidden mortality/food-crisis concealment receipt. | Adds the existing hidden Condemnation source with `famine_condemnation_gain.concealment` and sets `famine_achievement_blockade_concealed_mortality` only after proof. | Called once per state from `famine_record_exact_mortality_condemnation` only after exact famine deaths occur while the crisis is concealed. |

## On-demand food observation

An absent normal input represents the existing model's neutral loss-pressure baseline.
It does not prove physical crop output, a warehouse stockpile, spare housing, medical beds or an operating route.
The observer must collect current supported state, occupation, environmental and owner context before recording a current assessment.
Present malformed component/pressure/stage/negative stock or exposure data is rejected rather than clamped into a healthy receipt.
A declared surface/profile context needs all of its owner component fields, and an established positive stage needs its durable model, stock, exposure and clock inputs.
Current positive stage flags while simulation is active, or any current famine severity modifier, also require a complete valid numeric stage and durable model.
Those current severity markers must match the numeric stage, rather than allowing missing or inconsistent state to become stable through initialization.
Quiet retired historical stage flags alone, without active simulation or a current severity modifier, do not assert a current crisis and may receive a fresh neutral-model observation.

Observation may fill missing neutral initializer defaults but never resets an existing crisis stage, input, pressure, exposure, reserve amount or timer.
It does not call reserve refresh/update/replenishment/import/release, pressure decay, stage transition, mortality, survivor-flight, report, category or retirement effects.
The current blockade calculation reads existing exposure without advancing it.
Stable normal observation does not register famine simulation.
When the current score reaches the existing supply-strain threshold while simulation stage is still stable, the destination receipt stays invalid and only that exact state is enqueued through the existing sparse runtime with `famine_food_observation_pending_job`.
The observation enqueue does not set `famine_food_security_active`, category/phase flags, reports or incidents.
The registered-state processor consumes that pending job and activates the normal evaluator at the ordinary simulation boundary.
Requested assessment stage is distinct from committed simulation stage.
The normal evaluator records assessment after its stage logic so the pending-material flag clears when ordinary stage recognition or safe recovery occurs.
Stable-stage retirement refuses a current score at or above the existing supply-strain threshold, preserving the exact pending state's candidate timer.
When the score later falls below that threshold and the remaining famine obligations are clear, ordinary retirement removes the simulation registration and observation flags.
Cleanup clears pending-job, pending-material and current-assessment flags together.
Control changes invalidate the food assessment before its later bounded reassessment.

Example, in the exact state selected by a bounded migration owner:

```text
set_temp_variable = { famine_food_observation_result = constant:humanitarian_runtime.zero }
famine_observe_migration_food_context = yes
if = {
	limit = { check_variable = { famine_food_observation_result = constant:humanitarian_runtime.one } }
	famine_publish_migration_food_safety = yes
}
```

A valid assessment result does not mean the state is an eligible destination.
The published committed stage, original migration capacity, policy, native hazard, scope and route gates remain binding.
The observer creates no shelter/medical service, capacity, event target, cohort, population or Deaths output.

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

Generic occupation-law changes, strategic-bombing recency, war declarations, peace callbacks, event roots, and cluster dispatch remain API-only until an owner supplies an exact state-local food receipt.
Scenario intensity is consumed for the Hunger Lines scenario only, through `famine_apply_hunger_lines_scenario_pressure`; other scenarios remain API-only.
