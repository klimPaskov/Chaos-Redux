# Event 014 Interface and Focus Quality Audit

Scope: the five direct Event 014 GUI windows in `interface/014_cannibalism_frontline_hunger.gui`, their scripted GUI in `common/scripted_guis/014_cannibalism_scripted_gui.txt`, and the unified, Warlord, and Wendigo focus trees in `common/national_focus/014_cannibalism_focus.txt`.

The HOI4 MCP GUI matrix covered normal, hover, warning, long-text, and missing-localisation states at 1280x720, 1920x1080, 2560x1440, and 1920x1080 at 125% UI scale.

| Window | MCP result | Offline overlap count |
| --- | --- | ---: |
| `cannibalism_early_header_window` | `GUI_RENDERED`, no blockers | 24 |
| `cannibalism_network_window` | `GUI_RENDERED`, no blockers | 34 |
| `cannibalism_warlord_command_window` | `GUI_RENDERED`, no blockers | 29 |
| `cannibalism_revealed_command_window` | `GUI_RENDERED`, no blockers | 40 |
| `cannibalism_wendigo_command_window` | `GUI_RENDERED`, no blockers | 38 |

The overlap counts are intentional animated/static fallback siblings sharing coordinates; the scripted visibility preference selects one sibling at runtime.

Applied GUI corrections keep long dynamic text inside its cards: the early mission summary is 153x54 at (304,210), network tabs use 0.82 scale with Countermeasures at 0.74, network entry text allows 56 px inside 64 px cards, and the Warlord capacity readout is 150x52 at (304,248).

The selected-target tooltip uses recorded actor and state identity wording so the pre-reveal card remains descriptive without implying a revealed leader.

The GUI source has matching click handlers for every authored Event 014 button, and the current source audit found all direct Event 014 sprite, text, and tooltip references covered.

The MCP reports `player_context` as unknown for `cannibalism_network_scripted_gui`; the offline Paradox wiki and vanilla documentation define this context, so this is retained as a validator coverage limitation rather than rewritten engine-facing syntax.

Focus MCP inspection reports 108 unified focuses, 132 connectors, bounds x4..44/y0..27, 21 connector crossings, zero node intersections, and six long connectors; the full tree renders successfully.

The Warlord tree has 68 focuses and 79 connectors with zero node intersections and two long route-spanning connectors, while the Wendigo tree has 28 focuses and 32 connectors with zero node intersections and five deliberate anchor/countdown bridges.

The unified crossings are convergence prerequisites with fixed authored endpoints; the focus audit found no safe coordinate-only change that removes them without changing route structure. The long Warlord and Wendigo bridges are also deliberate cross-route prerequisites, not click-box collisions.

Focus MCP output additionally reports missing vanilla continuous-focus icons and one vanilla continuous-focus localisation key; those diagnostics are outside Event 014 source paths and do not identify missing Event 014 focus assets.

No additional direct Event 014 GUI or focus patch is justified by the final MCP matrix. The only remaining verification limitation is that MCP provides deterministic offline artifacts rather than a live game consumer view.
