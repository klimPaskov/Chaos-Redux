# Chaos Redux interface audit — 2026-07-22

This is the source-side handoff for the HOI4 GUI review. The review used the offline Interface Modding and Scripted GUI Modding wiki pages, vanilla GUI/GFX precedents, and the `hoi4.gui_inspect` / `hoi4.gui_render` MCP surfaces before the MCP transport closed during the final rerender pass.

## Surfaces reviewed

The MCP inventory covered the custom Chaos Redux windows and scripted GUI surfaces, with renders requested at 1280, 1600, and 1920 pixel widths across normal, hover, selected, locked, disabled, warning, active, full/empty list, long-text, and missing-localisation states where the renderer supported them.
The focused evidence included:

- Repression Ledger, event-log evolution detail (narrow and wide), settings, disease containment, Utopia, Secret Alliance, and the small decision panels.
- KRG and NZL focus-tree structure and CBRN technology GUI layout through the focus MCP review path.
- Vanilla font and sprite precedents for the settings and event-log controls.

Global MCP diagnostics include vanilla base assets and valid scripted contexts that the offline parser cannot model; those are not treated as local overlap by themselves.

## Fixes applied

- Repression Ledger now uses a compact decision-category header and a centered, movable `player_context` popup. Tab markers, state-pool rows, site rows, country actions, and the close control share the same visibility envelope as their parent surfaces, preventing invisible click blockers and cross-tab click-region conflicts.
- The disease board's Black Plague state now has its own metrics text and hides the private/public values that do not apply to that state.
- Removed stale Settings GUI visibility/effect hooks for controls no longer in the current layout while retaining valid right-click modifier handlers.
- Replaced invalid `hoi_14mbs` and `hoi_24b` references with the valid vanilla `hoi_16mbs` and `hoi_24header` fonts.
- Removed the generic site-inspection sprite alias to the Belgium/Congo texture. The generic decision now has its own ImageGen-generated inspection emblem.

## ImageGen assets

Built-in ImageGen was used for the Repression Ledger category emblem and the generic site-inspection emblem. Source PNGs, processed 53x53 PNGs, runtime DDS files, prompts, metadata, and `.gfx` handoff are retained under `docs/assets/system_camp_repression_rework/`.

## Remaining limitations

- The HOI4 MCP transport closed after the inventory and initial renders. A post-patch retry of both `hoi4.gui_inspect` and `hoi4.gui_render` returned `Transport closed` as well, so the validation artifact for the new Ledger header and popup is still queued. A subsequent MCP run must rerender those windows before a full completion claim.
- Large windows such as the muster board and disease board can hit the MCP `SCAN_BYTE_LIMIT`; this is a tool limitation, not proof that the source is valid. They still require a fresh targeted render when the transport is available.
- The decision-column audit found four other category-bound dashboards wider than the vanilla decision column: Secret Alliance (720px), Utopia (700px), Kruger Directorate (700px), and the Repression Ledger (900px before this popup split). The Repression Ledger is now split; the other three require a dedicated compact-header/popup pass rather than an unverified resize. Death's Black Atlas is 520px and remains a moderate-width surface.
- The KRG focus audit found 60 missing focus goal DDS files out of 100 focus icons. This is an asset-package blocker outside the safe scope of a layout adjustment and must be resolved before claiming complete visual coverage.
- One evolution-details overlap reported by MCP is the intentional portrait plus frame/flame overlay stack; the parser also reports unresolved vanilla portrait and tooltip sprites. These need an in-game or refreshed MCP visual confirmation.
