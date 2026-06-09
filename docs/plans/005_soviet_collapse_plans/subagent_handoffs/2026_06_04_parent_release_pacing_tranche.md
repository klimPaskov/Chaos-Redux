# Event005 Parent Release Pacing Tranche

Date: 2026-06-04

## Scope

Adjusted Soviet Collapse release pacing so the live event no longer releases every possible Soviet republic at the opening or after each normal progressive release.

## Changed Files

- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- `common/script_constants/005_soviet_collapse_constants.txt`
- `common/script_constants/chaosx_triggerable_scenarios_constants.txt`

## Implementation Notes

- Removed the broad dynamic follow-on release from `soviet_collapse_release_initial_republics`.
- Removed the broad dynamic follow-on release from `soviet_collapse_finish_progressive_release`.
- Restricted dynamic all-core progressive candidates to chaos tiers instead of `opening_wave_active` or `first_wave_recorded`.
- Restricted internal republic progressive candidates to chaos tiers.
- Restricted custom chaos successor progressive candidates to chaos tier 3+ or the explicit triggerable chaos scenario flag.
- Reduced non-chaos regional cascade follow-on releases from 8 to 2 so calm worlds stay gradual.
- Kept terminal collapse and triggerable scenario paths broad, so Union Unmade and standalone scenario release behavior remain separate from live staged pacing.
- Increased triggerable Soviet Collapse scenario force scaling so stronger republics still spawn much larger armies when the standalone scenario is launched.

## Validation

- Brace balance checked for edited effects, triggers, and constants: all zero.
- `git diff --check` on edited files: clean.
- Unsupported operator scan for `<=` and `>=` on edited files: clean.
- Flag asset status checked separately; no `gfx/flags` or `interface/flags` files changed.

## Remaining Work

- Focus-tree cleanup remains open. The read-only focus audit is available at `2026_06_04_163258_focus_tree_auditor_event005_full_readonly_audit.md`.
- Layout, indirect idea churn, and route-depth fixes still need implementation across the audited focus trees.
