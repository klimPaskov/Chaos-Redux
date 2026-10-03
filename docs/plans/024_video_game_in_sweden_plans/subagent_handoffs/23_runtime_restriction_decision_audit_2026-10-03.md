# Event 24 runtime restriction and decision audit

Status: bounded read-only audit complete. No gameplay, localisation, tests, Git index, or commit changes were made by this auditor. The parent owns implementation and final review.

Acceptance basis: the user states that all files under `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\specs\024_video_game_in_sweden_specs\` are accepted and binding. Preserve every accepted route. The retired Field-Validated Planner remains absent, and the experimental spirit continues to use vanilla `SWE_wargames`.

The scoped Event 24 decision, effect, trigger, event, and localisation sources contain no `Field-Validated Planner` or `field_validated_planner` identifier.

## Scope and source identity fence

Audited the current ordinary decision category, its 18 decision definitions, four mission definitions, their direct costs and effects, phase and host gates, lifecycle callbacks, daily observer, restriction receipts, closure, report event, costs and tooltips. The current category is the ordinary vanilla decision view with a static category picture. No dedicated Event 24 scripted GUI was found or authorized.

The first source capture matched the immutable `probability_snapshots\2026-10-03_post_runtime_restriction\` snapshot for decisions, main effects, and constants. The shared owner then changed those sources during this audit. The final live identities below are the versions reviewed for this handoff. The connected decision and probability calls returned no source revision, so their inputs cannot be tied to either identity.

| Source | First captured SHA-256 | Latest sampled SHA-256 | Drift reviewed |
| --- | --- | --- | --- |
| `common\decisions\024_video_game_in_sweden_decisions.txt` | `8b19fcb187ff40bcfd66c49ff54ec18b009d5724cc6d74ec5bc416af463b6eef` | `686e58631adfc7493ec1defac544ae470a60319ed04f74575ed3f5e3ac0607ba` | National League native cooldown ladder, aligned Foreign Licensing and Dual-Track factory terms, and hidden raw predicates. No `ai_will_do` factors changed in the reviewed diff. |
| `common\scripted_effects\024_video_game_in_sweden_effects.txt` | `0c2150446c29082bf684301d885375e9a3c516f7598f80f470c70eb7ef7a6223` | `dd97b58fabde606457c4f07a05492b74b5a4631e0674e025a5fe413716035c62` | Latest shared-tree drift adds guards to six mission callbacks and sets the Restriction failure receipt on the invalid-system closure path. |
| `common\script_constants\024_video_game_in_sweden_constants.txt` | `a498c1c0458a69b9e377efeb0a4e3d4c94828185db48797e520e1dc1e6159c19` | `da0a4c5918ff3f3f8b1e321d7454877c4971d8d33cb342b6863ea7cb49451f4e` | Added the 90-day National League burden cap. |
| `common\scripted_triggers\024_video_game_in_sweden_triggers.txt` | `3904b9a6db454c6c6abadaf5421514b354d1bd72f0563a2b9ad31c8ccb41eb48` | `1c3b24791f77e2e0ef4a76ced3b9af342366e0f0514cc3745811bd6f916b3fc8` | Latest shared-tree drift adds typed callback guards; Restriction and Dual-Track objective triggers also check the active mission id. |
| `common\scripted_effects\024_video_game_in_sweden_runtime_effects.txt` | `4aa52824d237180d59c2e57e8c23d4dc5a6841b93d243e779004f20466b89efb` | `4aa52824d237180d59c2e57e8c23d4dc5a6841b93d243e779004f20466b89efb` | No drift detected. |
| `common\on_actions\024_video_game_in_sweden_lifecycle_on_actions.txt` | `146ae2ff3ca85adf67a11de3374e842173e530f394cfc597e4b316d4cf1a68de` | `146ae2ff3ca85adf67a11de3374e842173e530f394cfc597e4b316d4cf1a68de` | No drift detected. |
| `events\024_hearts_of_iron.txt` | `36a3be4f03a942e08ea6dc3bdb3c20a8e112a54d667bda91d031beaecc51c159` | `36a3be4f03a942e08ea6dc3bdb3c20a8e112a54d667bda91d031beaecc51c159` | No drift detected. |
| `localisation\english\024_hearts_of_iron_l_english.yml` | No live entry hash was captured before the owner edits. The preserved snapshot hash is `b592952de06cf1ec8e14007750a669f6858d6236b30043c6c1f8ce77b1e1b1b0`. | `ae8911e200066dce4a9542bb40b5ac631a8a8a377270b8470c3bd53e1b6ad2a2` | Current wording updates the receipt report, Trust term, audit proof getter, requirements, and cost text. Current YAML retains a UTF-8 BOM. |
| `common\scripted_localisation\024_video_game_in_sweden.txt` | `8d1d97965bbcdd572503950684bb8677d10bb65a124146bbbb20011e616a92ad` | `357d92a47cea45066657eedcf5794fcdd91878171ab2bee2319d2e21e499137f` | Added `GetVideoGameAuditProofRequirements`, selecting full or narrow proof text from the actual narrow-audit flag. |
| `docs\plans\024_video_game_in_sweden_plans\tests\test_runtime_observation.py` | Earlier 10-case SHA-256: `aae30e8121fcf889c7ef7f93cfa23b553b3ee8dc848354f74eb546b77ea415c` | `5090f0ceecb948d8859439bcefbfeb76fe42c794b2542d714731b61ec3fab30e` | Owner-added tests cover native factory-duration alignment and the full/narrow proof getter. This file is not this auditor’s change. |

The drifted source diffs were reviewed against the preserved runtime-restriction snapshot. National League repeats now use `video_game_in_sweden_national_league_native_days`, initialized to 45 and increased by 15 days after each native removal until capped at 90, giving 45/60/75/90/90. Repeat factory burden reads the same current term. Foreign Licensing’s decision lock now matches its 30-day factory burden rather than its five-day response delay. Dual-Track’s action lock now uses the 30-day factory burden rather than its 120-day mission timeout. The audit did not change these owner edits.

The owner also moved raw audit, restriction, and mission objective helpers into existing `hidden_trigger` tooltip blocks, refreshed the Restriction report wording, exposed the Trust term, and added `GetVideoGameAuditProofRequirements` to select the actual full or narrow proof key. The current National League cost tooltip displays the variable reservation term and 90-day cap. These edits improve requirement and duration clarity. The source regression now selects the nested `video_game_national_league` from the actual `video_game_in_sweden_program_category` block rather than mistaking the file-scoped `@VIDEO_GAME_DECISION_FACTORY_BURDEN` for a category.

The final local hash check found additional shared-tree edits after the first handoff draft. The current effects file adds mission callback guards and a Restriction failure receipt; the current trigger file adds matching typed guard predicates. Findings below reflect these newer identities. These are the latest local samples before handoff completion; recheck them if the main agent edits these files again before commit. No gameplay source was edited by this auditor.

## Findings sorted by severity

### P1: Six non-Restriction mission callbacks are guarded in latest source; runtime verification remains pending

The first audit capture showed six non-Restriction callbacks without a current-mission guard. In the latest shared-tree source, all six wrappers check a typed callback predicate before running outcome logic or queueing a report (`common\scripted_effects\024_video_game_in_sweden_effects.txt:2887-2935`). The predicates require the active-program flag, matching mission-active flag, and exact active-mission enum (`common\scripted_triggers\024_video_game_in_sweden_triggers.txt:829-845`). Their downstream outcome helpers can clear mission state and change Reliance, ideas, modifiers, route flags, and recovery state (`common\scripted_effects\024_video_game_in_sweden_effects.txt:1403-1571`).

The Restriction callbacks retain the active-program, active-Restriction, and exact mission-id guard at `common\scripted_effects\024_video_game_in_sweden_effects.txt:2865-2884`. The objective trigger now also checks its exact active-mission id (`common\scripted_triggers\024_video_game_in_sweden_triggers.txt:686-689`).

The latest source therefore addresses the identified source gap. The remaining runtime hypothesis is that native delayed callbacks may arrive after cancellation or closure; this cannot be confirmed from source, and the native inspector returned no result. The current 12-case observer tests do not exercise wrong-mission callbacks or callbacks after closure, so the owner should add focused source regressions or otherwise verify the new guard behavior before treating it as tested.

No further source patch is recommended from this audit. Preserve the Restriction zero-reserve costs, emergency completion rule, and all current AI weights. These callback guards are owner-authored shared-tree drift, not this auditor’s changes.

### P1: Accepted supplied-division proof remains unsupported

The field objective requires a qualifying division count in one of states 138, 141, or 666 and uses the country stockpile-based `video_game_in_sweden_has_campaign_supply_gap` check (`common\scripted_triggers\024_video_game_in_sweden_triggers.txt:620-669,732-757`). The daily observer records a sticky interruption when this stockpile check or the field count fails (`common\scripted_effects\024_video_game_in_sweden_runtime_effects.txt:42-88`).

This proves neither per-division supply satisfaction nor local delivery to the formations. Keep the native supply-gap reader and per-division supply proof unresolved. Do not substitute national trains, trucks, or fuel stores for supplied-unit evidence. This is also the explicit limitation in handoff 20 and the current user instruction.

### P2: Restriction failure receipt now has a source producer; runtime path remains unverified

The latest source sets `video_game_in_sweden_restriction_failed` in the invalid-system branch of `video_game_in_sweden_failed_restriction_apply_current`, alongside disqualification, mission cleanup, and program closure (`common\scripted_effects\024_video_game_in_sweden_effects.txt:1601-1617`). The flag remains the reveal condition for the Restriction decision (`common\decisions\024_video_game_in_sweden_decisions.txt:602`) and report option B (`events\024_hearts_of_iron.txt:526`).

This resolves the prior source-only dead-receipt finding. The normal zero-reserve Restriction path remains successful, and its delayed report is allowed after closure (`events\024_hearts_of_iron.txt:503-529`). Whether an invalid-system timeout reaches this branch and presents the failure option in native runtime remains unverified. Keep the emergency path free of new resource gates.

### P2: Dual-Track verification still measures time and Stockholm control, not the accepted work products

`video_game_in_sweden_dual_track_objectives` checks current host, active flag, exact mission id, 90 elapsed days, and Stockholm ownership/control (`common\scripted_triggers\024_video_game_in_sweden_triggers.txt:673-684`). It still does not check receipts for independent simulated and conventional plans or their comparison, as required by the accepted decision map. The mission writes success through `complete_dual_track` without those product receipts (`common\scripted_effects\024_video_game_in_sweden_effects.txt:1534-1547`).

This remains the unresolved accepted gap recorded in handoff 20. The owner should add the accepted independent-result receipts before treating the mission as evidence of a completed comparison. No redesign was attempted here.

### P2: Full Reality Audit remains inaccessible from some High-Chaos openings

The full-audit start requires both `video_game_in_sweden_logistics_review_complete` and `video_game_in_sweden_red_team_complete` (`common\scripted_triggers\024_video_game_in_sweden_triggers.txt:446-462`). The Logistics action is visible only in baseline/Evolution I (`common\decisions\024_video_game_in_sweden_decisions.txt:41-73`) and the Red Team action is Evolution I only (`common\decisions\024_video_game_in_sweden_decisions.txt:196-225`). The High-Chaos route access problem is already listed as accepted and queued in ledger 16. Keep it there for the parent’s accepted route tranche. No route expansion was made here.

### P2: Foreign Licensing route lock and AI ranking remain unresolved

The current action checks for a valid partner and no current supply gap, and pays convoys, political power, and a civilian office (`common\decisions\024_video_game_in_sweden_decisions.txt:361-407`). The accepted P24-D4 condition also expects usable convoy access and invalidation while blockaded. Handoff 19 records that current source has no explicit blockade/usable-route predicate and leaves partner autonomy/scope unresolved. Preserve this as the existing accepted route-lock gap. No AI weight or target was changed.

## Decision category lifecycle and cognitive load

Category `video_game_in_sweden_program_category` remains an ordinary category, filtered to a valid current Swedish host and hidden when empty (`common\decisions\categories\024_video_game_in_sweden_categories.txt:1-21`). Its phase gates expose 18 distinct actions across the program, not simultaneously. Source-level maxima are four baseline actions, four Evolution I actions, five Evolution II actions, four initial Evolution III choices, three during Trust Model reassessment, and two in either post-audit or post-Dual-Track recovery. No phase exceeds five. The `video_game_in_sweden_no_active_mission` trigger checks all four missions (`common\scripted_triggers\024_video_game_in_sweden_triggers.txt:236-241`), and mission starts reset shared mission state before setting the active id. The normal route therefore displays at most one active mission.

The 18 decision ids are `video_game_controlled_exercise`, `video_game_logistics_module`, `video_game_expand_access`, `video_game_conclude_trial`, `video_game_rules_revision`, `video_game_field_validation`, `video_game_red_team`, `video_game_officer_league`, `video_game_national_league`, `video_game_protect_shifts`, `video_game_preparedness_clubs`, `video_game_foreign_licenses`, `video_game_separate_policy`, `video_game_begin_reality_audit`, `video_game_narrow_reality_audit`, `video_game_dual_track`, `video_game_restrict_use`, and `video_game_trust_model` (`common\decisions\024_video_game_in_sweden_decisions.txt:13-670`).

The four missions are `video_game_field_validation_mission`, `video_game_reality_audit_mission`, `video_game_dual_track_verification`, and `video_game_restriction_enforcement` (`common\decisions\024_video_game_in_sweden_decisions.txt:677-802`).

The category header shows Simulation Reliance with its band and next threshold, the current phase, current work, and next review (`localisation\english\024_hearts_of_iron_l_english.yml:94-95`). These fields have distinct decision value, route, mission, and timing meanings. The descriptions state how decisions move Reliance and identify the visible consequence. Text is compact and phase-based. No raw numeric dump or extra tab was found. Source-only review confirms the intended density; no rendered visual claim is made.

## Mission quality

| Mission | Owner/category | Region and requirement | Duration | Success and failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- |
| `video_game_field_validation_mission` | Valid current Swedish host; Swedish Campaign Cabinet | One of states 138/141/666, Stockholm ownership/control, committed stores, a logistics or Red Team review, and 90 proof days. Supply is the national stockpile proxy described above. | 120-day timeout, 90-day proof. | Full, partial, or failure outcomes. Timeout gives partial only when current field conditions remain; otherwise failure. | Latest source guards callbacks; wrong-mission and post-closure cases are not in the 12-case tests. |
| `video_game_reality_audit_mission` | Valid current Swedish host; Swedish Campaign Cabinet | Full route requires two divisions in each of 138/141/666, full control, Stockholm ownership/control, reserves, both reviews, and 120 proof days. Narrow route uses one region and 60 proof days. | 180-day full timeout, 90-day narrow timeout. | Full or partial completion uses sticky interruption receipts. Timeout may be partial or failure based on remaining field conditions. | Latest source guards callbacks; wrong-mission and post-closure cases are not in the 12-case tests. Exact supplied-unit proof remains blocked. |
| `video_game_dual_track_verification` | Valid current Swedish host; Swedish Campaign Cabinet | Stockholm ownership/control and 90 elapsed days. Independent plan and comparison receipts remain absent from the objective. | 120-day timeout, 90-day proof. | Completion grants Dual-Track success and recovery. Failure leaves a final review route. | Latest source guards callbacks; accepted plan-result proof remains unresolved. |
| `video_game_restriction_enforcement` | Valid current Swedish host; Swedish Campaign Cabinet | Restriction orders, league-closure receipt at 20 days, policy-exclusion receipt at 40 days, public-facility receipt at 60 days, plus 60 elapsed days. | 90-day timeout, 60-day proof. | Success closes the program, removes Event 24 benefits, and applies the finite backlash. A still-valid host resolves timeout through the emergency completion path. | Latest source guards callback and objective mission identity; invalid-system failure receipt source exists, but those branches are not covered by current tests. |

All four definitions omit `selectable_mission`, so they are goal-style auto-completing objectives. Failure and cancellation branches are distinct in source, but late callback ownership remains as above.

## Cost and requirement clarity

All 18 actions remain within the four-type spendable-cost limit. The counts include temporary civilian-factory commitment where the decision modifier ties up an office. Mission enforcement after the Restriction start has no additional payment.

| Decision | Cost types and count |
| --- | --- |
| `video_game_controlled_exercise` | Army XP, support equipment, fuel: 3. |
| `video_game_logistics_module` | Trains, trucks, support equipment, civilian factory: 4. |
| `video_game_expand_access` | Political power, army XP: 2. |
| `video_game_conclude_trial` | None: 0. |
| `video_game_rules_revision` | Army XP, command power: 2. |
| `video_game_field_validation` | Fuel, support equipment, trains, army XP: 4. |
| `video_game_red_team` | Political power, army XP: 2. |
| `video_game_officer_league` | Command power, army XP: 2. |
| `video_game_national_league` | Political power, civilian factory: 2. |
| `video_game_protect_shifts` | Political power, civilian factory: 2. |
| `video_game_preparedness_clubs` | Political power, support equipment: 2. |
| `video_game_foreign_licenses` | Convoys, political power, civilian factory: 3. |
| `video_game_separate_policy` | Political power, stability: 2. |
| `video_game_begin_reality_audit` | Army XP, support equipment, fuel, trains: 4. |
| `video_game_narrow_reality_audit` | Army XP, support equipment, fuel, trains: 4. |
| `video_game_dual_track` | Army XP, command power, civilian factory: 3. |
| `video_game_restrict_use` | Political power, stability, war support: 3. |
| `video_game_trust_model` | Command power, political power, stability, war support: 4. |

Every spendable appears with a texticon in its cost row or full cost tooltip. The verified icon map is Army XP `£army_experience`, political power `£pol_power`, command power `£command_power`, stability `£stability_texticon`, war support `£war_support_icon`, fuel `£fuel_texticon`, support equipment `£support_equipment_text_icon`, trains `£train_texticon`, trucks `£motorized_equipment_text_icon`, convoys `£convoy_texticon`, and civilian factories `£civ_factory`. The custom support-equipment and truck texticons are defined in `interface\chaosx_texticons.gfx:90-96`; vanilla texticons are registered in `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\interface\texticons.gfx`, and the war-support sprite is `GFX_war_support_icon` in `interface\topbar.gfx:257-258`. Offline Localisation documentation says a texticon uses its `GFX_` name without the prefix (`paradox_wiki\Localisation - Hearts of Iron 4 Wiki.md:221-242`, SHA-256 `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`).

The row strings keep at most three values. Full tooltips disclose the fourth value for Logistics, Field Validation, both audits, and Trust Model. Restriction shows political power and Stability inline and War Support in its full cost tooltip. No resource name is substituted for an icon, and no action exceeds four spendable types. Non-consumed requirements are separated into short custom tooltips. The dynamic Restriction quote caps fees at 30 political power, 0.04 Stability, and 0.03 War Support, charges each current reserve only once, accepts zero reserves, and has no fixed `ai_hint_pp_cost` (`common\scripted_triggers\024_video_game_in_sweden_triggers.txt:152-182`, `common\scripted_effects\024_video_game_in_sweden_effects.txt:756-775`).

The hidden finite backlash is applied after closure and survives its cleanup guard: `stability_factor = constant:video_game_in_sweden_effect.backlash_stability` with `backlash_stability = -0.03` for 90 days (`common\dynamic_modifiers\024_video_game_in_sweden_dynamic_modifiers.txt:60-62`, `common\script_constants\024_video_game_in_sweden_constants.txt:335,173`). The current cost tooltip states three percentage points for 90 days. Offline Modifiers documents `stability_factor` as a flat modifier (`paradox_wiki\Modifiers - Hearts of Iron 4 Wiki.md:522-528`, SHA-256 `fe41a26f2b8d3b8e78a9b0dea9ce1a55f001d1e27886807a0a3fb2d2f535f14f`) and installed documentation lists it under country modifiers (`C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\modifiers_documentation.md:4825-4828`, SHA-256 `00a0eca6d2b3a70ce4b8a0d38997dd609aa0c9349ddcd04c8cac92849425be7e`).

## AI, cleanup, and exploit risk

All 18 decisions contain `ai_will_do` blocks. The four mission definitions have no mission-selection AI scores. The current owner drift changed cooldown/burden durations but did not change any AI score factor. The Restriction emergency action intentionally has no fixed political-power AI hint because its reserve-limited quote can be zero.

The host trigger verifies that the saved host target matches the country calling the helper through `PREV` (`common\scripted_triggers\024_video_game_in_sweden_triggers.txt:46-56`). The state-control callback uses `FROM` as old controller and `FROM.FROM` as state, and the capitulation/annex callbacks retain their native scopes (`common\on_actions\024_video_game_in_sweden_lifecycle_on_actions.txt:10-21`; offline On actions, `paradox_wiki\On actions - Hearts of Iron 4 Wiki.md:450-461`, SHA-256 `6822adc85a374a1c1364f2def6f32c6d66da9fb0280319ddd6af4b84b33d882a`).

The close helper is idempotent behind `video_game_in_sweden_program_closed`. It clears shared targets only when the country owns the saved host target, removes all 18 decisions and all four missions, clears staged ideas, and preserves the restriction backlash applied after closure (`common\scripted_effects\024_video_game_in_sweden_effects.txt:1779-1913`). The `.91` observer schedules one next daily event behind `video_game_in_sweden_runtime_watch_pending`, clears the pending flag before observing, and never iterates the world (`common\scripted_effects\024_video_game_in_sweden_runtime_effects.txt:10-125`, `events\024_hearts_of_iron.txt:713-720`).

The success report path has a matching receipt description, and the tooltip explicitly states the 60-day enforcement period and lack of further payment. The latest owner source sets `video_game_in_sweden_restriction_failed` on the invalid-system closure path; that source path is present but not runtime-verified.

The restriction report event intentionally accepts `video_game_in_sweden_program_closed` with a pending report (`events\024_hearts_of_iron.txt:503-529`). The current success path files three receipts and the 12-case owner test checks one report event is queued. The latest source adds the failure receipt producer, but the test does not assert the report event’s option set or exercise a failed/disabled callback.

Repeated National League seasons are limited by the owner’s increasing native interval and temporary civilian-office burden. Controlled exercises have cooldown and diminishing returns, foreign licensing remains capped at three partner replies, Trust Model is one-shot, and Restriction closes the program without granting `video_game_validated_wargaming_methods`. No new exploit loop was introduced by this audit.

## MCP, validation, and remaining blockers

Offline reference context request: `hoi4.reference_context(surface="decision", limit=2)` remained pending for 63 seconds and was stopped without a response, artifact, revision, or source list. The relevant local references were read directly. Installed vanilla `common\decisions\_documentation.md` hash is `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`; it documents decision visibility/availability evaluation cadence at lines 1-18. Offline Decision modding lines 465-478, SHA-256 `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, covers native missions, timeout/availability/activation, and cancellation. Vanilla `common\decisions\AUS.txt:26-43`, SHA-256 `619f5e7d922c7900c2cfe31b54dc37d32b7583deae9f33336a430d753362ef0`, supplies a native mission timeout/effect precedent.

The connected `hoi4.decision_inspect` route accepted its bounded bridge request schema but did not return the requested scenario analysis. Earlier direct attempts rejected the nested object at `scenarios[8].state.division_counts_by_state`; the exact first diagnostic text was not retained. A later direct call returned `Decision inspection requires an identifier at id` even though the published input schema marked `id` optional. After correcting those arguments, three direct inspections for `video_game_restrict_use`, `video_game_restriction_enforcement`, and `video_game_reality_audit_mission` remained pending for about 59 seconds with no artifacts and were stopped. The single bounded bridge retry used server version `3.6.0`, protocol `2024-11-05`, 40-second per-call timeout, and one `video_game_restriction_enforcement` inspection with 10 explicit scenarios. The requested case dimensions covered zero-reserve Restriction, days 19/20/39/40/59/60/90, full-field with interruption, a late callback for the wrong mission, current versus cloned-host loss, duplicate watch scheduling, and report-after-close. It returned `TimeoutError: MCP id 2 returned no result after 40s`, empty stderr, and `ownedSessionSurvivors: []`. No source revision, scenario result, scenario artifact, or decision artifact was returned; no native request remains waiting. No scenario is presented as engine or live campaign proof.

`chaosx_ai_probability_auditor` attempted one `hoi4.probability_inspect` for the 18-decision `decision_ai_will_do` pool against the dispatch-time decision hash `8b19...`. It returned no result after about 59 seconds, no artifact/revision/scenario hash, and no numeric analysis. P24-D1 through P24-D5 and the requested C5/C7 orderings remain unresolved. The current National League availability-timer source is newer than that attempted identity. No evaluation, sweep, comparison, or render ran. Do not infer a candidate ranking or balance result.

The read-only vanilla window is `countrydecisionview` in `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\interface\countrydecisionview.gui`, SHA-256 `eedea36ade734b67a23181a650464f9168beadb0e024c0cedf2112d1b097194e`. Direct `hoi4.gui_inspect(windowName="countrydecisionview")` remained pending for 35 seconds, and the matching `hoi4.gui_render` at 1920x1080/UI scale 1 remained pending for 36 seconds. Neither returned an artifact or diagnostic. The category’s visual fit, visible row costs, and production-render defects therefore remain unreviewed. No source-only visual completion claim is made.

The parent-reported 12 runtime-observer source tests and six lifetime/source tests pass, but they do not execute HOI4 and do not prove per-division supply. I inspected the current 12-case test source but did not rerun it. The new tests verify the 45/60/75/90/90 factory-duration ladder and actual full/narrow proof-key selection. They do not cover wrong-mission callbacks or the Restriction failure option. No native game was launched, no service was restarted, no Git index entry or commit was made, and no test file was changed by this auditor.

Remaining owner work before publishing: review the latest owner-authored callback guards and add or run focused tests for wrong-mission and post-closure callbacks plus the invalid-system Restriction failure report; resolve the accepted Dual-Track institutional proof; keep the exact supplied-division route blocked until a supported native proof is available; finish the known High-Chaos review-access route; and obtain decision, probability, and GUI evidence only through a bounded route that returns artifacts tied to the latest source hash. Native MCP inspection/render/probability results are still absent. No all-package completion claim is made here.

## Disposition and handoff

Files changed by this auditor: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\plans\024_video_game_in_sweden_plans\subagent_handoffs\23_runtime_restriction_decision_audit_2026-10-03.md` only. No decision, mission, scripted-GUI, localisation, or gameplay identifier was changed by this auditor. No scratch test was added.

The bounded audit is complete as an actionable owner handoff. The full Event 24 package remains incomplete. No simplification, accepted-route removal, or plan handoff was made. Skills used: `chaos-redux-decisions-missions`, `chaos-redux-events`, `chaos-redux-subagents`, and `chaos-redux-scripted-gui`. No skill was created or updated.
