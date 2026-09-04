# Repression UI text and wiring audit

## Scope and status

This is a bounded read-only audit of the current repression administration redesign. Implementation files were not edited. The inspected runtime sources were `interface/camp_repression_ledger.gui`, `common/scripted_guis/camp_repression_ledger_scripted_gui.txt`, `localisation/english/camp_repression_ui_l_english.yml`, `common/scripted_localisation/camp_repression_ui_scripted_localisation.txt`, `localisation/english/camp_repression_rework_l_english.yml`, and `common/scripted_localisation/camp_repression_ledger_scripted_localisation.txt`.

The review distinguishes defects introduced or newly exposed by the redesign from inherited text or action-contract issues. It does not make a full-system completion claim and does not assess gameplay balance, AI weights, or unrelated repression mechanics.

## Concrete findings

### New regressions or redesign gaps

1. **High: the Situation page no longer shows labor output or resistance, although visible orders still change them.** The prior overview exposed `[GetCampLaborOutputDisplay]` and `[GetCampResistancePressureName]`. The redesign retains only civilian-loss pressure, aggregate administrative strain, and evidence. `Reduce Quotas` explicitly lowers labor output and resistance, while guard allocation also changes breakdown or resistance pressure, so the player cannot see two material sides of those choices before acting. Restore labor output and resistance as concise support information, preferably in the existing card tooltips or as one compact line rather than reviving the old component ledger. Active-site and eligible-territory counts do not need to return because the new scrollable lists expose the actual locations.

2. **High: disabled buttons retain yellow adjacent cost rows.** Every `camp_ui_cost_*` and `camp_ui_directive_cost_*` string uses yellow amounts regardless of the matching `*_click_enabled` result. A button can therefore be disabled while its adjacent cost still looks payable. The tooltip eventually provides a blocked-status sentence, but the immediate presentation conflicts with the decision/GUI rule that unaffordable amounts show a blocked state. Bind the cost row to an affordability-aware defined text or provide enabled and blocked variants that use the same predicates as the button.

3. **Medium: `camp_ui_selected_status` overstates action availability.** `[GetCampSelectedStateActionSummary]` resolves an active site to `camp_selected_action_active: "Site orders available"` and a discovered location to `camp_selected_action_reform: "Inspection or closure"` without testing resources, route authority, expansion freeze, an active closure, or other action gates. The actual buttons can all be disabled or absent. Replace these claims with non-committal navigation copy such as “Review site orders below” and “Review inspection and closure options,” leaving exact availability to each button and tooltip.

4. **Medium: the sidebar instruction is visible on tabs where location selection is impossible.** `camp_ui_navigation_note: "Select a location to review its status and orders."` has no element-level visibility trigger, so it remains on Situation, Policy, and Accountability as well as Territories and Sites. Show it only when either location tab is active, or replace it with a general description of the five sections.

5. **Medium: the Accountability help points to controls that do not exist on that page.** `camp_ui_evidence_help` says “Review scrutiny and closure under Accountability,” but Accountability is informational and contains no scrutiny or closure controls. Inspection, dismantlement, and evidence-destruction orders are on Sites, with general network orders under Policy. Point the player to Sites for location orders and describe Accountability as the record of exposure, deaths, and closure pressure.

6. **Medium: the Accountability introduction assumes operations have already ceased.** `camp_ui_accountability_intro: "Surviving records, civilian deaths and obligations remain after operations cease."` appears while the network is active as well as after closure. Use a temporally valid sentence such as “Surviving records, civilian deaths and state obligations can outlast the operating network,” or branch the text by network phase.

7. **Low: the selected-location empty state reads as three separate system fallbacks.** With no selected state, the panel combines `No state selected`, the site-type fallback `No active site`, and `No order selected`. This is mechanically safe but still feels like a diagnostic stack. Give the panel one direct instruction when `camp_selected_state_id` is absent, such as “Choose a territory or site from the list,” and hide the type and action-summary lines in that state.

8. **Low: `camp_ui_location_list_note` is redundant and becomes false beside an empty list.** “Locations available to this administration” repeats the tab introduction and remains visible when `camp_ui_pool_empty` or `camp_ui_site_empty` states that no location exists. Remove it, make it conditional, or use the space for information the list itself does not convey.

9. **Low: `camp_ui_harm_help` can imply that recorded deaths are reversible.** “Pursue inspection or closure to address civilian harm” is vague beside a cumulative-loss display. State the prospective effect directly, for example that inspection or closure can halt further harm; do not imply that the recorded deaths are reduced.

### Inherited issues newly made prominent

1. **Labor-project payment and start requirement are different quantities, but the tooltip does not name the reserve.** The displayed payment and existing tooltip both use `camp_rework_equipment_cost` values: 120 motorized, 18 trains, and 180 support equipment. The click gate instead requires `camp_rework_equipment_start_requirement`: 160 motorized, 24 trains, and 240 support equipment, because the mission must retain a reserve after paying the one-time charge. Payment display is therefore aligned with the debit, but a player holding more than the displayed cost and less than the start requirement sees a yellow cost row and a disabled action. The inherited blocked-status text names the deficient equipment without explaining that the larger amount includes a retained reserve. Add a concise requirement line or tooltip sentence that distinguishes “paid now” from “must be available at start.”

2. **Several inherited tooltips are longer than the normal two-to-four-line budget.** The restricted chemical and biological order tooltips combine consequences, payload cost, and status into long multi-paragraph blocks. This is not caused by the sidebar redesign, but the compact 172 by 34 cost area makes the same density more visible. Preserve all consequences and dynamic payload tokens while tightening repeated explanation if these tooltips are revised.

## Key, scripted-localisation, and encoding audit

- **Missing keys:** none among the current `.gui` `text`, `buttonText`, and `pdx_tooltip` references when resolved against English localisation.
- **Duplicate keys:** none among the current GUI-referenced keys across `localisation/english/*.yml`.
- **Scripted-localisation issues:** none unresolved in the new localisation set. Every named `[GetCamp…]` call resolves to a `defined_text`. `GetCampUiExpansionCost` selects the existing activation or expansion cost by the selected state's active-site status.
- **Dynamic row scope:** `camp_ui_location_name: "[This.GetName]"` and `camp_ui_location_select_tt` are correctly paired with `change_scope = yes` for both `camp_ui_pool_list` and `camp_ui_site_list`. This removes the former six-row cap without exposing array indices or raw variables.
- **Dynamic text opportunities:** use affordability-aware defined text for adjacent cost rows; branch the Accountability introduction by phase if a single temporally neutral sentence is rejected; use a no-selection branch for the selected-location panel rather than stacking generic fallbacks.
- **File encoding:** both inspected English localisation files are UTF-8 with BOM. No encoding concern was found.
- **Implementation-detail exposure:** the redesigned main text no longer exposes raw country counters or component-ledger rows. The remaining `Current course: [GetCampReformRouteName]` and country-action labels are player-facing policy language rather than implementation telemetry.

## Cost and action alignment

- Expansion, inspection, dismantlement, evidence destruction, restricted methods, guard allocation, and quota reduction use the same visible constant families as their inherited tooltip/payment strings.
- Country-directive rows use the existing dynamic political-power value plus `[GetCampCountryActionNCostDetails]`, matching the inherited action tooltip structure.
- The labor-project exception above is a requirement-versus-payment explanation gap, not a wrong debit amount.
- The restricted payload strings can contain a dynamic amount, text icon, and full equipment name inside a 172 by 34 fixed text box. Source review cannot prove that every researched payload name fits. This remains a visual-render question for the parent's Sites matrix.

## Cross-surface mismatch notes

- The strongest mismatch is between the Situation page and its actionable controls: the page omits labor output and resistance even though Policy and Sites actions explicitly change them.
- Accountability describes closure activity but hosts no closure controls.
- The category summary and header now show phase and institution rather than exact location counts. This is acceptable because the full scrollable location lists preserve actual location coverage; restoring raw counts is not necessary unless the production render shows the lists are not discoverable.
- No spreadsheet or event-log wording was inspected because neither surface was assigned in this bounded shared-UI audit.

## Prose-quality audit

- **Vagueness:** `address civilian harm`, `Review scrutiny`, and `Site orders available` fail to state the exact available surface or consequence.
- **Bloat:** the new main-panel prose is generally concise. The inherited restricted-method tooltips remain dense.
- **Obvious explanation:** `Locations available to this administration` merely restates the list and should be removed or replaced.
- **Repetition:** the no-selection panel repeats three fallback states; the list note repeats each tab introduction.
- **Overcomplication:** no new sentence has excessive clause nesting. Dynamic cost rows remain visually dense because several resources and equipment names must fit a narrow box.
- **Style-rule repair:** the redesign removes the old ledger-like component dump and raw country counters. No em dash, semicolon, implementation-history note, tuning note, prompt fragment, or staged contrast formula was found in the new player-facing file.

## Sourced quotations

No quote-bearing player-facing surface is used by the inspected repression window. The attributed super-event quotations at the start of `camp_repression_rework_l_english.yml` were outside this UI audit and were not changed or normalized.

## MCP evidence and blocker

The required read-only `hoi4.gui_inspect` call targeted `repression_ledger_window` with scenario `{ "id": "repression_ui_text_audit_current" }`. It failed with the exact server-boundary error `timed out awaiting tools/call after 180s` and returned no artifact URI. A subsequent render attempt was terminated when the parent requested no further MCP calls and reported that its final Sites render was pending. Therefore this report does not claim production-render proof for wrapping, overflow, click regions, empty-list presentation, disabled-state presentation, or restricted payload cost fit. Source review is not treated as equivalent visual evidence.

## Recommended parent fixes by file and key

- `localisation/english/camp_repression_ui_l_english.yml`: revise `camp_ui_navigation_note`, `camp_ui_harm_help`, `camp_ui_evidence_help`, `camp_ui_accountability_intro`, and `camp_ui_location_list_note`; replace or branch `camp_ui_selected_status`; add compact labor-output and resistance context without restoring the former component ledger.
- `localisation/english/camp_repression_rework_l_english.yml`: revise `camp_selected_action_none`, `camp_selected_action_active`, `camp_selected_action_reform`, and `camp_selected_action_pool` if the parent keeps `[GetCampSelectedStateActionSummary]`; clarify the retained labor-project reserve in `camp_gui_start_labor_project_tt` or a linked requirement key.
- `common/scripted_guis/camp_repression_ledger_scripted_gui.txt`: gate the sidebar location instruction to Territories and Sites, add a clean no-selection presentation branch, and give adjacent cost rows enabled/blocked presentation tied to the corresponding click predicates.
- `interface/camp_repression_ledger.gui`: reserve concise Situation space for labor output and resistance, and use the parent's production render to confirm all multi-resource cost strings fit their fixed 172 by 34 boxes.

## Skipped meaningful validation and uncertainty

- Production render review was unavailable to this subagent because the inspect route timed out and the parent retained the final render matrix.
- No live game validation was performed; it belongs to the user.
- The exact visual severity of yellow cost rows beside disabled buttons and the payload-name overflow risk remains dependent on the pending production render.
- No implementation changes, gameplay changes, cost changes, AI changes, or simplifications were made by this audit.

## Bounded clarity patch

After the audit, the parent assigned a narrow patch limited to the new English UI localisation and its scripted-localisation helper. No GUI geometry, visibility trigger, click gate, payment, gameplay effect, cost value, or AI behavior was changed.

### Changed files

- `localisation/english/camp_repression_ui_l_english.yml`
- `common/scripted_localisation/camp_repression_ui_scripted_localisation.txt`
- This handoff

### Changed and added keys

- Revised: `camp_ui_navigation_note`, `camp_ui_harm_help`, `camp_ui_evidence_help`, `camp_ui_location_list_note`, `camp_ui_selected_state`, `camp_ui_selected_status`, and `camp_ui_accountability_intro`.
- Added: `camp_ui_harm_tt`, `camp_ui_strain_tt`, `camp_ui_selected_state_value`, `camp_ui_selected_state_empty`, and `camp_ui_labor_project_tt`.
- Added scripted-localisation helper: `GetCampUiSelectedState`.

### Before and after

- The always-visible sidebar instruction no longer tells the player to select a location while viewing Situation, Policy, or Accountability. It now describes the complete five-section workflow.
- Civilian-harm guidance now states that inspection and closure halt further harm rather than implying that recorded deaths can be undone.
- `camp_ui_harm_tt` restores the omitted resistance band beside civilian-loss pressure. `camp_ui_strain_tt` restores forced-labor contribution beside aggregate administrative strain without restoring the removed component ledger.
- Evidence guidance now points location orders to Sites and treats Accountability as the surviving public record.
- Accountability text is valid during active operation and after closure.
- The selected-location panel now calls `GetCampUiSelectedState`. With a selection it preserves the existing state name and site type. Without a selection it returns only `camp_ui_selected_state_empty` instead of stacking three generic fallbacks.
- The selected status now says `Review the orders below` and no longer promises that any order is available.
- `camp_ui_labor_project_tt` preserves the original action, payment, and blocked-status information and adds the exact start requirement from the current gate: 160 motorized equipment, 24 trains, and 240 support equipment through dynamic constants. It identifies these amounts as including the retained mission reserve.

### Prose repair summary

- **Vagueness:** replaced `address civilian harm`, `review scrutiny`, and `orders available` with concrete consequences and destinations.
- **Bloat and repetition:** collapsed the empty selection into one instruction and replaced the redundant location-list label with an action instruction.
- **Obvious explanation:** removed the statement that the list contains locations available to the administration.
- **Overcomplication:** kept Situation context to two compact three-line tooltips instead of restoring the previous component rows.
- **Style rules:** no implementation history, raw variable name, semicolon, em dash, prompt fragment, or hidden-mechanic explanation was added to player-facing text.

### Dynamic localisation and preservation

- Added `GetCampUiSelectedState` with an explicit selected branch and neutral fallback.
- Preserved `[GetCampSelectedStateName]`, `[GetCampSiteTypeName]`, `[GetCampPopulationLossPressureName]`, `[GetCampResistancePressureName]`, `[GetCampOverstretchBandName]`, `[GetCampLaborOutputDisplay]`, `[GetCampLaborBlockedSummary]`, every cost constant, and every texticon token used by the patched surfaces.
- No sourced quotation was touched.

### Validation and remaining parent work

- Source review confirms that every added `[GetCamp…]` call resolves and every helper localisation key exists in the patched English file.
- The labor-project start-requirement constants match the current click gate: `motorized_equipment`, `trains`, and `support_equipment` from `camp_rework_equipment_start_requirement`.
- The parent still owns wiring `camp_ui_harm_tt`, `camp_ui_strain_tt`, and `camp_ui_labor_project_tt` into the relevant GUI controls, selected-status visibility, affordability-aware cost presentation, and the production MCP render matrix.
- No further MCP call was made because the parent explicitly retained recovery of the bounded production previews.

## Resource-level cost presentation patch

The parent subsequently assigned the final affordability presentation to the two new UI localisation files. This patch does not alter click gates, resource payments, costs, effects, AI, or GUI geometry.

### Changed files and keys

- `localisation/english/camp_repression_ui_l_english.yml`: retained the existing GUI-facing `camp_ui_cost_*` and `camp_ui_directive_cost_1` through `camp_ui_directive_cost_4` keys, but changed their values to call resource-level helpers. Added normal and red component keys for political power, manpower, command power, infantry equipment, support equipment, motorized equipment, trains, convoys, fuel, and each selected restricted payload. Added compact package composition keys `camp_ui_cost_activation`, `camp_ui_cost_expansion`, and `camp_ui_directive_cost_*`. Added `camp_ui_scroll_hint: "Scroll to see more locations."`, shortened `camp_ui_evidence_help`, and removed the unused `camp_ui_location_list_note`.
- `common/scripted_localisation/camp_repression_ui_scripted_localisation.txt`: changed `GetCampUiExpansionCost` to select the new UI-only activation or expansion composition. Added the resource helpers, four directive political-power helpers, four directive package helpers, `GetCampUiChemicalPayloadCost`, and `GetCampUiBiologicalPayloadCost`.
- This handoff records the final gate mapping and validation boundary.

### Source gate to display helper mapping

- Activation political power, manpower, command power, and support equipment map to `GetCampUiActivationPoliticalPower`, `GetCampUiActivationManpower`, `GetCampUiActivationCommand`, and `GetCampUiSupportCost`.
- Expansion political power, manpower, support equipment, and trains map to `GetCampUiExpansionPoliticalPower`, `GetCampUiExpansionManpower`, `GetCampUiSupportCost`, and `GetCampUiTrainCost`. The current GUI also requires expansion command power and infantry equipment, but `camp_rework_consume_expansion_resources` does not debit either resource. They therefore remain requirements in the detailed blocked tooltip rather than appearing as payments.
- The selected labor project maps political power to `GetCampUiLaborPoliticalPower`. Its displayed motorized, train, and support amounts remain the exact one-time debits from `camp_rework_equipment_cost`, while `GetCampUiLaborMotorizedCost`, `GetCampUiLaborTrainCost`, and `GetCampUiLaborSupportCost` turn red against the exact reserve-inclusive `camp_rework_equipment_start_requirement` click thresholds.
- Guard allocation maps to `GetCampUiGuardPoliticalPower`, `GetCampUiGuardManpower`, `GetCampUiGuardCommand`, and `GetCampUiInfantryCost`. Quota reduction reuses only the guard political-power helper, matching its sole resource gate.
- Inspection maps to `GetCampUiReviewPoliticalPower`. Dismantlement maps to `GetCampUiDismantlePoliticalPower`, `GetCampUiDismantleManpower`, and `GetCampUiSupportCost`. Evidence destruction maps to `GetCampUiEvidencePoliticalPower`, `GetCampUiActivationManpower`, `GetCampUiEvidenceCommand`, and `GetCampUiSupportCost`.
- Restricted methods map political power to `GetCampUiRestrictedPoliticalPower`. The compact payload helpers preserve the original chemical order of soman, sarin, tabun, lewisite, mustard, phosgene, and chlorine, including the three mastery-cost branches, followed by the same technology-only branches. The biological order remains smallpox, plague, anthrax, and tularemia, followed by the same technology-only branches. Capacity branches are normal and technology-only branches are red. Each compact result shows the selected amount followed by `£camp_restricted_payload_texticon`; the original detailed tooltips retain the payload identity.
- Directive political power maps through `GetCampUiDirective1PoliticalPower` through `GetCampUiDirective4PoliticalPower`, with explicit branches for every assigned directive cost: labor project, guard, review, dismantlement, redress, and evidence. Package resolvers `GetCampUiDirective1CostDetails` through `GetCampUiDirective4CostDetails` preserve the existing package order and map labor project, guard, evidence, dismantlement, support only, colonial guard, support and convoys, and transport guard to their exact resource helpers.

Every resource debit shown by the existing activation, expansion, labor, guard, quota, inspection, dismantlement, evidence, restricted-method, and directive presentations remains visible. No hidden cost omission was found. Non-resource locks such as routes, cooldowns, selected-state validity, factories, infrastructure, war state, and reform authority do not color otherwise affordable resources red.

### Display behavior before and after

- Before, every adjacent amount remained yellow even when that particular resource failed its affordability gate. After, only the failed amount and its icon turn red; each satisfied entry remains yellow even when another resource or a non-resource condition blocks the action.
- Payload rows previously included the full equipment name in the 172 by 34 cost area. They now show only the amount and established restricted-payload icon. Full payload identity remains in the existing tooltip.
- Every site cost row contains at most four icons. Every directive contains political power plus at most three package icons, for the same four-icon maximum.

### Prose and token preservation

- **Vagueness:** the scroll hint gives one direct instruction, and the shortened evidence guidance retains the exact destination for evidence and orders.
- **Bloat:** restricted payload names were removed only from the compact adjacent cost line; the detailed tooltip remains unchanged.
- **Obvious explanation and repetition:** no new explanatory cost prose was added. Resource repetition is mechanical and necessary for independent affordability coloring.
- **Overcomplication:** multi-resource costs are composed from short amount-plus-icon units and remain within the assigned four-icon limit.
- **Style repair:** no implementation history, raw tuning note, semicolon, em dash, or prompt label was added to player-facing text.
- All dynamic cost constants, display variables, icon tokens, selected-payload order, and original detailed payload strings were preserved. No sourced quotation was touched.

### Validation and limits

- Source checks found no duplicate localisation keys, no duplicate `defined_text` names, no unresolved `localization_key` reference in the new scripted-localisation file, and no unresolved `[GetCampUi…]` call in the new English file. Scripted-localisation braces balance, and it contains no direct formatting characters.
- The English file remains UTF-8 with BOM. The resulting site and directive compositions were counted against the assigned four-icon maximum.
- Production GUI rendering was not rerun because the parent explicitly owns the final MCP fixture and requested no further MCP calls from this subagent. Visual fit at 172 by 34 and 316 by 24 remains for the parent's production render matrix.
- No gameplay, balance, cost, AI, or sourced-quotation change was made. No simplification or fallback was introduced.

### Production-render icon boundary correction

The parent's final MCP render found that a color reset placed directly after a text icon, such as `£pol_power§!`, is consumed as part of the icon token and renders the missing pink icon. Every new cost component now terminates its icon with whitespace before the reset, such as `£pol_power §!`. This preserves per-resource coloring for both the amount and icon while giving the renderer an unambiguous icon-token boundary. A source check confirms that no `£icon§!` boundary remains in the new UI localisation file. The parent owns the post-correction production render.

### Selected-location line grouping

The parent's post-boundary MCP render confirmed that the icons resolve, but automatic wrapping in the 172 px selected-location cost area could separate the final icon from its amount. The five affected compositions now use an explicit line break after the first two resource helpers: `camp_ui_cost_activation`, `camp_ui_cost_expansion`, `camp_ui_cost_start_labor_project`, `camp_ui_cost_dismantle_selected_site`, and `camp_ui_cost_destroy_evidence`. Dismantlement places its final support-equipment entry alone on the second line; the other four keys place two complete resource entries on each line. Restricted-method rows remain two-entry single lines, and the wider Policy and directive rows remain unchanged. All whitespace icon terminators are preserved. The parent owns the affected-location rerender.
