# Event 006 focus geometry refresh — 2026-09-25

## Scope

Read-only current-source inspection and rendering for `independence_wave_focus_tree` in `common/national_focus/006_independence_wave_focus.txt`; no focus source, layout, prerequisite, reward, AI, or localisation edits were made.

## MCP evidence

- `hoi4.focus_inspect` returned `FOCUS_INSPECTED` with validation passed at source revision `a634332e13a8b44e25db76bf1bf537dc72ee4e8d7d43adf64057443d1ccda7c5`.
- The current graph contains 184 focuses and 196 connectors, layout hash `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`, zero crossings, and zero node intersections.
- One existing `FOCUS_LAYOUT_LONG_CONNECTOR` runs from `independence_wave_adopt_military_archetype_program` to `independence_wave_adopt_reclamation_doctrine`, spanning 10 columns and 1 row; its source is `common/national_focus/006_independence_wave_focus.txt:751`.
- The only other reported warning is missing vanilla localisation for `continuous_restrict_freedom_desc`; it is outside the Event 006 tree.
- `hoi4.focus_render` returned `FOCUS_RENDERED` at the same layout hash, 11,824 × 2,706 pixels, with the same diagnostics and validation passed.
- `hoi4.focus_raster` returned `FOCUS_RASTERIZED` at the same layout hash with validation passed and the same diagnostics. The raster was queued in the Codex panel for review. This receipt does not claim a pixel-level visual review or an in-game screenshot comparison.

## Artifacts

- Inspect JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/709ef7d99294381b21b86cb1c50fda14eeb4d005c1cb43aee8fbc3618b8262c1/b3df0755b09e9367c71494bb07b86b87cf5cae98d74e77fb5410383d53ebf41a/focus-inspect.a634332e13a8b44e.json`
- Render SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d657e740a218f78db884d095bf8d84c0f5223a875e50fb9eea6cc972eac076d7/7ae949edfda7ff1d3de559ce28db5f55fb4fd5a247a0a6db6ec6a0a7eba07df9/independence_wave_focus_tree.focus.svg`
- Render JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a69a5d66e7de39546898dcbc68294f03be58a2e72fe7ecdf0e77c298a22d7cd0/9588d5c4f9bc73e162545465eeff572a377f814870f38dbe49d3d695b3eacef4/independence_wave_focus_tree.focus.json`
- Render HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e613bcc995318d3b06fcab8aab98f15e2a5091348926ac31986e1dc70cf0e8cb/6ea0fe90d0260278beed9382c7fe2dfcf3da29c2eca1260a085dd7c5b8d57742/independence_wave_focus_tree.focus.html`
- Raster PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c08c5ca2aea0ce93cafe29d445854500d28856380da4ea5356ebdd533e35c78d/cf3202e5db2a2c56cde15461393054581962357e46778e2fdb0632e0c5659c81/independence_wave_focus_tree.focus.png`

## Remaining evidence

This structural refresh does not audit focus rewards, AI weights, path balance, or the focus-to-decision/event integration. The required focus-tree and AI/probability audits, comparison against any prior accepted design image, and user-owned live validation remain open. The accepted ten-column connector remains an authored diagnostic requiring design review; no rewrite was made because this task only refreshed evidence and did not establish that the route should change.
