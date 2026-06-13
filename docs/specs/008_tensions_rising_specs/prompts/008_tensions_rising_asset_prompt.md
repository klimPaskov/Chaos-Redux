# Asset Prompt: Event 008 Tensions Rising

You are producing visual asset handoffs for Chaos Redux Event 008 `Tensions Rising`.

Read and follow:

- `AGENTS.md`
- `chaos-redux-event-assets`
- `chaos-redux-frame-animation` for any animated sprite/state package
- The Event 008 source specs under `docs/specs/008_tensions_rising_specs/`

Do not edit gameplay, localisation, GUI, GFX, event, focus, decision, scripted effect, scripted trigger, country, history, or spreadsheet files. Produce source files, processed PNG previews, DDS files, manifest entries, and `gfx_handoff.md` only.

## Visual identity

This event is not a battlefield and not a map-change event. The imagery should show diplomatic pressure before the break: embassy lights at night, telegraph rooms, sealed cables, press bundles, staff offices, blackout curtains, side entrances, guards, shipping ledgers, and tense clerks.

Avoid generic war-room map tables as the main subject. Maps can appear as secondary props only.

## Required assets

### Report event image

- Asset name: `report_event_tensions_rising`
- Type: report event image
- Target: 210x176
- Source mode: generated staged-documentary preferred, sourced period diplomatic/press image acceptable only if license and era fit are clear
- Direction: 1936–1945 documentary-style diplomatic office, night desk lamp, cable sheets, sealed dispatch bag, no readable text, no modern props
- Final path direction: `gfx/event_pictures/report_event_tensions_rising.dds` or current repo pattern
- Suggested sprite: `GFX_report_event_tensions_rising`

### News event image

- Asset name: `news_event_tensions_red_line`
- Type: news event image
- Target: 397x153, black-and-white
- Source mode: generated period press image preferred
- Direction: bundled newspapers outside embassy gates, guarded entrance, dark city street, anxious crowd, no readable text
- Suggested sprite: `GFX_news_event_tensions_red_line`

### Super-event image

- Asset name: `super_event_tensions_red_line`
- Type: super-event image
- Target: 457x328
- Source mode: generated
- Direction: strong central composition of embassies/telegraph rooms/world ministries at night, lights in many windows, sealed cables, no battlefield, no readable generated text, no modern props
- Suggested sprite: `GFX_super_event_tensions_red_line`


### Achievement icons

Create completed 64x64 achievement icons for:

1. `achievement_tensions_thin_wire`  -  taut telegraph wire over dark map.
2. `achievement_tensions_only_headlines`  -  stacked newspapers under silent clock, no readable text.
3. `achievement_tensions_insurance_market`  -  marine insurance ledger and ship silhouette, no readable text.
4. `achievement_tensions_red_line`  -  broken red cord across dark embassy window.
5. `achievement_tensions_one_denial`  -  denied stamp motif over sealed cable, no readable text.
6. `achievement_tensions_blackout`  -  blacked-out embassy facade with ten lit windows.

Target: 64x64 each. Produce grey and not-eligible variants if the current achievement pipeline requires them.

### Optional animated event-detail accent

Only produce this if the current Event Log UI has an accepted sprite surface for event-detail accents or warning frames.

- Asset name: `tensions_rising_wire_pulse`
- Type: small animated UI accent
- Static fallback required: `tensions_rising_wire_pulse_static`
- Direction: subtle telegraph-wire pulse or red-line shimmer, state-driven, not distracting
- Must follow frame-animation rules: real source frames, processed frames, contact sheet, GIF preview for review only, final static fallback, frame sheet or sequence handoff, no transform-only animation
- If no accepted UI surface exists, mark this asset `not_needed` rather than inventing a GUI surface.

## Reference folders to inspect

Inspect the matching Chaos Redux reference folders before generation or processing:

- report event images: `.agents/skills/chaos-redux-event-assets/assets/report_event_images`
- news event images: `.agents/skills/chaos-redux-event-assets/assets/news_event_images`
- super-event images: `.agents/skills/chaos-redux-event-assets/assets/super_event_images`
- decisions: `.agents/skills/chaos-redux-event-assets/assets/decisions`
- achievements: `.agents/skills/chaos-redux-event-assets/assets/achievements`

## Manifest requirements

Create or update:

`docs/assets/008_tensions_rising/manifest.md`

Every asset entry must include source mode, prompt or source URL, license/source notes for sourced assets, source PNG path, processed PNG path, final DDS path, target size, sprite name, suggested `.gfx` file, status, and uncertainty.

Create:

`docs/assets/008_tensions_rising/gfx_handoff.md`

The handoff must include final DDS paths and ready-to-wire sprite names. Do not edit `.gfx` files yourself.
