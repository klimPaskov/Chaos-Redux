# Captured biological-facility recovery raid icon package

Package date: 2026-07-22  
Asset family: native HOI4 military raid `custom_map_icon` / raid-type map icon  
Related system: `chaos_warfare_system`, `stage_7_biological_warfare`  
Package status: complete static assets; parent `.gfx`/raid wiring handed off  
Source mode: `$imagegen` built-in image generation, with official chroma-key alpha extraction  
Animation: none; these are two independent static icons.

## Shared runtime contract

- Native canvas: 32x32 pixels, selected from exact vanilla raid-type DDS references and existing Chaos Redux raid-type assets.
- Transparency: RGBA source/processed previews with transparent unused pixels and no opaque square background.
- Final DDS: uncompressed 32-bit BGRA / B8G8R8A8, one mip level, legacy 128-byte header, exact 4224-byte file length.
- Suggested `.gfx`: `interface/chaosx_raids.gfx`.
- Related engine field: raid definition `custom_map_icon`.
- No generated text, gore, active-agent cloud, or operational biological procedure is present.

## Asset 1 — secure / preserve

- Requirement id: `bio_facility_secure_preserve_raid`
- Asset type: military raid type map icon
- Intended use: native raid map icon for securing and preserving a captured facility, emphasizing sealed access, armed biosecurity control, evidence custody, and containment.
- Independent generation: yes; separate ImageGen call from asset 2.
- Prompt record: `prompts/bio_facility_secure_preserve_raid_prompt.md`
- ImageGen source PNG: `source_png/bio_facility_secure_preserve_raid_source.png` (1254x1254 RGB)
- Processed PNG preview: `processed_png/bio_facility_secure_preserve_raid.png` (32x32 RGBA)
- Final DDS: `gfx/interface/raids/stage_7_biological_warfare/raid_type_icon_bio_facility_secure_preserve.dds` (32x32)
- Sprite id: `GFX_raid_type_icon_bio_facility_secure_preserve`
- Localisation: none; sprite-only asset
- Related runtime id: `bio_facility_secure_preserve_raid`
- Status: `handed_off`
- Notes: sealed steel/brass doorway with a containment seal, lock, compact shield cues, and a secured ledger/evidence case. No laboratory procedure is shown.

## Asset 2 — destroy safely

- Requirement id: `bio_facility_destroy_safely_raid`
- Asset type: military raid type map icon
- Intended use: native raid map icon for methodically neutralizing a captured arsenal chamber while maintaining containment.
- Independent generation: yes; separate ImageGen call from asset 1.
- Prompt record: `prompts/bio_facility_destroy_safely_raid_prompt.md`
- ImageGen source PNG: `source_png/bio_facility_destroy_safely_raid_source.png` (1254x1254 RGB)
- Processed PNG preview: `processed_png/bio_facility_destroy_safely_raid.png` (32x32 RGBA)
- Final DDS: `gfx/interface/raids/stage_7_biological_warfare/raid_type_icon_bio_facility_destroy_safely.dds` (32x32)
- Sprite id: `GFX_raid_type_icon_bio_facility_destroy_safely`
- Localisation: none; sprite-only asset
- Related runtime id: `bio_facility_destroy_safely_raid`
- Status: `handed_off`
- Notes: circular sealed chamber with crossed inert canister silhouettes and a controlled timer/demolition marker. No release, gore, smoke, flame, or active agent cloud is shown.

## Review and handoff files

- Contact sheet: `contact_sheets/captured_facility_raid_icons_contact_sheet.png`
- Validation: `notes/validation.md`
- SHA-256 records: `notes/hashes.sha256`
- Coverage crosswalk: `coverage_crosswalk.md`
- GFX handoff: `gfx_handoff.md`
- Parent handoff: `docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-07-22_biological_captured_facility_raid_icons_handoff.md`
