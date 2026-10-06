# Bounded CBRN localisation audit

Disposition: implemented audit with parent-accepted wording fixes.
Acceptance basis: parent assigned a read-only final review of the changed text from commit `e08c6fad`, then accepted the concrete corrections below on 2026-10-06.
This report does not establish completion of the CBRN workstream, its two unsupported accepted achievements, or its native evidence gates.

## Scope and findings

Reviewed all 13 achievement families in `localisation/english/cbrn_achievements_l_english.yml`, both reconciliation decision text families at the bottom of `localisation/english/cbrn_protection_l_english.yml`, and `category_cbrn_armored_delivery_support` in `localisation/english/chaosx_units_l_english.yml`.
The scoped check covered 53 keys, including both existing audit-summary fallbacks.
Checked their current achievement predicates, effects, on-actions, decision definitions, recovery predicates, recovery effects, and two scripted-localisation summaries.

- Missing key list: none found in the scoped achievement, custom-tooltip, decision, or summary references.
- Duplicate key list: none in the three owned localisation files, and no duplicate English definition for any scoped key.
- Scripted-localisation issues: none found in `GetCbrnOccupiedAuditSummary` or `GetCbrnExportAuditSummary`.
  Both return real localisation keys, read saved numeric results, and contain no direct formatting glyphs.
- Dynamic text: the restored tooltips reference existing `cbrn_achievement_threshold` constants for protection, pollution, civilian deaths, and military-loss fraction.
  Keep these tokens.
  Vanilla `localisation/english/TAOG_decisions_l_english.yml:503` uses `[?constant:propaganda.SIA.default_propaganda_campaign_cooldown]`, so direct constant access is not categorically unsupported.
  Further useful opportunities are constant-backed coverage, reserve ratio, stability, medical capacity, HQ count, and duration thresholds in the older achievement tooltips.
  These were not expanded in this bounded final pass.
- Encoding concerns: none found in the scoped files.
- Raw flags: both recovery decisions hide their predicates inside custom trigger tooltips and their effects inside hidden effects.
  Achievement conditions use custom override tooltips, which cover their underlying flag predicates.
- Report colour and duplicate popup checks: the parent supplied `report_colour_audit = 0` and duplicate-popup tracking `0` for the owned families.
  No report/news text or popup implementation was edited by this auditor, and those results were not independently rerun here.
- Quotation preservation: no sourced or attributed quotation occurs in the inspected strings.
- Spreadsheet: no workbook or CSV was opened or edited.
  No catalog mismatch claim is made.

## Accepted wording corrections

Parent owns all source edits.
All seven corrections were reread in the working tree after parent application.

| Key | Before issue | Accepted correction |
| --- | --- | --- |
| `chaos_warfare_evidence_survives_DESC` | Vague phrase "carry responsibility into" hides the actual action. | "Capture a biological facility, preserve its documents, and establish responsibility through inspections or international condemnation." |
| `chaos_warfare_quarantine_without_collapse_tooltip` | "the outbreak" implies clearing only one outbreak, while the predicate rejects any ordinary episode in any owned state. | "Contain a catastrophic outbreak, clear every owned state of active biological outbreaks, prevent foreign spread, and retain the required stability, medical capacity, and supply-vehicle readiness." |
| `chaos_warfare_terminal_contagion_DESC` | Overloaded sentence implies current sanctions and contamination instead of their histories. | "Field a complete three-section CBRN Headquarters under terminal doctrine during a chemical land strike. Survive ninety days, remain at war, have faced sanctions, and have experienced either serious Chemical Contamination or a catastrophic biological outbreak." |
| `chaos_warfare_terminal_contagion_tooltip` | Does not clearly require all three sections at the strike, and obscures mandatory sanctions plus one contamination branch. | "Use terminal Chaos Warfare doctrine and research the 1942 Chaos Battalion. Carry out a chemical land strike while a deployed CBRN Headquarters has all three sections, then survive ninety days and remain at war. You must have faced sanctions and experienced either serious Chemical Contamination or a catastrophic biological outbreak." |
| `chaos_warfare_air_still_breathable_tooltip` | "during that chemical war and afterward" suggests continuous postwar tracking instead of wartime tracking plus current protection. | Replace with "throughout that chemical war and when you qualify", retaining both constant tokens and all disqualifiers. |
| `chaos_warfare_antidote_arrived_tooltip` | Omits the same protection requirement for later nerve releases in the containment period. | Add "Maintain that protection for every nerve-agent attack until the state is clean.", retaining all constant tokens and existing conditions. |
| `cbrn_reconcile_export_shipment_records` | Dynamic country names can make an ordinary decision row excessively long. | Recommended static title "Audit Mask Shipment". Recipient identification remains in native targeted-decision presentation and `[FROM.GetNameDef]` in description and tooltips. |

Terminal's revised wording describes country-wide deployed headquarters capacity at the strike.
It does not claim that the headquarters army participated in that strike.
The final logical clarification to both Terminal strings and the static shipment title were applied by the parent and verified in the current files.

Vagueness repairs cover Evidence and Quarantine.
Bloat and overcomplication repair covers Terminal's long sentence and temporal requirements.
No gratuitous repetition, obvious-explanation sentence, em dash, semicolon, implementation-history wording, or banned administrative token was found in the scoped final prose.
All dynamic tokens and mechanics were preserved in the recommended replacements.

## Source and MCP evidence

Recovery descriptions match their actual effects: return confirmed held masks, write off remaining masks and spent unclosed fees, release the recovery block, and leave previously delivered coverage with recipients.
Sources are `common/decisions/cbrn_protection_decisions.txt:483–522`, `common/scripted_triggers/cbrn_occupied_transaction_triggers.txt:187–191`, `common/scripted_triggers/cbrn_export_transaction_triggers.txt:104–111`, `common/scripted_effects/cbrn_occupied_transaction_effects.txt:371–403`, and `common/scripted_effects/cbrn_export_transaction_effects.txt:466–513`.
The armored-delivery category label matches `common/unit_tags/chaosx_categories.txt:9`, its land subdoctrine consumers, and its support-unit consumers.

Live `hoi4.reference_context`, `reference_search`, `reference_read`, and `source_lookup` were exposed and responded successfully.
The occupied recovery decision lookup returned exact source lines 483–500 with revision `5687b3fa88ef5733324f42b38ee356a5de7353f5c5b27679c156fe3d5b109b99`, `complete = true`, and references intentionally disabled.
Read offline `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md` lines 59–72 and 184–215, revision `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`, for key structure, encoding, numeric formatting, and percentage behavior.
Installed `documentation/loc_formatter_documentation.md` context and heading read responded with revision `1fbd9a031fd09100d79bac08dec3c16e19468f23516c5e67c67578156282af08`, but that heading-only read establishes no numeric-constant rule.
The exact installed vanilla constant-localisation precedent above supplies the pertinent implementation example.

The technology inspect/render routes were separately confirmed exposed.
No standalone Technology Tree Viewer route was exposed, and no matching viewer package file was found in the checked repository `.tools` and `.agents` file inventories.
Record this as a package/discovery gap, without treating the technology routes as evidence that a standalone viewer exists.
A narrow `bonus_coverage` request for `category_cbrn_armored_delivery_support`, bounded to three nodes without refresh, did not return a final response during this audit.
The local waiting cell was terminated after repeated pending responses.
The server outcome is unobserved, not established as failed.
The matching `bonuses` render depended on that inspection and was not reached.
No technology artifact URI or final diagnostics were received.
Technology category inspection and rendering therefore remain unresolved evidence gaps.

## Validation limits and remaining work

Source-to-prose verification and scoped reference/key checks ran against the current files.
There is no native decision-panel render evidence for long target-country names or the proposed static title.
No GUI, event-chain, focus-tree, map, live game, or whole-roster audit was requested or claimed.
Technology category inspection does not prove decision-panel fit or native doctrine tooltip fit.
The parent retains responsibility for native evidence gates, final source reread, and the workstream completion verdict.
No gameplay/localisation source patch, workbook edit, CSV edit, or commit was made by this auditor.
Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`.
No skill was created or updated.

## Follow-up: thirty inherited prose and title replacements

Disposition: implemented bounded review of parent-applied replacements.
Acceptance basis: parent assigned the exact thirty before/after entries in `.git/cbrn_takeover_20261006/prose_review_inventory.json` and retained source ownership.
The nine localisation files named by that inventory were the only additional prose scope.
Other owners' `016_mengele` strings were excluded.
All thirty current values match the final inventory.
No missing or duplicate definition was found for those thirty exact keys in their named files.
All dynamic bracket tokens were preserved except the three explicitly approved `[FROM.GetName]` title removals: `cbrn_destroy_contaminated_records`, `cbrn_admit_accidental_release`, and `cbrn_permit_inspection`.
The shortened titles are Destroy Attack Evidence, Admit an Accidental Release, and Permit Inspection.

Two residual semicolons were found in `cbrn_export_protective_equipment_complete_tt` and `sp_cbrn_medical_trial_reward_desc`.
The parent replaced them with periods and clarified recipient opinion and supplier reserve ownership.
The final shipment text reads: "A complete shipment supplies [FROM.GetNameDef] and improves its government's opinion of us. If [ROOT.GetNameDef] meets international compliance terms, successful delivery may ease current Condemnation. The operation ends if either partner becomes ineligible. Undelivered masks return to the supplier's reserve."
The final medical trial text reads: "Trial batches can undergo a full clinical review or enter emergency production. Review earns public confidence but takes time. An emergency schedule carries political risk."
Both were reread in current source.
No remaining banned implementation words, em dashes, or semicolons occur in the thirty values.
The replacements describe physical orders, samples, laboratory papers, and shipping papers without confusing those objects with script bookkeeping.
No sourced quotation was changed.

Narrow semantic checks confirmed the following:

- `bio_battlefield_launch_available_tt` retains the no-release consequence for invalid target or authority.
  `common/scripted_effects/biological_battlefield_effects.txt:474–529` gates actual dispatch behind the native context and payload predicates and uses the rejected-reservation branch without dispatch when context is invalid.
- `cbrn_bio_facility.5.desc` identifies the former custodian and retains accidental-release framing without claiming deliberate use.
  `common/scripted_effects/biological_facility_capture_effects.txt:542–600` uses the exact original arsenal actor where that country exists, dispatches `captured_facility` source with `accident` result, and sends event `.5` to that original actor.
  `events/biological_facility_capture_events.txt` supplies an acknowledgement-only report option.
- `cbrn_answer_inspection_demand_timeout_tt` retains refusal only when the demanding country exists.
  `common/scripted_effects/cbrn_diplomacy_effects.txt:303–315` otherwise clears the demand without calling refusal.
  `common/scripted_effects/condemnation_response_effects.txt:321–337` removes inspectors and observers and adds public Coverup pressure on the refusal branch.
- Evidence destruction still reduces evidence more than sealing, raises Resistance, and adds hidden Coverup consequences.
  `common/scripted_effects/cbrn_occupation_effects.txt:802` starts the destruction branch, and `common/script_constants/cbrn_occupation_constants.txt:229–230` defines suppression as 10 for sealing and 25 for destruction.
  The renamed evidence is physical papers and samples already described by the prior text.
- Admission and inspection still operate on the selected state and preserve earlier attacks, deaths, and contamination.
  Target declarations, `[FROM.GetName]` requirement text, and FROM-scoped effects remain in `common/decisions/cbrn_occupation_decisions.txt:279–398`.
  `common/scripted_triggers/cbrn_occupation_triggers.txt:406–419` and `458–465` retain the control, responsibility, previous-response, and discovery gates.
  `common/scripted_effects/cbrn_occupation_effects.txt:896–936` retains the inspection evidence increase, seal removal, national inspections, and Coverup pressure clearing.
- `cbrn_startup_history_1939_uk_desc` restates its existing mass civilian issue and Parliament attribution claim.
  Removing setup terminology introduces no additional historical quantity, date, or gameplay benefit.
  This is a before/after semantic check, not fresh historical verification.

The remaining replacements preserve their prior conditions and consequences while removing implementation phrasing, shortening titles, or naming concrete evidence.
No additional semantic drift was found in this bounded review.
Long state names no longer expand the three approved static titles, while state requirements and native targeting still identify the selected target.
Native panel fit and target presentation were not rendered or observed.
No MCP retry, game launch, desktop control, workbook/CSV operation, source edit, or commit occurred in this follow-up.
The parent-provided source audit results of two fixed achievement-lifetime defects and 28 passes with 21 baseline fault checks were not rerun here and do not expand this localisation review's coverage.
No unresolved wording decision remains in the thirty replacements.
The existing native evidence gaps and incomplete whole-workstream verdict remain unchanged.

## Final two-key refinement

Disposition: implemented parent-owned wording refinement, verified by this read-only follow-up.
The final tracked inventory is `docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-10-06_prose_changes.json`.
This phase adds one numeric token and does not contradict the earlier phase's token-preservation finding.

`localisation/english/cbrn_diplomacy_l_english.yml:18`, `cbrn_share_forensic_evidence_desc`, restores "detected ordinary biological outbreak".
The ordinary qualifier makes the existing eligible pathogen scope explicit without changing a mechanic or losing a token.

`localisation/english/biological_facility_recovery_raids_l_english.yml:32`, `bio_facility_capture_secure_limited_tt`, replaces "40 percent" with `[?constant:bio_facility_capture_payload.secure_limited_fraction|%0]`.
`common/script_constants/biological_facility_capture_constants.txt:34–41` defines that category as fixed-point data and sets the fraction to `0.40`.
`common/scripted_effects/biological_facility_capture_effects.txt:665–675` binds the same constant to the fraction used by limited recovery's transfer helper.
The numeric scale and binding are correct: percentage formatting should multiply `0.40` by 100, append the percent sign, and show zero decimal places, yielding `40%`.
The final inventory contains both exact current values.
No pre-existing dynamic token was removed, and all other wording in these two values is unchanged from the prior phase.

Parent-provided local reference evidence, retrieved directly because the parent's reference routes were unavailable: offline Localisation wiki lines 196–200 and 214, revision `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`; installed `documentation/script_concept_documentation.md` lines 216–222, SHA-256 `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`; and vanilla `localisation/english/TAOG_decisions_l_english.yml:503`, SHA-256 `42b34845b31c1ddd77bfdbd23aafd775786184f75eec6a5b9fe9c765e6b8f177`.
The earlier successful auditor reference reads remain separate evidence and do not establish the parent's later route health.
The native formatter's actual `40%` display remains an acceptance check.
No native display proof, MCP call, game launch, gameplay/localisation source edit, workbook/CSV operation, or commit was made in this final follow-up.
No new wording issue or uncertainty was found beyond that native display gate.

## Final target-name placement

Verified `localisation/english/cbrn_occupation_l_english.yml:35` and `43`: Destroy Attack Evidence names "the nerve-suppression attack in [FROM.GetName]", and Admit an Accidental Release begins "Publicly acknowledge the toxic release in [FROM.GetName]".
Both shortened titles remain static.
The state-name getter was deliberately relocated from those titles into their descriptions, not accidentally lost.
Permit Inspection already retains `[FROM.GetName]` in its description at line 48.
The getter and existing selected-state binding are unchanged.
The parent reports that `2026-10-06_prose_changes.json` was updated to match this final placement.
This note adds no native display proof or new source, MCP, game, or spreadsheet validation.

## Parent's paired destruction-percentage check

After the specialist's thirty-key review, the parent replaced the adjacent limited-destruction tooltip's static fifty percent with `[?constant:bio_facility_capture_payload.destroy_limited_fraction|%0]`.
This is the thirty-first changed key in the final inventory, not part of the earlier thirty-key claim.
The existing fixed-point value is 0.50 at `biological_facility_capture_constants.txt:42`, and the existing effect reads that same constant at `biological_facility_capture_effects.txt:729`.
The parent read the same local formatting references recorded in `2026-10-06_prose_changes.md`; no earlier token is removed and no coefficient or source effect changes.
The two resulting percentage displays, forty and fifty percent, remain native UI acceptance checks.
