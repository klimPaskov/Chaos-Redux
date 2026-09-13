# CBRN decision-row wording handoff

Status: implemented and reviewed by the parent with native production MCP previews.
Acceptance basis: parent assigned compact row labels for the screenshot overlap in National CBRN Protection Program.

## Files and scope

Changed localisation/english/cbrn_protection_l_english.yml only for seven program decision names and their fourteen ready/blocked custom-cost keys.
No gameplay, cost, availability, AI, description, requirement tooltip, completion tooltip or GUI layout changes.
Exact byte baseline: baseline/localisation/english/cbrn_protection_l_english.yml.
Baseline SHA256: D9B08158DD60EDEFD4CC3212259C0A1FF9B110F689C32A06DFCE4AD9EDAC54CC.
The baseline already contains the parent-owned Black Friday shelter wording and costs, which this patch preserves.

## Names before and after

| Key | Before | After | Name length before/after |
| --- | --- | --- | --- |
| cbrn_convert_civilian_mask_industry | Convert Civilian Mask Industry | Convert Mask Factories | 30/22 |
| cbrn_establish_national_respirator_reserve | Establish a National Respirator Reserve | Build Respirator Reserve | 39/24 |
| cbrn_issue_masks_to_field_army | Issue Masks to the Field Army | Issue Army Masks | 29/16 |
| cbrn_recondition_old_masks | Recondition Old Masks | Rebuild Old Masks | 21/17 |
| cbrn_register_and_fit_population | Register and Fit the Population | Fit Civilian Masks | 31/18 |
| cbrn_replace_military_mask_filters | Replace Military Mask Filters | Replace Army Filters | 29/20 |
| cbrn_simplify_filters_for_mass_issue | Simplify Filters for Mass Issue | Simplify Mask Filters | 31/21 |

## Cost rows and width consideration

Every blocked key below changes from Additional project requirements are not met (43 visible characters) to Requirements unmet (18 visible characters).
This remains accurate because each custom_cost_trigger calls the full corresponding cbrn_can_* eligibility predicate, which includes more than resource availability.
Ready rows replace long resource words and the Additional prefix with the existing Chaos Redux support-equipment icon and installed vanilla manpower/civilian-factory icons followed by the existing dynamic integer amount.
Factory reservation and consumption timing remain in the unchanged cost tooltip.
The military-filter row retains + crates because replacement crates are consumed at completion.
The longest shortened name is Build Respirator Reserve at 24 characters.
These length reductions create room for the native right-aligned cost area but are source-level evidence, not a pixel-fit or rendered visual pass.
Parent must inspect and compare native rows with ready and blocked states for all seven actions, including the three-resource civilian fitting row.

Final changed keys:

```yaml
cbrn_convert_civilian_mask_industry: "Convert Mask Factories"
cbrn_convert_civilian_mask_industry_extra_cost: "£support_equipment_text_icon §Y[?constant:cbrn_protection_decision_cost.convert_industry_support|0]§!  £civ_factory §Y[?constant:cbrn_protection_decision_cost.convert_industry_factories|0]§!"
cbrn_convert_civilian_mask_industry_extra_cost_blocked: "§RRequirements unmet§!"
cbrn_establish_national_respirator_reserve: "Build Respirator Reserve"
cbrn_establish_national_respirator_reserve_extra_cost: "£support_equipment_text_icon §Y[?constant:cbrn_protection_decision_cost.establish_reserve_support|0]§!  £civ_factory §Y[?constant:cbrn_protection_decision_cost.establish_reserve_factories|0]§!"
cbrn_establish_national_respirator_reserve_extra_cost_blocked: "§RRequirements unmet§!"
cbrn_issue_masks_to_field_army: "Issue Army Masks"
cbrn_issue_masks_to_field_army_extra_cost: "£support_equipment_text_icon §Y[?constant:cbrn_protection_decision_cost.issue_field_army_support|0]§!  £civ_factory §Y[?constant:cbrn_protection_decision_cost.issue_field_army_factories|0]§!"
cbrn_issue_masks_to_field_army_extra_cost_blocked: "§RRequirements unmet§!"
cbrn_recondition_old_masks: "Rebuild Old Masks"
cbrn_recondition_old_masks_extra_cost: "£support_equipment_text_icon §Y[?constant:cbrn_protection_decision_cost.recondition_masks_support|0]§!  £civ_factory §Y[?constant:cbrn_protection_decision_cost.recondition_masks_factories|0]§!"
cbrn_recondition_old_masks_extra_cost_blocked: "§RRequirements unmet§!"
cbrn_register_and_fit_population: "Fit Civilian Masks"
cbrn_register_and_fit_population_extra_cost: "£support_equipment_text_icon §Y[?constant:cbrn_protection_decision_cost.register_population_support|0]§!  £manpower_texticon §Y[?constant:cbrn_protection_decision_cost.register_population_manpower_gate|0]§!  £civ_factory §Y[?constant:cbrn_protection_decision_cost.register_population_factories|0]§!"
cbrn_register_and_fit_population_extra_cost_blocked: "§RRequirements unmet§!"
cbrn_replace_military_mask_filters: "Replace Army Filters"
cbrn_replace_military_mask_filters_extra_cost: "£civ_factory §Y[?constant:cbrn_protection_decision_cost.replace_filters_factories|0]§! + crates"
cbrn_replace_military_mask_filters_extra_cost_blocked: "§RRequirements unmet§!"
cbrn_simplify_filters_for_mass_issue: "Simplify Mask Filters"
cbrn_simplify_filters_for_mass_issue_extra_cost: "£support_equipment_text_icon §Y[?constant:cbrn_protection_decision_cost.simplify_filters_support|0]§!  £civ_factory §Y[?constant:cbrn_protection_decision_cost.simplify_filters_factories|0]§!"
cbrn_simplify_filters_for_mass_issue_extra_cost_blocked: "§RRequirements unmet§!"
```

## Prose and coverage audit

Bloat and repetition: seven repeated full blocked sentences become a short requirement status.
Obvious explanation: Additional and resource word expansions move out of the compact row, while full details remain in their existing tooltips.
Overcomplication and style: shortened direct action names preserve the relevant reserve, civilian fitting, army issue, army filters, old-mask repair, industry conversion and simplified-filter identities.
Vagueness: the blocked status is deliberately a summary, and the decision tooltip retains the exact unmet requirement wording.
No missing or duplicate keys found in the assigned seven decision/cost families.
No scripted-localisation calls occur in the changed keys, so no scripted-localisation repair was needed.
All fourteen existing dynamic amount tokens across ready cost rows were preserved exactly and in their original order.
No sourced quotations occur in the assigned rows.
No event catalog field was assigned or changed, so there is no spreadsheet handoff.
Localisation BOM and all unassigned lines were preserved.

## Validation and limits

Validated the category has seven assigned custom_cost_text references and each resolves to its ready, blocked and tooltip key.
Compared the current file to the exact saved byte baseline, confirming precisely twenty-one changed keys and unchanged descriptions, requirement/cost tooltips and action effects text.
Verified dynamic amount tokens survive each ready-row rewrite.
Read offline core wiki pages, Localisation and Decision modding custom-cost rules, the events/decisions/subagents skills, installed vanilla script concept and localisation formatter documentation, EST custom-cost precedent, and vanilla decision civilian-factory cost localisation.
Mandatory native MCP GUI before/after inspection, render and compare are delegated to the parent, per the explicit task assignment.
No rendered visual pass claimed by this handoff.
No technology, doctrine, event, focus or map surface is changed by this bounded patch.
No new mechanics, fallback or design simplification.
Parent visual review: all seven names and both ready/blocked cost variants fit with separate glyph regions in fourteen production MCP native row renders at 1920 x 1080, scale 1.
The screenshot overlap is reproduced by the matching before fixture.
See cbrn_gui_final_before.json, cbrn_gui_final_after.json, cbrn_native_rows.png and cbrn_native_row_receipts.json.
Per-element button states are fixture inputs; this text-width review does not prove live eligibility, payment, click behavior or receiver execution.
No unresolved wording decision or mechanic plan handoff.

Resource icon source: interface/chaosx_texticons.gfx defines GFX_support_equipment_text_icon and its DDS exists. Vanilla interface/texticons.gfx defines GFX_manpower_texticon and GFX_civ_factory.
