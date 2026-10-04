# Scripted GUI state and effect contract skill handoff

Disposition: implemented.

Acceptance basis: the parent assigned a bounded update to the existing scripted GUI skill after a review fixture misclassified an action's availability.

Changed files:

- `.agents/skills/chaos-redux-scripted-gui/SKILL.md` — added one general scenario-review rule requiring source availability triggers, effect-time rechecks, side effects, and reason-specific disabled predicates to be traced before a reference or fixture is declared route-valid or impossible.
- `docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/gui_state_effect_contract_skill_handoff_2026-09-27.md` — records the skill change and its validation.

The reported failure treated a condition still present before an action as proof that the action must be locked, even though the action could start and clear that condition. The new rule makes reviewers check the actual action contract and provide a valid predicate for each locked fixture before approving its visual state. The skill text contains no event-specific identifiers or one-off implementation details.

Validation: `python C:/Users/klimp/.codex/skills/.system/skill-creator/scripts/quick_validate.py .agents/skills/chaos-redux-scripted-gui` returned `Skill is valid!`. Focused diff review confirmed the new rule sits in scenario coverage, contains no event-specific terms, and preserves concurrent edits. `git diff --check -- .agents/skills/chaos-redux-scripted-gui/SKILL.md` found no whitespace error.

No gameplay files or fixtures were changed. No game launch was performed.
