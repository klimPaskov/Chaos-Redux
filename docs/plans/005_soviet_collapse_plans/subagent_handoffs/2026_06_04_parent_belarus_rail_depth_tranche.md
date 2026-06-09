# Event 005 Parent Tranche: Belarus Rail-State Focus Depth

## Scope

Parent-side bounded implementation tranche for the Soviet Collapse focus overhaul.

Touched files:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `localisation/english/005_soviet_collapse_blr_focus_l_english.yml`

Flags were not inspected or edited.

## Changed focus ids

- `blr_soviet_collapse_the_rail_map_on_the_wall`
- `blr_soviet_collapse_timetable_state`
- `blr_soviet_collapse_last_train_east`
- `blr_soviet_collapse_every_track_through_minsk`
- `blr_soviet_collapse_armored_train_workshops`
- `blr_soviet_collapse_the_league_depot_at_minsk`

These focuses no longer rely on broad generic depot, rail, or League helper packages as their main payoff. They now call Belarus-specific rail-state scripted effects.

## New scripted effects

- `blr_soviet_collapse_apply_rail_map_on_wall`
- `blr_soviet_collapse_apply_timetable_state`
- `blr_soviet_collapse_apply_last_train_east`
- `blr_soviet_collapse_apply_every_track_through_minsk`
- `blr_soviet_collapse_apply_armored_train_workshops`
- `blr_soviet_collapse_apply_league_depot_at_minsk`

## Behavior changes

- The opening rail map now adds trains, improves the Minsk junction, improves a controlled rail route, and increases Soviet depot pressure.
- The Timetable State now adds a supply hub, rail link, resilience, rail-construction AI priorities, and Soviet depot pressure.
- The Last Train East now fortifies an eastern rail route, adds command authority, pressures Soviet command obedience, and prepares a war goal against Moscow when Belarus can declare.
- Every Track Through Minsk now improves controlled core infrastructure, creates a logistics hub, unlocks League unit deployment decisions, and raises League support.
- Armored Train Workshops now adds rail stock, support stores, army experience, an arms factory, anti-air, League templates, and Soviet command pressure.
- The League Depot at Minsk now creates capital supply and air defense, adds a guarded arms site, unlocks League unit deployments, and raises depot control, resilience, and League support.

## Localisation

Added tooltip keys:

- `blr_soviet_collapse_rail_map_on_wall_tt`
- `blr_soviet_collapse_timetable_state_tt`
- `blr_soviet_collapse_last_train_east_tt`
- `blr_soviet_collapse_every_track_through_minsk_tt`
- `blr_soviet_collapse_armored_train_workshops_tt`
- `blr_soviet_collapse_league_depot_at_minsk_tt`

## Validation

Run locally:

- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt common/scripted_effects/005_soviet_collapse_effects.txt localisation/english/005_soviet_collapse_blr_focus_l_english.yml`
- `rg -n "<=|>=" common/national_focus/005_soviet_collapse_republics.txt common/scripted_effects/005_soviet_collapse_effects.txt localisation/english/005_soviet_collapse_blr_focus_l_english.yml`
- brace-balance check over the three touched files
- `rg` against vanilla `triggers_documentation.md` for `can_declare_war_on` and `has_wargoal_against`
- `git status --short -- gfx/flags interface/flags`

Results:

- diff check clean
- no unsupported `<=` or `>=`
- brace balance zero for all touched files
- `can_declare_war_on` and `has_wargoal_against` are documented vanilla triggers
- no flag files touched

## Remaining gaps

This is not a completion claim for the focus overhaul. A quick mechanical count after the patch still found:

- `common/national_focus/005_soviet_collapse_republics.txt`: 36 focuses with two or more generic `soviet_collapse_apply_focus_*` helpers.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`: 7 focuses with two or more generic helper calls.

The next high-impact parent tranches should replace those multi-helper nodes with route-specific effects, starting with Ukraine political/League nodes and custom-splinter chaos assault nodes.
