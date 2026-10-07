# Event 033 Acid Rain asset production prompt

Produce the authorized visual package for Chaos Redux Event 33.
Read `AGENTS.md`, the Event 33 asset requirements, [the asset owner skill](../../../../.agents/skills/chaos-redux-event-assets/SKILL.md), [the frame-animation skill](../../../../.agents/skills/chaos-redux-frame-animation/SKILL.md), and the current consumers and GFX registries before creating anything.
Route non-portrait sourcing, generated scenes, and icons to their separate asset specialists under [the subagent contract](../../../../.agents/skills/chaos-redux-subagents/SKILL.md).
The parent owns final non-portrait GFX and gameplay wiring; the event UI worker owns only the dedicated Acid Rain window under the scripted-GUI skill.
The completion auditor reviews the integrated package after wiring.

## Visual target

Use a 1930s and 1940s civil-defense setting. Show corroded steel, stained stone, contaminated reservoirs, damaged railway infrastructure, field hospitals, protective capes, period respirators, pumps, shelters, and heavy rain. Use gray, yellow-brown, muted green, and rust-red. Avoid neon green, modern hazmat suits, modern vehicles, readable text inside art, copied propaganda, fantasy magic, or generic post-apocalyptic ruins that conceal the acid-rain subject.

Use the ten-source board in `research/033_acid_rain_visual_reference_board.md`.
The reference set must cover acid-damaged stone, acid-damaged forests, water and soil harm, wartime shelters, respirators, anti-gas instruction, protective clothing, period wardens, first-aid equipment, and rail or industrial corrosion.
Record source, license, access date, and the specific design fact taken from each reference.
Generate original compositions through native ImageGen under the asset owner skill.
Request native transparency for alpha-backed families and preserve it through processing and DDS conversion.

## Required event images

Create and register these exact outputs:

- `gfx/event_pictures/super_events/033_acid_rain.dds`, 457 by 328
- `gfx/event_pictures/033_acid_rain_arrival.dds`, 210 by 176
- `gfx/event_pictures/033_acid_rain_shelter.dds`, 210 by 176
- `gfx/event_pictures/033_acid_rain_severe.dds`, 210 by 176
- `gfx/event_pictures/033_acid_rain_transport.dds`, 210 by 176
- `gfx/event_pictures/033_acid_rain_dissipation.dds`, 210 by 176
- `gfx/event_pictures/news/033_acid_rain_news.dds`, 397 by 153 and grayscale
- `gfx/event_pictures/news/033_acid_rain_global_news.dds`, 397 by 153 and grayscale

The formation image should show a dark corrosive front arriving over a populated industrial region while civilians move toward shelters. Keep the main subject readable behind the super-event text and quote areas. The severe image needs a denser local storm core. The dissipation image should show damaged infrastructure and clearing weather without turning into a bright victory scene.

## Decision and modifier icons

Create 32 by 32 decision icons for the category, four permanent projects, five urgent actions, and four recovery actions listed in Part 10. Create 64 by 64 source icons for ordinary rain, strong rain, severe cell, global layer, global superstorm, aftermath tiers 1 to 3, and any reviewed country modifier that lacks a suitable existing icon. Use one clear silhouette per icon. Do not use small text. Aftermath tiers must share one base design with visibly increasing corrosion and runoff.

Create ten 64 by 64 achievement masters and their required state triplets under the asset owner skill.
Preserve one visual family and make each requirement recognizable without relying on text or tiny counters.

## Scripted GUI map and animation

Create a neutral world-map base and seven region overlays matching the stable Event 33 region IDs. Provide visited, warning, ordinary active, severe, and global-layer presentation states. Create front-card background, coverage-bar frame and fill, Preparedness badge, four component pips, front marker, severe marker, warning marker, and static fallbacks.

Create real frame sequences through the frame-animation pipeline:

- `acid_rain_front_00.dds` through the reviewed final frame count, 8 to 12 frames
- `acid_rain_warning_00.dds` through the reviewed final frame count, 6 to 8 frames
- `acid_rain_severe_00.dds` through the reviewed final frame count, 8 frames
- `acid_rain_global_00.dds` through the reviewed final frame count, 8 to 12 frames

Do not manufacture a sequence by simple rotation, scaling, opacity changes, or repeated copies of one still.
Preserve stable composition and create real cloud and rain movement.
Provide a static fallback for each sequence and assemble the runtime frame sheet required by the frame-animation skill.
Review cadence through the animation preview and matching MCP GUI renders, and avoid fast flashing.

## Registration and proof

Prefer one parent-owned registry, `interface/033_acid_rain.gfx`, unless current repository ownership requires a different reviewed location.
Every sprite ID must resolve to one texture path.
Update the asset manifest and wiring handoff with source PNG, final DDS, dimensions, alpha, compression, mipmap rule, sprite ID, generation record, reuse status, and inspection result.

Validate every file for dimensions, alpha, blank output, stretching, readable silhouette, correct path, registered sprite, and low-resolution UI fit. Test at 1920 by 1080, 1600 by 900, and 1366 by 768. Do not mark the task complete while placeholders, missing frames, unregistered textures, or copied reference images remain.
