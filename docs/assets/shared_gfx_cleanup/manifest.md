# Shared GFX Cleanup Asset Manifest

## Visual reference standard

All generated assets were reviewed against the restored examples under `.agents/skills/chaos-redux-event-assets/assets/` and the corresponding vanilla operation or division-template picker assets. Generated variants that were too ornate, too three-dimensional, or too busy were rejected before processing.

Generated source art uses the built-in OpenAI image-generation tool. Transparent icons were generated on a flat magenta key, processed through the official chroma-removal helper, trimmed, resized with Lanczos filtering, and exported as 32-bit RGBA DDS. Operation art and division symbols also reuse only the alpha/framing masks of their vanilla reference family so the new artwork fits the existing UI silhouette.

## Generated assets

| Asset | Source PNG | Processed PNG | Final DDS | Sprite | Size |
| --- | --- | --- | --- | --- | --- |
| Generic biological operation | `source/operations_plant_bioweapon.png` | `processed/operations_plant_bioweapon.png` | `gfx/interface/operations/chaosx_bioweapon/plant_bioweapon.dds` | `GFX_operations_plant_bioweapon` | 85x85 |
| Biological operation map icon | `source/operations_plant_bioweapon_map.png` | `processed/operations_plant_bioweapon_map.png` | `gfx/interface/operations/chaosx_bioweapon/map/plant_bioweapon_map.dds` | `GFX_operations_plant_bioweapon_map` | 48x48 |
| Reservoir phase | `source/bioweapon_plant_reservoir.png` | `processed/bioweapon_plant_reservoir.png` | `gfx/interface/operations/chaosx_bioweapon/phases/bioweapon_plant_reservoir.dds` | `GFX_phase_bioweapon_plant_reservoir` | 210x176 |
| Reservoir phase small | same generated source | `processed/bioweapon_plant_reservoir_small.png` | `gfx/interface/operations/chaosx_bioweapon/phases_small/bioweapon_plant_reservoir_small.dds` | `GFX_phase_bioweapon_plant_reservoir_small` | 59x58 |
| Medical-chain phase | `source/bioweapon_seed_medical_chain.png` | `processed/bioweapon_seed_medical_chain.png` | `gfx/interface/operations/chaosx_bioweapon/phases/bioweapon_seed_medical_chain.dds` | `GFX_phase_bioweapon_seed_medical_chain` | 210x176 |
| Medical-chain phase small | same generated source | `processed/bioweapon_seed_medical_chain_small.png` | `gfx/interface/operations/chaosx_bioweapon/phases_small/bioweapon_seed_medical_chain_small.dds` | `GFX_phase_bioweapon_seed_medical_chain_small` | 59x58 |
| Transport-hub phase | `source/bioweapon_contaminate_transport_hub.png` | `processed/bioweapon_contaminate_transport_hub.png` | `gfx/interface/operations/chaosx_bioweapon/phases/bioweapon_contaminate_transport_hub.dds` | `GFX_phase_bioweapon_contaminate_transport_hub` | 210x176 |
| Transport-hub phase small | same generated source | `processed/bioweapon_contaminate_transport_hub_small.png` | `gfx/interface/operations/chaosx_bioweapon/phases_small/bioweapon_contaminate_transport_hub_small.dds` | `GFX_phase_bioweapon_contaminate_transport_hub_small` | 59x58 |
| Smallpox vaccination | `source/decision_biowarfare_smallpox_vaccination.png` | `processed/decision_biowarfare_smallpox_vaccination.png` | `gfx/interface/decisions/biowarfare/decision_biowarfare_smallpox_vaccination.dds` | `GFX_decision_biowarfare_smallpox_vaccination` | 32x32 |
| Biological stockpile release | `source/decision_bio_unleash_stockpiled_pathogens.png` | `processed/decision_bio_unleash_stockpiled_pathogens.png` | `gfx/interface/decisions/biowarfare/decision_bio_unleash_stockpiled_pathogens.dds` | `GFX_decision_bio_unleash_stockpiled_pathogens` | 32x32 |
| Biological stockpile destruction | `source/decision_destroy_biological_stockpiles.png` | `processed/decision_destroy_biological_stockpiles.png` | `gfx/interface/decisions/biowarfare/decision_destroy_biological_stockpiles.dds` | `GFX_decision_destroy_biological_stockpiles` | 32x32 |
| Japan chemical campaign category | `source/decision_category_japan_chemical_campaign.png` | `processed/decision_category_japan_chemical_campaign.png` | `gfx/interface/decisions/japan_chemical_campaign/decision_category_japan_chemical_campaign.dds` | `GFX_decision_category_japan_chemical_campaign` | 52x40 |
| Biowarfare division symbol large | `source/division_template_biowarfare.png` | `processed/division_template_biowarfare.png` | `gfx/interface/counters/division_templates_large/custom_template_044.dds` | `GFX_div_templ_44_large` | 76x42 |
| Biowarfare division symbol small | same generated source | `processed/division_template_biowarfare_small.png` | `gfx/interface/counters/division_templates_small/custom_template_044.dds` | `GFX_div_templ_44_small` | 30x12 |
| Chemical-warfare division symbol large | `source/division_template_chemical_warfare.png` | `processed/division_template_chemical_warfare.png` | `gfx/interface/counters/division_templates_large/custom_template_045.dds` | `GFX_div_templ_45_large` | 76x42 |
| Chemical-warfare division symbol small | same generated source | `processed/division_template_chemical_warfare_small.png` | `gfx/interface/counters/division_templates_small/custom_template_045.dds` | `GFX_div_templ_45_small` | 30x12 |

## Reused and repaired assets

| Asset family | Source | Result |
| --- | --- | --- |
| Civilian-deaths map-mode buttons | Existing selected/deselected shared strip frame 18 | Dedicated selected and deselected `20x18` PNG/DDS assets under `source/map_modes/`, `processed/map_modes/`, and `gfx/interface/mapmode/custom/` |
| Contamination map-mode buttons | Existing selected/deselected shared strip frame 19 | Dedicated selected and deselected `20x18` PNG/DDS assets under the same folders |
| KHW flags | Existing real TGA triplets | Removed the one-column left/right seam at normal, medium, and small sizes; contact sheet at `processed/flags/khw_repaired_contact_sheet.png` |
| Legacy 24-bit custom flags | Existing real TGA triplets | Normalized 31 identities across three sizes to 32-bit bottom-origin TGA without changing filenames or artwork |

## Review artifacts

- `processed/contact_sheet.png`: generated shared icons at native-family scaling over checker backgrounds.
- `processed/flags/khw_repaired_contact_sheet.png`: repaired KHW flag triplets.
- `processed/map_modes/`: exact per-mode PNG previews.

