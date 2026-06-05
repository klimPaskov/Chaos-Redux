# Event 006 DFR Ideology Flag Variants Handoff

## Scope

- Role: `chaosx_generated_event_art` / flag asset worker
- Task surface: Darfur Council (`DFR`) ideology flag assets only
- Base files preserved:
  - `gfx/flags/DFR.tga`
  - `gfx/flags/medium/DFR.tga`
  - `gfx/flags/small/DFR.tga`
- Gameplay, localisation, `.gfx`, events, focuses, decisions, history, country files, and spreadsheets were not edited.

## Files Created

Final HOI4 TGA flags:

- `gfx/flags/DFR_democratic.tga`
- `gfx/flags/DFR_neutrality.tga`
- `gfx/flags/DFR_communism.tga`
- `gfx/flags/DFR_fascism.tga`
- `gfx/flags/medium/DFR_democratic.tga`
- `gfx/flags/medium/DFR_neutrality.tga`
- `gfx/flags/medium/DFR_communism.tga`
- `gfx/flags/medium/DFR_fascism.tga`
- `gfx/flags/small/DFR_democratic.tga`
- `gfx/flags/small/DFR_neutrality.tga`
- `gfx/flags/small/DFR_communism.tga`
- `gfx/flags/small/DFR_fascism.tga`

Source and processed review files:

- `docs/assets/006_independence_wave/flags/darfur/source_png/DFR_democratic_vector_source.png`
- `docs/assets/006_independence_wave/flags/darfur/source_png/DFR_neutrality_vector_source.png`
- `docs/assets/006_independence_wave/flags/darfur/source_png/DFR_communism_vector_source.png`
- `docs/assets/006_independence_wave/flags/darfur/source_png/DFR_fascism_vector_source.png`
- `docs/assets/006_independence_wave/flags/darfur/processed_png/DFR_democratic.png`
- `docs/assets/006_independence_wave/flags/darfur/processed_png/DFR_democratic_medium.png`
- `docs/assets/006_independence_wave/flags/darfur/processed_png/DFR_democratic_small.png`
- `docs/assets/006_independence_wave/flags/darfur/processed_png/DFR_neutrality.png`
- `docs/assets/006_independence_wave/flags/darfur/processed_png/DFR_neutrality_medium.png`
- `docs/assets/006_independence_wave/flags/darfur/processed_png/DFR_neutrality_small.png`
- `docs/assets/006_independence_wave/flags/darfur/processed_png/DFR_communism.png`
- `docs/assets/006_independence_wave/flags/darfur/processed_png/DFR_communism_medium.png`
- `docs/assets/006_independence_wave/flags/darfur/processed_png/DFR_communism_small.png`
- `docs/assets/006_independence_wave/flags/darfur/processed_png/DFR_fascism.png`
- `docs/assets/006_independence_wave/flags/darfur/processed_png/DFR_fascism_medium.png`
- `docs/assets/006_independence_wave/flags/darfur/processed_png/DFR_fascism_small.png`
- `docs/assets/006_independence_wave/flags/DFR_ideology_flags_contact.png`

Updated documentation:

- `docs/assets/006_independence_wave/flags/darfur/manifest.md`

## Method

- Used the existing base DFR flag as the style reference: green/red/black Darfur flag language with crescent symbolism.
- Built the four variants with ImageMagick vector drawing at 820x520, then downscaled to 82x52, 41x26, and 10x7.
- Converted final PNGs to uncompressed 32-bit RGBA TGA with `-orient TopLeft`, matching the existing DFR TGA header descriptor.
- No modern activist branding, readable text, real extremist symbols, or copied modern insignia were used.

Created variant identities:

- `DFR_democratic`: council tricolor with red hoist triangle, crescent, and council beads.
- `DFR_neutrality`: sultanate/authority standard with gold hoist and central crescent-star.
- `DFR_communism`: red popular-council banner with local crescent-star symbols and no hammer-and-sickle.
- `DFR_fascism`: dark emergency-authority standard with green hoist, red bar, and fictional spearhead/fortress emblem.

## Validation

ImageMagick `identify` confirmed dimensions, format, bit depth, alpha, compression, and orientation:

```text
DFR_democratic.tga TGA 82x52 8-bit srgba TrueColorAlpha None TopLeft
DFR_neutrality.tga TGA 82x52 8-bit srgba TrueColorAlpha None TopLeft
DFR_communism.tga TGA 82x52 8-bit srgba TrueColorAlpha None TopLeft
DFR_fascism.tga TGA 82x52 8-bit srgba TrueColorAlpha None TopLeft
DFR_democratic.tga TGA 41x26 8-bit srgba TrueColorAlpha None TopLeft
DFR_neutrality.tga TGA 41x26 8-bit srgba TrueColorAlpha None TopLeft
DFR_communism.tga TGA 41x26 8-bit srgba TrueColorAlpha None TopLeft
DFR_fascism.tga TGA 41x26 8-bit srgba TrueColorAlpha None TopLeft
DFR_democratic.tga TGA 10x7 8-bit srgba TrueColorAlpha None TopLeft
DFR_neutrality.tga TGA 10x7 8-bit srgba TrueColorAlpha None TopLeft
DFR_communism.tga TGA 10x7 8-bit srgba TrueColorAlpha None TopLeft
DFR_fascism.tga TGA 10x7 8-bit srgba TrueColorAlpha None TopLeft
```

TGA header checks matched the base DFR top-left-origin layout:

```text
gfx/flags/DFR_democratic.tga 000002000000000000000000520034002028
gfx/flags/DFR_neutrality.tga 000002000000000000000000520034002028
gfx/flags/DFR_communism.tga 000002000000000000000000520034002028
gfx/flags/DFR_fascism.tga 000002000000000000000000520034002028
gfx/flags/medium/DFR_democratic.tga 00000200000000000000000029001a002028
gfx/flags/medium/DFR_neutrality.tga 00000200000000000000000029001a002028
gfx/flags/medium/DFR_communism.tga 00000200000000000000000029001a002028
gfx/flags/medium/DFR_fascism.tga 00000200000000000000000029001a002028
gfx/flags/small/DFR_democratic.tga 0000020000000000000000000a0007002028
gfx/flags/small/DFR_neutrality.tga 0000020000000000000000000a0007002028
gfx/flags/small/DFR_communism.tga 0000020000000000000000000a0007002028
gfx/flags/small/DFR_fascism.tga 0000020000000000000000000a0007002028
```

SHA-256 checks confirmed the new variants are not byte-identical to the base or each other at normal and small sizes:

```text
ff32f9cb97de897b54beba27a8890d4cf917274914d8cc2c207762150f33409e  gfx/flags/DFR.tga
1dade368be093b007fe1aa0daf02653069c5a5e754bfe6ec562d60bb4751d444  gfx/flags/DFR_democratic.tga
2d06c9f5dc50b2b030dd5defbef2a227d641eeadce3d955f188d54c352a73000  gfx/flags/DFR_neutrality.tga
1c6b138d825c5b864c6c7750da92acf7ec39cc76841075ea48e04ebcb1802903  gfx/flags/DFR_communism.tga
fa83fcc63751a112f211f5c6825955f71d2d40c98d10eab7ad996037f3bd5e8f  gfx/flags/DFR_fascism.tga
d2bc6b548027a8943f7a5633c12844436f6a78b0c17498039f05d9c27ed1aa12  gfx/flags/small/DFR.tga
eb50805c722ebb7a56adb5b477db2f4a0b00dbe4de08548eb09a67c065728fbf  gfx/flags/small/DFR_democratic.tga
d1defd2da1fd428edc6a138e5ea38bc72651976a4a89f25211daa4b077794eec  gfx/flags/small/DFR_neutrality.tga
2288d4eab1721545f9aaf023a09e92127d3fe37c9aeadd30346e7704c5ba682f  gfx/flags/small/DFR_communism.tga
1a80a14bc7d40c3f8d33df0ba0e8bb57eee46723299234dcccaffa47b5f4ccf1  gfx/flags/small/DFR_fascism.tga
```

Visual validation:

- Contact sheet created at `docs/assets/006_independence_wave/flags/DFR_ideology_flags_contact.png`.
- Contact sheet includes 82x52 previews and enlarged 10x7 previews.
- The flags are upright in the review PNGs and all final TGA files report `TopLeft` orientation.

## Remaining Risks

- Fine emblem details are intentionally simplified at 10x7. The tiny files remain distinguishable by broad color layout, but small emblems should not be expected to read as precise symbols.
- Historical basis for ideological variants is alternate-history design work derived from the base Darfur style, not primary-source documented ideology flags.
- No blockers and no fallbacks or placeholders were used.
