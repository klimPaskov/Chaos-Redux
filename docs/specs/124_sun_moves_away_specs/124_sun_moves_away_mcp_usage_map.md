# Event 124 MCP usage map

This is a future implementation evidence map.
No HOI4 MCP route was exposed or executed during this planning task.
Configuration files and repository documentation establish intended capabilities, while the implementation session must discover its actual connected schemas.
Scenario identifiers refer to the [acceptance matrix](124_sun_moves_away_acceptance_matrix.md).
Owners refer to the [subagent usage map](124_sun_moves_away_subagent_usage_map.md).

## Evidence rules

Preserve revisions, roots, fixture inputs, hashes, artifacts, unresolved findings, and supported conclusions.
Reuse unchanged evidence.
Allow one initial read-only request and at most one useful corrected retry per underlying failure across tools, agents, and resumed work.
Then use pertinent source/reference review and local checks, recording the limit once.
No tool installation, profile repair, game launch, or log search is authorized.

Fix known defects and recheck affected behavior.
Unavailable optional evidence limits claims.
Missing actual darkness/night functionality, accepted features, or specifically requested artifacts leaves those outputs incomplete.
Static previews cannot establish either core engine mechanism.
Separate source conclusions from observed game behavior.

## Routed checks

| Check and owner | Exact surface, timing, and scenarios | Expected evidence and comparison | Findings requiring follow-up |
| --- | --- | --- | --- |
| M01 References: parent and `chaosx_scripted_system_architect` | Before native mechanism or helper implementation. Use exposed `hoi4.reference_context`, `reference_search`, `reference_read`, and `source_lookup` for lighting, night combat, weather modifiers, scope, iteration, and shared-owner endpoints. Cover CORE, STATE, and RETURN cases. | Cited offline wiki and installed documentation sections, exact vanilla/mod definitions, source revisions, and supported parameters. Follow omitted required sources. Inspect source directly when retrieval is unavailable. | Unsupported fields, scope assumptions, duplicate weather/night modifiers, guessed creature predicates, or missing owner contracts remain unresolved. A definition's existence alone proves no live survivor. |
| M02 Script validation: architect and owning patch worker | After each meaningful lifecycle, decision, incident, enrollment, or cleanup edit. Use exposed `hoi4.script_validate` on changed files under explicit scopes. Cover FLOW, PAY, STATE, CREATURE, and RETURN. | `checksPerformed`, file/line findings, known-mistake checks, unresolved helpers, scope bindings, and source review of unchecked arguments. Recheck actual fixes against the new revision. | Invalid scope, malformed dynamic fields, duplicate transaction calls, stale callback paths, or unsupported commands require fixes. A true result covers only its reported checks and proves no runtime execution. |
| M03 Event graph: parent and completion auditor | Inspect resolved entry, acknowledgement, stage, incident, manual-launch, Heat Wave, and Return paths before and after integration. Use `hoi4.event_inspect`, meaningful `event_render`, and `event_inspect(mode=compare)` where supported. | Preserve a graph-bearing `event-graph-<revision>.json` baseline. Compare branches, scopes, helper reachability, duplicate logs, and terminal paths. Use `state_flow` or `impact` for lifecycle questions and inspect helper source where coverage is partial. | An unguarded alternate entry, dangling owner callback, repeated manifestation, or post-Return mutation is a defect. Focused traces scan events/on_actions and cannot prove complete helper/lifecycle coverage, even with helper expansion. |
| M04 Opening and timing: `chaosx_ai_probability_auditor` | Before balance acceptance and after resolver changes. Start with `hoi4.probability_inspect`, then supported `probability_analyze` compare/sweep/simulate/sequence modes as relevant. Cover FLOW-02 through FLOW-06 and MANUAL. | Complete opening pools for all Chaos bands and toggle masks. Named constant-condition stage/Return fixtures, declared elapsed eligible exposure, interval lengths, seeds when sampled, and exact formula calculations. Compare preserved source and identical fixtures. | Wrong normalization, compounded stage medians, resetting paused exposure, fixed expiry, or toggle-created Chaos requires correction. Distribution targets require a demonstrated resolver. An MTTH label alone is insufficient. |
| M05 AI and selection: probability auditor with decision owner | After the action ledger and targeting logic exist. Inspect policy defaults, upkeep, mission commitments, relief targets, incident pools, and invalid-target pruning. Cover AI-01, PAY, and CREATURE. | Source-derived weight traces, complete relevant candidate pools, reserve/capacity fixtures, cooldown transitions, and before/after comparisons when weights change. Classify results exact, bounded, sampled, score-only, or unresolved. | Positive weight on impossible targets, abandoned commitments, endless retries, starvation, or receipt farming requires owner fixes. Decision willingness and target scores are not automatically normalized click probabilities. |
| M06 Panel review: `chaosx_event_ui_worker` | Before and after event-owned GUI edits, using `hoi4.gui_inspect` and available `gui_render`. Cover UI-01 with selected/no target, empty/crowded lists, valid/blocked costs, active/completed/failed missions, Return, hover, warning, and paused updates. | Accepted reference, native-element map, matching fixtures, source revision, supported resolutions/UI scales, click regions, hierarchy, assets, text, and before/after images. Optional `gui_rewrite` stays within the exact event-owned allowlist. | Clipping, dead controls, wrong cost/target, stale paused state, more than two public values, six action rows, or three missions requires repair. Undecided visibility fixtures need explicit flags/variables. Previews do not run the game. |
| M07 State and map review: `chaosx_map_states_worker` | Inspect connected state, controller, supply, railway, and adjacency data through `hoi4.map_inspect` before any scoped changes. Cover CORE-04, STATE, PAY-07, and CREATURE-04. | Named area/layer/overlay views, exact state and owner bindings, affected-state coverage, humanitarian preflight evidence, and pre/post transaction accounting. | Missing environmental states, invalid controllers, duplicate populations, or unproven route delivery require fixes. Map inspection does not establish day/night rendering behavior or actual supply throughput. |
| M08 Cross-system review: parent and completion auditor | When live schemas expose useful `impact_inspect`, `decision_inspect`, `mechanic_test`, `package_check`, or `scenario_test` routes. Apply narrow changed-surface cases from MANUAL, PAY, CHAOS, and RETURN. | Declared fixture inputs, exact covered files, package references, owner/caller deltas, and remaining unsupported behavior. Use these outputs alongside direct source and receipt review. | Broken owner integration, missed manual paths, conflicting registry references, or known cleanup defects require fixes. Optional tool absence is a disclosed evidence limit, and scenario analyzers are not live playtests. |

## Comparison and artifact discipline

Preserve exact before-source bytes outside gameplay directories.
Where supported, bind the original logical path to `snapshotPath` and raw-byte `expectedSourceHash`.
Arbitrary archive paths can fail discovery.
Use identical fixtures and verify both candidate pools after renames.
Current shared dependencies limit historical whole-workspace claims.

Event comparisons require graph payloads.
Label reverse source-overlay comparisons explicitly.
Never mutate live source to manufacture a baseline.
Missing baselines limit historical deltas while current behavior remains reviewable.

Retrieve large artifacts through bounded continuations, checking decoded ranges, complete assembly, size, hash, format, URI, and revision.
Use resource server key `hoi4_agent_tools`.
Discover required schemas, service health, job support, and viewer availability separately, retaining handles for unresolved jobs.
Keep evidence in current handoffs.
User-owned live testing requires separate explicit authorization.

## Source basis

The [MCP integration guide](../../systems/hoi4_agent_tools_mcp_integration.md) supports the current routes, reference workflow, rendering limits, comparison inputs, artifact recovery, and focused-analysis boundary.
The [runtime guide](../../runtimes.md) confirms canonical skill mirrors, runtime-owned model selection, and machine-specific MCP registration.
The planning pass pinned these guides at repository commit 41bc4e5045a7b5c131be69dda2f08079d478634c, and the research record keeps that revision.
Current AGENTS and owning skills remain required in the implementation environment.
