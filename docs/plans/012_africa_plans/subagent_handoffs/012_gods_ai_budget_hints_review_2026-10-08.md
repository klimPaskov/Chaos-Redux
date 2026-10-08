# Event012 Gods: AI Budget Hint Review

Status: The source mapping audit is complete. The single requested probability comparison did not return during its bounded wait, so score-level before/after evidence is unresolved. The observer/server outcome is unknown; this is not evidence that the probability route failed.

This review is limited to the nine fixed-cost decision AI saving hints in common/decisions/012_africa_gods_decisions.txt and is separate from the response-phase audit. No gameplay, AI, effect, trigger, event, localisation, Git, or game files were edited by this auditor.

The immutable BEFORE file is docs/plans/012_africa_plans/subagent_handoffs/012_gods_ai_budget_hints_review_2026-10-08_evidence/before/012_africa_gods_decisions.txt, 91,135 bytes, SHA-256 e808262b60c0ff34cfd6c0eac146fcb53f6ced3bb6d58bcc157799fe48720f93. Its bytes matched the parent-verified pre-patch hash.

The immutable AFTER file is docs/plans/012_africa_plans/subagent_handoffs/012_gods_ai_budget_hints_review_2026-10-08_evidence/after/012_africa_gods_decisions.txt, 92,838 bytes, SHA-256 ae732079d66e081b0b6a13fbbe411b42936722009652639106d42d2b2144bfb9. A byte-backed unified comparison found the nine requested ai_hint_pp_cost insertions, nine matching file-local literals, and the reconciliation explanation; no other decision-body changes appeared in that comparison. Parent reports commit dbed4c7db0337dcce216fc9f9c545be6e0143814, 21 source-validation groups passed, all ten total hints match their shared fixed charges, and a separate AST comparison proved every decision body unchanged after excluding hints and macros.

## Audited field mapping

| Decision id | Hint literal | Shared fixed charge | Payment owner |
| --- | --- | --- | --- |
| gods_of_africa_ultimatum_pay_settlement | GODS_OF_AFRICA_ULTIMATUM_PP_COST = 150 | gods_of_africa_ultimatum.settlement_pp = 150 | common/scripted_effects/012_africa_gods_punishment_effects.txt |
| gods_of_africa_council_speech | GODS_OF_AFRICA_COUNCIL_SPEECH_PP_COST = 25 | gods_of_africa_council.speech_pp = 25 | common/scripted_effects/012_africa_gods_focus_payoff_effects.txt |
| gods_of_africa_prepare_defensive_defiance | GODS_OF_AFRICA_DEFENSIVE_PREPARATION_PP_COST = 15 | gods_of_africa_transaction.defensive_preparation_pp_cost = 15 | common/scripted_effects/012_africa_gods_effects.txt |
| gods_of_africa_harden_stockpiles | GODS_OF_AFRICA_DEFENSIVE_STOCKPILE_PP_COST = 15 | gods_of_africa_transaction.defensive_stockpile_pp_cost = 15 | common/scripted_effects/012_africa_gods_effects.txt |
| gods_of_africa_secure_transport | GODS_OF_AFRICA_DEFENSIVE_TRANSPORT_PP_COST = 15 | gods_of_africa_transaction.defensive_transport_pp_cost = 15 | common/scripted_effects/012_africa_gods_effects.txt |
| gods_of_africa_prepare_countermeasures | GODS_OF_AFRICA_DEFENSIVE_COUNTERMEASURE_PP_COST = 15 | gods_of_africa_transaction.defensive_countermeasure_pp_cost = 15 | common/scripted_effects/012_africa_gods_effects.txt |
| gods_of_africa_arm_offender_enemies | GODS_OF_AFRICA_COALITION_PP_COST = 25 | gods_of_africa_coalition.pp_cost = 25 | common/scripted_effects/012_africa_gods_punishment_effects.txt |
| gods_of_africa_send_expedition | GODS_OF_AFRICA_EXPEDITION_PP_COST = 25 | gods_of_africa_expedition.pp_cost = 25 | common/scripted_effects/012_africa_gods_focus_payoff_effects.txt |
| gods_of_africa_coerce_occupier | GODS_OF_AFRICA_OCCUPIER_COERCION_PP_COST = 50 | gods_of_africa_occupier_coercion.pp_cost = 50 | common/scripted_effects/012_africa_gods_focus_payoff_effects.txt |

The source payment effects deduct the same shared constants shown above, and the corresponding affordability triggers test those fixed amounts. The existing protect-partner hint remains 10 PP and is outside the nine-row patch.

gods_of_africa_seek_reconciliation is intentionally not given a fixed hint. Its row offers free victor recognition through gods_of_africa_victor_can_request_relegitimation, or a paid reconciliation branch whose shared cost is gods_of_africa_transaction.reconciliation_pp_amount = 10. The scripted effect takes the victor branch first and deducts 10 PP only in the paid branch. A row-wide hint of 10 would misstate the free route. Preserve this zero-hint behavior and the existing price and branching UI.

## Probability evidence and limits

The required initial hoi4.probability_inspect completed with status ok and code PROBABILITY_SOURCE_INSPECTED for adapter decision_ai_will_do. Workspace: mod_chaos_redux_ea3b2d67c2c0. It scanned the frozen BEFORE source and found nine candidates, poolComplete true for the requested ids, zero required inputs, and zero unresolved findings. Its sourceRevision is 44f8b0fa155818a203c3e199c7fbf6cc24c853de31d65fd73b33ac6b994acfb8; request sourceHash is 2c6fa0d5568483f04bcf485fdfe79d1791b6b2caada44c7ac489615858de08ab. Candidate provenance records the raw BEFORE source hash e808262b60c0ff34cfd6c0eac146fcb53f6ced3bb6d58bcc157799fe48720f93.

The adapter artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d5fc22b3b7e78de69cbd57e64e444f0c9f5a69e0e6389d214aabb931cdd6feb5/fa6e880af12c53b8be84992c0b98bc3d691761df5c187d2d9adfa32e96754bba/probability-inspect-2c6fa0d55684.json. Its 368,110 bytes were assembled in contiguous byte ranges and the content SHA-256 matched the artifact SHA. The artifact states selectionRule score_only, normalizedProbability false, completePoolRequired false, rawScore and eligibility supported, and selection probability, sequence, and time distribution not modeled.

One hoi4.probability_compare was submitted with the BEFORE and AFTER snapshot selectors, candidatePool containing only gods_of_africa_ultimatum_pay_settlement, scenarioSet id gods_of_africa_fixed_pp_hint_thresholds_2026-10-08, scenario id ultimatum_pp_150_exact_150, state political_power = 150, and outputs json and unresolved only. It remained pending after one 30-second bounded wait, after which this auditor stopped observing it as instructed. No comparison id, result artifact, scenario hash, score trace, or rendered URI was returned. The comparison outcome is unresolved and the observer/server outcome is unknown.

An earlier wider evaluate request covered nine candidates across the nine threshold scenarios and was stopped without a returned result. A later reduced three-candidate, nine-scenario evaluate was still pending when the user interrupted that turn. Neither request returned evidence; neither is treated as a route failure. No additional evaluate, sweep, simulation, sequence, or render was run after the user narrowed the task.

The named fixture file is docs/plans/012_africa_plans/subagent_handoffs/012_gods_ai_budget_hints_review_2026-10-08_evidence/scenarios_fixed_cost_boundaries.json, SHA-256 f7975088f48e6e00b0c97733f8b83327d7bb30a9e47a7d78cea206326b66e336. The compare used the exact ultimatum_pp_150_exact_150 case from that fixture. No MCP scenario hash was returned.

## Interpretation

The source review proves the nine metadata values map to the fixed costs and that the payment owners and eligibility gates are unchanged. The source AI score expressions remain unchanged per the parent-reported AST comparison. Their existing base expressions include ultimatum_settlement_base, council_speech_base, defense_base for the four defensive actions, coalition_base, expedition_base, and coercion_base. No numeric before/after score values or modifier traces were returned, and no ranking, rank reversal, or timing result is available.

Decision ai_will_do values are willingness scores, not click probabilities. More specifically, the inspected adapter covers decision ai_will_do blocks and does not claim to model native ai_hint_pp_cost saving behavior. This audit therefore makes no claim that the AI saves, spends, or selects a decision at 150 PP. The exact-150 fixture is only the declared scenario input; its eligibility and helper state were not forced. Campaign flags, event targets, decision targets, and other runtime state remain incomplete for engine-behavior claims.

No dominance, starvation, repetition, or exploit result is established. The fixed costs and decision bodies were not changed, so this patch introduces no source-side willingness change according to the parent AST comparison. Whether concurrent hints alter PP hoarding or starve other spending is an unresolved native-engine risk and is outside this score adapter.

## Reference and source evidence

The offline wiki Decision modding section, id 0a37b9f1ad43a16c2d85d25b307d261fcc9e60292b4e164c335c03816535e4d8, revision 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162, lines 284–336, says ai_hint_pp_cost is a constant amount that tells the AI to budget for a custom decision cost. This supports the static hint mapping but does not prove engine behavior.

Installed game common/decisions/_documentation.md, id c8ba2a44d708fd3048c019dfb9e36f3ecf59ff754f7cb4ea3bb7c4704deb5c58, revision 5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019, lines 1–46, documents decision gate scopes and check cadence.

Installed common/script_constants/documentation.md, id 48deec564822a81f6806514736148c344258acac56db7e9989998ed30dd26b68, revision e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c, lines 1–34, limits script-constant usage to documented fields. Installed script_concept_documentation.md, id c859ab9d6a857bfc830f89b36b004514b78ee454e001a80238a9d1f7b355ccd0, revision 884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7, lines 216–222, describes script constants and the file-local @ macro. The file-local numeric literals keep the hint fields static while comments tie them to shared costs.

Vanilla source lookup revision e48072d49d9032bcd239a6c3e1f0b0b8b02741a1b9fdcf519630dc7a080b36f8 located game:common/decisions/CHI_decisions.txt, decision CHI_press_warlord_to_become_puppet, with ai_hint_pp_cost = 125 at line 7922. It is the vanilla precedent for a static hint alongside an AI-weighted decision.

## Recommendation and remaining blocker

Keep the nine listed hint-to-charge mappings and their file-local literals in common/decisions/012_africa_gods_decisions.txt. Keep the existing 10 PP protect-partner hint and leave seek-reconciliation without a fixed hint. Do not change costs, ai_will_do blocks, triggers, effects, outcomes, or branching UI based on this bounded audit.

The source mapping review is complete. The numeric before/after comparison remains unresolved because the one requested MCP compare did not return within the allowed wait; there is no returned compare receipt to attach. Parent may use the source and AST validation evidence for its commit while retaining this limitation.
