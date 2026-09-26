# Event 021 post-patch decision and mission AI comparison

Status: incomplete comparison; no balance claim. The read-only source review confirms the 21 pre-edit and post-edit ai_will_do blocks are identical, but HOI4 MCP could not produce the required before-and-after comparison for the preserved snapshot.

## Scope and source identities

Audited surfaces: the 18 decision ai_will_do entries and 3 mission ai_will_do entries in common/decisions/021_random_civil_war_decisions.txt.

Pre-edit source: docs/plans/021_random_civil_war_plans/probability_snapshots/event021_decisions_before_2026-09-26/021_random_civil_war_decisions.txt; verified raw SHA-256 8937CAC0802745EAD68D6F1EC1B2BFA97DCCAA451EFFCC925D45A715DEDD3123.

Post-edit source: common/decisions/021_random_civil_war_decisions.txt; verified raw SHA-256 C928B1B802B4B2CCCFA49913AF9E288571099398A0000DA1814B6E35CDE81BC1.

Scenario fixture: docs/plans/021_random_civil_war_plans/subagent_handoffs/event021_mission_ai_source_flag_scenarios_2026-09-26.json.

Supporting weights: common/script_constants/021_random_civil_war_constants.txt defines event021_ai.base_action = 1, base_mission = 1, priority_major = 1.5, discourage_concession = 0.75, and discourage_repression = 0.75. The referenced zero factor is constant:random_civil_war_value.zero.

Supporting strategy source: common/ai_strategy/021_random_civil_war_ai_strategy.txt contains role-specific army, equipment-production, and war-avoidance strategy values; it has no pp_spend_priority entry for decision selection. Those strategy values were not declared as scenario factors.

The source diff is limited to mission target, activation, availability, and cancellation plumbing. event021_hold_the_capital_mission now records and clears event021_hold_capital_mission_target_state and cancels on event021_hold_capital_failed. event021_secure_rail_spine_mission now gates activation and availability on event021_secure_rail_mission_target_valid, and cancels when event021_rail_spine_lost is set. A raw-block comparison found 21 of 21 ai_will_do blocks byte-for-byte identical between the snapshot and current source.

The rail target helper is common/scripted_triggers/021_random_civil_war_parent_triggers.txt, identifier event021_secure_rail_mission_target_valid. It requires random_civil_war_rail_mission_state, an existing state owned and controlled by ROOT, membership in ROOT.random_civil_war_opening_core_states, and a supply node or sufficient infrastructure.

## MCP route and result

All evidence is read-only. MCP source hashes below are analyzer hashes and are distinct from the verified raw file hashes above.

| Operation | Result and evidence |
| --- | --- |
| probability_inspect, decision_ai_will_do, post-edit source | PROBABILITY_SOURCE_INSPECTED; revision ffa62562a9076f5886d348b07261ee17dcda9983a5340e14fab0f2a366ff2d5c; analyzer source hash dd7464a0ba56c2e0060a5b9944baf0b13693e29255d741626dae4d9a54b161ce; 18 candidates; poolComplete false; 12 required inputs. |
| probability_inspect, mission_ai_will_do, post-edit source | PROBABILITY_SOURCE_INSPECTED; revision dfd7d8c4623fa0e09b91e2e18868b10d2779fc3c18d2c523b51e97d8869545fc; same analyzer source hash; 3 candidates; poolComplete false; 3 required inputs. |
| probability_inspect, decision_ai_will_do, pre-edit snapshot | PROBABILITY_SOURCE_DISCOVERED with discoveryReason no_weighted_surfaces; revision 9d1197843f94308e844e6a226015d0eab3f145db80c95ae58f99b675312829b; analyzer source hash 60f9751866c7a76c77b9255eadafb9ef242b92385ceebf3ff8ea01fb6f1abb0c; 0 candidates. |
| probability_inspect, mission_ai_will_do, pre-edit snapshot | PROBABILITY_SOURCE_DISCOVERED with discoveryReason no_weighted_surfaces; revision 2dcd2b2ad5d44beef9f3bbdcbe2ef17cc9174c577391f2902820dd1bdfc00914; same analyzer source hash; 0 candidates. |
| probability_compare, decision_ai_will_do, relative paths | PROBABILITY_SURFACE_EMPTY; “No weighted blocks matched this request” for the preserved before.path; no files scanned, artifacts, or comparison id. |
| probability_compare, mission_ai_will_do, relative paths | PROBABILITY_SURFACE_EMPTY for the same preserved before.path; no files scanned, artifacts, or comparison id. |
| probability_compare, both adapters, absolute paths retry | INTERNAL_ERROR, “Unexpected internal error”; no files scanned, artifacts, or comparison ids. |
| probability_evaluate, decision_ai_will_do, post-edit source | PROBABILITY_ANALYZED_PARTIAL; revision 84587b5004d302ea691809bb7201ce7bd0078167f95f1c40dfc72dc10085176f; source hash dd7464a0ba56c2e0060a5b9944baf0b13693e29255d741626dae4d9a54b161ce; scenario hash 69bf28ed34aa34e75cb7af9b991d1b0af7eee5480b4a0cb8bcf9abbafd9ad714; 108 candidate-scenario rows; 48 unresolved items; 10 diagnostics. |
| probability_evaluate, mission_ai_will_do, post-edit source | PROBABILITY_ANALYZED_PARTIAL; revision c7d472b070c6e6d6202c0e438ace0f056c9af20da5974c2e5f0c287f62e9479f; same source and scenario hashes; 18 candidate-scenario rows; 8 unresolved items; 0 diagnostics. |
| probability_render, both evaluation ids | PROBABILITY_ANALYSIS_NOT_CACHED for probability-831f0f18918fb9cf5883af62 and probability-2a5bdc172da56f02b85b8d3b. The evaluate calls themselves emitted ranking, matrix, waterfall, and unresolved visual artifacts listed below. |

The baseline inspector’s zero-candidate result conflicts with the source contents: the supplied snapshot contains 21 ai_will_do blocks, and all 21 match the post-edit blocks exactly. MCP therefore did not establish a numeric before-and-after delta. No comparison id was produced.

The adapter evidence classifies both decision and mission ai_will_do as score_only, with rawScore supported, normalizedProbability false, and selection probability not modeled. Neither scores nor ranks are click probabilities. The adapter reports completePoolRequired false, but every fixture result still reports poolComplete false; no complete game-wide decision or mission selection pool was established.

## Scenario completeness

The exact saved scenario set is event021_mission_ai_source_flags_2026-09-26, scenario hash 69bf28ed34aa34e75cb7af9b991d1b0af7eee5480b4a0cb8bcf9abbafd9ad714.

| Scenario id | Declared source flags |
| --- | --- |
| DM-01-CAPITAL-GOVERNMENT | random_civil_war_active; random_civil_war_government_side |
| DM-02-CAPITAL-OPPOSITION | random_civil_war_active; random_civil_war_opposition_side |
| DM-03-CAPITAL-EVENT006 | random_civil_war_active; random_civil_war_event6_front_active |
| DM-04-RAIL-RECONSTRUCTION | random_civil_war_active; random_civil_war_reconstruction_phase; random_civil_war_government_side |
| DM-05-RAIL-OPPOSITION-EVENT006 | random_civil_war_active; random_civil_war_reconstruction_phase; random_civil_war_opposition_side; random_civil_war_event6_front_active |
| DM-06-SETTLEMENT-NEGOTIATOR | random_civil_war_active; random_civil_war_settlement_phase; random_civil_war_negotiator_profile |

Every row uses actor POL, state {}, and scopes {}. No typed Clausewitz variables, unsupported fixture fields, or invented state facts were added.

These are score/willingness fixtures only. The fixture has no capital or rail target state, ownership/control, infrastructure, supply, opening-core array, equipment stockpile, political power, command power, war state, authority variable, exposure-target scope, or settlement hold-until variable. External factors and campaign availability are incomplete.

## Post-edit score evidence

Numeric entries are the MCP raw ai_will_do scores for the declared flags and current constants. “?” means the MCP returned rawValue null because a required source input was unresolved. All decision candidates remain eligibility unresolved in every fixture, including candidates with numeric scores.

| Decision id | DM-01 | DM-02 | DM-03 | DM-04 | DM-05 | DM-06 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| event021_complete_coalition_governance | 1 | 1 | 1 | 1 | 1 | 1.5 |
| event021_complete_disarmament | 1.5 | 1 | 1 | 1.5 | 1 | 1 |
| event021_defend_capital | ? | ? | ? | ? | ? | ? |
| event021_end_sponsor_commitment | 1 | 1 | 1 | 1 | 1 | 1.5 |
| event021_integrate_formations | 1 | 1 | 1 | 1 | 1 | 1 |
| event021_monitor_border | 1 | 1 | 1 | 1 | 1 | 1 |
| event021_offer_emergency_settlement | ? | ? | ? | ? | ? | ? |
| event021_offer_mediation | ? | ? | ? | ? | ? | ? |
| event021_open_relief_corridor | 1 | 1 | 1 | 1 | 1 | 1 |
| event021_protect_communications | 1 | 1 | 1 | 1 | 1 | 1 |
| event021_reconstruct_administration | 1 | 1 | 1 | 1 | 1 | 1 |
| event021_review_loyalty | ? | ? | ? | ? | ? | ? |
| event021_review_regional_administration | ? | ? | ? | ? | ? | ? |
| event021_secure_arsenals | 1.5 | 1 | 1 | 1.5 | 1 | 1 |
| event021_seize_depot | ? | ? | ? | ? | ? | ? |
| event021_set_priority_front | 1 | 1 | 1 | 1 | 1 | 1 |
| event021_support_government | ? | ? | ? | ? | ? | ? |
| event021_support_opposition | ? | ? | ? | ? | ? | ? |

The source base for each decision is event021_ai.base_action = 1. In the government and reconstruction-government fixtures, random_civil_war_government_side raises event021_complete_disarmament and event021_secure_arsenals to 1.5. In the settlement-negotiator fixture, random_civil_war_negotiator_profile raises event021_complete_coalition_governance and event021_end_sponsor_commitment to 1.5. Other numeric scores remain at the base in these fixtures. These are exact source-score observations, not evidence that the decisions are available.

The eight unresolved decision scores are event021_defend_capital, event021_offer_emergency_settlement, event021_offer_mediation, event021_review_loyalty, event021_review_regional_administration, event021_seize_depot, event021_support_government, and event021_support_opposition. Their traces require unavailable campaign inputs including capital_scope, random_civil_war_state_authority, random_civil_war_priority_front_state, random_civil_war_exposure_source_country_scope, political power, command power, equipment, war state, surrender progress, or unsupported compound/hidden trigger evaluation.

| Mission id | DM-01 | DM-02 | DM-03 | DM-04 | DM-05 | DM-06 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| event021_hold_the_capital_mission | 1.5 | 1.5 | 1.5 | 1.5 | 2.25 | 1 |
| event021_secure_rail_spine_mission | 1 | 1.5 | 1.5 | 1.5 | 3.375 | 1 |
| event021_hold_settlement_terms_mission | 1 | 1 | 1 | 1 | 1 | 1.5 |

All three mission scores are exact for the flags supplied. The hold-capital score applies priority_major for the declared side or Event006 flags; DM-05 activates two of its score modifiers. The rail score applies priority_major for reconstruction, opposition, and Event006 flags; DM-05 activates all three. The settlement-terms score applies priority_major only in DM-06. The MCP values show DM-05 rail at 3.375 above hold-capital at 2.25, and DM-06 settlement terms at 1.5 above the other two missions at 1. These score-only rank reversals are exact within the source-flag fixtures and do not establish campaign selection or availability.

Mission eligibility remains unresolved for every candidate in every fixture. The capital mission requires unresolved custom_trigger_tooltip/state conditions. The rail mission requires an actual target state and the helper event021_secure_rail_mission_target_valid, which depends on has_variable, var:random_civil_war_rail_mission_state, ownership/control, opening-core membership, and supply or infrastructure. The settlement mission requires random_civil_war_settlement_terms_hold_until, settlement-obligation state, and custom_trigger_tooltip evaluation.

The ranking SVG for the decision analysis renders null score entries as 0.00000. Those eight candidates are unresolved in the JSON and must not be treated as exact zero-weight or impossible outcomes. The JSON and unresolved artifacts take precedence for those entries.

## Risk findings and limits

Observed score-layer dominance is limited to DM-05 rail over hold-capital. The decision fixtures show 1.5 modifiers only for the explicit government or negotiator flags; no single numeric decision weight dominates all six fixtures. No calculable mission score is zero, and no calculable decision score is zero, so no score starvation is observed in the declared fixtures. Starvation and dominance in a real campaign remain unresolved because candidate availability and external factors are incomplete.

Rank changes are present in source-flag score traces as described above. Candidate ranks are not a selection probability, and ties at equal scores do not establish priority between candidates.

AI validity and positive weight on impossible choices are unresolved. Every Event 021 decision and mission has unresolved eligibility in these fixtures, so the analyzer cannot prove that a positive score belongs to a valid candidate or that a blocked candidate is actually selectable.

Repetition and exploit risk are unresolved. All three mission definitions use fire_only_once = no; the probability adapters did not model cooldown, success/failure lifecycle, target reset, repeated activation, or sequence behavior. No custom weighted pool with complete candidates, cadence, transitions, or terminal states was declared.

No unsafe snowball or campaign balance conclusion is supported. No exact selection probability, normalized probability, timing distribution, simulation, or sequence result was produced.

## Recommended follow-up, not applied

Do not tune or alter AI weights based on this partial pass. The source review shows that this plumbing patch changed none of the 21 ai_will_do blocks, while the required MCP comparison remains unavailable.

Repair the MCP baseline-source route so probability_inspect and probability_compare can recognize the immutable file under docs/plans/021_random_civil_war_plans/probability_snapshots/event021_decisions_before_2026-09-26/021_random_civil_war_decisions.txt. Do not substitute the current source for the baseline. Repeat probability_compare for both decision_ai_will_do and mission_ai_will_do with the same scenario set and retain the returned comparison ids and artifacts.

For any later availability pass, use only adapter-supported scenario inputs to resolve the capital target, rail target, settlement hold-until state, resource gates, and target scopes named above. The existing JSON is intentionally source-flag-only; do not add unsupported fields or fabricate campaign facts.

If mission repetition is a concern, evaluate the existing activation, completion, timeout, cancellation, and target-reset lifecycle separately with a valid declared campaign scenario before changing any weight. Relevant ids are event021_hold_the_capital_mission, event021_secure_rail_spine_mission, and event021_hold_settlement_terms_mission.

## Skipped analyses and evidence references

probability_sweep was skipped because the supplied state records contain no numeric values or declared sweep ranges, and the patch changed no weight coefficient. Sweeping a guessed state value would invent an input. probability_simulate was skipped because no uncertain input distributions or seed were declared. probability_sequence was skipped because this is not a complete declared custom pool with cadence, transitions, and terminal states. The explicit probability_render calls returned PROBABILITY_ANALYSIS_NOT_CACHED; the evaluate calls nevertheless emitted the SVG ranking, matrix, waterfall, and unresolved artifacts listed below.

Offline references reviewed: paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md; Decision modding - Hearts of Iron 4 Wiki.md; Triggers - Hearts of Iron 4 Wiki.md; Scopes - Hearts of Iron 4 Wiki.md; Modifiers - Hearts of Iron 4 Wiki.md; Data structures - Hearts of Iron 4 Wiki.md. Vanilla references reviewed: documentation/triggers_documentation.md, effects_documentation.md, script_concept_documentation.md, including has_country_flag, has_variable, activate_mission, clear_variable, set_variable, and script-constant usage. The wiki distinguishes ai_will_do score/race behavior from ai_chance probability-proportional sampling; the MCP adapters for this audit explicitly expose score_only and no normalized probability.

MCP workspace id: mod_chaos_redux_ea3b2d67c2c0.

Post-edit decision inspect: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a805ea89c14818744ccaed774cefebbb38b1054856e635b70dbc7390460780a8/de04bae5ab6ad509d56e925097d3c8cae370ac086a312db2e751f6207cebb095/probability-inspect-dd7464a0ba56.json

Post-edit mission inspect: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f320ec25ff1e9dbd189bd8676b4bdfe1945ccc505ea38e459f750954d479a8ba/019605fb3c575e627aad2b6025622b2866b0b281fe3c725c1ff1390584ba01f4/probability-inspect-dd7464a0ba56.json

Pre-edit decision inspect: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b1df5af6dc56aa59ab486932d79489d1bd5a3950fd23bbde99af2f132117ad66/d27b76c6c2a9c62472f0787b99cbd3bcc4a5a81de810c95074f0f1984b8938b3/probability-inspect-60f9751866c7.json

Pre-edit mission inspect: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2d7d537a6b00955927ee3e5f661aed262a9fafbbf4d1c182028ac652af788ebd/90266382e3061b60b2d61b9efc1ce11358af02de4c6e85b175f6bd7099ffcf34/probability-inspect-60f9751866c7.json

Decision evaluation JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1f6ad690b66cacfad6c0120936496d97274d6931978ca7631a7e474401ab05f3/4af7b24c4704d92e5f61cb46072b4133a4a43825181bca28127aa730c5be6bf3/probability-831f0f18918fb9cf5883af62.json

Decision ranking SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f172cb52803ea8d531f8c1d37eb8c18c069eebe5eb0496e8ab47f9a1611e01ac/bd697fc10132eb4ec22bd9e54665265d1f3fe445b35d418e92f3f7e1ce7f530d/probability-probability-831f0f18918fb9cf5883af62-ranking.svg

Decision matrix SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/601d85f52d39ee5f7878fe15d52dfe74a19e8d1bee6fd044e3ebdf82afff39c8/66e265fbc72cf8fcf89d56fd9715b1842794dab359f273bef31e06d8a51c4b30/probability-probability-831f0f18918fb9cf5883af62-matrix.svg

Decision waterfall SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/13b7fefddbdb1ba2d7f5a6deecf0c8937ad12cd0f685454bec971a4269a036e7/bf3c48d37a2938622cf7395ac366c011f48291ab5ee4e81d2b53693ec3192cff/probability-probability-831f0f18918fb9cf5883af62-waterfall.svg

Decision unresolved SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/235e5b2303b7a27dfc28c8771b43df6fa6ae452bbaab83511c8f8d8274d8b196/9de802d8f2efee57c6e1f703c61d361cc1e7f5ad702e1b31b6fe1285b1cdcd6b/probability-probability-831f0f18918fb9cf5883af62-unresolved.svg

Mission evaluation JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d9634ee2002057fee27ee392e2786d62f56e61fcd173337272db41d6a7a9ece9/52a37957dd780687e3ba7fc9412db54593b757934085dc19396146e9dd178fea/probability-2a5bdc172da56f02b85b8d3b.json

Mission ranking SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8db407cd89b202bb31790bd2b9d211e61d788f26acd5ad122e60276eab53a6ea/b2b11ede0a77fdca25c144327659b0f3432c5d9127b67fdb44a3c43b8cc02824/probability-probability-2a5bdc172da56f02b85b8d3b-ranking.svg

Mission matrix SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d73c70342be0790e9dcab8f5e530449fd77e5d76b8d2b741236b05cd277721f5/dc8ebd660d28cacfe62a7fa70a1706696be8793fef10dda41ac4e222a7bdda31/probability-probability-2a5bdc172da56f02b85b8d3b-matrix.svg

Mission waterfall SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0ea5f7ce4ceb7f1ba93acb01a8728053a3d64dd9390dc9326162a3640eb0326c/45eb9ebfcee2d9a5b1e40d9ac142f426c64c5ba89de346298f1e4db29783d158/probability-probability-2a5bdc172da56f02b85b8d3b-waterfall.svg

Mission unresolved SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4a1661329216d61843bb456af93f15cebccf726768a4c60e1249532a2b6ee1ee/d2d11641bf279d5264aae5d9efed1a5b70d012de819cca5a9ae2d6c221ee8a76/probability-probability-2a5bdc172da56f02b85b8d3b-unresolved.svg

Artifact transport note: both JSON evidence artifacts were retrieved with bounded byte-range reads, contiguous offsets, base64 validation, exact declared-size coverage (211,170 and 1,308,446 bytes), and successful JSON parsing. The server marked the final tail complete=false while returning no continuation URI; the full declared byte range was nevertheless present and valid JSON.

Disposition: unresolved. The required MCP before-and-after compare is blocked by the baseline adapter discovery failure and absolute-path internal error. The source-level finding that the 21 AI blocks did not change does not replace the missing MCP comparison.
