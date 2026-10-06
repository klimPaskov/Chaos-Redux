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
