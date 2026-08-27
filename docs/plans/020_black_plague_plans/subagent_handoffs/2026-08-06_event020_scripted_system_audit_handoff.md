# Event 020 scripted-system architecture audit handoff

Date: 2026-08-06

Owner: `chaosx_scripted_system_architect` (`/root/event020_scripted_system_audit`)

## Scope and outcome


One narrow defect was patched: `black_plague_scenario_seed_state` now checks `global.black_plague_scenario_rat_candidate_states` before appending an infected state, preventing duplicate candidate entries when a pre-existing infected fallback anchor is seeded.

No new scripted effect, trigger, script-constant category, GUI helper, or global event target was needed.

## Helper map

| Helper family | Scope | Inputs and outputs | Side effects | Main call sites |
|---|---|---|---|---|
| `black_plague_calculate_origin_weight` and `black_plague_select_weighted_mainland_origin` | State and root/any | State population, infrastructure, industry, prevention, resistance, transport, and controller context; emits a temporary ticket pool and `black_plague_selected_origin_state` | Saves the selected origin as a regular event target for the launch chain | `black_plague_start_natural_outbreak` in `common/scripted_effects/020_black_plague_effects.txt` |
| `black_plague_initialize_runtime`, `black_plague_register_current_state`, and `black_plague_rebuild_runtime_counts` | Root/state | Runtime generation, maintained state arrays, and country registries | Initializes global variables and arrays once, registers idempotently, and rebuilds counts | Natural outbreak, weekly scheduler, SCN-012 launch, and state pulse |
| `black_plague_apply_exposure`, `black_plague_apply_current_state_response`, `black_plague_apply_current_phase_growth`, and `black_plague_apply_current_state_mortality_once` | State | Temporary exposure route, amount, provenance, disease variables, response variables, and current pulse sequence | Mutates state phase/load/pressure/containment/treatment, invokes the exact population-loss adapter once per pulse, updates the global deaths ledger, and refreshes modifiers/registries | Natural spread, weaponized delivery, rat occupation, response callbacks, and scheduler |
| `black_plague_emit_current_state_spread`, `black_plague_queue_current_target_exposure`, and `black_plague_resolve_queued_exposures` | State/root | Source snapshot, physical route, target snapshot, and normalized exposure | Uses a two-phase ledger so newly established states cannot emit in the same pulse | `black_plague_run_spread_phase` from the scheduled pulse |
| `black_plague_rat_initialize_runtime`, `black_plague_rat_select_free_slot`, `black_plague_rat_create_from_state`, and `black_plague_rat_run_runtime_pulse` | Root/country/state | RTA/RTX package, candidate state, archetype signals, division floors, and pulse clocks | Maintains the finite Rat Nation carrier, country arrays, brood markers, growth, merger, King transfer, and defeat cleanup | Evolution III/IV, SCN-012 package, state-control hook, and scheduler |
| `black_plague_scenario_*` launch helpers | Root/state/country | Scenario intensity, continent anchors, candidate arrays, rat/King floors, and bootstrap flag | Performs preflight, reservations, seeding, RTA/RTX setup, scheduler nomination, air-source refresh, shared threat refresh, history, and success/failure cleanup | `black_plague_triggerable_scenario_launch` in `020_black_plague_scenario_effects.txt` |
| `black_plague_pay_response_cost`, `black_plague_process_country_response_pulse`, and shared response cleanup | Country/state | Positive payment inputs, response ownership variables, active-state arrays, and countermeasure progress | Debits resources, reconciles stale owners, processes countermeasure progress, cleans active response state, and rebuilds registries | Response action files, event `.902`, and weekly scheduler |

## Constants and tuning table

Event 020 uses the subsystem categories in `common/script_constants/020_black_plague_*_constants.txt`, including `black_plague_origin`, `black_plague_spread`, `black_plague_growth`, `black_plague_mortality`, `black_plague_response_*`, `black_plague_rat_*`, `black_plague_evolution_runtime`, `black_plague_scenario`, `black_plague_weaponization_program`, and identity/value/phase/route categories.


The weighted-origin ladder is centralized in `black_plague_origin`; spread route weights and exposure factors are centralized in `black_plague_spread`; mortality curve, response reduction, and population floors are centralized in `black_plague_mortality`; Rat Nation/King floors, growth, route bonuses, and terminal gates are centralized in the Rat categories; SCN-012 intensity targets and floors are centralized in `black_plague_scenario` and `black_plague_evolution_runtime`.

Residual literal zero checks and negative-one debit multipliers exist in a few legacy-adjacent surfaces (`020_black_plague_achievement_effects.txt`, `020_black_plague_weaponization_effects.txt`, and scenario triggers); they are not parser blockers and remain a style follow-up rather than a broad rewrite.

## Event targets, variables, flags, and cleanup

Global targets saved by the Event 020 package are `black_plague_origin_state`, `black_plague_origin_owner`, `black_plague_origin_controller`, `black_plague_scheduler_anchor_state`, `black_plague_rat_evolution_actor`, `black_plague_rat_king_defeat_actor`, and `black_plague_scenario_evolution_ii_port_state`.

Each global target has an explicit clear path in runtime initialization, evolution transition, King initialization/defeat, or SCN-012 success/failure cleanup.

Short-lived targets such as spread source/target/controller, response pulse state, spawn state, selected rat state, internal brood state, King expansion state, and weaponization delivery state use regular event targets and remain inside their initiating effect/event chain.

The SCN-012 bootstrap flag `black_plague_triggerable_scenario_bootstrap` gates narrative/event-log emissions and suppresses ordinary evolution/rat side effects while the transaction runs; both success and failure branches clear it.

SCN-012 failure branches clear scheduler, Evolution-II port, selected-rat, internal-brood, and King-expansion targets and release reservation flags. The scenario relaunch lock prevents a terminal or already-launched campaign from re-entering the bootstrap.

`black_plague_triggerable_scenario_suppressed_fire_once` is set by the fire-once suppression helper but is not read by the Event 020 root event; the actual suppression is performed by the global disabled/fired/fire-once arrays, matching the Soviet triggerable-scenario pattern. Treat this flag as telemetry unless a future root-event guard intentionally consumes it.

## Migration and duplication assessment

The disease lifecycle is already routed through `black_plague_apply_exposure`, `black_plague_apply_current_state_mortality_once`, and the state-owned scheduler, so spread, weaponization, rat occupation, and terminal takeover do not need separate disease categories or duplicate death transactions.

Response actions already converge on `black_plague_reset_response_payment`, `black_plague_pay_response_cost`, lane-start helpers, ownership reconciliation, and shared-state/country cleanup; extracting a larger generic response factory would alter design and is not recommended in this pass.

Rat Nation and Rat King operations already converge on finite-slot selection, the shared state phase/exposure effects, and the scheduler-owned pulse; the reusable RTA/RTX package does not add country tags during SCN-012.


## Patch details

Changed file: `common/scripted_effects/020_black_plague_scenario_effects.txt`.

Changed helper: `black_plague_scenario_seed_state`.

Change: append to `global.black_plague_scenario_rat_candidate_states` only when the state is infected-or-worse and not already present in that array; preserve the candidate marker flag on the appended state.

This prevents a pre-existing infected fallback anchor from being inserted twice, which could otherwise let the RTA spawn pass and internal-brood pass select the same state in one SCN-012 transaction.

## Validation evidence

Required offline Paradox wiki pages and the relevant vanilla documentation for effects, triggers, event targets, variables, meta effects, random lists, script constants, and scripted GUI were consulted before source review.

`hoi4.event_inspect` lint for selector `chaosx.nr20.1` completed with status `ok`, code `EVENT_INSPECTED_PARTIAL`, workspace `mod_chaos_redux_ea3b2d67c2c0`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/.../event-lint-c5c2ec44234b.json`, and zero blocking diagnostics; the workspace-wide pass deferred helper/lifecycle projections and reported 8,145 unresolved graph references in the oversized scan.

`hoi4.event_inspect` state-flow for the same selector completed with status `ok`, code `EVENT_INSPECTED_PARTIAL`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/.../event-state_flow-c5c2ec44234b.json`, and zero blocking diagnostics with the same workspace-wide deferral limitation.

`hoi4.gui_inspect` and `hoi4.gui_render` inspected the shared `chaosx_scenarios_window` before any GUI change; inspect artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/.../gui-inspect.13201b10a87f94a5.json` and render base `.../chaosx_scenarios_window-full.svg/png` completed with `GUI_INSPECTED`/`GUI_RENDERED`. No GUI rewrite was needed because this task did not own the shared settings window.

The required probability workflow began with adapter discovery and source inspection. `hoi4.probability_inspect` on `common/scripted_effects/020_black_plague_spread_effects.txt` using `random_list` produced `probability-inspect-a4ad50a7855d.json` with 12 candidates, `poolComplete=false`, and one unresolved input; the custom-pool inspection of `020_black_plague_effects.txt` produced `probability-inspect-5cb753ca9f2e.json` with zero candidates and no unresolved inputs; weaponization random-list inspection produced `probability-inspect-362254a8e39a.json` with 4 candidates, `poolComplete=false`, and one unresolved input.

Parallel probability inspections for the scenario and Rat Nation files returned the exact MCP blocker `INTERNAL_ERROR` with no artifact; those surfaces require a follow-up probability-auditor pass rather than source-only balance claims.


Live game launch and in-game validation were not performed, per repository policy; the user owns live consumer validation.

## Remaining risks and follow-up

The SCN-012 downstream failure path clears reservations and temporary targets but is not a full inverse transaction for already-mutated disease/country/evolution state; this is documented in the existing runtime handoffs and should remain a parent-level design decision.

Probability evidence is incomplete for scenario and Rat Nation source files because the MCP adapter returned `INTERNAL_ERROR`; no balance conclusion should be drawn from the source-only inspection of those files.

The Event MCP workspace scan is partial and GUI MCP diagnostics include unrelated global texture/context errors, so these artifacts are bounded evidence rather than a claim of whole-mod parser cleanliness.

No simplification was introduced by this subagent beyond the existing documented SCN-012 rollback limitation; no new helper was left without a call site.
