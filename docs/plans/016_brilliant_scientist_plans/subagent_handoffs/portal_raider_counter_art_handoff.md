# Portal Raider counter art handoff

Owner: `chaosx_icon_artist`.

Status: complete bespoke source, processed strips, DDS outputs, manifest, review evidence, and parent-reviewed `.gfx` registration; live consumer validation remains pending with the accepted 3D entity.

This package is generic shared API art for the `portal_raider` subunit and is not Kruger-named art.

## Final runtime outputs

- Large division strip: `gfx/interface/counters/divisions_large/unit_portal_raider_icon.dds`.
- On-map strip: `gfx/interface/counters/divisions_small/onmap_unit_portal_raider_icon.dds`.
- No gameplay, unit, entity, model, sound, localisation, or `.gfx` file was edited by this handoff.

## Source and processing evidence

- Native ImageGen source: `docs/assets/shared_portal_raider_system/models_3d/portal_raider/evidence/counter/source/portal_raider_imagegen_source_v3.png`.
- Official chroma-key result: `docs/assets/shared_portal_raider_system/models_3d/portal_raider/evidence/counter/source/portal_raider_imagegen_alpha_v3.png`.
- Prompt: `docs/assets/shared_portal_raider_system/models_3d/portal_raider/evidence/counter/source/prompt_v3.txt`.
- Source dimensions: `1254x1254` RGB.
- Source SHA-256: `7ced32688644143b46f7df64e13348d4f7c850efb9fa52da8bdbe9d45ca88f48`.
- Alpha-source SHA-256: `1973ac6370ed60b1114a8501c380cf105bd322eeccba19ac63b852503d586c5c`.
- The prompt keeps the subject charcoal/gray/bronze and reserves flat `#00ff00` for the removable background; no text, watermark, country, ideology, faction, provider, or named-character marking is present.
- Chroma-key removal used the official `C:/Users/klimp/.codex/skills/.system/imagegen/scripts/remove_chroma_key.py` helper with border auto-key, soft matte, despill, and retained alpha output.

## Vanilla reference gate

The canonical contact sheets were inspected before generation at:

- `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/counters_large/contact_sheet.png`.
- `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/map_counters/contact_sheet.png`.

The exact installed definitions are in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx`.

- `GFX_unit_infantry_icon_medium` uses `gfx/interface/counters/divisions_large/unit_infantry_icon.dds` with `noOfFrames = 2`.
- `GFX_unit_infantry_icon_medium_white` uses `gfx/interface/counters/divisions_small/onmap_unit_infantry_icon.dds` with `noOfFrames = 2`.
- Installed large DDS SHA-256: `b33a8e3b69cc789eb0e31ba99f4e5ba4e5b0a8b51ec1a7a7f709c3516f720c23`.
- Installed on-map DDS SHA-256: `58ab78662c2a64a519b8d5d144582e7b2785915bd0a0a822696d87a9de6f766c`.
- Large installed canvas is `152x42` with two `76x42` frames; on-map canvas is `60x12` with two `30x12` frames.
- Frame order is green custom symbol first and black/gray/white selected-state plate second.
- The sampled dominant vanilla green is RGB `(73,106,73)` with highlight anchors `(100,128,100)` and `(116,141,116)`.
- The package preserves transparent unused pixels, a black state-plate outline, a gray-white inset panel, and a dark neutral state silhouette.

## Processed strips and checksums

- Large processed strip: `docs/assets/shared_portal_raider_system/models_3d/portal_raider/evidence/counter/processed/portal_raider_large_strip.png`, `152x42` RGBA, SHA-256 `9965d34958d380d025f0a9d084cfa4896a6d0f6a43d91e9b9f664f65e5984fc7`.
- On-map processed strip: `docs/assets/shared_portal_raider_system/models_3d/portal_raider/evidence/counter/processed/portal_raider_map_strip.png`, `60x12` RGBA, SHA-256 `17562e3d7318c3a7d59a779336740a930a09f1e1e5c7646434ca30ef2f2cc7df`.
- Large frame bounds are `[19,4,56,38]` and `[13,9,64,38]` for the green and state frames respectively.
- On-map frame bounds are `[8,0,21,12]` and `[2,0,28,12]` for the green and state frames respectively.
- Per-frame exact PNG previews and nearest-neighbor review enlargements are under `docs/assets/shared_portal_raider_system/models_3d/portal_raider/evidence/counter/previews/`.

## DDS outputs and validation

- Large evidence DDS: `docs/assets/shared_portal_raider_system/models_3d/portal_raider/evidence/counter/dds/unit_portal_raider_icon.dds`.
- Large runtime DDS SHA-256: `4236df5183605af540d44339eed96f29b2b59a40d9f82e1472c5178963ef920e`.
- Large DDS format: `25664` bytes, `152x42`, legacy `124`-byte header, BGRA `32`-bit (`pf_flags=65`, `fourcc=0`, masks `0xff0000/0xff00/0xff/0xff000000`), one mip level.
- On-map evidence DDS: `docs/assets/shared_portal_raider_system/models_3d/portal_raider/evidence/counter/dds/onmap_unit_portal_raider_icon.dds`.
- On-map runtime DDS SHA-256: `fb009c5eeed40c1aad867d15c066422cb142aa24dc2c38d7311857bfa284d85e`.
- On-map DDS format: `3008` bytes, `60x12`, legacy `124`-byte header, BGRA `32`-bit (`pf_flags=65`, `fourcc=0`, masks `0xff0000/0xff00/0xff/0xff000000`), one mip level.
- Both DDS files were decoded from their native BGRA payloads and matched the processed PNG sheets pixel-for-pixel.
- Round-trip images are `previews/portal_raider_large_dds_roundtrip.png` and `previews/portal_raider_map_dds_roundtrip.png` under the evidence counter folder.

The machine-readable record is `docs/assets/shared_portal_raider_system/models_3d/portal_raider/evidence/counter/manifest.json`.

The visual comparison sheet is `docs/assets/shared_portal_raider_system/models_3d/portal_raider/evidence/counter/contact_sheet.png` and includes the generated source, alpha result, both processed sheets, decoded DDS previews, and the canonical installed infantry family at review scale.

## Parent-owned GFX registration

The parent registered the stable sprite names in `interface/portal_raider_system.gfx` after comparing the clone-system and installed vanilla naming precedents.

```text
spriteType = { name = "GFX_unit_portal_raider_icon_medium" textureFile = "gfx/interface/counters/divisions_large/unit_portal_raider_icon.dds" noOfFrames = 2 }
spriteType = { name = "GFX_unit_portal_raider_icon_medium_white" textureFile = "gfx/interface/counters/divisions_small/onmap_unit_portal_raider_icon.dds" noOfFrames = 2 }
```

Large consumer token: `unit_portal_raider_icon`.

On-map consumer token: `onmap_unit_portal_raider_icon`.

The generic `portal_raider` subunit token resolves through these exact group, medium, and on-map sprite IDs.

## Remaining risks and boundaries

- The rejected or incomplete Portal Raider 3D model handoff is separate from this counter package; do not claim entity or in-game model completion from these DDS files.
- Parent validation must verify that the accepted portal-raider entity/model and the two counter sprites load together, that the model is not a missing/rejected placeholder, and that the generic shared `portal_raider` identifier remains independent of Kruger route naming.
