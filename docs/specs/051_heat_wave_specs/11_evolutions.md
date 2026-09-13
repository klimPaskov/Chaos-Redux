# Evolutions

## Evolution structure

Event 51 has one ordered evolution track. Each stage changes the active crisis and future episodes.

An evolution is a persistent event capability, not an episode phase. Once activated, it remains part of Event 51 unless the shared evolution framework defines another behavior.

Evolution activation itself changes no Chaos. Only concrete outcomes add Chaos.

## Pacing

Evolution eligibility begins at the accepted Chaos threshold. Activation normally uses the shared MTTH evolution pattern.

Suggested base MTTH before dynamic factors: 90 days.

Factors that should shorten MTTH:

- active Heat Wave already in a high global band
- several populated states already at Extreme or Scorched
- previous evolution stage active
- severe global Famine, Migration, drought, or wildfire footprint connected to heat
- long active episode age

Factors that should lengthen MTTH:

- no active Heat Wave
- current event disabled
- current evolution disabled
- few valid ordinary states exposed
- world already under an incompatible terminal state

When no Heat Wave is active, an evolution can still activate and be logged. Its new behavior applies from the opening of the next episode.

## Enabled and disabled behavior

Each evolution stage must respect its Event Details toggle.

- A disabled stage does not activate or record.
- A disabled stage does not set a recorded flag used by later stages.
- Later stages requiring it remain unavailable.
- Baseline episode progression continues normally.
- Decisions and reports that only exist because of the disabled stage remain hidden.
- If a stage was activated earlier and is later disabled through a supported setting, implementation must follow the shared evolution framework's established policy. It must not leave half-active mortality or terrain logic.

The live repository must be inspected for the exact enabled-state lifecycle before implementation.

# Evolution I: The Killing Heat

## Requirement

- Global Chaos at `200+`
- Event 51 enabled
- Evolution I enabled
- Not previously activated

## Core change

Heat becomes systematically lethal. States can suffer recurring civilian population loss and divisions can suffer recurring military manpower loss after confirmed lethal exposure.

## Starting behavior

If Evolution I is active before a new Heat Wave starts:

- the opening episode can begin lethal
- lethal exposure starts recording immediately
- mortality still requires the state's confirmation and exposure rules
- an opening Scorched state with total water failure can use a shorter confirmation window than an ordinary Extreme state

If Evolution I activates during an episode:

- existing current Heat Stress applies immediately
- prior recorded exposure can determine how close a state is to lethal conditions
- no deaths are applied retroactively for days before activation

## Civilian mortality gate

A state becomes eligible for a mortality pulse only when:

- ordinary civilian systems apply
- Heat Stress is Extreme or Scorched
- lethal exposure has lasted long enough
- population is above the protected floor
- owner and controller proof is valid
- no state mortality transaction has already occurred for the current pulse
- mitigation has not reduced risk below the mortality threshold

Suggested confirmation bands:

| State condition | Minimum uninterrupted lethal exposure before ordinary recurring loss |
| --- | --- |
| Extreme with functioning water | 21 to 35 days |
| Extreme with severe shortage | 14 to 28 days |
| Scorched with rationed water | 10 to 21 days |
| Scorched with water-system failure | 5 to 14 days |

These values are planning anchors and require balance testing.

## Mortality strength

Mortality should use a bounded percentage or population-scaled exact amount with strong caps.

Strong multipliers:

- very high population exposure
- water-system failure
- high nighttime retention
- hospital overload
- active Famine
- war damage and low infrastructure
- very long lethal exposure

Strong reductions:

- cooling centers
- protected population priority
- functioning water delivery
- high infrastructure and supply
- successful evacuation preparation
- sustained local decline

The event must use the shared exact state-population loss helper and a registered heat-specific Deaths reason. Any recruitable-manpower credit created by the engine must be reconciled through the shared helper.

## Military mortality gate

A division or state military pool becomes eligible when:

- unit exposure is Critical
- the state is Extreme or Scorched
- the unit is undersupplied, in active combat, or without effective heat protocols
- the transaction uses a supported military casualty path
- a per-unit or per-state cooldown prevents repeated same-day loss

Loss should represent heat stroke, dehydration, sanitation failure, and failed logistics. It should scale with manpower and should not delete divisions through one unlucky pulse.

## Drought and wildfire interaction

Evolution I raises drought and wildfire risk under prolonged heat.

Event 51 owns:

- the persistent heat condition
- heat exposure
- drought pressure when no shared drought owner exists
- wildfire request eligibility

Event 013 owns:

- actual wildfire incident selection and impact
- wildfire damage
- wildfire smoke and ash contribution to Air Cleanliness
- wildfire aftermath and cleanup

A wildfire request should include state, intensity, heat exposure, vegetation or terrain suitability, existing disaster state, and generation proof.

Event 51 must not add a second contamination amount for the same wildfire.

## New decisions and reports

Evolution I can strengthen or unlock:

- expanded cooling centers
- hospital overflow support
- lethal-state evacuation preparation
- emergency military rest orders
- mass water delivery mission
- serious mortality reports

The category should still respect the visible-action cap.

## Evolution I success and failure

Success means lethal states are quickly mitigated and recurring deaths remain low or absent.

Failure means several states remain lethal, mortality repeats, hospitals and water systems fail, and Migration pressure rises.

# Evolution II: The Drying Earth

## Requirement

- Global Chaos at `600+`
- Evolution I active
- Event 51 and Evolution II enabled
- Not previously activated

## Core change

Sustained extreme exposure can create permanent environmental degradation. Heat episodes last longer and secondary Famine and Migration crises can become central.

## Exposure ledger

Every state has recorded extreme exposure from episode onset. Evolution II activates the permanent-degradation evaluation of that ledger.

The evaluation should consider:

- cumulative Extreme and Scorched days
- longest uninterrupted run
- current terrain family
- existing aridity
- water-system condition
- vegetation or agricultural role
- wildfire history
- prior episode degradation
- mitigation and recovery work
- population and infrastructure collapse

## Degradation warning

Permanent change requires a visible warning stage.

A state approaching degradation should receive:

- a state modifier or icon
- inclusion in hotspot or environmental summary
- a report or decision target
- one final mitigation opportunity where plausible

The warning should explain the physical process through soil, vegetation, wells, and failed recovery. It should not state raw hidden exposure points.

## Degradation stages

Evolution II can create:

- reduced environmental resilience
- persistent dryland or dried-terrain state
- desertification in suitable already dry or previously degraded states
- permanent water-capacity loss
- persistent agricultural penalty
- increased future Heat Stress vulnerability

Wasteland remains reserved for Evolution III.

## Episode duration

Evolution II increases:

- minimum active duration for severe episodes
- plateau length
- surge cap
- recovery lag
- persistence of local Heat Stress after global decline

It should not guarantee the maximum duration every time.

## Famine and Migration

Evolution II lowers the amount of additional failure needed for valid Famine and Migration requests, but it does not bypass their owner validation.

Expected outcomes:

- repeated harvest failure
- rural livelihood collapse
- internal movement toward cooler and better supplied states
- pressure on receiving cities and mountain regions
- food and water competition at destinations
- delayed return when permanent degradation remains

## Recovery

States that avoided permanent degradation can rebuild through water, agriculture, vegetation, and infrastructure recovery.

States that degraded retain their permanent ledger and map state. Later owner-approved restoration systems may reverse selected damage, but Event 51 cleanup does not.

# Evolution III: The Scorched World

## Requirement

- Global Chaos at `1000+`
- Evolution II active
- Event 51 and Evolution III enabled
- Not previously activated

## Core change

The highest intensity bands become capable of creating temporarily near-uninhabitable regions. Water, agriculture, civilian systems, military sustainment, and transport can fail together.

## Opening and mid-episode behavior

If Evolution III is active before a new episode:

- opening intensity receives a higher floor and wider volatility band
- more than one regional amplification can develop
- Scorched states can appear earlier
- permanent degradation evaluation begins from the start

If it activates during an episode:

- the current episode ceiling and duration budget rise within hard bounds
- a new surge becomes possible if terminal decline has not completed
- states already near the Scorched threshold can enter it quickly
- the escalation super-event remains gated by a separate real world milestone

## Near-uninhabitable state

A state becomes temporarily near-uninhabitable when:

- Heat Stress remains Scorched for a confirmation period
- water condition is Severe shortage or System Failure
- mitigation is insufficient
- population, infrastructure, or military load creates sustained exposure

Consequences can include:

- severe civilian mortality
- major Migration requests
- near-total agricultural failure
- strong factory and construction shutdown
- extreme supply and reinforcement penalties
- inability to sustain large armies
- evacuation or abandonment reports

The state remains part of the map. The condition is an extreme temporary crisis state, not automatic depopulation.

## Cross-continental milestone

The Evolution III super-event becomes eligible only after the world reaches a real escalation milestone, such as:

- several populated Scorched states across at least two continental regions
- the first cross-continental set of near-uninhabitable states
- one Scorched major capital plus a second severe region and a global intensity above the defined threshold

The super-event should fire once per campaign, not once per episode.

## Wasteland eligibility

Wasteland must remain rare. A state normally needs:

- Evolution III active
- existing desert or prior permanent degradation
- very long Scorched exposure
- failed mitigation
- severe water collapse
- major population and infrastructure decline
- no active successful recovery path
- episode and global wasteland caps

The implementation must prove safe map conversion through the required map tools. If actual terrain conversion cannot be validated, this feature remains blocked rather than being silently replaced by a generic modifier.

## Global displacement

Evolution III can produce large simultaneous Migration requests. Event 51 must stagger submissions and use owner capacity. It should not flood the Migration system with one request per state in one day.

Regional grouping can combine adjacent origin states into one validated incident where the Migration API supports it.

## Military collapse

Scorched fronts can become untenable. AI and player tools should support:

- organized withdrawal
- night movement
- reduced offensive tempo
- emergency supply corridors
- holding only key fortified positions
- evacuation of nonessential formations

A player can still choose to hold, but the cost should be visible.

## Evolution III recovery path

The Scorched World remains part of the active episode. Intensity eventually declines, temporary pressures clear by state, and cleanup restores repeat eligibility while permanent damage, lost population, altered terrain, Famine, and Migration remain under their owning systems.

## Evolution logging

For each stage:

- set the shared evolution event ID to 51
- use one consistent evolution type for the ordered track
- set stage to 1, 2, or 3
- set display tier from the current event-evolution convention
- include actor only if the shared design treats a global evolution as belonging to a specific country, which is not expected here
- gate record and recorded flag through `is_current_evolution_enabled = yes`
- update every required log and Event Details preview surface

## Evolution acceptance tests

1. Stage activation adds zero Chaos.
2. A disabled stage neither records nor unlocks behavior.
3. Evolution I deaths begin only after lethal exposure and use Deaths once.
4. Evolution II does not retroactively invent unrecorded exposure.
5. Evolution III super-event waits for its separate world milestone.
6. Wasteland requires prior degradation and cannot become common.
7. An episode still recovers and Event 51 remains repeatable after Evolution III.
