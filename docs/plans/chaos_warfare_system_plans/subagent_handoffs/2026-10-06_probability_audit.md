# CBRN AI and probability audit handoff

Audit status: incomplete with scenario-specific partial evidence.

This was a read-only audit; no gameplay, AI, event, decision, raid, effect, trigger, localisation, or runtime source was changed, and no commit was made.

Repository HEAD at report time was e08c6fadfeca19934617a2fe6a98f13e178f906a.

## Instructions and references reviewed

Read AGENTS.md, the chaos-redux-subagents, chaos-redux-decisions-missions, chaos-redux-mtth, and chaos-redux-events skills, the 2026-10-05 remaining-work plan, and the relevant entries in agent_decisions_2026-10-04.md.

Read offline paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md lines 26-45, Event modding - Hearts of Iron 4 Wiki.md lines 159-176, and Decision modding - Hearts of Iron 4 Wiki.md lines 361-388.

Read installed documentation/triggers_documentation.md lines 2110-2132 and 5033-5040, dynamic_variables_documentation.md lines 439-444, installed common/raids/_documentation.md lines 66-69 and 100-126, and the vanilla AUS targeted-decision precedent at common/decisions/AUS.txt lines 125-159.

The references distinguish ai_will_do willingness scores from ai_chance probability-proportional sampling and random_list selection.

The has_war_support expression in the doomsday raid is valid: the installed dynamic-variable documentation lists it as an auto-generated dynamic variable, as well as a native country trigger.

## Audited surfaces and source identity

| Surface | Current source files and identifiers | Source identity |
| --- | --- | --- |
| Untimed CBRN decision scores | common/decisions/cbrn_protection_decisions.txt; cbrn_reconcile_occupied_mask_records and cbrn_reconcile_export_shipment_records | Raw SHA-256 D263E1803A5DBD2B760F78A4F79A29EDFDD910B770B79A78600220327AFDC790 |
| Timed mask procurement and occupied/export actions | common/decisions/cbrn_protection_decisions.txt; cbrn_recondition_old_masks, cbrn_export_protective_equipment, cbrn_supply_occupied_population, cbrn_supply_occupied_population_sale | Raw SHA-256 D263E1803A5DBD2B760F78A4F79A29EDFDD910B770B79A78600220327AFDC790 |
| External protective-aid payment readiness | common/decisions/cbrn_occupation_decisions.txt; cbrn_deploy_protective_aid and cbrn_deploy_protective_aid_sale; common/scripted_triggers/cbrn_protective_aid_decision_triggers.txt | Raw SHA-256 7247630690F01A17DF3DDB41C51335984CC17D6E99AB63474129C9CDA741E4F3 for decisions and 7425B9992FB449A6BF3E2BE7D701D1932D790D84FF6BE52B5CCAE518D0B98164 for readiness triggers |
| Occupied/export reconciliation gates | common/scripted_triggers/cbrn_occupied_transaction_triggers.txt and cbrn_export_transaction_triggers.txt | Raw SHA-256 46EF50E95617F61DB386D1F243E36EA10EBF4C54B467902EBABC00BD16B13CF6 and 59256F7AF885DA05DA29EC5DB12BBC5D7869AAF5ED7B0ADE0F9A7952EEF4D39F |
| Biological sabotage raid target gate | common/scripted_triggers/biological_sabotage_triggers.txt, especially bio_sabotage_ai_may_target_state; shared actor contract in the same file; human/launch wrapper in common/scripted_triggers/biological_sabotage_raid_triggers.txt | Raw SHA-256 6AA9F022C49579F296F0C5921ED4130D83B3F54B8A7FD8E733CF35D11F679500 and 79048687FA29324E545E0DF75296F40C3B5873C0287049479FBD9D8DD7AE0160 |
| Native biological sabotage raid AI | common/raids/biological_sabotage_raids.txt; 12 base/theater/terminal raid candidates | Raw SHA-256 D1E055B63794B1C8784255A0EC59B1E1D792F4A60921D7D2E02B47B3209DCCC5 |
| Chemical doomsday raid AI | common/raids/cbrn_doomsday_raids.txt and common/script_constants/chemical_warfare_constants.txt | Raw SHA-256 558FC927880A094483A6B551F173470FA8467E1A9E0BBC05161AFBD4B9B9C799 and C400243BB1806EFB1494DC8E865BF10D7EFB93309006A6E838C2F60F7FE65993 |
| Treaty invitation option scores | events/chemical_warfare_events.txt; chaosx_contamination.9.a and chaosx_contamination.9.b; constant table in common/script_constants/fallout_consolidated_constants.txt | Raw SHA-256 4EA2CEFABC07BC30E8E67233B24B26BA2056ADB2A6C0EC5899ADB3D81715C43E and BFAD5A45F90DA32040E04E26D7F4CB324941C2E96D08BEF1A09C5A169E658056 |
| Single-option event chance | events/cbrn_protection_events.txt; cbrn_protection.2.a | Raw SHA-256 84A3B4195D8E691FD917B02723BF796D1BF8CDE0E1D3B87DB78DD6059F15923A |
| Defective-mask random list | common/scripted_effects/cbrn_protection_decision_effects.txt; cbrn_complete_mask_reconditioning | Raw SHA-256 3931110C80D36DCE6379FB10DD87386720D391222F2FFBCDCAED659ECE129B1B |

The corrected biological sabotage predicate is actually defined in biological_sabotage_triggers.txt, while biological_sabotage_raid_triggers.txt calls the shared country relationship helper from the native raid wrapper.

## Returned HOI4 probability evidence

All current tool results used workspace mod_chaos_redux_ea3b2d67c2c0 and the verified Operation Postern 1.19.2.0 (d245) adapter target.

The decision_ai_will_do inspection of common/decisions/cbrn_protection_decisions.txt found seven untimed candidates and reported poolComplete=false, source hash c1d7aeb94f5957bfcbbc66a7229715717212678f2be066d46d32a2c5e7da5a56, source revision 57eb36359d8841ec2ae87513181ab9c709fa8094f98d1e3332219e6fc9f625d5, and required inputs including FROM, controlled/enemy-state enumeration, the emergency-fee quote variables, and helper scopes. Its adapter declares selectionRule=score_only and normalizedProbability=false. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a706feb72537112ed478fd02fa5368037e8882ec50ff62db4dbd63089a5a6840/cd817ee7a2834fc344deddac68a18612443de6db7ab8068b5e5257d1157c98d4/probability-inspect-c1d7aeb94f59.json.

Its seven discovered IDs are cbrn_emergency_state_mask_distribution, cbrn_keep_industry_operating, cbrn_move_civilians_to_shelters, cbrn_protect_hospitals_and_utilities, cbrn_reconcile_export_shipment_records, cbrn_reconcile_occupied_mask_records, and cbrn_sound_chemical_alarm.

A second decision_ai_will_do inspection of common/decisions/cbrn_occupation_decisions.txt found six untimed candidates, poolComplete=false, source hash 7551437660a6977c9ba69b84c4a1520c461a449c6e6a5521b2a762c33114616e, source revision df88493e38744c368f84ea9b12ed068fb2a2607e702879946e2bb562d144ab96, and ten required scope/expression inputs. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/60763c7695d140dacf06af6a1a047f8dc5354f8485e0a14e82a38413d0fbf92f/4fd571e60a7f5b8af2a31f63d1b7779f0101ef063e73ec9e3b39e5678a7aa654/probability-inspect-7551437660a6.json.

The mission_ai_will_do inspection of common/decisions/cbrn_protection_decisions.txt returned eight timed candidates, poolComplete=false, 28 required input paths, source hash c1d7aeb94f5957bfcbbc66a7229715717212678f2be066d46d32a2c5e7da5a56, and source revision 470c2e5dbd0b3e8f012a610c536d899ec521f2a41f24b8abeed3b864a2f7fcec. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/95080669deaf4790a9f567b88721524b0deffcc4687fd7f16237e6cb4ab4c234/eb0fd759eb175a04e5aed7268d8a724cefa047ff6cc282f8442dc7cb71bae0b4/probability-inspect-c1d7aeb94f59.json.

The mission_ai_will_do inspection of common/decisions/cbrn_occupation_decisions.txt did not return before parent-directed cutoff after approximately seven minutes. It produced no usable inline candidate inventory, revision, or artifact URI, so the protective-aid mission weights remain uninspected by their matching adapter.

The random_list inspection of common/scripted_effects/cbrn_protection_decision_effects.txt returned two candidates, poolComplete=true, no required inputs, source hash fb71d98e7788859aca1bde595adb37869b9c6cee20e3281942470564c081dc48, and source revision 892147cde179a5566eea4135389c9cab2ffb4fd630430c32dbed6ef01ddc00d9. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c50203af1c604644e34217897cb8eb0427e729e360da44bdd8ee7bdb1ee15cd5/1f6b8fd8e82842e2714384452244ad9162d7fcb45f8dad0101dfcf976bebd8b4/probability-inspect-fb71d98e7788.json.

A bounded decision_ai_will_do inspection of common/scripted_triggers/biological_sabotage_raid_triggers.txt discovered no weighted surface, and an ai_strategy_factor inspection of common/raids/cbrn_doomsday_raids.txt returned PROBABILITY_SOURCE_DISCOVERED with no weighted candidates. The actual native raid ai_will_do definitions are in biological_sabotage_raids.txt and cbrn_doomsday_raids.txt, and no adapter in the exposed enum models that native raid field. The doomsday inspect source hash was 12b22e7189f2735a4dbd8dac62bdc356da59ac4372745c1b33ffce802975a6db, revision 9b580a9d311c4b2e553fdf6107969582cd2a20799597c86d0096645ba80d6739, artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/767a4a4059ccda78264787897a7b6bad4255a2011cc4195fa527abd77a66c7d6/22e559f97f240fda16cd0b4ad40f3a0a1784f8d22da47710278df06eb442a548/probability-inspect-12b22e7189f2.json.

The CBRN reconciliation current evaluation used candidatePoolHash 1efd50836783c9b65968741c9a7acce228c1da22278e25e243cbe8ac58e11844, two candidates, raw_value only, and score-only decision_ai_will_do analysis. The scenario set CBRN_RECONCILIATION_BOUND_2026_10_06 has scenario hash a30d92885289c775bebca35a306b92de75c6a61812d316365c2911a2f364697b and analysis id probability-ed49ad87705460a5b55fcd01. The MCP returned PROBABILITY_ANALYZED_PARTIAL, 12 candidate rows across six scenarios, zero eligible candidates, ten excluded rows, four unresolved items, two unresolved candidates, and the warning PROBABILITY_OUTCOME_NEVER_ELIGIBLE for cbrn_reconcile_export_shipment_records. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4e127210f3956bc7c26b3046ae809f8e872e202424b18b040b3777428003eb26/070aa5dd76b9aef8f954e45027ead3cd500485f048832f40be7e5c01bdcc35e1/probability-ed49ad87705460a5b55fcd01.json.

The decision trace proves the exact raw base score 6 for both reconciliation decisions through constant:cbrn_protection_ai.base_reconciliation; it does not prove either decision's actual availability in the undeclared runtime state. The adapter did not normalize either score into a click probability.

The first reconciliation evaluation CBRN_RECONCILIATION_2026_10_06 had scenario hash a2c769dcd542e10997bc48ba8ebd5b872648c1806f66ed98ef1b00b2aaac95bf and analysis id probability-142e8150dc0301ebe1cb4b62. Its top-level actor state and flags were not duplicated into scopes.ROOT, so its eligibility result is retained only as an invalidly bound first pass, not evidence that the choices are blocked. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/032de2e50eeb222faf148e04f1506e6fbf2bb8212890607d7b699eba6501f508/de4dcd6f394d81875c067daa88aa3c24486b3065d25aaa338c98a18f03e6e9e2/probability-142e8150dc0301ebe1cb4b62.json.

Both evaluations emitted ranking and unresolved JSON/SVG/PNG artifacts. An explicit probability_render call was not made before the parent’s cutoff.

The current AI/score result is bounded to the two named reconciliation choices. The supplied pool is not the full decision category or game-wide AI race, target arrays are incomplete, and the adapter does not model decision click probabilities.

## Scenario coverage and interpretation

| Scenario id | Scope | Candidate and external-factor completeness | Result class |
| --- | --- | --- | --- |
| NW_1936_NO_STOCKS_NO_WAR | Included in both reconciliation sets as GER with no stocks and no pending records | Synthetic fixture only; no live campaign evidence; country exists and occupied transaction variable were not explicitly bound in the second set | Bounded; false pending gates appeared, while helper coverage remained unresolved |
| OCC_REFUND_PENDING | Included in the second set with the recovery flag | Synthetic GER country scope; the analyzer still needed explicit exists and cbrn_occupied_committed_transaction values to resolve the country helper | Score-only exact base 6; eligibility unresolved |
| EXP_REFUND_PENDING | Included in the second set with an FRA scope and one incomplete target pool entry | cbrn_export_recipient_FRA was supplied as the tag FRA, but the analyzer required numeric operands for that saved-recipient equality; world recipient list is incomplete | Score-only base 6 in source trace; eligibility and rank unresolved |
| OCC_AND_EXP_REFUNDS_PENDING | Included in the second set | Same unresolved occupied inputs and dynamic export target-id comparison | Score-only exact base 6 for occupied; export eligibility unresolved; no exact tie/rank claim |
| OCC_PENDING_ACTIVE_PROGRAM | Included in the second set with active-program flags and transaction value 1 | The scenario still lacks a complete country-exists binding and some helper variables | Source gate is intended to exclude active programs; analyzer confirmation unresolved |
| EXP_STALE_RECEIPT_NO_RECOVERY_FLAG | Included in the second set with an owned receipt but no recovery flag | One FRA target only; incomplete worldwide target pool and unresolved recipient-id comparison | Bounded/unresolved |
| Wartime-ready protection | Not evaluated | Timed candidate inspection returned 28 required inputs but no scenario evaluation | Unresolved |
| Mask and factory shortages | Not evaluated | Mission-style affordability inputs were not scenario-bound and the matching occupation-file inspection did not return | Unresolved |
| Sale-active and sale-expired aid | Not evaluated | The ordinary/sale mission candidate set and quote/cost state were not evaluated | Unresolved |
| Morale high and low | Not evaluated for native doomsday raids | No native-raid AI adapter is exposed | Unresolved |

The evaluator’s PROBABILITY_OUTCOME_NEVER_ELIGIBLE warning for the export reconciliation action is not a confirmed source defect because its own trace reports unresolved variable.cbrn_export_recipient_@FROM versus FROM and the scenario cannot provide the required numeric country identity.

The current cbrn_reconcile_occupied_mask_records helper requires a live country, cbrn_occupied_transaction_recovery_pending, and no active occupied program. The export helper requires a recorded owner and recipient, a non-active transaction, and a mismatch or recovery marker. These are source-defined validity gates; the MCP did not establish all of them in the synthetic inputs.

## Findings by surface

The two new reconciliation decisions have identical willingness formulas: base constant:cbrn_protection_ai.base_reconciliation = 6 and no modifiers. If both become eligible, their local raw scores are tied. The analyzer supplied no eligible comparison row for export and no exact rank reversal or selection probability.

The reconciliation trigger gates are narrow enough to prevent ordinary ready transactions from opening the recovery actions. The occupied gate blocks an active program, and the export gate requires a receipt plus a recovery/mismatch marker and absence of the active marker. The exact malformed-record and write-off effects were not evaluated by the probability adapter.

Both reconciliation weights are positive even though agent_decisions_2026-10-04.md calls these bounded player-triggered routes. If player-triggered means AI countries must not execute a retry/write-off automatically, align that intent with the positive ai_will_do base by zeroing/removing the AI weight or by explicitly accepting AI action. This is a design follow-up, not a balance target selected by this audit.

The two protective-aid variants share one AI weight shape and route availability, custom-cost display, and payment readiness through cbrn_protective_aid_ordinary_payment_ready or cbrn_protective_aid_sale_payment_ready. The source gates quote the active sale/factory variant and test PP, factory availability, stock, target start/cooldown, and reservations. No matched AI evaluation was returned, so score dominance, shortage starvation, and sale-expiry rank changes are unresolved.

The biological sabotage repair puts the country relationship contract directly in bio_sabotage_ai_may_target_state at common/scripted_triggers/biological_sabotage_triggers.txt:183-205. The state-local pathogen and target-owner checks remain separate, while the full is_controlled_by = FROM wrapper remains in biological_sabotage_raid_triggers.txt for human prepare/launch paths. This matches the installed raid documentation’s stated ai_will_do scope for FROM and var:target_state. Probability conclusions for all 12 native raid types remain unresolved because the probability adapter does not expose native raid ai_will_do.

The 12 types recorded by the earlier native-raid scenario fixture are bio_sabotage_anthrax_base, bio_sabotage_anthrax_theater, bio_sabotage_anthrax_terminal, bio_sabotage_plague_base, bio_sabotage_plague_theater, bio_sabotage_plague_terminal, bio_sabotage_tularemia_base, bio_sabotage_tularemia_theater, bio_sabotage_tularemia_terminal, bio_sabotage_smallpox_base, bio_sabotage_smallpox_theater, and bio_sabotage_smallpox_terminal.

The previously saved machine evidence docs/testing/2026-10-04_bio_sabotage_scope_probability/probability_mcp_evidence.json records nativeRaidAiWillDoAdapterExposed=false and an actual raid-source PROBABILITY_SURFACE_EMPTY attempt for common/raids/biological_sabotage_raids.txt. Its named 13-case scenario matrix has empty state maps, incomplete biological-only candidate coverage, and no MCP scenario hash. It is not an executable probability result.

The doomsday AI modifier adds high-morale weight only when stability and has_war_support exceed their configured thresholds and adds stockpile weight above its stockpile threshold. The has_war_support read is valid as an auto-generated dynamic variable. The native-raid probability adapter is absent, so no doomsday score, dominance, or morale rank reversal is claimed.

The random_list inspect found a complete two-candidate local pool for the CBRN protection decision-effect source, but no named-scenario probability evaluation was completed. The source branches are the defective batch event and safe batch clearing path, with weights in common/script_constants/cbrn_system_constants.txt. Do not treat the source weights as evaluated probabilities in this handoff.

The treaty invitation event has accept/decline ai_chance options at chaosx_contamination.9.a and chaosx_contamination.9.b. The accept option is conditionally available; the decline option is unconditional. The source constant table includes factors for democracy, stockpile, prior unconventional use, war with the founder, and major status, but no probability scenario or complete external founder binding was evaluated.

The cbrn_protection.2 event has one option with source ai_chance 100. No event-option MCP evaluation was run.

## Skipped analyses, latency limits, and uncertainty

The two-file mission_ai_will_do inspection of common/decisions/cbrn_protection_decisions.txt and common/decisions/cbrn_occupation_decisions.txt ran for more than six minutes. The protection-file result was returned when the pending wrapper was canceled; the occupation-file result did not return. This leaves the timed protective-aid and full payment-readiness scenarios unresolved.

The random_list inspect returned after the parent-directed cancellation. Its two-candidate complete-pool inventory is retained, but probability_evaluate was not started after the parent asked to stop queuing MCP requests.

Event-option probability_inspect/evaluate, event_inspect, and event_render were not started after the same parent cutoff. Their source files and option identifiers are inventoried above, but no structural graph or event probability is claimed.

hoi4.reference_context was started for the bounded decision surface but was canceled after it remained pending; exact offline sources were read locally instead. hoi4.reference_search/read and hoi4.source_lookup were not called.

No probability_sweep was run because the only completed scenario evaluation remained partially unresolved and the relevant high-population/payment mission surfaces did not complete scenario analysis. No probability_compare was run because the biological native-raid adapter is absent and the new reconciliation IDs did not exist in the parent baseline. The saved sabotage comparison attempt from 2026-10-04 ended with PROBABILITY_SURFACE_EMPTY.

No probability_simulate was run because no uncertain inputs had calibrated distributions. No probability_sequence was run because these are decision scores, native raids, event options, and one simple random list rather than a fully declared custom weighted pool with cadence and state transitions.

No explicit probability_render call was made. The two reconciliation evaluations generated ranking and unresolved render artifacts as listed above.

No AI-weight or balance change is recommended from this partial evidence. Before a final balance claim, bind exists and transaction values for the occupied gate, supply the numeric saved-recipient country ID for export or preserve that analyzer limitation, run the matching mission evaluations for protection, aid, and sale scenarios, and retain the raid adapter gap if it remains unsupported.

## Skills used

Applied .agents/skills/chaos-redux-subagents/SKILL.md, .agents/skills/chaos-redux-decisions-missions/SKILL.md, .agents/skills/chaos-redux-mtth/SKILL.md, and .agents/skills/chaos-redux-events/SKILL.md.

No skills were created or updated.

## Parent disposition after review

The parent clarified the recovery design in `../agent_decisions_2026-10-05.md`, section Recovery action AI and public text.
Player-triggered denotes a chosen decision rather than a periodic automatic clear or grant; AI countries may choose either valid reconciliation decision under the same gates.
Both inherited willingness scores remain six.
This closes the wording ambiguity above without changing an AI coefficient or treating unresolved eligibility/rank evidence as a measured probability.
Timed protection, shortage, aid and sale evaluations, treaty options and the random-list evaluation remain unresolved as reported above.
