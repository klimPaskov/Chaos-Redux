# Event 006 Leader Portrait Manifest

Status: generated with imagegen, processed, converted, and wired.

## Current Scope

This manifest records the 2026-06-08 fictional leader portrait created for the Independence Wave African strange-story lane.

| id | source_mode | source_png | processed_png | final_dds | sprite | notes |
| --- | --- | --- | --- | --- | --- | --- |
| `portrait_independence_wave_gorilla_chair` | imagegen | `docs/assets/006_independence_wave/leader_portraits/source_png/portrait_independence_wave_gorilla_chair_source.png` | `docs/assets/006_independence_wave/leader_portraits/processed_png/portrait_independence_wave_gorilla_chair.png` | `gfx/leaders/006_independence_wave/portrait_independence_wave_gorilla_chair.dds` | `GFX_portrait_independence_wave_gorilla_chair` | Fictional gorilla head-of-state portrait for the Gorilla Chair decision route. Not based on a real person. |

## Prompt Summary

The source art was generated as a HOI4-style fictional leader portrait: a serious gorilla head-of-state in a subdued 1930s military tunic with sash and council medal, centered on a dark official studio backdrop. No text, watermark, modern props, cartoon styling, gore, or comedy elements were requested.

## Wiring

- Sprite registration: `interface/chaosx_characters.gfx`
- Gameplay caller: `independence_wave_seat_the_gorilla_chair_effect`
- Final texture size: `156x210`
