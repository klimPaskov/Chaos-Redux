# CBRN icon finish and visual QA handoff

Status: complete for the owned icon, mapmode, MIO badge, trait, doctrine, and Event016 raid surfaces. Parent integration review remains the final gate. No gameplay, cost, effect, AI, GUI layout, or zombie 3D/sound file was edited.

## Runtime changes

| Surface | Stable sprite or alias | Runtime path | Result |
| --- | --- | --- | --- |
| Event016 Engineered Black Plague native raid | `GFX_raid_type_icon_brilliant_scientist_black_plague` | `gfx/interface/military_raids/map_icons/raid_type_icon_brilliant_scientist_black_plague.dds` | New original 32x32 alpha-backed biological raid pictogram; `interface/016_brilliant_scientist_biological_raids.gfx` now resolves to this path. |
| Famine mapmode selected | `GFX_mapmode_buttons_selected_small_famine_state_map_mode` | `gfx/interface/mapmode/custom/famine_state_map_mode_selected.dds` | 20x18 selected tile now carries the same native border contract as neighboring custom mapmodes. |
| Migration mapmode selected | `GFX_mapmode_buttons_selected_small_migration_state_map_mode` | `gfx/interface/mapmode/custom/migration_state_map_mode_selected.dds` | 20x18 selected tile now carries the same native border contract as neighboring custom mapmodes. |
| Famine and migration deselected | existing exact sprite names | existing `..._deselected.dds` paths | Preserved glyph-only deselected contract and verified against the native family. |
| CBRN MIO gas-mask upgrades | `GFX_military_industrial_organization_gas_mask_equipment_3`, `..._4` | aliases to `gfx/interface/military_industrial_organization/cbrn_badges/gas_mask_equipment.dds` | Added missing exact aliases; all 23 CBRN MIO equipment ids now have a sprite registration. |

## Contrast revision requested by parent review

The four doctrine sprites called out for low contrast were edited with native ImageGen against their preserved transparent source PNGs. The contaminant fire support cannon now has a readable charcoal body and crisp orange muzzle accent, hazard assault formations has distinct soldier, rifle, and shield edges around the orange chevron, integrated CBRN command has readable gunmetal console and mount edges around the orange command tree, and toxic armored warfare has a visible charcoal tank, tracks, and wheels beneath the orange exhaust flame.

| Doctrine | Runtime DDS | Size and visible bounds | Source and processing evidence |
| --- | --- | --- | --- |
| `doctrine_contaminant_fire_support` | `gfx/interface/doctrines/icons/chaos_warfare_doctrine_style/doctrine_contaminant_fire_support.dds` | 64x64; 5,13 to 59,48 | `source_png/doctrine/doctrine_contaminant_fire_support_source.png`, `processed_png/doctrine_contaminant_fire_support.png`, prompt under `prompts/doctrine_contaminant_fire_support_contrast_revision_20260920.md` |
| `doctrine_hazard_assault_formations` | `gfx/interface/doctrines/icons/chaos_warfare_doctrine_style/doctrine_hazard_assault_formations.dds` | 64x64; 7,6 to 57,58 | `source_png/doctrine/doctrine_hazard_assault_formations_source.png`, `processed_png/doctrine_hazard_assault_formations.png`, prompt under `prompts/doctrine_hazard_assault_formations_contrast_revision_20260920.md` |
| `doctrine_integrated_cbrn_command` | `gfx/interface/doctrines/icons/chaos_warfare_doctrine_style/doctrine_integrated_cbrn_command.dds` | 64x64; 12,5 to 53,57 | `source_png/doctrine/doctrine_integrated_cbrn_command_source.png`, `processed_png/doctrine_integrated_cbrn_command.png`, prompt under `prompts/doctrine_integrated_cbrn_command_contrast_revision_20260920.md` |
| `doctrine_toxic_armored_warfare` | `gfx/interface/doctrines/icons/chaos_warfare_doctrine_style/doctrine_toxic_armored_warfare.dds` | 64x64; 7,19 to 59,49 | `source_png/doctrine/doctrine_toxic_armored_warfare_source.png`, `processed_png/doctrine_toxic_armored_warfare.png`, prompt under `prompts/doctrine_toxic_armored_warfare_contrast_revision_20260920.md` |

The pre-contrast source files remain beside the edited sources as `*_source_precontrast_20260920.png`, so the original generated inputs are preserved. All four edited sources retain native RGBA alpha range 0-255 with no opaque matte canvas.

The famine and migration mapmode selected glyphs received a restrained gold brightness and edge contrast lift inside their glyph area, and the deselected pair received the corresponding gray lift. The outer selected frame pixels were preserved exactly, selected and deselected runtime DDS remain 20x18, and DDS decode matches each processed PNG byte-for-byte.

## Final doctrine enlargement revision requested by parent review

The contaminant fire support and integrated CBRN command sprites received a second native ImageGen edit because their primary silhouettes still occupied too little of the 64x64 canvas. The artillery now fills visible bounds 2,11 to 62,50 with orange edge definition across the barrel, carriage, wheel rim, and muzzle assembly. The command headquarters now fills visible bounds 7,1 to 57,63 with orange highlights across the console frame, antenna base, supports, lower mount, and command-map connections. Both remain transparent RGBA sources with the same dark outlines and stable GFX names; the accepted hazard, toxic armor, main doctrine, and all mapmode assets were not changed in this revision.

The corresponding prompts and preserved pre-enlargement inputs are recorded at `docs/assets/chaos_warfare_cbrn/icon_package/prompts/doctrine_contaminant_fire_support_enlarge_revision_20260920.md`, `docs/assets/chaos_warfare_cbrn/icon_package/prompts/doctrine_integrated_cbrn_command_enlarge_revision_20260920.md`, `source_png/doctrine/doctrine_contaminant_fire_support_source_pre_enlarge_20260920.png`, and `source_png/doctrine/doctrine_integrated_cbrn_command_source_pre_enlarge_20260920.png`.

## Existing family QA

The current doctrine icons remain compact black/orange symbolic silhouettes rather than gray/photo art. The CBRN decision/category set is sepia/charcoal pictogram art at its native family scale. The five CBRN commander badges decode at 23x33 with transparent edges and distinct silhouettes. The 13 CBRN MIO badges decode at 48x48 with transparent edges and distinct equipment subjects. Eight special-project DDS files, six CBRN industrial-concern icons, and eight CBRN organization marks were checked and retained. The supplied zombie category, zombie bomb alias, CXT portrait, and SWE idea were inspected as neighbors and left untouched.

## Evidence

- Package manifest: `docs/assets/chaos_warfare_cbrn/icon_package/manifest.md`
- Doctrine contact sheet: `docs/assets/chaos_warfare_cbrn/icon_package/contact_sheets/doctrine_processed.png`
- Doctrine native-size review: `docs/assets/chaos_warfare_cbrn/icon_package/contact_sheets/doctrine_native_64_review.png`
- Decisions and category contact sheet: `docs/assets/chaos_warfare_cbrn/icon_package/contact_sheets/decisions_categories_processed.png`
- Mapmode contact sheet: `docs/assets/chaos_warfare_cbrn/icon_package/contact_sheets/mapmode_processed.png`
- Focused selected/unselected mapmode review: `docs/assets/chaos_warfare_cbrn/icon_package/contact_sheets/mapmode_selected_zoom.png`
- Trait contact sheet: `docs/assets/chaos_warfare_cbrn/icon_package/contact_sheets/traits_processed.png`
- MIO badge contact sheet: `docs/assets/chaos_warfare_cbrn/icon_package/contact_sheets/mio_badges_processed.png`
- Raid-family comparison: `docs/assets/chaos_warfare_cbrn/icon_package/contact_sheets/raid_type_icons.png`
- New raid source: `docs/assets/chaos_warfare_cbrn/icon_package/source_png/raids/raid_type_icon_brilliant_scientist_black_plague_source.png`
- New raid prompt and provenance: `docs/assets/chaos_warfare_cbrn/icon_package/prompts/raid_type_icon_brilliant_scientist_black_plague_prompt.md`
- New raid processed PNG and DDS round-trip: `docs/assets/chaos_warfare_cbrn/icon_package/processed_png/raid_type_icon_brilliant_scientist_black_plague.png` and `docs/assets/chaos_warfare_cbrn/icon_package/dds_roundtrip/raid_type_icon_brilliant_scientist_black_plague.dds`

The new raid DDS and all four updated mapmode DDS files were generated with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`. DDS round-trip pixels equal their processed PNG inputs; headers are uncompressed BGRA, one level, and dimensions are exact. The new raid source has native alpha range 0-255 and no matte background. The new raid runtime decode is 32x32 with visible bounds 7,3 to 25,29. The mapmode runtime decodes are 20x18 with alpha range 0-255; selected variants fill the tile with the standard selected frame, while deselected variants retain visible bounds 2,3 to 17,16.

The four revised doctrine DDS files were regenerated with the same converter and decode exactly to their 64x64 processed PNGs with alpha range 0-255. The revised doctrine contact sheets show all four black/orange subjects legible at native icon size. The selected famine and migration gold glyphs increased from interior means of approximately 118,98,68 to 173,145,100 RGB while their selected frame remained unchanged; the deselected pair increased from approximately 70,70,68 to 102,102,100 RGB with the existing glyph-only bounds retained.

The final enlargement revision decodes exactly for both touched doctrine DDS files, with source alpha range 0-255 and no matte background. The stable mapmode DDS hashes and the other three doctrine runtime assets remained unchanged during this revision.

The focused GFX audit found every texturefile in `interface/016_brilliant_scientist_biological_raids.gfx`, `interface/cbrn_mio_industry.gfx`, `interface/mapmodes_interface.gfx` custom entries, `interface/chaosx_traits.gfx`, and `interface/cbrn_doctrine.gfx` resolves for the CBRN paths. The parent’s global audit found unrelated baseline missing paths; none belongs to this package.

## Retired binary cleanup

After active source-reference checks, removed:

- `gfx/interface/traits/024_video_game_in_sweden/024_video_game_in_sweden_field_validated_planner.dds`
- `gfx/interface/ideas/stage_5_chaos_warfare/cbrn_operations_director.dds`

Historical `docs/testing/` snapshots still mention those retired files as past audit records. The existing commander-traits handoff was updated to record the completed removal.

## Needs parent review

Review the contact sheets and stable GFX paths above, then reconcile the handoff with the parent CBRN audit. Live game visual validation remains a user-owned step; no game launch or log inspection was performed here.
