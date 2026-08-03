# Event 016 easy-access decision audit handoff

Date: 2026-08-03

## Scope

Parent review of the active-Kruger access tranche for the seven project-force batch decisions and six bespoke equipment archetypes. No models or new art were created.

## Findings and disposition

- Active Kruger is a direct access route for clone, robot, paleogenetic, xenobiological, exotic, portal, and temporal batch decisions once the matching project family is operational.
- Active Kruger is a direct access route for the six project-force equipment lines once the matching project stage exists.
- Concrete material, factory, command-power, temporal, capacity, batch-cap, one-shot, suspension, damage, and dismantling locks remain in force.
- The seven timed batch decisions now cancel if the decision layer shuts down or if the matching project family is no longer operational. A cancelled timer cannot grant its physical output after a project is suspended, damaged, or dismantled.
- Temporal guard production retains the normal temporal synchronization and debt checks for non-Kruger routes; active Kruger bypasses that duplicate action-board gate while keeping its project, cost, cap, and one-shot checks.

## Files reviewed

- `common/decisions/016_brilliant_scientist_kruger_state_clone_machine_decisions.txt`
- `common/decisions/016_brilliant_scientist_kruger_state_paleo_xeno_decisions.txt`
- `common/decisions/016_brilliant_scientist_kruger_state_canonical_and_exotic_decisions.txt`
- `common/decisions/016_brilliant_scientist_kruger_state_portal_temporal_decisions.txt`
- `common/units/equipment/016_brilliant_scientist_project_force_equipment.txt`
- `common/scripted_triggers/016_brilliant_scientist_raid_triggers.txt`

## Validation and remaining evidence

Static brace/operator scans and focused diff review are required before commit. Live decision-panel, timer-cancellation, stockpile-output, and AI-frequency acceptance remain user-owned; Hearts of Iron IV was not launched by the agent. The accepted KRG biological stockpile ledger remains blocked by the native reservation/outcome/cancellation/expiry callback contract, with no fallback or parallel ledger added.
