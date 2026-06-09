# Event005 Parent Handoff: Focus Helper Spam Cleanup Tranche

## Scope

Parent-side cleanup for a narrow subset of Event005 Soviet Collapse focus reward spam.

This is not a completion claim for Event005. The full focus-tree rework, release pacing, evolution parity, scenario release coverage, and chaos-country depth remain active work.

## Files Changed

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_republics.txt`
- `localisation/english/005_soviet_collapse_l_english.yml`

No flag, sprite, image, GFX, GUI, or asset files were edited.

## Findings From Parent Scan

- Direct idea effects in the four Event005 focus files are currently clean: no focus blocks directly contain `add_ideas`, `remove_ideas`, `swap_ideas`, `add_timed_idea`, `add_idea`, or `remove_idea`.
- The remaining focus reward spam is indirect: many focuses call shared helper effects that carry their own custom tooltips and broad payloads.
- One concrete duplicate helper call existed inside a single focus:
  - `PRA_switchyard_denial_posts` called `soviet_collapse_build_capital_railway_to_this_state` twice.
- Several Ukraine League focuses displayed bespoke mechanics tooltips while also calling shared helper effects visibly, creating noisy reward presentation.

## Changes

### PRA Duplicate Helper Removed

`PRA_switchyard_denial_posts` now uses one capital-railway helper call and one direct railway construction effect instead of calling `soviet_collapse_build_capital_railway_to_this_state` twice.

### Ukraine League Reward Display Simplified

The following focuses now keep their bespoke player-facing tooltip and run shared helper payloads in `hidden_effect`:

- `ukr_soviet_collapse_league_of_equals`
- `ukr_soviet_collapse_kyiv_leads_the_front`
- `ukr_soviet_collapse_breadbasket_empire`

Added localisation:

- `ukr_soviet_collapse_breadbasket_empire_mechanics_tt`

## Validation

Run by parent:

- `git diff --check -- common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_republics.txt localisation/english/005_soviet_collapse_l_english.yml`
- Brace balance check on:
  - `common/national_focus/005_soviet_collapse_custom_splinters.txt`
  - `common/national_focus/005_soviet_collapse_republics.txt`
- Unsupported operator scan for `<=` and `>=` on touched files: no matches.
- Repeated-helper scan on touched focus files: `Repeated same helper inside one focus: 0`.
- Localisation BOM check for `localisation/english/005_soviet_collapse_l_english.yml`: BOM present.
- Scoped flag status check for `gfx/flags` and `interface/flags`: no entries from this pass.

## Remaining Gaps

- This is a narrow cleanup, not the full focus-tree rework.
- Many focus trees still rely on generic shared helper calls and need route-level replacement with bespoke political, industrial, military, diplomacy, and expansion mechanics.
- The current `chaosx_focus_tree_auditor` subagent was spawned after this parent scan and is still expected to produce a broader current-state audit.
