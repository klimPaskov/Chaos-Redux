# Shared interface repair handoff

The confirmed source repairs are implemented.
The requested full UI audit is incomplete because no production GUI artifact or validation result was returned by the MCP inspection and rendering routes.
Every main-window request, explicit resolution fixture and timeout is archived under `docs/testing/live_qa/20261003_full_playtest/screenshots/ui_audit/`.
The user explicitly instructed continued source review when a route is slow or fails.

## Changes

Event Logs retains the History view after opening, draws records without requiring an actor scope, and resolves the stored actor for map navigation.
Event Details replaces the entirely black Death flag box with a Map button whose tooltip names the actor.
Cluster Details attaches its activation tooltip to the text instead of painting a bar over it.
The empty History message remains accurate when a filter has no matching events.

Civilian Deaths enables its existing state-border thickness values.
Contamination enables an explicit bottom-layer border width, includes the actual global polluted-air state modifier in amber, and explains that atmospheric burden in its tooltip.
Terror Activity retains its Event 031 state-activity gate because Fallout alone does not create terror incidents.

Air-source cleared quantities are unsigned, including quantities that round to zero.
The existing zero branches remain in place, and the separate net change retains its sign.

Settings establishes the requesting player before event-owned preflight and supplies one plain failure report when preflight rejects the request.
Event owners can use the same documented hook for a more specific failure in their own entry effects.
The hook checks the regular requester target, human ownership, a two-day request flag and the per-request shown flag.
It sets the shown flag before sending the report.
The native report has six reason descriptions and one acknowledgement with no gameplay effect.
It does not enter the numbered event pool or the Event Logs history.

The manual timer policy is retained and explained in Settings, Event Details and Help.
Help Overview and Controls are shorter and include the confirmed Radeon shortcut conflict.

## Assets

The Map control reuses vanilla `GFX_mini_tooltip` and `hoi_16mbs` through `interface/chaosx_events_log_popup.gui`.
The removed overlay also used `GFX_mini_tooltip`, so no GFX registration or texture replacement is needed.
Country flags remain unchanged.
The native Settings failure report requires no custom icon or picture.
No visual asset was generated, replaced or introduced as a placeholder.

Every Banner Rises has no speculative shared allocator change.
The Event 006 same-reservation anchor repair is already present, and the allocator source audit passes.
Its live release outcome remains unresolved.

## Changed source files

- `interface/chaosx_events_log_popup.gui`
- `common/scripted_guis/chaosx_scripted_gui_events_log.txt`
- `common/scripted_effects/chaosx_events_log_effects.txt`
- `common/scripted_effects/chaosx_settings_effects.txt`
- `common/scripted_effects/chaosx_forced_event_feedback_effects.txt`
- `common/scripted_effects/chaosx_dynamic_effects.md`
- `common/script_constants/chaosx_forced_event_feedback_constants.txt`
- `common/script_constants/chaosx_mapmode_air_constants.txt`
- `common/map_modes/chaosx_state_map_modes.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_map_modes.txt`
- `events/chaosx_forced_event_feedback.txt`
- `localisation/english/chaosx_forced_event_feedback_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`
- `localisation/english/chaosx_chaos_meter_l_english.yml`
- `localisation/english/chaosx_map_modes_l_english.yml`

The shared GUI localisation changes are limited to `chaosx.help.body.overview`, `chaosx.help.body.controls`, `chaosx.help.body.chaos_meter`, the Settings and Event Details trigger tooltips, `chaosx.events_log.window.history.empty`, the Event Details actor tooltip and the Map label.
Concurrent Fury, White Peace, Equipment from the Heavens and other owner edits are excluded from the repair commit.

## Meaningful checks

`python .tools/report_colour_audit.py --event chaosx_forced_event_feedback` reached no coloured report title or description key.
The scoped JSON result is archived in `ui_audit/feedback_colour_audit.json`.

The hook's source evaluator checked missing and expired request context, AI and nonexistent requesters, duplicate failure suppression, a new request, separate requesters, all six reasons and the generic fallback.
This is source behavior evidence rather than an engine execution claim.
The delegation handoff records the exact limitations of the evaluator.

`python .tools/audit_event6_allocator.py` passed with 138 SCN-008 ranked packages and a static standalone witness of 20 admitted packages.
It does not prove that the game released those countries.
The shared scenario bridge's current arguments pass its source guard, and the existing package-specific anchor repair is retained.

The History call-order review traces its shared view arrays through the later Events builder's clear/write operations.
The visible History builder finishes last after the repair.
The record refresh path already chooses the current tab's builder.

Palette and width changes affect display only.
No AI weights, event-selection probabilities, rewards, costs or timer arithmetic were changed by this repair.
The requester flag duration is a callback guard rather than an event interval.

## Exact live checks for the orchestrator

Use a fresh 1936 United States setup such as `qa_001_fresh_head` for the History, Settings, Help and scenario tests.
Run the UI checks at 1920 by 1080 and 2560 by 1440, with UI scale 1.
The manual timer is expected to reset after a successful event request, so park it again between independent event tests when needed.

1. Open Event Logs immediately and select History with All selected.
   The empty message should read "No events in this view."
   Force Event 001 through Settings and answer its report.
   Open Event Logs again, switch Events to History, close and reopen it, and cycle the History filters and sort direction.
   The fired event should remain in History, and a filter with no matches should display the empty message.
   Open its History details to confirm that the event and date still match the selected row.
2. Force Event 010, then open Death in Event Details.
   The top-right control should read Map rather than appear as an empty black flag box.
   Hover it to see Death's name and click it to locate the actor's capital.
   A detail without a valid actor should have no Map control.
3. Open Clusters, choose Natural Disasters and open Cluster Details.
   The activation line should show its first letter, the members and eligible counts should remain separate, and hovering that line should show the roll explanation without a painted bar covering it.
4. In Chaos Meter, open Air Cleanliness and the Smoke, Ash, and Aerosols source details with no clearing performed.
   Directly cleared should read `0.000%`.
   After an actual source-clearing action, the cleared quantity should be positive and the separate net change should still show the correct direction.
5. Use the late Fallout setup such as `qa_fo_apr` for map checks.
   Select Civilian Deaths over a state with a positive civilian toll and a positive global maximum.
   Its border should have the death gradient and visible thickness.
   Select Contamination over a state carrying only `air_contamination_global_state`, then over a state with a live local nuclear record.
   The first should have an amber border and atmospheric tooltip, and the second should retain its local hazard contribution.
   A state with no hazard should retain the faint neutral background.
6. In a fresh setup before world-end locks, request Event 031 through Settings, letting its normal preflight arm the dispatcher.
   Follow the incident's chosen state and confirm that its activity is positive and its stage is above clear before checking Terror Activity.
   The state should receive its stage colour and thickness.
   Fallout without an Event 031 incident should not create terror colour.
   Directly firing the hidden root without its armed flag is not this test.
7. Park `event_timer_days` at a large value, then send Event 001 from Settings with Force Trigger Mode enabled.
   Its tooltip should explain the fresh interval, and the displayed timer should change to the current automatic range after sending it.
   For the failed-target test, set `random_terror_global_lock` in a disposable fresh test and request Event 031 through Settings.
   It should produce exactly one "Event cannot occur" report explaining that no suitable target is available, with no successful firing recorded.
   The failed preflight should leave the parked timer unchanged.
   A second manual request may produce one fresh failure report.
   Owner callbacks must also be tested from a target country to confirm that the report returns to the requesting player rather than that target.
8. Launch Every Banner Rises, scenario 008, at Medium intensity with its ordinary scatter type.
   Run three days and inspect the map for released countries.
   The visible result should contain releases rather than a silent zero-country launch.
   If it fails, use the existing failure result and inspect `global.independence_wave_execution_last_failure`, `_last_failure_detail`, `_last_failure_package_id`, `global.liberation_plan_phase` and `global.liberation_plan_last_failure` to identify whether the failure is a package guard or the shared plan start.
   The Event 006 owner retains the package repair.
9. Open every Settings page, all Event Logs and Chaos Meter tabs and their detail overlays, scenario confirmation, and each Help tab.
   Check the first and last list rows, long names, unavailable controls and large values at both resolutions.
   These broader visual checks remain required because MCP returned no production images.

## Simplifications, omissions and blockers

No source repair uses substitute art, a generic country package or a changed probability table.
The Event Details flag control is an accepted navigation design change under G6, not an asset placeholder.
The numeric feedback catalogue is an accepted implementation choice recorded in the decisions file.

The full production GUI audit, matched before/after image review and click-region review are blocked.
No full, cropped or annotated MCP PNG, validation JSON or source comparison artifact exists to claim as a visual pass.
The seven main window families were requested at both resolutions, but their complete tab and overlay state matrix was not evaluated successfully.
Pixel-level acceptance remains open for the repaired controls and all other owned windows.

Every Banner Rises requires a post-fix live release result.
The failure hook requires event owners to call it when a sent entry event itself cannot apply, and overlapping delayed requests need an owner-carried generation identity.
Description retention across outstanding reports remains a live engine check.
The custom map-mode colours require live verification because the available map renderer does not execute scripted colour callbacks.

Skills used: events, scripted GUI, event assets, subagents and shared Git commit.
No skill files, workbook or exported CSV were modified by this repair.
