# Famine and Migration Decision-Category Picture Manifest

Status: complete for matrix row `fm_pic_displacement`.

## Asset record

| Field | Value |
| --- | --- |
| Matrix ID | `fm_pic_displacement` |
| Runtime role | Static decision-category picture |
| Source mode | Native built-in ImageGen, original generated scene |
| Reference family | `icons/decision_categories/pictures` |
| Native consumer dimensions | 114×101 pixels |
| Background treatment | Opaque full-canvas scene, no transparency |
| Proposed sprite | `GFX_fm_pic_displacement` |
| Target `.gfx` | `interface/famine_and_migration_system.gfx` |
| Final texture path | `gfx/interface/decisions/famine_and_migration_system/fm_pic_displacement.dds` |
| GFX wiring status | Parent-owned; no `.gfx` file edited |

## Preserved files

| Role | Path | Dimensions / mode |
| --- | --- | --- |
| Generated source PNG | `docs/assets/famine_and_migration_system/category_picture/source_png/fm_pic_displacement_source.png` | 1536×1024 RGB |
| Processed PNG preview | `docs/assets/famine_and_migration_system/category_picture/processed_png/fm_pic_displacement.png` | 114×101 RGBA, alpha 255 |
| Final DDS | `gfx/interface/decisions/famine_and_migration_system/fm_pic_displacement.dds` | 114×101 BGRA8, no mipmaps |
| Prompt record | `docs/assets/famine_and_migration_system/category_picture/prompts/prompts.md` | Native ImageGen prompt and processing record |
| Review contact sheet | `docs/assets/famine_and_migration_system/category_picture/contact_sheets/category_picture_contact_sheet.png` | Source and exact-canvas review |
| GFX handoff | `docs/assets/famine_and_migration_system/category_picture/gfx_handoff.md` | Parent copy-ready sprite handoff |

SHA-256 hashes are `917b507ca51a3ff41c8ade4b2bc43aa29e54e8f7a23f9a3f3045bbfef80b63f2` for the source PNG, `eb337b245dfa7f09eaa381fc4c49f687c42dc91845d9f9a5ce21d48f15a645c7` for the processed PNG, `8c6d70b2b110e9b312d123fd358b1f800aa3cc561557067fc88bf18948db089d` for the final DDS, and `552c681046c904c4a78c224c81e406d186043b5b3f25ff917793831e009ff3d5` for the review contact sheet.

## Reference-family and consumer evidence

The matching canonical family at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decision_categories/pictures/` was inspected through its labeled contact sheet and 13 user-provided vanilla reference PNGs.

Every reference in that family is a lossless 114×101 review copy for the larger static decision-category picture surface, distinct from the 52×40 category icon family and from scripted-GUI backgrounds.

Installed vanilla `interface/decisions.gfx` registers this surface with `GFX_decision_cat_*` sprite names and texture paths under `gfx/interface/decisions/`, while the corresponding decision category definitions consume the sprite through their `picture = GFX_decision_cat_*` field.

Chaos Redux already uses the package folder `gfx/interface/decisions/famine_and_migration_system/` and the target registry `interface/famine_and_migration_system.gfx` for the shared system's category icon and decision assets.

The generated scene is a railway reception and relief station with civilians, luggage, period rail equipment, relief staff, handcarts, and crates, matching the matrix direction while avoiding readable text, flags, modern objects, UI artifacts, portraits, and graphic injury.

## DDS conversion and validation

The final file was produced from the processed PNG with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --width 114 --height 101`.

The validated DDS has a legacy 124-byte header, dimensions 114×101, no mipmaps, pixel-format size 32, flags 65, fourCC 0, 32-bit BGRA masks `0x00FF0000/0x0000FF00/0x000000FF/0xFF000000`, `DDSCAPS_TEXTURE` `0x1000`, and exact total length 46,184 bytes.

The processed PNG alpha range is `(255, 255)`. The DDS payload contains 46,056 bytes and matches the processed PNG byte-for-byte after RGBA-to-BGRA channel ordering, with zero mismatches.

## Parent boundary

Current source registers the proposed sprite and binds the shared decision category's `picture` field. The existing 52×40 `GFX_fm_cat_displacement` category icon is not a substitute for this 114×101 picture. No gameplay, decision, localisation, GUI, or `.gfx` file was edited by this package, and parent visual runtime validation remains open.
