# Event 018 focus-tree MCP layout correction

Date: 2026-08-09

Scope: `common/national_focus/018_resources_found_cave_focus_tree.txt`

## Result

The current 65-focus Oth-Kesh tree retains its accepted routes, prerequisites, rewards, costs, icons, localisation, and AI blocks. This pass changes coordinates only.

Fresh `hoi4.focus_inspect` initially reported six Event 018-specific `FOCUS_LAYOUT_LINEAR_DETOUR` warnings in the One Maw, Many Chambers, doctrine-introduction, Burrow War, and Scree Tide lanes. The first automatic compact `hoi4.focus_rewrite` was rejected after post-change inspection because it introduced a long connector and sibling asymmetry. Its generated sidecar was deleted and its source arrangement was not retained.

The accepted authored correction straightens the affected local chains while keeping all hierarchy and doctrine capstones within the existing convergence distance. The final MCP inspection reports:

- 65 focuses and 79 connectors;
- zero Event 018 diagnostics;
- zero connector crossings;
- zero connector-through-node intersections;
- zero long connectors;
- maximum horizontal connector span 8 and maximum Manhattan span 10;
- zero too-close same-row pairs and minimum same-row spacing 2;
- bounds x 3 through 26 and y 0 through 29;
- layout hash `9898f96a63e4c4f1207e27499800154ea2db4f2bed143a1df5ebedc9a84f10ca`.

Final source-linked artifacts:

- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4950a442494a1b61a0b28c713bb22139b0010d15ca32b1ce4cf6b0cfebc410d4/3a2275c6c2413533da8190ce7f61eae08c6b74c590ef3bf98208997d9444f0ab/018_resources_found_cave_focus_tree.focus.svg`
- decoded-icon PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4423e0b1ec5bd3ac574671a542d5d6fe3fa35a5c399e9ed3e2bcf55418deeaf9/bb0829941912f80e62801f10ac59d1a3605803de3c2ea5544b0b7d76366a5a5b/018_resources_found_cave_focus_tree.focus.png`
- structural JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/93bc591f40d9cb9c29f0a27f0056ebbd02c62be7eb707c020eb2ce6f513ae4aa/5ef886d47bcf23ae8fc9b1bf3fafad0a05c4f84d274280e04a4890719a2a53d2/018_resources_found_cave_focus_tree.focus.json`

Workspace-level MCP validation still reports fourteen unrelated vanilla continuous-focus reference diagnostics. None points to Event 018.

## Required independent audit status

Three attempts to start the required fresh `chaosx_focus_tree_auditor` were blocked before the agent could run: the project subagent environment timed out initializing the Meshy or Blender HOI4 MCP servers. This document records the parent-owned MCP layout correction only and is not a substitute for that independent completion audit. The auditor must still run successfully before Event 018 can receive a final completion claim.

No Hearts of Iron IV executable was launched.
