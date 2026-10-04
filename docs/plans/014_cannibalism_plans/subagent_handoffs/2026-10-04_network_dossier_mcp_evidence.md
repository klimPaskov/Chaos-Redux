# Event 014 Network dossier MCP evidence

Date: 2026-10-04.
Owner: implementing agent (Event 014 takeover, round 1).
Disposition: `implemented` for E014-FINAL-02 source and production-render review; live in-game behaviour remains with the orchestrator.

## Routes used

- `hoi4.gui_inspect` and `hoi4.gui_render` on `cannibalism_network_window`, generated scenarios disabled, 1920x1080 at UI scale 1.
- Artifact bytes were read through the MCP resource route with byte ranges (`?offset=&length=`), joined locally, and SVG renders were rasterized with headless Chrome (no visible window).
  The earlier `Artifact provenance manifest is unavailable` blocker did not recur.

## Before

| Call | Scenario | Result |
| --- | --- | --- |
| `gui_inspect` | `E014_R1_NETWORK_BEFORE_20261004` | `GUI_INSPECTED`, revision `622a3d1b98d13620687bf03aeb9df479bbd2ba223475c2b181ba207423d4c244`, 41 elements, 3 unresolved, 3 unsupported |
| `gui_render` normal | `E014_R1_NETWORK_BEFORE_20261004` | `GUI_RENDERED`, source revision `a0612d505a78e57fbb98fc83fd1ef3dbf02813aac6456b639913970a9a48c728`, cropped PNG SHA-256 `419b44f1a1ff2e471bb5e778befe353e941dc665f3082b4570fa0aa6595bbe22` |

The before render ([network_before_cropped.png](2026-10-04_network_dossier_mcp_evidence/network_before_cropped.png)) shows only the lower-right quarter of the window: `origo = center` with `clipping = yes` clipped the window at its anchor, and the inspector reported the list scrollbars clipped from 18x222 to 18x20.

## After

| Call | Scenario | Result |
| --- | --- | --- |
| `gui_render` normal, full-list, long-text | `E014_R1_NETWORK_AFTER_EMPTY` | `GUI_RENDERED`, source revision `262213203dfa86890698aba90c72ff4968a591a7f92f01cd395344902dc36864`, whole window visible, no scrollbar clipping |
| `gui_render` full-list | `E014_R1_NETWORK_AFTER_FULLSTATE` | `GUI_RENDERED`, populated rows and both dossier lists (renderer fills both one-row lists) |
| `gui_render` normal with lists and text | `E014_R1_NETWORK_AFTER_SELECTED_STATE_TEXT` | `GUI_RENDERED`, source revision `3e3b60567bffa8a103163039da4e187d3d3ad529b9a60db9d5f15aef6bb1d9a4`, SVG SHA-256 `c002771b0a2c1de21bbda395aef0ea65a2b438b4029021ae1e5c17dcce0e815f` |
| `gui_inspect` | `E014_R1_NETWORK_AFTER_20261004` | `GUI_INSPECTED`, revision `b355f216bb5b3edee24c60b70792350c7b7e31dc0f473d87e4501c209443fe84`, 39 elements, 3 unresolved, 3 unsupported |

The selected-state render ([network_after_selected_state.png](2026-10-04_network_dossier_mcp_evidence/network_after_selected_state.png)) uses worst-case localisation overrides: the longest country and state identity lines, the longest route, a two-line certainty sentence and a two-line counteraction.
All row lines fit inside the 374x64 cards; the state rows end before the right-hand paper decoration, and the country rows reach the red seal without losing legibility.
The dossier sits on a dark `GFX_mini_bg` panel, and its identity text clears the frame clamps.
The empty render ([network_after_empty.png](2026-10-04_network_dossier_mcp_evidence/network_after_empty.png)) shows the prompt on the painted bottom card.

## Remaining limits

- The renderer resolves dynamic scripted-localisation only through scenario overrides, so real record text is proven by source review and the override render, not by a live save.
- The renderer does not evaluate the prompt's ROOT-variable trigger; the in-game prompt hides while a selection exists.
- The background art's painted list panels are narrower than the 374-pixel card art; populated rows cover them, as in the original layout.
- Remaining inspector warnings are the vanilla `GFX_tiled_window_transparent` declared-size note, the pre-existing missing static fallbacks for the threads and island alert sheets, and background overlap notes.
