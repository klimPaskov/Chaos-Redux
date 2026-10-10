# Industrial Boom specification, part 1: Core event and baseline lifecycle

Catalog identity, implementation status and open questions live in the [package README](034_industrial_boom_spec_index.md).

## Event premise

A major country or player-controlled country experiences an abrupt industrial acceleration that exceeds what its factories, labor force, infrastructure and material access should allow.
Production lines fill, construction schedules shorten, new shifts appear, and firms accept orders that would normally take years to complete.
The benefit begins immediately and is large enough to change the country's military and civilian plans.

The expansion is unstable.
Every new order competes for labor, fuel, transport, machine time, credit, imports and maintenance.
These strains are gathered into one public value, Overheating (part 2).
The country may use the boom as a short power window, convert it into lasting development, or push it into Event 35 Great Depression 2.0.

The event should feel generous before it becomes urgent.
The player must have time to exploit the opening, see the first signs of strain, and choose how to manage it.
A brief bonus followed by an unavoidable punishment fails the premise.

## Core player experience

1. **Immediate abundance.** The first day changes production and construction priorities, and new lines become worth opening.
2. **Visible strain.** Overheating rises for readable reasons, and the category shows its band, trend, next threshold and leading cause.
3. **Competing uses of the boom.** Running hot buys output, stabilization costs logistics, a reserve sacrifices output for safety, and regional projects can become lasting gains.
4. **A landing problem.** The boom never ends on a hidden timer. The country lands it deliberately, is forced down, or crashes into Event 35.
5. **Campaign memory.** Later firings remember earlier landings and crashes, with diminishing permanent returns.

## Target selection

Each normal or cluster firing selects one country from the valid pool.

### Eligible countries

A country is eligible when it:

- is a major country or is controlled by a human player, including a non-major player;
- passes Event 35's `great_depression_has_viable_economy` (ordinary civilian economy with a usable industrial state);
- has no active boom, no frozen collapse snapshot and no pending collapse delivery;
- has no active Great Depression and no incompatible economic state.

The implemented entry already applies these gates (README, implementation status).
Special Chaos actors and nonhuman economies fail the viable-economy gate and do not receive the event.
Coexistence with an active Event 35 crisis is excluded by default.

### Target weighting

The implemented entry uses an unweighted `random_country`.
The design replaces it with a weighted pool in which every valid country keeps a nonzero chance.

Weight rises with a substantial industrial base, good infrastructure, high stability, a major war creating equipment demand, and a human player who has not recently received the event.
Weight falls sharply for a recent Event 34 firing in the same country, and moderately for an earlier Event 34 crash, a blockade, very low stability, or heavy loss of core industry.
Weighting prevents repetition, not difficulty: a country with weak logistics can still receive the event and face a harder version of it.

When no valid country exists, the event reports itself unavailable through the shared event-pool evaluator, as Event 35 already does for `great_depression_target`.

## Opening sequence

The firing chooses the target and records the event once, with the target as the Event History actor.
The target then receives the visible opening, the boom package, starting Overheating and its Industrial Regions.

The opening shows speed through concrete evidence: cleared backlogs, rail yards and ports at capacity, construction crews on several shifts, ministries and firms competing for workers, and new districts growing around existing works.
At baseline the cause is industrial mobilization and investment, not a mysterious gift; later evolutions can make the expansion physically impossible.

### Opening package

The functional target is roughly doubling practical industrial productivity after normal stacking, not `+100%` on every modifier.
The package should:

- raise factory output and civilian construction speed sharply;
- accelerate production-efficiency growth, with a modest efficiency-cap increase;
- raise dockyard output at a lower rate unless the country is strongly maritime;
- make new lines and large construction queues immediately attractive.

The implemented `industrial_boom` idea (static output, efficiency, construction, local resources and research speed) is interim.
Research speed and broad local resources are not part of the design promise, and the final package must not stack the old idea beneath the new staged effects.

### Starting Overheating

A baseline opening starts in the Sustainable band with a real benefit window before drift alone creates danger.
Exact ranges are in part 2.

### Industrial Regions

The opening names one to three existing industrial states as the boom's centers (part 4).
They anchor reports, projects, protection and incidents.
The implemented entry already freezes one random owned, controlled, populated industrial state as the inherited region for Event 35; the design replaces that random pick with the region ranking in part 4.

## Lifecycle

The boom has three lifecycle states.
They are not evolutions and never appear as evolution records.
Pressure inside the Running state is described by the Overheating bands in part 2, so the player follows one value instead of a second phase ladder.

### Opening

The first 90 days, tuned through a constant.
The full package is active, base drift is reduced, and Cool the Expansion is hidden unless the start was unusually high.
Prepare a Controlled Landing cannot start.
The player reorganizes production, starts construction, decides whether to run hot, and designates the first project.

### Running

The main period.
All actions are available according to the current band.
Projects advance, incidents occur, evolutions can arrive, and the player chooses between pushing, stabilizing and preparing to land.
High bands erode part of the package (part 2), so a near-crash economy is never a free maximum-output state.

### Landing

Prepare a Controlled Landing is active (part 3).
Voluntary pressure actions close, evolution pacing pauses, and the transition ends the boom in stages.

## Outcomes

The boom resolves into one of four outcomes.

| Outcome | How it happens | Result |
| --- | --- | --- |
| Controlled landing | Landing mission completes below 40 Overheating with at least one secured project | Package ends in stages, secured projects convert to legacy, short reconversion modifier |
| Rough landing | Landing mission completes at 40 or above, or with no secured project | Package ends, limited legacy, temporary industrial exhaustion |
| Forced landing | Emergency Production Halt succeeds in the Dangerous or Critical band | Package ends at once, no project converts, long exhaustion |
| Crash | Overheating reaches 100, Prevent the Crash fails, or the halt fails | Package ends, snapshot freezes, the same country enters Event 35 (part 6) |

A live supplier contract with a depressed country (part 7) upgrades a rough landing to a controlled one once, because foreign orders absorb the capacity that would otherwise go idle.

Rough and forced landings set Event 35's recent-industrial-expansion target signal for its normal duration, which raises the chance that an independent Great Depression later selects the country.
This replaces a hidden post-boom relapse trigger with an existing, documented Event 35 weight.

The landing forecast in the category header (part 9) shows which outcome the current conditions point to before the player commits.

## Repeatability

Event 34 remains Minor Repeatable.
The country remembers the number of booms, controlled landings, crashes, the highest evolution reached, its consumed legacy budget and the states that already hold a strong legacy (part 4).

A later firing starts with slightly higher Overheating after each earlier crash, finds fewer untouched states for raw capacity, and shifts its rewards toward efficiency, logistics and conversion.
A country with an earlier controlled landing gains a shorter Opening state and a better landing forecast.
History creates both advantages and liabilities, and never a permanent ban.

## Event flow

```text
Normal or cluster selection
  -> valid target, evolved opening when a stage is unlocked and enabled
  -> opening report, boom package, Overheating, Industrial Regions
  -> Opening (exploit, designate the first project, optional reserve)
  -> Running
       -> run hot, stabilize, cool, protect, build projects
       -> incidents and possible active evolution
  -> Landing mission, Emergency Production Halt, or collapse
  -> controlled, rough, forced, or crash into Event 35
  -> cleanup, bounded country and state memory
```

## Success standard

Without reading formulas, the player can answer: how hot is the economy, is it rising, what happens at the next threshold, and which action addresses the leading cause.
A player may rationally exploit a short wartime window and accept a rough landing, sacrifice output for lasting legacy, survive a shock with a reserve and protection, end the boom early, or push too far and knowingly risk Event 35.
No single route dominates every country and war state.
