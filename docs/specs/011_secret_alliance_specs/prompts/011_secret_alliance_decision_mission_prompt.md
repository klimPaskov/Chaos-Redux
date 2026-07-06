# Follow-Up Decision And Mission Prompt: Event 011 Secret Alliance

Use `hoi4-decisions-missions` before implementing Event 011 countermeasures.

Source package:

- `docs/specs/011_secret_alliance_specs/specs/011_secret_alliance_spec_part_3_decisions_sabotage.md`
- `docs/specs/011_secret_alliance_specs/matrices/011_secret_alliance_decision_map.md`
- `docs/plans/011_secret_alliance_plans/011_secret_alliance_decision_mission_handoff.md`

Implement:

- `common/decisions/categories/011_secret_alliance_categories.txt`
- `common/decisions/011_secret_alliance_decisions.txt`
- selected-target pattern for known pact members
- active mission cap and cleanup
- AI equivalents that bypass human selector
- Evolution II, Evolution III, war phase, and aftermath category states
- border-war helper using WTT-style paired states and no state transfer by default

Decision families:

- counterintelligence
- preparation
- exposure
- negotiation and splitting
- industrial protection
- propaganda and diplomacy
- border incidents and border wars

Every decision or mission needs:

- concrete cost beyond political power where appropriate
- custom blocked tooltip
- success effect
- failure or risk effect
- AI weight or AI blocker
- cleanup path
- state, target, and event validity checks

Do not:

- show the full category before Evolution II
- expose the hidden full roster without evidence
- let border wars transfer states by default
- allow target or mission state to go stale
- add daily or weekly world iteration

