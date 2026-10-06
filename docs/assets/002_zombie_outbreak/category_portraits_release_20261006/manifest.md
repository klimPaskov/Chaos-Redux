# Event002 weaponized-zombie category-picture package

Status: complete. All seven source portraits were parent-accepted. Infected and rabid were installed after their first crop review; the five remaining crop candidates were then reviewed and approved as a group and installed at the five stable runtime paths.

## Consumer and reference fit

The seven live category consumers are documented in docs/assets/002_zombie_outbreak/decision_category_pictures/manifest.md and use GFX_decision_cat_picture_weaponized_zombie_* in interface/visual_consistency_repair.gfx. This package changes only the seven named DDS textures and its evidence workspace; it does not edit GFX, decisions, portraits, or GUI files.

The exact reference family is .agents/skills/chaos-redux-event-assets/assets/gfx_references/icons/decision_categories/pictures/. I inspected its contact sheet and the 13 user-provided vanilla examples listed in CATALOG.md. The family canvas is 114x101. The active Event002 category-picture manifest specifies an opaque category consumer; the processed pictures therefore have alpha 255 at every pixel.

## Processing contract

Each completed picture is derived only from a parent-accepted fictional portrait PNG. No new portrait or category-picture identity was generated. The accepted portrait source is copied byte-for-byte into source_png/; its original portrait source file remains untouched. A scene-specific ImageOps.fit cover crop with Lanczos resampling is placed to keep the face and characteristic silhouette legible. The exact crop box, normalized vertical centering, source hash, processed PNG hash, DDS hash, and review state are stored per category in crop_json/ and notes/candidate_validation_infected_rabid.json.

## Requirement-to-runtime crosswalk

| Requirement | Accepted portrait source | Manual vertical center | Processed PNG | Final DDS | Sprite / category consumer | Status |
| --- | --- | ---: | --- | --- | --- | --- |
| ZZZ-CAT-INFECTED | portrait_ZZZ_weaponized_infected_v1.png | 0.06 | processed_png/decision_cat_picture_weaponized_zombie_infected.png | gfx/interface/decisions/visual_consistency_repair/pictures/decision_cat_picture_weaponized_zombie_infected.dds | GFX_decision_cat_picture_weaponized_zombie_infected / chaosx_weaponized_zombie_creator_infected_category | Complete, parent-approved and installed |
| ZZZ-CAT-RABID | portrait_ZZZ_weaponized_rabid_v2.png | 0.10 | processed_png/decision_cat_picture_weaponized_zombie_rabid.png | gfx/interface/decisions/visual_consistency_repair/pictures/decision_cat_picture_weaponized_zombie_rabid.dds | GFX_decision_cat_picture_weaponized_zombie_rabid / chaosx_weaponized_zombie_creator_rabid_category | Complete, parent-approved and installed |
| ZZZ-CAT-PARASITIC | portrait_ZZZ_weaponized_parasitic_v1.png | 0.06 | processed_png/decision_cat_picture_weaponized_zombie_parasitic.png | gfx/interface/decisions/visual_consistency_repair/pictures/decision_cat_picture_weaponized_zombie_parasitic.dds | GFX_decision_cat_picture_weaponized_zombie_parasitic / chaosx_weaponized_zombie_creator_parasitic_category | Parent-approved and installed |
| ZZZ-CAT-MUTANT | portrait_ZZZ_weaponized_mutant_v2.png | 0.05 | processed_png/decision_cat_picture_weaponized_zombie_mutant.png | gfx/interface/decisions/visual_consistency_repair/pictures/decision_cat_picture_weaponized_zombie_mutant.dds | GFX_decision_cat_picture_weaponized_zombie_mutant / chaosx_weaponized_zombie_creator_mutant_category | Parent-approved and installed |
| ZZZ-CAT-UNDEAD | portrait_ZZZ_weaponized_undead_v1.png | 0.09 | processed_png/decision_cat_picture_weaponized_zombie_undead.png | gfx/interface/decisions/visual_consistency_repair/pictures/decision_cat_picture_weaponized_zombie_undead.dds | GFX_decision_cat_picture_weaponized_zombie_undead / chaosx_weaponized_zombie_creator_undead_category | Parent-approved and installed |
| ZZZ-CAT-NECROTIC | portrait_ZZZ_weaponized_necrotic_v1.png | 0.02 | processed_png/decision_cat_picture_weaponized_zombie_necrotic.png | gfx/interface/decisions/visual_consistency_repair/pictures/decision_cat_picture_weaponized_zombie_necrotic.dds | GFX_decision_cat_picture_weaponized_zombie_necrotic / chaosx_weaponized_zombie_creator_necrotic_category | Parent-approved and installed |
| ZZZ-CAT-DEMONIC | portrait_ZZZ_weaponized_demonic_v1.png | 0.08 | processed_png/decision_cat_picture_weaponized_zombie_demonic.png | gfx/interface/decisions/visual_consistency_repair/pictures/decision_cat_picture_weaponized_zombie_demonic.dds | GFX_decision_cat_picture_weaponized_zombie_demonic / chaosx_weaponized_zombie_creator_demonic_category | Parent-approved and installed |

## Prior asset provenance

All seven prior runtime DDS files are archived byte-for-byte under previous_unverified/. The per-file hashes, sizes, decoded dimensions, and alpha ranges are in notes/previous_unverified_dds.json. These files remain explicitly unverified style assets; their archive does not establish authorship, licensing, or legal clearance.

All seven installed DDS files are uncompressed BGRA, 114x101, fully opaque, and decode pixel-exactly to their processed PNGs. Parent approved the complete native and 4x contact sheets on 2026-10-06. The candidate-review sheets remain at contact_sheets/category_picture_candidates_native.png and contact_sheets/category_picture_candidates_4x.png; final installed-state sheets are contact_sheets/category_picture_final_native.png and contact_sheets/category_picture_final_4x.png.

No in-game screenshot or live category consumer render was captured by this asset worker. Parent owns GFX integration review and live shared-window validation.
