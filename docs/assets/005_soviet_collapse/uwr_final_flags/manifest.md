# Event 005 UWR final flag family manifest

Status: complete for generated asset production and runtime installation.

Event: `005_soviet_collapse`.

Country: `UWR`, the fictional Unconventional Warfare Republic.

Asset classification: fictional alternate-history country flag family with one base flag and four ideology-specific variants.

Source mode: `$imagegen` via the official built-in ImageGen skill, with one separate generated source master for each visually distinct flag design.

Generation fit: UWR is fictional and high-chaos, and its Tver pathogen directorate, laboratory security, and chemical/biological warfare command have no historical flag that should be reproduced. Generation was therefore the correct source mode for an original institutional heraldry family.

Reference review: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/flags/contact_sheet.png` and its matching flat flag references were inspected before generation. Installed vanilla representatives confirmed the HOI4 ladder sizes of 82x52, 41x26, and 10x7 and 32-bit uncompressed TGA storage. Existing `UWR`, `DSC`, and `KMB` ladders were inspected in all three sizes; the old UWR base, democratic, and neutrality files were byte-identical to DSC, and the entire old UWR family was replaced in this scoped task.

Design language: the family uses a sealed laboratory containment device and a compact tri-lobed pathogen/leaf glyph as the UWR identity. The base design is a midnight-teal containment shield, the communist variant is an oxblood laboratory seal, the democratic variant is a steel-blue civic charter hexagon, the fascist variant is a severe black-and-vermilion containment standard, and the neutrality variant is an olive-grey research seal. None uses readable text, a waving flag, a flagpole, a scene, a watermark, DSC's orange gear/book language, or KMB's black crossed-arms composition.

## Generated source masters

| Variant | Source PNG | Native dimensions | Source SHA-256 |
| --- | --- | --- | --- |
| Base | `source_png/UWR_master.png` | 1576x998 RGB | `ead049ab8f8f30bf5fa5e251a88f6f1b798a4099555f38958f0cfcf7995258b5` |
| Communism | `source_png/UWR_communism_master.png` | 1576x998 RGB | `db097f60ff253b7c1b799f786847999e2a2fcbd1138a7b44deba84a2cf033e8d` |
| Democratic | `source_png/UWR_democratic_master.png` | 1576x998 RGB | `c7167074638e2ef465a60cc6687c0fce1fdbb71290feb0ee1457a9b946c55bf6` |
| Fascism | `source_png/UWR_fascism_master.png` | 1577x997 RGB | `d0d5dbc8bc8c5456d72ac4ca251ffdf5b51a2e17354cf4e43b69ed4e9cce62b9` |
| Neutrality | `source_png/UWR_neutrality_master.png` | 1576x998 RGB | `20c932e828ab9fdc444a3f0fb45c93ad75b834f2e9f5c249d36444ef996f7ae5` |

The exact prompts are retained in `prompts/uwr_flag_generation_prompts.md`.

## Runtime flag outputs

All final flags are 32-bit uncompressed truecolor TGA files with image type 2, zero ID and colour-map lengths, opaque alpha channel, and bottom-left TGA origin descriptor `0x00`. Each file is exactly `18 + width * height * 4` bytes and decodes pixel-identically to its processed PNG preview.

| Variant | Target size | Processed PNG | Runtime TGA | TGA SHA-256 | DDS QA artifact |
| --- | --- | --- | --- | --- | --- |
| Base | 82x52 | `processed_png/UWR_normal.png` | `gfx/flags/UWR.tga` | `d11f8da5da4f6309ca493a125700510d8a9c69c2b560ed13585a2b85b5e60998` | `dds_preview/UWR_normal.dds` |
| Base | 41x26 | `processed_png/UWR_medium.png` | `gfx/flags/medium/UWR.tga` | `d10a7ab5ec759778466c9111648f62d070d5f1237d075410e0f9a2f7df66d26d` | `dds_preview/UWR_medium.dds` |
| Base | 10x7 | `processed_png/UWR_small.png` | `gfx/flags/small/UWR.tga` | `68758eb430374d80065a3e8b81a45995766be344faffe805074b0a41cdd2ddf6` | `dds_preview/UWR_small.dds` |
| Communism | 82x52 | `processed_png/UWR_communism_normal.png` | `gfx/flags/UWR_communism.tga` | `a661499c75aeb022fd9a4fd9a2252af34ea159e03caa071e4b51f4851986fa18` | `dds_preview/UWR_communism_normal.dds` |
| Communism | 41x26 | `processed_png/UWR_communism_medium.png` | `gfx/flags/medium/UWR_communism.tga` | `411748ab8729344fdc126b61319dc3bc19044598de740d76daf1b3bbba55b6d5` | `dds_preview/UWR_communism_medium.dds` |
| Communism | 10x7 | `processed_png/UWR_communism_small.png` | `gfx/flags/small/UWR_communism.tga` | `d82cf3ff1defb567242096d5694668c7c42057b91783db602e31020cc66941dc` | `dds_preview/UWR_communism_small.dds` |
| Democratic | 82x52 | `processed_png/UWR_democratic_normal.png` | `gfx/flags/UWR_democratic.tga` | `65607d14f03d996cfa9434547ead20fb9d90ee5e1292f088c6c3bd7f4a2703ba` | `dds_preview/UWR_democratic_normal.dds` |
| Democratic | 41x26 | `processed_png/UWR_democratic_medium.png` | `gfx/flags/medium/UWR_democratic.tga` | `d60214aa09e3d594b4db5dff33a85c08ed546e93e3c3a4f983fd921339c4a3b1` | `dds_preview/UWR_democratic_medium.dds` |
| Democratic | 10x7 | `processed_png/UWR_democratic_small.png` | `gfx/flags/small/UWR_democratic.tga` | `6cfcd91c36de1e3d8efc5295aa8906d6232728565b9d514ea58ecd94664fa1a3` | `dds_preview/UWR_democratic_small.dds` |
| Fascism | 82x52 | `processed_png/UWR_fascism_normal.png` | `gfx/flags/UWR_fascism.tga` | `7ef3bd3f79b4f07332901360675ef44193d8f7b379d2174b70831d466982387a` | `dds_preview/UWR_fascism_normal.dds` |
| Fascism | 41x26 | `processed_png/UWR_fascism_medium.png` | `gfx/flags/medium/UWR_fascism.tga` | `c4564cdf206d7c5a8ae3baa5e4aa6c042deea50714dd82ed70a5da2d88b6001b` | `dds_preview/UWR_fascism_medium.dds` |
| Fascism | 10x7 | `processed_png/UWR_fascism_small.png` | `gfx/flags/small/UWR_fascism.tga` | `b046318a0bc43e66ef954aa6954e6da874723b3d17c29701f7f0c548b7075910` | `dds_preview/UWR_fascism_small.dds` |
| Neutrality | 82x52 | `processed_png/UWR_neutrality_normal.png` | `gfx/flags/UWR_neutrality.tga` | `4d622020ae31321efeabddf61422f7906c6b2a228b8501d5efe08a3918ccae5b` | `dds_preview/UWR_neutrality_normal.dds` |
| Neutrality | 41x26 | `processed_png/UWR_neutrality_medium.png` | `gfx/flags/medium/UWR_neutrality.tga` | `9b8f48860f26d6174e6e741d71bd25a51d3d958219ba446b13249ff4f764fd5b` | `dds_preview/UWR_neutrality_medium.dds` |
| Neutrality | 10x7 | `processed_png/UWR_neutrality_small.png` | `gfx/flags/small/UWR_neutrality.tga` | `99acb4673fe4fdfdfe0c8da14036a0b6818bd1828a6716492c9f4ae329a2b26e` | `dds_preview/UWR_neutrality_small.dds` |

The DDS files are repository-standard converter QA artifacts retained with the active asset package. HOI4 country flags use TGA runtime files and do not consume DDS paths.

## QA evidence

`contact_sheets/current_reference_flags.png` records the pre-change UWR/DSC/KMB reference ladder. `contact_sheets/final_flag_family_contact_sheet.png` compares each ImageGen source master with its normal, medium, and small decoded TGA exports.

All 15 runtime TGAs passed exact native dimensions, image type 2, 32-bit channel depth, bottom-origin descriptor `0x00`, expected byte length, alpha min/max `255/255`, and processed-PNG pixel equality. The Unix `file` utility was unavailable in the Windows shell, so the TGA header and origin checks were performed directly from the binary header and by round-trip decoding with Pillow.

All 15 DDS QA artifacts were produced with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` and passed the standard 128-byte legacy BGRA header, exact dimensions, exact file length, BGRA masks, texture caps, and alpha min/max `255/255` checks.

No final UWR TGA is byte-identical to the current DSC or KMB file at the corresponding size. Mean absolute RGB distance from DSC is 26.1 to 50.0 per channel byte across the UWR family and sizes; distance from KMB is 32.8 to 59.1.

No `.gfx`, localisation, gameplay, country, idea, focus, event, decision, GUI, or other flag file was edited.
