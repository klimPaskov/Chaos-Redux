# Event 025 decision and mission auditor prompt

Spawn `chaosx_decision_mission_auditor` with `fork_context=false` after the Event 025 decision, mission, and action-helper implementation exists.

Read the full Event 025 spec package and live decision files. Audit and apply only small bounded fixes inside Event 025 for:

- phase visibility and replacement
- three to five primary actions per phase, hard maximum six
- one to three active missions
- maximum four spendable cost types
- matching texticons
- costs beyond political power
- route, outpost, survey, rival, recovery, fragment, and aftermath objectives
- success, partial success, and failure logic
- dynamic costs and durations
- selected-rival cleanup
- target-specific and family cooldowns
- hostile-action counterplay and evidence
- AI access to the same helpers and costs
- reserve-floor behavior
- withdrawal and winner cleanup
- duplicate or low-impact actions
- exploit loops
- clear tooltips and blocked reasons

Any weighted change requires the separate probability audit, owner patch, and compare cycle. Do not tune weighted logic without that evidence.

Do not create a new mechanic, country, focus tree, GUI system, or route family. Broad gaps become a plan for the parent.

Write the handoff to:

`docs/plans/025_alien_technology_in_antarctica_plans/subagent_handoffs/025_decision_mission_auditor_handoff.md`
