# Event 32 specification, part 7: Assets, text, and achievements

## Visual direction

Event 32 should look mechanical, military, and period-authentic.

The visual language should focus on:

- missile canisters
- buried launch structures
- control rooms
- cable networks
- guidance equipment
- crews handling sealed components
- transport columns
- scorched launch pads
- damaged control panels
- warning displays
- guarded bunkers
- debris after a failed launch

Avoid:

- modern digital command rooms
- contemporary uniforms
- readable generated text
- modern missiles copied from one current real system
- cinematic science-fiction interfaces
- satellite views
- abstract map arrows as the main subject
- mushroom clouds for ordinary conventional missile content
- generic bomber art reused as the final Event 32 identity

## Source mode

The main report, news, and category images should use generated period-authentic documentary art because the simultaneous worldwide appearance is fictional.

The generated images should resemble photographs or press images from roughly the late 1930s through the early Cold War visual language, while remaining compatible with a 1936 campaign.

The prompt should avoid locking the image to one real country, one real missile type, or one modern launch system.

Icon families use generated icon art through the icon worker.

Existing Chaos Redux and vanilla assets may be reused only when the exact subject and consumer match. Reuse must be documented.

## Main image inventory

### Country report image

Purpose:

- first receipt of the missile program
- repeat-program expansion variants may reuse it if the event picture remains appropriate

Target:

- report-event canvas, normally `210x176`
- final engine consumer must be verified

Composition direction:

- military engineers and guarded crews around a newly completed buried launch entrance or missile canister
- equipment looks functional and heavy
- no visible national insignia that makes the image country-specific
- no readable labels
- no explosion

### First global news image

Purpose:

- first worldwide proliferation news event

Target:

- news-event canvas, normally `397x153`
- final engine consumer must be verified

Composition direction:

- several launch columns or transport silhouettes across a broad military landscape
- distant test plume or launch smoke
- press-photo realism
- the image should suggest many countries without using a literal world map

### Decision category picture

Purpose:

- identify the missile-program category

Target:

- inspect the canonical decision-category picture reference family
- current reference examples often use `114x101`
- final size follows the actual sprite and GUI consumer

Composition direction:

- underground command console or hardened launch entrance
- one clear focal subject
- no fake controls
- no dynamic values
- no painted buttons
- no text

### Decision category icon

Purpose:

- identify the category button separately from the larger category picture

Direction:

- compact missile canister and command-key motif
- simple silhouette designed for the exact category-icon consumer
- no reuse of a resized decision icon or idea icon

The category icon and category picture may share visual motifs. They require separate source art and separate manifest rows.

## Program and state icon families

### Missile program idea

Asset type:

- idea or national-spirit icon
- exact final size follows the canonical idea reference

Direction:

- missile canister, command key, and hardened bunker motif
- compact silhouette
- no focus-icon frame

Possible variants:

- initial program
- mature strategic command
- compromised command

Variants must be separate source art designed for the idea surface. Do not recolor one icon and call it a complete variant family.

### Launch-site state modifier

Direction:

- buried silo or launch gantry
- clear state-level infrastructure identity
- readable at state-modifier size

Possible variants:

- active
- hardened
- damaged
- compromised
- rogue

Only create variants that the implementation actually exposes.

### Readiness and command texticons

Required custom texticons:

- operational missile reserve
- launch readiness
- command control

The final cost strings and header use these icons consistently.

## Decision icon family

Each decision icon is its own decision-surface asset.

Required or likely icons:

1. survey launch state
2. establish command authority
3. replenish reserve
4. restore readiness
5. improve guidance
6. secure launch codes
7. harden site
8. expand capacity
9. establish secondary site
10. select missile target
11. precision strike
12. strategic barrage
13. saturation barrage
14. counterforce strike
15. integrate special payload
16. inspect incident
17. compensate neutral victim
18. suspend damaged site
19. rotate emergency codes
20. isolate site
21. send loyal forces
22. negotiate with command
23. scuttle site
24. verify warning
25. delay retaliation
26. sever network
27. restore retaliation network

The final implementation may merge icons when it merges actions. It may not leave a visible action on an unrelated generic icon without reporting it.

## Mission icon family

Likely mission icons:

- site survey
- secondary-site construction
- site repair
- strike preparation
- site recovery
- warning verification
- network restoration

Mission icons should remain visually distinct from clickable decision icons even when they share a theme.

## Raid or operation icons

When the native raid adapter is used, inspect the exact raid icon contract.

Possible required icons:

- conventional missile raid
- saturation missile raid
- chemical missile delivery
- biological missile delivery
- nuclear missile delivery
- thermonuclear missile delivery

Existing CBRN raid icons should be reused when they already identify the same payload and delivery surface. Event 32 should not create duplicate chemical or nuclear icon families only to change filenames.

## Achievement assets

Each achievement requires the full accepted triplet:

- eligible or unlocked art
- grey art
- not-eligible art

Achievement DDS files remain in the achievement root according to the event asset rules.

The achievement prompt lists eight planned achievements and icon directions.

## Scenario assets

SCN-015 should reuse the existing scenario window. It does not need a dedicated scenario image unless the final shared window requires one.

The scenario row can use the Event 32 category or event icon where the registry supports it.

## Animation review

No Event 32 animation is required by this design.

The event values, site states, warning states, and preparation missions can be communicated with static icons, native progress behavior, and ordinary state changes.

Do not create a transform-only pulse or fake animated warning light merely to add motion.

If implementation later proves that the shared decision category supports and benefits from an animated picture, that change requires a new accepted animation brief and the frame-animation workflow. It is outside the current accepted asset inventory.

## 3D review

Event 32 should reuse installed rocket-site, missile, raid, and explosion entities.

No custom unit, vehicle, aircraft, ship, creature, articulated asset, or map building is introduced.

A new 3D package is therefore not authorized.

If implementation discovers that the accepted operation cannot be represented with existing runtime entities, the coding agent must report the exact gap. It must not start paid model production without an accepted 3D brief.

## Asset paths

Recommended event-owned runtime grouping:

- `gfx/event_pictures/032_missiles/`
- `gfx/interface/decisions/032_missiles/`
- `gfx/interface/ideas/032_missiles/`
- `gfx/interface/state_modifiers/032_missiles/`
- exact raid or modifier folders required by the inspected consumer
- achievement files directly under `gfx/achievements/`

Recommended temporary workspace during active asset work:

- `docs/assets/032_missiles/`

The temporary workspace is deleted only after final assets are wired, durable provenance and coverage facts are promoted, and no runtime reference points into `docs/assets/`.

## Asset acceptance

An asset is complete only when:

- source art exists
- source mode is recorded
- prompt or source evidence exists
- processed PNG exists
- final DDS exists
- final dimensions and format are verified
- transparency is correct
- native-size review passes
- contact sheet exists where required
- sprite handoff exists
- final runtime path exists
- main implementation wires the sprite
- the manifest and permanent documentation agree

---

# Player-facing writing direction

## General tone

The event should use clear military and civilian observation.

Use:

- physical evidence
- working machinery
- guarded sites
- transport and maintenance activity
- command uncertainty
- unexplained crew knowledge
- debris and damaged infrastructure
- fear created by specific consequences

Avoid:

- generic strategic briefings
- abstract map summaries
- office paperwork as the emotional center
- generic statements that the world changed
- staged contrast formulas
- warning labels that tell the player how to feel
- final event text that lists raw mechanics

## First country report

### Viewpoint

The recipient government, military engineers, launch crews, and nearby civilians.

### Visible information

- a complete missile reserve and launch structure exists
- crews can operate it
- technical records do not explain its construction
- the government can use the program immediately
- security forces are already sealing the site

### Uncertain information

- who created the capability
- why several institutions recognize the procedures
- whether the program has deeper limits or later consequences

### Tone

Controlled alarm and practical military attention.

### Option direction

One acknowledgement option with dry official restraint. It should authorize custody and inspection without claiming the mystery has been solved.

## Repeat country report

### Visible information

- new components arrive
- guidance packages or engines improve
- reserve grows
- an existing site expands or another site begins operation
- crews treat the change as routine

### Tone

Growing normalization of something that remains unexplained.

### Option direction

Brief practical acceptance. Country or ideology variants can use researched military idiom, but plain wording is acceptable.

## First global news

### Viewpoint

Foreign observers, civilians near launch zones, military attachés, and press photographers.

### Visible information

- many countries activate missile sites within the same period
- test plumes and guarded transport appear
- governments restrict access
- no common supplier can be identified

### Tone

Global concern grounded in visible activity.

### Hidden information

- future evolutions
- exact reserve counts
- automatic-retaliation logic
- special payload access

## Conventional strike report

### Viewpoint

People and military units in the target state.

### Visible information

- impact on a named strategic target
- rail, factory, port, airfield, or launch-site damage
- fires, debris, and casualties
- likely actor when attribution is confirmed

### Tone

Direct and specific.

Do not write a generic sentence saying missiles have changed warfare.

## Neutral accidental strike

### Viewpoint

The neutral victim and foreign observers.

### Visible information

- missile debris or impact
- origin evidence
- deaths and damage
- contradictory claims when attribution is uncertain

### Tone

Anger, fear, and diplomatic urgency.

The text should not declare the incident a warning.

## Evolution text directions

### Saturation Arsenals

Show reserve expansion, repeated launch preparation, transport columns, hardened sites, and the industrial burden of sustained barrages.

### Unreliable Guidance

Show debris, wrong coordinates, damaged launch hardware, frightened border communities, and crews reviewing systems they no longer trust.

### Special Warheads

Show physical custody, protected handling teams, sealed payload sections, and the increased security around launch states.

Do not reveal a payload that the country does not own.

### Rogue Launch Commands

Show a site that no longer answers, loyal units arriving, codes being changed, and local commanders making demands.

### Automatic Retaliation

Show warning channels, countdowns, conflicting tracks, surviving command centers, and systems preparing a response before attribution is settled.

## Decision text direction

Decision names and descriptions should state the public action.

Good direction:

- concrete work
- exact target
- resource commitment
- visible tradeoff
- current program state

Avoid:

- raw helper names
- implementation language
- hidden chance
- future surprise
- long reward lists
- generic slogans

## Event Details direction

The Event Details text should explain:

- every country can receive a missile program
- repeat firings advance technology and expand arsenals
- launch states can change hands
- missiles can target strategic infrastructure
- higher chaos can create guidance, command, payload, and retaliation crises

It should not list exact evolution tiers, incident chances, or scenario bypasses.

## Spreadsheet direction

The workbook detail should match Event Details.

The evolution detail fields should explain each track's premise and visible change.

The scenario row should match final scenario localisation.

Do not paste implementation history or the old "mysterious missiles in the capital" wording into catalog fields after the rework.

---

# Achievement architecture

## Principles

Achievements should reward mastery of Event 32 systems.

They should require:

- several independent conditions
- event-specific tracking
- difficult restraint, recovery, or campaign use
- disqualifiers that prevent trivial setup
- no automatic unlock from one Event 32 firing
- no debug or force-trigger eligibility unless the project achievement rules allow it

The eight planned achievements are fully mapped in `032_missiles_achievement_prompt.md`.

## Tracking surfaces

Potential tracking includes:

- technology stage
- reserve peak
- readiness and control history
- site hardening
- launch count
- strike profile
- target profile
- civilian deaths caused
- neutral accidental strikes
- special payload use
- false warnings
- automatic-retaliation responses
- rogue-site recovery
- incident closure
- evolution unlocks
- scenario origin disqualifier
- world-end state
- country survival
- war outcome

Tracking must use stable flags, variables, incident receipts, and shared death data.

## Achievement presentation direction

Icon art should focus on one readable motif.

Possible motifs:

- paired command keys
- intact guidance gyroscope
- severed cable
- recaptured bunker
- untouched special-warhead seal
- precision sight over railway or factory
- five missile silhouettes in controlled formation
- hardened site under incoming tracks

Avoid:

- text
- flags unless country-specific eligibility requires one
- generic medals
- reused focus icons
- mushroom cloud on an achievement about conventional restraint
