# Asset prompt for Event 17: Random faction

Create the visual asset package for Event 17 `Random faction` using `chaos-redux-event-assets` and `chaos-redux-frame-animation` for animated items.

## Required reference inspection

Inspect these reference folders before creating assets:

- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decisions`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/ideas`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/report`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/achievements`

## Asset list

| Asset | Type | Target size | Source mode | Final path direction | Sprite direction |
| --- | --- | ---: | --- | --- | --- |
| bloc pressure category | decision category icon | repo pattern, likely 32x32 or category size | generated icon | event folder under decisions if supported | `GFX_decision_category_random_faction_bloc_pressure` |
| neutrality council | decision icon | 32x32 | generated icon | `gfx/interface/decisions/017_random_faction/` | `GFX_decision_random_faction_neutrality_council` |
| border posts | decision icon | 32x32 | generated icon | same folder | `GFX_decision_random_faction_border_posts` |
| liaison mission | decision icon | 32x32 | generated icon | same folder | `GFX_decision_random_faction_liaison` |
| radio networks | decision icon | 32x32 | generated icon | same folder | `GFX_decision_random_faction_radio_networks` |
| guarantee corridor | decision icon | 32x32 | generated icon | same folder | `GFX_decision_random_faction_corridor` |
| demand commitment | decision icon | 32x32 | generated icon | same folder | `GFX_decision_random_faction_commitment` |
| alignment shock | idea icon | 64x64 | generated icon | `gfx/interface/ideas/017_random_faction/` | `GFX_idea_random_faction_alignment_shock` |
| border pressure | idea icon | 64x64 | generated icon | same folder | `GFX_idea_random_faction_border_pressure` |
| bloc polarization | idea icon | 64x64 | generated icon | same folder | `GFX_idea_random_faction_bloc_polarization` |
| neutrality exhaustion | idea icon | 64x64 | generated icon | same folder | `GFX_idea_random_faction_neutrality_exhaustion` |
| liaison mission spirit | idea icon | 64x64 | generated icon | same folder | `GFX_idea_random_faction_liaison_mission` |
| regional cascade report | report event image | 210x176 | generated documentary-style image | `gfx/event_pictures/017_random_faction/` | `GFX_report_event_random_faction_regional_cascade` |
| bloc pressure seal animated | animated UI seal | implementation chosen, likely 64x64 or header size | generated frame art | `gfx/interface/decisions/017_random_faction/` | `GFX_random_faction_bloc_pressure_seal_animated` |
| bloc pressure seal static | static fallback | same frame size | generated | same folder | `GFX_random_faction_bloc_pressure_seal` |
| warning border animated or static | UI warning frame | implementation chosen | generated frames if animated | same folder | `GFX_random_faction_warning_border_animated` and static fallback |

## Visual direction

Use faction banners, crossed diplomatic cables, radio towers, border posts, stamped travel papers, small flags, and tense council-room symbols. Do not use readable generated text. Do not make the art mostly a map. The subject should be pressure, alignment, and choice.

## Animation brief

Animated bloc pressure seal:

- target surface: decision category header or scripted GUI header
- state: active when a country has Event 17 pressure decisions
- frame count target: 6 to 8 real source frames
- loop: subtle cable flicker and banner tension, no transform-only movement
- static fallback: same seal at rest
- sheet: horizontal frame sheet, width equals frame width times frame count
- source mode: generated per-frame art
- final handoff must include frame plan, source frames, processed frames, sheet PNG, sheet DDS, preview GIF, static DDS, manifest entry, and ready-to-copy `.gfx` snippet

Warning border:

- state: visible when neutrality resilience is low
- use animation only if a warning pulse clarifies the state without clutter
- static fallback required either way

## Achievement icons

Produce completed 64x64 achievement icons for every achievement in `prompts/017_random_faction_achievement_prompt.md`. Create grey and not-eligible variants if the achievement implementation requires the standard triplet.

## Manifest and handoff

Create:

- `docs/assets/017_random_faction/manifest.md`
- `docs/assets/017_random_faction/gfx_handoff.md`
- contact sheet for icons
- animation contact sheet and preview GIF for animated assets

Do not edit gameplay, `.gfx`, `.gui`, localisation, event files, decisions, ideas, or spreadsheets unless a parent prompt explicitly expands scope.
