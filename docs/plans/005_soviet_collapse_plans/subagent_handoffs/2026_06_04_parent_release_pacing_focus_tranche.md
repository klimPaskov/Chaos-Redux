# Event005 Parent Tranche: Release Pacing and Focus Cleanup

Date: 2026-06-04
Owner: parent Codex agent
Scope: Soviet Collapse release pacing, Ukraine focus layout, and narrow Far Eastern/Tunguska focus reward cleanup.

## Files Changed

- `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- `common/script_constants/005_soviet_collapse_constants.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `localisation/english/005_soviet_collapse_l_english.yml`

## Implemented Behavior

- Progressive Soviet release candidates no longer admit every possible Soviet-region country at once.
- Calm starts remain base-republic focused.
- Internal/vanilla republic follow-on releases begin from chaos tier 1 / Gathering Storm through the internal release pool.
- Custom pressure successors remain separated from the internal/vanilla follow-on pool.
- The internal follow-on release count is clamped against the internal follow-on cap, so tier 1 internal releases are not accidentally reduced to zero by the normal follow-on release cap.
- Ukraine focus tree duplicate coordinates are removed.
- Ukraine continuous focus panel moved farther right so it no longer sits over the right-side expansion/high-chaos branch.
- Ukraine random anti-air reward in the bread-line helper was replaced with supply hub/infrastructure style rewards.
- `FEV_war_plan` now clearly acts as an expansion/assault route by using annexation filtering, expansion claims, high-chaos neighbor expansion pressure, and assault columns.
- `FEV_pacific_between_empires` now deepens Japan-facing diplomacy when Japan exists, including the Japanese liaison decision tooltip, foreign League pressure, mutual opinion modifiers, decryption against Japan, and reciprocal AI support strategy.
- `TSC_claim_the_impact_zone` and `TSC_sky_over_siberia` now carry annexation filters to match their expansion and assault behavior.

## Validation

- Balanced braces checked for all touched files.
- `rg -n "<=|>="` returned no unsupported comparison operators in touched files.
- `git diff --check` passed for touched files.
- `localisation/english/005_soviet_collapse_l_english.yml` still has UTF-8 BOM.
- `git status --short -- gfx/flags` returned no changes.
- Local focus parser reported no duplicate coordinates for `soviet_collapse_ukraine_focus_tree`, `TSC_soviet_collapse_focus_tree`, or `FEV_soviet_collapse_focus_tree`.

## Remaining Gaps

- Ukraine still has automated pathline crossings. The exact-coordinate and too-close-focus issues are resolved, but full visual perfection needs a deeper manual branch-layout pass.
- Several short chaos trees remain shallow compared with the focus-tree branch-depth standard.
- The broader request to make every Soviet Collapse focus tree clearly split into political, industry, and expansion branches is not complete in this tranche.
- The working tree was already broadly dirty before this pass, so this tranche was not committed.
