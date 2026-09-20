# Event 067 Generalissimo Asset Production Prompt

Create the complete visual asset package for Event `067` Generalissimo.

## Required sources

Read:

- `docs/specs/067_generalissimo_specs/specs/067_generalissimo_spec_part_8_presentation_assets_localisation.md`
- every other Event 067 specification part that defines a consumer
- `AGENTS.md`
- `chaos-redux-event-assets`
- `.agents/skills/chaos-redux-event-assets/references/portrait-production.md`
- `chaos-redux-frame-animation` to confirm that no final animation is required
- `chaos-redux-super-events`
- `chaos-redux-subagents`

Inspect the current vanilla and Chaos Redux references for every asset family before production. Use the canonical skill-local contact sheets and current runtime consumers.

## Ownership and routing

Use narrow asset workers with complete context-free prompts:

- `chaosx_portrait_creator` for the Generalissimo portrait
- `chaosx_generated_event_art` for report art, news art, super-event art, category pictures, flags, faction emblems, and full-canvas UI art
- `chaosx_icon_artist` for focus, idea, trait, decision, mission, inlay, and achievement icons

Do not route any character portrait to the general event-art worker.

## Character portrait

Create one canonical fictional male Generalissimo portrait.

Classification:

- `fictional_high_chaos`
- no real-person identity
- no historical uniform copy
- no resemblance to a named real leader

Requirements:

- inspect current leader and commander portrait references
- period 1936 to 1945 officer styling
- one event-owned insignia system
- no modern tactical equipment
- no fantasy armor
- no text or watermark
- exact final role dimensions after consumer inspection
- one canonical identity used by commander and country-leader consumers
- stable runtime basename
- PNG and DDS outputs
- portrait-specific GFX and existing character reference wiring through the portrait worker's allowed scope
- manifest and handoff

## Category pictures

Create five separate full-canvas decision category pictures:

- `generalissimo_category_asset`
- `generalissimo_category_indispensable`
- `generalissimo_category_supreme_command`
- `generalissimo_category_state_within_state`
- `generalissimo_category_ultimatum`

Use the visual directions in Part 8. Each image must show a distinct stage of command and political control.

Requirements:

- inspect `icons/decision_categories/pictures/` references and its contact sheet
- use the current consumer canvas, not a remembered size
- no painted meter, number, button, ledger, or fake UI
- no readable generated text
- no modern equipment
- coherent character identity and insignia across all five
- each stage must remain readable at final size

Static state variants are final. Do not create a transform-only animation or animated replacement.

## Event and news art

Create every report and news image listed in Part 8.

Report roles:

- appearance
- demand
- removal operation
- revolt
- government victory

News roles:

- international appearance
- civil war
- military government established
- world military movement

Use generated period-documentary art. Keep the subject, officers, soldiers, institutions, and public consequences central. Do not default to maps, tables, arrows, or generic conference rooms.

## Super-event art

Create:

- `generalissimo_super_event_rule`
- `generalissimo_super_event_world`

The ruler image must work for peaceful submission and junta victory in any host country. The world-end image must show aligned and rival military governments with civilian resistance. It must not imply that the original Generalissimo already controls every country.

Coordinate final sprite names and paths with the super-event implementation.

## Flags

Create three fictional flat flag families:

- Personal Command
- Officer Directorate
- National Emergency Council

Each family needs normal, medium, and small runtime files.

Every flag uses ImageGen as a flat design. Reject:

- waving fabric
- folds
- flagpoles
- scenery
- perspective
- gradients
- lighting effects
- fake lettering
- copied real extremist symbols
- invented claims that the design is historical

The three flags share an Event 067 insignia language but remain clearly different. Compare geometry, orientation, symbol placement, and colors manually before resizing.

## Transparent icon families

Request genuine native transparency in the first ImageGen call and preserve alpha through processing and DDS conversion.

Create separate source art for each UI family. Do not resize focus icons into ideas, decisions, missions, traits, or achievements.

Required families:

- four Generalissimo country-leader trait icons
- four starting and aftermath idea icons
- one decision category icon
- every crisis decision icon listed in Part 8
- every crisis and postwar mission icon listed in Part 8
- every junta decision icon listed in Part 8
- all final focus icons in the implemented tree
- International Command emblem
- Civil Authority Compact emblem
- rival military-bloc emblem when the implementation uses one
- focus inlay panel and state assets
- eight achievement icon triplets

For focus icons, expand the manifest to one row per final focus. At minimum, every opener, route lock, branch choice, convergence focus, capstone, and world-end focus needs distinct art.

## Focus inlay assets

Create:

- compact inlay background
- portrait frame
- Command Cohesion meter frame
- fill or mask texture
- low-Cohesion warning frame
- Personal Command emblem
- Officer Directorate emblem
- National Emergency Council emblem
- unresolved structure emblem

These are static state assets. Do not add glow loops or frame animation.

## Achievement assets

Create completed, grey, and not-eligible icons for:

- `067_generalissimo_civilian_command`
- `067_generalissimo_refuse_the_ultimatum`
- `067_generalissimo_barracks_to_capital`
- `067_generalissimo_total_command`
- `067_generalissimo_first_among_generals`
- `067_generalissimo_guardian_state`
- `067_generalissimo_world_against_the_barracks`
- `067_generalissimo_no_second_shot`

Use the exact achievement IDs in filenames after inspecting current repository convention.

## QA requirements

For every asset:

- source file retained during active work
- prompt and source mode recorded
- processed PNG
- final DDS where required
- exact native dimensions
- alignment and crop review
- transparency review where applicable
- no white matte or opaque square
- no fake checkerboard
- no halo
- no generated text
- no modern anachronism
- contact sheet with filenames and dimensions
- manifest row
- sprite and runtime-path handoff

Review transparent icons over light, dark, and checker backgrounds. Review small icons at actual game size.

## Paths and cleanup

Use the temporary workspace:

```text
docs/assets/067_generalissimo/
```

Final assets must move to event-scoped runtime folders under the correct GFX categories. Flags and achievements follow their engine root naming conventions.

Before Event 067 is declared complete:

- verify every asset has a live runtime consumer
- promote durable provenance, prompt, review, and wiring facts into permanent event documentation
- verify no runtime path points into `docs/assets/`
- delete the complete temporary Event 067 asset workspace

## Exclusions

Do not create:

- custom unit art
- custom counters
- unit audio
- 3D models
- skeletal animation
- animated portrait
- animated category picture
- formable state pieces

Report any missing consumer, unavailable reference, failed generation, or damaged transparency as blocked. Do not substitute a placeholder or recycled unrelated asset.
