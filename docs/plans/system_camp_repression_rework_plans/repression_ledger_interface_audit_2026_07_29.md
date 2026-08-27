# Repression Ledger Interface Audit

## Scope

This audit covers only `repression_ledger_category_window` and `repression_ledger_window`, including the Overview, State Pools, Active Sites, Country System, and Evidence & Reform tabs.

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
- The Evidence & Reform label uses a bounded two-line presentation instead of clipping or shrinking into the marker.
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

## 2026-08-27 Five-Tab Correction Addendum

The live source now matches the five-tab contract described by this audit.

`State Pools` and `Active Sites` are separate named containers with separate click handlers, tab flags, panel-visibility triggers, six-row lists, and selection actions.

The fifth `Evidence & Reform` tab is also a real panel with discovery, condemnation, attributed-deaths, and reform cards plus the existing evidence and reform seals.

The compact decision-category presentation uses natural country-specific prose and sentence-based status text.

It no longer uses separator bars, fake telemetry columns, or a static Japanese sentence outside the Japan branch.

The `Country System` label uses a bounded two-line text box after the localisation audit identified its former 90-pixel single-line box as the only likely remaining text-overflow source.

Fresh full-Ledger inspection:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a4aea950c875ffe646f6ecf80fd43f47b816c97f0f9d88b663ed7292d9a17ca5/419a5f98e0bf835ad9d14504eaba284e07f8cbc8c4ece571618742dd14db0c53/gui-inspect.f323d376d55c4e21.json`

Fresh full-Ledger render:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b0179a2e4c0df19f733c338fc2bdf7d696c1236dd7cad8fa8ea08fc1d146f48b/c72eb7b994372a5107551192d7564eb62f4e40e25f416d989f4771eb7668c6bd/repression_ledger_window-full.svg`

Fresh category render:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/329de700000bcf60f3ae6a5c6944feb02199e57371a007e6a3fa302231160374/4c69af5a36a7c76bd0c7148c33e6408914f4338bc3825dab42ef6ded13c048a6/repression_ledger_category_window-full.svg`

The current MCP global graph still truncates repository-wide diagnostics and includes unrelated interface collisions and approximated visibility overlaps.

The category inspection route later recovered and produced:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f1afef8e42da556ecad6b031986f53f1fafa4de7e401df0034cea9c2586587f9/5378150cbce4191e690a1384f4b60a690ece89d60af19fe9252d0ba7d755c5cc/gui-inspect.92f2da424dc00017.json`

The matching final category render is:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/329de700000bcf60f3ae6a5c6944feb02199e57371a007e6a3fa302231160374/d8fc1bb8fd30d75db270da174c73bd6d478cad2a721127b4b0fa88607cb68752/repression_ledger_category_window-full.svg`

The latest successful post-cost Ledger inspection is:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/93389e8403c4d0d12cd6bf7298f99f31f6cc38b10274e3b4a14aae9f5ad06e96/dc01afdd231d38eb710ba49d40cdcec73a938ac5b2c858a2af35cda1950f40d3/gui-inspect.8d6b6d473e40a3ba.json`

The matching compact post-cost normal, long-text, and missing-localisation render at 1920 by 1080 is:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/125c3b778d52bee555772509f03a11c3fe23da527cd883fde7a3ee338475afbc/c7836af7bf903630ec97f86c24ef403f9e7b48032ac6d416fb6f1ea0366d1726/repression_ledger_window-full.svg`

Final inspection and compact-render retries after the restricted-payload localisation additions reached the MCP's 180-second graph limit without producing newer artifacts; those additions did not alter `interface/camp_repression_ledger.gui`.
