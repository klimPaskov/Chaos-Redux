# Event 014 command windows MCP evidence

Date: 2026-10-04.
Owner: implementing agent (Event 014 takeover, round 1).
Routes: `hoi4.gui_render` at 1920x1080, UI scale 1, generated scenarios disabled; cropped PNG artifacts read through the MCP resource route.
Scenario overrides set list sizes, element visibility for the page under test, and worst-case localisation, because the offline renderer does not run the page flags or scripted localisation.

## Host command window (`cannibalism_warlord_command_window`)

| Scenario | Result | Image |
| --- | --- | --- |
| `E014_R1_WARLORD_BEFORE_20261004` | `GUI_RENDERED`, source revision `910286ded76682f731db8997fe4c552d637f049ea2ff39a66616efdad3cd5c53`; four value groups, no page tabs, no state or raid card | [warlord_before.png](2026-10-04_command_windows_mcp_evidence/warlord_before.png) |
| `E014_R1_WARLORD_AFTER_OVERVIEW` | `GUI_RENDERED`, source revision `ca881af4034e1cc04b16a4c2666e5d6b76a03ab3dc063adeacd2ccbd1c83c7a9`; tabs above the four value groups, all inside the 340-pixel window | [warlord_after_overview.png](2026-10-04_command_windows_mcp_evidence/warlord_after_overview.png) |
| `E014_R1_WARLORD_AFTER_STATES_CROWDED` | `GUI_RENDERED`, source revision `90a877bfcf9431cec76e93a9af93e3e0781677a66080af6d9d4d8b0cca8b6799`; four state cards scroll in a two-card panel, the raid card shows a disabled-hub receipt | [warlord_after_states_crowded.png](2026-10-04_command_windows_mcp_evidence/warlord_after_states_crowded.png) |
| `E014_R1_WARLORD_AFTER_STATES_EMPTY` | `GUI_RENDERED`, source revision `2f8509d3093fe21a784520c5aa8ac89ae60b704a406ef1bf2db1f6069c98b989`; empty-list text and the no-raid card | [warlord_after_states_empty.png](2026-10-04_command_windows_mcp_evidence/warlord_after_states_empty.png) |

Remaining inspector warnings are the pre-existing missing static fallbacks for the larder glow, frenzy border and route emblem sheets and background overlap notes; the tab clipping note is a sub-pixel rounding report.
