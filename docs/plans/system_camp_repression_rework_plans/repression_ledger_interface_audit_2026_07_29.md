# Repression Ledger Interface Audit

## Scope

This audit covers only `repression_ledger_category_window` and `repression_ledger_window`, including the Overview, State Pools, Active Sites, Country Panel, and Discovery & Reform tabs.

The Event Log, general Chaos Redux windows, disease-containment windows, and unrelated CBRN interfaces are outside this audit.

## Maintained Visual Package

The Ledger continues to use its 24 static UI sprites derived from the accepted ImageGen sources.

No simple-shape substitute, placeholder frame, or newly generated fallback asset was introduced.

The authored 900 by 560 Ledger background, tab atlas, action-button atlas, country card, overview cards, selected-state frame, warning frame, icons, and seals retain their registered dimensions and one-to-one layout use.

## Review Method

The HOI4 GUI MCP inspected both linked windows and rendered the layout at 1280 by 720, 1366 by 768, 1600 by 900, and 1920 by 1080 with UI scale 1.

The rendered scenarios covered normal, hover, selected, disabled, warning, full-list, empty-list, long-text, and missing-localisation states.

Source review separately verified scripted tab visibility, scripted click handlers, localisation consumers, sprite registration, frame counts, and the interactive bounds that the offline renderer cannot execute.

Final category render:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/81ce704abc07fb41f4e2b5f55084d16e7781529aa5377c5e1a4a7f4c321ac235/101b7b0b48df864b4d4dedb8d68021986193a3a3c10cef306af3fc26e3ec3442/repression_ledger_category_window-full.svg`

Final Ledger render:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8362aa8398734e19481c12aede2828d8618d38f851ffeeb27a4fa7ee48f5f349/77754a56f603be5eba9a269b6f259b075b76ccaf4a7daf674bcc0b239266326a/repression_ledger_window-full.svg`

## Corrections

- The decision-category launcher now uses the same three-frame ImageGen-derived action atlas as the Ledger controls, with its click region matching the visible button.
- Category title and summary bounds now leave stable space for long country and panel names.
- Decorative textures, selected markers, warning overlays, status marks, and non-interactive text are click-through so they cannot intercept button clicks or tooltips.
- The title, phase indicator, and close control have explicit non-overlapping bounds.
- Tab labels are independent click-through text overlays, leaving room for the selected-tab emblem without label collisions.
- The Discovery & Reform label uses a bounded two-line presentation instead of clipping or shrinking into the marker.
- Overview card text and burden icons use separate columns, with burden icons stacked vertically.
- Discovery and reform card text leaves space for the 112 by 112 seals.
- The selected-state summary starts beyond its emblem and has a two-line bound.
- Pool and site rows retain six non-overlapping click regions inside their panels.
- Dense eligibility and available-action details moved to row-specific hover tooltips while the visible rows retain the core state, responsibility, burden, loss, labor, resistance, evidence, and proximity fields.
- Country directives use compact Ledger-only labels while their full descriptions, costs, status, and cooldown information remain in tooltips.
- All tab, row, and action controls have consistent hover audio; the authored three-frame atlases provide normal, hover, and pressed visual states.
- The two action rows remain within the 900 by 560 background at every reviewed resolution.

## Bounds Evidence

At 1280 by 720, the centered 900 by 560 Ledger leaves 190 pixels of horizontal margin and 80 pixels of vertical margin.

The six State Pools rows occupy y positions 32 through 242 with a height of 38 and a 42-pixel step.

The six Active Sites rows occupy y positions 34 through 244 with a height of 34 and a 42-pixel step.

The first action row ends at x 882, the second action row ends at y 554, and neither extends beyond the Ledger background.

The decision-category launcher is positioned at x 346 and y 64 inside its parent and uses the visible 136-pixel action frame as its click box.

## Tooling Boundaries

The MCP renderer does not evaluate element-level scripted visibility, so its composite Ledger render contains all five tab panels at once.

The live scripted GUI defines mutually exclusive visibility triggers for the five panels; source review verifies that only the selected tab is visible in engine.

The renderer reports unresolved dynamic text where values depend on scripted variables and scripted localisation.

The renderer also reports unsupported or missing offline assets for vanilla font atlases, `closebutton`, and `GFX_tiled_window_transparent`; these are supplied by the base game and are not missing Ledger assets.

The attempted `hoi4.gui_rewrite` was rejected by the MCP structure limit, so the reviewed corrections were applied directly to the linked source and then rendered again through the MCP.

Engine-runtime observation remains outside this repository audit.

## Simplifications, Omissions, and Blockers

No interface surface in the stated scope was omitted.

No fallback or unapproved simplification was introduced.

The only validation boundary is that the offline MCP cannot execute scripted visibility or observe the interface inside the running game.
