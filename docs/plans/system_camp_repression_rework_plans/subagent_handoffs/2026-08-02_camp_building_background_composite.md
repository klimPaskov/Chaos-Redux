# Camp building background composite handoff

Status: complete for the requested deterministic strip correction.

The runtime strip was subsequently recovered by `2026-08-03_building_icon_strip_recovery.md`; the checksum and first-33-payload statements below describe the pre-recovery runtime and are retained as historical evidence for the camp-frame composite.

## Runtime change

- Updated only `gfx/interface/buildings/building_icon_strip.dds`.
- Frames 34 and 35 now use the exact user-provided `gfx/interface/buildings/building_background.png` as their background while retaining the accepted ochre watchtower/fence and crematorium/chimney/fence pictograms.
- Frames 1-33 remain payload-byte identical to the pre-change strip.
- The strip remains 35 frames at `1610x46` with `46x46` frames.
- Historical composite strip SHA-256: `de2dc7538003b3966a64d4d8ad303e98ab4930a281cd60040bf01419e33bd1bf`.
- Historical pre-composite strip SHA-256: `c7359e1ff2de6d3105c0ef152adc12583aec43fd03ba42204810087ac520acdd`.

## User source provenance

The background was user-provided at `gfx/interface/buildings/building_background.png`.

- SHA-256: `0f462f0124d77862cbd36e8d8d4c69f222905b81d7270afa6a680ba7d489fe`.
- Decoded dimensions: `46x46`.
- Decoded mode: `RGBA`.
- Alpha extrema: `0..255`.

## Foreground extraction

The accepted ochre source foregrounds were retained from:

- `docs/assets/system_camp_building_icons_hoi4_style/processed_concentration_strip_frame34_46x46.png` (source hash `7e6d51e60cf6725efe1f655ffdee73b39bfedfc4cd57354a898d3ebe9f1ef806`).
- `docs/assets/system_camp_building_icons_hoi4_style/processed_extermination_strip_frame35_46x46.png` (source hash `1d1e0b89686f26fb0b9b09ae8f6aff781fa8a49792e1f4ec614a25e0b65a405b`).

The mask uses a warm-pixel seed (`red - max(green, blue) >= 8` and `red >= 20`) with a one-pixel expansion to retain the existing dark outline/shadow. The old generated charcoal tile and border are not included. Outside the final masks, every frame-34 and frame-35 pixel is byte-for-byte equal to the supplied background.

## Exact validation results

- Final DDS header: magic `DDS `, header size `124`, pixel format size `32`, flags `65`, fourCC `0`, 32-bit BGRA masks `0x00FF0000/0x0000FF00/0x000000FF/0xFF000000`, `DDSCAPS_TEXTURE=0x1000`.
- Dimensions: `1610x46`; exact file length `296368` bytes.
- Frame count: `35`.
- Frames 1-33 payload byte equality: `true`.
- Frame 34/35 final payloads decode exactly to their processed PNG previews: `true` for both.
- Frame 34 outside-mask background equality: `1380/1380` pixels exact.
- Frame 35 outside-mask background equality: `1382/1382` pixels exact.
- Final alpha extrema: `0..255`.
- Full machine-readable evidence: `docs/assets/system_camp_building_background_composite/evidence/runtime_validation.json` and `evidence/validation.json`.

## Review evidence

Permanent contact sheet: [2026-08-02_camp_building_background_composite_contact_sheet.png](2026-08-02_camp_building_background_composite_contact_sheet.png).

Temporary package: `docs/assets/system_camp_building_background_composite/` contains the copied user source, accepted source foregrounds, extracted masks and checker previews, final frame previews, full processed strip PNG, candidate DDS, validation JSON, source note, manifest, and reproducible processing scripts.

## Unchanged and skipped surfaces

- Standalone `gfx/interface/buildings/building_concentration_camp.dds` and `building_extermination_camp.dds` were not modified.
- No `.gfx`, `.gui`, gameplay, localisation, spreadsheet, or unrelated docs were modified.
- No Hearts of Iron IV launch or live consumer validation was performed; parent/user owns that gate.
- Parent cleanup duty: retain the temporary evidence workspace until acceptance, then remove it only when the user-approved cleanup point is reached. Keep this permanent handoff and contact sheet.
