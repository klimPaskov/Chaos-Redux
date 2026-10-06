# Event 013 GUI text repair handoff

Status: the authorized localization copy patch is implemented, while mandatory visual acceptance remains unresolved because the before and after GUI routes returned no artifacts.

## Authorization and ownership

The parent authorized the existing Event 013 abnormal-disaster path map copy repair and the listed follow-up keys, with no gameplay, layout, asset, or GFX changes.

The parent acceptance basis was the user direction to replace implementation and bookkeeping wording with concrete known affected states, disaster course, and details, keep the header useful, and fix every visible defect supported by evidence.

The owner is common/scripted_guis/013_natural_disasters_scripted_gui.txt, where natural_disaster_abnormal_path_gui uses player_context and names natural_disaster_abnormal_path_window at lines 11 to 13.

The independent container is interface/013_natural_disasters.gui, where natural_disaster_abnormal_path_window is a 1087 by 744 window beginning at line 19.

The entry decision is natural_disaster_review_abnormal_path_map in common/decisions/013_natural_disasters_decisions.txt, which calls natural_disaster_open_abnormal_gui at lines 92 to 99.

The event-owned view builder is natural_disaster_rebuild_abnormal_gui_view in common/scripted_effects/013_natural_disasters_effects.txt, with the history opener natural_disaster_open_abnormal_gui_history in the same file.

The interface is dedicated to Evolution III and manual abnormal history, and the task did not touch shared event log, event details, settings, or super-event surfaces.

## Files and identifiers

Changed files: localisation/english/013_natural_disasters_l_english.yml and this handoff.

No .gui, common/scripted_guis, scripted localization, effect, decision, GFX, sprite, or asset source was changed.

The localization SHA-256 immediately after the worker patch and before the parent's separate price-key update was 77D8C2A4CB524D0BDEDA3B564CDE5506A95D43618DE9BEFF677470D41810C447 at 207132 bytes.

The worker changed 29 keys: natural_disaster.gui.header_active, natural_disaster.gui.header_monitoring, natural_disaster.gui.card.1.tt through natural_disaster.gui.card.5.tt, natural_disaster.gui.refresh.tt, natural_disaster.gui.previous_path.tt, natural_disaster.gui.next_path.tt, natural_disaster.gui.previous_sequence, natural_disaster.gui.previous_sequence.tt, natural_disaster.gui.next_sequence, natural_disaster.gui.next_sequence.tt, natural_disaster.gui.marker.1.tt through natural_disaster.gui.marker.5.tt, natural_disaster.gui.event_details_button.tt, natural_disaster.gui.header_status.tt, natural_disaster.gui.selected_facts, natural_disaster.gui.path_queue.more, natural_disaster.gui.path_queue.all, natural_disaster.gui.severity_scale.tt, natural_disaster.gui.linked_state.none, natural_disaster.gui.recovery_progress.tt, natural_disaster.gui.timeline.report, and natural_disaster.gui.milestone.report.tt.

The dynamic selectors GetNaturalDisasterGuiHeaderSummary and GetNaturalDisasterGuiPathQueue remain the consumers for active and monitoring header text and the long and short path descriptions.

The five card tooltips keep their family, path-status, and arrival-date getters.

The five marker tooltips keep their state-name pointers, family and path-status getters, and arrival-date getters.

The recovery tooltip keeps all three numeric getters for rescue, stabilization, and reconstruction.

The report timeline and milestone tooltip keep the existing selected-state report-date getter.

The decision entry identifier is natural_disaster_review_abnormal_path_map, and its category and other gameplay requirements remain parent-owned.

The scripted-GUI identifiers include natural_disaster_abnormal_path_gui, natural_disaster_gui_card_1_click through natural_disaster_gui_card_5_click, natural_disaster_gui_marker_1_click through natural_disaster_gui_marker_5_click, natural_disaster_gui_previous_path_click, natural_disaster_gui_next_path_click, natural_disaster_gui_previous_sequence_click, and natural_disaster_gui_next_sequence_click.

The linked .gfx file is interface/013_natural_disasters.gfx, which registers GFX_013_abnormal_disaster_panel and GFX_013_abnormal_disaster_panel_damaged for the background, GFX_013_disaster_card_frame and warning or impact frame variants for cards, GFX_013_map_marker_impact and next-hit variants for pins, and GFX_013_recovery_progress_frame and GFX_013_recovery_progress_fill for the recovery meter.

The same interface references the existing family icons GFX_decision_cat_picture_nd_corridor, GFX_decision_cat_picture_nd_cyclone, GFX_decision_cat_picture_nd_drought, GFX_decision_cat_picture_nd_dust, GFX_decision_cat_picture_nd_earthquake, GFX_decision_cat_picture_nd_firefront, GFX_decision_cat_picture_nd_flood, GFX_decision_cat_picture_nd_hail, GFX_decision_cat_picture_nd_heat, GFX_decision_cat_picture_nd_landslide, GFX_decision_cat_picture_nd_massive_eruption, GFX_decision_cat_picture_nd_meteor_storm, GFX_decision_cat_picture_nd_rupture, GFX_decision_cat_picture_nd_severe_storm, GFX_decision_cat_picture_nd_skyfall, GFX_decision_cat_picture_nd_slope, GFX_decision_cat_picture_nd_tsunami, GFX_decision_cat_picture_nd_volcano, GFX_decision_cat_picture_nd_wind, and GFX_decision_cat_picture_nd_winter.

Other linked sprites include GFX_013_foreign_relief_badge, GFX_013_legend_aftermath, GFX_013_legend_blocked, GFX_013_legend_closed, GFX_013_legend_report, GFX_013_map_marker_chain_risk, GFX_013_eruption_plume_sheet, GFX_013_eruption_plume_static, GFX_013_meteor_fall_sheet, GFX_013_meteor_fall_static, GFX_013_rupture_wave_sheet, GFX_013_rupture_wave_static, GFX_013_storm_corridor_sheet, GFX_013_storm_corridor_static, GFX_013_tsunami_train_sheet, and GFX_013_tsunami_train_static.

The linked font family is hoi_16mbs, with hoi_20b and hoi_24header also present in the window.

No asset handoff was required because the text-only repair reuses the existing background, frames, icons, and animated sprites.

## Source identities and precedents

The scripted-GUI source hash at review time was 513D0AA2E298D5561F480DA34DF3778797328F42B11872EEBFC056C7D958921A.

The interface source hash at review time was C5F3C5274AEEB9161769EBB2FD4D0A16461AAB10A04401F8A590A8720C62791F.

The event-effects source hash at review time was D8A13F2188EE551A9D03AC22638FE5A37350EF8E2797F88181077425A891CE12.

The decision source hash at review time was 45AB9463291DD87694C11F67E25900BA56F8FD677F852F349BABE9313B13B0F9.

The scripted-localisation source hash at review time was E4E7BA2184747C6DD19165F22077FCD5F7F77FEA1EC1F17C30917C9B75C34196.

The GFX source hash at review time was 376D56D4FC010DD35D5A9522BCE2B47BD224D8E6B38F174F1C87D0BB3EFBFE18.

The offline Interface modding section instantTextBoxType was read at paradox_wiki/Interface modding - Hearts of Iron 4 Wiki.md lines 214 to 225, reference id 3938c8a2787ff3ce8eb27fdf5541b308c568308ed87bb09135d4d91751b0d95a and revision b74afc86be4e5dbb3b0fc600820d73a8340f7dc1821fc5ef02c9ee1f028c0b1c.

That section states that pdx_tooltip on instantTextBoxType takes a localization key, which matches the existing text and tooltip bindings.

The offline Scripted GUI modding window assignment section was read at paradox_wiki/Scripted GUI modding - Hearts of Iron 4 Wiki.md lines 51 to 67, reference id c3fdbebd7bd9df1124240c76a29539e6a348631e0bc2db4a42ff7440ffe75018 and revision b07d850ea78c4e1e3fc113574059ad2f3ea37df320b9259128d66814023c1f30.

That section establishes that window_name targets an independent container, which the exact Event013 source declares.

The offline Localisation Namespaces section was read at paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md lines 531 to 555, reference id aa80d1fb09d34bc976ba0f5c9446c9a686d2907e86fb885dd921edefe1dc74c4 and revision 1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064.

The installed Scripted GUIs documentation was read at C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_guis/_documentation.md lines 1 to 60, reference id e6d2e249edc2c6865ee3d109cfb67e3e30ebafd179ff4f2cb6b6bc2eb1494322 and revision 43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838.

The exact vanilla precedent inspected was interface/sov_paranoia_system_scripted_gui.gui and common/scripted_guis/SOV_paranoia_system_scripted_gui.txt.

Their SHA-256 hashes were B8925BF8DAF88BA82E6CE66F7B5131CAE7083E6EDA5367E2CF2B6EAEF6310A85 and 00DB231BF1D3183520E8E980B3433D5E5678A101849F96C17625D6B9384D85C5.

The vanilla example shows an instantTextBoxType paired with pdx_tooltip and a scripted GUI attached to a named container, while its decision_category context differs from this player_context window.

The source_lookup attempt for the SOV symbol returned sourceScope workspace_index with zero definitions, so the vanilla precedent was read from the installed files directly.

The GUI reference context reported no missing wiki or game-doc sources, one bounded omission with omittedSources empty, and no script_doc corpus.

## Reference and native mapping

No reference image was produced or selected because the before-change GUI render timed out without returning an artifact.

The accepted reference for text is the parent's bounded copy direction, and the intended layout adaptation is zero geometry or control changes.

The source layout comment maps the header plate, five-card column, path canvas, detail panel, legend tray, and severity strip to the existing 1087 by 744 background.

The header text uses natural_disaster.gui.header_status and resolves through GetNaturalDisasterGuiHeaderSummary, which selects natural_disaster.gui.header_active when a selected state exists and natural_disaster.gui.header_monitoring otherwise.

The five card buttons use natural_disaster.gui.card.1.tt through natural_disaster.gui.card.5.tt, and the five map pins use natural_disaster.gui.marker.1.tt through natural_disaster.gui.marker.5.tt.

The card and pin click regions remain native buttons with the existing matching click handlers.

The path navigation buttons use natural_disaster.gui.previous_path.tt and natural_disaster.gui.next_path.tt, while the disaster selection buttons use natural_disaster.gui.previous_sequence.tt and natural_disaster.gui.next_sequence.tt.

The selected detail area uses natural_disaster.gui.selected_facts, and the recovery meter keeps natural_disaster.gui.recovery_progress.tt.

The timeline's report milestone uses natural_disaster.gui.timeline.report and natural_disaster.gui.milestone.report.tt.

The background and all interactive or dynamic elements remain native HOI4 GUI elements.

No engine geometry adaptation was made or accepted.

## Text and action audit

The header now shows the known affected-state count and retains GetNaturalDisasterGuiSelectedPathDomain.

Card and marker tooltips retain dynamic family, path-status, arrival-date, and state-name values while replacing segment wording with affected-state wording.

The duplicate selected-facts ordinal was removed because the header now gives the useful affected-state count, while Hazard, Path, impact, and Deaths remain.

The recovery tooltip keeps its three existing numbers and describes recovery work and the three bar phases without exposing negative-score or burden calculations.

The report milestone now labels the existing date as Summary prepared and explains that the summary opens the next day or after the previous alert closes.

The modified card and marker tooltips use three or four short lines, the recovery tooltip uses three lines, and the report milestone uses three lines.

The information and navigation copy does not add gameplay actions, costs, requirements, or effects.

Cost-count audit: not applicable to this information and navigation copy repair because none of the changed controls charges a gameplay cost.

Texticon coverage: not applicable because the changed copy contains no costs.

The selected-facts source presents Hazard, Path, impact text, and Deaths after removing the duplicate ordinal, while the recovery meter values remain in a tooltip.

The visual value budget, action budget, text fit, and state coherence remain unverified because no production render was returned.

## MCP visual evidence

The connected tool schemas exposed hoi4.gui_inspect and hoi4.gui_render, while scenario was typed as unknown in the live tool metadata.

An initial inspect payload with country as a string was rejected with MCP error -32602 because scenario.country expected a record, and no source operation ran.

The corrected baseline inspect used windowName natural_disaster_abnormal_path_window, scenario {id: E013_GUI_USA_1936_BASELINE, date: 1936.1.1}, and generatedScenarios {enabled: false}.

The pre-change inspect then failed with tool call error timed out awaiting tools/call after 600s, with no artifact, diagnostics, sourceRevision, hierarchy, click-region report, or scenario fidelity report.

The pre-change render used the same baseline scenario, related abnormalactive, historyroute5_states, and longnames scenarios, generated scenarios disabled, resolutions 1920 by 1080 and 1366 by 768 at uiScale 1, and states normal, hover, selected, locked, disabled, warning, active, completed, empty-list, full-list, and long-text.

The pre-change render failed with tool call error timed out awaiting tools/call after 600s, with no image, crop, annotated view, hierarchy artifact, click-region artifact, sourceRevision, or scenario fidelity report.

The post-change inspect used the matching baseline scenario and failed with the same 600 second timeout, with no artifact or diagnostics.

The post-change render was requested with the matching baseline and related scenarios, both resolutions, the same state list, and a comparisonScenario for the open-related case.

The post-change render failed with tool call error timed out awaiting tools/call after 600s, with no image, crop, annotated view, hierarchy artifact, click-region artifact, sourceRevision, or comparison artifact.

A before-and-after source comparison cannot be established without the missing baseline artifacts, and a scenario comparison does not replace that source comparison.

The only supported scenario facts were the explicit ids and dates, the open-map flag for the related case, and declared route-total variables for the history and long-name cases.

No real state-name list or five-state history arrays were supplied, so those synthetic fixture labels are not confirmed rendered coverage.

## State and resolution matrix

| Scenario | Intended state | Resolution and scale | Evidence status |
| --- | --- | --- | --- |
| E013_GUI_USA_1936_BASELINE | Inactive USA baseline | 1920 by 1080 at 1 and 1366 by 768 at 1 | Requested before and after, artifacts unavailable |
| abnormalactive | Abnormal map open | 1920 by 1080 at 1 and 1366 by 768 at 1 | Requested before and after, artifacts unavailable |
| historyroute5_states | Five-state history route | 1920 by 1080 at 1 and 1366 by 768 at 1 | Requested with declared total, arrays and rendered coverage unresolved |
| longnames | Long state names | 1920 by 1080 at 1 and 1366 by 768 at 1 | Requested with no real state-name list, rendered coverage unresolved |

Normal, hover, selected, locked, disabled, warning, active, completed, empty-list, full-list, and long-text states were requested but not observed.

## Before and after behavior

Before the patch, visible copy described sequence identifiers, segments, records, score math, and report due dates, while the relevant dynamic getters and state pointers were already in place.

After the patch, the header describes known affected states and their domain, cards and pins describe affected areas, selected details omit the duplicate ordinal, recovery text describes work and bar phases, and the report date is labeled as the preparation date.

No behavior, state pointer, click effect, cost, requirement, AI behavior, cleanup rule, or route was changed.

## Blockers and remaining validation

Visual acceptance is blocked because both before-change GUI routes timed out and returned no artifacts, and the post-change inspection timed out as well.

The post-change render included a comparisonScenario request, but the call timed out before that comparison could be observed.

A before-and-after source image comparison could not be completed because no baseline artifact was returned by the pre-change render.

No visible alignment, spacing, clipping, overflow, background, asset, click-region, hover, selected, or disabled finding can be claimed without the required render artifacts.

No asset was created or modified, and linked asset existence and rendering remain unverified because GUI artifacts were unavailable.

The user's live consumer validation remains pending, and this handoff does not claim in-game completion.

No simplification was made to event mechanics or layout, but the required image reference and visual evidence are unresolved blockers.

The parent retains gameplay integration, final source reconciliation, shared surfaces, and the completion claim.

## Skills used

The worker read and applied chaos-redux-scripted-gui, chaos-redux-events, and chaos-redux-subagents.

Chaos Redux event assets and frame animation were not used because the authorized repair reused existing art and did not create or modify assets.

The worker did not commit because the parent assigned the isolated shared-worktree commit.
