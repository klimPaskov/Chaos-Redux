# Weaponized zombie category-picture asset handoff

Disposition: `implemented` for the seven live category-picture rows and `blocked` only for the unmapped wendigo source identity.

## Files changed

- Replaced the seven runtime DDS textures under `gfx/interface/decisions/visual_consistency_repair/pictures/decision_cat_picture_weaponized_zombie_{infected,rabid,parasitic,mutant,undead,necrotic,demonic}.dds`.
- Added the asset evidence package under `docs/assets/002_zombie_outbreak/decision_category_pictures/`, including decoded source portrait previews, processed `114x101` PNG previews, decoded DDS round-trip previews, contact sheets, `manifest.md`, and `gfx_handoff.md`.
- No `.gfx`, decision-category, localisation, GUI, gameplay, portrait-master, or zombie model/animation/sound file was edited.

## Exact surface and behavior

Each live weaponized zombie category picture now uses a deterministic aspect-preserving cover crop of its matching already-registered `GFX_portrait_ZZZ_weaponized_*` portrait source. The seven textures are opaque `114x101` full-canvas category panels and keep the portrait focal area readable without anisotropic stretching. Existing mismatched scene art was preserved in the evidence package for comparison.

The sprite names and `picture =` assignments already match the final runtime paths in `interface/visual_consistency_repair.gfx:55-61` and `common/decisions/categories/002_zombie_outbreak_categories.txt:71-145`, so the parent does not need duplicate wiring. The exact mapping, crop boxes, source paths, processed previews, and consumers are recorded in `docs/assets/002_zombie_outbreak/decision_category_pictures/manifest.md` and `gfx_handoff.md`.

## Validation

All seven outputs were converted with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`. Each final DDS is `114x101`, one-level uncompressed BGRA with the repository masks and texture caps, has a `46184` byte container, and decodes pixel-for-pixel equal to its processed PNG. All outputs have alpha range `(255,255)`. The native-size comparison contact sheet shows the old scene, selected portrait crop, and DDS round-trip for all seven rows.

Live HOI4 consumer rendering was not run because the parent owns final integration and the user owns live-game validation. No ImageGen call was used because this repair intentionally reuses the already-created outbreak portrait masters.

## Remaining issue and parent follow-up

The registered `GFX_portrait_ZZZ_weaponized_wendigo` source exists, but the named category consumer has no wendigo category or category-picture sprite. No orphan wendigo DDS was produced. The parent must either leave that source explicitly unmapped or accept a future category and sprite mapping before any wendigo category texture is created.
