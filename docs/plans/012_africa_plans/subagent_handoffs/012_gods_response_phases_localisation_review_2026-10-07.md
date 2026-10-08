# Event 012 Gods response phases localisation review

Date: 2026-10-07.
Disposition: implemented bounded read-only review deliverable, followed by parent application of the four scoped wording recommendations on 2026-10-08.
Authority: the explicit narrow host/participant phase text-audit assignment.
Only this report was written.
No gameplay, localisation, spreadsheet, asset or other file was written, and no Git or launch operation was performed.

Parent integration on 2026-10-08: all four proposed values below were accepted and applied within the authorized response-phase work.
The overview describes reviewing responses to offenses, the priorities status remains accurate when the saved view has no current shortage, the opening label says review, and the ordinary host text retains its meter and doctrine without repeating the phase instruction.
The report below preserves the auditor's original source hashes and findings as the pre-application review record.
Native presentation and MCP coverage limits remain unresolved.

## Findings and exact proposed wording

All proposed changes below belong to `localisation\english\012_africa_gods_l_english.yml`.
These are recommendations, not applied changes or accepted design.
Literal `\n\n` prefixes must remain inside the localisation values.

| Priority | Key and source line | Current wording | Proposed complete value | Reason |
| --- | --- | --- | --- | --- |
| Fix | `gods_of_africa_response_overview`, 271 | `\n\nChoose priorities, partner relations or proven offenses.` | `\n\nReview tribute priorities, partner relations or responses to proven offenses.` | Players choose responses to offenses, not offenses themselves. The revised line names the three navigation destinations without implying that opening one commits an action. |
| Fix | `gods_of_africa_response_priorities`, 268 | `\n\nChoose which current shortage the next demands should address.` | `\n\nReview Africa's tribute priorities.` | A saved priorities view can become empty while Back remains available. This getter checks the saved enum, not whether a shortage remains. The current imperative can ask for a choice the player cannot make. The revised text works both with available priorities and an empty view. |
| Optional clarity | `gods_of_africa_open_priorities`, 258 | `Choose tribute priority` | `Review tribute priorities` | Matches the review action of opening the private view and its existing description. The current name is understandable with its description, so this is not a gameplay-blocking defect. |
| Optional repetition trim | `gods_of_africa_host_category_desc_ordinary`, 720 | Meter and doctrine text followed by `Manage priorities, leniency, protection, and the final settlement of each relationship.` | `£GFX_012_africa_gods_strength Strength: [?global.gods_of_africa_strength|0] ([GetGodsOfAfricaStrengthBand]). Doctrine: [GetGodsOfAfricaDoctrineName].` | The appended phase getter already gives the immediate action. Removing the standing management instruction avoids repeating menu content and directing attention toward discretionary work while replies take precedence. Preserve every existing meter, icon and doctrine token. |

The first two findings are bounded wording defects.
They require no new mechanic, public metric, asset or scripted branch.
No broader plan handoff is needed.

## Reviewed labels, descriptions and wrappers

The four navigation rows use the explicit name/description pairs at lines 258–265.
`gods_of_africa_open_partner_relations_desc` names leniency, pardon, protection and an expedition without promising that all four are currently available or already granted.
`gods_of_africa_open_judgments_desc` says to review proven offenses and available responses, so opening the view does not promise punishment.
`gods_of_africa_return_to_overview_desc` accurately returns to the three families and does not imply a refund, timer reset or policy change.
The priority description at line 259 explicitly puts review before choosing what Africa asks partners to send.
Keep these four descriptions.

The decision definitions at `common\decisions\012_africa_gods_decisions.txt:1073–1118` associate the four rows with those exact localisation pairs.
Their icons reuse `GFX_decision_012_africa_gods_set_priority`, `GFX_decision_012_africa_gods_protect_partner` and `GFX_decision_012_africa_gods_mark_offender`.
Their hidden effect calls lead to the existing private-view effects, which set or clear only `gods_of_africa_response_view`.
This limited call read establishes what the navigation wording refers to, not a new gameplay audit or an asset-render approval.

Keep `gods_of_africa_response_pending` at line 266: `\n\nReview the offers awaiting Africa's answer.`
It covers substitute offers, paid reconciliation and victor recognition without claiming acceptance, affordability or delivery.
Keep `gods_of_africa_response_doctrine` at line 267, because directing tribute policy follows doctrine selection.
Keep `gods_of_africa_response_partners` at line 269 and `gods_of_africa_response_judgment` at line 270, which describe review or a response without guaranteeing an outcome.
Keep the intentionally empty `gods_of_africa_response_no_status` at line 272.
Keep `gods_of_africa_parallel_reviews_status` at line 273: `\n\nReconciliation and the final ultimatum have separate deadlines.`
It identifies the two independent obligations without implying that one suspends, extends or resolves the other.

The participant wrapper at line 255 remains `[GetGodsOfAfricaVictorCategoryDesc][GetGodsOfAfricaCouncilPhaseText][GetGodsOfAfricaParallelReviewText]`.
The host wrapper at line 257 remains `[GetGodsOfAfricaHostCategoryDesc][GetGodsOfAfricaHostResponsePhase]`.
Neither wrapper needs a namespace change.
Both call scripted localisation in the existing category country context.
The new getters introduce no `FROM`, `PREV`, actor target or temporary-variable substitution.
The ROOT-targeted worker handoff was read for scope boundaries, without re-auditing its gameplay predicates.

The existing participant base at line 703 and victor base at line 704 retain the exact Strength and Wrath tokens and qualitative bands.
The existing ordinary host base at line 720 contains Strength and doctrine, not a third numeric meter.
The new text adds no numeric value and does not change either public meter.
Do not add Wrath to the host base merely to make the two category descriptions symmetrical.
Recovery/member/consolidation leaves already selected by the wrapper remain outside this bounded prose rewrite.
Their keys were located in `localisation\english\012_africa_gods_recovery_l_english.yml:14,31–32`, and no missing leaf was inferred from their absence in the main file.

## Status precedence and source coverage

`common\scripted_localisation\012_africa_gods_response_scripted_localisation.txt:4–30` selects the following first matching host output.

| Context | Selected leaf |
| --- | --- |
| Valid active host with current pending answers, any saved view or doctrine state | `gods_of_africa_response_pending` |
| Valid active host without doctrine, no pending answer | `gods_of_africa_response_doctrine` |
| Valid active host with doctrine, no pending answer, priorities enum | `gods_of_africa_response_priorities` |
| Same conditions, partners enum | `gods_of_africa_response_partners` |
| Same conditions, judgment enum | `gods_of_africa_response_judgment` |
| Valid active host, doctrine selected, no pending answer, other/absent view | `gods_of_africa_response_overview` |
| Invalid or inactive host | Empty `gods_of_africa_response_no_status` |

This ordering puts answers before doctrine and discretionary views.
The new getter's eight leaves, counting the shared empty default once, all exist.
`GetGodsOfAfricaParallelReviewText` at lines 33–42 emits its note only when both `gods_of_africa_reconciliation_pending` and `gods_of_africa_final_ultimatum_pending` are present.
Either flag alone, or neither flag, gives the empty default.
It reports flags qualitatively and does not manufacture a countdown.

The existing participant getter at `common\scripted_localisation\012_africa_gods_scripted_localisation.txt:968–973` prioritizes a current recovery member request, then victor exemption, then the ordinary participant text.
The host getter at lines 989–995 prioritizes host recovery, consolidation, pending settlement delivery and its ordinary default.
The appended host response getter returns empty outside active host authority, avoiding ordinary policy instructions during those inactive recovery/delivery contexts.
The existing Council getter at `common\scripted_localisation\012_africa_gods_council_scripted_localisation.txt:22–32` appends its deferral note only while Council is open and its response phase is closed.
Appending the separate deadline note does not overwrite Council deferral or either category base.

The parent-supplied `012_gods_response_phases_review_2026-10-07.md` reports 21 passing source-model groups.
Its empty-view, reply-preemption, paid-offer, victor-renewal, AI-bypass and independent-clock evidence was used as context, not rerun or promoted to live engine proof.
Its six-primary-priority-plus-Back count and four partner/four judgment counts remain unchanged by every recommendation here.
The unchanged qualitative phase text does not expose the private enum or claim to change paid offers, bought preparations, ultimatum answers or deadlines.

## Mechanical and prose issue lists

- Missing key list: none among the 18 scoped wrapper/navigation/status keys or the directly selected new getter leaves.
- Duplicate key list: none for those 18 keys across the English localisation files. All five wrapper getter names have one definition across `common\scripted_localisation`.
- Scripted localisation issue list: no broken source reference or incorrect first-match ordering found in scope. MCP indexing coverage remains unresolved as described below.
- Dynamic text opportunities: none required. The phase getter already supplies qualitative context, the parallel note already reflects both flags, and existing meters use their established tokens. Do not add actor names, costs or countdown values to navigation merely to make it dynamic.
- Encoding concerns: the main English file begins with `EF BB BF`; no concern found there. The new scripted-localisation `.txt` starts with ASCII comments and is not a localisation YAML file requiring a BOM.
- Vagueness: the overview's choice of “proven offenses” is the concrete semantic defect above.
- Bloat and repetition: the standing host management sentence repeats the appended phase instruction. The optional trim preserves its factual meter and doctrine content.
- Obvious explanation: no additional “this button opens” explanation is needed. The four descriptions already give the subject of review.
- Overcomplication: none in the four navigation descriptions or eight status/default leaves. Keep the concise parallel-deadline sentence.
- Style-rule repair: no em dash, sentence semicolon, staged contrast, staccato dramatic chain, implementation history, tuning note, raw task label or secret-route disclosure found in the audited text. The priority fix addresses a misleading imperative in an empty saved view.
- Sourced quotations: no sourced or attributed quotation occurs in the audited text. No quotation was rewritten, repunctuated or normalized.
- Cross-surface mismatch: navigation and phase status wording currently differ in how directly they imply choosing a priority, addressed by the recommended label/status pair. No new cost, effect or outcome contradiction was found in the four navigation pairs.
- Spreadsheet handoff: no catalog workbook or export was read or changed, so catalog equality is unverified. These navigation/status strings are not identified here as catalog detail fields. If the spreadsheet owner mirrors them, use the exact proposed values above only after parent application. Do not claim that the existing catalog needs an update without locating its actual matching field.

## References and MCP limits

The exposed `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, `hoi4.source_lookup` and `hoi4.decision_inspect` schemas were inspected.
Live reference calls returned `OK` for workspace `mod_chaos_redux_ea3b2d67c2c0`, establishing that those requests completed rather than inferring service health from exposure.
The localisation context bundle reported no `omittedSources` or `missing` required source kind.

The offline `paradox_wiki\Localisation - Hearts of Iron 4 Wiki.md:656–705` was read through revision-bound MCP retrieval, revision `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`.
It explicitly defines current-scope default resolution and selection of the first matching `text` entry.
The same local file's lines 60–93 and 186–204 were read directly for BOM, optional version omission, literal newline escapes and numeric precision.
The installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\scripted_localisation\00_scripted_localisation.txt:1–33` was read directly for country-scoped triggers and a conditional/default vanilla pattern.
Its SHA-256 is `6f490e33736f4dc31568add5753a1afdef916f3993804febfbbe6d1583827587`.
The installed `common\decisions\_documentation.md:1–46` was read directly for native category actor/target visibility and availability scope, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`.
The retrieved formatter header did not document scripted first-match semantics, so it was not used as proof of that rule.

`hoi4.source_lookup` for `GetGodsOfAfricaHostResponsePhase` returned zero indexed definitions at workspace revision `d2d484d00542c47f960e898d9f832a2e5f5782b89f9a619521000e245845cf9c`.
The local file has the definition at line 5, so this is an unresolved index-coverage discrepancy, not evidence that the getter is absent.
No refresh or source mutation was attempted to reconcile the discrepancy.

The initial `hoi4.decision_inspect` request with `mode = inspect` and no scenarios was rejected with `-32602`, “Decision inspection requires declared scenarios at scenarios”.
A subsequent inventory request returned `DECISION_ANALYZED_PARTIAL`, with `complete = false`, 100 unresolved definitions and no scenarios.
Despite the supplied decision ID, its summary covered 2,070 categories and 8,314 decisions.
This broad, partial inventory is not narrow localisation coverage, gameplay validation or native visual evidence.
Its full artifact was not consumed because it is outside the requested narrow audit, and no findings here rely on its contents.
Retained URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a9ae3cd59093ae911968baedaa32e72f6efc01aa6c4c2a755570ceabddcd3559/acb23c815e192c85a8c4a7f5e6e1ea0069644dd17de7dd1fb4cb5e1347ce37b7/decision-c7cb224dd04adfc85dd810b9.json`.

The connected tool inventory exposes technology inspect/render/compare routes but no separately named standalone Technology Tree Viewer route.
Record the absent exposed standalone viewer as a session package capability gap.
Installed standalone viewer availability and the technology service's health were not established, and no technology surface is in scope.
No focus, map, event-popup or dedicated scripted-GUI surface was assigned here.
No missing-window GUI render was run.
Native category wrapping, clipping, alignment and geometry remain unverified user visual acceptance, without an inferred clipping defect or renderer exception.

## Source identities, validation and completion boundary

| Source | SHA-256 at read |
| --- | --- |
| `localisation\english\012_africa_gods_l_english.yml` | `7cbe3cd5a5b67bc3dd21ca29d9cc455930867e0a0ae90d9186ce84c52b10e28d` |
| `common\scripted_localisation\012_africa_gods_response_scripted_localisation.txt` | `6650782dd362a0faed6d35607fc43c08110163e49431b6dc526110ebdb040034` |
| `common\scripted_triggers\012_africa_gods_response_view_triggers.txt` | `3bfc5da6ed62f7d1f1d94410172f7544169479b519085fbb291913536ea0d65d` |
| `common\scripted_triggers\012_africa_gods_response_context_triggers.txt` | `91665ade663c79702514bfe28c75f17f2b880ddfaf8f90c776e92b404611dcac` |
| `common\decisions\012_africa_gods_decisions.txt` | `e808262b60c0ff34cfd6c0eac146fcb53f6ced3bb6d58bcc157799fe48720f93` |

Meaningful validation performed: English definition-count checks for the 18 exact keys, wrapper getter uniqueness, new getter leaf resolution, direct wrapper composition and first-match precedence review, and navigation label/description comparison against the four private-view call sites.
The empty-view wording defect was identified by comparing the getter's enum-only priority branch to the parent's documented retained Back path.
All recommendations preserve dynamic tokens, icons, public metrics and authored newline escapes.
No implementation before/after behavior is claimed because source was not patched.

Skipped meaningful validation: native visual acceptance, engine scope evaluation, catalog comparison and gameplay/probability retesting, because this is a read-only native category text audit and the parent supplied its gameplay review.
Source reads are not equivalent to those checks.
The report is complete as a bounded audit, with the two wording fixes awaiting parent action and the MCP index/native visual limits retained.
No simplification, gameplay fallback, new asset or new mechanic was introduced.
Skills applied: `chaos-redux-decisions-missions`, the writing and localisation sections of `chaos-redux-events`, and `chaos-redux-subagents`.
No skill was changed.
