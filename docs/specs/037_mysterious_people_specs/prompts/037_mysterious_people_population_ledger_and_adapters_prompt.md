# Prompt: Event 037 ledger, world transaction, and adapters

Delegation prompt for `chaosx_scripted_system_architect`.
The parent pastes this prompt with the repository root, the exact paths below, and any decisions taken since, because the subagent receives no conversation context.

## Read first

- `docs/specs/037_mysterious_people_specs/specs/037_mysterious_people_spec_part_2_population_and_ledger.md` (the whole design for this task)
- Part 1 sections Valid state definition, Firing sequence, and Direct Chaos
- Part 3 sections Overpopulation Pressure, Famine connection, and Migration connection
- `docs/systems/civilian_transfer_system.md`, `docs/systems/famine_system.md` (Adapters), `docs/systems/migration_system.md` (Adapters)
- `common/scripted_effects/chaosx_dynamic_effects.txt` and `.md`, `common/scripted_effects/camp_administration_occupation_effects.txt` (`camp_occ_apply_population_credit`), `common/scripted_effects/civilian_transfer_effects.txt`, `common/scripted_triggers/humanitarian_validation_triggers.txt`

## Build

1. The neutral gain helper `apply_state_population_gain_without_recruitable_manpower_gain`, with a measured applied output, documented in `chaosx_dynamic_effects.md`.
2. The world transaction called from `chaosx.nr37.1`: stage resolution, one grant per valid state, share and backlog update, lazy settlement of states not processed since the last firing, country and world counts, hotspot selection, a firing identity that cannot replay, and the four Chaos milestones.
3. The settlement rate per state and the monthly self-rescheduling host pulse over registered countries.
4. State and national pressure, and the variables that drive the Newcomers modifier.
5. The Famine adapter call and the Migration flight request for qualifying hotspots.
6. The one finalization hook in the civilian transfer primitive, which blends the destination share and removes measured departures from the origin backlog.
7. Ownership-change handling through the existing `on_state_control_changed` path.

All tuning goes in `common/script_constants/037_mysterious_population_constants.txt`.
No recurring whole-world scan, no edit to Famine or Migration ledgers, and no population removal by Event 037.

## Handoff

Write the handoff to `docs/plans/037_mysterious_people_plans/` with changed files, identifiers, constants, call sites, the engine result for recruitable manpower, checks run, and open risks.
Patch only inside this scope, and return broader gaps as a plan.
