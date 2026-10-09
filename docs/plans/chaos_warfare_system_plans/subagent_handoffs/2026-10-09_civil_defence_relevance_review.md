# Civil Defence Relevance and Automatic Priority Audit

Disposition: `unresolved`; this is a read-only source audit and leaves the accepted implementation for the parent to integrate.

## Scope and acceptance basis

The audit is limited to Civil Defence reveal, automatic real-stock civilian issue, state priority, and the linked AI/cost contracts.
The parent owns the protection and continuing-death implementation surfaces, so no gameplay, GUI, localisation, shared documentation, index, or commit changes were made.

Accepted spec 13 states that military and civilian mask issue is automatic and spends actual stock, while Civil Defence decisions appear for a real threat, outbreak, contamination, or response need (`docs/specs/chaos_warfare_system_specs/specs/13_2026_09_20_accepted_cbrn_overhaul.md:21`).
The accepted paid occupied-population programme reserves the exact quoted respirator amount at selection, caps delivery to that reservation, and returns unused stock on cancellation or invalidation (`.../specs/13_2026_09_20_accepted_cbrn_overhaul.md:25,37`).
The accepted historical exception is Britain’s separately sourced 1939 civilian issue; other countries start with zero civilian coverage absent country-specific evidence (`.../specs/13_2026_09_20_accepted_cbrn_overhaul.md:100` and `.../corrections/2026-09-26_historical_civilian_start_cleanup.md:3-11`).
The source decision prompt lists emergency distribution, hospital protection, shelters, and occupied supply, and says AI should prioritize frontline armies and high-value civilian states (`docs/specs/chaos_warfare_system_specs/prompts/chaos_warfare_decision_mission_prompt.md:35-52`).
The task instruction also requires automatic issue to prioritize military and threatened civilian states without bypassing the paid noncore occupied programme, and requires coefficients and rates to remain unchanged unless separately accepted.

## Issues ordered by severity

1. **High — permanent attack history keeps the public category and automatic civilian issue eligible.** `cbrn_civil_defence_category_visible` includes `cbrn_country_has_public_chemical_emergency` (`common/scripted_triggers/cbrn_protection_triggers.txt:27-35`), and the Civil Defence category has `visible_when_empty = yes` (`common/decisions/categories/cbrn_protection_categories.txt:19-23`). The public helper includes `has_enemy_used_chemical_weapons` (`.../cbrn_protection_triggers.txt:63-73`), which includes the permanent `cbrn_confirmed_chemical_attack_victim_history` flag (`common/scripted_triggers/cbw_triggers.txt:194-201`). That history flag is set without a duration (`common/scripted_effects/cbrn_consequence_effects.txt:524-528`) and no clear call was found in `common/`; the separate timed contamination expiry clears the state contamination fields (`events/cbrn_chemical_delivery_events.txt:45-61`). The helper’s other branches are temporary retaliation authorization and use-history on an existing enemy; unlike those, the permanent victim receipt can keep the empty category visible indefinitely after recovery and peace.

2. **High — the same history branch can continue to authorize real-stock issue in clean states.** `cbrn_country_needs_civilian_mask_issue` directly includes `has_enemy_used_chemical_weapons` (`common/scripted_triggers/cbrn_protection_triggers.txt:158-168`). On an existing protection maintenance cycle, that need calls `cbrn_complete_priority_distribution_program` (`common/scripted_effects/cbrn_protection_effects.txt:2416-2439`). The maintenance routine spends military service and issue first, then civilian filter service and issue (`.../cbrn_protection_effects.txt:2427-2439`), so the military-first order is already explicit. The civilian branch only consumes if stock remains, a selected state is below the current effective-coverage target, and it passes the receiver gate; this is not a free-equipment loop, but a victim-history-only country can still refill a clean capital or other eligible core after the incident has ended.

3. **High — automatic state issue does not prioritize local exposure and skips some contaminated cores.** `cbrn_complete_priority_distribution_program` tries the capital first and then every other controlled state (`common/scripted_effects/cbrn_protection_decision_effects.txt:173-190`). Its receiver requires a controlled ROOT core, a population, a distribution gap, no active project, and a “priority protection value” (`common/scripted_triggers/cbrn_protection_triggers.txt:404-457`). That value is limited to capital, victory-point fortification, industry, air/naval base, or supply node (`.../cbrn_protection_triggers.txt:386-402`); it does not include an active alert or contamination. Thus a contaminated low-value rural core is deterministically skipped by automatic issue, while an undercovered clean capital is attempted before a threatened state. Other noncapital receivers are visited in `every_controlled_state` order without a threat ranking; source review does not establish their engine iteration order.

4. **Medium — the category does not explicitly recognize active state response effects.** Raid alerts default to 7 days and can range from 1 to 30 days (`common/script_constants/cbrn_system_constants.txt:1096-1098`); the four protective response flags `cbrn_hospitals_utilities_secured`, `cbrn_civilians_moved_to_shelters`, `cbrn_chemical_alarm_sounded`, and `cbrn_industry_ordered_to_continue` are each set for 14 days (`common/script_constants/cbrn_system_constants.txt:967`, `common/scripted_effects/cbrn_immediate_response_cost_effects.txt:252-257`, and `common/scripted_effects/cbrn_protection_decision_effects.txt:455-473`). The category trigger tests alerts, contamination, enemy capability, outbreak, and the active occupied programme, but not these timed response flags (`common/scripted_triggers/cbrn_protection_triggers.txt:27-35`). If the alert ends before a 14-day response flag and no other reveal condition remains, the category condition becomes false while the response effect remains active. A narrow visibility repair should preserve this real “ongoing response” case without relying on permanent victim history.

5. **Medium — the AI’s civilian-gap signal and the automatic receiver disagree.** `cbrn_country_has_priority_civilian_protection_gap` sees every populated controlled core below the priority coverage target (`common/scripted_triggers/cbrn_protection_triggers.txt:174-180`), but the automatic receiver adds the priority-value filter (`.../cbrn_protection_triggers.txt:452-457`). The same country-level gap feeds `cbrn_country_below_mask_ai_target` and `cbrn_country_should_produce_masks` (`.../cbrn_protection_triggers.txt:202-246`). AI production can therefore respond to an undercovered rural core that its automatic issue loop cannot serve, especially when the public/history condition remains true.

6. **Low — outbreak-only visibility can show an empty Civil Defence category, but no code-backed reason supports automatic mask issue for biological effects.** `has_active_biowarfare_outbreak` is a direct category reveal condition and checks controlled states for biological contamination (`common/scripted_triggers/cbrn_protection_triggers.txt:27-35` and `common/scripted_triggers/cbw_triggers.txt:23-30`). The chemical civilian-issue trigger does not include this outbreak predicate (`.../cbrn_protection_triggers.txt:158-168`). A bounded source search of biological and biowarfare effects/events found no references to `cbrn_civilian_mask_effective_coverage`, civilian-mask stock variables, or `gas_mask_equipment`. Keep outbreak reveal if accepted, but do not spend civilian mask stock solely because a biological outbreak is active unless a game-code protection benefit is separately accepted and implemented.

## Category lifecycle and cognitive-load notes

A fresh country with no current chemical capability, alert, contamination, outbreak, active occupied programme, or incident history does not meet the Civil Defence reveal trigger.
An active alert or live chemical contamination reveals the category through the public emergency helper and starts the automatic civilian issue need.
A current enemy chemical capability independently reveals the category through `cbrn_country_faces_enemy_chemical_capability` (`.../cbrn_protection_triggers.txt:145-156`).
A biological outbreak independently reveals it, but does not start civilian mask issue.
An active occupied-population transaction is represented by `cbrn_civilian_distribution_program_active`; it is set after the exact reservation is committed and cleared by `cbrn_occupied_clear_committed_program` (`common/scripted_effects/cbrn_occupied_transaction_effects.txt:162-165,220-225`).
A pending British 1939 receipt remains a separate automatic-issue exception and is cleared after the historical issue completes (`common/scripted_effects/chaosx_startup_history_effects.txt:1113-1114` and `common/scripted_effects/cbrn_protection_effects.txt:2576-2578`).

There are nine decision definitions in `cbrn_civil_defence_category` (`common/decisions/cbrn_protection_decisions.txt:365-613`).
During a chemical alert, up to five immediate response action families can be visible: emergency state masks, hospitals/utilities, shelters, chemical alarm, and keeping industry operating.
One of the ordinary or sale occupied-population programme variants may appear when an eligible noncore state and its purchase variant match, bringing the acute primary-action count to six; the ordinary and sale variants are mutually exclusive by their variant triggers.
Two record-reconciliation decisions are conditional recovery tools rather than primary response choices.
No scripted GUI is attached to this category, and no GUI layout or clipping claim is made.
No missions or mission IDs are defined in the audited decision/category files, so active mission count, owner, region, and mission outcome quality are not applicable here.
The player-facing cost rows show dynamic amounts and explain their immediate effect; this audit found no raw uncategorized meter or unrelated counter dump.

## Costs, requirements, tooltips, and localisation

| Decision family | Distinct spendable types | Displayed cost tokens |
| --- | ---: | --- |
| `cbrn_emergency_state_mask_distribution` | 2 | `£pol_power`, `£GFX_archetype_gas_mask_equipment_medium` |
| `cbrn_supply_occupied_population` and `_sale` | 3 | `£pol_power`, `£GFX_archetype_gas_mask_equipment_medium`, `£civ_factory` |
| `cbrn_protect_hospitals_and_utilities` | 3 | `£pol_power`, `£GFX_archetype_gas_mask_equipment_medium`, `£support_equipment_text_icon` |
| `cbrn_move_civilians_to_shelters` | 3 | `£pol_power`, `£support_equipment_text_icon`, `£GFX_train_texticon` |
| `cbrn_sound_chemical_alarm` and `cbrn_keep_industry_operating` | 1 each | Native political-power cost |
| `cbrn_reconcile_occupied_mask_records` and `cbrn_reconcile_export_shipment_records` | 0 | No spendable cost |

Every reviewed player-facing custom cost uses resource texticons, and the largest current cost is three distinct spendable types.
The occupied-program row states that political power is spent, respirator crates are reserved at selection, factories remain assigned, and unused stock returns on early end or invalidation (`localisation/english/cbrn_protection_l_english.yml:76-83`).
The sale variant shares this cost contract and does not add a fourth or hidden cost (`common/decisions/cbrn_protection_decisions.txt:440-479`).
The emergency distribution row shows political power plus actual respirator crates and states that the shipment is capped by national stock (`.../cbrn_protection_l_english.yml:68-74`).
Response tooltips describe state consequences and duration; no literal resource label or cost-count violation was found.
The main tooltip mismatch is category presence after peace/history, not cost wording.

## AI validity, routes, cleanup, and exploit risk

No changed weights are proposed, and no AI score or normalized odds are claimed by this audit.
Do not replace `has_enemy_used_chemical_weapons` globally: its permanent history branch is also used by doctrine unlocks, chemical research and strategy logic, production signals, ability gates, ideas, and unrelated CBRN AI profiles.
`cbrn_country_has_public_chemical_emergency` itself also feeds CBRN abilities, country profiles, research modifiers, regiment support, and AI posture triggers; changing that shared contract globally would require a wider audit.

The local emergency-state mask decision still targets only states with an active exact alert or live contamination (`common/scripted_triggers/cbrn_protection_triggers.txt:467-492`), even when its country-level `visible` gate is broadened by historical use.
The occupied receiver is explicitly noncore and requires state-level alert or contamination, while priority/full receivers are core-only (`.../cbrn_protection_triggers.txt:452-499`).
This preserves the accepted paid occupied-population and protective-aid contracts and prevents the automatic core loop from delivering free noncore coverage.
Do not remove or weaken the exact quote, reservation, escrow, cooldown, refund, or cancellation checks as part of a category/priority repair.
The UK 1939 receipt is the only accepted initial civilian issue exception and must remain explicit.

The weighted/strategy surfaces to reassess if a parent patch changes these gates are `cbrn_emergency_state_mask_distribution`, `cbrn_supply_occupied_population`, `cbrn_supply_occupied_population_sale`, `cbrn_country_below_mask_ai_target`, `cbrn_country_should_produce_masks`, and any other existing consumers of `has_enemy_used_chemical_weapons` or `cbrn_country_has_public_chemical_emergency`.
A saved emergency-decision baseline already exists at `docs/plans/chaos_warfare_system_plans/subagent_handoffs/cbrn_emergency_state_mask_distribution_probability_baseline.md`, with scenario set `cbrn_emergency_state_mask_distribution_baseline_2026-09-25` and fixture cases `stock-none`, `stock-exact`, `stock-above`, `eligible-alert`, `stale-alert`, `pp-below`, `pp-exact`, and `pp-above`.
That evaluation is partial, `poolComplete = false`, unresolved on target/state/equipment/payment inputs, and score-only with `normalizedProbability = false`; it is not a click probability or eligibility proof.
The post-edit compare handoff records one failed MCP request because it supplied unsupported `sourceRevision` and `sourceHash` fields; do not repeat that same request, and reuse the saved scenarios/results through `chaosx_ai_probability_auditor` before any weighted patch.
Existing occupied/export probability results are under `docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-10-03_cbrn_occupied_export_probability/finalhandoff.md` and remain partial; do not rerun unchanged scenarios or retune weights.

The history flags are intentional historical receipts, so cleanup should correct their use in current-relevance gates rather than deleting the history.
The historical 1939 UK issue clears its pending receipt after issue; the occupied transaction active flag is cleared by its dedicated completion/recovery helper.
The automatic priority issue is capped by real stock and the current coverage gap; no free stock loop is present, but history-only demand can direct future stock into clean eligible cores.

## Scenario matrix for parent review

| Scenario | Current source result | Required repair check |
| --- | --- | --- |
| Fresh country, no CBRN signal | Category hidden; no civilian issue demand. | Keep hidden unless a current threat or outbreak appears. |
| Active exact chemical alert | Category visible; local response decisions can target the alerted state; army stock issue precedes civilian issue. | Confirm threatened core distribution runs before any clean fallback core target. |
| Live chemical contamination | Category visible; civilian issue need true; exact contaminated states may receive emergency manual distribution. | Test low-value rural core inclusion and stock exhaustion. |
| Biological outbreak only | Category visible; automatic civilian issue need false; no biological mask consumer found in current outcome code. | Preserve category reveal without mask-stock debit. |
| Expired contamination, peace, permanent victim-history only | Category still visible even if empty; civilian issue need remains true. | Category and automatic issue should no longer be kept active by victim history alone. |
| Ongoing occupied programme | Category visible through `cbrn_civilian_distribution_program_active`; exact paid transaction remains in progress. | Keep reserved stock, factory hold, refund, and cleanup semantics intact. |
| Ongoing state response after alert expiry | A response flag can remain for 14 days after the default 7-day alert ends; the category trigger does not inspect response flags. | Preserve reveal while any accepted response effect remains active, then close after the last one expires. |
| Contaminated rural core with no priority-value building | Country need true, but automatic state gate false; emergency targeted state decision remains the manual route. | Include genuinely threatened core states in the automatic priority pass. |
| Clean undercovered capital plus a threatened core | Capital is attempted first if it passes the current gap/value gates. | Threatened-state pass should precede clean strategic fallback without changing target percentages or coefficients. |
| Contaminated occupied noncore state | Automatic priority receiver false by core check; paid occupied receiver can be true through exact local alert/contamination. | Keep noncore issue inside the paid programme only. |
| Constrained stock with military shortage | Current maintenance sequence services/issues military masks first, then civilian service/issue from stock left over. | Preserve that order and reuse the existing 90-crate competition case in `2026-10-09_automatic_protection_repair.md`. |

## Recommended bounded fixes

Keep `has_enemy_used_chemical_weapons` and `cbrn_country_has_public_chemical_emergency` unchanged for their broad consumers.
Use a separate, narrow Civil Defence visibility condition that accepts live controlled-state alert/contamination, a current credible chemical threat, biological outbreak, active occupied programme, and active timed response flags.
Preserve an existing enemy’s confirmed-use history as a current credible threat, and keep the finite `cbrn_retaliation_authorized` window separate if the accepted “ongoing response” term includes it (`common/scripted_effects/cbrn_diplomacy_effects.txt:126-130`).
Use a separate current-demand predicate for automatic civilian issue so permanent victim history alone does not trigger it; retain the explicit UK historical receipt, a current enemy's confirmed-use history, and current threat/incident conditions.
Make the automatic state priority pass serve alerted or contaminated controlled cores first, including populated rural cores, before any clean capital/industrial fallback; retain the existing core-only automatic contract, coverage target, equipment costs, filters, and all current coefficients.
Align `cbrn_country_has_priority_civilian_protection_gap` with the actual receiver classes so AI mask-production demand does not promise automatic service to a state the receiver rejects.

## Validation and tool limits

Source review covered the current trigger, decision-category, decision, effect, occupied-transaction, localisation, and biological outcome paths.
The offline Decision modding visibility-when-empty section was read at `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:186-189`, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`; it states that `visible_when_empty = yes` makes a category visible without a visible child decision.
Installed documentation `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/_documentation.md:1-46`, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`, states that `visible` gates display and that `available` controls whether a visible decision can be taken.
`hoi4.source_lookup` returned the `has_enemy_used_chemical_weapons` definition at `mod:common/scripted_triggers/cbw_triggers.txt:194-202`, workspace index revision `163cae7cc23eec31546f0ec001693b84d2c1676fabac170c0e4379f2f7f41cc5`, but returned zero indexed references and `referencesComplete = false`; direct `rg` caller searches were used instead.
One oversized reference-context question, one wrong-section `reference_read` position, and one `source_lookup` request over the `maxDefinitions` limit were corrected within the shared retry allowance; the corrected context and source-lookup calls succeeded, and the wrong-section read was replaced by the correct visibility-section read.
No `hoi4.decision_inspect`, probability MCP, GUI renderer, script validator, engine, game process, or log action was used for this read-only audit; the existing partial probability artifacts are recorded above and no weights changed.
The existing automatic-protection source test report covers the military-first stock competition, but it does not cover category history visibility or contaminated-rural priority selection.

No source file was changed by this audit; its only output is this handoff.
The audited source SHA-256s at the time of review were `cbrn_protection_triggers.txt` 5E073AD69E3040B63C232B013304730A899000CF3B26ABB2D03ECEC99AA425C0, `cbw_triggers.txt` C8F3720E297F2D09A05E4F044C4FE388C13E1860F89D232CC07F5EE96C208B43, `cbrn_protection_effects.txt` B8A45B830F4A2E10C0CE4E5B4CBA35CFE527E22DAA63F0A3A734BC758D176A8C, `cbrn_protection_decision_effects.txt` BEE3A3F81726BD9093E1244CE1BCC7C61D45081BB522994E3B2C5D56B627F506, `cbrn_protection_categories.txt` 16EE2B82C125C66D3B716760F1401DA675A81A8769AB8065775F465DB4366C8C, and `cbrn_protection_decisions.txt` D263E1803A5DBD2B760F78A4F79A29EDFDD910B770B79A78600220327AFDC790.

## Skills used

Applied `chaos-redux-decisions-missions`, `chaos-redux-events`, and `chaos-redux-subagents` for the decision audit, event-linked source review, and bounded handoff.
No skill was created or updated.
`chaos-redux-scripted-gui` was not needed because the category has no scripted GUI attachment and this task made no layout change.
