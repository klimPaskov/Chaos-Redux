# Event 012 static graphics takeover

**Status:** 21 textures installed and reviewed, including both parent-wired native autonomy paths. The parent reviewed the native-size and 4x preview sheets and approved DDS promotion after strict round-trip and edge checks.

## Ticket results

| Ticket | Result | Runtime target | Evidence |
| --- | --- | --- | --- |
| Six tier-A badges | Complete: solid opaque-body laurel badges for gorilla kingdom, the green, living rivers, stoneborn, Pan high chaos, and ancient hosts. | Six `gfx/interface/goals/012_africa/tier_a/goal_012_africa_*.dds` files at 94x86. | `sources/imagegen/tier_a_focus_badge_atlas_source_v1.png`; prompt `prompts/tier_a_focus_badge_atlas.json`; 4x and round-trip sheet `evidence/source_png_4x_dds_focus_decision_contact_sheet.png`. |
| Six decision twins | Complete: each icon was directly re-exported from its matching generated badge source crop in one bicubic pass at the table's exact 32x32 target. | Six `gfx/interface/decisions/012_africa/tier_a/decision_012_africa_*.dds` files at 32x32. | The live texture dimensions were inspected as 32x32; vanilla decision reference was 33x32; exact pixel round-trip and alpha means above 217. |
| Four South America plaques | Complete: four separate scenes in the matching thin rectangular frame, with no seams or baked writing. | `goal_012_south_america_resource_sovereignty.dds`, `goal_012_south_america_defence_corridors.dds`, `goal_012_south_america_south_atlantic_partnership.dds`, and `goal_012_south_america_ratification.dds` at 94x86. | Accepted v2 atlas and prompt; source/PNG/DDS sheet `evidence/source_processed_dds_south_america_contact_sheet.png`. |
| Shared covenant emblem | Complete: tree and root ring inside the charter-family arch. Both current consumers share the 64x64 texture. | `gfx/interface/012_africa/emblems/012_africa_high_chaos_covenant_emblem.dds`. | Accepted v2 prompt/source; both `GFX_012_africa_high_chaos_covenant_emblem` and `GFX_idea_africa_unity_ancestral_covenant` map to it. |
| Elephant technology/equipment badge | Complete: 64x64 armoured war elephant with howdah. | `gfx/interface/technologies/012_africa/chaosx_elephant_equipment.dds`. | Compared against all eight existing Africa technology badges in `evidence/africa_tech_family_style_check.png`; the isolated painted subject fits their 64x64 family. The one DDS continues to serve the equipment and technology-medium aliases. |
| Federal-member autonomy | Art and DDS complete at 35x35. | `gfx/interface/autonomy/012_africa_federal_member_icon.dds`. | Uses two federal pillars and law seal; native vanilla autonomy DDS references and active custom state were inspected. The parent wired the exact native autonomy path while retaining the sprite name. |
| Integrated-region autonomy | Art and DDS complete at 35x35. | `gfx/interface/autonomy/012_africa_integrated_region_icon.dds`. | Uses three linked province tablets; native vanilla autonomy DDS references and active custom state were inspected. The parent wired the exact native autonomy path while retaining the sprite name. |
| Priority-member-departure report card | Complete: full-card grayscale plus the standard warm sepia map `#282018` to `#eee2c7`; card geometry and DDS alpha are byte-for-byte preserved. | `gfx/event_pictures/012_africa/priority_members/report_event_012_africa_priority_member_departure.dds` at 210x176. | `evidence/report_source_processed_dds_contact_sheet.png`; the source card was decoded from the preserved pre-change DDS. |

## Verification and promotion

The canonical reference contact sheets were inspected before individual reference examples. Current and installed vanilla DDS anchors were decoded and hashed before production. New alpha-backed art requested `transparent_background=true` in the initial built-in ImageGen call, retained real transparent canvas pixels, and had no alpha16 subject boundary coverage at the atlas-cell edges. No background-removal fallback was used.

All 21 PNGs were converted with the canonical asset-skill converter. All 21 DDS files passed strict BGRA header and declared-size checks and matched their PNG source pixels exactly after strict DDS decoding. Each final runtime file still matched its staged SHA-256 immediately after promotion.

The report sepia pass used `Pillow ImageOps.grayscale` followed by `ImageOps.colorize(black="#282018", white="#eee2c7")`; the source DDS alpha bytes were copied without change. Focus, decision, plaque, emblem, elephant, and autonomy subject alpha means all exceed 200 after target-size processing.

The parent approved texture promotion after the native-size and smooth 4x reviews. The final four family round-trip sheets are listed in `evidence/roundtrip_contact_sheet_inventory.json`.

## Parent-owned integration and related work

The parent wired both new autonomy textures in `interface/012_africa.gfx`, retaining `GFX_autonomy_africa_federal_member_icon` and `GFX_autonomy_africa_integrated_region_icon`.
The durable 21-row crosswalk is `docs/plans/012_africa_plans/takeover_static_gfx_inventory_2026-10-06.json`.
The original source, processing and review workspace remains at `docs/assets/012_africa/static_texture_repair_2026-10-06/` while live visual acceptance is pending.

The original review-plan claim that the autonomy states were unreferenced was corrected after the parent found live definitions and state-machine consumers in `common/autonomous_states/012_africa_autonomy.txt`.

The parent separately removed all 16 unused `division_template_emblems/012_africa` textures and their sprite definitions. Evidence is in `docs/plans/012_africa_plans/takeover_unused_emblems_2026-10-06.json`; those files were not restored here.

The initial plaque v1 candidate was retained but rejected for an extra wreath/medal frame and pseudo-writing. The initial covenant emblem v1 candidate was retained but rejected for a circular outer frame that did not match the existing charter arch. Accepted prompts and outputs are listed in the active manifest.

No counter textures, animation sheets or static animation endpoints, model/audio files, or interface files were changed in this tranche. The counter repair and reviewed parent promotion are documented in `takeover_counters_2026-10-06.md`. No in-game completion is claimed; the user owns live-game validation.
