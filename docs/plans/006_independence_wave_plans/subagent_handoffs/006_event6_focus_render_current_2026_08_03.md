# Event 006 current focus render receipt

Date: 2026-08-03.

Scope: read-only MCP inspection/render of the accepted one-tree Event 006 focus framework. No focus source or gameplay file was edited by this receipt.

## Current source result

The current source resolves one national tree, `independence_wave_focus_tree`, with 184 focus nodes, one continuous palette, 223 prerequisite connectors, 184 resolved titles, and 184 source layout decisions. The one-tree scope and generic package assignment remain intact.

The MCP compact-layout rewrite was attempted against a temporary backup and returned `FOCUS_COMPACT_QUALITY_BLOCKED` without changing the source. The authored layout remains the source of truth.

## Fresh render artifacts

The successful current render used `common/national_focus/006_independence_wave_focus.txt` and produced:

- HTML: `independence_wave_focus_tree.focus.html`, SHA-256 `d70102ea07ca4080d42e7c143f6bbe69929006ee5669b286ad0524d222b72db0`.
- SVG: `independence_wave_focus_tree.focus.svg`, SHA-256 `080fc9ef9ed09289d8dace963fee35ccc0eafe49d9ed6b6eecc3964c43298f9c`.
- JSON: `independence_wave_focus_tree.focus.json`, SHA-256 `316aa46d5899f4446f9593e367c691074f0fa6d3a9c446d4486a50d3279e17cf`.
- Source map: `independence_wave_focus_tree.focus.source-map.json`, SHA-256 `34caa01abdeb8caa03e051b25e8edd069edd662bd1331b5dfc95efa788b45b0b`.
- Plan: `independence_wave_focus_tree.focus.plan.json`, SHA-256 `e1e30fa59debc7b4a759b786ac27c745f62aae639e6929ce7b3e3c1e3618a547`.

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

## Diagnostics and disposition

Validation remains **PARTIAL / HOLD**. The render reports 14 blocking focus diagnostics: 43 connector crossings, 7 node intersections, 28 long connectors, and 5 same-row pairs below the required spacing. The largest connector spans 80 columns. Several crossings are explicitly marked unsatisfied because their endpoints are fixed or relative, so a broad reflow is not authorized merely to make the count smaller.

The render is now current static evidence and supersedes the earlier `SCAN_BYTE_LIMIT` wording for the focus-inspection surface. It does not prove live focus behavior, save/load, package admission, AI timing, or player-owned gameplay evidence. A future geometry tranche must preserve all 184 node IDs, prerequisites, route gates, shared-module ownership, one-tree assignment, and package-specific adapters while moving a reviewed coupled cluster or authoring explicit layout exceptions.
