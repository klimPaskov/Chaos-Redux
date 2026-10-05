# Shared interface decisions, 5 October 2026

Acceptance basis: the user assigned these shared systems and confirmed defects, authorized surgical framework changes, and explicitly authorized design corrections under G6.
Source repairs are implemented, while the production visual audit and live outcomes remain unresolved.
No workbook or exported CSV was edited.

| Surface | Finding and accepted decision | Implementation evidence | Disposition |
| --- | --- | --- | --- |
| B036 History | Opening Event Logs rebuilt History and then overwrote its shared view arrays with the Events catalogue. Build the visible History view last. A row should also survive a missing actor pointer, so iterate event identifiers without changing country scope and resolve the optional actor only for navigation. | `toggle_events_log_popup` in `common/scripted_effects/chaosx_events_log_effects.txt`, and `events_log_popup_history_gui` in `common/scripted_guis/chaosx_scripted_gui_events_log.txt`. | implemented, runtime and visual verification pending |
| B036 Event Details | Death's medium neutrality flag is a 41 by 26 texture whose RGB extrema are all zero. It appears as an empty framed box. Replace the flag control with a labelled Map button, retain its actor tooltip and capital navigation, and hide it when the actor no longer exists. | `events_log_event_detail_open_diplomacy_button` in `interface/chaosx_events_log_popup.gui`, its two predicates in the scripted GUI, and `chaosx.events_log.window.event_details.locate`. | implemented, visual verification pending |
| B038 Cluster Details | A painted `GFX_mini_tooltip` button covered the activation text at the same coordinates. Put the tooltip on the text itself and remove the painted overlay. | `events_log_cluster_details_meta_tertiary` in `interface/chaosx_events_log_popup.gui`. | implemented, visual verification pending |
| B037 Civilian Deaths | The top layer assigned thickness but did not enable scripted thickness. Enable the layer's existing thickness configuration. | `deaths_state_map_mode.top` in `common/map_modes/chaosx_state_map_modes.txt`. | implemented, live verification pending |
| B037 Contamination | Fallout's polluted atmosphere applies `air_contamination_global_state`, which the map did not include. Show that real atmospheric burden in amber, separately from local chemical residue, disease and nuclear fallout, and explain it in the tooltip. Enable explicit border thickness on the bottom state layer too, so local hazards and the atmosphere have a defined visible line width. | `state_map_modes_air` constants, the Contamination bottom layer, `GetGlobalAirMapModeTooltip`, and the map-mode localisation. | implemented, live verification pending |
| B037 Terror Activity | Fallout does not create Event 031 activity. A clear state should remain uncoloured until the normal Event 031 dispatcher creates an incident. | `031_random_terror_map_mode.txt`, `031_random_terror_effects.txt`, and the research handoff. | source finding accepted, positive-activity live check pending |
| B010 Air Cleanliness | The current source already has unsigned zero branches from `aadf7867f`. The cleared quantity itself should be unsigned because its label states the direction. Keep signed net change separately. This also removes a negative prefix if a tiny cleared value rounds to zero. | `chaos_meter.air.source.entry_cleared` and `.selected_cleared` in `localisation/english/chaosx_chaos_meter_l_english.yml`. | implemented, live verification pending |
| B032 Every Banner Rises | The shared bridge is country-scoped and its arguments pass the plan guard. The documented KAR/IW-033 reservation repair already exists in Event 006. Preserve it and use the allocator audit plus a fresh scenario check to distinguish any remaining failing package. | `scenario_research_20261005.md` and the passing Event 006 allocator audit. | unresolved live outcome, no speculative shared allocator patch |
| B043 Manual timer | Keep the fresh automatic timer interval after an event is sent. It provides the same interval between crises as the automatic path. State the behavior in Settings, Event Details and Help. | Two trigger tooltips and the Help Overview and Controls paragraphs in `localisation/english/chaosx_gui_l_english.yml`. | implemented |
| Settings failure feedback | Establish a regular requester target before owner preflight, provide one plain report hook, and suppress repeat reports within a request. Use a six-reason numeric catalogue and caller-set temporary input, following the existing helper convention. The dispatcher reports a rejected target before sending an event, while owner entry effects can report a more specific failure through the same hook. | `chaosx_report_forced_event_failure`, `chaosx_forced_event_feedback.1`, its constants, dispatcher wiring, and the appended contract in `chaosx_dynamic_effects.md`. | implemented, owner adoption and live callback verification pending |
| Help and empty text | Explain the timer plainly, shorten the Overview, describe Map navigation, mention the confirmed Radeon shortcut collision, and use an empty History message that remains truthful under filters. | The shared GUI localisation keys listed in the completion report. | implemented, visual verification pending |

## References and review basis

The supplied `el_details.png`, `el_history.png`, `el_clusters.png`, `cm_air.png` and `g_help.png` were opened directly.
The supplied October QA Settings and Event Logs screenshots were also opened for the existing design and spacing.
The accepted small repair preserves the surrounding window design.
The Event Details actor area changes from a black flag frame to a 40 by 24 labelled control at the existing x=414, y=5 position.
The Cluster Details activation text keeps x=14, y=76 and its 440-pixel width, with the tooltip attached to that text rather than a second painted element.
These are reference-to-native mappings, not claims of production pixel acceptance.

Installed `common/scripted_guis/_documentation.md` lines 57-97 documents visibility, properties and dynamic list scope.
The offline `Scripted GUI modding` Dynamic Lists section documents the same array/index contract, and its Temporary variable usage section covers trigger-created presentation variables.
The offline `Interface modding` lines 199-217 documents text bounds and `pdx_tooltip` on text.
Installed `common/map_modes/documentation.md` lines 14-53 and 72-74 defines the border colour callback and the layer opt-in required for thickness.
Installed `triggers_documentation.md` lines 3775-3790 allows `has_dynamic_modifier` in state scope.
The feedback handoff preserves installed event, regular target, native helper and conditional-description references with their revisions.
Detailed map and scenario citations and source hashes are preserved in the two research handoffs.

## Validation limits and follow-up

The local stdio connection identified HOI4 MCP 3.8.1 and returned its live schemas.
The GUI context bundle succeeded, but the targeted History inspection and render timed out after 120 and 180 seconds.
The separate narrow audit requests for all seven main window families, with explicit 1920 by 1080 and 2560 by 1440 scenarios at scale 1, also encountered non-response.
No production render, cropped or annotated render, click-region proof, validation JSON or accepted visual comparison was returned.
The exact request and timeout records are in `docs/testing/live_qa/20261003_full_playtest/screenshots/ui_audit/`.
The full tab, overlay, crowded-list, long-text and disabled-state visual matrix remains blocked.
Source review and the supplied screenshots do not replace that gate.

The failure hook's two-day requester guard does not identify overlapping delayed requests uniquely.
Owner failure callbacks must stay in their originating chain, and delayed overlapping requests need an owner-carried generation identity before that contract is extended.
The user or orchestrator must verify description retention across outstanding reports and the ordinary request's one-report behavior.
No new art or substitute portrait was introduced.
The black Death flag remains the country's flag, and the UI uses an explicit navigation label instead of altering that asset.

Skills used: events, scripted GUI, event assets, subagents and shared Git commit.
No skill file was changed because this task owns the shared interface source and its evidence, while the skill files contain concurrent work by other agents.
