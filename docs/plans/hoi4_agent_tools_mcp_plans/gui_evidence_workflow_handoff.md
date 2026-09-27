# GUI evidence workflow handoff

## Disposition and scope

Implemented in the Chaos Redux GUI skill.
The parent applied equivalent concise guidance to the Agentic GUI skill after reviewing this handoff.
No gameplay files changed.
The connected MCP server may expose a different schema from the local candidate; each GUI task must inspect its live routes before using these fields.

## Exact Chaos Redux skill hunk

Insert this paragraph immediately after `### Scenario identity and assertions` in `.agents/skills/chaos-redux-scripted-gui/SKILL.md`:

> Before using GUI scenario fields, verify connected server health and the live `gui_inspect`/`gui_render` schemas; record any unavailable field as a route gap. Read `visibilityStatus` (`shown`/`hidden`/`unresolved`) and `enablement` (`enabled`/`disabled`/`unresolved`) with their missing-fact reasons: dashed amber click regions are potential controls, not confirmed branch coverage, and explicit scenario overrides remain declared assumptions rather than observed campaign evidence. Where the live schema supports `scenario.tooltip`, supply `{ target, x, y, width, padding }` for a unique visible element ID/name with `pdx_tooltip` localisation; inspect the source `ToolTip` sprite, `cg_16b` font, measured text height plus caller padding, and diagnostics for unresolved, missing, hidden, ambiguous, or out-of-bounds requests. Resolve engine-generated `[!element_action]` text only from exact caller-supplied bracketed-token strings in `scenario.values` or `scenario.scriptedGui`; never fabricate the text. Keep native automatic positioning, frame composition, delayed timing, and `click_to_front` outside preview proof.

The adjacent skill edits visible in the shared working tree predate this task and were preserved.

## Source evidence

Local candidate: `C:\Users\klimp\Documents\Projects\hoi4-agent-tools`, revision `83079ff` with uncommitted GUI source and documentation changes; the request identifies it as development candidate 3.6.0, not a published or connected-server capability claim. The parent reports 78 focused tests and a real vanilla render. This guidance-only task inspected the source and existing test assertions but did not rerun tests or rendering.

- `src\hoi4_agent_tools\gui\types.ts:290,464-469` defines the tooltip request and three-state scene fields with reasons.
- `src\hoi4_agent_tools\gui\layout.ts:917-937,2504-2542,3448-3676` retains unresolved state, gates confirmed clickability, validates tooltip targets and assets, measures text, and records unsupported native behavior.
- `src\hoi4_agent_tools\gui\renderer.ts:511-512` draws unresolved click regions with dashed amber outlines.
- `src\hoi4_agent_tools\gui\studio.ts:948-969,1058-1087` separates confirmed and unresolved scenario and branch evidence.
- `tests\unit\gui-condition-pipeline.test.ts:75-163,166-285,285-382` checks missing facts, declared overrides, potential regions, and withheld branch coverage; `tests\unit\gui-tooltip.test.ts:327-393` checks hidden, unresolved, missing, ambiguous, bounds, and unresolved text cases.
- `docs\gui.md:8-40` and `docs\adr\0030-native-gui-composition.md:53-65` state the source-model evidence and tooltip fidelity boundaries.

## Exact proposed Agentic update for the parent

In `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\agentic_hoi4_modding\.agents\skills\hoi4-scripted-gui\SKILL.md`, insert the same five-sentence paragraph immediately before the existing paragraph beginning `` `gui_render` may expose a comparison scenario. ``:

> Before using GUI scenario fields, verify connected server health and the live `gui_inspect`/`gui_render` schemas; record any unavailable field as a route gap. Read `visibilityStatus` (`shown`/`hidden`/`unresolved`) and `enablement` (`enabled`/`disabled`/`unresolved`) with their missing-fact reasons: dashed amber click regions are potential controls, not confirmed branch coverage, and explicit scenario overrides remain declared assumptions rather than observed campaign evidence. Where the live schema supports `scenario.tooltip`, supply `{ target, x, y, width, padding }` for a unique visible element ID/name with `pdx_tooltip` localisation; inspect the source `ToolTip` sprite, `cg_16b` font, measured text height plus caller padding, and diagnostics for unresolved, missing, hidden, ambiguous, or out-of-bounds requests. Resolve engine-generated `[!element_action]` text only from exact caller-supplied bracketed-token strings in `scenario.values` or `scenario.scriptedGui`; never fabricate the text. Keep native automatic positioning, frame composition, delayed timing, and `click_to_front` outside preview proof.

This wording leaves the existing Agentic comparison, scenario, and visual acceptance guidance intact. No AGENTS.md or subagent routing change is needed for this bounded workflow note.
