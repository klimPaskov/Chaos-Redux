# Event 006 Statehood Ledger GUI re-audit — 2026-08-22

## Scope and disposition

This is a read-only refresh of the shared Event 006 Statehood Ledger presentation surface. No GUI source, scripted GUI helper, localisation, or gameplay file was changed. The surface remains source-complete but runtime/visual acceptance is partial because the installed GUI inspector reports workspace-wide diagnostics and the renderer exposes only an aggregate window artifact.

## MCP evidence

The mandatory `hoi4.gui_inspect` call targeted `independence_wave_status_window` with scenario `{ id: "independence_wave_status_default" }` in workspace `mod_chaos_redux_ea3b2d67c2c0`. It returned `GUI_INSPECTED` with 48 inspected Event 006 elements at shared revision `891b102d24ef4a83a9b55c7e51cb56ada4d2524bd0a47eb4b5c02194cc38862d`. The complete linked artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8bb5c582c2f3d3ddffa9b6bd430ccc17b1de33a55dea9b9e23cc11525455dbf5/ea08fc9b9078cce307128635d123b1a5d726de6a9e2a833d3eb5fc0b7e77cdb9/gui-inspect.891b102d24ef4a83.json`.

The inspect response reports 20 retained validation/graph diagnostics and one omitted hard diagnostic. The bounded global graph includes unrelated index collisions and unresolved references; the focused validation reports 75 visible-overlap findings and one missing, four unsupported, and twelve unresolved fidelity elements. Because the result is aggregate and the source graph contains 64,978 nodes, these diagnostics are not treated as Event 006-local defects without a family-isolated or source-linked finding.

The mandatory `hoi4.gui_render` call covered the normal, hover, selected, locked, disabled, warning, active, completed, empty-list, full-list, minimum-value, maximum-value, long-text, and missing-localisation states at 1920×1080, 1280×720, and 1024×768. It returned `GUI_RENDERED`; the aggregate full-window SVG is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d7d245b460614d138be4d724b8fbbe4c0c3ae510648ae12c90abf3733e231c13/269e8c47c0f222760458954b9b547d19d3fff7156306e1a809b6d3e79e099bff/independence_wave_status_window-full.svg`. The response was wire-truncated, and no per-state click-region, hierarchy, resolution, or comparison bundle was exposed.

## Review result

- The window remains bound to the active-country Statehood Ledger presentation and has no pre-event crisis category or queue dependency.
- No narrow layout patch is justified by the current evidence. The reported overlap and unresolved values are aggregate workspace diagnostics rather than a source-linked Event 006 element defect.
- Runtime rendering, save/load persistence, and clean pre/post comparison remain unclaimed. The existing static Statehood Ledger matrix and source checks remain the authoritative implementation evidence.
- A future GUI pass may proceed only when the MCP route can isolate Event 006 elements and expose the requested state/click-region comparison artifacts.

## Parent handoff

Keep this surface in the Event 006 **HOLD / PARTIAL** disposition. Do not use the aggregate `validation.passed = false` result as evidence of a gameplay defect, and do not claim visual completion from the linked SVG alone.
