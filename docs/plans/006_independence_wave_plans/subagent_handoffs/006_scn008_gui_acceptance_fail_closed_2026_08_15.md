# SCN-008 scenario-detail GUI acceptance handoff (2026-08-15)

## Disposition

SCN-008 has no event-owned scenario-detail window that this worker can safely patch. The selected-mode list and detail body resolve to the shared `chaosx_scenarios_window` used by every triggerable scenario. Event 006 owns `independence_wave_status_window`, which is the separate Statehood Ledger and does not contain the SCN-008 scenario list or detail body. The GUI scope is therefore fail-closed with no source edit.

The existing eight SCN-008 descriptions are already the current wording authority. They were shortened by the preceding localisation-fit handoff and retain the required mechanics without semicolons or vague mechanics. A further layout or text patch would either modify the shared scenario framework or diverge from the current workbook mirror, so no bounded fix is justified on this route.

## Event ownership and exact entry points

The named event is Event 006, `006_independence_wave`, with runtime scenario id `independence_wave` and catalog id `SCN-008`.

Event-owned GUI identifiers are `independence_wave_status_scripted_gui` and `independence_wave_status_window`. They are defined in `common/scripted_guis/006_independence_wave_scripted_gui.txt` and `interface/006_independence_wave.gui`. That window contains the Statehood Ledger values, tabs, and status controls. It has no `scenario_list_box`, `scenario_list_dynamic_list`, `scenario_detail_box`, or `scenario_detail_body`.

The SCN-008 list and detail route is shared. Its exact identifiers are:

- scripted GUI `chaosx_scenarios_gui` with `window_name = "chaosx_scenarios_window"`
- window `chaosx_scenarios_window`
- list container `scenario_list_box`
- dynamic list `scenario_list_dynamic_list`
- detail container `scenario_detail_box`
- selected title `scenario_detail_title`
- selected body `scenario_detail_body`
- generic list entry `triggerable_scenario_entry_generic`
- entry button `scenario_entry_open_details_button`
- confirmation window `chaosx_scenario_confirm_window`

The shared scripted GUI is `common/scripted_guis/chaosx_scripted_gui_settings.txt`. The shared layout is `interface/chaosx.gui`. The shared scripted localisation is `common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt`. The shared display localisation is `localisation/english/chaosx_gui_l_english.yml`. These files serve the generic triggerable-scenario framework and remain outside this event-owned task.

The settings entry point is the shared `open_chaosx_scenarios` flow and the `chaosx_scenarios_open` flag. Event 006's hidden launch event is `chaosx.triggerable_scenarios.8` and its summary event is `chaosx.triggerable_scenarios.80` in `events/006_independence_wave_scenario.txt`. Those event ids do not transfer ownership of the shared window to Event 006.

## Exact localisation and asset identifiers

The eight selected-mode descriptions are in `localisation/english/006_independence_wave_scenario_l_english.yml`:

- `chaosx.scenarios.independence_wave.desc.sovereign_scatter`
- `chaosx.scenarios.independence_wave.desc.common_congress`
- `chaosx.scenarios.independence_wave.desc.wars_of_separation`
- `chaosx.scenarios.independence_wave.desc.universal_former_hosts`
- `chaosx.scenarios.independence_wave.desc.universal_neighboring_releases`
- `chaosx.scenarios.independence_wave.desc.universal_nearby_nonleague`
- `chaosx.scenarios.independence_wave.desc.patron_worlds`
- `chaosx.scenarios.independence_wave.desc.great_partition`

The same file owns the intensity keys `chaosx.scenarios.independence_wave.impact.low`, `chaosx.scenarios.independence_wave.impact.medium`, `chaosx.scenarios.independence_wave.impact.high`, and `chaosx.scenarios.independence_wave.impact.maximum`, the launch status keys under `chaosx.scenarios.launch_status.independence_wave.*`, the entry id `chaosx.scenarios.entry.id.independence_wave`, and the scenario name key `chaosx.scenarios.independence_wave.name`.

The shared scripted-localisation identifiers used by the detail route are `GetTriggerableScenarioSelectedName`, `GetTriggerableScenarioSelectedDesc`, `GetTriggerableScenarioEntryName`, `GetTriggerableScenarioEntryId`, `GetTriggerableScenarioIntensityName`, `GetTriggerableScenarioTypeName`, `GetTriggerableScenarioWarning`, and `GetTriggerableScenarioLaunchStatus`.

The shared GUI reuses `GFX_tiled_window_2b_border`, `GFX_generic_popup_win`, `GFX_closebutton`, `GFX_scroll_drager`, and the Chaos Redux sprites `GFX_chaosx_settings_button_main_buttonstate`, `GFX_chaosx_chaos_meter_entry`, `GFX_chaosx_arrow_left`, `GFX_chaosx_arrow_right`, and `GFX_chaosx_button_123x34`. The Chaos Redux registrations are in `interface/chaosx.gfx`. No SCN-008-specific background, frame, icon, or animation asset is missing and no asset handoff is required.

## Current wording and workbook authority

The eight current descriptions are the ones in `006_independence_wave_scenario_l_english.yml` and are mirrored by the preceding fit audit. The current text is:

| Mode | Current description |
| --- | --- |
| Sovereign Scatter | Every viable movement is attempted. Each release keeps a protected former-host remnant and unique anchor. States remain outside pre-formed leagues and retain no release-created faction ties. Intensity changes territory, forces, institutions, and pressure. |
| Common Congress | Every viable movement is attempted under protected hosts and unique anchors. New states join an informal congress network. Higher intensity strengthens its charter and shared reserve. |
| Wars of Separation | Every viable movement is attempted. A country that can lawfully confront its surviving former host may open one separation war. Others receive a regional threat mission. |
| Universal Belligerence: Former Hosts | Every viable movement is attempted. Each new country may face one bounded former-host conflict. Invalid declarations become regional threat missions. Host remnants and homelands are secured first. |
| Universal Belligerence: Neighboring Releases | Every viable movement is attempted. Each new country may open one bounded war against one neighboring release from the same incident. One-time targets prevent an all-against-all cascade. |
| Universal Belligerence: Nearby Nonleague States | Every viable movement is attempted. Each new country may open one bounded war against one nearby independent state outside the League and every faction. Distance and one-time targets keep the crisis regional. |
| Patron Worlds | Every viable movement is attempted. Each new country seeks one reachable major patron, preferring ideological affinity and regional proximity. Intensity scales influence, aid, recognition, and capacity. |
| Great Partition | Every viable movement is attempted. Hosts retain one protected remnant state, preferring a controlled capital, then a safe core or owned state. Intensity grants the next non-overlapping tier, with stronger border pressure, host claims, ambitions, and formables. |

The editable workbook remains `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, with the SCN-008 mirror in `Scenarios!C8`. The export mirror is `docs/spreadsheets/chaos_redux_scenarios_catalog.csv`. The preceding handoff records the current Scenarios export SHA-256 as `489dc1772284bda64b8903a87b23b0d9f841335e866319b17b90d75570dd5af8` and `Scenarios!F8 = Unavailable`. This worker did not edit the workbook or either CSV.

## Layout hierarchy and value and action budgets

The shared `chaosx_scenarios_window` is a 760 by 500 movable window at `position = { x = -790 y = 92 }` with a tiled `GFX_tiled_window_2b_border` background. Its hierarchy is:

1. Header title and hint, followed by close control.
2. Left list heading and two sort-control rows.
3. Left `scenario_list_box` at 260 by 276 with a scrollbar and one-column `scenario_list_dynamic_list` at 220 by 260. Each `triggerable_scenario_entry_generic` is 224 by 41 inside 224 by 44 slots.
4. Right `scenario_detail_box` at 424 by 326.
5. Right selected title at `{ x = 310 y = 120 }` with `maxWidth = 404` and `maxHeight = 34`.
6. Right selected body at `{ x = 318 y = 160 }` with `maxWidth = 388` and `maxHeight = 104`.
7. Shared intensity, type, warning, trigger, and confirmation controls.

The detail body is descriptive text rather than an event-owned primary mechanic value. The shared panel exposes intensity and type as its supporting values. Its action budget is shared list selection, two sort controls, four intensity stops plus arrows, type arrows, trigger, confirmation, and close. These controls are not candidates for an Event 006 UI patch.

The background coverage map is the window tiled border, the list tiled plain background, the detail tiled plain background, and the vanilla or Chaos Redux button and slider sprites. There is no unassigned SCN-008 ornament or functional anchor to resolve.

## Mandatory MCP evidence

All MCP calls were made before any edit. No source edit followed the calls.

### Shared SCN-008 list and detail inspect

`hoi4.gui_inspect` used `windowName = "chaosx_scenarios_window"` and `scenario = { id = "independence_wave" }`.

The focused result was `GUI_INSPECTED` with 36 inspected elements, no local `GUI_VISIBLE_OVERLAP` failure, and complete model extraction. The artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/06d28e9174ee47d096b51b858dd0ea99deb795a308c674704badf93a383311e9/9bc3ee22e139032c4e69bf7b0642f5b39a1c3bd067460bc5a4d792e0489d9a/gui-inspect.57021b835ecdacd3.json`.

The shared graph is aggregate-invalid. The retained global diagnostic bound is 2,000 with source inventory, graph, and validation diagnostics truncated. The focused fidelity counts were 287 modelled, 8 approximated, 75 ignored, 6 missing, 58 unsupported, and 8 unresolved. This is not family-isolated acceptance evidence.

### Event-owned control inspect

`hoi4.gui_inspect` used `windowName = "independence_wave_status_window"` and `scenario = { id = "independence_wave" }`.

The result was `GUI_INSPECTED` with 48 inspected elements. It confirmed a separate Statehood Ledger surface and no local `GUI_VISIBLE_OVERLAP` failure. The artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/138d5d0ad9eeaa4d1aba596f8fd9e6763b079059a7185394894c63072a9055d1/f4d63b8000b03e33271723d3599f26a98ef8f65cb7440b1999971d977137ae15/gui-inspect.4380f9d774eb2b27.json`.

This route is also aggregate-invalid because the workspace graph retained 2,000 blocking diagnostics. Its focused output reported 75 overlap findings and 11 alignment findings in the event-owned ledger. Those findings are outside the SCN-008 scenario-detail surface and were not patched.

### Shared render

`hoi4.gui_render` used `windowName = "chaosx_scenarios_window"`, `scenario = { id = "independence_wave" }`, the states `normal`, `hover`, `selected`, `locked`, `disabled`, `warning`, `active`, `completed`, `empty-list`, `full-list`, `minimum-value`, `maximum-value`, `long-text`, and `missing-localisation`, and resolutions 1920 by 1080 and 2560 by 1440. A comparison scenario with the same SCN-008 id was supplied.

The result was `GUI_RENDERED` with a full-window SVG artifact at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ec5e0c0895fb42ae0b8d229c19e98de887e0909ccbaa016e2033308a3bb55a7b/f51a6d4c0a86501d94df206efa04fcc28a7e2b2b23e2286139b7a8d68e2145ca/chaosx_scenarios_window-full.svg`. The artifact SHA-256 is `ec5e0c0895fb42ae0b8d229c19e98de887e0909ccbaa016e2033308a3bb55a7b`.

The renderer response was wire-truncated and reported `MCP_RESPONSE_TRUNCATED`. It provided no reliable crop, annotation, hierarchy, click-region, per-state, or comparison payload. The renderer is an offline approximation, so the SVG is evidence of route resolution only and does not certify wrapping, clipping, state fidelity, or family isolation.

### Event-owned control render

The same state and resolution matrix was requested for `independence_wave_status_window`. The result was `GUI_RENDERED` with `MCP_RESPONSE_TRUNCATED` and a full-window SVG at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7151f87950fd10f39ae7cf64c5dc04fee0744ed2835a3358531571452bcdae64/64dee62894b5ffb9571530113242c1cc266282d49e3a15fb605c4b7558ce9613/independence_wave_status_window-full.svg`. This confirms the separate event-owned route but does not certify the shared scenario detail list.

An exploratory comparison payload using the unsupported `comparisonScenario.compare` field was rejected with MCP error `-32602` before rendering. The valid render call used the supported comparison scenario shape and still returned the wire-truncated result above.

The installed route does not expose a family-isolated SCN-008 render with separate cropped, annotated, hierarchy, click-region, and comparison artifacts. This is the exact renderer blocker. Source-only inspection cannot replace that evidence.

## Before and after disposition

There is no source before and after because the only candidate list/detail surface is shared. The prior localisation-fit change is already reflected in the current eight descriptions and workbook mirror. The focused pre-existing shared inspect found no local visible-overlap failure, and no safe geometry or text change can be justified without family-isolated wrapping and clipping evidence.

No `hoi4.gui_rewrite` was issued. A rewrite would target shared `interface/chaosx.gui` or shared scripted-GUI wiring and would violate the event-owned scope boundary.

## References inspected

The accepted Event 006 specifications are `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_6_formables_league_and_scenario.md` and `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_7_ai_balance_assets_and_acceptance.md`. The system contract is `docs/systems/event_system/triggerable_scenarios.md`. The preceding wording authority is `006_scn008_detail_localisation_fit_audit_2026_08_15.md`.

The required offline Paradox pages were consulted for Interface Modding, Scripted GUI Modding, Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding. Vanilla documentation was consulted in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation`, including script concepts, triggers, effects, and localisation formatting. The vanilla `war_escalation_scripted_gui` and `war_escalation_scripted_gui.gui` were inspected as the closest compact scripted-GUI precedent.

## Files changed

Only this handoff file was added. No GUI, scripted-GUI, scripted-localisation, display-localisation, GFX, sprite, gameplay, event, catalog, workbook, or CSV source was changed by this worker.

## Remaining parent-owned work and blockers

The parent retains gameplay, event admission, package attestation, typed scenario registration, event projection, catalog status, workbook authority, shared settings UI, and live consumer validation. SCN-008 remains catalog `Unavailable` and fail-closed under the existing gates.

The required next validation is a family-isolated MCP inspect and render for the actual SCN-008 scenario-detail route, including full-window, cropped, annotated, hierarchy, click-region, state, resolution, and comparison evidence. That route must be provided or activated by the shared GUI owner. Until then, no source layout change is authorized from this event-scoped worker.

## Simplifications and unresolved states

No source fix was applied. The shared scenario framework was not audited or restyled. The event-owned Statehood Ledger was not modified. No workbook or catalog edit was made. No in-game completion claim is made. The renderer remains offline or wire-truncated for the required family-isolated evidence.
