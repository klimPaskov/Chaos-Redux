# Event 037 Mysterious People: icon asset handoff

Manifest: docs/assets/037_mysterious_people/icons/manifest.md. Contact sheet: docs/assets/037_mysterious_people/icons/contact_sheets/icons_037_final_dds_native_and_enlarged.png (native 1x and enlarged review rows, plus the three achievement triplets).

## Final DDS files

All decision, category, and mission files are one-level uncompressed 32-bit BGRA with the pixel-format, mask, and texture-cap checks passed. Decoded alpha ranges from 0 to 255 with transparent corners, so these are native-transparent. Achievement files are 64x64 with alpha 254 to 255, because the supplied template is an opaque medallion, which matches the famine achievement family. Every achievement state passed the processor's strict audit and source-layer equality check.

| Final DDS (runtime path) | Size | Alpha | Sprite (already registered) | Status |
| --- | --- | --- | --- | --- |
| gfx/interface/decisions/037_mysterious_population/mysterious_people_category.dds | 52x40 | verified, transparent corners, roundel layer under the subject | GFX_mysterious_people_category | complete |
| gfx/interface/decisions/037_mysterious_population/mysterious_people_stance_open.dds | 32x32 | verified | GFX_mysterious_people_stance_open | complete |
| gfx/interface/decisions/037_mysterious_population/mysterious_people_stance_restricted.dds | 32x32 | verified | GFX_mysterious_people_stance_restricted | complete |
| gfx/interface/decisions/037_mysterious_population/mysterious_people_registration_drive.dds | 32x32 | verified | GFX_mysterious_people_registration_drive | needs_user_review (dense at 32 px) |
| gfx/interface/decisions/037_mysterious_population/mysterious_people_requisition.dds | 32x32 | verified | GFX_mysterious_people_requisition | complete |
| gfx/interface/decisions/037_mysterious_population/mysterious_people_emergency_housing.dds | 32x32 | verified | GFX_mysterious_people_emergency_housing | complete |
| gfx/interface/decisions/037_mysterious_population/mysterious_people_roads_water.dds | 32x32 | verified | GFX_mysterious_people_roads_water | needs_user_review (dense at 32 px) |
| gfx/interface/decisions/037_mysterious_population/mysterious_people_new_city.dds | 32x32 | verified | GFX_mysterious_people_new_city | complete |
| gfx/interface/decisions/037_mysterious_population/mysterious_people_mission_absorb.dds | 32x32 | verified | GFX_mysterious_people_mission_absorb | complete |
| gfx/interface/decisions/037_mysterious_population/mysterious_people_modifier_newcomers.dds | 32x32 | verified | GFX_mysterious_people_modifier_newcomers | complete; parent to confirm the consumer canvas |
| gfx/achievements/037_room_for_everyone.dds (+ _grey, _not_eligible) | 64x64 | opaque template by design | GFX_achievement_037_room_for_everyone (+ _grey, _not_eligible) | complete |
| gfx/achievements/037_a_billion_more.dds (+ _grey, _not_eligible) | 64x64 | opaque template by design | GFX_achievement_037_a_billion_more (+ _grey, _not_eligible) | complete |
| gfx/achievements/037_three_censuses.dds (+ _grey, _not_eligible) | 64x64 | opaque template by design | GFX_achievement_037_three_censuses (+ _grey, _not_eligible) | complete |

## Fallbacks and edits

No background removal was used. Native transparency passed validation for every decision and category source. The achievement subjects had alpha 1 to 7 exterior residue, which was zeroed before fitting (bounded cleanup, recorded in the manifest). The category subject uses the cataloged roundel as a persistent background layer beneath the generated subject, recorded as a component layer. The first 2:1 category candidate was rejected as too wide for the 52x40 roundel and is superseded by the square candidate.

## Items for the parent

1. Confirm that the modifier consumer expects a 32x32 canvas. The request gave 32x32 and the consumer was not separately inspected.
2. `GFX_mysterious_people_category_picture` (mysterious_people_category_picture.dds) already exists in the decisions folder but was not created here. The report image `GFX_report_mysterious_people_manifestation` is also registered and was not produced. Both are outside this icon request.
3. roads_water and registration_drive are dense at 32 pixels. Both read as a silhouette at 4x but are busy at native size. Consider simplifying the subject if the parent review rejects them.
4. No `.gfx`, localisation, script, or other gameplay files were edited. Nothing was committed to git. Hearts of Iron IV was not launched.
