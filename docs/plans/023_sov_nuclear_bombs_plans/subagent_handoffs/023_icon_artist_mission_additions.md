# Event 023 mission-icon additions handoff

Status: production complete; parent `.gfx` wiring and visual review remain `needs_user_review`.

This append-only handoff covers exactly two new mission icon assets for the accepted Event 23 decision map. Existing Event 23 assets, source files, processed previews, runtime DDS files, manifests, and handoffs were not overwritten or regenerated.

## Source and runtime inventory

| Asset / mission consumer | Native-alpha source PNG | Processed PNG | Runtime DDS | Size | SHA-256 source | SHA-256 processed | SHA-256 DDS |
| --- | --- | --- | --- | ---: | --- | --- | --- |
| `sov_nuclear_bombs_delivery_crews_mission` | `docs/assets/023_sov_nuclear_bombs/source_png/missions/sov_nuclear_bombs_delivery_crews_mission_source.png` | `docs/assets/023_sov_nuclear_bombs/processed_png/missions/sov_nuclear_bombs_delivery_crews_mission_33x32.png` | `gfx/interface/decisions/023_sov_nuclear_bombs/sov_nuclear_bombs_mission_delivery_crews.dds` | 33x32 | `341d96191631f60bbfa1d1fae54c4ff2aeafc1d3e08ba4616a8e02bdeb887389` | `3f34700aed157b10679c9fc61765dbc4a103e334c248c42151ebc7441db9cdcf` | `42e08118bbcd2776a08ac8d7aa4d7f9823990aa54700accadf7ec8553d357a1c` |
| `sov_nuclear_bombs_command_exercise_mission` | `docs/assets/023_sov_nuclear_bombs/source_png/missions/sov_nuclear_bombs_command_exercise_mission_source.png` | `docs/assets/023_sov_nuclear_bombs/processed_png/missions/sov_nuclear_bombs_command_exercise_mission_33x32.png` | `gfx/interface/decisions/023_sov_nuclear_bombs/sov_nuclear_bombs_mission_command_exercise.dds` | 33x32 | `f38a9d85f2ca6d64919dbb6bef7896f78a31323bd0d6256cdeac4ed13a467b93` | `ef1e466aceff0c6cf74f3af3cb3c16807129035f80dea9000535cfbe8d2c0e0f` | `6ff65f2c9a2da712184265a88919b0b7d4db1375897bad1232550fe9a090386d` |

The source prompts are `docs/assets/023_sov_nuclear_bombs/prompts/sov_nuclear_bombs_delivery_crews_mission.txt` and `docs/assets/023_sov_nuclear_bombs/prompts/sov_nuclear_bombs_command_exercise_mission.txt`.

## Proposed parent-owned sprite aliases

Add these exact aliases to the existing parent-owned `interface/023_sov_nuclear_bombs.gfx` registry when wiring the mission consumers.

```text
spriteType = {
	name = "GFX_mission_sov_nuclear_bombs_delivery_crews_mission"
	texturefile = "gfx/interface/decisions/023_sov_nuclear_bombs/sov_nuclear_bombs_mission_delivery_crews.dds"
}

spriteType = {
	name = "GFX_mission_sov_nuclear_bombs_command_exercise_mission"
	texturefile = "gfx/interface/decisions/023_sov_nuclear_bombs/sov_nuclear_bombs_mission_command_exercise.dds"
}
```

The expected mission consumers are `sov_nuclear_bombs_delivery_crews_mission` and `sov_nuclear_bombs_command_exercise_mission`, activated by the parent-owned Event 23 decision/effect implementation. This handoff does not edit those gameplay consumers or the `.gfx` file.

## Production and reference record

Both assets were generated with the official built-in ImageGen workflow on 2026-09-01. The initial prompts requested a genuinely transparent background, no readable text, no watermark, and no opaque or chroma backdrop. The delivery-crews source depicts paired period bomber flight helmets, a flight instrument, and a certification seal. The command-exercise source depicts paired period Bakelite handsets, a dual-key authentication block, and a red signal lamp. These subjects are distinct from the existing Event 23 decision delivery-preparation, command-exercise, and authentication icons.

Before generation, the canonical contact sheet `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/missions/contact_sheet.png` and all five individual references in that same canonical folder were inspected. No project-local visual-reference copy was used as the canonical reference source.

Processing used the existing Event 23 contained Lanczos convention with a 31x30 inner fit, one-pixel transparent inset, and alpha clamp below 2. The source PNGs are RGBA with alpha range 0..255. The processed PNGs are exactly 33x32 RGBA with alpha range 0..255, all four corners at alpha 0, and visible bounds `(1, 1, 32, 31)`. The command-exercise source has one bottom-left source pixel at alpha 1 from an anti-aliased edge; the established processing clamp removes that fringe in the processed/runtime files without changing the subject silhouette.

## Validation and review evidence

Validation record: `docs/assets/023_sov_nuclear_bombs/notes/mission_additions_validation.md` and machine-readable facts: `docs/assets/023_sov_nuclear_bombs/notes/mission_additions_validation.json`.

Contact sheets: `docs/assets/023_sov_nuclear_bombs/contact_sheets/mission_additions_contact_sheet.png` shows source, processed smooth enlargement, and decoded DDS round-trip over checkerboard. `docs/assets/023_sov_nuclear_bombs/contact_sheets/mission_additions_alpha_review.png` shows processed and DDS views over charcoal and ivory backgrounds.

Each DDS is 4352 bytes, 33x32, pitch 132, one-level, uncompressed 32-bit BGRA with the required legacy header masks and `DDSCAPS_TEXTURE` 0x1000. Decoded DDS pixels match the processed PNG byte-for-byte for both assets. No background-removal fallback was used.

## Remaining review and issues

Both assets are `needs_user_review` until the parent visually reviews the contact sheets, adds the proposed aliases, and connects the mission consumers. There is no production blocker. The only recorded QA note is the single alpha-1 anti-aliased source corner on the command-exercise source, which is clamped to transparent in the final processed/runtime outputs.

No animation, portrait, flag, counter, equipment, event art, additional asset family, gameplay file, localisation file, GUI file, spreadsheet, or final commit was created or edited by this handoff.
