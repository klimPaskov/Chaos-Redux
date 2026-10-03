# EC-A02 ordinary achievement receipt proof repair

Disposition: implemented and independently verified for the bounded typed proof, family admission, owned source, and three named external forwarding boundaries.
Native acceptance, full registry coverage, and exact proof binding for existing untyped rows remain unresolved.
Acceptance basis: the parent/user's explicit EC-A02 assignment requires Part 7's recorded positive payment, source, logical-primary role, claim equality and successful unrefunded commitment, with no price/action/AI changes.
The parent owns EC-A01's negated-alignment and shared VM NOT/NOR dispatcher; neither was edited by this worker.
The [completion audit](2026-10-03_exact_cost_source_completion_audit.md) is the defect source; [Part 7](../../../specs/026_black_friday_specs/026_black_friday_spec_part_7_assets_and_achievement.md) supplies the eligibility design.

## Public proof behavior

`black_friday_record_achievement_transaction` executes real strict receipt proof before appending an achievement row or calling family credit.
The new shared validator requires an indexed, structurally valid component chain, transaction/component source 26, the required record state, no component refund, zero refunded total, positive recorded ordinary/paid values, and an explicit owner-recorded logical family matching the claim.
It validates full stored totals against actual linked rows and validates claimed ordinary/paid amounts against the designated primary component or the owner's tagged primary-cost subtotal.
The logical family is never inferred from PP or another resource kind.
Unknown/conflicting source-26 role metadata cannot supply achievement proof.
Generic source-zero receipt recording, settlement and actual-paid refund remain usable and cannot supply Black Friday achievement credit.

Immediate ordinary credit requires settled state 4.
A pending-refundable registration requires recorded state 1, stores validated ordinary/paid claims with the existing family/sale fields, and gives no early family credit.
Confirmation revalidates those claims against a settled/unrefunded receipt before committing progress.
Ordinary confirmation after expiry remains excluded by the existing active-sale guard.
The explicit delayed PP-only owner path retains its accepted post-expiry eligibility and requires the PP primary component plus wholly PP-only positive receipt payment.
The accepted native Japan raid bridge is unchanged and tested independently through its actual callback; it does not fabricate a shared receipt.

Historical scanner-only observations that an indexed/refunded receipt had proof-valid one are not current eligibility evidence.
The earlier scanner can no longer be used to certify a public achievement claim from mere indexed-row existence.

## Reusable metadata contract

Before EVERY shared record call, the owner forwards:

| Temporary input | Meaning |
| --- | --- |
| `universal_cost_transaction_achievement_family_id` | registry-defined logical primary family |
| `universal_cost_transaction_achievement_primary_component_id` | exact primary component ID, or zero for the explicit group basis |
| `universal_cost_transaction_achievement_cost_basis` | `constant:universal_cost_achievement_basis.primary_component` (1) or `.primary_group` (2) |
| `universal_cost_transaction_achievement_primary_member` | one for a included primary-cost row, zero for secondary rows |

The record API snapshots and consumes this tuple to prevent its accidental reuse on an unrelated later component.
The first component binds the normal transaction role columns; every continuation must match that tuple.
Invalid/missing continuation invalidates proof only, not payment/receipt/refund success or amounts.
Per-component normal family/membership columns supply evidence independent of later public caller claims.
Single-component basis selects exactly one named member and compares its recorded ordinary/paid amounts.
Group basis sums all explicitly included concrete-model rows and excludes secondary costs; it is not a whole-bundle-total fallback.

Five normal arrays extend the payer receipt schema: transaction family IDs, proof-primary component IDs, cost bases, component family IDs and component primary-member flags.
`universal_cost_prepare_achievement_receipt_metadata` lazily resizes them to canonical row counts and preserves existing prefixes.
Missing legacy suffixes receive unknown zero metadata; no family is reconstructed from old primary flags or resource kinds.
`universal_cost_bind_achievement_receipt_metadata` is called only by successful component record and has normal metadata side effects, no temporary return.
The validator and scanners initialize caller-owned temporary outputs at nested boundaries.
The new helper overviews accurately name scope, inputs/outputs, defaults and side effects; the old record header is attached to the actual record helper again.

Two normal achievement claim columns store the validated ordinary/paid amounts for pending confirmation.
Lazy claim-schema preparation changes no earned family, counter, pending/refund state or targeted receipt pointer.
Legacy pending/source-26 receipts without trusted role/claim metadata retain their state and refundability but new proof is explicitly blocked.
No retrospective owner binding for those untyped rows is guessed or represented as implemented.
The source suite models regular-state serialization and rehydration; native save/reload evidence remains pending.

## Owned owner mappings

All 23 direct record boundaries in `026_black_friday_effects.txt` and the allowed RSA payment loop forward the four inputs.
The unique public-source test records the actual role statements at every boundary and asserts all fields exist before the real shared call.

| Owned logical owner | Family / exact claim basis |
| --- | --- |
| Fury bundle | supplied registry primary family and selected primary component; component basis |
| Communist national counter-agitation | political power / political-power component |
| Communist local/emergency intervention | equipment / infantry-equipment component |
| Biological medical capacity | equipment / support-equipment component |
| CBRN inspections/forensics | supplied diplomatic family / instrument model group 1–3, excluding support |
| CBRN sponsor | diplomatic / five gas-mask model rows, excluding decontamination and truck costs |
| CBRN shelter | state project / support-equipment component |
| Alien landing reservation | equipment / exact laser reserve component; pending-refundable until commitment |
| Africa elephant logistics | equipment / exact elephant-equipment component |
| CBRN protection pair | equipment / support-equipment component |
| CBRN theater assignment | equipment / three decontamination model rows, excluding CP and fuel |
| CBRN external protective-aid fee | political power / exact PP fee component; delayed PP-only completion |
| All five RSA purchases | political power / exact PP component; secondary CP, train, support and stability payments retain their resource identity and amounts |

Concrete resource-kind lists in the three group-forwarding helpers identify their already declared owner's model subtotal only.
They do not derive a logical family from resource kind.
The separate explicit proof-primary ID also avoids depending on legacy positive-primary-marker ordering in multi-resource owners.

## Parent-wired external owner forwarding

The parent wired the following three boundaries after the first frozen 31-case run.
This worker read these two source files without editing them and extended only the proof test and evidence artifacts.
The three forwarding blockers are closed in the bounded source proof.

| Exact external boundary | Required tuple |
| --- | --- |
| `common/scripted_effects/017_random_faction_effects.txt`, `random_faction_black_friday_pay_component_list`, current record call near line 1592 | `random_faction_black_friday_primary_family_id`, `random_faction_black_friday_primary_component_id`, component basis, member one iff current component matches that ID |
| same file, `random_faction_black_friday_pay_request_liaison_component` | command-power logical family, FILE-local `@random_faction_request_liaison_root_component_id = 1701`, component basis, member one only on row 1701 |
| `common/scripted_effects/germany_mengele_effects.txt`, `mengele_clone_army_black_friday_pay_command_power`, current record call near line 576 | command-power logical family and component ID, component basis, member one |

Line numbers are the read-time locations and may move with the external worker's patches; function names and shared-call identity are authoritative.
An attempted whole-file parse of the Germany file encountered an unrelated escaped clone-unit string unsupported by this test parser; the known record boundary was located directly with bounded source reads instead.
No broader Germany implementation claim follows from that limited discovery.
Neither the full family registry nor every owner is called complete by this repair.
The liaison requester and leader each own a separate receipt.
Leader equipment row 1702 retains logical family CP but primary membership zero, with no independent leader achievement call.
The source suite executes actual record-forwarding and public-claim fragments with the real shared record/lookup/scanner/credit APIs.
It verifies representative RF primary ID 4, exact liaison IDs 1701/1702, requester-only CP credit, rejection of equipment and CP claims against the leader-only receipt, and the actual Mengele successful record-to-settle-to-public-credit continuation.
It does not execute full owner allocation/quote/debit, cross-country outcome logic, or the native requester/leader eligibility gates.
Only consumed record-result storage is required by the fragment tests.
The unused recorded-component index is allowed to disappear under conservative cleanup rather than adding declarations to owner source.

## Source validation

[Public proof suite](2026-10-03_achievement_receipt_proof_source_tests.js) executes the actual public record, strict scanners, shared record/lookup/chain APIs, pending confirmation, committed-family accounting and family-credit body under conservative scripted-helper frame cleanup and the parent's NOR model.
No record, scanner, lookup, confirmation or family-credit helper is mocked.
Native country classification/eligibility, native resource operations and final engine achievement delivery are modeled or unobserved and are explicit limits.

34 public-boundary scenarios pass, including all EC-A02 adversarial cases: fully refunded, partly refunded, different source, stored paid 1 versus claimed 5, mismatched recorded ordinary amount, zero recorded payment/ordinary, and unsettled immediate credit.
The final external-owner extension executes 739 actual helper returns and drops 1,942 newly created temporary entries under conservative frame cleanup.
All 23 owned component-record boundaries explicitly forward all four metadata inputs.
The suite additionally rejects family, primary, component-source/refund, total and missing/conflicting-metadata defects; exercises exact primary/group subtotals, secondary non-PP evidence, pending no-early-credit and repeat confirmation, post-expiry exclusions/exceptions, source-zero generic refunds, legacy unknown migration, modeled reload, and manual/forced/AI disqualifiers.
Published family/payment evidence is retained in the result artifact.
Accepted native Japan delayed resolution still reaches its real family-credit body without a synthetic receipt.

The shared receipt/native dispatch suite is updated to typed strict-scanner fixtures; its old indexed/refunded scanner expectations are historical only.
Its final rerun passes 45 scenarios and records identical captured/final BF hashes with no concurrent source change.
The 434 arithmetic and 56 quantizer cases, the parent's NOR/misalignment checks, and RSA 295 purchase plus 30 request checks still pass in the inspected source models.
The outer declaration audit reports 743 known boundaries and zero missing consumed-output storage gaps.
The parent explicitly authorized reconciliation of `black_friday_outer_caller_source_tests.js` after its old lookup-location count failed 8 versus 18.
The reconciled suite passes 11 current scenarios with no fixed lookup delta or current-versus-current comparison.
It pins committed `e64e95aa3bcb9fcab5a38a248cad28aa78bd2294` as the post-caller/pre-proof baseline and retains `f32aaa4b7acc3621fcb5375743b63bfc7a81f739` for the historical outer-frame chapter.
It compares all 84 unchanged BF, 21 shared-core and 11 RSA definitions against that committed baseline after removing only the explicit four-input role statements, four shared record snapshots, verified pure metadata helper calls, and metadata-only IF blocks whose conditions contain only read-only variable checks.
No whole cost file or unchanged helper is skipped.
Three new metadata helpers are checked against declared write boundaries, including exact resize column/count shapes and a bind helper restricted to role-column and private-validity writes.
Negative controls retain payment, flag and mixed gameplay/metadata branches and reject an injected receipt-total write in the metadata binder.
The exact semantic-change allowlist contains only the two scanners, public achievement record and pending confirmation.
Their strict source/state/family/claim/pending semantics are tested by a fresh child-process execution of the current 34-case public proof suite, with matching BF/core/RSA hashes.
The added ordinary validator has separate public-proof coverage and the new claim-schema helper has explicit purity checks.
Current evidence includes all 743 declaration boundaries with zero missing storage gaps.

Source comparison and test identity are not native MCP, live debit/display, save/reload, multiplayer, or performance proof.
Reference context, a 20-line no-reference public-record lookup and narrow Event 026 inspect returned no result within 15,000 ms observation windows in this tranche.
No route absence, helper-expansion health, graph/artifact URI or engine acceptance is fabricated.
Installed array-resize documentation and the offline temporary/targeted-variable rules were consulted under the existing recorded local file identities.

## Frozen source evidence

[Current result artifact](2026-10-03_achievement_receipt_proof_source_results.json) retains complete production hashes, actual received family/payment evidence, actual owner forwarding expressions, strict scanner snapshots, frame cleanup counts and regression counts.
The last worker production edits were validator overview wording and indentation only.
The parent then wired only the external metadata declarations, with identical captured/final external file hashes in the 34-case run.

| Source | SHA256 |
| --- | --- |
| `common/scripted_effects/026_black_friday_effects.txt` | `02f16b293e6aa4c33d85d4b123a12126343b5547d7393dd07ad451a7f98b53fc` |
| `common/scripted_effects/chaosx_universal_cost_effects.txt` | `d2d04617d66ccb6dbd240e82cca8b1fabde24a2fec7fadc9bfa54c6de768d7f8` |
| `common/scripted_effects/012_africa_rsa_purchase_effects.txt` | `fc2b62492eedc337810a3844bc3d7b27725093443a2425b2ac11ef8946b617f0` |
| `common/script_constants/chaosx_universal_cost_constants.txt` | `97e0fd75044b15ab1735d935abc8648060ff20e7e977abc1d942cece43d10fb9` |
| `2026-10-03_achievement_receipt_proof_source_tests.js` | `17a8255ec846fe8e8204252ce3524be6951b2601c5b0cadd03d2bc17ee34c1aa` |
| `common/scripted_effects/017_random_faction_effects.txt` (read-only parent-wired source) | `09e82c482598cd5336a3407d32e4a270bc1aeed766ae06322de45ecbde6075a4` |
| `common/scripted_effects/germany_mengele_effects.txt` (read-only shared source, including unrelated work) | `783659c4fc394a007570210acd2d18fe7faad39249faa07f71b2832bb52536ae` |
| `exact_quote_source_tests.js` | `50dacff487c6487d8a32991bf9a9435c6351ef0a699c8a8a20d66ec051421bc0` |
| `universal_cost_receipt_lifetime_source_tests.js` | `fda92be7db9bf30a9680e71d4e8c722e71bb0db87fb993693bf08eb4524fa609` |
| `black_friday_outer_caller_source_tests.js` | `53b3aafd3d0a5125f5d7b23225d31e4d929ceec7bb303525a0b9aea7151ddeb7` |

Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, lines 435–442 (caller temporary lifetime/regular persistence), 551 (targeted variable pointers), and 1089/1111–1120 (array resize), SHA256 `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, supports the lexical model and lazy normal schema extension.
Installed `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`, lines 6397–6410, SHA256 `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, documents resize preserving the prefix and default-zero appended entries.
These local source rules do not prove native serialization, duplicate-preserving arithmetic traversal, performance, actual resource debit/delivery, multiplayer, or final achievement awarding.
No health/version/script_validate route was available in this worker's discovered tool inventory; the exposed narrow reference/lookup/event routes produced no result within the recorded windows rather than an established absent-service finding.

## Changed files and limits

Production changes: proof helpers/public record/confirmation and metadata forwarding in `026_black_friday_effects.txt`; neutral metadata prepare/bind/record in `chaosx_universal_cost_effects.txt`; only record metadata forwarding in `012_africa_rsa_purchase_effects.txt`; representation-only basis constants.
Documentation changes: matching universal API docs, universal system contract and this handoff.
Validation changes: unique public proof suite/results, strict receipt fixture expectations, and shared VM native `resize_array` support only.
The historical exact-quote handoff links this repair so its old scanner acceptance snapshots are not represented as current eligibility evidence.
Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`; no skill files were edited by this worker.
The parent-owned NOT dispatcher, exact math algorithms/central quote block, native Japan callback, action outcomes, all payment quantities/non-cost gates, prices, balance, AI, daily hooks, event enablement, assets and catalog are unchanged by this worker.
No game/log inspection or commit was performed.
No approximation or weaker family inference was introduced.
Old untyped-row proof binding and native evidence remain disclosed blockers/limits.
The outer preservation blocker is closed by the parent-authorized pinned-baseline reconciliation, with the exact source/metadata/proof boundaries described above.
The three known external role forwarding boundaries are parent-wired and covered by the bounded actual-source extension.

## Parent final family admission and source refresh

The independent auditor found EC-A02-F01: the declared consumer-goods family was absent from the validator's admitted families.
The parent added `constant:universal_cost_family.consumer_goods` without treating ongoing upkeep as a purchase.
The public suite now has 36 cases, including typed consumer-goods positives using PP and owner-adapter kinds and an undeclared-family negative control.
The independent auditor closes the bounded admission defect and verifies all 36 public cases and the 11 current-source preservation cases.
This is API admission evidence, not native consumer-goods payment or full family-registry coverage.

The canonical result JSON is refreshed from the actual final 36-case run.
BF effects are identified by SHA-256 `46c879e9627859104501ba84862daa80df1be3e46f5c1d9d757be1fc9514cec3`.
The final constants header correctly separates receipt-role basis documentation from the fixed-point guard, with no numeric value change, and the constants hash is `a113d8865c30d70075cd4fcf82655f5ab398cfca68072226abdc143c85742cc8`.
Earlier 31/34-case and before-family-admission fingerprints in this handoff are bounded historical snapshots.
They are not presented as the final source identity.

## Final parent F01 admission follow-up

This final note supersedes the earlier 34-case counts and the earlier BF/public-test/outer-test hashes above.
The parent accepted repair of F01 and added `constant:universal_cost_family.consumer_goods` to the ordinary receipt validator family admission list.
Consumer Goods family 65536 is admitted consistently with the accepted voluntary commitment and material-family classification.
The parent added a typed Consumer Goods public-positive case and an unknown-family negative case, refreshed the canonical result JSON with the current compact 36-case output, and updated the preservation suite's expected public-case count.
The parent reports 36 public-proof scenarios and 11 current preservation scenarios passing, plus 434 exact quotation, 56 quantizer, 84 malformed-registry, 45 real receipt/scanner and 325 RSA source-model checks.
This worker verified the refreshed artifact's 36-case count, current BF hash, admission line and current test hashes without editing source, tests or the parent-refreshed JSON.
The artifact now contains current public-proof evidence rather than the older combined pretty-printed regression/preservation bundle.
The parent is awaiting independent F01 auditor acceptance before committing its reviewed scope.

| Current final identity | SHA256 |
| --- | --- |
| `common/scripted_effects/026_black_friday_effects.txt` | `46c879e9627859104501ba84862daa80df1be3e46f5c1d9d757be1fc9514cec3` |
| `2026-10-03_achievement_receipt_proof_source_tests.js` | `f6f746f91735ccc49146c963075599224072f30b36664828abc89d7fb7bd6d7a` |
| `black_friday_outer_caller_source_tests.js` | `cdad3e219baf97ec82179e06fcbb682ebc335d5728173a3ac3977dd7a17bc94f` |

This is reusable API family admission and source-model proof, not evidence of a native Consumer Goods commitment surface or complete universal family-registry coverage.
Legacy unknown-role binding, native persistence, resource delivery, performance and final engine awarding remain unresolved as described above.
No price, budget, AI, outcome, enablement or other gameplay change was introduced by this documentation follow-up.
