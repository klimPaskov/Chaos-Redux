# Event 020 focus and shared disease-board layout audit

## Scope

This handoff covers the two Event 020 Rat Nation focus trees and the shared disease-containment scripted GUI presentation surface.

It does not close the Event 020 scenario tranche, modify the separately promoted shared rat model package, or claim live Hearts of Iron IV validation.

The offline Paradox wiki pages for focus trees, interface modding, scripted GUI modding, decisions, triggers, effects, scopes, localisation, and on actions were consulted alongside the vanilla focus and GUI documentation and vanilla precedents.

## Focus-tree implementation

The compact MCP rewrite proposal for the Rat Nation tree was rejected by the MCP quality gate because its proposed layout had crossings and node intersections, so the source was repaired by authored, source-controlled geometry instead of accepting that proposal.

The Rat Nation tree now has 52 focuses, including the visible `black_plague_rat_pressure_matrix` trunk after capped pulses and the visible `black_plague_rat_route_convergence` aggregation point before the four military methods.

The Rat King tree retains 71 focuses and keeps its four governance lanes, crisis row, royal-node watch, strike preparation, and terminal convergence in the compact authored geometry.

Every Event 020 focus has a route-appropriate `search_filters` declaration, direct localisation, an existing Event 020 icon, and an AI weight or inherited AI decision that matches its route.

The new visible aggregation points replace the previous isolated lower choices without adding tags or changing the two-tag Rat Nation and Rat King design.

The archetype-specific logistics lanes and the four-origin capped-pulse gate retain availability conditions tied to the selected origin and hierarchy route, while their coordinates remain separated from the visible shared trunk so the tree does not draw long fan connectors through the logistics lanes.

## MCP focus evidence

| Tree | Earlier layout | Final MCP national inspection | Final render and raster |
| --- | --- | --- | --- |
| Rat Nation | 50 focuses, bounds -9..9, 48 connectors, 4 crossings, 15 node intersections, and 7 long connectors | 52 focuses, bounds x -10..10 and y 0..18, 45 connectors, 0 crossings, 0 node intersections, 0 long connectors, maximum horizontal span 6, maximum vertical span 3, maximum Manhattan span 8, centered symmetry, and minimum same-row spacing 2 | `FOCUS_RENDERED` and `FOCUS_RASTERIZED`, 1752x1108 raster, layout hash `9b62e3206ed26a11a48793a905db1d1593fa352057cabba3417f410c26256987` |
| Rat King | 71 focuses, bounds -20..16, 78 connectors, 13 crossings, 8 node intersections, and 6 long connectors, including the royal-node watch and crown-strike parent-order defects | 71 focuses, bounds x -16..16 and y 0..20, 73 connectors, 0 crossings, 0 node intersections, 0 long connectors, maximum horizontal span 8, maximum vertical span 2, maximum Manhattan span 9, centered symmetry, and minimum same-row spacing 2 | `FOCUS_RENDERED` and `FOCUS_RASTERIZED`, 2712x1218 raster, layout hash `e80849e1e36f82f8f914954d387346b598d454ed170dc0cc6f63076bb6cff1a4` |

The final focus inspections report no Event020-owned diagnostics for either tree.

The MCP aggregate still reports 14 blocking diagnostics from the vanilla continuous-focus palette because the offline workspace scan cannot resolve those generic focus sprites; none points to an Event020 focus.

The focus probability adapter also passed bounded inspections without unresolved inputs: the Rat Nation candidate pool contained 4 focuses with 2 required inputs, and the Rat King candidate pool contained 6 focuses with 5 required inputs.

## Shared scripted GUI and layout

`common/scripted_guis/biowarfare_disease_containment_scripted_gui.txt` remains a single shared disease-category interface with five disease tabs, a state dynamic list, state selection, filtering, refresh, close, and map navigation actions.

State-row selection is now enabled only when the shared disease category is visible and the board-open flag is present in the player scope, which prevents stale dynamic-list click targets after the popup closes.

The board exposes navigation and target-selection controls only, while disease treatment, quarantine, cordon, rat-control, and cleanup actions remain decisions in the shared `biowarfare_disease_containment` category.

`interface/biowarfare_disease_containment.gui` keeps the presentation surface background-first and compact.

| Surface | Geometry and coverage |
| --- | --- |
| Header | 470x150, title at x22 y14, summary at x22 y48, Black Plague countermeasure text at x22 y104, infestation static and animated overlays at x288 y101, and one open action at x330 y106 |
| Popup shell | 900x650, title and summary in the top band, five disease tabs at y110, refresh and close in the top-right band, and no disease-specific decision category |
| Filters | Status, ownership, urgency, and region controls at y212, each with a tooltip and a scripted action |
| State list | Background panel at x18 y278 with a 400x338 scroll region and one 376x66 dynamic entry slot |
| Selected card | Background panel at x438 y212 with a 438x404 card, conditional private/public/Black Plague values, response target text, and one map-goto action |
| Dynamic entry | A transparent full-entry button owns selection, while the name, selected marker, and response marker are non-clickable text layers |

The header MCP inspection returned `GUI_INSPECTED` for `disease_containment_default`, with seven inspected elements and the local window source resolved.

The header MCP render returned `GUI_RENDERED` for normal, hover, selected, disabled, warning, long-text, and missing-localisation probes at 1920x1080 and 2560x1440, with a stable comparison and no local source overlap in the layout artifact.

The header layout artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a53580c3f16e27239c2f1acc7c408e04cee41b0bb2adbceb63bf42eba860ca5d/f8fa6af3fe36049d3cf21521dbdc022ee3a5a31bd0c897ceb18bf21cb9413d5b/disease_containment_header_window-layout.json`.

The board inspection and render both return `SCAN_BYTE_LIMIT` before producing an artifact because the repository-wide scripted-GUI source graph exceeds the configured offline scan budget.

The GUI source graph also reports the existing repository-wide `player_context` diagnostics and four global visible-overlap diagnostics; the offline wiki and vanilla scripted-GUI precedents support `player_context`, and the reported overlaps are outside the bounded Event020 header geometry.

The renderer reports the vanilla tiled-window texture and animated-sprite limitations as offline representation warnings, not missing Event020 runtime references.

## Remaining blockers and deviations

- Live Hearts of Iron IV testing is still required by the user and was not run because repository instructions reserve live consumer validation for the user.
- The separately promoted shared rat model/entity package is outside this layout pass; no per-subtype or Rat King-specific model is produced here, and sound-definition wiring, counter review, and live model playback remain open.
- Part 9 scenario content remains a separate partial tranche and is not claimed complete by this handoff.
- Full unbounded Rat Nation probability analysis timed out, so the committed evidence uses the bounded candidate pool with complete adapter coverage.
- The shared disease board could not receive a full popup render artifact because the MCP scanner stopped at `SCAN_BYTE_LIMIT`; the source geometry and header evidence remain available.

No dedicated Black Plague decision category was introduced, no extra rat tags were added, and no fallback asset or placeholder tree was introduced by this pass.
