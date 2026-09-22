# IW-179 FSM decision probability audit

Date: 2026-09-22

Disposition: read-only audit complete with partial MCP evidence; no gameplay patch authorized or applied.

## Scope and audited source

The audited source is `common/decisions/006_independence_wave_pacific_decisions.txt`, category `independence_wave_fsm_micronesia_category`, with the following eight actual source candidates:

- `independence_wave_fsm_convene_inter_island_revenue_congress`
- `independence_wave_fsm_establish_patrol_relay_network`
- `independence_wave_fsm_settle_external_administration_accounts`
- `independence_wave_fsm_ratify_federal_council_compact`
- `independence_wave_fsm_confirm_traditional_leaders_council`
- `independence_wave_fsm_adopt_inter_island_constitution`
- `independence_wave_fsm_accept_protected_ocean_mandate`
- `independence_wave_fsm_ratify_autonomous_federation_mandate`

The requested final identifier omitted `_fsm_`; the source and MCP candidate pool use `independence_wave_fsm_ratify_autonomous_federation_mandate`. The omitted-prefix identifier was not silently treated as an alias.

Relevant source locations are the category at line 287 and decision blocks at lines 302, 318, 334, 350, 366, 382, 398, and 418 respectively. The final block ends at line 442.

The parent-described bounded changes were treated as current facts: the four route-government decisions require the FSM inter-island authority receipt at 60 or higher, the final mandate requires stable FSM setup plus recognized-or-later state, and receipt loss cancels all eight ordinary FSM timed decisions through the setup-complete receipt predicate. No AI target was assumed or selected.

## Required references consulted

The audit used `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, and `.agents/skills/chaos-redux-decisions-missions/SKILL.md`. The offline wiki references consulted were `Data structures`, `Triggers`, `Effects`, `Modifiers`, `Localisation`, `Scopes`, `On actions`, `Event modding`, `Decision modding`, `Idea modding`, and `AI modding`. The vanilla documentation references consulted were `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md`, `triggers_documentation.md`, and `modifiers_documentation.md`.

## MCP inspection and artifacts

The required first call was `hoi4.probability_inspect`.

The first two schema errors were retained as workflow evidence:

```text
MCP error -32602: Input validation error: Invalid arguments for tool hoi4.probability_inspect: An adapter requires a source; provide a source alone to discover compatible adapters
```

After supplying a source object, not a string, the next exact error was:

```text
MCP error -32602: Input validation error: Invalid input: expected object, received string at source
```

The successful inspect used `source = { path = "common/decisions/006_independence_wave_pacific_decisions.txt" }` and discovered that this source is parsed by the live adapter as `mission_ai_will_do`, not `decision_ai_will_do`. The corrected inspect used the exact eight source IDs above.

Connected server and adapter evidence from the successful inspect:

- Game target: Operation Postern 1.19.2.0 (d245).
- Observed raw version: 1.19.2.0.
- Observed version: Operation Postern v1.19.2.0.a729 (d245).
- Checksum: d245.
- Adapter version: `hoi4-1.19.2.v1`.
- Workspace status: `workspace_verified`.
- Workspace ID: `mod_chaos_redux_ea3b2d67c2c0`.
- Capabilities: eligibility and raw score available; normalized probability, sequence analysis, and time distribution unavailable.
- Selection rule: `score_only`.
- Modifier order: base expression, source add/factor/modifiers in source order, then declared external factors.
- Evaluation cadence: mission-AI cadence; selection probability is not modeled.
- Source revision: `e0a3bc903780766d09b6c5b7c0c3a48a1351f523693de973ce79c4e5256abf9c`.
- Inspect source hash reported by the adapter: `85c7f7ca3eb4560584739762a9b2afb1beb813ebfbb6926742c0aa7188d13a7f`.
- Per-candidate provenance/local source file hash reported in the artifact: `a1c5676b1d4ed50daebc29582fdff423ea26f6b3b905f49c4c1461e94fb03685`.

The corrected inspect reported `poolComplete: true`, eight candidates, zero currently available candidates because no typed live runtime state was supplied, fifteen required inputs, and zero inspect-time unresolved inputs. Its artifact is:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3864fbcbf3fb1a8489bba57e1a3bd1b07984f7d9cabcc811b150038e701ae66a/ea55767bd8092bd8e4e57d79a259938d842fd397300eae8e24baf69b3a3c9714/probability-inspect-85c7f7ca3eb4560584739762a9b2afb1beb813ebfbb6926742c0aa7188d13a7f.json`

The preceding discovery inspect, which deliberately used the requested-but-nonexistent final ID, found 28 mission candidates and only 7 pool matches. Its artifact is:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/809604cc0e43092fcf7a07778d30b54fe3bcb967c14915425bb8232b167d173e/7fe7862778977d6abd051856e4ebe87b7799d523c65e340a6f15acb1a6bc64dc/probability-inspect-85c7f7ca3eb4560584739762a9b2afb1beb813ebfbb6926742c0aa7188d13a7f.json`

The discovery artifact URI above is retained as returned by MCP; the corrected inspect is the authoritative candidate-pool artifact.

## Scenario contract and completeness

The live scenario contract accepted only `scenarioSet = { id, scenarios = [{ id, actor: string, state: flat primitive map, flags: string[], scopes: record of { id, state: primitive map } }] }`. No fixture, variable declaration, trigger override, or other invented key was supplied.

The evaluation scenario set ID was `IW179_FSM_AI_2026_09_22`. All scenarios used actor `FSM`, flat primitive state values, flags, and scope records for the FSM root, capital state 684, the setup anchor target, and former host USA.

| Scenario ID | Intended state | Static candidate pool | Active runtime pool and external factors |
| --- | --- | --- | --- |
| `IW179-EARLY-UNDER-AUTHORITY` | FSM setup before the 60-point inter-island authority receipt threshold | Complete: all 8 source candidates supplied | Incomplete and unresolved because Clausewitz variables, compound triggers, active-mission/decision state, event targets, and route eligibility did not bind from the flat scenario fields |
| `IW179-AUTHORITY-ROUTES-OPEN` | Authority receipt at or above 60 with route-government gates intended to be open | Complete: all 8 source candidates supplied | Incomplete and unresolved for the same typed-binding limits; route availability was not proven by MCP |
| `IW179-RECOGNIZED-HOSTILE-PATRON` | Recognized-or-later FSM with hostile former-host pressure and patron dependency intended | Complete: all 8 source candidates supplied | Incomplete and unresolved; patron dependency and severe-host-threat scripted predicates did not bind as complete external factors |
| `IW179-RECOGNIZED-HOST-COLLAPSE` | Recognized-or-later FSM with former-host collapse intended | Complete: all 8 source candidates supplied | Incomplete and unresolved; host-collapse state and the final mandate's compound visibility/AI predicates did not bind as complete external factors |

The static pool is therefore complete for the declared selection race, but no scenario proves the complete active eligible pool. These are point scenarios, not sampled campaigns, and no exact click probability can be derived from them.

## Probability evaluation and rendered evidence

`hoi4.probability_evaluate` ran with the eight-candidate pool, the source object above, and the four named scenarios. The result was `PROBABILITY_ANALYZED_PARTIAL` with status `ok`, analysis ID `probability-bfc09a5c5f4068e61b6d870f`, scenario hash `edbb862ecbd791db41af1605e83d35a247591f272272b322e41f2cb6cddf9aa`, four scenarios, 32 candidate/scenario rows, and 273 unresolved items.

The evaluation diagnostics were eight total. Seven `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` warnings covered `independence_wave_fsm_accept_protected_ocean_mandate`, `independence_wave_fsm_adopt_inter_island_constitution`, `independence_wave_fsm_confirm_traditional_leaders_council`, `independence_wave_fsm_convene_inter_island_revenue_congress`, `independence_wave_fsm_establish_patrol_relay_network`, `independence_wave_fsm_ratify_autonomous_federation_mandate`, and `independence_wave_fsm_ratify_federal_council_compact` across the supplied scenarios. `independence_wave_fsm_settle_external_administration_accounts` was not in that compact never-eligible warning set. The remaining diagnostic was `PROBABILITY_MODIFIER_UNSATISFIED_IN_SCENARIOS` for the patrol relay network's severe-host-threat double factor; the hostile scenario did not activate that modifier through the typed adapter bindings.

The rendered matrix shows raw score values of 25 for `independence_wave_fsm_settle_external_administration_accounts` and 0 for the other seven candidates in all four supplied rows. The ranking render for `IW179-EARLY-UNDER-AUTHORITY` likewise ranks settle-external first at 25 and the other seven at 0. This is score-only evidence from a partial analysis, not a selection probability, and the zeroes must not be interpreted as proof that those choices are impossible in the game.

Evaluation JSON artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4a3daaad7f38e43cb8997c54814fd1d208fa833d02dbfed1d4c7ffca6931b236/26e126226b8730076624db2676c60e0950b39a8ceee77446e22f3bae15593a79/probability-bfc09a5c5f4068e61b6d870f.json`

The subsequent `hoi4.probability_render` used the same analysis ID and expected scenario hash and returned `PROBABILITY_ANALYZED_PARTIAL` with the same 273 unresolved items. Rendered evidence:

- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9b2d4496375082b3a16d5f6526512373f403cb80cbb9c557bf656544f44e5701/937394e99f9b10feaedf92eb6862854527de481aaf3a339fe2e2deb6330e2b2a/probability-bfc09a5c5f4068e61b6d870f.json`
- Ranking SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4b6f7adcc3371bfc1ffd5bd8407eabdce3e46c6a65a938a9fe452da87089ef8e/0bbb11263678d0a0e73dab2d8d8a9680b7861efcab2ac78e892af5390f017645/probability-probability-bfc09a5c5f4068e61b6d870f-ranking.svg`
- Ranking PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4bfdfc2f66e5cbe6db6dde5b0eaf9fbfbd3959380a73bf78ec77465cc8e82d9e/f17b441f7b9820a1be43dd38a5677e000cdb6a22a3317ec5802fdb8d90be91a3/probability-probability-bfc09a5c5f4068e61b6d870f-ranking.png`
- Matrix SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/51b6730f99621d8803bc45edab3518a2e4a59ff89113a91c36669f2e9db866af/fd0d84dabe84a12d0bde3d4c4340b0e7c13a79de6765ad4dde5faa221eaccef5/probability-probability-bfc09a5c5f4068e61b6d870f-matrix.svg`
- Matrix PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0ad33c868b4810b5e3e2a25b6362df2f07e7d134b3ddea0abd1b6e68a397fa96/e1cc3c966adafc66c539791b2e7e39af9a9208b8bb5f0fdca954b21f13a1fa45/probability-probability-bfc09a5c5f4068e61b6d870f-matrix.png`
- Unresolved SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b33c9bb9d37fd4c8e777324e5f1d58dbb722a001ab6f0553ecfe1cd37f058a6b/5716d94e5ec36788b70d360991b15c7e95d07684e81a4238af1f76152f8db5b9/probability-probability-bfc09a5c5f4068e61b6d870f-unresolved.svg`
- Unresolved PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3a63fec8b62e10dd55301daced42ad969ff82157a50ceb946a297e05ebe0258e/87f418dcb76562bb2842010fc2c57c66d66a873d805b57823f798504db1286d5/probability-probability-bfc09a5c5f4068e61b6d870f-unresolved.png`

## Source score surface, kept distinct from probability

The following are exact source-score values after substituting the current constants from `common/script_constants/006_independence_wave_constants_registry.txt`. They are classified as `score-only`, not balance or probability evidence.

| Decision | Base score | Conditional factors | Score ladder |
| --- | ---: | --- | ---: |
| Convene revenue congress | `urgent = 100` | none | 100 |
| Establish patrol relay network | `high = 25` | `modifier_double = 2` under severe host threat | 25 or 50 |
| Settle external administration accounts | `high = 25` | none | 25 |
| Ratify federal council compact | `high = 25` | none | 25 |
| Confirm traditional leaders council | `low = 5` | none | 5 |
| Adopt inter-island constitution | `standard = 10` | none | 10 |
| Accept protected ocean mandate | `very_low = 2` | `modifier_major = 5` for severe host threat and independently for patron dependency | 2, 10, or 50 |
| Ratify autonomous federation mandate | `low = 5` | `blocked = 0` unless host collapse or HBX host-collapse state; `modifier_major = 5` when host collapse is present | 0 or 25 |

The ladder shows a potential early dominance pattern for the urgent revenue-congress decision and a potential final-mandate starvation pattern, but it does not establish selection odds because the adapter reports `normalizedProbability: false`, uses `score_only`, and does not model selection probability or time distribution.

## Findings by decision and route

### Early FSM setup

`independence_wave_fsm_convene_inter_island_revenue_congress` is scored at 100 and is eligible only through its normal FSM package, capital, cost, and no-active-project gates. If it remains in the eligible pool, its score is four times the unmodified high-score actions and twenty times the traditional-council score. This is a dominance risk to validate, not a tuning target; the supplied MCP states did not prove the complete early pool.

`independence_wave_fsm_establish_patrol_relay_network` is high at 25 and doubles to 50 under `has_independence_wave_severe_host_threat = yes`. The MCP explicitly reported that its severe-host-threat modifier was unsatisfied in every supplied scenario, so the 50 branch remains unresolved. Its source availability and cancellation gates include the FSM package, capital control, no active project, and setup receipt continuity.

`independence_wave_fsm_settle_external_administration_accounts` is high at 25 and was the only candidate shown as nonzero by the partial matrix, at 25 in all four rows. Its source `available` block does not require capital control, unlike the other ordinary FSM actions, while its cancellation predicate checks package/setup/former-host continuity. This may be an intentional external-administration exception, but it is a route-validity or exploit-risk proposal for parent review because the AI can potentially select it after capital control is lost if the other gates remain true.

### Route-government decisions

The federal-council, traditional-leaders, inter-island-constitution, and protected-ocean decisions are gated by stable FSM inter-island authority and route-specific availability, with the parent-described 60-point receipt threshold controlling visibility. The source also serializes FSM work through the active-project trigger and the route-selection guards, which is a positive anti-repetition and anti-concurrency property.

Their AI scores are 25, 5, 10, and 2 respectively before conditional factors. Protected ocean rises to 10 under either severe host threat or patron dependency and to 50 when both factors hold. The partial MCP evaluation marked federal, traditional, constitution, and protected as never eligible in the supplied scenarios, so no route ranking or modifier activation was proven. This is unresolved adapter evidence, not proof of dead source logic.

### Final autonomous federation mandate

The actual final decision ID is `independence_wave_fsm_ratify_autonomous_federation_mandate`. Its visibility requires stable FSM setup, recognized-or-later state, and that delegation is not already ready, but its AI score is blocked at zero unless host collapse is present, then rises to 25. This creates a clear source-level visibility/AI mismatch if the intended AI behavior is to complete a recognized, stable FSM without waiting for host collapse: the choice can be visible yet receive no positive AI score. The mismatch is a concrete proposal for parent review, not an approved target.

The parent should choose whether the final mandate is intentionally reserved for host-collapse play or should receive a positive non-collapse branch. If changed, the owner must rerun the same named scenarios and a post-patch `hoi4.probability_compare`; no source patch is made by this audit.

### Cancellation, costs, and timing context

The receipt-loss repair is consistent with the stated scope: all eight ordinary FSM timed decisions use setup-complete receipt continuity in their cancellation logic. Costs, durations, and no-active-project serialization were not treated as AI weights. The MCP adapter exposes neither a complete timing distribution nor a sequence model, so repetition rate, completion timing, cooldown interaction, and campaign cadence remain unresolved.

## Risk classification

- AI validity: partially evidenced. The source candidate pool is complete, but active eligibility is not because required Clausewitz state did not bind.
- Dominance: score-only concern. Revenue congress at 100 can dominate high/standard/low choices whenever concurrently eligible.
- Starvation: unresolved in runtime, with a source-level concern that the final mandate is zero outside host collapse despite recognized-or-later visibility.
- Rank reversal: unresolved because the hostile-threat, patron-dependency, route, and host-collapse predicates did not bind in the partial evaluation.
- Repetition and cadence: unresolved because the adapter reports `sequence: false` and `timeDistribution: false`, and no complete custom pool cadence was declared.
- Exploit/validity: review whether settle-external intentionally lacks capital-control availability and capital-loss cancellation; do not infer a defect without the intended route contract.
- Probability interpretation: no result in this report is a click probability. The only MCP values are raw willingness scores under a partial, score-only adapter.

## Skipped validation and exact limitations

`hoi4.probability_sweep` was not run in the close-out. The live scenario contract accepts only flat primitive state, flags, and `{id, state}` scope records, while the required threshold and sensitivity dimensions are Clausewitz variables and compound scripted predicates that the evaluate call left unresolved. Adding fixture, variable-declaration, trigger-override, or range keys would violate the live schema and invent runtime bindings. Therefore threshold crossings, sensitivity ranges, and rank reversals are unresolved rather than approximated.

`hoi4.probability_compare` is not applicable because this task contains no authorized AI source patch or before/after candidate. It was intentionally not called.

`hoi4.probability_simulate` was skipped because no uncertain input distribution or seed was explicitly declared and the adapter does not expose a complete normalized selection model for this surface.

`hoi4.probability_sequence` was skipped because no complete custom pool manifest, cadence, state-transition table, or terminal-state contract was supplied, and the live adapter reports sequence analysis unavailable.

No separate decision-specific structural MCP inspector or renderer was exposed in the connected tool surface. The weighted-source probability path was used; no event-chain structural pass was required for this decision-score audit.

The inspect artifact's exact fifteen-input union was `HBX`, `capital_scope`, `check_variable`, `command_power`, `event_target:independence_wave_setup_anchor_state`, `event_target:independence_wave_setup_former_host`, `exists`, `has_active_mission`, `has_decision`, `has_equipment`, `has_manpower`, `has_stability`, `has_variable`, `original_tag`, and `var:independence_wave_former_host`. The main typed-schema limitation is the inability to bind these Clausewitz variables, event-target scopes, and compound scripted triggers from the permitted scenario shape. The evaluate artifact records 273 unresolved items. No source-only conclusion is promoted to exact probability evidence.

## Explicit no-patch conclusion

No gameplay source, AI weight, prerequisite, route gate, cost, duration, cancellation rule, localisation, or runtime file was edited. Only this handoff report is being written. The audit provides exact source-score ladders and partial MCP raw-score artifacts, but it does not approve a target or prove normalized selection probabilities. Parent review is required before any proposed final-mandate, settle-external, or dominance-related tuning change is considered.
