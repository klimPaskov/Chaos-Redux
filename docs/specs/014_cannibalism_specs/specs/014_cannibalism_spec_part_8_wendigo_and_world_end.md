# Event 014 Cannibalism, Part 8: Wendigo Connection and World-End Routes

## Terminal design principle

Event 14 has two world-end routes.

- Ordinary Hannibal world-end
- Wendigo Hannibal world-end

Neither is the default result. The event begins as a containable war-horror incident. Terminal routes require spread, failed containment, evolved content, country creation, unification, high chaos, territory, population consumption, and final route completion.

A world-end route can only trigger when global chaos is above 1000 and no other world-end is active.

## Existing Wendigo dependency

The alternate branch depends on the existing Chaos Redux Wendigo country. The specification does not guess its tag, focus tree, unit IDs, technologies, ideas, portraits, or shared classification.

Implementation must discover:

- exact country tag or dynamic identity
- creation routes
- leader and portrait
- unit types and recruitment systems
- national spirits and technologies
- special-country and nonhuman classification
- AI and decision hooks
- current player-facing naming

The alternate branch should reuse those systems and extend them. It must not replace them with a weak approximation.

## Wendigo merge trigger

The merge is evaluated during Hannibal's unification sequence.

Required conditions:

- Hannibal reveal conditions are satisfied
- a valid Wendigo country exists
- the Wendigo country is alive and controls meaningful territory or units
- no incompatible terminal world-end exists
- Evolution III is enabled

The branch can be presented as inevitable convergence or a rare choice depending on existing Wendigo lore. The implementation pass should preserve the established Wendigo event identity.

The scenario UI must not advertise this branch. Existing Wendigo presence changes the in-world unification outcome after the reveal.

## Player-control preservation

### Player controls a cannibal host

- host remains player-controlled
- Wendigo territory, units, and systems merge into the host or a transformed tag
- Hannibal becomes Wendigo Hannibal

### Player controls Wendigo country

- Wendigo country remains player-controlled
- cannibal network territory and units merge into it or a transformed tag
- Hannibal replaces the previous leader through a clear event
- the player does not lose control

### Player controls another warlord

- ordinary unification player-preservation rules apply first
- if the player's country is absorbed, the player transfers to the merged country with a clear choice and no silent control loss

## Wendigo Hannibal transformation stages

These are baseline stages inside the alternate route, not additional evolutions.

### Stage 1: Conjoined hunger

The two systems merge.

Effects direction:

- retain ordinary Larder
- retain all existing Wendigo units and technologies
- unlock transformed portrait
- create anchor states
- open alternate focus overlay and decisions
- register actual-nonhuman classification

The country is extremely powerful but still defeatable.

### Stage 2: Winter feeding network

The merged country establishes supernatural logistics and recruitment.

Effects direction:

- stronger cold and blizzard combat
- reduced supply dependence
- winter attrition against enemies
- additional Wendigo unit training
- consumption of controlled population strengthens both ordinary and supernatural units
- anchor states become visible strategic targets

### Stage 3: Terminal transformation countdown

A dynamic countdown begins after route, territory, consumption, and chaos conditions.

Countdown factors:

- number and strength of anchors
- population consumption
- winter victories
- controlled capitals
- Larder
- enemy disruption
- lost anchor states

Ordinary countries receive global counterplay missions. The merged country receives protection and acceleration decisions.

### Stage 4: Locked terminal form

When the countdown completes:

- set global `world_end`
- set Event 14 Wendigo terminal flag
- fire unique world-end super-event
- gate incompatible future systems
- grant the final impossible-to-defeat package
- direct AI toward complete world conquest and consumption

After lock, defeating the country is not an intended normal campaign path.

## Transformation anchors

Anchor states make the pre-lock route interactable.

Selection should prefer:

- major feeding capitals
- Wendigo sacred or mechanical locations already established by the existing system
- high-population controlled states
- cold or remote strongholds
- major ports or rail hubs connecting cannibal and Wendigo territory

Each anchor has:

- visible state modifier after the alternate reveal
- local garrison and special-unit capacity
- transformation progress contribution
- heavy population consumption
- unique assault or sabotage mission

Losing anchors delays or reverses progress before lock.

## Wendigo Hannibal military package

### Ordinary cannibal inheritance

- Scavenger Warbands
- Feast Cohorts
- Bone Guard
- origin specialists
- network cells
- Larder recruitment
- warlord commanders

### Wendigo inheritance

- every existing Wendigo unit type
- every existing recruitment decision
- relevant technologies and spirits
- established supernatural mechanics

### New transformed units

Role directions:

- transformed Bone Guard
- winter hunting packs
- anchor guardians
- spectral or supernatural courier units if consistent with existing Wendigo content

New units must fit existing Wendigo mechanics. The spec does not invent incompatible unit categories without repository inspection.

### Final power direction

After terminal lock:

- exceptional attack, breakthrough, organization, recovery, and reinforcement
- extreme supply-use reduction or supply independence
- severe enemy attrition and organization loss
- winter and blizzard dominance
- rapid Wendigo recruitment
- population and enemy losses converted into new strength
- resistance and occupation systems overwhelmed
- no ordinary diplomatic normalization
- global war access

The route should be stronger than ordinary Hannibal.

## Ordinary Hannibal world-end

### Eligibility

- chaos above 1000
- unified Hannibal country exists
- ordinary route active
- sufficient controlled territory
- sufficient population consumption
- mature global network
- final terminal focus or mission completed
- no world-end already active

### Pre-terminal counterplay

Ordinary countries can still win before lock by:

- destroying major Larder routes
- liberating network capitals
- breaking warlord loyalty
- seizing ports and courier hubs
- reducing controlled population and territory below threshold
- defeating Hannibal's main army and capital

### Terminal effects

- set `world_end`
- set Event 14 ordinary terminal flag
- fire unique ordinary world-end super-event
- stop automatic random event firing according to shared world-end behavior
- gate incompatible Event 14 branches
- convert surviving warlords and communes into the terminal state
- grant global war and absorption tools
- activate terminal population consumption

### Terminal military identity

Ordinary Hannibal remains human-origin horror. The final army becomes monstrous through organization, appetite, and violence rather than supernatural winter power.

Power themes:

- global Larder routes
- battlefield consumption
- enemy terror collapse
- rapid reinforcement
- mass warlord integration
- naval raiding and prison transport
- foreign cells behind every major front

## Wendigo Hannibal world-end

### Eligibility

- all ordinary world-end gates
- valid alternate merge
- transformation countdown completed
- required anchors active

### Terminal effects

- set `world_end`
- set Event 14 Wendigo terminal flag
- fire separate super-event with separate image, quote, remark, and music
- make the country effectively impossible to defeat
- retain all ordinary Hannibal bonuses
- retain all Wendigo bonuses
- add stronger supernatural recruitment, cold, supply, and enemy penalties
- direct conquest and consumption of the entire world

### Distinct presentation

The image should depict transformed Hannibal as the central subject. It should not resemble the ordinary world-end image with a snow filter. Every frame, icon, flag, portrait, and super-event asset needs separately designed source art.

## World-end super-event roles

### Ordinary terminal super-event

Role:

- irreversible global mobilization under revealed Hannibal

Image direction:

- Hannibal at the center of a massive cannibal army and feeding-state landscape
- explicit gore
- strong central composition
- no readable generated text

Quote direction:

- public-domain, scriptural, philosophical, or historical wording about insatiable hunger, devouring power, or judgment
- research required

Audio direction:

- unique licensed music
- relentless march, ritual percussion, or severe choral structure
- one to two minutes after editing where possible

### Wendigo terminal super-event

Role:

- terminal supernatural transformation and certainty of world consumption

Image direction:

- Wendigo Hannibal in frozen ruins with transformed armies
- explicit gore and cold body horror
- no borrowed living cultural regalia

Quote direction:

- public-domain wording about famine, winter, endless appetite, or extinction
- avoid invented Indigenous quotation
- research required

Audio direction:

- unique licensed music distinct from ordinary route
- cold choral, funeral, or severe orchestral structure
- real music, no drone or generated waveform

## Global defeat before terminal lock

Hannibal or Wendigo Hannibal can be defeated before terminal lock.

The victory should require:

- capital and command defeat
- anchor destruction where relevant
- enough warlord defection or capture
- liberation of major feeding states
- destruction of remaining communes and cells
- network stabilization period

A single capitulation should not automatically erase foreign cells.

## Defeat aftermath eligibility

A defeat aftermath package is justified only when:

- Hannibal was publicly revealed
- the threat controlled or devastated a broad region
- the war lasted long enough to reshape the campaign
- tracked population consumption crossed a major threshold
- multiple countries contributed to victory

Small regional containment does not create a global treaty or super-event.

## Defeat aftermath package

### Defeat super-event

Role:

- reflective global victory with severe cost

Image direction:

- liberated feeding capital, recovery teams, surviving prisoners, and ruined warlord symbols
- gore can remain visible, but the emotional center is survival and identification of the dead

Quote direction:

- public-domain wording about duty, memory, survival, or responsibility
- research required

Audio direction:

- unique reflective licensed music
- no triumphant reuse from another super-event

### Reconstruction system

- identify and bury victims
- restore state population tracking and administration
- reopen rail and port routes
- clear feeding-state modifiers
- rehabilitate coerced followers
- prosecute organizers and collaborators
- support locally cured countries

### International memory

A global compact or shared decision family can exist when the crisis was truly global.

Possible functions:

- prisoner-transfer inspection
- military burial protection
- anti-cult intelligence sharing
- relief convoy coordination
- warlord prosecution

The compact should not become a permanent universal faction unless campaign state supports it.

## Defeat of Wendigo Hannibal before lock

Stopping the alternate transformation before lock deserves a major global event and achievement route. The merged country can fall back to a powerful ordinary or partially transformed state depending on anchor loss and military outcome.

Possible outcomes:

- transformation broken and Hannibal returns to ordinary form
- Wendigo units remain but recruitment closes
- network fractures into warlords
- complete defeat and reconstruction

The final terminal form has no intended defeat aftermath because it represents the selected world-end state.
