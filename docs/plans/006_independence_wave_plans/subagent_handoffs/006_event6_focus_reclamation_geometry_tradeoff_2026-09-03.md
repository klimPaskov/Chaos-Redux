# Event 006 reclamation-focus geometry trade-off

Audit date: 2026-09-03. Scope: the visible prerequisite and layout of `independence_wave_adopt_reclamation_doctrine` in the parent `independence_wave_focus_tree`.

## Decision

The redundant visible prerequisite was removed from `common/national_focus/006_independence_wave_focus.txt`. The focus keeps its runtime gate through `available = { has_completed_focus = independence_wave_adopt_military_archetype_program ... }`, so the military-archetype requirement remains enforced without adding a long connector to the far-left high-chaos lane.

This preserves the accepted branch placement at `x = 32`, the ten-choice military row spacing, and the existing mutual exclusion with `independence_wave_adopt_border_defense`. A visible edge from the parent at `x = 42` to this focus would span ten columns; moving the focus into the row would either create a second outlier or disturb the accepted sibling spacing. The available gate is therefore the shortest clean presentation for this layout.

## MCP evidence

`hoi4.focus_inspect` completed with revision `146f3bf4716179267c2db9f6aa88d5ae81ec7471a100b8664d3b9e3ef8aeb6f5` and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aef79285f5b87ee3466cedbebe51763932270cfcf39174660e34cde9e46129/84ea5255d48871e997492d7f79e6c586d252bc8de7d14d1c846625776e5a4aed/focus-inspect.146f3bf471617926.json`.

The inspection resolves 184 focuses and 195 connectors with zero crossings, zero node intersections, zero long connectors, zero too-close same-row pairs, maximum horizontal span 8, maximum vertical span 4, and zero Event 006 layout diagnostics. The only warning is the unrelated vanilla `continuous_restrict_freedom_desc` localisation reference.

`hoi4.focus_render` completed with layout hash `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7` and artifacts `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b2b8b9da88967dc3b1624bef70895c825107186788fec5634d667491dba2333b/dbe0828b1b7fce9c9b920b169f1822c895afbd84d0baf2567d388abbb71b2c34/independence_wave_focus_tree.focus.html`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/790ac83c6f2cdb9816133b30e7a650f0e74f3823cf45efd0753fa9182ec87279/0cfa49fe34579a6a74f028e742ada002ba8caa29f178d1622985e4e046076734/independence_wave_focus_tree.focus.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8c866764d0746575942c0cc08e8f30f45450a4b59cff64e7c9a5b357fc32d150/8b01bc8933ee59f6f6b7cc4411430c9bac40f1ab825f5a70c359bfb845014714/independence_wave_focus_tree.focus.json`.

## Scope and risk

No icon, localisation, reward, AI, package-admission, or event-execution behavior changed. The change only removes a duplicate presentation edge while retaining the existing gameplay availability condition. No live Hearts of Iron IV launch or save/load evidence is claimed.

