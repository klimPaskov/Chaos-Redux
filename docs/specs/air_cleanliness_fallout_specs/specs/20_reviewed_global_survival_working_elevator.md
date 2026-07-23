# Reviewed Fallout Global Survival Pilot: The Working Elevator

## Purpose

The Working Elevator is a dormant country-level food-storage chain for the
third and fourth generation after the Fallout transition. It follows the
closed First Streetlight memory and asks who controls a surviving grain store
when a settlement can finally see its loading floor again. The choice links
food, fuel, logistics, market legitimacy, refugee integration, and spoilage. It
is not a super-event and it does not perform the thermonuclear transition. Its
report picture is dedicated to this chain.

## Entry contract

The candidate producer defines candidate `324`, transaction key `710020`, and
route `7120`. The gate requires current country registry, identity, and
resource rows, a closed First Streetlight memory, second-generation timing,
campaign day `1300` through `2800`, Food `28`, Power `20`, Reclamation `20`,
Cohesion `30`, Recognition `20`, and one affordable branch. The scheduler must
provide the ordinary receipt before the opening event. The opening target is
the current country and the target type is `none`.

The chain freezes Food, Power, Reclamation, Cohesion, Recognition, and five
working-elevator ledgers before it schedules a result. This keeps the recorded
ration policy stable while the 28-day hopper result is pending.

## Branches and results

| Branch | Immediate question | Durable identity |
| --- | --- | --- |
| Public granary | Can a common ledger make one store answer to every shelter? | Grain capacity and civic ration legitimacy |
| Military depot | Should patrol routes receive the first measured loads? | Logistics strength with narrower civilian access |
| Merchant exchange | Can licensed carriers reopen a clean grain market? | Market legitimacy and route knowledge |
| Refugee ration center | Can arrivals receive food without disappearing into a queue? | Refugee integration and visible intake |

Each branch grades the frozen Food, Power, Reclamation, and Cohesion values into
success, partial, or failure. Results update Food, Power, Recognition,
Cohesion, Stability, War Support, grain capacity, logistics, market legitimacy,
refugee integration, and spoilage. Failure requests population loss through the
Deaths contract. A successful, partial, or failed result opens a 210-day
storehouse maintenance callback. The callback has its own durable deltas and
closes the memory after authenticated cleanup.

## AI, memory, and cleanup

Hidden AI prefers a public granary when Food is healthy, a military depot when
Power is strong, a merchant exchange when Recognition is established, and a
refugee ration center when Cohesion is high. It falls through to the first
affordable branch in a stable order. Human and hidden-AI lanes share the same
transaction coordinator, registry generation, event token, mode, branch, due
day, and cleanup token.

The result records one of twelve branch and outcome payloads under history
`9125`. The callback records one of three maintenance payloads. Cleanup
releases exact result and callback receipts, clears transient registry and
frozen values, and retains only the grain ledgers, policy memory, and timed
modifiers.

## Presentation and wiring

The source event file is `events/fallout_world_end_events.txt` under
`add_namespace = chaosx.fallout`. Events `324` through `330` provide the human
opening, hidden AI opening, human and hidden AI result, human and hidden AI
callback, and authenticated cleanup. Localisation is in
`localisation/english/fallout_world_end_working_elevator_l_english.yml` with a
BOM. The dedicated report sprite is registered as
`GFX_report_event_fallout_working_elevator` in
`interface/fallout_world_end.gfx`.

## Review status

This is a reviewed dormant pilot. It is not counted toward the 660-block
release floor because activation, host authority, save recovery, multiplayer
delivery, and runtime Event Log delivery were not observed. The bounded
read-only `hoi4.event_inspect` request returned `Transport closed`, so the
engine-side graph remains an explicit blocker rather than a claim of proof.

## Future extension

The next expansion should connect the durable grain policy to a named regional
trade partner, a refugee settlement focus overlay, and a state-level elevator
target after the state ownership contract is reviewed. Those additions must
keep this memory as a prerequisite and must be authored as separate chains.
