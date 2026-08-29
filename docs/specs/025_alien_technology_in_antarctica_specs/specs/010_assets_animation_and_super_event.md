# Assets, animation, and super-event

## Asset direction

Event 025 needs a coherent visual package that supports the expedition race and its five evolutions.

The package should look like a 1930s or wartime Antarctic scientific expedition encountering an impossible object. Art should use period ships, aircraft, clothing, instruments, tents, radios, tracked vehicles where appropriate, and photographic or painted-documentary realism.

Avoid modern polar stations, satellites, modern snowmobiles, contemporary survival gear, modern digital screens, science-fiction user interfaces, generated readable text, and cinematic blue-orange grading.

## Source mode

The spacecraft, impossible materials, survivor traces, and evolution scenes are fictional. Generated event art is the default source mode.

Historical research images may be used as composition and equipment references. They must not be wired as final art unless a specific accepted asset requires real archival material and its rights are documented.

The event introduces no real person and requires no character portrait.

## Opening super-event

Event 025 uses one opening super-event.

### Role

First reveal of a global scientific and strategic race.

### Trigger

Immediately after the major event is selected and the participant-entry sequence is initialized.

### Presentation direction

The super-event should show an impossible descent or distant wreck in an Antarctic landscape, with a human expedition-scale element that establishes size and period.

Preferred composition:

- broad ice field or shelf
- dark or luminous damaged craft partly obscured by snow, mist, or distance
- one period ship, aircraft, radio team, or small expedition group for scale
- no clear surviving alien
- no readable markings
- no modern machinery

The image should communicate discovery and urgency. It should not reveal the technology family or later evolutions.

### Required image output

- source PNG
- processed preview
- final `457x328` DDS or the exact current super-event consumer size verified in the live repository
- source prompt and generation evidence
- manifest and permanent provenance note
- sprite handoff

### Text research

The title, quote, and cultural remark remain research tasks.

Quote direction:

- polar exploration
- discovery beyond knowledge
- uncertain horizons
- the danger of possession
- scientific ambition

Use a verified public-domain, historical, literary, philosophical, or expedition source. Do not invent a quote.

Button direction:

- short expeditionary or scientific reaction
- serious or dry understatement
- a brief cultural allusion only when verified and tonally appropriate

### Audio research

The cue should be structured music with cold, remote, exploratory tension.

Preferred source families:

- public-domain orchestral recording
- licensed chamber or choral work
- licensed polar documentary music
- public-domain early modern or classical composition with a usable recording

The cue needs a clear source title, composer, performer or recording source, license, duration, legitimate download, conversion record, unique audio ID, and a final WAV no longer than two minutes unless an exception is documented.

No synthesized drone, test tone, noise bed, placeholder stinger, or unlicensed film or game track is allowed.

## Winner news image

A global winner announcement needs one news image.

Direction:

- recovered component under guarded scientific examination
- period laboratory or field shelter
- several technicians in period clothing
- impossible material as the clear subject
- winner identity supplied by text and flag, not generated signage

Target the current vanilla or Chaos Redux news-event canvas, commonly around `397x153`, after live reference inspection.

## Report-event images

The implementation should authorize only report images that represent distinct recurring or milestone scenes.

Required report image families:

1. expedition departure
2. Antarctic outpost established
3. survey and radio triangulation
4. fragment recovery
5. route or outpost sabotage
6. rescue operation
7. final recovery approach
8. survivor trace or opened compartment
9. militarised outpost or blockade
10. wreck fragmentation field
11. alien-system containment accident

The implementation may reuse one image across closely related reports when the scene remains accurate. It may not reuse the opening super-event image for every report.

Target the current report-event canvas, commonly around `210x176`, after direct reference inspection.

## Expedition Board assets

### Full background

One complete board background with safe text and control regions.

### Header elements

- event crest or expedition emblem
- phase frame
- urgent mission indicator

### Main values

Separate icon families for:

- Expedition Progress
- Logistics Readiness
- Exposure Risk
- Alien Dependence

Exposure Risk and Alien Dependence are separate art because they communicate different states.

### Route and outpost states

Icons for:

- direct route
- long maritime route
- sponsored route
- improvised route
- open route
- interrupted route
- outpost planned
- outpost functioning
- outpost damaged
- outpost contested
- outpost abandoned

### Sector states

Graphics for:

- unknown
- surveyed
- probable
- confirmed
- blocked
- contested
- recovered
- buried or lost

Sector shapes need one shared Antarctic projection and consistent alignment.

### Rival card states

- normal
- selected
- cooperative
- hostile
- suspected interference
- public incident
- withdrawn
- winner

### Action states

Every button family needs:

- normal
- hover
- pressed or selected
- disabled
- insufficient cost
- cooldown
- warning
- active mission
- completed

The GUI may reuse one verified project button frame when it fits. Event-specific action icons remain distinct.

## Decision icons

Decision icons should be designed for their runtime size, commonly `32x32`, and must not be resized focus or idea icons.

Required action icon subjects:

- commit expedition
- select route
- charter staging access
- reinforce supplies
- build outpost
- survey sector
- study signal
- shield instruments
- jam signal
- steal coordinates
- spread false coordinates
- sabotage route
- defend outpost
- rescue rival crew
- exchange data
- collect fragment
- stabilize wreck
- launch final recovery
- withdraw
- contain systems
- destroy material
- transfer custody
- conceal research
- integrate systems

Closely related variants may share a coordinated family but need separate source art suited to the decision icon role.

## Decision category art

The ordinary decision category should use a strong static category picture that shows expedition equipment, a map, and a radio room without fake controls.

The full Expedition Board carries the dynamic mechanic. The category picture provides identity and an entry point.

An animated category picture is optional only when it uses real source frames and adds useful active-signal state. It is not required for event completion.

## Idea and dynamic-modifier icons

Required idea icon directions:

- Secured Antarctic Material
- Controlled Alien Research
- Integrated Alien Systems
- Shared Recovery Commission
- Sealed Antarctic Archive
- Compromised Alien Program
- Alien Systems Integration

These are `64x64` idea or national-spirit assets designed independently from decision icons.

Temporary route, weather, or outpost modifiers should reuse existing vanilla icons where the meaning is exact. Create a new state or modifier icon only when a visible new concept has no good precedent.

## Evolution art

### Evolution I: Active Signal

- radio waveform or luminous pulse over the ice
- instrument interference
- animated signal loop with static fallback

### Evolution II: Something Survived

- tracks, opened hatch, damaged camp, or moving machine trace
- no clear humanoid alien face in the first reveal
- later confirmed survivor art may show a machine, organism, or unclear figure according to the campaign result

### Evolution III: Militarised Antarctica

- warship, aircraft, guarded outpost, or submarine operating near the ice
- period-correct military hardware
- no modern weapons

### Evolution IV: Wreck Breaking Apart

- fragments scattered over ice and crevasses
- unstable light or material failure
- several recoverable sites visible

### Evolution V: Technology Changes Its Users

- period laboratory or command room reorganized around alien systems
- altered posture, procedure, or machinery
- avoid body-horror spectacle unless a specific accident requires it
- animated Dependence circuit or pulse only where it clarifies the active state

## Frame animation requirements

Required final animation candidates:

1. signal pulse loop
2. survivor trace loop
3. fragment instability loop
4. Dependence activity loop

The implementation may accept fewer loops when direct GUI precedent shows that a static state communicates the mechanic better. The opening super-event itself does not need animation.

Each accepted loop needs:

- animation brief
- frame plan
- separate source frame PNGs
- processed exact-size frames
- contact sheet
- preview GIF for review only
- horizontal sheet PNG
- horizontal sheet DDS
- static fallback PNG and DDS
- `frameAnimatedSpriteType` handoff
- verified target surface

No final motion may be created only by moving, scaling, rotating, blurring, recoloring, or changing opacity on one still.

## Achievements

Every achievement needs a native achievement triplet:

- eligible or unlocked image
- grey image
- not-eligible image

The filenames must match the final achievement IDs and remain in the root achievement folder according to engine convention.

Achievement art directions are listed in the achievement specification and asset matrix.

## No portrait package

Event 025 introduces no named scientist, commander, leader, operative, or advisor.

Do not invent an expedition leader merely to add a portrait. Country institutions and national expedition teams are represented through flags, icons, and report art.

## No flag package

No new country, cosmetic tag, faction, or route identity is created. Existing country flags are used on participant cards and reports.

## No required 3D package

The event does not require a map entity, custom spacecraft model, custom building, unit model, counter, or skeletal animation.

The expedition race is represented through events, the board, icons, and report art.

Event 036 is the better owner for any future reusable spacecraft or alien-aircraft 3D model because it has a direct aircraft and production consumer. A later cross-event asset plan may create a shared model, but Event 025 must not be blocked by it.

## Asset folders

Expected event-scoped runtime structure:

```text
gfx/event_pictures/025_alien_technology_in_antarctica/
gfx/interface/025_alien_technology_in_antarctica/
gfx/interface/decisions/025_alien_technology_in_antarctica/
gfx/interface/ideas/025_alien_technology_in_antarctica/
gfx/super_events/025_alien_technology_in_antarctica/
sound/025_alien_technology_in_antarctica/
```

Achievement DDS files remain in `gfx/achievements/` with full event-owned IDs.

The exact active paths must follow live repository conventions and engine consumers.

## Temporary asset workspace

During production use:

`docs/assets/025_alien_technology_in_antarctica/`

Keep source art, prompts, processed previews, audio sources, frame plans, contact sheets, manifests, and handoffs there while work is active.

Before full event completion:

- move final runtime assets into engine-facing folders
- promote durable provenance and review facts into permanent docs
- verify no runtime reference points into `docs/assets/`
- delete the complete event-scoped temporary workspace

Retain it when assets remain blocked or under review.

## Asset manifest fields

Every asset row records:

- stable asset ID
- event ID and slug
- asset type
- intended consumer
- target size
- source mode
- generation prompt or source URL
- rights or license note
- source and final paths
- sprite name
- animation frame count when applicable
- review status
- final runtime status
- blocker or exception

## Visual acceptance gates

- period fit is clear
- no modern equipment or digital interfaces
- no generated readable text
- no fake UI controls painted into backgrounds
- icons remain readable at native size
- transparent icons have real alpha and no white halo
- separate icon types have separate source art
- sector pieces align to one projection
- animated states have real source frames
- static fallbacks exist
- final DDS files use the verified format
- all sprites have live consumers
- no required asset is a placeholder

## Super-event completion gate

The super-event is complete only when all of these agree:

- slot
- trigger
- visibility flag
- image
- title
- description
- button text
- verified quote
- unique audio ID
- final licensed WAV
- settings-aware sound wrappers
- scripted localisation
- player localisation
- event docs
- audio catalogue
- catalog wording where applicable

The planning package does not choose an unsupported quote or audio source. Those remain bounded research tasks for the specialized subagents.
