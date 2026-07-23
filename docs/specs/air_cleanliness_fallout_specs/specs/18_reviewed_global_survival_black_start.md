# Reviewed Fallout Global Survival Pilot: Black Start

## Purpose

Black Start is a dormant country-level recovery chain for the second and third
generation after the Fallout transition. It asks who controls the first working
electrical circuit after the shelters have become settlements. It is not a
super-event and it does not perform the thermonuclear transition. Its report
picture is dedicated to this chain.

## Entry contract

The candidate producer defines candidate `310`, transaction key `710018`, and
route `7118`. The gate requires the current country registry and identity rows,
a durable resource row, a closed Shelter Marriage Law memory, at least two
generation changes, campaign day `900` through `2000`, Power `25`, Scrap `25`,
Cohesion `30`, Recognition `25`, Reclamation `20`, and one affordable branch.
The scheduler must provide the ordinary receipt before the opening event. The
opening target is the current country and the target type is `none`.

The chain freezes Power, Scrap, Cohesion, Recognition, Reclamation, and five
durable grid ledgers before it schedules a result. This prevents mid-chain
resource drift from changing the recorded policy outcome.

## Branches and results

| Branch | Immediate question | Durable identity |
| --- | --- | --- |
| Centralized grid | Can one guarded control room answer for the network? | Capacity and governance with lower dependency |
| Local cooperatives | Can neighborhood crews share switching authority? | Resilience and cohesion with uneven reach |
| Military grid | Can a garrison secure fuel and maintenance? | Capacity and readiness with political pressure |
| Foreign-backed | Can an outside partner supply compatible relays? | Fast capacity with Recognition cost and dependency |

Each branch grades the frozen Power, Scrap, Cohesion, and Recognition values into
success, partial, or failure. Results update resources, Cohesion, Stability, War
Support, capacity, governance, dependency, resilience, and exposure. Failure
requests population loss through the Deaths contract. A successful or partial
result opens a 270-day maintenance callback. The callback has its own success,
partial, and failure deltas and closes the memory after authenticated cleanup.

## AI, memory, and cleanup

Hidden AI uses a deterministic priority ladder. It first repairs a missing or
weak governance ledger through the central branch, then prefers cooperative
capacity when Cohesion is high, military security when Power is high, and an
outside partner when Recognition is high. Every delayed result and callback
uses the same transaction coordinator, registry generation, event token, mode,
branch, due day, and cleanup token as the human path.

The result records one of twelve branch and outcome payloads under history
`9123`. The callback records one of three maintenance payloads. Cleanup releases
the exact result and callback receipts, clears transient registry and frozen
values, and retains only the durable grid ledgers, policy, memory flags, and
timed modifiers.

## Presentation and wiring

The source event file is `events/fallout_world_end_events.txt` under
`add_namespace = chaosx.fallout`. Events `310` through `316` provide the human
opening, hidden AI opening, human and hidden AI result, human and hidden AI
callback, and authenticated cleanup. Localisation is in
`localisation/english/fallout_world_end_black_start_l_english.yml` with a BOM.
The dedicated report sprite is registered as
`GFX_report_event_fallout_black_start` in `interface/fallout_world_end.gfx`.

## Review status

This is a reviewed dormant pilot. It is not counted toward the 660-block
release floor because activation, host authority, save recovery, multiplayer
delivery, and runtime Event Log delivery were not observed. The read-only
`hoi4.event_inspect` lint request for `chaosx.fallout.310` returned `Transport
closed`, so the engine-side graph remains an explicit blocker rather than a
claim of proof.

## Future extension

The next expansion should connect a surviving grid policy to a named regional
partner, a supply route, and a country-specific focus overlay. Those additions
must keep the Black Start memory as a prerequisite and must be authored as
separate reviewed chains rather than multiplying this transaction.
