# CBRN occupied and export actual-source tests

Disposition: implemented within the parent-assigned test-only ownership.
Acceptance basis: the parent assigned durable source tests for the approved occupied/export fee transactions and concrete escrow, then explicitly requested baseline partial-native cases, repaired quarantine coverage, continuation checks, and control-change cleanup checks.
Only the three assigned test/evidence files were changed.
No engine-facing source, shared VM, index, commit, SDK, server, or game process was changed.

## Files and execution

- `docs/testing/2026-10-03_cbrn_occupied_export_source_tests.js`
- `docs/testing/2026-10-03_cbrn_occupied_export_source_results.json`
- This handoff.

Run from the mod root: `node docs/testing/2026-10-03_cbrn_occupied_export_source_tests.js`.
Final result: 46 scenarios passed, zero failed, 2,007 parsed helper returns, and 8,686 discarded helper-local temporary values.
Every captured selected body, selected constant category, scripted-localisation file, bounded control-change fragment, and reused VM remained unchanged during the final run.
The JSON contains all captured source hashes, executed body hashes, separately inspected body hashes, concrete native write observations, entry-contract counts, named fixture calls, and the pre-fix defective bodies.

The suite imports the parser and VM from `docs/plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js`.
Its adapters provide bounded native PP/equipment state, COUNTRY donor 7, recipient FROM 8 or 9, controlled STATE 100 or 101, targeted names, country/state flags, ordinary arithmetic/clamping, and literal MODEL token substitution for the actual meta blocks.
The conservative lexical cleanup remains intact for every scripted helper call.
Only caller-owned public outputs are declared by the test harness, while actual enclosing source must declare nested outputs.
The custom Black Friday quote audit checks its consumed final/valid outputs, matching the owner contract, while the shared exact quotation and receipt entry audits remain active.
No canonical fee quotation, allocator, debit, credit, record, settlement, concrete reserve, or concrete refund API was mocked.

## Executed source coverage

| Surface | Cases and meaningful assertions |
| --- | --- |
| Export fees | Actual canonical quotes 15, 8, 4 at balances fee minus one, exact fee, and fee plus one, with shortage causing no stock or PP write |
| Occupied fees | Actual canonical quotes 25, 13, 7 at the same three boundaries, factory quotations 2, 1, 1, exact affordability, typed PP-only receipt, and allocator-proof cleanup after insufficient payment |
| Missing source | Active sale without registered source rejects both canonical quotations and creates no debit |
| Source expiry | Actual shared source-clear API, persisted receipt/source fields, and actual active scripted-localisation trigger branches retain frozen paid fees |
| Accepted export cancellation | Actual start, reservation, PP payment/record, cancellation, fee settlement, and ownership release, with exact returned models, spent fee, and repeated start/cancel refusal |
| Occupied cancellation | Actual fee payment and explicit persisted program publication fixture, followed by actual cancel/refund/settle/clear, with spent fee and repeated cancel/finish no-op |
| Receipt rejection | Actual occupied payment with a conflicting existing receipt credits only the second unrecorded PP debit and preserves the original receipt |
| Export recipient isolation | Two actual accepted target rows, independent held fields and receipts, owned count 2 to 1 to 0, and repeated release refusal |
| Export exact transfer | Five real model primitives reserve and send 100 each, measure total 500, and refuse repeated sends |
| Export native anomalies | Actual reserve/refund/release/send primitives under partial debit, partial credit, partial release, partial paired send, and mismatched donor/recipient observations, including no duplicate refund of already released stock |
| Occupied/external concrete models | Actual shared STATE reserve/refund and new native observation helpers preserve mixed rows 20, 30, 40, 50, 60 and return every concrete model once |
| Valid partial STATE operations | Occupied and external debit 100 to 40 record only 40, occupied partial refund 100 to 40 retains 60 and donor/active receipt until exact retry |
| Invalid STATE observations | Both families reject negative and oversized debit/credit observations, retain mismatch evidence and active ownership, block later native writes, and refuse repeated reserve/refund |
| STATE donor isolation | Occupied cancel returns five models for its owned state while leaving another donor's marked receipt intact |
| Continuation fix | Actual owned-receipt/current-control/core/population/reserve/need gate allows a busy state with empty PP and unreserved stock, then rejects zero need and a different donor |
| Quarantine callback guards | Actual parsed national payment limit rejects a positive earlier aggregate while country recovery is pending, and the actual STATE marker block preserves a quarantined target |
| Control-change cleanup | Actual first FROM.FROM receipt cleanup block retains occupied/external target flags after partial blocked refund, clears them after exact retry, and performs no further native writes on repeat |

The fee cases assert source ID, one PP component, political-power achievement family, primary-component basis, primary ID 1, primary member 1, and stored actual payment.
Factory results are quotation evidence only and do not prove native commitment counts or timer behavior.

## Confirmed baseline defects and owner repair

The suite retained concrete pre-fix evidence under `baselineDefectEvidence` in its results JSON.
The baseline shared protection source SHA-256 is `ff04b3decb07dd1fa7fd21ce9070d6de1622a320fbb960bc2380126ad2c3dfce`.
The exact parsed bodies and their individual AST hashes are preserved there.

- Actual old reservation requested a native debit of 100 while the adapter removed 40, leaving stock 60 but publishing completed 100 and held 100.
- Actual old refund requested 100 while the adapter credited 40, then published refunded 100, cleared the held row and active receipt, and left stock 40.

These failures were sent to the parent and STATE helper owner before patching.
The owner repaired the shared reserve/refund wrappers and added measured COUNTRY primitives.
The final tests execute those repaired bodies and prove measured partial accounting, exact retry, and quarantine behavior under the stated adapters.
The baseline establishes source defects under explicit partial-native inputs and does not establish that the native engine produced those observations in a live campaign.

## Final key source hashes

| File | SHA-256 |
| --- | --- |
| common/scripted_effects/cbrn_export_transaction_effects.txt | 49e275ad1804ae924b0e8bc3d9cc70b6dac27c3639fac96637c7ebd17be1b36b |
| common/scripted_triggers/cbrn_export_transaction_triggers.txt | 3c8146ed1b56dae158a06db801ebeb8838545a8abc74ddfbe6e03aa1c98006aa |
| common/scripted_effects/cbrn_occupied_transaction_effects.txt | b6224ef5db2a4f9144af5679ebcefaa010e3d978b330373829cea585e1ef5c39 |
| common/scripted_triggers/cbrn_occupied_transaction_triggers.txt | 8259ae53dcaf594b46391e5d51b8ac8a727fbb8f06ca94380ce0542caaaf3440 |
| common/scripted_effects/cbrn_protection_effects.txt | 62248367f0e75540ad18141d3636c31215f4a5a1d1502a0ce92824dc5182fdb6 |
| common/scripted_effects/cbrn_state_escrow_native_effects.txt | 107d041e9762e2e54e131c4d23e26cdab8842f2cd611213f45f181091cd1b567 |
| common/scripted_effects/cbrn_protection_decision_effects.txt | 3931110c80d36dce6379fb10dd87386720d391222f2ffbcdcaed659ece129b1b |
| common/on_actions/chaosx_on_actions.txt | 5b170cea4fe8f082949c0da1f79ce1235a4e6489ba5c06833437d86b0e78c557 |

The results JSON is authoritative for the full loaded-source hash list and selected-body stability evidence.
Re-run the suite after source changes instead of treating these identities as current evidence for another revision.

## References and skills

Parent-named export/occupied helper source, scripted-localisation files, and the two dated helper handoffs were read.
Installed documentation and offline wiki sections were read directly for the modeled native operations and scope/lifetime assumptions.
The parent explicitly prohibited new MCP/server work for this test-only task, so no live domain or reference inspection is claimed.
The connected worker tool list does not expose the HOI4 reference routes, and source tests do not replace parent MCP evidence.

| Reference | Read spans | Source revision |
| --- | --- | --- |
| Installed documentation/effects_documentation.md | 1252-1265 stock edits, 1854-1861 PP, 4833-4857 meta effects, 6550-6558 sends, 7820-7841 temporaries | 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af |
| Installed documentation/triggers_documentation.md | 3835-3842 equipment, 4547-4554 PP | 7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29 |
| Installed documentation/dynamic_variables_documentation.md | 557-560 concrete stock reader | 538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda |
| paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md | 437-446 temporary lifetime, 551-553 targeting | 62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4 |
| paradox_wiki/Effects - Hearts of Iron 4 Wiki.md | 2248-2305 stock/send rules and examples | 997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c |
| paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md | 254-267 ROOT/THIS/PREV/FROM and chained FROM | 18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49 |
| paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md | 339-356 timer, selection and cancellation semantics | 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162 |

Installed documentation paths are beneath `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`.
Skills applied: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`.
No skill update was needed because the existing source-lifetime and handoff rules cover the work.

## Simplifications, omissions, and blockers

No gameplay fallback or design simplification was introduced by this test worker.
The bounded requested source tests are complete, with exact fixture and unsupported-engine boundaries recorded here and in the JSON.
No additional source defect remains within the executed scenarios.

Named excluded context fixtures are `cbrn_protection_program_category_visible`, `cbrn_target_can_receive_exported_masks`, `cbrn_refresh_country_mask_snapshot`, and `cbrn_occupation_close_external_aid_reservation`.
The continuation scenario also supplies explicit current-need and emergency-query results instead of executing the large state demand/environment system.
The new continuation predicate itself, stored-donor ownership, native control/core/population inputs, and national reserve flag are evaluated from actual parsed source.
The country quarantine check executes the actual parsed payment limit and marker block in isolation, without simulating full national selection.
The occupied accepted-program fields are an explicit fixture after actual payment, so full selection-time state iteration, cooldown stamping, variant visibility, publication, and aggregate rollback orchestration remain outside this suite.

Actual export positive reserve/send primitives are tested, while complete positive export finish outcomes, opinions, aid counters, maintenance, Condemnation, and achievement acceptance are unproven.
Actual occupied cancel and inactive repeated finish are tested, while positive occupied physical issue, updated coverage, resistance/compliance, reduced need, and achievement confirmation are unproven.
The continuation AST check verifies that positive completion uses the reserved-distribution predicate and that its state outcome body does not clear another project's busy flag, without claiming execution of the full positive outcome body.
Control-change proof covers only the first receipt cleanup block and modeled FROM.FROM binding, excluding later contamination/fallout callbacks and external aid counter closure.
Producer/variant provenance, stock unlock restrictions, synchronous native stock readers, engine resource caps, timer lifetime, save persistence, native AI, GUI rendering, performance, and complete ROOT/FROM lifecycle behavior require parent/native evidence.
No HOI4 launch, log search, staging, or commit was performed.
