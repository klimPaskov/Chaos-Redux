# Chaos Redux Stage 6 Chemical Designers

Package root: `docs/assets/chaos_warfare_system/stage_6_chemical_designers/`

Runtime root: `gfx/interface/ideas/cbrn_designers/`

Both icons are independent `$imagegen` source renders for stable generic Stage 6 MIO designer IDs. They are separate idea/MIO icon assets, not resized or recolored variants of one another. The closest inspected vanilla 64x64 manufacturer precedent was `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/ideas/fra_sncaso.dds`: one-level uncompressed BGRA, 16,512 bytes, transparent unused canvas.

Chaos Redux reference assets inspected before generation: `.agents/skills/chaos-redux-event-assets/assets/ideas/idea_generic_coastal_defense_ships.png`, `idea_generic_constitutional_guarantee.png`, and `generic_wall_line.png`. The generated icons follow the compact aged HOI4 idea treatment while retaining real transparency.

## Asset: `cbrn_chemical_munitions_combine`

- Related Stage 6 MIO designer ID: `cbrn_chemical_munitions_combine`
- Asset type: idea/MIO manufacturer icon
- Intended use: generic chemical munitions combine designer emblem
- Source mode: `$imagegen`
- Source prompt record: `prompts/cbrn_chemical_munitions_combine.md`
- Source PNG: `source_png/cbrn_chemical_munitions_combine.png`
- Source PNG dimensions/format: 1254x1254, RGB PNG, 2,338,023 bytes
- Source PNG SHA-256: `9a1ea7d0539accf8896fc6c75a33d4548dbb9614fc0ea5adb9678ea566d251c6`
- Processed PNG: `processed_png/cbrn_chemical_munitions_combine.png`
- Processed PNG dimensions/format: 64x64, RGBA PNG, 9,617 bytes
- Processed PNG SHA-256: `99dc9e97cecb85042a18d40138231e28d46cd54bab6cefaf493a4198fe8360d4`
- Final archive DDS: `dds_archive/cbrn_chemical_munitions_combine.dds`
- Final runtime DDS: `gfx/interface/ideas/cbrn_designers/cbrn_chemical_munitions_combine.dds`
- Archive/runtime DDS SHA-256: `504a34fbb2f5359deb4f066fb4b6b5ba640815290d4ea4b7bde36ab86dae4edf`
- DDS dimensions/format: 64x64, legacy one-level uncompressed 32-bit BGRA/B8G8R8A8, 16,512 bytes
- Sprite name supplied by parent: `GFX_cbrn_chemical_munitions_combine`
- Sprite registration: `interface/cbrn_designers.gfx`
- Related localisation key: parent-owned; not changed in this asset-only task
- Transparency evidence: alpha min/max 0/255; 1,095 transparent pixels; 770 partially transparent pixels; 2,231 opaque pixels; no detected opaque magenta residue
- Visual identity: amber, oxidized steel, muted olive; capped chemical shell and shell-filling carousel, sealed reagent canister, and heavy factory gear; no text, national/company logo, skull, or modern biohazard symbol
- Status: `complete` / wired

## Asset: `cbrn_aerosol_air_delivery_bureau`

- Related Stage 6 MIO designer ID: `cbrn_aerosol_air_delivery_bureau`
- Asset type: idea/MIO manufacturer icon
- Intended use: generic aerosol air-delivery bureau designer emblem
- Source mode: `$imagegen`
- Source prompt record: `prompts/cbrn_aerosol_air_delivery_bureau.md`
- Source PNG: `source_png/cbrn_aerosol_air_delivery_bureau.png`
- Source PNG dimensions/format: 1254x1254, RGB PNG, 1,809,512 bytes
- Source PNG SHA-256: `9c00935304b6838fbb097d44f8ce144a2aefc71f23f70fa40556a5f9ea83e2d5`
- Processed PNG: `processed_png/cbrn_aerosol_air_delivery_bureau.png`
- Processed PNG dimensions/format: 64x64, RGBA PNG, 7,046 bytes
- Processed PNG SHA-256: `70d8f14935037aa155da83d36ad51678bac87e4d4ac417f46939591c47446d76`
- Final archive DDS: `dds_archive/cbrn_aerosol_air_delivery_bureau.dds`
- Final runtime DDS: `gfx/interface/ideas/cbrn_designers/cbrn_aerosol_air_delivery_bureau.dds`
- Archive/runtime DDS SHA-256: `9653875f1eef0ff6010c0ff078aa94e01afed7d01a1a518831f9886cb1db4732`
- DDS dimensions/format: 64x64, legacy one-level uncompressed 32-bit BGRA/B8G8R8A8, 16,512 bytes
- Sprite name supplied by parent: `GFX_cbrn_aerosol_air_delivery_bureau`
- Sprite registration: `interface/cbrn_designers.gfx`
- Related localisation key: parent-owned; not changed in this asset-only task
- Transparency evidence: alpha min/max 0/255; 2,234 transparent pixels; 805 partially transparent pixels; 1,057 opaque pixels; no detected opaque magenta residue
- Visual identity: slate blue, brass, muted silver; winged sealed dispersal rack, precision manifold/nozzle, and controlled aerosol fan; no text, national/company logo, skull, modern biohazard symbol, or reused bomb-lock silhouette
- Status: `complete` / wired

## Shared processing and validation

- Source preservation: generated PNGs copied unchanged from the independent built-in imagegen outputs into `source_png/`.
- Transparency processing: `remove_chroma_key.py --auto-key border --soft-matte --transparent-threshold 12 --opaque-threshold 220 --despill`, using the generated flat `#00ff00` key background.
- Final PNG processing: FFmpeg Lanczos resize to exact 64x64 RGBA PNG.
- DDS conversion: repository `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`, which used its standard FFmpeg BGRA fallback because `texconv` was unavailable.
- DDS header: `DDS ` magic; header size 124; flags 4111; width/height 64x64; pitch 256; pixel-format size 32; flags 65; fourCC 0; bits 32; masks `0x00FF0000/0x0000FF00/0x000000FF/0xFF000000`; texture caps `0x00001000`; no mipmaps; no caps2 flags.
- Payload: exact `128 + 64*64*4 = 16,512` bytes for both archive and runtime DDS files.
- Identity: each archive/runtime pair is byte-identical; the two final DDS SHA-256 hashes are distinct.
- Review contact sheet: `contact_sheets/stage_6_chemical_designers_checkerboard.png`
- Exact validation record: `notes/validation.md`
- Runtime sprite registration: `interface/cbrn_designers.gfx`
