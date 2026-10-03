# CBRN occupied distribution and export cost architecture review

Status: read-only contract review completed; parent implementation and execution evidence remain pending.
Acceptance basis: the parent records user approval of CBRN/Event 026 completion and requests canonical service fees/native factory adaptation while preserving physical shipment quantities, exact model escrow, existing outcomes, and existing periodic-hook boundaries.
Only this handoff was created for this task.
No gameplay, staging, commit, game, log, or MCP-server operation was performed.
This is a bounded technical completion plan, with no new grants, cheaper physical shipments, balance targets, administrative actions, equipment, or worldwide loops.

## Exact surfaces and scopes

| Surface | Scope and current source | Required retained behavior |
| --- | --- | --- |
| `cbrn_supply_occupied_population` | COUNTRY ROOT, no meaningful decision FROM; `cbrn_protection_decisions.txt:377–426` | One country program, 30-day native timer, ordinary PP 25/two factories, full five-model reservation distributed across selected controlled occupied states |
| `cbrn_begin_occupied_distribution_program` | COUNTRY ROOT; state iterators change THIS/PREV while ROOT stays donor; `cbrn_protection_decision_effects.txt:231–263` | Selection already omits the repeated free-factory gate, reserves real stock per STATE, publishes active program and charges PP only after positive total reserved |
| Occupied finish/clear | COUNTRY ROOT iterating its controlled STATE receipts; same effects file 265–296 | Revalidate original receipts, distribute from escrow, refund unused/invalid-state models to stored donor, clear target markers |
| `cbrn_export_protective_equipment` | COUNTRY ROOT donor and COUNTRY FROM recipient; decisions file 216–253 | Fourteen-day native timer, one factory, 60-day targeted native re-enable, PP service fee at start, fixed 500 real mask transfer at completion |
| Export start/finish | COUNTRY ROOT; completion recreates local `cbrn_protection_trade_partner` from FROM; effects file 370–372 and 387–417 | Preserve valid-recipient rules, real model transfer, exported/received statistics, aid/opinion/Condemnation outcomes only on actual successful physical delivery |

Normal prices/timing are centralized in `common/script_constants/cbrn_system_constants.txt`: occupied PP 25, factories two, duration 30, cooldown 90; export PP 15, factories one, shipment 500, duration 14, cooldown 60; export start reserve threshold 1500.
Parent-requested canonical sale quotations are occupied PP 25/13/7 and native factories two/one, and export service PP 15/8/4 with native factory commitment one.
These are expected ordinary/half/quarter outputs under the existing exact whole-unit producer, not replacement hardcoded fee branches.
All additional eligible source composition must remain canonical; unsupported occupied native factory quotes fail closed.
No export factory variant is needed because ceiling of one factory under those discounts remains one.

## Occupied program contract

Pre-click `cbrn_country_can_start_occupied_mask_reservation` currently adds the ordinary factory requirement to `cbrn_country_can_pay_occupied_mask_reservation` (`cbrn_protection_triggers.txt:613–627`).
The selection body already calls the latter and omits the second free-factory check.
Preserve that accepted correction when introducing canonical fee/variant guards.
The national quote at lines 593–610 sums live uncapped state needs and caps the physical total at actual five-model stock.
Do not discount that need, model quantity, distribution cost/wastage, filters, or ledger increments.

Use the existing Protective Aid factory-quote/source pattern for ordinary/sale decision IDs with the same public name, outcomes, willingness logic, duration, and native re-enable.
One shared COUNTRY cooldown flag guards both IDs because this is one national program, not a targeted foreign-state purchase.
Stamp its 90-day duration unconditionally on native selection through a temporary duration from the existing constant.
The immediate callback recheck omits both the just-stamped cooldown and already committed factories.
Persist the selected factory variant while the country's active program exists; active visibility must remain valid after sale expiry and after reserving all unreserved stock.
Both variants use one begin/finish/cancel callback family and the same active program guard, so switching IDs cannot start a second national escrow program.

Keep STATE `cbrn_occupied_mask_escrow_*` receipts, their stored donor, and `cbrn_occupied_distribution_program_target` markers as the physical ownership evidence.
The COUNTRY program separately stores its frozen fee amount, canonical source ID, PP transaction ID, sale sequence, and selected variant.
There is one PP receipt for the whole country program, not one fee per selected state.
Require stored STATE donor equality with ROOT in every finish/refund decision; do not consume an unrelated donor's receipt based on marker name alone.
An exact selected-state list is sufficient if the parent needs explicit enumeration, but no whole-world scan is necessary: current controlled-state processing and the existing exact control-change refund hook already cover ownership loss.
`common/on_actions/chaosx_on_actions.txt:27–36` refunds a lost state's occupied receipt to its stored donor before clearing the program marker.
Keep that hook intact; do not add periodic refund scans.

Begin must initialize aggregate quote/reserved count, each state escrow-completed output, fee quote validity/affordability, and fee payment result in the enclosing caller before reading nested returns.
Require positive real aggregate reservation before final publication; payment/record failure refunds the selected masks and rolls back only actually paid, unrecorded/recorded PP as appropriate.
Freeze the fee/receipt/source at accepted selection; completion must not price again or require the sale to remain active.
Aggregate actual consumed/usable quantities or existing per-state supplied proof in the country callback before fee achievement confirmation.
Existing `cbrn_distribute_reserved_occupied_masks_to_state` supplies positive-usable proof and refunds unused models (`cbrn_protection_effects.txt:1830–1844`).
A program that delivers no actual protection must not credit the PP service achievement merely because its timer elapsed.
Cancellation or loss of every valid recorded target refunds only remaining escrow and closes the fee receipt without successful-delivery achievement credit.
Follow the accepted timed Protective Aid service-fee cancellation policy; do not silently introduce an ordinary PP fee refund where the existing owner spent that fee at start.

## Export escrow and continuity contract

Current pre-click donor gate at `cbrn_protection_triggers.txt:37–48` requires at least 1500 archetype masks, one free factory, and ordinary PP 15.
Retain the 1500 eligibility floor for new starts while replacing only the fee price with the canonical quote and checking enough actual concrete-model stock for the 500 escrow.
Current recipient rules at lines 823–840 require existence, not ROOT, human/noncapitulated, no war with ROOT, a valid protection partnership or humanitarian-carveout membership, and recipient stock no greater than the same reserve threshold.
Retain those rules unless the parent explicitly distinguishes start-only demand from continuing recipient eligibility.

Selection must reserve exactly 500 actual mask units in the same oldest-first model order.
Export cannot reuse STATE escrow helpers because FROM is COUNTRY.
Store the five reserved model counts, fee/source/transaction/sale-sequence fields, and active/refund/closed status on the donor COUNTRY keyed by the recipient, for example `cbrn_export_reserved_basic_@FROM` and `cbrn_export_receipt_@FROM`.
That separates simultaneous recipient timers and prevents one later selection from overwriting another fee or shipment.
Use a stored recipient pointer or the native callback FROM to address the correct keyed row; no single durable `cbrn_protection_trade_partner` target can represent simultaneous recipients.
Recreate a regular event target locally inside one finish callback only if needed for nested effects.
No global event target is needed.

After native selection reserves factories and masks, begin must not require another free factory or a second 1500 unreserved stock balance.
Require recipient/context, fresh fee/source validity, and exact 500 model allocation instead.
After accepted payment/reservation, `visible`, `target_root_trigger`, and `target_trigger` need an owned active-receipt continuity branch so native target enumeration does not hide paid timers when the donor stock falls below 1500 or the live sale expires.
Cancellation must use owned active receipt and continuing donor/recipient context, never a fresh start reserve check.
This directly avoids the existing cancel condition at decisions line 250 self-cancelling when the newly reserved 500 lowers unreserved stock from 1500 to 1000.
Retain native targeted cooldown; this single-ID export requires no extra national blanket cooldown or duplicate decision family.

Completion must transfer only the stored five-model escrow quantities, totaling exactly 500, and consume/close them once.
Do not debit the donor stock again at completion.
Any positive recipient stock change must be backed by consumed reservation fields; it is an escrow transfer, never an ordinary grant.
If using native `send_equipment`, first release the exact reserved model quantities to the donor once, then transfer those exact models and capture delivery evidence; if crediting directly from escrow, bind every credit to that same stored receipt and clear/commit only the actual credited quantity.
Either implementation must preserve the same concrete model counts and cannot credit 500 from an empty or already-closed receipt.
The parent must choose the bounded transfer implementation and carry its native validation limits.
No helper should refund released donor stock while also retaining recipient masks.

Current `cbrn_export_masks_to_protection_partner` sends archetype 500 with `old_prioritised = yes` then increments all aid statistics by nominal 500 without checking actual delivery.
Its initial stock guard makes that plausible for the ordinary path, but it is not an escrow release implementation or an actual native receipt proof.
A completed exact 500 transfer must precede those unchanged success outcomes and fee achievement confirmation.
Cancel/invalid recipient returns every remaining concrete model to the original donor once, clears only that recipient's active receipt, and closes its service-fee receipt without delivery credit.
If native partial transfer can occur, retain the measured delivered/remaining model split and report the unresolved engine behavior; never claim exact 500 outcome from the nominal send amount alone.
Do not refund already delivered masks as though they remained in escrow.

## Shared service-fee receipt and temporary contract

For both owners the achievement receipt contains PP service only: family `political_power`, basis `primary_component`, exact primary/component ID PP 1, member one.
Forward all four typed metadata inputs before recording the component; physical masks are conserved issued/transferred property and must not be represented as discounted paid material components.
Freeze source/fee/receipt identity in owner normal fields through the timer.
The global sale expiry clears only the registry source, not these selected receipts or variant markers.
Successful post-expiry completion may use the existing explicit delayed PP-only confirmation contract from `black_friday_settle_cbrn_external_aid_pp_fee_receipt`, with frozen sale sequence and exact stored fee claims.
Do not use the ordinary active-sale achievement gate alone for delayed confirmation or infer achievement family from resource kinds.

Initialize outer quote final/valid/affordability outputs, allocator ID, payment result, record result/index, settlement result, refund result/totals, and physical delivery/proof outputs before each nested API whose result is consumed.
Copy PP and factory component results to dedicated scratch before reusing generic quote fields.
Refund recorded actual fee components through the shared receipt API; explicitly credit an unrecorded successful debit if record fails.
Clear unused allocator proof on pre-receipt failure when no transaction row mapping exists, matching the corrected immediate response owner.
Preserve failed credit/refund evidence rather than claiming restoration from a native dispatch call alone.
Settlement/refund and physical escrow cleanup must be idempotent and scoped to the matching program or recipient receipt.

## Minimal implementation touchpoints and meaningful checks

Direct decision changes: occupied ordinary/sale native definitions, shared visibility/cooldown callbacks, current export target continuity/cancel callback, and fee custom-cost text.
Owner helper changes: `cbrn_begin_occupied_distribution_program`, `cbrn_complete_occupied_distribution_program`, `cbrn_clear_occupied_distribution_targets`, `cbrn_begin_protective_equipment_export`, and `cbrn_export_masks_to_protection_partner`, or bounded local adapters directly called by those entry points.
Trigger changes: occupied start/payment gates and exact continuing-program predicate; export start fee gate, concrete 500 reserve preflight, per-recipient active receipt and cancellation predicates.
Constants: add only the occupied sale factory anchor/variant enumeration needed by the canonical native pattern; reuse all existing ordinary prices, quantities, durations, and cooldowns.
Presentation: canonical PP getters, frozen in-flight fee getters, occupied native factory quote/variant text, and export cost text that keeps the shipment at 500.
Helper documentation and the parent's Event 026 coverage registry must match actual implemented calls and validation limits.
Shared generic quote/payment/refund/proof code and adjacent callers are read-only dependencies owned by others.

Meaningful parent scenarios: occupied exact two/one free factories; half/quarter fees; shared country cooldown across variant switching; all masks/factories reserved without self-cancel; one state lost versus every selected state lost; partial need reduction with unused-model refund; zero versus positive supplied proof; source expiry before delivery; missing active source failing closed; first record failure clearing allocation proof; repeated cancellation/completion; export starts at exactly 1500, reserves 500, and remains active at 1000; two different recipients retain separate receipts; donor stock consumed elsewhere cannot steal the 500 escrow; invalid recipient refunds remaining exact models; successful shipment/fee proof after expiry; and no nominal 500 statistics from partial or absent actual transfer.

No engine actions or scenarios were executed by this reviewer.
Connected direct HOI4 routes remain absent; no alternate server/client was launched, and the parent owns reference/script/domain/probability evidence through its isolated SDK client.
The offline Data structures targeting/temp lifetime rules, Decision modding timer/cancel semantics, installed native stockpile/send documentation, current universal receipt docs, and actual Protective Aid callback/source contracts informed this bounded review.
Source-only continuity/refund architecture is not native timer, transfer, model provenance, save-persistence, or AI proof.
No design simplification is proposed; exact native transfer acceptance and parent implementation remain required work.

Sampled worktree SHA-256 identities: decisions `959ede805e2b30d99ce9aeb6b7c0ccd6834e594e28aefd4e9937ce0563c75c4f`; owner effects `54b5bf3b166d4df25987890a717afa657e92270d3f656f221f1312afd9695e98`; protection triggers `20adf65c8f92d5af549fbe20bd9087b0471b5c0a44bfad507648f41da67d32f4`; system constants `e8364f5895aec72ca6066c096f456190b87dbc1ca252e13260293056324113ea`.
These identify concurrent-worktree samples, not immutable before fixtures or committed revisions.
Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`; none created or updated.
