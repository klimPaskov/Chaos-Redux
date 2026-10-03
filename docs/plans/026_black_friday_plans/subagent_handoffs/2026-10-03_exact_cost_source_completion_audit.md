# Event 026 bounded exact-cost source completion audit

Date: 2026-10-03.
Disposition: blocked bounded completion, with substantial implemented source work.
Baseline status: finalized and retained, with the narrow EC-A01 source recheck recorded below.
EC-A01, the original EC-A02 receipt-integrity defect and EC-A02-F01 are implemented and independently verified for their bounded source criteria.
The reconciled bounded cost-preservation suite is independently verified, while broader canonical-family registry, native and runtime acceptance gates remain unresolved.
Closing the original defects does not establish full family coverage, native achievement acceptance or completion of the supplied tranche.
The full Event26BlackFriday goal remains active and incomplete, and default disablement remains required.
No universal, native, live, multiplayer, save, or whole-achievement completion claim is made.

## Authority and evidence boundary

The parent authorized a read-only audit of the exact quotation and receipt core, existing Black Friday caller-storage integration, and the five RSA purchase integrations.
The acceptance basis is the parent's explicit original-goal contract and the directed Part 3 reusable cost architecture, Part 4 cost coverage, Part 7 assets/achievement, and Part 8 acceptance scenarios.
This report does not reopen all Event 26 owners, the 100-owner declaration inventory, Event 12 country content, native cost groups, dedicated GUI production, or model production.
Only this report was created.
No gameplay, localisation, asset, workbook, export, index, or commit was changed, and no game or log inspection was performed.

The parent subsequently reported a frozen 43-path integration, an abbreviated `f32` base and `cf041...` proposed tree.
Those abbreviations are parent-supplied context, not independently verified full object identities.
The worktree HEAD observed during this audit was `c3c91450ca9d9c37bd386c3f560160991410ba1a`.
The file fingerprints below identify the actual audited source, independently of a shared-tree commit or the parent's proposed tree.
Reconcile these fingerprints against the final owned-path commit before using this report for that revision.

## Parent review and accepted repair dispositions

Acceptance basis: the parent's explicit 2026-10-03 follow-up accepts EC-A01 and EC-A02 as actionable findings, reports publication of the source integration identified as `e64` before this report became visible, assigns the repairs below, and requests finalization of this baseline followed by a separately requested recheck.
Publication is recorded from that parent message and does not close either finding or establish bounded source completion.
The abbreviated `e64` identity could not be resolved independently in this auditor checkout with `git rev-parse --verify 'e64^{commit}'`, which returned `fatal: Needed a single revision`.
No full commit ID is inferred, and the original audited file fingerprints remain intact.

| Finding or follow-up | Finding status | Repair disposition and owner | Accepted work and queue reason |
| --- | --- | --- | --- |
| EC-A01 | Closed for the bounded source defect, native acceptance remains unresolved | `implemented`, parent-owned and independently rechecked | Explicit AND grouping, NOT/NOR model corrections and the extended rejection matrix were reviewed and rerun in the narrow EC-A01 recheck below. The original queued assignment and baseline evidence are retained as history. This disposition does not close EC-A02 or the event goal. |
| EC-A02 | Closed for the original bounded receipt-integrity defect only | `implemented`, architect `01a10115`, external forwarding applied by parent, independently rechecked | Actual public record/confirmation/family-credit cases, the owned role declarations and three external record boundaries were reviewed at the exact hashes below. This is not complete owner coverage, native execution or whole-achievement acceptance. The separately found EC-A02-F01 is also source-repaired and rechecked below. |
| EC-A02-F01 | Closed for the consumer-goods admission defect only | `implemented`, parent-owned and independently rechecked | Declared family 65536 is admitted with explicit typed proof. Both resource-kind positives and unknown logical-family rejection pass. No native consumer-goods surface/payment implementation or full canonical-family registry coverage is certified. |
| Other existing caller integration | Outside this finalized baseline | Separately assigned to outer worker `01a101a7` | Review only the other 22 existing caller files. Lifecycle and native rules remain untouched. This assignment does not expand the current audit's three-file caller inventory or certify those additional files. |

The EC-A01 recheck below uses its original acceptance criteria and actual owner-applied patch, regression tests and source identities.
The bounded EC-A02 recheck below uses its original acceptance criteria and actual owner-applied patch, public-record-to-credit regression tests, source identities and handoff.
The subsequent EC-A02-F01 recheck below supplies reviewed source and task-specific evidence for its closure.
The subsequently supplied cost-preservation reconciliation was independently reviewed and executed below.
Closing either finding requires reviewed implementation and task-specific evidence, not parent acceptance, assignment, commit publication or an unchanged historical PASS count.
The source-semantic findings, diagnostic results, original test limits and unresolved MCP/runtime gates below remain the audit baseline.
The earlier baseline finalization changed report dispositions only and performed no gameplay edits, additional source audit, tests, MCP retry or commit.
The separately requested narrow EC-A01 recheck performs the source reads and tests recorded below and changes only this report.

## Immediate blocking findings

### EC-A01: malformed source alignment is not rejected under HOI4 NOT semantics

Current disposition: implemented and independently verified for the bounded source defect.
The following diagnosis and diagnostic results describe the original audited source fingerprint, not the repaired source.
See the narrow source recheck below for the accepted repair and its exact evidence.

Evidence: `common/scripted_triggers/chaosx_universal_cost_exact_triggers.txt:528-536` places three sibling equality predicates inside `NOT`.
They compare the ratios, priorities, and eligibility-mask array lengths with the source-ID array length.
HOI4 evaluates those siblings as NOR, so the rejection branch runs only when every equality is false.
An individual misaligned array, or two misaligned arrays while the third remains aligned, leaves `universal_cost_quote_valid = 1`.

The offline reference `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md:337-345`, specifically line 341, explicitly identifies this semantics.
It also agrees with the supplied AGENTS.md guidance to retain an explicit `AND` when negating a multi-condition conjunction.
The exact API documentation at `common/scripted_triggers/chaosx_universal_cost_exact_triggers.md` and `docs/systems/universal_cost_modifier.md:61-66` promises malformed-registry rejection, so current source does not satisfy its documented contract.

The checked-in interpreter instead implements `NOT` as `if (this.eval(v)) return false` at `subagent_handoffs/exact_quote_source_tests.js:142`.
Since `eval(v)` is a conjunction, this models NAND.
Its ratios-only malformed fixture at lines 378-383 therefore passes under a different Boolean rule from HOI4.
The 434 quotation and 56 quantizer PASS results cannot establish this rejection property.

A read-only diagnostic loaded the actual parsed quotation bodies and changed only the interpreter's NOT dispatch in process memory to `v.some(n => this.eval([n]))`.
No source or test file was edited.
The fixture used ordinary cost 3, quantum 1, family 1, and one source `{ id: 26, ratio: 5000, priority: 26, mask: 0 }`.
For each nonempty mismatch subset, an extra harmless row was appended to the indicated aligned-data arrays while retaining the source-ID length of one.
This avoids assuming how the engine handles an absent array element.

| Extra-array mismatch | Actual-source diagnostic validity | Quote |
| --- | ---: | ---: |
| None, control | 1 | 2 |
| Ratios only | 1 | 2 |
| Priorities only | 1 | 2 |
| Eligibility masks only | 1 | 2 |
| Ratios and priorities | 1 | 2 |
| Ratios and eligibility masks | 1 | 2 |
| Priorities and eligibility masks | 1 | 2 |
| All three arrays | 0 | 3, invalid diagnostic amount |

Owner action: correct the rejection predicate's Boolean grouping and the test interpreter's NOT semantics, then test individual and combined short/long array mismatches through both quotation frontends and affordability rejection.
Preserve the full arithmetic domain and one-final-quantization design.
This is a source completion blocker, not a new balance target or a request to redesign the framework.

### EC-A02: the default public achievement proof accepts ineligible indexed receipts

Current disposition: the original wrong-receipt acceptance defect is implemented and independently verified for the bounded strict API and named record boundaries.
The following diagnosis and diagnostic table describe the original audit fingerprint, not the repaired proof code.
The new recheck below separately records EC-A02-F01 and the remaining coverage and preservation limits.

Evidence: `common/scripted_effects/026_black_friday_effects.txt:66-85` sets the default scanner's `black_friday_purchase_receipt_proof_valid = 1` after an indexed receipt lookup.
It does not validate the sale-source ID, receipt/refund state, actual paid amount, positive recorded ordinary amount, or registry primary-family/component correspondence.
The non-political component count is only an additional flag.

The public `black_friday_record_achievement_transaction` body at lines 306-400 accepts positive caller-supplied ordinary and paid amounts plus that proof.
For `black_friday_purchase_is_refundable = 0`, it appends a committed achievement row and invokes family credit without independently requiring the receipt to be settled, unrefunded, or source 26.
The stronger PP-only scanner at lines 88-123 checks settled state, source and component identity, positive recorded payment, and paid-amount equality.
That scanner does not establish the ordinary default path's contract.

This violates Part 7's recorded positive payment, successful commitment, matching registry family, and refunded/free exclusions.
It also leaves the parent's explicitly requested source-mismatch rejection unimplemented in the public default proof path.
The ordinary sale guard still excludes inactive, manual, forced, debug, and AI contexts in the inspected source.
Those guards do not repair receipt provenance once the natural human sale is valid.

A separate read-only diagnostic executed the actual public record, default scanner, and shared transaction lookup bodies.
It supplied an indexed payer receipt and assumed the existing valid-natural-human-sale predicate, then observed the final family-credit call instead of executing the achievement-award subsystem.
It did not mock the record, scanner, or lookup.
All fixtures supplied family 1, claimed ordinary cost 10, claimed paid amount 5, the current sale sequence, and nonrefundable immediate credit.

| Stored receipt fixture | Stored state/source/paid | Achievement row appended | Family-credit call |
| --- | --- | ---: | --- |
| Valid settled control | 4 / 26 / 5 | 1 | Yes |
| Fully refunded | 2 / 26 / 5 | 1 | Yes |
| Partially refunded | 3 / 26 / 5 | 1 | Yes |
| Different sale source | 4 / 99 / 5 | 1 | Yes |
| Claimed payment mismatch | 4 / 26 / 1 | 1 | Yes |
| Zero recorded payment | 4 / 26 / 0 | 1 | Yes |
| Unsettled immediate credit | 1 / 26 / 5 | 1 | Yes |

State values above are the actual constants: recorded 1, refunded 2, refund-partial 3, settled 4.
These are public-source adversarial fixtures, not observed gameplay exploits, native execution, or a full five-family award proof.
The ordinary RSA happy path settles its new receipt before invoking this API, but that owner convention does not fulfill the required public receipt-integrity check.
Its settlement call cannot establish the missing source, amount, or family verification.

Owner action: require the default scanner/public record path to prove the qualifying source, positive recorded ordinary/payment amounts, matching primary family/component and claimed payment, and appropriate settled/unrefunded state for immediate credit.
Preserve the distinct pending-refundable contract and the accepted native-raid exception.
Exercise the public record-to-credit boundary with the rejected fixtures, rather than inferring it from the seventeen direct scanner cases.

## Completion status by surface

| Surface | Status in this audit | Evidence and limit |
| --- | --- | --- |
| Exact represented arithmetic and final upward quantization | EC-A01 source defect repaired, native acceptance unresolved | The explicit AND grouping and NOR models agree with the documented Boolean semantics. The 434 quotation and 56 quantizer cases, eight Boolean checks and 84 malformed-registry frontend/affordability rejections pass. Native arithmetic, iteration and consumer performance remain unresolved. |
| Positive minimum, zero/reward exclusion and source composition | Implemented source behavior for aligned fixtures | Valid-registry tests cover the represented fractional boundaries, large costs, source permutations, arbitrary quanta, masks, and more than 1,000 sources. Native arithmetic, duplicate iteration and performance remain unresolved. |
| Receipt output storage, actual-paid refund and source expiry | Implemented bounded source behavior | Six receipt bodies have caller-owned nested storage. The actual core suite passes recorded-paid refund after expiry, double-refund rejection, payer isolation and corrupt-chain cases. Native effects and serialization are modeled or missing. |
| Black Friday outer caller storage | Implemented bounded source behavior | Nine scenarios pass and 739 known boundaries have zero missing consumed-output declarations across the three explicitly inventoried files. This is not every owner/caller. |
| Sale snapshot and current quotation context | Preserved source behavior | `black_friday_activate_sale` snapshots the ratio once, registration uses that snapshot, the producer reads the current registry, and expiry removes source 26 without rewriting receipts. Whole lifecycle timing remains outside this tranche. |
| Five RSA purchases and eleven components | Implemented normal source flow, partial completion | One current quote drives display, affordability and payment. Every component is preflighted before debit and receives an actual-paid receipt. Component failures refund once in the modeled scenarios. Exceptional post-outcome settlement recovery remains open. |
| RSA request/reply integrity | Implemented bounded source behavior | Settlement precedes queueing, one pending donor lock excludes duplicate requests, and registration precedes the unchanged shipment under the two-supporter cap. Thirty fixture checks pass. Native dispatch remains unproven. |
| Ordinary public achievement receipt proof | Original EC-A02 and consumer-goods admission defects repaired in bounded source tests | Actual public record/confirm/credit rejects the original adversarial receipts, validates typed primary/group claims and admits declared consumer-goods proof. Full canonical-family registry, native and whole-achievement acceptance remain open. |
| RSA price localisation | Implemented source text, native display unresolved | Fifteen fresh getters initialize output storage, invalid quotes select Price unavailable, pending receipts select Order pending, and all four corridor costs remain in the full tooltip. Native expansion and row fit have no returned render proof. |
| AI and probability | Blocked evidence | Numeric AI expressions and reply weights are preserved, while affordability, hints and pending-target eligibility affect the selection surface. Required probability artifacts and comparisons remain missing. |
| Existing five Event 26 visual finals | Unchanged source package | All five DDS hashes still match `event26_asset_audit.md`. This is identity preservation, not a fresh visual or native texture acceptance pass. |
| Catalog and event documentation | Bounded record retained | The parent/readonly-worker reports sole ID 26 row 27, Minor Fire-Once, Needs Testing, and matching premise/evolution bodies. This auditor did not open or modify the workbook. |

All eleven RSA component rows BF-RSA-001 through BF-RSA-011 remain explicitly `blocked_pending_evidence` in `docs/systems/africa_rsa_purchase_transactions.md`.
The corridor keeps PP, CP, concrete `train_equipment_1`, and concrete `support_equipment_1` costs.
Citizenship retains its 0.01 stability quantum, and the other three actions retain their original PP/CP components.
The baseline and evolved prices in the owner ledger agree with the supplied independent rational source-model cases.
The sovereignty entry verifies the native guarantee predicate before publishing its original outcome and otherwise refunds its actual-paid receipt.

The decision/source comparisons and manual source review retain original action identities, target arrays, target requirements, fire-once controls, cooldown/timer fields and outcome quantities.
No normal/50/75 duplicate static decision records were introduced.
The intentional extra admission guard is the documented pending-donor exclusion that closes duplicate request/shipment behavior.
No cost approximation, reduced source-count/arithmetic domain, suppressed route, new daily country-wide hook or new asset substitution was found in this bounded tranche.

## Design and documentation gaps

The four immediate RSA outcomes call `africa_rsa_confirm_pending_purchase` after applying their outcome, but do not handle a non-success confirmation return in their entry effects.
The persistent pointer then blocks another purchase through `africa_rsa_can_pay_selected_purchase`.
The request action explicitly checks confirmation and refunds on failure, whereas the other four entry paths leave the pointer pending.
Evidence: `common/scripted_effects/012_africa_rsa_purchase_effects.txt:217-250`, `:251-265`, `:291-308`, `:311-343`, and `:346-357`.
The existing owner ledger's Remaining owner findings and integration plan lines 92-93 disclose this limitation.
Disposition: unresolved owner recovery/acceptance work, not hidden future polish and not established as a normal reachable failure by this audit.
The parent must retain that disposition rather than call all five outcome/receipt paths fully atomic under abnormal settlement rejection.

The original integration plan labels the bounded tranche implemented in source.
The reviewed EC-A01 and original EC-A02 repairs have implemented source dispositions within their bounded criteria.
EC-A02-F01 is now independently verified within its source admission scope, while broader native/registry/runtime completion claims remain unresolved.
The updated current cost-preservation baseline is verified within its explicit three-file comparison bounds.
The existing architect, outer-caller, RSA decision, localisation, and probability handoffs are present.
No missing patch-handoff note was identified within this assigned integration.

`docs/systems/universal_cost_modifier.md:134` still says native design and commander factors are covered, while the current registry explicitly classifies the fourteen native groups as source implementations pending composition, rounding and live evidence.
Its line 157 also retains a sixteen-native-kind summary although the actual documented dispatch map has twenty-nine pairs.
Disposition: stale summary wording, with the current registry and exact API documentation taking precedence.
The Part 8 record expressly marks its old scalar-cache discussion as Historical acceptance snapshot and links the newer exact producer, so that historical section is not treated as current twelve-family implementation evidence.

Accepted plan disposition for this audit is therefore implemented source subparts and independently verified EC-A01/original EC-A02/EC-A02-F01 repairs with reconciled bounded preservation evidence, disclosed RSA recovery unresolved, and broad canonical-family registry/native/inaccessible-surface and runtime acceptance gates retained unresolved.
No additional expansion plan or replacement design was created.

## Narrow EC-A01 source recheck, 2026-10-03

Authority: the parent's explicit request to recheck EC-A01 only, read `../2026-10-03_registry_alignment_boolean_repair.md`, verify the source and logic independently, update this disposition only after evidence review, and leave EC-A02 open.
The repair document was read completely and matches the reviewed scope.
No public achievement guard, remaining caller-file tranche, lifecycle or native rule was assessed as repaired by this recheck.

The repaired producer at `common/scripted_triggers/chaosx_universal_cost_exact_triggers.txt:528-538` nests all three array-length equality checks inside one `AND` child of `NOT`.
The outer NOT now negates that conjunction under HOI4's documented NOR semantics.
The shared VM at `subagent_handoffs/exact_quote_source_tests.js:142` evaluates NOT using `v.some`, and both RSA models use the equivalent `!a.some(...)` rule.
The offline flow-control table at `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md:337-345` was reread, including the explicit NOT/NOR rule at line 341.

An independent read-only diagnostic evaluated the parsed production rejection guard using its own Boolean evaluator, separate from the shared VM dispatch.
It covered 256 length tuples with IDs, ratios, priorities and masks each taking lengths 0, 1, 2 or 4.
All 252 mismatched tuples rejected, and the four exactly aligned tuples did not trigger rejection.
The expected result was calculated independently as any data-array length differing from the ID-array length.

The diagnostic pinned the then-current HEAD to `888e5045359e16e2a8616de3ed8ba576f2dbbe2d` before reading its original exact-trigger source.
That original source retained the audit baseline SHA-256 `07c7b7291b749ea7920b6c1d8a79ef119fd09a091c2f5791078497ccd4a028f9`.
Flattening only the new explicit AND child in the in-memory repaired AST produced exact equality with that original parsed file.
The rest of the producer and arithmetic implementation was therefore preserved in this comparison.
No source file or test file was modified by the diagnostic.

| Independently executed recheck | Result and scope |
| --- | --- |
| Existing exact quotation suite | PASS, 434 quotation and 56 quantizer cases, plus its eight Boolean truth-table checks and asserted 84 malformed-registry gate cases. |
| Separate source-VM Boolean/rejection diagnostic | PASS, eight NOT/NOR versus explicit NOT/AND truth-table checks and 28 malformed states across three frontends, with all 84 quotes invalid and shared quoted affordability rejecting. |
| Separate production-guard evaluator | PASS, 252 mismatched length tuples rejected and four aligned controls accepted. |
| RSA purchase suite | PASS, 295 existing source-model checks under corrected NOT semantics. |
| RSA support-request suite | PASS, its 295 bundle checks and 30 request checks under corrected NOT semantics. |
| Nine outer caller scenarios | PASS, with preservation reads pinned to immutable `f32aaa4b7acc3621fcb5375743b63bfc7a81f739`. |

The 28 malformed states include all 26 unequal short/equal/long combinations across ratios, priorities and masks, plus a short and long ID array.
Each was independently exercised through `universal_cost_quote_exact`, `universal_cost_quote_integer` and `black_friday_quote_custom_cost`, followed by `universal_cost_check_quote_affordable`.
The bare producer/effect return convention and false Black Friday bridge return were checked separately from the validity output and affordability rejection.
No rejection was accepted merely because a fixture threw an absent-element exception.

The repaired exact-trigger SHA-256 was independently measured before and after this completed recheck as `9f5831663708c2b25d2a25ec27b2c047cbeb4fbb52ecb15c772d6fcc62110101`, matching the parent-supplied completed-run identity.
Reviewed test-file fingerprints were exact suite `04e6b414a64fa9f59bc4cfce550850ac13365f44cf2ec45a12ad3c32b96f765f`, RSA purchase model `b5c7d86587388b53f0dc37e924ff0b621be059241e38c4fc4a59ee2b8a6945d7`, RSA support model `30ab76bf5456175e0aa194c96518f3bb9e517e8eba432a1f958e6bb215103426`, and outer caller suite `73da5f9332fecb8d09aed1ba618b3292162b72f6f34f930b7993577116fb48d0`.
The source/model/hash agreement closes EC-A01 as a concrete bounded source defect.

This remains source-semantic evidence, not native Boolean execution, native arithmetic, UI, save/reload, multiplayer or full event completion.
No new event-chain or weighted surface was added to this source-only recheck, and no broad MCP wait or new MCP acceptance was attempted.
All previously recorded MCP and native/runtime limitations remain open.
At the EC-A01-only recheck, EC-A02 remained open because its architect-owned public receipt/family/payment guards and actual record-to-credit regression evidence were explicitly not ready and were not reviewed then.
The subsequently authorized EC-A02 recheck follows.

## Bounded EC-A02 strict API and external forwarding recheck, 2026-10-03

Authority: the parent supplied `2026-10-03_achievement_receipt_proof_repair.md` and requested independent review of the actual public negative fixtures, typed family/primary/group claims, pending confirmation, preserved native/delayed contracts and unknown metadata state.
The parent then supplied the completed three external forwarding boundaries, their file identities and the 34-case extension, authorizing their bounded recheck.
The architect handoff was read completely, including its updated external-coverage appendix.
The uncommitted unrelated imports/deaths in the Germany file remain outside this audit and outside any commit recommendation.

### Original defect closure and validation

The new `black_friday_validate_ordinary_receipt_proof` requires an indexed receipt, a valid linked chain, source 26 on the transaction and all components, the appropriate recorded/settled state, zero refunded total and no refunded component, matching owner-recorded family, internally consistent totals and exact positive primary/component-group claim equality.
The public record invokes that proof before appending progress or family credit.
Immediate ordinary credit requires settled state 4.
Pending registration requires recorded state 1, stores the validated normal ordinary/paid claims, and gives no early family credit.
Confirmation revalidates the stored claims against the settled receipt before changing pending state or crediting the family.
The PP-only exception additionally requires the explicit PP component basis and no positive non-PP payment.
The logical family is read from explicit role metadata and never reconstructed from PP resource kind or from the old primary flag.

The five regular metadata columns and two pending-claim columns lazily resize to canonical row counts and preserve existing prefixes.
The metadata tuple is snapshotted and consumed at each real record call, so a later component cannot inherit it accidentally.
Missing/conflicting continuation metadata disables new achievement proof without changing payment, receipt, settlement or actual-paid refund accounting.
Legacy untyped receipts and pending claims retain their exact state and existing earned progress while unknown metadata blocks new proof.
This is a disclosed compatibility/proof limit, not a state reset and not an implemented retrospective migration.

| Independently executed check | Result and useful limit |
| --- | --- |
| Original architect public suite at the initially supplied snapshot | PASS, 31 actual public record/confirm/family-credit cases. |
| Parent-extended public suite at the final inspected snapshot | PASS, 34 cases, 739 real helper returns, 1,942 discarded helper-local temporary entries. Its three external fragments execute real record/settlement/public-credit continuations. |
| Additional independent in-memory scenarios | PASS, 12 cases validating actual family progress and flags as well as credit calls, rather than only scanner success. |
| Shared actual receipt suite with typed fixtures | PASS, 45 scenarios; captured/final BF source identical. Native resource operations remain modeled. |
| Existing scoped caller declaration audit | PASS, 743 known boundaries, zero missing consumed-output declarations. This is a storage inventory, not preservation of every prior effect. |
| Immutable before/after helper comparisons | Eight named native/delayed/credit helpers or predicates retain exact parsed source equality against `6ce9a5a81abd0966417fad68645c01ecbf83f6b3`. |
| Parent-authorized preservation reconciliation | PASS, 11 scenarios; normalized comparison of 84 BF, 21 core and 11 RSA pre-existing functions, three metadata-helper purity checks, negative mutation controls and the embedded current 34-case proof suite. |

The public cases reject fully refunded, partially refunded, wrong transaction/component source, claimed paid 5 versus stored 1, mismatched ordinary values, zero recorded ordinary/payment and unsettled immediate credit.
They also reject wrong family/primary, missing/conflicting metadata, refunded components, tampered totals and whole-bundle claims substituted for the tagged primary subtotal.
Primary-component and primary-group positives are exercised separately.
One successful multi-resource action credits only its explicit logical family, with secondary payments contributing non-PP evidence only when actually positive.

The 12 independent cases additionally verify:

- PP-only resource payment does not infer either an institutional or material family.
- Explicit law-family metadata paid in PP can establish an institutional family without claiming a non-PP payment.
- A secondary component recorded before the selected primary still credits the correct primary amount/family.
- Consumed metadata followed by an untyped continuation leaves the receipt usable while blocking achievement proof.
- Nonzero refunded total rejects even if the transaction state was tampered to settled.
- A component quote/paid mismatch rejects even when aggregate paid total is adjusted to match.
- Tampered pending claim values reject confirmation and leave the pending state intact.
- A group with no included primary members cannot credit the whole bundle.
- Group basis with a nonzero named primary, or unknown basis 3, cannot credit.
- A new ordinary public claim after expiry cannot credit.
- A zero-paid non-PP secondary does not become positive non-PP evidence or invalidate a genuinely PP-only payment.

All extra scenarios use the checked-in public test's existing native fixture model and actual core/public helper definitions loaded in memory.
No production record, scanner, lookup, confirmation or family-credit body is mocked or rewritten.
No scratch test file was written.
Actual native resource mutation, native country classification, serialization, timing and final engine delivery remain modeled or unobserved.

### Reviewed forwarding boundaries

The observed owned declaration count is 22 direct record boundaries in `026_black_friday_effects.txt` plus one RSA loop boundary, 23 total.
All four explicit role inputs are forwarded before each shared record, including the primary-membership condition where required.
The bounded external extension adds three known record boundaries:

| External helper | Reviewed role and observed result |
| --- | --- |
| `random_faction_black_friday_pay_component_list` | Registry-selected family and primary component, component basis and exact member test; the actual record/public-credit fragment credits the designated CP primary and preserves secondary receipt data. |
| `random_faction_black_friday_pay_request_liaison_component` | Requester component 1701 is the CP primary; leader component 1702 is a separate secondary-only receipt. ROOT's public claim credits once, and neither an equipment claim nor a CP claim from the leader's secondary-only receipt credits another family. |
| `mengele_clone_army_black_friday_pay_command_power` | Explicit CP family, exact CP component and component basis; the actual successful record/settle/public-credit continuation credits once and repeat claim does not credit again. |

The named external definitions and their exact forwarding statements were inspected directly.
The suite deliberately extracts these bounded definitions/fragments and does not parse or certify unrelated Germany clone-unit strings, imports, deaths or other ownership changes.
This closes missing metadata at these three record boundaries, not complete Event 17/Germany gameplay, AI or whole-file preservation coverage.

### Preservation and limits

Exact parsed equality against commit `6ce9a5a81abd0966417fad68645c01ecbf83f6b3` was verified for `black_friday_credit_native_japan_cbrn_raid_family`, `black_friday_credit_achievement_family`, `black_friday_add_committed_achievement_family`, `black_friday_remove_committed_achievement_family`, `black_friday_settle_cbrn_external_aid_pp_fee_receipt`, `black_friday_achievement_can_credit_native_japan_raid`, `black_friday_achievement_is_valid_sale` and `black_friday_achievement_possible_campaign_is_valid`.
The actual native Japan bridge case still reaches the real family-credit body after expiry without a synthetic shared receipt.
The accepted delayed PP-only public case also credits after expiry, while ordinary pending confirmation remains gated by the active sale.
These are preserved source contracts, not observed native callbacks or live delivery.

The old nine caller-preservation snapshot is historical for this proof rewrite.
Its old hardcoded lookup-location count initially failed because the authorized validator/confirmation structure changed, as the architect handoff disclosed.
The parent subsequently authorized a current preservation reconciliation in the same test path, and this auditor read the full 300-line script and ran it independently.
The revised suite passes 11 scenarios and compares against immutable pre-proof commit `e64e95aa3bcb9fcab5a38a248cad28aa78bd2294`, retaining `f32aaa4b7acc3621fcb5375743b63bfc7a81f739` only for the earlier caller-frame/trigger comparison.

Normalization removes only the four exact role-input temporary fields, four exact record snapshot fields, metadata-only IFs without an ELSE/ELSE_IF continuation, and calls to the three individually verified metadata helpers.
It retains every other original function and compares its normalized AST without skipping whole cost files.
The observed comparison covers 84 BF functions, 21 neutral-core functions and 11 RSA functions.
The four explicit proof-semantic exceptions are the public record, ordinary scanner, PP-only scanner and pending confirmation; the same test invokes all 34 actual public cases and requires their source hashes to match the preservation snapshot.

The two schema-preparation helpers must match their exact resize-only shapes.
The binding helper may write only the seven declared normal metadata columns and its one local metadata-valid temporary, with read-only condition structure.
Negative controls verify that payment and flag changes remain in the normalized structure, a mixed metadata/gameplay IF remains intact, and a binding helper that writes `universal_cost_transaction_total_paid_costs` is rejected.
The source also rejects unexpected added/removed helpers and duplicate helper IDs.
These are meaningful preservation checks, not replacement of the missing comparison with the 743-boundary declaration scan.

The preservation script SHA-256 is `53b3aafd3d0a5125f5d7b23225d31e4d929ceec7bb303525a0b9aea7151ddeb7`.
Its pre-proof decoded-source identities are BF `db17dc9f13c6e8419151aeccb558c33eb660ee2de0a2656878f143c7997511fa`, core `a78805dcdbbeea5e6f3517fe86a86f817ba78631d56ce02cfcb5f7dd1bf40c56` and RSA `5df2cab6b5a0e628c096db4fbda1443fd011863135d85c7aa091d230dc531fee`.
The successful execution returned the current proof/core/RSA hashes listed below and the matching 34-case public evidence.
The comparison is source-semantic and does not establish native execution or preservation of unrelated external-file work.

The native-raids skill was applied only to the preserved exception boundary.
Installed raid documentation at `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\raids\_documentation.md` documents native CP allocation at line 31, creation-time essential-equipment collection at lines 167-173 and raid-instance outcome dispatch at lines 246-264.
Installed effect documentation lines 6397-6410 was read for normal-array resizing, and offline Data structures lines 435-442 was reread for temporary lifetime and regular-state persistence.
No raid definition, native callback package, cost or refund rule was changed or independently certified as engine-executed.
The earlier MCP/event/probability/native acceptance limits remain unchanged, with no broad MCP retry in this source recheck.

### EC-A02-F01: declared consumer-goods family absent from public admission

Current disposition: implemented and independently verified for this exact public admission defect.
The following diagnostic describes the pre-fix BF source `02f16b293e6aa4c33d85d4b123a12126343b5547d7393dd07ad451a7f98b53fc`.
The parent-owned repair and its completed narrow recheck follow.

The strict validator's family whitelist at `common/scripted_effects/026_black_friday_effects.txt:88-113` omits `constant:universal_cost_family.consumer_goods`.
The enum declares this family as 65536 at `common/script_constants/chaosx_universal_cost_constants.txt:116`.
The unchanged material-family flag and final-family conditions still explicitly admit it at BF effect lines 339 and 376, and Part 4 includes voluntarily committed consumer-goods burdens.

A read-only typed-receipt diagnostic supplied source 26, settled state 4, family 65536, positive ordinary 10 and paid 5, valid component/chain totals and explicit primary component/member metadata.
The public record appended no achievement row and called no family credit.
Identical political-power, factory-commitment and state-project controls each appended and credited once.
The result was reproduced both with a PP component and with an owner-adapter component kind 100.

Original disposition: unresolved public family-admission/coverage gap, separately reported immediately to the parent and subsequently repaired as documented below.
It is a false-negative admission limit and does not reopen the verified original false-positive receipt-integrity defect for the reviewed families.
No current implemented consumer-goods transaction owner, native payment consumer or live regression was established by this synthetic API fixture, and no complete universal-family coverage is claimed.
The parent chose to restore the declared admission and add its typed public positive and unknown-family negative cases, with no exclusion design.
The full general registry/native-family gates remain open.

### Narrow EC-A02-F01 recheck, 2026-10-03

Authority and acceptance basis: the parent explicitly implemented the declared `consumer_goods = 65536` whitelist entry, rejected an exclusion design, supplied the two additional public scenarios and requested independent F01-only review plus the existing bounded preservation suite.
This recheck admits only this documented logical family and does not infer any native consumer-goods surface, payment adapter or completed canonical-family registry.

The source whitelist now contains `constant:universal_cost_family.consumer_goods` alongside the already accepted material-family conditions.
A read-only exact text comparison removed only that one new whitelist statement in memory and recovered the prior BF whole-file SHA-256 `02f16b293e6aa4c33d85d4b123a12126343b5547d7393dd07ad451a7f98b53fc`.
The current whole-file SHA-256 is `46c879e9627859104501ba84862daa80df1be3e46f5c1d9d757be1fc9514cec3`.
There is no other production change in that comparison.

The updated public suite passes all 36 cases independently, with 793 actual helper returns and 2,078 discarded helper-local temporary entries.
Its new positive scenario uses family 65536, source 26, settled state 4, explicit primary/member metadata, ordinary 10 and paid 5 for both native-resource kind 1 and owner-adapter kind 100.
Both real public calls credit exactly logical family 65536.
The new unknown combined logical-family 4097 case credits none despite a positive typed settled receipt.

A separate in-memory diagnostic confirmed actual regular family count one and the sole family row 65536 for each resource-kind positive.
The material-family flag is set, no institutional family is inferred, and repeat public claims do not credit again.
The unknown-family control appends no achievement row and leaves family count zero.
These diagnostics execute the actual shared record, settlement, public record and family-credit bodies under the existing modeled native fixture contract.
They do not execute a native consumer-goods payment.

The current preservation suite independently passes all 11 scenarios and invokes the matching 36-case public suite.
It retains the immutable pre-proof baseline `e64e95aa3bcb9fcab5a38a248cad28aa78bd2294`, compares 84 BF, 21 core and 11 RSA existing functions, verifies the same three metadata helpers' purity, and retains its payment/flag/mixed-control and impure-paid-total negative controls.
The scope and normalization rules recorded in the earlier preservation recheck are unchanged.
The current core/RSA hashes remain `d2d04617d66ccb6dbd240e82cca8b1fabde24a2fec7fadc9bfa54c6de768d7f8` and `fc2b62492eedc337810a3844bc3d7b27725093443a2425b2ac11ef8946b617f0`.

The reviewed public-suite SHA-256 is `f6f746f91735ccc49146c963075599224072f30b36664828abc89d7fb7bd6d7a`.
The reviewed preservation-suite SHA-256 is `cdad3e219baf97ec82179e06fcbb682ebc335d5728173a3ac3977dd7a17bc94f`.
These identities were checked before and after the completed runs without a concurrent source/test change observed.
Earlier 31/34-case counts and hashes remain historical evidence for their exact snapshots.

EC-A02-F01 is closed for the bounded source admission defect after this independent patch/test review.
All future canonical logical-family IDs, the general owner registry, native consumer-goods surfaces/payments, engine achievement delivery, UI, save/reload, multiplayer and existing MCP limitations remain unverified or incomplete under their prior dispositions.
No source, test, result JSON, asset, workbook, index or commit was changed by this auditor.
Only this audit report was updated.

### EC-A02 recheck identities

| Reviewed source/test | SHA-256 |
| --- | --- |
| BF effects | `02f16b293e6aa4c33d85d4b123a12126343b5547d7393dd07ad451a7f98b53fc` |
| Neutral cost/receipt effects | `d2d04617d66ccb6dbd240e82cca8b1fabde24a2fec7fadc9bfa54c6de768d7f8` |
| RSA purchase effects | `fc2b62492eedc337810a3844bc3d7b27725093443a2425b2ac11ef8946b617f0` |
| Universal constants | `97e0fd75044b15ab1735d935abc8648060ff20e7e977abc1d942cece43d10fb9` |
| Random Faction effects, only named boundaries reviewed | `09e82c482598cd5336a3407d32e4a270bc1aeed766ae06322de45ecbde6075a4` |
| Germany Mengele effects, including unrelated unreviewed work | `783659c4fc394a007570210acd2d18fe7faad39249faa07f71b2832bb52536ae` |
| Final 34-case public suite | `17a8255ec846fe8e8204252ce3524be6951b2601c5b0cadd03d2bc17ee34c1aa` |

The final 34-case execution returned matching captured/final external source hashes and the three supplied proof/core/RSA identities.
The earlier 31-case handoff fingerprint was an earlier test snapshot, not the current extended-suite identity.
The public suite and stored result artifact both report 34 cases, 739 helper returns and 1,942 discarded helper-local temporaries.
No production, test, result JSON, asset, workbook, index or commit was changed by this auditor.
Only this completion audit was updated.

## Original meaningful verification performed

| Executed existing source suite | Observed result | What it establishes |
| --- | --- | --- |
| `subagent_handoffs/exact_quote_source_tests.js` | PASS, 434 quote and 56 quantizer scenarios | Actual helper bodies against the rational oracle under the checked-in interpreter. Its NOT semantics limit the malformed-registry claim as described in EC-A01. |
| `subagent_handoffs/universal_cost_receipt_lifetime_source_tests.js` | PASS, 45 scenarios | Actual shared APIs, two actual BF scanners, conservative helper lifetime and twenty-nine native debit/credit pairs with native operations modeled. It is not public achievement-to-credit proof. |
| `subagent_handoffs/black_friday_outer_caller_source_tests.js` | PASS, 9 scenarios | Bounded real caller storage/preservation and protection quotation behavior. |
| `subagent_handoffs/black_friday_outer_caller_contract_audit.js` | PASS, 739 boundaries, zero gaps | 427 effect, 227 trigger and 85 localisation calls in its known definition graph. |
| `verification/rsa_purchase_source_tests.mjs` | PASS, 295 cases | Five actions, eleven components, three price tiers and source text/failure/pending-state checks with shared/native contracts mocked. |
| `verification/rsa_support_request_source_tests.mjs` | PASS, 295 bundle cases plus 30 request cases | Explicit request scopes, duplicate exclusion, cap, refusal, cleanup and original reward/AI preservation with native dispatch/transfer and polity queries mocked. |
| In-memory NOR diagnostic | Six malformed alignment combinations accepted | Concrete EC-A01 reproduction with source unchanged. |
| In-memory public achievement diagnostic | Six ineligible receipt fixtures reached committed family credit | Concrete EC-A02 reproduction, with a valid-sale assumption and final credit observed as a call only. |

An initial parallel Node run encountered Windows/V8 startup out-of-memory failures for two suites and a nonzero exact-suite launch.
Sequential reruns completed successfully.
Those process failures are recorded as execution limits, not gameplay assertion failures.
The listed PASS results do not erase the separately reproduced semantic defects.

## MCP and reference limits

The current callable catalog exposes `hoi4.reference_context`, `reference_search`, `reference_read`, `source_lookup`, `event_inspect`, `event_render`, `event_compare`, and probability routes.
No HOI4 health/version or script-validation route was exposed, and no unverified helper-expansion, job or native-task route was used.
Exposure did not establish service health.

This auditor observed no result within 20,000 ms for an event reference context with limit 2, then the narrower installed-document `all_of_scopes` search with limit 1.
No cited id/revision was returned to enable a revision-bound reference read.
Local references were read directly instead.
An initial incomplete event selector returned `MCP error -32602`, requiring `selector.kind`.
Corrected trace requests used `{ kind: "event", eventId: "chaosx.nr26.1" }` and `{ kind: "event", eventId: "chaosx.nr12.1202" }`, depth 1, one node and one edge.
Both returned no result in the 20,000 ms observation windows.
One-node scope renders of both selectors also returned no result in those windows.
A bounded Event 26 compare with the recorded historical revision `9a7c9c23f5d02569f7457fa868eaecdea03c47f77dc3652d62c24492f5e65755` likewise returned no result.
That historical revision is a comparison input, not proof of a matching frozen baseline.
The RSA event comparison remains missing with no returned graph/revision or comparison artifact.
No result, artifact URI, continuation, current graph revision or engine-flow coverage was claimed for these observations.
They are observation-window failures, distinct from the parent's separately reported completed `timed out awaiting tools/call after 600s` result.
The parent's later instruction to finalize promptly ended further route waits.

The weighted sidecar was routed to `chaosx_ai_probability_auditor` with no inherited context, exact source paths and read-only/no-write scope.
The existing `2026-10-03_rsa_probability_audit.md` remains incomplete and explicitly lacks analysis, evaluation, sweep, comparison and render artifacts.
Its five-purchase pool cannot establish complete decision normalization without the unpaid lease candidate and expanded target instances.
The immutable decision baseline and event baseline are named under `docs/testing/2026-10-03_event26_rsa_before/`.
The new sidecar was instructed to finalize without further lengthy MCP attempts.
No source-only willingness score or arithmetic test is promoted to probability or engine evidence.

The specialist returned its final inline evidence before this report was handed off.
Its `decision_ai_will_do` inspect used the five purchase IDs and `{ path: "common/decisions/012_africa_rsa_decisions.txt" }`, with `refresh = true`.
Its `event_option_ai_chance` inspect used both `chaosx.nr12.1202.a` and `.b` and `{ path: "events/012_africa_rsa.txt" }`, also refreshed.
Each initial call and its one narrower retry without `candidatePool` returned no payload during a 20-second observation window.
The specialist received no artifact URI, revision, scenario hash, server error body or comparison ID, and did not claim evaluate, sweep, compare or render completion.

The six purchase scenario descriptions are `ordinary_funded`, `baseline_sale_funded`, `evolution_sale_funded`, `each_component_below_payable`, `invalid_target_or_route` and `pending_receipt`.
The reply descriptions are `reply_valid`, `pending_duplicate`, `cap_reached` and `crisis_ended`.
These descriptions are not accepted complete MCP fixtures.
Resource, route, actor/target, date, source state and strategy inputs remain unbound for purchases, and donor/coalition, opinion, flags, support count, timing and callback inputs remain unbound for replies.
The reply's two-option local pool is complete, while the decision category pool is not complete in this bounded slice.

The specialist verified the tracked physical decision baseline at SHA-256 `40283784e0d0ea091bd96c96c46f0155ec01e911091b2b20a0389ac5e1d696cc`.
The event baseline at `f0776f45258613e443ba09ebc1608fdc560ce6c904bf2e574dd3509cd585b1ef` and target-trigger baseline at `54eb5fc822dffad685ab73ff6b7c820efb4366750e6a26e867115006475f31cc` were physically present but untracked at its check.
Purchase-effect, support-request-effect and purchase-trigger before snapshots were absent.
These are baseline durability/coverage observations, not a claim that an untracked physical file is unusable as an MCP source.
No new unintended eligibility-source regression was found, and no normalized probability, rank reversal, starvation, repetition or timing result was established.
The five ordinary PP AI hints remain conservative source literals, not sale-sensitive AI proof.
The specialist changed no source and wrote no report.

Direct local sections read for this audit include offline Triggers lines 337-345, Data structures lines 435-449 and 1069-1089, installed trigger documentation `all_of_scopes` lines 1052-1064, `resize_temp_array` lines 7414-7427 and `set_temp_variable` lines 7482-7501.
The installed scripted-effect precedent at lines 498-520 performs temporary arithmetic in `all_of_scopes` inside an effect limit.
Installed decision documentation lines 1-46 establishes country/target evaluation scopes and cadence.

| Reference source | SHA-256 |
| --- | --- |
| `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md` | `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06` |
| `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md` | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\scripted_effects\00_scripted_effects.txt` | `93ddd0d2e9f7a1a5640cfdafbae6b9ff0e1b4ee57e829c81d13b0cac23ad90bf` |

These are actual local file identities and section reads, not fabricated MCP citations.

## Source fingerprints

| Audited baseline source | SHA-256 |
| --- | --- |
| `common/scripted_effects/chaosx_universal_cost_effects.txt` | `a0fe5277e7251fc5ee8164f71128f0b836ce6be39dc93d06562620d27b0a633c` |
| `common/scripted_triggers/chaosx_universal_cost_exact_triggers.txt` | `07c7b7291b749ea7920b6c1d8a79ef119fd09a091c2f5791078497ccd4a028f9` |
| `common/scripted_triggers/chaosx_universal_cost_triggers.txt` | `3a10f0dfb8a4d99fa4f05d73f6e691ae333441a6674dff69c14cb966fce5a48c` |
| `common/scripted_effects/026_black_friday_effects.txt` | `62398cd3d6bd431b54d36190f497913a3ebe44c8be02d0abc06f2e3806fd727b` |
| `common/scripted_triggers/026_black_friday_triggers.txt` | `53783b7a3d8b125eb1c24bef6f59cdfd6b5265b89a0f6cfc67e45948afb43d5b` |
| `common/scripted_effects/012_africa_rsa_purchase_effects.txt` | `5df2cab6b5a0e628c096db4fbda1443fd011863135d85c7aa091d230dc531fee` |
| `common/scripted_effects/012_africa_rsa_support_request_effects.txt` | `206c1aabd0c2bcc908c939e2827018223ef1ef3987241d486961a75ea85d1d92` |
| `common/scripted_triggers/012_africa_rsa_purchase_triggers.txt` | `ec3c1adf78c811f6729b63ce4b0544d1db00d04fe90f59e34f1f80a001431653` |
| `common/scripted_triggers/012_africa_rsa_triggers.txt` | `eef3da47d63377910dd2a9feef4f17fc9a139692a67dff71ca66d88bf56b14bf` |
| `common/decisions/012_africa_rsa_decisions.txt` | `0f5cfc6369be6a42c5c0705c318352b9c70951dfdc7c6244be9172dd1d15f884` |
| `events/012_africa_rsa.txt` | `89d5165760c2b0505d50265be01720fba546bd6f62c45d7082323caf58ce325e` |
| `common/scripted_localisation/012_africa_rsa_purchase_localisation.txt` | `4245fe74cf31a6442b536c03ba821c6e4aa95f73a7aa575d816ebeaf57ff3f20` |
| `localisation/english/012_africa_rsa_l_english.yml` | `dbe357d5f22b510ff80c8e4acdae7fc604b0e3874d70dfd33616898f167ec95e` |

## Assets, catalog and remaining gates

The five unchanged DDS files retain the hashes recorded in `event26_asset_audit.md`: report `9430a02a...e102`, idea `375eca0d...a434`, completed achievement `507bc29d...d57c`, grey `be8eacee...2f70`, and not-eligible `a7a29a4a...4596`.
The complete identities are in that audit and were compared with freshly read SHA-256 values here.
No visual asset, portrait, animation, unit/model sound package, bespoke counter or dedicated event GUI was introduced by this tranche.
The existing asset record remains relevant without inferring a new worker or asset requirement.
Native popup/texture acceptance is still open.

The parent/readonly catalog worker's single ID 26 row and exact premise/evolution mirror are retained as supplied evidence.
No workbook change was requested or performed, so no exporter was run.
The active event asset workspace remains retained because the overall goal is incomplete.

The remaining all-owner semantic registry, fourteen native factor groups, exact strategy-D inaccessibility evidence, other production caller integrations, MCP event/probability artifacts, native consumer arithmetic/performance, live UI/debit agreement, save/reload and multiplayer acceptance gates remain open.
They were not expanded or certified by this bounded audit.

Recommended next actions are explicit disposition of exceptional RSA settlement recovery, reconciliation of stale neutral-document summaries, completion of the broader canonical-family/owner registry under its own scope, and preservation of every already-disclosed broad/runtime gate.
Retain the closed EC-A02 bounded strict-proof and three external forwarding results without promoting them to full family, owner, native or whole-achievement acceptance.
Retain the independently verified EC-A01 repair evidence and reconcile its exact source fingerprint when publishing the scoped repair commit.
Existing passing suites should be rerun after the corrections together with rejection cases that cover the actual public proof boundaries.

Skills used: chaos-redux-events, chaos-redux-subagents, chaos-redux-improvement-loop, chaos-redux-event-planning, chaos-redux-event-assets, chaos-redux-decisions-missions and chaos-redux-native-raids for the preserved native exception.
No skill was created or updated.
