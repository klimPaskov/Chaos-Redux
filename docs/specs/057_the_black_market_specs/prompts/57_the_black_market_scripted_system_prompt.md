# Event 57 Scripted-System Architecture Prompt

Design and implement the reusable Event 57 scripted architecture from:

- `docs/specs/057_the_black_market_specs/01_core_event_spec.md`
- `docs/specs/057_the_black_market_specs/02_membership_secrecy_and_government_postures.md`
- `docs/specs/057_the_black_market_specs/03_smuggling_routes_and_network_growth.md`
- `docs/specs/057_the_black_market_specs/04_inventory_trade_and_provider_api.md`
- `docs/specs/057_the_black_market_specs/07_ai_probability_balance_and_edge_cases.md`

Follow the current repository versions of `AGENTS.md`, `chaos-redux-events`, `chaos-redux-subagents`, the shared dynamic-effect and trigger registries, the offline wiki, vanilla documentation, and current Chaos Redux patterns.

Use `chaosx_scripted_system_architect` for the bounded architecture work. The parent retains final event, decision, localisation, asset, workbook, and completion ownership.


Spawn every project subagent with a complete self-contained prompt and `fork_context=false`.

## Required registries

Use `uses_normal_civilian_systems = yes` and exclude `is_special_chaos_country = yes` in the ordinary participant trigger. Allow a special human actor only through an explicit owner adapter.

Create sparse event-owned registries for:

- candidate, invited, active, dormant, suspended, former, and expelled members
- active, disrupted, compromised, and burned routes
- regional cells
- inventory offers
- active deliveries
- outsider evidence cases
- provider packages
- recent imports
- completed transaction and milestone receipts

Use stable IDs, aligned arrays or another verified repository pattern, explicit bounds, and cleanup.

## State machines

Implement idempotent state transitions for membership, routes, offers, and transactions.

Transaction states must cover generated, available, reserved, source debit pending, dispatched, delayed, partial, settled, seized, canceled, and invalidated.

A repeated call after save and reload must return the existing result or a safe reject reason. It must never repeat a debit, grant, credit movement, Chaos milestone, or achievement receipt.

## Public values

Implement country Market Credit and Exposure plus global Network Reach.

Centralize all floors, caps, bands, gains, losses, and durations. Provide concise scripted-localisation accessors and fail-closed setters.

Do not expose hidden trust, route pressure, capacity, reliability, provider proofs, or candidate scores as extra public values.

## Route API

Create helpers for:

- endpoint validation
- route creation
- route lookup
- status refresh
- capacity class
- risk class
- route selection
- route pressure
- regional-cell rebuild
- route burn and cleanup

Refresh only affected route records after world changes. Do not create a broad recurring world scan.

## Offer and transaction API

Create helpers for:

- demand registration from active members
- bounded offer generation
- source proof
- buyer validity
- reservation
- source debit
- dispatch
- delivery outcome
- settlement
- recent-import lock
- expiration
- cancellation

Reuse existing shared stockpile debit helpers when their contracts fit. Add a neutral shared helper only when several systems genuinely need it and update the matching dynamic-effect documentation in the same change.

## Provider API

Create owner files and permanent documentation for the versioned provider request and receipt contract.

Require:

- provider ID
- package ID
- offer class
- minimum evolution
- availability trigger
- buyer trigger
- source debit
- delivery effect
- quantity and price rules
- route rule
- Exposure rule
- reveal rule
- completion isolation
- DLC rule
- cleanup rule

Missing proof returns a stable reject reason and queues no offer.

An owner package remains owned by its source event. Event 57 must not set its completion flags, read its private ledger, or infer stock that was never published.

## Pulse architecture

Use one bounded event-owned scheduler for:

- inventory rotation
- invitation attempt
- registered Exposure recovery
- route-pressure recovery
- dormancy reconstruction
- evolution MTTH checks

Each pulse iterates only registered arrays or one bounded candidate sample. Do not add a whole-world daily, weekly, or monthly on-action.

Use narrow on-action adapters only when a relevant country, state, war, embargo, annexation, capitulation, route, or provider fact changes.

## Tuning

Place shared Event 57 tuning in `common/script_constants/057_the_black_market_constants.txt` where supported.

Centralize founder counts, slot caps, cadence, route limits, Exposure bands, Reach thresholds, price factors, reserve factors, handling classes, auction timing, recent-import lock, evolution MTTH, AI anchors, and Chaos values.

## Evidence and handoff

List every created helper, trigger, constant group, array, event target, state transition, call site, and public input or output in the handoff.

Document request proofs, reject reasons, default behavior, cleanup, and save safety.

Run source-level tests for duplicate IDs, array alignment, state transitions, one-time receipts, invalid scopes, missing cleanup, and public input reset.

Do not invent a generic global trade framework beyond what Event 57 and declared providers need.
