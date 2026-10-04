# Event 014 Network ledger dossier records

The Network window (`cannibalism_network_window`) lists every registered country actor and confirmed state node, plus states with a live inbound route warning.
Each row and the selected dossier show the seven node-card fields required by spec part 6: country or state, node type, strength band, known route, last incident, selected counteraction, and certainty.
Every field reads a record that a real game transaction wrote onto the subject itself.
A missing record is shown as "unknown", "none on record" or "none ordered", never as a zero.

## Record model

Records live on their subject: a STATE for nodes and route warnings, a COUNTRY for actors.
The ledger is one shared counter-intelligence board, so every viewer reads the same subject records; only the tab filter, sort order and selection belong to the viewer.

| Variable on the subject | Meaning |
| --- | --- |
| `cannibalism_ui_strength_band`, `cannibalism_ui_strength_date` | Last measured strength band (`cannibalism_ui_strength_band` quiet, active, severe) and the date of that measurement |
| `cannibalism_ui_route`, `cannibalism_ui_route_date` | Last delivered spread route (`cannibalism_spread_route` enum) and when it was recorded |
| `cannibalism_ui_incident`, `cannibalism_ui_incident_date`, `cannibalism_ui_incident_operation` | Latest reported incident (`cannibalism_ui_incident` enum), its date, and the counteraction behind a result incident |
| `cannibalism_ui_counteraction`, `_status`, `_actor`, `_date`, `_spread_id` | Latest ordered counteraction (`cannibalism_ui_counteraction` enum), its status (`cannibalism_ui_action_status`), the ordering country, the date of the last status change, and for route screening the inbound spread ID it covers |

All enums are integer identifiers in `common/script_constants/014_cannibalism_constants.txt`; none of them is a tuning value.
Dates are stored as `global.date` values and are only compared or displayed with `GetDateStringNoHour`; no day arithmetic is done on them.

## Writers

| Transaction | Subject and record |
| --- | --- |
| `chaosx.nr14.2` delivered | Recipient country: discovery incident and measured cell strength; the opening state, when it is a node: discovery incident and measured node strength |
| `chaosx.nr14.20`, `.21` delivered | Recipient country: ritual or network incident and measured cell strength |
| `chaosx.nr14.30` delivered | New warlord country: host emergence incident |
| `chaosx.nr14.60` delivered (inside the warning guard) | Warned state: inbound route and route warning incident |
| `chaosx.nr14.61`, `.62` delivered | Receiving country and arrival node: route, arrival, reinfection or second arrival incident, measured strength |
| `cannibalism_try_pay_humane_route_screening_cost`, `cannibalism_try_pay_hard_route_screening_cost` (successful payment) | Screened state: screening or route seal order (active) tied to the spread ID, route, and "ordered" incident |
| `cannibalism_resolve_loaded_spread_containment` | Screened state: order succeeded and route contained incident; the receiving country, when it is an actor: route contained incident |
| `cannibalism_clear_loaded_spread_pending_state` | Screened state: a still-active order for the finished spread closes as cancelled; a state that never became a node drops its records with the warning |
| Six mission starts (`cannibalism_start_*_mission`, after `activate_mission`) | Mission target: active order by the ordering country |
| Six mission results (`cannibalism_complete_*`, `cannibalism_partial_*`, `cannibalism_fail_*`, before the clear effect) | Mission target: succeeded, partial or failed status when the order is still that country's active order, a result incident in every case, and measured strength for investigation, prison hold, sea road and route cut successes and partial results |
| Six mission clears (`cannibalism_clear_*_mission`) | Mission target: a still-active order by that country closes as cancelled |

The investigation mission records on its target state when that state was a confirmed node at activation, and otherwise on the ordering country's own row, because it then examines that country's own cells.
Every family adapter checks the family's existing target identity trigger first, so a stale target publishes nothing.
Strategic interdiction and anchor strikes record orders and results but never measure strength.

## Certainty

| Certainty | Rule |
| --- | --- |
| Observed | A strength measurement exists and no later incident has been recorded |
| Stale | A strength measurement exists and the latest incident date is later than the measurement date |
| Partial | Route, incident or order records exist, but strength was never measured |
| No reports | No record exists beyond the subject's identity |

The rule compares two stored dates and uses no timer.

## Lifecycle and cleanup

`cannibalism_ui_clear_current_subject_records` clears every record on a subject.
It runs when a country actor registers a new generation or unregisters, when a state node registers, retires, or is liberated into recovery, and when a route warning ends on a state that never became a node.
A viewer's incarnation reset (`cannibalism_reset_current_country_incarnation_state`) clears that viewer's lists, open page and selection through `cannibalism_gui_reset_current_viewer`, and its mission clears close its own active orders as cancelled.
No daily, weekly or whole-world iteration is involved; inbound warning rows read the bounded spread queue only while a player refreshes the window.

## Readers and layout

The getters in `common/scripted_localisation/014_cannibalism_scripted_localisation.txt` (`GetCannibalismUi*`) run in the scope of one row or of the one-row dossier list, so rows and dossier read the same records.
Rows (374x64 cards) show identity, type or stage, certainty, strength, route, latest incident and current order on three lines.
The dossier is a one-element native list (`cannibalism_network_selected_country_dynamic_list` or `cannibalism_network_selected_state_dynamic_list`) that adds measurement, recording and order dates and the ordering country.
`cannibalism_gui_rebuild_network_selection` drops a selection whose actor or node has retired.
The Network window is hidden from the reveal onward, and no field names the concealed organizer.

## Host command window

`cannibalism_warlord_command_window` has an Overview page with Larder, Frenzy, Network Alignment and raised formations, and a States page.
The page is the presentation-only country flag `cannibalism_warlord_gui_states_view`; no gameplay check reads it, and `cannibalism_gui_clear_command_view` clears it on an incarnation reset.
Opening the States page runs `cannibalism_gui_rebuild_warlord_state_view`, which fills `cannibalism_command_gui_state_entries` from `every_controlled_state` of the viewing Host.
Each card rechecks control when drawn and shows the state's name, its status (no longer held, liberated and recovering, exhausted or unusable, feeding territory resting or ready, or held ground), its population and its feedings against the exhaustion limit.
The raid card reads the March Host's own receipt (`cannibalism_march_raid_target_state`, `_date`, `_receipt_result`, `_owner_generation`, `_target_controller`, `_target_controller_generation`), written only by a successful targeted depot raid.
A receipt from an earlier actor generation of the same tag is not shown, and a controller whose actor generation changed since the strike is shown as a Host that no longer exists.
Without a receipt the card says no raid was committed.

## Revealed command window

`cannibalism_revealed_command_window` has three pages: Overview, Loyalty and Targets.
The pages are the presentation-only country flags `cannibalism_revealed_gui_loyalty_view` and `cannibalism_revealed_gui_targets_view`; Overview is open when neither is set, and `cannibalism_gui_clear_command_view` clears both on an incarnation reset.
Overview keeps the global Larder, Network Reach, the integration count, the unification seal and, once eligible, the terminal mobilization line.
The seal and the terminal line are shown on Overview only, so the list pages never sit under them.

### Integrated warlord history

The revealed host keeps nine aligned arrays: `cannibalism_integrated_history_generation`, `_slot`, `_name`, `_origin`, `_region`, `_personality`, `_origin_state`, `_disposition` and `_date`.
`cannibalism_record_integrated_warlord_slot` appends one row per integrated actor generation, after `cannibalism_capture_current_integration_history_identity` reads the donor's generation and origin state in the donor's scope.
The three writers are the unification host's own record, each absorbed warlord, and the primary Wendigo donor; a generation already in the history is not appended again.
`cannibalism_ui_load_integrated_history_row` reads the row at the native list index `cannibalism_loyalty_index` only while all nine arrays have the same length, and a misaligned history shows "Record unavailable" instead of another row's values.
Each row shows the warlord portrait, name, origin route, disposition and joining date, and the tooltip names the state where the warlord rose when it is known.
`cannibalism_clear_integrated_history_and_targets` clears the history and the targets on an incarnation reset.

### Surviving warlords

Opening the Loyalty page runs `cannibalism_gui_rebuild_revealed_loyalty_view`, which fills `cannibalism_command_gui_warlord_entries` from the bounded `global.cannibalism_actor_countries` registry and stamps each listed warlord with `cannibalism_loyalty_listed_generation`.
A row is current while the country exists, is still a warlord and has the same actor generation it was listed with; otherwise it reads "no longer stands as a warlord".
The row shows the warlord's current answer to the revealed host: awaiting absorption, autonomous governor, defiant, challenger, or outside the command.

### Continental targets

`cannibalism_unified_record_continental_target` runs at the end of the six committed continental executors (front collapse, army cell seeding, global campaign, terror ultimatum, border incident and coalition hub strike).
It inserts the target country, the kind (`cannibalism_continental_target_kind`), the commit date and the target's actor generation at the front of four aligned arrays and trims them to `cannibalism_continental_target_record.rolling_count` (three).
`cannibalism_ui_load_continental_target_row` reads the row at `cannibalism_continental_index`.
A target that was an Event 014 actor and whose actor generation changed since the order is shown as a Host that no longer exists, so a recycled tag never inherits an older strike.
Without a committed operation the page shows one empty card.

## Icons and assets

The dossier reuses existing sprites only: `GFX_cannibalism_network_country_card`, `GFX_cannibalism_network_state_card`, `GFX_cannibalism_network_target_frame`, `GFX_cannibalism_selected_target_overlay_animated` and its static fallback in `interface/014_cannibalism.gfx`, plus the vanilla `GFX_mini_bg` panel and `GFX_flag_small2`.
The revealed command window reuses `GFX_cannibalism_continental_target_card` for each target card, the existing `GFX_portrait_<slot>_warlord_<region>` warlord portraits for loyalty rows, and the vanilla `GFX_sort_button_100x29` tab buttons and `GFX_mini_bg` row panels.
No new icon is required.

## Future plans

- A per-viewer intelligence layer could hide strength and route records from countries that never received the report, if multiplayer secrecy becomes a design goal.
- Foreign intelligence agencies could buy a strength measurement on a foreign node, writing through `cannibalism_ui_store_observed_strength_band`.
- Warlord raids and continental campaign operations could add their own incident kinds once those windows read the same record model.
