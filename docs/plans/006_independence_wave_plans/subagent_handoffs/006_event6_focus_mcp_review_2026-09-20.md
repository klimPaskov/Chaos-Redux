# Event 006 focus MCP review — 2026-09-20

Disposition: evidence-only / no source change.

This handoff records the current read-only focus inspection and render for `independence_wave_focus_tree` after the 2026-09-19 source and asset refreshes.

## MCP evidence

`hoi4.focus_inspect` inspected `common/national_focus/006_independence_wave_focus.txt` with tree `independence_wave_focus_tree` in national mode and returned `FOCUS_INSPECTED` with validation passed.

The inspection resolved 184 focuses and 196 connectors with zero connector crossings, zero node intersections, zero too-close same-row pairs, and one non-blocking authored long-connector warning.

The warning is `independence_wave_adopt_military_archetype_program -> independence_wave_adopt_reclamation_doctrine`, which spans 10 columns and one row against the MCP threshold of 8 columns.

The inspection source revision is `c436f2f19c1c7cdfb0c3286a168fa3ddaddfa27f5c32672c1e4a0a72fe4df8eb`, the layout hash is `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`, and the inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/31ae75368c352d4f30abd9ed39b3a80d0b52ce98a7e120bf32d346fdde1e0c69/34ab25c79b102488f09cde67e165cc0193a36a103d1c52a892d3709c53043e16/focus-inspect.c436f2f19c1c7cdf.json`.

`hoi4.focus_render` completed for the same tree at review scale `0.75` and returned HTML, SVG, JSON, source-map, and plan artifacts.

The render artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f2b282094ed9cf36d4fb4add8a8b80205a8cd8d12e2e396c2e4f1f9f48302602/a2b6b39ee0acf26e88d8de162a1b894c11e206e6494ac3429c1b53453268ac67/independence_wave_focus_tree.focus.html`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/352b090f1cd955f9cbb30a41e0ae581761c08f51f20d788d63598a7bd7d4c3e2/c2907d891c67154463b2aecdf40e3c5d2f8772bbd4f4972f4b409fc041bb4dfa/independence_wave_focus_tree.focus.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a69a5d66e7de39546898dcbc68294f03be58a2e72fe7ecdf0e77c298a22d7cd0/d0dd8893eaf58f70ca9bd578c893f8d84e9499b06ee116c9f668293b169a3c94/independence_wave_focus_tree.focus.json`.

The inspection also reports the unrelated vanilla `continuous_restrict_freedom_desc` localisation reference; it is outside Event 006 ownership and was not changed.

## Source decision

No focus coordinate was changed because the warning is an authored military-choice cohort edge rather than an isolated parser or route defect.

Moving the parent or the reclamation child would either trade the warning to another military-choice edge, disturb the accepted cohort alignment, or require a broader lane reflow with no accepted design basis.

The current Event 006 focus source therefore remains unchanged, with route prerequisites, mutual exclusions, rewards, localisation, icons, and AI behavior preserved.

## Boundary

This receipt does not claim live focus-tree rendering, save/load behavior, whole-tree gameplay completion, or whole-event completion.

No gameplay, localisation, asset, admission, probability, or fallback change was made by this review.
