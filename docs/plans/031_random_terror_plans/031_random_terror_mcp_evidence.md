# Event 31 Random Terror MCP evidence ledger

## Purpose

This ledger records the mandatory HOI4 MCP routes used against the current Event 31 implementation and preserves exact blockers where a route did not return evidence.

Source review, local validation, wiki references, and vanilla precedents remain required in parallel and are not treated as substitutes for a failed MCP route.

## Workspace

- MCP workspace: `mod_chaos_redux_ea3b2d67c2c0`
- Event root: `chaosx.nr31.1`
- Focus tree: `random_terror_actor_focus_tree`
- Shared scenario GUI: `chaosx_scenarios_window`
- Shared super-event framework: Event 31 slots `114` and `115`

## Event route

The narrow post-repair event lint for `chaosx.nr31.1` completed with no blocking diagnostics.

- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5d493356efdd2fec675d0ad2b4da7da857c9b5ff5017ecb79ab440cf82336878/a4c54b601df599852226342a16112bdb27b658b0370620af0cfed05893e37384/event-lint-00d629f508b7.json`
- The event renderer did not complete within the tool limit and therefore supplies no current rendered-chain artifact.

## Focus route

The post-repair structural focus render covered all 114 Event 31 focuses and 104 connectors.

- Structural hash: `69ec88315409c5c578ffca2852052037f7ee6a48510a92189c11ac79a1a6d2a9`
- Structural diagnostics: zero connector crossings, zero node intersections, and zero same-row spacing violations.
- High-fidelity raster blocker: `tool call failed for hoi4_agent_tools/hoi4.focus_raster: timed out awaiting tools/call after 180s`

The earlier raster remains useful visual evidence for the icon family, but it is not post-repair topology proof.

## GUI routes

Event 31 introduces no dedicated scripted GUI, so the event UI worker and an Event 31 GUI rewrite are out of scope by accepted design.

The shared Global Jihad selection surface completed inspect and render at 1920x1080 with UI scale 1 using Event 31 selected, Random Pattern, and Maximum intensity.

- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a92973eefa049d05f8bcd45622a120d0f4c83054c4354c9bb7df29160140c10f/5632b6e15e45b3065c52dfa6eaf61390432d48066f97c4f3d53d970211db9a93/gui-inspect.426cc63d2ec2c831.json`
- Render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5f6830b2501a441bcebdecc03874ce13a16f1d7e4d5ded5792c4ce73deab4906/f748c30500493d5bba5e686607517d49e5d10f6a2c6efcdd3b3e98c3a9ee9fab/chaosx_scenarios_window-full.svg`
- The inspector reported no missing Event 31 scenario fields.

The shared super-event framework route did not return fresh inspect or render evidence.

- Inspect blocker: `tool call failed for hoi4_agent_tools/hoi4.gui_inspect: timed out awaiting tools/call after 180s`
- Render blocker: `tool call failed for hoi4_agent_tools/hoi4.gui_render: timed out awaiting tools/call after 180s`

## Technology route

The technology compatibility route was invoked for the carrier baseline technology `infantry_weapons` with prerequisite and descendant tracing, sub-technologies enabled, depth 4, and a 100-node cap.

- Exact blocker: `tool call failed for hoi4_agent_tools/hoi4.tech_inspect: timed out awaiting tools/call after 180s`

The carrier history files still require source-level verification against installed vanilla technology identifiers, but that review is not reported as MCP evidence.

## Map route

The map inspector was invoked for state `104`, the dormant carrier fallback capital used before Event 31 transfers a live state and replaces the capital.

- Exact blocker: `tool call failed for hoi4_agent_tools/hoi4.map_inspect: timed out awaiting tools/call after 180s`

Exact state ownership, capital transfer, adjacency, and allocation checks still require source-level and country-package audit evidence, but those checks are not reported as MCP map evidence.

## Probability route

The previous baseline handoff records partial and failed probability routes and cannot support a final balance claim.

The current comparison pass is assigned to `chaosx_ai_probability_auditor` against the complete accepted scenario matrix.

Its final artifact references, scenario evidence classes, and exact blockers belong in `031_random_terror_probability_comparison.md`; until that file is complete, the probability route remains open.

## Completion status

This ledger is evidence bookkeeping, not a completion claim.

Event, focus, GUI, technology, map, and probability entries must be reconciled with the final subsystem audits and completion review before Event 31 can be declared complete.
