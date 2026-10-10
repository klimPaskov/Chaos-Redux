# Event 012 bounded final localisation audit

Status: bounded report and final Charter source review complete, with no unresolved wording finding; final Charter production-render review remains with the owning GUI worker and parent.
Read-only audit requested by the parent on 2026-10-06.
Only this handoff was written; no gameplay, GUI, localisation, spreadsheet, or commit changes were made by this auditor.

## Scope and revisions

Reviewed `localisation/english/012_africa_gods_l_english.yml`, `common/scripted_localisation/012_africa_gods_scripted_localisation.txt`, `common/scripted_effects/012_africa_gods_report_effects.txt`, and the changing Charter copy in `localisation/english/012_africa_charter_gui_l_english.yml`.
Report baseline is `ad31061b3^`; the requested report change is `ad31061b32b605a0d3c06d4d3c6878a361f9ecb2`.
`f9c56e115d1045785468cb745e074e20aca64971` and `685a977d62cf1d22ffc93a750188537ffbbd8fa5` contain accounting and closure source changes, with no additional localisation changes in the assigned files.
The initial audit HEAD was `8172a80ba`; the parent's subsequent expiry wording correction is committed as `e9cd71fcd` and included below.

Final reviewed SHA-256 identities:

| Source | SHA-256 |
| --- | --- |
| `localisation/english/012_africa_charter_gui_l_english.yml` | `4b8fa3278f5d4052ded0e173877d56f501e8d6db4245955ac4ecd1431b406404` |
| `localisation/english/012_africa_gods_l_english.yml` | `f7fa5bd92c2803c2713af2ea19a7bf713ce92e2c1819c55bedd9c127298d1153` |
| `common/scripted_localisation/012_africa_gods_scripted_localisation.txt` | `67fd4744b911e1b7c38a0c25e4063a1a521f7b6da534dd1519b34a2dd48e4b7b` |
| `common/scripted_effects/012_africa_gods_report_effects.txt` | `b64f07248386f56b718e7a041e560dbd7adaf351b6eec58d5911d8ba8443fac9` |

## Report findings and resolved correction

The changed keys are `gods_of_africa_response_refusal_report`, `gods_of_africa_response_expired_report`, and `gods_of_africa_response_support_summary`.
They describe the current demand, refusal, missed payment, amount sent, and unpaid amount directly, without update history, private bookkeeping, or formatting colours.
The summary uses actual `\n\n` escapes and retains `GetGodsOfAfricaResponsePaidAmount` and `GetGodsOfAfricaResponseBalance`.
`gods_of_africa_capture_response_report` captures the material family and stores the total paid as demand amount minus captured remaining balance.
Its support-summary flag is set only for signed continuing support with a non-partial response, and cleared at a fresh capture, an undelivered receipt, and receipt cleanup.

**Repetition, resolved by the parent:** support expiry formerly printed the unpaid balance in both its opening and appended summary.
The parent added `gods_of_africa_response_support_expired_report`: "The support deadline passed. Africa has ended the demand and will remember the missed payment.[GetGodsOfAfricaResponseOutcomeLine]"
The first branch of `GetGodsOfAfricaResponseReport` now selects that key for failure plus `gods_of_africa_last_response_support_agreement`, before ordinary failure.
Ordinary expiry keeps its original unpaid amount, while signed-support expiry prints the amount once in the summary.
Textual expansion examples with 1200.125 fuel sent / 799.875 unpaid and 3500 infantry equipment sent / 1500 unpaid each print the unpaid amount once.
These examples validate the composed prose and substitutions, not execution of Clausewitz effects.

## Key coverage, encoding, and writing quality

- Missing report keys: none found.
- Duplicate keys in the two assigned localisation files: none found at the initial snapshot.
- Scripted localisation issues: no broken report output reference found; three recovery-category outputs are correctly defined in `012_africa_gods_recovery_l_english.yml`, rather than the main Gods file.
- Dynamic text: the existing paid, unpaid, material-family, country, state, and constant substitutions were preserved; no new opportunity is required for the narrow report change.
- Encoding: both assigned localisation files retain UTF-8 BOM; no double-escaped newline mistake was found.
- Vagueness, bloat, obvious explanation, overcomplication, and style-rule violations: none found in the changed report passages.
- Repetition: the support-expiry repetition above was resolved by the parent.
- Sourced quotations: none occur in the changed passages inspected; no quotation was altered.
- Cross-surface/catalog mismatch: no mirrored Event Details or catalog field was changed by these report keys; the workbook was not inspected or edited, so this is not a general catalog-alignment claim.

## Final Charter source review

The GUI worker wrote the final source before this verdict.
Default main readings are Authority in `africa_charter_gui_primary_values`, Pressure and Readiness in `africa_charter_gui_secondary_values`, and Objective in `africa_charter_gui_action_summary`.
Country, region, origin, skill programme, proposal and family remain navigation/selection labels.
The former member, region, diaspora and project summaries become explicit hover cues, while secondary values move into seven native `pdx_tooltip` bindings.

| New key | Authored lines | Content retained |
| --- | --- | --- |
| `africa_charter_gui_authority_tt` | 3 | Meaning, dynamic measure range, causes and uses |
| `africa_charter_gui_secondary_values_tt` | 4 | Reach, Burden, range, Pressure and Readiness context |
| `africa_charter_gui_selected_member_detail_tt` | 4 | Relationship, confidence, protection, clauses, obligations, projects and departure pressure |
| `africa_charter_gui_regional_metrics_tt` | 4 | Congresses, readiness, overlap, corridor, restoration, pressure and settlement |
| `africa_charter_gui_rival_warning_tt` | 2 | Rival member and warning totals, plus warning status |
| `africa_charter_gui_diaspora_summary_tt` | 2 | Settlement capacity, trust, reserve and representation |
| `africa_charter_gui_project_summary_tt` | 2 | Projects, actions, administration and intelligence reserve |

All seven new keys have definitions and matching bindings in `interface/012_africa_charter.gui`.
Comparison against the preceding committed Charter source found no lost bracketed dynamic token.
Both assigned localisation files have no duplicate keys at the final snapshot.
The final Charter file preserves BOM and authored newline escapes.

**Style repair, resolved by the GUI worker:** `africa_charter_gui_authority_tt` initially joined its range and fulfilled-proposal explanation with a sentence semicolon.
It now reads "Range [?constant:africa_measure.minimum|0]-[?constant:africa_measure.maximum|0]. Fulfilled Charter proposals raise it and failed proposals lower it."
Remaining semicolons separate compact label/value pairs rather than prose clauses.
No unresolved vagueness, bloat, obvious explanation, repetition, overcomplication, or style-rule issue was found in the bounded final changed copy.
The hover cues serve discoverability for hidden values rather than explaining an obvious button action.
No quote-bearing passage was changed.

## Reference and MCP evidence

Offline wiki `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`, Dynamic scripted localisation, lines 706–728, revision `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`, was read through `hoi4.reference_read`.
Installed `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md`, Using a localization object, lines 134–140, revision `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`, was read through the same route.
The formatter context returned only its document heading, so no substantive formatter coverage is claimed from that citation.

`hoi4.event_render` used `view=options`, event selector `chaosx.nr12.604`, `maxNodes=1`, `maxDepth=1`, `expandHelpers=false`, and no refresh.
It returned `EVENT_RENDERED_PARTIAL`, source revision `4969042f8122a553c30402d067b14cdc9c731bc3674b68dd419cb0813fb913a7`, and one selected node.
Source-linked render data: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e1b1541f7bd05fb26ab3391d16d4dfaccd93670f3675aac9e79bb5c715fedd63/16e48254d7bdf00541a26e2391a81ecec5a7e3b621093a4d1b68337da9c7fe3c/event-options-4969042f8122.json`.
This is an event-chain diagram, not a report-popup typography or dynamic-state render.
The lint route accepted the narrow selector but returned workspace-wide counts of 2,285 diagnostics; that result is excluded from the bounded localisation verdict and its global findings were not investigated.
Initial schema rejections were corrected for the event request; the GUI inspection attempt lacked a scenario and was rejected, so it establishes no GUI coverage.

A corrected final `hoi4.gui_inspect` request used `africa_charter_window` and the saved normal Charter host fixture, removed stale localisation overrides, and replaced obsolete helper text overrides with current wording.
It returned `GUI_INSPECTED`, no blockers and no missing localisation, with shared revision `950f99b51e4b3afdba37ee4b3fa37e7bd20464e635e5ed9bb30f06d68b7d7bb7` and emitted scenario `012_charter_localisation_source_review-generated-1`.
The generated suffix is retained because the request did not disable generated scenarios; it is not presented as the worker's exact final render fixture.
Inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/60213175c2e116aedc3781b60c64c13fa1f897dedd83ce3f7c31295b84285767/4752491c88828597218fa59a9cf1d9f0ebd270b4d6c44427639f01b03a70788c/gui-inspect.950f99b51e4b3afd.json`.
It inspected 106 window elements and retained 8 unresolved fidelity items and 134 non-blocking visible-overlap diagnostics.
These results are source/scenario linkage evidence, not proof that the final tooltip wraps or the window has no visible defects.

`python .tools/report_colour_audit.py --event 012` independently returned zero colour-bearing keys, covering report/news text and reachable scripted localisation.
No technology surface is in this assignment; no Technology Tree Viewer availability or technology review is claimed.
No game or desktop windows were launched, logs requested, refresh/state-flow/helper-expansion routes used, or spreadsheet edits made.

## Remaining gate

Final four-reading Charter copy and native tooltip bindings have been reviewed at the hashes above.
The GUI worker's matching normal/empty/full and member-tooltip production render was still pending when this handoff was finalized.
The parent must review that evidence and the worker's updated `takeover_gui_animation_2026-10-06.md`; earlier multi-value renders cannot establish final four-reading overflow, wrapping or visual completion.
No separate duplicate production-render batch was started by this auditor while the owning worker was preparing the required run.
Gameplay execution, accounting, AI, and parent final integration remain outside this localisation verdict.

Skills read and applied: `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-scripted-gui`, and `chaos-redux-decisions-missions`.
No skill was created or updated.
