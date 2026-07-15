# Event 014 CBA-CBD Warlord GFX Handoff

No `.gfx` edit is required. `interface/014_cannibalism.gfx` already registers the complete sprite family and was deliberately left unchanged.

## Existing registration

- `GFX_portrait_<TAG>_warlord` uses `leader_<TAG>_warlord.dds`.
- `GFX_portrait_<TAG>_warlord_europe` deliberately aliases the same default DDS.
- The six additional suffixes are `_africa`, `_asia`, `_middle_east`, `_north_america`, `_south_america`, and `_oceania`.
- This structure exists for each of CBA, CBB, CBC, and CBD at `interface/014_cannibalism.gfx:153` through `:184`.

## Installed texture contract

- Directory: `gfx/leaders/014_cannibalism/`.
- Changed files: the 28 `leader_CBA_warlord*.dds` through `leader_CBD_warlord*.dds` textures represented in `manifest.md`; every texture was reconverted from the final selected regenerated source set after the native-size action review.
- Dimensions: 156x210 each.
- Pixel format: uncompressed 32-bit RGBA/BGRA-compatible DDS with an opaque alpha channel.
- Expected byte length: 131,168 bytes each, including the 128-byte DDS header.
- Exact final processed-PNG and DDS SHA-256 values are recorded in `validation.md`.

No gameplay, localisation, interface, sprite, spreadsheet, flag, or unrelated texture file is part of this handoff.
