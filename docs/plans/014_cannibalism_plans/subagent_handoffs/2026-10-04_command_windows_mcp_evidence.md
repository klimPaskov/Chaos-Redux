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

## Revealed command window (`cannibalism_revealed_command_window`)

| Scenario | Result | Image |
| --- | --- | --- |
| `E014_R1_REVEALED_BEFORE_20261004` | `GUI_RENDERED`, source revision `a75fb6dfc549383b44da797ca5dac4fb427eb702cd94e88881aad5cadef6528a`; one page with the Larder, Network Reach and integration count, no loyalty list and a single static target card holding totals | [revealed_before.png](2026-10-04_command_windows_mcp_evidence/revealed_before.png) |
| `E014_R1_REVEALED_AFTER_OVERVIEW` | `GUI_RENDERED`, source revision `4bea8b442738fef3a1c958d2e2324428f134924d9deb7362b13890fe98c73b15`; three page tabs under the portrait, the Overview values and the terminal progress line below the tabs | [revealed_after_overview.png](2026-10-04_command_windows_mcp_evidence/revealed_after_overview.png) |
| `E014_R1_REVEALED_AFTER_LOYALTY_CROWDED_V2` | `GUI_RENDERED`, source revision `7d547b811f93c6aa4ad4d8617f904d150bfab6a3b5e9191436d6086186f77733`; four rows in each list scroll inside two-row panels, portraits, names, origins, dispositions and dates stay clear of the scrollbars | [revealed_after_loyalty_crowded.png](2026-10-04_command_windows_mcp_evidence/revealed_after_loyalty_crowded.png) |
| `E014_R1_REVEALED_AFTER_TARGETS` | `GUI_RENDERED`, source revision `7399fb3359fa622a510f5c70a6bf2d6baad404cb93066aa2d585d8ba6cff4e53`; the three rolling target cards fill the panel with a long country name, kind and commit date | [revealed_after_targets.png](2026-10-04_command_windows_mcp_evidence/revealed_after_targets.png) |
| `E014_R1_REVEALED_AFTER_TARGETS_EMPTY_V2` | `GUI_RENDERED`, source revision `2c2b8488b539e6946f46b5f815a5f2d2b7a4f04fe1d7b4f35e4411b74485bad1`; the empty card text fits on three lines | [revealed_after_targets_empty.png](2026-10-04_command_windows_mcp_evidence/revealed_after_targets_empty.png) |

The first empty-targets render (`E014_R1_REVEALED_AFTER_TARGETS_EMPTY`, revision `980c2f84`) clipped the fourth line of the empty text, and the text was shortened before the V2 render.
The first crowded loyalty render (`E014_R1_REVEALED_AFTER_LOYALTY_CROWDED`) put row text under the scrollbar, and the rows were narrowed to 258 pixels before the V2 render.
An earlier target layout with a scrollbar overran the 470-pixel window, so the target panel holds exactly the three rolling cards without one.
Remaining inspector warnings are the pre-existing missing static fallback for the animated revealed portrait and background overlap notes.
