# Asset subagent handoff — captured biological-facility recovery raid icons

Date: 2026-07-22  
Scope: exactly two independent native HOI4 raid-type icon packages  
Producer scope: new asset/package/handoff paths only

## Completed assets

| Requirement id | Final DDS | Sprite id | Size | Status |
|---|---|---|---:|---|
| `bio_facility_secure_preserve_raid` | `gfx/interface/raids/stage_7_biological_warfare/raid_type_icon_bio_facility_secure_preserve.dds` | `GFX_raid_type_icon_bio_facility_secure_preserve` | 32x32 | handed_off |
| `bio_facility_destroy_safely_raid` | `gfx/interface/raids/stage_7_biological_warfare/raid_type_icon_bio_facility_destroy_safely.dds` | `GFX_raid_type_icon_bio_facility_destroy_safely` | 32x32 | handed_off |

## Package contents

Package root:

`docs/assets/chaos_warfare_system/stage_7_biological_warfare/captured_facility_raid_icons/`

- independent ImageGen source masters in `source_png/`
- exact 32x32 RGBA processed previews in `processed_png/`
- prompt records in `prompts/`
- review contact sheet in `contact_sheets/captured_facility_raid_icons_contact_sheet.png`
- manifest, coverage crosswalk, validation, and hashes
- exact copy-ready `.gfx` entries in `gfx_handoff.md`

## Exact `.gfx` wiring handoff

Suggested existing target: `interface/chaosx_raids.gfx`.

```text
spriteType = {
	name = "GFX_raid_type_icon_bio_facility_secure_preserve"
	texturefile = "gfx/interface/raids/stage_7_biological_warfare/raid_type_icon_bio_facility_secure_preserve.dds"
}
spriteType = {
	name = "GFX_raid_type_icon_bio_facility_destroy_safely"
	texturefile = "gfx/interface/raids/stage_7_biological_warfare/raid_type_icon_bio_facility_destroy_safely.dds"
}
```

The parent should reference the exact sprite ids above from the corresponding raid definitions' `custom_map_icon` fields. This subagent did not edit `.gfx`, `.gui`, gameplay, raids, localisation, or any existing icon.

## Visual semantics

- `bio_facility_secure_preserve_raid`: sealed laboratory/arsenal doorway, shield-and-lock containment mark, and secured ledger/evidence case; orderly armed-control symbolism.
- `bio_facility_destroy_safely_raid`: sealed arsenal chamber, crossed inert canisters, and a controlled timer/demolition marker; methodical safe-neutralization symbolism.

Both are fictional symbolic UI art only. Neither depicts operational biological procedures, gore, active agent clouds, smoke, flames, or release.

## Source and conversion evidence

- Both icons were generated with separate built-in ImageGen calls; neither is a recolor, crop, transform, cross-type resize, or derivative of the other.
- Official `remove_chroma_key.py` was used on the flat `#00ff00` source background with soft matte, despill, and edge contract 1.
- Processed previews are 32x32 RGBA with transparent corners and no opaque-ish green pixels.
- DDS conversion used `python -B .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` from the mod root.
- Both DDS files are 4224 bytes with exact 32x32 dimensions, 32-bit uncompressed BGRA/B8G8R8A8, one mip level, texture caps `0x1000`, and alpha range 0..255.
- DDS decoded pixels match the processed PNGs byte-for-byte after BGRA→RGBA channel reorder.
- Full evidence: `docs/assets/chaos_warfare_system/stage_7_biological_warfare/captured_facility_raid_icons/notes/validation.md`.

## Remaining parent action

Register the two exact sprite entries in the existing Chaos Redux raid `.gfx` file and reference the exact sprite ids from the requested raid definitions. No asset naming or path uncertainty remains.
