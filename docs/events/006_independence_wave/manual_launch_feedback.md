# Independence Wave manual launch feedback

The Event 006 entry receives normal and Settings-triggered requests through `chaosx.nr6.1`.
The release planner keeps its existing exact-count, protected-capital, reservation and package-validation rules.
An unfinished wave blocks another launch until the opening, host and foreign replies have closed.

## Request flow

1. The shared Settings dispatcher binds the human requester as `chaosx_manual_event_requester` and opens its request window.
2. Event 006 tests the pending-response barrier inside its entry effect.
3. A blocked request, or a standalone allocation that fails to commit, calls `independence_wave_report_failed_manual_launch`.
4. That helper validates the human requester and sets the shared per-request failure flag before firing `chaosx.nr6.73`.
5. The report explains pending talks, an unconfirmed launch, or unfinished changes after a release failure.
6. Its single acknowledgement clears only Event 006's frozen reason flags, with the ordinary 13-day timeout as the default acknowledgement.

One failed Settings request produces at most one popup, including repeated failures within a batch request.
The helper does not fire world news, grant content, unlock the event interface, clear a release barrier, or change the next automatic timer.
Automatic calls without a Settings requester retain internal diagnostics without a popup.
SCN-008 continues to use its separate `.80` success and `.81` failure results.

## Files and presentation

- Entry and report: `events/006_independence_wave.txt`.
- Request-owned helper: `common/scripted_effects/006_independence_wave_launch_feedback_effects.txt`.
- Plain report text: `localisation/english/006_independence_wave_launch_feedback_l_english.yml`.
- Reused report sprite: `GFX_report_event_006_asset_001_wave_summary`, registered in the existing Event 006 event-picture GFX family and backed by its existing 210x176 DDS.

No new icon, portrait, sound or GUI is needed.
The required native check is a failed manual Event 006 request through Settings, followed by another request after the barrier closes.
The first must explain the obstruction once, and the second must follow the ordinary allocator.

## Future work

If release diagnostics establish a player-relevant distinction between individual failure stages, the report can gain a short stage-specific explanation using a frozen requester value.
Internal package ids and executor codes should remain outside player-facing prose.
