# Chaos, Event Logs, Cluster Behavior, and Repeatability

## Chaos design rule

Evolution activation adds zero Chaos. Heat Wave should add event-owned Chaos only for concrete outcomes that are not already represented by Deaths, Air Cleanliness, war, annexation, or another shared source.

Every event-owned change should be a one-shot milestone per episode or per campaign. Routine daily stress must not farm Chaos.

## Proposed Chaos milestones

These values are tuning proposals. The implementation should centralize them and test their total contribution against other events.

| Milestone | Suggested change | Frequency guard |
| --- | --- | --- |
| Global Heat Wave onset | `+2` to `+3` | Once per episode |
| First multi-region Extreme footprint | `+5` | Once per episode |
| First systemic harvest failure accepted by Famine | `+5` | Once per episode |
| First permanent environmental degradation | `+3` | Once per campaign or episode, choose one after balance review |
| First desertification caused by Event 51 | `+5` | Once per campaign |
| First new wasteland state caused by Event 51 | `+10` to `+15` | Once per campaign |
| First cross-continental near-uninhabitable footprint | `+15` to `+20` | Once per campaign |
| Severe episode ends with limited permanent harm | `-2` to `-5` | Once per episode |
| Evolution III episode fully recovers without a new wasteland state | `-5` to `-10` | Once per episode |

The onset change is optional if overall event density already raises Chaos too quickly. The higher milestones are more important because they mark actual world change.

## Sources that must not be duplicated

### Deaths

Heat deaths already add Chaos through the shared rule of one Chaos per one million tracked deaths. Event 51 adds no second death-based Chaos.

### Wildfire and Air Cleanliness

Event 013 wildfire smoke and ash already affects Air Cleanliness, which changes Chaos through the shared contamination rule. Event 51 adds no second wildfire contamination Chaos.

### Wars and annexations

Military withdrawals, unrest, or war outcomes use their shared sources. Heat Wave should not add extra Chaos merely because a war continues during the crisis.

### Famine and Migration

If these systems have owner-specific Chaos consequences, Event 51 should not duplicate them. The proposed harvest-failure milestone is valid only when it represents the global realization that heat has broken a food region, not the same numeric consequence already applied by Famine.

## Chaos history wording direction

Each event-owned history entry should name the concrete outcome:

- global heat crisis began
- extreme heat spread across several regions
- a major harvest failed under heat
- land suffered permanent heat degradation
- desertification occurred
- a state became wasteland
- large regions became temporarily near-uninhabitable
- the episode ended with limited damage

The history should not expose internal thresholds, point formulas, caps, or episode variables.

# Normal event history

## Entry record

The entry event records one normal Event 51 history row.

Actor handling:

- The event is global, so the normal history actor should use the established global-event convention.
- Do not invent a random country actor merely because one player receives the popup.
- If the event-log framework requires an actor, use the documented neutral or player-context mapping after live inspection.

## Follow-up records

Ordinary reports, decisions, missions, mortality pulses, and recovery events should not become additional normal random-event history rows.

Major world milestones can appear as related details or dedicated consequence records only if the existing log supports that distinction.

# Event Details

Event Details should contain:

- event name and ID
- Minor Repeatable type
- Chaos level 1 and Calm World name
- Natural Disasters cluster membership
- current enabled state
- current weight, cap, and fired count
- premise text about a persistent global heat crisis
- three evolution preview rows
- current active or recovery status where the framework supports it
- last episode summary, if a safe compact event-owned history surface exists

The premise should describe heat, water, armies, food, industry, transport, and lasting environmental risk without listing numeric effects.

## Evolution preview

The evolution catalog preview should show:

- The Killing Heat
- The Drying Earth
- The Scorched World
- requirement tier or Chaos threshold
- enabled state
- concise premise

It should not show fake dates or history sequence numbers.

## Evolution history rows

Actual logged evolution rows should show the shared metadata expected by the main Evolutions tab and selected-event history:

- sequence
- date
- Event 51 identity
- evolution name
- tier
- stage
- enabled state

No actor is expected for this global track unless the live framework requires one.

# Natural Disasters cluster behavior

## Membership

Event 51 should be registered as a High-severity member of the Natural Disasters cluster.

The current export snapshot lists Event 13 repeatedly and Event 33, but not Event 51. Implementation must inspect the authoritative workbook and live cluster registry to determine the correct row structure and role fields.

## Cluster eligibility

Event 51 is a valid cluster member when:

- no Heat Wave episode is active
- no Heat Wave recovery or cleanup is active
- Event 51 is enabled
- Chaos level gate is met
- the member-specific cluster gate is met

If invalid, the cluster records a clear skip reason and continues evaluating valid members.

## Pacing

A cluster firing counts as one global pacing event. Event 51 still applies:

- its normal history entry
- repeatable fired count
- cap reduction
- event effects

It must not apply a second timer or major-weight pacing transaction.

## Duplicate heat prevention

The Natural Disasters cluster may contain heat-like or wildfire incidents. The cluster must not start two persistent Heat Wave episodes or create a second Event 51 setup through Event 13.

If another cluster member creates a short local heat incident, it remains distinct and bounded. Event 51 owns only the persistent global episode.

# Repeatable-event behavior

## Weight

Event 51 uses the normal repeatable weight model:

- starts at the shared default weight
- fires and reduces its cap through the shared factor
- recovers weight monthly to the current cap
- can fire again after complete cleanup

The event should not maintain a second private repeatable weight.

## Active-state exclusion

While active, recovering, or cleaning up, Event 51 should be unavailable to:

- automatic random selection
- normal manual event firing
- cluster membership firing
- any generic repeatable recovery action that assumes the event can immediately fire again

The Event Details row can show an active or recovering status rather than a misleading selectable weight when the framework supports this.

## Later episode scaling

The event does not automatically become weaker on repeat. The shared weight cap makes it less likely to reappear, while the world's permanent damage can make a later episode more dangerous.

A later episode can also be easier if:

- infrastructure was repaired
- long-term preparation exists
- population and industry moved into safer regions
- prior degradation removed vulnerable load from a state, though this can carry other severe costs

## Fired-count use

Fired count can influence flavour and limited setup variation, but it should not directly multiply all damage. Permanent world state already provides natural escalation.

Possible repeat-specific changes:

- reports refer to familiar emergency routines
- countries with prior successful preparation receive quicker setup
- previously degraded states start with higher vulnerability
- achievements track repeated survival

# Last episode summary

A compact event-owned summary can persist after cleanup:

- peak global intensity band
- active duration
- number of states that reached Extreme and Scorched
- total heat deaths read from the event's registered transaction totals, if the shared Deaths system exposes a source total
- new degradation, desert, and wasteland counts
- number of accepted Famine and Migration requests
- completed recovery date

This summary is for Event Details and documentation. It should not become a second live ledger.

# Acceptance tests

1. One entry event creates one history row and one pacing transaction.
2. Evolution activation creates an evolution row but no Chaos.
3. Heat deaths change Chaos only through Deaths.
4. Wildfire contamination changes Chaos only through Air Cleanliness.
5. A cluster firing records Event 51 effects without duplicate pacing.
6. An active episode produces a clear cluster skip reason.
7. Cleanup returns the event to normal repeatable eligibility.
8. A later episode has a fresh generation and retains permanent world damage.
