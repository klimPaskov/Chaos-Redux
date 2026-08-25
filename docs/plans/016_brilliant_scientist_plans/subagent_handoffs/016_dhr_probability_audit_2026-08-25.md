# Event 016 D’Rhondan weighted-logic audit — 2026-08-25

Status: partial, read-only, and not a balance certification.

No gameplay, AI, event, focus, decision, mission, technology, doctrine, localisation, or runtime file was edited by this audit.

The parent-requested audit was stopped after the current random-list and decision/mission evidence was captured, so the unrun surfaces and exact MCP blockers remain explicit below.

## Scope and source boundary

The audited Event 016 weighted surfaces are:

- `common/decisions/016_dhrondan_contact_decisions.txt` (`dhrondan_send_kruger_to_dhronda`, `dhrondan_send_mengele_to_dhronda`, `dhrondan_honor_accord`, and the expedition/rebellion missions).
- `common/decisions/016_alien_infantry_landing_decisions.txt` (`alien_infantry_call_landing` and its seven-day reservation mission).
- `common/scripted_effects/016_dhrondan_contact_effects.txt` (`dhrondan_resolve_rebellion_pulse`, the automatic expedition authorizer, and the deterministic Kruger-first route helper).
- `common/scripted_triggers/016_dhrondan_contact_triggers.txt` and `common/scripted_triggers/016_alien_infantry_api_triggers.txt` (contact, landing, route, target, and rebellion gates).
- `common/script_constants/016_dhrondan_contact_constants.txt` (the 180/90-day cadences, 6/8/10 arrival thresholds, 30/50 strain thresholds, 600/800 Chaos thresholds, 10/20/40 rebellion weights, and 25/100/10,000 AI scores).
- `events/016_dhrondan_country_events.txt` (`chaosx.nr16.49` diplomatic response options and `ai_chance`).
- `common/special_projects/projects/016_dhrondan_envoy_project.txt` (`sp_dhrondan_envoy_craft`).
- `common/ai_strategy_plans/016_dhrondan_focus_ai.txt` and `common/national_focus/016_dhrondan_focus_tree.txt` (DHR route plans and focus selection).

The accepted scenario contract is `docs/plans/016_brilliant_scientist_plans/016_alien_dhrondan_acceptance_scenarios.md`, supplemented by `docs/specs/016_brilliant_scientist_specs/acceptance/016_acceptance_criteria.md`, `docs/specs/016_brilliant_scientist_specs/matrices/016_ai_behavior_matrix.md`, and `docs/specs/016_brilliant_scientist_specs/matrices/016_decision_mission_map.md`.

The required repository guidance and references were read before the audit: `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-mtth/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, the offline Data Structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, AI focuses, National focus modding, and Technology modding pages, plus the relevant vanilla `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, and `script_concept_documentation.md` files under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`.

## MCP provenance

All completed MCP analyses used workspace `mod_chaos_redux_ea3b2d67c2c0` and game target Operation Postern 1.19.2.0 (d245), adapter version `hoi4-1.19.2.v1` where reported.

The current workspace source revision reported by the successful Event 016 probability calls is `f8c71280728febbf69ebeb808d8b53edc8889b0f32da63208616defeecf7b48d`.

### Mandatory initial random-list inspection

`hoi4.probability_inspect` started the audit with adapter `random_list` and source `common/scripted_effects/016_dhrondan_contact_effects.txt`.

The successful inspection returned `PROBABILITY_SOURCE_INSPECTED`, `poolComplete = true`, two candidates, zero currently available candidates, two required inputs, and zero inspect-unresolved inputs.

The inspect source hash is `4ecd98b765f62b7a2fc88c22fd9c0a461f1722465f80d6ed082b50db505ed86`.

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c72b074d9aeaae47cd2dc9ca6011d099f0b71d2a8289d6a018e6d9d40936f776/09d5f8b16d74cfa31fb7af4fd4c775213fcd79a4694615babc8fc8128b2dfe47/probability-inspect-4ecd98b765f6.json`.

A later refresh of this same inspection timed out after 180 seconds with `tool call error: tool call failed for hoi4_agent_tools/hoi4.probability_inspect: timed out awaiting tools/call after 180s`; the successful initial inspection remains the authoritative current inspect receipt.

### D’Rhondan expedition mission inspection

`hoi4.probability_inspect` with adapter `mission_ai_will_do` on `common/decisions/016_dhrondan_contact_decisions.txt` discovered the Kruger, Mengele, and Honor Accord mission-style blocks.

The inspect returned `PROBABILITY_SOURCE_INSPECTED`, `poolComplete = false`, three candidates, zero currently available candidates, seven required input classes, and zero inspect-unresolved inputs.

The source hash is `4a370bea603b8759a82a054d48def6cc59b821ba28929b5e6f3ab605da32ee94`.

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3b6bad52efe5c36c2f44f9c0a6c8f3b313f09a9d34cf89916457a815c94b95ce/6328d96f90d99757cc84d523c1e72e7c35d1391cfd7e8640310bee42445a6585/probability-inspect-4a370bea603b.json`.

The adapter is score-only with raw-score support and no normalized probability or timing distribution.

### Landing inspection and adapter routing

`hoi4.probability_inspect` with requested adapter `decision_ai_will_do` on `common/decisions/016_alien_infantry_landing_decisions.txt` returned `PROBABILITY_SOURCE_DISCOVERED` with `requested_adapter_empty` and suggested adapter `mission_ai_will_do`.

The discovered candidate is `alien_infantry_call_landing`; the decision adapter itself did not expose this state-targeted decision.

The source hash is `ee65b59c5aebc613eb16d5e63f8819ef7ad89390e5a7cd50e65777b105b0ebfc`.

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4ba5df215c4597dc8b93ed286e3ef8a68f9de8030ef0db45a30451759f9c70bb/c77bf302d219c97c7c01d6cd5f37f42bb13ab7f3d5f0bd7df3da6df2dcd64919/probability-inspect-ee65b59c5aeb.json`.

## Named scenario contract and completeness

The random-list scenario set `DHR_REBELLION_TIERS_2026_08_25` supplied the complete two-entry pool and direct declared temporary weights for the following boundary states.

| Scenario id | Declared revolt weight | Declared no-revolt weight | Completeness classification |
| --- | ---: | ---: | --- |
| `NO_CONTACT_BELOW_6` | 0 | 100 | Complete pool and direct weights; rebellion eligibility gate intentionally not typed, so this is a conditional pool probe rather than proof that the mission can activate. |
| `ARRIVALS_6_CHAOS_600_STRAIN_30` | 10 | 90 | Complete pool and direct weights; exact conditional result. |
| `ARRIVALS_7_CHAOS_799_STRAIN_49` | 10 | 90 | Complete pool and direct weights; exact conditional result. |
| `ARRIVALS_8_CHAOS_600_STRAIN_30` | 20 | 80 | Complete pool and direct weights; exact conditional result. |
| `ARRIVALS_9_CHAOS_799_STRAIN_49` | 20 | 80 | Complete pool and direct weights; exact conditional result. |
| `ARRIVALS_7_STRAIN_50` | 20 | 80 | Complete pool and direct weights; exact conditional result. |
| `ARRIVALS_7_CHAOS_800` | 20 | 80 | Complete pool and direct weights; exact conditional result. |
| `ARRIVALS_10_CHAOS_800` | 40 | 60 | Complete pool and direct weights; exact conditional result. |
| `ARRIVALS_12_CHAOS_900` | 40 | 60 | Complete pool and direct weights; exact conditional result. |

The expedition mission scenario set `DHR_CONTACT_MISSION_BOUNDARIES_2026_08_25` used `KRUGER_VALID`, `MENGELE_VALID`, and `NO_CONTACT` with declared craft completion, route, character, resource, pact, cooldown, and world-end fields.

The mission adapter did not recognize the flat fixture fields as declarations for nested helper dependencies, leaving route, character, special-project, country-identity, `custom_trigger_tooltip`, and numeric strain inputs unresolved.

The landing scenario sets `DHR_LANDING_AI_BOUNDARIES_2026_08_25` and `DHR_LANDING_AI_COMPLETE_RECEIPT_BOUNDARIES_2026_08_25` used `NO_CONTACT`, `BASE_VALID`, and `ALL_LANDING_MODIFIERS` with receipt, equipment, target, and four landing-factor states.

The landing adapter still reported all five receipt variables, `num_equipment@alien_laser_weapon_equipment_1`, and scoped `any_controlled_state` as undeclared, so the target pool and public gate are not MCP-proven.

No scheduled state changes, uncertain-input distribution, seed, custom cadence manifest, or terminal-state sequence was declared for these score/random probes.

## Rebellion pulse random list — exact conditional evidence

The complete candidate pool is `common/scripted_effects/016_dhrondan_contact_effects.txt:359.entry.1` (revolt) and `common/scripted_effects/016_dhrondan_contact_effects.txt:359.entry.2` (no revolt).

The source sets the qualifying low weight to 10, replaces it with 20 for the medium tier, replaces it with 40 for the high tier, and derives no-revolt as 100 minus revolt before entering the two-entry `random_list` at lines 359–367.

`hoi4.probability_evaluate` returned `PROBABILITY_ANALYZED`, analysis id `probability-fedc30a49c5461669eb47b59`, nine scenarios, 18 rows, zero unresolved rows, and four diagnostics.

The source hash is `4ecd98b765f62b7a2fc88c22fd9c0a461f1722465f80d6ed082b50db505ed86` and the scenario hash is `94075e1cecd98fc7c4850396fe680b32938962596cd1cdd7a145a31df2344dcf`.

Authoritative JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dfa838f159810ca6f095235a1cabd42cf180cf5fcbb486ac6deeb0f6e4d66c73/9b7f24f7e1b5706ef83b53d9eed196e42eaeae20cb2a124f3bcac7107506c32c/probability-fedc30a49c5461669eb47b59.json`.

Rendered ranking: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3627dbe1be3cd9dc2af95d6525b55a6443fcedbacd89aaec0466e9e8f2e5e67f/7a83b2f1d6cfd3301a21e8eef31e1fb447d0883e30ce27776337d6d63960da25/probability-probability-fedc30a49c5461669eb47b59-ranking.svg`.

Rendered matrix: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/81bdf51e16e9f36b0b8db1ee467da2ecf821ee19a56fda8aed9a1a42dab7bcfc/c403b40e416d8b68429d913fbd3444562a38fef7f5bd7a4fa67534f64f0b1a76/probability-probability-fedc30a49c5461669eb47b59-matrix.svg`.

Rendered sensitivity: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5b5c9f25c05e945e4802758bf83a6ae6c00e228396e9d6b66826e5e21c99ad27/f63620b16987b158ff0754ceb7f9f6a35a7f588f83f8a0a990a76bd261a656ad/probability-probability-fedc30a49c5461669eb47b59-sensitivity.svg`.

Rendered threshold view: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3a1d04933d4bee944ffe273a6638b17e8217400e7f2a1272f8b890f82789bfc6/1502c4c0e3691122c3e2cc28f600fc69a31a55f44bfaebc72c10c9cc379130db/probability-probability-fedc30a49c5461669eb47b59-threshold.svg`.

Rendered unresolved view: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6cc34de4a6f32afd16a90b09c5631e732e81cfd45199abec74fe2209cf8029b/443e8acd517504f04adcf1e6efea6d55fa28c3055471fff32d40f99bd9ca2ee1/probability-probability-fedc30a49c5461669eb47b59-unresolved.svg`.

The MCP result proves the declared conditional outcomes as 0/100, 10/90, 20/80, and 40/60 in the named rows, with no rank reversal across those tiers.

The 100% no-revolt result in `NO_CONTACT_BELOW_6` and 90% no-revolt results in both low-tier rows triggered dominance warnings, and the 0% revolt row triggered a starvation warning.

Those warnings are expected consequences of the declared tier weights and are not evidence that the source should remove its below-gate guard.

The result is exact for the declared two-entry pool and direct weights, but it is not a campaign-level probability, a cumulative 90-day chance, or a timing distribution because the adapter does not model the mission cadence or the eligibility gate.

The source cadence is a one-country-scoped 90-day pulse mission with cancellation outside the pact/arrival/strain/Chaos gates; that timing and cleanup remain source-backed rather than MCP timing evidence.

## Expedition mission AI — score-only and unresolved eligibility

`hoi4.probability_evaluate` used the complete declared candidate list `{dhrondan_honor_accord, dhrondan_send_kruger_to_dhronda, dhrondan_send_mengele_to_dhronda}` under `DHR_CONTACT_MISSION_BOUNDARIES_2026_08_25`.

The result returned `PROBABILITY_ANALYZED_PARTIAL`, analysis id `probability-b8cebaa477512d4b075e6a36`, source hash `4a370bea603b8759a82a054d48def6cc59b821ba28929b5e6f3ab605da32ee94`, scenario hash `f2a98db3da2f984cb5e3b50312f34f7d96c28a6bb3d1973febfffb8936629326`, three scenarios, nine candidate rows, 11 unresolved items, and eight diagnostics.

Authoritative JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c9fdf89bef67a4c75ee9babac612d6cf66ce2bd688005202e5b2d6e2248cab1d/5a9702299c2b9ca07aea344ea734044492c28383f0f1db454ea7a5989f515b1d/probability-b8cebaa477512d4b075e6a36.json`.

Rendered ranking: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/67ba7f7d024b2c562b3c908443b8faccd14c646b9fa358f34ff7464352edb38f/5c2806d7236d50724ba5f1fb3cb6de726c15fcd0789b3296206834627135a741/probability-probability-b8cebaa477512d4b075e6a36-ranking.svg`.

Rendered matrix: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1c1060abfad4b9be2f38f2cefdc928a3075d88c7a8349e74b3028e1dd9d7c06d/e981bfce2588fb59d6a6f70859ee30faf1cf7a9a2c91de54ba2b0e7ebc7b0bc4/probability-probability-b8cebaa477512d4b075e6a36-matrix.svg`.

Rendered unresolved view: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/82d1506a90f1e34eecbd71aa9448006c988556b0a0b5ba55f9f3529a4c62ee69/1c34a1750006aa5ae8d90de1e391a708ec51454ab316cabc5367a19cf32d1c54/probability-probability-b8cebaa477512d4b075e6a36-unresolved.svg`.

The adapter emitted `PROBABILITY_EXTREME_MODIFIER_GROWTH` for both expedition decisions because the source base of 1 is multiplied to the dominant score 10,000 in the trace.

The source constants make both expedition authorization scores 10,000, so the warning is a real score-race design signal, but it is not a normalized click probability and does not establish which route a valid campaign will select.

The helper `dhrondan_ai_try_authorize_expedition` is source-deterministic and checks Kruger before Mengele when both route predicates pass; this is a first-valid route priority, not a two-way weighted pool.

The MCP marked Kruger and Honor Accord never eligible across the supplied fixtures, but the unresolved helper dependencies (`has_character`, `KRG_warren_kruger`, `exists`, `has_cosmetic_tag`, `is_special_project_completed`, `custom_trigger_tooltip`, and numeric `dhrondan_pact_strain`) mean those diagnostics are not proofs of dead routes.

No exact expedition selection probability, route starvation result, or 180-day success/failure timing distribution is available.

## Alien landing AI — adapter reroute with unresolved target gate

The first landing evaluation used `DHR_LANDING_AI_BOUNDARIES_2026_08_25` and returned `PROBABILITY_ANALYZED_PARTIAL`, analysis id `probability-35d33fd3af1b454f74dd8aef`, source hash `ee65b59c5aebc613eb16d5e63f8819ef7ad89390e5a7cd50e65777b105b0ebfc`, scenario hash `1a4c92a122b2fc104eb229cf5076d1828daf9a8a3c1aed24b7a26611e5bc74df`, one candidate across three rows, seven unresolved items, and four diagnostics.

The follow-up receipt/equipment probe used `DHR_LANDING_AI_COMPLETE_RECEIPT_BOUNDARIES_2026_08_25` and returned `PROBABILITY_ANALYZED_PARTIAL`, analysis id `probability-d7d344df73dc57572483baee`, source hash `ee65b59c5aebc613eb16d5e63f8819ef7ad89390e5a7cd50e65777b105b0ebfc`, scenario hash `94d0aeae0be759d27ad0ce69adc33677b4494b89d41eb219bffe5cb3826f20db`, one candidate across three rows, seven unresolved items, and four diagnostics.

Follow-up authoritative JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ab13e82780c8b85f6ca381da9279793aa4badc06e0d1ed692dcf9ce42cd4d391/d14c1797ac6ecf52bbfdc03a0bdfba51b65cad959d94502cfc003cbdc5301339/probability-d7d344df73dc57572483baee.json`.

Follow-up ranking: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7a060ddfebb88e996cc6285d04f5b92639f1ffb62202d09cbb1482d385e672f0/9fb8cc3d943075972050f600b3cec29d0906d8ef1d7ad3d249d92e77c2a0c5d8/probability-probability-d7d344df73dc57572483baee-ranking.svg`.

Follow-up matrix: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2a3e3a00a8a369d56e03e3b8149da9e684ef28cb392509b3be772044f4b352aa/7e686f6eb14e87c662bbdaf72c6bfe7be004c9b14a026b8e349e9d14d27b6682/probability-probability-d7d344df73dc57572483baee-matrix.svg`.

Follow-up unresolved view: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/77ef599430cf74ee4b1abe7791690bbc5f03551a5eb7979dcca65dbc123f5510/9722ebd8ccbec9932c5823944efa14f345fbc69a2e3043012b84a111ab93c61e/probability-probability-d7d344df73dc57572483baee-unresolved.svg`.

The unresolved inputs are all five contact receipt variables, `num_equipment@alien_laser_weapon_equipment_1`, and scoped `any_controlled_state`.

All four landing modifiers were inactive in the supplied scenarios, so no MCP sensitivity result exists for network, reserve-priority, guarded-descent, or near-space factors.

The source contract still clearly requires one valid controlled target state, no pending/cooldown/world-end gate, contact from a positive receipt, and at least 2,000 laser weapons, but no exact AI score or target-state availability claim is MCP-proven.

## Event `.49` `ai_chance`, project selector, focus, research, and strategy surfaces

The current source review finds `chaosx.nr16.49.a` with base 70, friendly-opinion factor, and democratic-government factor, `chaosx.nr16.49.b` with base 30 and hostile-opinion factor, and `chaosx.nr16.49.c` as an invalid-state cleanup option without `ai_chance`.

The `.49` event trigger and diplomatic actor target are external factors, and the complete `.49` option pool was not evaluated in this stopped pass.

A prior 2026-08-22 `event_option_ai_chance` inspection of the then-current source found multiple categorical pools (`.48`–`.51`) and required isolating `{chaosx.nr16.49.a, chaosx.nr16.49.b, chaosx.nr16.49.c}`; its follow-up evaluation failed when the MCP transport closed.

That prior inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3079874637a8cff279a993a85f894ce665790b956895101e9c80b818d2c0da84/88041f721f1160ae22df30e4c768dc3b1299123753827d21e26699da6b1d5beb/probability-inspect-3450c0c84ae1.json` with prior source revision `db66eb28f03a2ff607653780ff373b30d46649ab3138248e9057ef72260b50e0` and source hash `3450c0c84ae155683be4e87b3142e167a73a9beca4b56a7a4d8d1239d25f7909`.

It is retained only as a stale blocker receipt and does not certify the current `.49` source.

The current special-project source gives `sp_dhrondan_envoy_craft` base `constant:dhrondan_contact_ai.standard` at `common/special_projects/projects/016_dhrondan_envoy_project.txt:32-34`, but the installed probability adapter set has no `special_project_ai_will_do` adapter.

No exact project-selection score, completion timing, or random-project selector probability was MCP-proven.

The current strategy-plan source contains four DHR route plans with ordered `ai_national_focuses`, route-specific `focus_factors`, weight factor 1, and mutually exclusive enable/abort conditions.

No current `ai_strategy_factor` probability evaluation was completed, so ordered strategy-plan precedence and route-factor interaction remain score/source-only.

The prior focus audit found an 88-candidate DHR focus pool, but its source revision and evaluation artifacts are from 2026-08-22 and are not reused as current proof here.

No current technology/research or doctrine weighted-surface inspection was completed before the parent stop, so the requested research/focus weighting conclusion is unresolved rather than “balanced.”

## Compare, sweep, sequence, and structural status

No current before/after `hoi4.probability_compare` was run because this audit was supplied no owner patch or historical source fixture, and the parent stopped additional MCP retries after the completed current evaluations.

The prior same-source/current-vs-current random-list compare is a capability receipt only and is stale relative to this handoff; it reported zero source delta and must not be treated as balance evidence.

Prior compare JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/349c1278eaabdfd9983859dabdcd47b2a23c0f79c204abec4ff6091681a543e3/b3b4d2c680974abfdb8a1f6bf0ae0f27beb9401ed6ef8f54a992e30e30ef110b/probability-9d33bda5ac0552ba7cb4ddea.json`.

An Event 016 rebellion `hoi4.probability_sweep` was started with paths `dhrondan_revolt_weight`, four steps, pairwise sensitivity, and rank-reversal search under `DHR_REBELLION_SWEEP_2026_08_25`, but it was aborted by the parent before MCP returned an artifact; no sweep conclusion is claimed.

`probability_simulate` was not used because no uncertain input distribution or seed was declared.

`probability_sequence` was not used because no complete custom Event 019/provider pool manifest declared cadence, cooldown, recovery, removal, reset, timer, and terminal states.

The mandatory structural `hoi4.event_inspect`/`event_render`, `hoi4.focus_inspect`/`focus_render`, and `hoi4.tech_inspect`/`tech_render` calls were not completed before the parent stop; this handoff therefore does not claim structural MCP proof for the event chain, DHR focus tree, or research surface.

## Findings and recommended owner actions

1. Keep the two-entry rebellion tier ladder as authored pending a complete gate-and-cadence audit; the current MCP evidence proves the declared 0/100, 10/90, 20/80, and 40/60 conditional weights and shows no rank reversal.

2. Treat `dhrondan_ai_try_authorize_expedition` as deterministic Kruger-first routing when both routes are valid, not as a normalized Kruger/Mengele probability pool; document that priority or expose a complete explicit route pool before tuning scores.

3. Review the 10,000 expedition score against the intended AI willingness scale after a typed helper fixture is available; the MCP extreme-growth warning is a score-race warning, not a click-probability claim.

4. Re-run `alien_infantry_call_landing` through the discovered `mission_ai_will_do` route with an adapter-supported target-state fixture containing all five receipt variables, the 2,000-equipment variable, controlled-state validity, pending/cooldown/world-end flags, and all four landing modifiers.

5. Isolate the current `.49` event pool and rerun `event_option_ai_chance` with complete diplomatic actor/opinion/government validity for friendly, neutral, hostile, and invalid-target boundaries before describing 70/30 as a normalized chance.

6. Provide a special-project adapter or a declared custom selector manifest for `sp_dhrondan_envoy_craft`; until then its base 100 is source-only and completion timing is unresolved.

7. Rerun the full 88-focus candidate pool with ordered route-plan activation/abort state, prerequisite history, bypass state, crisis choice, and external country factors, then inspect technology/research and strategy adapters before making DHR route balance claims.

8. Any owner-applied weighted patch requires the same named scenarios and a fresh `hoi4.probability_compare` pass; the stale current/current capability receipt above is not a substitute.

## Simplifications, omissions, and blockers

- No gameplay or tuning patch was applied.
- The current Event `.49` option evaluation, project-selector evaluation, focus/research evaluation, strategy-factor evaluation, and structural MCP passes were skipped because the parent explicitly stopped additional MCP retries after the current rebellion/mission/landing evidence was collected.
- The random-list refresh timed out after 180 seconds, but the mandatory initial random inspection and complete current rebellion evaluation succeeded.
- The rebellion sweep was aborted before return, so no threshold/sensitivity/rank-reversal sweep artifact exists.
- Mission and landing MCP results remain partial because the adapter did not accept the declared flat helper-state fields; never-eligible diagnostics are not generalized campaign conclusions.
- No exact click/selection probability is claimed for decision, mission, focus, research, strategy, special-project, or event-option score surfaces.
- No timing-distribution, repeated-cadence, custom-pool cleanup, or terminal-state proof is claimed beyond the source-level 90-day rebellion and 180-day expedition constants.
