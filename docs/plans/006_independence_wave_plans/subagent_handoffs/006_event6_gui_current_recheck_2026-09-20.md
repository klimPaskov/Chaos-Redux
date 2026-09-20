# Event 006 GUI current recheck — 2026-09-20

## Scope and disposition

This is a read-only current-source recheck of the event-owned Statehood Ledger window `independence_wave_status_window`. It does not authorize a layout redesign, a shared-interface edit, gameplay changes, or a completion claim.

The current disposition is **PARTIAL / VISUAL ACCEPTANCE OPEN**. The source graph parses and the focused inspect has no blocking diagnostics, but the matched render response is wire-truncated and the offline route cannot prove live tab isolation, effective click regions, blendframe playback, or save/load state persistence.

## Current MCP evidence

`hoi4.gui_inspect` targeted `independence_wave_status_window` with scenario `{id: "independence_wave_status_default"}` in workspace `mod_chaos_redux_ea3b2d67c2c0`. It returned `GUI_INSPECTED`, status `ok`, 48 inspected Event 006 elements, zero skipped sources, and no blockers at shared source revision `d693e4849f1fb8db6423669415e24dcd4397016f46ed8d61bebec930800a7ec9`. The fidelity counts were 557 modelled, 5 approximated, 15 ignored, 0 missing, 4 unsupported, and 0 unresolved.

The inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/69b89294c9b29f55351f744aeac1fb406d77ed5a30ef456000ab255581f7192e/7ed64ac814bee72ea5c9dba7ab8c83634b52d12b321cb440af668bd7e35b74fb/gui-inspect.d693e4849f1fb8db.json`.

The matching `hoi4.gui_render` used the same scenario, the fourteen accepted state labels, and 1920x1080, 1280x720, and 1024x768 at UI scale 1. It returned `GUI_RENDERED` with no blockers and one linked full-window SVG, but the response reported `MCP_RESPONSE_TRUNCATED` because 35,453 bytes exceeded the 32,768-byte wire budget. The linked artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/59f6553cef8e7fd4dc1c9bf83f49ecdc73cc9b89870e862fd9604d20349ab236/0418a7cfdd28b758498beabd1c2a1910d61563893261a48099e3d0ee4dc803d7/independence_wave_status_window-full.svg`.

## Findings and limits

The inspect route reports expected background-to-child overlap findings because the full-panel sprite owns the window canvas, alongside the deliberate static/animated sibling overlap used by the scripted visibility contract. Those findings are not treated as visual acceptance; the linked render must still be reviewed for clipping, overflow, text placement, state isolation, and effective hit regions.

The animated state siblings retain `gfx/FX/buttonstate_blendframes.lua`, which the offline renderer records as a partial appearance rather than executing. The render therefore cannot certify blendframe playback or the live visibility handoff between static and animated siblings.

No source file changed during this recheck. No `gui_rewrite` operation was attempted, and no self-comparison or wire-truncated image is promoted as a before/after acceptance artifact. The prior event-owned worker handoff remains the authority for the earlier rewrite failure and the existing source-preservation result.

## Remaining owner actions

The event-owned GUI owner must obtain a complete readable render or equivalent artifact review for the accepted state and resolution matrix, inspect the actual images and click regions, and close any visible clipping, overflow, text, hierarchy, or state-isolation defects before claiming GUI completion. Dynamic values, live tab behavior, blendframe playback, and user-side runtime validation remain outside this read-only recheck.

No simplification or fallback was introduced.
