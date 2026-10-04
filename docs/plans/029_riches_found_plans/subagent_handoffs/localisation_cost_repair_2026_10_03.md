# Event 029 cost localisation repair, 2026-10-03

Disposition: implemented for all 92 original cost recipes and the owner's subsequent Predatory Prosperity source change.
Engine and visual cost-row evidence remain unresolved.

Acceptance basis: the parent assigned only COST `GetRichesFoundCost*` definitions and `riches_found_cost*` strings, then directed that four-resource recipes show every resource in the compact row.
That explicit four-value instruction takes precedence over the decisions skill's general three-value inline guideline.
The parent retains gameplay, AI, account mechanics and account prose, category descriptions, non-cost decision prose, GFX, spreadsheets, commits, and integration.
No gameplay source, AI, spreadsheet, GFX, achievement alias, or Git index was changed by this worker.
No game was launched.

## Changed files

- `common/scripted_localisation/029_riches_found_scripted_localisation.txt`: 24 original cost selectors now invoke the matching authoritative inclusive component, one new cost-only sacrifice selector follows the owner's physical payment family, and one adjacent cost comment describes the four-value contract.
- `localisation/english/029_riches_found_decisions_l_english.yml`: 45 compact rows restore their fourth resource, and all 92 full cost tooltips name every resource.
- This handoff.

`localisation/english/029_riches_found_l_english.yml` needed no cost-type label changes.
The 48 existing `riches_found.cost.<type>.<available|blocked>` component strings and their numbers, colours, icons, and constant tokens remain intact.
All 92 `riches_found_cost_<action>_blocked` aliases remain unchanged and resolve through the component selectors.
Comparison against the captured working-file content confirms that non-cost YML content was preserved.
The worker made only targeted text patches and did not restore files from Git, preserving the shared tree and the achievement aliases from `01bc85ee3`.

## Changed selectors

| `GetRichesFoundCostPpHeavy` | `riches_found_cost_can_afford_pp_heavy` |
| `GetRichesFoundCostCommandStandard` | `riches_found_cost_can_afford_command_standard` |
| `GetRichesFoundCostSupportStandard` | `riches_found_cost_can_afford_support_standard` |
| `GetRichesFoundCostManpowerStandard` | `riches_found_cost_can_afford_manpower_standard` |
| `GetRichesFoundCostMotorizedStandard` | `riches_found_cost_can_afford_motorized_standard` |
| `GetRichesFoundCostPpStandard` | `riches_found_cost_can_afford_pp_standard` |
| `GetRichesFoundCostManpowerLight` | `riches_found_cost_can_afford_manpower_light` |
| `GetRichesFoundCostSupportLight` | `riches_found_cost_can_afford_support_light` |
| `GetRichesFoundCostInfantryHeavy` | `riches_found_cost_can_afford_infantry_heavy` |
| `GetRichesFoundCostFuelStandard` | `riches_found_cost_can_afford_fuel_standard` |
| `GetRichesFoundCostCommandHeavy` | `riches_found_cost_can_afford_command_heavy` |
| `GetRichesFoundCostInfantryStandard` | `riches_found_cost_can_afford_infantry_standard` |
| `GetRichesFoundCostMotorizedLight` | `riches_found_cost_can_afford_motorized_light` |
| `GetRichesFoundCostPpLight` | `riches_found_cost_can_afford_pp_light` |
| `GetRichesFoundCostManpowerEmergency` | `riches_found_cost_can_afford_manpower_emergency` |
| `GetRichesFoundCostTrainStandard` | `riches_found_cost_can_afford_train_standard` |
| `GetRichesFoundCostConvoyStandard` | `riches_found_cost_can_afford_convoy_standard` |
| `GetRichesFoundCostSupportHeavy` | `riches_found_cost_can_afford_support_heavy` |
| `GetRichesFoundCostManpowerHeavy` | `riches_found_cost_can_afford_manpower_heavy` |
| `GetRichesFoundCostConvoyHeavy` | `riches_found_cost_can_afford_convoy_heavy` |
| `GetRichesFoundCostTrainLight` | `riches_found_cost_can_afford_train_light` |
| `GetRichesFoundCostCommandLight` | `riches_found_cost_can_afford_command_light` |
| `GetRichesFoundCostConvoyLight` | `riches_found_cost_can_afford_convoy_light` |
| `GetRichesFoundCostInfantryLight` | `riches_found_cost_can_afford_infantry_light` |

Each original selector's first branch is now `trigger = { riches_found_cost_can_afford_<type> = yes }`.
Its available and blocked output keys are unchanged.
This reuses the exact parsed gate instead of duplicating resource predicates or manpower conversions in another file.

New selector: `GetRichesFoundCostSacrifice`, COUNTRY scope with the decision's mine state in FROM.
It selects the industrial or human family from `riches_found_account_next_obligation` and uses the owner's state-scoped `riches_found_account_predatory_payment_is_valid` for available colour.
Blocked branches retain that family's actual amount.
The non-payable fallback says “No payable claim” and does not fabricate a payment.

Added keys and final wording:

- `riches_found_cost_sacrifice_industry_available`: `§Y[?constant:riches_found_account_terms.industrial_development_cost|0]§! Mine Development`
- `riches_found_cost_sacrifice_industry_blocked`: `§R[?constant:riches_found_account_terms.industrial_development_cost|0]§! Mine Development`
- `riches_found_cost_sacrifice_workers_available`: `§Y[?constant:riches_found_harm.predatory_prosperity_civilian_deaths|0]§! marked workers`
- `riches_found_cost_sacrifice_workers_blocked`: `§R[?constant:riches_found_harm.predatory_prosperity_civilian_deaths|0]§! marked workers`
- `riches_found_cost_sacrifice_unavailable`: `§RNo payable claim§!`

The parent's optional-symbol instruction permits concise literal family labels for this custom physical sacrifice.
No manpower icon was used for civilian population, and no GFX or invented icon was added.
The two-word label preserves the four-word inline text budget.

## Changed compact-row keys

Each key below formerly displayed the first three payments even though its tooltip and debit contained four.
Each now displays the same four helper calls, in the same order, as its full tooltip.
Other compact rows remain unchanged.

- `riches_found_cost_gilded_revoke_charter`
- `riches_found_cost_gilded_buy_back_district`
- `riches_found_cost_gilded_violent_nationalization`
- `riches_found_cost_account_pay_material`
- `riches_found_cost_account_predatory_prosperity`
- `riches_found_cost_curse_stabilization_diversification`
- `riches_found_cost_gold_replace_workforce`
- `riches_found_cost_gold_military_control`
- `riches_found_cost_gold_quarantine`
- `riches_found_cost_gold_seal_depths`
- `riches_found_cost_gold_controlled_access`
- `riches_found_cost_gold_destroy_confiscated_material`
- `riches_found_cost_demons_permanent_seal`
- `riches_found_cost_demons_evacuate_district`
- `riches_found_cost_demons_military_purge`
- `riches_found_cost_demons_scientific_assistance`
- `riches_found_cost_demons_controlled_exploitation`
- `riches_found_cost_armed_workers`
- `riches_found_cost_pay_train`
- `riches_found_cost_clear_barricades`
- `riches_found_cost_disarm_private_forces`
- `riches_found_cost_quarantine`
- `riches_found_cost_workforce_replacement`
- `riches_found_cost_seal_depths`
- `riches_found_cost_repair`
- `riches_found_cost_evacuation`
- `riches_found_cost_permanent_seal`
- `riches_found_cost_occupation_reopen`
- `riches_found_cost_occupation_replace_concession`
- `riches_found_cost_occupation_deny_mine`
- `riches_found_cost_curse_nationalize_extraction`
- `riches_found_cost_trade_access_infrastructure`
- `riches_found_cost_nationalize_with_compensation`
- `riches_found_cost_nationalize_without_compensation`
- `riches_found_cost_mine_police`
- `riches_found_cost_army_cordon`
- `riches_found_cost_camp_administration`
- `riches_found_cost_specialist_labor`
- `riches_found_cost_sanitation`
- `riches_found_cost_rail_spur`
- `riches_found_cost_port_route`
- `riches_found_cost_shaft_reinforcement`
- `riches_found_cost_processing_works`
- `riches_found_cost_housing`
- `riches_found_cost_drive_deeper`

## Changed full-tooltip keys

Each key below uses the same helper calls and constant amounts as its compact row.
The only additional text is the resource name: Political power, Command power, Manpower, Infantry equipment, Support equipment, Trucks, Fuel, Civilian trains, or Convoys.
No action title, requirement, consequence, or future route was copied into these tooltips.

- `riches_found_cost_demons_make_agreement_tooltip`
- `riches_found_cost_gilded_revoke_charter_tooltip`
- `riches_found_cost_gilded_buy_back_district_tooltip`
- `riches_found_cost_gilded_share_sovereignty_tooltip`
- `riches_found_cost_gilded_recognize_board_tooltip`
- `riches_found_cost_gilded_violent_nationalization_tooltip`
- `riches_found_cost_gilded_let_govern_tooltip`
- `riches_found_cost_account_close_tooltip`
- `riches_found_cost_account_bind_terms_tooltip`
- `riches_found_cost_account_pay_material_tooltip`
- `riches_found_cost_account_spend_authority_tooltip`
- `riches_found_cost_account_predatory_prosperity_tooltip`
- `riches_found_cost_curse_distribute_revenue_tooltip`
- `riches_found_cost_curse_stabilization_diversification_tooltip`
- `riches_found_cost_curse_tolerate_corruption_tooltip`
- `riches_found_cost_curse_private_interests_tooltip`
- `riches_found_cost_curse_independent_revenue_authority_tooltip`
- `riches_found_cost_gold_share_revenue_tooltip`
- `riches_found_cost_gold_replace_workforce_tooltip`
- `riches_found_cost_gold_military_control_tooltip`
- `riches_found_cost_gold_quarantine_tooltip`
- `riches_found_cost_gold_close_temporary_tooltip`
- `riches_found_cost_gold_seal_depths_tooltip`
- `riches_found_cost_gold_controlled_access_tooltip`
- `riches_found_cost_gold_destroy_confiscated_material_tooltip`
- `riches_found_cost_demons_permanent_seal_tooltip`
- `riches_found_cost_demons_evacuate_district_tooltip`
- `riches_found_cost_demons_military_purge_tooltip`
- `riches_found_cost_demons_religious_assistance_tooltip`
- `riches_found_cost_demons_occult_assistance_tooltip`
- `riches_found_cost_demons_scientific_assistance_tooltip`
- `riches_found_cost_demons_controlled_exploitation_tooltip`
- `riches_found_cost_armed_workers_tooltip`
- `riches_found_cost_pay_train_tooltip`
- `riches_found_cost_clear_barricades_tooltip`
- `riches_found_cost_truce_tooltip`
- `riches_found_cost_disarm_private_forces_tooltip`
- `riches_found_cost_temporary_closure_tooltip`
- `riches_found_cost_quarantine_tooltip`
- `riches_found_cost_workforce_replacement_tooltip`
- `riches_found_cost_seal_depths_tooltip`
- `riches_found_cost_repair_tooltip`
- `riches_found_cost_evacuation_tooltip`
- `riches_found_cost_permanent_seal_tooltip`
- `riches_found_cost_occupation_reopen_tooltip`
- `riches_found_cost_occupation_requisition_tooltip`
- `riches_found_cost_occupation_keep_administration_tooltip`
- `riches_found_cost_occupation_replace_concession_tooltip`
- `riches_found_cost_occupation_share_revenue_tooltip`
- `riches_found_cost_occupation_strip_equipment_tooltip`
- `riches_found_cost_occupation_deny_mine_tooltip`
- `riches_found_cost_curse_nationalize_extraction_tooltip`
- `riches_found_cost_local_revenue_tooltip`
- `riches_found_cost_central_revenue_tooltip`
- `riches_found_cost_stabilization_fund_tooltip`
- `riches_found_cost_audit_tooltip`
- `riches_found_cost_replace_administration_tooltip`
- `riches_found_cost_independent_revenue_authority_tooltip`
- `riches_found_cost_tolerate_patronage_tooltip`
- `riches_found_cost_concession_auction_tooltip`
- `riches_found_cost_exclusive_concession_tooltip`
- `riches_found_cost_offtake_tooltip`
- `riches_found_cost_trade_access_infrastructure_tooltip`
- `riches_found_cost_disclosure_tooltip`
- `riches_found_cost_publish_contract_tooltip`
- `riches_found_cost_nationalize_with_compensation_tooltip`
- `riches_found_cost_nationalize_without_compensation_tooltip`
- `riches_found_cost_buyout_tooltip`
- `riches_found_cost_renegotiate_contract_tooltip`
- `riches_found_cost_mine_police_tooltip`
- `riches_found_cost_private_guards_tooltip`
- `riches_found_cost_army_cordon_tooltip`
- `riches_found_cost_survey_tooltip`
- `riches_found_cost_claim_register_tooltip`
- `riches_found_cost_claim_freeze_tooltip`
- `riches_found_cost_recognize_local_claims_tooltip`
- `riches_found_cost_reserve_deposit_tooltip`
- `riches_found_cost_claims_court_tooltip`
- `riches_found_cost_camp_administration_tooltip`
- `riches_found_cost_license_traders_tooltip`
- `riches_found_cost_local_labor_tooltip`
- `riches_found_cost_specialist_labor_tooltip`
- `riches_found_cost_worker_cooperatives_tooltip`
- `riches_found_cost_sanitation_tooltip`
- `riches_found_cost_rail_spur_tooltip`
- `riches_found_cost_port_route_tooltip`
- `riches_found_cost_shaft_reinforcement_tooltip`
- `riches_found_cost_processing_works_tooltip`
- `riches_found_cost_housing_tooltip`
- `riches_found_cost_development_fund_tooltip`
- `riches_found_cost_drive_deeper_tooltip`
- `riches_found_cost_dividend_tooltip`

## Before, exact threshold, and after

All 24 original first branches used strict `>`.
At exactly the affordable amount, the decision gate could succeed but its component still displayed red.
The new selectors use the existing components' `greater_than_or_equals`, or the fuel component's exact `NOT = { has_fuel < ... }`, and select yellow at equality.
Below the amount they remain red.
Above it they remain yellow.
The parsed-source arithmetic checks covered one unit below, equality, and one unit above all 24 thresholds, with people converted to thousands for manpower.
They are source-model checks, not executed engine outcomes.

| Cost family | Checked player-visible thresholds | Gate reader |
| --- | --- | --- |
| Political power | 10, 25, 40 | `political_power` |
| Command power | 5, 10, 15 | `command_power` |
| Manpower | 100, 300, 600, 1,000 people | `manpower_k`, thresholds 0.1, 0.3, 0.6, 1.0 |
| Fuel | 300 | `has_fuel` with negated less-than |
| Infantry equipment | 100, 300, 600 | `num_equipment@infantry_equipment` |
| Support equipment | 25, 75, 150 | `num_equipment@support_equipment` |
| Trucks | 25, 75 | `num_equipment@motorized_equipment_1` |
| Civilian trains | 1, 3 | `num_equipment@train_equipment_1` |
| Convoys | 5, 15, 30 | `num_equipment@convoy_1` |

Example: the original Mine Police compact row omitted 75 support equipment.
It now shows 25 political power, 300 manpower, 300 infantry equipment, and 75 support equipment.
Its full tooltip names those same four resources.
At each exact reserve all four components select their available strings.

Train selectors previously checked the `train_equipment` archetype and convoy selectors checked `convoy`.
They now follow the components' `train_equipment_1` and `convoy_1`, matching the current debit tokens.
The tooltip calls trains “Civilian trains” because the current recipe uses that concrete vanilla level.

## Meaningful validation

A bounded actual-source parser audited 92 paid decisions, their components and composites, 24 cost selectors, 276 action cost keys, and 48 component output keys.
For every original recipe it compared compact-row helper order with full-tooltip order, component names with the decision composite, positive component amounts with negative `complete_effect` debit constants, equipment inventory tokens with the corresponding debit token, and both `available` and `custom_cost_trigger` composite calls.
Results: 92/92 recipes match, 45/45 four-resource rows contain all four payments, zero recipes exceed four distinct resource families, and all 24 threshold triplets resolve blocked/available/available.

The same source pass checked the 75 delayed transactions containing the controller/registered-state guard and compared their outer stale-refund branch with each original recipe.
All 75 contain the matching exact refund amounts.
Seventeen staged mission/event transactions remain outside that guard coverage as recorded in `decision_affordability_repair_2026_10_03.md`.
This worker did not change payment timing, refunds, state checks, mission objectives, AI, or outcomes.

Relevant-key coverage: zero missing original cost output keys or cost helper definitions.
Duplicate-key list: none among the 324 original cost keys after checking their definitions across English localisation files.
Raw-flag/placeholder list: none in the bounded cost strings.
Unrelated flags, descriptions, achievements, category text, and account prose were excluded from this audit.
File encoding concern list: none for the touched YML, with its existing UTF-8 BOM retained.

Validated source identities at the original-recipe pass:

- Decisions: `b46caeab5fd0392b9d3fe2fe5dbc4cae46b007b46bcd662536573ac84633e0e6`.
- Cost triggers: `3f38ec6896090385732678a5f385afdbb735a52cfc8ab6a8edb7e6d1a7e4309a`.
- Scripted localisation: `6e9a7c5f42536f85a5f90672fd07fe928837f7d8be14696a8acfd74fcf16e93a`.
- Decision localisation: `13a40021237a96c68ee8a924aa06f084a3f7526649cdbbcd3f81fcfea1be171d`.

These identities identify the inspected tranche in a shared tree.
Later owner edits need another recipe check.

## Prose-quality audit

- Vagueness: icon-only full tooltips did not name the resource or distinguish the concrete train level.
The final tooltip names identify every displayed amount, with “Civilian trains” matching the current concrete recipe.
- Bloat: none found in the bounded cost strings.
Names remain short and no explanatory sentences were added.
- Obvious explanation: no button narration, repeated action title, “costs,” “requires,” or filler was added.
The full tooltip deliberately repeats the numbers to identify each resource, as requested.
- Repetition: no redundant sentence chains found.
Compact strings remain icon-and-number output only.
- Overcomplication: the duplicated strict resource predicates became shared predicate calls.
Player-facing text uses familiar resource names.
- Style-rule repair: no em dash, semicolon, dramatic filler, dialectical formula, implementation-history text, or prompt label was found in the scoped cost strings.
No prose outside the cost assignment was rewritten.

Sourced quotations: none appear on these cost surfaces.
No attributed quotation was edited.
All existing dynamic amount tokens, formatting codes, output keys, and texticons were preserved.
The 45 rows gained their previously omitted fourth helper call, and available-branch trigger expressions were intentionally replaced by shared cost-component calls.

## References and MCP evidence

All requests used explicit workspace `mod_chaos_redux_ea3b2d67c2c0`.
The live reference context route eventually succeeded for `surface = localisation`, `limit = 4`.
It returned no missing or omitted required source kinds, and identified installed localisation documentation plus offline Localisation and Data structures.
Context identifies sources and does not establish a detailed read or service health for other routes.

Pertinent sections were read directly from the installed and offline files:

- `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`, lines 65–88, 184–200, 221–251, and 657–687: encoding, formatting, texticons, nested keys, and first-matching scripted localisation branches.
SHA-256 revision `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`.
MCP source id `03cc129621ab7c7a6acdfaeeffc6a5d0b7f4dab0318063b874830c706af16397`.
- `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`, lines 284–336: custom-cost text, blocked/tooltip suffixes, and explicit manual payment.
SHA-256 revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`.
- `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\dynamic_variables_documentation.md`, lines 427–432, 466–490, and 557–559: `has_manpower`, `has_political_power`, deprecated plain `manpower`, thousands-valued `manpower_k`, and `num_equipment@<token>`.
SHA-256 revision `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda`.
The installed docs do not deprecate the `has_manpower` trigger.
The original selectors' defect is strict equality handling.
- `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md`, lines 2110–2127, 3835–3842, 3957–3966, and 4121–4128: inclusive comparison names and resource trigger descriptions.
SHA-256 revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.
- Installed `documentation\effects_documentation.md`, lines 1252–1265: stockpile debit and producer handling.
- Installed `common\scripted_localisation\00_scripted_localisation.txt`, lines 1–35: country-scope conditional output and default branch precedent.
- Installed `common\units\equipment\trains.txt`, lines 3–57, and `convoys.txt`, lines 3–54: separate archetype and concrete equipment-level definitions.

No Paradox wiki web access was used.
No focus, event popup, technology, map, or scripted GUI was edited or reviewed as an assigned text surface.
Event029 uses the ordinary native decision category.
No dedicated Technology Tree Viewer tool or package was found separately from the exposed `hoi4.tech_inspect`, `hoi4.tech_render`, and `hoi4.tech_compare` tools.
Record that as a standalone viewer package gap, not proof about those services.

MCP detailed-read, exact-source lookup, and single-decision inspection results and any cancellations are recorded in the final evidence addendum below.
No render artifact has been obtained.
Native row fit, icon resolution, clipping, and four-value overflow remain unresolved, and source checks are not equivalent visual or engine proof.

## Owner follow-up and unresolved decisions

The owner supplied the Predatory Prosperity source change during this pass.
Its composite, direct debit, and stale refund no longer include political power.
The final compact row contains `GetRichesFoundCostCommandStandard`, `GetRichesFoundCostInfantryStandard`, `GetRichesFoundCostSupportLight`, and `GetRichesFoundCostSacrifice`.
Its full tooltip identifies those three ordinary resources and the same physical sacrifice in `[FROM.GetName]`.
The physical payment selects 15 Mine Development for `industrial_sacrifice` or 100 marked workers for `human_crisis`, using the owner's constants and state-scoped predicates.
No fifth cost was added.
Material and Authority cost strings retain their original payment recipes.
The parent's stability loss consequence remains in action prose, outside this cost patch.

A transient source inspection found the old PP refund while the owner's patch was in progress.
The final validation found that it had been removed by the owner, with all 75 guarded refund recipes matching.
This worker did not patch gameplay.

Final-source recheck: all 92 ordinary payment recipes match their gate/debit and row/tooltip helper lists.
Predatory Prosperity matches three ordinary resource components plus one physical-family component.
There are still 45 four-component rows.
The new physical component has source-model boundary checks at Mine Development 14/15/16 and state population 99/100/101, producing blocked/available/available with the other owner-defined payment conditions held satisfied.
The available branch calls the owner's full payment predicate, including the severe human-crisis gates, rather than checking population alone.
Both family amounts use the exact debit or harm-record constant.
`riches_found_account_predatory_terms_are_valid` in `common/scripted_triggers/029_riches_found_triggers.txt`, lines 781–797, defines these inclusive thresholds.
`riches_found_record_predatory_prosperity_harm` in `common/scripted_effects/029_riches_found_harm_effects.txt` uses `riches_found_harm.predatory_prosperity_civilian_deaths`, matching the human cost output.
Final relevant-key count is 329, with zero duplicate or missing component output keys.
The original 92-recipe audit above remains the before-source evidence, and the final audit includes the owner-changed recipe.

Final validation source identities:

- `common/decisions/029_riches_found_decisions.txt`: `1311db902a995a07dba378e3a78d1cd662996e5b221ea8845b529c8839e22d9f`.
- `common/scripted_triggers/029_riches_found_cost_triggers.txt`: `fbaf8071a016f30f2d937a92af31e67e89965307b83f0b916afa9bd3b38dc621`.
- `common/scripted_localisation/029_riches_found_scripted_localisation.txt`: `1d2a27128758bfa20c49c968e5510daf11709db07fb8bc291f9dbefdf5d33bfa`.
- `localisation/english/029_riches_found_decisions_l_english.yml`: `54d211b8dfb8161fec6cb56502bdadf290c3dc09d390b50fbd2fa54006aaccaf`.

Potential equipment semantics gap: matching source tokens does not prove how `num_equipment@<archetype>` and `add_equipment_to_stockpile` aggregate concrete levels, variants, captured equipment, or producers.
Infantry and support use archetype tokens in both gate and debit, while trucks, civilian trains, and convoys use concrete tokens.
The installed short descriptions do not settle aggregate-removal behavior.
Mixed-level and captured-stockpile acceptance remains unresolved.
Do not describe archetype totals as verified concrete-level debit coverage.

No catalog wording was reviewed or changed because this assignment concerns native cost strings only.
There is no spreadsheet wording handoff for event-details or evolution text.
The final key lists above provide the cost wording for a documentation owner if a catalog field explicitly mirrors a cost recipe.

No original recipe, payment, route, or fourth cost was removed or simplified.
The bounded source repair is implemented.
Engine/render validation and mixed-level inventory semantics remain open.
Skills used: chaos-redux-events, chaos-redux-decisions-missions, and chaos-redux-subagents.
No skill was created or changed.

## Final MCP evidence addendum

- `hoi4.reference_context` succeeded with explicit workspace, localisation surface, and limit 4.
Its returned source IDs and revisions are retained above.
It returned no artifacts.
- Initial narrow `hoi4.reference_search` queried `manpower_k`, game documentation only, limit 1.
Initial `hoi4.source_lookup` queried `GetRichesFoundCostTrainStandard`, references disabled, one definition and 12 lines.
Neither returned evidence before the pending request was cancelled.
- Narrower retries queried `num_equipment`, game documentation only, limit 1, and `riches_found_cost_can_afford_train_standard`, references disabled, one definition and four lines.
Both again returned no result before cancellation.
Exact source/reference service gap: no detailed search or lookup evidence was obtained from these calls.
- `hoi4.reference_read` requested the prior handoff's installed dynamic-variable source id `1d55490d9a71c1001c4f320d8c7396dc574795b5a8e9eef0bc53addb7f40db55`, revision `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda`, lines 557–559.
It returned `timed out awaiting tools/call after 600s`.
A narrower current-context read of offline Localisation, lines 657–686, also returned no evidence before cancellation.
- The first `hoi4.decision_inspect` targeted only `decision_riches_found_survey` and returned `timed out awaiting tools/call after 600s`.
A retry without scenarios was rejected with `Decision inspection requires declared scenarios at scenarios`.
The subsequent minimal named `survey_cost_exact` scenario declared USA with PP 10, manpower_k 0.1, and motorized_equipment_1 stockpile 25.
It returned no result before cancellation.
These are declared inputs only, not observed state or confirmed decision availability.
- For the native row consumer, installed `interface\countrydecisionview.gui` identifies window `countrydecisionview`.
The GUI route requires windowName and scenario together, and an explicit `scenario.id`.
The bounded `event029_native_cost_window` inspect and render requests used that window and explicit workspace.
Render requested normal and long-text states at 1920×1080, UI scale 1.
Neither returned an artifact before cancellation.
No dynamic native decision-row binding or successful visual result was obtained, so fit, overflow, clipping, icon resolution, and production-view correctness remain blocked.
The absence of a successful render is not attributed to a renderer discrepancy.
- All viewer and inspector calls were read-only.
No jobs, helper-expansion route, native MCP task, GUI rewrite, source rewrite, or game launch was used.
No useful artifact URI was returned by any of these bounded calls.
