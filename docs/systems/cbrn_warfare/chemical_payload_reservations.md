# Chemical payload reservations

This CBRN-owned API holds the exact prepared chemical equipment assigned to a scripted operation.
Event 032 uses it for preparation, current launch authorization, once-only consumption, physical custody settlement and cancellation.
Native raids retain their own equipment payment contract and do not use this scripted reservation as an additional debit.

## Identity and payment

Each holder country allocates a monotonically increasing receipt handle.
The identity is holder, handle, consumer and operation nonce; the record freezes exact agent, concrete model, route, intended state, source state and required quantity.
The four existing prepared-air model families retain the exact national agent profile alongside their model token.
No payload technology, free equipment or new model family is granted.

`cbrn_reserve_action_payload` validates the current CBRN target policy, technology/project unlock, profile and free stock, then measures the real native debit.
A full observed payment becomes a held receipt.
A valid partial payment becomes a pending return, and an invalid observation remains quarantined with before/after/requested evidence.
A repeated request with the same live identity and binding reuses that receipt without paying again.
An unresolved earlier receipt blocks the same consumer from silently opening a replacement, and closed nonces cannot be replayed as new reservations.

The native wrappers in `cbrn_payload_reservation_native_effects.txt` reuse the existing concrete-model measurement implementation from `cbrn_state_escrow_native_effects.txt`.
They preserve the original request and expose actual observed deltas.
Caller-owned temporary output storage is required at every wrapper boundary.
Receipt API results are separately named normal country variables and must not be shadowed by same-named temporary variables.

## Calling contract

Public transactions run in the actual holder COUNTRY.
Reservation, launch validation and consumption additionally require that country to be ROOT so the existing exact-target CBRN policy has its intended actor.
Refund, capture and destruction callbacks may arrive under a different ROOT and still account to the selected holder.

Normal COUNTRY request fields are `cbrn_payload_request_consumer`, `cbrn_payload_request_nonce`, `cbrn_payload_request_site` (STATE pointer), `cbrn_payload_request_target` (STATE pointer), `cbrn_payload_request_agent` and `cbrn_payload_request_route`.
Follow-up transactions also supply `cbrn_payload_request_handle`; transfer supplies `cbrn_payload_request_recipient` as a COUNTRY pointer.
The caller initializes the separate temporary `cbrn_payload_custody_proof`, `cbrn_payload_recovery_proof`, `cbrn_payload_transfer_proof` or `cbrn_payload_loss_proof` to missing and supplies only the proof it has established for this transaction.
The registered consumer is `constant:cbrn_payload_receipt_consumer.missiles` and its nonce is the owning operation ID, never a reused display counter.

Normal results are `cbrn_payload_result`, `cbrn_payload_result_amount` and `cbrn_payload_handle`.
Validation writes the separate `cbrn_payload_validation_result`; a positive validation is not a fresh consumption acknowledgement.
Successful consumption publishes `cbrn_payload_consumed_agent`, `cbrn_payload_consumed_model` and `cbrn_payload_consumed_class`; transfer publishes the receiver's `cbrn_payload_transferred_handle`.
Missing identity, binding, authorization or physical proof defaults to rejection and makes no nominal payment or consequence record.
`already_settled` is replay evidence, not permission to emit another release.
Partial and quarantined results require custody settlement and must never launch.

Event 032's concrete usage is `missiles_reserve_chemical_payload_receipt` at preparation, `missiles_check_chemical_receipt_for_commit` at commitment, and `missiles_consume_chemical_payload_receipt` immediately before delivery.
Each builds the request from the same frozen operation fields; cancellation calls `missiles_release_chemical_payload_receipt` rather than restoring a nominal equipment quantity.
Site lifecycle callers use `missiles_settle_chemical_payloads_at_site` with the exact holder target and one `constant:cbrn_payload_site_action` disposition.
The selector's result and settled quantity are `cbrn_payload_site_result` and `cbrn_payload_site_settled_amount`.
The sanctions owner supplies the existing temporary `cbrn_payload_disposal_fraction` to `cbrn_dispose_reserved_payload_fraction`; it does not re-price or debit held stock.

`cbrn_air_payload_can_fund_strategic_action` is a COUNTRY read-only quote predicate taking temporary `cbrn_action_agent` and using the existing strategic-route quantity, exact profile, unlock and shared class/stock checks.
`cbrn_payload_consumer_has_no_open_receipt` takes temporary `cbrn_payload_lookup_consumer` and rejects an unresolved current-holder consumer slot without mistaking a copied foreign ledger for a new country's reservation.
Neither predicate mutates stock, durable state, policy or custody.

## Launch and settlement

`cbrn_validate_payload_reservation` rechecks the exact full hold and current authorization without requiring replacement free stock.
Its validation result is separate from the fresh consumption acknowledgement.
`cbrn_consume_payload_reservation` repeats identity and held-state checks before moving the quantity to consumed, closes the live receipt, and publishes the frozen agent/model/quantity without another equipment debit.
Only the delivery owner may then submit an actual release to the shared protection, exposure, Deaths, evidence, Condemnation and Air Cleanliness pipeline.

`cbrn_return_payload_reservation` needs an explicit recovery proof, the actual holder, matching source identity/control and the original exact profile.
It measures the credit, removes only observed returns from held quantity, and retains partial or quarantined balances.
Launch technology or policy can be lost without invalidating a physically recoverable refund.
Closed, consumed or transferred receipts do not pay again.

`cbrn_discard_payload_reservation` requires a proven loss disposition and creates no release, casualties or confirmed-use record.
`cbrn_transfer_payload_reservation` verifies the frozen source state and its new controller, then moves known held stock into a sealed linked receipt on that controller.
It credits no native stock and grants no technology or use authority.
`cbrn_integrate_captured_payload_reservation` requires current holder/control, recovery proof, technology and an exact matching profile before measured credit into usable stock.
Sealed capture is excluded from the captor's profile lock until integration begins; a partial integration retains the lock on its remainder.

The per-receipt invariant is `reserved + received = held + returned + consumed + destroyed + transferred` for reconciled observations.
Received/transferred quantities are internal movement, not new native production.
Country held, captured, bound-profile and quarantine totals update from the selected receipt's previous contribution and current contribution in constant time.
They do not require a recurring scan or a recount of every captured arsenal.

## Owner and compliance hooks

The Event 032 adapter distinguishes the payload's own launch site from other barrage participants.
Capture, proven destruction, isolation, recovery, captured integration and removed-country processing supply explicit physical dispositions.
Pending records remain with CBRN even after a missile order closes.
An exact-site selector freezes matching handles before any settlement removes entries from the live array, and uses private initialized loop-break variables.

Air-profile changes cannot relabel original holds, pending returns or quarantined reservations.
The stockpile detection contract includes held and quarantined chemical quantities.
The sanctions owner's existing destruction fraction also applies to reserved holdings, rounded to bounded whole equipment units; it never debits that equipment a second time.
Destroyed holdings cannot be recovered through a later cancellation.
Unreconciled native observations withhold a completed compliance acknowledgement.

## Files and visual consumers

- Constants: `common/script_constants/cbrn_payload_reservation_constants.txt`.
- Receipt owner: `common/scripted_effects/cbrn_payload_reservation_effects.txt` and `common/scripted_triggers/cbrn_payload_reservation_triggers.txt`.
- Native primitives: `common/scripted_effects/cbrn_payload_reservation_native_effects.txt`.
- Event adapter: `common/scripted_effects/032_missiles_payload_receipt_effects.txt` and `common/scripted_triggers/032_missiles_payload_receipt_triggers.txt`.
- Source-driven scenarios: `.tools/test_cbrn_payload_reservations.py`.

This extends existing chemical-delivery and missile-operation consumers without a new GUI, equipment model or CXT content grant; the existing chemical payload and Event 032 CXT packages supply their owned content.
The preparation cost display uses shared chemical/biological payload texticons registered by `interface/cbrn_payload_texticons.gfx`, plus the exact vanilla `GFX_unit_nuclear_missile_icon_small_texticon` for nuclear stock.
Their asset lineage and parent review belong to the Event 032 payload-cost icon handoff, not the reservation ledger.

## Validation limits and future work

Source execution scenarios cover real helper bodies with conservative temporary lifetimes and explicit native/world leaves.
They do not prove engine stock timing, producer/variant identity, native temporary presence checks or live callback ordering.
Quarantined native observations are preserved, not reported as complete refunds or inferred stock destruction.
Future consumers must register their identity and provide their own exact physical-custody contract before using this API.
Nuclear and biological receipt generalization remains separate work; these helpers do not reinterpret their stock models.
