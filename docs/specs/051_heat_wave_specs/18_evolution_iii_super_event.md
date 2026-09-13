# Evolution III Super-Event Specification

## Role

The super-event marks the first moment when the Heat Wave becomes a cross-continental habitability crisis under Evolution III. It is an escalation presentation. It does not end the campaign or replace the event's recovery path.

## Working identity

- Event owner: 051 Heat Wave
- Evolution: III, The Scorched World
- Working super-event label: The Scorched World
- Presentation count: Once per campaign
- Trigger type: Concrete global milestone after Evolution III activation

The final slot and numeric super-event ID require live registry inspection.

## Trigger contract

All of these must be true:

- Evolution III is active and enabled
- Event 51 has an active episode
- the super-event has not fired before
- no incompatible terminal presentation is active
- a validated cross-continental habitability milestone has occurred

The milestone should use one accepted route:

### Preferred route

At least two continental regions each contain a configurable number of populated Scorched states, with at least one near-uninhabitable state in each region.

### Alternate route

One major capital becomes near-uninhabitable while a second distant region contains several Scorched populated states and Global Heat Wave Intensity remains above the defined threshold.

The implementation should use one clear rule, not several loosely overlapping chances.

## Gameplay effect

The super-event itself should not apply a large hidden damage package. It presents a milestone that already exists.

Allowed bounded effects:

- record the once-per-campaign milestone
- apply the proposed event-owned Chaos change once
- unlock the final emergency decision phase
- strengthen world reaction reports
- update Event Details

Mortality, Migration, Famine, military collapse, and terrain change continue through their normal state systems.

## Title direction

The title should be short and tied to the established Evolution III identity. It should communicate a world where heat has changed ordinary habitation without using a generic apocalypse title.

The accepted evolution name can be used when slot duplication and localisation review support it.

## Description direction

The description should show several regions reaching the same severe condition:

- daytime streets emptying
- water under guard
- armies leaving exposed ground
- work moving into the night
- settlements sending people toward cooler regions
- formerly safe climates becoming dangerous

It should state what observers can see. It should not list exact thresholds, say that the event is a warning, or claim the world has ended.

## Button direction

The reaction should be brief, restrained, and severe. Suitable directions include:

- a biblical or classical allusion after source verification
- a practical admission that ordinary schedules and borders no longer fit the heat
- bitter understatement from a government that has run out of ordinary measures

Do not use a cheap joke around mass death or displacement.

## Quote research direction

No final quote is selected in this planning package.

Primary research direction:

- Revelation 16:8-9 in a verified public-domain or otherwise usable English text. The passage directly connects the sun and severe heat. The researcher should select only a short excerpt and verify translation rights and exact wording.

Secondary research direction:

- Dante's *Inferno*, Canto XIV, in a verified public-domain translation. The burning sand and falling fire imagery can fit environmental ruin, though it may feel more supernatural than the event.

Third research direction:

- public-domain poetry, travel writing, military memoir, or scripture about relentless sun, drought, and land emptied by heat.

The text researcher should compare at least five candidates and record attribution confidence, source work, year, rights status, and why the selected excerpt fits this exact milestone.

## Image direction

Use asset `HW-ART-09` from the asset specification.

The image should show a human landscape under oppressive pale heat:

- major road, city edge, rail line, or agricultural settlement
- sparse daytime movement
- guarded water distribution
- columns moving toward safer ground
- dust, smoke, or haze in the distance
- period-authentic vehicles, clothing, and infrastructure

Avoid:

- satellite or globe view
- planet on fire
- mushroom cloud
- fantasy meteorological symbols
- modern emergency equipment
- empty desert without evidence of society
- text in the image

## Audio direction

No final recording is selected because the live repository audio catalogue and downloadable source files were unavailable.

The audio researcher should first inspect the existing Chaos Redux audio catalogue and current super-event tracks to prevent reuse.

Preferred musical direction:

- slow, structured orchestral, choral, or sacred music
- severe sustained movement rather than action-trailer rhythm
- a recording between one and two minutes after an approved edit
- public-domain or clearly licensed recording with composition and recording rights checked separately

Potential composition search directions:

- fire, drought, judgment, desolation, or funeral music from public-domain composers
- restrained sacred choral work with a legally reusable recording
- a public-domain orchestral passage with low brass, strings, or choir and no modern cinematic production

Musopen and Wikimedia Commons can provide candidate pools, but every file's description page and recording rights require separate verification.

Reject:

- drones, test tones, noise beds, stingers, and generated audio
- copyrighted film or game music
- a track already assigned to another completed super-event without explicit user approval
- a public-domain composition paired with an unverified recording

## Sound implementation contract

After selection:

- preserve the source download and rights record
- convert to a game-ready WAV
- place it under `sound/051_heat_wave/`
- create one unique base sound definition
- create required volume-wrapper soundeffects
- assign a unique super-event audio ID
- set `global.current_super_event_audio_id`
- call the settings-aware `play_current_super_event_sound = yes` helper
- update the canonical music track catalogue
- document title, composer, performer, source, license, duration, edits, IDs, and paths

## Slot and image wiring

Implementation must:

- reserve or select the correct super-event slot
- set the matching visibility state
- update `GetSuperEventImage` or current equivalent
- align title, description, button, quote, image, and audio to the same slot
- prevent unrelated slot content from appearing
- use the one-time campaign guard

## Event Details and documentation

Permanent documentation should record:

- trigger milestone
- slot
- title
- quote and source
- image and provenance
- audio and rights
- audio ID and sound definitions
- once-per-campaign state
- gameplay unlock or Chaos milestone

## Validation

- fires only after Evolution III and real cross-continental conditions
- does not fire from one isolated Scorched state
- fires once per campaign
- presents the correct image, text, quote, and audio
- uses settings-aware volume
- does not apply duplicate state damage
- leaves the episode active so its decline, recovery, and cleanup still occur
- remains correct after save and reload
