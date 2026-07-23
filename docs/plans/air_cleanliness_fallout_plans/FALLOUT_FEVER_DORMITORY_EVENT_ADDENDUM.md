# Fallout Fever Dormitory event addendum

## Scope

This tranche adds the dormant global `Fever Dormitory` family to the Fallout-owned candidate registry. It is a state-scoped disease and shelter crisis for the first winter year. It does not open the Fallout scheduler or claim release-floor credit.

The candidate is `256`, transaction key `710012`, route `7112`, and the event blocks are `256` through `268`. The chain has one human opening, one hidden AI opening, four delayed human results, four hidden AI results, one human callback, one hidden AI callback, and one cleanup event.

## Target contract

The producer selects the lowest owned state id that has a current identity row, a durable resource row, a produced Air Winter snapshot, shelter capacity at or above `20`, disease pressure at or above `35`, and more than `5` thousand people. The owning country must retain at least `8` Filters and `8` Food, have Medicine below `55`, and have enough stock for at least one policy. A committed state row is excluded until cleanup.

The opening freezes the state receipt and the current country ledgers. A fourteen-day delayed result and a one-hundred-twenty-day callback are scheduled through the existing delayed-result coordinator. Human and hidden AI lanes use the same transaction, target, branch, result, callback, and cleanup receipts.

## Policies and consequences

* Quarantine the dormitory spends filters, medicine, and food. It can reduce disease pressure and exposure while improving shelter discipline.
* Disperse the bunks spends food and recognition. It trades immediate crowding relief for a slower adaptation gain and a higher exposure risk.
* Treat in public spends medicine and shelter capacity. It preserves access to treatment but raises recognition pressure if the ward cannot be kept supplied.
* Conceal the fever spends scrap and recognition. It protects the public ledger briefly, then creates the largest delayed disease and casualty risk.

Each policy is scored against frozen shelter, adaptation, filters, medicine, and disease pressure values. Success, partial, and failure are deterministic. Failure requests civilian losses through `apply_exact_state_civilian_population_loss`, never by writing population directly. The callback applies a second state and ledger consequence, records memory, and releases both delayed receipts before the chain flags and state registry are cleared.

## Presentation and ownership

The event uses the dedicated `GFX_report_event_fallout_fever_dormitory` asset under `gfx/event_pictures/fallout_world_end/`. It does not use zombie identifiers, art, audio, sprites, or paths. The event log uses history id `9117` and fifteen payloads for the four policy outcomes and the callback outcomes.

## Review boundary

The family is statically wired and remains dormant. Scheduler activation, host-authority behavior, multiplayer ordering, and live GUI presentation remain runtime review surfaces. No HOI4 runtime was launched for this tranche.
