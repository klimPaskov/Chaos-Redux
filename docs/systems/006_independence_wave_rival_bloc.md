# Event 006 rival bloc contract

The rival bloc is the concrete post-expulsion branch of the Event 006 league. It is a separate registry contract, not a second vanilla faction and not a cosmetic phase flag. The main Event 006 network remains the shared pool of independent countries; the rival contract owns its own generation, member rows, leader target, values, invitation lock, and action history.

## Contract state

Global values are stored under `global.independence_wave_rival_bloc_*`:

- `contract_generation`, `route`, `cohesion`, `common_cause`, `patron_capture`, `shared_reserve`, `member_confidence`, `host_pressure`, `member_count`, `region_count`, `contract_open_date`, and `last_action_date`.
- `independence_wave_rival_bloc_leader` is the scope-valued leader pointer; `independence_wave_rival_bloc_leader_target` is its durable event target.
- `independence_wave_rival_bloc_active`, `independence_wave_rival_bloc_league_rivalry_active`, and `independence_wave_rival_bloc_invitation_open` are contract flags. The invitation target is held by `independence_wave_rival_bloc_pending_invitation_target` and is always cleared on acceptance, decline, cancellation, origin cleanup, or dissolution.

Member rows are parallel and generation-checked:

`member_country_entries`, `member_generation_entries`, `member_contract_generation_entries`, `member_region_entries`, `member_contribution_entries`, and `member_confidence_entries`.

## Helper map

| Helper | Scope and inputs | Outputs and side effects | Call sites |
| --- | --- | --- | --- |
| `independence_wave_rival_bloc_initialize_runtime` | Any scope; no inputs | Seeds missing global counters and value variables without resetting an active contract | All rival effects before a read/write |
| `independence_wave_rival_bloc_change_values` | Any scope; temporary six `*_delta` values | Applies and clamps cohesion, common cause, patron capture, reserve, confidence, and host pressure | Expulsion opening, acceptance, reserve, host, patron, leadership, leave |
| `independence_wave_rival_bloc_reconcile_registry` | Any scope; current contract arrays | Reverse-prunes dead countries, stale origin generations, stale contract generations, and missing member flags; rebuilds regions and confidence | Explicitly available to later audits; register/unregister call the rebuild routines |
| `independence_wave_rival_bloc_register_member` | Country scope; current network member, no main-league/client/rival membership | Appends one aligned row with current origin and contract generations and member confidence | Expelled origin opening, invitation acceptance, reunification |
| `independence_wave_rival_bloc_unregister_member` | Country scope; rival member flag | Removes every aligned row, clears member/host/patron/invitation flags, selects a replacement leader, and dissolves an empty contract | Leave action, origin cleanup, reunification |
| `independence_wave_rival_bloc_open_after_expulsion` | Expelled active origin with network membership and discredited flag | Starts a new contract generation, derives route from the main league route, applies main-league losses, enters crisis/split transition, registers the expelled origin, and records host/patron pressure | End of `independence_wave_expel_league_member` |
| `independence_wave_rival_bloc_issue_invitation` | Leader scope with `active_target_country` pointer | Opens one generation-locked invitation and stores the target pointer for cleanup | Targeted invitation decision timeout |
| `independence_wave_rival_bloc_accept_invitation` / `...decline_invitation` | Pending target scope | Clears invitation pointers; acceptance registers the target and raises confidence; decline records a confidence loss | Accept/decline decisions |
| `independence_wave_rival_bloc_commit_reserve` / `...fail_reserve` | Member scope after a timed mission | Adds/removes reserve and shared values after paid equipment/trains/fuel commitment | Reserve mission timeout/cancellation |
| `independence_wave_rival_bloc_coordinate_host` | Host-front member with a living former host | Applies the existing bilateral host ledger delta and lowers bloc host pressure after a paid front action | Host-front decision |
| `independence_wave_rival_bloc_balance_patron` | Patron-pressure member | Clears the pressure marker, lowers bloc patron capture, and refreshes the country patron ledger after a paid balancing action | Patron balancing decision |
| `independence_wave_rival_bloc_challenge_leadership` | Non-leader member meeting confidence gate | Moves durable leader target/flag and commits cohesion/confidence changes | Leadership mission timeout |
| `independence_wave_rival_bloc_leave` | Rival member | Applies departure losses and unregisters the country while preserving network membership | Leave decision |
| `independence_wave_rival_bloc_dissolve_contract` | Active contract | Clears pending target, member rows, leader target, contract values, and rival flags; returns the main phase to formal league or informal network when appropriate | Empty-contract cleanup and explicit reunification |
| `independence_wave_rival_bloc_cleanup_for_origin` | Any Event 006 origin cleanup scope | Leaves a rival member or cancels a pending invitation without touching network/origin history | Network unregister and origin end |
| `independence_wave_rival_bloc_reunify_into_league` | Main league after phase moves to formal | Copies rival members before row mutation, unregisters rival membership, and registers eligible countries into the main league | `independence_wave_reunify_rival_leagues` |

## Constants and tuning

`common/script_constants/006_independence_wave_rival_bloc_constants.txt` owns the shared tuning tables:

- `independence_wave_rival_bloc`: value bounds, opening values, gates, and per-action consequences.
- `independence_wave_rival_bloc_route`: grievance caucus, counter-league, and patron-balanced routes.
- `independence_wave_rival_bloc_duration`: invitation, acceptance, reserve, leadership, patron, and host timers.
- `independence_wave_rival_bloc_cost`: command power, equipment, convoy, train, fuel, and Army Experience commitments.
- `independence_wave_rival_bloc_ai`: decision weights and production priorities.

The decision layer owns payment. Effects do not check for the already-spent resources again at timeout; they only revalidate the live member/contract state before applying the result.

## Lifecycle and interaction rules

1. DM-60 removes the factual-ground member and leaves it in the Event 006 network. The expulsion helper opens the rival contract and marks the main league crisis/split transition as pending for that transaction.
2. The expelled origin is the initial rival leader. It retains its former-host and patron ledgers; the bloc records host pressure and patron capture rather than silently erasing those relationships.
3. The leader can invite one network country at a time. The target must accept explicitly. Main-league members, founders, clients, stale generations, and countries below the network-standing gate cannot be invited.
4. Members spend real stockpiles to build a reserve, coordinate the former-host front, balance patron capture, or challenge leadership. Each action changes visible contract values and may fail or be cancelled when the member disappears.
5. Leaving removes only rival membership and preserves network/origin history. A vanished leader is replaced by the highest-confidence surviving member; an empty contract dissolves and clears every event target.
6. Main-league registration and founder reconciliation reject rival members, preventing duplicate membership rows. Reunification copies rival members before mutation, then registers eligible countries into the formal main league.

## Validation notes and limitations

Source audits cover balanced braces, helper-reference resolution, constant-reference coverage, absence of broad on-actions, and BOM encoding for the new localisation. The offline wiki and vanilla documentation were used for arrays, event targets, targeted decisions, mission timeout/cancel effects, stockpile costs, and scripted localisation.

The bloc intentionally uses a registry rather than a vanilla faction because the accepted Event 006 league already exposes registry values and generation-safe event-detail surfaces. No GUI rewrite, map rewrite, automatic world scan, or new visual asset was added. A later GUI surface can consume the global value names and member arrays without changing the contract API.
