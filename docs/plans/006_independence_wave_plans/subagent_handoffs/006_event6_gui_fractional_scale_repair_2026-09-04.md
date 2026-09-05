# Event 006 status-window fractional-scale repair

Audit date: 2026-09-04. Scope: the Event 006 `independence_wave_status_window` icon placements only.

## Repair

`interface/006_independence_wave.gui:17-31` now uses `scale = 0.75` for the five 64x64 ledger icons, the four state-strip/static seal icons, and their four animated siblings. The previous `scale = 0.72` produced a 46.08-pixel footprint; the focused GUI inspector reported repeated `GUI_ACCIDENTAL_CLIPPING` findings caused by the fractional raster boundary. The new 0.75 scale produces an exact 48x48 footprint without changing positions, sprite identifiers, frame variables, visibility triggers, or the accepted five-tab layout.

The largest right-edge placement remains inside the 700-pixel window (`x = 598` plus 48 pixels), and the left ledger icons remain separated from their value text (`x = 24` plus 48 pixels before the text at `x = 74`). No asset bytes, texture paths, GFX definitions, gameplay effects, or localisation changed.

## Evidence

Pre-change focused `hoi4.gui_inspect` on the same window and Government-tab fixture returned `GUI_INSPECTED` with a complete source graph and the expected nonblocking background/animation diagnostics; it also reported fractional clipping for the 46.08-pixel icon renders. The post-change `hoi4.gui_inspect` retry and the narrow `hoi4.gui_render` retry both timed out at the installed MCP 180-second boundary before returning an artifact. This is recorded as a tooling limitation, not as a post-change visual pass.

The source-level GUI matrix still passes its five mutually exclusive tab contracts, four static/animated sibling pairs, frame counts, and cleanup receipts. The earlier explicit Government-tab render remains the last successful consumer render; no live game or save/load claim is made.

## Status

The source-local fractional clipping condition is repaired. ASSET-039 remains `needs_user_review` because dynamic tab-state rendering, click-region proof, and animated playback still require a responsive MCP route or live owner verification. The generated no-flag renderer's stacked explanatory panels remain a fixture limitation: the actual scripted GUI exposes only the selected panel.

No fallback art, duplicate sprite, unsupported GFX field, or cross-family asset was introduced.
