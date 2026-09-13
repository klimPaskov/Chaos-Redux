# Lifecycle and Episode State Machine

## Episode identity

Every Heat Wave firing receives a new monotonically increasing episode generation. All temporary state registrations, country participation records, incident cooldowns, missions, delayed events, and report targets must carry or prove that generation.

A delayed effect from an old generation must fail closed. It must not modify a state during a later Heat Wave because an old event target survived longer than expected.

Proposed event-owned global state:

- active episode flag
- recovery-active flag
- cleanup-in-progress flag
- episode generation
- current Global Heat Wave Intensity
- current intensity trend
- episode age
- dynamic duration budget
- surge reserve
- recovery progress
- one-shot milestone flags for the current generation
- registered country and state arrays or their supported sparse equivalent

The live repository should determine exact variable and array names. The design requires the behavior, not these provisional names.

## Entry eligibility

Event 51 can enter the normal random pool only when:

- no Heat Wave episode is active
- no Heat Wave recovery is active
- no Heat Wave cleanup transaction is active
- the event is enabled
- its Chaos level gate is met
- normal repeatable weight and selection rules allow it
- no shared terminal state blocks ordinary event firing

The event should not depend on a particular season. The world contains both hemispheres and many climates. Local latitude and climate should influence state Heat Stress, but the global event can begin at any date.

## Opening transaction

The entry event performs one bounded setup transaction:

1. Increment the episode generation.
2. Set active state and clear stale current-generation milestones.
3. Roll the episode's initial intensity, duration tendency, volatility, and surge reserve from the current world.
4. Register valid ordinary countries and states through bounded owner-driven or chunked logic.
5. Calculate initial state vulnerability and Heat Stress.
6. Apply the initial temporary effects.
7. Open the event-owned decision category for normal countries with actionable exposure.
8. Select the first national hotspots and first world report targets.
9. Record the normal event history entry once.
10. Apply the event-owned onset Chaos milestone once, if retained by balance review.
11. Queue the next lifecycle pulse through the supported event-owned runtime pattern.

The opening should not perform a permanent terrain change or systematic mortality transaction.

## Phases

### Phase 1: Onset

Suggested duration: 7 to 20 days.

Intensity rises from its opening value or remains briefly stable while state Heat Stress catches up. Countries select national priorities and receive first reports. Emergency actions are cheaper to start before the first major surge because systems have not yet failed.

Onset ends when one of these occurs:

- global intensity reaches the first severe threshold
- the opening duration expires
- a high initial roll begins the episode directly in expansion

Evolution I can make the onset lethal when it was already active before the episode started, but mortality should still respect a short local exposure confirmation unless the initial state is already at the final stress band and has no functioning protection.

### Phase 2: Expansion

Suggested duration: 30 to 90 days.

Intensity and state exposure spread. National priorities begin to change outcomes. State incidents, missions, and competing sector demands become active. The event should identify places where vulnerability is increasing faster than mitigation.

Expansion can move into a surge, a short lull, or a direct plateau.

### Phase 3: Surge

Suggested duration: 14 to 45 days per surge.

A surge spends part of the episode's surge reserve and raises intensity momentum. It can be global or regionally amplified. The global value should rise visibly, while local states respond according to their vulnerability.

A severe episode can have several surges. Repeated surges require enough duration budget and must not occur so frequently that the player cannot respond.

### Phase 4: Plateau

Suggested duration: 20 to 80 days.

Intensity remains high with smaller fluctuations. This is where accumulated consequences become important. Reservoirs, crops, railways, armies, hospitals, and power systems may fail even without a new peak because exposure continues.

Evolution II environmental exposure gains should be strongest during a long extreme plateau.

### Phase 5: Lull or resurgence

A lull is a real temporary easing, not the end of the event. Intensity falls by a meaningful amount and some states leave their highest stress band. Countries can restore reserves or make the mistake of ending measures too early.

A resurgence is allowed when:

- the episode retains surge reserve
- the dynamic duration budget has not entered terminal decline
- the previous surge ended long enough ago
- the current global intensity has fallen below its last peak
- the event has not exceeded its episode surge cap

The first lull should display uncertainty through trend and system behavior, not through text that directly announces a future resurgence.

### Phase 6: Decline

The decline begins when the episode's duration budget, volatility, and surge reserve no longer support another major rise. Global intensity trends downward, but local Heat Stress may stay elevated because water, crops, power, and infrastructure recover slowly.

The system must not clear all state effects when global intensity crosses one threshold. Each state cools and recovers through its own stress calculation.

### Phase 7: Recovery

Recovery begins when Global Heat Wave Intensity reaches the inactive floor and no new surge can occur.

During recovery:

- heat generation stops
- temporary heat penalties decay by state
- repair, reopening, reservoir restoration, agricultural recovery, and military rest missions can remain active
- Famine and Migration continue under their own systems
- active wildfire incidents continue under Event 013
- permanent degradation remains
- cleanup waits for delayed heat-owned jobs and temporary modifiers to reach a safe state

Recovery should last long enough to make repair choices matter. Suggested ordinary range: 20 to 90 days, scaled by damage and national response.

### Phase 8: Cleanup

Cleanup is one idempotent transaction, not a loose collection of delayed removals.

It should:

- close or retire Heat Wave decisions and missions
- remove temporary state and country modifiers
- clear heat-owned temporary unit exposure markers
- clear current-generation targets and incident cooldowns
- clear active state and country registrations
- clear episode-only variables and milestone flags
- preserve permanent damage and owner-system consequences
- verify that no Heat Wave delayed job remains pending
- clear recovery and cleanup flags
- return Event 51 to repeatable eligibility

If cleanup encounters incomplete proof, it should leave the cleanup state active and retry through a bounded owner path rather than declaring the episode finished.

## Dynamic duration

The event should not roll one hidden end date and ignore everything that happens afterward. Duration should emerge from a budget that changes within defined limits.

Suggested duration tendencies:

| Episode profile | Expected active span |
| --- | --- |
| Mild baseline | 75 to 140 days |
| Severe baseline | 120 to 240 days |
| Evolution I lethal episode | 120 to 280 days |
| Evolution II drying episode | 180 to 420 days |
| Evolution III scorched episode | 240 to 540 days hard ceiling |

These are tuning bands, not guaranteed dates. Implementation should centralize them in script constants after engine validation.

Duration can increase through:

- high opening intensity
- high global aridity and drought footprint
- repeated severe regional heat states
- Evolution II or III
- failed world mitigation milestones
- large existing environmental degradation footprint

Duration can decrease through:

- sustained global decline momentum
- broad effective mitigation
- low drought and wildfire pressure
- few states remaining in severe bands
- completion of an episode-level relief threshold

A single small country should not meaningfully shorten the entire global event by spending resources. Global mitigation should be an aggregate of valid participating countries and only within a capped influence band.

## Mid-episode evolution

An evolution can become eligible while a Heat Wave is already active.

The normal sequence is:

1. The Chaos threshold and prior evolution stage become valid.
2. The evolution remains enabled in Event Details.
3. A dynamic MTTH process begins, normally around a 90-day baseline but scaled by current episode severity and stage relevance.
4. The evolution is recorded through the shared evolution log once.
5. New behavior begins from that date forward.
6. Existing state exposure can be read as prior exposure where the evolution design explicitly requires it.

Evolution II should not retroactively convert terrain based on days that were never recorded. Event 51 should record accumulated extreme exposure from the start of every episode even before Evolution II activates. The exposure ledger remains dormant until the evolution is active.

Evolution I can begin recurring mortality after activation, but it should respect the current state's lethal exposure duration and mitigation. It does not kill people retroactively for earlier baseline days.

## Repeat firing

A later episode receives:

- a new generation
- a new opening intensity
- a new duration and volatility profile
- new surge timing
- fresh temporary state Heat Stress
- fresh decisions, missions, and reports

It inherits:

- current state population
- damaged or repaired buildings
- permanent environmental degradation
- current terrain
- persistent Famine outcomes
- persistent Migration outcomes
- current infrastructure and supply state
- any long-term country preparations created by other systems

It does not inherit:

- old Global Heat Wave Intensity
- old trend or surge reserve
- old active duration
- old temporary Heat Stress
- old national priority
- old active missions
- old incident cooldowns
- old active report targets

## Save and multiplayer behavior

All lifecycle state must survive save and reload without rerolling the episode profile or duplicating setup. A reload during a surge must resume the same generation and phase.

In multiplayer, the global episode is shared. Every player country receives its own exposure summary and actions. One player cannot pause cleanup for the entire world by leaving a local decision open. Local player choices affect that country and its states, while the global intensity process remains deterministic and shared.
