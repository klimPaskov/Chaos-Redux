# Parent Tranche Handoff: Belarus Rail Pathline Cleanup

## Scope

Bounded Event005 Soviet Collapse focus-tree layout cleanup for the Belarus rail, League freight, and rail-war branches.

No flag, sprite, gfx, interface, localisation, decision, or scripted-effect files were touched in this tranche.

## Files Changed

- `common/national_focus/005_soviet_collapse_republics.txt`

## Identifiers Changed

- `blr_soviet_collapse_league_supply_timetables`
- `blr_soviet_collapse_railway_neutrality`
- `blr_soviet_collapse_rail_war_state`
- `blr_soviet_collapse_prepare_league_freight_tables`
- `blr_soviet_collapse_join_the_league_when_war_comes`
- `blr_soviet_collapse_armored_train_workshops`

## Before

The Belarus rail/League area had several visible pathline problems:

- `join_the_league_when_war_comes` drew prerequisite lines from every main political route choice, causing route-lock lines to cut across the middle of the tree.
- `railway_neutrality` and `rail_war_state` were not adjacent, so their mutual-exclusion link and incoming rail edges were visually messy.
- `armored_train_workshops` depended on `league_supply_timetables`, pulling a downstream military rail line through the rail-war/neutrality area.
- `prepare_league_freight_tables` sat too close to the League join row.

## After

- Moved `league_supply_timetables` to `x = 9, y = 8`, directly under `timetable_state`.
- Moved `rail_war_state` to `x = 10, y = 10` and `railway_neutrality` to `x = 12, y = 10`, keeping the rail-war mutex adjacent.
- Moved `prepare_league_freight_tables` to `x = 22, y = 11`, keeping it in the recognition/League freight lane and below the League join row.
- Moved `join_the_league_when_war_comes` to `x = 19, y = 9`.
- Removed the multi-focus route prerequisite from `join_the_league_when_war_comes` and preserved that requirement in `available`, so the focus still requires a completed Belarus route but no longer draws route-lock pathlines from all four route starts.
- Moved `armored_train_workshops` to `x = 10, y = 12` and changed its route prerequisite from `league_supply_timetables` to `rail_war_state`, matching the armored-train war route and preventing a line through the mutex pair.

## Validation

- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt` passed.
- Brace balance passed for `common/national_focus/005_soviet_collapse_republics.txt`.
- No unsupported `<=` or `>=` operators found in `common/national_focus/005_soviet_collapse_republics.txt`.
- Coordinate/prerequisite inspection confirmed the changed focus positions and prerequisites.
- `git status --short -- common/national_focus/005_soviet_collapse_republics.txt gfx/flags interface/flags` showed only the focus file modified.

## Remaining Gaps

This is a focused pathline cleanup, not the full Belarus rework. Belarus still needs deeper decision integration, stronger rail/corridor mechanics, and another visual pass around late League/front convergence after the wider Soviet Collapse focus-tree rework proceeds.
