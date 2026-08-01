# Event 016 World-Reaction Bridge Handoff

## Scope

Three existing world incidents now inform an active Kruger host without replacing their source mechanics:

- Event 032 missile sites record a rocketry-infrastructure lead.
- Event 044's space-race commitment records a public rocketry posture.
- Event 049's first mass-panic report records a public-risk shock.

Each bridge is a one-time causal receipt. None creates a project stage, free unit, Event Log row, evolution, new event path, asset, or 3D model.

## Gameplay files

- `common/script_constants/016_brilliant_scientist_directorate_constants.txt`
  - adds `brilliant_scientist_world_reaction` deltas for missile, space, and panic outcomes.
- `common/scripted_effects/016_brilliant_scientist_context_effects.txt`
  - adds `brilliant_scientist_record_missile_crisis`, `brilliant_scientist_record_space_race`, and `brilliant_scientist_record_mass_panic`.
- `events/032_missile_crisis.txt`, `events/044_space_race.txt`, and `events/049_mass_panic.txt`
  - add current-host-only tooltips and guarded hidden-effect calls after their existing choices.
- `common/scripted_effects/016_brilliant_scientist_effects.txt` and `common/scripted_effects/016_brilliant_scientist_country_effects.txt`
  - carry the three country receipts through ordinary transfer and fixed-tag sovereignty formation.
- `localisation/english/016_brilliant_scientist_l_english.yml`
  - adds the three player-facing causal tooltips.

## Runtime contract

The missile bridge writes `brilliant_scientist_missile_crisis_recorded` and its fixed-character counterpart, then applies Mandate +5, Dependence +5, Exposure +10, Project Capacity +5, Independent Capacity +5, and Grievance +5. The space bridge writes `brilliant_scientist_space_race_recorded` and applies Mandate +5, Dependence -5, Exposure +5, Project Capacity +5, Independent Capacity +10, and Grievance -5. The panic bridge writes `brilliant_scientist_mass_panic_recorded` and applies Mandate -5, Dependence +5, Exposure +15, Project Capacity -5, Independent Capacity -5, and Grievance +10. Each helper requires the active host, a missing country receipt, and a missing fixed-character receipt.

## Validation evidence

- Static source review checked all three helper guards, exact country and character receipt IDs, centralized deltas, and option order.
- Gameplay braces, unsupported comparison operators, localisation BOM, and `git diff --check` were checked on the owned files.
- No source event's ordinary technology, idea, construction, or stability effect was replaced.

## Remaining risks

The source events retain broad existing world-iteration behavior. Kruger State missile-site seizure, Singularity delivery, portal/alien space routes, secret panic suppression, and world-threat escalation remain separate design hooks. No model production or wiring was attempted.
