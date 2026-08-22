# Event 016 project-force equipment loader and causality handoff

Date: 2026-08-02

Status: implemented in the current branch and documented for parent review.

## Scope

The six Event 016 project-force equipment archetypes now use loader-safe file-local family and stage values inside their `can_be_produced` blocks. Each gate is independent and requires the matching project ledger to reach deployment, carried Kruger or host completion history, the required country and state facilities, and an operational project state. Production is denied when the family is suspended, damaged, or dismantled. Xenobiological equipment additionally requires exactly one recorded control mode. All six archetypes remain non-lend-leasable.

## Covered equipment

- `kruger_portal_equipment`
- `kruger_robot_equipment`
- `kruger_paleogenetic_equipment`
- `kruger_xenobiological_equipment`
- `alien_laser_weapon_equipment`
- `kruger_temporal_equipment`

## Evidence

- `common/units/equipment/016_brilliant_scientist_project_force_equipment.txt` contains the six family constants, deployment-stage constant, and the six expanded production gates.
- The matching scripted triggers in `common/scripted_triggers/016_brilliant_scientist_project_force_triggers.txt` remain the reusable history and operational reference; the equipment blocks retain explicit fields because the loader-sensitive equipment surface needs static values.
- The current source expansion is present in ancestor commit `26b659fb7`; `41ad06d13` is retained only as historical evidence of the earlier macro-repair line. This handoff records the current Event 016 contract and does not add another gameplay path.

## Validation evidence

- The equipment source has balanced braces and no unsupported `<=` or `>=` operators.
- All six equipment archetypes have `can_be_produced` blocks and `can_be_lend_leased = { always = no }`.
- The six stage indices map to the existing Event 016 project ledger order: teleportation 6, robotics 8, paleogenetics 9, xenobiological synthesis 10, alien arms 12, and temporal 13.
- The xenobiological gate retains the four mutually exclusive control-mode branches used by the scripted trigger.

## Remaining risks

No in-game production or save-state validation was run. The seven Event 016 3D packages remain intentionally deferred; ordinary HOI4 archetype sprites are still the runtime fallback until those packages are separately approved and produced.
