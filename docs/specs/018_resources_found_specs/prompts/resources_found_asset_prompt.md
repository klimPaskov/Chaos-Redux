# Asset Prompt for Event 018 Resources Found

Use `chaos-redux-event-assets` and route work through the correct narrow asset subagents. Use `chaos-redux-frame-animation` for every animated asset. Inspect the matching reference folders before creating or processing anything. Do not wire `.gfx`, `.gui`, gameplay, localisation, or spreadsheet files unless the parent explicitly expands scope.

All asset names here are working labels only. Preserve final filenames and sprite names selected by the implementation agent.

## Source mode rules

- Generated art is appropriate for fictional cave monsters, Cave Host leader, Cave Host flags, supernatural resource seams, public attack scenes, high-chaos report images, super-event images, icons, UI, and animated elements.
- Sourced real images may be used for ordinary mining, oil, survey, or rail discovery report images if a period-fitting source is found and licensing is documented.
- Do not generate real leader portraits or historical flags. This event has no required real leader portrait.
- News images must be black and white. Report images must use the report-event card treatment.
- Super-event audio is not part of this prompt.

## Reference folders to inspect

Use these project reference folders from the asset skill:

- ideas: `.agents/skills/chaos-redux-event-assets/assets/ideas`
- decisions: `.agents/skills/chaos-redux-event-assets/assets/decisions`
- report event images: `.agents/skills/chaos-redux-event-assets/assets/report_event_images`
- news event images: `.agents/skills/chaos-redux-event-assets/assets/news_event_images`
- super-event images: `.agents/skills/chaos-redux-event-assets/assets/super_event_images`
- focuses: `.agents/skills/chaos-redux-event-assets/assets/focuses`
- flags: `.agents/skills/chaos-redux-event-assets/assets/flags`
- achievements: `.agents/skills/chaos-redux-event-assets/assets/achievements`

## Required visual assets

Create or plan source, processed PNG, final DDS or TGA as appropriate, manifest entries, contact sheets where useful, and `gfx_handoff.md`.

### Report images, 210x176

- discovery report: period survey or extraction crew at a newly recognized field
- boom report: extraction settlement with rail, mine, derrick, or resource activity
- sickness report: medical or worker exhaustion around lower works
- public attack report: evacuation or damaged extraction site with a visible nonhuman threat if appropriate
- closure report: sealed shaft or abandoned extraction works
- aftermath report: sealed origin and reconstruction if Cave Host defeated

### News images, 397x153 black and white

- border crisis over resource field
- Cave Host emergence if implementation uses news in addition to super-event
- continental world reaction if world-end branch needs a news layer

### Super-event images, 457x328

- Cave Host reveal: generated fictional image of a nonhuman host emerging from an excavated resource field
- Cave Host world-end: generated image of global resource seams or cave mouths opening across continents
- Cave Host defeat aftermath: generated image of costly victory, sealed depths, and survivors

### Decision and category icons

Create icons for category, survey, extraction, infrastructure, concession, nationalization, security, safety, medical relief, evacuation, cave hunt, closure, resource denial, and reclamation. Decision icons should be 32x32 unless the existing repo category pattern requires another size.

### Idea and national spirit icons, 64x64

Create icons for resource boom, foreign concessions, unsafe extraction, worker sickness, public panic, sealed depths, anti-monster lessons, Cave Host resource-bound rule, Cave Host slow armored bodies, Cave Host origin nest, and Cave Host surface terror.

### Cave Host country assets

- Generated fictional leader portrait, 156x210. The subject is a literal cave monster leader. Record as nonhuman fictional. If a one-person monster name is later used, use a fictional monster-appropriate pool and do not mix with human gender metadata.
- Cave Host flags in normal, medium, and small sizes. Use a fictional cave maw, mineral seam, claw, or stone-host motif. No text.
- Cave Host focus icon family at 94x86 for opening trunk, hunger lane, stone hide lane, tunnel lane, brood hierarchy lane, surface terror lane, and continental maw lane.

### Achievement icons, 64x64

Create completed icon directions for every achievement in the achievement prompt. Produce grey and not-eligible variants only according to the existing achievement workflow.

## Animated assets

Use `chaos-redux-frame-animation`. Each animation must have real source frames, processed frames, sheet PNG, sheet DDS, static fallback DDS, preview GIF for review, manifest entry, and `.gfx` handoff.

Required animated asset plans:

- resource field category seal, 6 to 10 frames, cracks and glow by stage
- extraction pressure warning frame, 6 to 8 frames
- public panic warning frame, 6 to 8 frames
- closure seal, 6 to 10 frames, available, last chance, sealed variants
- breach warning, 8 to 12 frames, fissure widening
- Cave Host leader portrait, 8 to 12 frames, breathing or stone dust, 156x210 fallback and sheet

Do not make final animation from a shifted, recolored, blurred, or glow-filtered still image.

## Manifest requirements

For every asset record source mode, prompt or source URL, license when sourced, source path, processed PNG path, final path, target size, intended use, sprite name if known, status, and uncertainty. For animated assets record frame count, fps, loop behavior, static fallback, sheet path, and frame source notes.


## Continuation scripted GUI assets

Part 8 adds animated UI assets for the field ledger. Add these to the asset manifest if the richer panel is implemented.

| Asset slug | Use | Target frame size | Frames | Sheet size | FPS | Static fallback |
| --- | --- | --- | ---: | --- | ---: | --- |
| resource_field_seal | Category or window emblem | 96x96 | 8 | 768x96 | 8 | resource_field_seal_static |
| pressure_warning_border | Value panel warning border | 320x64 | 8 | 2560x64 | 10 | pressure_warning_border_static |
| below_pressure_pulse | Dangerous-depth indicator | 96x96 | 10 | 960x96 | 8 | below_pressure_pulse_static |
| closure_seal_glow | Closure card availability | 96x96 | 10 | 960x96 | 8 | closure_seal_glow_static |
| cave_hunt_card_edge | Hunt card active edge | 300x86 | 8 | 2400x86 | 8 | cave_hunt_card_edge_static |
| cave_host_maw_emblem | Host war board emblem | 128x128 | 12 | 1536x128 | 8 | cave_host_maw_emblem_static |
| continent_maw_progress | Late continental pressure meter | 320x48 | 10 | 3200x48 | 6 | continent_maw_progress_static |

Every animated asset needs real source frames, processed frames, sheet PNG, sheet DDS, static fallback DDS, preview GIF, manifest entry, and GFX handoff. Do not create final animation from a transformed still image.
