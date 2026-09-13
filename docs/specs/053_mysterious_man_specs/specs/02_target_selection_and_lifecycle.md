# 2. Target Selection and Lifecycle

## Initial eligibility

The parent Event 53 entry is available only when at least one valid player-controlled country exists.

A valid target must satisfy all of the following:

- it currently exists as a country scope
- it is controlled by a human player at the moment of selection
- it uses normal civilian and political systems
- it is not classified as a special Chaos system actor
- it is not currently classified as an actual nonhuman country
- it owns at least one valid state
- it can receive country events and ordinary resource transactions
- it is not already marked as the Event 53 target

The shared `is_special_chaos_country`, `is_actual_nonhuman_country`, and `uses_normal_civilian_systems` classifiers remain the authoritative cross-system exclusions. Event 53 may add owner-specific checks, but it must not copy or fork those shared classifier bodies.

A government-in-exile with no owned state is excluded from initial selection because too many core consequence families would be invalid. An existing target that later loses all land follows the target-loss rules below.

## Uniform multiplayer selection

Every valid player country receives one target-selection ballot. The initial target draw is uniform.

Player country size, ideology, major status, war status, Chaos settings, prior event history, host status, and country tag do not alter the draw.

If one valid player country exists, it is selected. If four valid player countries exist, each has one-quarter probability. Invalid player countries are absent from the pool and do not receive zero-weight placeholders.

The random-event system records Event 53 as fired once for the selected actor. It must not create a separate history entry for an unselected player.

## Persistent target identity

The selected country receives a stable Event 53 target marker. Event 53 also keeps one authoritative persistent pointer or equivalent owner ledger entry for direct routing.

The country marker is the recovery proof if the persistent pointer becomes unavailable. The implementation must still guarantee that no more than one country has the active target marker.

The target is attached to the country scope, not to a Steam account or player name. If another human later takes control of the same country, that human receives future visits.

The chain survives:

- save and reload
- cosmetic tag changes
- ideology changes
- government changes within the same country scope
- faction entry or exit
- puppet status changes
- capital relocation
- civil war participation when the original country scope remains alive

## Human-control pause

The selected country is the only country allowed to make the pay-or-refuse choice. If the target country becomes AI-controlled, no visit popup is sent to the AI and no automatic payment or punishment occurs.

A pending visit enters a paused state. The country receives a bounded delayed recheck. Only one recheck can exist at a time. The check resumes the visit when the country is human-controlled again.

The pause does not:

- clear the target
- create accumulated visits
- roll demands in advance
- build consequence pools in advance
- shorten the future interval several times
- allow the AI to pay
- allow the AI to refuse

This design preserves the player-only choice and prevents popup loss after a disconnect, observer switch, host migration, or temporary tag switch.

## Country extinction

When the target country ceases to exist, Event 53 ends cleanly by default.

The owner cleanup must:

- clear the Event 53 active-chain state
- clear the target marker and persistent pointer
- cancel any visit, pause, or evolution-check state that can still resolve
- clear locked demand values
- clear temporary package-selection data
- retain the historical Event 53 firing and evolution log entries
- avoid selecting a replacement player country

The man does not jump to another surviving player merely because the original target was annexed.

## Legal successor transfer

A successor transfer is permitted only through an explicit Event 53 adapter called by the system that created the legal successor.

The calling system must provide proof that the successor is the continuation of the original target government, not merely a breakaway, occupier, ally, puppet, ideological match, or state holder.

A valid transfer must be atomic:

1. prove the old target and successor
2. prove the successor exists and uses normal civilian systems
3. prove the successor is the legal continuation under the owning system's rules
4. move the Event 53 marker and persistent pointer
5. move visit counters, refusal counters, payment counters, evolution state, and pending schedule state
6. clear the old target state
7. reconcile any currently locked demand before another popup can open

The implementation must not infer a successor from core count, capital ownership, faction leadership, ideology, largest territory, player control, or tag similarity.

If no owner system submits valid proof, the chain ends.

## Civil war behavior

An ordinary civil war does not automatically transfer the chain. The original target country remains the target while it exists.

If the original target loses and a civil-war owner explicitly identifies the winner as the legal continuation, that owner may call the successor adapter. A rebel country does not inherit the man merely because it controls the former capital.

When the Mysterious Man himself causes a civil war, the package adapter must preserve which country remains the Event 53 target. The consequence cannot duplicate the target marker across rival governments.

## Annexation during a visit

The pay or refuse result must validate the target immediately before applying the transaction. If the country becomes invalid while a popup is open, the event closes through target-loss cleanup without charging the player or rolling a punishment.

This is an engine-race safeguard, not a player escape route. Ordinary annexation ends the chain under the same rule as any other target extinction.

## Target-state invariant

At all stable points in the chain, exactly one of these states is true:

| State | Meaning |
| --- | --- |
| Inactive | Event 53 has not fired, or its target has ended without a successor |
| Scheduled | One valid target exists and exactly one future visit is pending |
| Paused | One valid target exists, control is not human, and exactly one bounded recheck is pending |
| Present | One valid target exists and one demand is locked for the current visit |
| Resolving | One valid target exists and one payment or refusal transaction is running |
| Transferring | A proven legal-successor transaction is moving the chain atomically |

No stable state may contain two targets, two locked demands, two pending visits, or two simultaneous Event 53 consequence transactions.

## Lifecycle counters

Event 53 should retain the following internal memories:

- total completed visits
- total paid visits
- total refusals, including inability to pay
- consecutive refusals
- date of first appearance
- date of latest completed visit
- active evolution level or enabled evolution feature flags
- latest demand type
- latest demand amount
- latest consequence package ID
- latest consequence result receipt
- current schedule state

These are internal values. Event Details may show the current target and a simple active status when the shared UI supports it. It should not expose a full ledger.

## Parent firing and follow-up accounting

Only `chaosx.nr53.1`, or the final canonical entry event that retains this identity, counts as the official Event 53 firing.

Recurring appearances, hidden scheduling events, demand calculation events, consequence bridge reports, lifecycle cleanup events, and evolution checks are follow-ups. They do not:

- increment the Event 53 fired count
- consume another Fire-Once entry
- advance the global random-event timer
- apply another minor-event pacing transaction
- count as another cluster member firing
- create duplicate Event 53 History rows

Actual evolution milestones use the shared evolution log and identify the selected country as actor.
