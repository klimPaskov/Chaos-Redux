# Event 029 narrow cost localisation audit

Date: 2026-10-07.

Disposition: the six specific source and presentation findings are implemented by the parent and verified below.
Partner-name cache coverage remains unresolved, native row fit remains blocked by missing render evidence, and the broader dynamic-cost requirement remains incomplete.
This is a ten-profile audit handoff, not Event 029 completion or a full decision-family audit.

## Authority and scope

The parent authorized a read-only review of survey, claim_register, reserve_deposit, camp_administration, drive_deeper, seal_depths, nationalize_with_compensation, buyout, repair, and permanent_seal.
The parent subsequently authorized this durable handoff and clarified that “no new writes” prohibited additional source changes, not the report.
Only this new Markdown file was written by the localisation auditor.
No gameplay, localisation, scripted localisation, assets, workbook, exports, index, or commit was changed, and no child or game process was launched.

Primary sources are `common\decisions\029_riches_found_decisions.txt`, `common\scripted_triggers\029_riches_found_cost_triggers.txt`, and `localisation\english\029_riches_found_decisions_l_english.yml`.
Directly linked getters, constants, reimbursement and partner helpers were inspected only to establish their text contracts.
The earlier `physical_cost_audit_2026_10_07.md` was read as parent-supplied evidence, with its old presentation findings reconciled against current source.
Its last-mine category lifecycle finding is outside this narrow localisation pass and is not resolved by this report.

## Current ten-profile crosswalk

All decision IDs below have the prefix `decision_riches_found_`, affordability composites have `riches_found_can_afford_`, and cost localisation bases have `riches_found_cost_`.
Line references in this table use the three primary files above.
Factory commitments are native temporary capacity commitments, not equipment or manpower debits.

| Profile | Current payment and commitment | Decision block | Composite line | Cost keys: base, blocked, hover | Inline values |
| --- | --- | --- | --- | --- | --- |
| survey | 2 civilian factories for 30 days, 100 manpower, 25 trucks | 39–116 | 97 | 588–590 | 3 |
| claim_register | 2 civilian factories for 30 days, 10 political power, 300 manpower | 118–212 | 102 | 595–597 | 3 |
| reserve_deposit | 2 civilian factories for 30 days, 25 political power, 100 manpower, 25 support equipment | 405–497 | 116 | 616–618 | 3 |
| camp_administration | 2 civilian factories for 60 days, 300 manpower, 25 support equipment | 592–680 | 126 | 630–632 | 3 |
| drive_deeper | 2 civilian factories for 90 days, 300 manpower, 150 support equipment, temporary 25% output reduction | 1725–1839 | 192 | 714–716 | 3 |
| seal_depths | 2 civilian factories for 60 days, 300 manpower, 150 support equipment, ordinary sealed-deposit output reduction | 4724–4811 | 343 | 355–357 | 3 |
| nationalize_with_compensation | 2 civilian factories for 90 days, 40 political power | 3283–3380 | 262 | 540–542 | 2 |
| buyout | 2 civilian factories for 90 days, 40 political power | 3487–3575 | 272 | 554–556 | 2 |
| repair | 2 civilian factories for 90 days, 75 trucks, 75 support equipment, conditional one-use reserve reimbursement | 4813–4913 | 348 | 362–364 | 3 |
| permanent_seal | 2 civilian factories for 90 days, 600 manpower, 150 support equipment, permanent mine-output loss | 5097–5181 | 364 | 384–386 | 3 |

Manual tracing found no amount mismatch between these current displays, the matching affordability components, and the decision payments.
Reserve Deposit places its fourth spendable value, support equipment, in its full hover tooltip rather than exceeding the three-value inline limit.
Drive Deeper and Permanent Seal state their output consequences in the full cost tooltip, while Seal Depths states its output consequence in its effect tooltip.
The shared affordability composite is present in both `available.hidden_trigger` and `custom_cost_trigger` for all ten profiles.
Claim Register, Reserve Deposit, and Repair also put their mission-start gate in `custom_cost_trigger`, so affordable resource colours alone do not establish action availability.

## Parent fixes verified in current source

1. **Ordinary Seal Depths output and exception wording: implemented.**
   `decision_riches_found_seal_depths_tt`, localisation line 354, now says ordinary workings retain the formatted `sealed_depth_output_factor` and explicitly preserves existing partial-seal or bound-account restrictions.
   The output calculation caps the ordinary score at effects line 1188, then applies the sealing reducer at lines 1199–1205 only for `riches_found_depths_sealed` without `riches_found_mine_partial_seal` or `riches_found_account_terms_bound`.
   The factor is 0.75 at constants line 1278.
   The decision sets the persistent seal and applies development and deep-excavation losses at decision lines 4788–4791.
   No clearer for `riches_found_depths_sealed` was found in the linked source search, and shaft restoration at effects lines 2699–2745 leaves that flag intact.
   The previous missing-output finding is superseded, not carried forward as an unimplemented mechanic.

2. **Repair reimbursement ownership: implemented.**
   `decision_riches_found_repair_tt`, localisation line 361, now requires ownership and a reserve still available when the crews arrive.
   This matches `riches_found_stabilization_reserve_can_pay`, triggers lines 521–524, which requires a reserve and excludes occupied mines.
   Decision lines 4893–4897 consume that reserve and return exactly the support-equipment and truck payments.
   `riches_found_spend_stabilization_reserve`, maintenance-effects lines 376–378, consumes the one-use reserve.

3. **Repair factory duration: implemented.**
   The effect tooltip at line 361 and cost hover at line 364 both use `riches_found_decision_duration.long_project`, currently 90 days.
   This matches native `modifier` and `days_remove` at decision lines 4863–4864 and no longer implies that factories remain committed for the separate Restore the Shaft mission's full duration.

4. **All ten factory hover durations: implemented.**
   Every `_tooltip` key in the crosswalk states its exact constant-backed commitment duration.
   The duration constants are admin 30, project 60, and long_project 90 at constants lines 643–645.
   Resource getters and matching texticons remain intact.

5. **Claim Register and Reserve Deposit mission-start text: implemented.**
   `decision_riches_found_claim_register_tt` at localisation line 594 and `decision_riches_found_reserve_deposit_tt` at line 615 both begin `Starts §YSecure the Rush§!.`
   Their source starts that mission at decision lines 173–176 and 460–463.
   The actual mission title is `mission_riches_found_secure_rush: "Secure the Rush"` at localisation line 14.
   The earlier physical audit's “Secure the First Rush” wording is not the current localisation title.

6. **Drive Deeper retention guarantee: implemented.**
   The sole `deep_output_loss_factor` application now follows the ordinary ceiling, at effects lines 1191–1194, before the ordinary sealing reducer.
   The factor remains 0.75 at constants line 1277.
   For a fixed pre-project capped score C, the running project yields 0.75 × C, followed by the same applicable ordinary sealing factor.
   This supports the retention sentence in `riches_found_cost_drive_deeper_tooltip`, localisation line 716, including above-ceiling inputs.
   This is source arithmetic evidence, not observed native engine execution.

The previously fixed compensated-exit effect text also remains aligned.
`decision_riches_found_nationalize_with_compensation_tt`, localisation line 539, includes foreign claim pressure +8, matching decision line 3360.
`decision_riches_found_buyout_tt`, localisation line 553, includes foreign claim pressure −8, matching decision line 3557.
Both mention partner compensation and improved relations, matching the partner helper at partner-effects lines 116–129, which grants compensation and adds the partner's settled-opinion modifier before contract cleanup.

## Remaining gaps and parent follow-up

**Unresolved partner-name cache coverage.**
The two compensated-exit effect tooltips read `[?riches_found_selected_foreign_partner.GetName]` directly, without an existence fallback.
`riches_found_refresh_partner_display`, partner-effects lines 179–208, clears the country cache first and populates it only through a selected mine with an existing contract partner or foreign target.
The inspected decision gates require a controlled mine and contract conditions, but do not independently require this display cache to exist.
No blank, stale, or raw-name result was observed.
The parent should prove cache population for these tooltip contexts or use a guarded getter tied to the actual decision target and contract partner, preserving the named actor when valid.
This remains a display-risk finding, not a confirmed gameplay failure.

**Blocked native fit evidence.**
No native decision-row render route was exposed in the connected tool list.
The exposed GUI renderer was not used as a substitute for these ordinary decision rows.
The longest titles, blocked strings, and full hovers have therefore not been visually verified for clipping, wrapping, overflow, or overlap.
The three-value source budget does not establish native fit.
No standalone Technology Tree Viewer was exposed in that tool inventory, and its package availability was not independently established.
No technology surface is in this task, so this is an availability uncertainty rather than a technology validation claim.

**Incomplete broader dynamic-cost requirement.**
The quotes still resolve to fixed light, standard, and heavy constants through getters and matching affordability components.
Displaying constants dynamically does not implement per-mine scaling by population, development, damage, distance, war, supply, order, exposure, or previous failure.
The parent accepted the ten current vectors for this pass, but the parent prompt explicitly retained the broader dynamic-quote requirement as incomplete.
Any future quote calculation must keep display, affordability, debit, refund, and reserved capacity aligned.
No scaling coefficient or balance target was chosen by this auditor.

## Key, fallback, encoding, and prose findings

Missing key list: none found among the 84 directly linked decision title, description, effect, cost base/blocked/hover, and resource available/blocked keys.
Duplicate key list: none found for those keys across the English localisation files inspected in the earlier bounded pass.
Scripted localisation issue list: no broken cost-getter reference or absent blocked fallback found, with the partner-name cache risk listed separately above.
Visible flag checks from the ten `available` blocks had localisation coverage.
The cost getters call the matching resource affordability components, including exact truck/support inventory tokens and manpower in thousands.
This source agreement is not an executed below/exact/above engine scenario.

No encoding concern was found in the localisation file during the earlier pass.
No sourced or attributed quotation occurs in the assigned text set.
The auditor changed no text, formatting codes, dynamic tokens, or quotations.

Prose before-and-after assessment: vague factory-duration language was replaced by exact durations, overgeneralized reimbursement and retention statements were qualified, and omitted mission starts were made explicit.
No material bloat, obvious explanatory filler, repetitive passage, excessive subordinate structure, or prohibited punctuation was found in the assigned passages.
The earlier suggestions to rename `Claim Register` or replace “Shore the damaged workings” were minor readability suggestions, not required fixes or unresolved semantic blockers.
They do not justify an additional source patch in this read-only assignment.

Cross-surface mismatch notes: the three compensated-exit and repair fixes and the six later bounded corrections above replace the older physical audit's presentation findings.
No workbook was read or edited, so no catalog mismatch is claimed and no invented spreadsheet replacement text is supplied.
If the spreadsheet owner mirrors these action tooltips, the exact final keys and current wording are in the line-linked localisation entries above.

## References and meaningful validation limits

Skills read and applied: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`.
AGENTS.md was read before the original audit, and its scope and source requirements remained authoritative during this bounded follow-up.

Offline and installed references consulted in the original pass:

- `paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md`, lines 311–329, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`: native base/blocked/hover keys, manual custom-cost subtraction, and fixed political-power AI hint.
- `paradox_wiki\Localisation - Hearts of Iron 4 Wiki.md`, lines 184–198, 221–242, 244–259, and 656–686, revision `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`: numeric formatting, texticons, nested keys, and first-matching scripted-localisation fallback.
- `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\modifiers_documentation.md`, lines 2202–2206, revision `00a0eca6d2b3a70ce4b8a0d38997dd609aa0c9349ddcd04c8cac92849425be7e`: native civilian factory modifier schema.
- Installed `common\decisions\_documentation.md`, lines 1–33, SHA-256 `5E7E686B5582F32C38D898D805E17171E88F3BFEEE4A030DEB1884F9726DE019`: acting country and targeted FROM scope plus availability refresh behavior.
- Vanilla `game:common/decisions/AST.txt`, `AST_union_strike`, lines 2–42, source-index revision `cd462879c32f57be2fab9c00e2c16e14a27f3982ad13dbab95f71a5fba97d098`: native timed civilian-factory commitment precedent.

The connected reference-context, search, read, and source-lookup routes returned usable results in the original pass.
The initial Repair decision-inspection request was rejected because declared scenarios were required, then retried with an explicit source-only exact-payment scenario.
That call returned `DECISION_ANALYZED_PARTIAL`, `complete=false`, source revision `aefdfc7d9741c2541b319419394b82330f23aa9edb00bef633a883d8582c5d83`, and a failed decision-coverage check with unresolved definitions.
Its evidence URI is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/14b541182a17afb42ff7b5eeb43fa8492f0b1ac4b0f99066d7503735827f2a20/5056cd7c3ca92e4561e9319bf171fcbf835bbdb1237137dc2ac8157420afc341/decision-72402c10c3f196b3a99e20e9.json`.
Reading it failed with MCP error `-32603: Artifact provenance manifest is unavailable`.
The unread artifact and partial scenario result are not engine, visual, or complete cost validation.

The follow-up re-read the ten changed cost hovers, four corrected effect tooltips, the reordered contribution calculation, and unchanged factors.
No new MCP scenario or render was run for the parent fixes, and no live game execution, probability audit, or complete 92-decision review was attempted.
The meaningful validation here is manual current-source agreement and arithmetic order, with native fit and cache-context behavior explicitly unverified.

Current source SHA-256 identities at the follow-up read:

| File | SHA-256 |
| --- | --- |
| `common\decisions\029_riches_found_decisions.txt` | `EBC33D0F6516E4B88ECBED35BB213F53381C729002226D6AF77B48D6AD5C166B` |
| `common\scripted_triggers\029_riches_found_cost_triggers.txt` | `5B93479FCC2E3367847CD5D97B4A0AE4D4275227A2D55F3F9BABA157D465A0D2` |
| `common\scripted_effects\029_riches_found_effects.txt` | `0F603E0ABB9854441CE62AE69DC41CE845D21A55E2F592D5E49F02A355836D54` |
| `common\script_constants\029_riches_found_constants.txt` | `C478961A3F1024859B7BCA1752C02E26A50F61874B798D51B85BA04770039C71` |
| `localisation\english\029_riches_found_decisions_l_english.yml` | `064994C368B6AF112B192B5E587ED8D32E3E583B44EB5E765F774E3AE2A755F0` |

Changed file: this handoff only.
Changed gameplay IDs and localisation keys by this auditor: none.
No additional plan, package-completion claim, or commit was created.
