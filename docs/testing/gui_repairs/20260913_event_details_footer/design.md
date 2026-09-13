# Event Details footer and help wording repair

Acceptance basis: the user explicitly requested removal of the Acid Rain details button and its occupied space, correction of text bleeding, and plain descriptions of famine, migration, and camps.
The shared Event Details window and shared help text remain parent-owned; no Astra worker or computer control is authorized.
The supplied screenshots are references for the surrounding design; `reference.html` marks the accepted small layout repair before source edits.

| Reference region | Native mapping | Accepted correction |
| --- | --- | --- |
| Acid Rain control and extra footer row | `events_log_event_detail_open_acid_rain_map_button`; Event Details window, entry, and root list sizes | Delete the orphaned control and reduce the window and list/entry heights by 44 pixels. |
| Trigger and checkbox | `events_log_event_detail_entry_trigger_button`, both event toggle buttons, empty toggle label | Move up 44 pixels. |
| Remaining event navigation | Abnormal Path and rival-member previous/next controls | Keep existing behavior and visibility; place them to the right of the compact footer controls. |
| Empty-state message | `events_log_event_detail_world_end_empty` and matching evolution empty message | Use 12-pixel panel-relative offsets and keep text within the panel width. |
| Help page paragraphs | `chaosx.help.body.chaos_meter` in English localisation | Replace only the famine, migration, and camp paragraphs; preserve other help sections. |

Entry point: `events_log_popup_event_details_gui`, player context, parent `top_bar`, window `events_log_event_details_window`.
Assets: existing tiled window/panel sprites, existing 123×34 button family and checkbox sprites, existing HOI fonts.
No new asset, mechanic, cost, AI score, or event-catalog field is needed.
MCP fixture values represent the user-supplied Random War state; visibility inputs follow the existing scripted-GUI predicates.
Optional navigation controls are checked separately, since Abnormal Path and rival-member browsing cannot coexist on one normal event row.
