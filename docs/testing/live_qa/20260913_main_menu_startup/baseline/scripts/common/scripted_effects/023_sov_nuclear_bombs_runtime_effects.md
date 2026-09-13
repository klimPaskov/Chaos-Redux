# Event 023 Soviet Nuclear Bombs Runtime Effects

This file is the reusable runtime boundary for Event 023's event-owned nuclear ledger and native delivery contract.

Event 023 owns authorization, action context, target selection, evolution gates, and player-facing decisions.

The shared contract in this file owns reservation, native `launch_nuke` invocation, and the single commit point for an accepted action.

The existing native `on_nuke_drop` route remains responsible for Chaos, deaths, contamination, Fallout, condemnation, and other detonation consequences.

No effect in this file calls `chaos_meter_on_nuke_drop` or a Fallout effect directly.

## Ledger model

The global ledger uses mutually exclusive intact buckets named `sov_nuclear_bombs_ledger_operational`, `sov_nuclear_bombs_ledger_assigned`, `sov_nuclear_bombs_ledger_reserved`, and `sov_nuclear_bombs_ledger_transferred`.

Terminal buckets are `sov_nuclear_bombs_ledger_dismantled`, `sov_nuclear_bombs_ledger_missing`, and `sov_nuclear_bombs_ledger_expended`.

The conservation equation is `total_registered = operational + assigned + reserved + transferred + dismantled + missing + expended`.

`sov_nuclear_bombs_refresh_ledger_reconciliation` recomputes physical custody and the accounted total after each transaction and stores `sov_nuclear_bombs_ledger_reconciliation` as clean or disputed.

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
| `sov_nuclear_bombs_release_reserved_device` | Country scope | Active reservation | Returns exactly one reserved device to its original operational or assigned bucket. |
| `sov_nuclear_bombs_commit_reserved_device` | Country scope | Active reservation after native launch or exact callback | Moves exactly one reserved device to expended or dismantled custody and stamps a transaction sequence. |
| `sov_nuclear_bombs_execute_shared_action` | Country scope | Valid Event 023 action context and active reservation | Invokes native `launch_nuke` with the exact state id and holds a detonation reservation until the callback confirms it; demolition commits synchronously. |
| `sov_nuclear_bombs_confirm_native_delivery` | Country scope | Event 023 pending native delivery after exact `on_nuke_drop` state checks | Records the native stockpile-after snapshot, commits exactly one reserved device, and marks the action accepted without applying detonation consequences. |
| `sov_nuclear_bombs_clear_action_context` | Country scope | Optional active reservation | Rolls back a live reservation and clears transient action context and target pointers. |
| `sov_nuclear_bombs_mark_site_transferred` | State scope | Registered storage site | Moves current intact site buckets into transferred custody without granting operational access. |
| `sov_nuclear_bombs_mark_site_dismantled` | State scope | Registered storage site | Moves all current intact site buckets into dismantled custody and marks the terminal state flag. |
| `sov_nuclear_bombs_mark_site_missing` | State scope | Registered storage site | Moves all current intact site buckets into missing custody and marks the terminal state flag. |
| `sov_nuclear_bombs_snapshot_event5_release_tranche` | Country scope | Existing `soviet_collapse_dynamic_release_target` event target | Takes one bounded pre-release snapshot across the candidate's owned/controlled registered storage states. |
| `sov_nuclear_bombs_snapshot_event5_state` | State scope | Registered state selected by the release tranche | Records all site buckets, custody state, owner, controller, and snapshot generation. |
| `sov_nuclear_bombs_reconcile_event5_state` | State scope | Pending Event 005 snapshot | Reads exact current owner/controller state, classifies custody, preserves non-operational status, and clears the pending flag. |
| `sov_nuclear_bombs_reconcile_event5_release_country` | Country scope | Event 005 release callback | Reconciles only pending registered states owned or controlled by the released country. |
| `sov_nuclear_bombs_cleanup_annexed_actor` | Country scope | Event 005 `on_annex` FROM scope | Rolls back a reservation, clears transient action context, and leaves the state ledger for state-level reconciliation. |

## Shared action contract

The parent must write the following country variables before calling `sov_nuclear_bombs_reserve_device_for_action` and `sov_nuclear_bombs_execute_shared_action`.

`sov_nuclear_bombs_action_actor_proven` must equal `constant:sov_nuclear_bombs_ledger.one`.

`sov_nuclear_bombs_action_authorized` must equal `constant:sov_nuclear_bombs_ledger.one`.

`sov_nuclear_bombs_action_type` must use one of the action constants `test`, `demonstration`, `combat_strike`, `accident`, or `demolition`.

`sov_nuclear_bombs_action_weapon` must equal `constant:sov_nuclear_bombs_action.nuclear_bomb`.

`sov_nuclear_bombs_action_route` must equal `constant:sov_nuclear_bombs_action.native_launch_nuke`.

`sov_nuclear_bombs_action_detonation` must equal `constant:sov_nuclear_bombs_action.detonation_required` for test, demonstration, accident, and strike actions, or `non_detonating` for demolition.

`sov_nuclear_bombs_action_nonce` must be strictly greater than the actor's recorded `sov_nuclear_bombs_last_action_nonce`.

`sov_nuclear_bombs_action_state` must point to the exact target state and `sov_nuclear_bombs_action_target` must point to its current owner or controller.

The validator requires `atomic_research`, `nukes`, a positive native `num_of_nukes` value for detonating actions, a valid target pointer, an exact selected state, a verified deployed bomber route, fuel, airbase access, and a non-terminal global state.

The accepted path issues exactly this native route: `launch_nuke = { state = var:sov_nuclear_bombs_action_state_id use_nuke = yes nuke_type = nuclear_bomb }`.

The adapter marks the launcher with a short-lived Event 023 atomic-delivery context before calling `launch_nuke`. The neutral Chaos consequence hook consumes that context to prevent an independently researched thermonuclear technology from changing this explicitly atomic action's consequence profile.

The native `on_nuke_drop` callback is the confirmation boundary. It must match the exclusive pending request's state id and selected owner/controller before calling `sov_nuclear_bombs_confirm_native_delivery`; the parent then calls `sov_nuclear_bombs_finalize_confirmed_native_delivery` to record the action and close its Event 023 flow.

Vanilla does not echo the Event 023 nonce, request id, or action type through `on_nuke_drop`. The bounded correlation therefore uses one pending request, the exact state id, the selected owner/controller, and the native stockpile snapshot. A future engine/API surface that exposes a nonce should replace this correlation with an exact receipt.

The parent must not add a second Chaos, Fallout, death, contamination, or condemnation call around this contract.

## Event 005 custody bridge

The bridge is activated only when Event 005 calls `sov_nuclear_bombs_snapshot_event5_release_tranche` immediately before its existing release operation.

The snapshot is restricted to registered states that are cores of the existing `soviet_collapse_dynamic_release_target` and is deduplicated by `sov_nuclear_bombs_event5_snapshot_pending`.

`on_release_as_free` and `on_release_as_puppet` call `sov_nuclear_bombs_reconcile_event5_release_country` for the new country.

`on_state_control_changed` calls `sov_nuclear_bombs_reconcile_event5_state` only for the exact changed state when its pending snapshot flag is present.

The bridge never turns a breakaway's physical custody into immediate technical, command, or delivery access.

The bridge records central Soviet, Soviet siege, breakaway physical, foreign, technical denial, missing, and dismantled classifications from exact current owner/controller facts.

If the engine does not expose a stable post-release callback for an ownership-only transfer, the pending snapshot remains available for the next exact state-control callback rather than being guessed from an unsupported scope.

## Constants

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

The parent can add an event-owned technical-access progression helper when the staged breakaway months and command thresholds are finalized in the Event 023 decision surface.

No additional non-detonating action profile is accepted without a shared contract boundary; Event 023's instrument-failure return and synchronous demolition are the only explicit non-detonating paths.
