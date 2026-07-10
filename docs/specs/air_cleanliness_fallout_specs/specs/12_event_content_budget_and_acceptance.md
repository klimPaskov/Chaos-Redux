
# Event Content Budget, Quality Bar, and Acceptance Criteria

Working labels in this file are not final localisation.

## Scale target

The full Fallout event implementation should contain roughly 660 to 910 unique event blocks.

The release floor is 660 manually reviewed event blocks. Expansion toward 910 is allowed only after every added block receives the same choice, AI, memory, effect, and cleanup review as the release floor.

The implementation count target is detailed in `matrices/fallout_run_event_budget_matrix.md`.

## Coverage target

Required coverage:

- complete transition and orientation
- 70 or more global survival and society blocks
- 90 or more regional blocks
- 120 or more archetype blocks
- at least two unique chains for every successor candidate that can spawn
- 50 or more character and leader blocks
- 45 or more diplomacy, trade, war, and settlement blocks
- 35 or more cause-memory, mutant-fiction, and altered-ecology blocks
- 40 or more recovery and late-world-order blocks

One event may satisfy more than one narrative role. It should have one primary ownership family for counting and fatigue.

## Per-campaign target

A human country should normally see roughly 90 to 180 meaningful Fallout events over ten years.

The run budget matrix controls:

- ordinary event cooldown
- major arc count
- crisis interruption
- broadcast frequency
- bilateral reservations
- small-country and large-country variation
- late-game pacing

A library of hundreds of events must not become hundreds of popups in one game.

## Event block quality

Every event block needs:

- eligibility
- scope
- event class
- actor
- visible information
- one primary family
- cooldown
- memory behavior
- option meaning
- actual effects
- AI choice
- failure or cancellation behavior
- follow-up or closure
- log behavior
- art direction or approved shared image family
- localisation direction
- multiplayer behavior where relevant

## Multi-event chain quality

Every major chain needs:

- opening
- conflict
- choice
- delayed result
- success, partial success, and failure where appropriate
- institutional or character memory
- later callback
- cleanup

A major chain should not end with one small modifier.

## Mechanical integration

Events must connect to the accepted systems.

Required integration surfaces:

- food
- water
- medicine
- salvage
- power
- shelter
- radiation burden
- survival cohesion
- reclamation capacity
- old-world memory
- winter phase
- climate adaptation
- state population
- shared Deaths
- buildings
- state category
- state class
- decisions and missions
- focus branches
- idea lifecycle
- leaders, advisors, and commanders
- diplomacy
- trade
- compact cohesion
- war and settlement
- country identity
- AI behavior

No event needs every surface. The whole library must cover them.

## Flavour with effects

Routine incidents must still change play.

Accepted small effects:

- a modest survival-resource change
- a one-state repair or damage pressure change
- a character loyalty change
- a relationship memory change
- a future event weight
- a local support change
- a short mission
- a small population movement
- a market or corruption change
- a climate adaptation change

A tiny flat modifier with no future connection does not count.

## Choice quality

Choices should:

- use different costs
- create different beneficiaries
- create different future risks
- be valid for current country
- have AI logic
- avoid obvious best answers
- show visible baseline consequences
- keep hidden surprises hidden
- respect route and character memory

Repeated choice patterns must be adapted.

## Tone quality

The library needs tonal range.

Required proportions by direction:

- no more than two thirds of routine events should be purely negative
- at least one third of routine and society events should contain competence, recovery, affection, humor, celebration, discovery, or mixed outcomes
- major crises remain serious
- atrocities and mass death do not use cheap comedy
- technical events use concrete detail
- cultural references require research

## Regional quality

Regional content passes when:

- geography matters
- climate cues differ
- infrastructure differs
- food systems differ
- travel and contact differ
- historical material is researched
- living communities are not reduced to stereotypes
- local institutions affect choices
- no region is only famine, raiders, and ruins

## Archetype quality

Archetype content passes when:

- each archetype has ten or more anchor chains
- mature political outcomes differ
- internal conflict differs
- citizenship differs
- military logic differs
- diplomacy differs
- AI differs
- archetype change cleans up obsolete content

## Country quality

A selected successor passes when it has:

- orientation
- opening chain
- domestic identity chain
- external relationship chain
- late memory chain
- local routine incidents
- recurring character or institution
- route-specific AI
- unique visual identity
- failure callbacks
- Year 5+ content

Shared focus and event skeletons do not remove this requirement.

## Character quality

Characters pass when:

- they affect mechanics
- they persist
- they can change office or status
- their death or exit has consequences
- names and portraits match region and gender
- councils use institutional identity
- apprentices and second-generation characters appear
- AI can resolve their arcs

## Diplomacy and war quality

Diplomacy passes when:

- contact requires a route
- recognition matters
- trade moves actual resources
- aid creates memory
- compacts have cohesion and internal events
- wars have causes
- war conduct affects population and infrastructure
- settlements handle borders, resources, prisoners, and integration
- both sides store memory

## Mutant-fiction quality

Mutant content passes when:

- it is explicitly fictional
- societies have political variety
- biology does not determine morality
- medical consent and abuse are treated as political questions
- human-mutant diplomacy has real branches
- altered ecology has regional gates
- assets do not use zombie language
- no zombie event id, namespace, file, or asset is reused

## Climate visual quality

Air Winter presentation passes when:

- the ordinary map looks colder
- the dedicated mapmode remains precise
- tropical and desert phases do not default to northern snow
- cold, ash, and radiation remain distinct
- visual state matches gameplay
- recovery is visible
- performance is bounded
- engine support is proven locally
- no mapmode-only substitution is hidden

## Anti-bloat check

Remove or merge content when:

- two events have the same trigger, choice, effects, and follow-up
- a routine incident repeats a major chain without adding memory
- an event exists only to display text
- a character has no later use
- a country-specific event differs only by name
- a regional event ignores region
- a late event does not recognize prior choices
- a popup would work better as a mission update or tooltip
- art production exceeds the event's importance

Depth comes from connection, not raw count.

## Audit stages

### Tranche audit

After every 40 to 60 implemented event blocks:

- duplicate check
- family fatigue check
- option-effect check
- AI check
- memory cleanup
- art coverage
- localisation coverage
- event log
- save-load
- active arc count
- visible event volume

### Regional audit

After each region:

- local specificity
- state and route validity
- historical research
- climate presentation
- contact topology
- AI
- assets

### Country batch audit

After each successor batch:

- unique opening
- unique domestic chain
- external chain
- late chain
- characters
- focus and decision integration
- flags and portraits
- AI
- failure routes

### Final audit

Run:

- scripted-system audit
- country-package audit
- focus-tree audit
- decision-mission audit
- localisation audit
- documentation curation
- spreadsheet update
- event-completion audit
- improvement-loop closure pass

## No completion claim when

Do not claim completion if:

- the event catalogue is still mostly categories
- successor events are copied
- AI is missing
- visible cold exists only in the mapmode
- climate visual support is unproven
- event effects do not reach mechanics
- recovery ends after a few events
- second-generation politics is absent
- war settlements are absent
- mutant fiction is presented as science
- Fallout events exist outside the dedicated file
- zombie assets or ids are reused
- manual scenario id was assumed
- any accepted event layer remains queued without a reason

## Final quality bar

A ten-year playthrough should produce a country history that another playthrough does not repeat.

The player should remember:

- who controlled food
- who was admitted
- who kept the power on
- who led the first expedition
- which neighbor answered
- what treaty was signed
- why the first war began
- how the war ended
- which leader survived
- what the children learned
- what the sky looked like
- what state recovered
- what old identity was kept or rejected
- how altered and machine societies were treated
- what world order began to form
