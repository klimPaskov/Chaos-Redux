# Asset Prompt: Event 021 Random Civil War

Create the complete authorized visual asset package for Event 021 under `docs/specs/021_random_civil_war_specs/`.

Read:

- `AGENTS.md`
- `chaos-redux-event-assets`
- `chaos-redux-frame-animation`
- `chaos-redux-subagents`
- `021_random_civil_war_spec_part_9_presentation_assets_achievements.md`
- the final implemented decision, mission, idea, event, news, and achievement identifiers

Use `chaosx_generated_event_art` for generated non-icon scenes and `chaosx_icon_artist` for icons. Spawn every project subagent with `fork_context=false`.

## Authorization boundary

Create only assets that have a final runtime consumer.

Authorized families:

- baseline report image
- multi-front news image
- Global Fracture news image
- optional Event 006 independence-front report image only when no Event 006 image fits
- optional strange-incident report image only when implemented incidents justify it
- one static decision-category picture
- one decision-category icon
- final implemented decision icons
- final implemented mission icons
- three staged idea icons
- six achievement icon triplets

Do not create:

- new generic flags
- new portraits for ordinary claimants
- advisor portraits
- animated category art
- animated seal
- animated portrait
- scripted GUI panel
- faction emblem
- 3D asset
- super-event image
- super-event audio

Event 006 owns its country flags, portraits, route art, and package-specific identity assets.

## Event and news art

### Baseline report

Working ID: `report_event_021_random_civil_war_opening`

Target: verify the current report-event consumer, with `210x176` as the planning reference.

Direction:

- 1936 to 1945 period-documentary scene
- divided formations and civilians at a rail yard, barracks gate, regional hall, or city street
- visible political and military rupture
- no modern props
- no readable generated text
- no map table
- no generic explosion-only composition

### Multi-front news

Working ID: `news_event_021_multi_front_war`

Target: verify the current news consumer, with `397x153` as the planning reference.

Direction:

- black-and-white period press scene
- several distinct armed groups around one city, junction, or public square
- visible separation without modern labels or text
- high contrast and readable composition

### Global Fracture news

Working ID: `news_event_021_global_fracture`

Direction:

- one coherent period scene that suggests simultaneous political fracture across several countries
- rail station, border crossing, delegations, military columns, or displaced administrations
- no literal world map
- no fake newspaper text
- black-and-white press treatment

### Optional reports

Use an independence-front report only after checking Event 006 art ownership.

Use a strange-incident report only if the implemented event family uses it enough to justify a separate asset. Keep the scene uncertain. Show banners, oath circles, night gatherings, ruined shrines, or frightened soldiers. Do not show a monster, gore, or a confirmed supernatural cause.

## Decision-category picture

Create one static category picture after inspecting:

`.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decision_categories/pictures`

Use the verified runtime canvas. The current reference-family canvas is `114x101`, not a universal assumption.

Direction:

- divided barracks, occupied rail junction, split government square, or soldiers facing former comrades
- strong territorial and political identity
- no fake buttons
- no fake meter
- no dynamic values
- no text
- no map diagram
- no animation

## Icon families

Every UI family requires separate source art.

### Category icon

Direction:

- split command baton, divided standard, or fractured national seal
- clear silhouette
- readable at the verified category size
- real transparency where required

### Decision icons

Create icons only for implemented actions. Expected families include:

- secure arsenals
- capital defense
- restore rail spine
- loyalty review
- integrate formations
- regional guarantee
- amnesty
- emergency coalition
- local mobilization
- depot seizure
- field administration
- foreign liaison
- recognition
- ceasefire
- reconstruction
- border monitoring
- relief corridor
- military aid corridor
- sponsor exposure
- strange-incident countermeasure

Do not reuse one resized icon across different UI roles.

### Mission icons

Create separate mission art for implemented objectives, including:

- hold capital
- secure rail junctions
- defend depot belt
- keep corridor open
- complete mobilization
- deny recognition
- preserve settlement
- fulfill disarmament
- rebuild administration

### Idea icons

Create distinct `64x64` source art for:

- Fractured Command
- War-Torn Administration
- Unsettled Settlement

Use compact national-spirit composition, transparent unused canvas, dark outline, clear silhouette, and no focus frame.

### Achievement icons

Create completed, grey, and not-eligible variants for:

- `021_random_civil_war_hold_the_center`
- `021_random_civil_war_no_state_left_behind`
- `021_random_civil_war_a_flag_of_our_own`
- `021_random_civil_war_war_within_a_war`
- `021_random_civil_war_the_terms_hold`
- `021_random_civil_war_fractals_of_sovereignty`

Follow the icon directions in Part 9.

## Production contract

For every authorized asset:

- inspect the exact vanilla or established Chaos Redux reference family
- record source mode and prompt
- preserve source PNG
- create processed PNG
- create final DDS in the correct event-scoped runtime folder
- verify dimensions, alpha, crop, alignment, and readability
- create a contact sheet
- write the asset manifest
- write `gfx_handoff.md`
- list final sprite names and consumers
- keep separate art for separate icon types
- mark blocked assets instead of substituting weak art

Temporary work belongs under `docs/assets/021_random_civil_war/` while active. Before full event completion, promote durable evidence into permanent event or plan documentation, verify that no runtime reference points into `docs/assets/`, and remove the temporary event workspace.

Do not claim the asset goal complete while a required runtime asset is missing, unwired, visually unreviewed, or replaced by a placeholder.
