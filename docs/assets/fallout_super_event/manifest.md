# Fallout Super-Event Asset Manifest

## Package

This package supports the fallout air-contamination collapse super-event documented in `docs/events/002_zombie_outbreak.md`.

Source and processed PNG previews live under:

- `docs/assets/fallout_super_event/source_png/`
- `docs/assets/fallout_super_event/processed_png/`

## Final Assets

| Asset | Type | Final path | Sprite | Size |
| --- | --- | --- | --- | --- |
| Fallout | super-event art | `gfx/super_events/super_event_fallout.dds` | `GFX_super_event_fallout` | 457x328 |

## Wiring

- `interface/chaosx_super_events.gfx` registers `GFX_super_event_fallout`.
- `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt` maps super-event slot `4` to `GFX_super_event_fallout`.
- `events/chemical_warfare_events.txt` shows super-event slot `4` and marks `world_end_fallout`.

## Super-Event Art Record

- Asset name: Fallout
- Related event id: `super_event.4.*`
- Related event slug: `fallout_super_event`
- Asset type: super-event image
- Intended in-game use: world-end super-event image for `GFX_super_event_fallout`
- Source mode: `image_gen`
- Image generation prompt: `Create a single HOI4 super-event image in a bleak alternate-history documentary style, intended to be cropped to 457x328. Subject: "Fallout" as a global atmospheric collapse after nuclear contamination. Scene: a ruined modern city and empty highway under a radioactive ash sky, distant nuclear fire glow behind broken towers, black snow and dust drifting through the street, abandoned evacuation buses and collapsed power lines, dim silhouettes of civil-defense structures, cold ration-line barriers with no readable signs, a sickly white-gray sun hidden by fallout clouds. Visual language: cinematic black-and-white with subtle toxic amber and red-orange glow, grainy wartime newsreel texture, realistic painted-photographic finish, strong central composition readable at small size, oppressive and cold. Avoid: text, captions, UI elements, watermarks, visible gore, readable signage, cluttered tiny details, cartoon style.`
- Source PNG path: `docs/assets/fallout_super_event/source_png/super_event_fallout_source.png`
- Processed PNG path: `docs/assets/fallout_super_event/processed_png/super_event_fallout.png`
- Final DDS path: `gfx/super_events/super_event_fallout.dds`
- Target size: 457x328
- Sprite name: `GFX_super_event_fallout`
- `.gfx` file: `interface/chaosx_super_events.gfx`
- Related super-event: `4`
- Review status: `needs_user_review`
- Notes: cropped and resized to 457x328, converted to uncompressed ARGB8888 DDS, and placed under the existing sprite definition.
- Asset status: `wired`
