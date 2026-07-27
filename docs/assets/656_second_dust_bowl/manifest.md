# Spec 66 The Second Dust Bowl asset manifest

## Requirement-to-runtime crosswalk

| Requirement | Source package | Runtime output | Runtime registration | Consumer | Status |
| --- | --- | --- | --- | --- | --- |
| Spec 66 report image, fictional ash-darkened North American plains with farm families, trucks, windbreaks, and covered seed rows, static 210x176 report card | `source_png/report_event_fallout_second_dust_bowl_source.png` -> `processed_png/report_event_fallout_second_dust_bowl.png` | `gfx/event_pictures/fallout_world_end/report_event_fallout_second_dust_bowl.dds` | Registered `GFX_report_event_fallout_second_dust_bowl` in `interface/fallout_world_end.gfx` | Events `chaosx.fallout.656`, `chaosx.fallout.658`, and `chaosx.fallout.660` | static wiring present in dormant reviewed tranche, live presentation unverified |

## Asset entry

- Asset name: `report_event_fallout_second_dust_bowl`
- Related event: Spec 66, The Second Dust Bowl.
- Asset type: static report event picture.
- Intended use: HOI4 report-card event image.
- Source mode: `$imagegen` generated fictional/alternate-history scene.
- Generation fit: the event depicts an invented second Dust Bowl rather than a real documented person, place, battle, or archival object. Generation gives the required specific farmstead composition without recreating a famous photograph.
- Source PNG: `docs/assets/656_second_dust_bowl/source_png/report_event_fallout_second_dust_bowl_source.png`
- Source PNG SHA-256: `A7B4542648AF14B3D4DD9C766819397E6F4030B8A14E2993EC1E3952D205287B`
- Source PNG dimensions/mode: `1370x1148`, `RGB`.
- Processed PNG: `docs/assets/656_second_dust_bowl/processed_png/report_event_fallout_second_dust_bowl.png`
- Processed PNG SHA-256: `CD5738165E2D1BED925117A8C28079D7233CE857945EE62A50E4738127D54526`
- Processed PNG dimensions/mode: `210x176`, `RGBA`. Transparent outer corners match the vanilla report-card presentation.
- Final DDS: `gfx/event_pictures/fallout_world_end/report_event_fallout_second_dust_bowl.dds`
- Final DDS SHA-256: `2C8E2044A94FF07DE7DD95D7D23D5375D2DFEEAE6CC96B3263150F41C78A352D`
- Final DDS dimensions: `210x176`. It is one-level uncompressed BGRA 32-bit.
- Runtime sprite name: `GFX_report_event_fallout_second_dust_bowl`.
- Target `.gfx`: `interface/fallout_world_end.gfx`.
- Localisation key: not applicable to the asset package. Event localisation remains separate.
- Related consumers: opening, delayed result, and planting callback events for Spec 66.
- Animation/audio: not applicable. This is a static report image.
- Status: `static wiring present in dormant reviewed tranche`. Source, processing, runtime DDS, `.gfx` registration, and event consumers are present. This asset does not activate the chain or establish runtime acceptance. Live presentation remains unverified because HOI4 was not launched.

## Visual and source constraints

The generated scene is fictional and alternate-history. It contains no real-person likeness, famous archival composition, readable text, brands, flags, attested symbols, zombie imagery, animation, or audio. Period clothing, farm trucks, architecture, and documentary monochrome treatment were requested explicitly.

Canonical visual reference inspected before generation: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/report/contact_sheet.png` plus the report-art entries in `README.md` and `CATALOG.md`. The reference family establishes the `210x176` card canvas, monochrome/sepia documentary treatment, and transparent tilted-card presentation. No reference pixels were reused.
