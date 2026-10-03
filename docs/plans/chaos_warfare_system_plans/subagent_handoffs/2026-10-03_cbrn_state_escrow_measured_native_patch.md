# Measured native STATE mask escrow repair

Disposition: implemented source repair with persistent bounded source scenarios; parent MCP/final integration evidence remains pending.
Acceptance basis: parent repair assignment dated 2026-10-03 requires actual before/after concrete mask stock observations for existing occupied/external state reservation and refunds.
The parent subsequently authorized the two reserved-completion guards to reject quarantined receipts.
This is a repair of existing resource lifecycle behavior, with no balance/design simplification, new grant, periodic hook, equipment, GUI, administrative retry or generic projected-busy cleanup.

## Owned changes and contracts

Changed existing common/scripted_effects/cbrn_protection_effects.txt blocks:

- cbrn_reserve_requested_masks_to_state
- cbrn_refund_occupied_state_mask_reservation
- cbrn_refund_external_state_mask_reservation
- cbrn_distribute_reserved_occupied_masks_to_state: two negative quarantine/recovery guards only
- cbrn_distribute_reserved_external_masks_to_state: two negative quarantine/recovery guards only

Added common/scripted_effects/cbrn_state_escrow_native_effects.txt with four local helpers and this handoff.
Other blocks, original donor/control-change semantics, five-model order, fitting/coverage/filter/resistance/compliance outcomes, and generic busy/projected state were not edited by this worker.
Parent edits to owner callbacks/on-actions are reviewed integration inputs, not worker-owned changes.
Nothing was staged or committed.

| Helper | Scope and inputs | Outputs and defaults | Side effects and consumers |
| --- | --- | --- | --- |
| cbrn_state_escrow_measure_model_debit | COUNTRY current donor; temporary cbrn_mask_native_model equipment token and cbrn_mask_native_requested remainder | Caller-owned temporary before/after/requested/observed/valid; observed0 and valid0 until validated; requested bounded against nonnegative before stock | One negative native model stock dispatch, reread that exact model; reserve wrapper ROOT consumer |
| cbrn_state_escrow_measure_model_credit | COUNTRY stored original donor; model token and exact held requested amount | Same temporary outputs; observed gain and valid only for nonnegative snapshots and gain between0/requested | One positive native model stock dispatch, reread exact model; common STATE refund consumer |
| cbrn_state_escrow_refund_models | STATE; temporary cbrn_mask_escrow_external0/1, corresponding normal held rows and original donor | Caller-owned cbrn_mask_escrow_refunded and refund_blocked; initially0 | Applies measured credit in original donor scope, subtracts only measured valid gain, marks blocked while any row/quarantine remains; both existing refund wrappers |
| cbrn_state_escrow_record_native_mismatch | STATE; external selector and native before/after/requested/observed/model outputs | Caller-owned cbrn_mask_escrow_quarantined1 | Stores exact observation, marks family state mismatch/recovery, stops later native operations; occupied donor also receives country recovery_pending |

Native model substitution uses documented meta_effect with a single MODEL argument resolved from [?cbrn_mask_native_model.GetTokenKey].
No unverified parameterized scripted-effect syntax was introduced.
The reserve wrapper and common refund helper initialize every native output in STATE before entering the COUNTRY child scope.
The existing public outputs completed/refunded/refund_blocked retain their names and their documented outer-caller declaration obligation.
No input/output temporary token is scoped with ROOT/PREV.
Internal generic temporary names are local to one synchronous call family.

## Exact reservation and refund behavior

Reservation preserves the existing oldest-first order: reconditioned, basic1, improved2, advanced3, sealed4.
It binds the original donor and active state receipt before the first native debit.
Each nonnegative bounded observed debit alone populates its existing model held row, increments completed, and decreases remaining need.
A partial debit preserves that smaller actual held quantity and proceeds to later models for the remaining original request.
A zero debit creates no held quantity.
All-zero valid attempts clear their empty donor/active receipt.

Negative stock readers, negative observed debit, negative after stock or an observed debit exceeding the requested dispatch cause quarantine.
They are never clamped into accepted ownership.
The family normal fields native_before/native_after/native_requested/native_observed/native_model retain the first mismatched observation.
The family STATE native_mismatch and recovery flags preserve the original donor and every earlier valid held model row.
completed returns0 even if earlier models in that state had valid debits, preventing that state from publishing a paid program.
The occupied donor country gets cbrn_occupied_transaction_recovery_pending.
Additional occupied state reservations reject that country flag, so later states cannot reserve around quarantine.
An existing active/mismatch/recovery receipt cannot be overwritten by a repeated reserve.

Refund validates the stored original donor's existence rather than using the current controller.
For each exact held row, it reads that donor's concrete model count before the credit and again afterward.
Only a gain between0 and requested is accepted.
The held row decreases only by that measured gain and refunded increases only by the same amount.
A partial/zero credit retains the exact remainder, original donor and active receipt, returns refund_blocked1, and marks family recovery.
Later explicit refund invocations can credit only the remaining held quantity; they do not repeat already returned units.
No periodic or administrative retry was added.

A negative/overlarge gain or invalid reader preserves the unreduced held row and exact first observation, marks native_mismatch, returns blocked1 and prevents any further native credit in that family.
This protects against duplicating a suspect prior native credit.
All-zero rows with no mismatch clear the five model rows, donor, active and family recovery flags.
The country recovery_pending flag is intentionally retained; it may describe other unresolved paid/physical receipts and must not be globally cleared by one successful state return.

Both reserved completion wrappers reject family native_mismatch and recovery before consuming any model.
A quarantined receipt therefore cannot later issue its retained rows as protection.
A partially returned canceled receipt is likewise a refund obligation rather than a completion source.
Already issued positive coverage is never reversed or credited back by this family.

## Parent consumer review

The parent-owned national begin now requires positive aggregate reservation AND absence of country recovery_pending before paying the fee/publishing the program.
If earlier states reserved valid models and a later state quarantines, the parent refunds the earlier marked valid receipts and retains the quarantined state.
The parent preserves an owned target marker for an active mismatched state even when its completed output is0.
This makes the exact unresolved receipt visible to bounded owner cleanup without treating it as successful delivery.

The parent-owned on_state_control_changed callbacks now initialize refunded/refund_blocked before each refund call.
They clear the occupied target/external active project flags only on blocked0, preserving unresolved state receipts on loss of control.
The existing scopes remain ROOT=new controller, FROM=old controller, FROM.FROM=transferred state; actual refund still uses the stored original donor.

The existing Protective Aid single-state begin invokes PP payment and active project publication only after positive completed.
Quarantine returns completed0 and therefore requests no fee or publication.
No additional pre-fee rejection gap remains in the reviewed country/aid call sites.
The parent owns final inventory of other consumers and their exported-output initialization.

## Meaningful evidence and limitations

The test worker captured the pre-fix shared source file SHA-256 ff04b3decb07dd1fa7fd21ce9070d6de1622a320fbb960bc2380126ad2c3dfce and selected bodies/AST hashes before this edit.
Its two counterexamples use declared native partial-operation fixtures, not claims that these native anomalies occurred in game:
requested debit100 with actual removal40 had incorrectly reported completed/held100;
held100 with actual refund gain40 had incorrectly reported refunded100 and erased the active receipt.
Both defects motivated this specific repair.

Current full-source parsing succeeds through the existing exact quotation test parser: four new helper definitions and43 existing protection helper definitions.
The parent-assigned persistent source-test worker confirms 46 combined occupied/export scenarios passed with zero failures, 2,007 actual helper returns and 8,686 helper-local temporary values discarded.
Reproduction command: node docs/testing/2026-10-03_cbrn_occupied_export_source_tests.js from the mod root.
Evidence: [persistent results](../../../testing/2026-10-03_cbrn_occupied_export_source_results.json), with immutable defective-before bodies and current shared/helper hashes matching the implementation below.
Repair-specific cases execute the parsed occupied/external mixed-five-model reserve/refund order with model counts20/30/40/50/60, full return and repeated no-op; external valid partial debit100 to40, storing/returning only40; occupied valid partial debit100 to40, held40; occupied partial credit40 leaving held60, then exact remainder60 and repeated no-op; negative/oversized debit and credit quarantines with repeated refusal for both families; parent national positive-aggregate payment rejection under quarantine; and parent control-change partial-return marker retention then exact remainder cleanup for both families.
The domain adapter models native stock changes, token expansion and COUNTRY/STATE scope bindings and preserves conservative scripted-helper temporary cleanup.
It executes the actual parsed source/receipt bodies rather than substituting payment or refund algorithms.
Full physical fitting/coverage/outcome execution, negative initial stock-reader cases and actual reserved-completion dispatch remain separate parent validation limits; the completion quarantine guards were source-reviewed but no complete state distribution was inferred from those guards.
These results do not claim observed native partial behavior or engine delivery evidence.

The connected worker exposes reference_context/search/read/source_lookup, while script_validate is absent.
Reference context/search/read succeeded with no missing or omitted required source kinds for this surface; script_doc coverage is unavailable but installed game_doc and offline wiki are available.
No alternate MCP server/client was launched.
The parent owns final MCP validation and source-linked decision/event evidence.

Read syntax sections with exact source identities:

| Reference | Lines | Revision |
| --- | --- | --- |
| C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md: add_equipment_to_stockpile | 1252-1266 | 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af |
| Same effects documentation: meta_effect | 4833-4852 | same revision |
| C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/dynamic_variables_documentation.md: num_equipment COUNTRY | 557-559 | 538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda |
| C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/paradox_wiki/Effects - Hearts of Iron 4 Wiki.md: Equipment | 2246-2255 relevant table; read returned2246-2263 | 997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c |
| Same Effects snapshot: Meta effects | 4617-4682 | same revision |
| Same Effects snapshot: Scripted effects | 4683-4714 | same revision |
| C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md: Variable types | 435-443, read in preceding bounded owner tranche | 62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4 |
| Same Data structures snapshot: Token-valued variables | 955-972 | same revision |

Installed effect documentation explicitly permits negative equipment removal and a variable amount.
Installed dynamic documentation identifies the concrete COUNTRY equipment reader.
Neither documentation establishes synchronous native reader updates, exact producer/variant provenance, consumer execution or save/reload behavior.
Vanilla meta substitution precedent read: C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_effects/CZE_scripted_effects.txt:438-490 injects a variable-resolved SKODA_OPT into a static idea token through meta_effect.
Its file SHA-256 is cb5ee5136b5759efe4caaaace23189964fce57af18558d0ac535336ea93319c6.
Installed add_equipment_to_stockpile documentation above supplies the exact native equipment debit/credit precedent.
The parent-provided export measured primitive is the same-repository precedent; it was read only.
Its sampled source SHA-256 is 49e275ad1804ae924b0e8bc3d9cc70b6dac27c3639fac96637c7ebd17be1b36b.
Source observation and modeled native changes are not observed game proof.

Current raw file SHA-256:

- common/scripted_effects/cbrn_protection_effects.txt: 62248367f0e75540ad18141d3636c31215f4a5a1d1502a0ce92824dc5182fdb6
- common/scripted_effects/cbrn_state_escrow_native_effects.txt: 107d041e9762e2e54e131c4d23e26cdab8842f2cd611213f45f181091cd1b567

Normalized-LF selected-body SHA-256 without a trailing line break:

- Reserve: 42f599e366aaf4cca15fb766f34686cee4b3e44c64fb862163dab4548a965972
- Occupied refund: 46f5dcbdea1c94c4a46ea076d6f5b476a7c0b65ad013b428fb7a9a89777f461f
- External refund: 0dff6f7e9e10dba947926eb6a13e89aa1c86f054349bfbcd3ea7bfc84743e5cc
- Occupied completion guard body: dec04e1225becc0409178879446274defec5bc8cff8b975233f393d46f904414
- External completion guard body: 95887642266ea77eef8e4a6146af7522c3a282e2e2de3bc228a7bf4fdc20e00b

These are concurrent-worktree implementation samples, not immutable before fixtures.
The parent's persistent test evidence retains the immutable selected before bodies separately.

No design simplification or fallback was used.
Native anomalous deltas remain explicit unresolved recovery cases; no rollback is fabricated.
No new constants or asset/localisation keys were needed because these are hidden mechanical receipt guards.
Future follow-up belongs to existing owner recovery/evidence handling; no broader mechanic is proposed here.

Skills reused: chaos-redux-events, chaos-redux-decisions-missions and chaos-redux-subagents.
No skill change was needed; the existing exact-delta and temporary-output rules cover this repair.
