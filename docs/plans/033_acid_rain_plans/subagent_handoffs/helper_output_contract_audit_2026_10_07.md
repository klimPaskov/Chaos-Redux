# Event033 temporary output contract audit, 2026-10-07

Disposition: `unresolved` caller repairs required, with this bounded read-only audit delivered for parent review.
Authority is the parent's explicit 2026-10-07 instruction to audit the remaining Event033 helper ABI and write this one new handoff.
No gameplay implementation of the Humanitarian retirement proposal is authorized or performed.
Only this file is written, with no source, test-file, other documentation, asset, workbook, role, game, log or Git mutation.

## Outcome and ownership

Six remaining fault families cover 19 observed helper-return consumption boundaries under the repository's conservative temporary-variable ABI.
The concrete owner repairs are caller storage declarations for warning facts, severe-impact facts, operation-family selection, front-marker anchors, nested superstorm-marker outputs and localisation tooltip getters.
No new helper architecture, public meter, saved-field replacement, tuning change, event target or gameplay design change is needed.
The operation-family repair is the first priority because the selected family controls paid operation row binding and completion scheduling.
The report and GUI repairs follow without changing their authored facts or presentation layout.

The parent's region patch is excluded from the new findings.
The parent reports 28 repaired returns: 16 region-cursor callers, two front-result callers, three selector callers with two outputs each, and seven candidate-weight callers, plus the regular-to-temporary retry-candidate correction.
The parent reports 160 cold-frame/native-fixture cases with a negative control.
That test was not duplicated here, and its mandatory AA comparison remains parent/auditor-owned and pending.

## Source identity

The opening runtime source and the supplied immutable archive both hashed to `f0cb9c24b684b7cccd66e90adc7128bf68b2db29b859b3e302c7d8a96f50766d`.
The archive is `docs\plans\033_acid_rain_plans\validation\probability\current_2026_10_07\sources\common\scripted_effects\033_acid_rain_effects.txt`.
The parent's reported region patch hashed to `e19bde24b2da80812558d5155631f36fdc093f6d2d292683b670963a84687b51`, independently verified during this audit.
The runtime subsequently changed to `556f36480beb40cd43bd1c061b804cf1f6ef90426741541fb2ad3d9b9a73db56` while the parent continued work.
That latest hash was verified before the final frame replay and source-reference refresh, and its warning/impact caller omissions still existed.
Runtime line references below use that latest hash.
No acceptance or balance result is inferred from either runtime hash change.

| File | Verified SHA-256 |
| --- | --- |
| `common\scripted_effects\033_acid_rain_effects.txt` | `556f36480beb40cd43bd1c061b804cf1f6ef90426741541fb2ad3d9b9a73db56` |
| `common\scripted_effects\033_acid_rain_achievement_effects.txt` | `256d6a5b22675343cde0775f219b645520455f236fb28a744d5218bcf89e1e68` |
| `common\scripted_effects\033_acid_rain_preparedness_effects.txt` | `1f6d6534ab595972e3ffa6d8a509e25c9bd04db87043a0db02549f824f422fa6` |
| `common\scripted_effects\033_acid_rain_gui_effects.txt` | `24b1c3767bdc82094e37c602f297ea71e92637f7b758aff9ceec3615cf1ef64c` |
| `common\scripted_effects\033_acid_rain_aftermath_effects.txt` | `2805a9af30ac54e332fb0ec09136c62c232f1b57083df9bee2cedebd6fcae09c` |
| `common\scripted_effects\033_acid_rain_cxt_effects.txt` | `35867e2dd578320882675703f283b02d0dcc4e583106e775d788df29c535b49b` |
| `common\scripted_triggers\033_acid_rain_triggers.txt` | `f2ec10e0cc2c3894dd2caf03d877cc62a8a4637e8bd60437d48314afb12ebaa7` |
| `common\scripted_triggers\033_acid_rain_achievement_triggers.txt` | `d811d87b3bc1e4e299f5a257213aa71af5539ff1518f85b7933c089cd141ee75` |
| `common\scripted_localisation\033_acid_rain_scripted_localisation.txt` | `0c9bbd39cfce6cf8c28417424efc18522e8bea97170f571661cf107e10402894` |
| `common\scripted_guis\033_acid_rain_scripted_guis.txt` | `6f04ffdc4596f6ce54ece1c0f87de7edd7aa2b8021bb915f9712836cc1893903` |
| `common\on_actions\033_acid_rain_on_actions.txt` | `41419cc70f8e5068f609d5802b7510a77f11c4f716722a9bfc6647a36feb6d05` |
| `events\033_acid_rain.txt` | `d56087f8f0a8db8ec705c0894da2682c254b5bda238df589f75b16242a5657e4` |

Recheck hashes before applying repairs because the checkout is shared and active.
The previous Humanitarian handoff remains an unresolved dependency and is not edited by this audit.

## ABI rule and audit method

The relevant rule is `chaos-redux-events`, Helper output lifetime, and offline Data structures lines 435-443, particularly line 440.
On a helper call, the conservative model clones the caller's temporary storage into a new frame and remembers the names already present.
On return, only modifications to those inherited names propagate back.
Names first created in the returning helper are discarded.
This applies at every nested scripted-effect or scripted-trigger boundary, including an outer wrapper that must forward a child's result.
Merely reading a missing variable as zero does not establish caller-owned temporary storage.

Temporary variables are unscoped across native scope changes within the current effect chain.
They do not become `ROOT` or `PREV` fields.
Normal `set_variable` outputs and flags persist on their actual subject and are tracked separately.
A saved-state sink inside the helper does not require the caller to retain that helper's private temporary scratch.
Input envelopes consumed inside a helper are also distinct from results consumed after its return.

The read-only lexical inventory covered 394 Event033 effect/trigger definitions and 918 calls to those definitions across owned files and exact current caller blocks.
Caller discovery included Event033 events, on-actions, scripted GUI and scripted localisation, plus only matching current blocks in shared dispatchers.
The scan produced 179 possible missing-storage rows after including nested consumer inputs.
Those rows were navigation aids, rather than execution evidence.
Future overwrite, private scratch, durable saved sinks and inherited outer storage eliminated many warnings.
Localisation consumers were checked separately against their actual substitutions in `localisation\english\033_acid_rain_l_english.yml:273-278`, because a parser of script commands alone cannot see those uses.

## Confirmed remaining contract defects

`confirmed_missing` means the current caller path consumes the result without locally declaring or receiving the required temporary storage from its current callers.
The failure is confirmed against the mandated conservative return model, not claimed as observed native game execution.

| ID and status | Exact caller and helper | Consumed temporary outputs | Minimal owner repair and effect |
| --- | --- | --- | --- |
| A1 `confirmed_missing`, two boundaries | `acid_rain_commit_front_region` at runtime line 1942 and `acid_rain_prepare_front_warning` at 2193 call `acid_rain_prepare_warning_report:1718-1732`. Their state/controller loops then invoke `acid_rain_send_front_warning_report`. | `acid_rain_warning_report_key`, `acid_rain_warning_arrival_days` | Initialize both to `constant:acid_rain_runtime.zero` in each consuming caller before the prepare call. The helper fills both. This preserves distinct visit keys and actual arrival days when country report facts are saved. |
| A2 `confirmed_missing`, one boundary | `acid_rain_apply_state_pulse:3229` calls `acid_rain_prepare_severe_impact_report:3246-3274`, then enters CONTROLLER and calls `acid_rain_send_severe_impact_report`. | `acid_rain_impact_episode_key`, `acid_rain_impact_end_day`, `acid_rain_impact_evacuation_status` | Initialize these three in the pulse caller immediately before preparation. Zero is suitable storage initialization because the helper assigns its end-day default and status on entry. The episode-key gate must see the real positive identity, and `acid_rain_fire_severe_impact_report` must receive the real status/end day. |
| A3 `confirmed_missing`, one boundary | `acid_rain_open_operation` at preparedness line 1029 calls `acid_rain_resolve_operation_family:958-966`, then reads its result at 1041 and binds/schedules national rows. `acid_rain_start_action` does not supply this storage before its `acid_rain_open_operation` call at 1170. | `acid_rain_op_family` | Initialize to zero inside `acid_rain_open_operation` before the resolver. The zero branch is for state evacuation/recovery operations, while national actions require the actual nonzero family. This fixes the local selector without changing payment or operation design. |
| A4 `confirmed_missing`, three boundaries | `acid_rain_gui_project_front_1`, `_2`, `_3` call `acid_rain_gui_set_region_anchor:690-728` at GUI-effect lines 590, 619, 648, then write persistent marker positions. | `acid_rain_gui_anchor_x`, `acid_rain_gui_anchor_y` | Initialize both in each front projector before the anchor helper. The coordinates are consumed inside the projector, so a new outer refresh API is unnecessary for these front calls. |
| A5 `confirmed_missing`, four nested boundaries | `acid_rain_gui_refresh_read_only` calls `acid_rain_gui_project_superstorm_marker:666-686` at 340, 357, 374 and immediately reads its outputs. The marker helper calls `acid_rain_gui_set_region_anchor` at 669 and forwards coordinates. | `acid_rain_gui_marker_shown`, `acid_rain_gui_anchor_region`, `acid_rain_gui_anchor_x`, `acid_rain_gui_anchor_y` | Initialize all four in the refresh frame before each marker call. That inherited x/y storage also reaches the nested anchor helper. Fixing only the inner helper leaves all outer results discarded. Document the public marker's four required caller-owned outputs. |
| A6 `confirmed_missing`, eight boundaries | `GetAcidRainRegion1Tooltip` through `GetAcidRainRegion7Tooltip` use `acid_rain_gui_load_region_tooltip` in scripted-localisation lines 488, 493, 498, 503, 508, 513, 518. `GetAcidRainPreparednessTooltip` uses `acid_rain_gui_load_preparedness_tooltip` at 544. | Ten region outputs and fourteen Preparedness outputs listed below | Initialize every consumed getter output directly in each `text.trigger` before its scripted-trigger call. Keep `acid_rain_gui_tt_region` as the existing input. Do not replace these values with saved fields or inline invented values. |

The 19 observed missing boundaries can be resolved through 18 consuming caller edits because A5's three complete outer envelopes provide the nested anchor storage too.
An explicit x/y declaration inside the marker helper is optional defensive self-containment, but it cannot replace the three outer declarations.

A1's frame replay stores warning key zero and arrival days zero without the declarations, against key seven and nine days with them.
A2's replay emits no impact report when the episode key disappears, against one report for severe episode nine with caller storage.
A3's six national action variants resolve to zero after return without caller storage, against the authored family IDs 1, 2, 2, 3, 4 and 5 with storage.
Do not interpret absent family output as legitimate evacuation/recovery selection.

The ten A6 region outputs are `acid_rain_gui_tt_eligible`, `acid_rain_gui_tt_touched`, `acid_rain_gui_tt_untouched`, `acid_rain_gui_tt_status`, `acid_rain_gui_tt_front`, `acid_rain_gui_tt_active`, `acid_rain_gui_tt_visit`, `acid_rain_gui_tt_quota`, `acid_rain_gui_tt_severe`, and `acid_rain_gui_tt_days`.
The fourteen Preparedness outputs are `acid_rain_gui_tt_shelter_tier`, `acid_rain_gui_tt_water_tier`, `acid_rain_gui_tt_medical_tier`, `acid_rain_gui_tt_transport_tier`, `acid_rain_gui_tt_shelter_points`, `acid_rain_gui_tt_water_points`, `acid_rain_gui_tt_medical_points`, `acid_rain_gui_tt_transport_points`, `acid_rain_gui_tt_shelter_max`, `acid_rain_gui_tt_water_max`, `acid_rain_gui_tt_medical_max`, `acid_rain_gui_tt_transport_max`, `acid_rain_gui_tt_max_tier`, and `acid_rain_gui_tt_preparedness_max`.
The helper definitions are in `common\scripted_triggers\033_acid_rain_triggers.txt:2113-2124,2129-2152`.
These are real localisation consumers, including status selection by `GetAcidRainRegionTooltipWeather`, rather than unused temporary bookkeeping.

## Reviewed non-findings and safe boundaries

`verified_local_storage` means the actual consuming caller initializes the field before the child call.
`verified_inherited_storage` means current outer callers supply storage that reaches every required nested boundary.
`saved_sink` means the helper publishes durable normal variables/flags inside its own frame, so private temporary retention is unnecessary.
`private_or_overwritten` means the named scratch is never consumed as that child's returned value.
`no_current_consumer` is not permission to remove the helper.

| Surface and status | Exact relevant contract |
| --- | --- |
| Episode cap, `verified_local_storage` | `acid_rain_calculate_mortality_profile` initializes `acid_rain_cap_baseline_people` and `acid_rain_cap_applied_people` before `acid_rain_load_episode_cap_ledger`, currently runtime lines 2768-2770. They are consumed inside the profile, so no additional outer cap-output initialization is needed. |
| Mortality request, `verified_local_storage` | `acid_rain_apply_state_pulse` initializes `acid_rain_pulse_applied_request` and `acid_rain_unprotected_requested_people` before `acid_rain_calculate_mortality_profile:3111`. It also initializes `state_civilian_population_loss_applied` and `state_civilian_population_loss_result` before the exact shared population helper at 3123. This is ABI evidence only, not native population or balance proof. |
| Measured damage, `verified_local_storage` | Runtime damage processing initializes `acid_rain_damage_observed` and `acid_rain_damage_target_applied` before the twelve selected-building calls at 3541, 3546, 3551, 3556, 3561, 3566, 3571, 3576, 3581, 3586, 3591, 3596. `acid_rain_damage_selected_building_measured` initializes `acid_rain_damage_read_damaged` and `acid_rain_damage_read_undamaged` before nested/meta reads at aftermath lines 190-198. Normal before/after building records remain state-owned. |
| Floor conversion, `verified_local_storage` and `private_or_overwritten` | `acid_rain_floor_value` is assigned by each consumer before `acid_rain_floor_consequence_component`. `acid_rain_floor_unrounded` is private to that helper and replaced on each call. Its later lexical occurrences are not a returned output. |
| Front quota, `saved_sink` | `acid_rain_calculate_front_goal:1355-1390` publishes `global.acid_rain_front_target_goal_entries` and `global.acid_rain_region_first_visit_target_entries`. Dwell timing reads those saved arrays, rather than requiring the private `acid_rain_front_goal` temporary after return. |
| Dwell timing, `saved_sink` | `acid_rain_initialize_front_visit_timing:2076` commits its min/max/deadline results into the existing durable front date arrays. Private dwell rolls and deadline scratch do not need outer return storage. No timing or quota weight change is proposed. |
| Date conversions, `verified_local_storage` | A dedicated source walk checked all 68 `chaosx_convert_days_to_date_offset` and `chaosx_convert_date_offset_to_days` calls in owned effect/trigger files. The respective `chaosx_date_offset` or `chaosx_date_days` output has caller-owned temporary storage before every call. This checks lifetime storage, not date arithmetic, callback delivery or elapsed-time behavior. |
| Normal report facts, `saved_sink` | Departure, arrival, casualty, dissipation, weakest-component and strongest-component helpers store their country report fields with `set_variable`. For example, `acid_rain_store_report_weakest_component:1762` and `_strongest_component:1790` are not transient return APIs. Forecast reports also store facts in the recipient country before dispatch. A1/A2 are the missing temporary preparation seams feeding those durable sinks. |
| Project/action quote refresh, `verified_inherited_storage` | Preparedness `acid_rain_refresh_country_project_quotes:234-275` and `acid_rain_refresh_country_action_quotes:505-557` declare the quote outputs and `acid_rain_component_quote` before loaders and display publishers. Their eight base project quote fields and thirteen action-loader fields survive the nested calls. |
| Display quote warning rows, `verified_inherited_storage` | `acid_rain_store_project_cost_display:1700` has four display-loader calls and `acid_rain_store_action_cost_display:1734` has eleven. Each publisher currently has only its matching quote refresher as a caller. The refreshers' quote/component storage reaches `acid_rain_load_display_*_row`, `acid_rain_finalize_loaded_quote` and all eight `acid_rain_quote_component` calls. The lexical missing-local-declaration warnings are not current-path defects. Direct new callers would need the same documented envelope. |
| Quote affordability/payment, `verified_local_storage` | `acid_rain_prepare_current_row_quote:1117-1224` initializes its quote/target/component envelope, and transaction callers initialize forwarded outputs. Project/action starts declare `acid_rain_quote_payment_success` before `acid_rain_debit_loaded_quote`. The debit helper declares both CBRN motorized debit outputs and each consumed `universal_cost_payment_result` before their owner helpers. AI reserve and motorized-stock predicates similarly declare consumed local fields. This does not certify pricing, resources or payment rollback. |
| Stored action quote loader, `no_current_consumer` | `acid_rain_load_stored_action_quote:564-578` has no exact `= yes` caller in current `common`/`events` source. Do not add speculative callers or patch its API as part of this task. |
| Operation achievement view, `saved_sink` | `acid_rain_load_operation_achievement_view:1000-1023` writes normal `acid_rain_033_achievement_active_action_*` fields on the paying country. Its family input is supplied by the national completion event or by the state operation path's explicit zero. This is distinct from A3's missing resolver output during operation opening. |
| Achievement recording/evaluation, `saved_sink` | Runtime pulse, forecast, closure, recovery, action and warning bridges construct their `acid_rain_033_input_*` envelopes and consume them inside the bridge into normal ledgers/flags. The achievement trigger file has no temporary setter return family. `acid_rain_033_input_generation` being recreated by a later bridge is not consumption of an earlier helper's lost output. |
| Achievement deadlines, `saved_sink` | `acid_rain_033_achievement_schedule_deadline:2508-2555` stores due date, generation and scheduling flag before queuing its event. Its private candidate and delay temporaries are consumed inside that helper. Callback at 2559-2571 rebuilds its own input generation. `acid_rain_project_country_obligations` follows the same persistent obligation-clock pattern. |
| Humanitarian watermark, `verified_local_storage` | The retained parent repair at aftermath 614-679 forwards `famine_adapter_result` into caller-owned `acid_rain_humanitarian_result`, and the tier caller declares it before consumption. Mortality/evacuation callers do not consume that returned result. The separate source ledger/proof/retirement problem remains unresolved. |
| GUI publication/CXT/entry callers, `saved_sink` or input-only | GUI counters/cards are normal presentation globals. Event and on-action consumers read normal runtime fields, flags, or arrays, rather than incidental scratch created by `acid_rain_start_runtime` or a projection helper. CXT registration's temporary extension token is an input consumed before its wrapper returns. No extra return defect is established there. |

The safe rows are scoped to current call paths and the output-lifetime question.
They do not close broader achievement, quota, payment, source-retirement, AI, visual or live-game gates.

## Meaningful frame replay

An in-memory read-only Node runner parsed current helper bodies and executed 37 isolated cases.
No runner or test fixture file was created, and the parent's region test was not invoked.
The model used separate temporary call frames and separate normal STATE, COUNTRY and global maps.
It copied only caller-preexisting temporary names back on helper return.
In the severe-report case, preparation ran in STATE scope and report publication ran in COUNTRY scope.
It did not prefix temporary variables with a subject or flatten them into normal saved storage.

| Cases | Observed conservative-model result |
| --- | --- |
| Six national action variants, missing vs initialized output, 12 cases | Missing family output returns zero for all six. Initialized storage returns 1, 2, 2, 3, 4, 5. |
| Warning preparation plus actual report consumer, 2 cases | Missing outputs publish key 0/days 0. Initialized outputs publish key 7/days 9. |
| Severe preparation plus actual send/fire helpers, 2 cases | Missing outputs emit no report. Initialized outputs emit one report with evacuation status 2. |
| Seven region anchors, missing vs initialized x/y, 14 cases | Missing coordinates return 0/0. Initialized coordinates match the authored pairs 201/83, 350/126, 368/61, 220/115, 385/175, 148/74, 125/138. |
| Nested superstorm marker, 3 cases | No storage and inner-only storage both lose outer marker results. Complete outer storage returns marker 1 at 201/83. |
| Region/Preparedness tooltip getters, missing vs initialized output envelopes, 4 cases | Missing envelopes retain 0 of 10 and 0 of 14 fields. Initialized envelopes retain all ten and fourteen, including touched count 37 and shelter tier 3. |

All 37 assertions passed, including the assertions that current missing-storage calls fail to retain their outputs.
That is defect reproduction plus caller-storage controls, not a production-fix pass.
The runtime file hash for the final replay was `556f36480beb40cd43bd1c061b804cf1f6ef90426741541fb2ad3d9b9a73db56`.
Date conversion was explicitly stubbed to nine days and `country_event` was only recorded in memory.
Full payment/open-operation execution, native arithmetic limits, ROOT/FROM authority, route/building behavior, actual tooltip rendering, save/reload and HOI4 execution were not modelled.
The source walk of 68 date-return sites is separate static evidence, not part of those 37 executions.

## Minimal parent implementation sequence

1. Add the zero `acid_rain_op_family` declaration at preparedness `acid_rain_open_operation` before the resolver, then check all six national families and the intentional zero-family state actions through the actual opening path.
2. Add the two warning declarations at both runtime callers and the three impact declarations in the pulse gateway. Verify new visit/episode, same-visit/episode repetition, registry-overflow warning key and severe/superstorm status cases without changing report cadence or authored fact selection.
3. Add two anchor declarations in each front projector and the complete four-output superstorm envelope at all three refresh callers. Retain the nested return negative control so an inner-only repair cannot be accepted.
4. Add the ten-field region getter envelope in each of the seven localisation triggers and the fourteen-field Preparedness getter envelope in its trigger. Verify nonzero counts/tiers and the clear, approaching, front-over-region and global status selections using the real localisation consumers.
5. Document the exact caller-owned output fields/defaults on the existing helper comments or matching owner documentation, then rerun relevant source-frame tests against refreshed hashes. The parent owns code/docs changes beyond this new handoff.

Keep existing inputs and cursor values intact while adding storage declarations.
Do not clear quote inputs or reset saved operation/achievement data as an ABI repair.
Do not turn these findings into a broad runtime rewrite.
No constants, tuning values, event targets, new helpers or cleanup mechanics are proposed.
Any weighted behavioral comparison remains with the existing probability owner and its frozen baseline, with no claim that the pending AA comparison has passed.

## Primary references and MCP evidence

All new MCP calls used explicit workspace `mod_chaos_redux_ea3b2d67c2c0`.
Connected schemas for reference context/search/read, source lookup, GUI inspection and event inspection were inspected.
No helper-expansion, job, native-task, version or health capability was assumed.
The current regular read-only routes returned results, so prior under-load timeout history is not reported as a current blanket outage.

`hoi4.reference_context`, event surface, returned installed Effects and offline Data structures but omitted Event modding, Effects, Triggers, Scopes, On actions, Localisation and extra installed source sections at limit two.
No complete context coverage is claimed.
Targeted `hoi4.reference_search(set_temp_variable)` found the installed effect and trigger sections.
Revision-bound reads returned offline `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md:435-443`, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, and installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md:7820-7827`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
The wiki read states caller-predefined temporary storage survives scripted-helper modification, while helper-created storage can disappear on return and temporaries are unscoped.
The installed read confirms temporary assignment accepts variables/math expressions in any scope.
The precise helper-return cleanup behavior remains the repository's conservative contract, rather than a newly measured engine guarantee.

`hoi4.source_lookup(acid_rain_load_episode_cap_ledger)` returned its complete, unshadowed definition at aftermath 144-168, workspace-index revision `25c3ef3692804e173ab7ffd16fb78b39af3b70c9b4179b0f81758e5ae2cd75af`.
Its reference coverage was incomplete: zero returned references, `referencesComplete = false`, and `unresolvedReferenceCount = 20077`.
The actual consumer was therefore traced directly, not inferred absent from that result.
The warning helper's bounded source-location lookup returned owner/chain information at 1716-1730, revision `b3c9d8e44c4224f086da03b5070ad7d5777a9af388fbef2bd9829f6d8e86f483`, but no expanded definition body.
Those location lines precede the later runtime's two-line shift to 1718-1732, so the final report uses the directly hashed current source.

The first GUI request without a scenario was rejected with MCP `-32602`, `windowName and scenario must be provided together`.
The corrected inspection used `acid_rain_world_window` with declared scenario `event033_helper_abi_audit` and returned `GUI_INSPECTED`, shared revision `f899db6892afd7fe199224b116f6b34c83f3e216fc5e407dd0fc861ab25164ab`, 160 inspected elements, no skipped source and fidelity counts including 63 unresolved and 22 unsupported entries.
The generated scenario ID was `event033_helper_abi_audit-generated-1`.
Reported warning families include unresolved dynamic text, unresolved animation fallback, clipping and non-positive sizes, which are not repaired or visually accepted by this ABI audit.
The complete GUI/visual review remains with its owner.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f33a25d9c382bad3c28c5b8edb013b69fd8e7d8fe868638a877ea4aca20e8a71/148f5fe99ad6004b03384324af776a5dd2ab95b29394ed41a18405517cb23f10/gui-inspect.f899db6892afd7fe.json`, declared size 2047093 bytes.

The bounded event lint selected `chaosx.nr33.47`, depth one/nodes three/edges four/helpers off.
It returned `EVENT_INSPECTED_PARTIAL`, revision `3c38803347d1f19442342fda0bfb3f88c4990c503d8ad25cb418cd0226caf472`, graph hash `0997806f144fa4388a25221761a9c6f5339e7ced88e8d7677bd0ef0ab5d49ee7`, focused analysis, zero helpers and zero blocking diagnostics.
The linked report's header explicitly has `complete = false`.
It does not establish helper-lifetime or whole-system lifecycle coverage.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/71a14045be19d96062787c3ab2fcfda91286fb3dab6654cea3a70bc47e20b0f1/c2e865df077d61343f1aeea259c97598619443a687c58fa14a97364d2e9f12cf/event-lint-3c38803347d1.json`, declared size 2066342 bytes.

Both artifact resources allowed bounded initial byte reads with range `[0,3000)` and `complete = false`, retaining a continuation at offset 3000.
Only those initial ranges were retrieved in this bounded ABI task, so no complete artifact byte-count/hash verification or full visual/lifecycle evidence is claimed.
The source-model ABI cases remain separate from MCP source graph and scenario coverage.
No rewrite, render or compare is claimed for a code change, because this subagent applied none.

## Completion and limits

Completed: source identity checks, broad owned-definition/current-caller inventory, concrete consumed-output/forwarding trace, 68 local date-output storage checks, 37 conservative helper-frame cases, matching read-only MCP/reference calls, and this one handoff.
Unimplemented: A1-A6 owner fixes, their full gateway/localisation validation and final parent acceptance.
Unresolved outside this task: Humanitarian source proof/retirement, the region patch's AA comparison, full event completion gates and native runtime behavior.
No simplification or fallback was implemented.
Files changed by this subagent: only `docs\plans\033_acid_rain_plans\subagent_handoffs\helper_output_contract_audit_2026_10_07.md`.
Skills used: `chaos-redux-events` and `chaos-redux-subagents`, with no skill creation or update.
