# Reviewed archetype: Load Shedding

## Identity

Load Shedding is a first-season technate chain for the Manchurian Reactor Keeps memory. It follows a closed Engineer Franchise district and reopens the same East Asian state only when its current owner, controller, Air Winter receipt, Supply Access receipt, population, power or industrial building, and foreign neighbor remain valid.

The chain is an ordinary Fallout consequence-side chain. It is not the Fallout consequence, a world-end event, a super-event, or an evolution row.

## Candidate contract

- Candidate id `803`
- Transaction key `710086`
- Route `7204`
- Reserved upper bound `7205`
- Event Log history `9192`
- Opening events `chaosx.fallout.803` and `.804`
- Delayed result events `chaosx.fallout.805` and `.806`
- Callback events `chaosx.fallout.807` and `.808`
- Cleanup event `.809`
- State target only
- Region `east_asia`
- Government archetype `technate`
- Country memory `manchurian_reactor_keeps`
- Prior country memory `fallout_event_366_memory_closed`
- Prior state memory `fallout_event_796_memory_closed`

The candidate producer initializes the load, sector, power, technician, scrap, and grid ledgers, selects the lowest eligible state id, and appends one scheduler row only after the country and state receipts pass their current-generation checks. The row remains dormant until the Fallout scheduler opens it.

## Opening choice

The player sees the reactor keep's hospital ward, food depots, repair halls, and perimeter sharing one turbine circuit during the first ash season.

1. Hospital priority spends Food 1, Medicine 4, and Recognition 1. It protects sterilizers and oxygen pumps while consuming the grid reserve.
2. Food priority spends Fuel 2, Recognition 2, and Cohesion 3. It keeps cold rooms and ration scales operating while the public queue absorbs the cut.
3. Industry priority spends Scrap 3, Power 3, and Medicine 1. It runs a crane, lathe, and salvage press while technician capacity and scrap stores carry the risk.
4. Defense priority spends Food 2, Fuel 3, and Recognition 2. It keeps the patrol road, radio mast, and gate sensors live while the reserve and technical roster shrink.

Human and hidden AI openings use the same affordability checks, branch reservation, receipt authentication, delayed result scheduling, and cleanup ownership.

## State and country ledgers

The chain freezes Air Winter shelter, Supply Access, Adaptation, Exposure, Disease Pressure, population, owner, controller, generation, infrastructure evidence, and the lowest valid foreign neighbor. Country ledgers are load legitimacy, sector pressure, sector trust, power reserve, technician capacity, scrap reserve, and grid memory.

The result grades shelter, Supply Access, Adaptation, Disease Pressure, Exposure, Medicine, Recognition, load legitimacy, sector trust, technician capacity, sector pressure, and the technate government bonus. The callback grades every load and material ledger as well as the same state receipt.

## Delayed results and callback

The result resolves after `28` days. It changes Air Winter, Supply Access, Medicine, Recognition, Cohesion, Stability, War Support, the selected sector memory, bilateral opinion, technical ledgers, and bounded Deaths failure. A failed result damages one native infrastructure level.

The first-winter review resolves after `240` days. It grades the live ledgers and the same state receipts, applies Air Winter and Supply Access changes, sends failure through the Deaths system, records the callback memory, and releases both result and callback rows through idempotent cleanup.

## Event Log, assets, and cleanup

Choice, result, callback, and cancellation payloads use Event Log history `9192` and the dedicated scripted localisation `GetFalloutEvent803EventLogDetail`. The report picture is `GFX_report_event_fallout_load_shedding`, backed by the dedicated DDS and manifest under `docs/assets/803_load_shedding/`.

Cleanup clears the country and state reservations only after the delayed result and callback tickets are released. It writes the closed Load Shedding state memory, retains the durable sector memory, and does not delete tags, create countries, request Fallout, or register a public Fallout event.

## Deferred engine surfaces

Scheduler release receipts, reviewed producers, and activation setters remain absent. The exact native all-valid-province thermonuclear sweep belongs to the completed Fallout consequence core.
