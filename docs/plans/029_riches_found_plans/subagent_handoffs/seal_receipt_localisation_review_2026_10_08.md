# Event 029 seal receipt localisation review

Disposition: implemented bounded read-only audit, with two wording recommendations and unresolved native evidence.
Authority: the parent's 2026-10-08 assignment limits this review to `decision_riches_found_gold_seal_depths`, `decision_riches_found_demons_permanent_seal`, the new readiness key, and their directly linked requirement, cost, and consequence text.
Only this handoff was written.
No gameplay, localisation, spreadsheet, export, Git, game, child-agent, GUI, or probability changes were made.
This is not acceptance or completion of the whole Event 029 sealing route.

## Reviewed source and exact keys

The workspace is `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
Paths below are relative to it unless an installed-game path is supplied.

- `common\decisions\029_riches_found_decisions.txt:6951-7107`: Gold decision.
- `common\decisions\029_riches_found_decisions.txt:7297-7455`: Demons decision.
- `docs\events\029_riches_found\seal_receipt_contract.md:1-118`: current public wrapper, caller-storage, payment, cancellation, and refund contract.
- `common\scripted_triggers\029_riches_found_seal_receipt_triggers.txt:7-203` and `common\scripted_effects\029_riches_found_seal_receipt_effects.txt:9-218`: directly linked preflight, quote, receipt, debit, refund, and family wrappers.
- `common\scripted_triggers\029_riches_found_cost_triggers.txt:9-18,56-63,80-82,465-486` and `common\scripted_localisation\029_riches_found_scripted_localisation.txt:428-443,524-533`: the four relevant resource gates and text selectors.
- `common\scripted_effects\029_riches_found_effects.txt:394-402,1457-1468,2513-2525`, `common\scripted_triggers\029_riches_found_triggers.txt:572-579`, and `common\scripted_effects\029_riches_found_harm_effects.txt:193-210`: pressure bounds, partial-seal ordering, and conditional entombment.
- `docs\events\029_riches_found\seal_project_contract.md:40-41` and the relevant evidence/limits in `docs\plans\029_riches_found_plans\subagent_handoffs\seal_safety_review_2026_10_08.md`: existing route gaps, human harm, and independent achievement disqualification.

All 22 selected English keys have exactly one definition across `localisation\english\*_l_english.yml`.
The following 14 primary keys are in `localisation\english\029_riches_found_decisions_l_english.yml`:

```text
riches_found_seal_project_ready_tt
decision_riches_found_gold_seal_depths
decision_riches_found_gold_seal_depths_desc
decision_riches_found_gold_seal_depths_tt
riches_found_cost_gold_seal_depths
riches_found_cost_gold_seal_depths_blocked
riches_found_cost_gold_seal_depths_tooltip
decision_riches_found_demons_permanent_seal
decision_riches_found_demons_permanent_seal_desc
decision_riches_found_demons_permanent_seal_tt
riches_found_cost_demons_permanent_seal
riches_found_cost_demons_permanent_seal_blocked
riches_found_cost_demons_permanent_seal_tooltip
decision_riches_found_permanent_seal_tt
```

The other eight reviewed keys are `riches_found.cost.civ_standard.available`, `riches_found.cost.civ_standard.blocked`, `riches_found.cost.manpower_standard.available`, `riches_found.cost.manpower_standard.blocked`, `riches_found.cost.manpower_heavy.available`, `riches_found.cost.manpower_heavy.blocked`, `riches_found.cost.support_heavy.available`, and `riches_found.cost.support_heavy.blocked`.
The direct visible flags `riches_found_mine_state`, `riches_found_layer_gold`, `riches_found_gold_depths_sealed`, `riches_found_layer_demons`, `riches_found_contract_active`, `riches_found_occupation_active`, and `riches_found_demons_permanent_seal` also have wording in `localisation\english\029_riches_found_requirement_flags_l_english.yml`.
This is selected-key coverage, not an audit of the entire decision set or asset package.

## Findings

Missing key list: none found in the selected keys and directly checked flag keys.
Duplicate key list: none found among the 22 selected English keys.
Scripted localisation issue list: none found in the four selected getters, their eight result keys, or the three inspected aliases.
File encoding concerns: none found in the two relevant English localisation files, which decode strictly as UTF-8 and retain BOMs.
No source wiring was changed.

The new key at line 783 is `riches_found_seal_project_ready_tt: "This project is not already under way for our government, and its crews and tools are available."`.
Both `available` blocks call their pure manual preflight inside `hidden_trigger` under this `custom_trigger_tooltip`.
All thirteen outer temporary outputs are allocated there, and in each custom-cost, start, removal, and cancellation block.
The preflight and its nested trigger definitions write temporary scratch only.
The dynamic `rf_seal_pending_[FAMILY]_[SEQ]` flag, stored receipt fields, counter predicates, and `rf_seal_epoch_exhausted` flag therefore have no exposed requirement path in these two source blocks.
The readiness sentence is concise, describes project availability, and contains no achievement or receipt implementation disclosure.
Actual native tooltip rendering remains unverified.

| Decision | Native commitment | Manual quote | Duration |
| --- | --- | --- | --- |
| Gold | 2 civilian factories | 300 manpower and 150 support equipment | 60 days |
| Demons | 2 civilian factories | 600 manpower and 150 support equipment | 90 days |

Each inline row retains exactly three resource getters, with matching civilian-factory, manpower, and support-equipment texticons.
Their available/blocked selectors invoke the same component gates as their decision cost composites.
The factory gate is `num_of_available_civilian_factories > 1`, and manpower gates use inclusive `manpower_k` thresholds of 0.3/0.6, not 300/600 in thousands.
Support gates and the receipt quote both use the exact `support_equipment` inventory at an inclusive 150 threshold.
Source boundary reasoning gives blocked/ready/ready at 1/2/3 factories, 299/300/301 Gold manpower, 599/600/601 Demons manpower, and 149/150/151 support equipment when all other requirements are satisfied.
These are predicate traces, not executed native scenarios.
If the receipt gate blocks for a non-stock reason, the aliased blocked cost row may still show individually affordable resources in their normal colour, while the readiness requirement explains the separate block.

The start helper snapshots the quote before a single manpower/support debit.
The two decisions contain no additional old direct debit or fixed refund branch.
Removal uses the family's resolver and gates success on `result_consumed`.
Cancellation delegates to the matching cancel helper, and the shared refund path credits the stored quote after a fresh successful closure.
This aligns displayed current costs with selection payment in source, while cancellation refunds the amount actually paid rather than rereading current tuning.
The source proof does not establish native factory reservation, callback serialization, or execution.

Gold's effect key at line 229 references the existing `riches_found_scaling.partial_seal_pressure_add` (+12) and `riches_found_action_delta.negative_18` (-18).
The new partial seal runs only when no partial seal exists and temporary closure is allowed, then its helper clamps pressure to 0-100 before the -18 operation.
The later refresh clamps again.
The tooltip correctly states conditional strain before the reduction and does not promise a universal net -6.
For example, a successful new partial seal at pressure 95 produces 82 after the two bounded operations, while pressure 50 produces 44.
Without that partial-seal branch, pressure 50 produces 32.
These examples explain source ordering only.

Demons' key at line 250 is exactly `$decision_riches_found_permanent_seal_tt$\nA military purge does not evacuate the trapped shift.`.
The shared key at line 383 describes conditional entombment, up to 220 deaths, Local Order -15, Revenue Legitimacy -20, condemnation, and safe evacuation/exhaustion cases through existing constants.
The owning harm predicate checks severe collapse or supernatural crisis, excludes exhausted deposits and both evacuation flags, and does not treat military purge as evacuation.
Harm is recorded before permanent cleanup in the Demons success body.
Achievement disqualification is independent of the human-harm amount and remains documentation-only in this review.
Neither inspected decision tooltip exposes achievement routes or disqualifiers.

## Prose-quality recommendations, not applied

- Vagueness: no blocking issue in the new readiness sentence or selected descriptions.
- Bloat, repetition, and obvious explanation: Gold's `The deep sections are sealed` repeats the title, description, and action already established in the cost tooltip.
- Overcomplication: the shared permanent-seal key joins the conditional deaths, two value losses, and condemnation into one long sentence.
- Style-rule repair: no em dash, sentence semicolon, staged contrast, staccato chain, process-history text, or achievement spoiler found in the inspected passages.

Recommended Gold wording for `localisation\english\029_riches_found_decisions_l_english.yml`, key `decision_riches_found_gold_seal_depths_tt`:

```text
Extraction Pressure: §G[?constant:riches_found_action_delta.negative_18|0]§!, with §R+[?constant:riches_found_scaling.partial_seal_pressure_add|0]§! strain beforehand if a new partial seal is needed.\nCompulsion recedes in the lower workings, leaving only stable upper workings in production.
```

This keeps the pressure sentence and both dynamic tokens, then combines the outcome text without the repeated sealing explanation.
It does not change gameplay meaning or make a net-change claim.

Recommended shared wording for the same file, key `decision_riches_found_permanent_seal_tt`:

```text
The mine is permanently sealed and removed from production.\nIf the workings are in a severe collapse or a supernatural crisis and the workforce has not been evacuated, the trapped shift is entombed. Up to §R[?constant:riches_found_harm.entombment_civilian_deaths|0]§! people die, Local Order §R[?constant:riches_found_harm.entombment_order_loss|0]§!, Revenue Legitimacy §R[?constant:riches_found_harm.entombment_legitimacy_loss|0]§!, and the world condemns it as an atrocity.\nAn evacuated mine, or one sealed because the deposit is exhausted, is closed without loss of life.
```

This splits the condition from its consequence while retaining every condition, value, colour code, and safe-case exception.
The existing Demons alias would inherit it automatically.
The shared key also has other consumers, so the parent must review those before applying this optional recommendation.
No recommendation has been installed or presented as final player-facing wording.

Dynamic text opportunities: the reviewed costs, timers, pressure deltas, and harm amounts already use existing constants and scripted selectors.
The conditional Gold wording is sufficient for this bounded integration.
A future route-owned patch may give specific entrance, integrity, and resistance blocked reasons when those mechanics are accepted and implemented.
Do not expose receipt identifiers, invent unavailable gates, or promise an exact net pressure change to fill that gap.

Sourced-quotation preservation notes: no sourced or attributed quotation appears in the inspected passages.
No existing quotation, dynamic token, format code, condition, cost, requirement, or consequence was changed by this audit.
Cross-surface mismatch notes: receipt documentation and the selected source cost/display contract agree on the above quotes and timers.
The existing entrance/integrity/resistance gaps remain full-route blockers, not proof of new receipt-localisation defects.
The workbook and export CSVs were not read or edited, so catalog agreement is unverified.
For `chaosx_spreadsheet_doc_worker`, the only newly integrated key is `riches_found_seal_project_ready_tt` with the exact current wording quoted above.
No catalog change is requested for this requirement key, and the two recommendations are proposals rather than wording to mirror.

## MCP evidence and limits

The connected reference and source-lookup routes were discovered through live metadata and returned successful read-only results.
This verifies those individual calls, not universal service health.
`hoi4.source_lookup` returned one exact unshadowed definition per decision under workspace-index revision `3b390fb7f959e7370db5174396f1cfb22d7e6f9aa8d86bd46f5eeaf3473cd4fc`.
Their full bounded bodies were read directly from disk.
No helper-expansion, job, task, probability, rewrite, or renderer route was invoked.

Initial `hoi4.decision_inspect(mode=inspect)` calls without scenarios were rejected with `Decision inspection requires declared scenarios at scenarios`.
Corrected requests selected each exact decision ID and one `receipt_localisation_cost_floor` scenario with actor GER and only 2 free factories, 0.3/0.6k manpower, and 150 support equipment declared.
They returned `DECISION_ANALYZED_PARTIAL`, `complete = false`, 100 unresolved definitions, and failed `decision-coverage` validation at the same source revision above.
The adapter reported an aggregate index of 8,316 decisions and 2,070 categories, despite the exact ID selectors.
Those counts do not expand this assignment or establish coverage of any other surface.
No route/control/receipt bindings or live native outcome can be inferred from these partial scenarios.
The linked full reports were retained as URIs only and were not opened or interpreted as numeric AI or payment evidence.

- Gold artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7400740c13238865803dcb3a722e181f1f3a8ce43575eb5ae435e9d8ac280964/d4f36d1c417c3b7075d2236bea2ecf8f23dbae9277a00958cd27ba0a379c9fcb/decision-d3db8a51a47e5a4d958ba0b7.json`.
- Demons artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f3a8a2f8b071da09b87bc016b6e2cd3eaed1c1f57174bca385be0ceaa6187b3a/adb554286cc3263d588cd65937c833a75d445c31e74950425a84af7abf57dbef/decision-c066fb601223f29376e04323.json`.

`nativeListVisualEvidence` remains unavailable under the parent-reported existing GUI category-name/window mismatch.
The prior safety handoff records attempts using `windowName = riches_found_mine_management` without a returned render.
This review did not retry that category name as a valid window, invent a dedicated GUI, or claim overflow, wrapping, alignment, or cost-row fit passed.
No render is needed to establish the source existence of one new text key, and source review is not native visual proof.
No event popup, focus, technology, map, or dedicated GUI surface was included in this assignment.

Standalone Technology Tree Viewer availability was checked separately against the connected tool inventory.
No standalone viewer capability was exposed, although `hoi4.tech_inspect`, `hoi4.tech_render`, and `hoi4.tech_compare` are exposed.
This is a connected-package viewer gap, not proof that those services are healthy or that a separate local application is absent.
Technology routes were not called because no technology is in scope.

## Reference citations and source identity

Read through `hoi4.reference_context`, targeted search, and revision-bound `hoi4.reference_read`:

- Installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md:2431-2441,2482-2489`, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`: overridden AND tooltips and the compatible `custom_trigger_tooltip` alias.
- Offline `paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md:311-336`, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`: native base/blocked/hover key selection and custom display versus manual payment.
- Offline `paradox_wiki\Localisation - Hearts of Iron 4 Wiki.md:276-346`, revision `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`: localisation bindings and custom-trigger tooltip use.

Installed `common\decisions\_documentation.md:1-46` was read directly, SHA-256 `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`, for native country/target scope and refresh semantics.
Vanilla precedent `game:common/decisions/AST.txt:2-42`, `AST_union_strike`, was read directly and through `hoi4.source_lookup`, revision `51dfe78c66fc13df21be2d4991dbe9eced8c7a1ad081df1b087c39ae91a9d10d`, for timed `civilian_factory_use` and native removal.
The index revision changed during the shared-workspace review, so these references are independently dated evidence, not a frozen whole-workspace snapshot.
The three exact texticon definitions were located at installed `interface\texticons.gfx:111,172` and mod `interface\chaosx_texticons.gfx:90`.
The two decision sprite definitions were located at `interface\029_riches_found.gfx:176,224`.
Their presence proves source definition coverage only, not a rendered asset package.

Snapshot SHA-256 values recorded during this audit:

| File | SHA-256 |
| --- | --- |
| `common\decisions\029_riches_found_decisions.txt` | `6cc508136d8e3b94443204603f16506ec4cb10760e1deaeb665b57dd69df4107` |
| `localisation\english\029_riches_found_decisions_l_english.yml` | `972deef98d14ba2f24708e70f441032c5f8b438749f1655482524997f3ec36a4` |
| `localisation\english\029_riches_found_requirement_flags_l_english.yml` | `5980102291097d4a138e0bdd9940a7f5db0ce028516dd2087e329b2a18eda783` |
| `common\scripted_triggers\029_riches_found_seal_receipt_triggers.txt` | `9f8c3f10fd8a7f67652ea5d4e45bba4cefc9eb9e38ddb73f49287bfcf5aa5b0e` |
| `common\scripted_effects\029_riches_found_seal_receipt_effects.txt` | `0154ef86f38c47ebf9324252ffc4f662551ce6e819fb934eb40a07cf1649dc81` |
| `docs\events\029_riches_found\seal_receipt_contract.md` | `798fcdbaa3c7f6e3d72af04c706e9ba8ce5c272edbd971f227358d82faeab609` |

Completed validation: selected-key uniqueness, direct scripted getter/alias resolution, resource-gate/display/debit tracing, thirteen-slot caller storage review, hidden receipt requirement review, conditional pressure ordering, entombment ordering, and actual prose review.
Skipped validation: native list rendering and engine execution remain unavailable/unperformed, full scenario coverage failed, spreadsheet comparison and probability analysis are outside this assignment, and the parent-owned source tests were not rerun or counted as this review's evidence.
No new mechanic plan, source patch, or skill update was created.
Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`.
The bounded localisation review is complete, with the two optional prose decisions above left to the parent.
There were no implementation simplifications because no implementation was authorized here.
Full-route and native evidence limitations remain explicitly unresolved.

## Parent acceptance and implemented prose, 2026-10-08

Disposition: implemented.
Acceptance basis: the parent's follow-up explicitly accepts and reports applying both wording recommendations in this handoff.
Direct readback confirms that `localisation\english\029_riches_found_decisions_l_english.yml:229`, key `decision_riches_found_gold_seal_depths_tt`, contains the proposed combined compulsion/upper-workings sentence, and line 383, key `decision_riches_found_permanent_seal_tt`, contains the proposed period separating entombment from its consequences.
Both values exactly match the proposals quoted above.
The earlier proposal-only disposition is historical and superseded by this acceptance for these two keys.
Neither prose decision remains unresolved.

Gold retains the same conditional +12 strain before the -18 reduction, with the same constant references and formatting.
The shared permanent-seal text retains the same conditional harm of up to 220 deaths, Local Order -15, Revenue Legitimacy -20, condemnation, and evacuation/exhaustion exceptions, with every existing dynamic token preserved.
The Demons alias inherits the shared wording without an additional key change.
These changes remove repeated explanation and separate an overloaded sentence without changing gameplay meaning.
No sourced quotation is affected.

Current callback identity is accepted under the native inline contract in `docs\events\029_riches_found\seal_receipt_contract.md:4,21,91-98,127`.
The family wrappers require COUNTRY THIS = ROOT = original payer and FROM = the exact original mine STATE, with resolve/cancel called inline at the matching original native removal/cancellation boundary.
This is accepted contract identity and source integration, not observed engine execution.
Native callback execution, serialization, civilian-factory ordering/reservation, and native display remain unproven by this follow-up.
The entrance/integrity/resistance full-route gaps also remain unresolved.

Direct hash readback confirms the decisions source still matches `6cc508136d8e3b94443204603f16506ec4cb10760e1deaeb665b57dd69df4107`, receipt triggers still match `9f8c3f10fd8a7f67652ea5d4e45bba4cefc9eb9e38ddb73f49287bfcf5aa5b0e`, and receipt effects still match `0154ef86f38c47ebf9324252ffc4f662551ce6e819fb934eb40a07cf1649dc81`.
The earlier localisation hash is the pre-prose snapshot and no longer identifies the current localisation file.
Current localisation SHA-256 is `3c1a4497d7812cdd277924b92cee610df9630b75fb4cb916e12fc0943d9dc274`.
The receipt contract has gained parent-integration text since the original review, shifting its current line references by nine lines.
The original contract hash and line citations above remain historical snapshot evidence.
This follow-up changes only this handoff and makes no new MCP query, pixel/render, cost-row, raw-flow, probability, engine, Git, child-agent, or spreadsheet validation claim.
The existing partial MCP artifacts and visual evidence limits retain their original scope.
