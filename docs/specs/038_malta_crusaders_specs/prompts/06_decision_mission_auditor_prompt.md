# Prompt for `chaosx_decision_mission_auditor`

Work with no inherited conversation context. Audit and make only bounded local patches to Event 38 decisions, missions, timed objectives, categories, and linked gameplay helpers.

Read `AGENTS.md`, `chaos-redux-decisions-missions`, `chaos-redux-events`, `chaos-redux-subagents`, and the complete Event 38 pack, especially `04_crusade_council_mechanic.md`, `07_decisions_missions_and_failure.md`, `12_holy_world_terminal.md`, `13_triggerable_scenario.md`, `23_acceptance_scenarios.md`, `25_decision_register.md`, and `28_balance_tuning_tables.md`.

Audit every action family:

- Crusade Council
- order demands and disputes
- regional campaigns
- settlements and direct commanderies
- principalities and charters
- relics
- Eleventh Crusade
- Holy World preparation and terminal actions
- hidden Teutonic and Atlantis actions
- scenario-only setup controls where they are decision-backed

Check lifecycle, visibility, availability, selected targets, exact named regions, trigger tooltips, costs, mission durations, success, failure, partial success, cooldowns, active mission caps, replacement of obsolete actions, AI equivalents, cleanup, stale targets, save persistence, multiplayer ownership, and exploit resistance.

No decision may have more than four spendable cost types. Cost text must be compact and icon-first. Avoid raw trigger dumps, passive checklist missions, repeated tiny rewards, political-power stores, free-unit loops, factory loops, claim spam, repeated settlement rewards, and actions that duplicate focus effects without new play.

Every visible phase should normally show three to five primary actions and no more than six. Active missions should normally stay between one and three. Use target selection and phased visibility rather than a wall of regional decisions.

Any AI weight, mission score, random selection, target score, or probability-bearing modifier needs the dedicated probability baseline, owner patch, and comparison cycle. Do not patch it without the named baseline evidence.

Patch small local defects and list exact decision or mission IDs changed. Write broad design gaps under `docs/plans/038_malta_crusaders_plans/` and stop. Write the mandatory handoff to `docs/plans/038_malta_crusaders_plans/subagent_handoffs/decision_mission_auditor.md`.
