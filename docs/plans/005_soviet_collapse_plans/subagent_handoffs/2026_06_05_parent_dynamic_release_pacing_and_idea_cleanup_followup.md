# 2026-06-05 Parent Follow-Up: Dynamic Release Pacing And Idea Cleanup

## Scope

- Tightened nonbase Soviet Collapse release pacing so nonbase releases require the nonbase chaos lane and live pressure/urgency/backlog conditions.
- Kept the exhaustive all-possible release pass reserved for the standalone triggerable scenario path.
- Changed normal terminal collapse to release base republics and subjects, then run pressure-based dynamic follow-on batches instead of immediately freeing every possible internal core country.
- Consolidated the Pale Railway Authority route reward into one visible idea and route variables/effects instead of swapping several separate PRA ideas.
- Repaired a local brace error in `soviet_collapse_create_custom_splinter_assault_templates`.
- Repaired the missing closing brace in `soviet_collapse_apply_high_chaos_focus_payload`.

## Changed Files

- `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`

## Behavior Notes

- Calm-world release pacing remains base-republic focused.
- Vanilla/internal republics can enter the follow-on pool only when the relevant chaos lane is open and crisis variables such as threat, release urgency, accumulated release pressure, failures, war pressure, component pressure, or regional cascade justify it.
- Custom pressure successors remain gated behind their high-chaos successor readiness and pressure-successor release pressure.
- The standalone triggerable scenario still uses `soviet_collapse_force_terminal_all_possible_core_countries_exhaustive`.
- Normal Union Unmade no longer calls the exhaustive all-possible release helper directly.
- PRA focuses now keep `pra_timetable_sovereignty_board` as the single visible authority idea, localized as `Pale Railway Authority`; route completion deepens `pra_rail_authority`, `pra_rolling_stock`, `soviet_collapse_depot_control`, `soviet_collapse_republic_institution_strength`, and `soviet_collapse_liaison_reach` instead of adding route-specific ideas.

## Validation

- Brace balance:
  - `common/scripted_effects/005_soviet_collapse_effects.txt`: depth 0, no negative closes.
  - `common/scripted_triggers/005_soviet_collapse_triggers.txt`: depth 0, no negative closes.
  - `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`: depth 0.
- `git diff --check` passed for touched files.
- Unsupported operator scan found no `<=` or `>=` in touched files.
- Focus indirect idea scan across the four Event005 focus files found `multi_idea_focus_count 0`.
- `gfx/flags` was not touched.

## Remaining Work

- The broader focus-tree cleanup is still open. The focus audit subagent `019e969d-eb96-7ad0-8633-ad2fa5d31c25` was still running at the time of this handoff.
- The parent goal remains incomplete until the user-facing focus-tree structure, expansion branches, and depth issues are fully audited and patched.
