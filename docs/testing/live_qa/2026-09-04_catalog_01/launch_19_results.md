# Launch 19 startup results

The supplied shortcut launched PID 3352 at 13:35:48 local time on 2026-09-05.
Engine frontend startup completed at 13:37:07 after 78467ms, and the process remained responsive.
The game was stopped at the nonempty-error gate and fresh logs were archived.
No desktop control, visual main-menu acceptance, or country-map acceptance was performed.

The archived error.log has 1758 lines and 307247 bytes, SHA256 b4222d5b1bc1a06c1af0cc53dc16e61ee9e6722e9ff9ca326c2daf3475699e94.
All seven tracked source files remained byte-identical during the launch.
This comparison normalizes wall-clock time, game date, engine source locations, and referenced source line numbers consistently in both runs.
It yields 677 distinct lines for launch 18 and 652 for launch 19, with 26 removed lines and one new aggregate count (541 errors).
The earlier launch 18 report used a slightly different normalization and reported 678; this does not indicate a source or log change.
Raw diagnostics decreased from 1940 to 1758 lines.

## Repairs verified by the native loader

- Five Event21 infrastructure comparisons: seven repeated invalid-trigger records to zero.
- Twelve Acid Rain building comparisons: twenty-four repeated invalid-trigger records to zero.
- Twelve Acid Rain damage calls: twenty-four malformed acid_rain_damage_one records to zero after routing through the documented dynamic helper.
- Twenty-five proven Event32 temporary cleanup deletions: operations-file invalid cleanup records decreased from 92 to 42, exactly fifty fewer repeated records.

The Event21 edits preserve their original scopes, thresholds, and candidate conditions.
Acid Rain retains its building cursor order and damage amount; actual meta-effect execution and damage receipts still require campaign tests.
The Event32 cleanup patch preserves every other source byte and retains the four separately identified unresolved contracts in the reviewed first 2000-line region.
Other unsupported cleanup calls elsewhere in the file remain for review.
See event21_infrastructure19_handoff.md, event33_damage19_handoff.md, dynamic_building_damage19_handoff.md, and event32_operations_temp19_handoff.md for exact contracts and backups.
MCP helper projections and probability eligibility remain incomplete; comparison cache failures are recorded rather than claimed as passes.

## Remaining coverage and limitations

The clean-start gate remains pending because attributable errors remain.
No campaign, save, feature screenshot, teaser video, custom-unit recording, or mechanics-guide media replacement has occurred.
All requested gameplay and media coverage remains pending, including runtime validation of these repairs.
No broad redesign or simplified gameplay fallback was introduced.
The next repairs address the remaining Event32 temporary contracts and Event21 building comparisons, preserving concurrent event work.
