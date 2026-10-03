# Event 24 Remaining Routes Probability Baseline

Audit date: 2026-10-03.

Workspace: C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux.

Status: immutable pre-route source baseline captured and verified. The installed MCP server and probability schemas were confirmed, but no probability or event-graph analysis returned an artifact. Rankings, conditional probabilities, normalized pools, timing distributions, and engine-validity conclusions remain unresolved. This handoff is not balance signoff.

## Ownership, acceptance, and scope

The user explicitly accepted the complete Event 24 package under docs\specs\024_video_game_in_sweden_specs. The source package and plans 13, 14, 15, 16, and 18 were read before this audit. The accepted scenario IDs are retained below without adding new IDs.

The user's 2026-09-20 correction retires Field-Validated Planner and any conversion to that trait. The Rulebook Commander trait is the only Event 24 commander trait in scope. The vanilla SWE_wargames picture for the experimental Swedish spirit is an explicit owner choice.

This is a read-only probability baseline. No gameplay, AI, event, decision, effect, trigger, constants, ideas, dynamic modifier, localisation, asset, workbook, skill, or runtime source was edited. No commit was made, and Hearts of Iron IV was not launched.

The analyzed and queued scenario sets are opening choices P24-O1 through P24-O4, evolution pacing P24-E1A through P24-E3B, event choice pools .11, .12, and .50 using applicable P24-C1 through P24-C7 scenarios, the seven current incident families under P24-I1 through P24-I5, the full eighteen-decision category under P24-D1 through P24-D5 and applicable crisis cases, and the five foreign responses under P24-F1 through P24-F5 as added by the parent's comparison instruction.

The accepted future Casualties as Counters opening and National Final are not present in the current seven-family incident selector. They were not inserted into this baseline.

## Immutable pre-route snapshots

The directory docs\plans\024_video_game_in_sweden_plans\probability_snapshots\2026-10-03_pre_remaining_routes did not exist at capture. Fourteen physical byte copies were created once with File.Copy under mirrored source paths. SHA-256 values were compared against the live files after capture and again during the final drift check. The copies are not reparse points, and no read-only attribute was set on live files. The folder has not been recopied or overwritten.

| Source path | Bytes | Frozen SHA-256 |
| --- | ---: | --- |
| common\decisions\024_video_game_in_sweden_decisions.txt | 38,572 | 8b19fcb187ff40bcfd66c49ff54ec18b009d5724cc6d74ec5bc416af463b6eef |
| common\decisions\categories\024_video_game_in_sweden_categories.txt | 945 | 12778be8725534f1872a568f137f079f2f7f69e3f8d775e2c89653991ddac68b |
| common\dynamic_modifiers\024_video_game_in_sweden_dynamic_modifiers.txt | 2,763 | 5cf4c7bf7ec5fe053a77a4ac3a69ac3db141ccc38abd87c03501ce9971971fc8 |
| common\ideas\024_hearts_of_iron_ideas.txt | 3,981 | b4e3517a79d27c0347a94be4c2a88d1dd32553e5f911208d56c2391f532bdd0d |
| common\ideas\024_video_game_in_sweden_cxt_ideas.txt | 563 | 8db195e24487f97fbdcc8429c8c5c80672e17eb957fbeca1d9ff75e3e1b00e29 |
| common\on_actions\024_video_game_in_sweden_cxt_on_actions.txt | 1,108 | fda4e7869525bb22c3956bc5d6015b59dbac10f82ab80b402cce68bcd1028d64 |
| common\scripted_effects\024_video_game_in_sweden_cxt_effects.txt | 1,858 | 84e2d9f1143504fb308720047d33c7e669cbecbe6e2cd29309a372855095469d |
| common\scripted_effects\024_video_game_in_sweden_effects.txt | 122,845 | 36b7a83af58de302240c561cc95fb45892b856e0b302a9c2afcd74b874ef499c |
| common\scripted_localisation\024_video_game_in_sweden.txt | 13,835 | 8d1d97965bbcdd572503950684bb8677d10bb65a124146bbbb20011e616a92ad |
| common\scripted_triggers\024_video_game_in_sweden_triggers.txt | 31,247 | 81c4b0839b9e3c22c03e268a8f91cc4039cbbab0596d5f629c2ab6682b622b9f |
| common\script_constants\024_video_game_in_sweden_constants.txt | 14,363 | 5ee57066f537ce917910cbe6c678622cf61b9e99a5018fd123c56b74f4a907f5 |
| events\024_hearts_of_iron.txt | 34,317 | 75e81ff4f8889a30957f23bc67a473f617fc4238b8dda07eca0a6edb8693798c |
| localisation\english\024_hearts_of_iron_l_english.yml | 43,354 | a0b3442db8fc1a6c84215a39bbb6ceb396e7990f599464c04a331fc670ed548c |
| localisation\english\024_video_game_in_sweden_requirement_flags_l_english.yml | 2,693 | bc445ba7a9363fda1c4f69d1b8b6105d73bff7326f849615ef94339878460ba2 |

The frozen event, effect, trigger, decision, and constants source paths are the weighted analysis inputs. The ideas, category, dynamic modifier, scripted localisation, on-action, and localisation files are retained as named dependency and identity cross-checks.

## Post-capture source drift

At the final hash check, the event, main effects, triggers, constants, and CXT on-action files differed from the immutable snapshot. The user reports that the owner patch initializes prefire-pool adjusted_weight and active_load inputs, changes current-host validation to use PREV when called from foreign scope, and initializes the daily CXT registration receipt. The user reports that no AI weights changed. I did not inspect the patch diff or recopy the frozen files.

| Source | Frozen baseline SHA-256 | Current live SHA-256 at final check |
| --- | --- | --- |
| common\on_actions\024_video_game_in_sweden_cxt_on_actions.txt | fda4e7869525bb22c3956bc5d6015b59dbac10f82ab80b402cce68bcd1028d64 | 9310c9b6fa4cb0edf918db0499f19958bf330d840a38995bdeb86c8ec82761d1 |
| common\scripted_effects\024_video_game_in_sweden_effects.txt | 36b7a83af58de302240c561cc95fb45892b856e0b302a9c2afcd74b874ef499c | 95ec123ba5e2382db5653a28b8c0a71f2f8858d18a7cf19921d6c31ce2609955 |
| common\scripted_triggers\024_video_game_in_sweden_triggers.txt | 81c4b0839b9e3c22c03e268a8f91cc4039cbbab0596d5f629c2ab6682b622b9f | d030792f946030bd262c4a3ec873bde1b2febf431f0b41595c68782c2b2ad39c |
| common\script_constants\024_video_game_in_sweden_constants.txt | 5ee57066f537ce917910cbe6c678622cf61b9e99a5018fd123c56b74f4a907f5 | a498c1c0458a69b9e377efeb0a4e3d4c94828185db48797e520e1dc1e6159c19 |
| events\024_hearts_of_iron.txt | 75e81ff4f8889a30957f23bc67a473f617fc4238b8dda07eca0a6edb8693798c | 859cad1c74ee1dd4b92e6a3f416402eb181d9744cf9137dc27e475cf245aae87 |

The frozen quote helper is another cross-file dependency for the .50 restriction option and video_game_restrict_use. In the snapshot, video_game_in_sweden_pay_restriction preinitializes its three debited quote outputs before the nested if.limit call in effects lines 751-764. The scripted-localisation cost triggers initialize the quote value each text.trigger consumes in scripted_localisation lines 332-372. The helper video_game_in_sweden_quote_restriction writes temporary outputs and ends with always = yes in triggers lines 145-173. The parent reports additional caller-output initialization edits after this capture, including the if.limit and text.trigger boundaries. I did not apply those changes. Any P21 result for .50.c or Restrict Use must retain the before/after helper provenance and must not assume values created only inside a returning helper survive the call.

The other nine snapshot/live pairs still matched at that check. The parent-reported patch is after this baseline and must be compared against these frozen copies in handoff 21. The current hashes above are not immutable AFTER snapshots.

## Source inventory and raw score evidence

All numeric values in this section are copied source bases, factors, thresholds, or fixed day counters. They are not evaluated scores or probabilities. I did not multiply factors or infer an ordering.

### Opening pool and P24-O1 through P24-O4

The three local candidates in chaosx.nr24.2 are .2.a Controlled Staff Trial, .2.b Civilian Commercial Release, and .2.c Competitive Officer League. Their base values are 4.0, 3.0, and 2.0.

The Controlled option has an at-peace factor of 1.8, a low-stability factor of 0.5, and a severe-crisis factor of 8.0. The Commercial option has a high-stability factor of 1.5, a wartime factor of 0.4, and a severe-crisis factor of 0.0. The Officer option has a wartime factor of 2.0, a low-army-experience factor of 1.4, a supply-crisis-flag factor of 0.25, and a severe-crisis factor of 0.25.

The three definitions form the complete source-level local pool. Runtime host validity, event-target binding, Stockholm ownership, capitulation, world_end, severe-crisis helper resolution, and the complete scenario state were not confirmed by MCP. P24-O2's high world tension and good industry do not appear as direct modifiers in the frozen .2 option blocks. Government type is also not a direct opening modifier.

The bounded opening evaluation request used P24_FINAL_OPENING_MATRIX and the complete three-option pool. Its declared source assumptions were actor SWE, controller SWE for state 141, host-selected and program-active flags, and video_game_in_sweden_host mapped to SWE. It used has_war, has_stability, and has_army_experience values of false/0.65/40 for O1, false/0.65/10 for O2, true/0.55/10 for O3, and true/0.15/10 for O4. It also supplied has_fuel 500 for O3 and 0 for O4. O3 carried an Officer-route flag even though O3 concerns the pre-route opening. That flag is not read by the frozen .2 ai_chance blocks, but it is an unvalidated and unnecessary scenario assumption and must not be treated as accepted fact or silently reused. The request used no tool-confirmed ownership binding for Stockholm. No scenario hash was returned.

The bounded opening sweep kept the same scenario IDs and candidate pool. It declared has_stability ranges 0.5-1 for O1 and O2, 0-1 for O3, and 0-0.2 for O4, with 21 steps and rank-reversal detection enabled. These are declared sensitivity ranges around the source thresholds, not accepted campaign observations. The sweep returned no result or scenario hash.

### Evolution timing P24-E1A through P24-E3B

No mean_time_to_happen or mtth: entry exists in the frozen Event24 event, effect, trigger, or decision files. The pacing surface is deterministic day-counter gating inside video_game_in_sweden_maintenance, called by hidden event chaosx.nr24.90. The maintenance event is rescheduled every 30 days. It adds 30 to program_days and, during an active evolution, 30 to evolution_elapsed_days. The timing constants are evolution_i_delay_days = 120, evolution_ii_delay_days = 150, and evolution_iii_delay_days = 120.

The frozen source gates Evolution I at Chaos 200 and either Reliance at least 25 or the Officer route, completed Officer League, or high-Chaos Officer opening. Evolution II gates at Chaos 400 and Reliance at least 50. From baseline it also requires broad_public_reach and the 150-day program counter. From Evolution I it uses the 150-day evolution counter. Evolution III gates from Evolution II at Chaos 600, Reliance at least 75, and the 120-day evolution counter.

The six accepted timing scenarios are P24-E1A, P24-E1B, P24-E2A, P24-E2B, P24-E3A, and P24-E3B. Their campaign factors include war, world tension, route, Reliance, prediction history, league seasons, field validation, red team, protected shifts, and policy separation. The frozen eligibility code uses some of these as gates or flags, but contains no campaign-dependent timing modifiers or MTTH. Its fixed day anchors do not distinguish the expected fast and slow counterparts once their gates are satisfied. This is exact source inventory and a bounded source-level specification mismatch, not an engine timing result.

### Evolution option pools and applicable P24-C scenarios

For P24-C1 and P24-C2, event chaosx.nr24.11 has three options, each with base 2. Option .11.a adds the war factor 1.8 and route factors 1.3/0.8/3.0 for Controlled/Commercial/Officer. Option .11.b adds the low-army-experience factor 2.0 and route factors 1.1/0.8/3.0. Option .11.c adds the Democratic-government factor 2.0 and route factors 1.2/0.8/1.3.

For P24-C3 and P24-C4, event chaosx.nr24.12 has three options, each with base 2. Option .12.a adds a stability-above-0.50 factor 1.6, a severe-crisis factor 0.10, and route factors 0.9/1.4/0.8. Option .12.b adds a wartime factor 2.0, a severe-crisis factor 3.0, and route factors 0.8/1.3/0.9. Option .12.c adds a broad-public-reach factor 1.6, a severe-crisis factor 1.5, and route factors 1.0/1.2/0.8.

For P24-C5, P24-C6, and P24-C7, event chaosx.nr24.50 has three options. Reality Audit has base 3.5, supply-crisis-flag factor 2.0, and route factors 1.2/0.8/1.0. Dual-Track has base 2.0, stability-above-0.50 factor 1.6, and route factors 1.1/0.8/1.4. Restriction has base 4.0 and route factors 1.1/1.0/0.9.

The source definition pools are complete at three options each. The .11 and .12 pools are only applicable to C1/C2 and C3/C4. The .50 event itself requires Trust the Model or mandatory reassessment state, so that trigger state must be declared alongside each C5/C6/C7 case. All three .50 options have native source gates. Host scope, event targets, resources, flags, affordability, country state ownership, and helper output lifetime remain unconfirmed. P24-C5 must distinguish a historical supply_crisis flag from a current supply gap because current supply and field-package requirements affect Reality Audit availability. P24-C7 uses surrender progress 0.9 as an audit assumption in prior handoffs, while the source maximum-risk cutoff is 0.75.

### Incident selector and P24-I1 through P24-I5

The complete source-level native random_list in video_game_in_sweden_roll_incident has seven entries: terrain 2.0, supply 3.0, enemy 2.0, template 2.0, diplomatic 2.0, workplace 2.0, and party 2.0. These are weight-variable identifiers video_game_in_sweden_incident_terrain_weight, _supply_weight, _enemy_weight, _template_weight, _diplomatic_weight, _workplace_weight, and _party_weight. Their values are set to zero before eligibility checks and receive the constants only if their scripted validity and recent-family checks pass.

Selection requires program_days at least incident_ready_day, no incident pause crisis, and current_incident exactly zero. The source uses a 45-day normal incident cooldown and a 20-day Trust the Model cooldown. The maintenance pulse runs every 30 days. Family-seen state is reset when no currently valid unseen family remains. The last family is excluded when a different valid family is available, and can repeat if no alternative is valid. This is a native random_list with dynamic eligibility, not a declared custom weighted sequence manifest.

Terrain is currently valid during any war or while Field Validation or Reality Audit is active, if the family has not been seen. The source gate does not require a named mountain or forest target and does not directly lower its weight after relevant validation. Supply requires the current war-plus-train/truck/fuel supply-gap trigger and is invalid after the mismatch is removed or reduced. Enemy requires war and an unseen, non-reduced family. Template requires broad public reach and Evolution II or III. Diplomatic requires only the diplomacy_active flag and an unseen family, without a live-target validity check. Workplace requires broad public reach in Evolution II. Party appropriation requires public_response_available, broad_public_reach, and Evolution II.

The response event chaosx.nr24.30 contains the full 14-option source pool, with two responses per family. Every option base is 1. Conditional factors are supply_b 0.25 during supply crisis, enemy_a 2.0 with red team, enemy_b 0.2 during supply crisis, template_a 1.8 under separate policy, template_b 0.25 during supply crisis, workplace_a 1.8 when shifts are protected, workplace_b 0.2 at war, party_a 1.7 under democracy, and party_b 0.2 during supply crisis. The other five response options have no conditional factor in the frozen source.

P24-I1 uses incident 1 for a conditional terrain response. P24-I2 uses incident 2 for supply. P24-I3 requires separate response traces for current_incident 6 workplace and current_incident 7 party. P24-I4 uses incident 5 and needs an active diplomacy target. P24-I5 is a before-draw selector state with current_incident 0 and an explicit prior-supply-family assumption last_incident 2, retained from handoff 13. The source candidate catalog has seven entries, but no scenario has MCP-confirmed eligibility or external-factor completeness. Runtime cooldown cadence, recent-family state, validation receipts, war, public reach, diplomacy targets, and host state remain unresolved. No repetition frequency is measured.

### Decision pool and P24-D1 through P24-D5

The source category contains all 18 requested decision definitions. Their raw ai_will_do base and source modifier traces are:

| Decision | Raw base | Named modifier traces |
| --- | ---: | --- |
| video_game_controlled_exercise | 1 | Controlled-route 3.0, Commercial-route 0.7, Officer-route 1.2, supply-gap 0.4 |
| video_game_logistics_module | 2 | Supply-gap 2.0, peace 0.3, route 1.4/1.1/0.9 |
| video_game_expand_access | 1 | Peace 2.0, supply-gap 0.25, route 1.1/1.4/0.8 |
| video_game_conclude_trial | conclude_low_value 4.0 | Peace 1.8, war 0.4, route 1.4/1.1/0.8 |
| video_game_rules_revision | 1 | Route 1.3/0.8/3.0, war 2.0, supply-gap 0.25 |
| video_game_field_validation | validation_caution 2.5 | Supply-gap 0.0, low stability 0.5, reality-check-disqualified or validation-failed 3.0, route 1.5/1.0/1.3 |
| video_game_red_team | red_team_caution 2.0 | Democracy 2.0, war 2.0, route 1.2/0.8/1.3 |
| video_game_officer_league | 1 | Route 1.1/0.8/3.0, war 2.0, supply-gap 0.15 |
| video_game_national_league | 1 | War 2.5, war-support-below-0.45 2.0, supply-gap 0.35, route 0.9/1.4/0.8 |
| video_game_protect_shifts | 1 | War 3.0, workplace distraction 2.0, route 0.8/1.3/0.9 |
| video_game_preparedness_clubs | 1 | Democracy 2.0, war 1.6, route 1.0/1.2/0.8 |
| video_game_foreign_licenses | foreign_interest 2.0 | War 0.2, route 0.8/1.5/0.9 |
| video_game_separate_policy | 2 | Democracy 2.0, supply-gap 2.0, route 0.9/1.3/0.8 |
| video_game_begin_reality_audit | audit_crisis 3.5 | Supply-gap 2.0, low stability 0.5, route 1.2/0.8/1.0 |
| video_game_narrow_reality_audit | audit_crisis 3.5 | Supply-gap 2.0, low stability 0.5, route 1.2/0.8/1.0 |
| video_game_dual_track | 2 | Stability above 0.50: 1.8, red team 1.5, supply-gap 0.5, route 1.1/0.8/1.4 |
| video_game_restrict_use | restrict_crisis 4.0 | Severe crisis 2.0, peace 0.1, route 1.1/1.0/0.9 |
| video_game_trust_model | trust_safe 1.5 | Severe crisis 0.0, stability below 0.35: 0.0, reality-check-disqualified 0.0, war 1.5, route 0.9/0.8/1.4 |

The bases and factors are score evidence only. Decision ai_will_do values are willingness scores in a candidate race and are not click probabilities. All 18 definitions exist at source level. The live available category pool, active host, phase flags, affordability, target validity, foreign partners, current stocks, and external AI plans were not returned by MCP.

P24-D1 must separate a historical supply crisis from present train stock because the Logistics Module costs four trains while the supply-gap trigger uses fewer than three trains in war. P24-D2 must distinguish a mismatch incident from the two explicit AI factor flags, reality_check_disqualified and field_validation_failed. P24-D3 must declare war support and workplace distraction. P24-D4 must declare a valid partner, convoy stock, route access, autonomy, and scope. The foreign-licensing availability source checks a valid partner and no current supply gap, but source review found no explicit blockade or usable-convoy-route trigger. P24-D5 must declare review age, Reliance, peace, and mission state. The crisis cases must declare restriction affordability and active reassessment state.

### Foreign response pool and P24-F1 through P24-F5

The foreign response event chaosx.nr24.40 has a complete five-option source pool: .40.a Copy, .40.b Study, .40.c Ban, .40.ridicule Ridicule, and .40.e Ignore. Raw bases are Copy 1.0, Study 1.0, Ban 0.8, Ridicule 1.0, and Ignore 0.8.

Copy factors are friendly opinion 2.5 above 50, low Army Experience 1.8 below 25, hostile opinion 0.35 below 0, and Swedish reality-check disqualification 0.4. Study factors are friendly opinion 1.3 above 50, hostile opinion 2.5 below 0, low Army Experience 1.5 below 25, and major status 2.0. Ban factors are Fascist government 2.2, hostile opinion 1.8, and Swedish mismatch disqualification 1.5. Ridicule factors are hostile opinion 1.4, low world threat 1.8 below 0.30, mismatch disqualification 2.0, and recent Swedish victory 0.15. Ignore has base 0.8.

P24-F1 through P24-F5 are included for the parent's requested P21 compare. Their expected orderings are in the accepted matrix. Foreign actor identity, Swedish host scope, opinion input path, target validity, major status, foreign war state, ideology, Army Experience, threat, Swedish mismatch and victory flags, response count, and the complete foreign-partner population remain incomplete. P24-F5 concerns an invalid or exhausted target pool, where the response event itself may be ineligible. No exact option share or AI ranking is claimed.

### Commander selection and host prefire selection

The Officer opening calls video_game_in_sweden_assign_rulebook_commander. It first selects a random assigned field marshal with units, if one exists, otherwise it selects a random assigned general with units. There is no explicit random = chance or direct percentage in the frozen source. When the selected tier has at least one eligible leader, the effect assigns the Rulebook Commander trait. The eligible leader catalog and conditional probability of a target are unresolved. This is random target selection, not a weighted event-option pool. It may be inconsistent with the accepted description of a rare trait result. The user's decision forbids conversion to Field-Validated Planner and defines the permitted Rulebook Commander removal after validation.

The prefire host selectors build temporary arrays over living original-tag SWE countries. The frozen helper assigns each candidate a base ticket, calls adjust_individual_crisis_candidate_ticket_weight, repeats the country in the temp array according to the adjusted weight, then calls random_scope_in_array. The Stockholm-controller pool is tried before the Stockholm-owner pool. can_receive_program uses valid-host and individual-crisis-load gates. This weighted host-target pool depends on the complete current original-tag SWE candidate catalog and the shared adjusted-weight helper. No adapter result or complete target catalog exists. Parent-reported changes to adjusted_weight, active_load, and current-host scope are post-baseline and reserved for P21.

## Scenario-by-scenario candidate and external-factor completeness

The rows below name every in-scope accepted scenario. Source-definition pools are listed as complete only at the local file level. MCP poolComplete was not returned for any row. No adapter scenario hash exists.

| Scenario | Surface and source pool | Declared facts and missing inputs |
| --- | --- | --- |
| P24-O1 | chaosx.nr24.2, three opening options | Bridge request assumed SWE, peace, stability 0.65, Army Experience 40, selected host, active program, and controller SWE for state 141. Stockholm ownership, original-tag/valid-host trigger, world_end, and scenario binding remain unproved. |
| P24-O2 | chaosx.nr24.2, three opening options | Bridge request assumed SWE, peace, stability 0.65, and Army Experience 10. High tension and good industry were not supplied as adapter facts. Host ownership and event-target gates remain unproved. |
| P24-O3 | chaosx.nr24.2, three opening options | Bridge request assumed SWE, war, stability 0.55, Army Experience 10, fuel 500, and controller SWE for state 141. It also mistakenly set the Officer-route flag before route choice. That flag was not read by the frozen .2 weights, but the request is not an accepted campaign fixture. Host ownership and event-target gates remain unproved. |
| P24-O4 | chaosx.nr24.2, three opening options | Bridge request assumed SWE, war, stability 0.15, Army Experience 10, fuel 0, supply-crisis and core-loss flags, and controller SWE for state 141. Exact train/truck stocks, owner scope, original tag, and host event target remain unbound. |
| P24-E1A | Fixed evolution-I pacing gate, no MTTH candidate pool | Accepted state is Gathering Storm, Reliance 30, Controlled route, one successful exercise, red team active, and peace. Exact date, program age, Chaos value, route flags, host, and the maintenance polling phase were not evaluated. |
| P24-E1B | Fixed evolution-I pacing gate, no MTTH candidate pool | Accepted state is Gathering Storm, Reliance 45, Officer League, war, and no field validation. Exact program age, Chaos value, active route flags, host, and counter cadence were not evaluated. |
| P24-E2A | Fixed evolution-II pacing gate, no MTTH candidate pool | Accepted state is Rising Chaos, Reliance 55, Commercial route, protected shifts, play separated from policy, and high stability. Broad-public-reach flags, current phase, evolution counter, exact date, and host were not bound. |
| P24-E2B | Fixed evolution-II pacing gate, no MTTH candidate pool | Accepted state is Rising Chaos, Reliance 65, two league seasons, foreign licensing, and high tension. The source flags/counters for seasons, licensing, phase, host, and maintenance schedule were not bound. |
| P24-E3A | Fixed evolution-III pacing gate, no MTTH candidate pool | Accepted state is Chaos Tier, Reliance 78, red team, recent successful field validation, and separate policy. Exact validation receipt, elapsed evolution counter, Chaos value, host, and event flags were not bound. |
| P24-E3B | Fixed evolution-III pacing gate, no MTTH candidate pool | Accepted state is Chaos Tier or Totalen Chaos, Reliance 90, both leagues, no recent validation, and apparent prediction successes. Exact Chaos value, league and prediction flags, elapsed counter, host, and scheduled changes were not bound. |
| P24-C1 | chaosx.nr24.11, three Evolution-I options | Prior handoff assumption is phase 2 and Controlled route, stable democratic Sweden. Exact stability, government binding, host, flags, and availability remain unresolved. |
| P24-C2 | chaosx.nr24.11, three Evolution-I options | Prior handoff assumption is phase 2 and Officer route, militarized Sweden at war with low Army Experience. Supply, exact Army Experience, government binding, host, flags, and availability remain unresolved. |
| P24-C3 | chaosx.nr24.12, three Evolution-II options | Prior handoff assumption is phase 3 and Commercial route with strong industry and high tension. Public reach, stability, phase flags, host, and decision effects remain unresolved. |
| P24-C4 | chaosx.nr24.12, three Evolution-II options | Prior handoff assumption is phase 3 and Commercial route in a factory/stability crisis. The matrix gives no stability point. Crisis thresholds are source constants, but host and current public-reach flags remain unresolved. |
| P24-C5 | chaosx.nr24.50, three reassessment options | Prior handoff assumption is phase 4, Controlled route, current_incident 0, last_incident 2, supply failure, lost core, low fuel/trains, and no mission. Historical supply-crisis flag versus current supply gap, complete stocks, field package, host ownership, and restriction quote helper binding remain unresolved. |
| P24-C6 | chaosx.nr24.50, three reassessment options | Prior handoff assumption is phase 4 and Officer route with high stability, strong supply, offensive war goal, and Totalen Chaos. Trust/reassessment flags, exact stability and supply, host, and active war-goal inputs remain unresolved. |
| P24-C7 | chaosx.nr24.50, three reassessment options | Prior handoff assumption is phase 4, Controlled route, near capitulation, low resources, and surrender progress 0.9. The 0.9 value is an audit assumption. Host, mission state, available project factories, resource binding, and reassessment flags remain unresolved. |
| P24-D1 | Full 18-decision pool | Logistics under train shortage. Current train stock must be separated from historical supply-crisis state because the action costs four trains and the live-gap trigger uses fewer than three trains in war. |
| P24-D2 | Full 18-decision pool | Field validation after mismatch. Exact mismatch flag, supplied divisions, field package, equipment, fuel, trains, host, and current supply remain unresolved. |
| P24-D3 | Full 18-decision pool | National League during total mobilization. War support, workplace distraction, factory output, industry, public reach, and active decision subset remain unresolved. |
| P24-D4 | Full 18-decision pool | Foreign Licensing while blockaded. Convoy stock, usable route, blockade, living partner, autonomy, recipient/host scope, and no-current-supply-gap facts remain unresolved. |
| P24-D5 | Full 18-decision pool | Conclude Trial ignored baseline. The accepted review age, Reliance below 50, peace, experience, no active mission, valid host, and phase flags were not bound. |
| P24-I1 | Seven-family random_list and 14-option .30 response pool | Terrain mismatch. The source requires war or an active field/audit mission, but the accepted terrain type and recent relevant validation state were not bound. |
| P24-I2 | Seven-family random_list and 14-option .30 response pool | Train/fuel shortage. War, train/truck/fuel thresholds, crisis flag, seen/reduced flags, host, and response state were not bound. |
| P24-I3 | Seven-family random_list and 14-option .30 response pool | Evolution II public league. Workplace response current_incident 6 and party response current_incident 7 require separate traces. Public reach, public-response flag, template-family competition, seen flags, and host were not bound. |
| P24-I4 | Seven-family random_list and 14-option .30 response pool | Evolution III active diplomacy. The source diplomacy_active flag is not proof of a living target. Target identity, target scope, route, host, and recent-family state were not bound. |
| P24-I5 | Seven-family random_list before-draw state | Prior family 2 is an explicit audit assumption retained from handoff 13. Current incident 0, other six family-validity states, seen flags, cooldown day, host, and scheduled campaign changes were not bound. |
| P24-F1 | chaosx.nr24.40, five foreign-response options | Friendly Nordic neighbor. Partner actor, Swedish host target, opinion above 50, route/war validity, foreign experience, and complete partner pool were not bound. |
| P24-F2 | chaosx.nr24.40, five foreign-response options | Hostile major intelligence power. Foreign actor, hostile opinion, major status, ideology, Army Experience, war state, target scope, and host flags were not bound. |
| P24-F3 | chaosx.nr24.40, five foreign-response options | Authoritarian unstable state. Foreign actor, Fascist government, domestic stability, hostility, Swedish target, and partner pool were not bound. |
| P24-F4 | chaosx.nr24.40, five foreign-response options | Peacetime complacent rival. Foreign actor, low global threat, recent Swedish victory flag, hostility, partner target, and complete pool were not bound. |
| P24-F5 | chaosx.nr24.40, five foreign-response options when the event is valid | Invalid or exhausted pool. If actor or target validity fails, the response event may not fire at all. The complete partner catalog, duplicate history, response cap, and no-action fallback eligibility were not bound. |

## MCP tools, schemas, and results

The configured local service handshake returned server hoi4-agent-tools version 3.6.0 and protocol 2024-11-05. The client sent no task capability and used only ordinary tools/call routes. The bounded read-only session bridge at docs\plans\024_video_game_in_sweden_plans\tests\mcp_readonly_session.py was read in full before use. Its allowlist permits only read-only HOI4 operations and its owned Windows job cleanup reported no surviving processes after completed bridge calls.

A bridge tools/list request succeeded and returned live schemas for probability_inspect, probability_evaluate, probability_sweep, probability_compare, probability_render, event_inspect, event_render, reference_context, reference_search, reference_read, and source_lookup. The probability schema accepts source selectors with path, snapshotPath, and expectedSourceHash according to installed package files. The official scenario-set schema is version 1.0. The parent reports no native MCP task negotiation. Package adapter documentation targets HOI4 Operation Postern 1.19.2.0 checksum d245 and adapter version hoi4-1.19.2.v1. No probability result confirmed this installation's game build or checksum.

| Attempt | Source and scope | Result |
| --- | --- | --- |
| Native probability_inspect | event_option_ai_chance, frozen events\024_hearts_of_iron.txt, candidatePool .2.a/.2.b/.2.c, refresh true | Tool error: timed out awaiting tools/call after 600s. No source revision, candidate rows, poolComplete, analysis ID, scenario hash, resource URI, or artifact. |
| Bounded bridge probability_inspect, refresh true | Same frozen .2 source and complete three-option pool | TimeoutError: MCP id 2 returned no result after 45s. No result artifact or identifiers. |
| Bounded bridge probability_inspect, refresh false | Same frozen .2 source and complete three-option pool | TimeoutError: MCP id 2 returned no result after 45s. No result artifact or identifiers. |
| Bounded bridge probability_evaluate | P24_FINAL_OPENING_MATRIX, P24-O1 through P24-O4, frozen .2 source and complete three-option pool, raw_value and conditional_probability requested | TimeoutError: MCP id 1 returned no result after 45s. No analysis ID, source revision, scenario hash, candidate traces, unresolved rows, or result URI. |
| Bounded bridge probability_sweep | Same named opening scenarios and complete pool, has_stability swept across declared ranges with 21 steps and rank-reversal detection requested | TimeoutError: MCP id 2 returned no result after 45s. No analysis ID, scenario hash, sensitivity result, or artifact. |
| Bounded bridge event_inspect | Trace from chaosx.nr24.1 downstream, depth 1, 4-node and 6-edge caps, helpers disabled | TimeoutError: MCP id 2 returned no result after 45s. No graph revision or artifact. |
| Bounded bridge event_render | Options view for chaosx.nr24.1 downstream, depth 1 and 4-node cap, helpers disabled | TimeoutError: MCP id 2 returned no result after 45s. No render URI. |
| Bounded bridge reference_context | Event surface, limit 16, question scoped to Event24 weights, random_list, fixed delays, and AI semantics | TimeoutError: MCP id 2 returned no result after 45s. No references or revision bundle. |
| Parent-reported native event_inspect | Refreshed lint for root chaosx.nr24.1, maxNodes 4, maxEdges 4, maxDepth 1, expandHelpers false | Parent reports final error timed out awaiting tools/call after 600s. No artifact or source revision. |
| Parent-reported native reference_search | Narrow game_doc reference search | Still running at the last parent update. It returned no evidence to this handoff. |

The initial five-adapter registry-wrapper batch was terminated when the parent supplied the configured bridge instructions. It produced no inspect result. The later direct native .2 inspect returned the 600-second timeout receipt above. No completed probability artifact has a source revision, scenario hash, analysis ID, comparison ID, or URI. No rendered evidence path or URI exists.

## Results classification and risk findings

| Conclusion | Classification | Evidence |
| --- | --- | --- |
| Frozen source identities and 14-file candidate-source inventory | Exact | Real byte copies, SHA-256 verified against live files at capture, with a later check identifying five post-baseline live-file changes. |
| Raw bases, source factors, source thresholds, fixed day counters, and local candidate definitions | Score-only or exact source inventory | Frozen Event24 source and constants. These are not calculated scores, eligibility proof, or probabilities. |
| Event-option, incident random_list, and foreign-response conditional shares | Unresolved | No probability inspect/evaluate result, poolComplete, source revision, or scenario hash. |
| P24-D1 through P24-D5 decision scores and ordering | Unresolved score race | Raw source bases and modifier traces are known. No MCP eligibility result or decision ranking exists. No click probability is inferred. |
| P24-E1A through P24-E3B timing distributions | Unresolved and no MTTH source present | The frozen code uses fixed day counters and 30-day maintenance pulses. No event_mean_time_to_happen candidate or cumulative timing artifact returned. |
| Positive weights on runtime-ineligible choices | Unresolved | Source-level option triggers and decision availability gates exist, but host, target, affordability, resource, and scope facts were not engine-analyzed. |
| Dominance, starvation, rank reversal, and probability cliffs | Unresolved | No normalized share or ranking output exists. |
| Incident repetition and recovery | Bounded source logic, runtime result unresolved | Exact-zero current-incident sentinel, unseen-family cycle reset, and alternate-family exclusion are visible in source. Cadence, valid-family pool, last-family state, and state transitions were not MCP-confirmed. |
| Unsafe snowball or excessive repetition | Unresolved | No scenario sequence, repeated selection rate, or cumulative prevalence was returned. Sequence analysis is inapplicable because this is a native random_list, not a complete custom-pool manifest. |

The accepted evolution pacing order is not represented by MTTH or source timing factors. Evolution I's accepted E1A/E1B distinction and Evolution II/III fast/slow scenario distinctions are not supported by the frozen pacing code beyond eligibility gates and Reliance/route flags. This is a source-to-accepted-scenario gap. No actual event firing day or timing percentile is claimed.

The opening source does not use every expected O-scenario factor. World tension, industry, and government type are absent from the .2 option score blocks. O3's militarized state does not independently increase an opening weight in the frozen .2 source. This is a source-level coverage finding, not a measured rank reversal.

The current terrain incident gate is broader than the accepted terrain-specific expectation, and the diplomatic family gate checks diplomacy_active without a live foreign-target validity condition. Template incidents remain eligible in Evolution II with broad public reach even in the accepted P24-I3 context. These create bounded candidate-validity and ranking questions. Their dominance or exploit effects are unresolved.

The host-selection arrays use a shared adjusted-ticket helper and a dynamic set of original-tag SWE countries. Host capacity, country ownership, event-target scope, and active-load factors are incomplete in every opening and foreign scenario. The parent reports those scope/capacity repairs are now live after the frozen baseline. No host-selection probability is claimed.

The offline AI-modification reference distinguishes the decision ai_will_do score race from event ai_chance and random_list proportional selection. The installed probability adapter documentation states that decision adapters return scores and ranks without normalized choice probabilities, event-option and random_list shares require complete local pools, direct_random is an independent percentage, and MTTH timing uses a daily hazard with trigger polling. None of those semantics is claimed as an Event24 result because no adapter response returned.

## Recommendations for the owner, not applied

1. Preserve the current snapshot folder. Capture and hash the owner-patched after sources separately before P21. Never recopy pre_remaining_routes.
2. Run handoff 21 with the same accepted P24-O1 through P24-O4 and P24-F1 through P24-F5 IDs, the complete .2 and .40 option pools, and explicit host-capacity, ROOT/PREV, event-target, and foreign-actor bindings. Record missing owner/opinion inputs as unresolved rather than forcing candidates eligible.
3. Compare the host selection and current-host helper changes using confirmed before/after source selectors for effects, triggers, constants, and event definitions. A frozen single event file does not freeze referenced helpers. Use a multi-file comparison only if the live schema confirms it. A zero delta on the event file alone cannot prove the helper patch had no effect.
4. For the prefire host array, declare the complete candidate countries and adjusted-ticket/active-load inputs before requesting any normalized share. If the country catalog cannot be complete, retain an unresolved target-pool result.
5. Implement or explicitly reconcile the accepted campaign-dependent evolution pacing expectations for P24-E1A through P24-E3B in common\scripted_effects\024_video_game_in_sweden_effects.txt, video_game_in_sweden_maintenance, and common\script_constants\024_video_game_in_sweden_constants.txt, video_game_in_sweden_timing.evolution_i_delay_days, evolution_ii_delay_days, and evolution_iii_delay_days. The current anchors are 120/150/120 days and the checks run through 30-day maintenance. The auditor does not select replacement MTTH values or chance factors.
6. Preserve P24-O1 through P24-O4 ordering requirements in events\024_hearts_of_iron.txt, chaosx.nr24.2.a/.2.b/.2.c, and the video_game_in_sweden_ai/video_game_in_sweden_ai_factor groups in common\script_constants\024_video_game_in_sweden_constants.txt. The source currently omits direct world-tension, industry, and government factors. No numeric factor is recommended here.
7. For P24-I4, bind a living diplomacy target in common\scripted_triggers\024_video_game_in_sweden_triggers.txt, video_game_in_sweden_incident_diplomatic_is_valid, or keep the family unresolved. For P24-I1, decide whether terrain or recent relevant validation must affect video_game_in_sweden_incident_terrain_is_valid or its selector weight. Keep the P24-I3 workplace and party response traces separate in events\024_hearts_of_iron.txt, chaosx.nr24.30, and include the template-family competitor.
8. Resolve P24-D1's current train shortage versus the four-train cost through video_game_in_sweden_has_campaign_supply_gap and video_game_logistics_module. Resolve P24-D2's exact mismatch flags in video_game_field_validation. Resolve P24-D4's usable convoy route, blockade, autonomy, partner, and recipient scope through video_game_foreign_licenses and video_game_in_sweden_has_foreign_partner_available before exact category analysis.
9. For P24-F1 through P24-F5, preserve the complete five-option pool in events\024_hearts_of_iron.txt, chaosx.nr24.40, and bind the foreign ROOT, Swedish host event target, opinion threshold, and partner state. Compare the parent-reported PREV scope correction against this frozen event and trigger baseline.
10. The prefire host array in common\scripted_effects\024_video_game_in_sweden_effects.txt, video_game_in_sweden_add_current_country_to_prefire_pool, video_game_in_sweden_select_stockholm_controller_host, and video_game_in_sweden_select_stockholm_owner_host needs a complete Swedish candidate catalog and adjusted-ticket/active-load inputs for any normalized comparison. Keep an incomplete catalog unresolved.
11. The Officer opening calls video_game_in_sweden_assign_rulebook_commander without an explicit chance gate. Keep the eligible commander candidate pool complete for any direct-random or custom-pool analysis. Do not convert the trait to Field-Validated Planner.

## Remaining uncertainty and skipped analyses

No exact candidate-pool completeness flag, modifier trace, ranking matrix, timing curve, sensitivity breakpoint, unresolved view, source revision, scenario hash, or artifact URI was returned. The analyzer did not prove the current foreign partner pool, valid host scope, candidate availability, dynamic random_list weights, or decision category race.

No probability_compare was run because this is the prepatch baseline. No probability_render call was possible without an analysis ID. No probability_simulate was justified because the accepted matrices declare no probability distributions, correlations, or seed. No probability_sequence was run because the source uses a native random_list and there is no complete declared custom-pool manifest. No numeric hand calculation was performed.

The MCP tools were exposed and their live schemas were listed. The exact blocker is that read-only tools/call requests did not return within the bounded bridge window, while the native probability_inspect and parent event_inspect returned or were reported as timing out after 600 seconds. This is a service-response blocker, not an absent-tool-registry claim. Parent-side reference_search had not returned at the last update. Offline wiki and installed documentation fallback sections were read directly.

## Evidence references

Offline wiki sections read directly: AI modding, lines 26-57, SHA-256 917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818; Event modding, lines 120-176, SHA-256 96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d; Decision modding, lines 359-385, SHA-256 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162; Scopes, random_unit_leader and random_list entries, lines 535-547 and 891-909, SHA-256 18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49; Effects, random_list, lines 4518-4560, SHA-256 997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c.

Installed documentation read directly: common\decisions\_documentation.md, lines 1-21, SHA-256 5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019; documentation\effects_documentation.md, random_list lines 5413-5441 and random_unit_leader lines 5604-5617, SHA-256 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af; documentation\triggers_documentation.md, has_army_experience lines 3193-3201, has_equipment lines 3835-3842, has_stability lines 4800-4807, has_war_support lines 5033-5040, and surrender_progress lines 7640-7647, SHA-256 7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29; documentation\dynamic_variables_documentation.md, has_political_power/has_stability/has_war_support lines 431-443 and surrender_progress lines 791-794, SHA-256 538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda.

Installed vanilla source examples read: events\AAT_Generic_Events.txt:42-49 for event-option ai_chance, SHA-256 e718d19edba2d56c75a5bbf1fa0c51bbb6cda54e0919434c4490fec9dabcea69; common\decisions\_generic_decisions.txt:56-63 for decision ai_will_do, SHA-256 83cd276f8fd2c0c90470225c996d7afee7b8c08437289dd23d819a4a29edb187; events\AAT_Sweden.txt:1760-1767 for a Sweden random_list, SHA-256 8fad5c10d147afab27eb42c78f3261c804cd6149f1c81927418ab0bbe3b8bf29; events\Yugoslavia.txt:49-51 for a vanilla MTTH example, SHA-256 138279b294ef0d567e477efe2f0ebb72c5c0a7f2920ed3fd03d2792749624dbc; events\BFTB_Bulgaria.txt:514-521 for random_unit_leader selection, SHA-256 d2740d3716de01b81aef29c95527d974dedebfac3a1571695955815115387d88.

Installed MCP package reference read: C:\Users\klimp\AppData\Roaming\npm\node_modules\hoi4-agent-tools\docs\probability.md, SHA-256 a392933e376396fe135e25711f513fe3b0f5f09d03847455c1a95948fed030c8; docs\events.md, SHA-256 8e06d594fb46d0a8718ce6596fb2e8372c06a8731b481626eecf3eeebf8e5b36; research\probability-adapter-evidence.md, SHA-256 6099e1f4bca4eddd136752e35fa00f3cb35c5dfcf416d81d2395088400e8282f; schemas\probability-scenario-set.schema.json, SHA-256 2ab6cc512ed9d3c0ebeebcf469be96010654fff1c18647f121e8a8a8532c8962. These local package files document schemaVersion 1.0, snapshotPath plus expectedSourceHash, and the adapter distinction between event-option shares, raw decision scores, random_list shares, independent direct random percentages, and MTTH timing.

Skills read in full: chaos-redux-subagents, chaos-redux-events, chaos-redux-mtth, and chaos-redux-decisions-missions. No skill was created or updated.

Handoff disposition: baseline incomplete for numerical probability, ranking, timing, and sensitivity. Immutable source evidence is ready for owner-patched P21. The follow-up comparison must reuse P24-O1 through P24-O4, P24-E1A through P24-E3B, P24-C1 through P24-C7, P24-D1 through P24-D5, P24-I1 through P24-I5, and P24-F1 through P24-F5 on applicable surfaces, with complete local candidate pools and declared host-capacity conditions. The only completed edits by this auditor are the fourteen physical snapshot copies and this Markdown handoff. No gameplay, localisation, asset, workbook, or skill edit was made, and no commit was made.
