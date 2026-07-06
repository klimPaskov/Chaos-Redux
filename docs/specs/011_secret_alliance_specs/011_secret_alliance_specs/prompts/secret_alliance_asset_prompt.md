# Asset prompt for 011 Secret Alliance

Use `chaos-redux-event-assets` and `chaos-redux-frame-animation` where animation is requested. Use the appropriate asset subagent routing from `chaos-redux-subagents`. Work with `fork_context=false` and explicit context if using project subagents.

Event: 011 Secret Alliance
Intended package path: `docs/assets/011_secret_alliance/`
Source spec path: `docs/specs/011_secret_alliance_specs/`

## Visual identity

Secret Alliance is a hidden intelligence and diplomacy crisis that becomes a public faction against the player. The visuals should emphasize dossiers, sealed files, shadowed delegates, intercepted radios, courier routes, burned factory floors, border watch posts, and a circle of governments closing around the target. Avoid making the main visual a generic map-table scene. Maps can appear as secondary props.

## Required reference folders

Inspect the matching reference folders before creating assets:

- ideas and national spirits: `chaos_redux/.agents/skills/chaos-redux-event-assets/assets/ideas`
- decision and decision category icons: `chaos_redux/.agents/skills/chaos-redux-event-assets/assets/decisions`
- achievement icons: `chaos_redux/.agents/skills/chaos-redux-event-assets/assets/achievements`
- super-event images: `chaos_redux/.agents/skills/chaos-redux-event-assets/assets/super_event_images`

## Static icons

Create separate source art for each asset type. Do not derive decision icons from focus icons or idea icons.

### Decision category icon, 32x32 or established category size

- working asset name: `decision_category_secret_alliance_dossier`
- sprite proposal: `GFX_decision_category_secret_alliance_dossier`
- visual direction: sealed dossier, clasp, small red string or wax mark, no readable text
- source mode: generated icon art

### Decision icons, 32x32

- `decision_secret_alliance_trace_couriers`: magnifier over rail ticket or courier bag
- `decision_secret_alliance_intercept_radios`: radio set and torn code sheet, no text
- `decision_secret_alliance_guard_industry`: guarded factory gate or helmet over gears
- `decision_secret_alliance_secure_rail`: rail switch with lock
- `decision_secret_alliance_neutral_inquiry`: neutral observer seal and lamp
- `decision_secret_alliance_public_dossier`: open file with silhouetted stamps, no readable text
- `decision_secret_alliance_border_watch`: binoculars and frontier post
- `decision_secret_alliance_preemptive_war`: crossed plan arrows and mobilization marker, no country flags

### Idea and national spirit icons, 64x64

- `idea_secret_alliance_dossier_pressure`: compressed file stack, dim lamp
- `idea_secret_alliance_hardened_internal_lines`: locked rail bridge and guards
- `idea_secret_alliance_diplomatic_encirclement`: ring of seals around a central blank state emblem
- `idea_secret_alliance_hidden_signatory_network`: hands signing in shadow, no readable text
- `idea_secret_alliance_patron_channels`: money, cipher, and diplomatic pouch
- `idea_secret_alliance_open_pact`: public faction seal, sharp and threatening
- `idea_secret_alliance_fractured_war_table`: cracked meeting table or broken seals

## Super-event image, 457x328

Create or source one reveal super-event image after the super-event research prompt confirms the final role. Preferred source mode is generated period-authentic symbolic documentary art unless the implementation chooses a sourced historical analogue image with clear licensing.

Visual direction:

- a shadowed conference circle or sealed war council
- delegates shown as silhouettes or partial figures
- secondary props can include maps, sealed folders, phones, flags blurred into generic shapes, and military attaché caps
- no readable generated text
- strong central composition and contrast for HOI4 super-event UI
- avoid modern clothing, modern conference rooms, modern microphones, and cinematic colour grading

Suggested sprite proposal:

- `GFX_super_event_secret_alliance_reveal`
- final DDS path proposal: `gfx/interface/super_events/011_secret_alliance/super_event_secret_alliance_reveal.dds`

## Faction emblem or seal

If the implementation supports faction emblem display or dossier UI emblem use, create a symbolic faction seal:

- working name: `secret_alliance_pact_seal`
- sprite proposal: `GFX_secret_alliance_pact_seal`
- direction: ring of blank seals, hidden clasp, no readable text, no real nation symbols
- source mode: generated symbolic art

## Animated assets

Use `chaos-redux-frame-animation`. Every final animation must have real source frames, a static fallback, frame sheet DDS, preview GIF for review only, and GFX handoff. Do not fake motion by filtering or shifting one still image.

### Animated dossier seal

- in-game use: decision category header or optional dossier GUI
- static sprite: `GFX_secret_alliance_dossier_seal`
- animated sprite: `GFX_secret_alliance_dossier_seal_animated`
- target size: implementation should choose established category header size, suggested 96x96 if custom GUI uses it
- frame count target: 8 real source frames
- fps: 8 to 10
- loop: yes
- states: closed, active, urgent, public, compromised
- visual change: seal opens slightly, red warning mark or file string tightens, papers shift only if source frames actually show that state
- source mode: generated frame art
- static fallback: closed or active state based on mechanic phase

### War Clock warning pulse

- in-game use: warning frame around War Clock or public confrontation button
- static sprite: `GFX_secret_alliance_warning_frame`
- animated sprite: `GFX_secret_alliance_warning_frame_animated`
- target size: match chosen meter or button frame
- frame count target: 6 to 8 real source frames
- fps: 6 to 8
- loop: yes
- visual change: warning frame grows more urgent through hand-authored or generated frame states, not filter-only opacity changes
- state logic: visible when War Clock is high or reveal is imminent

## Achievement icons, 64x64

Create completed icon direction for each. Grey and not-eligible variants follow achievement asset rules.

- `chaosx_secret_alliance_read_the_room`: magnifier and three faint seals
- `chaosx_secret_alliance_every_door_locked`: locked factory, rail, and port motif
- `chaosx_secret_alliance_the_empty_chair`: abandoned chair at a meeting table
- `chaosx_secret_alliance_pact_against_me`: central country silhouette surrounded by ring of seals, no real map shape if possible
- `chaosx_secret_alliance_no_shadow_left`: torn network threads and exposed lamp
- `chaosx_secret_alliance_bad_guess`: cracked false stamp and cleared file
- `chaosx_secret_alliance_three_knives_one_table`: three daggers laid beside a sealed document, no gore
- `chaosx_secret_alliance_public_enemy_number_one`: spotlight on central file with two major seals in shadow
- `chaosx_secret_alliance_quietly_undone`: closed file with cut red strings

## Manifest and handoff

Write `docs/assets/011_secret_alliance/manifest.md` and `docs/assets/011_secret_alliance/gfx_handoff.md`. Include source mode, prompts, source PNG, processed PNG, final DDS, target sizes, sprite names, related decisions or ideas, animation frame counts and static fallbacks, and any uncertainty.
