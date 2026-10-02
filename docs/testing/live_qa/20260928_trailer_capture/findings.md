# Live findings from the trailer capture session (2026-09-28)

Session: debug launch, 1920×1080 borderless, save `trailer_045_autosave_horde` (USA, June 1936, Chaos 1,000+, five zombie hordes at war), later `trailer_050_horde_june` and a tag switch to Tibet (the Holy Realm).
Scope: observations made while recording footage; each entry says whether it was fixed in this session.

## Fixed

### Scenario-suppressed fire-once events show "Type: Unknown" in the settings window

- Seen: Chaos Redux Settings → Trigger Events, event 5 "Soviet Union Collapse" showed `Type: Unknown`; other events show `Fire-Once`, `Repeatable`, or `Major`.
- Cause: `suppress_soviet_collapse_fire_once_for_triggerable_scenario` (`common/scripted_effects/chaosx_triggerable_scenarios_effects.txt`) and `black_plague_scenario_suppress_fire_once` (`common/scripted_effects/020_black_plague_scenario_effects.txt`) removed the event from `global.fire_once_events`, which `get_event_type` also uses as the type registry.
- Fix: the removal is dropped. The same helpers already add the event to `global.disabled_events` and `global.fired_events`, and `evaluate_random_event_active_pool_candidate` excludes both, so the event stays out of the random pool; Event 5 also keeps its `soviet_collapse_triggerable_scenario_suppressed_fire_once` guard.
- Second effect of the same fix: `events_log_fire_candidate_is_available` (`common/scripted_triggers/chaosx_settings_triggers.txt`) lets a fired event be fired manually again when it is in neither `global.major_events` nor `global.fire_once_events`, so the removed scenario event could be re-fired from the Event Log; it now reads as a fired fire-once event and is not offered.
- Event 020 has no event-level suppression flag (Event 005 does); it stays out of the pool through the disabled and fired arrays alone, which every automatic path checks.
- Limit: saves that already ran the suppression keep the old array contents; a new game shows the correct type.

### Map crash when a foreign camp is viewed up close

- Seen: an access violation in `raid_target_status.cpp` during "Update Provinces" whenever the camera zoomed in on certain states (first on the Danube front in the June horde save, later over Brandenburg and Japan in a fresh November 1936 campaign). Every dump faults on the same building object, and the crash is deterministic: `goto_state 64` plus a close zoom in `trailer_150_nov` crashed every time.
- Cause: `concentration_camp`, `extermination_camp`, and `gulag_labor_camp_network` (`common/buildings/chaosx_buildings.txt`) are state buildings with `need_detection = yes`. The engine keeps raid detection data only for provincial buildings (vanilla uses `need_detection` only on facilities, dams, and the naval facility), so the save's raid target registry never contains the camps. When the map draws a level-2 camp owned by a country that is neither the viewer nor an ally, it asks whether the building is hidden, gets no detection record, and dereferences it. Germany's history camps in states 53, 60, and 64 are enough; it starts once the raid system is active, which explains why the first months of a game looked stable.
- Fix: the three camp buildings no longer declare `need_detection` or `detecting_intel_type`. No script reads camp detection; raids target states, not camp buildings.
- Verified: the same save and camera path over states 64, 60, and 53 no longer crash. Existing saves are covered because building definitions load from the files.

### New unit models load cleanly

The Event 039 assassin units, the rebuilt cave monster, and the plague carriers load with no entity, mesh, or animation errors in `error.log` (commit `8c3a4f847`).

## Open (not fixed here)

### Peace-treaty dialogs flood the player at Chaos 1,000+

- Seen: in about three weeks of game time at World Collapse, more than 60 modal "Treaty of …" white-peace dialogs queued (Chişinău, Riga, Alma-Ata, Lhasa, Berlin, Varna, …). Each one blocks map input until dismissed, and they keep arriving while the game is paused because the queue was filled before pausing.
- `game.log` shows 2–6 minor peaces a day (`CHAOS METER: Minor … made peace`), largely short wars between the many released minors, and Mengjiang's and Yunnan's wars ending in white peace with major powers.
- Impact: at high chaos a player spends most of their time clicking OK. Candidates: have Event 009 White Peace and the chaos-driven settlements prefer fewer, larger settlements, or check whether many of these wars are started and ended by scripted war declarations within days.
- Needs a design decision; not changed.

### Tag switch adds about 530 errors

Switching from USA to TIB with the `tag` console command raised the on-screen error counter from 2,502 to 3,032. Not investigated in this pass; the console `tag` is a debug path, but the burst suggests an on-player-change hook that evaluates something invalid for a non-USA player.

### Script errors at startup from in-progress work

`error.log` at the main menu lists unknown triggers and effects from files other agents are editing (not touched here):

- `common/scripted_effects/006_independence_wave_opening_dispatch_effects.txt` lines 245, 293, 374: `independence_wave_opening_report_callbacks_pending`, and `is_at_war` used as a trigger with an invalid form.
- `common/scripted_effects/006_independence_wave_host_response_effects.txt` lines 150, 331–334: `independence_wave_host_response_*` triggers not defined.
- `common/scripted_effects/026_black_friday_effects.txt` line 4135: `black_friday_quote_cbrn_external_aid_pp_fee` effect not defined.
- `common/scripted_effects/chaosx_startup_history_effects.txt`: `recruit_character` called outside history files (about 30 lines, 503–777).

### Minor UI observations

- The Trigger Events panel's `+` / `−` buttons step by 5 by default; the tooltip explains the modes, but it covers the event type text while the cursor rests on the button.
- The "Treaty of Chişinău" title renders as "Chisin?u" in the dialog title font (vanilla city name `VICTORY_POINTS_3707`); it is a vanilla font limitation, not mod text.
