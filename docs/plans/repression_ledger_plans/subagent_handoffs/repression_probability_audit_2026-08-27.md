# Repression Ledger probability audit — 2026-08-27

## Disposition

This is a read-only weighted-logic audit for the 1936 Repression Ledger/camp-repression baseline repair.

No gameplay, AI, event, decision, mission, trigger, effect, constant, localisation, or runtime file was edited by this audit, and no commit was created.

The audit is partial and must not be read as proof of live-game country behavior: the HOI4 probability adapter accepted the named scenario set but received empty state fixtures, so country, target, cap, cooldown, resource, and route predicates remain unresolved unless a source-level hard gate proves otherwise.

## References and source surfaces

I read `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, and `.agents/skills/chaos-redux-decisions-missions/SKILL.md` before the audit.

The required offline wiki references consulted were the Decision modding, AI modding, Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, and Idea modding pages under `paradox_wiki/`.

The required vanilla documentation consulted was `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md`, `effects_documentation.md`, `modifiers_documentation.md`, and `script_concept_documentation.md`.

The weighted source surfaces were:

- `common/decisions/camp_repression_generic_decisions.txt:12` (`camp_repression_network_category`), with 14 decision-adapter candidates and 7 mission-adapter candidates discovered by MCP.
- `common/decisions/genocide_crisis_decisions.txt`, with 33 decision-adapter candidates; the mission inspect fell back to the decision adapter because this file exposes no `ai_will_do` mission candidates.
- `common/decisions/camp_repression_major_country_decisions.txt`, with 29 decision-adapter candidates; the mission inspect fell back to the decision adapter because the country mission definitions are passive/non-selectable and expose no mission `ai_will_do` candidates.
- Directly referenced weighting and gate sources: `common/script_constants/camp_repression_rework_constants.txt`, `common/script_constants/genocide_crisis_constants.txt`, `common/scripted_triggers/camp_repression_rework_triggers.txt`, `common/scripted_triggers/genocide_crisis_triggers.txt`, `common/scripted_effects/camp_repression_rework_effects.txt`, `common/scripted_effects/genocide_crisis_effects.txt`, and `common/scripted_effects/camp_repression_major_country_effects.txt`.

The source-level weighted identifiers audited in the generic file were `generic_activate_detention_network`, `generic_expand_labor_quotas`, `generic_redirect_labor_to_construction`, `generic_redirect_labor_to_resource_extraction`, `generic_allocate_additional_guards`, `generic_reduce_labor_quotas`, `generic_upgrade_existing_site_to_radicalized_atrocity_site`, `generic_restricted_contaminated_site_escalation`, `generic_destroy_evidence_before_retreat`, and `generic_inspect_active_site`, plus the four ledger control decisions `camp_repression_open_ledger`, `camp_repression_close_ledger`, `camp_repression_show_actions`, and `camp_repression_hide_actions`.

The generic mission-adapter pool was `camp_gui_selected_dismantlement_mission`, `camp_repression_close_dormant_legacy_site`, `generic_dismantle_detention_network`, `generic_labor_project_cycle`, `generic_network_overstretch_crisis`, `generic_reform_and_dismantlement`, and `generic_retreat_evidence_crisis`.

The genocide decision pool was `genocide_show_hidden_decisions`, `genocide_hide_hidden_decisions`, `germany_wartime_camp_administration`, `germany_expand_occupied_poland_camp_system`, `germany_expand_extermination_site_network`, `germany_intensify_extermination_policy`, `germany_transfer_prisoners_to_experiment_site`, `genocide_restricted_chemical_site_escalation`, `genocide_build_extermination_camp`, `genocide_intensify_deportations`, `genocide_hide_evidence_from_foreign_observers`, `genocide_suppress_internal_reports`, `genocide_redirect_trains_and_supplies`, `genocide_deal_with_resistance_sabotage`, `genocide_handle_refugee_waves`, `genocide_manage_military_objections`, `genocide_destroy_camp_evidence`, `genocide_cover_up_liberated_camps`, `japan_expand_forced_labor_camps`, `japan_conduct_anti_partisan_reprisals`, `japan_transfer_prisoners_to_experimental_facilities`, `japan_destroy_occupation_records`, `sov_show_gulag_decisions`, `sov_hide_gulag_decisions`, `sov_expand_gulag_network`, `sov_deport_suspected_opposition_groups`, `sov_confiscate_food_from_disloyal_regions`, `sov_purge_camp_administrators`, `sov_raise_forced_labor_quotas`, `sov_destroy_gulag_records`, `genocide_publicize_survivor_testimony`, `genocide_support_resistance_movements`, and `genocide_prepare_tribunal_records`.

The major-country decision pool was `germany_route_prisoner_labor_to_war_construction`, `germany_redirect_prisoner_labor_to_eastern_fortifications`, `germany_tighten_deportation_logistics`, `germany_increase_guard_allocation_to_ss_sites`, `germany_build_ss_laboratory_annex_at_auschwitz`, `germany_destroy_auschwitz_evidence_before_retreat`, `germany_dismantle_auschwitz_complex`, `japan_establish_pingfang_research_bureau`, `japan_expand_occupation_test_records`, `japan_shield_ishii_from_army_review`, `japan_redirect_records_to_army_medical_control`, `japan_invite_kwantung_army_medical_officers`, `japan_suppress_chinese_resistance_cells`, `japan_route_supplies_to_epidemic_prevention`, `japan_open_epidemic_containment_office`, `japan_destroy_pingfang_records`, `japan_evacuate_pingfang_research_staff`, `japan_submit_to_army_review`, `japan_remove_ishii_from_program_control`, `japan_shut_down_prisoner_experiments`, `sov_transfer_prisoners_to_industrial_camps`, `sov_reinforce_nkvd_authority`, `sov_reduce_paranoia_through_party_review`, `sov_release_prisoners_for_military_service`, `sov_dismantle_overextended_gulags`, `sov_emergency_famine_relief`, `sov_conceal_famine_mortality`, `sov_admit_local_administrative_collapse`, and `sov_authorize_extreme_periphery_repression`.

## MCP evidence

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

The mandatory read-only `hoi4.probability_inspect` calls returned the following source-relative evidence.

| Adapter and source | Result | Artifact |
| --- | --- | --- |
| `decision_ai_will_do` / `common/decisions/camp_repression_generic_decisions.txt` | `PROBABILITY_SOURCE_INSPECTED`; 14 candidates; 0 available without a state fixture; pool not runtime-complete; 27 required inputs; eligibility/raw score supported; normalized probability and timing unsupported; selection rule `score_only`; initial source revision `16180bd1ba440c26af3b647f56c67eaa923f5de534a357e89274334687d848bc`; source hash `15747dd2bf63536f1da7afc24f099eac1c156ad94b722ea1a3ce13f2e37746ab` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/153da2c44df3c49e86f2ec6754feac54f041b4dc7d2f6089532bac48471b0501/cfd1b73ae6412f92871fc706b478816cdfa7365a3ada93081d13ec7304641591/probability-inspect-15747dd2bf63.json` |
| `mission_ai_will_do` / generic source | `PROBABILITY_SOURCE_INSPECTED`; 7 candidates; 0 available without a state fixture; 5 required inputs; normalized probability and timing unsupported | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6062a03c96c125c5075ebdf3bb0d999c34f025e9a6a23947e060ac8c2298aa29/84b1169582acc5d335aa060a35fa5d5f2e6bcbed74d0ed0884e991b8d1ab2bd2/probability-inspect-15747dd2bf63.json` |
| `decision_ai_will_do` / `common/decisions/genocide_crisis_decisions.txt` | `PROBABILITY_SOURCE_INSPECTED`; 33 candidates; 0 available without a state fixture; pool not runtime-complete; 32 required inputs; score-only adapter | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c8658765ab9e5adee49fcbbc6724591798c487408b582009e3f066f050ad040f/3788edd1968af6367eec6410da2f6ea04d92c2ed466e562c051448308055375d/probability-inspect-99a31656ce5e.json` |
| `mission_ai_will_do` / genocide source | `PROBABILITY_SOURCE_DISCOVERED` with `requested_adapter_empty`; suggested `decision_ai_will_do`; 0 mission candidates and 33 decision candidates | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b1401cac1d31663323d72abd4d0d7b79a55881c24c5401c6b09f86fab0b896e0/97f4009c154cd45c3851fefdf9af2d5e46d406f474dd53d8c3f388a0f4e75a5e/probability-inspect-99a31656ce5e.json` |
| `decision_ai_will_do` / `common/decisions/camp_repression_major_country_decisions.txt` | `PROBABILITY_SOURCE_INSPECTED`; 29 candidates; 0 available without a state fixture; pool not runtime-complete; 14 required inputs; score-only adapter | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1e0c0c1df9058f0a8e47c30e26a239bb8a56a811633d1d7061bedfc370706469/133c1c0186820fe38983f87f5f284f2e2cac63bbc775bc30bfb35f1f9ee06628/probability-inspect-86161d8558e4.json` |
| `mission_ai_will_do` / major-country source | `PROBABILITY_SOURCE_DISCOVERED` with `requested_adapter_empty`; suggested `decision_ai_will_do`; 0 mission candidates and 29 decision candidates | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/da2c13b5422f0a7dd8a39497e3f68a99c5853ee024ff30b05b51a87807b21300/9f0c526f3c6b6b7b976fc470a099a038d6fb5422e852908d5ef49cde147b6d22/probability-inspect-86161d8558e4.json` |

The completed evaluator call was `hoi4.probability_evaluate` for `decision_ai_will_do` on `common/decisions/camp_repression_generic_decisions.txt`, with the full 14-candidate decision pool, `horizonDays=365`, and `metrics=["raw_value"]`.

Its scenario set was `REPRESSION_1936_BASELINE_2026_08_27` with scenario IDs `GER_1936_DACHAU_ONLY`, `JAP_1936_STATE_716_ACTIVE_611_PINGFANG_DORMANT`, and `SOV_1936_KOLYMA_MAGADAN_KARAGANDY_FAMINE_AFTERMATH`.

The evaluator returned `PROBABILITY_ANALYZED_PARTIAL`, `analysisId=probability-459377b8e95245f21b0f0e30`, `sourceRevision=334f4d35a63f05d79183e88a3c3cba900d91ac6b70c4279306162c13e2c01f34`, `sourceHash=15747dd2bf63536f1da7afc24f099eac1c156ad94b722ea1a3ce13f2e37746ab`, `scenarioHash=35d257245a3a0c4217bcf022d847019d091cc89cd55d5f03e1de4ee41323a2c6`, 42 candidate rows across three scenarios, 241 unresolved items, and zero diagnostics.

The authoritative evaluator artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/043d0d1c7450c95e45d89a50e8a047ec4c40c51278e4bc5ff1a8638d20e441a2/e6e9c36edc6a7f127b55a263a6fdb0213b3cb7c4e6b2fa464197a78176c30222/probability-459377b8e95245f21b0f0e30.json`.

Rendered evidence from that evaluation was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cf8417001981553ee95063d83c1b9fbf636703a840b95e443bbecbce27b0f1da/a2fff24b54f7b6ace22678095d72c22506c8e301ab95c85e338cf1d12b076c47/probability-probability-459377b8e95245f21b0f0e30-ranking.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/65c02b518a8265f830ae89db5d4c06244072e24df5a12392d9901333854e5486/4ba10ee0c8e52fe2c044f6641598dbb6774a76bea362c0181ea3351827f6fbd9/probability-probability-459377b8e95245f21b0f0e30-matrix.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ffb0f5d4bbcd8ca5f7da7a63dd713aa8201212a88e73f43dabca5b6b6e433224/4131905eff622f98505d36fa082a189d8d1ed56f83222f1d3259711ef4b631a4/probability-probability-459377b8e95245f21b0f0e30-unresolved.svg`.

The artifact's selection boundary is explicitly `score_only`: decision `ai_will_do` values are not a click probability, and this adapter does not provide normalized probability, timing distribution, sequence, or effective MTTH conversion.

The first evaluator request attempted `eligibility` and `rank` as metrics and was rejected by the MCP schema; the accepted rerun requested `raw_value` and used ranking/matrix/unresolved outputs. This is a tool-schema limitation, not a source conclusion.

## Scenario contract and completeness

The scenario IDs above are the named audit surfaces, but all three MCP `state` objects were `{}`.

The intended GER contract was a fascist AI GER on 1936-01-01 with only the Dachau site active, no other German historical site active, no war or retreat, no exposed crisis, and no later genocide flags.

The intended JAP contract was a fascist AI JAP on 1936-01-01 with state 716 active, state 611 and the Pingfang escalation dormant, no China war, no Pingfang route/unlock, and no Ishii/biowarfare escalation flags.

The intended SOV contract was a communist AI SOV on 1936-01-01 with Kolyma state 644, Magadan state 874, and Karagandy state 881 active, famine-aftermath pressure at the declared 12-point constant, no later escalation flags, and no reform route.

Those assumptions were not executable runtime fixtures because the adapter requires primitive scenario declarations and cannot resolve the nested state, target, variable, equipment, flag, and scope structures needed by these sources.

Consequently, candidate-pool completeness is source-relative for the generic evaluator, but runtime-state completeness is false for every scenario.

The unresolved inputs include country identity/government/date, `ROOT`/`FROM` target scope, active-site registration and responsibility, historical/dormant markers, site/project/experiment/radicalized/restricted caps, cap counts, cooldown flags, freeze/reform flags, labor output, overstretch, resistance, condemnation, evidence exposure, surrender progress, war/war-with-China state, equipment, command power, manpower, civilian factories, focus hooks, technologies, character flags, famine and paranoia values, and `any_controlled_state`/`any_subject_country` pool membership.

## Source score and gate findings

The following are source-derived score values and hard gates, classified as `score-only` or `bounded` rather than as final scenario probabilities.

### Generic network

- The four ledger controls are `base = 0` and are UI controls, not repression actions.
- `generic_activate_detention_network` has `base = 0`, then adds 25 for the generic authoritarian activation route or 45 for the fascist activation route; it is hard-zeroed when `camp_rework_country_under_ai_site_cap` fails and is reduced by the 0.10 high-condemnation factor and 0.20 losing-war factor when their conditions apply.
- `generic_expand_labor_quotas`, `generic_redirect_labor_to_construction`, and `generic_redirect_labor_to_resource_extraction` use a 25 base; the two project routes are hard-zeroed when the project cap fails or overstretch reaches the overstretched band, and all require an active network, valid target, labor output, equipment, and factory/resource gates.
- `generic_allocate_additional_guards` and `generic_reduce_labor_quotas` use a 35 base and a 1.35 high-resistance/high-overstretch factor respectively; visibility and availability require an active network and valid resource gates.
- `generic_upgrade_existing_site_to_radicalized_atrocity_site` and `generic_restricted_contaminated_site_escalation` use a 12 base and are hard-zeroed by their cap, condemnation, overstretch, route, and fixed-country exclusion gates.
- `generic_destroy_evidence_before_retreat` uses a 55 base and the losing-war 0.20 factor on its non-fascist branch; it also requires an active network, a valid enemy-near evidence target, and resources.
- `generic_inspect_active_site` uses an 85 base but is hard-zeroed for fascist countries when no exposed crisis exists; it still requires an active network and valid inspection target.
- `generic_dismantle_detention_network` and `camp_repression_close_dormant_legacy_site` are routed through the mission adapter despite decision-shaped source blocks, use an 85 base, and receive a 2.00 postwar reform factor when the condition applies; both require reform authority, valid target state markers, and resources.
- The five passive generic mission blocks have `ai_will_do = { base = 0 }`, use activation/availability/timeout handling, and are not evidence of selectable AI escalation.

### Germany

- Genocide Germany actions are dated or target-gated: `germany_wartime_camp_administration` and `germany_expand_occupied_poland_camp_system` require a date after 1939-12-31, `germany_expand_extermination_site_network` requires a date after 1940-12-31, and `germany_intensify_extermination_policy` requires a date after 1941-12-31.
- Their source bases are 55 for direct Holocaust administration, 55 for occupied Poland, and 70 for extermination; the 1936 date gates therefore bound those named later-war actions to zero in the intended baseline if the date fixture is actually supplied.
- `genocide_build_extermination_camp` has a generic base of 0 and only adds the Germany occupied-Poland value of 70 under its fixed-country route and valid target/cap conditions; it is not proven dormant by the empty MCP fixture.
- The major Germany actions have high score bases despite their target gates: war construction, eastern fortifications, deportation logistics, guard allocation, and evidence destruction use the 70 Germany expansion family, while the Auschwitz laboratory annex uses 45 and dismantlement uses 2.
- The major Germany war-construction action is visible/available when GER fascism, non-frozen expansion, positive `camp_labor_output`, equipment, and cooldown conditions hold; it has no explicit 1939 date gate in the source block. Therefore a 1936 GER with positive labor output could receive a score of 70 even though the MCP fixture did not prove that labor output or equipment state.
- The major Germany eastern-fortification action adds project-cap, active-mission, critical-overstretch, target-state, and equipment gates, and uses a 60-day generic cooldown; its target requires a valid active site and Germany prisoner-source pool.

### Japan

- `japan_expand_forced_labor_camps` is 42, `japan_conduct_anti_partisan_reprisals` is 34, `japan_transfer_prisoners_to_experimental_facilities` is 28, and `japan_destroy_occupation_records` is 60, but the first three require Japan fascism plus China/occupation, biowarfare, site, experiment, resistance, or cap conditions and the evidence action requires an enemy-near undiscovered target.
- Major Japan Pingfang establishment uses 55 and requires fascist JAP, a China/Manchuria route or war, state 328 anchor responsibility/control, and site/project/experiment cap availability; the source has no unconditional 1936 trigger.
- Major Japan experiment, review, containment, evacuation, and shutdown actions use 35 or 8 and are gated by Ishii flags, outbreak risk, route state, active missions, cooldowns, equipment, and reform/shutdown state.
- The user-specified `state 611/Pingfang` wording does not match the source gate: vanilla state 611 is South Chahar, while the source's Pingfang branch explicitly evaluates state 328 and the vanilla comments identify state 328 as Kirin and state 716 as Liaotung. This mapping must be resolved before a JAP baseline can prove Pingfang dormancy.
- Because state 328 control/responsibility, the Japan China/Manchuria pool, China-war state, and route flags were not supplied, the 1936 JAP low-priority conclusion is `unresolved`, not exact.

### Soviet Union

- `sov_expand_gulag_network` uses a 38 base plus a 20 focus-hook add and is hard-zeroed by reform, site cap, and project-cap gates; its stability factor is 1.40 below the 0.55 threshold.
- `sov_deport_suspected_opposition_groups` uses 34 plus a 20 focus-hook add and a 1.40 stability factor below 0.50; it requires the medium-paranoia/periphery route.
- `sov_confiscate_food_from_disloyal_regions` uses the famine-pressure base of 14, adds 20 for the focus hook and 34 at high famine pressure, and requires high paranoia and a valid periphery target.
- `sov_purge_camp_administrators` uses 34 plus the focus-hook add, while `sov_raise_forced_labor_quotas` uses 18 plus the focus-hook add; both require the relevant paranoia, active-site, and target gates.
- `sov_destroy_gulag_records` uses the 60 evidence-destruction base and requires an enemy-near undiscovered evidence target.
- Major Soviet transfer and NKVD actions use 48 plus the 20 focus-hook add and are hard-zeroed by reform, site-cap, project-cap, and target/resource gates; relief actions use 40; famine concealment uses 18 and is hard-zeroed on reform; extreme periphery repression uses only 2 plus a 2 focus-hook add and is hard-zeroed unless the extreme route and extreme cap are available.
- Source trigger `is_soviet_gulag_periphery_pool_state` explicitly includes states 644, 874, and 881, so the named Kolyma/Magadan/Karagandy pool is structurally recognized. The actual active flags, ownership/control, responsibility, paranoia, stability, famine target, focus hook, cap, and cooldown state remain unresolved in the MCP run.
- The SOV surface is therefore bounded as “more responsive than GER/JAP when the declared famine/paranoia pressure and periphery gates are true,” but no exact ranking or selection probability is proven.

## Caps, cooldowns, timing, and repetition risk

The source centralizes the main generic timing values in `camp_rework_timing`: standard action 150 days, suppression 180 days, reform 270 days, dismantle 365 days, retreat 45 days, idea-medium 180 days, decision cooldown 60 days, and restricted-method suppression 35 days.

The genocide decision cooldown constant is 60 days, applied broadly through `days_re_enable = constant:genocide_timing.decision_cooldown`.

Major-country action cooldowns and passive mission timeouts are explicit: Germany uses 180-day Poland/fortification/laboratory missions, 120-day military review, 45-day evidence destruction, 270-day dismantlement, and a 365-day war-construction re-enable; Japan uses 180-day Pingfang, 120-day review, 150-day containment, 45-day evacuation, and 270-day shutdown; Soviet missions use 180-day quota/famine-pressure/relief, 150-day administrator review, 270-day dismantlement, and 45-day retreat records.

The cap helpers are `camp_rework_country_under_ai_site_cap`, `camp_rework_country_under_ai_radicalized_cap`, `camp_rework_country_under_ai_experiment_cap`, `camp_rework_country_under_ai_restricted_method_cap`, `camp_rework_country_under_ai_project_cap`, and `camp_rework_soviet_under_ai_extreme_cap` in `common/scripted_triggers/camp_repression_rework_triggers.txt:1644-1716`.

These helpers require both cap variables and current counts, and several also require a country flag or positive cap. Active mission flags, action cooldown flags, expansion freeze, reform-route flags, critical overstretch, and target validity provide additional anti-repetition gates.

The MCP adapter could not evaluate these caps/cooldowns because the scenario state was empty, and it does not convert `days_re_enable`, `days_remove`, or `days_mission_timeout` into a timing distribution. Repetition/starvation and timing-drift conclusions remain `unresolved` beyond the bounded source observation that positive score is repeatedly blocked by these gates.

## Findings by requested behavior

- GER 1936 low priority: later-war genocide actions are source-bounded by hard date gates, but major Germany war-construction and other country-specific actions retain 70-point score bases and do not all carry a date gate. If labor output, equipment, target validity, and cap state are already positive, the source does not prove low priority. MCP did not resolve those inputs. Classification: `unresolved`, with a concrete dominance risk on the 70-point war-construction branch.
- JAP 1936 low priority: the major Pingfang branch is strongly route/anchor/cap gated and the genocide actions require war, target, or biowarfare inputs, but the requested state-611/Pingfang fixture conflicts with the source's state-328 anchor. Classification: `unresolved` pending a corrected state-328 plus route fixture.
- SOV 1936 appropriate responsiveness: active periphery states 644/874/881 are recognized by the source pool and famine pressure has a declared 12-point aftermath threshold, while relief/escalation scores are separated by route and stability/paranoia gates. Classification: `bounded` source evidence, not an exact rank or probability.
- Dormant later-war escalation: Germany's date gates are a strong bounded safeguard; Japan's route/war/anchor and Ishii gates are strong bounded safeguards; Soviet extreme repression is explicitly 2 plus 2 and hard-zeroed unless extreme-route/cap gates pass. The empty state fixture prevents an exact “does not immediately fire” claim for any country.
- Dominance/starvation/rank reversal: no valid cross-candidate probability or rank-reversal conclusion was produced. The generic evaluator's visible no-state ranking excerpt only showed the four zero-valued ledger controls ahead of unresolved substantive rows; this is fixture behavior, not a live-game ranking.
- Exploit risk: the highest concern is not a proven probability bug but the possibility that a 70-point Germany major-country score becomes selectable in 1936 when `camp_labor_output > 0` and equipment/cap gates are true. This needs a complete GER fixture and a rerun of evaluate/sweep before any tuning target is chosen.

## Skipped analyses and blockers

- `hoi4.probability_evaluate` was completed only for the generic decision adapter because the parent requested immediate handoff with the current evidence. Genocide and major-country decision pools have inspect evidence but no named-scenario evaluator artifact in this run; their scenario conclusions remain `score-only`/`unresolved`.
- `hoi4.probability_sweep` for thresholds, sensitivity, and rank reversals was not run, so no rank-reversal or threshold claim is made.
- `hoi4.probability_compare` was not run because no before/after or candidate patch was in scope; no comparison ID exists.
- `hoi4.probability_simulate` and `hoi4.probability_sequence` were not run because no complete uncertain-input distribution or complete custom pool cadence/state transition contract was supplied.
- `hoi4.probability_render` was not called separately because `probability_evaluate` emitted ranking, matrix, and unresolved renders; those URIs are preserved above.
- The MCP scenario adapter could not consume the required nested target/flag/equipment/variable/state-pool fixture, leaving 241 unresolved items in the generic evaluate artifact.
- Concurrent worktree activity changed the generic source revision between inspect (`16180bd1...`) and evaluate (`334f4d35...`) while the source hash remained `15747dd...`; no audit file was changed by this subagent. The parent should rerun the probability compare/evaluate pass after the source worktree is stable.
- No `chaosx_ai_probability_auditor` callable route was exposed in the available tool inventory; this handoff is the direct read-only audit record.

## Recommended follow-up without applying changes

1. Freeze the relevant source revision and rerun `hoi4.probability_inspect` for all three decision sources.
2. Build an adapter-accepted primitive scenario fixture that separately declares GER labor output/equipment/caps, JAP state 328 control/responsibility plus 716/611 status and route flags, and SOV state 644/874/881 control/responsibility plus famine/paranoia/stability/focus/cap flags.
3. Run `hoi4.probability_evaluate` for the full 33- and 29-candidate pools under the same three scenario IDs, then run `hoi4.probability_sweep` for cap, war, date, labor-output, and famine-pressure sensitivities and rank reversals.
4. Use `hoi4.probability_compare` only after an owner-applied patch or an explicitly named candidate comparison, reusing the same scenario hashes and complete pools.
5. Resolve whether the user-facing “611/Pingfang” reference should be state 611 South Chahar or source anchor state 328 Kirin before accepting a JAP dormancy conclusion.

No balance target or gameplay fix was selected or applied by this audit.

## Post-patch audit — 2026-08-27

### Scope and source state

This dated section records the read-only post-patch pass requested by the parent after the owner changed availability and resource-cost gates.

The owner patch was reviewed at `common/decisions/camp_repression_major_country_decisions.txt:40-82` and `common/scripted_effects/camp_repression_rework_effects.txt:2967-2993`.

The German war-construction route `germany_route_prisoner_labor_to_war_construction` now has `has_war = yes` in both its decision `visible` block at `common/decisions/camp_repression_major_country_decisions.txt:51-58` and its decision `available` block at `common/decisions/camp_repression_major_country_decisions.txt:59-68`.

The matching Germany GUI slot in `camp_rework_rebuild_country_gui_actions` has the same `has_war = yes` gate at `common/scripted_effects/camp_repression_rework_effects.txt:2983-2992`.

The route's AI block remains `base = constant:camp_rework_ai_weight.germany_expansion` with only the existing critical-overstretch zero factor at `common/decisions/camp_repression_major_country_decisions.txt:74-82`; no `ai_will_do` weight or modifier was changed in the reviewed route hunk.

The reviewed expansion cost packages remove the former command-power and infantry-equipment requirements while retaining manpower, support-equipment, and train requirements for the Germany laboratory annex, Japan Pingfang establishment, Soviet industrial transfer, and Soviet extreme-periphery actions in `common/decisions/camp_repression_major_country_decisions.txt`.

This is an availability/cost change, not a probability-weight change: a candidate can retain the same willingness score while becoming unreachable in peacetime or cheaper to execute after its route gates pass.

### Post-patch probability inspect evidence

The mandatory post-patch `hoi4.probability_inspect` calls used workspace `mod_chaos_redux_ea3b2d67c2c0` and the `decision_ai_will_do` adapter.

| Source | Post-patch MCP result | Artifact and revision |
| --- | --- | --- |
| `common/decisions/camp_repression_major_country_decisions.txt` | `PROBABILITY_SOURCE_INSPECTED`; 29 candidates; 0 available with the empty fixture; `poolComplete=false`; 15 required inputs | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d5d6d5023d530b794d2c8d32a41cebca5b1f365aef4523163cf7d7860446a1f6/456721ceb960c06080b3b5e41fbe3cea6d0f69faebb16bb1c287adf0f543e3c1/probability-inspect-9d281e9e6401.json`; source revision `8a3dd5f72ff5e53e96a1d1fb281ce299f311df60656295776c3ff2c4156784ab`; source hash `9d281e9e64010863a8d6cc61387ec072ea9eff75736f7777ece9f61920ae9124` |
| `common/decisions/camp_repression_generic_decisions.txt` | `PROBABILITY_SOURCE_INSPECTED`; 14 candidates; 0 available with the empty fixture; `poolComplete=false`; 27 required inputs | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d0c2988de0378d44556c449c0a75150e7b11f6bac50f18c34f31af8449c1484b/5cee3384fc1d719baf03aa929102e9c088bc25d645e23ddf8a5e45cfc2901a22/probability-inspect-c20bfccf365e.json`; source revision `45e1df0aec2c508dc7525de40ef444a30dda18bb59937ad50ed383eb922ed442`; source hash `c20bfccf365e7bebae06bc654fb5bd39587e4e0bdc1af84af3523080fafff803` |
| `common/decisions/genocide_crisis_decisions.txt` | `PROBABILITY_SOURCE_INSPECTED`; 33 candidates; 0 available with the empty fixture; `poolComplete=false`; 32 required inputs | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/16ca66e2a12e552d87d35e6b5c199dc3b1e78441586218cb46821b16fb7ff464/e08a9143fd5ca1c5538494bd4fd3bc2c03ac949a7b002131061c25dd885a4192/probability-inspect-d7ca799e638e.json`; source revision `45e1df0aec2c508dc7525de40ef444a30dda18bb59937ad50ed383eb922ed442`; source hash `d7ca799e638e1aa090b0b95bbb31f832e082f69b02a8b927bd052a67f81a0e66` |

The exact named scenario set reused by the post-patch comparison was `REPRESSION_1936_BASELINE_2026_08_27` with `GER_1936_DACHAU_ONLY`, `JAP_1936_STATE_716_ACTIVE_611_PINGFANG_DORMANT`, and `SOV_1936_KOLYMA_MAGADAN_KARAGANDY_FAMINE_AFTERMATH`.

All three scenario states were `{}` again, so candidate-pool completeness is source-relative but country, target, state, war, equipment, cost, cap, cooldown, and route inputs remain runtime-incomplete.

### Baseline/post comparison attempt

The first compare request attempted `before = { source = { path = ... } }` and `after = { source = { path = ... } }` and was rejected with the exact MCP error `MCP error -32602: Input validation error: Invalid arguments for tool hoi4.probability_compare: Unrecognized key: "source" at before; Unrecognized key: "source" at after`.

The accepted retry used path-shaped snapshots, `before = { path = "common/decisions/camp_repression_major_country_decisions.txt" }` and `after = { path = "common/decisions/camp_repression_major_country_decisions.txt" }`, with the complete 29-candidate major-country pool and the exact scenario set above.

That compare returned `PROBABILITY_ANALYZED_PARTIAL`, `analysisId=probability-12e49ed5bbb7ad85220be135`, `sourceRevision=45e1df0aec2c508dc7525de40ef444a30dda18bb59937ad50ed383eb922ed442`, `sourceHash=9d281e9e64010863a8d6cc61387ec072ea9eff75736f7777ece9f61920ae9124`, `scenarioHash=35d257245a3a0c4217bcf022d847019d091cc89cd55d5f03e1de4ee41323a2c6`, 87 candidate rows across three scenarios, 159 unresolved items, 6 diagnostics, and `comparisonChanges=0`.

The authoritative compare artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ae8a0745c1d9a699890e56684bddbb4b92e9b872dec0843c78a6605a9eb84a60/faa1135d42022e738b92179ce840e77401dbca2e9a0687ff6679adf04fab9ae8/probability-12e49ed5bbb7ad85220be135.json`.

The compare renders are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/50a13fd7717ca4201f23366cd990030747be4850c64be4d6f5a110f55e7e262c/probability-probability-12e49ed5bbb7ad85220be135-comparison.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a989473f74bf89e49d20354aa26cc6a09e8b2eabc775a8a359c5ec6ae6efc98f/47c676c5189eb79975f8af462b149505d4d4ee57b0cb4c6db33f13e7769de9a9/probability-probability-12e49ed5bbb7ad85220be135-ranking.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f30dce392efbdd49ab3c6b1afc4ae4721a9d5f648a7b3b2a0c9f11695f1574fb/311747fdc5b62a20f143790779054ca957ffa6e7a65b155cce7a2ac149fc7c93/probability-probability-12e49ed5bbb7ad85220be135-matrix.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a7f76f1a68bc7b729df06449d5306f67b871749746b2ed23068515336e4784ff/d007870dd89b058599a36f6232d00f90cab5eb56396f4a812740b93651b6a664/probability-probability-12e49ed5bbb7ad85220be135-unresolved.svg`.

Because both path-shaped snapshots resolved the current post-patch file, `comparisonChanges=0` is not a historical baseline/post delta and cannot prove that the old source and new source had identical AI weights.

The compare diagnostics were limited to empty-fixture outcomes: an unsatisfied Japan invite modifier, never-eligible Japan Ishii removal, unsatisfied Japan Ishii shield modifier, never-eligible Soviet famine concealment, never-eligible Soviet NKVD reinforcement, and never-eligible Soviet industrial transfer. These diagnostics do not establish a post-patch regression because the required scenario state was not supplied.

### German route result

The German peacetime conclusion is source-proven and exact at the availability layer: under `GER_1936_DACHAU_ONLY` as intended, `has_war = no` makes `germany_route_prisoner_labor_to_war_construction` unavailable even if its AI willingness score evaluates to 70, because the decision `available` block contains a hard `has_war = yes` requirement.

The same hard gate is present in the GUI action rebuild, so the corresponding country-panel action is not marked available during intended peacetime 1936 either.

The wartime reachability conclusion is exact but conditional: the route can become available when GER is fascist and at war, expansion is not frozen, `camp_labor_output > 0`, the action cooldown is clear, and motorized, train, and support-equipment requirements pass.

The route retains `days_re_enable = @CAMP_GERMANY_WAR_CONSTRUCTION_COOLDOWN_DAYS`, whose source constant is 365 days, and the AI score remains the 70-point `camp_rework_ai_weight.germany_expansion` family with only the critical-overstretch hard-zero modifier.

Therefore the owner patch closes the specific 1936 peacetime visibility/availability hole without lowering wartime AI willingness; wartime rank, dominance, repetition, and execution timing remain unresolved until the analyzer receives complete state and resource fixtures.

### Cost and cross-country implications

The reduced expansion resource packages do not alter the `ai_will_do` score trace, but they can widen the set of executable candidates after route eligibility is true.

For Germany, the war-construction route still requires motorized equipment, trains, and support equipment in both the decision and GUI paths, while the laboratory-annex package no longer requires command power or infantry equipment in its custom-cost trigger.

For Japan and the Soviet Union, the reviewed Pingfang-establishment, industrial-transfer, and extreme-periphery packages similarly retain manpower, support-equipment, and train requirements while dropping command power and infantry-equipment requirements.

This is a bounded availability observation, not a claim that those actions will be selected: the MCP adapter provides score/eligibility traces but no normalized decision probability or timing distribution.

### Post-patch status, blockers, and follow-up

- `GER_1936_DACHAU_ONLY`: German route hard-unavailable in intended peacetime 1936 is `exact` at source availability; complete country ranking and post-patch probability are `unresolved`.
- `JAP_1936_STATE_716_ACTIVE_611_PINGFANG_DORMANT`: route and cost effects remain `unresolved`; the source still uses state 328 for the Pingfang anchor while the scenario name references state 611.
- `SOV_1936_KOLYMA_MAGADAN_KARAGANDY_FAMINE_AFTERMATH`: cap, famine, paranoia, and periphery ranking remain `unresolved` with the empty fixture.
- No `hoi4.probability_sweep` was run in this post-patch pass, so no sensitivity or rank-reversal claim is made.
- No separate `hoi4.probability_render` call was needed because compare emitted comparison, ranking, matrix, and unresolved artifacts.
- A true historical baseline/post compare remains blocked because the MCP compare API accepts source paths but no baseline revision or artifact snapshot field, and the old source file is not available as an in-scope immutable path.
- The parent should rerun compare after supplying an immutable pre-patch source snapshot and adapter-compatible primitive state for GER peacetime/war, Japan state 328 plus route status, and Soviet famine/periphery values.

No gameplay, localisation, GUI, decision, mission, trigger, effect, or constant file was edited by this post-patch audit, and no commit was created.

## Final colonial availability probability audit — 2026-08-27

### Scope and current source

This dated section is the final read-only pass for the colonial availability change requested by the parent.

The audited decision source is `common/decisions/camp_repression_colonial_country_decisions.txt`, with the directly relevant decision `uk_expand_raj_detention_districts` at lines 240-323 and the adjacent United Kingdom/Raj candidate pool listed below.

The generic cross-country control was audited in `common/decisions/camp_repression_generic_decisions.txt`, with `generic_restricted_contaminated_site_escalation` at lines 684-773.

The shared tuning source was `common/script_constants/camp_repression_rework_constants.txt`, including `camp_rework_cost.expansion_manpower = 10000.00` at line 661, `camp_rework_equipment_cost.infantry_equipment = 650`, `support_equipment = 180`, and `trains = 18` at lines 678-681, `camp_rework_timing.decision_cooldown_days = 60` at line 754, `camp_rework_ai_weight.blocked = 0.00` at line 849, `uk_wartime_low_expansion = 25.00` at line 889, `uk_wartime_high_expansion = 45.00` at line 891, `uk_high_chaos_expansion = 55.00` at line 895, and `generic_radicalized = 12.00` at line 878.

The current `uk_expand_raj_detention_districts` source has a `custom_cost_trigger` requiring manpower above the 10,000 threshold and infantry/support equipment above the 650/180 thresholds, while its `available` block repeats those three resource requirements and has no `command_power` requirement.

The same decision remains restricted to `original_tag = ENG`, requires an active camp network, not-frozen expansion state, and either war or Indian autonomy resistance above the medium band for visibility, and requires an AI-controlled or player-selected valid UK-expandable action state for availability.

Its `ai_will_do` remains `base = constant:camp_rework_ai_weight.blocked` with a 25-point wartime low-resistance modifier, a 45-point wartime high-resistance modifier, and a 55-point non-democratic chaos-tier modifier, all subject to the source-local crisis/chaos exclusions shown at lines 281-323.

The current `generic_restricted_contaminated_site_escalation` source adds a `custom_cost_trigger` containing only the chemical-route or radicalized-route-plus-biological-capacity OR condition at lines 689-697.

Its `ai_will_do` remains `base = constant:camp_rework_ai_weight.generic_radicalized` with factor-zero gates for being outside the AI restricted-method cap, condemnation at 25, and high `camp_overstretch` at lines 762-773.

The source diff confirms that the colonial owner change removed only `command_power > constant:camp_rework_cost.expansion_command` from `uk_expand_raj_detention_districts` availability and added the matching non-political-power cost trigger/text; the generic owner change inserted its custom cost trigger before `custom_cost_text` and did not alter the generic restricted decision's `ai_will_do` block.

### Mandatory MCP inspect evidence

The required first weighted-surface call used the `decision_ai_will_do` adapter in workspace `mod_chaos_redux_ea3b2d67c2c0` with `refresh = true`.

The colonial inspect returned `PROBABILITY_SOURCE_INSPECTED`, `poolComplete = false`, 37 discovered candidates, 0 available under the empty adapter fixture, 26 required inputs, and 0 unresolved items.

The authoritative colonial inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b63f945196c0f4f32cca258f3da986659f8958f718bd4b7163667eaaa1180c43/7da3e4696bc742de7000e36ac88d7849d97ffa7473ae48ecccd637e96cb16c67/probability-inspect-8ff3cf4a2b2c.json` with artifact SHA-256 `b63f945196c0f4f32cca258f3da986659f8958f718bd4b7163667eaaa1180c43`, source revision `8769e5bb4854e144b5f9c720fb288d62ab9fc134938ebfd6d90fe58d4c420c21`, and source hash `8ff3cf4a2b2c2e6b42e453206f0b76cdae9bc238ab73321533f5ce5be2e651ad`.

The generic inspect returned `PROBABILITY_SOURCE_INSPECTED`, `poolComplete = false`, 14 discovered candidates, 0 available under the empty adapter fixture, 27 required inputs, and 0 unresolved items.

The authoritative generic inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d421885f88fcbd1034cf1622641d93b8d48585bd0eefead12e13192dac1c08ea/d9162d2d97a0785830c563ae890202b6865297165723632f0d4a6bccc5ee5020/probability-inspect-7ee49034b6f5.json` with artifact SHA-256 `d421885f88fcbd1034cf1622641d93b8d48585bd0eefead12e13192dac1c08ea`, source revision `8769e5bb4854e144b5f9c720fb288d62ab9fc134938ebfd6d90fe58d4c420c21`, and source hash `7ee49034b6f5e17786c320a5d6e3e0fef68c320a0523b0ab2203e46c890b4e55`.

The adapter identifies decision `ai_will_do` as score-only, exposes raw values and eligibility, does not normalize selection probabilities, and does not convert decision cooldowns into timing distributions.

### Candidate pool and scenario contract

The explicit UK/Raj comparison pool was `uk_survey_raj_emergency_detention`, `uk_activate_raj_emergency_detention`, `uk_route_colonial_labor_to_military_construction`, `uk_expand_raj_detention_districts`, `uk_demand_indian_manpower_levy`, `uk_tighten_dominion_security_coordination`, `uk_allocate_additional_colonial_guards`, `uk_release_political_prisoners_for_negotiations`, `uk_reform_colonial_labor_administration`, `uk_dismantle_raj_detention_network`, `uk_hold_raj_security_line`, `uk_complete_raj_military_works`, `uk_postwar_raj_review`, and `uk_negotiate_indian_release_terms`.

This is a deliberate country-specific pool, not the complete 37-candidate source pool, so no cross-country rank or normalized selection claim is made.

The named scenario set was `REPRESSION_ENG_RAJ_EXPANSION_2026_08_27` with the following four scenarios: `ENG_RAJ_PEACETIME_RESOURCES_SUFFICIENT`, `ENG_RAJ_PEACETIME_RESOURCES_INSUFFICIENT`, `ENG_RAJ_WARTIME_RESOURCES_SUFFICIENT`, and `ENG_RAJ_WARTIME_RESOURCES_INSUFFICIENT`.

The sufficient fixtures declared `tag = ENG`, `original_tag = ENG`, `is_ai = yes`, `manpower = 100000`, `infantry_equipment = 1000`, `support_equipment_1 = 1000`, `indian_autonomy_resistance = 0`, and `camp_labor_output = 1`, with `has_war = no` for peacetime and `has_war = yes` for wartime.

The insufficient fixtures used the same identity and route-neutral values but set `manpower = 0`, `infantry_equipment = 0`, and `support_equipment_1 = 0`, with the same peacetime/wartime split.

The primitive country values were accepted by the adapter, but compound/scoped checks remained incomplete because the scenarios did not declare state targets, controlled-state pools, `has_variable` flags, country/global flags, active-network/cap variables, cooldown flags, route decisions, government, or the scoped `has_equipment` facts.

Therefore candidate-pool completeness is intentionally source-relative and scenario completeness is incomplete; all probability conclusions below are classified as exact source gates, score-only, bounded, or unresolved rather than exact live selection probabilities.

### Colonial evaluate evidence

The full explicit-pool evaluator returned `PROBABILITY_ANALYZED_PARTIAL` with analysis ID `probability-fce98a316ae3ecdb7277622c`, source revision `237dd2ca17b82dbaeac302a250a15b1ea8dcffffb4c75f7e6d5db10de66ff13c`, source hash `8ff3cf4a2b2c2e6b42e453206f0b76cdae9bc238ab73321533f5ce5be2e651ad`, scenario hash `3a1e4c9a49c4fb0221b7832e6de320bf5c03d09a94f7a6d52533aa89545e3780`, 36 candidate rows, 59 unresolved items, 2 diagnostics, and 6 emitted visual resources.

The authoritative full-pool evaluator artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6b5665589635fb1cc696e4a176392897bb9263eaa8c9676ab7ea3f7085eee961/0f1f2666889409910d4960d9096df046b5244a3f72945a363d6c9819a0148c5f/probability-fce98a316ae3ecdb7277622c.json` with artifact SHA-256 `6b5665589635fb1cc696e4a176392897bb9263eaa8c9676ab7ea3f7085eee961`.

The full-pool diagnostics were `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` for `uk_activate_raj_emergency_detention` across all four supplied scenarios and `PROBABILITY_MODIFIER_UNSATISFIED_IN_SCENARIOS` for the exposed-reform modifier on `uk_release_political_prisoners_for_negotiations`.

A narrowed evaluator for `uk_expand_raj_detention_districts` returned `PROBABILITY_ANALYZED_PARTIAL` with analysis ID `probability-9fdbcf9b3548ce2ebc500b04`, source revision `237dd2ca17b82dbaeac302a250a15b1ea8dcffffb4c75f7e6d5db10de66ff13c`, source hash `8ff3cf4a2b2c2e6b42e453206f0b76cdae9bc238ab73321533f5ce5be2e651ad`, the same scenario hash `3a1e4c9a49c4fb0221b7832e6de320bf5c03d09a94f7a6d52533aa89545e3780`, 4 candidate rows, 10 unresolved items, 0 diagnostics, and 6 emitted visual resources.

The authoritative narrowed artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a9e4ed4dc7685ebd7f648ae6b64d44c6e60fee6c70e1b1a13440e82251de2aa6/8f5d085faf3c2cdb89e22f7557cb20a0a3dc4c8dbe4c49cd627fd32cc048b2df/probability-9fdbcf9b3548ce2ebc500b04.json` with artifact SHA-256 `a9e4ed4dc7685ebd7f648ae6b64d44c6e60fee6c70e1b1a13440e82251de2aa6`.

The emitted narrowed matrix is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/95414a9ec26645d2580fa407d20f7b1f274512bf99f810910fd08c0e3ea6dc6e/b13d48cc4906763d8b11925cb1088d669608c7fae6443d849b096c37933a5964/probability-probability-9fdbcf9b3548ce2ebc500b04-matrix.svg` and records raw value `0` for `uk_expand_raj_detention_districts` in all four scenarios.

The emitted narrowed ranking is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2739f9238e8c46bd50fab4601df3e6f3dc07af4482f31b8cce1be00c6d030fd6/c57da7b130e5458c791a3cd9609774bd80cf9cbb6c86476ec6659dc11ccd44df/probability-probability-9fdbcf9b3548ce2ebc500b04-ranking.svg` and shows `0.00000` for the peacetime sufficient row.

The zero rows are score-only fixture outcomes, not proof that the wartime modifiers can never activate, because the adapter left route flags, cap state, government, crisis flags, and compound conditions unresolved.

### Colonial identical-scenario compare

The mandated path-shaped compare used the same current colonial path for `before` and `after`, the same 14-candidate UK/Raj pool, and the exact four scenario IDs above.

It returned `PROBABILITY_ANALYZED_PARTIAL` with analysis ID `probability-5b77bfe4a4ec9879226f03cd`, source revision `237dd2ca17b82dbaeac302a250a15b1ea8dcffffb4c75f7e6d5db10de66ff13c`, source hash `8ff3cf4a2b2c2e6b42e453206f0b76cdae9bc238ab73321533f5ce5be2e651ad`, scenario hash `3a1e4c9a49c4fb0221b7832e6de320bf5c03d09a94f7a6d52533aa89545e3780`, 36 candidate rows, 59 unresolved items, 2 diagnostics, and `comparisonChanges = 0`.

The authoritative colonial compare artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3ae694e52a2eae36d093569144a113c0486c67ac357a226adf3596b1e99d0f1f/9aeb3c954ca120f6007e0d57a7f4176c48b486a12802458c12cfba6c6a16ec78/probability-5b77bfe4a4ec9879226f03cd.json` with artifact SHA-256 `3ae694e52a2eae36d093569144a113c0486c67ac357a226adf3596b1e99d0f1f`.

The emitted comparison render is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/b9193d6ab96cc8fa73621d91ad08d98b8af68559d8556a5f424e932bc032cf7e/probability-probability-5b77bfe4a4ec9879226f03cd-comparison.svg`.

The emitted compare matrix is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/78daed08fa58534330b20cfbd3c8c6eee5481a54fccc54007021b96c253af1b4/616596d358078129666f88f15b2d665867d6519f11b0324103132b8ec2e967f0/probability-probability-5b77bfe4a4ec9879226f03cd-matrix.svg`.

Because the MCP compare API accepted only path-shaped snapshots in this run, both sides resolved the same current post-change file and `comparisonChanges = 0` is not a historical prepatch/postpatch delta.

The explicit render retry also returned `PROBABILITY_ANALYSIS_STALE` with the exact warning `Workspace sources changed after this analysis; run the analysis again before rendering`, reporting analysis revision `237dd2ca17b82dbaeac302a250a15b1ea8dcffffb4c75f7e6d5db10de66ff13c` and current revision `6d4a9838a1eb99f45315e828277b34ec080f325a6ede98e473728acc5ea6758d`.

This concurrent worktree revision drift is an additional blocker on claiming that the emitted render is final-current evidence, although the in-scope source hunk was re-read after the drift and remained unchanged.

### Generic restricted-site compare

The generic path-shaped compare used the same four named ENG/Raj scenarios and the single candidate `generic_restricted_contaminated_site_escalation` on identical current paths.

It returned `PROBABILITY_ANALYZED_PARTIAL` with analysis ID `probability-e0343d603ff8c1da5d74c706`, source revision `237dd2ca17b82dbaeac302a250a15b1ea8dcffffb4c75f7e6d5db10de66ff13c`, source hash `7ee49034b6f5e17786c320a5d6e3e0fef68c320a0523b0ab2203e46c890b4e55`, the same scenario hash `3a1e4c9a49c4fb0221b7832e6de320bf5c03d09a94f7a6d52533aa89545e3780`, 4 candidate rows, 103 unresolved items, 0 diagnostics, and `comparisonChanges = 0`.

The authoritative generic compare artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/097e275f22b20f94c7c462a63272e5d6402abeed578b2094a78a54f0439762f0/6e927f6d3317ed365da8d0dea109bb9d69ec0b53667ad089acfaf87bd50cba2c/probability-e0343d603ff8c1da5d74c706.json` with artifact SHA-256 `097e275f22b20f94c7c462a63272e5d6402abeed578b2094a78a54f0439762f0`.

The emitted generic comparison render is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/66ce7de54e4e7adee2debbb332a9bfaa5afc3803fc0101f56a459c5b6a5ee67a/probability-probability-e0343d603ff8c1da5d74c706-comparison.svg`.

The zero-change result is not a historical delta, but source inspection and the identical current snapshot compare both show that the new `custom_cost_trigger` did not alter the `ai_will_do` weighting surface.

### Findings by scenario and requested risk

- `ENG_RAJ_PEACETIME_RESOURCES_SUFFICIENT`: the AI score is source-bounded to 0 in the intended 1936 baseline when war is false, the high-chaos branch is absent, and the source's crisis/route exclusions are satisfied; the MCP narrowed matrix also observed 0, but left 10 trigger inputs unresolved. The decision is not hard-unavailable solely because it is peacetime: its `available` block has no war requirement, so if active-network/visibility, valid target, unfrozen state, resources, and the AI state pool are true, removing command power can make the decision executable in peace. Classification: `bounded score-only`, with source-proven availability gates and runtime-unresolved target/cap facts.
- `ENG_RAJ_PEACETIME_RESOURCES_INSUFFICIENT`: the source's manpower, infantry-equipment, and support-equipment requirements are hard availability gates, so a zero-resource state cannot execute the decision even if an AI modifier were otherwise active. The custom cost trigger mirrors the same resource floor. The MCP fixture did not bind compound equipment checks, so the runtime eligibility result remains unresolved. Classification: `exact source gate` plus `unresolved runtime eligibility`.
- `ENG_RAJ_WARTIME_RESOURCES_SUFFICIENT`: war satisfies the wartime branch and visibility OR, and the resource values exceed the declared thresholds, but valid UK-expandable state selection, active network, cap, cooldown, crisis, government, and resistance facts were not fully supplied. Conditional source score is 25 at low resistance or 45 at high resistance over the blocked base, with a separate 55 high-chaos branch for non-democratic chaos tiers 4/5. Classification: `bounded conditional score`, not a rank or probability.
- `ENG_RAJ_WARTIME_RESOURCES_INSUFFICIENT`: war can activate the AI modifier, but the source's three resource gates still block execution when manpower or either equipment requirement is below threshold. The MCP matrix observed raw 0 under the unresolved fixture and cannot distinguish an AI score from executable eligibility. Classification: `exact source gate` plus `unresolved runtime score/eligibility`.
- AI weighting invariance: the colonial patch changes only availability/custom cost logic; `uk_expand_raj_detention_districts` retains the same base and modifiers. The generic `custom_cost_trigger` similarly changes only route/resource execution gating; its base 12 score and three factor-zero conditions are unchanged. Classification: `source-proven score invariance`, with historical delta unverified because the prepatch snapshot is unavailable.
- Dominance/starvation/rank reversal: no exact cross-candidate rank, normalized probability, timing, or rank-reversal result is valid because the adapter requires a documented complete selection rule and the supplied pool is intentionally country-scoped. The full-pool compare is score/eligibility evidence only.
- Cooldown/repetition: `days_re_enable = constant:camp_rework_timing.decision_cooldown_days` is source-proven as 60 days, but the adapter does not model decision cadence, cap transitions, cooldown flags, or post-completion state. Repetition and timing claims remain unresolved.
- Exploit risk: the availability change can widen peacetime execution reachability if the high-resistance visibility branch and valid target/resource conditions are true, while the AI score remains 0 in ordinary low-chaos peace. This is not a proven exploit in the supplied fixture and no balance target is selected.

### Blockers and unmodified follow-up

- The MCP compare API rejected the earlier nested `before = { source = { path = ... } }` shape with `MCP error -32602: Input validation error: Invalid arguments for tool hoi4.probability_compare: Unrecognized key: "source" at before; Unrecognized key: "source" at after`; the accepted path-shaped retry cannot reference an immutable prepatch snapshot.
- The explicit render call was stale because another worktree edit changed the workspace revision after evaluation; the exact analysis/current revision pair is recorded above.
- The adapter left state targets, controlled-state pools, flags, variables, caps, cooldowns, governments, route decisions, and compound equipment checks unresolved, so no exact live eligibility, rank, normalized probability, timing, repetition, or dominance claim is made.
- `hoi4.probability_sweep` was not run because the supplied scenarios did not provide complete declared ranges for the scoped state/flag/cap inputs; no sensitivity or rank-reversal claim is made.
- `hoi4.probability_simulate` and `hoi4.probability_sequence` were not run because no uncertainty distribution or complete custom-pool cadence/state-transition manifest was supplied.
- A follow-up should freeze the two source revisions, provide an immutable prepatch copy to `probability_compare`, and rerun inspect/evaluate/compare/render with adapter-compatible declarations for active-network state, valid Raj target ownership, cap/cooldown flags, route state, government, resistance, and compound equipment facts.
- No gameplay, AI, decision, mission, trigger, effect, GUI, localisation, constant, or other runtime file was edited by this audit, and no commit was created.
