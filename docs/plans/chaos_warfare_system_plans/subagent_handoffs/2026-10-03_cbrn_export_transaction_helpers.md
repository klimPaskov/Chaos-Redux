# CBRN export transaction helpers

Disposition: implemented as bounded helper source, with parent integration and native acceptance pending.
Acceptance basis: the parent records user approval of CBRN/Event 026 implementation, canonical fee adaptation, exact real model reservation/refund, retained native factory/timer/cooldown behavior, and no weaker delivery contract.
The parent assigned only the three new helper files and this handoff.
Existing decisions, gates, callbacks, English localisation, accepted documentation, test artifacts, MCP evidence, staging, and commits remain parent-owned.
No game launch, log search, new event, periodic hook, world iterator, UI, equipment definition, grant, or shared API mutation was performed.

## Changed files and integration state

- `common/scripted_effects/cbrn_export_transaction_effects.txt` implements donor-owned model reserve/release/send/refund, fee receipts, start/finish/cancel, and preserved success outcomes.
- `common/scripted_triggers/cbrn_export_transaction_triggers.txt` implements canonical fee and stock readers, preflight, pre-click factory eligibility, owned-receipt validation, and continuity.
- `common/scripted_localisation/cbrn_export_transaction_localisation.txt` declares `GetCbrnExportPoliticalCost` with frozen, blocked, and fresh quote text branches.
- This handoff documents all helpers and the pending call sites.

The helpers have internal call sites, but the existing public decision callbacks still require parent wiring.
They are owner adapters rather than new neutral APIs in `chaosx_dynamic_effects.txt`.
The existing dynamic registry and its markdown were read and left unchanged under the explicit ownership boundary.
The parent should link this owner document from accepted CBRN documentation or its owner index when integrating.
No completed export integration or complete native delivery proof is claimed.

## Scope and caller temporary contract

Every public entry uses COUNTRY THIS equal to COUNTRY ROOT donor, and COUNTRY FROM recipient.
Call the entry directly in the donor's native targeted decision callback.
Do not enter recipient scope around an entry, replace ROOT, or use a STATE FROM.
Recipient country existence is checked through the existing `cbrn_target_can_receive_exported_masks` predicate, without relying on `scope_exists` on a numeric pointer.

The outer caller must declare every temporary output that it reads before calling a helper.
Public entry outputs are `cbrn_export_started`, `cbrn_export_completed`, and `cbrn_export_cancelled`, with zero meaning no completed operation and one meaning the named operation completed.
An export completion result of one means exact measured physical delivery was proved and original outcomes were applied.
It does not independently establish achievement acceptance, because the shared achievement API has no success output consumed by this adapter.
Persistent recovery flags and settlement results remain authoritative for unresolved fee closure.

Fee reader outputs are `cbrn_export_fee`, `cbrn_export_fee_valid`, `cbrn_export_fee_source`, and `cbrn_export_fee_affordable`.
Stock reader output is `cbrn_export_available`.
Held reader output is `cbrn_export_held_total`.
Internal reserve input/output `cbrn_export_remaining` and internal equipment token input `cbrn_export_model` are caller-created before nested calls.
Every nested component quote, allocator, payment/record adapter, and settlement output actually consumed after return is initialized by its enclosing owner caller.
The component payment/refund adapters remain the committed immediate-response dependency, not a copied cost engine.

Example selection callback:

```txt
set_temp_variable = { cbrn_export_started = constant:universal_cost_framework.zero }
cbrn_export_transaction_start = yes
```

Example native completion and cancellation callbacks:

```txt
set_temp_variable = { cbrn_export_completed = constant:universal_cost_framework.zero }
cbrn_export_transaction_finish = yes
# In cancel_effect instead:
set_temp_variable = { cbrn_export_cancelled = constant:universal_cost_framework.zero }
cbrn_export_transaction_cancel = yes
```

## Helper map

| Name | Scope and inputs | Outputs and defaults | Side effects and call sites |
| --- | --- | --- | --- |
| `cbrn_export_transaction_quote_fee` | Donor, ordinary fee from existing constant | Four fee outputs, normal fee without active sale, invalid while sale source proof is missing | Temporary quote only, called by preflight and getter |
| `cbrn_export_transaction_quote_stock` | Donor concrete stock | Five-model sum, missing reader values treated as zero by normal script semantics | Temporary read only, called by preflight |
| `cbrn_export_transaction_quote_held` | Donor, recipient-targeted fields | Five held counts summed, unset fields zero | Temporary read only, called by continuity/refund/finish/ownership cleanup |
| `cbrn_export_transaction_preflight` | Donor with recipient FROM | Predicate, retains original donor 1500 floor and target context, canonical affordability and actual 500 preflight | No debit, used by selection callback, deliberately omits already committed factory |
| `cbrn_export_transaction_can_start` | Same | Predicate, adds original native one free factory | Pre-click only, parent available/custom-cost start gates |
| `cbrn_export_transaction_has_any_owned_receipt` | Donor actor only, no FROM required | Predicate, donor owned-receipts count greater than zero, missing count defaults zero | Read only, parent native `target_root_trigger` continuity before target iteration |
| `cbrn_export_transaction_has_owned_receipt` | Donor and FROM | Predicate, owned flag and stored recipient equality | Read only, local owner continuity/cleanup/getter |
| `cbrn_export_transaction_can_continue` | Same with accepted active row | Predicate, exact nonnegative held 500 and paid receipt identity | Read only, retains donor/recipient context, omits unreserved 1500 floor, live sale and free factory requirement |
| `cbrn_export_transaction_start` | Donor and FROM | `cbrn_export_started`, zero on rejection/failure | Reserves five real models oldest-first, records PP-only receipt, freezes fee/source/sale identity, publishes active only after exact reservation and recorded payment |
| `cbrn_export_transaction_finish` | Donor and FROM owning row | `cbrn_export_completed`, zero without complete proof | Revalidates continuity, measures model transfers, applies original outcomes once only for exact 500, closes/ confirms fee, otherwise cancels/refunds |
| `cbrn_export_transaction_cancel` | Donor and matching FROM row, recipient may be invalid | `cbrn_export_cancelled`, zero while recovery remains | Refunds only held models, closes accepted service fee without success credit, repairs pre-acceptance failed fee through shared exact refund API |
| `cbrn_export_transaction_reserve_model` | Internal donor, `cbrn_export_model` existing equipment token and caller `_remaining` | Decreases remaining only by bounded actual native debit | Writes one donor-recipient model row, five calls from start, initializes model diagnostics for the selected row |
| `cbrn_export_transaction_refund_model` | Internal donor, model token | Reduces held only by bounded measured native gain | Real return from matching held row, called by refund wrapper, zero held is no-op |
| `cbrn_export_transaction_refund_held` | Internal donor and FROM | Persistent remaining/recovery evidence | Five bounded concrete refund calls, called by cancellation |
| `cbrn_export_transaction_send_model` | Internal donor, model token and matching held row | Paired actual debit/gain, model delivered amount, unsent released amount | Releases held quantity, requires exact release before native send, stops subsequent sends after partial/mismatched transfer |
| `cbrn_export_transaction_close_fee` | Internal donor, positive receipt | Persistent settlement result and closed flag | Settles accepted fee once, cancellation does not create ordinary PP refund |
| `cbrn_export_transaction_confirm_fee` | Internal donor with exact delivery and closed fee | Shared achievement row if its proof accepts, no independent result output | Explicit political-only post-expiry confirmation using frozen source/fee/sale and typed receipt |
| `cbrn_export_transaction_apply_success` | Internal donor with delivery-proven flag | Existing aid statistics/outcomes once | Receiver aid flag, maintenance and opinion, donor Condemnation compliance outcomes, unchanged existing package |
| `cbrn_export_transaction_publish_ownership` | Internal donor and target FROM | Donor `cbrn_export_owned_receipts_count`, initializes missing count zero | Increments only when first setting the target owned flag, including start-failure escrow, called by start |
| `cbrn_export_transaction_release_ownership` | Internal matching donor row | Clears active/owned/recovery only with zero held, closed fee and no mismatch | Decrements count only when releasing an existing owned flag, keeps receipt/diagnostic evidence after closure, called by finish/cancel |
| `GetCbrnExportPoliticalCost` | Donor and FROM | Frozen in-flight fee or canonical fresh fee | Temporary read and three parent-owned English keys, no payment |

All model primitives are internal and must not be called to credit stock without an owner row.
`meta_effect` injects only the existing equipment token into static native model fields and the matching model ledger name.
Recipient key targeting remains `@FROM`, with no double-target variable scheme or shared durable partner pointer.

## Tuning and receipt metadata

No constants were added or changed.
All policy values remain in `common/script_constants/cbrn_system_constants.txt`.
Normal service fee is `cbrn_protection_decision_cost.export_masks_pp` 15, with canonical whole-unit half and quarter quotes expected to be 8 and 4.
Shipment is `cbrn_protection_decision_cost.export_masks_crates` 500, never a discounted material component.
Start stock floor is the existing `cbrn_protection_ai.export_minimum_reserve` 1500.
Native factory commitment one, duration 14, and targeted re-enable 60 stay parent decision fields.
Arithmetic uses existing `cbrn_math.zero` and `cbrn_math.negation_multiplier`.

The receipt family is `universal_cost_family.political_power`, basis `universal_cost_achievement_basis.primary_component`, exact primary/component ID `universal_cost_resource_kind.political_power` 1, with that component marked a primary member.
These explicit typed inputs precede the reused `cbrn_pay_and_record_response_component` call.
Masks are escrowed property and never discounted or recorded as paid material components.
Frozen fee/source/receipt/sale fields survive sale expiry and are not rewritten by completion quotations.
Failed selection payment/recording returns its unused models and repairs only actual fee debits through `cbrn_refund_unfinished_response_transaction`.
After acceptance, the service fee is spent even on cancellation, matching the existing timed service policy.

## Persistent storage and cleanup

Donor fields keyed by recipient are `cbrn_export_recipient_@FROM`, `cbrn_export_fee_@FROM`, `cbrn_export_source_@FROM`, `cbrn_export_receipt_@FROM`, `cbrn_export_sale_sequence_@FROM`, `cbrn_export_delivered_total_@FROM`, and `cbrn_export_fee_settle_result_@FROM`.
Donor actor field `cbrn_export_owned_receipts_count` counts outstanding owned rows independently of FROM and is maintained only by guarded ownership publication and successful release.
It includes paid active rows, failed-start rows with retained physical or fee recovery, and delivered rows whose fee cannot yet close.
It is not cleared when a sale expires, native transfer fails, or cancellation leaves recovery pending.
Repeated publication or release of the same target cannot change the count twice.
The implementation mirrors `cbrn_occupation_register_external_aid_reservation` and `cbrn_occupation_close_external_aid_reservation` in `common/scripted_effects/cbrn_occupation_effects.txt:68-98`, including initialization of a missing count and a lower bound after genuine release.
No recount, forced recovery closure, or migration sweep was added.
For each of the five concrete model tokens, donor fields use `cbrn_export_held_<model>_@FROM`, `cbrn_export_reserved_debit_<model>_@FROM`, `cbrn_export_refund_gain_<model>_@FROM`, `cbrn_export_refunded_<model>_@FROM`, `cbrn_export_release_gain_<model>_@FROM`, `cbrn_export_sent_debit_<model>_@FROM`, `cbrn_export_received_gain_<model>_@FROM`, `cbrn_export_delivered_<model>_@FROM`, and `cbrn_export_unsent_released_<model>_@FROM`.
The five models are reconditioned, basic `_1`, improved `_2`, advanced `_3`, and sealed `_4`, in that reservation order.

Targeted donor flags are `cbrn_export_owned_@FROM`, `cbrn_export_active_@FROM`, `cbrn_export_start_failed_@FROM`, `cbrn_export_fee_closed_@FROM`, `cbrn_export_delivery_proven_@FROM`, `cbrn_export_outcomes_applied_@FROM`, `cbrn_export_transfer_failed_@FROM`, `cbrn_export_native_mismatch_@FROM`, and `cbrn_export_recovery_@FROM`.
Boolean state uses flags.
No global or regular event target is needed.
A single native callback FROM selects its own row, so two simultaneous recipients cannot overwrite one another.
No recipient array or world cleanup scan was introduced.

Remaining held counts are the only quantities eligible for a physical refund.
Released but unsent units already remain on the donor, and cancellation does not credit them again.
An accepted partial send retains its measured delivered/remaining split but earns no aid history, recipient aid flag/opinion, Condemnation credit, or purchase achievement.
Matched bounded partial stock credits decrement only the actual credit and keep the remainder for exact retry.
Negative, oversized, or donor-debit/recipient-gain-mismatched native deltas set a recovery flag and retain observations, with no guessed restoration or later automatic credit.
Fee cancellation may close its PP receipt while physical recovery remains blocked, without delivery achievement confirmation.
A closed row keeps diagnostics until the next valid selection for that recipient resets the model row.
Shared transaction arrays preserve historical fee evidence independently.

## Parent migration and presentation

The exact parent before fixture is `docs/testing/2026-10-03_cbrn_occupied_export_before/source_manifest.json`.
The reused immediate-response tranche is committed at `52ad81ab99d857be4fd1022db7c2adbb69e526bf`.

Replace the existing `cbrn_begin_protective_equipment_export` body with an initialized call to `cbrn_export_transaction_start`.
Replace the existing `cbrn_export_masks_to_protection_partner` body with an initialized call to `cbrn_export_transaction_finish` in native donor ROOT and recipient FROM.
Remove the completion callback's unnecessary shared `cbrn_protection_trade_partner` target if no other code still consumes it.
Use `cbrn_export_transaction_can_start` for fresh availability/custom cost and preserve donor visibility and target eligibility.
Add an owned active continuity branch to visibility/target enumeration so selection at 1500 remains visible after reserving 500 and unreserved stock falls to 1000.
The native `target_root_trigger` runs before target iteration, so use actor-only `cbrn_export_transaction_has_any_owned_receipt` there in an OR with the original actor start stock/factory qualification.
Do not call `can_start`, `can_continue`, or targeted `has_owned_receipt` in that root gate because FROM is not yet defined.
When the target is known, `target_trigger` and `visible` may use an OR between matching owned receipt and the existing recipient start eligibility.
Use `cbrn_export_transaction_can_continue` for the active cancellation requirement, without reintroducing free factory, 1500 unreserved stock, or live-sale requirements.
Add `cancel_effect` that initializes `cbrn_export_cancelled` and calls `cbrn_export_transaction_cancel`.
A failed start publishes no active row, so the native timer must cancel rather than apply nominal completion.
Preserve native targeted cooldown and the existing one factory modifier.
Keep implementation flags inside hidden triggers and use existing meaningful requirement text.

Add English keys `cbrn_export_fee_cost_frozen`, `cbrn_export_fee_cost_short`, and `cbrn_export_fee_cost_ready`, each reading `[?cbrn_export_fee|.0]` with the normal PP icon and appropriate shortage color.
Wire existing `cbrn_export_protective_equipment_extra_cost` to `[This.GetCbrnExportPoliticalCost]`, retaining the full physical 500 shipment and native factory/time text.
No icon or asset change is needed.
The existing `GFX_decision_cbrn_export_protective_equipment` consumer remains the owning decision's presentation.
Parent accepted docs and Event 026 coverage registry must distinguish integrated source, scenario proof, and native transfer acceptance.

## Meaningful source evidence

Twelve final-revision inline scenarios executed the actual parsed model primitives and ownership publication/release/predicates with the existing source VM under conservative helper-local temporary cleanup.
The scenarios passed: mixed oldest-first exact 500 at donor stock 1500, repeated send refusal, exact model cancellation return with repeated refund refusal, two isolated recipient rows, native partial send 100 with 400 already released units retained on donor, partial release 250 with no send and exact remaining refund, partial refund 200 with exact later retry, mismatched donor debit 500 versus recipient gain 250 retaining evidence and refusing retry, and a negative stock reader unable to turn a reservation into a grant.
The first scenario covers exact successful conservation at stock 1000 after reservation.
The two-recipient scenario starts at stock 2000, so the second genuine start can retain the original 1500 floor.
The negative-reader guard was added during the first review and its eight primitive scenarios passed afterward.
Parent integration then identified that native `target_root_trigger` needs an actor-only continuity predicate before FROM exists.
The requested owned-receipts count and guarded lifecycle helpers were implemented and all twelve scenarios rerun on the final revision.
Four added scenarios verified two targeted rows with repeated publication and release, a failed-start row retaining ownership/count through partial refund until exact return, a native mismatch retaining recovery ownership/count, and a zero-held row retaining ownership/count until fee closure.
The actor predicate was executed with no usable recipient fixture, and its actual parsed body contains no FROM reference.
Fee-closed state and start-failed state were explicit fixtures in these counter scenarios, rather than execution proof of shared fee APIs or the full start callback.

The VM source is `docs/plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js`, SHA-256 `50dacff487c6487d8a32991bf9a9435c6351ef0a699c8a8a20d66ec051421bc0`.
Its native adapter precedent is `docs/testing/2026-10-03_cbrn_immediate_protection_source_tests.js`, read without executing its file-writing suite.
The inline model adapter explicitly modeled native stock mutations, concrete token interpolation, `@FROM` recipient keys, and synchronous reads.
It did not replace the model helper bodies or relax lexical helper cleanup.
Tool result chunk `48a779` contains the final twelve-scenario result and executed source hashes.
No standalone test artifact or new test runner was created because the parent owns test files.
An initial inline attempt stopped before any scenario because the reused parser cannot parse unrelated complex schema lists in the whole CBRN constants file.
The successful run loaded the exact numeric `cbrn_math` category needed by the exercised bodies instead.
This was a test input correction, with no gameplay schema fallback.

Final exercised helper file SHA-256 identities are effects `49e275ad1804ae924b0e8bc3d9cc70b6dac27c3639fac96637c7ebd17be1b36b`, triggers `3c8146ed1b56dae158a06db801ebeb8838545a8abc74ddfbe6e03aa1c98006aa`, and scripted localisation `c3bf7a24d8d62a550999e1ee1d54e956f9914eb602ac173a36f5ec255a7b3ab4`.
These identify the actual uncommitted helper bytes tested, not a parent commit or native engine revision.

Source review verified that success outcomes are downstream of the measured exact 500 gate, that released stock is removed from escrow before native sends, that cancelled accepted fees have no ordinary PP refund, and that selection rollback uses the reused exact component/refund primitives.
It also resolved the negation token to the existing `cbrn_math.negation_multiplier` and confirmed all referenced tuning constants exist.
Start, whole finish/cancel orchestration, canonical fee quote/payment/record/achievement execution, recipient context, AI, save persistence, and native behavior were not exercised by this worker's model primitive scenarios.

## Local reference evidence and route gaps

Direct `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, `hoi4.source_lookup`, `hoi4.script_validate`, and domain inspection routes are absent from this worker's connected `ALL_TOOLS` list.
The parent explicitly owns isolated SDK 3.6 reference/domain/script/probability evidence and instructed this worker not to start a server.
No native MCP retrieval, domain inspection, rewrite, or runtime transfer scenario is claimed here.
Local source reading is not equivalent native evidence.

| Reference path | Read lines/sections | SHA-256 revision |
| --- | --- | --- |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md` | 1252-1267 add/remove equipment, 4833-4857 meta effects, 6550-6557 send equipment, 7820-7840 temporary variable writes | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md` | 2110-2134 variable comparisons, 3624-3640 country flags, 5006-5015 variable existence | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/dynamic_variables_documentation.md` | 557-559 country concrete equipment reader | `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md` | 216-249 script constant lifetime/access | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/script_constants/documentation.md` | Schema and examples, entire short document | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |
| `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md` | 2248-2305 native stock/send rules and examples, 4683-4714 scripted helper lifecycle | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` | 125 flag targeting, 263-281 target lifetime, 435-443 temporary storage, 548-553 variable targeting, 1615 stockpile reader | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md` | 339-355 native selection timer/cancellation | `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162` |
| `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md` | ROOT/FROM scope definitions at 260-263 | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |
| `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md` | 656-689 scripted text priority and trigger temporary lifetime | `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064` |

Installed `events/AAT_Finland.txt:3722-3736` uses live native send blocks with `equipment =` archetypes.
Installed `events/DOD_Hungary.txt:525` and `:653` use `type =` send blocks, while `common/scripted_effects/SAF_german_coup_effects.txt:141-150` provides concrete `type =` examples in effect tooltips.
The helper preserves the current owner's `type =` spelling and uses real concrete tokens rather than asserting one spelling is invalid from the thin generated documentation.
The three installed precedent file SHA-256 revisions are AAT Finland `363c53751ed2fbe113fbed5635940f4494b5c67f3bfa0a3787aa327f6cdfda13`, DOD Hungary `951ed86af53737a062c63b9434a15b93980149e1804d53c5056cc2dfa4a309ad`, and SAF scripted effects `a075a33130685a1987336491da37fd6d9e595e13de2576ecab51aff3a6727959`.
The offline stock/send rule notes native partial sends when stock is insufficient, so a nominal amount is not used as proof.
The existing token interpolation precedent is `chaosx_dynamic_effects.txt:50-57`.
The existing shared quote/component/refund docs are `docs/systems/universal_cost_modifier.md` and `common/scripted_effects/chaosx_universal_cost_effects.md`.
The delayed PP-only sale confirmation precedent is `026_black_friday_effects.txt:black_friday_settle_cbrn_external_aid_pp_fee_receipt`.

## Limitations, blockers, and follow-up

No design simplification or weaker physical shipment contract was introduced.
The helpers conserve measured model units and fail closed rather than authorizing nominal delivery.
Native acceptance remains unresolved: generated send documentation has no returned delivery receipt or explicit promise that both stockpile readers update synchronously within one script block.
The offline documentation warns that positive stockpile additions can depend on producer equipment unlocks.
Reservation/refund/recredit operate on concrete model totals, with no script-visible per-producer or per-variant provenance inventory.
Therefore exact native recredit and synchronous donor/recipient deltas, including foreign or locked models, require parent evidence.
If the installed engine cannot satisfy that contract, the parent must keep exact delivery blocked and report the engine limitation, without activating a grant or nominal-send fallback.
Unexpected native deltas remain recovery evidence and cannot automatically reconstruct lost producer or variant information.

Native cancellation must preserve original donor ROOT and target FROM even when the recipient becomes invalid.
A nonexistent donor whose stock cannot accept a native return retains pending model escrow instead of fabricated restoration.
No whole-world cleanup or alternate recipient fallback is supplied.
The parent should cover actor loss in existing native owner callbacks and retain unresolved recovery if that engine scope cannot execute.
Post-expiry purchase confirmation follows the existing delayed service precedent, including its original sale-sequence checks.
The shared proof may reject a receipt after a subsequent sale supersedes its achievement sequence, and the adapter does not weaken that gate.

Parent task-specific checks remain: start at exactly 1500 with one factory already committed, normal/half/quarter fee execution, missing source failing closed, failed first record and allocator cleanup, canonical typed PP proof, continuity after source expiry, two simultaneous native targets, invalid target and actor cleanup, full five-model exact delivery, partial delivery with no nominal success outcomes, repeated whole callbacks, stockpile unlock/provenance behavior, save persistence, and matching MCP evidence.
Parent probability evidence must cover any existing decision gate integration that changes observed AI scenarios, even though this worker did not alter weights.
Parent localisation and cost text wiring remain pending.
Shared-tree staging and commit are intentionally left to the parent.
Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`.
No skill was created or updated.
