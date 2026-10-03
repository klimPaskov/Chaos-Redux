# CBRN immediate response receipt source tests

Disposition: implemented within the parent-assigned test-only scope.
Acceptance basis: parent assignment of 2026-10-03 authorized bounded actual-source payment/refund tests and these three evidence files.
No gameplay source, shared test VM, shared receipt API, or integration call site was edited.
No files were staged or committed, as directed by the parent.

## Changed files

- `docs/testing/2026-10-03_cbrn_immediate_protection_source_tests.js`
- `docs/testing/2026-10-03_cbrn_immediate_protection_source_results.json`
- This handoff.

The suite imports the exported parser and VM from `docs/plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js`.
Its small PP/equipment adapter follows `universal_cost_receipt_lifetime_source_tests.js` in that folder.
The adapter models native resource comparisons and additions only.
`cbrn_pay_and_record_response_component`, `cbrn_refund_unfinished_response_transaction`, the shared debit/credit/record/refund APIs, and their called helpers execute their parsed repository bodies.
The VM discards temporary storage first created in returning helpers and preserves caller-owned temporary storage and regular payer storage.
Entry audits require nested helper outputs to have storage already declared by their actual source caller.

## Meaningful validation

Command: `node docs/testing/2026-10-03_cbrn_immediate_protection_source_tests.js` from the mod root.
Final result: 21 scenarios passed, zero failed, 1,074 actual helper returns, and 3,576 helper-local temporary values discarded.
Both cold and warm scenarios verify retained `cbrn_response_all_paid`, exact native debits, per-model credits, and repeated-refund idempotence.
Cold cases do not preseed nested API scratch or output variables.
Warm cases seed output and cursor storage with stale values of 999 to expose incomplete resets and cross-call lifetime errors.

| Hospital component fixture | PP | Support | Total masks | Oldest-first five-model fixture |
| --- | ---: | ---: | ---: | --- |
| Normal | 10 | 20 | 30 | 3, 4, 5, 6, 12 |
| Nominal half | 5 | 10 | 15 | 3, 4, 5, 3, 0 |
| Nominal quarter | 3 | 5 | 8 | 3, 4, 1, 0, 0 |

All seven resource-kind components are recorded, including zero-paid models, using hospital `state_project` / `primary_group` metadata with PP primary-member zero and every material primary-member one.
The separate zero-paid counterfactual case records ordinary 22 and actual-paid zero for an empty reconditioned-mask model, plus eight paid basic masks.
Neither debit nor refund creates reconditioned equipment from that ordinary accounting field.

Cold and warm failure scenarios cover insufficient first PP payment, negative ordinary first-record input, missing allocator proof, insufficient later support payment, and negative ordinary later-record input.
Failed record debits are credited by the actual shared credit API.
Recorded earlier components are refunded by the actual shared refund API.
Subsequent component calls skip payment after `cbrn_response_all_paid` becomes zero.
Every failed order restores its initial modeled resources and retains no unused allocator proof.

The emergency cases use political-power-only / `primary_component` metadata with PP primary-member one.
An unissued receipt refunds its fee and repeated calls add no credit.
A positive-issued committed-marker fixture blocks the refund helper before settlement, preserves the paid fee, and does not enter the shared refund API.
A marker for another receipt ID does not block an uncommitted transaction.

The corrupt-recorded-chain scenario includes cold and warm subcases.
Each changes the first component's stored next pointer to 999, then attempts the actual refund path twice.
Both attempts retain `cbrn_response_refund_status_@<receipt_id> = result_rejected`, preserve the paid balances and recorded state, and create no credits or refunded component states.
Repairing that fixture pointer allows the actual shared refund to restore the recorded PP/support debits and clear the retained diagnostic.
A further refund attempt creates no additional credit.

The stored-unrecorded-credit scenario includes 14 subcases covering cold and warm entry for native kinds 1, 11, and 20-24.
Every subcase first executes the actual native debit API for seven units, then supplies the exact persisted pending amount/kind as a recovery fixture.
The owner refund helper executes the actual shared credit API, restores those seven units to the same PP or concrete equipment kind, and clears both pending fields and the unused allocator proof.
Two repeated calls create no additional credit or receipt.
An unrelated receipt's pending fields remain unchanged.
These are two additional top-level scenarios with 16 internal subcases, alongside the original 19 scenarios.

The JSON contains captured SHA-256 values for each loaded source file, AST hashes for every executed source body, the reused VM hash, and final reread comparisons.
No loaded source file changed during the final run, every selected body remained identical, and the reused VM remained unchanged.
The tested CBRN effect source SHA-256 is `fe7b34d970279f89e2e7413f7ef547670cb322ba189831f61cd70975ca2d48ed`.
The tested shared receipt effect source SHA-256 is `d2d04617d66ccb6dbd240e82cca8b1fabde24a2fec7fadc9bfa54c6de768d7f8`.
Re-run the assigned test after parent source edits rather than carrying these hashes forward as current evidence.

## Reference evidence

The connected coding-tool inventory exposes none of `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, or `hoi4.source_lookup` to this subagent.
Relevant local sections were read directly.
This is a route-exposure gap for this worker and does not establish the health or availability of the parent's separately connected MCP client.

- Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, lines 437-446 and 551-553, covers temporary lifetime, unscoped temporary variables, regular scoped storage, and targeted variable names.
Its SHA-256 is `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
- Installed `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`, lines 1252-1265, 1854-1861, and 7820-7841, covers country equipment additions/removals, country PP additions, and temporary variable assignment.
Its SHA-256 is `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
- Installed `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`, lines 3835-3842 and 4547-4554, covers country equipment and PP comparisons.
Its SHA-256 is `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.

Skills applied: `chaos-redux-events` for helper output lifetime and evidence limits, and `chaos-redux-subagents` for ownership and handoff rules.
No skill changes were needed because the existing skills already cover this workflow.

## Simplifications, omissions, and blockers

No gameplay fallback or simplification was introduced.
No concrete source defect was found within these two helper contracts.
This bounded test task is complete, while parent integration and broader feature completion remain outside this handoff.

Component amounts are explicit fixtures, including the nominal half and quarter values.
These tests do not execute quotations, the allocator, or the actual oldest-first allocation block.
Persisted allocator proofs are fixture inputs that the actual receipt API must validate and consume.
Emergency commitment is a marker fixture, so positive physical issue, marker creation, fee settlement, receipt confirmation, and state/country crate accounts require parent evidence.
Stored pending-credit fields are explicit recovery inputs, so their creation after a native credit failure is not exercised.
The actual parsed native-kind credit branches report success, and no API was mocked or modified to manufacture a failure.
Retained rejected status is tested through explicit persisted-chain corruption, which does not prove native engine corruption or runtime occurrence.
Partial or unhandled recorded-refund diagnostics and unsupported-kind pending-credit retry failure are outside the requested native-kind recovery cases.
The existing VM does not represent the full `ROOT`/`FROM` issue/outcome/state-scope path or native producer provenance and resource caps.
No native AI, GUI rendering, engine behavior, or performance validation is claimed.
No Hearts of Iron IV launch or log search was performed.
Mandatory engine/MCP inspection and broader integration QA remain with the parent and cannot be replaced by these source semantics results.
