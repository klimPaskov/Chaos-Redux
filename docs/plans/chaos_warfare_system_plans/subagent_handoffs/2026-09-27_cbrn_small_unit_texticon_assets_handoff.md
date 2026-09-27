# CBRN Small Unit Texticon Asset Handoff

Disposition: implemented for all twenty-three current CBRN unit and unit-category small texticons. The parent visually approved all three source contact sheets at original resolution, wired all paths, and source-verified the complete 23-sprite crosswalk.

## Acceptance basis and scope

The parent directed a CBRN small-texticon production pass under the user-approved overhaul, first prioritizing Protection Company, Field Medical Company, and the three consolidated HQ functions. After reviewing Batch 1, the parent authorized the other seven current unit sprites and eleven surviving category sprites. The accepted overhaul in `docs/specs/chaos_warfare_system_specs/specs/13_2026_09_20_accepted_cbrn_overhaul.md` names one Protection Company, one Field Medical Company, and three consolidated HQ functions.

This asset worker owns source art, processed PNGs, DDS files, native-size contact sheets, asset manifests, and GFX handoffs. The parent owns all `.gfx` edits and final integration; the user performs live-game visual validation.

## Completed files and identifiers

The twelve unit-icon runtime files are `gfx/texticons/unit_cbrn_gas_mask_decon_detachment_icon_small.dds`, `gfx/texticons/unit_cbrn_medical_countermeasure_detachment_icon_small.dds`, `gfx/texticons/unit_cbrn_hq_operations_section_icon_small.dds`, `gfx/texticons/unit_cbrn_hq_protective_logistics_section_icon_small.dds`, `gfx/texticons/unit_cbrn_hq_medical_countermeasure_directorate_icon_small.dds`, `gfx/texticons/unit_cbrn_chemical_recon_detachment_icon_small.dds`, `gfx/texticons/unit_cbrn_chemical_projector_battery_icon_small.dds`, `gfx/texticons/unit_cbrn_chemical_ammunition_train_icon_small.dds`, `gfx/texticons/unit_cbrn_light_armored_delivery_detachment_icon_small.dds`, `gfx/texticons/unit_cbrn_medium_armored_delivery_detachment_icon_small.dds`, `gfx/texticons/unit_cbrn_heavy_armored_delivery_detachment_icon_small.dds`, and `gfx/texticons/unit_cbrn_biosecurity_assault_detachment_icon_small.dds`.

The eleven category-icon runtime files and all exact sprite identifiers are listed in the durable crosswalk `docs/systems/cbrn_warfare/cbrn_unit_texticon_assets.md`. All existing `GFX_` identifiers remain unchanged. The parent wired and source-verified all twelve unit-icon DDS paths, passed all eleven category roles and frame boundaries, wired the category paths, and source-verified all 23 unique sprite-to-DDS mappings.

## Source, reference, and validation evidence

The compact tracked source/runtime crosswalk, per-file source hashes, DDS hashes, and parent review status are in `docs/systems/cbrn_warfare/cbrn_unit_texticon_assets.md`. The bulky native sources, exact prompts, processed previews, round-trip PNGs, frame bounds, processing JSON, DDS audit JSON, and contact sheets remain in the ignored local staging package `docs/assets/chaos_warfare_cbrn/unit_texticon_replacements/`.

The exact vanilla consumer examples are installed `interface/texticons.gfx` and the `60x12`, two-frame support, HQ, and category DDS textures under `gfx/texticons/`. The canonical visual family is `.agents/skills/chaos-redux-event-assets/assets/gfx_references/units/land/map_counters/`; its contact sheet was inspected before the individual `onmap_infantry.png` and `onmap_artillery.png` references. Generated art requested native transparency in every initial ImageGen source; no background-removal fallback or component layer was used.

All twenty-three DDS files are `60x12`, one-level uncompressed BGRA, `3,008` bytes, with alpha `0–255`. Each DDS decoded pixel-for-pixel to its processed PNG. The parent independently source-verified the 23 unique sprite-to-DDS mappings. These checks establish texture integrity; they do not establish live-game rendering.

## Remaining work and blockers

No asset production or parent wiring remains. The parent completed the 23-sprite source crosswalk. The user retains live-game visual validation. No `.gfx` edits, in-game tests, or Git commit were made by this asset worker.
