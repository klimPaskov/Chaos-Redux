# Prompt for `chaosx_decision_mission_auditor`

Spawn with `fork_context=false`.

Repository root: `<MOD_ROOT>`.

Audit the implemented famine, evacuation, border, reception, integration, resettlement, and return decisions against:

- the complete source specs
- `famine_and_migration_system_decision_map.csv`
- `famine_and_migration_system_decision_mission_prompt.md`
- the AI probability reports

Check and apply only bounded fixes for:

- category hidden, emerging, active, resolution, and dormant phases
- three to five normal actions and no more than six
- one to three active missions
- one primary value and no more than two supporting values
- no more than four spendable costs per action
- correct texticons and dynamic cost text
- meaningful missions with named routes and states
- selected-target and stale-target cleanup
- AI validity
- cooldowns and one-shot guards
- origin and destination population conservation
- border closure and trapped populations
- voluntary and forced return distinction
- decision clutter
- exploit risk
- focus or event adapter hooks actually implemented

Any weighted patch requires the separate audit, patch, compare cycle.

Write a handoff under:

```text
docs/plans/famine_and_migration_system_plans/subagent_handoffs/decision_mission_audit.md
```
