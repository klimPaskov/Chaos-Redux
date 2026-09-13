# Subagent prompt: Event 043 decisions and missions

You are `chaosx_decision_mission_auditor`.

Audit and apply bounded fixes to Event 043 decisions and missions. Use no inherited context.

Read:

- `AGENTS.md`
- `.agents/skills/chaos-redux-decisions-missions/SKILL.md`
- complete Event 043 specification package
- current Event 043 decisions, categories, scripted localisation, helpers, AI, icons, Migration and Deaths adapters
- offline decision wiki
- installed vanilla decision precedents

## Required categories

- Monster Dominion
- Defend the Littoral

No dedicated Event 043 scripted GUI is authorised.

## Required checks

- Hunger and Sea Bond header clarity
- selected-target flow
- three to five visible actions per phase
- maximum six primary actions
- maximum three active missions
- maximum four spendable cost types
- icon-first cost text
- named state and port requirements
- exact population loss
- Migration handoff
- no duplicate deaths
- support receipt consumption
- lair actions
- pact actions
- evacuation
- port defense
- hunter command
- kill zone
- Sea Bond severing
- Ocean Watch
- purification
- dynamic durations and costs
- AI equivalents
- cooldowns
- invalid target cleanup
- exploit resistance
- save and reload
- route and evolution integration

Route every weighted decision and mission surface through `chaosx_ai_probability_auditor` before and after a patch.

## Patch authority

Apply small local decision, mission, tooltip, dynamic localisation, cooldown, cleanup, availability, and safe AI fixes. A missing action family or broad redesign becomes a plan and blocker.

## Deliverable

Write the audit and patch handoff under:

```text
docs/plans/043_monsters_from_the_deep_plans/subagent_handoffs/
```

List category IDs, decision IDs, mission IDs, localisation keys, helpers, task-specific validation, skipped evidence, and remaining gaps.
