# Fallout Triage Wall report asset manifest

## Package

- Event family: The Triage Wall
- Event identity: fictional Fallout survival event family
- Package slug: `fallout_triage_wall`
- Asset requirement: one unique report-event image
- Requirement source: parent asset brief dated 2026-07-22, with the event-family choice contract in `fallout_global_event_family_matrix.md`
- Source mode: `$imagegen`
- Source rationale: the scene is fictional and has no real archival source requirement. Generated documentary art gives the triage wall a specific authored identity while keeping the Fallout survival setting distinct from other report assets.
- Reference family inspected: canonical `assets/vanilla_reference/event_art/report/` and its `contact_sheet.png`
- Existing Fallout and zombie art: not reused. No existing Fallout or zombie basename, sprite id, DDS path, or source image was used.

## Asset entry

### `fallout_triage_wall_report`

- Asset type: report event image
- Intended use: report image for The Triage Wall medicine-allocation event
- Source mode: `$imagegen`
- Generation record: built-in ImageGen output `C:\Users\klimp\.codex\generated_images\019f8af2-57fd-7160-af39-65304923f8fa\exec-25d57f33-2ea3-4127-90fd-f34a75a11980.png`
- Prompt record: `docs/assets/fallout_triage_wall/prompts/fallout_triage_wall_report_prompt.txt`
- Source PNG: `docs/assets/fallout_triage_wall/source_png/fallout_triage_wall_report_source.png`
- Processed PNG preview: `docs/assets/fallout_triage_wall/processed_png/fallout_triage_wall_report.png`
- Final DDS: `gfx/event_pictures/fallout_triage_wall/fallout_triage_wall_report.dds`
- Target size: `210x176`
- Sprite name: `GFX_report_event_fallout_triage_wall`
- `.gfx` target: `interface/fallout_world_end.gfx`
- Localisation key: `chaosx.fallout.175.t` and result family `chaosx.fallout.177` through `chaosx.fallout.185`
- Related event id: `chaosx.fallout.175` through `chaosx.fallout.187`
- Scene identity: improvised shelter clinic triage wall with cloth tabs, punched metal tags, wooden tally blocks, anatomical diagram, gloved medic forearm, enamel tray, ampoules, hand-crank lamp, and respirator cabinet
- Intentional exclusions: no patient queue, no crowd, no zombies, no monsters, no blood, no gore, no readable text, no map, no UI overlay, no modern props
- Report treatment: processed with `process_report_event_image.py` using the repository black-and-white, sepia, grain, tilted-card, transparent-corner treatment
- Status: `wired`

## Requirement to runtime coverage

| Requirement | Source package and manifest entry | Runtime artifact | Sprite or owning definition | Consumer | Status |
| --- | --- | --- | --- | --- | --- |
| Triage Wall report image | `fallout_triage_wall_report` in this manifest | `gfx/event_pictures/fallout_triage_wall/fallout_triage_wall_report.dds` | `GFX_report_event_fallout_triage_wall` in `interface/fallout_world_end.gfx` | Triage Wall events `175` through `187` | wired |

## Validation evidence

- Processed PNG is exactly `210x176` RGBA.
- Processed PNG corner pixels are transparent: `(0,0)`, `(209,0)`, `(0,175)`, and `(209,175)` all have alpha `0`.
- Processed PNG alpha range is `0..255`.
- DDS is exactly `147968` bytes, matching `128 + 210 * 176 * 4`.
- DDS header declares width `210`, height `176`, header size `124`, pixel format size `32`, flags `65`, fourCC `0`, bit count `32`, BGRA masks `0x00FF0000`, `0x0000FF00`, `0x000000FF`, `0xFF000000`, and texture caps `0x1000`.
- Final `.gfx` registration is wired in `interface/fallout_world_end.gfx`.
- SHA256 source PNG: `34D82FCFD04DE34443CF0B95DAB5696F91A976C852F6BAD8E32CD365E5A3B151`
- SHA256 processed PNG: `9AF0B66638152A54708C852D90C9AD6FD165A2F6F297744C1B66D878977A5151`
- SHA256 final DDS: `0304EDAA55EAFF749F38D8AEA602819AB7BECCDCEB4EE8596F92B322E26C276B`

## Review note

The processed PNG is the review preview for this single-asset package. Independent visual review should confirm that the triage wall remains legible at report size and remains distinct from the existing Fallout well queue, Fallout orientation, Fallout living-world, and zombie asset families before final wiring.
