# Event 016 D’Rhondan final AI/probability acceptance audit — 2026-08-22

## Acceptance status

**Conditional / weighted-AI acceptance blocked.** This was a read-only audit. No gameplay, AI, event, focus, decision, mission, special-project, provider, constant, or runtime file was edited. The Event 016 rebellion random pool is MCP-proven exact for its three requested tiers. The D’Rhondan focus tree is structurally present at 88 focuses and has a complete declared focus candidate pool, but route-state evaluation is partial. Contact missions, the landing decision, Event 019 provider 508, the custom provider registry, and the special-project selector do not have a complete probability result because the installed MCP route timed out, closed its transport, or has no adapter for the construct. No exact AI selection probability, provider probability, focus route probability, project completion probability, or landing click probability is claimed for those surfaces.

## Required references and audit boundary

The audit read `AGENTS.md`, `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-mtth`, `chaos-redux-focus-trees`, `chaos-redux-decisions-missions`, `chaos-redux-event-planning`, and `chaos-redux-improvement-loop`. It also consulted the required offline Paradox wiki pages (Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and National focus modding) and the vanilla documentation under `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation`.

The verified MCP game target was Operation Postern 1.19.2.0 (d245), workspace `mod_chaos_redux_ea3b2d67c2c0`. MCP calls were read-only. The final MCP transport closed after several long source calls; no further calls were made once that blocker repeated.

## Audited source surfaces

Primary Event 016 sources:

- `events/016_dhrondan_country_events.txt` (`chaosx.nr16.48`–`.52`, especially `.49` response options).
- `events/016_brilliant_scientist_dhrondan_contact_events.txt` (`chaosx.nr16.40`–`.47`, contact, warning, rebellion, and report chain).
- `common/decisions/016_dhrondan_contact_decisions.txt` (Kruger/Mengele authorization, Honor Accord, two 180-day expedition missions, 90-day rebellion mission).
- `common/scripted_triggers/016_dhrondan_contact_triggers.txt` (craft access/operational work, Antarctic bypass, route validity, rebellion gates and tier predicates).
- `common/scripted_effects/016_dhrondan_contact_effects.txt` (automatic expedition helper, pulse refresh/resolve, Honor Accord state transition).
- `common/script_constants/016_dhrondan_contact_constants.txt` (180/90-day cadences, PP/fuel costs, 6/8/10 arrival gates, 30/50 strain gates, 600/800 chaos gates, 10/20/40 weights, 25/100/10000 AI scores).
- `common/decisions/016_alien_infantry_landing_decisions.txt`, `common/scripted_triggers/016_alien_infantry_api_triggers.txt`, `common/scripted_effects/016_alien_infantry_api_effects.txt`, and `common/script_constants/016_alien_infantry_api_constants.txt` (contact/equipment/state-target landing contract).
- `common/special_projects/projects/016_dhrondan_envoy_project.txt` (`sp_dhrondan_envoy_craft`).

Event 019/provider sources:

- `common/scripted_triggers/016_brilliant_scientist_project_force_event19_triggers.txt`.
- `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt`.
- `events/019_infantry_spawn.txt`, `events/019_infantry_spawn_scenario.txt`, and the `common/scripted_effects/019_infantry_spawn_*` registry/ledger/management/core/pulse sources.

Focus and strategy sources:

- `common/national_focus/016_dhrondan_focus_tree.txt` (exactly 88 DHR focus IDs).
- `common/ai_strategy_plans/016_dhrondan_focus_ai.txt` (opening, Imperial, Synod, and Covenant plans).
- `common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt` (Kruger route plans and route factors).

## MCP provenance and structural evidence

### Event chain

`hoi4.event_inspect` was called with selector `{kind: event, eventId: chaosx.nr16.40}`, `mode=scan`, `expandHelpers=true`, `maxNodes=300`, and `maxEdges=600`. It returned `EVENT_INSPECTED_PARTIAL`, revision `bc0062fc8506bf5505d078e07d30ec754f89ff356b2b63f89df990e808aa23b9`, graph hash `b1d3bee3988caf66732214ea0c5dade1d84fbeeefe8d3c2cab0d2be636205e18`, and the bounded scan artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/392c95554950feaca5baf560c83861e8e3b960c629cd73ebf42b97bf99017f72/56fdcdfc217bc389f6ca6ef00ec6f519445eace0e73b5bf46204696a4969001d/event-scan-bc0062fc8506.json`. The workspace-wide helper/lifecycle pass was deferred; this is structural partial evidence only.

`hoi4.event_render` returned `EVENT_RENDERED_PARTIAL`. Overview artifacts were `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7ad9c6415b82e294819014e62f6a77c04f3ec4935a7e88df3b02e8099f749851/0b6e8e790f0b18f6a172dc58c939fa332090359ac469b23c5a830063a9057b38/event-overview-bc0062fc8506.json`, SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4b40b2bf1656ab045651c29ea710eb397cd71703a13b873b7420bfbdb2be177c/daaaa739e2fd7f92dd59bcb1b9f65a280033fd904dec20181124317c0cae2cb9/event-overview-bc0062fc8506.svg`, and HTML `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/02b3220576c1e47b93ffa904a29bd2e0037184b47b2ad4c8121e67431959a2d2/dbe12d2564865df41498c40d2958b9ad876416605be4f7353d1fa7a796021668/event-overview-bc0062fc8506.html`.

### DHR focus structure

`hoi4.focus_inspect` on `common/national_focus/016_dhrondan_focus_tree.txt` returned `FOCUS_INSPECTED`, revision `22137c0a0c2ce42c8956335fc14717fbafc6b150f521ff7fedd8cceca3ef3bf7`, tree `dhrondan_focus_tree`, 88 nodes, 102 connectors, layout hash `6f6605398964d2a7b6fa02d051bab7a888e980f816c3bc48f4f6738b10773556`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/48e5be7b33723c5f3aa40e9dc634a21a742f379e402a1a73e728b3870b07f4a4/00ebed336faf6d7a2734bafe49ca28c96609fda867a461720ca4f85dd258ec0c/focus-inspect.22137c0a0c2ce42c.json`. The DHR-local warnings are non-blocking connector detours/spacing; the 12 missing-icon diagnostics refer to imported vanilla continuous focuses, not DHR nodes.

`hoi4.focus_render` returned `FOCUS_RENDERED` with HTML `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ec5279ab90369a3c173c9c9ecd71d1ad07163c3f5867e9a52b0a23f7c3c1aecc/a719f228d223c2b7d6425d0ce73b2df78a2f0b261aaf98f8a10919fbee4426d1/dhrondan_focus_tree.focus.html`, SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6052a7774f2c2aab1e5fad45d4c9f4375c0d15ee76cf67f83414f39b8423cc48/48d59d4364a8a27ecea74f4ef90241e83f29c03bcb02789128819f69f96ac2f2/dhrondan_focus_tree.focus.svg`, and JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b5df8123186d1b54ccdb48326b5c7cf6046cd7b3d535e57b0a86c25b7a00a597/508e6526cae56f45cbd5c478841c47dd912fa090758f54309e7eff4bbb173c6d/dhrondan_focus_tree.focus.json`.

## Probability evidence

### 1. Rebellion pulse: exact conditional random-list tiers

The required first pass, `hoi4.probability_inspect` with adapter `random_list` on `common/scripted_effects/016_dhrondan_contact_effects.txt`, succeeded. Source revision was `0b582f5b761b1f861482a5609130d1bb3d6382894eb0bc69ab09351be5ad5f76`, source hash `ed0e8caeac0d11a0fe4453319a52e65dfe06fa8a99b5edb569087710f26e1672`, and the complete two-entry local pool was discovered at `dhrondan_resolve_rebellion_pulse` lines 354–361. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/338250675c4781804aa22ff3a0728044bba9659434b55d88ea414484ac28f714/ae580d956c156f1eb9e563951c4e1b61507f0031bf31101206779ee881038c8e/probability-inspect-ed0e8caeac0d.json`. Adapter selection is `proportional_categorical`; complete pool is required; effect-derived weights are unsupported unless supplied as scenario values.

`hoi4.probability_evaluate` used candidate pool `{common/scripted_effects/016_dhrondan_contact_effects.txt:354.entry.1, common/scripted_effects/016_dhrondan_contact_effects.txt:354.entry.2}`, scenario set `DHR_REBELLION_TIERS_2026_08_22`, horizon 90 days, and direct declared weights. Source revision `f0d028199a3b254b15a74355d155f0404c0ca4de89de39d9cc33e94c9475f460`, source hash `ed0e8caeac0d11a0fe4453319a52e65dfe06fa8a99b5edb569087710f26e1672`, scenario hash `7b02306acb106d0a87a35455490a4cd6e1a309f2a107739c335aff0dfd603468`, analysis `probability-e229b5f0ec516f93981a5a5e`. JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1774efb8d3a48f72911baab8b06cf422139f17855a5614d14ab98a5a915a8f53/a80c76c4b48b538f592410c83d7b2a250606450b711eb766a760ac50f7bf1cf0/probability-e229b5f0ec516f93981a5a5e.json`. Ranking and matrix renders: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f5f97da1814eb267495fc56cf69cfdb1caf0f1327456476dd3868105eab9157b/cb0c22dfd88c4abad7ef003c278d376bf5cd075a0efcf0f046995d37201c311f/probability-probability-e229b5f0ec516f93981a5a5e-ranking.svg` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/119776eaca70aa0fef6fd01f200d9bfa607ebdadb872412f950c180f8594557a/766b23c1a73dfb23c6837098d2ac2a2746f0670e03e52ef3b17f4ce0ea4738ec/probability-probability-e229b5f0ec516f93981a5a5e-matrix.svg`.

Exact result:

| Scenario and source gate | Revolt entry | No-revolt entry | Result class |
| --- | ---: | ---: | --- |
| `REBELLION_LOW_10`: pact, no rebellion flag, arrivals 6–7, strain 30–49, chaos 600–799 | 0.10 | 0.90 | Exact conditional pool; no pulse-activation/timing claim |
| `REBELLION_MEDIUM_20`: pact, no rebellion flag, eligible; arrivals 8–9 **or** strain >=50 **or** chaos >=800 | 0.20 | 0.80 | Exact conditional pool; source OR semantics confirmed |
| `REBELLION_HIGH_40`: pact, no rebellion flag, arrivals >=10 **and** chaos >=800 | 0.40 | 0.60 | Exact conditional pool; high tier overrides medium/low |

The MCP emitted one design warning, `PROBABILITY_DOMINANT_OUTCOME`, for the 0.90 no-revolt outcome in `REBELLION_LOW_10`. No rank reversal occurs: no-revolt remains rank 1 at 90%, 80%, and 60%; revolt remains rank 2 at 10%, 20%, and 40%. The revolt path is not starved by the tier ladder, but the low tier is intentionally no-revolt dominant. The exact 90-day mission cadence and terminal cleanup are source-backed (`days_mission_timeout = constant:dhrondan_contact.rebellion_pulse_days`, cancellation when eligibility fails, and refresh after no-revolt); the random-list adapter explicitly does not model time distributions.

`hoi4.probability_sweep` used the same complete pool and three tier scenarios, `DHR_REBELLION_SWEEP_2026_08_22`, analysis `probability-673354f982ed8df5f5c9260a`, scenario hash `3e52089f26b79ff3608b89fbc8e680a6f7b92883d3e94b03ae700b7669a943ba`, and three sweep points. JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/011ca19615c318dbbb6cd7fb1c6559eb3018a1f2ffcb656b250d46edcac12e18/c69facd3653a950e4630fa0c5a3d0f0524036af9706abe30c899af3d92088e74/probability-673354f982ed8df5f5c9260a.json`. It confirms the same ordering and the 0.90 dominance warning; no threshold rank reversal was found.

`hoi4.probability_compare` was exercised as a same-source/current-vs-current capability receipt because no owner patch or historical pre-change source was supplied. Analysis `probability-9d33bda5ac0552ba7cb4ddea`, scenario hash `2ddacc7c51f437a1a93b4ca50d279856d747256c5894cddfb89cb685cb4e5beb`, `comparisonChanges=0`, and no unresolved rows. JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/349c1278eaabdfd9983859dabdcd47b2a23c0f79c204abec4ff6091681a543e3/b3b4d2c680974abfdb8a1f6bf0ae0f27beb9401ed6ef8f54a992e30e30ef110b/probability-9d33bda5ac0552ba7cb4ddea.json`; comparison render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/30fed412428ef1bf208c3c1333836bcfb73cab0598d437b00622ecbba316f590/probability-probability-9d33bda5ac0552ba7cb4ddea-comparison.svg`. This is not a before/after balance proof.

### 2. DHR focus route AI and mutual exclusion

`hoi4.probability_inspect` with `national_focus_ai_will_do` on `common/national_focus/016_dhrondan_focus_tree.txt` found 88 candidates, source revision `35a9528a0a9732b020c2f030bf4013f8fdc3d3f8841c619b3ca02a9f86fa6fb4`, source hash `860246e3a2d4f1a7fd88dfb4a8b3ff202b573e70bac059bb8042ad7af57bf269`, and five required scenario-input classes. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/72eb0ea62279a4cbfd23c2e7de9d7eed55240dbea894b3c576afbbca29e8dd97/2d2add0047068b48483871680cbd774782dabdc8b33efe8f52100807b0653c96/probability-inspect-860246e3a2d4.json`.

The full declared candidate pool was all 88 `DHR_*` focus IDs. `hoi4.probability_evaluate` used scenario set `DHR_FOCUS_ROUTE_MATRIX_2026_08_22` with `DHR_OPENING_PEACEFUL`, `DHR_IMPERIAL_ROUTE`, `DHR_SYNOD_ROUTE`, `DHR_COVENANT_ROUTE`, and `DHR_EXISTING_COUNTRY_LOW_CHAOS`. It returned `PROBABILITY_ANALYZED_PARTIAL`, analysis `probability-d3a4016d6115c3cfc3606c6f`, source revision `db07f8ed4384053d3fd965aabcd06c382aa7ff3b81616dbf455c657d9082be03`, source hash `860246e3a2d4f1a7fd88dfb4a8b3ff202b573e70bac059bb8042ad7af57bf269`, scenario hash `71ddacbb48f08ae9de79fd6927d06ce561681982ad41147e19c71bce5af66d6d`, 440 candidate rows, 129 unresolved outcomes, and 34 diagnostics. JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eab02a9f1a200478b37d0d8a59afb248eea117eb6afa652bedde03dace9db284/3f40b3d6d7dc1c6054b52a3ff6cc4a3a15297fef7af58a6ac17416521e69a34d/probability-d3a4016d6115c3cfc3606c6f.json`. Ranking, matrix, and unresolved renders were emitted at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/104c01df156f713b077f2689bef51794c533d7ed6230f4da55ffe00f0a2d20c2/c84ca5c6a406968dcb24e6f8f9c4d6471dedb6e96baa776ceb5a81a76b7a96a4/probability-probability-d3a4016d6115c3cfc3606c6f-ranking.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f45a046e4a00eb184be8cceff5298d9166a42ecfdc45aab669dbdd64155a52bf/40c5a43fcb6523a777b7f49fdc316cf48591dc818908fea877974e17feb73f40/probability-probability-d3a4016d6115c3cfc3606c6f-matrix.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2cf244fda2d15a0faabbf339cc3fbbbe8621e2c0fa2525f566b17895175e582d/93fb564ffbf236a9cf40363315b69404b2e794aaf13dd31a62a76975d19e7b90/probability-probability-d3a4016d6115c3cfc3606c6f-unresolved.svg`.

This is **partial score evidence**, not focus-choice probability. The adapter models an independent AI score race, not `weight / sum(weights)`. Prerequisite history, route triggers, ordered strategy-plan state, bypass state, and external country factors were not fully typed. The 34 diagnostics include never-eligible descendants in the supplied incomplete states; they are not proof those focuses are dead in a campaign. The source does contain mutually exclusive regime roots (`DHR_vael_ix_takes_the_throne`, `DHR_sera_qel_presents_the_calculus`, `DHR_ilyr_ren_opens_the_chamber`) and mutually exclusive crisis choices (`DHR_offer_a_shared_horizon`/`DHR_break_the_separatist_ciphers`).

`hoi4.probability_inspect` with `ai_strategy_factor` on both `common/ai_strategy_plans/016_dhrondan_focus_ai.txt` and `common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt` returned `PROBABILITY_SOURCE_DISCOVERED`, `discoveryReason=no_weighted_surfaces`, zero candidates, and no adapter evidence. DHR artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0ed9f9d540a10d56f1d67e3fbf5e9a0b0555eb9cec773948e1a67e055632bc4c/0e9769677352a665d4d1df748cfa9298baea647435217bfa1815362c32b1cfa7/probability-inspect-c19b9403c254.json`; Kruger artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bd06a6058b6bd49652e11e14cb73ca019239b12c25fe6c7a65f89a3d08dcdbea/5bd0b6b89524f8a270c6d8e89bd1674a0d924414b3f338c38e5980d97ca681ad/probability-inspect-e7bad91e8a60.json`. Inline DHR plan factors are source values (`@dhr_ai_plan_weight=1`, preferred 15, urgent 20); they are strategy-plan priorities, not proven selection probabilities. Ordered plans can override the focus score race. Route-specific strategy dominance/starvation and rank reversals remain unresolved.

### 3. Kruger/Mengele expedition missions and Honor Accord

`hoi4.probability_inspect` with `mission_ai_will_do` on `common/decisions/016_dhrondan_contact_decisions.txt` and declared pool `{dhrondan_send_kruger_to_dhronda, dhrondan_send_mengele_to_dhronda}` succeeded. It discovered two mission-style AI surfaces, `poolComplete=false`, required inputs `KRG_warren_kruger`, `custom_trigger_tooltip`, `has_character`, `has_cosmetic_tag`, `exists`, and `is_special_project_completed`; source revision `29febf73e3cd259f48943b53e277306f6b52e6eda79683c4947fa135c3e8a868`, source hash `4a370bea603b8759a82a054d48def6cc59b821ba28929b5e6f3ab605da32ee94`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/345866ba60a635b164849b22dfb274a9b54f57bb460ff4aaef9c1ade2e22a69c/1dbf253548754b614d6f4a19eb658699a22d1dca7f420be9b2ca03409afa0f57/probability-inspect-4a370bea603b.json`.

The mission adapter is `score_only`; it never supplies a click/selection probability. Two `probability_evaluate` attempts (two-candidate pool and one-candidate Kruger pool) timed out after 180 seconds with `tool call failed for hoi4_agent_tools/hoi4.probability_evaluate: timed out awaiting tools/call after 180s`. Therefore no AI score trace, rank, validity, dominance, or starvation result is MCP-proven for Kruger/Mengele. Source evidence is still concrete: both authorization decisions use `constant:dhrondan_contact_ai.dominant` (10,000) at lines 44 and 74; the source availability gates require completed `sp_dhrondan_envoy_craft`, route-valid character/country state, no pact/transaction lock, and fuel. The helper invoked after the AI decision selects Kruger first when both route predicates pass and Mengele otherwise (`common/scripted_effects/016_dhrondan_contact_effects.txt:145–174`). That is deterministic first-valid priority, not a normalized two-way probability, and should be reviewed as a possible route-order dominance risk.

The contact-category `decision_ai_will_do` inspect found only the non-clickable `dhrondan_contact_status_header` (`selectionRule=score_only`, base 0); its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7c61d7a1101623422c5fd820fef43ed2d2b0cd9b4b593f736fa9baa7213b5647/54b2737fd2e8246b1848309fd8b23f6ae6a4696c23fee67c37bbdf7ebed6ea2c/probability-inspect-4a370bea603b.json`. A candidate-override inspect identified `dhrondan_honor_accord` as available, but the follow-up inspect timed out after 180 seconds. A direct Honor Accord evaluate returned `PROBABILITY_SURFACE_EMPTY` / `No weighted blocks matched this request`. No MCP score trace exists. Source-only base is 25, multiplied by 4 to 100 at strain >=50, while availability requires an active pact, strain >0, no Honor cooldown, no rebellion, and no world end. It remains score-only and not a click probability.

### 4. Landing decision and landing API

The landing source is `common/decisions/016_alien_infantry_landing_decisions.txt`. It has one state-targeted decision, `alien_infantry_call_landing`, with source base `alien_infantry_landing_ai.standard` and factors 1.25 for the DHR network, 1.50 for landing-reserve priority, 1.25 for guarded descent, and 1.50 for secured near space (lines 40–57). The public gate requires a contact receipt, a valid controlled target state, no pending/cooldown/world-end state, and at least 2,000 `alien_laser_weapon_equipment_1`; the API debits/refunds exactly 2,000 and the mission reservation lasts seven days.

The required `decision_ai_will_do` inspect on this source timed out after 180 seconds: `tool call error: tool call failed for hoi4_agent_tools/hoi4.probability_inspect ... timed out awaiting tools/call after 180s`. No landing score, target-pool completeness, target validity, rank, dominance, or starvation result is therefore available. `INSUFFICIENT_LASERS`, `NO_CONTACT`, and invalid target cases are source-gated ineligible, but the MCP route did not prove them. Do not convert the 10/15/18/22.5-style source factors into click probabilities.

### 5. Event `.49` response, contact/rebellion news/options

`hoi4.probability_inspect` with `event_option_ai_chance` on `events/016_dhrondan_country_events.txt` succeeded. Source revision `db66eb28f03a2ff607653780ff373b30d46649ab3138248e9057ef72260b50e0`, source hash `3450c0c84ae155683be4e87b3142e167a73a9beca4b56a7a4d8d1239d25f7909`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3079874637a8cff279a993a85f894ce665790b956895101e9c80b818d2c0da84/88041f721f1160ae22df30e4c768dc3b1299123753827d21e26699da6b1d5beb/probability-inspect-3450c0c84ae1.json`. The source has multiple categorical pools (`.48`, `.49`, `.50`, `.51`), so whole-file normalization is blocked with `MULTIPLE_CATEGORICAL_POOLS`; `.49` must be isolated with candidate pool `{chaosx.nr16.49.a, chaosx.nr16.49.b, chaosx.nr16.49.c}`. Evaluation was attempted after inspect but the MCP transport closed; no `.49` analysis artifact exists.

Source base factors are exact but score/chance conclusions remain unresolved: accept 70, refuse 30; accept factors 1.5 for opinion >25 and 2 for democratic government; refuse factor 3 for opinion <-25 (`common/script_constants/016_dhrondan_country_constants.txt:130–142`). The `.49.c` invalid-state option is gated and has no weight. No exact normalized response probability is asserted. Contact/rebellion news/report options are triggered-only presentation options without AI weights; the `.46` warning is one-time and `.47` starts the rebellion bridge.

### 6. Event 019 provider 508 and custom provider pool

Provider 508 is registered in `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt:55–65` only when the alien-arms project is active or the custom alien-infantry technology is operational; registration grants the Event 019 provider-508 contact receipt and calls `chaos_unit_family_provider_508_register`. Its provider row (`:169–184`) is `spawn_only`, family-only Event 019 lot policy, and supplies cleanup/parent-isolation profiles plus a source spawn weight. `brilliant_scientist_event19_alien_infantry_provider_unlocked` is a receipt-variable gate (`common/scripted_triggers/016_brilliant_scientist_project_force_event19_triggers.txt:85–91`). The eligibility callback selects provider kind `alien_interface` and marks the candidate eligible only when that receipt is positive (`...effects.txt:560–595`).

The required `custom_weighted_pool` inspect on `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt` timed out after 180 seconds. A narrower trigger-source inspect then returned the exact blocker `Transport closed`. No provider candidate pool, source revision/hash, normalized weight, selection rank, cleanup probability, or compare artifact exists. The MCP probability adapter cannot represent the registry/meta-effect dispatch, dynamically assembled Event 019 provider candidates, provider receipt, provider cleanup profile, or deferred landing transaction as a complete categorical pool. This is an unresolved custom-pool adapter limitation, not evidence that provider 508 is absent or dominant.

Required scenarios `PROVIDER_508_PRESENT`, `PROVIDER_508_ABSENT`, and `PROVIDER_508_CLEANUP` therefore remain unresolved. Source review indicates absent receipt blocks provider 508, present receipt admits it, and the provider's cleanup/rollback path is owned by the shared Event 019 registry/API; no exact selection or cadence statement is made.

### 7. Envoy special project and random selector

`sp_dhrondan_envoy_craft` in `common/special_projects/projects/016_dhrondan_envoy_project.txt` has `ai_will_do = { base = constant:dhrondan_contact_ai.standard }` (100), visible/available gates delegated to `dhrondan_envoy_craft_is_visible`/`dhrondan_envoy_craft_is_available`, and a project output that calls `dhrondan_complete_envoy_craft`. The probability adapter enum has no `special_project_ai_will_do`; a direct inspect attempt returned the exact validation blocker: `Invalid option: expected one of event_mean_time_to_happen|event_option_ai_chance|decision_ai_will_do|mission_ai_will_do|national_focus_ai_will_do|technology_ai_will_do|doctrine_ai_will_do|direct_random|random_list|ai_strategy_factor|custom_weighted_pool at adapter`.

The custom project/effect selector route was not MCP-proven. The `custom_weighted_pool` inspect on the large Event 019 provider source timed out, and subsequent source calls closed the transport. No project completion timing, special-project rank, or random selector probability is claimed. The Antarctic bypass is source-gated by current host + `antarctica_success` + not consumed + no world end and is not a probability result.

## Named scenario disposition

| Named scenario | MCP disposition | Acceptance classification |
| --- | --- | --- |
| No contact | Landing API source gate requires a contact receipt; landing inspect timed out | Source-gated but probability unresolved |
| Antarctic bypass | Trigger requires current host, `antarctica_success`, unused bypass, no world end; completes craft once | Source-gated exact predicate; project timing unresolved |
| Project craft | Envoy project has base AI score 100 and operational-work/access gates | Score-only/source evidence; no special-project adapter |
| Kruger valid | Mission inspect found candidate, but all evaluations timed out; source base 10,000 | Score-only unresolved effective validity/rank |
| Mengele valid | Mission inspect found candidate, but all evaluations timed out; source base 10,000 | Score-only unresolved effective validity/rank |
| Insufficient lasers | Public landing gate requires 2,000 laser weapons | Source-gated; landing AI MCP unresolved |
| Six/seven arrivals, chaos 600–799 | Complete random-list evaluation: 10% revolt / 90% no revolt when strain is 30–49 | Exact conditional pool; 90% dominance warning |
| Eight/nine arrivals, or strain 50, or chaos 800 | Complete random-list evaluation: 20% / 80% | Exact conditional pool; OR semantics confirmed |
| Ten+ arrivals with chaos 800 | Complete random-list evaluation: 40% / 60% | Exact conditional pool; high tier overrides |
| Low chaos (<600) | Rebellion pulse eligibility fails | Source-gated no-pulse condition; no timing claim |
| Existing DHR | Focus evaluator partial; landing/provider/pulse external state not typed | Unresolved route balance |
| Imperial regime | Focus evaluator partial; strategy adapter found no indexed surfaces | Unresolved route score/rank |
| Synod regime | Focus evaluator partial; strategy adapter found no indexed surfaces | Unresolved route score/rank |
| Covenant regime | Focus evaluator partial; strategy adapter found no indexed surfaces | Unresolved route score/rank |
| Provider 508 present | Custom provider inspect timed out/transport closed | Unresolved custom pool |
| Provider 508 absent | Source receipt gate is clear; no provider selection adapter | Source-gated, probability unresolved |
| Provider 508 cleanup | Registry/API cleanup source exists; no complete dynamic pool/cadence manifest | Unresolved custom lifecycle |

## Findings and owner recommendations (no changes applied)

1. Preserve the rebellion tier order and complete two-entry pool. The MCP result proves exact 10/20/40 conditional revolt chances and no rank reversal. Review the intentional 90% no-revolt dominance against desired pacing; do not call the 10/20/40 values world-level or cumulative probabilities.
2. Treat Kruger/Mengele authorization as a deterministic first-valid route helper, not a two-way probability pool. If both can be valid in a campaign, the owner should either document Kruger-first priority or expose an explicit complete route pool and rerun the same named scenarios through `mission_ai_will_do` and `probability_compare` after any source change.
3. Keep Honor Accord as score-only until the decision adapter can index the nested block. Re-run with pact, strain 0/30/50+, cooldown, rebellion, PP, and world-end state typed; do not describe 25 or 100 as a click chance.
4. Re-run the landing audit with a target-state candidate pool and explicit receipt/equipment/target/landing-network/guarded/near-space flags. The current timeout leaves landing AI dominance/starvation and target starvation unresolved.
5. Provide a typed custom-pool adapter or a complete declared Event 019 provider manifest containing provider IDs 504–510/522, eligibility, receipt state, registration/removal, cleanup, rollback, deferred landing transaction, cadence, and terminal states. Until then, provider-508 present/absent/cleanup conclusions remain source-only and unresolved.
6. Provide a special-project AI adapter or explicit project candidate/cadence contract for `sp_dhrondan_envoy_craft`; the current adapter set cannot analyze special-project `ai_will_do` or completion timing.
7. For focus acceptance, rerun the 88-candidate pool with complete prerequisite history, each regime route, ordered plan activation/abort state, crisis choice, bypass, and external country factors. The current focus artifact proves structure and source discovery, not route selection balance.

## Skipped analyses and exact blockers

- `probability_simulate`: skipped because no uncertain input distribution or seed was declared; deterministic tier states were available and evaluated exactly.
- `probability_sequence`: skipped because no complete Event 019/custom provider pool manifest declared cadence, cooldown, recovery, removal, reset, timer, and terminal states. The source/provider adapter cannot represent that registry as a complete pool.
- `probability_render`: ranking/matrix/unresolved/comparison renders were emitted automatically by successful rebellion and focus analyses. No separate render was possible for timed-out/empty surfaces because no analysis ID existed.
- Event `.49` evaluate: no result; MCP transport closed after successful inspect.
- Kruger/Mengele mission evaluate: two attempts timed out after 180 seconds.
- Honor Accord inspect: candidate-override inspect timed out; evaluate returned `PROBABILITY_SURFACE_EMPTY` / `No weighted blocks matched this request`.
- Landing decision inspect: timed out after 180 seconds.
- Event 019 custom provider inspect: timed out after 180 seconds; narrower trigger inspect returned `Transport closed`.
- Special-project adapter: exact enum blocker shown above; no `special_project_ai_will_do` adapter is installed.
- `ai_strategy_factor` for DHR and Kruger plan files: `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason=no_weighted_surfaces`, zero candidates. Plan factors remain source-only.

## Final handoff conclusion

The implementation is structurally reviewable and the 90-day rebellion pulse is probability-accepted for its complete local pool and exact 10/20/40 tiers. The overall Event 016/DHR weighted-AI acceptance gate remains **blocked/conditional** because the mandatory MCP route could not prove mission AI, Honor Accord score evaluation, landing target AI, Event 019 provider selection/cleanup, special-project AI/timing, or route-specific focus/strategy behavior. These are explicit MCP coverage/transport blockers; source inspection is retained as separate evidence and is not substituted for probability evidence.
