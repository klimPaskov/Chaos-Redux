# Event 028 scene-source replacement handoff, 2026-10-04

Disposition: implemented and parent-accepted as two staged original-art packages; both are `handed_off` with runtime promotion pending.

## Scope and acceptance basis

This handoff covers exactly two distinct Event 028 scene-art source replacements: the static 114x101 recovery decision-category picture and the 397x153 impact-news image. The parent explicitly accepted both artworks after reviewing each original, processed native image, native DDS view, both family sheets, and canonical references.

The parent assignment explicitly authorized original generation after the bounded source-recovery handoff found none of the 45 historical masters, including the accepted crater/rail category master. It also confirmed that the inherited impact-news DDS has no verified original master, author, source, or rights record.

The new files establish independent fictional ImageGen lineage; they are not archival authorship, recovered historical sources, public-domain photographs, or evidence about the inherited DDS.

The accepted category picture remains a static `PICTURE` surface under `GFX_decision_cat_picture_028_asteroid_recovery`; the image is not a small category button icon, decision icon, focus icon, idea icon, or scripted-GUI background.

## Files created

- `docs/assets/028_asteroid_incoming/regeneration/scene_replacements/v001_20261004/manifest.md` records both rows, source provenance, prompts, hashes, consumer paths, processing, alpha evidence, DDS checks, contact sheets, and review status.
- `docs/assets/028_asteroid_incoming/regeneration/scene_replacements/v001_20261004/gfx_handoff.md` lists both existing sprites, target GFX file, intended runtime paths, and consumers.
- `docs/assets/028_asteroid_incoming/regeneration/scene_replacements/v001_20261004/prompts/decision_category_028_asteroid_recovery_v001.md` and `docs/assets/028_asteroid_incoming/regeneration/scene_replacements/v001_20261004/prompts/news_event_028_asteroid_impact_v001.md` preserve the submitted prompts.
- `docs/assets/028_asteroid_incoming/regeneration/scene_replacements/v001_20261004/source_png/` contains the two untouched generated source PNG copies; their hashes match the tool-returned source paths in the manifest.
- `docs/assets/028_asteroid_incoming/regeneration/scene_replacements/v001_20261004/processed_png/` contains the exact 114x101 category and 397x153 news previews.
- `docs/assets/028_asteroid_incoming/regeneration/scene_replacements/v001_20261004/final_dds/` contains the two repository-converter DDS candidates.
- `docs/assets/028_asteroid_incoming/regeneration/scene_replacements/v001_20261004/dds_roundtrip/` contains decoded round-trip PNGs pixel-identical to the processed previews.
- `docs/assets/028_asteroid_incoming/regeneration/scene_replacements/v001_20261004/contact_sheets/` contains one individually labeled review sheet for each asset family, including the source, enlarged native preview, and decoded DDS preview.
- `docs/assets/028_asteroid_incoming/regeneration/scene_replacements/v001_20261004/reference_inspection/` retains comparison decodes of the pre-existing category/news runtime DDS files; these are not source inputs.
- `docs/assets/028_asteroid_incoming/regeneration/scene_replacements/v001_20261004/validation/build_contact_sheets.py` is the bounded reproducible builder for the two family sheets and repeats the DDS pixel-equality check.

## Visual findings

`CAT-CRATER-RAIL-V001` shows a large, unmistakable physical impact crater with broken track and a period steam repair consist carrying rail, timber, and filter drums. The crater dominates the scene, so it does not repeat the rejected train/tent-only concept.

`NEWS-IMPACT-AFTERMATH-V001` is a separate full-width monochrome aftermath panorama with a long crater gouge, dust-softened industrial horizon, and broken rail foreground. It contains no impact-flash column and is not a report or super-event crop.

The category-family references were inspected only under the canonical `assets/gfx_references/icons/decision_categories/pictures/` root, including its contact sheet and two full 114x101 examples. The news-family contact sheet and all five full 397x153 references were inspected only under the canonical `assets/gfx_references/event_art/news/` root.

The category consumer and current sprite path were read from `common/decisions/categories/028_asteroid_incoming_categories.txt:8-10` and `interface/028_asteroid_incoming.gfx:34-35`. The news consumer and sprite path were traced in `events/_chaosx_news.txt` and `interface/028_asteroid_incoming.gfx:30-31`; both sprite names and destinations remain unchanged.

The category’s inspected consumer and reference family support an opaque 114x101 full-canvas picture. The news consumer, vanilla reference DDS, and canonical news examples support an opaque 397x153 full-canvas image. Both initial generation calls therefore requested no transparency, and both staged results remain alpha 255 throughout.

The standard repository `convert_to_dds.py` produced one-level legacy uncompressed BGRA DDS files. Both DDS headers, dimensions, pixel-format masks, caps, file lengths, alpha, and decoded pixels were checked; the exact evidence is in the staging manifest.

## Remaining review and limits

Both artworks are parent-accepted and their packages are `handed_off`; runtime promotion remains pending and parent-owned. This handoff does not claim in-game validation or runtime completion.

No GFX, event, category, gameplay, localisation, GUI, spreadsheet, global manifest, existing asset audit, or runtime DDS was modified. No game was launched, and no in-game consumer result is claimed.

No fallback, placeholder, borrowed artwork, or simplification was used within these two assigned rows. The user’s broader Event 028 visual audit remains outside this handoff’s two-asset ownership boundary.

## Parent acceptance details and ImageGen receipts

For `CAT-CRATER-RAIL-V001`, the parent accepted the crater-dominant picture with the working rail consist along the crater perimeter rim, not restoration of the empty center; no tents are present.

For `NEWS-IMPACT-AFTERMATH-V001`, the parent accepted the distinct wide monochrome aftermath with the intact industrial horizon and broken foreground rails, without flash, gore, modern props, or text.

The exact returned ImageGen `output_hint` strings, tool paths, prompt hashes, and byte-matched staged source hashes are recorded in the staging manifest. The observed tool result exposed `image_url` and `output_hint`; no separate receipt ID, raw retained image payload, or additional model metadata was available or inferred.

The earlier staged `needs_user_review` state is superseded by parent art acceptance. The two final DDS candidates remain in the versioned staging directory until the parent reports runtime promotion.

## Parent-reported runtime promotion, 2026-10-04

The parent reports that both DDS files have been promoted to their existing runtime paths, with current runtime hashes byte-for-byte matching the staged candidates.

| Asset | Runtime path | Parent-reported runtime SHA-256 |
| --- | --- | --- |
| Decision-category picture | `gfx/interface/decisions/028_asteroid_incoming/decision_category_028_asteroid_recovery.dds` | `15FC509F0BF338A02AC9CD57BC25A038D1F6F196A922558427A0D0EAA267C8B8` |
| Impact-news image | `gfx/event_pictures/028_asteroid_incoming/news_event_028_asteroid_impact.dds` | `A9A03D0FC41A26BC9F33BE198CFBA7FF480110300A41B418E3C8AC197B5EAE69` |

The parent reports that the previous runtime DDS hashes were verified against baseline and those files were backed up under `runtime_before_20261004/` before replacement. The parent also reports canonical BGRA headers and byte lengths, opaque alpha 255, and decoded pixel identity for the promoted files.

This parent-reported promotion supersedes the earlier promotion-pending note. Native consumer acceptance remains pending. The inherited news source/master provenance and rights remain unknown; its prior DDS is archived in the reported before-state backup and is no longer live.

No runtime readback, runtime write, new art call, source move, or commit was performed for this status update.
