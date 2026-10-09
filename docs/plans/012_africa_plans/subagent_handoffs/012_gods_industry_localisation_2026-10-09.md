# Event 012 industrial repair localisation handoff

Date: 2026-10-09.
Disposition: implemented bounded localisation patch, pending parent review and native visual acceptance.
Acceptance basis: the parent delegation for accepted F1 and `012_gods_industrial_tribute_design_2026-10-08.md`, whose parent-reviewed disposition selects funded one-site repair without changing the CPP price.
Parent retains gameplay integration, tests, documentation, workbook reconciliation and commit.
No gameplay, GUI, GFX, AI, country, workbook or Git operation was performed.
The public-values GUI worker's files, fields and ordinary category-description keys were not edited.

## Changed files and identifiers

- New `common\scripted_localisation\012_africa_gods_industry_scripted_localisation.txt`: the seven getters listed below.
- New `localisation\english\012_africa_gods_industry_l_english.yml`: 23 keys listed below.
- `localisation\english\012_africa_gods_l_english.yml`: 13 owned keys listed below.
- `common\scripted_localisation\012_africa_gods_scripted_localisation.txt`: two first-match industry branches in `GetGodsOfAfricaResponseReport` only.
- This handoff.

The existing main-file report amount and balance getter names are `GetGodsOfAfricaResponsePaidAmount` and `GetGodsOfAfricaResponseBalance`.
There is no `GetGodsOfAfricaReportPaidAmount` definition in the inspected source.
Their political-power leaf strings already use `|3` and were preserved.

| New getter | Input and leaf contract |
|---|---|
| `GetGodsOfAfricaIndustryTermsLine` | Actor family `industry_repair`, bound terms flag, normal frozen site/Q/D/remaining and `industry_full_new_days` cache. Completion predicate selects financial settlement without extra days. Empty for nonindustry or unbound terms. |
| `GetGodsOfAfricaIndustryPartialTermsLine` | Same family/binding selection, normal `partial_payment_amount` and `industry_partial_new_days` cache. Completion predicate selects partial settlement without extra days. |
| `GetGodsOfAfricaIndustryResponseLine` | Frozen `last_response_industry` flag and receipt fields. Selection order is retired, completed, positive paid increment for compliance/partial, substitute, unchanged, empty. |
| `GetGodsOfAfricaPaymentAmountValue` | Classifies normal `payment_family`, displays normal `payment_amount`. |
| `GetGodsOfAfricaPartialPaymentValue` | Classifies normal `demand_family`, displays normal `partial_payment_amount`. |
| `GetGodsOfAfricaDemandRemainingValue` | Classifies normal `demand_family`, displays normal `demand_remaining`. |
| `GetGodsOfAfricaDemandAmountValue` | Classifies normal `demand_family`, displays normal `demand_amount`. |

All omitted variable prefixes in the table are `gods_of_africa_`.
The four numeric getters set the caller-owned bare `gods_of_africa_family_to_check` before invoking `gods_of_africa_family_uses_political_power`.
They select real YML leaves with `|3` for the eight CPP families and `|0` for material quantities.
No normal game variable is mutated by scripted localisation, and no arithmetic output from a returned helper is read.
All repair day values come from normal owner-prepared caches or frozen response receipts.
The speed is displayed from `constant:gods_of_africa_industry.repair_speed` with `|%0`, currently +50%.

### Main-English changed keys

| Key | Final change |
|---|---|
| `chaosx.nr12.603.d` | Existing description preserved, appended `[GetGodsOfAfricaIndustryTermsLine]`. |
| `chaosx.nr12.604.d` | Existing report and breach getters preserved, appended `[GetGodsOfAfricaIndustryResponseLine]`. |
| `gods_of_africa_family_industry_repair` | `civilian-factory repair funding` |
| `gods_of_africa_demand_balance_diplomatic` | `Complying costs [GetGodsOfAfricaDemandAmountValue] political power and is done in full.` |
| `gods_of_africa_demand_balance_material` | `[GetGodsOfAfricaDemandRemainingValue] of [GetGodsOfAfricaDemandAmountValue] remains due.` |
| `gods_of_africa_prioritize_industry_desc` | `Seek funding first for damaged civilian factories at an eligible African site when Africa has capacity for repair projects.` |
| `gods_of_africa_prioritize_industry_effect_tt` | `Industrial repair takes priority when Africa has a damaged site, available civilian factory capacity and room for one repair programme.` |
| `gods_of_africa_current_demand_cost` | Replaced only amount token with `[GetGodsOfAfricaPaymentAmountValue]`, preserved colour and payment icon getter. |
| `gods_of_africa_current_demand_cost_blocked` | Same numeric getter, preserved blocked colour and payment icon getter. |
| `gods_of_africa_partial_payment_cost` | Replaced only amount token with `[GetGodsOfAfricaPartialPaymentValue]`, preserved colour and demand icon getter. |
| `gods_of_africa_partial_payment_cost_blocked` | Same numeric getter, preserved blocked colour and demand icon getter. |
| `gods_of_africa_current_demand_cost_tooltip` | `Africa receives the payment when we fulfil the demand.[GetGodsOfAfricaIndustryTermsLine]` |
| `gods_of_africa_partial_payment_cost_tooltip` | `The unpaid remainder keeps its current deadline.[GetGodsOfAfricaIndustryPartialTermsLine]` |

### New English keys

The final wording and exact dynamic tokens are in the new YML file.
These keys form the complete new set, with no duplicate aliases elsewhere in English.

| Key | Purpose |
|---|---|
| `gods_of_africa_industry_text_empty` | Empty nonindustry/unbound output. |
| `gods_of_africa_industry_terms` | Full remaining CPP, new days, named state, full Q/D, repair-speed promise, recipient capacity and expiry/completion. |
| `gods_of_africa_industry_terms_completed` | Named completed state, remaining CPP and no new service. |
| `gods_of_africa_industry_partial_terms` | Actual partial CPP, newly funded days, named state, repair speed, recipient capacity and expiry/completion. |
| `gods_of_africa_industry_partial_terms_completed` | Partial financial settlement after completion, no new service. |
| `gods_of_africa_industry_response_paid` | Frozen actual new days, cumulative funded CPP/Q and granted days/D, named state and finite support. |
| `gods_of_africa_industry_response_completed` | Completed factories, cumulative received CPP/Q, no new repair days. |
| `gods_of_africa_industry_response_retired` | Received CPP/Q and site, previously paid valid support survives finance closure. |
| `gods_of_africa_industry_response_substitute` | Material substitute adds no service, previously paid support retains its own term. |
| `gods_of_africa_industry_response_unchanged` | Other answers add no service, previously paid support retains its own term. |
| `gods_of_africa_industry_lapsed_report` | `Africa can no longer receive the agreed industrial funding. The demand has ended with [GetGodsOfAfricaResponseBalance] unpaid, without a penalty for refusal or credit for fulfilment.` |
| `gods_of_africa_industry_undelivered_report` | `Africa could not receive this industrial payment. No payment is credited and the remaining balance stays due.` |
| `gods_of_africa_industry_repair_program` | `Funded Civilian Factory Repairs` |
| `gods_of_africa_industry_repair_program_desc` | `Foreign tribute funds faster repair of damaged civilian factories in this state until the paid term expires or those factories finish repairing. Africa must retain the site.` |
| `gods_of_africa_industry_unavailable_tt` | Qualitative original site ownership/control/core, agreement, recipient capacity, positive further service or confirmed paid completion requirement. |
| `gods_of_africa_payment_amount_cpp_value` | `[?gods_of_africa_payment_amount|3]` |
| `gods_of_africa_payment_amount_material_value` | `[?gods_of_africa_payment_amount|0]` |
| `gods_of_africa_partial_payment_cpp_value` | `[?gods_of_africa_partial_payment_amount|3]` |
| `gods_of_africa_partial_payment_material_value` | `[?gods_of_africa_partial_payment_amount|0]` |
| `gods_of_africa_demand_remaining_cpp_value` | `[?gods_of_africa_demand_remaining|3]` |
| `gods_of_africa_demand_remaining_material_value` | `[?gods_of_africa_demand_remaining|0]` |
| `gods_of_africa_demand_amount_cpp_value` | `[?gods_of_africa_demand_amount|3]` |
| `gods_of_africa_demand_amount_material_value` | `[?gods_of_africa_demand_amount|0]` |

## Wiring and parent follow-up

The .603/.604 descriptions and both full/partial native cost-hover strings are wired in this patch.
The two industry-specific report wrapper branches precede generic lapsed/undelivered shipment wording, selected by frozen family and kind rather than a live quote.
Existing response kind/family wrappers remain otherwise intact.
The lapsed branch uses the named `gods_of_africa_history_kind.lapsed` constant and `industry_repair` family, currently 18 and 7.

`gods_of_africa_industry_unavailable_tt` is localised but had no gameplay caller at the final source search.
Parent must attach it as the custom tooltip for the appropriate pure industrial preflight, keeping actual availability and payment checks with the owning code.
This is the one explicit caller-wiring item left to the parent, not a missing localisation key.

Parent must retain `gods_of_africa_refresh_industry_payment_quotes` calls wherever it prepares full and partial normal display quotes.
The getter intentionally does not refresh them or calculate service days.
Parent response capture must precede cleanup, preserving site, quote, service_days, new_days, funded, granted_days and both last-response flags.
The current integration API source exposes those caches and capture fields at `common\scripted_effects\012_africa_gods_industry_integration_effects.txt:87–162`.
The CPP classifier is at `common\scripted_triggers\012_africa_gods_industry_integration_triggers.txt:41–54`.
It includes industry_repair, recognition, territory, end_enemy_support, emergency_relief, military_access, non_aggression and guarantee_africa.

No workbook was read or edited, so catalog parity is unverified rather than declared mismatched.
For `chaosx_spreadsheet_doc_worker`, mirror the final keys only where catalog text actually describes this funding surface, especially the industry-family phrase, priority wording and .603/.604 report composition above.
Do not insert repair effects into the catalog's premise-only Event Details fields.
No event-log or Event Details wording was changed by this pass.

## Audit and prose decisions

- Missing keys: the modifier title/description, blocker tooltip, industrial terms/response leaves and numeric leaves are supplied in the new 23-key file. No unresolved missing key was found within this set.
- Duplicate keys: zero for the new 23 English keys, and one definition of each of the seven new getter IDs across installed mod scripted-localisation files.
- Scripted localisation: all new selected leaf keys resolve. Existing generic industrial lapsed and undelivered wording implied an empty material shipment, repaired by the two narrow first-match branches.
- Dynamic opportunities implemented: actual site name, CPP/Q/balance, full and partial newly funded days, full service entitlement, frozen funded/granted totals, dynamic repair percentage and recipient capacity requirement.
- Cross-surface mismatch repaired: CPP rows and balances previously showed integers while response CPP receipts already showed three decimals. All owned CPP amount paths now select three decimals. Material quantity formatting remains integer.
- Encoding concerns: no unresolved concern in the written files. The new English file has UTF-8 BOM and unversioned keys. Shared-file edits used byte-baseline checks and atomic sibling replacement, preserving unrelated current content.
- Vagueness: `industrial repair support` became `civilian-factory repair funding`. Priority text now names damaged factories, an African site and recipient capacity instead of an undefined valid need.
- Bloat: the full terms present one financing consequence and two necessary conditions, without copying the guide, price formula, private ledger or programme history.
- Obvious explanation: the partial hover stopped narrating sending the displayed portion, and the full hover stopped repeating its family label. They retain payment/deadline context and the industrial consequence.
- Repetition: retained short common receipt wrappers, with one appended industrial result line. No second action, category or public meter was introduced.
- Overcomplication: player text uses site, payment, factories and paid days. It omits tuple terminology, helper names, cumulative floor arithmetic and native-evidence labels.
- Style repair: all new player strings avoid em dashes, semicolons, task labels, update history, hidden-mechanic explanations and colour codes on report parchment.
- Sourced quotations: none occur on the inspected owned surfaces. No quotation was altered, invented or attributed.
- Tokens and names: existing colour codes and icon getters in dark cost rows were preserved. Normal variable tokens and existing wrapper calls were preserved or replaced with explicit equivalent formatting getters. State-name access follows the existing `[?variable.GetName]` pattern.

## Meaningful validation

An inline read-only actual-source display evaluator ran 87 cases against the new getters and the parent CPP classifier.
It checked four numeric getters across all eight CPP families and nine material families, full/partial bound and unbound terms, nonindustry empty outputs, fixture-proven completion, positive actual new-day reports, substitution, neutral retirement even with the completion flag, unchanged service and wrapper precedence.
It also verified normal cache tokens, frozen response tokens, all 23 leaf-key resolutions, cross-file key uniqueness, single getter definitions, report CPP precision parity and unchanged cost icon getter tokens.
The evaluator explicitly fixture-binds the pure completion predicate and does not emulate its gameplay proof, native formatting or repairs.
This is display branch evidence only.

`python .tools/report_colour_audit.py --event 012` found zero reached colour-bearing report keys.
The retired-response sentence was subsequently simplified without changing any token or selection branch, followed by another report colour audit and final token/encoding review.
No gameplay owner tests were rerun because the parent owns them and this patch changes no gameplay.

## References and MCP evidence limits

Verified live exposure and successful calls: `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, `hoi4.source_lookup`, `hoi4.event_inspect` and `hoi4.event_render`.
Localisation context included both required source kinds, with no omittedSources or missing files.
The installed formatter-documentation heading alone supplied no detailed numeric rule, so detailed object access and formatting context were also read.

| Reference | Read spans and revision |
|---|---|
| `paradox_wiki\Localisation - Hearts of Iron 4 Wiki.md` | Scripted localisation 656–705 and temporary display 729–792 through reference_read. Numeric formatting 184–214 read directly after broad search returned an unrelated section. Revision/SHA-256 `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`. |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\script_concept_documentation.md` | Object access 134–140 and formatted localisation 161–170 through reference_read. Revision `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`. |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\loc_formatter_documentation.md` | Heading 1–2 through reference_read, limited evidence. Revision `1fbd9a031fd09100d79bac08dec3c16e19468f23516c5e67c67578156282af08`. |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\scripted_localisation\00_scripted_localisation.txt` | Vanilla first-match/backup precedent 1–32 read directly. SHA-256 `6f490e33736f4dc31568add5753a1afdef916f3993804febfbbe6d1583827587`. |
| `common\scripted_effects\012_africa_gods_industry_effects.md` | Public pure preflight, normal record, cumulative service and native-evidence limitations read directly. This handoff relies on the owner's mechanism references and does not independently claim native repairs. |

Source lookup for the response getter returned no indexed definition despite the source definition being present.
Its revision was `7752339650698692db6289c748a58ae3075b7b36b2996c8587e39ce1e682de3b`.
This route result is a scripted-localisation indexing gap, not evidence of a missing getter.

Both .603 and .604 had successful bounded trace and options-render calls using `selector: { kind: event, eventId: ... }`, depth 1, at most 8 nodes and no helper expansion.
Earlier invalid `id` selector requests were rejected and corrected, not treated as service-health failures.
Returned graph revision: `283a550085362183c930b3e9508acd4051d381fab0d6edd4f1b8afac59de6889`.
Returned graph hash: `617f6c3a15682e0d5e30f22be099e2c82ee27e98d9212d5fa81efa00b039a00f`.
The tools report `EVENT_INSPECTED_PARTIAL` and `EVENT_RENDERED_PARTIAL`, with helper/lifecycle work deferred.
These are event-chain artifacts and do not establish native report font fit, popup overflow, wrapping, hover fit or dynamic localisation evaluation.
No event script or graph structure was changed, so no graph-delta claim or event_compare pass is made.

Useful artifacts:

- .603 trace: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0ad8288c52df121f2376dd135aec9b6e3b72cbfd1a3d4a2fc6cee9f50f20d263/b5dc70f78b529dd9c31ad39f13cb87463f4650a7cadc99d1a628c5eb20f1ee79/event-trace-283a55008536.json`
- .603 options PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cb73af89242fc755af208686083866f6da2a5f139bc57203aef5cd7e15659252/656d6b4ec820b835b0db8f57d6abd04130017b9b081a9a9cf5006e8e0833c7ab/event-options-283a55008536.png`
- .604 trace: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/05535d492c1ce0ad6621fe02dde35d8a388f30ef1ad3ae2e059b8919b2a4fb67/e58c26ed1be889f4fd3206842061463276340e222da3fe83c4d1543e712fdd65/event-trace-283a55008536.json`
- .604 options JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c1b776ed693a0d4bf446cb6c03927bf33ea13fa37fa0b62b6706810b8bc042ba/54ae3f8060fdf5ca049dae32b1279d759e57c90323e79f3463e9b1cbc2caf39b/event-options-283a55008536.json`
- .604 options PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/99157c4d88cd0c6301d0b63bb9fbd65eca70204480811d773b73514ffa676b6d/6f85c1f6055b35d197f91930dbc51b92fbcc69591562ab1fede0d8f4ef520414/event-options-283a55008536.png`

Artifact read blocker: the .604 options JSON full resource read returned malformed/truncated JSON, although its resource wrapper declared application/json.
The bounded retry with `?offset=0&length=16000` failed with MCP error -32603, `Artifact provenance manifest is unavailable`.
The live artifact resource template was independently discovered and does advertise byte-range selectors.
The configured local fallback path under `C:\Users\klimp\AppData\Local\hoi4-agent-tools\workspaces\mod_chaos_redux_ea3b2d67c2c0\artifacts\c1\c1b776ed693a0d4bf446cb6c03927bf33ea13fa37fa0b62b6706810b8bc042ba\event-options-283a55008536.json` was absent.
No incomplete resource payload was accepted as coverage or visual proof.

Standalone Technology Tree Viewer availability was checked separately from tech tool exposure.
No standalone technology viewer tool exists in the connected inventory, and the inspected npm package has no technology-viewer file or executable.
The cached package is `C:\Users\klimp\AppData\Local\npm-cache\_npx\e5002410e5b7105a\node_modules\hoi4-agent-tools`, package version 3.10.0, with stdio/http/setup executables only.
This is a standalone-viewer package gap, not a claim about the connected process version or health of uncalled technology routes.
Configured transport invokes `hoi4-agent-tools@latest` with `HOI4_AGENT_CONFIG` pointing to `C:\Users\klimp\AppData\Roaming\hoi4-agent-tools\config.json`.
No native tasks, jobs or helper-expansion routes were used.

## Remaining limits

The bounded text/getter implementation is finished for parent review.
Native report and decision-hover overflow, font fit and wrapping remain unresolved, because available event rendering supplies a graph rather than the native popup and artifact retrieval failed.
Public-values GUI visual evidence remains with its explicitly separate owner, and this patch does not change its text or layout.
Native CPP precision, timer refresh/restoration/expiry, factory assignment and actual repairs remain unverified user-owned evidence, as required by the accepted helper contract.
The blocker-tooltip gameplay caller is pending parent wiring.
Workbook parity is pending the spreadsheet owner if those fields contain industrial terms.
There are no additional unresolved wording decisions, design expansion proposals or gameplay simplifications introduced by this patch.
Skills used: chaos-redux-events, chaos-redux-decisions-missions and chaos-redux-subagents.
No skill was changed.
