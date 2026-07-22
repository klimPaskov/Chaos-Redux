# Validation record

Date: 2026-07-22

## Reference analysis

Inspected the canonical vanilla military-raid reference set:

- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/military_raids/contact_sheet.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/military_raids/raid_unit_air_raids.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/military_raids/raid_unit_paratrooper.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/CATALOG.md`
- vanilla raid-type DDS references: `raid_type_icon_facility_raid.dds`, `raid_type_icon_nuclear_facility_raid.dds`, and `raid_type_icon_oilfield_raid.dds`

Inspected read-only existing Chaos Redux raid-type references:

- `gfx/interface/military_raids/map_icons/raid_type_icon_chemical_sarin_strike.dds`
- `gfx/interface/military_raids/map_icons/raid_type_icon_zombie_cure_strike.dds`
- `interface/chaosx_raids.gfx`

The matching family reads as a compact, centered 32x32 transparent map icon with a dark outline, warm brass/ochre highlights, and a single readable subject. Vanilla raid-type textures are 32x32, uncompressed B8G8R8A8, one level, with 4224-byte files. Existing Chaos Redux raid-type examples are also 32x32 uncompressed BGRA but retain a legacy mip chain (5588 bytes); the new package follows the active repository converter contract and vanilla one-level header.

## Source and alpha validation

- Both source masters are independent ImageGen outputs at 1254x1254 RGB.
- The official built-in ImageGen chroma-key workflow was used with `#00ff00`, followed by `remove_chroma_key.py` with border auto-key, soft matte, despill, and edge contract 1.
- Both processed PNGs are exact 32x32 RGBA.
- Both processed PNGs have fully transparent corners and alpha range 0..255.
- Preserve processed PNG: 413 fully transparent pixels; 0 opaque-ish green pixels.
- Destroy-safely processed PNG: 399 fully transparent pixels; 0 opaque-ish green pixels.
- The contact sheet shows both final previews over a checker background at 8x nearest-neighbour scale and is review-only.

## DDS validation

Both final DDS files passed the complete uncompressed one-level BGRA check:

- `DDS ` magic; header size 124; header flags `0x100f`.
- Declared dimensions 32x32; pitch 128.
- Pixel format size 32; flags `0x41` (`RGB | ALPHAPIXELS`); fourCC 0; bit count 32.
- Masks: R `0x00ff0000`, G `0x0000ff00`, B `0x000000ff`, A `0xff000000`.
- Texture caps `0x1000`; mip count 0; exact file length 4224 bytes.
- Alpha range 0..255; DDS BGRA decode matches each processed PNG's RGBA pixels byte-for-byte after channel reorder.

## Scope validation

- Only new package paths, two new final DDS paths, and the requested subagent handoff path were created.
- Existing `gfx/interface/military_raids` assets were read-only references and were not overwritten, renamed, resized, deleted, or edited.
- No gameplay, raid, localisation, `.gfx`, or `.gui` file was edited.
- No operational biological procedure is depicted; both icons are fictional containment/recovery symbols with no gore or active-agent cloud.
