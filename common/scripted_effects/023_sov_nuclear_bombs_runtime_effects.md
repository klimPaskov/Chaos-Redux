# Event 023 Soviet Nuclear Bombs Runtime Effects

This file describes the source-level runtime boundary for Event 023's event-owned nuclear ledger and native delivery contract. The current implementation and unresolved consumer limits are summarized in `docs/plans/023_sov_nuclear_bombs_plans/subagent_handoffs/023_documentation_curator_final_2026-09-19.md`; this document does not certify native delivery or save/reload conservation.

Event 023 owns authorization, action context, target selection, evolution gates, and player-facing decisions.

The shared contract in this file owns reservation, native `launch_nuke` invocation, and the single commit point for an accepted action.

The existing native `on_nuke_drop` route remains responsible for Chaos, deaths, contamination, Fallout, condemnation, and other detonation consequences.

No effect in this file calls `chaos_meter_on_nuke_drop` or a Fallout effect directly.

## Ledger model

The global ledger uses mutually exclusive intact buckets named `sov_nuclear_bombs_ledger_operational`, `sov_nuclear_bombs_ledger_assigned`, `sov_nuclear_bombs_ledger_reserved`, and `sov_nuclear_bombs_ledger_transferred`.

Terminal buckets are `sov_nuclear_bombs_ledger_dismantled`, `sov_nuclear_bombs_ledger_missing`, and `sov_nuclear_bombs_ledger_expended`.

The conservation equation is `total_registered = operational + assigned + reserved + transferred + dismantled + missing + expended`.

The bounded Part 6 transit register `global.sov_nuclear_bombs_ledger_in_transit` is a subset of `global.sov_nuclear_bombs_ledger_assigned`, not another additive term. The source state's `sov_nuclear_bombs_site_assigned` loses one device at departure and its `sov_nuclear_bombs_site_in_transit` holds that same device until exact arrival, return, capture, or loss. The global and SOV actor assigned aggregates continue to include it while it is in transit; their in-transit counters are memorandum subsets with `0 <= in_transit <= assigned`. Arrival places it in the exact destination site's assigned bucket without touching the aggregate or native stockpile. Return reverses the source-site movement. Capture restores the one source-site assigned entry only so the existing native-aware `sov_nuclear_bombs_mark_site_transferred` can move it into transferred custody once; a proven loss moves the assigned aggregate into missing custody once and marks native proof disputed.

The bounded active-dismantlement register `global.sov_nuclear_bombs_ledger_active_dismantlement` is a subset of the existing `reserved` bucket, with `0 <= active_dismantlement <= reserved`. The accepted demolition action stages and reserves one device at mission start through the preexisting action contract. A nonce-bound state and SOV actor receipt identifies that reserved device as undergoing dismantlement; only the existing accepted action commit changes `reserved` to completed `dismantled` and spends the native device. Cancellation releases the reservation through the existing action context. The register itself never debits or grants an additional device.

`sov_nuclear_bombs_refresh_ledger_reconciliation` recomputes physical custody and the accounted total after each transaction and stores `sov_nuclear_bombs_ledger_reconciliation` as clean or disputed. Negative buckets, a pending native callback, or a native stockpile mismatch force the disputed state instead of silently repairing a missing device.

The event ledger never overwrites the vanilla country nuclear stockpile.

Native `num_of_nukes` is checked before delivery, while the event-owned counters remain the authoritative allocation and conservation record.

## Effect registry

| Identifier | Scope | Inputs | Outputs and side effects |
| --- | --- | --- | --- |
| `sov_nuclear_bombs_initialize_ledger` | Any country or state scope | None | Idempotently creates global ledger variables and sets `sov_nuclear_bombs_ledger_active`. |
| `sov_nuclear_bombs_initialize_actor_ledger` | Country scope | None | Idempotently creates actor allocation, action receipt, and reservation variables. |
| `sov_nuclear_bombs_refresh_ledger_reconciliation` | Any country or state scope | Existing global ledger buckets | Recomputes physical custody, accounted total, and clean/disputed reconciliation. |
| `sov_nuclear_bombs_register_event_owned_devices` | Country scope | `sov_nuclear_bombs_registration_amount` | Credits the one-shot Event 023 opening allocation and marks `sov_nuclear_bombs_event_registration_complete`. |
| `sov_nuclear_bombs_credit_evolution_devices` | Country scope | `sov_nuclear_bombs_evolution_stage`, `sov_nuclear_bombs_evolution_credit_amount` | Credits a strictly increasing evolution tranche once and clears the two input variables. |
| `sov_nuclear_bombs_register_production_devices` | Country scope | `sov_nuclear_bombs_production_amount` | Credits a one-shot event-owned production batch to the native stockpile and operational ledger, increments the transaction sequence, and clears the input variable. |
| `sov_nuclear_bombs_register_storage_site` | State scope | `sov_nuclear_bombs_site_registration_amount` | Moves devices from the exact owner's operational bucket into the state's assigned bucket and records owner/controller pointers. |
| `sov_nuclear_bombs_reserve_device_for_action` | Country scope | Previously staged Event 023 action context | Moves exactly one device into reserved custody, preferring the action state's assigned bucket when available. |
| `sov_nuclear_bombs_release_reserved_device` | Country scope | Active reservation with matching source-specific mirrors and no native pending receipt | Returns one device to its original assigned, operational or stored-holder transferred bucket. Missing proof moves nothing and retains a disputed active receipt. |
| `sov_nuclear_bombs_commit_reserved_device` | Country scope | Active reservation after native launch or exact callback | Moves exactly one reserved device to expended or dismantled custody and stamps a transaction sequence. |
| `sov_nuclear_bombs_select_disperse_source` | Country scope | Player-selected dispersal destination and a valid assigned depot pool | Locks one bounded source state before the dispersal mission starts without changing its ledger bucket. |
| `sov_nuclear_bombs_clear_disperse_selection` | Country scope | Dispersal source and destination event targets | Clears the temporary endpoint flags and source pointer without changing custody. |
| `sov_nuclear_bombs_finalize_one_device_dismantlement` | State scope | A registered site after one-device commit | Marks the site dismantled only when its intact operational, assigned, reserved, and transferred buckets are all zero; it does not spend a second device. |
| `sov_nuclear_bombs_execute_shared_action` | Country scope | Valid Event 023 action context and active reservation | Invokes native `launch_nuke` with the exact state id, records the expected native stockpile-after value, and holds a detonation reservation until the callback confirms it; demolition commits synchronously. |
| `sov_nuclear_bombs_confirm_native_delivery` | Country scope | Event 023 pending native delivery after exact `on_nuke_drop` state and nonce checks | Records the native stockpile-after snapshot, requires the exact one-device delta, commits exactly one reserved device, and marks the action accepted without applying detonation consequences. |
| `sov_nuclear_bombs_commit_disputed_native_delivery` | Country scope | Pending native delivery whose stockpile delta or callback contract fails | Moves the single pending reservation to missing custody, marks the state and global native custody disputed, and clears the pending context without replaying shared consequences. |
| `sov_nuclear_bombs_reconcile_unreturned_native_delivery` | Country scope | SOV-only daily maintenance while an Event 023 native delivery is pending | Increments the persisted callback-age counter and, after `constant:sov_nuclear_bombs_tuning.native_delivery_timeout_days`, commits the unresolved reservation once to disputed/missing custody. It never refunds or replays the action. |
| `sov_nuclear_bombs_clear_action_context` | Country scope | Optional active reservation | Attempts a verified rollback and clears flags, nonce and pointers only after the active receipt closes. Native pending and refused rollback preserve their full context. |
| `sov_nuclear_bombs_mark_site_transferred` | State scope | Registered storage site | Moves current intact site buckets into transferred custody without granting operational access. |
| `sov_nuclear_bombs_operationalize_breakaway_site` | State scope | Transferred site and completed actor delivery capability | Moves the exact held cohort into the breakaway operational bucket and conditionally grants that quantity to its native stockpile; it does not grant Soviet technology or a new cohort. |
| `sov_nuclear_bombs_mark_site_dismantled` | State scope | Registered storage site | Moves all current intact site buckets into dismantled custody and marks the terminal state flag. |
| `sov_nuclear_bombs_mark_site_missing` | State scope | Registered storage site | Moves all current intact site buckets into missing custody and marks the terminal state flag. |
| `sov_nuclear_bombs_snapshot_event5_release_tranche` | Release-host country scope | Existing `soviet_collapse_dynamic_release_target` event target | Visits owned target cores and snapshots only those with represented Event 23 site or target context. |
| `sov_nuclear_bombs_snapshot_event5_kaz_release_tranche` | SOV country scope | None; static target is KAZ | Takes the same bounded owned-core snapshot before either static KAZ release. |
| `sov_nuclear_bombs_begin_event5_state_transfer` | State scope | Exact state at an Event 005 literal transfer | Finishes an older pending receipt if present, increments the generation, and snapshots the state if it has represented Event 23 context. |
| `sov_nuclear_bombs_snapshot_event5_state` | State scope | Registered storage, reactor, native delivery, dispersal, or persisted target state selected by a transfer boundary | Reads site buckets, custody value, and holder only for registered storage; clears those snapshot fields for non-storage states while retaining the broader context receipt. |
| `sov_nuclear_bombs_capture_event5_context_before` | Exact state scope | Current snapshot generation and live Event 23 variables, flags, and state targets | Persists global, SOV, site, holder, and target-context values without changing gameplay. |
| `sov_nuclear_bombs_capture_event5_context_after` | Exact state scope | Same generation after transfer and ledger refresh | Persists the observed post-transfer context, including exact target IDs and owner/controller pointers, without restoring source values. |
| `sov_nuclear_bombs_finish_event5_state_transfer` | State scope | Pending state after its transfer command | Clears the in-progress marker and invokes the existing exact-state reconciler once. |
| `sov_nuclear_bombs_finish_event5_release_tranche` | Release-host country scope | Existing dynamic release target | Finishes pending target-core receipts in the host and released country's owned states after the release. |
| `sov_nuclear_bombs_finish_event5_kaz_release_tranche` | SOV country scope | None; static target is KAZ | Finishes pending KAZ-core receipts in SOV and KAZ owned states after the release. |
| `sov_nuclear_bombs_reconcile_event5_state` | State scope | Pending Event 005 snapshot with no transfer in progress | For registered sites, compares frozen buckets and classifies custody; for every affected context state, records the post-transfer view, checks arsenal conservation, records completion generation, and clears pending once. |
| `sov_nuclear_bombs_reconcile_event5_release_country` | Country scope | Event 005 release callback | Visits pending represented-context states owned or controlled by the released country; the state reconciler waits while an explicit transfer is in progress. |
| `sov_nuclear_bombs_cleanup_annexed_actor` | Country scope | Event 005 `on_annex` FROM scope | Rolls back a reservation, clears transient action context, and leaves the state ledger for state-level reconciliation. |

## Shared action contract

The parent must supply the following country flags and variables before calling `sov_nuclear_bombs_reserve_device_for_action` and `sov_nuclear_bombs_execute_shared_action`.

The country flag `sov_nuclear_bombs_action_actor_proven` records proven actor identity.

The country flag `sov_nuclear_bombs_action_authorized` records Event 23 authorization.
The optional country flag `sov_nuclear_bombs_action_remote_recovery_authorized` permits only the existing validated remote demolition custody path.

`sov_nuclear_bombs_action_type` must use one of the action constants `test`, `demonstration`, `combat_strike`, `accident`, or `demolition`.

`sov_nuclear_bombs_action_weapon` must equal `constant:sov_nuclear_bombs_action.nuclear_bomb`.

`sov_nuclear_bombs_action_route` must equal `constant:sov_nuclear_bombs_action.native_launch_nuke`.

Exactly one country flag supplies the physical yield profile.
`sov_nuclear_bombs_action_detonating` covers yielded tests, demonstrations, true-yield accidents and strikes, while `sov_nuclear_bombs_action_non_detonating` covers demolition and failed/no-yield tests.
The `sov_nuclear_bombs_action_yield_profile_is_valid` trigger rejects both missing and contradictory profiles, and context cleanup clears both flags together with actor proof, authorization and remote-recovery permission.
These Boolean permissions use flags rather than numeric 0/1 variables, while action type, weapon, route, nonce, custody pointers and outcome remain categorical or numeric variables.
An accident outcome above the centralized catastrophic Integrity threshold (10) is a non-yield preparation accident; at or below it, that same selected outcome is a true-yield accident.
The non-yield test contract commits one reserved device and calls the shared `chaos_meter_on_non_yield_test_accident` endpoint once after acceptance; it never calls `launch_nuke` or terminal Fallout.
The threshold is the parent's tuning choice under the user's approved physical severity gate, and the four outcome weights remain unchanged.

`sov_nuclear_bombs_action_nonce` must be strictly greater than the actor's recorded `sov_nuclear_bombs_last_action_nonce`.

`sov_nuclear_bombs_action_state` must point to the exact target state and `sov_nuclear_bombs_action_target` must point to its current owner or controller.

The validator requires `atomic_research`, `nukes`, a positive native `num_of_nukes` value for detonating actions, a valid target pointer, an exact selected state, deployed-bomber capability inputs, fuel, airbase access and a non-terminal global state.
Those preflight inputs do not establish aircraft assignment, a launchable native raid or real bomber delivery, and native preparation/cancellation custody receipts remain required acceptance evidence.

Target validation checks geometry and country identity independently of reservation state.
Before reservation, `sov_nuclear_bombs_action_unreserved_source_is_valid` requires an eligible assigned, operational-country or permitted transferred source with the matching actor/global counters.
Ordinary assigned and operational sources must remain owned and controlled by the actor, while remote demolition validates the actual physical holder's transferred counter.
After reservation, `sov_nuclear_bombs_action_reservation_is_valid` requires the active source receipt, transaction sequence, global reserved count and applicable actor/state mirrors.
Assigned and transferred reservations require a reserved site mirror, while the operational-country pool uses its actor/global mirrors without manufacturing a site-reserved device.
Remote transferred reservations require their stored physical-holder pointer and cannot substitute another actor's positive reserved counter.
Rollback uses this source proof rather than current target or route eligibility, so a valid cancellation still returns its original device after a target becomes invalid.
An incomplete or mismatched proof moves no bucket and grants no refund, marks `sov_nuclear_bombs_action_reservation_disputed`, and retains the active flag and every source/holder/nonce field.
Context cleanup clears those fields only after the reservation actually closes, and a verified later rollback clears the dispute marker.
Clearing the actor dispute marker does not itself certify the broader global or site reconciliation, whose existing owner must validate its totals and physical provenance.
No unknown source discriminator can reach the operational-refund branch.
When no assigned source remains but the actor/global operational pool is positive, staging locks one existing owned and controlled registered depot as the operational source identity.
The source helpers read existing context and counters, grant nothing and default to failure for missing or mismatched input.
For example, `sov_nuclear_bombs_reserve_device_for_action` reaches the unreserved branch through the context gate, and native confirmation validates the resulting reservation branch before expenditure.

The accepted path issues exactly this native route: `launch_nuke = { state = var:sov_nuclear_bombs_action_state_id use_nuke = yes nuke_type = nuclear_bomb }`.

The adapter marks the launcher with a short-lived Event 023 atomic-delivery context before calling `launch_nuke`. The neutral Chaos consequence hook consumes that context to prevent an independently researched thermonuclear technology from changing this explicitly atomic action's consequence profile.

The native `on_nuke_drop` callback is the confirmation boundary. It must match the exclusive pending request's state id and action nonce before calling `sov_nuclear_bombs_confirm_native_delivery`; the parent then calls `sov_nuclear_bombs_finalize_confirmed_native_delivery` to record the action and close its Event 023 flow. The callback intentionally does not require the state to retain its pre-launch owner or controller, because the pending state and nonce are the Event 23 correlation contract while the native route resolves its own consequences.

The SOV-only maintenance hook also tracks a persisted callback-age counter. If no exact callback arrives before `constant:sov_nuclear_bombs_tuning.native_delivery_timeout_days`, `sov_nuclear_bombs_reconcile_unreturned_native_delivery` moves the reservation into disputed/missing custody and closes the request. This is a fail-closed ledger result, not a second detonation or a refund.

After that closeout the Event 023 state-pending flag, callback nonce, and action context are cleared. A late native callback therefore cannot satisfy the Event 023 correlation contract or commit a second device; the ordinary shared native consequence route remains the sole owner of any consequence the engine actually reports.

Vanilla does not echo the Event 23 nonce, request id, or action type through `on_nuke_drop`. The bounded correlation therefore uses one pending request, the exact state id, the action nonce stored on that state, and the native stockpile snapshot. A future engine/API surface that exposes a nonce should replace this correlation with an exact receipt.

The parent must not add a second Chaos, Fallout, death, contamination, or condemnation call around this contract.

## Event 005 custody bridge

The bridge runs only for an active Event 005 collapse with an active Event 023 ledger. Terminal collapse in progress does not block custody accounting; Soviet-only gameplay and world-end ownership retain their separate gates. The 82 direct transfers in the 34 Event 005 successor helpers call `sov_nuclear_bombs_begin_event5_state_transfer` immediately before the command and `sov_nuclear_bombs_finish_event5_state_transfer` immediately after. The four dynamic and two static KAZ releases likewise use their bounded pre/post tranche helpers.

Release sweeps are restricted to the release host's owned target cores, matching vanilla `release`'s owned-state contract. Within that actual transfer set, only states with represented Event 23 context receive a receipt: registered storage, reactor pending/owned, dispersal, native delivery pending, or one of the five persisted state targets. Direct transfers inspect only their literal state. A later transfer first closes any older pending receipt for its state, then takes a fresh generation. Each receipt persists the six site buckets where applicable, exact affected-state owner/controller, broader context, and generation. A global pending count and per-state pending flag remain auditable through save/reload. The pre-transfer in-progress flag keeps a synchronous release or state-control callback from closing the receipt before the script command returns; the explicit post-transfer helper then closes it. A second callback sees no pending flag and cannot count the transfer again. Repeated successor transfers take sequential generations.

The exact-state snapshot reads the six storage buckets, custody value, and site holder only under `sov_nuclear_bombs_state_is_registered = yes`. On a non-storage reactor, test, dispersal, native-delivery, or target state it clears all eight storage-only snapshot fields, then still captures the generation-bound wider context and exact owner/controller. The post-transfer bucket comparison and device-custody classification remain registered-storage-only.

The broader context is stored on the affected state under `sov_nuclear_bombs_event5_before_*` and `sov_nuclear_bombs_event5_after_*`, each with the site's snapshot generation. The global view includes registered, operational, assigned, reserved, transferred, dismantled, missing, expended, accounted, physical-custody, reconciliation, and transaction-sequence ledger values; Soviet usable devices; evolution last credited stage; breakaway actor counts; and the existing native stockpile snapshot. The native value is copied as observed evidence only and is never refreshed or written back by this bridge. The SOV view records the seven actor ledger buckets, Readiness, Integrity, posture, public knowledge, custody doctrine, evolution stage, reactor count/entitlement/pending count and pending state ID, cumulative production and active production amount, test attempts/result, phase, maintenance counter, and the existing native-delivery request IDs, nonce, age, and stockpile observations. Each optional source variable is copied only when it exists; absence clears the corresponding receipt field. SOV existence itself is recorded before and after.

The receipt also records current SOV mission/command/delivery flags, exact affected-state site flags, and the physical holder's, owner's, and controller's breakaway custody, technical, command, and delivery access markers where those countries exist. For each existing global state target `sov_nuclear_bombs_test_state`, `sov_nuclear_bombs_selected_test_state`, `sov_nuclear_bombs_selected_state`, `sov_nuclear_bombs_pending_reactor_state`, and `sov_nuclear_bombs_disperse_source_state`, it stores the scope pointer, numeric state ID, and the target state's owner and controller before and after. `sov_nuclear_bombs_event5_receipt_state` is a regular effect-chain target used only to write those owner/controller pointers back to the affected state; it is not a new persistent global target. Missing pointers clear their own receipt fields and do not stand in for a state.

After the physical site transaction and ledger refresh, the bridge compares the pre/post registered total and checks the observed accounted total against the observed registered total. A mismatch sets `sov_nuclear_bombs_event5_context_total_mismatch` on that state and keeps global reconciliation disputed. Normal per-bucket and SOV actor changes are recorded as deltas, not treated as new devices or copied back into gameplay. Non-storage context states do not create a storage ledger entry, physical holder, or breakaway nuclear actor.

If a site's six bucket values differ from its frozen receipt before the post-transfer reclassification, `sov_nuclear_bombs_event5_snapshot_bucket_mismatch` persists on that state and as a global flag. The site's reconciliation state and global ledger reconciliation remain disputed until a separate proven repair clears those flags. The bridge does not invent a compensating device or silently mark the receipt clean. The old and current owner/controller pointers remain available as transaction evidence after the pending flag clears.

`on_release_as_free` and `on_release_as_puppet` call `sov_nuclear_bombs_reconcile_event5_release_country` for the new country.

`on_state_control_changed` calls `sov_nuclear_bombs_reconcile_event5_state` only for the exact changed state when its pending snapshot flag is present. The reconciler itself refuses an in-progress receipt. Both callbacks and explicit post-command calls share the same one-shot reconciler.

The bridge never turns a breakaway's physical custody into immediate technical, command, or delivery access. A pending native reservation remains attached to its source state during transfer and cannot be operationalized until its callback is accepted; a native dispute blocks both breakaway operationalization and Soviet recovery.

The bridge records central Soviet, Soviet siege, breakaway physical, foreign, technical denial, missing, and dismantled classifications from exact current owner/controller facts.

Ownership-only releases are closed by the explicit post-release sweep over the release host and released country's owned states. The callback remains a secondary path for a pending receipt observed after the transfer command. If `SOV` is annexed or otherwise disappears while a native request is pending, the reservation is disposed into missing custody before transient context is cleared, preserving the ledger total without granting a callback a second commit.

If `SOV` disappears before a registered breakaway site's native-custody-removed receipt exists, the site remains transferred physical custody and does not auto-operationalize or receive a native stockpile grant. This is the fail-closed local-custody disposition for an incomplete transfer order; recovery, dismantlement, or a later verified native-custody transfer must resolve it.

### Transfer helper contracts

`sov_nuclear_bombs_snapshot_event5_kaz_release_tranche` has no parameter or output value. In SOV scope, it increments the global generation, closes an older pending receipt if found, and snapshots represented Event 23 context on SOV-owned KAZ cores; with an inactive Event 005 bridge it has no side effect. Example: `sov_nuclear_bombs_snapshot_event5_kaz_release_tranche = yes` immediately before `release = KAZ`.

`sov_nuclear_bombs_begin_event5_state_transfer` has no parameter or output value. In the exact state scope, it first closes any older pending receipt, then increments the generation and snapshots the state if it has represented Event 23 context. With an inactive bridge or no represented state context it creates no receipt. Example: `248 = { sov_nuclear_bombs_begin_event5_state_transfer = yes transfer_state_to = CFR sov_nuclear_bombs_finish_event5_state_transfer = yes }`.

`sov_nuclear_bombs_capture_event5_context_before` and `sov_nuclear_bombs_capture_event5_context_after` have no caller parameters or gameplay output. They run only in the exact state scope from the existing snapshot and reconciler, use the current state generation as their receipt key, and default absent optional variables and targets to absent receipt fields. The pre helper observes before ownership changes; the post helper observes after site reconciliation. Their side effects are state-local receipt variables/flags and one temporary regular event target; they do not grant devices, technology, staff, delivery forces, or native stockpile. Example: `sov_nuclear_bombs_snapshot_event5_state = yes` invokes the pre helper and `sov_nuclear_bombs_reconcile_event5_state = yes` invokes the post helper for the same pending generation.

`sov_nuclear_bombs_finish_event5_state_transfer` has no parameter or output value. In the exact state scope, it clears the in-progress marker, classifies the post-transfer owner/controller and physical holder, records the reconciliation generation, and decrements the pending count once. With no pending receipt it has no side effect. Example: `248 = { sov_nuclear_bombs_finish_event5_state_transfer = yes }` after a transfer.

`sov_nuclear_bombs_finish_event5_release_tranche` has the existing dynamic release target as its only input and no output value. In release-host country scope, it visits only pending target cores still owned by the host and pending states owned by the released country. If the target is missing it has no side effect. Example: `release = event_target:soviet_collapse_dynamic_release_target` followed immediately by `sov_nuclear_bombs_finish_event5_release_tranche = yes`.

`sov_nuclear_bombs_finish_event5_kaz_release_tranche` has no parameter or output value. In SOV scope, it visits only pending KAZ cores still owned by SOV and pending states owned by KAZ. If KAZ is not released, it closes any SOV-owned candidate receipts without changing custody ownership. Example: `release = KAZ` followed immediately by `sov_nuclear_bombs_finish_event5_kaz_release_tranche = yes`.

### Part 6 bounded registry helper contracts

All helpers below default to no gameplay mutation when their exact scope, selected state, country capability, or nonce proof is absent. None creates a device, aircraft, new country, terminal consequence, or player-facing control. Their examples are calls inside existing Event 23 source, not new decisions.

| Helper | Purpose and scope | Inputs and output | Side effects and example |
| --- | --- | --- | --- |
| `sov_nuclear_bombs_register_central_command_state` | State scope; identify the opening command capital. | Registered SOV-owned/controlled capital; outputs the state flag and SOV state pointer, otherwise no-op. | Registry only; `capital_scope = { sov_nuclear_bombs_register_central_command_state = yes }`. |
| `sov_nuclear_bombs_register_backup_command_state` | State scope; bind the first explicitly hardened non-capital depot as backup. | Registered, hardened, SOV-owned/controlled state and no current backup pointer; outputs state flag and SOV pointer, otherwise no-op. | Registry only; `event_target:sov_nuclear_bombs_selected_state = { sov_nuclear_bombs_register_backup_command_state = yes }`. |
| `sov_nuclear_bombs_register_production_reactor_site` | State scope; identify a completed Event 23 production reactor. | `sov_nuclear_bombs_reactor_event_owned`, an actual reactor, and SOV control; outputs role flag and original owner pointer. | Does not claim assembly capability; `sov_nuclear_bombs_register_production_reactor_site = yes` after reactor completion. |
| `sov_nuclear_bombs_register_institutional_access` | State scope; bind accepted breakaway technical access to its selected depot. | Registered site, exact holder, and holder's completed technical stage; outputs site flag and actor pointer. | Never grants a stage; `event_target:sov_nuclear_bombs_selected_state = { sov_nuclear_bombs_register_institutional_access = yes }`. |
| `sov_nuclear_bombs_register_breakaway_command_site` | State scope; bind accepted command formation to the same depot and institutional actor. | Institutional marker, matching holder pointer, and completed command stage; outputs site flag and actor pointer. | No delivery grant; `event_target:sov_nuclear_bombs_selected_state = { sov_nuclear_bombs_register_breakaway_command_site = yes }`. |
| `sov_nuclear_bombs_register_delivery_force_owner` | Country scope; record an actor with the installed vanilla bomber, fuel, technology, and airbase route. | Existing `sov_nuclear_bombs_event_has_delivery_route`; outputs self-pointer and registration flag or clears them when capability is absent. | Does not create or transfer aircraft; `sov_nuclear_bombs_register_delivery_force_owner = yes` at delivery mission start. |
| `sov_nuclear_bombs_register_delivery_force_site` | State scope; tie a selected depot to the actual holder with current vanilla delivery capability. | Registered site and valid holder route; outputs site role flag and owner pointer. | No instant operationalization; `event_target:sov_nuclear_bombs_selected_state = { sov_nuclear_bombs_register_delivery_force_site = yes }` after staged completion. |
| `sov_nuclear_bombs_begin_transit` | SOV country scope; depart one device on the existing reserve-dispersion decision. | Exact selected source/destination, assigned device, no active nonce; outputs paired state pointers/IDs, nonce, source transit bucket, global/actor transit subsets, and active flag. | Debits only the source site assigned bucket; `sov_nuclear_bombs_begin_transit = yes` before the 120-day decision waits. |
| `sov_nuclear_bombs_refresh_transit_registry` | Any scope; check the subset invariant. | Existing global assigned and transit counts, optional SOV active receipt; outputs a persistent dispute flag if negative, excessive, or pointer-incomplete. | No repair or scan; `sov_nuclear_bombs_refresh_transit_registry = yes` after a transit transaction. |
| `sov_nuclear_bombs_close_transit_receipt` | Exact source-state scope; close matching endpoint mirrors once. | Active state nonce, destination mirror, optional SOV country receipt; outputs a closed nonce and clears active source/destination/country pointers and transit subsets. | No physical bucket decision; `sov_nuclear_bombs_close_transit_receipt = yes` after arrival or disposition. |
| `sov_nuclear_bombs_settle_transit_source` | Exact source-state scope; resolve cancellation or Event 5 seizure. | One active transit device and current owner/controller; outputs returned, captured, or lost state flag. | Restores source assigned for return, invokes existing native-aware transfer for capture, or moves one device to Missing with native dispute; `sov_nuclear_bombs_settle_transit_source = yes`. |
| `sov_nuclear_bombs_complete_transit` | SOV country scope; arrive at the exact selected destination. | Matching source/destination nonce and IDs, SOV ownership/control, registered valid destination; outputs success flag or no-op. | Credits destination assigned and closes receipt once; `sov_nuclear_bombs_complete_transit = yes` from the existing dispersion completion. |
| `sov_nuclear_bombs_cancel_transit` | SOV country scope; settle the one selected source on mission cancel or annex. | Active country pointer and nonce; outputs the source disposition or a dispute when the pointer is missing. | Never chooses another source; `sov_nuclear_bombs_cancel_transit = yes` before clearing selected targets. |
| `sov_nuclear_bombs_reconcile_transit_state_change` | Exact changed-state scope; detect transfer of source or destination. | State transit flags and paired source pointer; outputs a single source settlement where necessary. | No world loop; `sov_nuclear_bombs_reconcile_transit_state_change = yes` inside the Event 5 state reconciler. |
| `sov_nuclear_bombs_register_active_dismantlement` | SOV country scope; identify the already reserved demolition device. | Accepted assigned-source reservation, exact source pointer, action nonce; outputs one state/country active receipt and global/actor memorandum subset. | Never reserves twice; `sov_nuclear_bombs_register_active_dismantlement = yes` after staging action context. |
| `sov_nuclear_bombs_refresh_dismantlement_registry` | Any scope; check active subset of reserved. | Global active and reserved totals; outputs persistent dispute on an impossible bound. | No extra debit; `sov_nuclear_bombs_refresh_dismantlement_registry = yes` after start or close. |
| `sov_nuclear_bombs_close_active_dismantlement` | SOV country scope; close a matched completed or canceled mission receipt. | Active country flag, exact source pointer and nonce; outputs site closed nonce and clears state/country mirrors and memorandum subset. | Does not commit or release the reserved device; `sov_nuclear_bombs_close_active_dismantlement = yes` after the existing commit or release. |
| `sov_nuclear_bombs_reconcile_dismantlement_state_change` | Exact changed-site scope; stop Soviet dismantlement when custody changes. | Active site flag and current SOV existence/control; cancels through the existing reservation-release path while SOV exists, or marks orphaned native custody disputed. | No automatic breakaway access; `sov_nuclear_bombs_reconcile_dismantlement_state_change = yes` after the Event 5 bucket comparison. |
| `sov_nuclear_bombs_reconcile_registry_state_change` | Exact changed-state scope; mark a command, reactor, institutional, or delivery role contested. | Existing role flags and exact SOV/holder pointers; outputs contested state flags and clears a lost backup pointer. | No role grant to a new owner; `sov_nuclear_bombs_reconcile_registry_state_change = yes` after Event 5 custody reconciliation. |
| `sov_nuclear_bombs_capture_event5_registry_before` / `sov_nuclear_bombs_capture_event5_registry_after` | Exact affected-state scope; freeze and observe registry context. | Current Event 5 snapshot generation; outputs matching before/after global subset, SOV pointer/nonce/flags, and state role/pointer/nonce fields, clearing absent optional fields. | Receipt only; `sov_nuclear_bombs_capture_event5_registry_before = yes` at the existing snapshot and `_after = yes` at reconciliation. |

The existing assembly decision selects one SOV-owned and controlled registered storage depot with usable infrastructure and an actual civilian or military factory.
The parent chose that rule within the user's authorization to implement the bounded registry; it adds no action, mission, cost type, facility, or device at start.
The current reactor and atomic-technology requirements, batch amounts, duration, and AI weights remain unchanged.
`sov_nuclear_bombs_register_assembly_site` runs in country scope with the short-lived `sov_nuclear_bombs_assembly_selection` target as input and stores the exact persistent state pointer, state id, owner, active state mirror, and transaction nonce.
It records SOV institutional access at the selected facility without granting another country's technical or command stage.
`sov_nuclear_bombs_close_assembly_receipt` runs in country scope on completion, rejection, cancellation, or SOV annexation, closes only the matching nonce, removes active mirrors and the global display target, and retains the historical facility identity and closed nonce.
For example, the assembly decision saves its FROM state as `sov_nuclear_bombs_assembly_selection`, then calls `sov_nuclear_bombs_assemble_batch = yes`; the production mission revalidates `sov_nuclear_bombs_event_active_assembly_site_is_valid` before registering a batch.
Event 5 freezes the facility role, owner, batch nonce, country state pointer/id/nonce, and observes cancellation or survival after the transfer.
Ordinary state-control callbacks use the same exact-state registry, transit, and dismantlement reconciliation helpers after any pending Event 5 snapshot closes; no world scan or periodic registry loop is added.
Loss of the assembly depot cancels the batch rather than moving its work or granting devices to a successor.
Save/reload and mandatory MCP scenario evidence remain outstanding.

### Exact callback and local-project ownership

Transit and dismantlement country helpers read the calling actor's nonce through PREV inside their exact source-state scope, rather than treating a capture/annex callback's ROOT as that actor.
The stored recorded-owner country returns through PREV to inspect the operationalized site flag; an identical recorded owner and physical holder must not receive two operational debits.
After an operationalized site's transfer accounting completes, its live operational marker is cleared and a separate historical marker is retained, so a successor can enter physical-custody stages without inheriting operational status.

Breakaway custody is selected into `sov_nuclear_bombs_local_custody_state` and its exact state ID on that actor.
The three timed stages retain and revalidate that actor-owned pointer, state ID and current physical holder; their completion or cancellation never clears Soviet/global selection.
The return-request action uses a separate transient actor pointer and clears it after its immediate request, without overwriting a timed project.
Event 5 before/after snapshots include each affected site's holder-owned local pointer, state ID, progress stage and active-stage marker.
Annex cleanup removes the dead actor's local pointer, while only SOV cleanup clears SOV-owned global selected, coercion and reactor targets.

The Secure Custody action accepts another depot only when the actor's current selected depot is no longer a valid pending physical-custody site.
Completion, loss, transfer, dismantlement and joint custody therefore release that selection slot without granting access to a second depot.
Securing a depot records `sov_nuclear_bombs_local_custody_actor` on that state and projects only that depot's proven technical and command receipts into the actor's current stage flags.
The state-scoped `sov_nuclear_bombs_event_state_has_local_custody_receipt`, `sov_nuclear_bombs_event_state_has_local_technical_receipt` and `sov_nuclear_bombs_event_state_has_local_command_receipt` triggers require matching current-holder pointers and uncontested institutional markers.
Their country-scoped `sov_nuclear_bombs_event_selected_site_has_local_*_receipt` wrappers also validate the exact selected state, ID and territorial custody.
Stage starts, completion and mission cancellation use these receipts, and operationalization additionally requires the holder's active timed delivery stage for that exact state ID.
Territorial reconciliation clears a former holder's live secured-custody flag and marks mismatched technical or command records contested while retaining their historical identities.
Event 5 before/after registry snapshots preserve the site custody actor, secured marker and access/command contested markers.
These helpers read state and flags only, add no device, technology, aircraft, cost type or world scan, and default to failure when a receipt is absent or mismatched.
For example, `sov_nuclear_bombs_start_breakaway_command_formation` checks the selected-site technical receipt, while the state's operationalization effect checks its command receipt and current holder's active delivery-stage identity.

An assembly closure requires the exact state ID and either a matching active nonce or the same state's already-closed nonce.
A mismatch retains its actor pointer and nonce, marks `sov_nuclear_bombs_assembly_receipt_disputed`, writes no closed receipt and blocks a replacement batch.
There is no guessed repair or device grant on that path.

`sov_nuclear_bombs_prepare_production_quote` is a country-scoped, scratch-only trigger used by both assembly start and `GetSovietNuclearBombsProductionQuote`.
Its inputs are the existing production tuning constants and optional reactor count; its output is the unscoped `sov_nuclear_bombs_production_quote` temporary variable, with no persistent state or resource side effects.
Callers initialize that output before invoking the helper; the helper returns true after computing the unchanged clamped quantity.
For example, the production effect initializes the quote, calls the trigger in its validated limit, then stores the result in the pending production amount; localisation initializes and calls the same helper before displaying it.
The mission displays the already-fixed pending amount, and cancellation retains the upfront resource expenditure.

## Constants

### Device-bearing resource profile

The six device-bearing strategic actions use `sov_nuclear_bombs_can_pay_release_cost` and `sov_nuclear_bombs_pay_release_cost` in the event's cost trigger/effect files.
Their inputs are the existing heavy command-power, light support-equipment and light fuel constants, with no optional fallback or new amount.
Payment spends those three resource types and does not touch the arsenal ledger, while the separate action contract alone reserves or spends the atomic device.
Together these are four spendable types, with political power retained only in the original strategic profile for non-device actions.
The matching cost and blocked-cost localisation is `sov_nuclear_bombs_cost_release`, `sov_nuclear_bombs_cost_release_blocked` and its tooltip.
For example, Give Final Authorization checks the release cost profile and then delegates the device transaction to its existing authorization/action chain.
Before/after affordability and probability acceptance remains pending in the dedicated release-cost audit.

`common/script_constants/023_sov_nuclear_bombs_constants.txt` defines the complete shared numeric vocabulary.

The evolution ladder is baseline 100, Evolution I 175 with a +75 increment and 2 reactors, Evolution II 275 with a +100 increment and 4 reactors, Evolution III 400 with a +125 increment and 6 reactors, and Evolution IV 600 with a +200 increment and 8 reactors.

The runtime helper only credits the caller-supplied incremental amount and stage receipt; reactor activation and progression gates remain parent-owned.

No MTTH, AI weight, Arms-race cluster, or periodic world loop is introduced by this file.

## Assets and localisation

This infrastructure adds no player-facing text, icons, GUI, report art, or localisation keys.

No sprite, `.gfx`, DDS, or asset-manifest entry is required for these helpers.

## Integration example

The Event 023 opening should set `sov_nuclear_bombs_registration_amount = constant:sov_nuclear_bombs_evolution.baseline` and call `sov_nuclear_bombs_register_event_owned_devices = yes` after the native stockpile grant.

Each registered site should set `sov_nuclear_bombs_site_registration_amount` to the site allocation and call `sov_nuclear_bombs_register_storage_site = yes` in the exact state scope.

An event-owned production batch should set `sov_nuclear_bombs_production_amount` and call `sov_nuclear_bombs_register_production_devices = yes` once from the Soviet country scope.

Each action should set its context, call `sov_nuclear_bombs_reserve_device_for_action = yes`, then call `sov_nuclear_bombs_execute_shared_action = yes`.

Cancellation, target invalidation, annexation, or side-change cleanup should call `sov_nuclear_bombs_clear_action_context = yes`.

## Future plans and suggestions

If a future engine/API surface exposes a reliable launch success receipt or nonce echo, replace the bounded one-pending-request correlation with that exact receipt without changing the ledger buckets.

The staged breakaway physical, technical, command, and delivery route already has source helpers and mission gates. Its timing, native delivery, one-device transaction, and save/reload behavior remain acceptance scenarios rather than a future helper request.

Failed tests, non-yield test accidents and demolition are the explicit non-detonating paths.
Accepted failed tests and non-yield accidents consume their reserved device synchronously, while demolition records its dismantled disposition.
No additional non-detonating profile is accepted without a shared contract boundary.

## Scratch lifetime and nested custody calculations

The reconciliation, opening-reactor, operationalization, transfer, rebind, return-delta, dismantlement and missing-disposition calculations use unscoped temporary variables.
Their owning operation initializes every scratch input before reading it, copies results into the existing country/state/global ledger, and leaves temporary expiration to the enclosing effect chain.
There is no supported `clear_temp_variable` effect, and `clear_variable` is not a substitute for temporary expiration.
Nested holder/owner scopes read these temporary amounts without `PREV.` prefixes.
The similarly named `global.sov_nuclear_bombs_soviet_usable_devices` is a persistent public output and remains distinct from reconciliation scratch.
No caller uses absence of the scratch values as an eligibility sentinel or reads them from a delayed event.
Exact identifier and caller evidence for the startup repair is recorded in `docs/testing/live_qa/20260913_main_menu_startup/script_targets_temp_references.txt` and `script_targets_temp_callers.txt`.
