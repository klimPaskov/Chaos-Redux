# Event 31 False Revelation entity animation handoff

Producer: Event 31 entity-animation worker.

Date: 2026-08-30.

Status: `complete` for the requested bounded animation package; parent consumer wiring and live review remain parent-owned.

## Scope and changed files

The worker changed only the requested asset/GFX surfaces:

- `gfx/interface/animated/031_random_terror/false_revelation_entity_sheet.png`
- `gfx/interface/animated/031_random_terror/false_revelation_entity_sheet.dds`
- `docs/assets/031_random_terror/false_revelation_entity_animation/` source frames, processed frames, sheet evidence, static fallback evidence, review GIF, contact sheet, validation, prompt record, manifest, frame plan, and GFX handoff
- `interface/031_random_terror.gfx`
- this handoff

The GFX edit removed only the eight redundant early portrait definitions identified in the concurrent file: `Clandestine_01`, `Council_01`, `Council_02`, `Council_03`, `Entity`, `Jihadist_01`, `Military_01`, and `Revolutionary_01`. The later complete pool definitions were retained. The two new IDs are `GFX_Portrait_Random_Terror_Entity_Static_Fallback` and `GFX_Portrait_Random_Terror_Entity_Animated`.

No shared GUI, scripted GUI, scripted localisation, trigger, gameplay, event, focus, decision, country, character, sound, or workbook file was changed. No 3D model, custom unit, counter, audio, or dedicated Event 31 GUI was created.

## Verified consumer and reference inspection

The parent-provided consumer is the shared Event Details evolution portrait property `[GetEventsLogSelectedEvolutionPortrait]`, displayed by `interface/chaosx_events_log_popup.gui` `events_log_evolution_details_portrait` at `{ x = 34 y = 20 }`, scale `0.60`, in a clipped `160x160` frame. The worker did not modify those shared files.

The required canonical family was the single canonical reference root at `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders`. Its `contact_sheet.png` was inspected before the individual 156x210 leader references. The existing Event 31 entity portrait was inspected as the identity and static-fallback master.

Vanilla/repository animated-sprite precedents inspected: offline `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md` `frameAnimatedSpriteType` section, vanilla animated definitions under `interface/`, and repository `interface/014_cannibalism.gfx` and `interface/005_soviet_collapse.gfx`. These establish one-row horizontal sheets, `noOfFrames`, `animation_rate_fps`, `looping`, `play_on_show`, and optional `pause_on_loop` fields.

## Animation package

| Field | Value |
| --- | --- |
| Frame count | 10 real source frames, `000` through `009` |
| Frame dimensions | 156x210 |
| Sheet dimensions | 1560x210, one horizontal row |
| Rate | 6 FPS |
| Loop | yes |
| Play on show | yes |
| Pause on loop | 0.15 seconds |
| Anchor | stable bottom-center |
| Background | `consumer_opaque`, full painted canvas, alpha 255 throughout |
| Animated sprite | `GFX_Portrait_Random_Terror_Entity_Animated` |
| Static alias | `GFX_Portrait_Random_Terror_Entity_Static_Fallback` |
| Runtime sheet DDS | `gfx/interface/animated/031_random_terror/false_revelation_entity_sheet.dds` |
| Runtime static DDS | `gfx/leaders/031_random_terror/leader_random_terror_entity.dds`, accepted existing portrait reused |

Frame 000 is the approved existing portrait. Frames 001–009 are separate built-in ImageGen edits using the fictional entity source as the edit target. The authored content changes are window reflections and physically contradictory wall shadows; the entity identity, pose, suit, camera, crop, room palette, and anchor remain stable. The final motion is not produced by moving, scaling, rotating, warping, blurring, recoloring, filtering, opacity changes, glow pulses, or shape overlays.

The package intentionally keeps the entity ambiguous. It does not depict Allah, any deity, sacred or devotional imagery, scripture, call to prayer, sacred chant, real extremist names, real extremist symbols, propaganda, stereotypes, gore, readable text, or modern props.

## Validation evidence

`validation/validation.json` reports:

- 10 source frames and 10 processed frames.
- Every processed frame is exact 156x210 RGBA with alpha extrema 255/255.
- The sheet is exact 1560x210 and each 156x210 slice is pixel-equal to its processed frame.
- The final DDS is strict legacy uncompressed BGRA, one mip, pitch 6240, exact length 1310528 bytes, dimensions 1560x210, and alpha extrema 255/255.
- Static fallback evidence and the accepted runtime static DDS are exact 156x210 uncompressed BGRA, pitch 624, exact length 131168 bytes, alpha extrema 255/255, and pixel-equal to the fallback PNG.
- The review GIF contains 10 frames at 156x210 and remains review-only.
- The reviewed contact sheet and DDS round-trip show stable framing and the planned rest/contradiction/peak/return arc.

The evidence manifest is `docs/assets/031_random_terror/false_revelation_entity_animation/manifest.md`, and the ready-to-copy sprite snippet is `docs/assets/031_random_terror/false_revelation_entity_animation/gfx_handoff.md`.

## Parent follow-up and remaining review

The parent should bind the animated sprite to the terminal False Revelation entity portrait property and use the static alias for unsupported, hidden, disabled, or inactive states. The parent should perform live consumer review in the existing Event Details frame.

No known production blocker remains within this bounded worker scope. The package is ready for parent review; in-game visual validation was not performed because agents do not launch Hearts of Iron IV.
