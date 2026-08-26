# Event 012 strange-force bespoke counter production handoff

Date: 2026-08-06
Owner: chaosx_icon_artist subtask
Scope: counters only; no gameplay, GFX, localisation, entity, sound, or runtime files changed.

> This 2026-08-06 counter-production handoff records retained asset evidence, not eight completed model packages or current runtime promotion. The current per-package manifests and the 2026-08-26 model handoffs supersede its blanket acceptance and parent-receipt wording.

## Result

All eight requested unit folders retain original counter-art evidence. The package root is docs/assets/012_africa/models_3d/<slug>/counters/. Each package includes:

- source/<slug>_imagegen.png and source/prompt.txt
- processed/<slug>_alpha.png with approved chroma-key removal and no bright-green fringe
- reference/land_counters_large_contact_sheet.png, reference/unit_infantry_icon.png, reference/land_map_counters_contact_sheet.png, and reference/onmap_infantry.png
- previews/<slug>_large.png (152x42), previews/<slug>_map.png (60x12), smooth enlarged preview, decoded DDS round-trips, and contact_sheet.png
- dds/unit_<slug>_icon.dds and dds/onmap_unit_<slug>_icon.dds
- manifest.json with source/reference/preview/DDS hashes, dimensions, alpha extrema, frame footprints, complete legacy BGRA header evidence, and parent runtime paths
- manifest.md and gfx_handoff.md

| Unit | Large DDS | On-map DDS |
| --- | --- | --- |
| gorilla_heavy_infantry | docs/assets/012_africa/models_3d/gorilla_heavy_infantry/counters/dds/unit_gorilla_heavy_infantry_icon.dds | docs/assets/012_africa/models_3d/gorilla_heavy_infantry/counters/dds/onmap_unit_gorilla_heavy_infantry_icon.dds |
| pan_sappers | docs/assets/012_africa/models_3d/pan_sappers/counters/dds/unit_pan_sappers_icon.dds | docs/assets/012_africa/models_3d/pan_sappers/counters/dds/onmap_unit_pan_sappers_icon.dds |
| stone_cohorts | docs/assets/012_africa/models_3d/stone_cohorts/counters/dds/unit_stone_cohorts_icon.dds | docs/assets/012_africa/models_3d/stone_cohorts/counters/dds/onmap_unit_stone_cohorts_icon.dds |
| forest_giants | docs/assets/012_africa/models_3d/forest_giants/counters/dds/unit_forest_giants_icon.dds | docs/assets/012_africa/models_3d/forest_giants/counters/dds/onmap_unit_forest_giants_icon.dds |
| oracle_recon | docs/assets/012_africa/models_3d/oracle_recon/counters/dds/unit_oracle_recon_icon.dds | docs/assets/012_africa/models_3d/oracle_recon/counters/dds/onmap_unit_oracle_recon_icon.dds |
| riverborn | docs/assets/012_africa/models_3d/riverborn/counters/dds/unit_riverborn_icon.dds | docs/assets/012_africa/models_3d/riverborn/counters/dds/onmap_unit_riverborn_icon.dds |
| disaster_wardens | docs/assets/012_africa/models_3d/disaster_wardens/counters/dds/unit_disaster_wardens_icon.dds | docs/assets/012_africa/models_3d/disaster_wardens/counters/dds/onmap_unit_disaster_wardens_icon.dds |
| plague_carriers | docs/assets/012_africa/models_3d/plague_carriers/counters/dds/unit_plague_carriers_icon.dds | docs/assets/012_africa/models_3d/plague_carriers/counters/dds/onmap_unit_plague_carriers_icon.dds |

## Vanilla reference gate

The canonical skill-local root inspected before generation was C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units. Contact sheets were inspected first for land/counters_large and land/map_counters, followed by unit_infantry_icon.png and onmap_infantry.png.

The exact installed definition file inspected was C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx. The large precedent is GFX_unit_infantry_icon_medium -> gfx/interface/counters/divisions_large/unit_infantry_icon.dds, noOfFrames = 2. The on-map precedent is GFX_unit_infantry_icon_medium_white -> gfx/interface/counters/divisions_small/onmap_unit_infantry_icon.dds, noOfFrames = 2. Installed reference DDS SHA-256 values are recorded per-unit in counters/manifest.json.

## Palette and frame contract

Large frame 0 uses the sampled vanilla infantry green palette (dominant RGB 73,106,73; mapped range 20,34,21 through 154,175,147). Large frame 1 uses the inspected neutral plate treatment with each generated silhouette. Both on-map frames preserve the inspected neutral grayscale family and use the generated unit-specific silhouette. Frame order, per-frame canvas dimensions, alpha behavior, border, and visible bounds are recorded in each manifest.json.

## Validation

All 16 DDS outputs were decoded at native size and matched their target PNGs pixel-for-pixel. Each passed the complete legacy uncompressed BGRA header contract: DDS magic, 124-byte header, declared dimensions, 32-bit RGB|ALPHAPIXELS pixel format, zero fourCC, BGRA masks, DDSCAPS_TEXTURE, no mipmaps, and exact file length. Alpha extrema and frame bounds are recorded in every manifest. All 16 DDS hashes are unique; no copied or renamed vanilla counter was used.

Combined review sheet: docs/assets/012_africa/models_3d/counters_contact_sheet.png.
The 16 DDS files remain production evidence, and their presence or prior path audit does not establish family-wide promotion. Oracle Recon now has a parent-reviewed replacement counter staged at both runtime destinations with exact hashes recorded in its current manifest; live consumer validation remains open. Disaster Wardens uses the vanilla `infantry` model override and retains its counter as an optional bespoke presentation. Gorilla, Pan, Stone, Riverborn, Forest, and Plague remain blocked or unpromoted with their current model packages. `interface/012_africa_strange_force_counters.gfx` retains the stable Oracle rows, and the fail-closed package manifest prevents any all-eight readiness claim until every family is explicitly promoted. A runtime path audit finding zero missing counter textures is historical evidence, not an all-eight readiness receipt.
