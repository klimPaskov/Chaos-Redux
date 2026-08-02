# Event 016 KRG biological stockpile and delivery lifecycle addendum

Date: 2026-08-03

Status: design contract queued; no gameplay, shared CBRN, model, or asset files changed.

## Purpose

The Event 016 country package already carries biological project history, native delivery technologies, containment ideas, and the confirmed-use world-threat hook. It does not yet own a bounded quantity ledger for the Kruger State. The missing layer must make biological deployment a concrete production and delivery system without creating a free payload or bypassing the existing condemnation, contamination, retaliation, and Fallout systems.

This addendum is the implementation contract for a later reviewed tranche. It is intentionally not a one-flag patch. The lifecycle must be added as one transaction family so transfer, fixed-tag formation, institutional takeover, defeat, and terminal cleanup cannot leave a usable payload behind.

## Current runtime evidence

`brilliant_scientist_apply_biological_force_history` restores native biological delivery technologies and the Event 016 delivery ideas from the carried scientist history, but it does not create a quantity ledger. `biological_cap = 4` is defined in the Event 016 constants and currently has no KRG stockpile consumer. `brilliant_scientist_krg_record_confirmed_offensive_biological_use` is correctly called only after a real offensive release and must remain that way.

The native CBRN systems own equipment payloads, reservations, consumption, condemnation, contamination, diplomacy, retaliation, and world-end accounting. Event 016 must not duplicate those effects or infer an offensive release from readiness, research, staging, authorization, a failed delivery, or an attacker accident.

## Event 016-owned identifiers

The implementation should add the following names in Event 016-owned files.

| Surface | Identifier | Contract |
| --- | --- | --- |
| Script constants | `brilliant_scientist_krg_biological` | One shared tuning table for cap, batch size, production cost, reservation expiry, recovery delay, and AI weights. |
| Country variables | `brilliant_scientist_krg_biological_stockpile` | Integer number of ready delivery charges owned by KRG. It is never negative and never exceeds the cap. |
| Country variables | `brilliant_scientist_krg_biological_reserved` | Integer number of charges reserved by an in-flight native delivery. It is not spendable by a second action. |
| Country variables | `brilliant_scientist_krg_biological_production_cycles` | Completed bounded production cycles, used for history and route AI, not for direct combat strength. |
| Country variables | `brilliant_scientist_krg_biological_consumed_total` | Total confirmed payload charges consumed by a real native release. |
| Country variables | `brilliant_scientist_krg_biological_last_action_date` | Date receipt used to prevent same-day replay and to support UI text. |
| Country flags | `brilliant_scientist_krg_biological_stockpile_ledger_active` | Set only after the KRG biological history bridge initializes the ledger. |
| Country flags | `brilliant_scientist_krg_biological_production_locked` | Set by containment, terminal cleanup, defeat, or a dismantled biological project. |
| Country flags | `brilliant_scientist_krg_biological_delivery_in_flight` | Mirrors a native reservation and is cleared only by the native outcome callback or expiry cleanup. |
| Country flags | `brilliant_scientist_krg_biological_use_recorded` | Event 016 history marker set after the first confirmed release; it is not a substitute for the shared CBRN history. |
| Character flags | `brilliant_scientist_krg_biological_agent_[family]_enabled` | Per-agent authorization receipt for anthrax, plague, tularemia, smallpox, and weaponized zombies. The exact family suffix must be expanded into concrete flags rather than a dynamic flag name. |
| Event targets | `brilliant_scientist_krg_biological_delivery_actor` | Short-lived target for the KRG country entering the native reservation and callback chain. |
| Event targets | `brilliant_scientist_krg_biological_delivery_receipt` | Short-lived receipt for the one native operation being resolved. |

The implementation must keep the existing `brilliant_scientist_krg_record_confirmed_offensive_biological_use` helper and existing native `bio_*` variables as the authoritative release evidence. The new Event 016 variables are an accounting layer, not an alternate biological weapon system.

## Production contract

Add one visible KRG decision in the existing exotic and biological category, named `brilliant_scientist_krg_produce_biological_delivery_batch`.

The decision is available only to sovereign KRG when the biological deployment and containment chain is operational, the ledger is active, production is not locked, the total stockpile plus reservations is below `constant:brilliant_scientist_krg_biological.stockpile_cap`, and no biological production timer is active. It pays the standard project-batch material, fuel, manpower, civilian-factory, and time costs through the existing KRG cost helpers. It must not add political power or equipment payload directly.

Its completion effect performs the following steps in order.

1. Re-check the ledger, cap, project history, and containment trigger.
2. Pay the concrete batch cost.
3. Add one bounded quantity to `brilliant_scientist_krg_biological_stockpile`.
4. Increment `brilliant_scientist_krg_biological_production_cycles`.
5. Set the production receipt and refresh the KRG decision layer.
6. Re-evaluate exposure, condemnation, and security only through existing Event 016 helpers; production itself is not a confirmed offensive use.

The decision must have a visible trigger tooltip showing the current stockpile, reservations, cap, cost, and containment requirement. It must have an AI factor that prefers production only when a native staging state exists, the corresponding biological agent is enabled, the KRG route has an active delivery authority, and stockpile is below the cap. AI must not queue production when the project is locked, the KRG is in terminal cleanup, or the operation is already reserved.

## Native delivery boundary

Event 016 must not implement a second raid outcome. The existing native biological raid and lifecycle code remains responsible for payload type, equipment debit, reservation, target, success or failure, contamination, condemnation, retaliation, and world-threat effects.

A separately reviewed shared-system patch is required at the native reservation and outcome boundary. The hook must be narrow and opt-in:

1. Before a native reservation succeeds, resolve `event_target:brilliant_scientist_krg_biological_delivery_actor` and verify that the actor is sovereign KRG, has an active Event 016 ledger, has `brilliant_scientist_krg_biological_stockpile >= 1`, has no delivery already in flight, and has the matching per-agent authorization receipt.
2. On successful reservation, decrement the Event 016 ready stockpile by one, increment `brilliant_scientist_krg_biological_reserved` by one, set `brilliant_scientist_krg_biological_delivery_in_flight`, and store the native operation receipt. The native equipment payload remains authoritative for the actual delivery type.
3. On confirmed native consumption, decrement the Event 016 reserved quantity by one, increment `brilliant_scientist_krg_biological_consumed_total`, clear the in-flight flag, set the Event 016 confirmed-use receipt, and call the existing `brilliant_scientist_krg_record_confirmed_offensive_biological_use` helper. The native system continues to apply all condemnation, contamination, diplomatic, retaliation, and Fallout effects.
4. On a failed delivery, attacker accident, cancelled reservation, or expired operation, return the reserved Event 016 charge exactly once. Do not set the confirmed-use receipt and do not call the confirmed-use helper.
5. If a native operation has already debited its equipment payload, the callback must use the stored operation receipt and never refund or debit the Event 016 ledger twice.

The hook needs an explicit shared-CBRN owner and its own audit. It must not be added opportunistically to `016_brilliant_scientist_kruger_state_decision_effects.txt` because the current Event 016 helper has no access to native reservation identity or outcome scope.

## Transfer, formation, and defeat cleanup

The ledger follows Kruger only through a verified transfer transaction or the verified fixed-tag KRG formation transaction. The current host may not retain a usable Event 016 biological ledger after Kruger leaves.

For an ordinary transfer, copy the ready stockpile, reserved quantity, production cycles, consumed total, last-action receipt, and per-agent authorization receipts only after the recipient has passed the existing valid-country and Kruger-identity checks. The old host clears all Event 016 ledger variables and flags after the recipient transaction succeeds. An in-flight native operation remains owned by the original native actor until its callback resolves; if the transfer contract cannot preserve that native actor pointer, the transfer must be rejected while delivery is in flight.

For fixed-tag formation or institutional takeover, copy the ledger only after the existing KRG formation receipt, capital viability, laboratory inheritance, and Kruger identity transaction succeeds. The former host is cleared by the existing sovereignty cleanup. Do not create a second charge during formation.

For defeat, arrest, exile, permanent death, project dismantling, terminal Fallout, or a failed formation, clear ready and reserved Event 016 quantities, clear all in-flight receipts, lock production, and leave native CBRN history untouched. If a native operation is active, its owner must resolve or cancel it through the native cleanup contract before the Event 016 country is removed. No defeat path may transfer a charge to a new country without an explicit verified formation or transfer receipt.

## Safety and containment interactions

The production decision requires the existing biological containment chain. The ledger must be included in the same containment and authority checks that currently gate `brilliant_scientist_krg_authorize_canonical_biological_last_resort_actions`.

Low authority, failed quarantine, unresolved safety incidents, or production lock prevents new batches. A previously reserved operation is resolved by the native outcome contract and is not silently cancelled by a GUI refresh. High authority and strong Independent Capacity may preserve the ledger during a containment attempt, but a successful release still records the shared native consequences and can still trigger the existing terminal threat pipeline.

## UI, localisation, and AI surfaces

The category tooltip must expose the current ready quantity, reserved quantity, cap, last production date, and whether an operation is in flight. The decision detail must explain that production creates a bounded delivery charge and does not itself deploy a weapon. The native operation's existing tooltip remains authoritative for the actual payload and outcome.

Add localisation in the existing Event 016 KRG localisation file for the decision name, description, trigger tooltip, cost tooltip, stockpile display, reservation display, production receipt, returned-charge receipt, and confirmed-use receipt. Do not describe variables, implementation history, or a fallback to the player.

Add the decision to the KRG route AI plan only after the native callback contract exists. The AI should prioritize a single batch when a matching staging state and authority are ready, maintain a small reserve below the cap, and stop production when containment or security is degraded.

## Required validation before implementation acceptance

The gameplay tranche must provide static and targeted scenario evidence for the following cases.

| Scenario | Required result |
| --- | --- |
| Biological project history enters KRG | Ledger initializes at zero and never grants a free charge. |
| One production decision | Exactly one charge is added after real costs and the decision timer. |
| Cap reached | Production is unavailable and stockpile plus reservations never exceeds the cap. |
| Duplicate production click | One completion receipt and one batch only. |
| Successful native release | One reserved charge is consumed, native effects run, and Event 016 confirmed-use history is written once. |
| Failed native release or attacker accident | The reserved charge returns once and no confirmed-use history is written. |
| Transfer before reservation | Ledger and authorization receipts move once; old host clears. |
| Transfer during reservation | Transfer is rejected or preserves the native actor pointer; no orphan receipt is allowed. |
| Fixed-tag formation | KRG inherits the ledger once and the former host cannot produce or deliver afterward. |
| Defeat, terminal cleanup, or project dismantling | Ready and reserved Event 016 quantities are cleared and native history remains intact. |
| AI with no staging or containment | No production decision is selected. |

No implementation should be called complete until these receipts, native callback evidence, localisation, and balance values are reviewed together. The seven Event 016 unit model packages remain deferred and are not a prerequisite for this ledger.
