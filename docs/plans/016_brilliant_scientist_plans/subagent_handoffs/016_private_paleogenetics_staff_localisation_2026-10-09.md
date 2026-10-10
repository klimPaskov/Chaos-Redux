# Private Paleogenetics staffing localisation review

Disposition: implemented bounded localisation patch, ready for parent integration review.
Acceptance basis: the parent's explicit 2026-10-09 bounded localisation assignment and staffing contract, with current source checked against `016_private_paleogenetics_staff_integration_2026-10-09.md` and the core API/handoff.
The exact accepted parent file is `docs/plans/016_brilliant_scientist_plans/016_private_paleogenetics_staff_integration_2026-10-09.md`, read in full after the parent clarified its earlier shorthand.
The parent's explicit contract and the located integration document agree on 250 personnel, 100 handlers, 150 veterinary staff, nominal 100 concrete Support1, UNIVERSAL 100/50/25 quotes, native two civilian factories for 60 days, and returnable personnel allocation.
The parent identifies that accepted plan as already committed in `9be5ce075`; the earlier shorthand was not a literal filename and leaves no missing-file uncertainty.
The plan also assigns cleanup to the owner and preserves original actor-bound release obligations after programme loss.
No full Event016 or private-payoff completion claim is made.

## Ownership and delivered files

The assigned handoff did not exist when checked; the existing Event016 subagent_handoffs directory and staffing core handoff established its owner and location.
Changed only these assigned destinations:

- `localisation/english/016_mengele_paleogenetics_staff_l_english.yml`: fourteen prose keys changed and two numeric keys added.
- `common/scripted_localisation/016_mengele_paleogenetics_staff_localisation.txt`: two constant-backed numeric getters added.
- This single assigned handoff.

No gameplay, paired API, workbook, export CSV, asset, model, unit, game, Git or index writes occurred.
The parent owns integration and commit.

## Exact changed prose keys and final wording

All keys below live in the assigned English localisation file.
Literal `\n` and existing state/status calls are retained.

| Key | Final wording |
|---|---|
| mengele_event016_paleogenetics_train_staff_desc | [This.GetMengelePaleogeneticsPaidPair]\nTrain [This.GetMengelePaleoStaffHandlers] handlers and [This.GetMengelePaleoStaffVeterinaryStaff] veterinary staff over [This.GetMengelePaleoStaffDuration] days. These personnel remain reserved until released. |
| mengele_event016_paleogenetics_demobilize_staff_desc | [This.GetMengelePaleoStaffStatus]\nRelease the personnel still allocated to the sites. Supplies used in completed training are not returned. |
| mengele_event016_paleogenetics_complete_staff_training_desc | [This.GetMengelePaleoStaffStatus]\nFinish training and confirm the existing payment. No further payment is required. |
| mengele_event016_paleogenetics_recover_staff_release_desc | [This.GetMengelePaleoStaffStatus]\nReturn the personnel and unused supplies still owed. An unconfirmed transfer will not be repeated. |
| mengele_paleo_staff_requirements_tt | The Paleogenetics programme and restored-creature operations must be active. Own and control both commissioned sites, with their roads and hatchery industry repaired. Release any previous personnel allocation and resolve its outstanding transfers.\n[This.GetMengelePaleogeneticsPaidPair] |
| mengele_paleo_staff_release_requirements_tt | The allocated personnel and training supplies must belong to this country. Any transfer awaiting confirmation cannot be repeated.\n[This.GetMengelePaleoStaffStatus] |
| mengele_paleo_staff_completion_requirements_tt | The fully funded team must remain assigned to the original repaired sites. Its training period must have ended and the programme must be active. |
| mengele_paleo_staff_started_tt | Assign personnel and training supplies to the selected sites. Training requires the full team and payment to be confirmed.\n[This.GetMengelePaleoStaffStatus] |
| mengele_paleo_staff_cancelled_tt | End the training assignment and release the allocated personnel and unused supplies. Any unconfirmed transfer remains pending.\n[This.GetMengelePaleoStaffStatus] |
| mengele_paleo_staff_completed_tt | The team can serve the reserve and hatchery once training and payment are confirmed.\n[This.GetMengelePaleoStaffStatus] |
| mengele_paleo_staff_released_tt | Release the personnel and unused training supplies still owed. Any unconfirmed transfer remains pending.\n[This.GetMengelePaleoStaffStatus] |
| mengele_paleo_staff_status_uncertain | A transfer of personnel or training supplies remains unconfirmed and will not be repeated. |
| mengele_paleo_staff_status_suspended | Service is suspended. The trained team remains allocated to the sites. |
| mengele_paleo_staff_status_settlement | The team remains allocated while its training payment awaits confirmation. |

Added keys: `mengele_paleo_staff_handlers_value: "[?paleo_staff_display_handlers|0]"` and `mengele_paleo_staff_veterinary_staff_value: "[?paleo_staff_display_veterinary_staff|0]"`.
Added getters: `GetMengelePaleoStaffHandlers` reads `constant:mengele_paleogenetics_staff.handlers`; `GetMengelePaleoStaffVeterinaryStaff` reads `constant:mengele_paleogenetics_staff.veterinary_staff`.
Each sets its own temporary display value and selects its numeric localisation key.
No existing selector, gate, amount, icon, formatting token or persistent gameplay field was changed.

## Audit findings and before/after

Missing key list: none among the six native decision titles/descriptions, custom requirement/effect/cost consumers and all assigned scripted-localisation branches.
Duplicate key list: none for the final assigned keys across English localisation files.
Scripted localisation issue list: no unresolved assigned getter or branch-key references found.
Identity protection remains intact: held personnel and supplies due display only after `staff_identity_is_visible`, requiring an existing country, both receipt flags, matching original actor and a positive transaction.
The qualified branch independently requires the stricter current receipt.

Dynamic opportunities implemented: the training description previously said only “one team”; it now shows the existing constant-backed 100 handlers and 150 veterinary staff.
Duration, workforce, support quote, CIC, held/due amounts and frozen state names were already dynamic and remain so.
The paired getter still selects `mengele_event016_paleogenetics_paid_pair`, whose names use `This.mengele_event016_paleogenetics_paid_reserve.GetName` and the equivalent hatchery expression.
No raw serials, tables, separators or telemetry were introduced into player text.

Prose review grouped by issue:

- Vagueness: “Their allocation remains committed” becomes a direct statement that personnel remain reserved; “one team” becomes the specific handler/veterinary composition.
- Bloat: “Complete the outstanding settlement using the recorded payment” becomes “Finish training and confirm the existing payment.”
- Obvious explanation: retained the useful no-further-payment statement because the recovery decision must not imply another purchase; no button-title explanations were added.
- Repetition: existing conditional status calls remain useful across individual decision hovers; amounts are not duplicated in ordinary descriptions.
- Overcomplication: “training timer finished” becomes “training period must have ended”; “recorded transfer still awaiting confirmation cannot be issued again” becomes a direct no-repeat requirement.
- Style and truthfulness repair: “The team's remaining personnel allocation is returned” falsely asserted full success before a potentially partial native credit; the replacement describes the release action and preserves pending transfers.
The old uncertain status claimed all further transfers were suspended, although one independent resource may still be recoverable; the replacement applies the no-repeat restriction only to an unconfirmed transfer.
The old suspended status prescribed only control/repair as a remedy, although provider/entitlement/pair loss also suspends qualification; the replacement reports the actual suspended service without an incomplete diagnosis.

Cross-surface mismatch: action tooltips now agree with actual partial allocation, release and acknowledgment semantics in the core API.
The existing paired construction and ordinary neutral Prototype/production remain separate and unchanged.
No event-log, event-detail, evolution or cluster key was changed.
The workbook was neither edited nor inspected in this bounded decision-text pass, so catalogue equality is not claimed.
If the spreadsheet owner has mirrored staffing prose, the exact final keys and wording above are its handoff; no catalog-specific mismatch has been established.

Encoding concerns: none found in the owned files after the patch.
The English file retains UTF-8 BOM; formatting remains in YML rather than scripted localisation.
Quotation preservation: no sourced or attributed quotation appears on the inspected staffing surfaces.
All pre-existing dynamic calls, numeric fields and formatting tokens were preserved; the two staff-composition calls were added.
No quote wording or historical claim was invented.

## Meaningful validation and references

An inline, no-output-file Node check executed the final scripted-localisation trigger branches through the existing actual-source `StaffVM`, using its real quote and staffing gates.
Twenty-six selector scenarios passed: nominal/50/25 support prices one below/exactly at/one above cost, manpower 249/250/251, malformed quote, both new role counts, CIC/duration, unstaffed/training/qualified/suspended/settlement, partial allocation, in-flight transfer, foreign actor and nonpositive transaction.
The partial allocation case held 125 personnel and zero supplies due and selected the owed-release status rather than claiming a trained full team.
Selectors caused no native writes or persistent variable changes.
Final keys were checked against every assigned scripted branch and native tooltip consumer, with an English duplicate scan restricted to these keys.
Native primitives and paired eligibility remain the existing fixture boundaries, not observed engine behavior.

Current reused `.tmp/event016_paleogenetics_staff/native_results.json` records 17 native source cases, including selection versus reserved entry, real Personnel claim, cancellation/restoration, programme-loss cleanup, human navigation/AI reachability, completed-training recovery hiding, non-sale and expired-sale handling, 50/25 fee boundaries, inert observation/CXT and zero-debt in-flight protection.
Current reused `.tmp/event016_paleogenetics_staff/core_results.json` records 57 real receipt/API cases, for 74 parent/core source cases in total.
These were read and reused without claiming a new run by this localisation reviewer.
This review does not relabel either suite as renderer or engine proof.

The inline row remains two icons and two amounts, with no literal cost labels and no factory value: `support_equipment_text_icon` and `manpower_texticon`.
The complete hover retains all three resource commitments and duration.
Support sprite definition was read at `interface/chaosx_texticons.gfx:90-94`; native manpower sprite is at vanilla `interface/texticons.gfx:111`.
Source bounds read in vanilla `interface/countrydecisionview.gui:515-565,631-674`: title widths 280/300, cost-and-timer width 320 and height 32.
Nominal and blocked amounts are three or fewer digits; invalid support quote uses the existing two-word “Quote unavailable” fallback and does not print a diagnostic zero.
These source bounds and compact strings support a bounded text review but do not prove clipping, wrapping or font metrics at any resolution.
Shared native view wiring was not changed.
Whole-person whole-equipment display is supported by the explicit one-unit quote quantum in the staffing quote and `common/script_constants/chaosx_universal_cost_constants.txt:23`, with producer contract in `common/scripted_triggers/chaosx_universal_cost_exact_triggers.md:10-20` and source initialization at `.txt:512-528`.

Reference routes were confirmed exposed by the connected tool list; no new MCP domain request was needed because no unresolved syntax question changed the implementation.
The current parent references were reused for decision semantics, with pertinent local localisation excerpts read where their context result had omitted Localisation.
Direct local reads are not claimed as new MCP retrieval.
Both required source kinds were gathered through the available MCP workflow by the owner and their actual returned text was read from `docs/testing/event016_private_paleogenetics_20261008/parent_references.json`, rather than treating context source lists as excerpts.
Specifically, `paleoDecisionRead0` contains installed `common/decisions/_documentation.md:15-46`, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`, covering live availability and visibility scopes; `paleoDecisionRead1` contains offline `Decision modding:531-537`, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, covering the matching trigger timing/scopes.
Those actual MCP-returned excerpts were reused for the final category/recovery grouping review without rereading the same filesystem documentation or issuing another request.
Read references:

- Offline `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md:656-686,706-791,188-204`: first-match branch selection, trigger-local temporary display values and precision formatting; SHA-256 `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`.
- Offline `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:311-330`: base/blocked/hover custom-cost keys; reused revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`.
- Installed `documentation/script_concept_documentation.md:126-140`: contextual object/property syntax; SHA-256 `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`.
- Installed `common/scripted_localisation/00_scripted_localisation.txt:1-32`: native defined_text/text/trigger/localization_key precedent; SHA-256 `6f490e33736f4dc31568add5753a1afdef916f3993804febfbbee6d1583827587`.
- Installed `interface/countrydecisionview.gui`: relevant row spans above; SHA-256 `eedea36ade734b67a23181a650464f9168beadb0e024c0cedf2112d1b097194e`.

Installed paths are under `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`.
No web wiki access occurred.

## Limits and parent follow-up

Skipped populated-row rendering: the underlying renderer failure allowance was already exhausted by the owner's initial request plus corrected retry, as explicitly carried in this assignment.
Zero new render, whole-graph, health/status or screenshot-wait attempts were made.
A materially corrected renderer/input capability addressing that original failure would be needed to justify another attempt; unrelated source edits or another agent do not reset the budget.
Clipping, wrapping, alignment and overflow remain visually unobserved.
No known rendered defect was hidden by a source-only acceptance claim.

No gameplay simplifications were made and no new mechanic or design-gap plan was needed.
Unresolved wording decisions: none within the explicit staffing contract.
Remaining uncertainty: native display/transfer behavior remains outside this source review.
The accepted integration-plan identity is resolved.
Parent should review the key-level patch and complete its own integration/commit; no user-owned game testing is awaited.
Skills applied: chaos-redux-decisions-missions and chaos-redux-subagents; neither changed.

Final owned source SHA-256:
YML `ea7a55cda497454fa7b7fd7fc0eab7365eb8353bd808a10943fc400db0f45258`.
Scripted localisation `8aa39133a7678178bfa5e49bc6b7af96ad4f97a8e3803ba8408a538526a6ecb3`.
## Final parent-state grouping check

Read current `common/decisions/categories/germany_mengele_categories.txt:74-87`: the existing Biological Programs category remains visible for the provider OR the original staffing receipt, preserving release access after provider loss.
The staffing rows remain inside that category; no new category or dedicated window was introduced.
Open/close navigation remains human-only and the two row-context predicates retain AI bypass.
The category description invokes the existing `GetMengelePaleoOperationsSummary` only while that private view is open.
The paired neutral Prototype and ordinary production remain independent of staffing.
These are source grouping checks, not populated-row visual observations.

Current owner safeguards were read directly: completed full training does not expose settlement recovery; zero-debt recovery requires neither resource credit to be in flight.
The ordinary UI supplies no positive native acknowledgment receipt and does not manufacture one from later balances.
The existing ambiguous-transfer wording and pending debt display remain appropriate for these corrected gates.
The 26 localisation selector cases remain the reviewer-run evidence; the parent will rerun affected consumer cases against its final integrated source.
No fresh MCP requests, rendering attempts or further text patch were needed after this parent-state update.
