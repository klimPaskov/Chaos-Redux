# Air Winter Regional Particle Frame Brief

## Purpose

Create dedicated, fictional particle art for four ordinary-map climate families:

1. regional snow and frost
2. cold rain and mist
3. ash and dirty snow
4. thaw and flood

The animation must convey changing particle shape and density through separately authored frames. It must not be manufactured by translating, rotating, scaling, warping, blurring, recoloring, or filtering one still image.

## Visual rules

- Keep cold separate from soot. Snow/frost is pale blue-white. Ash/dirty snow is charcoal-grey with contaminated clumps.
- Keep warm-region cold legible without snow: cold rain/mist uses long droplets, suspended beads, and fog wisps.
- Make recovery materially different: thaw/flood uses droplets, splash crowns, ripples, wet fragments, and melt runoff.
- Use no radiation-green or toxic-amber cues. Those belong to separate hazard art.
- Use a black source background so the processing step can derive a clean alpha channel.
- Avoid text, symbols, UI frames, flags, logos, recognizable landmarks, or photographic scenery.
- Design each frame as a particle cell, not as a complete landscape.

## Authored source arrangement

The approved generated source is a 4x4 atlas at `source_png/particles/regional_particle_frames_source.png`.

Rows, top to bottom:

1. `snow_frost`
2. `cold_rain_mist`
3. `ash_dirty_snow`
4. `thaw_flood`

Columns, left to right, are authored states 1-4. The processing script extracts every cell into a separate 384x384 source file under `source_png/particles/source_frames/<family>/frame_01_source.png` through `frame_04_source.png`. Those files are the source-frame proof required by the animation workflow.

## Runtime output

Each authored state becomes a 256x256 RGBA processed frame. Four frames are packed horizontally into a 1024x256 atlas. The PDX particle definitions declare `x = 4` and `y = 1` and use the family-specific atlas.

The particle system supplies movement, velocity, rotation, fade, and forces. The authored atlas supplies changing internal silhouettes, clusters, droplets, flakes, and splashes. The animation therefore does not depend on transform-only manipulation of one still.

## Static fallback

Frame 1 of each family is the approved static state because it has the clearest silhouette at small map scale. It is exported in two forms:

- a normal-mapped three-card mesh entity for ordinary-map placement
- a registered GUI sprite for a possible UI-based accessibility route

The static route must replace the animated route. The two should not stack.

## Palette and readability

| Family | Primary palette | Readability target |
| --- | --- | --- |
| Snow/frost | blue-white, pale cyan, muted grey | readable over dark terrain without becoming a radiation cue |
| Cold rain/mist | slate blue, cold grey, subdued cyan | visible over warm classes without suggesting snowfall |
| Ash/dirty snow | charcoal, dirty grey, cold off-white | dominant soot signal at phases 4-6 |
| Thaw/flood | wet slate, desaturated blue, muddy grey | visibly different from bright frozen water |

## Evidence

- `contact_sheets/particle_authored_frames.png` shows all 16 authored states together.
- `contact_sheets/particle_static_fallbacks.png` shows the chosen fallback frames.
- `previews/snow_frost_authored_frames.gif`
- `previews/cold_rain_mist_authored_frames.gif`
- `previews/ash_dirty_snow_authored_frames.gif`
- `previews/thaw_flood_authored_frames.gif`

The GIFs are review previews only. They use frame durations of 240, 200, 180, and 220 milliseconds. Runtime timing remains controlled by each PDX particle definition and particle lifetime.
