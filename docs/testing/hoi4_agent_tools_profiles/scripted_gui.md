# Scripted GUI review profile

Check the connected server version, health, live `hoi4.gui_inspect`, `hoi4.gui_render`, and `hoi4.scenario_test` schemas, and client task negotiation before using those routes. Run the supported read-only calls only. `scripted_gui_suite.json` names explicit 1920 by 1080, UI scale 1 scenarios and retains inspect and render artifacts; run it through `hoi4.scenario_test` only when that route is present. A successful suite identifies the tested source and scenarios but does not establish a visual match by itself.

| Surface | Source | Scenario facts and review |
| --- | --- | --- |
| Chaos Meter history | `common/scripted_guis/chaosx_scripted_gui_chaos_meter.txt`, `interface/chaosx_chaos_meter_popup.gui`; `chaos_meter_popup_window` and `chaos_meter_history_content_window` | Set `chaos_meter_window_open` and `chaos_meter_history_tab`. Inspect header, history filters, list rows, detail selection, labels, and click regions. |
| Chaos Meter air | The same files; `chaos_meter_air_content_window` | Set `chaos_meter_window_open` and `chaos_meter_air_tab`. Inspect the cleanliness checkbox, source rows, disabled reasons, detail overlay trigger, and clipping. |
| Settings | `common/scripted_guis/chaosx_scripted_gui_settings.txt`, `interface/chaosx.gui`; `chaosx_settings_window` | Set `chaosx_settings_open`. Inspect selected controls, dynamic text, button states, and reference alignment. |
| Scenarios | The same files; `chaosx_scenarios_window`, `chaosx_scenario_confirm_window`, `triggerable_scenario_entry_generic` | Set `chaosx_scenarios_open`, `triggerable_scenarios_selected = 16`, and intensity 1, 2, 3, and 4 in separate scenarios. Inspect list selection, launch gate, confirmation, row click regions, and empty-list state. |
| Communist insurgency | `common/scripted_guis/001_communism_spread_scripted_guis.txt`, `interface/chaosx_decisions.gui`; `communism_spread_dashboard_container` and `communism_control_state_mapicon_container` | Inspect the threat meter image, dashboard bounds, and source state flags. Mapicon level 1, 2, and 3 visibility requires explicit owned-state and global-flag facts. |

For each window, save the `hoi4.gui_inspect` source identity, hierarchy, fidelity findings, and click regions, then review the full and cropped `hoi4.gui_render` images at the same scenario and resolution. Compare text glyph bounds, background interiors, list clipping, panel spacing, button availability, and effective hitboxes. Retain source revisions and exact scenario IDs. `comparisonScenario` compares scenarios supported by the render route; it does not supply an older source baseline. The user performs live-game validation.

The installed GUI and scripted GUI documentation and the offline wiki pages are the syntax references. The installed `sov_paranoia_system_scripted_gui.gui` and `SOV_paranoia_system_scripted_gui.txt` show a vanilla meter consumer. This profile changes no GUI source.
