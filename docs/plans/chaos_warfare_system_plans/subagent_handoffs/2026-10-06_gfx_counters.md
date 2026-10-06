# CBRN counter and texticon GFX handoff

Asset production and DDS conversion are complete for 31 counter and texticon outputs. Parent integration is recorded below; native live-game acceptance remains pending.

The adjacent JSON is the package manifest; durable strict conversion evidence is `2026-10-06_counter_dds_validation.json`, and the active source workspace is `docs/assets/chaos_warfare_system/2026-10-06_gfx_tech_counters/`.

The final package re-converted 30 existing output paths and added `gfx/texticons/support_equipment_text_icon.dds` as the thirty-first output.

All 31 DDS files pass exact header, format, size, alpha, and pixel-equality checks against their processed PNGs, and all 26 approved texticon frame-1 snapshots remain pixel-exact after DDS decode.

The large land and land map contact sheets under the canonical reference root and the installed vanilla counter evidence at `evidence/vanilla_counter_sample.json` informed the silhouettes, frames, palette, contrast, and transparent canvas treatment.

## Parent-owned texture path updates

The seven Livens projector aliases currently point to separate `unit_light_chemical_tank_support_[agent]` texture files; repoint them to the shared two-frame `gfx/texticons/unit_livens_projector_support_icon_small.dds` output.

- `GFX_unit_livens_projector_support_chlorine_icon_small`: `gfx/texticons/unit_light_chemical_tank_support_chlorine_icon_small.dds` → `gfx/texticons/unit_livens_projector_support_icon_small.dds`.
- `GFX_unit_livens_projector_support_phosgene_icon_small`: `gfx/texticons/unit_light_chemical_tank_support_phosgene_icon_small.dds` → `gfx/texticons/unit_livens_projector_support_icon_small.dds`.
- `GFX_unit_livens_projector_support_mustard_icon_small`: `gfx/texticons/unit_light_chemical_tank_support_mustard_icon_small.dds` → `gfx/texticons/unit_livens_projector_support_icon_small.dds`.
- `GFX_unit_livens_projector_support_lewisite_icon_small`: `gfx/texticons/unit_light_chemical_tank_support_lewisite_icon_small.dds` → `gfx/texticons/unit_livens_projector_support_icon_small.dds`.
- `GFX_unit_livens_projector_support_tabun_icon_small`: `gfx/texticons/unit_light_chemical_tank_support_tabun_icon_small.dds` → `gfx/texticons/unit_livens_projector_support_icon_small.dds`.
- `GFX_unit_livens_projector_support_sarin_icon_small`: `gfx/texticons/unit_light_chemical_tank_support_sarin_icon_small.dds` → `gfx/texticons/unit_livens_projector_support_icon_small.dds`.
- `GFX_unit_livens_projector_support_soman_icon_small`: `gfx/texticons/unit_light_chemical_tank_support_soman_icon_small.dds` → `gfx/texticons/unit_livens_projector_support_icon_small.dds`.

Repoint the CBRN armored-delivery category sprite to the new texture path: - `GFX_unit_category_cbrn_armored_delivery_support_icon_small`: `gfx/texticons/unit_category_chemical_tank_support_companies_icon_small.dds` → `gfx/texticons/unit_category_cbrn_armored_delivery_support_icon_small.dds`.

Add `noOfFrames = 2` to `GFX_support_equipment_text_icon`, which consumes `gfx/texticons/support_equipment_text_icon.dds` as two adjacent 30x12 frames in a 60x12 strip.

Keep the eight old texture paths in place until the parent has updated all references and confirmed each path is unreferenced.

## Converted runtime outputs

- `unit_cbrn_gas_mask_decon_detachment_icon_small` uses `gfx/texticons/unit_cbrn_gas_mask_decon_detachment_icon_small.dds` at `60x12` with 2 frame(s); the processed PNG and final DDS hashes are in `2026-10-06_gfx_counters.json`.
- `unit_cbrn_chemical_recon_detachment_icon_small` uses `gfx/texticons/unit_cbrn_chemical_recon_detachment_icon_small.dds` at `60x12` with 2 frame(s); the processed PNG and final DDS hashes are in `2026-10-06_gfx_counters.json`.
- `unit_cbrn_chemical_projector_battery_icon_small` uses `gfx/texticons/unit_cbrn_chemical_projector_battery_icon_small.dds` at `60x12` with 2 frame(s); the processed PNG and final DDS hashes are in `2026-10-06_gfx_counters.json`.
- `unit_cbrn_chemical_ammunition_train_icon_small` uses `gfx/texticons/unit_cbrn_chemical_ammunition_train_icon_small.dds` at `60x12` with 2 frame(s); the processed PNG and final DDS hashes are in `2026-10-06_gfx_counters.json`.
- `unit_cbrn_light_armored_delivery_detachment_icon_small` uses `gfx/texticons/unit_cbrn_light_armored_delivery_detachment_icon_small.dds` at `60x12` with 2 frame(s); the processed PNG and final DDS hashes are in `2026-10-06_gfx_counters.json`.
- `unit_cbrn_medium_armored_delivery_detachment_icon_small` uses `gfx/texticons/unit_cbrn_medium_armored_delivery_detachment_icon_small.dds` at `60x12` with 2 frame(s); the processed PNG and final DDS hashes are in `2026-10-06_gfx_counters.json`.
- `unit_cbrn_heavy_armored_delivery_detachment_icon_small` uses `gfx/texticons/unit_cbrn_heavy_armored_delivery_detachment_icon_small.dds` at `60x12` with 2 frame(s); the processed PNG and final DDS hashes are in `2026-10-06_gfx_counters.json`.
- `unit_cbrn_medical_countermeasure_detachment_icon_small` uses `gfx/texticons/unit_cbrn_medical_countermeasure_detachment_icon_small.dds` at `60x12` with 2 frame(s); the processed PNG and final DDS hashes are in `2026-10-06_gfx_counters.json`.
- `unit_cbrn_biosecurity_assault_detachment_icon_small` uses `gfx/texticons/unit_cbrn_biosecurity_assault_detachment_icon_small.dds` at `60x12` with 2 frame(s); the processed PNG and final DDS hashes are in `2026-10-06_gfx_counters.json`.
- `unit_cbrn_hq_operations_section_icon_small` uses `gfx/texticons/unit_cbrn_hq_operations_section_icon_small.dds` at `60x12` with 2 frame(s); the processed PNG and final DDS hashes are in `2026-10-06_gfx_counters.json`.
- `unit_cbrn_hq_protective_logistics_section_icon_small` uses `gfx/texticons/unit_cbrn_hq_protective_logistics_section_icon_small.dds` at `60x12` with 2 frame(s); the processed PNG and final DDS hashes are in `2026-10-06_gfx_counters.json`.
- `unit_cbrn_hq_medical_countermeasure_directorate_icon_small` uses `gfx/texticons/unit_cbrn_hq_medical_countermeasure_directorate_icon_small.dds` at `60x12` with 2 frame(s); the processed PNG and final DDS hashes are in `2026-10-06_gfx_counters.json`.
- `unit_category_cbrn_regimental_support_icon_small` uses `gfx/texticons/unit_category_cbrn_regimental_support_icon_small.dds` at `60x12` with 2 frame(s); the processed PNG and final DDS hashes are in `2026-10-06_gfx_counters.json`.
- `unit_category_cbrn_primary_protection_icon_small` uses `gfx/texticons/unit_category_cbrn_primary_protection_icon_small.dds` at `60x12` with 2 frame(s); the processed PNG and final DDS hashes are in `2026-10-06_gfx_counters.json`.
- `unit_category_cbrn_reconnaissance_icon_small` uses `gfx/texticons/unit_category_cbrn_reconnaissance_icon_small.dds` at `60x12` with 2 frame(s); the processed PNG and final DDS hashes are in `2026-10-06_gfx_counters.json`.
- `unit_category_cbrn_engineer_support_icon_small` uses `gfx/texticons/unit_category_cbrn_engineer_support_icon_small.dds` at `60x12` with 2 frame(s); the processed PNG and final DDS hashes are in `2026-10-06_gfx_counters.json`.
- `unit_category_cbrn_offensive_delivery_icon_small` uses `gfx/texticons/unit_category_cbrn_offensive_delivery_icon_small.dds` at `60x12` with 2 frame(s); the processed PNG and final DDS hashes are in `2026-10-06_gfx_counters.json`.
- `unit_category_cbrn_artillery_logistics_icon_small` uses `gfx/texticons/unit_category_cbrn_artillery_logistics_icon_small.dds` at `60x12` with 2 frame(s); the processed PNG and final DDS hashes are in `2026-10-06_gfx_counters.json`.
- `unit_category_cbrn_occupation_support_icon_small` uses `gfx/texticons/unit_category_cbrn_occupation_support_icon_small.dds` at `60x12` with 2 frame(s); the processed PNG and final DDS hashes are in `2026-10-06_gfx_counters.json`.
- `unit_category_cbrn_biosecurity_support_icon_small` uses `gfx/texticons/unit_category_cbrn_biosecurity_support_icon_small.dds` at `60x12` with 2 frame(s); the processed PNG and final DDS hashes are in `2026-10-06_gfx_counters.json`.
- `unit_category_cbrn_medical_support_icon_small` uses `gfx/texticons/unit_category_cbrn_medical_support_icon_small.dds` at `60x12` with 2 frame(s); the processed PNG and final DDS hashes are in `2026-10-06_gfx_counters.json`.
- `unit_category_cbrn_assault_battalions_icon_small` uses `gfx/texticons/unit_category_cbrn_assault_battalions_icon_small.dds` at `60x12` with 2 frame(s); the processed PNG and final DDS hashes are in `2026-10-06_gfx_counters.json`.
- `unit_category_cbrn_hq_icon_small` uses `gfx/texticons/unit_category_cbrn_hq_icon_small.dds` at `60x12` with 2 frame(s); the processed PNG and final DDS hashes are in `2026-10-06_gfx_counters.json`.
- `unit_livens_projector_support_icon_small` uses `gfx/texticons/unit_livens_projector_support_icon_small.dds` at `60x12` with 2 frame(s); the processed PNG and final DDS hashes are in `2026-10-06_gfx_counters.json`.
- `unit_category_cbrn_armored_delivery_support_icon_small` uses `gfx/texticons/unit_category_cbrn_armored_delivery_support_icon_small.dds` at `60x12` with 2 frame(s); the processed PNG and final DDS hashes are in `2026-10-06_gfx_counters.json`.
- `unit_chaos_battalion_icon_small` uses `gfx/texticons/unit_chaos_battalion_icon_small.dds` at `60x12` with 2 frame(s); the processed PNG and final DDS hashes are in `2026-10-06_gfx_counters.json`.
- `support_equipment_text_icon` uses `gfx/texticons/support_equipment_text_icon.dds` at `60x12` with 2 frame(s); the processed PNG and final DDS hashes are in `2026-10-06_gfx_counters.json`.
- `unit_category_chemical_support_companies_icon_small` uses `gfx/texticons/unit_category_chemical_support_companies_icon_small.dds` at `60x12` with 2 frame(s); the processed PNG and final DDS hashes are in `2026-10-06_gfx_counters.json`.
- `unit_cbrn_chemical_recon_detachment_large` uses `gfx/interface/counters/divisions_large/unit_cbrn_chemical_recon_detachment_icon.dds` at `152x42` with 2 frame(s); the processed PNG and final DDS hashes are in `2026-10-06_gfx_counters.json`.
- `onmap_unit_cbrn_chemical_recon_detachment_icon` uses `gfx/interface/counters/divisions_small/onmap_unit_cbrn_chemical_recon_detachment_icon.dds` at `60x12` with 2 frame(s); the processed PNG and final DDS hashes are in `2026-10-06_gfx_counters.json`.
- `cbrn_instruments_texticon` uses `gfx/texticons/cbrn_instruments_texticon.dds` at `20x20` with 1 frame(s); the processed PNG and final DDS hashes are in `2026-10-06_gfx_counters.json`.

The support-equipment full-strip contact sheet and the skull, gauge, and six-glyph review sheets are in the `evidence/` folder, and parent visual approval is recorded in the manifest.

## Source lineage and alpha

The eight newly generated final glyph sources have saved built-in ImageGen edit prompts, native source PNGs, source hashes, transparent-corner checks, and prompt hashes in `evidence/imagegen_edit_sources_native_alpha_review.json`.

The older opaque decontamination source and the older checkerboard-backed crossed-infantry X source remain preserved with their original hashes; the selected final decon art and X use validated native-alpha ImageGen edits.

The historical X fallback record is `evidence/chaos_battalion_crossed_box_glyph_processing_pre_prompt_edits.json`; the final X source is native-alpha, so no background removal was used on the final source.

The skull v4 edit remains preserved as a rejected scale candidate because its eye and nose openings collapsed at the 12x8 fit; the approved skull v5 uses large source-derived negative openings and the generated X underlay.

The seven earlier hand-authored frame-2 glyph drafts remain preserved in `source/` and are not used by any final runtime PNG or DDS.

## Validation boundary

The asset worker did not modify shared `.gfx` files. The parent-owned path and frame-count application is recorded below.

The parent reviewed the output and wiring as recorded below. The package does not claim in-game completion or user live-game validation.

## Parent integration and acceptance

Disposition: implemented and parent accepted under the October 6 graphics-repair task.
The parent reviewed the final native/four-times DDS sheets and the focused skull, gauge and generated-glyph sheets.
Eight exact paths are repointed in the shared texticon registry, and the support-equipment sprite declares two frames.
The eight superseded shared tank/category textures are retired only after the post-repoint engine-source search returns no references; their hashes and replacements are in the adjacent retirement JSON.
The twenty-six accepted first frames remain exact, and all thirty-one decoded textures match their processed PNGs.
Eight final generated sources retain exact pre-call requests and hashes after the host-restart recovery; rejected hand-drawn, missing-request and scale candidates remain source evidence.
Native engine presentation remains user-owned acceptance, with no gameplay or AI change in this package.
