# Reviewed archetype: The Engineer Franchise

## Identity

The Engineer Franchise is a technate chain for the Manchurian Reactor Keeps memory. It begins after the Reactor Without a Country memory closes and selects one current East Asian state that still has a live Air Winter receipt, a power or industrial building, an external neighbor, and a surviving population.

The chain is an ordinary Fallout consequence-side chain. It is not the Fallout consequence, a world-end event, a super-event, or an evolution row.

## Candidate contract

- Candidate id `796`
- Transaction key `710085`
- Route `7202`
- Reserved upper bound `7203`
- Survivor Event Log history `9191`
- Opening events `chaosx.fallout.796` and `.797`
- Delayed result events `.798` and `.799`
- Callback events `.800` and `.801`
- Cleanup event `.802`
- State target only
- Region `east_asia`
- Government archetype `technate`
- Country memory `manchurian_reactor_keeps`
- Prior memory `fallout_event_366_memory_closed`

The candidate producer initializes the seven technical ledgers, selects the lowest eligible owned state id, and appends one scheduler row only after the country and state receipts pass their current-generation checks. The row remains dormant until the Fallout scheduler opens it.

## Opening choice

The player sees the reactor keep's turbine hall, public load register, civilian wards, and garrison at one constitutional table.

1. Engineer vote spends Food 2, Medicine 2, and Recognition 2. It favors a public technical mandate and repairs the power district when successful.
2. Public council spends Fuel 2, Recognition 3, and Cohesion 2. It gives households a formal vote while retaining an emergency maintenance register.
3. Military oversight spends Scrap 2, Power 2, and Medicine 2. It protects the switch rooms under garrison control and accepts a civilian review debt.
4. Universal vote spends Food 2, Fuel 2, and Recognition 2. It gives every surviving ward a binding vote over clinic and shelter power.

Human and hidden AI openings use the same affordability checks, branch reservation, receipt authentication, delayed result scheduling, and cleanup ownership.

## State and country ledgers

The chain freezes Air Winter shelter, Supply Access, Adaptation, Exposure, Disease Pressure, population, owner, controller, generation, infrastructure evidence, and the lowest valid foreign neighbor. Country ledgers are engineering legitimacy, class pressure, public trust, power budget, technician capacity, scrap reserve, and grid memory.

The result grades shelter, Supply Access, Adaptation, Disease Pressure, Exposure, Medicine, Recognition, engineering legitimacy, public trust, technician capacity, class pressure, and the technate government bonus. All seven technical ledgers contribute to the delayed callback grade.

## Delayed results and callback

The result resolves after `35` days. It changes Air Winter, Supply Access, Medicine, Recognition, Cohesion, Stability, War Support, technical ledgers, the selected government route, the authenticated state, bilateral opinion, and bounded Deaths failure. A failed result damages one native infrastructure level.

Successful Engineer Vote preserves the technate. Successful Public Council shifts the government archetype to continuity government. Successful Military Oversight shifts it to bunker authority. Successful Universal Vote preserves the technate while opening the universal charter memory. Government generation is updated from the current Fallout transition generation.

The first winter review resolves after `270` days. It grades the live technical ledgers and the same state receipts, applies Air Winter and Supply Access changes, sends failure through the Deaths system, records the callback memory, and releases both result and callback rows through idempotent cleanup.

## Event Log, assets, and cleanup

Choice, result, callback, and cancellation payloads use Event Log history `9191` and the dedicated scripted localisation `GetFalloutEvent796EventLogDetail`. The report picture is `GFX_report_event_fallout_engineer_franchise`, backed by the dedicated DDS and manifest under `docs/assets/796_engineer_franchise/`.

Cleanup clears the country and state reservations only after the delayed result and callback tickets are released. It is generation-bound and does not delete tags, create countries, request Fallout, or register a public Fallout event.

## Deferred engine surfaces

Scheduler release receipts, reviewed producers, and activation setters remain absent. The exact native all-valid-province thermonuclear sweep belongs to the completed Fallout consequence core.
