# Event 021 Decision and Mission AI Probability Baseline

Status: incomplete and unresolved. This is a read-only baseline handoff; no gameplay source was changed. This handoff file was written at the user's explicit request.

## Scope and source identity

Audited all 18 decision and 3 mission ai_will_do blocks in common/decisions/021_random_civil_war_decisions.txt.

The exact current decision source and the immutable pre-edit snapshot at docs/plans/021_random_civil_war_plans/probability_snapshots/event021_decisions_before_2026-09-26/021_random_civil_war_decisions.txt both hash to SHA-256 8937CAC0802745EAD68D6F1EC1B2BFA97DCCAA451EFFCC925D45A715DEDD3123.

Current related source hashes:

| Source | SHA-256 |
| --- | --- |
| common/decisions/021_random_civil_war_decisions.txt | 8937CAC0802745EAD68D6F1EC1B2BFA97DCCAA451EFFCC925D45A715DEDD3123 |
| common/script_constants/021_random_civil_war_constants.txt | 1525A8ED1D75CBCFF5983139F709A7511D4EE9418CF4B11B389057101AD348F9 |
| common/scripted_triggers/021_random_civil_war_parent_triggers.txt | 97E43B7BEB01FEBE49D13E26F169FDE1EB2B751EB451250C7E35C748D24AC622 |
| common/scripted_triggers/021_random_civil_war_triggers.txt | 4DC65730400CDA342321D8E68A1FA670B49CFCFBC94A44789ACF0D39D58F1D63 |
| common/ai_strategy/021_random_civil_war_ai_strategy.txt | 6ADBB93B2CD17665C4BD967368F08BC953738D81DB7A2069171241F45C309DCA |
| common/scripted_effects/021_random_civil_war_decision_effects.txt | A1ED64466537E6E2F0235B7D268BE68AB525AEC119FC08E3240CEB6FE35DDF23 |

The MCP-reported sourceHash for every inspect, evaluate, and sweep was 12ca435e5fc299a8f7cf7e65715523672aae889ab964e9f80c9b91678ea9606c, which does not match the local or immutable decision-source SHA-256 above. MCP analysis therefore is not certified against the exact local source bytes.

The shared repository advanced during the audit. The final observed git HEAD was f573a8759a3095265ff11d98da6c7fb226ef9427. Commit 9ed45bae5 changed the Event 021 maximum planned fronts from 4 to 5 and added tertiary-front allocation constants; the decision file hash and the event021_ai score constants remained unchanged across the observed source checks. MCP sourceRevision values also changed between calls, so the evidence below is retained per artifact rather than treated as one stable revision.

## Weighted surface and source-level traces

The centralized bases are event021_ai.base_action = 1 and event021_ai.base_mission = 1. Shared factors are priority_major = 1.5, discourage_concession = 0.75, discourage_repression = 0.75, and random_civil_war_value.zero = 0. The source-defined near-defeat threshold is 0.70. random_civil_war_authority_is_failing is true above 14 and at or below 39 State Authority.

These are source modifier traces, not computed final scores. No arithmetic combination is claimed because the complete scenario result payload was not readable and key inputs were unresolved.

| ID | Base | Conditional source factors |
| --- | --- | --- |
| event021_secure_arsenals | base_action | government side: ×1.5; settlement pending: ×0 |
| event021_defend_capital | base_action | capital controlled by ROOT: ×1.5; government side: ×1.5 |
| event021_review_loyalty | base_action | command claimant: ×1.5; government side: ×1.5; failing State Authority: ×0.75 |
| event021_seize_depot | base_action | opposition side: ×1.5; invalid priority-front depot target: ×0 |
| event021_open_relief_corridor | base_action | neighbor exposure: ×1.5; humanitarian pressure: ×1.5 |
| event021_offer_emergency_settlement | base_action | negotiator profile: ×1.5; failing State Authority: ×1.5; hardliner profile: ×0.75 |
| event021_reconstruct_administration | base_action | successor side: ×1.5 |
| event021_integrate_formations | base_action | multi-front active: ×1.5; command claimant: ×1.5 |
| event021_set_priority_front | base_action | multi-front active: ×1.5 |
| event021_monitor_border | base_action | containment profile: ×1.5 |
| event021_support_government | base_action | mediator profile: ×0; invalid or non-viable government target: ×0; near defeat or insufficient PP/infantry/convoys: ×0; opportunistic sponsor: ×1.5; government target aligned: ×1.5; opposition target aligned: ×0.75 |
| event021_support_opposition | base_action | mediator profile: ×0; invalid or non-viable opposition target: ×0; near defeat or insufficient PP/infantry/convoys: ×0; opportunistic sponsor: ×1.5; opposition target aligned: ×1.5; government target aligned: ×0.75 |
| event021_offer_mediation | base_action | mediator profile: ×1.5; insufficient PP/command power/convoys: ×0; opportunistic sponsor: ×0.75 |
| event021_end_sponsor_commitment | base_action | negotiator profile: ×1.5 |
| event021_complete_disarmament | base_action | government side: ×1.5 |
| event021_complete_coalition_governance | base_action | negotiator profile: ×1.5 |
| event021_protect_communications | base_action | capital supply risk: ×1.5 |
| event021_review_regional_administration | base_action | failing State Authority: ×1.5 |
| event021_hold_the_capital_mission | base_mission | government side: ×1.5; opposition side: ×1.5; Event 006 front active: ×1.5; same-tag route active: ×1.5 |
| event021_secure_rail_spine_mission | base_mission | reconstruction phase: ×1.5; opposition side: ×1.5; Event 006 front active: ×1.5 |
| event021_hold_settlement_terms_mission | base_mission | settlement phase: ×1.5 |

The results are AI willingness scores. They are not click probabilities and were not normalized as probabilities. No dominance, starvation, rank-reversal, or balance claim is supported by the partial outputs.

Source review found redundant weight guards: event021_secure_arsenals has a settlement-pending zero factor although its visible opening-phase gate excludes settlement pending; event021_seize_depot's opposition-side multiplier and invalid-target zero factor duplicate its visibility gates; event021_integrate_formations and event021_set_priority_front multiply on the multi-front flag already required by their visible phase; event021_open_relief_corridor multiplies on neighbor exposure already required by its exposure-phase gate. These are source-level observations, not a requested coefficient change.

## Decision and mission eligibility findings

The named source contains the complete in-file ID inventory of 18 decisions and 3 missions. The parent direct mission inspect reported poolComplete=false, however, so the complete runtime candidate pool and simultaneously available mission pool are not proven. An inspect call supplied the three in-file mission IDs explicitly and returned poolComplete=true for that supplied list; this does not supersede the parent source-only result.

The decision adapter's source inspect reported 18 candidates and 12 required inputs; the mission adapter reported 3 candidates and 3 required inputs. Both source-only inspections reported zero available candidates without a campaign scenario.

event021_hold_the_capital_mission activates in opening or multi-front phases and its available trigger requires capital control by ROOT, positive infrastructure and a supply node, plus capital-defense-active or capital-held state. Its timeout resolver, event021_mission_hold_capital_resolve in common/scripted_effects/021_random_civil_war_decision_effects.txt, checks only the capital's state at resolution. The inspected sources do not show a continuous hold-duration ledger, so continuous-hold completion remains unresolved.

event021_secure_rail_spine_mission is repeatable with fire_only_once = no. Its activation requires the reconstruction phase and absence of rail-secured, mission-active, repaired, and restored flags, but it does not gate activation on a currently valid target state. Its available trigger requires random_civil_war_rail_mission_state, ROOT ownership and control, membership in ROOT.random_civil_war_opening_core_states, and a supply node or infrastructure above the configured gate. On timeout, event021_mission_secure_rail_resolve checks the current target and calls success or failure resolution. Failure clears the active flag and sets event021_rail_spine_lost, which activation does not test; retry and repeated failure remain possible if reconstruction continues and the target is still eligible. Continuous rail-hold duration is not demonstrated by these checks.

The settlement-terms mission requires an obligation-active flag and hold-until variable; its obligation value, timer, and terminal objective are not representable as a typed campaign fixture through the connected probability adapter.

The Event 006 and same-tag flags were included in the exploratory scenario matrix. The audited AI weight and AI strategy sources do not themselves enroll countries in a league, but this weighted pass cannot certify the broader no-automatic-enrollment contract.

## Scenario and MCP coverage

Parent direct mission inspect: adapter mission_ai_will_do; status PROBABILITY_SOURCE_INSPECTED; sourceRevision 0fc0c947583e19d22b9a6733bc2644e685f1dc65911f6195177bf96241760847; sourceHash 12ca435e5fc299a8f7cf7e65715523672aae889ab964e9f80c9b91678ea9606c; poolComplete=false; candidates=3; requiredInputs=3; unresolved=0. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/31c4889ef58e06e7f0cc91df6270254de40c72b542ddae17b38a77c3c9f003de/3156276505cae08044efb90007cb5725dae7a4a7be3b3ef9071090503d03da7f/probability-inspect-12ca435e5fc2.json.

Auditor refreshed decision inspect: sourceRevision b9841b07c26a7bcdc269e1324bcf1d548267e2cdde5c0ca4cd9f9967b827550d; sourceHash 12ca435e5fc299a8f7cf7e65715523672aae889ab964e9f80c9b91678ea9606c; 18 candidates; 12 required inputs; zero inspect-time unresolved; candidatePool explicitly supplied. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fdd47ce697a549ca09511c2b3dcbf95ed4b47c7e8fd28f943d19926382db8918/c709530371c75fd6e6ce363977d260d2834d807f6467171c1f584804e47999c8/probability-inspect-12ca435e5fc2.json.

Auditor refreshed mission inspect: sourceRevision d77c19ef8a28aeaaea97a3970f38cbb6a91a7dacb5808988b7b636c836215bd7; sourceHash 12ca435e5fc299a8f7cf7e65715523672aae889ab964e9f80c9b91678ea9606c; 3 candidates; 3 required inputs; zero inspect-time unresolved; candidatePool explicitly supplied. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f7273698cacc03b8fc655600d3549f7a11a099237d48055e3d9dc4ed5e6157df/c06d4ae8e94cefd7d27d63a37ddcfa230ef5f701834a93b63b93ea93d57f072a/probability-inspect-12ca435e5fc2.json.

Exploratory evaluate set event021_campaign_states_v2 used 12 scenario IDs: opening_government; opening_opposition; multifront_government_claimant_failing_authority; exposure_containment_humanitarian; exposure_neutral_mediator; exposure_opportunistic_sponsor_targets_declared; settlement_government_hardliner_negotiator_disarmament; settlement_sponsor_repayment_negotiator; settlement_coalition_governance_negotiator; reconstruction_opposition_successor_event6; global_prevention_regional_grievance_failing_authority; event6_same_tag_government_route. ScenarioHash 1ad44b2a5f779cef7b01c352cfae37a6015c1aecf35461d6a5117aaf8d89196c.

Those exploratory scenarios assigned flat primitive values to source variables, resource quantities, and external target scopes without a live save or a typed fixture binding. The connected adapter instructions state that flat primitive state may not bind Clausewitz numeric variables or compound triggers. Treat these evaluate results as partial diagnostics only, not truthful exact campaign scores.

Decision evaluate artifact probability-31c2ffcd092a47e52f324190: sourceRevision d77c19ef8a28aeaaea97a3970f38cbb6a91a7dacb5808988b7b636c836215bd7; sourceHash 12ca435e5fc299a8f7cf7e65715523672aae889ab964e9f80c9b91678ea9606c; scenarioHash 1ad44b2a5f779cef7b01c352cfae37a6015c1aecf35461d6a5117aaf8d89196c; 12 scenarios; 216 candidate-scenario rows; 51 unresolved; status PROBABILITY_ANALYZED_PARTIAL. Diagnostic: event021_secure_arsenals' factor 0 was inactive in all 12 scenarios.

Decision evaluate artifacts: JSON hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e17a83bfb7f0beff5ef597e87f6b8a38c81311d02abdd751a7e442985346d3ed/dae8b9745be1ce925bfe459a4de519446e6a00f6317f1d99cda7acf09cc0eaef/probability-31c2ffcd092a47e52f324190.json; ranking SVG hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3e2f6b9a95ab49554f372300505f6c31452cb40544301ab7cc4e4429383751ad/93fb1e43b06e2cb1b749b9185b3ef24d05a0a092578cda1460968d2b82a5d320/probability-probability-31c2ffcd092a47e52f324190-ranking.svg; matrix SVG hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/617a3590ba80f38ec495b0f162f23bfc9497aff7be958fcef1b59101740aca11/e9df6ac408ead2d935ffbfc6853957bb2c09122ecb006490d60279e71a6a6abc/probability-probability-31c2ffcd092a47e52f324190-matrix.svg; unresolved SVG hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/85475ecef633ab5be06fd4aa7169398cdd2650c813d5a07d6fb118ae7e3ea447/b828b0be27ea6234915ae7de9c0a735f322aa2ca7a9d8603f09c52af25f16361/probability-probability-31c2ffcd092a47e52f324190-unresolved.svg.

Mission evaluate artifact probability-a96d9dff14216f80b158fe77: sourceRevision 83a117ba7d2b189ab5c28bfa6a1db5c448558227796985c079641ac25a5c1e24; sourceHash 12ca435e5fc299a8f7cf7e65715523672aae889ab964e9f80c9b91678ea9606c; the same scenarioHash; 12 scenarios; 36 candidate-scenario rows; 6 unresolved; status PROBABILITY_ANALYZED_PARTIAL.

Mission evaluate artifacts: JSON hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ea26a9b3b3ee2680104afa38d0f61f9efeb3686529131d0efad6839b5e7e07f4/a5c5ec4027b2389aec493d6047bed426b72f6d6ac5336c012f161076bbbe1707/probability-a96d9dff14216f80b158fe77.json; ranking SVG hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8d75f670767fa1f8842bda66818f487b60c14254abf7fe65c0be6a3c0eab98a9/4204fede98f89a2056690d0e72cc9c8f01e19e1d51ac55bb7c68de6344eb0650/probability-probability-a96d9dff14216f80b158fe77-ranking.svg; matrix SVG hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/91ed2e07d39a2caf13caaf9b3f138c5153a754a1e248df81e47f3c8c2e65786c/6614a2dad2d62a2f0cde646990555ea8728420cb2f14d1a4892a93c32a5972aa/probability-probability-a96d9dff14216f80b158fe77-matrix.svg; unresolved SVG hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ef93c595e5d258148a72acde8a554d824c0b4f69be64fe090674437581180d7b/84372aaa018dbceb08bd1f11940af7e4b787c7a6997ce60e17d3d6c344dd66f5/probability-probability-a96d9dff14216f80b158fe77-unresolved.svg.

Sensitivity set event021_threshold_sensitivity_v1 named: support_pre_surrender_threshold (surrender_progress 0.69, authority 39); support_at_surrender_threshold (0.70, 39); support_post_surrender_threshold (0.71, 40); authority_failing_boundary (39); authority_above_failing_boundary (40). ScenarioHash 9790b1e10b3f31d210aba93852487d75fb6d9e19018b664932fa3ce694f53d8a. The values are probes around source thresholds, not live-save observations.

Latest sweep artifact probability-724ee62cd91078e441765044: adapter decision_ai_will_do; sourceRevision 0fc0c947583e19d22b9a6733bc2644e685f1dc65911f6195177bf96241760847; sourceHash 12ca435e5fc299a8f7cf7e65715523672aae889ab964e9f80c9b91678ea9606c; scenarioHash 9790b1e10b3f31d210aba93852487d75fb6d9e19018b664932fa3ce694f53d8a; paths surrender_progress and random_civil_war_state_authority; steps=5; pairwise=true; findRankReversals=true; 5 sweep points; 90 candidate-scenario rows; 48 unresolved; 9 informational diagnostics; status PROBABILITY_ANALYZED_PARTIAL.

Sweep artifacts: JSON hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8f25c606e179155aeab67c416b6188809f4ca11b7084fcefabb0080542780355/abdde1a458fa2f43b663007af144e3c04ffaca60252accacde05fa387d347609/probability-724ee62cd91078e441765044.json; sensitivity SVG hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/68f1d5a2b323a3f2e9d398088242cf3c216981c337b3a7a8ab99d225e846be66/ecd807b123785e93ef9bbc3807991c7ebe5bbcbf34ecd8ac1a8eed1b61c08a00/probability-probability-724ee62cd91078e441765044-sensitivity.svg; threshold SVG hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a6d32ffc270e06218fbe6e53b5f3d111d3f383d152a2e17fa057722f7cf35cc8/70338af03f39806f2a44d5db83c0b595a15bb06c176a69a20f02bc8ec5769102/probability-probability-724ee62cd91078e441765044-threshold.svg; unresolved SVG hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/08c059fb40727a33921034b6b66bcff6da28af3e0cfe29fe93a03d6f66d441fe/00bb9ef46b91aa09f7112343a8d832300340579d3578148cd0f2e6e73f669e9e/probability-probability-724ee62cd91078e441765044-unresolved.svg.

## Truthful fixture boundary and comparison coverage

The source-flag-only scenario IDs prepared for a clean same-scenario baseline are opening_government, opening_opposition, multifront_opposition_command_claimant, exposure_containment_humanitarian, exposure_neutral_mediator, exposure_opportunistic_sponsor, settlement_hardliner, settlement_negotiator, reconstruction_opposition_successor_event6, global_prevention_regional_grievance, and event6_same_tag_government. They use actor POL, an empty state map, and only source-named flags.

That source-flag-only evaluation sequence was interrupted by the user before any tool result returned. It has no accepted scenarioHash, analysisId, artifact, or score result and must not be represented as evaluated coverage.

Missing fixture inputs include typed values for random_civil_war_state_authority and random_civil_war_settlement_obligation; capital and rail state scope pointers; current state ownership/controller, supply, infrastructure, and opening-core-array membership; exposure target/host/opposition scopes and target viability/alignment; PP, command power, manpower, and equipment stockpiles; settlement hold-until date and terminal objective state; and global-versus-country flag scope. The connected scenario schema accepts only actor string, flat primitive state, flags, and scopes with id/state; it does not provide typed Clausewitz variable declarations or compound-trigger fixtures. Do not add invented variable declarations to force a result.

hoi4.probability_render coverage is blocked for the latest sweep by PROBABILITY_ANALYSIS_NOT_CACHED: the render call said it requires an analysis ID produced by that server process. An earlier render attempt returned PROBABILITY_ANALYSIS_STALE after the workspace revision changed. Evaluate and sweep calls did return ranking, matrix, waterfall, sensitivity, threshold, and unresolved resources, but the analysis JSON contents were not readable through the available resource listing, so exact numeric ranking order and final modifier values cannot be reported here.

hoi4.probability_compare was not run. This is a baseline-only pass with no owner-applied after source; comparing the file to itself is invalid. No comparisonId exists. The parent can use the exact immutable pre-edit source path and hash above with the same named source-flag scenario fixture after the mission patch.

hoi4.probability_simulate was not run because no uncertain-input distribution was declared. hoi4.probability_sequence was not run because these are native decisions and missions, not a complete custom weighted-pool cadence manifest. No decision/mission structural inspect or render route was exposed; the weighted probability adapters were used.

## Findings, limits, and parent follow-up

No balance, click probability, normalized probability, starvation, dominance, or rank-reversal conclusion is certified. The sweep is partial and its numerical rank details were not accessible. Scenario availability, target validity, active mission count, and action count against the accepted 3–5 decisions and 1–3 missions bounds remain unresolved.

Mission repetition risk is concrete at source level: event021_secure_rail_spine_mission is repeatable, activation does not test event021_rail_spine_lost or a retry cooldown, and timeout clears the active flag while setting the lost flag. Its activation also does not require a valid rail target, although availability and the timeout resolver test target validity. The parent-requested fix should make target validity and retry/terminal state agree between activation, availability, cancellation, and resolution.

Continuous hold is not proven: event021_mission_hold_capital_resolve and event021_mission_secure_rail_resolve in common/scripted_effects/021_random_civil_war_decision_effects.txt check current conditions at resolution. The source does not show a continuous-duration ledger for capital or rail control. The parent-requested fix should implement the intended continuous hold semantics while leaving all ai_will_do coefficients unchanged.

Concrete parent follow-up: patch event021_hold_the_capital_mission and event021_secure_rail_spine_mission in common/decisions/021_random_civil_war_decisions.txt and their named resolvers in common/scripted_effects/021_random_civil_war_decision_effects.txt; then run probability_compare against the immutable pre-edit decision source using an identical, MCP-accepted scenarioSet. If the same pool or fixture limits remain, preserve them as unresolved rather than claiming balance.

The Event 006 human-package reuse and no-automatic-league-enrollment contract is not certified by this weight pass. The Event 006 and same-tag flags were scenario probes only; the weighted decision/mission source does not prove enrollment lifecycle behavior.

No source changes were made by the auditor. The only write in this task is this requested handoff. Skills used: chaos-redux-subagents, chaos-redux-decisions-missions, and chaos-redux-mtth.
