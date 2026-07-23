# Reviewed Fallout Global Survival Pilot: First Streetlight

## Purpose

First Streetlight is a dormant country-level urban recovery chain for the
second and third generation after the Fallout transition. It follows a closed
Black Start memory and asks which district receives the first dependable public
current. The branch is a civic decision with material consequences, not a
generic infrastructure bonus. It is not a super-event and it does not perform
the thermonuclear transition. Its report picture is dedicated to this chain.

## Entry contract

The candidate producer defines candidate `317`, transaction key `710019`, and
route `7119`. The gate requires current country registry, identity, and
resource rows, a closed Black Start memory, at least two generation changes,
campaign day `1100` through `2200`, Power `30`, Black Start capacity `25`,
Black Start governance `25`, Cohesion `30`, Reclamation `25`, and one
affordable branch. The scheduler must provide the ordinary receipt before the
opening event. The opening target is the current country and the target type is
`none`.

The chain freezes Power, Black Start capacity and governance, Cohesion,
Reclamation, Recognition, and five First Streetlight ledgers before it
schedules a result. This keeps the recorded civic priority stable while the
35-day result is pending.

## Branches and results

| Branch | Immediate question | Durable identity |
| --- | --- | --- |
| Capital first | Can the capital make public time visible again? | City identity and civic trust |
| Clinics first | Should night care receive the first reliable feeder? | Civic care and lower exposure |
| Factories first | Can workshops justify a public night shift? | Production and industrial security |
| Perimeter first | Should ash roads and gates be visible before the center? | Security and reclamation reach |

Each branch grades the frozen Power, capacity, governance, Cohesion,
Reclamation, and Recognition values into success, partial, or failure. Results
update Power, Scrap, Recognition, Cohesion, Stability, War Support, city
identity, civic capacity, production, security, and exposure. Failure requests
population loss through the Deaths contract. A successful, partial, or failed
result opens a 240-day public maintenance callback. The callback has its own
success, partial, and failure deltas and closes the memory after authenticated
cleanup.

## AI, memory, and cleanup

Hidden AI uses a deterministic priority ladder. It prefers the capital when
governance is strong, the clinics when Cohesion is high, the factory streets
when capacity is high, and the perimeter when Reclamation is high. It falls
through to the first affordable branch in a stable order. Every delayed result
and callback uses the same transaction coordinator, registry generation, event
token, mode, branch, due day, and cleanup token as the human path.

The result records one of twelve branch and outcome payloads under history
`9124`. The callback records one of three maintenance payloads. Cleanup
releases the exact result and callback receipts, clears transient registry and
frozen values, and retains only the durable urban ledgers, policy memory, and
timed modifiers.

## Presentation and wiring

The source event file is `events/fallout_world_end_events.txt` under
`add_namespace = chaosx.fallout`. Events `317` through `323` provide the human
opening, hidden AI opening, human and hidden AI result, human and hidden AI
callback, and authenticated cleanup. Localisation is in
`localisation/english/fallout_world_end_first_streetlight_l_english.yml` with a
BOM. The dedicated report sprite is registered as
`GFX_report_event_fallout_first_streetlight` in
`interface/fallout_world_end.gfx`.

## Review status

This is a reviewed dormant pilot. It is not counted toward the 660-block
release floor because activation, host authority, save recovery, multiplayer
delivery, and runtime Event Log delivery were not observed. The bounded
read-only `hoi4.event_inspect` request returned `Transport closed`, so the
engine-side graph remains an explicit blocker rather than a claim of proof.

## Future extension

The next expansion should connect the durable city identity to a named regional
partner, a country-specific focus overlay, and a streetlight-related diplomacy
choice. Those additions must keep the First Streetlight memory as a
prerequisite and must be authored as separate reviewed chains rather than
multiplying this transaction.
