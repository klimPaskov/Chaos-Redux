# Event 58: Random Buildings

## Catalog identity

- Event ID: `58`
- Event name: Random Buildings
- Type: Minor Repeatable
- Status before implementation: To Be Reworked
- Chaos level: `1`
- Cluster: Positive Economy
- Cluster member severity: Medium

## Playable promise

Random Buildings creates one sudden worldwide construction wave. Every land state receives an independent chance to gain a valid state-level building. The result follows the state. Occupation, conquest, liberation, and later border changes naturally transfer the value of what appeared.

The event should feel broad and visibly uneven. One state may gain a railway-related facility, another an air base, another a civilian factory, and another a building tied to a separate Chaos Redux system. Neighboring states do not share a result, regional quota, or balancing rule.

The event remains easy to understand from the player side. A report event announces that construction has appeared across the world, then gives each human player a compact account of what appeared in their own territory. The complexity belongs in validation, candidate ownership, placement, and future integration.

## One global construction transaction

Each firing is one bounded global transaction.

At transaction start, the event freezes the list of loaded land states that exist in the campaign. New states, released tags, ownership changes, and other mutations caused by provider callbacks cannot cause the same transaction to revisit or add another state.

The frozen list controls membership only. Candidate validity is checked again immediately before every placement. Earlier layers can fill capacity, change a special system, or invalidate a later candidate. A later layer must respect the current state after all prior placements.

A state is processed once per active layer. A province package can affect several provinces inside the selected state, but it still counts as that state's one Evolution II result.

The transaction order is:

1. baseline state construction
2. Evolution I expanded state construction, when active
3. Evolution II provincial construction, when active
4. Evolution III exceptional construction, when active
5. result aggregation, transaction finalization, event logging, achievements, and player reports

The ordering is fixed so every implementation and test run can reason about capacity consistently.

## State universe

The event starts from every loaded land state. It does not globally exclude occupied states, states controlled by unusual actors, wastelands, low-population states, islands, or states owned by special Chaos countries.

Individual candidates can exclude a state when their own building cannot function there. A civilian-only structure can require a country that uses normal civilian systems. A naval structure can require a real coastline. A special project facility can require its DLC and owner API. A camp can require the camp system's own valid placement and initialization path.

A state receives no result for a layer when every candidate in that layer is invalid or at capacity. The state is recorded as exhausted for that layer. The event never forces a building above its maximum level, invents a province, replaces an existing building, or substitutes a different effect that is not a registered construction result.

## Ownership, control, and later conquest

The physical result belongs to the state and follows ordinary Hearts of Iron IV state behavior.

Ordinary buildings do not need a responsible country record. Player summaries attribute the immediate result to the country controlling the state when the transaction fires. If no valid controller can be resolved, the legal owner is used for the summary.

Special systems may need responsibility, institutional ownership, or an operating country. Their provider entry must define that rule. Event 58 does not assume that every special structure should blame or benefit the controller, owner, occupier, or original builder in the same way.

Later conquest does not remove an Event 58 building. The new controller or owner gains whatever normal use the building's system allows. Special owner systems retain their own capture, shutdown, discovery, transfer, evidence, or destruction rules.

## Baseline firing

At every successful firing, every state on the frozen list attempts one roll from the baseline state-building registry.

The baseline contains ordinary development and strategic structures. It can also contain rare special entries that their owner has explicitly approved for baseline Event 58 construction.

The baseline roll is independent in every state. Results do not react to neighboring results, global totals, country strength, player status, historical borders, or an attempt to distribute one of each building across the map.

Context can alter relative weights inside one state. A coastal state can gain a dockyard candidate. A low-infrastructure state can favor infrastructure. A state with no free industrial slots cannot roll a factory. These local changes do not create a world quota.

## Evolution stacking

Every evolution adds another layer. It never replaces the baseline or a lower enabled layer.

| Chaos | Active construction when every evolution is enabled |
| --- | --- |
| `0-199` | one baseline state-building roll per state |
| `200-399` | baseline plus one expanded state-building roll per state |
| `400-599` | baseline plus expanded state construction plus one province package per state |
| `600+` | baseline plus expanded state construction plus one province package per state plus a limited exceptional world allocation |

Evolution toggles remain independent. Disabling Evolution I removes only the expanded state-building layer. Evolution II and Evolution III can still operate at their own Chaos requirements when enabled. A disabled lower evolution cannot block baseline behavior or a higher enabled layer.

## Evolution activation and logging

The evolution thresholds change the next qualifying firing. They do not start a separate country crisis or a delayed evolution process.

This event uses pre-fire evolved openings. If Random Buildings first fires at `600+` Chaos, the same transaction can apply the baseline and all three enabled evolution layers.

Each evolution is recorded once, on the first transaction where its layer successfully creates at least one result. If a layer has no valid location in an unusual campaign, its recorded flag remains unset and a later firing can try again.

If all three evolutions first succeed on the same date, all three receive separate evolution-log entries because their mechanics stack and remain independently controllable.

Evolution state alone gives no Chaos. Any event-owned Chaos change comes from a completed construction consequence defined below.

## Repeatable behavior

Every firing reevaluates the world from its current state.

Existing Event 58 buildings remain. Later firings can add another level of the same building when capacity permits, add a different building, extend province construction, or select a new exceptional location.

Capacity exhaustion should become more common across repeated firings. That is an intended brake. The event does not clear old buildings or raise their maximum levels to preserve full coverage.

Before committing the event history and repeatable-weight transaction, the resolver performs a bounded firing preflight. If no active layer has any valid result anywhere in the frozen world, the attempt returns as unavailable and does not consume the event's firing count, cap reduction, timer transaction, or event-log row. This preflight occurs only when Event 58 has already been selected or manually requested. It does not justify a recurring world scan.

If at least one result is possible, the event fires normally even when some states or layers are exhausted.

## Player interaction

The event has one acknowledgement response. It does not ask countries to approve, pay for, redirect, demolish, or choose the random construction.

The report should communicate three facts clearly:

- construction appeared worldwide without a known builder
- every region developed differently
- the player's own states received a compact set of summarized results

The option tone should use dry bewilderment or administrative resignation. Final wording must be written during implementation from this direction. It should not become a generic warning, a map summary, or a list of raw probabilities.

## AI behavior

AI countries receive the same state and province results through the global transaction. They do not need event options, decisions, or an equivalent hidden purchase system.

Special structures continue to affect AI through their owner systems. Event 58 does not create separate AI rules for how a reactor, camp, stronghold, facility, port, railway, or dam operates after placement.

## Positive Economy cluster behavior

Random Buildings joins Cluster `7`, Positive Economy, as a Medium-severity member.

Its dominant effect is permanent development, so the cluster assignment remains valid even though a very small restricted pool can contain harmful or politically dangerous structures.

When Event 58 is selected by the normal event picker, the Positive Economy cluster can roll through the usual cluster path. When another member initiates the cluster, Random Buildings should have a reduced participation profile appropriate to a global Medium member. It should be noticeable without becoming a near-guaranteed second worldwide construction wave whenever the cluster appears. Exact participation must be measured with the complete cluster pool.

A cluster firing remains one global pacing event. Event 58 still applies its own effects, repeatable cap change, fired history, evolution records, and event details when it participates.

## Chaos impact map

Random Buildings has a small bounded event-owned Chaos footprint.

- The first successful baseline world construction adds `+2` Chaos once per campaign.
- The first successful Evolution II provincial wave adds `+1` Chaos once per campaign because borders, coastlines, rail systems, and supply networks are altered at world scale.
- The first successful Evolution III exceptional wave adds `+2` Chaos once per campaign.
- Evolution I adds no separate direct Chaos. It is another state-level expansion layer.
- Repeat firings add no direct Event 58 Chaos after these one-shot milestones.

The event must not duplicate generic Chaos sources. Military factory accumulation, deaths, unconventional warfare, contamination, condemnation, annexation, or other shared consequences continue through their normal systems.

A special structure can create later Chaos only through its owner system and a concrete consequence. A camp appearing is not permission for Event 58 to log camp deaths, evidence, condemnation, or atrocity Chaos itself.

The maximum lifetime direct Event 58 contribution is therefore `+5` Chaos when all three mapped milestones occur.
