# Event 017 Direct Interface Visual Audit

Audit refresh: 2026-07-25.

## Scope

This audit is limited to the direct Event 017 surfaces.
Event 017 does not define a bespoke `.gui` window or scripted-GUI root: its live interface is the vanilla decision surface (`countrydecisionview.gui`) populated by `random_faction_bloc_pressure_category`, its category picture/icon, and the decision rows in `common/decisions/017_random_faction_decisions.txt`.
Event report pictures remain on the vanilla report-event surface.

The vanilla category-header, category-description, and decision-row layout was checked against the offline Interface Modding documentation and the vanilla `interface/countrydecisionview.gui` precedent.
The standard row click boxes, track controls, collapse control, hover/select states, and scrollbar are therefore shared vanilla geometry rather than Event 017-owned coordinates.

## Event 017 asset and bounds checks

- The category icon and all eleven static decision icons are 32x32, matching the vanilla decision-row icon contract.
- Alpha bounds remain inside each static icon canvas, with no edge clipping.
- `random_faction_bloc_pressure_bg.dds` is 114x101, matching the vanilla category-picture slot used by other decision categories.
- The two animated decision sprites use eight 64x64 frames in 512x64 sheets, with stable per-frame anchors and static companions.
- Their use follows the existing vanilla animated-decision precedent in `003_holy_realm`.
- All 26 texture references in `interface/017_random_faction.gfx` resolve to existing runtime files.
- The four report-event images are already processed through the repository report-event pipeline.
- Their source and processed PNGs, transparent corners, and 210x176 runtime DDS copies are recorded in `docs/assets/017_random_faction/manifest.md`.

## Resolution and interaction review

The vanilla decision surface keeps the category description and decision list inside its scrollable 550px panel.
The Event 017 picture and 32px static icons fit the vanilla header/row bounds at the supported 1920x1080, 1366x768, 1280x720 (`uiScale = 0.9`), and 1024x768 (`uiScale = 0.8`) profiles.
The animated 64px rows follow the same unclipped oversized-icon convention used by the vanilla Holy Realm decision precedent; their alpha bounds stay centered and do not drift between frames.
No Event 017-owned position, click box, hover state, or clipping rule needs a patch.

The HOI4 MCP GUI inspector and renderer completed deterministic state and resolution matrices for `category_header`, `decision_category_desc`, `decision_item`, `targeted_decision_item`, `timed_decision_item`, and `countrydecisionview` using normal, hover, selected, locked, disabled, warning, active, completed, empty-list, full-list, long-text, and missing-localisation states.
The same matrix was rendered for 1920x1080 at UI scale 1.0, 1366x768 at UI scale 1.0, 1280x720 at UI scale 0.9, and 1024x768 at UI scale 0.8.
The MCP also inspected `EventWindow` for the four report-event picture variants.
The MCP reported shared vanilla-source diagnostics such as missing placeholder sprites and synthetic invisible controls, but none pointed to an Event 017-owned source path.
The main Events Log window was not inspected, per scope.

## Result

No direct Event 017 GUI defect was found and no Event 017 layout source needed editing.
Adding a custom window would change the accepted design (the spec explicitly uses the standard decision surface), so it is not introduced as a visual-audit workaround.
