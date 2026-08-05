# CBRN division-template emblem package v3

This package contains only the two requested CBRN division-template emblem families for Chaos Redux: custom templates 046 chemical warfare and 047 biological warfare, each with a large 76x42 texture and a native small 30x12 texture.

## Review state

Production files and evidence are present, but all four visual assets remain `needs_user_review`; this handoff does not claim acceptance.

No GFX, GUI, gameplay, localisation, event, decision, focus, idea, or spreadsheet file was edited.

## Required reference inspection

- Canonical contact sheet inspected before production: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/division_template_emblems/contact_sheet.png`.
- Every canonical individual reference `custom_template_000.png` through `custom_template_014.png` in that same folder was inspected at native 76x42 resolution.
- Existing runtime 044 and 045 large and small DDS assets were inspected through their retained decoded evidence and their legacy DDS dimensions/lengths.
- Existing inspection evidence inspected: `contact_sheets/existing_custom_templates_inspection.png`, `existing_custom_template_044_large.png`, `existing_custom_template_044_small.png`, `existing_custom_template_045_large.png`, and `existing_custom_template_045_small.png`.
- Prior v1 evidence inspected under `templates/contact_sheets/`, including `accepted_templates_native.png`, `accepted_templates_review_4x.png`, and `final_dds_decoded_review.png`.
- Prior v2 evidence inspected under `v2_templates/contact_sheets/`, including `v2_templates_native.png`, `v2_templates_review_4x.png`, and `final_dds_decoded_review.png`.

The canonical family established one centered muted green stamped mark, dark outline/shadow, transparent unused canvas, smooth illustrated edges, and generous empty space. The prior packages were treated as review precedents only; no v1/v2 art was copied, resized, recoloured, or used as a substitute.

## Source and ImageGen record

Source mode was the official built-in ImageGen workflow from the `imagegen` skill, not a local drawing or fallback route.

The source masters were generated at high resolution on uniform removable magenta chroma backgrounds because the emblem foreground is green.

| Asset family | Retained ImageGen source | Source size | Prompt | Source SHA-256 |
| --- | --- | --- | --- | --- |
| 046 chemical | `source_png/custom_template_046_source.png` | 1254x1254 | `prompts/custom_template_046_source.txt` | `06de8a57bc8140b148a0bcaeae4e257a190cfad4705077aabd554ab56d302211` |
| 047 biological | `source_png/custom_template_047_source.png` | 1254x1254 | `prompts/custom_template_047_source.txt` | `f9226c5668c4d58309a7e6e6127871a9df6fedb4787d69af463cae61db80b3d3` |

The original built-in ImageGen outputs remain at `C:/Users/klimp/.codex/generated_images/019fd27e-77e2-7553-86d0-5c1c45e1d1ba/exec-0934c159-9e41-4116-b632-62ffdc9bf4f2.png` for 046 and `exec-bb47a2d0-41ab-48f3-965b-fd83fd689038.png` for 047; the workspace copies above are the retained package sources.

## Processing record

The approved chroma-key helper was used at `C:/Users/klimp/.codex/skills/.system/imagegen/scripts/remove_chroma_key.py` with `--auto-key border --soft-matte --transparent-threshold 12 --opaque-threshold 220 --despill`.

The helper-produced transparent masters are retained as `processed_png/custom_template_046_transparent.png` and `processed_png/custom_template_047_transparent.png`, both 1254x1254 RGBA images.

Each target was then made from its own transparent ImageGen master by tight alpha cropping, muted green reference-aligned colour grading, alpha-aware premultiplication, and smooth Lanczos downsampling into a centered transparent canvas. Nearest-neighbour was not used for final target creation.

The colour comparison used the canonical family checkpoints `#496A49`, `#96A996`, and `#1F2C1F` together with the muted olive outline/midtone language visible in the inspected 044/045 precedents. The final foreground is olive/green only; the magenta key is absent from final alpha-bearing pixels.

## Requirement-to-runtime crosswalk

| Requirement | Processed PNG | Canvas | Visible bounds, alpha >32 | Runtime DDS | DDS length | Status |
| --- | --- | --- | --- | --- | ---: | --- |
| 046 chemical emblem, large | `processed_png/custom_template_046_large.png` | 76x42 | `(29,11)-(45,30)`, 17x20 | `gfx/interface/counters/division_templates_large/custom_template_046.dds` | 12896 | needs_user_review |
| 046 chemical emblem, native small | `processed_png/custom_template_046_small.png` | 30x12 | `(11,1)-(17,9)`, 7x9 | `gfx/interface/counters/division_templates_small/custom_template_046.dds` | 1568 | needs_user_review |
| 047 biological emblem, large | `processed_png/custom_template_047_large.png` | 76x42 | `(28,11)-(47,30)`, 20x20 | `gfx/interface/counters/division_templates_large/custom_template_047.dds` | 12896 | needs_user_review |
| 047 biological emblem, native small | `processed_png/custom_template_047_small.png` | 30x12 | `(10,1)-(18,9)`, 9x9 | `gfx/interface/counters/division_templates_small/custom_template_047.dds` | 1568 | needs_user_review |

All four processed target PNGs are RGBA with alpha range 0..255 and transparent corners. The large marks stay within the requested 15-20 px visual range and do not touch the frame.

## DDS and evidence files

The final DDS files were converted with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` using exact target dimensions.

All four outputs have the required legacy one-level uncompressed BGRA contract: `DDS ` magic, 128-byte header, `DDS_HEADER` size 124, pixel-format size 32, flags 65, fourCC 0, 32-bit RGB, masks `0x00FF0000/0x0000FF00/0x000000FF/0xFF000000`, `DDSCAPS_TEXTURE` `0x1000`, no mipmaps, and exact file lengths.

Decoded DDS pixels are byte-identical to the corresponding processed PNGs.

Validation details are retained in `contact_sheets/dds_validation.txt`.

The review contact sheet `contact_sheets/v3_templates_review_contact_sheet.png` shows the native ImageGen source, processed transparent target, smooth enlarged preview, and decoded DDS for all four runtime files.

The enlarged individual reviews are in `contact_sheets/enlarged/`, and the decoded DDS images are in `contact_sheets/decoded/`.

## Final hashes

| File | SHA-256 |
| --- | --- |
| `processed_png/custom_template_046_large.png` | `d4ce9835ea4bb01c430f321033fb8e217ef68f75c748dd26dcec0f37ba0ed70c` |
| `processed_png/custom_template_046_small.png` | `b41004dffabfd5451301bd3efc21b9759ca2c16ed366b29090f9d3dcc7b6aba7` |
| `processed_png/custom_template_047_large.png` | `1e8ac59ba7a02d7f24d0cb9c644fe586fc61624ba63eed576ec4e2f2502b987f` |
| `processed_png/custom_template_047_small.png` | `14f9d32b11288c331a2739edab185f4792dd7b074f3224b251066fd9990d1007` |
| `gfx/interface/counters/division_templates_large/custom_template_046.dds` | `284c7c86d2b087e568975b94ffbff1cbce71619af64b9b940c2068d3a89de420` |
| `gfx/interface/counters/division_templates_small/custom_template_046.dds` | `f4c8f7b97a2ec8646b919bfe51d0d6ceaf7e94ca35b05121edeae5c722ae3c30` |
| `gfx/interface/counters/division_templates_large/custom_template_047.dds` | `ceecf68ac8d27209ef8c4e1b5c66c9a1411072164806be9cd4b4d6a51e8edfdd` |
| `gfx/interface/counters/division_templates_small/custom_template_047.dds` | `3092743e203d9311dd7110534741e478c9fd2b3e128e81d23291fe1061cf0966` |

## Remaining review note

The parent agent should perform the final visual acceptance review of the v3 contact sheet and live consumer wiring. No asset is marked accepted by this package.
