# Reviewed archetype: The Reactor Shift

## Identity

The Reactor Shift is a first-season technate chain for the Manchurian Reactor Keeps memory in East Asia. It follows a closed Load Shedding state and tests whether an unsafe turbine roster can be negotiated, compelled, cooled, or staffed by a foreign team before the second winter.

The chain is an ordinary Fallout consequence-side chain. It is not the Fallout consequence, a world-end event, a super-event, or an evolution row.

## Candidate contract

- Candidate id `810`
- Transaction key `710087`
- Route `7206`
- Reserved upper bound `7207`
- Event Log history `9193`
- Opening events `chaosx.fallout.810` and `.811`
- Delayed result events `chaosx.fallout.812` and `.813`
- Callback events `chaosx.fallout.814` and `.815`
- Cleanup event `.816`
- State target only
- Region `east_asia`
- Government archetype `technate`
- Country memory `manchurian_reactor_keeps`
- Prior country memory `fallout_event_366_memory_closed`
- Prior state memory `fallout_event_803_memory_closed`
- Prior durable branches `fallout_load_shedding_hospital_priority_memory`, `fallout_load_shedding_food_priority_memory`, `fallout_load_shedding_industry_priority_memory`, and `fallout_load_shedding_defense_priority_memory`

The candidate producer initializes the safety, fatigue, trust, power, capacity, spare-parts, and safety-memory ledgers. It selects the lowest eligible owned state id and appends one scheduler row only after the country, state, Air Winter, Supply Access, building, population, controller, and foreign-neighbor receipts pass their current-generation checks.

## Opening choice

The player sees an East Asian reactor control hall after Load Shedding, with a turbine crew refusing an unsafe roster and a foreign team waiting behind the ash checkpoint.

1. Negotiate a safe roster spends Food 2, Medicine 3, and Recognition 2. It improves operator trust and safety legitimacy while reducing fatigue and power reserve.
2. Compel the duty roster spends Fuel 3, Recognition 1, and Cohesion 4. It can preserve output while increasing fatigue and reducing operator trust.
3. Cool the reactor and shut down spends Scrap 2, Power 4, and Medicine 2. It lowers exposure and disease pressure after a controlled reduction in supply.
4. Recruit a foreign team spends Food 2, Fuel 4, and Recognition 3. It can restore capacity and recognition while creating a durable bilateral inspection obligation.

Human and hidden AI openings use the same affordability checks, branch reservation, receipt authentication, delayed result scheduling, Event Log payloads, and cleanup ownership.

## State and country ledgers

The chain freezes Air Winter shelter, Supply Access, Adaptation, Exposure, Disease Pressure, population, owner, controller, generation, infrastructure evidence, and the lowest valid foreign neighbor.

Country ledgers are safety legitimacy, operator fatigue, operator trust, power reserve, operator capacity, spare parts, and safety memory. Result grading also includes Medicine, Recognition, Cohesion, the technate government bonus, and the live state receipt.

## Delayed results and callback

The result resolves after `35` days and applies Air Winter, Supply Access, Medicine, Recognition, Cohesion, Stability, War Support, one branch memory, one bilateral opinion, technical ledgers, and bounded Deaths failure. A failed result damages one native infrastructure level.

The first-winter callback resolves after `270` days and grades the live ledgers and the same state and neighbor receipts. It applies Air Winter and Supply Access changes, sends failure through the Deaths system, records the callback memory, and releases both delayed rows through idempotent cleanup.

## Event Log, assets, and cleanup

Choice, result, callback, and cancellation payloads use Event Log history `9193` and the dedicated scripted localisation `GetFalloutEvent810EventLogDetail`.

The report picture is `GFX_report_event_fallout_reactor_shift`, backed by `gfx/event_pictures/fallout/report_event_fallout_reactor_shift.dds` and the manifest under `docs/assets/810_reactor_shift/`.

Cleanup clears country and state reservations only after the delayed result and callback tickets are released. It writes the closed Reactor Shift state memory, retains durable branch flags, and does not delete tags, create countries, request Fallout, or register a public Fallout event.

## Deferred engine surfaces

Scheduler activation, host authority, save recovery, multiplayer delivery, and live Event Log presentation remain user-owned runtime checks. The exact native all-valid-province thermonuclear sweep remains a separate Fallout consequence blocker.
