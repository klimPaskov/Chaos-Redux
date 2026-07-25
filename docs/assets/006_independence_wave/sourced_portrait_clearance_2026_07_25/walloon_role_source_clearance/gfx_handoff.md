# GFX handoff: Wallonia sourced alternatives

This is a parent-wiring handoff only. No `.gfx` file was edited and no DDS was generated in this bounded source-clearance tranche.

## Recommended future sprite names

- `GFX_portrait_AFX_fernand_jacquet` for the commander candidate.
- `GFX_portrait_AFX_charles_de_broqueville` for the civic candidate.

## Source-locked crop paths

- Jacquet source crop: `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/walloon_role_source_clearance/source_crops/fernand_jacquet_1915_head_shoulders_crop.png`.
- de Broqueville source crop: `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/walloon_role_source_clearance/source_crops/charles_de_broqueville_commons_head_shoulders_crop.png`.

These PNGs are exact lossless archival crops, not final HOI4 dimensions. The parent may pass an accepted crop through the repository-standard portrait processor and DDS converter after legal and identity review. The resulting DDS path and texturefile must be recorded in the runtime handoff when that parent-owned step is authorized.

## Blocked comparison

Albert Devèze has a source-locked crop at `source_crops/albert_deveze_1929_head_shoulders_clean_crop.png`, but vanilla owns `BEL_albert_deveze`; do not wire it without an explicit additive-transfer decision.

## Visual caveats

Jacquet is the strongest commander fit and shows both ears and uniform details. De Broqueville is the strongest civic source-rights fit and shows both shoulders and a clear facial likeness, but the frontal pose partly occludes the left ear. If the runtime identity gate requires two fully visible ears, keep Jacquet and request a different civic source rather than reconstructing the missing feature.
