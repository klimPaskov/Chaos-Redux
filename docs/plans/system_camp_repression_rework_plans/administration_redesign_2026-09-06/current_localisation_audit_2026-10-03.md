# Current camp localisation audit and patch, 3 October 2026

Disposition: implemented source corrections, with final visual evidence blocked or pending.
The parent initially assigned a read-only camp administration, repression, genocide crisis and original Soviet/German/Japanese package audit, then explicitly authorized the three bounded localisation files below for contextual tooltip and blocked-reason corrections.
A follow-up parent instruction authorized the pure institution progress projection, short native civil status getter and paired UI effect documentation listed below.
Other agents are editing the shared tree, so these hashes identify the reviewed state and this report does not attribute the complete Git diff to this subagent.
No gameplay, GUI layout, workbook, CSV, index or commit changes were made.

## Changed files and identifiers

| File | Reviewed SHA-256 |
| --- | --- |
| common/scripted_localisation/camp_administration_country_localisation.txt | b925eba0dafa3dbe90c7dd9d3bb7ce54ceee2da510e90a8823dcf9622ef5c03d |
| common/scripted_localisation/camp_administration_ui_localisation.txt | 7f6dd202c43810a5634272a51e83b9851f728d3ea6608c72061ae177cf344f8e |
| common/scripted_effects/camp_administration_ui_effects.txt | 6402e97cef4a38250acb64c4bf5964d5331b3e6da95906d22f30b6638ef3087a |
| common/scripted_effects/camp_administration_ui_effects.md | 9ec2ae063ba244043da4f8cdab9902d39ee9298efd7352bad4867a5fcea9a44a |
| localisation/english/camp_administration_ui_l_english.yml | c705648eed7041af330cf62b76e26a9289512f9420ce692410b2be065e04051a |
| localisation/english/camp_administration_country_l_english.yml | 38e66fec368ae094cbd78f23df6e10f96051bad50a942bc92a048808975b0637 |

- `common/scripted_localisation/camp_administration_country_localisation.txt`: added `GetCampAdminInstitutionTooltip`; repaired `GetCampAdminCountryAction1BlockedReason` and `GetCampAdminCountryAction2BlockedReason`.
- `localisation/english/camp_administration_ui_l_english.yml`: changed `camp_admin_institution_tt`, `camp_admin_budget_tt`, `camp_admin_option_role_killing_tt`, `camp_admin_option_role_killing_existing_tt`.
- `localisation/english/camp_administration_country_l_english.yml`: changed `camp_admin_country_authorize_tt`; added `camp_admin_institution_inactive_tt`, `camp_admin_civil_action_1_blocked_general`, `camp_admin_civil_action_2_blocked_general`.
- Added bounded source fixture evidence in `current_localisation_getter_fixtures_2026-10-03.json` beside this report.

## Before and after

The Institution Program panel used `camp_admin_institution_tt` at `interface/camp_repression_ledger.gui:50`, universally promising a research award and quoting 12 support equipment and 5 Political Power per funded month.
The panel also shows civilian programs whose actual costs differ and which do not grant research awards.
The tooltip now selects the existing exact route-specific text through `GetCampAdminInstitutionTooltip`.

| Context, in first-match order | Selected localisation | Actual funded installment or outcome |
| --- | --- | --- |
| Civilian property claims | `camp_admin_civil_usa_claims_text` | 10 support, 12 PP, six funded months, property burden resolved |
| Civilian review | `camp_administration_civil_action_two_tt` | Existing country-specific review getter, 15 support, 8 PP, three funded months |
| Authorized civilian policy without reform | `camp_administration_civil_action_one_tt` | Existing authority getter, 10 support and 5 PP, continuing policy |
| Other civilian state | `camp_admin_institution_inactive_tt` | No institutional installment or research award asserted |
| Major-country archival work | `camp_admin_archives_tt` | 8 support, 10 PP, six funded months, records preserved |
| Major-country oversight | `camp_admin_oversight_tt` | 12 support, 5 PP, six funded months, authority dispute reduced |
| Valid major-country program | `camp_admin_country_authorize_tt` | 12 support, 5 PP, program progress and eligible single-use research award |
| No matching program | `camp_admin_institution_inactive_tt` | Neutral inactive state |

These claims were checked against `camp_administration_civil_monthly`, `camp_admin_country_tick_authority`, `camp_admin_country_tick_aftermath`, `camp_admin_country_tick_institution`, `camp_admin_try_pay_project`, and the civil/country constants.
The universal monthly payment envelope still retains maintenance and protected stock first.
No debit, progress or award helper was changed.

Civilian blocked getters previously fell into major-country coercive mandate and upfront stock reasons.
The repaired action-one getter preserves the institutional-slot reason first and uses the site-records reason only for the democratic French release/conversion branch which actually requires it.
A civilian fallback then precedes major-country budget, mandate, PP and support reasons.
The repaired action-two getter preserves its slot-first ordering, uses the site-records check for civilian release/review and preserves the United States postwar claims bypass, then stops at its civilian fallback before major-country reform cost reasons.
Authorization is described as having no immediate cost, with monthly funding explained separately.

## Coverage and findings

Missing key list: no missing keys found in the 1,201 explicit visible text, tooltip, event option and scripted-localisation branch references checked across 68 scoped source files before this patch.
The scoped getter and substitution scan covered 1,446 camp, genocide, Soviet, German and Japanese package keys and found no undefined unscoped or `This` getter references or missing `$key$` substitutions.
The new getter branches and added keys were checked after both patches.
A final implicit-key sweep found no missing decision title or description for the administration, repression or genocide-crisis decision files.
GUI element names were excluded from localisation requirements because they identify controls rather than displayed strings.
Implicit keys and engine-generated helper tooltip presentation have source coverage limits and are not claimed as engine proof.

Duplicate key list: none found among the scoped keys.
Scripted-localisation issue list: the contextually incorrect institution tooltip and civil blocked fallback ordering are repaired as listed above.
No unmatched new scripted-localisation reference remains.
Dynamic text opportunities: the existing major-program tooltip still spells out the 50 to 100 percent award range and two annual awards, whose current constants match the prose.
This is a tuning synchronization opportunity rather than a current mechanical mismatch.

Current Records wording uses recorded custody rather than claiming every recorded person is a usable living worker.
`camp_admin_project_origin_uncertainty` counts custody and occupation hosts with a deduplicated union, and `GetCampAdminUnknownOriginNote` has an explicit blank fallback.
`camp_admin_records_unknown_origin_note` uses escaped newline tokens, not a raw multiline quoted string.
Unidentified territorial losses are not claimed as attributed camp deaths.

`soviet_gulag.2.d` resolves to the famine description and `soviet_gulag.2.shortfall` resolves to its separate option text.
`soviet_gulag_relief_funded_tt` includes the full motorized/train/support quote through `$sov_emergency_famine_relief_cost$` and the signed dynamic negative two percent stability cost.
The equipment quote is 120 motorized, 18 trains and 180 support equipment at this reviewed source.
The helper consumes the same equipment and applies the same stability constant.
The native decision PP cost remains separately presented by the decision consumer.
The institution receipt flag `camp_admin_institution_slot_active` has a player-facing key in the requirement-flags localisation.

File encoding concerns: no concern found in the inspected scoped UTF-8 localisation files, and the two patched YAML files retain BOM.
The UTF-8 scripted-localisation file contains no added direct formatting characters.
Console display substitutions for some non-ASCII text were transport/output effects, so checks read actual file bytes and decoded source rather than treating console replacement glyphs as a file defect.

## Prose review

Vagueness: replaced the institution panel's context-free research promise with actual selected program and completion text, while an inactive branch explicitly identifies that no institutional payment is due.
Bloat and overcomplication: kept existing country-specific quote text instead of adding another full explanation of each program.
Obvious explanation and repetition: the contextual getter reuses the authoritative order tooltip, which keeps cost and consequence wording synchronized across the two surfaces.
Style-rule repair: replaced semicolons with periods or a natural conjunction in `camp_admin_budget_tt`, `camp_admin_option_role_killing_tt`, `camp_admin_option_role_killing_existing_tt`, and `camp_admin_country_authorize_tt`.
No clear specific passage was changed solely for voice.

The two confirmed semicolon repairs in the parent-owned `camp_administration_integration_l_english.yml`, `camp_admin_generic_reform_cost_tt_tooltip` and `camp_admin_generic_reform_effect_tt`, were handed to the parent.
A final source reread confirms that both were repaired by the concurrent owner.
Legacy ledger strings also contain semicolons or an em dash: `repression_ledger_category_summary_active`, `repression_ledger_category_summary_reform`, `repression_ledger_gui_phase`, `repression_ledger_gui_summary_active`, `repression_ledger_gui_summary_reform`, `repression_ledger_gui_summary_dormant`, `camp_gui_dismantle_selected_site_tt`, `camp_ui_selected_status_tt`.
They are outside the three newly assigned patch files and were not silently rewritten.
Their presentation reachability outside the current administration layout remains a parent review item.

Sourced quotations: no sourced or attributed quotation was edited.
Existing dynamic tokens and formatting were preserved in all prose repairs.
The old universal institution cost tokens were moved out of that key by replacing its text with a getter which returns the matching existing cost tokens, so their context is corrected rather than their information deleted.
Historical event claims were checked for concrete readable prose without inventing additional lore or silently correcting attributed source material.

## Cross-surface and spreadsheet handoff

The institutional order tooltips are reused by the panel, so their current costs and outcomes are consistent after the getter correction.
No event-log, event-details, evolution-detail or cluster-detail key was changed by this patch.
No workbook or export-only CSV was edited or used as a source of truth.
A workbook wording mismatch was not established in this bounded pass, and workbook correspondence remains unverified rather than asserted current.
The three new tooltip-only keys above need no catalog replacement unless the parent or spreadsheet owner identifies a matching catalog field.

## Meaningful validation and limits

Ten source-only first-match getter fixtures selected the expected contextual branch, including civil claims over review, review over policy, civilian reform/inactive, archives over oversight, oversight over major program, valid and invalid major programs and unsupported countries.
`current_localisation_getter_fixtures_2026-10-03.json` records the fixture expectations and exact source hashes.
The fixtures explicitly assume domain predicate booleans and do not execute Clausewitz triggers or prove campaign eligibility.
Source assertion confirms that the civil fallback precedes the major coercive mandate and payment reasons.
Source reading verifies that the displayed quotes match their actual named payment helpers and current constants.

Production overflow, wrapping, alignment and tooltips remain unresolved without a completed MCP render.
The native civil status row at `interface/camp_repression_ledger.gui:50` now uses the short states listed below rather than full progress sentences.
Installed font metrics establish source advance widths, without claiming production glyph bounds or pixel acceptance.
No source-only check is offered as equivalent visual evidence.
No game was launched, no additional logs were sought, and the supplied cycle-one snapshots predate the parent's repairs.
A fresh clean runtime claim is therefore unavailable.

## MCP and reference evidence

Connected metadata exposes reference context/search/read, source lookup, GUI inspect/render and event inspect/render routes.
The `hoi4.reference_context` localisation request with `limit:4` returned `timed out awaiting tools/call after 600s`.
Local fallback sections were therefore read directly and retained below with content SHA-256 revisions.
The reference search for localisation variable formatting also returned `timed out awaiting tools/call after 600s`.
The first narrow GUI inspection returned the same 600-second timeout.
The event trace for `soviet_gulag.2` was rejected with MCP `-32602`, because its selector lacked the required discriminator `kind` from `event | namespace | file | source | node | manifest`.
That rejected request is not accepted as event inspection coverage.
The source lookup for `custom_effect_tooltip`, corrected GUI inspect and GUI render had not produced final artifacts at this handoff snapshot.
The first narrow GUI inspect mistakenly named `camp_repression_ledger_window`; it is not accepted as coverage.
A corrected inspect request names the actual `repression_ledger_window`, disables generated scenarios and uses `camp_current_localisation_oct3`.
The render request names `repression_ledger_window`, requests the same scenario identity and a declared USA context at 1920 by 1080 with scale 1, and remains pending.
The parent has separately reported full and narrow requests under `mcp/origin_pause_gui_2026-10-03` ending in `maxTotalTimeout`, followed by a current native full inspect `INTERNAL_ERROR` and render `JOB_WORKER_EXIT` with zero artifacts.
There is no current production artifact URI from this subagent to cite.

Standalone Technology Tree Viewer: no separately named viewer tool was present in connected metadata, although `hoi4.tech_inspect`, `hoi4.tech_render` and `hoi4.tech_compare` were exposed.
Record that as a standalone viewer package gap, with service health unproved.
No new technology tree, focus tree or map surface was added or changed in this localisation patch.

| Directly read reference | Lines | Content SHA-256 revision |
| --- | --- | --- |
| paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md | 184-211, 656-685 | 1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064 |
| C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md | 125-160 | 884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7 |
| C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_guis/_documentation.md | 1-50 | 43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838 |
| C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_localisation/00_scripted_localisation.txt | 13-19 | 6f490e33736f4dc31568add5753a1afdef916f3993804febfbbe6d1583827587 |

The offline localisation sections establish percent/sign/decimal formatting and first matching scripted-localisation branch behavior.
Installed contextual-localisation documentation establishes scope-specific object lookup.
The vanilla scripted-localisation file supplies a bounded `defined_text` precedent, and installed scripted-GUI documentation identifies player context and named window attachment.
Skills applied: chaos-redux-events, chaos-redux-subagents, chaos-redux-decisions-missions, and the scoped inspection guidance in chaos-redux-scripted-gui.
No skill was changed.

## Remaining work and uncertainty

Parent review and integration of the six source/documentation edits is required.
Resolve presentation reachability of legacy strings as needed and obtain the final production GUI artifacts before claiming visual completion.
The broader camp package's engine state, unrelated event families, full special-project/focus content and workbook synchronization are outside this bounded localisation proof.
No fallback mechanic or simplification was introduced by this patch.
No separate expansion plan was written because the confirmed issues were contextual text selection and prose, not missing gameplay design.


## Follow-up native institution value and status repair

Disposition: implemented under the parent's explicit follow-up ownership instruction.
Added country-scoped `camp_admin_project_institution_progress` in `common/scripted_effects/camp_administration_ui_effects.txt`, called by `camp_admin_refresh_interface` in place of the former single-counter projection.
Its only written normal variables are `camp_admin_gui_institution_progress` and `camp_admin_gui_institution_target`.
It selects active civil claims and review, major archives and oversight, then an active or saved suspended major-country institution program.
It divides the actual selected progress counter by the matching duration, protects zero targets, clamps the display fraction to zero through one, and leaves an inactive unpaid slot without a displayed target.
A saved suspended program requires a major-country kit, a nonzero program identity and positive paid progress, so an empty halted slot does not invent progress.
It never sets flags, consumes resources, advances program counters, touches population/custody/cause ledgers or grants an award.
The documentation paragraph is in `common/scripted_effects/camp_administration_ui_effects.md` beside interface refresh documentation.

Changed `GetCampAdminInstitutionProgress` in `common/scripted_localisation/camp_administration_ui_localisation.txt` to select the value when the projected target is positive, which retains paid suspended progress after the slot flag clears.
Changed `camp_admin_institution_progress_value` to `Funded progress: [?camp_admin_gui_institution_progress|%0]`.
Changed the civil branch of `GetCampAdminInstitutionStatus` to `camp_admin_civil_institution_status`, which calls new `GetCampAdminCivilInstitutionStatus`.
The full `GetCampAdminCivilInstitutionSummary` branches and existing descriptive texts remain intact.

| New status key | Final wording | Installed font advance width |
| --- | --- | --- |
| `camp_admin_civil_status_claims` | Property claims | 105 |
| `camp_admin_civil_status_review` | Review and release | 126 |
| `camp_admin_civil_status_claims_complete` | Property claims settled | 157 |
| `camp_admin_civil_status_conversion` | Civilian conversion | 124 |
| `camp_admin_civil_status_funded` | Administration funded | 150 |
| `camp_admin_civil_status_authorized` | Awaiting administration funding | 215 |
| `camp_admin_civil_status_inactive` | No active review | 110 |

These are source advance widths including installed BMFont kerning against the 388-pixel native text-box width.
They are not an MCP production render or full glyph-bound measurement.
The eighth added key, `camp_admin_civil_institution_status`, contains `[This.GetCampAdminCivilInstitutionStatus]`.
No native GUI coordinates changed.

`current_institution_projection_source_tests_2026-10-03.py` reuses the existing `foundation_source_tests.Runtime` rather than creating a replacement policy mapper.
It loads the actual current effect, major-country trigger and civil/country constants.
Eleven projection fixtures pass: civil claims at 50 percent, civil review at one third, archives at 50 percent, oversight at two thirds, active major program at 50 percent, suspended major program at one third, zero target blank, inactive unpaid blank, suspended unpaid blank, and upper/lower clamping.
Each fixture compares complete country and state snapshots and proves that only the two display variables changed, with no payment, death logging or temporary variable mutation.
Each fixture also runs the actual `GetCampAdminInstitutionProgress` branch through the existing runtime's condition evaluation and verifies visible-value versus blank selection.
Seven actual short-status getter fixtures pass, including claims before review, review before funded policy and funded before authorized policy.
Font advance checks read `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/fonts/hoi_18mbs.fnt`, SHA-256 `46710d2d1c68162e54f397df2293686f9712bdd7d79f08a3b8db4be46c7c656c`.
Results and final source hashes are in `current_institution_projection_source_results_2026-10-03.json`.
The earlier ten tooltip fixture results retain their pre-projection source identities and are prior-source evidence, not a claimed final-source render.

Prose effect: replaced long civil completion/progress sentences in the single native status row with specific short states, leaving the actual percentage to its separate progress row and full descriptions to their existing summaries/tooltips.
All new visible keys and dynamic getter calls resolve in a final source coverage sweep.
No sourced quotation, cost, route identity, consequence or existing dynamic formatting token was removed.
The overall visual gate remains blocked by the production MCP failures above.

Follow-up variable arithmetic reference: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`, directly read lines 2695-2711, 3609-3622, 7888-7904, SHA-256 `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.

Follow-up variable arithmetic reference: `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`, directly read lines 712-715, 772-776, 792-795, SHA-256 `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`.


## Final inclusive authorization quote alignment

The country owner changed `camp_admin_country_can_commit` and `camp_admin_country_archives_available` to inclusive comparisons under the unchanged monthly/archive quote constants.
The reviewed country trigger SHA-256 is `2a4a63a60f1335a4e45eab059f66a9b6619e231c1ed95324bfc959c9b9bfaa76`.
Under the parent's final instruction, `GetCampAdminCountryAction1BlockedReason` now uses `NOT check_variable ... greater_than_or_equals` for `political_power` and `num_equipment@support_equipment`, matching the inclusive authorization predicate.
Its civil fallback and all institution progress/status branches remain intact.
The two blocked prose keys `camp_admin_country_action_1_blocked_pp` and `camp_admin_country_action_1_blocked_support` now say ?at least? the quote, with the latter explicitly naming support stock.
They continue to state that payment occurs only during a funded month, preserving the separate maintenance/reserve/budget payment contract.
No cost or payment semantics changed.

Four additional parsed-production fixtures pass at exact quotes, one fixed-point unit below each resource quote separately, and just above both quotes.
They evaluate the actual two getter trigger bodies through the existing runtime and compare them with the actual `camp_admin_country_can_commit` predicate.
Exact quotes select neither resource-shortage reason, each individual shortage selects its matching reason, and no scope is mutated.
The eleven projection and seven status fixtures were rerun with the final source and still pass.
Final hashes are recorded in `current_institution_projection_source_results_2026-10-03.json`, while `current_localisation_getter_fixtures_2026-10-03.json` keeps its earlier fixture lineage and separately lists current source hashes.
No new MCP requests or Git operations were issued for this final consistency update.


## Final saved institution location repair

The parent authorized one further value-only change to `GetCampAdminInstitutionPlace` in `common/scripted_localisation/camp_administration_country_localisation.txt`.
Its former active-slot gate hid a saved program location after an ordinary halt even though the program, location and paid progress remained available for resumption.
The getter now requires a positive program identity and an existing positive `camp_admin_institution_state_id`, independent of the active-slot flag.
A halted or captured saved program therefore retains its plain state-name value through the unchanged `camp_admin_institution_active_place` localisation.
The name implies neither current operation nor authority and invokes no action helper.
A zero/missing state ID, zero program identity, national archive, national oversight or civil review without a single saved program site selects `camp_admin_blank`.
No role, work, release, archive or metadata action gate was changed.
No additional source file, cost, layout or Git edit was made for this repair.

Nine actual-getter fixtures pass for active, halted saved, captured saved, zero state, missing state, national archives, national oversight, civil review and zero-program stale-state cases.
Each evaluates the production getter through the existing source runtime, compares complete country/state snapshots, and observes no scope mutation, payment or death logging.
The eleven projection, seven status and four inclusive quote fixtures were rerun and still pass on the current shared source snapshot.
Final source hashes were refreshed in both existing evidence JSON files, including concurrent owner changes to UI effects and country triggers without attributing those changes to this subagent.
The final country localisation SHA-256 is `b925eba0dafa3dbe90c7dd9d3bb7ce54ceee2da510e90a8823dcf9622ef5c03d`.
The final shared country trigger SHA-256 at this fixture run is `dff35a3956cd8c507a787ad28b33315196537e42e04dd566d7d4fcc3a0e3af17`; the earlier inclusive-quote hash above records its prior owner snapshot.
The final shared UI effect SHA-256 at this fixture run is `6402e97cef4a38250acb64c4bf5964d5331b3e6da95906d22f30b6638ef3087a`.
Production MCP visual completion remains blocked and no new MCP requests were issued.


## Final read-only USA release wording coverage

The parent's repaired `usa_release_detainees_under_supervision_desc` describes verified supervised release, relief of displacement/court challenges and continued security administration while sites remain active.
It no longer claims a lasting reduction of security reach.
`usa_release_detainees_under_supervision_effect_tt` delegates to `$camp_rework_usa_release_order_effect_tt$`, so the old and current effect surfaces use the same wording.
The shared effect tooltip uses `[?constant:camp_rework_equipment_cost.support_equipment|0]`, whose current quote is 180 support equipment, and states that equipment is spent only on a confirmed release.

Source reading of `camp_rework_usa_release_detainees_under_supervision` confirms that `camp_admin_release_actual_k > 0` gates the history entry, support consumption, relief values and reform flag.
The named support-consumption helper reads the same equipment-cost constant.
`camp_rework_update_colonial_country_monthly_bridge` resets `wartime_security_reach` from active site count and clamps displacement and court-challenge pressures from zero to the configured maximum, so the repaired prose matches the final bridge rather than the intermediate reach decrement.
The native decision retains its separately presented Political Power charge and refunds it if the release order was not accepted.
The custom requirements tooltip matches current USA authority/control, consistent living custody rows and the recognized mandate gate before civil-administration handoff.
No remaining missing reference or incorrect mechanical claim was found in these three assigned USA keys.
No source or prose edit was made in this read-only extension.

The final bounded reference sweep covers 68 source files and 1,213 distinct explicit text references, with no missing referenced keys.
The three USA keys are each defined once, their substitution resolves, and the dynamic support quote token is retained.
Exact reviewed wording, source locations and current hashes are recorded in `current_usa_localisation_coverage_2026-10-03.json`.
The earlier tooltip, projection, status, place and quote fixture evidence retains its own source identities and source-only limitations.
The origin owner's empty closed-history warning repair remains a separate gameplay/display-predicate responsibility and is not declared fixed merely from this localisation scan.
No new native pixel claim, MCP request, workbook edit or Git operation was made.

| Final USA/source review file | SHA-256 |
| --- | --- |
| localisation/english/camp_repression_country_kits_l_english.yml | 16ab06d5745c7875137eb1cdf8fc800a22f4722b80ab48e61aaecc6e11f331b5 |
| localisation/english/camp_repression_rework_l_english.yml | b7f0d42693b03d3e5d0be33d21804b2b134eb4b01803aa99906aefd59c9da0f6 |
| common/scripted_effects/camp_repression_colonial_country_effects.txt | 343827a57c4eeefbf6839988894d693f7a8c961435527a97658e12b2df271b48 |
| common/decisions/camp_repression_colonial_country_decisions.txt | 7e1c49de4433a9bdbaa9445592076c700c0ec9fc07077b5488c934c5fcfd8a47 |
| common/scripted_triggers/camp_repression_rework_triggers.txt | ece4ff86dbbd96e160c843616d090f1fc25356530e6545fd84189ae7292ba10d |
| common/script_constants/camp_repression_rework_constants.txt | 4c55a56e61f436b449a625c69e2f4b9fed2c3bcf67411e4918347d38980360e8 |
| common/scripted_effects/camp_administration_ui_effects.txt | 6402e97cef4a38250acb64c4bf5964d5331b3e6da95906d22f30b6638ef3087a |
| common/scripted_triggers/camp_administration_ui_triggers.txt | 7df9104b8d1c707e0e780b0a3838d1393709ef5be0393a5d4f017271ddde460f |
| common/scripted_triggers/camp_administration_country_triggers.txt | dff35a3956cd8c507a787ad28b33315196537e42e04dd566d7d4fcc3a0e3af17 |
