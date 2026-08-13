# Independence Wave decision and mission implementation prompt

Implement the complete decision, mission, and mechanic action layer for Chaos Redux Event 6.

Read:

- `AGENTS.md`
- `.agents/skills/chaos-redux-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-focus-trees/SKILL.md`
- Event 6 spec parts 1 through 7
- `matrices/006_decision_mission_map.csv`
- `matrices/006_wave_tuning_model.csv`
- `matrices/006_idea_lifecycle_matrix.csv`
- `matrices/006_ai_strategy_matrix.csv`

## Required mechanic values

Implement visible, dynamic state for:

- Founding Legitimacy
- International Recognition
- Government Capacity
- Security Readiness
- Post-Release Instability
- Former Host Relationship
- per-patron influence and dependency
- network standing
- league values when the league exists

Centralize thresholds, caps, gains, losses, duration bands, AI weights, and scaling in documented constants or tuning helpers.

## Required decision families

Implement every accepted row in `matrices/006_decision_mission_map.csv`.

The families are:

- founding
- government construction
- recognition
- security and army
- former-host relations
- patron support and anti-puppet play
- network cooperation
- league congress, votes, goals, rescue, and leadership
- border survey, plebiscite, negotiation, ultimatum, and integration
- formable discovery, formation, and post-formation integration
- high-chaos breakaway sponsorship and coordinated reclamation

## Design rules

- Decisions represent real actions.
- Missions require map, unit, supply, diplomatic, or institutional objectives.
- Do not build a political-power store.
- Use equipment, manpower, army XP, civilian factory burden, trains, convoys, fuel, unit commitment, local support, recognition, legitimacy, capacity, cohesion, and time where appropriate.
- Use dynamic costs and duration bands.
- Name regions and objectives through custom tooltips or scripted localisation.
- Provide success, failure, partial success, cooldown, and cleanup.
- Hide obsolete actions.
- Use phase gating, active mission caps, selected target flow, and route locks.
- AI must use equivalent effects without the human scripted GUI.
- Prevent free units, repeated depot rewards, recognition farming, patron aid loops, reserve duplication, core spam, and repeated formable rewards.

## Former-host and origin safety

- Only Event 6 origin countries receive these categories.
- Existing countries are not converted because they share a tag.
- Soviet Collapse origin countries do not receive Event 6 decisions.
- Clean up active missions and targets on annexation, voluntary reunion, formable transition, host death, league dissolution, and route closure.

## Formables

Use the family registry rather than one-off country code.

- focuses reveal or prepare formation
- decisions verify territory, members, consent, route, recognition, and legitimacy
- negotiated members can receive broader immediate integration
- conquered or disputed regions use staged missions
- every new tag or cosmetic tag created for Event 6 ends in `X`

## Scripted GUI

A custom panel can show values, targets, and status. Buttons must call the same balanced helpers as decisions. Provide cost, requirement, blocked, warning, and result text. Animation clarifies state and never substitutes for readable information.

## Validation and handoff

After implementation, run a decision and mission audit and write a handoff under:

`docs/plans/006_independence_wave_plans/subagent_handoffs/`

Report:

- files changed
- decision, mission, category, helper, variable, flag, and target IDs
- rows implemented or intentionally rejected
- dynamic cost and duration model
- AI paths
- cleanup paths
- exploit controls
- meaningful scenario checks
- remaining simplifications or blockers
