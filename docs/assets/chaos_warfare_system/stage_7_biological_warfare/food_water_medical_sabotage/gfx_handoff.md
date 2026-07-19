# GFX Handoff: Stage 7 Food/Water/Medical-Chain Sabotage

## Wiring boundary

The four final DDS assets were delivered to the main agent. The parent supplied
the exact sprite ids and texture paths; they must not be renamed. The asset
subagent did not edit `.gfx`, `.gui`, localisation, or gameplay files.

Copy the following sprite definitions into the appropriate existing
`spriteTypes` block, preserving the repository's local formatting:

```text
spriteType = {
	name = "GFX_decision_bio_sabotage_anthrax"
	texturefile = "gfx/interface/decisions/biowarfare/decision_bio_sabotage_anthrax.dds"
}

spriteType = {
	name = "GFX_decision_bio_sabotage_plague"
	texturefile = "gfx/interface/decisions/biowarfare/decision_bio_sabotage_plague.dds"
}

spriteType = {
	name = "GFX_decision_bio_sabotage_tularemia"
	texturefile = "gfx/interface/decisions/biowarfare/decision_bio_sabotage_tularemia.dds"
}

spriteType = {
	name = "GFX_decision_bio_sabotage_smallpox"
	texturefile = "gfx/interface/decisions/biowarfare/decision_bio_sabotage_smallpox.dds"
}
```

At asset-production handoff, no localisation key or individual decision id was
supplied. Main-agent integration subsequently wired the sprites only to the
separate covert food/water/medical-chain sabotage decisions from Spec 06, never
to battlefield dissemination.

## Changed files

### Source and review package

- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/food_water_medical_sabotage/source/decision_bio_sabotage_anthrax_imagegen.png` — SHA-256 `4498f2bf965f6002708bb42815e94e1d5a80ba079dbf0c5b1e7ea8441e8dd5ef`, 1254×1254 RGB
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/food_water_medical_sabotage/source/decision_bio_sabotage_plague_imagegen.png` — SHA-256 `6e818996b9aae079f8640049cb05ddaab76827c070a523be2367a1ce35e4b143`, 1254×1254 RGB
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/food_water_medical_sabotage/source/decision_bio_sabotage_tularemia_imagegen.png` — SHA-256 `2ab82f3fb96846b6ce10c4f7b80c2f8a690e6603abb2fa77c2c225856532302e`, 1254×1254 RGB
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/food_water_medical_sabotage/source/decision_bio_sabotage_smallpox_imagegen.png` — SHA-256 `749126e5c0abf3cbfa01750fde09273a5d0285895d630fbc2e1250458b32a165`, 1254×1254 RGB
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/food_water_medical_sabotage/processed/decision_bio_sabotage_anthrax.png` — SHA-256 `02d85c536e2f8e049ccd7fc3d0b9e2757040519ee6a1a31d630a82025bf6afda`, 32×32 RGBA
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/food_water_medical_sabotage/processed/decision_bio_sabotage_plague.png` — SHA-256 `1fa627c00008306f3945771cf8eacfb3036480949df9a048b6a3a1c5f8b3ec5f`, 32×32 RGBA
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/food_water_medical_sabotage/processed/decision_bio_sabotage_tularemia.png` — SHA-256 `16fb4afd1df0c8f90f1b85af9d8450cac5076d121e20ca461a9c3f8c30222855`, 32×32 RGBA
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/food_water_medical_sabotage/processed/decision_bio_sabotage_smallpox.png` — SHA-256 `b75fbda0f2cc324159228d66ac506170f569968e5b76b2b29fe7e867cfb3fd61`, 32×32 RGBA
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/food_water_medical_sabotage/contact_sheet.png` — SHA-256 `30523168d18d64dafd9dd090a13e33a6f7a9f7621ef457cc14c0b78046827b7f`, 760×600 review sheet
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/food_water_medical_sabotage/manifest.md`
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/food_water_medical_sabotage/prompt_ledger.md`
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/food_water_medical_sabotage/gfx_handoff.md`

The retained 1254×1254 alpha intermediates are listed with hashes in
`manifest.md` and are part of the same authorized package folder.

### Final DDS outputs

| Sprite | Final DDS | Dimensions | Bytes | SHA-256 |
|---|---|---:|---:|---|
| `GFX_decision_bio_sabotage_anthrax` | `gfx/interface/decisions/biowarfare/decision_bio_sabotage_anthrax.dds` | 32×32 | 4224 | `694b1aafb23db0ed56da760e0dc606c3a948a3bda367c208659b148e56a061e1` |
| `GFX_decision_bio_sabotage_plague` | `gfx/interface/decisions/biowarfare/decision_bio_sabotage_plague.dds` | 32×32 | 4224 | `512092522e8e402d63c5cf7712d26cba5e60ade8552e6d38eeb15c3b3c332f7f` |
| `GFX_decision_bio_sabotage_tularemia` | `gfx/interface/decisions/biowarfare/decision_bio_sabotage_tularemia.dds` | 32×32 | 4224 | `7c1fdecedd679231225c0f68dc2d44508adc5264ea498e67fe11e5cf378d0ca0` |
| `GFX_decision_bio_sabotage_smallpox` | `gfx/interface/decisions/biowarfare/decision_bio_sabotage_smallpox.dds` | 32×32 | 4224 | `58a72fd3cac0caf013d5580857a0f7655923e6b9e5c2b65975ce5f90ea705659` |

## Meaningful validation

- All four processed PNGs and DDS outputs are exactly 32×32.
- All DDS files have a 128-byte legacy header, `DDS ` magic, header size 124,
  32-bit RGB+alpha pixel format flags 65, zero fourCC, BGRA masks
  `0x00FF0000 / 0x0000FF00 / 0x000000FF / 0xFF000000`, texture caps `0x1000`,
  and zero mipmaps.
- Every DDS is exactly `128 + (32×32×4) = 4224` bytes.
- Decoding DDS BGRA pixels back to RGBA matched the corresponding processed
  PNG byte-for-byte for all four assets.
- Every processed icon has alpha range 0–255 and transparent corners.
- All four final DDS hashes are distinct.
- Native 32×32 visual review and the enlarged checkerboard contact sheet show
  four readable, distinct silhouettes with no embedded text.
- No files outside the authorized asset package, the four exact DDS outputs,
  and this handoff were intentionally changed.

## Main-agent integration result

- All four exact ids and texture paths are registered in
  `interface/biological_warfare.gfx`.
- The four player-facing sabotage actions and twelve doctrine-timing variants
  use the corresponding sprites and final English localisation.
- The tularemia source's generic painted medical cross remains part of its
  original generated medical-crate still life. Native-size and contact-sheet
  review found no embedded text, placeholder, or cross-surface substitute.
