# Event 016 Mengele Singularity construction AI audit

Date: 2026-09-25

Status: read-only source comparison complete; corrected MCP scenario schema was accepted and evaluated as partial. Candidate scores are exact from the current source formula and constants, while MCP eligibility coverage remains unresolved. No gameplay source was edited, no file was staged, and no commit was created.

Disposition: unresolved. The source formula scores are clear and matched between the two choices and the Kruger references. The corrected evaluator returned ranking and unresolved artifacts, but its response did not expose candidate-level score rows; a cached render attempt failed. Eligibility, complete state-target enumeration, full-pool ranking, and historical comparison remain unresolved.

## Scope and final source revision

Audited the two new state-target decisions in C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\decisions\016_mengele_singularity_construction_decisions.txt:

- mengele_event016_construct_singularity_command_node
- mengele_event016_construct_singularity_power_link

The parent reported that only presentation tooltip text changed after this audit started and that no weight changed. The final local SHA-256 of the decision file is 65D6F2D35B5D148F9A2C7F3476C05E6A6DEF91E62BDF2597F51549CFB16D4461.

The initial MCP inspect captured source revision 9eb5d2a45df076a7f6399b4e74eff1d7bf1e31394d11f8c4097215bb74b5ffda and source hash bcf1b9375e01fe65f61d793c39ab0a4f2367817d31cacd34e899bdd5a4034103. That hash differs from the final local file hash and, per the parent’s update, predates the presentation tooltip edits. The later evaluate and compare calls used refresh=true but failed input validation before returning an analysis or refreshed source revision.

Corrected follow-up on 2026-09-25 used the final file and the accepted scenario schema from .agents/skills/chaos-redux-subagents/SKILL.md after the parent reported the presentation tooltip edits. The refreshed inspect and evaluate report the same MCP sourceHash, 7af51fc12db45eba9cec268889ac81eaaa983cdabb342365350d5a19d9422b64, while their sourceRevision values differ; see the call records below. These refreshed calls do not predate the reported tooltip edits by call timing. The MCP sourceHash is distinct from the local raw-file SHA-256, so byte-for-byte identity is not established by the hash values alone. The final local SHA-256 remains 65D6F2D35B5D148F9A2C7F3476C05E6A6DEF91E62BDF2597F51549CFB16D4461.

The reference decisions are in C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\decisions\016_brilliant_scientist_directorate_project_board.txt:

- brilliant_scientist_construct_singularity_command_node
- brilliant_scientist_construct_singularity_power_link

The shared values are defined in C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\script_constants\016_brilliant_scientist_project_constants.txt.

## MCP evidence and diagnostics

The mandatory first call was hoi4.probability_inspect with adapter decision_ai_will_do and source object {path: "common/decisions/016_mengele_singularity_construction_decisions.txt"}. It returned status ok and code PROBABILITY_SOURCE_DISCOVERED. The requested adapter had zero candidates and discoveryReason requested_adapter_empty. The MCP suggested mission_ai_will_do and reported two candidates there, with both requested decision identifiers as examples. No diagnostics or unresolved inputs were reported by that discovery call.

Inspect artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8ee04b3bb23e4ac23e91efd5d0079ef604a6a5331e301ef4d8539e0743fd945c/7f16bd16fe924919de8a231d6b68de94655af8014297bbb17ff186532bcc90bb/probability-inspect-bcf1b9375e01.json

The initial bounded probability_evaluate attempt used the suggested mission_ai_will_do adapter, the current source path with refresh=true, the two new decision IDs as candidatePool, and scenario-set ID MENGELE_SINGULARITY_CONSTRUCTION_AI_2026_09_25. Its intended scenario IDs were AVAILABLE_PEACETIME, AVAILABLE_WARTIME, UNAVAILABLE_ROUTE_LOCKED, and UNAVAILABLE_SITE_INVALID. This initial call returned an input validation error before analysis:

~~~text
MCP error -32602: Input validation error: Invalid arguments for tool hoi4.probability_evaluate:
Invalid input: expected record, received undefined at scenarioSet.scenarios[0].state
Invalid input: expected record, received undefined at scenarioSet.scenarios[1].state
Invalid input: expected record, received undefined at scenarioSet.scenarios[2].state
Invalid input: expected record, received undefined at scenarioSet.scenarios[3].state
Unrecognized keys: "name", "inputs" at scenarioSet.scenarios[0]
Unrecognized keys: "name", "inputs" at scenarioSet.scenarios[1]
Unrecognized keys: "name", "inputs" at scenarioSet.scenarios[2]
Unrecognized keys: "name", "inputs" at scenarioSet.scenarios[3]
Unrecognized key: "name" at scenarioSet
~~~

No evaluator artifact, analysis ID, source revision, scenario hash, score trace, or ranking was returned by that initial call. The rejected four-scenario attempt is superseded by the corrected two-scenario follow-up below.

The corrected probability_inspect used adapter mission_ai_will_do, source {path: "common/decisions/016_mengele_singularity_construction_decisions.txt"}, refresh=true, and the same two candidate IDs. It returned status ok and code PROBABILITY_SOURCE_INSPECTED, with no diagnostics or blockers. Its sourceRevision was 15d7e7f308ec9d5ad611bbe5182e825d06747beb04110dcab1eb5d3f42136373 and sourceHash was 7af51fc12db45eba9cec268889ac81eaaa983cdabb342365350d5a19d9422b64. It reported poolComplete=true, candidates=2, availableCandidates=0, availableAdapters=[], requiredInputs=3, unresolved=0. Record the reported zero available candidates as an adapter discovery result, not proof that the decisions are unavailable in game.

Corrected inspect artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4b80d899376da2919af53552908650dc34d818078d2e72ec5aa388caf36a085c/cd9dbccdb9baa49eb46bb78f71f68298ceed8c39acca9d4e9cc0f0ce4d8485f4/probability-inspect-7af51fc12db4.json

The corrected bounded probability_evaluate used mission_ai_will_do, the same final source path, refresh=true, and exactly the same two candidate IDs. It supplied scenarioSet ID MENGELE_SINGULARITY_CONSTRUCTION_AI_2026_09_25 with scenarios MENGELE_SINGULARITY_CONSTRUCTION_PEACE and MENGELE_SINGULARITY_CONSTRUCTION_WAR, each using the accepted shape {id, actor, state, flags, scopes}. Both used actor ABC, flags mengele_clone_army_scenario_country and mengele_clone_focus_directorate_project_registry, and FROM scope {id: "STATE_1", state: {is_owned_by: "ABC", is_controlled_by: "ABC", land_facility: 1}}. The flat state map set has_war=false for peace and true for war. Metrics requested were raw_value; outputs were json, ranking, and unresolved.

The evaluator returned status ok, code PROBABILITY_ANALYZED_PARTIAL, analysisStatus partial, analysisId probability-09ecd7d5a4a466da1c6da10d, sourceRevision ef6fcdfca25a4d499f854391e4d952cc2221183a6e9d8ecc8b26fb44b437e59e, sourceHash 7af51fc12db45eba9cec268889ac81eaaa983cdabb342365350d5a19d9422b64, scenarioHash 38783290d5eb972d0b1da7dad2a9fc9f8dd819933942f140992f226d9ddff3e6, cacheKey 09ecd7d5a4a466da1c6da10db95d2a409cf587ecb44efa5bc2ce15bd548090cf, scenarios=2, candidates=4, unresolved=4, diagnostics=0, and visualResources=4. There were no blockers. The source hash matches the corrected inspect hash although the reported sourceRevision differs between calls.

Evaluation JSON artifact (authoritative scenario report, 40,765 bytes): hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/435a7f7c0458853a259f1289425f8c81bf2d33870cd353ed46a1ec4b954ecf2d/ef97b4d2cf51a0fcc933254cb4bedb17761c42d2371b1ad125b5dda04295f412/probability-09ecd7d5a4a466da1c6da10d.json

Generated ranking artifacts: SVG hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c196d271a966d544d1bfdf8b3bbffdbeda0d74b4818b90fcdfa286c9a7eaeb1e/b9d7eeb92588c4c0d72b4672ed4125eac474e54191567cd761d34a30409f9d9b/probability-probability-09ecd7d5a4a466da1c6da10d-ranking.svg; PNG hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9541d671748c3dee9bd8482215d3d5488b1597e19ce58a0db05df50eee577ea0/f0e24a1da86eb22336d5cb7901c7868f2a758a12c451473209c1731dac491464/probability-probability-09ecd7d5a4a466da1c6da10d-ranking.png. Generated unresolved artifacts: SVG hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cca88b9c439b35f859afb44bf779000dd9123662084fe5b9f40841dc76933ed7/70acbede40a97a440ae0153262782c478f95d19c5176b56cb5176a8cacd939f3/probability-probability-09ecd7d5a4a466da1c6da10d-unresolved.svg; PNG hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b3780c80be6119fc127c47432d526bcf4ec77eea8c4b2fec881c1293f2c52d6f/a520c32af0adb55973ba0916059d74b51c4af8fb28f45188309ae59efce7f886/probability-probability-09ecd7d5a4a466da1c6da10d-unresolved.png.

The evaluate response did not inline candidate-level raw_value rows; it linked the authoritative JSON artifact. One probability_render request against that analysisId and scenarioHash returned status error, code PROBABILITY_ANALYSIS_NOT_CACHED, with exact blocker: "Render requires an analysis ID produced by this server process". No render retry was made. Thus the MCP envelope proves the corrected scenarios were accepted and analyzed partially, but its visible result does not independently expose exact score rows or identify the four unresolved items by name.

Source-expanded raw scores from the exact current formula and constants are 10 for each decision in peace and 20 for each decision in war: base constant:brilliant_scientist_project_board.ai_high=10, multiplied by constant:brilliant_scientist_project_ai.preferred_factor=2 only when has_war=yes. These are exact source-derived score values, classified score-only; do not attribute them to an inline MCP trace. They are not click probabilities.

The earlier absent-before probability_compare attempt used before=null, the current source as after, refresh=true, the same candidate IDs, and the same four scenario IDs. The call rejected the absent baseline and submitted scenario shape:

~~~text
MCP error -32602: Input validation error: Invalid arguments for tool hoi4.probability_compare:
Invalid input: expected object, received null at before
Invalid input at scenarioSet.scenarios[0].state.country
Invalid input at scenarioSet.scenarios[0].state.targetState
Invalid input at scenarioSet.scenarios[0].state.declaredCandidateInstances
Invalid input at scenarioSet.scenarios[1].state.country
Invalid input at scenarioSet.scenarios[1].state.targetState
Invalid input at scenarioSet.scenarios[1].state.declaredCandidateInstances
Invalid input at scenarioSet.scenarios[2].state.country
Invalid input at scenarioSet.scenarios[2].state.targetState
Invalid input at scenarioSet.scenarios[2].state.declaredCandidateInstances
Invalid input at scenarioSet.scenarios[3].state.country
Invalid input at scenarioSet.scenarios[3].state.targetState
Invalid input at scenarioSet.scenarios[3].state.declaredCandidateInstances
~~~

No comparison ID, scenario hash, artifact, or refreshed source revision was returned. The route did not accept null as an absent-before representation. The historical before-source file remains absent, so this comparison is still blocked; it was not retried after the corrected inspect/evaluate pass.

No probability_sweep was run: the requested pass was bounded to the two named scenarios, and the partial evaluation leaves eligibility and pool coverage unresolved. A probability_render was attempted once for the accepted evaluation and failed with PROBABILITY_ANALYSIS_NOT_CACHED as recorded above. No probability_simulate was used because no uncertain inputs were declared. No probability_sequence was used because these decisions are not a declared custom weighted pool with cadence and state transitions.

## Source score comparison

Both new decisions use the same source expression:

- Base: constant:brilliant_scientist_project_board.ai_high, whose value is 10.
- Modifier: multiply by constant:brilliant_scientist_project_ai.preferred_factor, whose value is 2, when has_war = yes.
- No other ai_will_do modifier appears in either new decision.

The existing Kruger command-node and power-link decisions in 016_brilliant_scientist_directorate_project_board.txt use the exact same base, factor, and has_war condition. Source-level comparison therefore finds no direct score difference between each Mengele choice and its Kruger counterpart. This is a score-only source comparison; MCP did not confirm an expanded value. The source expression is 10 at peace and applies the 2 multiplier during war, but that arithmetic is not an MCP-evaluated trace.

The base is positive and bounded by the single conditional multiplier. There is no flat or zero weight, contradictory modifier, or weight differing between the two new decisions. No named AI-strategy plan targeting these four decision IDs was found in the searched mod AI-strategy paths. Other engine-level decision selection factors remain unverified. MCP generated ranking artifacts for the two scenarios, but the linked ranking contents were not returned inline and are not interpreted here as a complete game-wide race.

ai_hint_pp_cost = 100 is an AI cost hint, not part of ai_will_do. The 5 and 6 civilian_factory_use values and the underlying payment checks are eligibility or construction burdens, not score modifiers.

## Candidate pools and scenario completeness

The candidate pool submitted to MCP contained only the two new decision identifiers. The initial inspect found those two definition-level candidates under mission_ai_will_do, but the pool is not complete for a selection analysis: state_target = yes creates target instances for qualifying states, and no live state list, state IDs, or count of eligible sites was supplied. The scenario fixtures declared one target instance per choice when available, but MCP rejected the fixture shape. The Kruger reference decisions were compared from source and were not part of the submitted MCP candidate pool. Other concurrently eligible decisions and engine-level decision factors were not enumerated.

| Scenario ID | Declared intent | Candidate and external-factor completeness | Result |
| --- | --- | --- | --- |
| AVAILABLE_PEACETIME (initial attempt) | Both new choices available; peace; provider and unlock gates true; no active or pending construction receipt; both payment helper checks true; one intact owned and controlled target state for each choice. | Assumed helper outputs rather than their underlying campaign state; one target instance per choice; no full decision universe. | Initial four-scenario shape rejected. Superseded by corrected peace scenario below. |
| AVAILABLE_WARTIME (initial attempt) | Same gates and target assumptions, with has_war = yes. | Same incomplete target and decision pools; has_war was the only intended score-changing input. | Initial four-scenario shape rejected. Superseded by corrected war scenario below. |
| UNAVAILABLE_ROUTE_LOCKED (initial attempt) | Route unlock gates false, with otherwise valid target and payment assumptions. | No candidates declared for these choices; unrelated AI candidates and live route state absent. | Initial four-scenario shape rejected. Not included in bounded corrected pass. |
| UNAVAILABLE_SITE_INVALID (initial attempt) | Unlock gates true but target-state validity false. | No target instances declared; no live state set or wider decision pool. | Initial four-scenario shape rejected. Not included in bounded corrected pass. |
| MENGELE_SINGULARITY_CONSTRUCTION_PEACE | Actor ABC, has_war=false, the two named decision candidates, route/registry flags, and a symbolic FROM state scope with owner/controller ABC and land_facility=1. | Candidate pool complete only for the two requested definitions, not all game decisions or all state-target instances. Actor and state are scenario fixtures, not verified live campaign IDs; complex route, receipt, payment, and state validity helpers are not proven by the fixture. | Accepted; partial analysis, 2 candidate instances in the two-scenario result; source-derived score 10 each; eligibility unresolved. |
| MENGELE_SINGULARITY_CONSTRUCTION_WAR | Same fixture and candidates, with has_war=true. | Same limits; only declared score-changing input is has_war. | Accepted; partial analysis, 2 candidate instances in the two-scenario result; source-derived score 20 each; eligibility unresolved. |

The corrected schema supplies only state.has_war plus the listed flags and symbolic FROM scope; it does not assert a complete campaign snapshot. The outer evaluate result reports four unresolved analysis items but does not expose their identifiers. The fixture did not expose the provider's required branch idea or program flags, route-unlock and component-need helper state, active/pending receipt state, exact payment resources, other qualifying facilities, every target state, or the complete AI strategy and decision context.

## Eligibility and state-target validity review

The new decisions set state_target = yes and use target_root_trigger for route unlock plus target_trigger for brilliant_scientist_mengele_singularity_site_state_is_intact_and_owned. Their available blocks additionally require the matching can_begin helper, the same state validity check, and the matching payment helper.

The direct construction triggers require a valid Mengele project-stage provider, the component unlock and site-need gates, no active construction receipt, no pending site receipt, and the relevant can-pay helper. The site trigger checks a valid state owned and controlled by the receipt-owning country and the qualifying intact facility condition. These source gates make no static positive-weight-on-an-ineligible-choice defect apparent: the AI score is attached to decisions whose route, target, and availability conditions gate eligibility.

That is a source review only. The probability adapter did not confirm the game’s candidate enumeration or prove that every helper and target gate is honored in an AI trace.

## Findings by requested risk

- Dominance: no direct score dominance between the two new choices or their Kruger references; all four source formulas match. Relative dominance against other available decisions is unresolved; the MCP ranking resources cover only the submitted two-candidate pool.
- Starvation: no score-level starvation between the two choices is visible. Starvation against the full decision pool, and the effect of cost or factory availability on actual starts, are unresolved.
- Rank reversal: no direct formula difference exists to reverse the pair’s source-score ordering. Target-instance multiplicity, availability, other decisions, and external factors could change the effective race; the generated ranking artifact content was not retrieved, so no further ranking claim is made.
- Repetition: the shared active-receipt and per-site pending-receipt gates constrain concurrent starts. Repeated starts across remaining eligible sites and their campaign cadence were not evaluated.
- Exploit risk: source gates reject invalid routes, states, outstanding construction receipts, and unaffordable starts. No exploit finding is established without the helper execution trace and complete state pool.
- Timing: the decisions have construction timers, but no AI timing distribution was analyzed. ai_will_do is willingness scoring, not a construction-duration or click-probability measure.
- Exact selection probability: none is claimed. The two-candidate definition pool is complete for the bounded score comparison, but target multiplicity, the full decision pool, and external factors are incomplete; the corrected evaluation is partial, and historical comparison remains blocked.

## References reviewed

Read AGENTS.md, .agents/skills/chaos-redux-decisions-missions/SKILL.md, .agents/skills/chaos-redux-subagents/SKILL.md, and the parent-named 016_alien_api_audit_current_2026-08-26.md handoff.

Read the required core offline wiki pages in paradox_wiki: Data structures, Triggers, Effects, Modifiers, Localisation, On actions, Event modding, Decision modding, Idea modding, and AI modding. The relevant decision and AI sections describe state-target matching and ai_will_do as an AI willingness score used in a score race; they do not justify presenting a score as a probability-proportional selection chance.

Consulted the installed vanilla documentation references in C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md for activate_targeted_decision and remove_targeted_decision scopes, plus the triggers, modifiers, and script-concept documentation for relevant source constructs. The vanilla state-target example reviewed is C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\AFG.txt, which uses explicit state targets and target_trigger filtering; it is structural precedent, not evidence for these AI weights.

## Recommendations, blockers, and omissions

No weight change is recommended from this bounded evidence. Keep the Mengele scores aligned with the existing Kruger pair unless complete analyzer evidence or a parent design decision supports a change. Eligibility remains unresolved across provider branch/idea gates, unlock and site-need helpers, construction receipts, payment checks, and actual state-target enumeration. The comparison remains blocked because the historical before-source file is absent; the earlier before=null diagnostic was "Invalid input: expected object, received null at before". Do not infer a before/after result from source parity.

Skipped analyses: probability_sweep was outside this bounded correction and cannot resolve the four evaluator uncertainties without a broader declared pool. The one probability_render request failed with PROBABILITY_ANALYSIS_NOT_CACHED and was not retried. Historical compare was not retried because its before-source is absent. No gameplay edits, staging, commits, or live-game runs were made; only this handoff was updated.
