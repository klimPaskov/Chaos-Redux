# Famine Foreign Relief Helpers

This package-owned helper set implements the famine-owned sparse, exact foreign-relief contract. It does not own migration cohorts, reception, border lifecycle, or corridor operations. It does not invent a donor, initialize reserve stock, infer vanilla sea or air pathfinding, mutate population, subtract pressure directly, create an event, add a GUI, add a mapmode, or scan the world on a recurring hook.

This is an implementation handoff for parent review, not a final system completion claim.

## Owned files and identifiers

| File | Identifiers |
| --- | --- |
| `common/script_constants/famine_relief_constants.txt` | `famine_relief_route_mode`, `famine_relief_result`, `famine_relief_pool.prob_relief_donor`, `famine_relief_endpoint`, `famine_relief_logistics`, `famine_relief_threshold`, `famine_relief_weight`, `famine_relief_timing` |
| `common/scripted_triggers/famine_relief_triggers.txt` | actor, donor registration/state, recipient, candidate availability, candidate route, selection relation, action route, route, contract, and delivery predicates |
| `common/scripted_effects/famine_relief_effects.txt` | registration, unregister, sparse selection, action-proof contract creation, exact delivery, war-corridor recording, and cleanup effects |
| External wiring | The recovered-state producer, famine decision consumers, mapmode, and player-facing text consume the famine-owned relief contract. |

The famine core reserve-transfer effect remains the sole physical reserve transfer owner. Its public definition is `famine_transfer_reserves` in `common/scripted_effects/famine_core_effects.txt` (with the narrow requisition alias `famine_requisition_reserves`).

## Producer census and stock ownership

The current external producer is the recovered-state retirement path, which supplies registration proof only after an initialized reserve and positive amount above `famine_relief_threshold.donor_reserve_floor`. It sets only `famine_relief_registration_proven` and `famine_relief_land_route_proven_input`; no producer initializes donor stock for relief.

After this tranche there is still exactly one registration producer. It supplies sea and air endpoint inputs only when the current source state has a positive, undamaged naval base or air base. The registration effect independently rechecks those live engine facts before persisting endpoint capability. The producer still never sets a sea or air route proof and never writes `famine_food_reserve_amount` or `famine_food_reserve_initial_amount`.

The smallest non-fabricated source path remains the normal food-reserve owner path: provide positive owner-proven initial stock or preserve an existing positive reserve, run `famine_refresh_reserve_capacity`, then register the exact recovered source state. A zero-stock row is retained sparsely but fails donor validity and contributes zero weight.

## Candidate pool and probability contract

`global.famine_relief_registered_donor_states` is the only source array. `famine_relief_select_donor` performs a bounded two-pass selection over that array and persists `famine_relief_donor_state`, `famine_relief_donor_country`, `famine_relief_actor`, and `famine_relief_selection_result` on the recipient state. No generic country, fabricated donor, or fallback row is admitted.

`famine_relief_donor_candidate_is_valid` is the declared `prob_relief_donor` row gate. It requires donor registration, initialized positive stock above floor, recipient free reserve headroom, requested amount, exact candidate route facts, and the same relation/tie/persecution/war-corridor legality used by the action. Every invalid registered row reaches neither the weight effect nor delivery and therefore has weight zero. Route and stock terms are bounded by the centralized weight constants; ideology is a bounded preference only, while persecution and an exact wartime corridor are explicit overrides.

The pre-contract route gate is `famine_relief_donor_candidate_route_is_valid`. Land requires the owner-proven land route capability. Sea requires both live undamaged naval endpoints, the registered donor sea endpoint capability, and the recipient's complete blockade proof. Air uses the corresponding undamaged air endpoints, donor air endpoint capability, and blockade proof. Sea and air do not require a generic route variable at selection time because the route is proven only after the exact donor is bound by the action.

## Endpoint and route truth

A functional undamaged naval base proves only that state-side sea endpoint. A functional undamaged air base proves only that state-side air endpoint. The registration producer and registration effect use `naval_base` or `air_base` plus `non_damaged_building_level`; a damaged or absent base is invalid at registration and again at selection and delivery.

Vanilla exposes no general trigger for an arbitrary distant sea-zone path or air route. Therefore ports, naval bases, air bases, infrastructure, and matching countries are not treated as paths. The action-owned route proof is `famine_relief_action_route_proven` on the recipient state. During contract creation, a short-lived `famine_relief_action_route_pending` marker permits the exact donor route predicate to recheck the selected donor, recipient, endpoints, relation or wartime corridor, and route mode. `famine_relief_action_route_inputs_are_valid` then requires actor-owned logistics: land convoys and fuel, sea convoys plus escort equipment and fuel, or transport planes plus air experience and fuel. Only then is the action proof persisted.

For sea and air, the route action also requires `famine_blockade_proof`, which includes live war, island/isolation/maritime dependence, disrupted route or port, convoy or escort shortage, no current humanitarian corridor, and insufficient local food. Thus an endpoint pair is never silently upgraded into a path. Delayed delivery rechecks the same donor, recipient, mode, owner/control, stock, endpoint, blockade, tie, and action proof; any lost proof fails closed.

The existing donor-side `famine_relief_sea_route_proven` and `famine_relief_air_route_proven` fields are reset and never used as generic route facts. Registration clears any transient route-input tokens. Sea and air route proof is recipient-local and action-owned, so one donor cannot accidentally grant a route to every recipient.

## Contract lifecycle

The four decision rows use the same lifecycle.

1. Player and AI visibility/targeting use the recipient candidate predicates. Candidate predicates include exact donor stock, relation/tie, mode endpoints, blockade/local inadequacy/no-current-relief for sea and air, and the mode's logistics floor. A zero pool is unavailable.
2. `complete_effect` sets the request and fixed action mode, selects one exact donor, persists the route proof and contract before subtracting any action cost, and subtracts costs only inside a `contract_is_valid` guard. A failed selection therefore never charges a cost. General relief uses the foreign-donor `famine_relief_select_donor` pool. The same-country safer-state requisition instead calls `famine_select_safe_food_reserve_donor`, which deterministically selects the adjacent safe state with the largest already existing positive reserve and returns `famine_requisition_donor_state`; it does not initialize untracked neighbors or substitute a foreign donor.
3. The timed contract stores donor state, donor country, actor, mode, request amount, generation/date, action proof, and the active state flag. It uses recipient-local scope-valued variables, not a shared global event target.
4. `remove_effect` for imports, convoy, and airlift calls `famine_relief_deliver_contract`. Delivery saves regular chain-local targets and invokes `famine_transfer_reserves` only after exact revalidation. The transfer helper debits the donor and credits the recipient, rolling residuals back and exposing measured debit and credit.
5. Relief access and recipient corridor proof are written only when the transfer result is valid, the measured debit equals measured credit, and the credit meets the minimum grant. `famine_mark_relief_access` remains the existing timed access effect; no pressure fraction is subtracted directly.
6. Failed delivery, stale endpoints, control loss, relation loss, depleted stock, insufficient headroom, or expiry runs idempotent cleanup and leaves relief access unchanged. Successful delivery clears only the active contract while preserving exact donor/mode/date history.

`famine_invite_relief` is intentionally land-only. It creates one exact land contract and leaves delivery to `famine_emergency_imports`; it no longer selects an impossible sea or air mode and no longer creates a cost-paid/no-contract fallback. `famine_emergency_imports` remains exact land donor-backed delivery. `famine_escorted_relief_convoy` and `famine_emergency_airlift` never call local reserve release; local release remains owned by `famine_release_reserves`.

## Cleanup and persistence

`famine_relief_clear_selection`, `famine_relief_clear_contract`, `famine_relief_cleanup_contract`, `famine_relief_cleanup_state`, `famine_relief_unregister_donor_state`, `famine_relief_clear_corridor_proof`, and `famine_relief_clear_war_corridor_proof` are safe to repeat. The exact donor pointer is a normal scope-valued recipient variable and survives save/reload without a shared global pointer collision. Existing bounded control-change, retirement, and registry callbacks can call these helpers for the exact affected state; no new recurring world scan is required.

## Canonical policy and acceptance

Persecution scoring and relation acceptance consume the migration-owned reception-policy contract as an external input. No relief helper creates or consumes a relief-specific migration policy flag.

The relationship gate accepts opinion, alliance, faction, subject, military-access, guarantee, or explicit humanitarian persecution override when not at war. War requires an exact donor-owned corridor proof for the same recipient, actor, and mode. Ideology only adjusts bounded probability weight and never overrides an invalid route, stock, relation, or capacity gate.

## Validation and blockers

Source review covered the current reserve initializer/refresh, `famine_transfer_reserves`, blockade proof, endpoint documentation, producer, four decision blocks, offline Paradox wiki pages, and vanilla `triggers_documentation.md`, `effects_documentation.md`, `script_concept_documentation.md`, and script-constant documentation. Targeted brace/operator checks were run on the touched script files; no live game was launched.

The installed probability route `hoi4_probability_inspect` was callable for source discovery. The required project probability subagent is currently unavailable because every spawn returned the service usage-limit response. The parent-owned same-scenario `prob_relief_donor` comparison remains an open completion gate. The pre-patch source artifact is retained as historical evidence:

```text
hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a5cdd4cab94abac47b886fa7856bd2224857cfa4269ec542bd76ee83e0/02548e937ad4e2e7b4cb21542c9623f8965bdca1aa751fa67e62aec41e5d2925/probability-inspect-be8bf65bfbdf.json
```

The engine blocker is explicit: vanilla arbitrary sea/air pathfinding is not observable from script. The action-owned endpoint-and-logistics corridor is the truthful bounded contract; if any owner cannot provide those exact facts, the row remains invalid instead of falling back to a generic route.

## Parent review and remaining wiring

Parent review should inspect the exact four famine decision rows and retain the existing phase/density gates and `cancel_if_not_visible` values. The parent owns final consumer validation and the probability comparison.

## Namespace and external boundary

The relief runtime is famine-owned and uses `famine_relief_*`. Its decision consumers are `famine_emergency_imports`, `famine_escorted_relief_convoy`, `famine_emergency_airlift`, `famine_invite_relief`, and `famine_release_reserves` in `common/decisions/famine_decisions.txt`.

The only migration input is the bounded, already-valid reception-policy contract used for persecution and admission precedence. Relief does not read migration load, migration routes, or migration lifecycle state.

The relief surface calls no `humanitarian_corridor_*` API. Its `famine_relief_*_corridor_*` fields are famine-owned delivery and wartime relief-route proofs.
