# Other icon production handoff

The assigned 013, 015, 017, and 018 icon assets are generated, processed, installed, and documented. The full manifest and source lineage are in [`docs/assets/gfx_fix_other_icons_resume/manifest.md`](../../assets/gfx_fix_other_icons_resume/manifest.md) and [`asset_manifest.json`](../../assets/gfx_fix_other_icons_resume/asset_manifest.json).

| Event | Delivered assets | Runtime DDS count | Parent review |
|---|---|---:|---|
| 013 Natural Disasters | 53x40 Meteor Storm Command category icon | 1 | Accepted after alpha normalization and native/4x opacity review; standalone evidence is in [`evidence/013_meteor/meteor_validation.json`](evidence/013_meteor/meteor_validation.json). |
| 015 Utopia | Nine 52x40 category icons and one 64x64 Plural Compact emblem | 10 | Nine category icons and emblem accepted after source/native and 4x review. |
| 017 Random Faction | 32x32 Radio Networks icon | 1 | Alpha-normalized v2 accepted after native/4x opacity review; v1 was rejected for a narrow silhouette. |
| 018 Resources Found | 32x32 Deeper Test icon | 1 | Accepted after alpha normalization and native/4x opacity review. |

The nine exact 015 category suffixes are `league`, `ledger`, `district`, `island`, `necessary_ground`, `stewardship`, `defense`, `governance`, and `formation`.

Every selected runtime DDS passes strict one-level BGRA header validation, exact raw payload comparison to its processed PNG, Pillow native DDS decode comparison, and a check that the existing `.gfx` texturefile path still matches. The full report is [`docs/assets/gfx_fix_other_icons_resume/notes/runtime_validation.json`](../../assets/gfx_fix_other_icons_resume/notes/runtime_validation.json).

The selected sources request genuine transparency in ImageGen. Low-alpha exterior residue below alpha 8 was cleared only outside each source's alpha>=8 subject bounds before premultiplied-alpha resizing; all processed canvases retain zero-alpha corners and the reviewed visible margins. No background-removal fallback or component background was used.

Runtime texture paths and sprite names remain stable, and no `.gfx`, GUI, gameplay, script, localisation, focus, portrait, photo, spreadsheet, or commit changes were made by this subagent. The parent owns GFX wiring and commit selection. The parent accepted the three normalized final contrasts after native/4x opacity review; RGB, placement, visible bounds, and intentional gaps remain unchanged. User/orchestrator live checks remain pending.


The selected processed PNGs and pre-alpha runtime DDS bytes are retained as superseded evidence under `docs/plans/gfx_fix_2026-10/evidence/017`, `evidence/018`, and `evidence/013_meteor`; the alpha-normalized runtime DDS replaces only the assigned texture bytes.
