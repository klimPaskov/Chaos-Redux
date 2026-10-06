# Event 024 probability audit handoff — 2026-10-06

Disposition: **unresolved overall; partial scenario evidence only.** The probability tools returned usable conditional results for several event-option pools, but the opening evaluation timed out, the incident-list inspector and main comparison timed out, the decision adapter exposed only 4 of 23 ai_will_do candidates, and the pacing adapter found no weighted timing surface. No campaign-level balance acceptance is supported. The owner-applied no-repeat incident change is source-visible in a frozen final weighted snapshot, but its required before/after MCP comparison did not finish.

This audit made no gameplay, weight, trigger, localisation, asset, or runtime edits and no commits. It wrote this handoff and retained frozen source snapshots in the allowed evidence directory.

## Scope and source identity

Audited or attempted:

- events/024_hearts_of_iron.txt — event-option pools .2, .11, .12, .38, and .40.
- common/decisions/024_video_game_in_sweden_decisions.txt — 23 declared decision ai_will_do surfaces.
- common/scripted_effects/024_video_game_in_sweden_effects.txt — incident firing, opening/main random lists, pace accumulation, cadence, cooldown, seen-family flags, and state transitions.
- common/scripted_triggers/024_video_game_in_sweden_triggers.txt — AI caution, option eligibility, decision availability, and mission guards.
- common/mtth/024_video_game_in_sweden_mtth.txt — three pace-rate entries used by the monthly evolution-progress effect.
- common/script_constants/024_video_game_in_sweden_constants.txt — AI factors, incident weights, fire/skip weights, cooldowns, and MTTH pace tuning.

Frozen sources in docs/plans/024_video_game_in_sweden_plans/20261006_probability/:

| Purpose | File | SHA-256 |
|---|---|---|
| Real pre-G2 working-tree effects baseline used for the attempted compare | current_024_video_game_in_sweden_effects.txt | 3f0f91908d7b33f9f01d885f95f60f44a5a1aab8f9270b2541f6dd2e96902a95 |
| Git HEAD effects retained separately | HEAD_024_video_game_in_sweden_effects.txt | e2ad72fb103ccd2d03dcd39ce9827786278402063be160dc25c5898dba040736 |
| Parent-confirmed final weighted-pool effects snapshot after G2 | after_final_024_video_game_in_sweden_effects.txt | 715b572e4302f49a55a4232f07702372b836d670edbf4dcacb31dbda239c042d |
| Exact event source used for .11, .12, .30, .38, and .40 evaluations | events_after_current_20261006.txt | 0f0f127d8b4f1ecd7d418ee5160a717b39866c0ed2352e3ef32c52882f246189 |
| Exact decision source used by the decision evaluator | decisions_current_20261006.txt | d854c1affee958fb66068866056a71760dbd423f1a795fa7d1f985024b84dc6d |
| Pre-G4 mission-guard trigger snapshot | before_mission_guard_024_video_game_in_sweden_triggers.txt | b03af211dd99198654460a7b508bcf174c1999cb310890d76b58e9bcb3292ddd |

The pre-G2 working-tree copy is the real frozen source from immediately before the owner patch, not an invented or reconstructed baseline. Git HEAD is separate because the working tree already contained a nonweighted feedback tail. The parent later made presentation/report, queued-report, stale-answer, and equivalent foreign-helper refactor changes and confirmed no AI factor, MTTH value, incident weight, or weighted-pool definition changed after 715b.... These later changes were not independently compared. The trigger file hash after G4 is d878d47ff11ac33cfc478414c7539ab168442345520dc3cda0cfd65c7bb764dc; G4 adds four active-mission flags to video_game_in_sweden_no_active_mission, affecting eligibility but not ai_will_do values.

Read the Event 024 probability scenario matrix and spec part 3, plus agent_decisions_2026-10-04.md decisions D23, R2-8, R3-8, and R4-5. D23 sets expected orderings, not numeric probability targets. R2-8/R3-8 add peacetime incident entries, the avoids-Reliance-gain helper, .38, and the third incident responses. R4-5 records that R4-1 through R4-4 changed no weighted surface.

Offline and installed references read after targeted searches:

- Offline wiki AI modding, MTTH/scoring lines 26–37, revision 917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818.
- Offline wiki Event modding, ai_chance lines 151–179 and event MTTH lines 117–150, revision 96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d.
- Offline wiki Decision modding, AI lines 357–374, revision 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162.
- Offline wiki Data structures, MTTH variables lines 887–913, revision 62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4.
- Offline wiki Effects, random_list lines 4504–4571, revision 997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c.
- Installed effects_documentation.md, random_list lines 5413–5432, revision 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af.
- Installed triggers_documentation.md, has_country_flag lines 3624–3639, has_stability lines 4800–4808, and has_war lines 5024–5032, revision 7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29.

Decision ai_will_do values are raw competing scores, not click probabilities. Event ai_chance is conditional proportional selection only when the whole pool and source constructs resolve. random_list weights are proportional for each draw among currently valid candidates. The three MTTH-file entries feed monthly progress accumulation, not a native event MTTH distribution. Event-option shares say nothing about how often the event or incident queues. The adapter targets HOI4 1.19.2.0 (d245), marked workspace-verified. Results are offline scenario models, not observed campaign behavior.

## Required probability inspection and adapter results

1. The first audit call was probability_inspect, adapter event_option_ai_chance, source events/024_hearts_of_iron.txt, refresh:false. It found 73 options across multiple pools, poolComplete:false, MULTIPLE_CATEGORICAL_POOLS, and 20 required inputs. This was discovery only, not a complete .2 pool; the live event later changed in nonweighted presentation. Artifact URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/97d3f222ab69efa2310df35bb08faa6e5796690722f1a6cb890ccb64decb7d62/83ddb2a6c5956e245792421492c60cbf82c829c6cc73cfd6ae3d186d91e57be9/probability-inspect-7f6ef66bc532.json; source hash 7f6ef66bc532dd55ca4699177d308d76cf4d66acfc571f59c5a142100757dd2e; source revision 5bcf6d2253dd41f2c0abb96fbc5de7836636c6245cf89b5fda7371625fd69eac.

2. probability_inspect, adapter random_list, source common/scripted_effects/024_video_game_in_sweden_effects.txt, without refresh, timed out after 600 seconds. It returned no artifact, source revision, pool completeness, or candidate trace. No retry was made.

3. probability_inspect, adapter decision_ai_will_do, source common/decisions/024_video_game_in_sweden_decisions.txt, discovered only video_game_conclude_trial, video_game_dual_track_independent_plans, video_game_dual_track_resolve_differences, and video_game_independent_adjudicators out of 23 definitions; candidateCount 4, poolComplete false. Artifact URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c0ed0a329d4c9196e5871f8bd1b465c7477f6dd47a27e4b11fd4b621d2711195/ec13eadec95e4dab7dd8c505c0bfd14c82699fe900df577672b33e6b9e36b0bb/probability-inspect-26122f4e02de.json; source hash 26122f4e02de3c343ec7b8e6e8135c07e77b693916db0859d99af7f16017d274; source revision ba5624a2c68a5b1ffc54f599e3827ab629036724e6a33f82bd9e7f6888982149. This catalog cannot complete P24-D1–D5 or P24-C5–C7.

4. probability_inspect, adapter event_mean_time_to_happen, source common/mtth/024_video_game_in_sweden_mtth.txt, returned PROBABILITY_SOURCE_DISCOVERED with no_weighted_surfaces, zero candidates, and no blockers. Artifact URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5b559c1fca0b78d5ea72d7f4238760de10a842d3f71745a7a064e0dfdadd3ffa/d90ace73ae65180cb5386ea7671c452c5bfef37909fc4f1af7ebd5762d99ca4f/probability-inspect-f0b6fd8d94f0.json; source hash f0b6fd8d94f098c63278162657909e0a57ca0ac1eeae39eb72f723e7edf95be7; source revision 633d5fff22fa94763078d299acc37e6ef15d76e5ad0f64fdfc6a3a90901ffec4.

## Named scenario results

| Scenario | Pool and declared state | Result |
|---|---|---|
| P24-O1 calm democratic peace | .2.a/.b/.c; democratic or neutral, peace, high stability, adequate experience, no shortage, Calm World | Unresolved; evaluate timed out after 600 seconds with no artifact, scenario hash, or ranking. |
| P24-O2 calm democratic rearmament | .2.a/.b/.c; democratic peace, high tension, low experience, good industry/supply | Unresolved for the same timeout. |
| P24-O3 militarized Sweden at war | .2.a/.b/.c; authoritarian, war, low experience, good supply/fuel/trains, Gathering Storm+ | Unresolved for the same timeout. |
| P24-O4 emergency defense | .2.a/.b/.c; war, recent core loss, poor supply/fuel, low stability | Unresolved for the same timeout. |
| P24-E1A/E1B, E2A/E2B, E3A/E3B | Six pace scenarios specified in the matrix | Unresolved. The MTTH adapter found no weighted timing surface, so no median or timing distribution is claimed. |
| P24-C1 stable democracy | Complete .11.a/.b/.c pool | Exact conditional model: red-team .11.c raw 4.8, rank 1, 24/49 (48.98%); auxiliary .11.a raw 3.9, rank 2, 39/98 (39.80%); competitive .11.b raw 1.1, rank 3, 11/98 (11.22%). The expected top pair leads. |
| P24-C2 militarized wartime Sweden | Complete .11.a/.b/.c pool, recent mismatch | Exact conditional model: competitive .11.b raw 36, rank 1, 48/65 (73.85%); auxiliary .11.a raw 10.8, rank 2, 72/325 (22.15%); red-team .11.c raw 1.95, rank 3, 4/100 (4%). Red-team remains eligible after the mismatch. |
| P24-C3 Evolution II, strong industry/high tension | Complete .12.a/.b/.c pool | Exact conditional model: exhibitions .12.a raw 6.72, rank 1, 168/377 (44.56%); preparedness .12.c raw 5.76, rank 2, 144/377 (38.20%); protect .12.b raw 2.6, rank 3, 5/29 (17.24%). The two expected leading paths are close. |
| P24-C4 Evolution II, factory/stability crisis | Complete .12.a/.b/.c pool | Exact conditional model: protect .12.b raw 31.2, rank 1, 3900/4987 (78.20%); preparedness .12.c raw 8.64, rank 2, 1080/4987 (21.66%); exhibitions .12.a raw 0.056, rank 3, 7/4987 (0.14%). The adapter flags starvation/d100-quantization risk for .12.a. The decision “keep the craze outside government” is not a candidate in this event-option pool. |
| P24-C5/C6/C7 and P24-D1/D2/D3/D4/D5 | Decision score races across the 23 declared actions | Unresolved. Although 23 IDs were declared, inspect discovered four candidates only; evaluation scenarios also omitted video_game_in_sweden_host and video_game_in_sweden_host_selected. Output: 0 eligible, 32 excluded and 48 unresolved rows across eight scenarios. No score rank is valid. |
| P24-F1/F2/F3/F4 | Complete five-option .40.a/.b/.c/.e/.ridicule pool; host bound to SWE | Partial/unresolved. Copy/Study/Ban/Ridicule are unsupported due scope.meta_trigger; .40.a also has unresolved is_in_faction_with and .40.b has unresolved has_war. Only Ignore .40.e has supported raw score 0.8/rank 1. No shares or full ranks are valid. Mismatch, communist-ban and other modifiers were inactive in the inputs. |
| P24-F5 invalid/exhausted pool | No valid live partner or no remaining response | Not an option-choice case: .40 is not queued for an invalid/exhausted target, so .40 option shares do not apply. No numeric choice claim was made. |

The .2 evaluation used candidate pool chaosx.nr24.2.a/.b/.c and P24-O1 through P24-O4, timed out after 600 seconds, and returned no artifact. Initial discovery was multi-pool, so the complete .2 candidate pool was not confirmed.

The .11 evaluation artifact is probability-c66624fb332659728b51cf01, scenario hash 0ffd614d7edf990d9671e90effb82992a061bd4c65018fae8354474188913341, source revision ecf2c601175eaef50efa1f3556e5c5d1596a25b99c69c13a9803aa06790bd3dc, pool hash fa3f9ac2d2fd95679612ddc4d064fff8f7514f28a9d1d57a6196e47793ffa584. Its exact JSON resource URI was not retained in the available result transcript.

The .12 evaluation artifact is probability-b6e97ba13731d6ea6914b665, scenario hash 01f8e4bcc1d75c1a07997619ac4915c32ecad74d0e75f55bec0ac4c015d4618b, source revision ecf2c601175eaef50efa1f3556e5c5d1596a25b99c69c13a9803aa06790bd3dc, pool hash d7c2bed67ac996e3de6106c4d41829b050dbc441d0d945305fa734fb6728b9d6. Its exact JSON resource URI was not retained in the available result transcript.

The .40 evaluation used event snapshot SHA 0f0f..., complete pool hash a70c9859562fa762f28ceb8e54012081be4ae9ca7b24fb98b0c74b2314827098, analysis probability-fae2af0a9c46c9ac53f7b1af, scenario hash a45b9b27edb164f503c12956882d113c29002725868783843278e11d6ab25b72, source revision 55cc337b2c6f2404c461d2b6bf11a846db9430aa213e07edc6e141f4e72b6d88, and source hash 0f0f127d8b4f1ecd7d418ee5160a717b39866c0ed2352e3ef32c52882f246189. JSON URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c4bb12938dcc7e30dbe570e24f463ad88ede56aa471f3ad7514ef0a7bbe5a458/905a3af2b4094b4db12d4c5cf5e5e55d5c3b42c18a678797ff37e0613d603ee/probability-fae2af0a9c46c9ac53f7b1af.json.

The .11 and .12 explicit render calls returned PROBABILITY_ANALYSIS_STALE and zero visual resources after workspace revisions changed. Their evaluate responses generated views, but their individual ranking/matrix/waterfall/unresolved URIs are not preserved here.

## Decision guard and score races

The decision evaluation used frozen source SHA d854c1affee958fb66068866056a71760dbd423f1a795fa7d1f985024b84dc6d, 23 declared decision IDs and eight scenarios for C5/C6/C7 and D1–D5. Analysis ID probability-c70badf7992ceacee8d61911; scenario hash fa6642c9dc284fde2feff3550212be6b141909d5b884457fbed216573802fb0a; source revision bfade00a22b6dbdf736e6b400b819bcc2fba119a0d0bcf887b85a02ed25d2983; MCP source hash 03545adab5330363de1d1d198af1dccfe2975402f9d29b377bebe0b26516e0fa. It produced four discovered candidates across eight scenarios, 0 eligible, 32 excluded, 48 unresolved. Host and host-selected event targets were not bound. Together with incomplete inspection, the results prove no D/C5–C7 score ordering.

The owner’s G4 patch closes a same-day gate gap where has_active_mission could remain false before native mission activation. This is an eligibility issue, not a numeric score change. The pre-G4 trigger snapshot hash and current trigger hash are listed above. The decision adapter cannot attribute this guard-only change because it lacks a complete candidate race and no valid host-bound scenario was evaluated. Do not treat the source change as probability evidence.

## .38 event and stability sensitivity

The .38.a/.b/.c pool was complete in each of four cases on exact event snapshot SHA 0f0f.... Analysis probability-56852e2246fac69e022a8e0c; scenario hash f1b90bb0c9108a038c9bc4d50bb6e4bca4f9024c43a2c094a28eee788c0cca0c; source revision b2c49b79bdaae60ae6f618b437aa6e6823270cc08305b11ce651558e31f2fa19; MCP source hash a5c312b7b2d53172344fa8437a077d0bfbbbd58ab0cec9bec211b268dddaf970; pool hash 884bfa3e27d3ea7c1c71cd89286a984cb00a378a4d1cd75aafa3d61451efaf. JSON URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/795db16926acd013fed512905f362ad8fd7f23a3743bafb0d109bed4aa1fdfca/ca8755d0cb586d5338d14f239e67bdec59851a4150ec4045b532a2abd57f6adb/probability-56852e2246fac69e022a8e0c.json.

| Scenario | Resolved and unresolved rows |
|---|---|
| P24-38-DEM-PEACE | .38.a raw 3/rank 1/share 30/49 (61.22%); .38.c raw 1.3/rank 2/share 13/49 (26.53%); .38.b raw 0.6/rank 3/share 6/49 (12.24%), unresolved. Overall shares/ranks partial. |
| P24-38-FASCIST-WAR | .38.b raw 5.4/rank 1/share 27/38 (71.05%), unresolved; .38.a raw 1.2/rank 2/share 3/19 (15.79%); .38.c raw 1/rank 3/share 5/38 (13.16%). Overall shares/ranks partial. |
| P24-38-HIGH-TENSION | .38.a raw 3/rank 1/share 15/26 (57.69%); .38.c raw 1.3/rank 2/share 1/4; .38.b raw 0.9/rank 3/share 9/52 (17.31%), unresolved. Overall shares/ranks partial. |
| P24-38-LOW-STABILITY | .38.a raw 3/rank 1/share 20/37 (54.05%); .38.c raw 1.95/rank 2/share 13/37 (35.14%); .38.b raw 0.6/rank 3/share 4/37 (10.81%), unresolved. Overall shares/ranks partial. |

Every .38.b trace through video_game_in_sweden_ai_avoids_reliance_gain remains unresolved because the analyzer cannot resolve set_temp_variable, subtract_from_temp_variable, simulation_reliance, or video_game_in_sweden_ai_threshold_floor. It also reports the threshold-caution factor inactive in all four cases. Do not present .38.b shares or ranks as validated.

The stability sweep varied has_stability from 0.2 to 0.8 at nine deterministic points, with no input distribution. Analysis probability-366c9da1766030535faa1cea; scenario hash df517cf93ef9de8905f6b8dcaabd4a18b47f2e854ac4115128da41566315475b; same source revision and pool hash as .38 evaluation. The supported .38.a score stayed 3, .38.c varied 1.3–1.95, and the tool reported no rank reversal between those two supported rows. .38.b remained unresolved, so this is not a full-pool sensitivity finding. Explicit render returned PROBABILITY_ANALYSIS_STALE for analysis revision b2c49... versus current workspace revision a788a59362b1d5d934ea3ae0fc7f1291f4ede6545e6d0e686de99a5367295a25, with no visual resources. Evaluate/sweep responses had generated sensitivity/unresolved views, but individual render URIs are not preserved here.

## .30 third responses

The .30 evaluation used a full 27-option pool, complete within each of seven family-specific cases on exact event snapshot SHA 0f0f.... Cases covered counterplan with officer competition and no/with field evidence; bootleg on the commercial route at peace/war; and party appropriation under democratic/fascist/communist governments. Analysis probability-505cd8ca58c72c6626a6d199; scenario hash e76d9d0be615ea2575217595313392cf7f0cc365affd808e06e6db8374d2a156; source revision 8af3d8507a9b5de5a08bd4bd8ae13aaf3dc8518be5a360fd4b65371f644cf84d; source hash a5c312b7b2d53172344fa8437a077d0bfbbbd58ab0cec9bec211b268dddaf970; pool hash 485ceaa5028fdafb209f30e4ff31308cded61b3768559ce370dbb1e0298860be. Main JSON URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ccf62ef91d1d126eee19bd642268ecaf102d65ce8fb8d205408222e7ef819bbb/7ef36e95405f1e4eec26d9c2a56a734421a758a74b63598d607c83/probability-505cd8ca58c72c6626a6d199.json. The artifact summary reports 189 projections, 20 eligible rows, 3 unresolved, and complete local pools.

| Case | Result |
|---|---|
| Counterplan, officer, no field evidence | .30.counterplan_a raw 1.5/rank 1 and .30.counterplan_c raw 1.5/rank 2 each report 3/8; .30.counterplan_b raw 1/rank 3 reports 1/4. counterplan_c uses the unresolved threshold helper, so no full-pool share/rank conclusion is exact. |
| Counterplan, officer, field evidence | .30.counterplan_a raw 1.5/rank 1, 15/34; .30.counterplan_b raw 1/rank 2, 5/17; .30.counterplan_c raw 0.9/rank 3, 9/34, but counterplan_c remains unresolved. |
| Bootleg, commercial, peace | .30.bootleg_c raw 1.5/rank 1, 3/7; .30.bootleg_a and .30.bootleg_b raw 1 each, 2/7 each. Exact conditional result for supported pool. |
| Bootleg, commercial, war | .30.bootleg_a raw 1.5/rank 1, 15/31; .30.bootleg_b raw 1/rank 2, 10/31; .30.bootleg_c raw 0.6/rank 3, 6/31. Exact conditional result for supported pool. |
| Party appropriation, democratic | .30.party_a raw 1.7/rank 1, 17/31; .30.party_b raw 1/rank 2, 10/31; .30.party_c raw 0.4/rank 3, 4/31. Exact conditional result for supported pool. |
| Party appropriation, fascist | .30.party_c raw 2/rank 1, 1/2; .30.party_a and .30.party_b raw 1 each, 1/4 each. Exact conditional result for supported pool. |
| Party appropriation, communist | .30.party_c raw 2/rank 1, 1/2; .30.party_a and .30.party_b raw 1 each, 1/4 each. Exact conditional result for supported pool. |

counterplan_c is unresolved through video_game_in_sweden_ai_avoids_reliance_gain: unsupported scoped set_temp_variable and subtract_from_temp_variable, plus missing simulation_reliance and video_game_in_sweden_ai_threshold_floor. The analyzer warns EVENT_OPTION_FALLBACK_NOT_PROVEN because every option is gated and no unconditional fallback is proven. It marks 24 candidates from other incident families never eligible across these cases; those rows are family-gated here, not evidence of global dead options.

The narrow .30 JSON was read through the exposed artifact template, but its response exceeded available inline output; ranged follow-up could not be completed because the copied URI components were rejected as invalid. The exact main JSON URI is preserved above. The evaluation response generated ranking/matrix/waterfall/unresolved links, but individual render URIs are not recoverable from the available transcript. No new evaluate or render call was made.

## Incident selection and no-repeat patch comparison

The incident system has a fire/skip random list, Evolution III opening pool, and main pool of terrain, supply, enemy, template, diplomatic, workplace, party, casualties, counterplan, bootleg, production, and offensive. Valid-family predicates, ready-day cooldown, rare counterplan/bootleg cooldown, crisis pause, and last_incident also affect cadence. Constants include terrain 100, supply 200 (supply-table variant 75), enemy 100, template 100, diplomatic 100, workplace 100, party 100, casualties 100, counterplan 50, bootleg 50, production 100, and offensive 100. Modifiers include validation, peace/war, route, protected-work shifts, and other state factors. Fire has base 60 and min/max 10/100 with tier, doctrine, red-team, and validation factors. These are source weights only; no family frequency is inferred.

Before G2, video_game_in_sweden_roll_incident reset all seen-family flags when no currently valid unseen family remained, allowing an exhausted baseline program to cycle through counterplan/bootleg again. The owner removed that invocation and the unused reset helper, leaving weights unchanged and seen flags persistent until program cleanup. A later source review found the separate Evolution III opening pool also lacked seen-family gates. Final snapshot 715b... adds per-family zeroing and calls its random_list only when total weight is positive, preserving relative weights.

Required matching compare: frozen pre-G2 working-tree SHA 3f0f... against final weighted snapshot SHA 715b...; main selector before line 3344/after line 3353; all 12 family candidates; P24-I5-BASELINE-INSTRUMENT-EXHAUSTED and P24-I5-WORLDVIEW-UNSEEN. This exact compare timed out after 600 seconds with no comparison id, artifact, scenario hash, or trace. A prior path-only compare returned PROBABILITY_SURFACE_EMPTY because the file contains multiple random lists. Opening-pool compare, before line 1893/after line 1917, four candidates and matching Evolution III seen/unseen cases, returned PROBABILITY_SURFACE_EMPTY with filesScanned empty. No retry was made.

The source review finds the original repeat-reset defect and owner patch addresses both pools; the required selection-eligibility comparison remains unresolved. This handoff does not call the once-only property probability-validated or infer incident frequency from static weights.

## Event structural evidence

event_inspect on .30 with narrow trace, no helpers, max depth 2 timed out after 600 seconds with no artifact.

event_render for .30 returned EVENT_RENDERED_PARTIAL, graph revision ce8d42d8302c354d2085f12075b14162a185dd5d77a9ea393f90dc6c04558379, selected the .30 root and 27 options, but scanned 401 source files, 10,374 events, and 2,285 diagnostics. The manifest reports unresolved edges for video_game_in_sweden_adjust_incident_reliance (27) and video_game_in_sweden_record_rules_revision (1), though both helpers exist in the local effects source. Treat this as incomplete MCP structural coverage, not proof those helpers are missing.

Manifest URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/66d762d3f64853aecb014f932ed93e96f6559a73967eaee3237e1160f4a9bcf2/ceec1df82d808d1f648c4cb095bd69a3485c8992bba6bb23870d909e7a8de552/event-options-ce8d42d8302c-manifest.json. It links the JSON/SVG/PNG event views.

## Remaining blockers and recommendations

1. Keep overall weighted acceptance unresolved and catalog status Needs Testing. C1–C4 are exact conditional event-option results only; they do not complete D23/R2-8/R3-8.
2. Resolve the .2 timeout and inspect its complete option pool with all source conditions before evaluating P24-O1–O4. Compare only against a real frozen source.
3. Extend analyzer support for Event 024 progress accumulation/monthly cadence before making claims about P24-E1A/B, E2A/B, or E3A/B. Do not convert pace multipliers to medians by hand.
4. Fix decision candidate discovery, bind host and host-selected event targets, and declare mission flags, ideology, resources, war/capitulation, route, and external state for P24-C5–C7 and P24-D1–D5. The scores remain score-only until a full competing set resolves.
5. Resolve scope.meta_trigger, is_in_faction_with, and has_war in .40 before evaluating P24-F1–F4 again. Ignore’s 0.8 raw score is not a global or winning probability.
6. Make random_list inspection traverse nested scripted helpers and every dynamic validity gate. Then declare the complete fire/skip/opening/main pool, cadence, cooldowns, phase unlocks, terminal cleanup and state flags; compare the frozen pre-G2 source to 715b... for P24-I5-BASELINE-INSTRUMENT-EXHAUSTED and P24-I5-WORLDVIEW-UNSEEN. Existing relative weights need no retuning based on present evidence.
7. Resolve or model video_game_in_sweden_ai_avoids_reliance_gain so .38.b and .30.counterplan_c can be scored from simulation_reliance and the threshold floor. Do not say the 0.1 caution fired in these scenarios.
8. Broader sensitivity across Reliance thresholds, Chaos boundaries, stability, supply/trains/fuel/convoys, experience, ideology, war/peace/capitulation, and enabled/disabled evolutions remains outstanding. Only .38 received a stability sweep. No simulation was run because no uncertainty distribution or seed was declared.
9. F5 no-target cleanup, foreign response caps, .41 summary acknowledgement, and visible report limits are availability/presentation/state-flow surfaces. This pass does not establish their runtime behavior. The owner says the foreign max-one summary cap is presentation-only and does not require a probability comparison.

Skipped/incomplete analyses: no probability retry loops; no probability_sequence because complete dynamic pool/cadence/state transitions could not be declared; no probability_simulate because uncertain distributions and seed were absent; no full incident or decision sweeps; no new render/evaluation after the parent froze weighted sources. No game, desktop window, runtime log, or live campaign was used.


Skills applied: chaos-redux-subagents, chaos-redux-events, chaos-redux-mtth, and chaos-redux-event-planning.
