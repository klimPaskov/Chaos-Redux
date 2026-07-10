# Event 011 Secret Alliance decision and mission re-audit

## Verdict

The Event 011 decision, mission, reveal, scenario, settlement, aftermath, achievement, AI, and cleanup implementation at commit `b7965b7e3743b43c643f0a3ef10c2d57ad723665` was clean in its audited scope. DM-01 through DM-14 and RA-01 through RA-02 remain resolved. This is a historical scoped freeze. Final gameplay authority is `407b9a05`, balance remains frozen at `1c87d923`, and the holistic verdict is maintained in `completion_audit.md`.

This was a report-only audit. The auditor did not edit gameplay, localisation, interface, AI, event, scenario, achievement, asset, or spreadsheet files.

## Audited freeze

The evidence below was taken from exact HEAD `b7965b7e3743b43c643f0a3ef10c2d57ad723665` with no working-tree change on the audited files.

| File | SHA-256 |
| --- | --- |
| `common/decisions/011_secret_alliance_decisions.txt` | `772868373EBCD13C51A34BAB3E187CBE4DA91345B0024509171BA7097BAAA2FF` |
| `common/scripted_triggers/011_secret_alliance_triggers.txt` | `92B5F615CA0E13A3086D2B1AA518FF38D747E435CEFBC43DD187FF4022C7443B` |
| `common/scripted_effects/011_secret_alliance_effects.txt` | `94AD1483D080E3E35E68D1431C2C2E48725E26A73945F9811BA75CA756F9F184` |
| `events/011_secret_alliance.txt` | `BF1580C6721C58D6AB94FA3D9968A964B717D8E0336C81708CC6E1C473698CA6` |
| `common/on_actions/011_secret_alliance_on_actions.txt` | `EF6E86688F64128750B7F86E67A5DA6642806D8D5D0D3DD13C5A6E47DC1497EE` |
| `common/scripted_guis/011_secret_alliance_scripted_gui.txt` | `C715868C26CF43EE937E89EF327562F0724BEAB63714F7A74B82C5E14166989F` |
| `common/scripted_localisation/011_secret_alliance_scripted_localisation.txt` | `34D1ABAB4FEB30B83942BC949BC6EDB7D19414EC7D1246EA42CE587726347339` |
| `common/ai_strategy/011_secret_alliance.txt` | `E8BB9188D862A43AD37C886CFCE2C517DEC421368D45C78405D01F275C067898` |
| `common/script_constants/011_secret_alliance_constants.txt` | `800F893F858EC75679A546AFCEF6A32D1D3906E7607664E08FE4C9063854E9A6` |
| `common/achievements/chaos_redux_achievements.txt` | `5EB5788E910458092B516C76057D996618AD6E3817B0AE6273ED0675BD519A72` |
| `common/ideas/011_secret_alliance_ideas.txt` | `EFF8F98B876D0455BC52D1AFBE1E196D41436D8DAA237245F7902488AFFA8104` |
| `common/factions/goals/011_secret_alliance_goals.txt` | `0B642E95557FBCBA43556995FF5533AE9F6F1BA23C4BF64461CB1934B350AD2E` |
| `common/factions/rules/011_secret_alliance_rules.txt` | `616FF72B9CA4ECD7047AA01BE5F5F1B04096AE6D0A83AA36A874BDED72C20DE8` |
| `common/factions/rules/groups/011_secret_alliance_rule_groups.txt` | `94BB6F61C6B7D0FA6E03B400A4B405846294A151102D729A2DEAA526EE9F1BF9` |
| `common/factions/templates/011_secret_alliance.txt` | `302C3EE29D851B07981FA7EF30371151A687AE13F2AB520031A0BBA4F72D30ED` |
| `localisation/english/011_secret_alliance_l_english.yml` | `44E05B87D68E83A4B503EBF4BCB10ADFED73763F8B4CF94C2457F558F2DFCA99` |

## References used

The audit used the accepted Event 011 specs, especially the decision/mission matrix, AI matrix, achievement matrix, event-chain map, tuning model, spec parts 1 through 5, and the accepted improvement-loop resolution.

Required offline Paradox wiki references were consulted for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Faction modding, Interface modding, and Scripted GUI modding. Vanilla documentation was consulted for decisions, scripted GUIs, factions, on actions, AI strategy, triggers, effects, modifiers, script concepts, dynamic variables, localisation formatters/objects, and script constants. The exact-state and border-war structure was compared with the vanilla Japanese border-conflict implementation in `common/decisions/JAP.txt`.

## Final repair re-audit

| Surface | Result | Evidence |
| --- | --- | --- |
| Hidden-collapse aftermath | Clean | `secret_alliance_prepare_hidden_collapse_aftermath` copies only confirmed participants, innocent suspects, Evidence, and Preparedness before runtime teardown. Event `chaosx.nr11.194` exposes four real choices with AI weights: publish the proven case, seal the files, repair innocent relations, or retain a Preparedness-scaled counterintelligence idea. Final freeze `1c87d923` raises that idea's ceiling to 730 days and the English tooltip states that it can last as long as two years. The effects clear copied aftermath arrays and snapshots only after the selected option resolves, and Empty Chair readiness is recorded before cleanup. |
| Reveal transaction | Clean | First-sponsor registration remains durable at effects line 778. `secret_alliance_select_reveal_leader` applies designated sponsor, strongest active major, strongest active founder, and hostile-war anchor precedence at line 3788. Snapshotting begins at line 3856, faction creation at line 3971, rollback at line 4028, and the guarded convergence transaction at line 4274. Prior factions are restored after failed creation or failed mandatory hostile-war calls, while a successful transaction clears rollback snapshots. |
| Postwar dispositions | Clean | `secret_alliance_count_current_public_faction_survivors` at effects line 4749 resolves the live leader of the owned Event 011 faction template and counts only members still in that faction. Target and coalition victory helpers at lines 4789 and 4884 apply the named continuation-member threshold plus saved doctrine, Resolve, leadership, sponsor-collapse, dispute, and conflicting-promise facts. Qualifying blocs are converted before runtime cleanup by `secret_alliance_promote_public_faction_to_postwar_bloc` at line 5106 to a static name, manifest, goal, and four localised postwar rules. All other owned Event 011 factions are dismantled in `secret_alliance_finalize_outcome` at line 5228. The outcome transition holds the reveal transaction guard across synchronous faction on-actions. Promotion immediately invokes `secret_alliance_refresh_postwar_bloc_state` at line 5165, which dismantles an invalid or one-country remnant and clears its registry. |
| Scenario composition identities | Clean | Launch viability is type-aware at `common/scripted_triggers/011_secret_alliance_triggers.txt:681-808`. Regional Ring requires same-continent operational reach; Ideological Front requires target-opposed partners; Great-Power Sponsor requires a reachable major and reachable minor network; Unlikely Coalition requires both aligned and opposed minors; Random Coalition remains type-neutral. Runtime selection forces one aligned and one opposed minor for Unlikely Coalition before filling the remaining safe roster at effects line 5832. `secret_alliance_apply_scenario_identity` at line 5908 assigns doctrine, roles, support capability, incompatible commitments, fracture reserve, and intensity-scaled materiel. Launch resets prior run snapshots at line 6067 and aborts instead of substituting an invalid composition. |
| Achievement timing | Clean | Per-run readiness and outcome snapshots reset in `secret_alliance_reset_target_run_snapshots` at effects line 868 for both ordinary and manual entry. Every Thread snapshots immediately before reveal; Their Man in the Room becomes ready only when the preserved turned channel produces the false-plan opening consequence at effects line 4084; Divide the Table and Surrounded, Not Buried are checked after a final outcome is recorded but before cleanup at lines 5079-5101; Two Giants, One Grave records capital control and collapsed Resolve before teardown at lines 4794-4805. The annex disqualifier is isolated to the correctly scoped `on_annex` handler at effects line 6180. The achievement registry additionally requires `achievement_secret_alliance_resolution_qualified` for Surrounded, Not Buried at `common/achievements/chaos_redux_achievements.txt:2134-2153`. |
| Cleanup and lifecycle | Clean | `secret_alliance_cleanup_runtime_context` begins at effects line 5478, cancels the exact border conflict, removes missions and event ideas, clears target/member/suspect runtime state, clears arrays and event targets, removes AI strategies, and preserves only explicit achievement/outcome memories and a valid postwar registry. Bounded member and suspect cleanup archives retain teardown ownership even after active arrays are pruned. The first sponsor-collapse pulse is guarded so one capitulation cannot drain Resolve repeatedly. Narrow on-actions cover war, capitulation, government, annexation, faction, leadership, subject, civil-war, and peace-conference changes at `common/on_actions/011_secret_alliance_on_actions.txt:8-76`. A mechanical comparison found no Event 011 global flag set without a clear path and no saved Event 011 global target without a clear path. |

## DM-01 through DM-14

| ID | Result | Evidence |
| --- | --- | --- |
| DM-01 | Resolved | The ROOT-only scripted GUI disables AI use, supplies three clickable suspect cards plus clear/animation controls, and drives meters and card frames through properties at `common/scripted_guis/011_secret_alliance_scripted_gui.txt:5-76`. Matching interface elements remain at `interface/011_secret_alliance.gui:30-47`. |
| DM-02 | Resolved | Strict leader precedence, post-validation, hostile-war all-member retry, rollback, prior-faction restoration, and route preservation are covered by the reveal-transaction evidence above. |
| DM-03 | Resolved | Dynamic cost calculation begins at effects line 1063; reusable payment helpers begin at lines 2490-2546. Family affordability gates at `common/scripted_triggers/011_secret_alliance_triggers.txt:463-577` cover every base resource, and decision-specific gates cover all extra trains, trucks, convoys, fuel, manpower, Stability, and War Support. Allied Consultation and Neutral Inquiry use the same full diplomacy payment gate at `common/decisions/011_secret_alliance_decisions.txt:495-516`. The strict-resource sweep found no exact-balance affordability site using a bare strict `>`. AI shared-effect paths check the same base and extra payment gates before invocation. |
| DM-04 | Resolved | Seven named, nonselectable investigation missions occupy decisions lines 229-337. Preparation stores an exact state and suspect pointer beginning at effects line 2239; delayed verification begins at line 2336 and requires that exact state plus a route-specific field fact. Completion, partial, failure, cancellation, and expiry paths clear the matching state and suspect pointer. |
| DM-05 | Resolved | `secret_alliance_recalculate_preparedness` at effects line 3137 rebuilds Preparedness from distinct maintained sources. Project and source-specific expiry helpers prevent one expiring contribution from deleting another. Emergency, patrol, and consultation expiry events remain wired at `events/011_secret_alliance.txt:433-459`. |
| DM-06 | Resolved | Per-suspect source-class storage and global independent-class tracking remain in `secret_alliance_apply_new_clue` at effects line 1939. Confidence and corroboration gates remain explicit in triggers lines 438-458, while mission clues retain their prepared suspect and a defined evidence class. |
| DM-07 | Resolved | The canonical suspect trigger at triggers line 393 rejects invalid, cleared, target-aligned, and target scopes. Concealed AI reads the full suspect array, revealed AI reads the public-member array, and `secret_alliance_rebuild_visible_suspects` independently ranks and caps the human GUI pool at effects line 1872. |
| DM-08 | Resolved | Foreign Interference remains concealed Evolution II only and Coalition Crisis owns Evolution III/revealed play. Reveal closes the response category inside `secret_alliance_reveal_pact`. |
| DM-09 | Resolved | `secret_alliance_prepared_border_pair_has_units` at triggers line 606 binds infrastructure, railways, divisions, and both stored states to the exact pair. Decisions lines 651-732 require and highlight that pair. Start, escalation, negotiation, win/loss, and `secret_alliance_cancel_exact_border_conflict` at effects line 3041 share exact-state cleanup. |
| DM-10 | Resolved | `secret_alliance_convert_hidden_values_to_war_state` at effects line 4049 converts hidden values into Resolve, opening coordination, known weaknesses, and target defenses. Low, medium, and high stages remain distinct in `common/ideas/011_secret_alliance_ideas.txt`, while zero applies no stage and cleanup removes every event-owned stage. |
| DM-11 | Resolved | Ordinary eligibility remains human-target-only, with a hidden opt-in AI test route. Every ROOT-scoped and runtime candidate trigger excludes the target; both subject directions are excluded. Concealed and revealed AI target the full valid arrays. Wartime AI at effects line 4587 uses the same selected public member and cost-gated shared actions as player decisions. |
| DM-12 | Resolved | `secret_alliance_apply_false_accusation_consequences` at effects line 3305 records the immutable innocent-accused fact and applies Stability, cohesion, alertness, opinion, and recruitment consequences. Corroboration and achievement safeguards continue to read the durable innocent facts. |
| DM-13 | Resolved | Full teardown and narrow lifecycle coverage are covered by the final repair cleanup evidence above. |
| DM-14 | Resolved | Each concealed pulse selects one incident at effects line 1401. Weighted operation selection begins at line 1662 and consumes roles, motives, doctrine, recent family, operational surface, and readiness layer. Decision visibility remains phase-, incident-, suspect-, objective-, and cap-aware; named cooldown, AI-factor, AI-hint, and slot constants replace raw decision tuning values. The complete Event 011 scripted-call audit found 357 definitions and 338 calls with zero undefined effect or trigger calls. |

## RA-01 and RA-02

| ID | Result | Evidence |
| --- | --- | --- |
| RA-01 | Resolved | Maximum still requests twelve members and two majors through named scenario-scale constants. Type-aware prechecks exclude the target, require a viable identity-specific composition, and use the same runtime-safe minor/major gates as selection. Requested, safe, achieved, and major counts are snapshotted at effects lines 5784-6055. Maximum qualification requires the achieved major count and either the requested total or exact exhaustion of the safe pool. |
| RA-02 | Resolved | `secret_alliance_outcome_band` constants define full, partial, failure, and expired identities in `common/script_constants/011_secret_alliance_constants.txt`. Outcome helpers write those names at effects lines 2553-2829, and downstream decisions/effects read the same names. No raw numeric outcome identity remains in the audited flow. |

## Task-specific verification

- Confirmed the hidden-collapse choice can still read copied participants, innocents, Evidence, and Preparedness after runtime cleanup, and that each option clears the copied state only after applying its effect.
- Confirmed the hostile-war reveal cannot commit while a valid snapshot member remains outside the target war; failure retries once, dismantles the Event 011 faction, restores recorded prior factions, and cleans runtime state.
- Confirmed doctrine-specific postwar disposition runs before target-dependent state is cleared, and a surviving faction contains no target-, doctrine-, Resolve-, or reveal-dependent name, manifest, goal, or rule.
- Confirmed immediate postwar validation dismantles a one-country remnant and the outcome reentrancy guard prevents synchronous faction on-actions from reopening settlement logic.
- Confirmed all five scenario types have executable composition identity rather than label-only differentiation.
- Confirmed all six achievement readiness paths are written before cleanup and Surrounded, Not Buried cannot qualify from Maximum selection alone.
- Confirmed all seven missions use named outcome bands, exact objectives, delayed verification, partial-result effects, and per-suspect corroboration.
- Confirmed Event 011 global flags and saved global event targets all have teardown coverage.

## Simplifications, omissions, and blockers

None in the audited scope. No fallback, placeholder, skipped route, or weaker substitute was accepted.
