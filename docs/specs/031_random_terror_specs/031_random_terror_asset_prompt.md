# Event 31 Random Terror asset-production prompt

## Task

Create the complete final visual asset package for Event 31 Random Terror.

The source specification is the folder:

`docs/specs/031_random_terror_specs/`

Read every specification part, the country-package matrix, the achievement file, the research notes, and the super-event prompt before production.

Follow:

- `AGENTS.md`
- `chaos-redux-event-assets`
- `.agents/skills/chaos-redux-event-assets/references/portrait-production.md`
- `chaos-redux-frame-animation` for the authorized entity animation
- `chaos-redux-super-events` for super-event image coordination
- `chaos-redux-subagents`

Use the narrow asset subagents with `fork_context=false` and context-complete prompts.

Route every character portrait to `chaosx_portrait_creator`.

Route fictional non-icon event, news, category, faction, flag, and super-event art to `chaosx_generated_event_art`.

Route focus, idea, decision, mission, state-modifier, map-mode, faction-surface, and achievement icons to `chaosx_icon_artist`.

Use `chaosx_asset_source_researcher` only for real historical visual research that is genuinely needed. Event 31 actors and scenes are fictional, so generated period-documentary art is normally the correct mode.

The main implementation agent owns final non-portrait `.gfx`, GUI, gameplay, localisation, and runtime wiring. The portrait worker owns portrait-specific `.gfx` and existing character portrait references within its normal exception.

## Hard representation rules

Every Event 31 organization, leader, flag, emblem, country identity, slogan, and faction is fictional.

Do not use:

- a real extremist organization name
- a real extremist flag or emblem
- real extremist uniforms or propaganda
- sacred Islamic calligraphy as hostile branding
- a depiction of Allah
- Quran recitation, the call to prayer, or Islamic sacred chant as enemy audio
- ethnic, religious, or national caricature
- modern body armor, weapons, vehicles, optics, streets, or command rooms
- generated readable text
- graphic gore
- meme imagery
- copied political symbols that falsely identify an ordinary community with terrorism

The fictional jihadist branch appears only in Evolution IV and later.

Muslim governments, communities, clerics, soldiers, and fictional religious councils can be its main opponents.

Visuals for their opposition should show public protection, civic resistance, military defense, relief, local leadership, and rejection of the movement's claim.

They should not become a visual disclaimer pasted onto otherwise stereotyped art.

## Reference inspection

Before creating each asset type, read the reference-library rules and inspect the matching contact sheet and source catalog under:

`C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/`

Inspect the exact installed-vanilla consumer and closest Chaos Redux precedent where engine behavior or final canvas matters.

At minimum inspect:

- report art
- news art
- super-event art
- country leader portraits
- advisor dossiers only for explicitly authorized characters
- flat flags at normal, medium, and small sizes
- national focus icons
- idea and national-spirit icons
- decision icons
- mission icons
- decision category pictures
- state modifier icons
- faction icons
- achievement triplets
- any current map-mode sprite family used by Chaos Redux

Do not wire, recolor, trace, or ship reference images.

If a required contact sheet is missing, create it with filenames and native dimensions, then update the reference README and catalog before production.

## Temporary workspace

Use:

`docs/assets/031_random_terror/`

Recommended structure:

```text
docs/assets/031_random_terror/
  manifest.md
  prompts/
  source_png/
  processed_png/
  contact_sheets/
  portraits/
  flags/
  event_art/
  icons/
  animations/
  super_events/
  notes/
  gfx_handoff.md
```

This is a temporary evidence and review workspace.

Keep it while work is active, blocked, or awaiting review.

Before the event is fully complete, promote durable provenance, review, and runtime crosswalk facts into permanent event or plan documentation, place final runtime assets in engine folders, verify that no runtime reference points into `docs/assets/`, and delete the complete event-scoped workspace.

Do not delete the durable portrait archive under `docs/assets/portraits/`.

## Stable runtime folder direction

Use event-scoped folders where the engine accepts explicit paths.

Suggested roots:

- `gfx/event_pictures/031_random_terror/`
- `gfx/interface/decisions/031_random_terror/`
- `gfx/interface/ideas/031_random_terror/`
- `gfx/interface/goals/031_random_terror/`
- `gfx/interface/event_31_random_terror/`
- `gfx/super_events/031_random_terror/`
- event-owned leader folders that match the verified character consumer

Flags remain in the standard `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/` roots with verified tag or cosmetic-tag filenames.

Achievement DDS files remain directly under `gfx/achievements/` and use the full achievement IDs.

The final implementation agent can refine folders after inspecting live precedents. Preserve stable basenames and sprite proposals once registered.

## Decision category pictures

Create three static category pictures.

### Government response

Working basename: `random_terror_government_response_category`

Direction:

A 1936 to 1945 documentary-style emergency response after a fictional attack. Show damaged transport or public infrastructure, guarded civilians, relief workers, and period security personnel. The image should show protection and material disruption.

Avoid a tactical map, fake controls, real insignia, modern uniforms, or a generic command table.

### Territorial actor command

Working basename: `random_terror_actor_command_category`

Direction:

An improvised command center inside a captured civic, railway, warehouse, or industrial building. Show mixed fictional militia and defecting regulars, damaged infrastructure, supply shortages, and improvised administration.

Avoid a triumphant propaganda tableau or copied real movement imagery.

### Final state command

Working basename: `random_terror_false_revelation_category`

Direction:

A transformed terminal command space with impossible light or shadow, synchronized messengers or officers, damaged period architecture, and a sense of worldwide unrest. The entity may be suggested indirectly.

Do not depict a deity or use sacred calligraphy.

Inspect the active category-picture consumer before fixing target size. The reference family currently uses `114x101` examples, but the live sprite and GUI decide the final canvas.

## Report-event art

Create a coordinated generated period-documentary family for these accepted scenes.

1. damaged railway and civilian evacuation
2. guarded station and emergency transport
3. hostage or public-building crisis shown indirectly
4. burned depot and captured-equipment aftermath
5. intelligence raid aftermath with recovered documents
6. relief workers and victims after an attack
7. border corridor under military protection
8. armed enclave in a captured town
9. defecting soldiers or police joining an insurgency
10. national capital under emergency guard
11. rival extremist groups fighting over a border or urban district
12. fictional Muslim religious and civic leaders publicly rejecting the jihadist movement
13. territorial actor proclamation inside a captured public building
14. fictional jihadist international gathering with original emblems
15. synchronized uprising during the Final Jihad
16. liberation and reconstruction after the movement's defeat

Give each scene a stable basename, source prompt, processed preview, final DDS, manifest row, and contact-sheet entry.

Use one event-art family style, but vary composition and subject enough that the images do not look like repeated crops of one scene.

## News-event art

Create distinct wider-composition news images for:

1. first major coordinated international attack wave
2. first durable territorial Event 31 country
3. formation of the Jihadist International
4. activation of the Final Jihad
5. defeat of a major territorial network
6. defeat aftermath of The False Revelation

The reveal of The False Revelation itself uses the dedicated super-event image.

News images should read at the verified news-event canvas and should not be resized report images.

## Portrait pool

Create a prebuilt fictional pool large enough to avoid visible duplicate leaders during a high-intensity or Maximum scenario.

Minimum full leader and council masters:

- `6` fictional military-command leaders
- `6` fictional clandestine coordinators or council delegates
- `6` fictional revolutionary or ideological leaders
- `6` fictional criminal-political leaders
- `6` fictional millenarian or cult leaders
- `8` fictional jihadist-route leaders
- `6` fictional institutional council portraits
- `1` False Revelation entity portrait

Total minimum: `45` masters.

Every one-person portrait uses `fictional_high_chaos` through `chaosx_portrait_creator`.

Required portrait qualities:

- exact `156x210` full leader framing
- period photographic treatment
- head and shoulders visible
- role-specific clothing and environment
- a memorable invented motif
- varied age, gender, appearance, and pose
- no real-person likeness target
- no ethnic or religious caricature
- no real extremist insignia
- no modern props
- no readable text
- matching name and gender metadata
- independent identity, framing, and provenance review

Council portraits are fictional institutional subjects. Use a staged group or symbolic institutional composition only after the portrait brief authorizes it and identifies the institution's role.

Review the complete portrait contact sheet for duplicate faces, accidental resemblance, stereotype, framing drift, and route mismatch.

Preserve every portrait's source prompt and evidence under the portrait worker's durable archive contract.

## Route-critical advisor and commander portraits

Do not create a blanket advisor family.

Authorize no more than `12` route-critical fictional characters unless the final country-package implementation proves another character has a clear gameplay role.

Potential roles:

- field commander
- quartermaster
- civil administrator
- foreign liaison
- intelligence chief
- ideological organizer

A character who appears as both leader and advisor needs separately designed role-specific outputs.

An advisor dossier uses the verified `65x67` advisor reference family and cannot be satisfied by shrinking a `156x210` leader portrait.

Record every authorized character and consumer in the manifest before production.

## False Revelation entity portrait and animation

Create one final static entity portrait at `156x210`.

The entity is impossible and ambiguous. It can appear humanlike, shadowed, masked by light, optically inconsistent, or physically difficult to interpret. Avoid a generic horned demon, alien cliché, sacred figure, or real-person resemblance.

Create one animated portrait or transparent portrait overlay only after the implementation agent verifies the exact GUI consumer and approves the mode.

Follow `chaos-redux-frame-animation`.

Required animation package:

- written brief
- frame plan
- separately generated or edited source frames
- processed frames at exact target size
- horizontal sheet PNG
- sheet DDS
- static fallback PNG and DDS
- review GIF
- contact sheet
- stable static and animated sprite proposals
- verified frame count, FPS, loop, anchor, and `play_on_show` expectation
- GUI and scripted-GUI handoff when an overlay is used

The motion should show subtle impossible optical change through source frames. A shifted still, scale pulse, glow filter, opacity loop, or GIF conversion is invalid.

## Flag pool

Create flat fictional flag designs with ImageGen.

Minimum pool:

- `24` ordinary Event 31 actor flags
- `8` fictional jihadist-route flags
- `4` merger or transnational-command flags
- `1` False Revelation final flag

Every selected flag needs normal, medium, and small variants.

The ordinary pool should cover military, clandestine, revolutionary, criminal-political, and millenarian profiles.

Requirements:

- flat graphic design
- simple geometry and strong contrast
- readable at small size
- exact transparent or opaque treatment from vanilla precedent
- no text
- no fabric folds
- no flagpole or scene
- no lighting, perspective, or painterly texture
- no real extremist symbol
- no sacred calligraphy
- no copied religious or ethnic emblem without a cited and approved reason
- no duplicate design assigned to two simultaneous actors

Create a contact sheet showing all three sizes and route classification.

The parent must perform the full tag and cosmetic-tag audit before final filenames are locked.

## Faction emblems

Create separate original emblems for:

- regional Event 31 coordination structure
- transnational network confederation
- Jihadist International
- Final Jihad command

Create an anti-Event 31 terminal coalition emblem only if the final faction implementation uses a dedicated visible identity.

Faction emblems must be designed for the faction surface and cannot be resized country flags.

## State activity and map-mode assets

Create distinct icons or sprites for:

- dormant activity
- active cell
- entrenched network
- armed insurgency
- lost local control
- recovery or restored authority
- damaged transport
- relief corridor
- safe haven
- foreign corridor
- capital infiltration
- forced rule
- selected government operation target

The map presentation must pair color with symbols, borders, patterns, or labels.

Inspect the live state-map and state-modifier consumer before choosing size, frames, and alpha.

## Focus icons

Create original focus icons after the final tree count and IDs are registered.

Planning budget:

- opening survival: `6`
- Shadow Council: `10`
- War Directorate: `10`
- Ideological Secretariat: `10`
- Captured Economy: `12`
- Armed Movement: `12`
- Network and Diplomacy: `12`
- Expansion and State Capture: `12`
- Crisis and Failure: `8`
- Jihadist International: `12`
- Final Jihad and terminal route: `10`

Target total is about `114`, subject to the final focus-tree plan.

Each focus icon needs its own focus-surface brief, source PNG, processed preview, final `94x86` DDS, manifest row, and contact-sheet review.

Do not satisfy focus icons with resized idea or decision art.

## Idea and national-spirit icons

Create distinct `64x64` icon families for the visible lifecycle forms of:

- Improvised Command
- Distributed Command
- Network Directorate
- Unified Field Command
- Directorate General Staff
- Cadre Authority
- Ideological State
- Compromised Network
- Rival Warlords
- Doctrinal Schism
- Captured Economy
- External Supply System
- Directed War Economy
- Civil Administration
- Patron Development Mission
- Looting Spiral
- Famine
- Sponsor Dependency
- Contested Legitimacy
- Security State
- Claimed Authority
- Recognized Enclave
- International Mandate
- Local Revolt
- Mass Defection
- Failed Rule
- Presence of the Entity
- World in Revolt
- Supply Through Ruin

The implementation may merge minor visual stages that retain the same institution. Record every accepted merge before production.

Do not create a new icon for a numerical upgrade that keeps the same visible identity.

## Decision and mission icons

Create separate icon families for the accepted decision matrix.

Government themes:

- response coordination
- transport protection
- victim support
- intelligence
- rapid security deployment
- targeted raid
- support disruption
- allied intelligence
- defection channel
- movement restriction
- community-site protection
- sponsor exposure
- military reinforcement
- capital security
- enclave isolation
- relief corridor
- state retaking
- negotiated surrender
- foreign intervention
- service restoration
- public accounting
- security reform

Actor themes:

- local recruitment
- defector integration
- captured-depot repair
- external corridor
- sponsor search
- foreign-cell support
- network relocation
- militia conversion
- ideological mobilization
- actor merger
- leadership contest
- state offensive
- civil administration
- coerced extraction
- foreign fighters
- Jihadist International membership
- coordinated uprising
- revelation acceleration

Decision icons must read clearly at the verified final decision size with one strong subject and limited interior detail.

Mission icons remain separate when the UI uses a distinct mission family.

## Achievement icons

Create one original completed icon and required grey and not-eligible variants for each full achievement ID:

- `031_no_second_blast`
- `031_the_long_watch`
- `031_the_city_still_stands`
- `031_cut_every_route`
- `031_the_false_claim_rejected`
- `031_no_collective_punishment`
- `031_enemy_of_my_enemy`
- `031_fracture_from_within`
- `031_maximum_survivor`
- `031_false_revelation_denied`
- `031_victims_before_victory`
- `031_war_without_a_capital`

Achievement icons use their own source art and cannot be resized focus, idea, or decision icons.

Follow the root-only achievement path and exact triplet naming convention verified from the achievement registry.

## Super-event images

Create two generated super-event images after the super-event text and role research confirms the final identity.

### Reveal

Role:

First reveal and terminal campaign announcement.

Direction:

A period-authentic command hall, captured public building, or gathering where the entity appears through impossible light, altered shadow, physical distortion, or followers' reaction. Show the event indirectly enough to preserve ambiguity.

Do not depict a deity, sacred calligraphy, real extremist symbols, or a generic fantasy monster detached from the period.

### Defeat aftermath

Role:

Reflective global defeat and reconstruction announcement.

Direction:

Liberated ruins, survivors, relief workers, abandoned final emblems, restored civic or religious life, and uncertain evidence that the entity is gone. The scene should carry loss and recovery without triumphant spectacle.

Each image needs source PNG, prompt, processed preview, final DDS, sprite handoff, contact sheet, and permanent provenance note.

## Audio boundary

This asset prompt does not authorize audio production.

The two super-event tracks belong to `chaosx_super_event_audio_researcher` under the separate super-event prompt.

Do not create, synthesize, record, or substitute audio.

## 3D and custom-unit boundary

Do not invoke `chaosx_3d_model_pipeline` for this event.

Do not create a custom combat battalion, equipment archetype, model, skeletal animation, custom unit sound, or bespoke unit counter.

Existing HOI4 unit types satisfy the accepted design.

If implementation later adds a custom combat unit, stop and return the change for design approval because it activates the full Event 19, 3D, sound, and counter contracts.

## Processing and DDS

For every final asset:

1. preserve the generated or sourced master
2. record prompt or source mode
3. process mechanically to target composition and size
4. preserve real transparency where required
5. validate final appearance at native size and enlarged nearest-neighbor review
6. convert with the repository DDS workflow
7. validate DDS header, dimensions, alpha, frame count, and round-trip appearance
8. place the DDS in the final runtime folder
9. record proposed sprite and consumer
10. add the asset to the contact sheet and manifest

Do not use primitive local drawings, simple shapes, placeholders, or resized unrelated art as final assets.

## Manifest

The manifest must record for every asset:

- asset ID and basename
- Event 31 owner
- exact asset type
- route or progression state
- source mode
- prompt or source record
- source checksum
- target dimensions
- processed PNG path and checksum
- final DDS path and checksum
- sprite proposal
- actual runtime consumer after wiring
- status
- producer
- reviewer
- review date
- identity, framing, style, transparency, readability, and provenance verdicts where relevant
- blocked reason or user-review requirement

Portrait entries also record name, role, gender metadata, source classification, durable archive path, and duplicate-face review.

Animation entries also record frame count, frame dimensions, sheet dimensions, FPS, loop, anchor, static fallback, frame-source status, and GUI precedent.

## Handoff

Write `gfx_handoff.md` with:

- final file paths
- stable sprite proposals
- target `.gfx` files
- target GUI, event, focus, idea, decision, achievement, character, country, state, or super-event consumers
- frame and animation metadata
- category-picture dimensions and consumer
- flags and cosmetic-tag naming dependencies
- missing runtime identifiers
- blocked assets
- review status

Asset subagents must not edit unrelated gameplay, localisation, GUI, event, focus, idea, decision, history, AI, or spreadsheet files.

## Completion gate

Do not mark the asset package complete until:

- every accepted asset row has final source and DDS files
- every portrait has passed identity, framing, provenance, and duplicate review
- the flag pool is flat, distinct, and large enough for the verified simultaneous actor limit
- separate icon families remain separate
- category pictures are final and contain no fake controls
- super-event art matches the researched text and audio role
- the entity animation has real source frames, a static fallback, and a verified consumer
- no real extremist symbol, sacred hostile branding, modern prop, or stereotype remains
- every manifest and handoff row is complete
- the parent has enough information to wire every asset without guessing

Report every missing, rejected, blocked, or reduced asset. Do not substitute a weaker image or reuse an unrelated asset to close the package.
