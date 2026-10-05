# Event 008 Probability Baseline — 2026-10-05

**Status: incomplete; analyzer evidence is blocked.** This is a read-only source baseline for Event 008, Tensions Rising. The HOI4 probability service exposed the required tools, but a valid source-backed `hoi4.probability_inspect` request timed out after 600 seconds, so no probability, ranking, timing, sensitivity, sequence, comparison, or render result is claimed. Source evidence below names the surfaces and scenarios the parent can reuse after the analyzer route is available.

No gameplay or AI source was edited. This handoff is the only file written by this subagent. No commit was made.

## Scope and source identifiers

The root event is `chaosx.nr8.1` at `events\008_tensions_rising.txt:35-51`; the delayed reports are `chaosx.nr8.2` through `chaosx.nr8.12` at lines 55-250; hidden border-war result callbacks are `chaosx.nr8.13` through `.15` at lines 255-289; the Thin Wire check is `.20` at lines 294-312; and opinion-modifier expiry is `.21` at lines 314-322. The root and follow-ups are `is_triggered_only = yes`; the event file contains no `mean_time_to_happen`, event-option `ai_chance`, decision or mission `ai_will_do`, or direct `ai_strategy_factor` block.

The Event 008 scripted surfaces are `tensions_rising_prepare_random_event_fire` at `common\scripted_effects\008_tensions_rising_effects.txt:44-50`, `apply_tensions_rising_event_effect` at lines 84-102, timer randomization at lines 270-323, relation-pair count and country selection at lines 482-598, AI posture selection and timed-idea application at lines 698-774, delayed follow-up chance/delay at lines 776-833, follow-up dispatch at lines 836-950, and safe border-war chance/pair selection at lines 1091-1237.

The five branch-local `random_list` candidate pools are in `select_tensions_rising_followup_event`, `common\scripted_effects\008_tensions_rising_effects.txt:898-950`:

| Branch predicate order | Candidate event IDs and raw weights | Source lines |
| --- | --- | --- |
| Stage II+ and `tensions_rising_recent_relation_damage` | `10:25`, `9:25`, `8:25`, `6:25` | 908-917 |
| Stage I | `2:45`, `3:35`, `4:20` | 919-925 |
| Stage II, when the earlier recent-damage branch did not match | `5:30`, `6:25`, `10:25`, `7:20` | 927-934 |
| Full world tension, after the earlier stage and relation-damage branches | `4:25`, `8:25`, `9:25`, `10:25` | 936-943 |
| Fallback branch | `8:25`, `9:25`, `7:25`, `10:25` | 945-950 |

These are source weights, not evaluated selection percentages. The pool rows are complete for each literal `random_list`; reachability depends on the preceding stage, recent-relation flag, full-world-tension predicate, and the one-time Stage IV briefing flag.

The follow-up chance and delay tuning is `tensions_rising_followup` in `common\script_constants\008_tensions_rising_constants.txt:115-133`: Stage I/II/III/IV chance thresholds are `30/50/75/90`; delay bounds are `5-15`, `4-12`, `3-10`, and `2-8` days. The border-war thresholds are in `tensions_rising_incident_border_war` at lines 202-213: minimum stage `3`, standard Stage III/IV thresholds `35/60`, Last Normal Briefing thresholds `50/80`, and a division threshold of `3`. The effect draws integer rolls with `min = 1`, `max = 100` at `008_tensions_rising_effects.txt:817-828` and `1142-1152`.

The four timed AI ideas are `tensions_rising_cautious_alignment`, `tensions_rising_alarmist_rearmament`, `tensions_rising_general_staff_fever`, and `tensions_rising_permanent_alert` in `common\ideas\008_tensions_rising_ideas.txt:11-64`. They apply AI-related modifiers, not direct selection weights: `ai_join_ally_desire_factor` is `0.08/0.12/0.18/0.25`; `ai_get_ally_desire_factor` is `0.08` at Stage I; and `enemy_justify_war_goal_time` is `-0.10/-0.15` at Stages III/IV. `common\scripted_effects\008_tensions_rising_effects.txt:698-774` selects up to `4/6/8/12` AI countries per stage from the current pool of valid AI majors, faction leaders, or countries at war, excluding those with the recent-posture flag. The exact candidate set is campaign-dependent.

The timer-pulse ranges are Stage I/II/III/IV 45-75, 75-120, 120-180, and 180-240 days; relation-pair count ranges are 1-2, 2-3, 3-5, and 5-8, from common\script_constants\008_tensions_rising_constants.txt:63-100. The timed AI-idea durations are 45/75/100/140 days at lines 229-238. These are source bounds and durations; the probability adapter did not confirm the draw distributions.

The only Event 008 on-action is `on_war_relation_added` in `common\on_actions\008_tensions_rising_on_actions.txt:5-9`; it triggers relation tracking and contains no direct weight.

## Shared root-event weighted pool

Event ID `8` is registered as a repeatable event at `common\scripted_effects\chaosx_logic_effects.txt:287`. The event system combines major, fire-once, and repeatable registrations into `global.all_events`; it initializes default event weights and caps in `chaosx_logic_effects.txt:373-404`, with `event_system_defaults.event_weight = 1000`, `recovery_rate = 20`, and `reduce_cap_factor = 0.5` in `common\script_constants\event_system_constants.txt:29-45`.

`common\scripted_effects\chaosx_settings_effects.txt:3808-3920` filters candidates, reads each active event weight, scales it, totals the active weights, draws a shared roll, and picks the first cumulative weight that reaches the roll. `common\on_actions\chaosx_on_actions_system.txt:58` and lines 180-191 run this selector from the daily event-timer handler when `event_timer_days = 0` and the country has activated the event system.

When Event 8 fires through the ordinary repeatable handler, `common\scripted_effects\chaosx_logic_effects.txt:1180-1238` halves that event cap, sets its weight to zero, and runs the minor pacing update; the active repeatable-weight updater moves a valid zero-weight entry to its floor and later recovers it by `global.minor_event_recovery_rate` up to its cap at lines 1060-1113. Thus the event source baseline is 1000, while its post-fire weight and cap vary with prior firings and pacing updates. This lifecycle was not simulated.

The Event 008 full-tension gate is correctly present in the shared candidate prefilter: `evaluate_event_pool_candidate_unavailability` checks `is_tensions_rising_automatic_event_available` for event ID 8 at `common\scripted_effects\chaosx_logic_effects.txt:651-659`, and `evaluate_random_event_active_pool_candidate` rejects candidates with a nonempty unavailability reason at lines 887-929. This matches the root prefire check at `common\scripted_effects\008_tensions_rising_effects.txt:44-50`; the earlier suspicion that a calm/full-tension Event 8 retains positive active-pool weight is cleared by current source.

The outer Event 8 selection chance is still unresolved. The complete static event registration lives in the shared arrays, but the active candidate set and weights depend on `global.disabled_events`, `global.fired_events`, current `global.event_weights` and caps, event-type availability predicates, current chaos tier, world tension, world-end state, settings, and other event-owned gates. A USA/date fixture alone does not declare those inputs.

The installed effects documentation defines `set_variable_to_random` as sampling from an inclusive minimum to an exclusive maximum. The source uses `min = 1`, `max = 100` for follow-up and border-war rolls, and `max = random_event_selection_total_weight_scaled` for the outer event-pool roll at `chaosx_settings_effects.txt:3885-3918`. This exposes a boundary-sensitive analysis lead: the intended d100 interpretation and the cumulative selector’s terminal roll need to be confirmed by the probability adapter. No exact probability or frequency has been calculated here. The Event 008 timer-pulse ranges and relation-pair counts also use integer random draws with named `min` and `max` values; the documented exclusive upper endpoint means the configured maxima may be unreachable unless the source deliberately treats the constants as exclusive limits.

## Scenario IDs declared for owner reuse

These scenarios were declared but not evaluated. Where supported by the live scenario schema, use actor `USA` and date `1936.1.1`. For each scenario, include the named stage, flags, tension state, AI/player status, and any eligible country/state candidate state explicitly; the date/tag pair does not supply those values by itself.

| Scenario ID | Intended surface and explicit state | Candidate/external completeness |
| --- | --- | --- |
| `e008-root-pool-USA-1936-01-01-calm` | Root pool selection, Stage 0, world tension below the full threshold | Static registrations are present, but active event weights, disabled/fired sets, settings, and other event availability gates are unknown. Incomplete; unresolved. |
| `e008-root-pool-USA-1936-01-01-stage0-fullWT` | Root pool selection, Stage 0, full world tension | Event 8 should fail its source availability gate; the other active pool candidates and weights are unknown. Incomplete; unresolved. |
| `e008-root-pool-USA-1936-01-01-stage1-fullWT` | Root pool selection, Stage I, full world tension | Event 8 gate is open by source, but the active global event pool and weights are unknown. Incomplete; unresolved. |
| `e008-followup-stage1-below-fullWT` | Stage I, no recent relation-damage flag, below full world tension | Stage I literal candidates and weights are complete; analyzer branch result unavailable. |
| `e008-followup-stage1-fullWT` | Stage I, no recent relation-damage flag, full world tension | Stage I branch precedes the later full-tension branch; the Stage I pool is complete, but branch evaluation unavailable. |
| `e008-followup-stage2-below-fullWT-no-relation-damage` | Stage II, recent-damage flag absent, below full world tension | Stage II literal candidates and weights are complete; analyzer branch result unavailable. |
| `e008-followup-stage2-fullWT-no-relation-damage` | Stage II, recent-damage flag absent, full world tension | The Stage II branch precedes the later full-tension branch; the Stage II pool is complete, but branch evaluation unavailable. |
| `e008-followup-stage2-recent-relation-damage` | Stage II, recent-damage flag present | The Stage II+ relation-damage pool is complete; analyzer branch result unavailable. |
| `e008-followup-stage3-below-fullWT-no-relation-damage` | Stage III, no recent damage, below full world tension | The fallback pool is complete; analyzer branch result unavailable. |
| `e008-followup-stage3-fullWT-no-relation-damage` | Stage III, no recent damage, full world tension | The full-tension pool is complete; analyzer branch result unavailable. |
| `e008-followup-stage3-fullWT-recent-relation-damage` | Stage III, recent damage, full world tension | The earlier relation-damage branch shadows the later full-tension branch; the relation-damage pool is complete, but analyzer branch result unavailable. |
| `e008-followup-stage4-first-briefing-fullWT` | Stage IV, first normal briefing not yet seen, full world tension | Source selects event 12 and sets the one-time briefing flag; no random-list candidate race in this branch. Analyzer result unavailable. |
| `e008-followup-stage4-first-briefing-below-fullWT` | Stage IV, first normal briefing not yet seen, below full world tension | Same deterministic event-12 branch; analyzer result unavailable. |
| `e008-followup-stage4-recent-relation-damage` | Stage IV, first briefing already seen, recent-damage flag present | The relation-damage pool is complete; it precedes the full-tension/fallback branches. Analyzer result unavailable. |
| `e008-followup-stage4-after-briefing-fullWT` | Stage IV, briefing already seen, no recent damage, full world tension | Full-tension pool is complete; analyzer result unavailable. |
| `e008-followup-stage4-after-briefing-below-fullWT` | Stage IV, briefing already seen, no recent damage, below full world tension | Fallback pool is complete; analyzer result unavailable. |
| `e008-border-war-stage3` | Standard incident border-war roll at Stage III | Chance threshold is source-known; actor, neighbor, target, division, war, faction, cooldown, and state-control candidates are incomplete. Unresolved. |
| `e008-border-war-stage4` | Standard incident border-war roll at Stage IV | Same incomplete actor/target/state pools. Unresolved. |
| `e008-last-briefing-border-war-stage3` | Last Normal Briefing roll at Stage III | Special threshold is source-known; candidate pools remain incomplete. Unresolved. |
| `e008-last-briefing-border-war-stage4` | Last Normal Briefing roll at Stage IV | Special threshold is source-known; candidate pools remain incomplete. Unresolved. |
| `e008-ai-posture-stage1-USA-1936-01-01` | Stage I AI posture candidate pool and timed idea | `is_ai`, eligible-country count, major/faction/war state, cooldown flags, and human status need explicit scenario inputs. Incomplete; no action probability. |
| `e008-ai-posture-stage2-USA-1936-01-01` | Stage II AI posture candidate pool and timed idea | Same incomplete candidate state. |
| `e008-ai-posture-stage3-USA-1936-01-01` | Stage III AI posture candidate pool and timed idea | Same incomplete candidate state. |
| `e008-ai-posture-stage4-USA-1936-01-01` | Stage IV AI posture candidate pool and timed idea | Same incomplete candidate state. |

The scripted relation-pair selector has additional missing state: current country roster and validity, major/faction/neighbor status, war and subject state, cooldown flags, stage-specific pair count, and target relationships. The border-war selector additionally requires adjacent owned-and-controlled nonimpassable state pairs with no existing border war. None of those dynamic candidate sets is implied by `USA` and the start date.

## MCP evidence and blocked analyses

The probability tool metadata exposed `hoi4.probability_inspect`, `evaluate`, `sweep`, `compare`, `simulate`, `sequence`, and `render`. The source-object schema accepts a mod-relative `{path: ...}` object; invalid string and empty source forms were not treated as evidence.

| Route | Request | Result |
| --- | --- | --- |
| `hoi4.probability_inspect` | `adapter = event_mean_time_to_happen`, `source = { path = "events/008_tensions_rising.txt" }` | Call remained pending for several minutes and was interrupted; no artifact, revision, or adapter report returned. |
| `hoi4.probability_inspect` | `adapter = random_list`, `source = { path = "common/scripted_effects/008_tensions_rising_effects.txt" }` | Call remained pending and was interrupted; no candidate report returned. |
| `hoi4.probability_inspect` | Source discovery with `source = { path = "events/008_tensions_rising.txt" }` | Failed after 600 seconds: `tool call failed for hoi4_agent_tools/hoi4.probability_inspect ... timed out awaiting tools/call after 600s`. No artifact or source revision returned. |
| `hoi4.probability_evaluate` | Not called | No inspect result or accepted scenario schema was available; all declared scenarios remain unevaluated. |
| `hoi4.probability_sweep` | Not called | No inspect/evaluate artifact or analyzer-confirmed parameter paths were available. |
| `hoi4.probability_compare` | Not called | No baseline analysis, before/after sources, or comparison ID exists. The parent may re-use the scenario IDs above after its bounded edits. |
| `hoi4.probability_simulate` | Not called | No explicitly parameterized uncertain input set was established. |
| `hoi4.probability_sequence` | Not called | The global event pool needs a complete current candidate manifest plus cadence, state transitions, weight recovery, caps, and terminal behavior; no sequence analysis can be claimed. |
| `hoi4.probability_render` | Not called | No `analysisId`, scenario hash, or retained probability artifact exists to render. |

The current Event Completion handoff at `docs\plans\008_tensions_rising_plans\subagent_handoffs\event_completion_audit_2026-10-05.md:112-127` records corrected `hoi4.event_inspect`, `hoi4.event_render`, `hoi4.event_compare`, `hoi4.source_lookup`, and `hoi4.reference_context` calls timing out after 600 seconds, with no structural artifact. This is cross-agent service evidence, not an artifact produced by this probability pass.

`hoi4.reference_context` and one `hoi4.reference_search` for `random_list` returned source paths, line spans, and revisions for offline wiki and installed documentation. `reference_context` reported no missing or omitted required source kinds. Four later targeted `hoi4.reference_search` calls timed out after 600 seconds; no citations were returned for those queries. Three revision-bound `hoi4.reference_read` requests for the returned random-list references remained pending and were interrupted; the corresponding local sections were read directly as the documented fallback. Successful `random_list` source discovery identifiers were `443f582ff7608109d67f72cd410f3008aa3175f6e1a1463b51644545d0927a89` (installed effects documentation), `9f905cec3724c4a9cdceff2b65c318387108e42b3a18d021460335fede9cb422` (offline Scopes page), and `86394a37361bd0cc6156f2c56a05f102678e1b43db46df156403945cf3eea043` (offline Effects page); their path spans and revisions are listed below. The context result workspace ID was `mod_chaos_redux_ea3b2d67c2c0`.
No probability artifact URI, analysis revision, scenario hash, comparison ID, rendered evidence URI, or scenario output was returned.

## Findings and result classification

| Finding | Classification | Evidence and limit |
| --- | --- | --- |
| Event 008 root eligibility is integrated into the global pool prefilter and matches the prefire availability trigger. | Source-confirmed control flow; probability unresolved. | `chaosx_logic_effects.txt:651-659`, `887-929`; Event 008 helper `008_tensions_rising_effects.txt:44-50`. No active-pool scenario was evaluated. |
| Follow-up `random_list` rows are distinct across five predicates, with no nested weight modifiers in the listed branches. | Raw source weights known; selection results unresolved. | `008_tensions_rising_effects.txt:908-950`. The earlier Stage II and Stage III/IV recent-damage predicates shadow later stage/full-tension branches. |
| Stage I includes `chaosx.nr8.4` in its pool regardless of the later full-tension branch. | Source/intent mismatch lead; unresolved. | `008_tensions_rising_effects.txt:919-943`; the historical specification describes “The Calm Map Says Nothing” as a report for when world tension is already `100%` at `008_tensions_rising_spec.md:100,264`. Current overview says evolved Event 8 can fire at full tension but does not establish that event 8.4 must be full-tension-only. Parent review should resolve intent before calling this a defect. |
| Stage IV first-briefing selection is deterministic and sets `tensions_rising_last_normal_briefing_seen`; other pools are conditional on relation damage and tension. | Source-confirmed branch routing; repeat frequency unresolved. | `008_tensions_rising_effects.txt:898-950`. No sequence analysis measured repeated reports or starvation. |
| Follow-up, timer-pulse, relation-count, border-roll, and shared-pool draws use `set_variable_to_random` or `set_temp_variable_to_random` with named max values. | Source bounds known; distribution/timing unresolved. | Event helper lines 282-323, 485-514, 780-828, 1142-1152; shared pool `chaosx_settings_effects.txt:3885-3918`; installed effects docs define the maximum as exclusive. Exact outcome frequencies were not hand-calculated. |
| The shared pool’s final cumulative-roll endpoint is boundary-sensitive because its random upper limit is exclusive. | Unresolved analyzer issue. | `chaosx_settings_effects.txt:3885-3918`, installed `effects_documentation.md:7910-7922`, offline `Data structures - Hearts of Iron 4 Wiki.md:564`. The exact impact on Event 8 depends on the complete active pool and candidate order, which were not modeled. |
| AI modifiers are not AI click probabilities or direct `ai_will_do` scores. | Score/modifier-only at source; resulting AI ranking unresolved. | Four timed ideas are defined at `common\ideas\008_tensions_rising_ideas.txt:11-64` and assigned by the random candidate selector at `008_tensions_rising_effects.txt:698-774`. The wiki distinguishes AI willingness score races from event-option probability-proportional sampling at `AI modding - Hearts of Iron 4 Wiki.md:30-33`. |
| Border-war thresholds do not equal border-war start probability. | Unresolved. | `008_tensions_rising_effects.txt:1113-1237` applies a threshold before selecting valid actors, neighboring targets, and mutually valid controlled-state pairs; those dynamic pools are incomplete. |
| No positive weight on an invalid follow-up ID was found. | Source-confirmed candidate existence only; no runtime eligibility claim. | Follow-up IDs in the five lists all have event definitions in `events\008_tensions_rising.txt`; no MCP graph/runtime confirmation was received. |
| No Event 008 decision/mission score or event-option AI choice surface was found. | Source-scan finding. | The named Event 008 event file has a single visible option for each public event and no `ai_chance`; the adjacent decision audit also found no Event 008 decision definitions. |

The specification’s AI matrix describes directional stages, but those expectations do not identify complete vanilla AI candidate races or provide actor-target factors. No dominance, starvation, exact rank reversal, exact cumulative timing, or measured repetition conclusion is made from these source values.

## Recommended follow-up, without applying changes

1. Re-run `hoi4.probability_inspect` for `random_list`, `direct_random`, `ai_strategy_factor`, and the `custom_weighted_pool` or adapter the installed service identifies for the shared event scheduler, starting from the affected source files. The 600-second timeout means every affected probability conclusion remains unresolved.
2. Evaluate the declared follow-up and border-war scenarios with complete stage, flag, tension, candidate-pool, and external-state inputs. Use the same scenario IDs for any subsequent `hoi4.probability_compare` after the parent’s authorized fixes.
3. Verify the `set_variable_to_random` endpoint behavior with the game-version adapter before changing any threshold or bound. If the design intent is an inclusive named maximum, the source bounds need an exclusive endpoint that preserves that intent; the parent owns the value decision.
4. Review whether `chaosx.nr8.4` should be restricted to full world tension or is intentionally part of the Stage I report pool. Keep that question unresolved unless the parent accepts the historical specification as current design.
5. Trace timed idea modifiers into the actual vanilla AI decision/strategy candidates before making claims about action likelihood. The modifier values alone are not normalized probabilities.
6. Keep the global Event 8 pool analysis separate from the local follow-up `random_list` analysis. The outer candidate race includes event weights and gates for the complete dynamic event system.

## Source revisions and hashes

The repository `HEAD` at capture was `8d0a28d7fe9866113718bf41a54c33996a76c722`. Hashes below identify the exact working-tree bytes read during this audit. At capture time, the shared event-system constants and scheduler files were marked modified in the shared worktree; I did not edit them.

| Windows path | SHA-256 |
| --- | --- |
| `events\008_tensions_rising.txt` | `0813C4EC4F58D164CBFE2182C75C76189658924B2CF88DD40AA3C9942EBBEE30` |
| `common\script_constants\008_tensions_rising_constants.txt` | `5C2CFF30C1714ED353C4FEDC96A1F53672B41B04AD6E190E0D15B609D6AB562D` |
| `common\scripted_effects\008_tensions_rising_effects.txt` | `4A912025DCFD60634BE365DEB9666FC0627FA88373E43E78B1E4CAE3A9ABAE65` |
| `common\ideas\008_tensions_rising_ideas.txt` | `3B0B0586A98310087D0B634BA9F3BDF01096038E53DDCF985CF96ECADDB0FEFC` |
| `common\on_actions\008_tensions_rising_on_actions.txt` | `15AF45BCBE8E033C3C2E597A4DCD964EE832B85EE05E76744D3C1084B294131B` |
| `common\scripted_triggers\008_tensions_rising_triggers.txt` | `FDC722EF70F6C8901472D46052F8EE0A49ADD7583F15C558A11698FFDFB727D4` |
| `common\scripted_effects\chaosx_logic_effects.txt` | `7D4AE19F327AEBA7A62C98BDA9236369A319BE528752E80A9B5C6C734A5F2B81` |
| `common\scripted_effects\chaosx_settings_effects.txt` | `59F3DDD64CA1077A1977A157E9BB1CC18539F25B06A3BF8A29D34C95600B056B` |
| `common\on_actions\chaosx_on_actions_system.txt` | `CC7708D49F8056310A011041F21C9EB648B7537C5993CEF4F6FFE8F01D015F24` |
| `common\script_constants\event_system_constants.txt` | `FC41DE829BA836FA43E76E9866834810D0FAEE63ED71A5642F9E07572E98DE0A` |

## Reference material read

The connected `hoi4.reference_context` route returned an AI-surface bundle with no missing or omitted required source kinds. The connected `hoi4.reference_search` route returned the random-list game-doc and wiki sections; local source text was also read directly for the exact lines below.

| Reference path and section | Revision or hash | Use |
| --- | --- | --- |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md:5413-5432` | MCP revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` | `random_list` selects one weighted effect; weight can be a current-scope variable. |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md:7910-7922` | SHA-256 `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF` | `set_variable_to_random` range semantics; the maximum is exclusive. |
| `paradox_wiki\Effects - Hearts of Iron 4 Wiki.md:4504-4571` | MCP revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` | Random-effect and probability-proportional weight explanation. |
| `paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md:894` | MCP revision `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` | `random_list` candidate weights are proportional. |
| `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md:564,588-598` | SHA-256 `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4` | `set_variable_to_random` range and integer argument. |
| `paradox_wiki\AI modding - Hearts of Iron 4 Wiki.md:30-34` | SHA-256 `917CD261F7DA51FE4D8687C5D7663E768A09C5C101AC130CE646BC64637AA818` | Distinguishes `ai_will_do` score races from `ai_chance` proportional event-option sampling. |
| `paradox_wiki\Event modding - Hearts of Iron 4 Wiki.md:130-145,159-165` | SHA-256 `96327B896298420D84058394A44ED08BE7EB518726B8F207B392FEA71F05D43D` | MTTH automatic event behavior, `is_triggered_only`, and event-option `ai_chance`. |
| `paradox_wiki\Modifiers - Hearts of Iron 4 Wiki.md:546,810-811` | SHA-256 `FE41A26F2B8D3B8E78A9B0DEA9CE1A55F001D1E27886807A0A3FB2D2F535F14F` | `enemy_justify_war_goal_time`, `ai_get_ally_desire_factor`, and `ai_join_ally_desire_factor` descriptions. |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\modifiers_documentation.md:1482-1486,2488-2494` | SHA-256 `00A0ECA6D2B3A70CE4B8A0D38997DD609AA0C9349DDCD04C8CAC92849425BE7E` | Installed modifier kinds/categories for the AI and enemy-justify modifiers. |

## Skills used and remaining blockers

Read and applied `AGENTS.md`, `.agents\skills\chaos-redux-subagents\SKILL.md`, `.agents\skills\chaos-redux-events\SKILL.md`, `.agents\skills\chaos-redux-mtth\SKILL.md`, and the relevant AI-audit section of `.agents\skills\chaos-redux-decisions-missions\SKILL.md`. No skill or source file was created or changed.

The remaining blocker is the missing probability artifact delivery. Until a valid inspect/evaluate/sweep/render pass returns, all numeric selection and timing conclusions, AI ranking outcomes, border-war rates, repetition rates, and exact outer-pool probabilities remain unresolved. No campaign-live behavior is inferred.
