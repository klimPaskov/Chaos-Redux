# Event 020 runtime floor and actor correction handoff

Date: 2026-08-01

## Scope

This bounded runtime tranche hardens the source-complete Event 020 gameplay core without producing rat models or adding a third country tag. `RTA` remains the reusable Rat Nation carrier and `RTX` remains the separate Rat King.

## Implemented

- Natural Rat King initialization now transfers the Royal Basin before setting the `RTX` capital and creating the natural Royal Brood Guard, so the guard has a valid friendly spawn state.
- The natural King guard count is centralized in `black_plague_rat_pool.king_starting_guard_divisions`; SCN-012 defers the natural minimum while its exact intensity floor is assigned.
- SCN-012 reconciles both rat division counters against live `num_divisions` before topping up, and its postcondition verifies the RTA and RTX division floors.
- SCN-012 rejects a stale Evolution IV flag unless a living RTX King exists, before disease or country mutation begins.
- Evolution II clears its actor-capture state on activation and remains pending in a natural campaign until the first successful overseas destination captures one verified human port controller; SCN-012 supplies its verified dock-signal destination during bootstrap without emitting the natural news event.
- Occupation Infection Drive cannot be repaid while its timed 60-day exposure consumer is active.
- Ordinary shared state-action custom-cost colouring now follows the selected state's population-scaled material cost. Train-routed Port Inspections, Relief Corridor, and Evacuate Threatened Perimeter also show the required train reserve.
- Missing blocked custom-cost localisation was added for the Royal Strike and weaponization stockpile controls.
- The achievement matrix now describes Crown of One Continent as a pre-terminal route achievement, matching its runtime trigger.

## Files changed

- `common/script_constants/020_black_plague_rat_constants.txt`
- `common/scripted_effects/020_black_plague_rat_effects.txt`
- `common/scripted_effects/020_black_plague_effects.txt`
- `common/scripted_effects/020_black_plague_evolution_effects.txt`
- `common/scripted_effects/020_black_plague_scenario_effects.txt`
- `common/scripted_triggers/020_black_plague_scenario_triggers.txt`
- `common/scripted_triggers/020_black_plague_evolution_triggers.txt`
- `common/scripted_triggers/020_black_plague_shared_response_triggers.txt`
- `common/decisions/020_black_plague_rat_decisions.txt`
- `common/decisions/020_black_plague_shared_response_decisions.txt`
- `localisation/english/020_black_plague_rat_decisions_l_english.yml`
- `localisation/english/020_black_plague_weaponization_l_english.yml`
- `docs/specs/020_black_plague_specs/matrices/achievement_matrix.md`
- `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-01_event20_runtime_floor_actor_correction_handoff.md`

## Validation evidence

- Focused `hoi4_event_inspect` lint on `events/020_black_death.txt` returned `status: ok`, `code: EVENT_INSPECTED_PARTIAL`, no blockers, and `blockingDiagnostics: 0`.
- The Event 020 namespace scan found 53 definitions and 53 references with no undefined IDs.
- The rat tag scan found exactly `RTA` and `RTX`.
- Touched Event 020 scripts are brace-balanced and contain no unsupported `<=` or `>=` operators.
- The ten Event 020 English localisation files retain UTF-8 BOM encoding.
- The decision audit found 59 custom-cost pairs with base and `_blocked` localisation, and the train affordability helper is used only by the three train-routed state actions.

## Remaining risks and deviations

- No Hearts of Iron IV process was launched; live scenario, natural King transfer, pulse timing, and save-reload validation remain user-owned checks.
- Evolution II's natural route now defers the milestone row until the first successful overseas destination; the new actor capture is statically wired but not empirically proven in a live save.
- SCN-012 preflight and retry cleanup are implemented, but a complete inverse rollback of every disease and transfer mutation after a late failure is not proven.
- The defensive stale-Evolution-IV recovery branch remains intentionally retained as a guarded recovery hook.
- Broader queued narrative/presentation, source-frame crisis animation, release attribution, and focused live balance work remain outside this bounded runtime correction.
- Rat 3D models and skeletal animations are intentionally not produced by user instruction and are not load-time prerequisites.
