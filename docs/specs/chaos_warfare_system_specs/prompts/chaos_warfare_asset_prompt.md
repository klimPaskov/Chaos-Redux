# Chaos Warfare Asset Production Prompt

## Task

Produce the complete visual asset package for the accepted Chaos Warfare CBRN rework. Read the accepted specification files and the relevant sections of the Chaos Redux event-assets and frame-animation skills. Use the project asset subagent split. Icons belong to `chaosx_icon_artist`. Fictional UI panel art belongs to `chaosx_generated_event_art`. Real company logos, historical symbols, or archival scenes belong to `chaosx_asset_source_researcher` only after the implementation agent confirms they are required.

Do not edit gameplay, localisation, GFX, GUI, doctrine, technology, decision, unit, or spreadsheet files. Produce source art, processed PNGs, final DDS files, contact sheets, manifest entries, and `gfx_handoff.md`.

## System identity

System slug: `chaos_warfare_system`

Working asset package:

`docs/assets/chaos_warfare_system/`

Final DDS folders should follow existing category and event-system conventions without adding an unnecessary project namespace layer.

## Required reference inspection

Before generation, inspect:

- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/national_focus`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/ideas`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decisions`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/technologies/legacy`
- vanilla officer-corps spirit icons for HQ and officer-corps assets
- existing Chaos Warfare doctrine and technology icons

Do not copy reference assets.

## Doctrine icons

Target: 94x86 focus or doctrine-style icons unless current doctrine UI uses another verified size.

Required family:

- `doctrine_chaos_warfare`
- `doctrine_hazard_assault_formations`
- `doctrine_toxic_armored_warfare`
- `doctrine_contaminant_fire_support`
- `doctrine_integrated_cbrn_command`
- four grand-doctrine milestone icons
- five mastery icons for each of the four tracks

Visual language:

- period military CBRN equipment
- masks, sealed vehicles, shell filling, decontamination hoses, field meteorology, command maps as secondary props
- one strong subject per icon
- no text
- avoid generic skull-only iconography
- avoid glamorizing civilian death
- terminal route icons can feel severe and contaminated without modern hazmat imagery

## Technology icons

Target: 64x64 small technology icons, plus 132x52 equipment cards where the existing equipment UI requires them.

Required:

- four protective equipment models
- three decontamination equipment models
- three CBRN instrument models
- Hazard Pioneer Formation
- Chaos Assault Battalion
- Improved Chaos Assault Equipment
- Chemical Artillery Shells
- Persistent Agent Shell Filling
- Armored Agent Delivery
- Sealed Tank Crews
- Nerve Suppression Detachment
- Mobile Decontamination Columns
- Chemical Air Interdiction
- Theater CBRN Headquarters
- Biological Security Assault Detachment
- Respiratory Treatment
- Burn and Blister Treatment
- Nerve Antidote Kits
- Mobile CBRN Hospitals

Tech icons must be designed as technology art, not resized doctrine icons.

## Army HQ and regimental support icons

Inspect the verified current vanilla size and framing before work.

HQ support:

- CBRN Operations Section
- Chemical Intelligence and Weather Cell
- Protective Logistics Section
- Mobile Decontamination Column
- Medical Countermeasure Directorate
- Biological Security Section

Regimental support:

- Gas Mask and Decontamination Detachment
- Chemical Reconnaissance Detachment
- Hazard Pioneer Detachment
- Chemical Projector Battery
- Chemical Ammunition Train
- Armored Chemical Delivery Detachment
- Nerve Agent Suppression Detachment
- Field Epidemiology and Quarantine Detachment
- Medical Countermeasure Detachment
- Biological Security Assault Detachment

Provide unit-counter and small text-icon variants only where the verified UI requires them.

## Equipment art

Required equipment-family art:

- Basic Respirator Crate
- Improved Service Mask Crate
- Advanced Protective Set
- Sealed Assault Set
- Field Decontamination Kit
- Mobile Wash Column
- Rapid Decontamination Plant
- Field Detection Set
- Mobile Sampling Laboratory
- Theater CBRN Command Set
- Choking Agent Payload Lot
- Blister Agent Payload Lot
- Nerve Agent Payload Lot
- Chemical Shell Lot
- Chemical Air Payload Lot

Use period containers and equipment. Do not generate readable labels.

## Decision and category icons

Target: 32x32 decisions. Category sizes must follow inspected existing patterns.

Categories:

- CBRN Program Management
- Civil Defence and Protective Distribution
- Chemical Operations
- Biological Operations and Containment
- Occupation CBRN Measures

Decisions:

- establish respirator reserve
- register and fit population
- priority city distribution
- full state distribution
- emergency distribution
- replace filters
- recondition old masks
- export protective equipment
- prepare chemical offensive
- chemical artillery fire plan
- chemical air operation
- strategic chemical raid
- decontamination corridor
- surveillance network
- quarantine
- field hospitals
- antibiotics
- vaccination
- border closure
- international medical mission
- inspection
- stockpile destruction
- retaliation policy
- nerve suppression
- protected occupation

Decision icons need simple silhouettes readable at 32x32. They must not be resized focus or idea icons.

## Ideas and officer-corps spirits

Target: 64x64 ideas and 45x45 transparent officer-corps spirits where verified.

Required idea family:

- Chemical Readiness stages
- national use policies
- civil-defence reserve
- protection shortage
- medical saturation
- stockpile risk bands
- treaty retaliation posture

Officer-corps spirits:

- Controlled Retaliation Doctrine
- Theater Contamination Doctrine
- Terminal Hazard Doctrine
- Mask Discipline
- Hazard Assault Cadres
- Contaminant Fire Coordination

## State modifiers

Target: 64x64 idea-style state modifier icons.

- Trace contamination
- Local contamination
- Serious contamination
- Severe contamination
- Catastrophic contamination
- civilian mask coverage
- active decontamination corridor
- medical saturation
- active quarantine
- biological contamination and outbreak severity states

Use a coherent severity family that remains distinguishable without color alone.

## Designer assets

Generate generic symbolic icons for:

- Protective Equipment Consortium
- Chemical Munitions Combine
- Mobile Decontamination Works
- Aerosol and Air Delivery Bureau
- Biological Security Directorate
- Medical Countermeasure Directorate

Do not generate logos for real historical companies. Historical company assets require source research and documentation.

## UI assets

Create a restrained period CBRN management panel family:

- window background
- header plate
- five tab buttons with normal, hover, selected, locked, and warning states
- readiness meter frame and fill states
- military and civilian protection meters
- contamination severity frames
- evidence and attribution markers
- operation target cards
- stockpile warning overlays
- close button and tooltip icons only if existing shared UI cannot be reused

Generated art must not decide exact interactive layout. The implementation agent owns GUI slicing and placement.

## Animation

Animated CBRN readiness seal:

- target frame: 64x64 unless GUI inspection requires another size
- eight real source frames
- horizontal sheet: 512x64
- six frames per second
- looping
- static fallback
- rest, rising readiness, ready, falling, and warning states drawn as real frame variants
- no transform-only, recolor-only, or filter-only animation

Optional Severe or Catastrophic contamination warning border:

- use only if the custom GUI is accepted
- real source frames
- subtle loop
- static fallback

Follow `chaos-redux-frame-animation` for brief, frame plan, source frames, sheet, DDS, GIF preview, contact sheet, and GFX handoff.

## Achievements

Create completed, grey, and not-eligible 64x64 assets for every achievement in `chaos_warfare_achievement_prompt.md`. Use the required achievement overlay workflow. Final DDS files belong directly under `gfx/achievements/` with exact achievement IDs.

## Manifest

Every asset entry must record:

- asset type
- working and final identifiers
- source mode
- prompt or source URL
- target size
- source PNG
- processed PNG
- final DDS
- sprite name
- intended GFX file
- related gameplay ID
- status
- uncertainty

No asset is complete without final DDS and handoff. No placeholder is acceptable.
