# Event 089 Doctor Wu portrait animation asset handoff

## Result

Created two independent fictional continuity-dispute portrait animation options. The unresolved specification difference is preserved: Part 19 and the event asset prompt request AN01 at twelve frames and 6 fps; Part 7 requests a distinct ten-frame, 5 fps animation. No source specification was changed.

The event asset workspace is ignored by Git by repository policy (`.gitignore:80`, `docs/assets/`). All image outputs and evidence therefore live under `docs/assets/portraits/089_doctor_wu/` and must not be committed or pushed.

## Production and identity

The Event 089 asset prompt identifies Doctor Wu as fictional and says he keeps a recognizable, period-fit identity. The fictional image-generation route was used; no real-person image or reference supplied identity. The master and every frame were generated with Codex native ImageGen. The tool did not expose a backend model selector; no unreported model name is claimed.

Before production, the canonical vanilla leader reference family was inspected at `.claude/skills/chaos-redux-event-assets/assets/gfx_references/portraits/leaders/contact_sheet.png` and its eight 156×210 references. Wu's generated master has a hand-painted HOI4-era portrait treatment. Each animation frame was generated separately using the master as the identity reference and a specific expression/eye-focus state prompt.

## Delivered outputs

The durable inventory and exact file hashes are in `docs/assets/portraits/089_doctor_wu/portrait_animation_manifest.json`; per-frame crop boxes, source/processed paths and hashes are in `processing_qa.json`.

| Option | Genuine source frames | Processed frames | Sheet PNG / DDS | Rate | Static PNG / DDS |
| --- | ---: | ---: | --- | ---: | --- |
| AN01 | 12 | 12 × 156×210 | 1872×210 | 6 fps | 156×210 |
| `alternative_legacy_10f` | 10 | 10 × 156×210 | 1560×210 | 5 fps | 156×210 |

Each option has source and processed PNG frames, sheet PNG and DDS, static fallback PNG and DDS, a labeled contact sheet, and a review-only GIF. Frame prompt records are in each option's `prompts.json`. The original generated master is `AN01/source/doctor_wu_continuity_master.png`.

## QA and binding status

Both contact sheets were visually reviewed. Face identity, clothing, framing, palette, background, lighting, and placement remain consistent, and the separately generated eyes/expression states read as subtle continuity uncertainty. Both GIF frame counts and PNG sheet dimensions match their specification. DDS conversion used `.claude/skills/chaos-redux-event-assets/tools/convert_to_dds.py`; each DDS begins with the DDS magic/header and is nonempty. DDS dimensions were requested at exact sheet/static sizes.

No GFX, character portrait field, scripted GUI, or other UI binding was made, per the asset-only scope. The exact character key and portrait field for the qualified continuity officeholder, actual state trigger for showing the animation, and approved choice between AN01 and the Part 7 legacy option remain for parent integration and review. The manifest proposes `GFX_089_wu_continuity_static` and `GFX_089_wu_continuity_animated` as names only; they are not registered.

No runtime/game view or target-surface behavior was checked. DDS pixel decoding and engine loading were not tested; the recorded DDS evidence is conversion output, magic/header, nonzero size, and expected dimensions passed to the converter. The output is generated candidate art awaiting parent selection and any integration review.
