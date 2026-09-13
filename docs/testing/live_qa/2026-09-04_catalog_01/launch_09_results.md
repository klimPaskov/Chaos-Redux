# Launch 09 startup checkpoint

Status: startup gate remains incomplete.
The supplied shortcut launched HOI4 PID 24272 on 2026-09-05 at approximately 11:09:26 local time.
The process remained responsive through the final process check and was stopped by the parent before further repairs.
The exact stop time is recorded in `logs/launch_09/stopped_utc.txt`.
No visual main-menu verification, country-map entry, campaign, save, feature capture, or recording was performed.

The fresh logs are preserved under `logs/launch_09/logs/`.
The error log contains 589,403 bytes and 3,578 lines, compared with launch 08's 765,041 bytes and 4,598 lines.
These totals count repeated engine records and are not counts of distinct defects.
The targeted comparison is stored in `logs/launch_09/comparison_counts.json`.

The five prior invalid `set_timed_country_flag` effect records are absent.
The prior literal `$STATE$` repression argument records are absent.
The 214 invalid doctrine `index` effect records remain.
Direct Event 31 flags resolve, but the engine reports 48 repeated slow-format warnings for their 24-bit encoding.
Their artwork requires an encoding-only repair and another native check.

The unreferenced `track_index` probe produced two `InitPostRead` failures, each immediately preceded by `add_mastery: Amount of mastery to add is 0`.
No unknown `track_index` record appeared.
This is inconclusive about exact-track behavior and does not justify dropping the track filter.
The probe was archived as `logs/launch_09/doctrine_index_probe.txt`, then removed from the runtime tree after verifying its recorded SHA-256.
A subsequent parser probe must use a nonzero amount and remain unreferenced.

Gameplay and teaser work remain pending while the confirmed startup errors are repaired.
