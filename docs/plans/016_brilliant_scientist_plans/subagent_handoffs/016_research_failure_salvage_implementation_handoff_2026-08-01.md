# Event 016 Research-Failure Salvage Handoff

## Scope

The Event 060 cross-event hook is implemented as one bounded intervention for an active Doctor Warren Kruger Directorate. It preserves the existing ordinary failure path and does not create a new Event 016 evolution, project reward, Event Log row, country route, art asset, or 3D model dependency.

## Gameplay files

- `common/script_constants/016_brilliant_scientist_directorate_constants.txt`
  - `brilliant_scientist_research_failure_salvage`
  - `brilliant_scientist_research_failure_salvage_ai`
- `common/scripted_triggers/016_brilliant_scientist_triggers.txt`
  - `brilliant_scientist_can_prevent_research_failure`
- `common/scripted_effects/016_brilliant_scientist_context_effects.txt`
  - `brilliant_scientist_prevent_research_failure`
- `events/060_research_failure.txt`
  - `chaosx.nr60.2.b`
- `localisation/english/060_research_failure_l_english.yml`
  - option and effect tooltip keys

## Runtime contract

The option is visible only to the current host while the world-end flag is absent, the permanent receipt is absent, and the country has more than 49 Political Power. Choosing it spends 50 Political Power, keeps the current research-slot total, and sets `brilliant_scientist_research_failure_prevented`. The existing bounded effects move Mandate by 10, Dependence by 15, Exposure by 10, Project Capacity by -5, Independent Capacity by -10, and Grievance by 10. The AI favors salvage, especially during war or under a secret Directorate, and public science reduces that preference.

## Validation evidence

- Event-level inspection targeted at `chaosx.nr60.2` after the edit.
- Gameplay braces and localisation BOM checked on all touched files.
- Exact option and helper identifiers checked for duplicate definitions.
- The event remains a separate Event 060 chain and has no Event 016 log, evolution, project, claim, actor, or model reference.

## Remaining risks

The reserved `brilliant_scientist_alien_material_authenticated` trigger remains intentionally unwritten. It is a separate Xenobiological Theory evidence gate and needs a future authenticated nonhuman biological-material outcome rather than being aliased to Antarctic recovery or spacecraft wreckage.
