# Event 033 Acid Rain achievement audit prompt

The ten `acid_rain_033_*` achievements are implemented in `common/achievements/chaos_redux_achievements.txt`, `common/scripted_effects/033_acid_rain_achievement_effects.txt` and `common/scripted_triggers/033_acid_rain_achievement_triggers.txt`, with icons in `gfx/achievements/` and Event Details status (D34).
Part 10 owns every goal, eligibility, disqualifier, tracking fact and visibility rule.
[The achievement threshold and launch-origin addendum](../specs/033_acid_rain_achievement_threshold_and_launch_acceptance.md) owns the per-state Three Evacuations threshold and the launch markers.

Use this prompt for an audit or a fix, with `chaosx_event_completion_auditor` and, for icons, `chaosx_icon_artist`.

## Integrity checks

- Every achievement reads stored event facts and actual helper-applied deaths, never current modifiers, requested losses or prevented-death estimates.
- Each generation is separate, and a forced launch, CXT setup or invalid migration data disqualifies through the launch-origin flag.
- One operation receipt cannot satisfy two incompatible requirements, and a state transfer moves responsibility once.
- Updates happen only at Event 33 edges and bounded deadlines, never through a daily world scan.
- Hidden achievements reveal only at their Part 10 condition.
- Each achievement completes once through the shared framework.

Positive and negative source replays for all ten are agent evidence; earning them in a running game is a user live check.
