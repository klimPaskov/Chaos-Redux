# Event 24 Runtime Restriction Probability Comparison

Status: incomplete and blocked for numerical probability acceptance. The required probability and event analysis routes returned no analysis artifacts, comparison IDs, source revisions, scenario hashes, pool-completeness results, or rendered evidence. No balance clearance is given.

Acceptance basis: the user accepted the complete package in docs\specs\024_video_game_in_sweden_specs and requested this read-only postpatch comparison. The parent’s later L24 decision, duration, getter, and localisation patch arrived after the original AFTER snapshot and is preserved in a separate supplemental snapshot below.

## Scope and disposition

This audit wrote only this handoff, the original physical AFTER snapshot folder, its accepted-scenario-matrix copy, post_localisation_reservations and its D fixture, post_localisation_reservations_followup, post_l24_private_output_followup, post_l24_mission_callback_followup, and post_l24_event_text_followup. No gameplay or localisation source, shared index, unrelated agent work, or Git state was changed. No commit was made, no HOI4 session was launched, no service was restarted, and no tests were run.

I read AGENTS.md, chaos-redux-subagents, chaos-redux-events, chaos-redux-mtth, chaos-redux-decisions-missions, all files in the Event24 specification package, and the named source reports 16, 19, and 20. The four required repo skills were used as read-only audit guidance. No skill was created or changed.

The parent’s note named 12 current runtime source cases, but the final live test file contains 14 test methods and has SHA-256 356eb2564293f60e5a1452d901500f224c35a2289d223c92dac33a2211e9b036. The 12 earlier cases cover daily elapsed accounting, sticky interruptions, one pending watch, Stockholm disqualification, early reassessment, ownership-aware cleanup, closed-receipt idempotence, cloned-host annexation, restriction proof receipts, restriction closure, native factory-reservation progression, and full/narrow proof localisation. Two later cases cover wrong-mission/closed-callback rejection and failure cleanup without backlash. I verified the current source contains 14 methods but did not execute them, so this report does not call them passing.

## Frozen source identities

The BEFORE remains the immutable 14-file physical copy at docs\plans\024_video_game_in_sweden_plans\probability_snapshots\2026-10-03_pre_remaining_routes. Its identity and capture evidence remain in handoff 19. That folder still contains 14 files. Earlier 13/14/15/18 evidence folders remain in place and were not edited or recopied.

The original AFTER remains the physical copy at docs\plans\024_video_game_in_sweden_plans\probability_snapshots\2026-10-03_post_runtime_restriction. It was captured before the parent’s L24 patch and was not overwritten. It contains 18 mirrored Event24 source files and the copied accepted scenario matrix. At the latest drift check, 11 original AFTER sources still matched live; three sources matched post_localisation_reservations; one trigger source matched post_l24_private_output_followup; one effects source matched post_l24_mission_callback_followup; and the current event/localisation pair matched post_l24_event_text_followup.

All original AFTER source files were copied with Copy-Item, not hard-linked. Their copied SHA-256 values matched live source at capture. No copied source was a reparse point, and no live source had the ReadOnly attribute. The accepted scenario matrix copy is fixtures\024_video_game_in_sweden_ai_probability_scenarios.md, SHA-256 288cd312f9bedac91159f970cce16ed6dcf71dfb1d459411360dea0a355b34ca.

| Original AFTER source path | Bytes | SHA-256 |
| --- | ---: | --- |
| events\024_hearts_of_iron.txt | 34,773 | 36a3be4f03a942e08ea6dc3bdb3c20a8e112a54d667bda91d031beaecc51c159 |
| common\decisions\024_video_game_in_sweden_decisions.txt | 38,572 | 8b19fcb187ff40bcfd66c49ff54ec18b009d5724cc6d74ec5bc416af463b6eef |
| common\decisions\categories\024_video_game_in_sweden_categories.txt | 945 | 12778be8725534f1872a568f137f079f2f7f69e3f8d775e2c89653991ddac68b |
| common\dynamic_modifiers\024_video_game_in_sweden_dynamic_modifiers.txt | 2,970 | e78b8fa660c12808fd36e0f4e0f3bf951bf79f9b8871e83a053590741de34670 |
| common\ideas\024_hearts_of_iron_ideas.txt | 3,981 | b4e3517a79d27c0347a94be4c2a88d1dd32553e5f911208d56c2391f532bdd0d |
| common\ideas\024_video_game_in_sweden_cxt_ideas.txt | 563 | 8db195e24487f97fbdcc8429c8c5c80672e17eb957fbeca1d9ff75e3e1b00e29 |
| common\on_actions\024_video_game_in_sweden_cxt_on_actions.txt | 1,228 | 34ab09370af68a547cf69c99626c8a42c0dd4747efda7efe84fa75ae40905812 |
| common\on_actions\024_video_game_in_sweden_lifecycle_on_actions.txt | 907 | 146ae2ff3ca85adf67a11de3374e842173e530f394cfc597e4b316d4cf1a68de |
| common\opinion_modifiers\024_video_game_in_sweden_opinion_modifiers.txt | 743 | 64f9202fdaa6116eb2ea3ec634bbfc5c4a7930db31784dda5099db1377fc2cd8 |
| common\scripted_effects\024_video_game_in_sweden_effects.txt | 124,675 | 0c2150446c29082bf684301d885375e9a3c516f7598f80f470c70eb7ef7a6223 |
| common\scripted_effects\024_video_game_in_sweden_cxt_effects.txt | 1,858 | 84e2d9f1143504fb308720047d33c7e669cbecbe6e2cd29309a372855095469d |
| common\scripted_effects\024_video_game_in_sweden_runtime_effects.txt | 8,712 | 4aa52824d237180d59c2e57e8c23d4dc5a6841b93d243e779004f20466b89efb |
| common\scripted_localisation\024_video_game_in_sweden.txt | 13,835 | 8d1d97965bbcdd572503950684bb8677d10bb65a124146bbbb20011e616a92ad |
| common\scripted_triggers\024_video_game_in_sweden_triggers.txt | 31,869 | 3904b9a6db454c6c6abadaf5421514b354d1bd72f0563a2b9ad31c8ccb41eb48 |
| common\script_constants\024_video_game_in_sweden_constants.txt | 14,387 | a498c1c0458a69b9e377efeb0a4e3d4c94828185db48797e520e1dc1e6159c19 |
| common\unit_leader\024_video_game_in_sweden_traits.txt | 690 | a00b80adc5dbb04e58068b8ac3568bf751633df809ab70b7584029c388e8b240 |
| localisation\english\024_hearts_of_iron_l_english.yml | 44,014 | b592952de06cf1ec8e14007750a669f6858d6236b30043c6c1f8ce77b1e1b1b0 |
| localisation\english\024_video_game_in_sweden_requirement_flags_l_english.yml | 3,122 | e4bc29c9a933d871c5f8f3adea10e331d92585478569b2f5b86eb941547866a8 |

## Supplemental L24 snapshot

The parent’s L24 source patch arrived after the original AFTER capture. I preserved it under docs\plans\024_video_game_in_sweden_plans\probability_snapshots\2026-10-03_post_runtime_restriction\post_localisation_reservations without changing the original AFTER. This child contains five current source copies and fixtures\P24_FINAL_DECISION_MATRIX.json. The fixture declares P24-D1 through P24-D5 and the relevant P24-C5/P24-C7 cases, with incomplete inputs retained as unresolved rather than forced through candidateOverrides.

| Supplemental source path | Bytes | SHA-256 |
| --- | ---: | --- |
| common\decisions\024_video_game_in_sweden_decisions.txt | 39,349 | 686e58631adfc7493ec1defac544ae470a60319ed04f74575ed3f5e3ac0607ba |
| common\scripted_effects\024_video_game_in_sweden_effects.txt | 124,789 | 38579b04e9bff4c8de72c952782041256f8771adad5568b451bd1b309dd1cdbf |
| common\script_constants\024_video_game_in_sweden_constants.txt | 14,425 | da0a4c5918ff3f3f8b1e321d7454877c4971d8d33cb342b6863ea7cb49451f4e |
| common\scripted_localisation\024_video_game_in_sweden.txt | 14,164 | 357d92a47cea45066657eedcf5794fcdd91878171ab2bee2319d2e21e499137f |
| localisation\english\024_hearts_of_iron_l_english.yml | 45,293 | ae8911e200066dce4a9542bb40b5ac631a8a8a377270b8470c3bd53e1b6ad2a2 |
| fixtures\P24_FINAL_DECISION_MATRIX.json | 2,104 | 91668b4b3e4a9ac11c3de7a224fc57d314bf2edd89254859c0c23b83b38545ce |

All five post_localisation_reservations copies matched live files at capture, had no reparse points, and their live sources did not have ReadOnly set. The decision, constants, and scripted-localisation copies still match live. The effects and English localisation copies were superseded by later captures. The original AFTER remains unchanged and is still the source identity for the pre-L24 runtime restriction comparison.

## Intermediate source drift after the L24 reservation capture

The live main effects and scripted trigger files changed again after post_localisation_reservations and after the D1-D5 probability compare attempt. I preserved that intermediate state in docs\plans\024_video_game_in_sweden_plans\probability_snapshots\2026-10-03_post_runtime_restriction\post_localisation_reservations_followup. The first AFTER and first supplemental copies remain untouched, and this intermediate child is retained even though a later identity superseded it.

| Intermediate follow-up source path | Bytes | SHA-256 |
| --- | ---: | --- |
| common\scripted_effects\024_video_game_in_sweden_effects.txt | 126,214 | c8a5203462dee60e550adeddd04d8524c37407ec988c822ecc495099ca1d1adc |
| common\scripted_triggers\024_video_game_in_sweden_triggers.txt | 33,411 | 22d7c3ee6c5311b68f739d599470cbfc2ba392bf1610671b3a0268312bc6fc1d |

These two intermediate copies matched live source at capture, had no reparse points, and their live files did not have ReadOnly set. They were later superseded by post_l24_private_output_followup. This child contains two intermediate source copies. The seven-scenario D fixture remains in post_localisation_reservations\\fixtures and was not duplicated.

## Intermediate helper and callback source drift

The main effects and scripted trigger files changed again after post_localisation_reservations_followup. I preserved those intermediate bytes without rewriting either earlier snapshot in docs\\plans\\024_video_game_in_sweden_plans\\probability_snapshots\\2026-10-03_post_runtime_restriction\\post_l24_private_output_followup.

| Intermediate source path | Bytes | SHA-256 |
| --- | ---: | --- |
| common\\scripted_effects\\024_video_game_in_sweden_effects.txt | 126,267 | fba6a2b5e44590e376ea60add2ae2ee7e394a8078c2d4333e929b1753e9bf9e2 |
| common\\scripted_triggers\\024_video_game_in_sweden_triggers.txt | 33,732 | 1c3b24791f77e2e0ef4a76ced3b9af342366e0f0514cc3745811bd6f916b3fc8 |

The main effects change adds a restriction-callback wrapper, renames the old body to video_game_in_sweden_failed_restriction_apply_current, and routes restriction success/timeout through video_game_in_sweden_restriction_callback_is_current. Field-validation, Reality Audit, and Dual Track success callbacks also check the current host. The new scripted trigger binds program-active, restriction-active, and the active-mission receipt. These edits affect mission lifecycle and stale-callback eligibility, not an ai_will_do numeric factor.

These intermediate copies matched live source at capture, had no reparse points, and their live files did not have ReadOnly set. The effects copy was later superseded by the failure-callback wrapper version below; the trigger copy remains the current trigger identity.

The intermediate follow-up effect and trigger hashes postdate every probability_compare attempt recorded below. No returned analysis used them. Earlier comparisons cannot be interpreted as a zero delta for later helper changes.

## Latest mission callback source drift

The main effects file changed again after post_l24_private_output_followup. I preserved the latest bytes in docs\\plans\\024_video_game_in_sweden_plans\\probability_snapshots\\2026-10-03_post_runtime_restriction\\post_l24_mission_callback_followup without replacing any prior copy.

| Latest source path | Bytes | SHA-256 |
| --- | ---: | --- |
| common\\scripted_effects\\024_video_game_in_sweden_effects.txt | 126,881 | dd97b58fabde606457c4f07a05492b74b5a4631e0674e025a5fe413716035c62 |

This final source delta renames the field-validation, Reality Audit, and Dual Track failure bodies to *_apply_current helpers and adds wrappers requiring each mission’s current-callback receipt before dispatching a failure body. It follows the restriction callback receipt pattern in post_l24_private_output_followup. The latest copy matched live source at capture, had no reparse point, and its live source did not have ReadOnly set.

These final effects and the current trigger identities postdate every probability_compare attempt in this handoff. No returned analysis used them. Numerical acceptance cannot be inferred from the earlier helper versions.

## Latest event and localisation source drift

The Event24 event and English localisation files changed after the probability_compare attempts. I preserved their current bytes in docs\plans\024_video_game_in_sweden_plans\probability_snapshots\2026-10-03_post_runtime_restriction\post_l24_event_text_followup without changing the original AFTER or any earlier supplemental copy.

| Latest source path | Bytes | SHA-256 |
| --- | ---: | --- |
| events\024_hearts_of_iron.txt | 34,906 | 38275738d6372aafad4c6ff4773dac5de545e3e5a269ec3dfcd7541ca17ab80c |
| localisation\english\024_hearts_of_iron_l_english.yml | 45,480 | aff2bc54cf7c4b53e188fc1a39fdba1276c4b606e243b81978c1ee4270f4bf1a |

The event diff changes chaosx.nr24.34’s description selector when video_game_in_sweden_restriction_failed is present. A source diff found no changed ai_chance, base, or factor lines in that event delta. The English localisation diff contains text changes only. Both copies matched live source at capture, had no reparse points, and their live files did not have ReadOnly set. They postdate the event-source comparison attempts, so no probability result covers this final source pair.

## L24 source delta relevant to D1-D5

No ai_will_do block or numeric AI score factor changed in the supplemental diff. The raw scores therefore have no source-level numeric weight delta in this patch. This does not establish unchanged campaign availability, rank, cadence, or lifetime, and the requested MCP compare returned no result.

The National League decision now uses days_remove = var:video_game_in_sweden_national_league_native_days. The variable is initialized to the 45-day national_league_burden_days value, and the remove effect adds the difference between the 60-day repeat burden and the 45-day initial burden, clamped at the new 90-day maximum. The repeated league’s civilian burden uses the same native variable.

Foreign licensing now uses a 30-day foreign_license_burden_days decision duration instead of the prior 5-day foreign_response_delay_days value. That 5-day constant remains the response-delivery delay and is a different timer. Dual Track now uses a 30-day dual_track_burden_days decision duration instead of the prior 120-day dual_track_days value. These decision row durations do not redefine the separately declared mission duration constants.

The patch wraps four decision availability predicates and four mission objective predicates in hidden_trigger while preserving their custom tooltip calls. The score factors are unchanged. The source diff changes visibility and tooltip exposure boundaries, so the D1-D5 availability comparison remains required even though no AI score factor changed.

The scripted-localisation file adds GetVideoGameAuditProofRequirements, selecting video_game_full_audit_proof_requirements or video_game_narrow_audit_proof_requirements from the narrow-audit state. The English YAML adds eight dynamic modifier names: video_game_in_sweden_model_surge, video_game_in_sweden_dual_track_package, video_game_in_sweden_field_failure_penalty, video_game_in_sweden_commercial_aftermath, video_game_in_sweden_foreign_copy, video_game_in_sweden_foreign_study, video_game_in_sweden_foreign_ban, and video_game_in_sweden_foreign_ridicule.

The source-only effect and mission updates are distinct from native decision timer evidence. The installed decision inspection schema supports point-in-time actor, date, control, state, flag, target, and scope declarations, but it has no scheduled timer-transition field. The connected read-only bridge’s allowlist does not include hoi4.decision_inspect, and no direct callable decision-inspect binding was available in this session. No tool result evaluated the native 30-day, 45-day, 60-day, or 90-day transitions.

## Weighted surfaces and source evidence

The following values are source bases and modifier traces, not evaluated scores, normalized shares, or campaign observations. The current Event24 event-option blocks and full 18-decision source have no changed ai_chance or ai_will_do source lines across the original AFTER and supplemental diff. Static source values do not replace the unavailable MCP pass.

| Surface and accepted scenarios | Complete local source candidate pool | Raw bases and named modifier traces | Candidate and external-factor completeness |
| --- | --- | --- | --- |
| Opening event chaosx.nr24.2, P24-O1 through P24-O4 | 3 options: chaosx.nr24.2.a, .2.b, .2.c | Controlled base 4.0 with peace 1.8, low stability 0.5, severe crisis 8.0. Commercial base 3.0 with high stability 1.5, war 0.4, severe crisis 0.0. Officer base 2.0 with war 2.0, low army experience 1.4, supply-crisis flag 0.25, severe crisis 0.25. | Source-local pool complete. Sweden host ownership/control, original-tag candidate population, host capacity, event-target validity, world_end and severe-crisis helper state are unconfirmed. O2 high tension/industry and O3 government type are not direct .2 score factors. The earlier O3 Officer-route flag assumption is intentionally omitted. |
| Evolution I event chaosx.nr24.11, P24-C1/C2 | 3 options | All bases 2.0. Auxiliary doctrine: war 1.8, route 1.3/0.8/3.0. Officer culture: low army experience 2.0, route 1.1/0.8/3.0. Red team: democratic 2.0, route 1.2/0.8/1.3. | Source-local pool complete. Host, phase, route, government, war and eligibility flags are not MCP-bound. No evaluate, sweep, or compare artifact. |
| Evolution II event chaosx.nr24.12, P24-C3/C4 | 3 options | All bases 2.0. National league: stability above threshold 1.6, severe crisis 0.10, route 0.9/1.4/0.8. Protect shifts: war 2.0, severe crisis 3.0, route 0.8/1.3/0.9. Preparedness: broad public reach 1.6, severe crisis 1.5, route 1.0/1.2/0.8. | Source-local pool complete. Public reach, crisis, industry, stability, route and host facts are incomplete. |
| Incident response event chaosx.nr24.30, P24-I1 through P24-I5 | 14 source options, two gated responses for each of seven incident families | Every response base is 1.0. Non-unit factors include supply response 0.25, enemy/red-team 2.0, enemy/supply 0.2, template/separate policy 1.8, template/supply 0.25, workplace/protected shifts 1.8, workplace/war 0.2, party/democratic 1.7, and party/supply 0.2. | Local option definitions complete; per-scenario eligible pair not MCP-confirmed. I3 workplace and party cases require separate current_incident values 6 and 7. P24-I4 lacks a verified live target. |
| Foreign response event chaosx.nr24.40, P24-F1 through P24-F5 | 5 options: Copy, Study, Ban, Ridicule, Ignore | Bases 1.0/1.0/0.8/1.0/0.8. Copy factors: friendly 2.5, low army experience 1.8, hostile 0.35, host mismatch 0.4. Study: friendly 1.3, hostile 2.5, low experience 1.5, major 2.0. Ban: fascist 2.2, hostile 1.8, mismatch 1.5. Ridicule: hostile 1.4, low threat 1.8, mismatch 2.0, recent Swedish victory 0.15. | Local pool complete. Foreign actor identity, Swedish host target, opinion, ideology, major status, army experience, threat, victory, target validity and complete partner pool are unresolved. P24-F5 may be ineligible before its five-option local pool is reached. |
| Evolution III reassessment event chaosx.nr24.50, P24-C5/C7 | 3 options: .50.a Reality Audit, .50.b Dual Track, .50.c Restrict Use | Audit base 3.5 with supply-crisis 2.0 and route 1.2/0.8/1.0. Dual Track base 2.0 with stability above threshold 1.6 and route 1.1/0.8/1.4. Restrict base 4.0 with route 1.1/1.0/0.9. | Local pool complete. Event trigger still requires current host, enabled Evolution III, and Trust Model active or mandatory reassessment pending. Host, current resources, reserve-limited quote outputs, affordability, active mission and full-audit field-package gates are incomplete. P24-C7’s surrender_progress 0.9 is an audit assumption, not live state. |
| Event incident selector video_game_in_sweden_roll_incident, P24-I1 through P24-I5 | 7 named random_list candidates: terrain, supply, enemy, template, diplomatic, workplace, party | Source weights are terrain 2.0, supply 3.0, enemy 2.0, template 2.0, diplomatic 2.0, workplace 2.0, party 2.0. The source initializes temporary weights to zero and applies each constant only through its family-validity gate. | Source candidate catalog complete. Current valid subset, seen-family receipts, cooldown, host, diplomacy target, campaign state and scheduled maintenance transitions are unresolved. No exact or bounded shares and no repetition frequency. |
| Prefire Stockholm host selection, P24-O1 through P24-O4 context | Dynamic country pool over every living original-tag SWE candidate; no complete candidate catalog supplied | The owner helper adds each country to a temporary array once per adjusted ticket and then calls random_scope_in_array. The parent’s caller now preinitializes adjusted-weight and active-load outputs. | Incomplete candidate pool. Shared helper source is not in the immutable BEFORE and AFTER Event24 snapshots. No normalized host share can be claimed. |
| Full Event24 decision category, P24-D1 through P24-D5 plus P24-C5/C7 | 18 definitions: video_game_controlled_exercise, video_game_logistics_module, video_game_expand_access, video_game_conclude_trial, video_game_rules_revision, video_game_field_validation, video_game_red_team, video_game_officer_league, video_game_national_league, video_game_protect_shifts, video_game_preparedness_clubs, video_game_foreign_licenses, video_game_separate_policy, video_game_begin_reality_audit, video_game_narrow_reality_audit, video_game_dual_track, video_game_restrict_use, video_game_trust_model | Raw bases and modifiers: controlled exercise 1, route 3.0/0.7/1.2, supply 0.4; logistics 2, supply 2.0, peace 0.3, route 1.4/1.1/0.9; expand access 1, peace 2.0, supply 0.25, route 1.1/1.4/0.8; conclude low-value 4.0, peace 1.8, war 0.4, route 1.4/1.1/0.8; rules revision 1, route 1.3/0.8/3.0, war 2.0, supply 0.25; field validation 2.5, supply 0, low stability 0.5, mismatch/failure 3.0, route 1.5/1.0/1.3; red team 2.0, democracy 2.0, war 2.0, route 1.2/0.8/1.3; officer league 1, route 1.1/0.8/3.0, war 2.0, supply 0.15; national league 1, war 2.5, low war support 2.0, supply 0.35, route 0.9/1.4/0.8; protect shifts 1, war 3.0, workplace distraction 2.0, route 0.8/1.3/0.9; preparedness 1, democracy 2.0, war 1.6, route 1.0/1.2/0.8; foreign licensing 2.0, war 0.2, route 0.8/1.5/0.9; separate policy 2, democracy 2.0, supply 2.0, route 0.9/1.3/0.8; begin and narrow audit each 3.5, supply 2.0, low stability 0.5, route 1.2/0.8/1.0; dual track 2, stability 1.8, red team 1.5, supply 0.5, route 1.1/0.8/1.4; restrict 4.0, severe crisis 2.0, peace 0.1, route 1.1/1.0/0.9; trust model 1.5, severe crisis 0, low stability 0, disqualified 0, war 1.5, route 0.9/0.8/1.4. | Decision source pools all 18 definitions. The adapter intentionally reports AI willingness scores and ranks, not normalized click probabilities. Host, active phase, mission, cost, supply, train/fuel stock, foreign target, route and custom trigger inputs are incomplete. No D1-D5 score/rank output or L24 duration/availability comparison returned. |

Other conditional event-option pools are also present. Events chaosx.nr24.13, .21, and .41 each have one base-1 option; .20 has three base-1 route-gated options; .31 and .32 have three base-1 result-gated options each; and .33 and .34 have two base-1 result-gated options each. Their local definitions are source-complete, but the adapter did not confirm mutually exclusive route and result receipts.

The Officer League route also calls video_game_in_sweden_assign_rulebook_commander in common\scripted_effects\024_video_game_in_sweden_effects.txt. It selects a random eligible field marshal with units, or a general with units if no eligible field marshal exists. This is random target selection, not a direct random percentage or weighted event-option pool. The live eligible commander catalog is not complete in the declared fixtures, so frequency and the specification’s “rare” expectation remain unresolved.

The scoped source search found no direct random chance block or Event24-specific AI strategy file. The event weight surfaces in this handoff are ai_chance, decision ai_will_do, the native random_list, and the ticket-replicated host pool. Literal base weights remain in event files, including base 2.0 in .11/.12 and repeated base 1.0 in conditional report/incident options. Centralize these literal anchors if they are intended as tunable weights; no numerical change is recommended or applied.

The decision bases and modifier traces above match the 18-row inventory in handoff 19 and the prepatch decision source hash 8b19fcb187ff40bcfd66c49ff54ec18b009d5724cc6d74ec5bc416af463b6eef. The current supplemental decision diff has no changed ai_will_do blocks. This is a source-diff observation only; it is not an MCP score comparison.

## Timing source and L24 native duration questions

No mean_time_to_happen block or mtth: entry exists in the Event24 events, decisions, effects, triggers, runtime effects, or constants reviewed. Evolution timing is driven by 120/150/120-day counters checked by a 30-day maintenance event. The accepted E1A/E1B, E2A/E2B, and E3A/E3B timing expectations therefore have no returned timing distribution, percentile, daily hazard, or sensitivity result. The accepted faster/slower campaign distinctions remain a source-to-spec timing gap from handoff 19.

L24 changes the Native decision durations as follows: foreign licensing changes from the 5-day foreign_response_delay_days value to the 30-day foreign_license_burden_days value, while the 5-day constant remains the foreign reply dispatch delay; Dual Track changes from the 120-day dual_track_days value to 30-day dual_track_burden_days; National League changes from a fixed 45-day removal duration to a caller-initialized 45-day variable that increases by the 60-minus-45-day difference on removal and clamps at a new 90-day maximum. These are source-defined timer inputs, not MCP-observed availability transitions.

The live v3.6.0 probability_compare schema lists before and after source selectors, candidatePool, scenarioSet, outputs and custom-pool manifests. It does not expose a multi-source source overlay list. The decision_inspect schema accepts point-in-time actor/date/controls/state/flags/eventTargets/scopes and proposedSources, but no scheduled state-transition or decision timer schedule. I did not put a guessed timer path or an artificial native schedule into the probability fixture.

## MCP call receipts

The connected probability tools/list request succeeded on hoi4-agent-tools 3.6.0 with protocol 2024-11-05. Its live top-level schemas described probability source selectors with snapshotPath and expectedSourceHash, plus scenarioSet and candidatePool. The direct model callable for probability_inspect returned the exact error: MCP tool hoi4_agent_tools/hoi4.probability_inspect is not available to the model.

| Call | Narrow request | Exact result |
| --- | --- | --- |
| probability_inspect first probe | event_option_ai_chance, complete .2 option IDs, with the physical snapshot supplied directly as source.path | MCP id 2 returned no result after 55 seconds. No source validation, artifact, or analysis ID. |
| probability_inspect corrected retry | event_option_ai_chance, logical events/024_hearts_of_iron.txt path, snapshotPath, expectedSourceHash and complete .2 pool | MCP id 2 returned no result after 55 seconds after initialization succeeded. No candidate trace, poolComplete, source revision, scenario hash, or artifact URI. |
| probability_compare .2 detailed attempt | P24-O1 through O4, complete three-option pool, declared host/ROOT/PREV/context assumptions | MCP id 1 returned no result after 55 seconds. No tool response. |
| probability_compare .2 narrow retry | P24-O1 through O4, complete three-option pool, immutable pre_remaining_routes event source versus original AFTER event source | MCP id 2 returned no result after 55 seconds after initialization succeeded. No comparison ID, source revisions, scenario hash, ranking, poolComplete, or artifact URI. |
| probability_compare .40 | P24-F1 through F5 and complete five-option .40 pool, immutable event BEFORE versus original AFTER | MCP id 2 returned no result after 45 seconds after initialization succeeded. No comparison result or identifiers. |
| probability_compare .50 | P24-C5/C7 and complete three-option .50 pool, immutable event BEFORE versus original AFTER | MCP id 2 returned no result after 45 seconds after initialization succeeded. No comparison result or identifiers. |
| probability_compare decision AI scores | Full 18-decision candidate pool and P24-D1 through D5 plus C5/C7, immutable BEFORE decision source versus supplemental L24 decision source | MCP id 2 returned no result after 55 seconds. A bounded 45-second retry with the same pool and fixture also returned no result at MCP id 2. No score/rank comparison or timer output. |
| event_inspect first selector probe | trace from chaosx.nr24.1 passed as a string | MCP rejected the request with -32602: Invalid input, expected object, received string at from. No graph. |
| event_inspect corrected trace | selector object for chaosx.nr24.1, downstream, depth 1, 8-node and 8-edge caps | MCP id 2 returned no result after 55 seconds. No graph revision or artifact URI. |
| event_render | options view for chaosx.nr24.2, downstream, depth 1, 12-node cap | MCP id 2 returned no result after 55 seconds. No render URI. |
| reference_context | event surface, limit 2, scoped to Event24 probability rules | MCP id 2 returned no result after 55 seconds. No reference bundle or revision. |
| source_lookup first probe | video_game_in_sweden_is_current_host, scripted_trigger, with refresh supplied | MCP rejected the request with -32602: Unrecognized key refresh. No source result. |
| source_lookup corrected retry | Same symbol, one definition, 20-line bound, references disabled, no refresh field | MCP id 2 returned no result after 55 seconds. No source revision or artifact. |

Every completed bounded-bridge call reported ownedSessionSurvivors: []. No service was restarted. The corrected reference pages were read locally after reference_context failed.

## Findings by audit concern

| Concern | Evidence and disposition |
| --- | --- |
| Score race versus probability | Offline AI modding distinguishes ai_will_do highest-score races from event ai_chance proportional sampling. The installed MCP probability documentation likewise states that decision adapters return scores/ranks without normalized choice probabilities. The Event24 decision outputs therefore remain score-only in kind, and their actual ranks remain unresolved. |
| Event-option probability | The local three/five/three-option pools are identified above. No poolComplete, modifier trace, normalized share, or conditional probability was returned. Exact event-option probabilities are unresolved. |
| Dominance and starvation | No MCP ranking, matrix, threshold, or sensitivity output exists. No candidate is claimed dominant, starved, or free of rank reversal. |
| Impossible or route-incompatible positive weights | Local option triggers and decision availability predicates exist, but dynamic host, event-target, cost, world_end, mission, route, and foreign-target eligibility were not evaluated by the MCP adapter. Candidate validity is unresolved. |
| Evolution timing drift | Fixed 120/150/120-day counters and 30-day maintenance are exact source facts. The campaign-dependent fast/slow ordering required by P24-E1A through P24-E3B is not represented by an MTTH surface in the source evidence. No timing distribution or rank/timing reversal is claimed. |
| Incident validity and repetition | The source sets the seven weights to zero, checks eligibility, then uses random_list. It excludes the prior family while an alternative valid family exists and resets seen-family state if no unseen valid family remains. Source logic is bounded; runtime cadence, eligible subsets and repetition rate remain unresolved. |
| Specific validity gaps | Handoff 19’s source review identified a broad terrain family gate without a specific terrain target/relevant validation effect, and a diplomatic family gate based on diplomacy_active without a live-target check. These remain source-level audit risks, not MCP-confirmed exploitable outcomes. |
| Foreign recipient integrity | The current .40 event trigger validates a host target and a live non-capitulated, non-war foreign-partner target, but does not prove in that trigger that the event recipient is the stored foreign_partner. Handoff 20 already identified this scope risk. No receiver/target scenario or probability result resolved it. |
| Host selection | The adjusted-ticket caller output storage is now initialized, but the original-tag SWE candidate population and external adjusted-ticket/active-load factors are not complete in the snapshot pair. No normalized host-selection probability is claimed. |
| Repetition, snowball and exploit risk | No probability sequence is applicable to the native random_list without the complete custom-pool manifest required by the adapter. Source-level cadence and cooldowns are visible, but repetition frequency, cumulative burden, and snowball magnitude are unresolved. |
| Restriction route source | The current source has three timed departmental receipts at 20/40/60 proof days, closes the program after restriction, and applies the existing 90-day backlash modifier without granting Validated Wargaming Methods. Current source structure matches the owner patch description; no native mission/timer execution was observed. |

The 14 current source-model cases are not native HOI4 execution or probability evidence. They do not establish the actual AI choice distribution, native decision timers, field-unit supply, callbacks, save persistence, or UI rendering.

## Concrete follow-up recommendations, not applied

1. After the HOI4 probability route responds, repeat probability_inspect first, then evaluate and sweep the accepted named cases and compare the immutable pre_remaining_routes sources to the correct captured AFTER snapshots. Use P24-O1 through O4, P24-F1 through F5, P24-C5/C7, and the full 18-decision pool under P24-D1 through D5 plus C5/C7. Do not mark exact probability or balance accepted without adapter artifacts, scenario hashes, complete pool evidence, and complete required inputs.

2. Keep the per-source comparison boundary explicit. The pre_remaining_routes and all AFTER folders do not freeze the referenced shared helper source for the individual_crisis ticket/load system or chaosx_test_country receipt API. The existing related source identities in handoff 20 are evidence for their bounded source repairs, not a historical multi-source probability baseline. The live probability compare schema exposed single before/after selectors and no source-overlay collection. Do not simulate a historical helper overlay by inventing unsupported schema fields.

3. For P24-O1 through O4, complete and bind the original-tag SWE host pool, current host actor, Stockholm owner/controller, event target and active-capacity facts. The source paths are common\scripted_effects\024_video_game_in_sweden_effects.txt, video_game_in_sweden_add_current_country_to_prefire_pool, video_game_in_sweden_select_stockholm_controller_host, video_game_in_sweden_select_stockholm_owner_host, and the shared individual_crisis_targeting_effects.txt / individual_crisis_targeting_triggers.txt. If the full candidate country set is unavailable, keep host-selection shares unresolved.

4. For P24-F1 through F5 and video_game_foreign_licenses, supply a complete target catalog and recipient/host/opinion scope. Reconcile the .40 receiver to its saved foreign_partner and cover valid route, blockade, convoy access, autonomy and overlord permission in common\scripted_triggers\024_video_game_in_sweden_triggers.txt, events\024_hearts_of_iron.txt, and common\decisions\024_video_game_in_sweden_decisions.txt before claiming partner validity.

5. For P24-E1A through E3B, reconcile the accepted campaign-dependent pacing ordering with the source’s fixed evolution_i/evolution_ii/evolution_iii day anchors in common\scripted_effects\024_video_game_in_sweden_effects.txt and common\script_constants\024_video_game_in_sweden_constants.txt. The auditor supplies no replacement day count, MTTH, factor, or balance target.

6. For P24-I1 through I5, evaluate the seven-family random_list only with current family-validity receipts, cooldown day, host and route state. Keep the workplace and party response traces separate. Bind a living target for diplomatic-category-error scenarios. Do not use sequence analysis unless the source is deliberately represented as a complete custom pool with every required transition and timer.

7. For P24-D1 through D5, compare all 18 candidates with the D scenario fixture and declare actual cost, phase, target, and host facts. D1 must separate the current train stock from the four-train module cost. D2 must distinguish a mismatch incident from the exact flags currently read by AI. D4 must bind usable convoy route, blockade, partner and autonomy. D5 must bind review age, reliance and mission state. Compare the L24 30/45-to-90-day decision timing only through a verified native decision lifecycle route; the probability score adapter did not return, and its score outputs cannot serve as timer evidence.

## References and schema evidence

The MCP stdio bridge file docs\plans\024_video_game_in_sweden_plans\tests\mcp_readonly_session.py was read in full before use. It permits reference, source, event, and probability calls but not decision_inspect. The connected server initialization reported hoi4-agent-tools 3.6.0 and protocol 2024-11-05. Client capabilities were empty, so no native task negotiation or job route was used.

The connected probability tools/list result exposed probability_inspect and probability_compare. Their live top-level schemas describe source selectors with snapshotPath and expectedSourceHash, a complete scenarioSet and candidatePool. The installed v3.6.0 probability documentation explains the selector fields and the decision-score versus event-option/random_list adapters. The connected decision_inspect schema exposes point-in-time state but no scheduled transition field. The connected event_inspect and event_render schemas require an object selector, confirmed from docs\events.md after the first string-selector probe was rejected.

probability_evaluate and probability_sweep were not submitted after both corrected probability_inspect calls timed out without required-input paths or a candidate trace. probability_render was not called because no analysis ID or scenario hash existed. probability_simulate was not justified because the accepted fixtures declare no input distribution or seed. probability_sequence was not applicable to the native random_list and lacks the required complete custom-pool transition manifest. Reference search/read were not called after the bounded reference_context request timed out; their pertinent sections were read directly from the offline wiki and installed local documentation as AGENTS.md permits.

The probability_compare D1-D5 request used the full 18-decision AI-score pool against the supplemental L24 source, but returned no result. It did not compare native decision timers. The probability decision adapter returns willingness scores/ranks, and the connected decision_inspect schema has no scheduled transition field. decision_inspect was listed by the live server but was outside the read-only bridge allowlist and had no direct callable binding in this session. The 30/45/60/90-day decision availability changes therefore remain an explicit native-timing blocker. P24-C6, the stable high-Chaos Evolution III scenario, was not in the specifically requested C5/C7 comparison and also remains unresolved.

| Local reference | Relevant span | SHA-256 or revision |
| --- | --- | --- |
| paradox_wiki\AI modding - Hearts of Iron 4 Wiki.md | 26-57, MTTH score race versus event-option ai_chance | 917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818 |
| paradox_wiki\Event modding - Hearts of Iron 4 Wiki.md | 120-176, MTTH timing and event-option pool/trigger semantics | 96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d |
| paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md | 359-385, ai_will_do is a score block | 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162 |
| paradox_wiki\Effects - Hearts of Iron 4 Wiki.md | 4518-4560, random_list proportional weights | 997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c |
| paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md | 535-547, random army leaders; 891-909, random_list | 18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49 |
| paradox_wiki\On actions - Hearts of Iron 4 Wiki.md | 257-260 and 450-461, annex and state-control ROOT/FROM scope contracts | 6822adc85a374a1c1364f2def6f32c6d66da9fb0280319ddd6af4b84b33d882a |
| paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md | 437-442, temporary variable lifetime at scripted helper boundaries | 62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4 |
| paradox_wiki\Localisation - Hearts of Iron 4 Wiki.md | 729-791, temporary variables in scripted-localisation text triggers | 1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064 |
| Installed common\decisions\_documentation.md | Full file, decision gate evaluation cadence | 5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019 |
| Installed documentation\effects_documentation.md | 5413-5441, native random_list | 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af |
| Installed documentation\triggers_documentation.md | 3193-3201 and 5033-5040, army experience and war-support readers | 7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29 |
| Installed documentation\dynamic_variables_documentation.md | 431-443, political power, stability, war support numeric readers | 538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda |
| Installed events\AAT_Generic_Events.txt | 42-49, event ai_chance precedent | e718d19edba2d56c75a5bbf1fa0c51bbb6cda54e0919434c4490fec9dabcea69 |
| Installed common\decisions\_generic_decisions.txt | 56-63, decision ai_will_do precedent | 83cd276f8fd2c0c90470225c996d7afee7b8c08437289dd23d819a4a29edb187 |
| Installed events\AAT_Sweden.txt | 1760-1767, Sweden random_list precedent | 8fad5c10d147afab27eb42c78f3261c804cd6149f1c81927418ab0bbe3b8bf29 |
| Installed hoi4-agent-tools\docs\probability.md | Version 3.6.0 adapter distinctions, source selectors and rendering contract | a392933e376396fe135e25711f513fe3b0f5f09d03847455c1a95948fed030c8 |
| Installed schemas\probability-inspect-input.schema.json | Source selector and candidate-pool fields | b1f9095809b881a49251cc0b9f96a7c8a43c1af77855e14e57d697a67c4a8825 |
| Installed schemas\probability-compare-input.schema.json | Before/after source selectors and scenarioSet | b5ff6669a1867220e0ddcef0f92c508486aa27e0f15dfac884fa7c5df75cf1cc |
| Installed schemas\probability-scenario-set.schema.json | Version 1.0 scenario, actor, state, scope, candidate and schedule fields | 2ab6cc512ed9d3c0ebeebcf469be96010654fff1c18647f121e8a8a8532c8962 |
| Installed schemas\decision-inspect-input.schema.json | Point-in-time decision scenario and proposedSources fields | e617eb0387d2449701af41636125399259abd605dfc48586642e05746461c60b |
| Installed hoi4-agent-tools\docs\events.md | Event selector object forms and bounded inspect/render workflow | 8e06d594fb46d0a8718ce6596fb2e8372c06a8731b481626eecf3eeebf8e5b36 |

## Completion disposition

Completed: required files and skills read; original 18-source AFTER copy frozen and hash-verified; post_localisation_reservations and its D fixture, post_localisation_reservations_followup, post_l24_private_output_followup, post_l24_mission_callback_followup, and post_l24_event_text_followup preserved as distinct source identities; raw current source pools, decision scores, timer constants, and parent patch deltas reviewed; local wiki, vanilla documentation, vanilla precedents, official probability docs and relevant schemas read; narrow probability_compare attempts made for .2, .40, .50 and the full decision pool; event inspect/render attempts made; 14 current source-test methods counted but not run.

Blocked: the probability_inspect, probability_compare, event_inspect, event_render, reference_context, and corrected source_lookup calls either returned the exact errors recorded above or timed out without an artifact. probability_evaluate, probability_sweep and probability_render were skipped for the reasons above; decision_inspect was not callable through the bounded read-only bridge. No source revision, scenario hash, poolComplete flag, rank, normalized probability, timing distribution, comparison ID, event graph revision, rendered URI, or native cooldown transition was produced.

Remaining uncertainty: all AI dominance, starvation, rank reversal, event-choice shares, weighted incident shares, foreign-response shares, host-selection shares, repeated incident frequency, campaign timing distribution and D1-D5 native timer/availability comparisons remain unresolved. Static source values are score evidence only, and decision ai_will_do values are not click probabilities. No numerical acceptance may be inferred from the earlier helper bindings or source-model tests.

No gameplay patch, simplification, balance target, or event completion claim is made by this audit. The parent can resume only with the preserved original and supplemental snapshots and the exact MCP blockers above; do not overwrite either snapshot to make a comparison appear complete.
