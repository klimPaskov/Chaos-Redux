# Event 065 Random Trait

## Part 1: Core Loop and Evolutions

## Catalog entry

- Event ID: `65`
- Event name: `Random Trait`
- Type: `Minor Repeatable`
- Status at planning start: `To Be Reworked`
- Chaos level: `1`
- Cluster: `Randomizations`
- Cluster member severity: `Medium`

## Core premise

Every active country leader in the world suddenly acquires one or more traits selected from the complete country-leader trait pool loaded from Hearts of Iron IV and Chaos Redux.

The event does not explain why the change occurs.

The change is immediate, global, cumulative, and indifferent to context.

A pacifist can become a warmonger.

A military dictator can gain the habits of a harmless administrator.

A revolutionary council can receive a monarchical trait.

A head of state can gain the trait of a dog, industrial concern, theorist, minister, pretender, exile, or route-specific historical figure when those entries exist in the same country-leader trait database.

The event treats those results as valid.

## Player experience

A firing should have a fast and readable sequence.

1. The game selects Event 65 through the normal random-event or cluster path.
2. One authoritative hidden executor determines the active Evolution.
3. The executor processes every eligible existing country.
4. Each eligible leader receives the required number of distinct new source traits.
5. The executor records the global result, the Evolution manifestation, direct Chaos milestone, and report data.
6. Every human-controlled country receives one report showing the global scale and its own leader's grants.
7. The event ends without opening an ongoing mechanic.

The visible event is a report.

It is not the place where the traits are granted.

Closing the report must never change which leaders were affected or which traits they received.

## Eligible countries and leaders

A country is eligible when all of the following are true at the moment the executor begins its global pass:

- the country currently exists in gameplay
- the country has an active political country leader role
- the role can receive a country-leader trait through the engine's supported effect path

The pass includes majors, minors, subjects, civil-war countries, governments in exile, capitulated countries that still exist as countries, dynamic countries, special Chaos Redux countries, and AI-controlled countries.

The event does not use ordinary-country exclusions because the user's rule is global.

Unused tags, countries that do not currently exist, dummy scopes, and countries without an active political leader do not create a target.

The implementation must count skipped no-leader countries for validation and reporting.

## Recipient identity

The processing unit is the active country-leader role exposed by a country.

Each existing country contributes one role.

If the engine exposes the exact same role object through more than one country scope, the implementation must deduplicate that role so it does not receive more than the advertised number of grants.

Separate country-leader roles held by the same named character can roll independently.

The implementation agent must verify how shared characters and country-leader roles are represented before selecting the final ledger scope.

## Atomic firing semantics

The event uses snapshot semantics.

The eligible world is the set of existing country-leader roles at the start of the Event 65 execution pass.

No time should advance between the first and last country.

A leader appointed after the pass is not affected.

A leader removed before their role is processed is counted as invalidated and receives nothing.

If the engine cannot retain a direct role target safely across the pass, the same immediate-tick `every_country` traversal is acceptable when inspection confirms that no time or unrelated on-action can intervene.

## Baseline

At the baseline form, every eligible leader receives exactly one accepted source trait.

All eligible source traits have equal selection weight.

No trait receives a preference based on:

- country
- ideology
- leader identity
- leader age
- leader gender
- government type
- war status
- faction
- subject status
- historical plausibility
- existing personality
- current national strategy
- whether the trait is useful
- whether the trait is harmful
- whether the trait contradicts another trait
- whether another game system normally reserves it for a specific route or person

The only roll exclusions are identity collisions and technically unavailable source definitions.

Those rules are defined in Part 2.

## Evolution I: Double Traits

### Requirement

- Raw Chaos Meter requirement: `200+`
- User-provided Evolution name: `Double Traits`

### Effect

Every eligible leader receives exactly two accepted source traits in the same firing.

Both slots use the complete uniform trait distribution over the traits still eligible for that leader.

The second slot does not copy the first slot's result.

A repeated source ID is rejected and redrawn.

No weight class is active at this Evolution.

### Presentation

The report must make the doubled scale clear.

The player's own results should be listed as two separate trait names when both grants succeed.

If the leader has fewer than two traits left in the pool, the report must show the actual number added and identify the leader as near saturation.

## Evolution II: Exceptional Personalities

### Requirement

- Raw Chaos Meter requirement: `400+`
- User-provided Evolution name: `Exceptional Personalities`

### Effect

Every eligible leader receives exactly three accepted source traits.

The pool remains complete.

Traits tagged as featured receive a modest weight increase.

A featured tag can come from power, rarity, unusual identity, extreme behavior, or Chaos Redux origin.

The tags never remove ordinary traits and never create compatibility filtering.

Weighting is defined in Part 2 and audited through the probability matrix.

### Presentation

The report should frame the event as a world of increasingly distinctive leaders.

It should not imply that every result is beneficial.

It should not hide the fact that ordinary traits remain common.

## Evolution III: Walking Contradictions

### Requirement

- Raw Chaos Meter requirement: `600+`
- User-provided Evolution name: `Walking Contradictions`

### Effect

Every eligible leader receives exactly five accepted source traits.

Featured traits receive a larger but still bounded weight increase.

Contradictory, harmful, bizarre, useless, and route-inappropriate combinations remain valid.

The event makes no effort to build a coherent personality package.

The five grants are separate draws from the stage distribution over the source traits still eligible for that leader.

At raw Chaos values above `600`, including the higher global Chaos bands, Event 65 remains at five grants unless a future accepted Evolution changes the design.

### Presentation

The report should emphasize the density of conflicting personal qualities.

The tone may use dry absurdity.

It should not describe the change as a carefully formed ideology, doctrine, or character arc.

## Evolution selection

Event 65 is an instant repeatable event, so its Evolutions apply through an evolved opening at firing time.

The executor resolves the highest enabled Evolution that has become available.

The event follows these rules:

1. An Evolution cannot manifest below its raw Chaos requirement.
2. An Evolution disabled through the shared Evolution settings cannot manifest.
3. A higher enabled Evolution can manifest even when a lower Evolution was disabled or never appeared.
4. Once an Evolution has manifested, it becomes the persistent Event 65 Evolution state.
5. A later decline in raw Chaos does not remove a manifested Evolution.
6. If a higher Evolution is disabled, the event uses the highest lower manifested or currently available enabled form.
7. Enabling a previously disabled Evolution allows it to manifest on a future firing once its requirement is met.
8. Evolution history is recorded when the evolved effect successfully fires, not when the Chaos threshold becomes reachable.

A direct jump from baseline to Evolution III is valid.

The first Evolution III firing then grants five traits.

The system does not replay Evolution I or Evolution II as separate effects during that firing.

## Repeat behavior

Event 65 remains in the normal repeatable minor-event framework.

Each later firing adds the number of traits required by the active form.

Previously granted traits are never rerolled or replaced by Event 65.

Existing traits from vanilla, DLC, Chaos Redux, focuses, decisions, events, advisors, leaders, or prior Random Trait firings remain attached unless another owning game system later removes them.

Event 65 also records a source-ID grant history for its own rolls.

A source trait previously granted to the same recipient by Event 65 is not granted again even when another system later removed its visible trait.

This prevents the event from cycling the same source trait instead of expanding the leader's history.

## Exact grant count

The advertised count is a target count of accepted additions.

The executor must keep rolling until one of these conditions is reached:

- the leader has received the stage's required number of accepted traits
- the leader has no source trait left that is neither currently owned nor present in the Event 65 grant ledger
- the leader target becomes invalid during execution

The event must not count a rejected collision, a missing trait, a failed effect, or an unavailable definition as a successful grant.

## Saturation

A leader is saturated when every source trait in the current loaded Event 65 pool is either currently owned or recorded in that leader's Event 65 grant ledger.

A saturated leader receives no new trait.

A leader with fewer remaining traits than the stage target receives every remaining eligible trait and is then saturated.

Saturation is a valid late-save outcome.

The report and debug counters must distinguish saturation from script failure.

## Event choice

The report has one acknowledgment option.

Its option effect may clear report-only temporary data.

It must not grant traits, reroll results, remove traits, alter weights, change Evolution state, or change the event's Chaos result.

The player receives no veto because the core idea is an involuntary global randomization.
