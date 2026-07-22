# Event 014 Interface and Focus Visual Quality Audit

## Scope

This review is limited to the five direct Event 014 GUI windows in
`interface/014_cannibalism_frontline_hunger.gui` and the unified, Warlord, and
Wendigo focus trees in `common/national_focus/014_cannibalism_focus.txt`.

HOI4 MCP renders were exercised at 1280x720, 1920x1080, 2560x1440, and
1920x1080 at 125% UI scale. Event 014 states covered normal, hover, warning,
long-text, and missing-localisation. The focus trees were inspected and
rendered with the focus-tree skill's route, connector, bounds, icon, and
localisation checks.

## Applied Event 014 UI corrections

- The early active-mission summary now has a wider/taller text box and is moved
  up slightly so three-line dynamic objectives do not collide with the button
  row.
- Network tabs use a consistent 0.82 scale, with the long Countermeasures label
  at 0.74, preventing text clipping while retaining separate click targets.
- Network country/state entries allow 56 px of dynamic text height inside their
  64 px cards, covering long names and stage/node labels.
- The Warlord raised-formations readout is widened and given additional height
  for large unit-capacity values.
- The selected-target tooltip says “recorded actor and state identity,” keeping
  pre-reveal language descriptive without implying a revealed leader.

## MCP and audit evidence

- All five Event 014 windows rendered successfully before the final text-box
  patch at all four resolution/scale profiles; authored backgrounds, cards,
  meters, portraits, lists, and controls stayed within their parent bounds.
- The renderer's visible-overlap counts (24, 32, 29, 39, and 37) are the
  intentional animated/static fallback siblings sharing a position. The
  scripted GUI visibility gates select one sibling at runtime.
- The MCP source graph reports `player_context` as unknown in the Event 014
  scripted GUI. Offline Paradox wiki and vanilla documentation use this
  context, so it is retained rather than rewritten around a validator-only
  false positive.
- The decision audit found 16 GUI buttons with matching click handlers, 31 text
  keys and 38 tooltip keys localized, and no gameplay effect bypass in GUI
  callbacks.
- The country audit found all five windows bounded, all 54 Event 014 GUI sprite
  references declared, all texture files present, and 24 animation sheets with
  static fallbacks.

## Focus-tree findings

- Unified: 108 focuses, 132 connectors, bounds x4..44/y0..27, zero node
  intersections, and the documented convergence-bridge crossings. The
  crossings are structurally minimized with fixed authored endpoints; no safe
  coordinate-only patch was identified.
- Warlord: 68 focuses, 79 connectors, no crossings or node intersections; two
  unobstructed long bridges remain as deliberate route-spanning prerequisites.
- Wendigo: 28 focuses, 32 connectors, no crossings or node intersections; five
  long bridges remain as deliberate anchor/countdown prerequisites.
- All 204 focuses have rewards, AI weights, icons, localisation, and matching
  GFX coverage. No dangling references or duplicate coordinates were found.

## Remaining limitations

The Event 014 catalog audit also corrected the authoritative scenario ordering:
`Scenarios!A10:F10` is now SCN-010 “The Hunger Lines,” with SCN-009 retained
at row 11. The three canonical catalog CSV exports were regenerated from the
workbook after that save.

- The final post-patch MCP rerender could not reconnect after a parallel MCP
  transport shutdown. The pre-patch matrix is complete, and the applied changes
  are bounded source-only text/scale adjustments; a fresh MCP rerender should
  be performed when the server is available.
- MCP's offline overlap counter and whole-mod diagnostics include known vanilla
  texture-inventory and scripted-context false positives. They are recorded,
  not “fixed” by changing valid engine contracts.
