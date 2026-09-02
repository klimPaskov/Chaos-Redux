# Event MCP Evidence Skill Note Handoff

Date: 2026-09-02

## Status

Complete for the bounded skill-maintenance scope. This subtask changed no gameplay, MCP configuration, generated-agent, event, asset, or spreadsheet files. No commit was created.

## Verification proof

- The production command `C:\Users\klimp\AppData\Roaming\npm\hoi4-agent-tools.cmd` resolves to the installed package at `C:\Users\klimp\AppData\Local\hoi4-agent-tools\3.0.7\node_modules\hoi4-agent-tools`, whose `package.json` reports version `3.0.7`.
- The installed `dist\hoi4_agent_tools\event\service.js` selects focused analysis for `trace` and `explain_path`, and for `scan`, `roots`, or `lint` when a selector is supplied (`service.js:750-762`).
- Focused source patterns are exactly `events/**/*.txt` and `common/on_actions/**/*.txt` (`service.js:154-180`). Focused graph construction forces `projectHelpers = false`, adds `EVENT_FOCUSED_ANALYSIS_DEFERRED`, skips workspace-wide lifecycle passes, and remains incomplete even when traversal receives `expandHelpers = true` (`service.js:729-742`, `graph.js:1836-1862`).
- `state_flow` and `impact` use full analysis even when narrowed, while selector-free `scan` uses full analysis. Selector-bearing `event_render` also requests focused analysis (`service.js:834-881`, `service.js:939-946`).
- `event_compare` resolves `artifactUri` through event-graph validation (`service.js:1234-1237`, `artifact-validation.js:357-390`). Trace report artifacts and render or manifest artifacts can carry `event-analysis.v1`, `event-render.v1`, or `event-render-manifest.v1` envelopes without a graph payload (`service.js:897-924`, `render.js:389-416`, `service.js:1085-1114`), which can produce `EVENT_GRAPH_ARTIFACT_INVALID` instead of a comparison.
- The loaded tool declarations expose the actual read-only routes `mcp__hoi4_agent_tools__hoi4_event_inspect`, `mcp__hoi4_agent_tools__hoi4_event_render`, and `mcp__hoi4_agent_tools__hoi4_event_compare`.

A targeted live inspect was started and canceled before completion to avoid contending with the parent agent's pending probability baseline. The route and schema verification above came from the loaded tool declarations and the installed production source. No live artifact is claimed from the canceled call.

## Exact skill edit

Updated `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-events\SKILL.md` under `### MCP event-chain pass`.

Added `#### MCP evidence gate` requiring agents to inspect `analysisMode`, `complete`, `counts.helpers`, source coverage, unresolved entries, and diagnostics before lifecycle claims. It records focused-route selection, focused helper and lifecycle omissions, the full-route escalation rule, and the warning that focused traces or zero helper counts do not prove helper absence. It also records the graph-artifact requirement for `event_compare`, preserves exact blockers, and forbids invented conversions or comparison evidence.

## Probability compare follow-up

- Local inspection of the installed probability schemas confirms `probabilityCompareInputSchema` takes `before` and `after` `probabilitySourceSchema` objects, or paired `beforeManifest` and `afterManifest` inputs, with an explicit `scenarioSet` (`dist\hoi4_agent_tools\schemas\probability.js:260-276`, `498-512`; `dist\hoi4_agent_tools\mcp\tools\probability.js:125-173`). The service analyzes those inputs directly, while `probability_render` resolves a cached `analysisId` separately (`dist\hoi4_agent_tools\probability\service.js:1346-1400`).
- Added one sentence to the existing probability-evidence paragraph requiring source/inline/virtualPatch or paired declared manifests under identical scenarios, and distinguishing render `analysisId` from compare source inputs. No corrected comparison was run or claimed; the probability auditor owns that validation.

## Caveats and parent review

- The skill change is documentation guidance only and does not alter MCP behavior.
- The parent should review the focused diff, retain the handoff, and create the meaningful closure-tranche commit.
- No simplification was used in the skill guidance. The only unperformed evidence is the canceled live inspect result, which is explicitly recorded above.
