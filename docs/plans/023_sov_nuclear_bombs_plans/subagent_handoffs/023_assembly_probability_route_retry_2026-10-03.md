# Event 23 device assembly AI score: probability route retry

Disposition: unresolved for probability and ranking conclusions because the connected HOI4 probability adapter was not exposed and its MCP server did not complete resource handshaking. The read-only source trace is complete within the bounded assembly-decision scope.

Audit date: 2026-10-03.

Repository: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.

## Scope and ownership

Audited only `sov_nuclear_bombs_assemble_device_batch` in `common/decisions/023_sov_nuclear_bombs_decisions.txt`; the initially supplied spelling `sov_nuclear_bombs_assemble_devices` does not occur as the decision id. The current id is `sov_nuclear_bombs_assemble_device_batch` at lines 292-315.

Reviewed only the eligibility, readiness input, assembly start/completion path, runtime production grant adapter, and named constants that bear on this score. Did not inspect or assess other AI weights. Per-depot custody and its repair remain parent-owned and were not audited here.

No gameplay, AI, event, decision, scripted effect, trigger, localisation, asset, workbook, skill, or Git changes were made. No game, save, or logs were used.

## Live MCP route status

The live `ALL_TOOLS` inventory contained zero `mcp__hoi4_agent_tools__*` entries and zero `hoi4.probability_*`, `hoi4.reference_*`, or `hoi4.source_lookup` routes. No live schemas were available. Consequently, `hoi4.probability_inspect` could not be called as the required first analysis step; no probability analysis was started, and no service version, health result, adapter revision, or scenario schema was returned.

Read-only `list_mcp_resource_templates({ server: "hoi4_agent_tools" })` and `list_mcp_resources({ server: "hoi4_agent_tools" })` both failed with: `MCP startup failed: timed out handshaking with MCP server after 119.9999997s`. They returned no reusable scenario definitions or artifacts. The HOI4 server's artifact template could not be confirmed in this turn. No job, helper-expansion, or native task was created.

The prior handoff at `docs/plans/023_sov_nuclear_bombs_plans/subagent_handoffs/023_assembly_registry_audit_retry_2026-10-03.md` contains the five scenario names but no accepted scenario payloads, scenario hashes, probability artifact URIs, or scores. A bounded repository search found those names only in that handoff. No `probability_inspect` retry with an explicit workspace was possible because the route was absent, rather than exposed and timing out on a request.

`hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, and `hoi4.source_lookup` were also absent from the live inventory. The pertinent offline wiki and installed vanilla decision documentation were read directly from local files; their paths, line spans, and SHA-256 identities are listed below. This is local reference evidence, not MCP retrieval.

## Audited source trace

In `common/decisions/023_sov_nuclear_bombs_decisions.txt:292-315`, the decision declares `state_target = any_owned_state`. Its `ai_will_do` block has `base = 0.80` and one modifier, `factor = 1.50`, whose condition is `check_variable` on `sov_nuclear_bombs_readiness` with `compare = less_than` and `value = 50`. This is a source-defined willingness score, not a click probability. No evaluated numeric score is claimed here.

The exact source-condition trace is: readiness 49 satisfies the modifier condition; readiness 50 and 80 do not. This reports the authored comparison only. The adapter did not evaluate the score, apply external factors, or rank it against candidates, and no hand-calculated final score is substituted for those missing results.

The weight expression itself does not test technology, production capacity, target validity, project status, receipt state, or affordability. Those conditions are separate from the score: `visible` and `target_root_trigger` require a valid SOV actor, production phase, production capacity, no active project, and no assembly cooldown; `target_trigger` requires the selected state to satisfy `sov_nuclear_bombs_event_state_is_valid_assembly_site`; and `available` additionally requires `atomic_research`, `nukes`, a clear assembly receipt, and the security-cost predicate. The completion effect repeats the critical actor, capacity, technology, project, receipt, cost, and selected-site checks before beginning production (`common/decisions/023_sov_nuclear_bombs_decisions.txt:298-314`).

The target-site predicate requires a registered, passable storage state owned and controlled by SOV, with infrastructure above zero and no dismantled, missing, Event 5 snapshot-pending, or technical-denial state flags; the assembly predicate additionally requires at least one arms factory or industrial complex (`common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:655-674`). Production capacity requires the valid SOV actor, no atomic moratorium, a positive reactor-count variable, and at least one owned and controlled state flagged as a production reactor site with a nuclear reactor (`...event_triggers.txt:597-606`).

The successful assembly path begins a mission only after its own capacity, technology, active-mission, receipt, moratorium, selection, and production-quote checks pass (`common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:2150-2179`). Completion grants devices through `sov_nuclear_bombs_register_production_devices` only after actor, exact active-site, capacity, technology, and positive-amount checks; that runtime adapter updates the native stockpile and ledger together (`common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:1918-1953`; `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt:269-287`). Cancellation clears the pending amount and active mission and records rejection consequences; it does not run the production grant helper (`...event_effects.txt:1955-1964`).

The named constants file is `common/script_constants/023_sov_nuclear_bombs_constants.txt`. It contains the readiness changes for production start and completion and the production mission duration, but the audited score block uses inline literals rather than constants (`...constants.txt:235-301,476`). The score's base `0.80`, factor `1.50`, and threshold `50` are therefore hardcoded at the decision definition. The source review found no target-specific score constant reference in that block.

The source establishes a single active-project gate and a success cooldown whose duration uses the production-mission constant. Production start and successful completion also change Readiness through named constants. This prevents concurrent starts in the source path and means future willingness depends on later Readiness state; it does not establish AI action frequency, repeated-cancellation behavior, a long-run score trajectory, or the absence of a strategic snowball.

## Scenario evidence

No scenario was submitted to an analyzer, so there are no scenario hashes, evaluated traces, ranking results, comparison ids, or render URIs. The labels below are the only retained scenario identities. Candidate-pool and external-factor completeness are stated separately for every case.

| Scenario id | Source-only trace | Candidate pool | External factors | Result classification |
| --- | --- | --- | --- | --- |
| `P23_ASSEMBLY_AI_READINESS_49_VALID_SITE` | The modifier condition is true if the scenario supplies readiness 49 and a valid site. Base literal 0.80 and factor literal 1.50 are present in source. | Incomplete: the state ids and full set of matching owned-state targets are not supplied. | Incomplete: live strategy factors and other engine-level modifiers were not inspected or evaluated. | Exact source predicate; score-only source trace. Evaluated score, rank, selection probability, and dominance are unresolved. |
| `P23_ASSEMBLY_AI_READINESS_50_VALID_SITE` | The strict `less_than 50` condition is false at readiness 50; the authored base remains 0.80. | Incomplete: the state ids and full set of matching owned-state targets are not supplied. | Incomplete: live strategy factors and other engine-level modifiers were not inspected or evaluated. | Exact source predicate; score-only source trace. Evaluated score, rank, selection probability, and dominance are unresolved. |
| `P23_ASSEMBLY_AI_READINESS_80_VALID_SITE` | The strict `less_than 50` condition is false at readiness 80; the authored base remains 0.80. | Incomplete: the state ids and full set of matching owned-state targets are not supplied. | Incomplete: live strategy factors and other engine-level modifiers were not inspected or evaluated. | Exact source predicate; score-only source trace. Evaluated score, rank, selection probability, and dominance are unresolved. |
| `P23_ASSEMBLY_AI_SITE_LOST` | A target that no longer satisfies the assembly-site predicate is excluded by the source target gate. The label does not specify which ownership, control, registration, infrastructure, or site flag changed, or whether another valid depot remains. | Incomplete: no affected state id or remaining target set is supplied. | Incomplete: live strategy factors and engine state were not inspected or evaluated. | Source gate is exact; scenario eligibility, remaining pool, score evaluation, and selection are unresolved. |
| `P23_ASSEMBLY_AI_NO_CAPACITY` | If the production-capacity helper is false, the decision's visible and target-root gates fail before a selectable target is offered. The label does not provide a typed input showing which capacity requirement is absent. | Incomplete: no scenario payload or target enumeration is available. | Incomplete: live strategy factors and engine state were not inspected or evaluated. | Source gate is exact; scenario evaluation and confirmation that the helper is false are unresolved. |

The native target pool is bounded in source to SOV-owned states selected by `any_owned_state` and filtered by the target trigger. Installed decision documentation states that each matching target creates a dedicated decision entry (`common/decisions/_documentation.md:31-45`). The number and identity of qualifying entries at each scenario state remain unknown. No complete race pool covering the relevant SOV decisions or the external AI modifiers was provided, so no exact probability or normalized share can be stated.

## Findings and unresolved risk

- Weight shape: one base and one readiness-gated multiplier. No duplicated or contradictory clause exists inside this decision's `ai_will_do` block. The threshold has a strict boundary at 50, but whether that causes a rank reversal against other choices is unresolved.
- AI validity: the decision's own eligibility checks cover actor, phase, capacity, project/cooldown, state validity, technologies, receipt, and affordability. Because the score does not include those checks, validity relies on the separate decision gates. Source review cannot establish whether the connected analyzer or running AI excludes every blocked candidate as expected.
- Candidate ranking: no ranking or tie behavior was returned. The same source score expression has no target-specific modifier, but per-target rank behavior and the full candidate pool are unresolved.
- Dominance and starvation: unresolved. No competing candidate scores, external AI factors, or complete pool were available.
- Repetition and snowball: the source blocks concurrent projects and applies a success cooldown; production effects also change Readiness. No cadence simulation or sequence analysis was possible, so repeated attempts, rank drift, and long-horizon snowball risk remain unresolved.
- Site loss and no capacity: source predicates identify the blocking gates, but scenario state is not represented by an accepted fixture and no MCP result confirms target removal.
- Classification: authored literals and trigger truth by the named readiness values are exact source facts; the weight itself is score-only; all scenario evaluations, rankings, dominance/starvation, and long-run behavior are unresolved. No sampled result exists.

## Recommended follow-up

Do not change the three AI-score values based on this audit. If the owner wants to address centralized tuning, consider moving the existing base, factor, and threshold into the Event 23 tuning constants or a documented tuning table while preserving their current values, after confirming that the installed parser accepts `constant:` in these `ai_will_do` fields. This is a maintainability recommendation, not a balance target or an applied patch.

When the probability route is available, rerun `hoi4.probability_inspect` first for this decision, then evaluate the same five scenario ids with complete supported inputs and target pools, sweep the threshold around 50 for rank reversals, and render the unresolved or ranking view if the adapter supplies one. Include declared external AI factors. Do not compare the current source to itself: no authoritative pre-change source was supplied, this audit made no source change, and no numeric before/after comparison is available.

## MCP and local-reference evidence

MCP probability adapter: unavailable in this turn. `probability_inspect`, `probability_evaluate`, `probability_sweep`, `probability_compare`, `probability_render`, `probability_simulate`, and `probability_sequence` were not callable. No probability artifact URI, adapter revision, scenario hash, analysis id, comparison id, or rendered path/URI exists.

`probability_evaluate` and `probability_sweep` were skipped because the required inspect route and schemas were absent. `probability_render` was skipped because no analyzer result or renderer route existed. `probability_simulate` was not used because no explicit uncertain-input distribution was supplied. `probability_sequence` was not used because this is a native decision score, not a declared custom weighted pool with a complete candidate set, cadence, and state transitions. `probability_compare` was not applicable to a read-only retry with no authoritative before source; comparing the current file to itself was intentionally avoided.

Local reference sections read directly:

- `paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md:357-372` describes decision `ai_will_do` as a weighted MTTH block.
- `paradox_wiki\AI modding - Hearts of Iron 4 Wiki.md:26-34` distinguishes the general `ai_will_do` highest-roll score race from event-option `ai_chance` probability-proportional sampling and explains `base` and multiplicative `factor`. Applying the general score-race description specifically to this decision is an inference from that section together with the Decision modding section.
- `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\_documentation.md:1-45` documents visible/available and targeted-decision evaluation, including that each matching target creates a separate entry.

## Source identities

Current local SHA-256 values identify the files reviewed; no MCP source revision was returned.

| File | Relevant lines | SHA-256 |
| --- | --- | --- |
| `common/decisions/023_sov_nuclear_bombs_decisions.txt` | 292-315 | `EDD21C1D4F062DBD02C4DF5FC99FF5B50F23093ECF6C8582777B946AABB01AAB` |
| `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt` | 597-606, 655-674 | `B09ED078E9FBA26628488CA1BC51656CC5FCE7F301492263E545D74948B168DD` |
| `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt` | 1918-1964, 2150-2179 | `7899FFCDD5550FDD7D870FA7CF9A107E1B2E5D7C3F56889A72EFBC43369DA2E7` |
| `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt` | 269-287 | `CAC0F35DE4A3CBAF52DB12AB462E62B9C7C6860775F89A02AA9C7405A527E001` |
| `common/script_constants/023_sov_nuclear_bombs_constants.txt` | 235-301, 476 | `5BCF3F563B9ABEEC59C8A93A73FA1F89A7AF3FB1EF9B9D4B9D7FDE90B40E54FC` |
| `paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md` | 357-372 | `7713B9BCEE5F3818D63AAFBD45D18E812A9173A7C59AB238384B57DB60DB6162` |
| `paradox_wiki\AI modding - Hearts of Iron 4 Wiki.md` | 26-34 | `917CD261F7DA51FE4D8687C5D7663E768A09C5C101AC130CE646BC64637AA818` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\_documentation.md` | 1-45 | `5E7E686B5582F32C38D898D805E17171E88F3BFEEE4A030DEB1884F9726DE019` |

## Omissions and remaining blockers

The required MCP probability evidence is absent, so this is not a completed balance determination. Candidate-pool completeness, external-factor completeness, evaluated scores, rank reversals, dominance, starvation, long-run repetition, and exploit/snowball outcomes remain unresolved. No baseline comparison was possible. No source patch, localisation change, save inspection, or game validation was performed; the source was reviewed locally as documented above. The exact blocker is the absent HOI4 tool namespace in the live inventory plus MCP startup handshake timeout for both resource queries.

Skills read and applied: `chaos-redux-subagents`, `chaos-redux-mtth`, and `chaos-redux-decisions-missions`. No skill was created or modified.
