# Event 032 ordinary preparation localisation handoff

Disposition: implemented source patch, pending parent review and engine evidence.
Acceptance basis: the parent explicitly assigned the four ordinary preparation cost rows, human selector prose, cooldown tooltip names, and the subsequent persistent failure-reason and precision-readiness additions on 2026-10-03.
This handoff does not claim Event 032 completion.

## Files changed

- `common\scripted_localisation\032_missiles_localisation.txt`
- `localisation\english\032_missiles_decisions_l_english.yml`
- `docs\plans\032_missiles_plans\subagent_handoffs\032_ordinary_preparation_localisation_2026-10-03.md`

No gameplay files, workbook, CSV exports, assets, or unrelated localisation were edited.
No Git operations, desktop control, GUI operations, or game launch ran.

## Cost display and source contract

| Preparation | Command power | Fuel | Support equipment | Conventional reserve | Special reserve |
| --- | ---: | ---: | ---: | ---: | ---: |
| Precision | 8 | 250 | 40 | 1 | 2 |
| Strategic | 15 | 450 | 80 | 2 | 3 |
| Saturation | 25 | 700 | 140 | 4 | 5 |
| Counterforce | 15 | 450 | 40 | 2 | 3 |

Before: each blocked inline row made all three fees red, even when only one resource or reserve escrow was unaffordable.
The fourth Operational Reserve amount was always yellow.
After: each fee resolver compares its own live stock against the corresponding constant, so only an unpaid amount turns red.
Both native normal and blocked aliases call the same per-amount resolvers.
Inline rows retain three cost types.
The fourth Operational Reserve escrow remains explicit in the full tooltip through the existing registered `GFX_032_missiles_operational_reserve_texticon`.
No fifth cost or image asset was added.

Command checks read `command_power`, fuel checks read `fuel_k` against 0.250/0.450/0.700, and support checks read `num_equipment@support_equipment`.
Temporary display amounts derive from those same constants, with fuel multiplied by 1000 for display.
Reserve colors compare the live Operational Reserve to the base or special-inclusive constants using `missiles_preparation_has_special_payload`.
They do not use the preview cache as an affordability threshold.
The displayed reserve amounts now use `missiles_preparation_precision_reserve_display`, `missiles_preparation_strategic_reserve_display`, `missiles_preparation_saturation_reserve_display`, and `missiles_preparation_counterforce_reserve_display`, calculated in each selected text trigger.
The parent retains its normal preview caches, but the four reserve cost resolvers no longer consume them.
Parent availability and debit logic remains authoritative and unchanged.

Cancellation and timeout text now calls the persistent `missiles_last_preparation_failure` resolver.
All enum values 0–10 have mappings, with an absent or unknown value falling back to “No preparation failure has been recorded.”
The text states that uncommitted Operational Reserve returns, while command power, fuel, and support equipment spent on preparation remain spent.
It does not claim complete chemical or biological physical-payload escrow.

## New scripted localisation functions

- `GetMissilesPreparationFailureName`
- `GetMissilesCommandLowCost`
- `GetMissilesCommandStandardCost`
- `GetMissilesCommandHighCost`
- `GetMissilesFuelLowCost`
- `GetMissilesFuelStandardCost`
- `GetMissilesFuelHighCost`
- `GetMissilesSupportLowCost`
- `GetMissilesSupportStandardCost`
- `GetMissilesSupportHighCost`
- `GetMissilesPrecisionReserveCost`
- `GetMissilesStrategicReserveCost`
- `GetMissilesSaturationReserveCost`
- `GetMissilesCounterforceReserveCost`

Fee call sites are the twelve existing ordinary preparation cost keys, covering each row, blocked alias, and tooltip.
Reserve call sites are the four full cost tooltips.
The failure resolver is called by `missiles_preparation_cancelled_tt` and `missiles_preparation_timeout_tt`.

## Prose review

- Vagueness: the country selector now names `[FROM.GetName]`, and the state selector names the chosen state instead of saying “freeze this exact state.”
The failure messages identify the failed programme, target, objective, launch site, payload custody, readiness, command, reserve, deadline, or order condition.
- Bloat: replaced “several strategic objects” and abstract selection language with installations and direct choices.
The header retains three main values plus one existing context line.
- Obvious explanation: removed the repeated explanation that clearing a target does not modify a committed operation, and moved the actual restriction into the clear-target description.
- Repetition: compact shared fee resolvers replace independently maintained literal fee amounts.
The full cost tooltips keep one consistent refund statement.
- Overcomplication: expanded unexplained CBRN terminology into chemical, biological, and nuclear facilities, and replaced “bind” and “freeze” with choose/select.
- Style repair: removed em dashes and sentence semicolons from the inspected header/context passages.
No update-history language, new lore, or secret route revelations was introduced.

No sourced or attributed quotations occur in the assigned preparation, selector, header, and failure passages.
No quotations were changed.
Existing icons, numeric formatting, country/state scope tokens, and reserve cache references were preserved.
New scoped tokens and formatted temporary values were added intentionally.
Thresholds in the header mirror current constants: generic readiness 50, precision readiness 60, and command control 40.

## Meaningful validation

An in-memory evaluator parsed the actual cost resolver definitions, shared preparation affordability triggers, and constants.
It evaluated 128 source scenarios: four preparations, conventional/special payloads, and all 16 combinations of sufficient/exact versus insufficient command, fuel, support, and reserve stocks.
All 512 component color selections matched individual affordability, and the aggregate gate matched the conjunction of those four components.
Fuel and fee display amounts matched the assigned 8/250/40, 15/450/80, 25/700/140, and 15/450/40 contracts.
This is source-model evidence, not executed HOI4 behavior.
A further 13 failure cases covered absent, 0–10, and unknown code 99, with the intended fallback.
The final explicit zero-code branch is equivalent to the tested fallback.

Task-specific key coverage checked 140 unique explicit tooltip/cost references from the current decisions, missions, operations effects, and operations triggers against English localisation, including native `_blocked` and `_tooltip` aliases.
No missing references were found.
All assigned scripted-localisation output keys and `This.GetMissiles...` calls resolve.
No duplicate keys exist in the assigned English file and no duplicate function names exist in the assigned scripted-localisation file.
There are no dollar-key aliases in the assigned English file.
The four previously missing cooldown flag names now have player-facing wording.
The localisation BOM was preserved.
No encoding concern was found in the patched English file.

Source inspection confirms all eight preparation cancellation/timeout paths call the parent's `missiles_cancel_preparation` helper.
The parent's failure recording precedes abort/cleanup.
The parent's precision readiness tooltip is wired in the decision source.
The new editable/general requirement keys still require the parent's source wiring at the last check.

## Parent wiring and unresolved evidence

Use `missiles_target_selection_editable_tt` for the clear/back availability checks:
`custom_trigger_tooltip = { tooltip = missiles_target_selection_editable_tt NOT = { has_country_flag = missiles_operation_active } }`.
Use `missiles_ordinary_preparation_requirements_tt` to wrap `missiles_country_can_prepare_operation = yes` in the four ordinary preparation availability blocks.
Keep the per-operation cooldown flags separately visible through their four newly localised names.
Keep affordability in its current hidden/shared checks.
Keep `missiles_precision_readiness_requirements_tt` on the precision-specific readiness condition.

Production GUI review, overflow/wrapping validation, runtime observation, and live failure-tooltip timing are outside the explicit assignment.
No visual fit claim is made.
The parent must review whether native cancellation/timeout tooltip evaluation observes the stored failure receipt after the helper runs, rather than a prior receipt while inspecting a running mission.
Fresh reserve display no longer depends on preview refresh after payload changes or evolution toggles.
Normal preview-cache lifecycle remains parent-owned and outside the repaired display contract.

The HOI4 reference/inspection routes were absent from the first tool inventory, then became exposed later in the same task.
Live `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.source_lookup`, and `hoi4.decision_inspect` requests were issued when exposed.
The reference-context call returned `OK` for workspace `mod_chaos_redux_ea3b2d67c2c0`, with no missing or omitted sources and no artifacts.
Its Localisation snapshot revision matched the local SHA-256 recorded below.
Search failed with MCP `-32603`: `UNKNOWN: unknown error, scandir 'C:\Users\klimp\AppData\Local\hoi4-agent-tools\state\request-capacity\43f52410ceeba65a\3'`.
Source lookup failed with the same error at request-capacity child `1`.
Decision inspect rejected the initial request with `-32602`: `Decision inspection requires declared scenarios at scenarios`.
The request was corrected by declaring `ordinary_precision_exact_fee_stock` for GER with 8 command power, 0.250 fuel_k, 40 support equipment, 1 Operational Reserve, 60 readiness, and 40 command control.
That fixture intentionally does not establish active launch-site or selected-target state, so even a returned result cannot prove complete availability.
The corrected decision-inspect request produced no final response during the bounded check, and its waiting orchestration cell was terminated.
Domain inspection therefore remains unresolved, with no scenario artifact or findings to report.
No scenario inspection result or usable artifact URI was produced.
These results show partial reference-route service health, not healthy domain inspection or engine validation.
The revision-bound reference-read request returned `OK` for installed `loc_formatter_documentation.md`, revision `1fbd9a031fd09100d79bac08dec3c16e19468f23516c5e67c67578156282af08`, lines 1–2.
That section contains only the heading, so it does not establish detailed rules.
The relevant detailed rules were read locally at the paths and lines below.
No source-only check is presented as equivalent MCP or engine evidence.
No standalone Technology Tree Viewer tool was present in the separately checked tool inventory, although `hoi4.tech_inspect`, `hoi4.tech_render`, and `hoi4.tech_compare` were exposed later.
Standalone viewer availability remains a package/capability gap in this session, with installed-package availability unverified.
No technology surface was edited or inspected.

Missing key list: none remaining in the bounded checks.
Duplicate key list: none in the assigned localisation file.
Scripted localisation issue list: none unresolved in source key/function coverage.
Dynamic text opportunities implemented: fee amounts and independent colors, reserve colors, selected country/state names, stored failure reason.
Dynamic opportunities remaining: native mission tooltip timing remains unverified, but the unread failure context line now exposes the persistent cause after a mission disappears.
Cross-surface mismatch repaired: header precision readiness, false saturation cancellation-loss implication, broad refund wording, and stale reserve amounts after live evolution toggles.
Catalog comparison was not performed because workbook review is outside this bounded task.
The final wording table below is the key-level handoff for `chaosx_spreadsheet_doc_worker` if any catalog field mirrors these passages.
No spreadsheet update is claimed.
No broader design-depth gap was invented and no expansion plan was written.
No simplifications were made to the assigned source implementation.
Parent final review is required.

## Local reference evidence

Local reads used the repository offline snapshot and installed documentation when reference routes were initially unavailable.
Line numbers are one-based.
SHA-256 hashes below identify the read revisions.

| Source | Lines read | SHA-256 |
| --- | --- | --- |
| `paradox_wiki\Localisation - Hearts of Iron 4 Wiki.md` | 658–691, 731–792 | `1A8F72362A34B4BB653186746B9FAE0B98E463205CB02F12CCF2C3D9CCD3A064` |
| `paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md` | 305–336 | `7713B9BCEE5F3818D63AAFBD45D18E812A9173A7C59AB238384B57DB60DB6162` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\scripted_localisation\00_scripted_localisation.txt` | 1–35 | `6F490E33736F4DC31568ADD5753A1AFDEF916F3993804FEBFBBE6D1583827587` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\script_concept_documentation.md` | 214–222 | `884BFE9F9207EA4B25B36B5129D0F77D11D4B2F7EB0592587767EC58D24930C7` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md` | 2110–2135 | `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\dynamic_variables_documentation.md` | 194–196, 385–387, 557–559 | `538525747F0C285062C9CE8DB14B4E07C3CF6BAC1013115FA4F57291CB4EBDDA` |

Skills applied: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`.
No skills were created or updated.

## Exact changed keys and final wording

| Key | Final value |
| --- | --- |
| `missiles_cost_precision_strike` | [This.GetMissilesCommandLowCost] [This.GetMissilesFuelLowCost] [This.GetMissilesSupportLowCost] |
| `missiles_cost_precision_strike_blocked` | [This.GetMissilesCommandLowCost] [This.GetMissilesFuelLowCost] [This.GetMissilesSupportLowCost] |
| `missiles_cost_precision_strike_tooltip` | [This.GetMissilesCommandLowCost] [This.GetMissilesFuelLowCost] [This.GetMissilesSupportLowCost]\n[This.GetMissilesPrecisionReserveCost] missiles reserved. Aborting returns uncommitted Operational Reserve. Command power, fuel, and support equipment remain spent. |
| `missiles_precision_preparation_cooldown` | Precision preparation crews are still occupied |
| `missiles_cost_strategic_barrage` | [This.GetMissilesCommandStandardCost] [This.GetMissilesFuelStandardCost] [This.GetMissilesSupportStandardCost] |
| `missiles_cost_strategic_barrage_blocked` | [This.GetMissilesCommandStandardCost] [This.GetMissilesFuelStandardCost] [This.GetMissilesSupportStandardCost] |
| `missiles_cost_strategic_barrage_tooltip` | [This.GetMissilesCommandStandardCost] [This.GetMissilesFuelStandardCost] [This.GetMissilesSupportStandardCost]\n[This.GetMissilesStrategicReserveCost] missiles reserved. Aborting returns uncommitted Operational Reserve. Command power, fuel, and support equipment remain spent. |
| `missiles_strategic_preparation_cooldown` | Strategic preparation crews are still occupied |
| `missiles_cost_saturation_barrage` | [This.GetMissilesCommandHighCost] [This.GetMissilesFuelHighCost] [This.GetMissilesSupportHighCost] |
| `missiles_cost_saturation_barrage_blocked` | [This.GetMissilesCommandHighCost] [This.GetMissilesFuelHighCost] [This.GetMissilesSupportHighCost] |
| `missiles_cost_saturation_barrage_tooltip` | [This.GetMissilesCommandHighCost] [This.GetMissilesFuelHighCost] [This.GetMissilesSupportHighCost]\n[This.GetMissilesSaturationReserveCost] missiles reserved. Aborting returns uncommitted Operational Reserve. Command power, fuel, and support equipment remain spent. |
| `missiles_saturation_preparation_cooldown` | Saturation preparation crews are still occupied |
| `missiles_cost_counterforce_strike` | [This.GetMissilesCommandStandardCost] [This.GetMissilesFuelStandardCost] [This.GetMissilesSupportLowCost] |
| `missiles_cost_counterforce_strike_blocked` | [This.GetMissilesCommandStandardCost] [This.GetMissilesFuelStandardCost] [This.GetMissilesSupportLowCost] |
| `missiles_cost_counterforce_strike_tooltip` | [This.GetMissilesCommandStandardCost] [This.GetMissilesFuelStandardCost] [This.GetMissilesSupportLowCost]\n[This.GetMissilesCounterforceReserveCost] missiles reserved. Aborting returns uncommitted Operational Reserve. Command power, fuel, and support equipment remain spent. |
| `missiles_counterforce_preparation_cooldown` | Counterforce preparation crews are still occupied |
| `missiles_program_management_category_desc_live` | §Y£GFX_032_missiles_operational_reserve_texticon Operational Reserve:§! [?missiles_operational_reserve\|0] weapons available for preparation. Aborting returns uncommitted missiles.\n§Y£GFX_032_missiles_launch_readiness_texticon Launch Readiness:§! [?missiles_launch_readiness\|0]/100. Ordinary operations need at least 50, precision strikes 60. Train crews to restore readiness.\n§Y£GFX_032_missiles_command_control_texticon Command Control:§! [?missiles_command_control\|0]/100. Operations need at least 40. Secure launch codes to restore control.\n\n[This.GetMissilesCategoryContextLine] |
| `missiles_category_context_guidance` | §YGuidance:§! [This.GetMissilesGuidanceGradeName]. Poor guidance increases drift and collateral risk. Recalibrate before choosing a crowded target. |
| `missiles_category_context_retaliation` | §YRetaliation:§! [This.GetMissilesCategoryRetaliationLine]. Verify the warning or stand down. Delegated orders can commit a response. |
| `missiles_select_target_country` | Target [FROM.GetName] |
| `missiles_select_target_country_desc` | Choose [FROM.GetName] as the enemy, then select an objective and target state. |
| `missiles_select_target_effect_tt` | Select an objective and target state in [FROM.GetName]. |
| `missiles_choose_strategic_profile_family_desc` | Target command, confirmed launch or special-payload facilities, or several installations in one state. |
| `missiles_choose_counterforce_profile_desc` | Select a confirmed missile, chemical, biological, or nuclear facility. Civilian intelligence on its controller must exceed 50%. |
| `missiles_select_target_state_desc` | Choose [FROM.GetName] for the selected objective. Prepare the strike after selecting the state. |
| `missiles_select_target_state_effect_tt` | Missile command retains [FROM.GetName] until the target is cleared or the operation finishes. If the state becomes invalid, choose another target. |
| `missiles_clear_target_desc` | Clear the selected enemy, objective, and state. Active launch orders must be aborted first. |
| `missiles_clear_target_effect_tt` | Clears the selected enemy, objective, and state. |
| `missiles_back_to_target_profiles_desc` | Keep the selected enemy and choose another objective. |
| `missiles_precision_readiness_requirements_tt` | Precision strikes require at least §Y60§! Launch Readiness. |
| `missiles_target_selection_editable_tt` | No missile operation is awaiting preparation or launch. |
| `missiles_ordinary_preparation_requirements_tt` | The missile programme needs an active launch site and no active operation or unresolved programme incident. Launch Readiness must be at least §Y50§! and Command Control at least §Y40§!. The launch crews must have completed their cooldown. |
| `missiles_preparation_cancelled_tt` | Preparation is cancelled. [This.GetMissilesPreparationFailureName]\nUncommitted Operational Reserve returns. Command power, fuel, and support equipment spent on preparation are not refunded. |
| `missiles_preparation_timeout_tt` | Preparation has expired. [This.GetMissilesPreparationFailureName]\nUncommitted Operational Reserve returns. Command power, fuel, and support equipment spent on preparation are not refunded. |
| `missiles_abort_prepared_operation_desc` | Stand down the launch crews and return uncommitted missiles to Operational Reserve. Preparation fees remain spent. |
| `missiles_abort_operation_effect_tt` | Uncommitted Operational Reserve returns. Command power, fuel, and support equipment spent on preparation are not refunded. |
| `missiles_saturation_barrage_preparation_mission_desc` | Crews are assembling a large salvo against the selected state. Cancelling returns uncommitted missiles, but preparation fees remain spent. |
| `missiles_preparation_failure_program` | The missile programme can no longer support this operation. |
| `missiles_preparation_failure_target` | The selected enemy or target state is no longer valid. |
| `missiles_preparation_failure_objective` | The target state no longer contains a suitable installation for the selected objective. |
| `missiles_preparation_failure_site` | The assigned launch sites are no longer available for this operation. |
| `missiles_preparation_failure_payload` | Missile command can no longer authorise or secure the selected payload. |
| `missiles_preparation_failure_readiness` | The launch crews no longer meet this operation's readiness requirement. |
| `missiles_preparation_failure_command` | Command Control has fallen below the required level. |
| `missiles_preparation_failure_reserve` | The reserved missiles no longer cover the launch order. |
| `missiles_preparation_failure_deadline` | The preparation deadline has passed. |
| `missiles_preparation_failure_order` | The launch order is no longer valid. |
| `missiles_preparation_failure_none` | No preparation failure has been recorded. |
| `missiles_preparation_command_low` | £command_power §Y[?missiles_preparation_command_low_display\|0]§! |
| `missiles_preparation_command_low_blocked` | £command_power §R[?missiles_preparation_command_low_display\|0]§! |
| `missiles_preparation_command_standard` | £command_power §Y[?missiles_preparation_command_standard_display\|0]§! |
| `missiles_preparation_command_standard_blocked` | £command_power §R[?missiles_preparation_command_standard_display\|0]§! |
| `missiles_preparation_command_high` | £command_power §Y[?missiles_preparation_command_high_display\|0]§! |
| `missiles_preparation_command_high_blocked` | £command_power §R[?missiles_preparation_command_high_display\|0]§! |
| `missiles_preparation_fuel_low` | £fuel_texticon §Y[?missiles_preparation_fuel_low_display\|0]§! |
| `missiles_preparation_fuel_low_blocked` | £fuel_texticon §R[?missiles_preparation_fuel_low_display\|0]§! |
| `missiles_preparation_fuel_standard` | £fuel_texticon §Y[?missiles_preparation_fuel_standard_display\|0]§! |
| `missiles_preparation_fuel_standard_blocked` | £fuel_texticon §R[?missiles_preparation_fuel_standard_display\|0]§! |
| `missiles_preparation_fuel_high` | £fuel_texticon §Y[?missiles_preparation_fuel_high_display\|0]§! |
| `missiles_preparation_fuel_high_blocked` | £fuel_texticon §R[?missiles_preparation_fuel_high_display\|0]§! |
| `missiles_preparation_support_low` | £support_equipment_text_icon §Y[?missiles_preparation_support_low_display\|0]§! |
| `missiles_preparation_support_low_blocked` | £support_equipment_text_icon §R[?missiles_preparation_support_low_display\|0]§! |
| `missiles_preparation_support_standard` | £support_equipment_text_icon §Y[?missiles_preparation_support_standard_display\|0]§! |
| `missiles_preparation_support_standard_blocked` | £support_equipment_text_icon §R[?missiles_preparation_support_standard_display\|0]§! |
| `missiles_preparation_support_high` | £support_equipment_text_icon §Y[?missiles_preparation_support_high_display\|0]§! |
| `missiles_preparation_support_high_blocked` | £support_equipment_text_icon §R[?missiles_preparation_support_high_display\|0]§! |
| `missiles_preparation_precision_reserve` | £GFX_032_missiles_operational_reserve_texticon §Y[?missiles_preparation_precision_reserve_display\|0]§! |
| `missiles_preparation_precision_reserve_blocked` | £GFX_032_missiles_operational_reserve_texticon §R[?missiles_preparation_precision_reserve_display\|0]§! |
| `missiles_preparation_strategic_reserve` | £GFX_032_missiles_operational_reserve_texticon §Y[?missiles_preparation_strategic_reserve_display\|0]§! |
| `missiles_preparation_strategic_reserve_blocked` | £GFX_032_missiles_operational_reserve_texticon §R[?missiles_preparation_strategic_reserve_display\|0]§! |
| `missiles_preparation_saturation_reserve` | £GFX_032_missiles_operational_reserve_texticon §Y[?missiles_preparation_saturation_reserve_display\|0]§! |
| `missiles_preparation_saturation_reserve_blocked` | £GFX_032_missiles_operational_reserve_texticon §R[?missiles_preparation_saturation_reserve_display\|0]§! |
| `missiles_preparation_counterforce_reserve` | £GFX_032_missiles_operational_reserve_texticon §Y[?missiles_preparation_counterforce_reserve_display\|0]§! |
| `missiles_preparation_counterforce_reserve_blocked` | £GFX_032_missiles_operational_reserve_texticon §R[?missiles_preparation_counterforce_reserve_display\|0]§! |

## Parent-review repair: live evolution toggles and retained failure context

Disposition: implemented source repair, pending parent final review.
Acceptance basis: the parent's follow-up explicitly required live temporary reserve amounts, an unread failure context branch, and the shared fuel conversion constant.
Parent review confirmed that temporary arithmetic inside scripted-localisation triggers is valid, so that pattern was retained.

Changed functions in this repair: `GetMissilesPrecisionReserveCost`, `GetMissilesStrategicReserveCost`, `GetMissilesSaturationReserveCost`, `GetMissilesCounterforceReserveCost`, `GetMissilesFuelLowCost`, `GetMissilesFuelStandardCost`, `GetMissilesFuelHighCost`, and `GetMissilesCategoryContextLine`.
Changed existing keys: `missiles_preparation_precision_reserve`, `missiles_preparation_precision_reserve_blocked`, `missiles_preparation_strategic_reserve`, `missiles_preparation_strategic_reserve_blocked`, `missiles_preparation_saturation_reserve`, `missiles_preparation_saturation_reserve_blocked`, `missiles_preparation_counterforce_reserve`, and `missiles_preparation_counterforce_reserve_blocked`.
Added key: `missiles_category_context_preparation_failure`.

Final added wording: "§YLast preparation:§! [This.GetMissilesPreparationFailureName] Uncommitted Operational Reserve returns. Preparation fees remain spent."

Before the repair, reserve colors used a fresh gate but their numeric fragments consumed a saved preview that could still contain a special surcharge after a live toggle.
Every normal and blocked reserve path now assigns its own temporary display variable directly from the relevant base or special-inclusive constant.
The parent's current `missiles_preparation_has_special_payload` requires `missiles_special_warheads_active`, so disabling all five evolutions while retaining the selected payload makes new conventional ordinary-operation quotes use base reserve costs.
The four normal cache variables are neither read nor changed by these display resolvers.
No payment, normal-variable mutation, payload-copy effect, or active operation receipt was changed by this subagent.
Frozen special-receipt invalidation remains parent-owned, with no automatic downgrade introduced.

The context resolver checks warning, rogue command, and programme incident first, then unread preparation failure when `missiles_operation_active` is absent, then guidance.
This preserves one context slot and surfaces the last recorded cause after the native mission disappears.
Current parent source sets `missiles_preparation_failure_unread` while recording the failure and clears it on accepted new preparation preflight, retaining the historical code and IDs.
The new branch does not clear history or the unread flag.

All six multiplication sites in the three fuel resolvers use `constant:missiles_preparation_cost.fuel_units_per_k`, including their blocked branches.
The parent added that constant with value 1000.
The script comment cites installed trigger documentation and the actual vanilla temporary-arithmetic precedent.

The repair's source-model regression evaluated 640 cost scenarios, yielding 2560 component amount/color checks.
Those cases cover all four preparations, conventional/chemical/biological/nuclear/thermonuclear retained selections, enabled special evolution versus all five evolution disable flags, and all 16 sufficient/exact versus insufficient resource combinations.
Saved preview costs were deliberately set to 999 and temporary display storage to -999 to expose stale-value reuse.
All quoted amounts and colors matched the current shared affordability predicates, including disabled-evolution retained-special selections that quote 1/2/4/2 base reserve rather than 2/3/5/3 special reserve.
This cost-quote evidence does not claim that the saturation action is visible when its evolution is disabled, or prove full target/site eligibility.
Sixteen context scenarios covered unread/read status, active/inactive operation, and warning/rogue/incident/no crisis.
They selected the intended single context branch.
No key or resolver coverage issue or duplicate key was found.
Source-model evidence remains distinct from runtime and production rendering.

Prose-quality change in this repair: the concrete last-failure context replaces silence after mission removal.
Its refund sentence reuses the established distinction between returned missile escrow and spent preparation fees.
No vague, bloated, repetitive, overcomplicated, or prohibited-style sentence was introduced.
All resource icons, colors, integer formatters, failure resolver calls, and sourced quotations were preserved.
The eight cache tokens were intentionally replaced by their temporary display tokens.
No sourced quotations occur on this repaired surface.

Additional installed evidence: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md`, lines 6455–6469 and 7482–7501, same SHA-256 as the reference table.
Additional vanilla precedent: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\scripted_localisation\SEA_PRC_scripted_loc.txt`, `GetFiveYearPlanGoalCivFactoriesText`, lines 37–51, SHA-256 `387CCED4840EF6988E3BA6AF4A72B99DC0BA71E82201CFCACD2F875FE5D64A0E`.
The vanilla precedent assigns and multiplies a temporary variable inside `text.trigger`.
Its inline numeric `localization_key` form was not copied, because this task requires literal localisation-key branches.
Offline wiki Localisation lines 678–684 describe temporary values remaining available to the selected key and first-matching-branch selection.

No new GUI, runtime, Git, spreadsheet, or gameplay operation ran.
No simplification was made.
The prior MCP/domain evidence limitations remain recorded above.
The follow-up `hoi4.reference_search` request for `set_temp_variable` produced no final response during this bounded check, and its waiting orchestration cell was terminated.
No new MCP artifact or service-health claim is made for this repair.

## Final validation after native temporary-quote contract repair

Disposition: handoff evidence updated, pending parent final review.
Acceptance basis: the parent removed named-argument and dollar-parameter helper calls, retained the numerical cost contract, and explicitly requested revalidation against the current source.
Only this handoff changed in this pass.
The two localisation files, gameplay source, and all other files were left untouched.
The original evaluator's named-argument support is superseded by the native evaluator described here.

Current `common\scripted_triggers\032_missiles_preparation_cost_triggers.txt` was read directly before testing.
Each of its four wrappers assigns these five temporary inputs from constants and invokes `missiles_can_afford_preparation = yes`:

- `missiles_preparation_command_quote`
- `missiles_preparation_fuel_quote`
- `missiles_preparation_support_quote`
- `missiles_preparation_base_quote`
- `missiles_preparation_special_quote`

The shared helper reads those temporary fields, validates positive command/fuel/support/base quotes, applies inclusive stock comparisons, and selects base or special reserve using the unchanged active-selection helper.
These are fresh temporary payment inputs, separate from the normal preview caches and the scripted-localisation temporary display fields.
The evaluator now rejects dollar-parameter tokens and named helper-argument blocks instead of interpreting them.
It separates normal and temporary storage and conservatively discards temporary fields first created inside a returning helper.
It retains changes to temporary fields preinitialized by the caller.

The updated source regression reran all 640 cost scenarios against the actual native wrappers, with 2560 component amount/color checks and no disagreements.
The scenarios retain all four preparations, five payload selections, enabled versus all-five-disabled evolutions, and all sixteen resource sufficiency combinations.
It also evaluated 1280 helper-call cases by testing each scenario twice, once with fresh temporary quote storage and once with all five caller-owned fields poisoned to -999.
Every wrapper recalculated its inputs before the shared affordability check.
Fresh wrapper-local quote fields were discarded after return in the conservative model, and preinitialized fields received the new values.
No normal variable changed.
Deliberately stale normal preview values of 999 did not affect displayed amounts or affordability.
The previous sixteen context tests remain applicable because neither context resolver nor its flags changed in this repair.
This is source-model evidence, not HOI4 execution, native UI inspection, or balance approval.

Read source revisions for this final pass:

| Source | SHA-256 |
| --- | --- |
| `common\scripted_triggers\032_missiles_preparation_cost_triggers.txt` | `E4EE30D2C87985947B5A2148486A30241712292C491672453648BCD78E87CDB3` |
| `common\script_constants\032_missiles_constants.txt` | `77BEB588E0B8CEDF8E45459F4790A58234B6EA67C5286C5037C0C7396A80DDEE` |
| `common\scripted_triggers\032_missiles_triggers.txt` | `D09F35F7BD6EA7717CBB497A93EE0872D3CF029510112AABCA162B732E8788AA` |
| `common\scripted_localisation\032_missiles_localisation.txt` | `CFEA347FDC61F2B05C871F2E110293981A8F92F354DB735E23FC274D1DDE5D27` |
| `localisation\english\032_missiles_decisions_l_english.yml` | `08EF41E921811F7E7FE5E6CD3EA4FC4EF3591FAB0292A5125ED93CFC4AEB580A` |

Installed `documentation\triggers_documentation.md` lines 7482–7501 and 6455–6470 were reread.
Vanilla `common\scripted_localisation\SEA_PRC_scripted_loc.txt` lines 38–54 were reread as the temporary-trigger precedent.
Their revisions are the hashes already recorded above.

Changed localisation keys or functions in this pass: none.
No player-facing prose, quotations, icons, formatting, or dynamic tokens changed.
No new missing-key, duplicate-key, encoding, prose, or cross-surface issue was introduced.
The parent will wire the requirement tooltips after all reviews, so their wiring remains parent-owned and pending.
No gameplay, GUI, runtime, spreadsheet, or Git operation ran.
No simplification was made.
Prior MCP and runtime evidence limits remain unchanged, and no full-event completion is claimed.
