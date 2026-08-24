# Famine Migration Foreign Relief Helpers

This package-owned helper set implements the exact foreign-relief donor contract without inventing a donor, reserve stock, route, event, GUI, mapmode, or recurring world scan.

This is an implementation handoff, not a completion claim.

## Files and source contract

The implementation is split across these package-owned files.

| File | Contents |
| --- | --- |
| `common/script_constants/famine_migration_relief_constants.txt` | Route modes, `prob_relief_donor` pool id, result ids, thresholds, bounded weights, and contract timing. |
| `common/scripted_triggers/famine_migration_relief_triggers.txt` | Fail-closed actor, donor-row, recipient, route, candidate, contract, and delivery predicates. |
| `common/scripted_effects/famine_migration_relief_effects.txt` | Sparse registration, selection, contract creation, exact delivery, corridor recording, and idempotent cleanup. |
| `common/scripted_effects/famine_migration_relief_effects.md` | This identifier, scope, input, output, side-effect, owner-wiring, and blocker handoff. |

The existing reserve API remains the only reserve mutation owner: `famine_migration_transfer_food_reserves` in `common/scripted_effects/chaosx_famine_migration_effects.txt`.

## No fabricated donor or initial stock

The current famine package has no producer that initializes positive donor stock specifically for foreign relief.

`famine_migration_refresh_food_reserve_capacity` may initialize a state only from owner-proven positive `famine_migration_food_reserve_initial_amount` and `famine_migration_food_reserve_initialization_proven`, or preserve a positive amount already present; it does not promote zero to stock.

The relief registration effect never calls the initializer, never writes `famine_migration_food_reserve_amount`, and never writes `famine_migration_food_reserve_initial_amount`.

The smallest non-fabricated owner path is: establish the normal reserve ledger with the existing initializer's owner proof, call `famine_migration_refresh_food_reserve_capacity`, set transient `famine_migration_relief_registration_proven` and the route-proof inputs from a real owner callback, then call `famine_migration_relief_register_donor_state` in that exact source state.

A registered zero-stock row is retained as a sparse row but fails `famine_migration_relief_donor_state_is_valid` and contributes exactly zero weight until an owner-owned replenishment path produces positive stock.

## Identifier map

### Constants

`famine_migration_relief_route_mode.land`, `.sea`, and `.air` are the only route modes.

`famine_migration_relief_pool.prob_relief_donor` names the declared weighted surface.

`famine_migration_relief_result.invalid`, `.valid`, `.no_candidate`, `.delivered`, and `.partial` are result values.

`famine_migration_relief_runtime.zero`, `.one`, `.roll_minimum`, and `.roll_maximum` are runtime values.

`famine_migration_relief_threshold.*` owns donor floor, minimum grant, reserve capacity, infrastructure, opinion, stock-step, stock-cap, headroom-step, and headroom-cap values.

`famine_migration_relief_weight.*` owns the positive base, route, tie, ideology, override, and final clamp values.

`famine_migration_relief_timing.contract_expiry_days` and `.corridor_proof_days` own timed lifecycle durations.

### Triggers

All triggers are read-only and fail closed.

| Identifier | Scope and contract |
| --- | --- |
| `famine_migration_relief_actor_is_valid` | `COUNTRY`; validates the decision actor scope. |
| `famine_migration_relief_donor_registration_is_valid` | `STATE`; requires an existing owned and controlled reserve ledger, positive capacity, and transient owner registration proof. It does not require positive stock and never initializes stock. |
| `famine_migration_relief_donor_state_is_valid` | `STATE`; requires registered state, initialized reserve variables, positive stock above the donor floor, positive capacity, live owner, and owner control. |
| `famine_migration_relief_recipient_is_valid` | `STATE`; requires active food security, initialized reserve variables, positive capacity, and free headroom. |
| `famine_migration_relief_route_mode_is_valid` | `STATE`; accepts only the three declared route modes. |
| `famine_migration_relief_donor_route_is_valid` | Registered donor `STATE`; rechecks recipient and actor targets, ownership, infrastructure, relation or tie, persecution policy, war corridor proof, and route-mode facts. |
| `famine_migration_relief_donor_candidate_is_valid` | Registered donor `STATE`; combines route, request amount, destination headroom, and donor post-floor stock gates. Invalid rows never reach weighting. |
| `famine_migration_relief_contract_is_valid` | Recipient `STATE`; validates the persisted donor state/country, actor, route mode, amount, and active contract flag. |
| `famine_migration_relief_delivery_is_valid` | Recipient `STATE`; revalidates the exact persisted identities and donor route immediately before the reserve transfer. |

### Effects

| Identifier | Scope and inputs | Outputs and side effects |
| --- | --- | --- |
| `famine_migration_relief_register_donor_state` | Source `STATE`; transient registration and route-proof inputs listed below. | Adds the exact state to `global.famine_migration_relief_registered_donor_states` once, updates the count, stores route proofs, and returns temporary `famine_migration_relief_registration_result`. It never creates stock. |
| `famine_migration_relief_unregister_donor_state` | Source `STATE`; no input. | Removes only the exact source from the sparse array, clears registration and route proofs, and clears its war-corridor proof. Safe to repeat. |
| `famine_migration_relief_donor_candidate_weight` | Donor `STATE` with selection aliases saved. | Returns temporary non-negative `famine_migration_relief_donor_candidate_weight`; it starts at zero for every invalid row and applies only bounded route, tie, ideology, policy, war, stock, and headroom terms after the candidate trigger passes. |
| `famine_migration_relief_select_donor` | Recipient `STATE`; `ROOT` is actor, `famine_migration_relief_route_mode` and `famine_migration_relief_requested_amount` are set by the owner. | Iterates only the registered sparse array, performs a two-pass weighted selection, persists `famine_migration_relief_donor_state`, `famine_migration_relief_donor_country`, `famine_migration_relief_actor`, and `famine_migration_relief_selection_result`, and returns no-candidate when the complete registered pool totals zero. |
| `famine_migration_relief_create_contract` | Recipient `STATE`; a valid persisted selection, route mode, request amount, and `ROOT` actor. | Rechecks the selected route and sets the recipient-local active contract flag, amount, actor, date, and generation. It does not move reserves or mark access. |
| `famine_migration_relief_deliver_contract` | Recipient `STATE`; the persisted contract and `ROOT` actor. | Copies the exact donor state and recipient into regular event targets, calls `famine_migration_transfer_food_reserves`, and records measured debit/credit. It calls `famine_migration_mark_relief_access` and writes delivery/corridor proof only when transfer result is valid, debit equals credit, and credit meets the minimum grant. |
| `famine_migration_relief_record_war_corridor` | Donor endpoint `STATE`; owner supplies recipient and actor event targets, route mode, and positive acceptance proof. | Persists a donor-owned corridor proof for the exact recipient, actor, and mode. No route is inferred from war or endpoints alone. |
| `famine_migration_relief_clear_contract` | Recipient `STATE`; no input. | Clears active contract, persisted donor/country/actor/amount/date/generation/request/selection fields while preserving successful delivery history. Safe to repeat. |
| `famine_migration_relief_clear_corridor_proof` | Recipient `STATE`; no input. | Clears recipient delivery/corridor flags and donor/mode/date history. It does not directly clear timed `famine_migration_relief_access_active`. |
| `famine_migration_relief_clear_war_corridor_proof` | Donor `STATE`; no input. | Clears donor war-corridor flags and identity fields. Safe to repeat. |
| `famine_migration_relief_cleanup_contract` | Recipient `STATE`; no input. | Idempotent alias for contract cleanup. |
| `famine_migration_relief_cleanup_state` | Recipient `STATE`; no input. | Clears contract and recipient corridor proof. Owner callbacks should call it for stale or invalidated recipient state. |

## Transient owner inputs

The registration caller must set these positive proof variables on the source state before invoking `famine_migration_relief_register_donor_state`.

`famine_migration_relief_registration_proven` is the explicit registration authorization.

`famine_migration_relief_land_route_proven_input` is the owner-proven land endpoint fact.

`famine_migration_relief_sea_endpoint_proven_input` and `famine_migration_relief_sea_route_proven_input` are both required for sea delivery.

`famine_migration_relief_air_endpoint_proven_input` and `famine_migration_relief_air_route_proven_input` are both required for air delivery.

The effect copies those proofs to persistent source-state variables and clears the transient inputs. A missing proof is zero.

For a recipient requesting sea or air delivery, the owner must also set recipient-state `famine_migration_relief_recipient_sea_endpoint_proven` or `famine_migration_relief_recipient_air_endpoint_proven` from the same exact endpoint contract.

Ports, naval bases, air bases, and infrastructure are inspected engine facts used as additional gates; they are not path proofs by themselves.

## Contract lifecycle and conservation

The owner sets route mode and requested amount on the recipient state before selection.

`famine_migration_relief_select_donor` saves regular event targets only during the current effect chain and persists the selected source/country as normal scope-valued recipient variables.

`famine_migration_relief_create_contract` creates one recipient-local timed contract without a global pending pointer, so concurrent recipients do not overwrite one another.

Delivery saves the persisted source as `famine_migration_relief_delivery_donor_state`, the persisted donor country as `famine_migration_relief_delivery_donor_country`, and the current recipient as `famine_migration_food_reserve_destination`.

The source calls `famine_migration_transfer_food_reserves` with positive request, route, and actor proof inputs. The source is debited and the recipient is credited by the shared helper's measured outputs, with its existing rollback behavior.

No pressure, population, manpower, cohort, or death-ledger mutation is performed by this package.

Failed selection, stale route, control loss, depleted stock, exhausted capacity, invalid transfer, or contract expiry clears the contract and leaves relief access unchanged.

After exact successful transfer, the recipient stores `famine_migration_relief_last_delivery_debit`, `famine_migration_relief_last_delivery_credit`, `famine_migration_relief_corridor_donor_state`, `famine_migration_relief_corridor_donor_country`, `famine_migration_relief_corridor_mode`, and `famine_migration_relief_corridor_proof_date`.

The recipient then receives the existing timed `famine_migration_relief_access_active` mark and a separate exact delivery/corridor proof; access is never granted at invitation or selection time.

## Required parent wiring

The parent must edit these gameplay files after reviewing this handoff.

| File | Required owner work |
| --- | --- |
| `common/decisions/famine_migration_decisions.txt` | Set request amount and route mode, use the same candidate gate for player availability/targeting and AI, call selection/contract on invitation, call delivery for imports/convoy/airlift, remove flat pressure subtraction, and keep `fm_release_reserves` as the only local release path. |
| Existing reserve owner callbacks in `common/scripted_effects/chaosx_famine_migration_effects.txt` or their package-owned call sites | After normal owner-proven reserve initialization and route proof, register or unregister exact source states. Do not add a daily/weekly/monthly world scan. |
| Existing route, control, war, peace, annexation, retirement, and expiry callbacks | Clear or unregister only the exact affected contract, source row, and corridor proof by calling the cleanup helpers. |
| Owner route/corridor action | Set `famine_migration_relief_corridor_recipient_target`, `famine_migration_relief_corridor_actor_target`, `famine_migration_relief_corridor_mode`, and positive `famine_migration_relief_corridor_acceptance_proven` before calling `famine_migration_relief_record_war_corridor`. |
| Localisation and system/spec docs | Describe donor/source identity, route, contract, stock/capacity failure, exact delivery, partial result, and corridor proof in the parent-owned localisation and documentation files. |

For `fm_invite_relief`, acceptance must create only a real donor contract and diplomatic outcome.

For `fm_emergency_imports`, `fm_escorted_relief_convoy`, and `fm_emergency_airlift`, delivery must debit the persisted foreign source and credit the recipient through the exact transfer helper.

Convoy and airlift rows remain unavailable when the owner cannot supply explicit source and recipient endpoint/route proof.

## Blockers and validation boundary

The installed tool list exposed `hoi4.probability_inspect` and related probability tools, but no callable `chaosx_ai_probability_auditor` route was available, so the mandatory auditor evidence pass and the full twenty-scenario `prob_relief_donor` compare remain blocked for the parent owner.

The probability source-discovery artifact for the existing famine decision source was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a5cdd4cab94abac47b886fa7856bd2224857cfa4269ec542bd76ee83ab5ef8e0/02548e937ad4e2e7b4cb21542c9623f8965bdca1aa751fa67e62aec41e5d2925/probability-inspect-be8bf65bfbdf.json`.

The inspected vanilla trigger/effect documentation exposes ownership, control, adjacency, ports, air bases, relations, ties, war, and event targets, but no general trigger that proves an arbitrary distant sea-zone path or air route.

Therefore sea and air candidate rows intentionally require the mod-owned endpoint and route proof variables in addition to naval-base or air-base facts.

No decision call site, localisation, on-action, event, GUI, mapmode, spreadsheet, or live game validation was changed in this package tranche.

Task-specific source review covered the existing reserve initializer/refresh, exact reserve transfer, relief-access marker, destination selector, and the four named famine decisions before implementation.
