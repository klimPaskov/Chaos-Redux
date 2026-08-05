# Event 014 focus and scripted-GUI layout audit

## Scope

This handoff covers the Event 014 unified CBL focus tree and the five direct Event 014 scripted-GUI windows. The main events-log window was intentionally excluded from this pass.

## Evidence

`hoi4.focus_inspect` was run against `common/national_focus/014_cannibalism_focus.txt` with `treeId = cannibalism_unified_focus_tree` and `mode = national`. The tree contains 108 unified CBL focuses, and the final inspect reports zero Event 014 layout diagnostics for connector crossings, node intersections, and long connectors. The MCP still reports unrelated vanilla continuous-focus icon references elsewhere in the repository; those are outside this surface.

The final focus artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8ebc714be99b3a3b2f232fd3e956a0d5d2fffd93e094f696fe24b3b2fa944133/76c9715ea7bf0bd36ce4221d3e783b5f6a21f4aa51b9ad63623189dbcb09eabf/focus-inspect.b1e84a03d06419f8.json`, with layout hash `290eac3bef0f6310896213ac4c172e5a0673f2290afcba1465a8ef4e08023d2d`. It reports 103 visible connectors, zero crossings, zero node intersections, zero long connectors, and zero Event 014 layout diagnostics.

The final unified render is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/93c07085238e0691a876a4a91aee97afa38567e340825eade683cb700c8c7742/38cb15bcb4390f54903a799ab3e8d89aeeeaad08faf38623b2003872301f211d/cannibalism_unified_focus_tree.focus.html` with its companion SVG, JSON, source-map, and plan artifacts.

The final Warlord inspect reports 68 focuses, 79 connectors, zero crossings, zero node intersections, and zero long connectors. The final Wendigo inspect reports 28 focuses, 28 connectors, zero crossings, zero node intersections, and zero long connectors. The Warlord and Wendigo renders were also regenerated after the coordinate pass; their deterministic HTML/SVG/JSON/source-map/plan artifacts are available from the MCP render calls.

`hoi4.focus_render` produced the deterministic HTML, SVG, JSON, source-map, and plan artifacts for the revised CBL tree. The compact automatic rewrite was rejected by the MCP because its proposed reflow introduced node intersections and longer connectors, so the final layout uses authored local moves and explicit availability gates instead.

`hoi4.gui_inspect` and `hoi4.gui_render` were run for `cannibalism_early_header_window`, `cannibalism_network_window`, `cannibalism_warlord_command_window`, `cannibalism_revealed_command_window`, and `cannibalism_wendigo_command_window`. Renders covered 1280x720 and 1920x1080 with normal, hover, selected, disabled, warning, minimum-value, maximum-value, empty-list, full-list, and long-text state probes where supported. The final network inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5169fb6d2b5ce622c3ff4cacba679216595912ec13e64cfa94fd75ab28bed4ec/195d334d09038045f346aceff9d95c1582fbddd7190f7cde5bae67c602f67446/gui-inspect.5d19b94621a071ab.json`. The final network render is artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1400f648d294b965b9c40181909726c5a642a648fe3dcb1764cdca5664a28ffe/43fd118011a3c1b6fc4bda7d8e1a908abee45a8dd96b74c21d7318bce8b3a79a/cannibalism_network_window-full.svg` and reports a full 860x620 scene at x=530,y=245 on the 1920x1080 reference, with the previous inherited bottom clipping removed by `origo = center`. The five network tabs now use a single click box with a scripted-localisation sprite selector, so the selected tab receives the repository's active treatment without duplicate overlapping controls.

The GUI MCP adapter reports `player_context` as unknown for the network scripted GUI, but the offline Paradox Scripted GUI reference explicitly lists `player_context` as valid and the same context is used by the repository's other player-context windows. This is retained as an adapter false positive rather than changing a valid runtime context to an invalid decision-category parent arrangement.

## Source changes

- Dense focus convergence remains fully gated with OR/AND semantics preserved in `available` custom trigger tooltips. The supreme hierarchy, warband integration, continental larder, continental supply, and courier network use connector-free convergence gates because their mutually exclusive alternatives produced misleading crossings; continental weakness and final mobilization retain their visible common prerequisites with the remaining gates in `available`.
- Local focus positions were moved to remove the remaining authored connector crossings and long spans without changing route rewards, mutual exclusions, AI weights, or completion effects.
- The Warlord origin fan and Wendigo branch fan were compacted to remove their long spans. Wendigo's five-way countdown requirement remains an explicit AND gate in `available` and its tooltip, with the stabilized anchor chain retained as the single short visible parent edge.
- The network container now declares `origo = center` and `click_to_front = yes`, keeping the movable 860x620 window inside the viewport at the reviewed resolutions. The scaled counter, sort, and refresh controls were vertically offset to align their visual centers with the tab row.
- Dynamic country and state entry buttons now use the documented `size = { width = ... height = ... }` form, their country flag is click-through, and all Event 014 buttons provide hover audio feedback through `oversound = ui_menu_over`.
- Network tab buttons use dynamic active/idle sprites through `GetCannibalismNetwork*TabSprite` scripted localisation, preserving one stable click region per tab while making the selected view visible.

## Remaining MCP caveats

The GUI source graph is repository-wide and remains blocked by unrelated context-type diagnostics, missing base-game texture resolution for `GFX_tiled_window_transparent`, and global visible-overlap counts from other windows and intentionally paired animation/static layers. Event 014 source parsing, local geometry, click-box dimensions, and direct-window render artifacts are otherwise available for review.

## Runtime boundary

No Hearts of Iron IV process was launched. Live consumer validation remains the user's in-game responsibility under the repository guidelines.
