# Event005 Soviet Collapse Parent Tranche: PRA Authority Idea Churn

## Scope
- Reduced helper-mediated idea churn for the Pale Railway Authority focus route.
- Did not touch flag assets or interface flag definitions.

## Changed Files
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `localisation/english/005_soviet_collapse_l_english.yml`

## Implementation Notes
- Reworked `soviet_collapse_update_pra_authority_idea` so it no longer removes every PRA authority spirit and re-adds the same current spirit whenever a focus calls the helper.
- Each route stage now removes only stale non-current PRA authority spirits.
- The current stage spirit is only added when missing.
- Reworked `soviet_collapse_update_consolidated_republic_ideas` so the obsolete staged republic-spirit cleanup runs once per country through `soviet_collapse_legacy_staged_ideas_cleanup_checked`.
- Removed the duplicate component clamp inside the same updater. Component clamping still happens before sponsor-pressure updates through `soviet_collapse_clamp_republic_country_components`.
- Moved the generic mobile-column payoff out of every `soviet_collapse_apply_focus_military_consolidation` call and into the first and second military route-depth milestones. Military focuses still build readiness every time, but new formations arrive when the route meaningfully develops.
- Updated `soviet_collapse_apply_focus_military_consolidation_tt` to describe the milestone-based formation payoff.

## Remaining Risks
- This is a focused churn fix, not the full Soviet Collapse focus-tree depth cleanup.
- Other helper-mediated staged idea systems still need the same review pass before the broader focus reward bloat can be considered resolved.
