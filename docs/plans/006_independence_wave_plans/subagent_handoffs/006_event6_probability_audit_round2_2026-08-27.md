# Event 006 bounded weighted-logic audit — 2026-08-27

## Disposition

**MCP-BLOCKED / CURRENT ENGINE CONCLUSIONS UNRESOLVED.** This was a bounded read-only audit of the current checkout, and no gameplay, AI, event, decision, mission, strategy, random-list, focus, localisation, country, asset, or runtime file was changed.

No balance patch is authorized by this handoff.

## References reviewed

I read AGENTS.md, .agents/skills/chaos-redux-subagents/SKILL.md, .agents/skills/chaos-redux-events/SKILL.md, .agents/skills/chaos-redux-decisions-missions/SKILL.md, and .agents/skills/chaos-redux-mtth/SKILL.md.

I read the required offline wiki pages in paradox_wiki/: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.

I read the relevant vanilla documentation in C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\: script_concept_documentation.md, triggers_documentation.md, effects_documentation.md, modifiers_documentation.md, dynamic_variables_documentation.md, and script_collection_input.md.

The current source-of-truth map was docs/plans/006_independence_wave_plans/006_source_of_truth_map.md, and the prior probability control handoff was subagent_handoffs/006_event6_probability_audit_round2_2026-08-24.md.

The wiki and vanilla documentation distinction used here is material: ai_will_do and focus AI are willingness score races, ai_chance is probability-proportional event-option sampling, and random_list is probability-proportional sampling only after the complete valid pool is known.

## Audited surfaces and current source fingerprints

| Surface | Current source authority | Read-only source census |
| --- | --- | --- |
| Allocator/package pool | common/scripted_effects/006_independence_wave_effects.txt, common/scripted_effects/006_independence_wave_package_planner_effects.txt, common/scripted_effects/006_independence_wave_package_region_effects_registry.txt, and common/script_constants/006_independence_wave_constants_registry.txt | The merged allocator authority exposes one random_list in 006_independence_wave_effects.txt, fourteen regional random_list blocks in the region registry, and the candidate weight calculation in the planner. The former 006_independence_wave_package_allocator_effects.txt path is absent. |
| Root and support event options | events/006_independence_wave.txt and events/006_independence_wave_support_events.txt | The root has 11 ai_chance blocks and 20 option IDs; the merged support-event registry has 136 ai_chance blocks. |
| Shared decisions | common/decisions/006_independence_wave_shared_decisions.txt | The current merged shared file has 14 ai_will_do blocks. |
| Package decision/mission scores | common/decisions/006_independence_wave_decisions.txt, common/decisions/006_independence_wave_frontier_decisions.txt, and common/decisions/006_independence_wave_siberian_decisions.txt | The main decision file has 67 ai_will_do blocks. The KUB founding mission is independence_wave_kub_hold_mounted_compact_together; the TAT founding mission is independence_wave_tat_hold_river_compact_together. |
| AI strategy factors | common/ai_strategy/006_independence_wave_ai_strategy_registry.txt | The registry has 724 ai_strategy = { ... } blocks. These are additive strategy values with enable and abort predicates, not a normalized candidate pool. |

Current local SHA-256 fingerprints are:

| File | SHA-256 |
| --- | --- |
| events/006_independence_wave.txt | 206631AD2C4A56375112A144BB9D178C06A9623E1D2E8444B43CE8B27C54027F |
| events/006_independence_wave_support_events.txt | F8DB738666DC14003DC3240DD027DA3DDD8EC3F67EE85465B9C8F580B4265021 |
| common/scripted_effects/006_independence_wave_effects.txt | 8F2C907541C7BE5CE693D1C411642BB2F87FD9D980473A99DBB3DA16C1067E50 |
| common/scripted_effects/006_independence_wave_package_planner_effects.txt | 41A10C557224F11749C08CA8B97DB965222FC1826CA1F7DD581ECE3B4DFE3D44 |
| common/scripted_effects/006_independence_wave_package_region_effects_registry.txt | 2C309B2400D987B93C45159699A1A936FD4FECF7D3E883978E288E854A941728 |
| common/decisions/006_independence_wave_shared_decisions.txt | 1F5787C3C2BB3A92E9C914CF1148270A0BD7E96556FF49DC7EC6C3A8BC8F682C |
| common/decisions/006_independence_wave_decisions.txt | 030F3605F6E5EB3EAD306FC51FC3EEA9F7721BFC72EFA3DBF9CBB9C281259635 |
| common/ai_strategy/006_independence_wave_ai_strategy_registry.txt | C8AEC1A0E8FC67600F43FE7FB1E539D4B3AE6CCC2277023341B5D5491B6C678F |

Source-only constants visible in the current files are the automatic count ladder 3/4/5/7/10/10 for Calm, Gathering, Rising, Chaos Tier, Totalen, and World Collapse, respectively.

The source-declared allocator weight components are base 100, sponsored candidate +100, registered tag +25, new region +30, new host +20, prior package -80, prior region -25, prior host -20, signature at low chaos -35, high-chaos +45, minimum 1, and World Collapse rarity multiplier 1.35.

The source-declared shared decision score constants are blocked 0, very low 2, low 5, standard 10, high 25, urgent 100, with half, double, and major modifiers 0.5, 2, and 5.

These values are source declarations only. No current MCP modifier trace or normalized selection result was produced.

## Mandatory MCP calls and exact results

The HOI4 MCP workspace was mod_chaos_redux_ea3b2d67c2c0.

1. The required first call, hoi4.probability_inspect({}), returned status = ok, code = PROBABILITY_ADAPTERS_LISTED, adapters = 11, candidates = 0, availableCandidates = 0, availableAdapters = [], no blockers, validation passed, and no artifacts.
2. hoi4.probability_inspect with adapter custom_weighted_pool and the retired path common/scripted_effects/006_independence_wave_package_allocator_effects.txt returned status = error, code = PROBABILITY_SOURCE_NOT_FOUND, and the exact message Probability source path was not found; no artifact, source revision, source hash, or analysis was returned. This is path-drift evidence, not a current allocator result.
3. hoi4.probability_inspect with adapter custom_weighted_pool and current source common/scripted_effects/006_independence_wave_effects.txt returned status = error, code = ARTIFACT_MANIFEST_INTEGRITY_FAILED, artifactCount = 0, empty filesScanned, empty artifacts, validation failed, and the exact blocker message Artifact provenance manifest does not match its immutable address.
4. hoi4.probability_inspect with adapter event_option_ai_chance and current source events/006_independence_wave.txt returned the same ARTIFACT_MANIFEST_INTEGRITY_FAILED status and exact blocker message, with artifactCount = 0 and no scanned files or artifacts.
5. hoi4.probability_inspect with adapter event_option_ai_chance and current source events/006_independence_wave_support_events.txt returned the same ARTIFACT_MANIFEST_INTEGRITY_FAILED status and exact blocker message, with artifactCount = 0 and no scanned files or artifacts.
6. hoi4.probability_inspect with adapter decision_ai_will_do and current source common/decisions/006_independence_wave_shared_decisions.txt returned the same ARTIFACT_MANIFEST_INTEGRITY_FAILED status and exact blocker message, with artifactCount = 0 and no scanned files or artifacts.
7. hoi4.probability_inspect with adapter mission_ai_will_do and current source common/decisions/006_independence_wave_decisions.txt returned the same ARTIFACT_MANIFEST_INTEGRITY_FAILED status and exact blocker message, with artifactCount = 0 and no scanned files or artifacts.
8. hoi4.probability_inspect with adapter ai_strategy_factor and current source common/ai_strategy/006_independence_wave_ai_strategy_registry.txt returned status = ok, code = PROBABILITY_SOURCE_DISCOVERED, and one artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/43aca06d5c3833b9f939906398346c2a889590e3dc29e17960490801716e3551/291a9b75f2871d660f965be5d2ef5c375ffc8163306f21ce0171a43ada1de3c1/probability-inspect-a35190937fed.json. The returned source revision was 2375381d0e0468efccef10c185078eeba27ce904e1052220b39cef5d8758f447, source hash a35190937fed7a0e7a3e156244ad0dbac468bdc2c0c05366da6cce0d3d482396, discoveryReason = no_weighted_surfaces, candidates = 0, availableCandidates = 0, requiredInputs = 0, and unresolved = 0. This proves only that the current adapter did not expose a supported normalized strategy surface; it is not a score or balance result.
9. The matching structural call, hoi4.event_inspect lint for selector {kind: event, eventId: chaosx.nr6.1} with bounded downstream expansion, returned status = error, code = ARTIFACT_MANIFEST_INTEGRITY_FAILED, the exact blocker message Artifact provenance manifest does not match its immutable address, and no artifacts.

Because the current allocator, event, decision, mission, and structural qualification calls failed before source analysis, no hoi4.probability_evaluate, hoi4.probability_sweep, hoi4.probability_compare, hoi4.probability_render, hoi4.probability_simulate, or hoi4.probability_sequence call was made after the failure.

No current scenario hash, analysis ID, comparison ID, source revision, or rendered evidence exists for the failed surfaces.

## Named scenarios and completeness

The following exact scenario names are retained from the current Event 006 audit contract and are listed as required control IDs, not as current results.

| Surface and scenario set | Named scenarios | Candidate pool and external-factor completeness | Classification |
| --- | --- | --- | --- |
| Allocator/package pool — E6_ALLOCATOR_LADDER_2026_08_24 | ALLOC_UNIFORM_COMPLETE, ALLOC_CALM_3, ALLOC_RISING_5, plus target-count cases 3, 4, 5, 7, 10, and World Collapse 10 | The 14 outer region keys and nested package candidates are source-known, but the current MCP did not accept a complete pool containing all current package IDs, attestation state, earliest bands, hosts, anchors, sponsorship, novelty, prior-wave arrays, collisions, optional-expansion state, cadence, and terminal rules. | Unresolved; no normalized probability, rank, timing, dominance, starvation, or repetition claim. |
| Root options — E6_ROOT_OPTION_MATRIX_2026_08_24 | E6_CORE_EMPTY_CURRENT_2026_08_24, E6_SHARED_DECISION_EMERGENCY_2026_08_24, E6_SHARED_DECISION_PROVISIONAL_2026_08_24 | The complete static root option ID list is chaosx.nr6.2.a, chaosx.nr6.35.a, chaosx.nr6.300.a, chaosx.nr6.301.a, chaosx.nr6.301.b, chaosx.nr6.301.c, chaosx.nr6.302.a, chaosx.nr6.302.b, chaosx.nr6.302.c, chaosx.nr6.303.a, chaosx.nr6.303.b, chaosx.nr6.304.a, chaosx.nr6.304.b, chaosx.nr6.304.c, chaosx.nr6.305.a, chaosx.nr6.306.a, chaosx.nr6.307.a, chaosx.nr6.308.a, chaosx.nr6.311.a, and chaosx.nr6.311.b. The 11 ai_chance candidates are the .301, .302, .303, and .304 options; helper validity, route, host, target, league, patron, ownership, capacity, recognition, and instability state were not typed into MCP. | Unresolved ai_chance; no event-option probability or invalid-option exclusion claim. |
| Shared decisions — E6_SHARED_DECISION_EMPTY_2026_08_24 and E6_SHARED_DECISION_NUMERIC_MATRIX_2026_08_24 | Empty, emergency, provisional, low/high capacity, low/high recognition, and low/high instability fixtures | The shared source contains 14 score blocks, but candidate availability, package identity, capital, host, costs, ledgers, resources, war, cooldown, and external modifiers were not accepted by MCP. | Unresolved score race; source constants are not click probabilities. |
| KUB package mission — E6_KUB_MISSION_MATRIX_2026_08_24 | KUB_FRAGILE_PEACE, KUB_SEVERE_HOST_WAR for independence_wave_kub_hold_mounted_compact_together in common/decisions/006_independence_wave_frontier_decisions.txt | The source mission has activation, setup, capital/control, former-host, route, and timeout/cancellation gates, but no complete runtime candidate pool or external state was accepted. Its available = { always = no } line is not evidence of a probability of zero. | Unresolved score race. |
| TAT package mission — E6_TAT_MISSION_MATRIX_2026_08_24 | TAT_FRAGILE_PEACE, TAT_SEVERE_HOST_WAR for independence_wave_tat_hold_river_compact_together in common/decisions/006_independence_wave_siberian_decisions.txt | The source mission has the corresponding setup, capital/control, former-host, route, and timeout/cancellation gates, but no complete runtime candidate pool or external state was accepted. | Unresolved score race. |
| Focus/strategy companion contexts — E6_FOCUS_ROUTE_RACE_2026_08_24 | FOCUS_OPEN_CALM, FOCUS_HOST_CRISIS, FOCUS_ROUTE_LOCKED, and FOCUS_NO_VALID_ROUTE | These are focus-route control contexts, not a dedicated strategy probability scenario. The strategy inspect returned no_weighted_surfaces, so no active/additive/aborted factor trace is available in any context. | Unresolved strategy surface. |
| Evolution timing — E6_EVOLUTION_MTTH_MATRIX_2026_08_24 | Base, chaos-tier, network-thin, and network-dense timing states | No current MTTH probability inspect was attempted after the allocator qualification failed; date, active-country count, chaos flags, and MTTH distribution inputs remain untyped. | Unresolved timing. |

## Findings and risk boundary

The automatic ladder and source-declared allocator modifiers are exact source observations only, not engine-backed probability evidence.

The nested allocator is stateful and recomputes novelty and prior-wave memory before each draw, so a static one-shot normalization would not prove campaign selection behavior.

Root event options are ai_chance sampling, while decisions, missions, focus choices, and strategy factors are score or additive-factor surfaces; these quantities must not be normalized or compared as if they were the same probability.

Positive weights on dead, hidden, blocked, or route-incompatible choices remain unresolved because the current MCP did not evaluate validity gates and external state.

Dominance, starvation, rank reversal, timing drift, repetition, cooldown/recovery behavior, cap handling, terminal behavior, and unsafe snowball risk remain unresolved.

No current MCP result authorizes changing any numeric constant, event ai_chance, decision or mission ai_will_do, strategy factor, random-list weight, MTTH value, candidate gate, or pool membership.

## Recommended owner follow-up without applying a patch

1. Repair the artifact provenance manifest or MCP transport, then repeat source-qualified hoi4.probability_inspect on the current authorities listed above.
2. Re-run E6_ALLOCATOR_LADDER_2026_08_24 with all 14 outer entries, every current candidate, attestation, earliest-band, host/anchor, novelty, previous-wave, sponsorship, collision, optional-expansion, cadence, and terminal state declared.
3. Re-run E6_ROOT_OPTION_MATRIX_2026_08_24 with all 20 root option IDs retained and every helper validity input typed, including zero-available options.
4. Re-run E6_SHARED_DECISION_EMPTY_2026_08_24, E6_SHARED_DECISION_NUMERIC_MATRIX_2026_08_24, E6_KUB_MISSION_MATRIX_2026_08_24, and E6_TAT_MISSION_MATRIX_2026_08_24 with complete candidate pools and route, prerequisite, resource, capital, host, former-host, ledger, patron, and terminal state.
5. Re-run probability_sweep only after inspect/evaluate accepts the complete pool, and use probability_compare with the same named scenarios only after an owner-applied candidate change exists.
6. Use probability_sequence only after cadence, cooldown, recovery, removal, reset, cap, retry, replacement, and terminal transitions are declared.

## Historical artifacts retained for parent review

The following older artifacts are preserved as historical capability and fixture evidence only and are not relabelled as current results: allocator inspect hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/51ba0f1ca30228868d32e098eccf06028b6af9d4fff0b88996c9cac8c026765d/a6337fa215e774e3109e3ad2a27dc907af3a20bc638f2f1b330340675d6e7387/probability-inspect-bc6f7ff8598d.json at prior source revision 3771942e4d960525d9213bb00bc6d4e257650cc3f466c5aba0920128723f67d8, allocator analysis probability-820fc7081d76f1373d2ed61d with prior scenario hash 68b32e03267da5726b7df85f725bc57a61e7ef2adafb27488351b60bfa37c4fc, root-option analysis probability-e9dbbb5097d2250d656746df with scenario hash c2e87adec18afe6a1068492c3e2c31f2d51d7798a05a75407a3dc362da750703, and focus partial analysis probability-5157df1afa15b89c3fa9403f with scenario hash 2f723739b3836a436a5b314738e798c5da8b2a6b2185a8c7658df27c949704b3.

Those historical records do not establish current source parity, current candidate validity, current probability, or current balance.

## Skipped analyses and blockers

probability_evaluate, probability_sweep, probability_compare, and probability renders were skipped because the required current source qualification failed with ARTIFACT_MANIFEST_INTEGRITY_FAILED, and the strategy source exposed no supported weighted surface.

probability_simulate was skipped because no uncertain-input distribution, correlation model, seed, or horizon was declared.

probability_sequence was skipped because no complete current custom-pool cadence and state-transition manifest was accepted.

No gameplay patch, numeric tuning choice, balance target, or commit was applied.
