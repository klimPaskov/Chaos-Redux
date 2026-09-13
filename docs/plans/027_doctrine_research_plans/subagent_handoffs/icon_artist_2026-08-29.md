# Event 027 Doctrine Research icon artist handoff

Date: 2026-08-29.

## Result

Complete original achievement icon triplets were produced for `027_doctrine_research_first_lesson`, `027_doctrine_research_single_school`, and `027_doctrine_research_joint_curriculum`.

Each triplet has a completed, grey, and not-eligible state.

The three completed motifs are distinct and coherent: a first-lesson field manual with pencil and staff-college insignia, five curriculum tabs converging on one school crest, and four track emblems around a binder and compass.

The artwork does not reuse or imitate the official Doctrine of Choice achievement artwork.

## References inspected

- Canonical contact sheet: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/achievements/contact_sheet.png`.
- Canonical individual references: `30_minutes_of_hel`, `assuming_direct_control`, `britzkrieg`, `crusader_kings_2`, and `the_revolution_triumphant`, each inspected in completed, grey, and not-eligible form under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/achievements/`.
- Installed Vanilla achievement DDS family: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/achievements/`.
- Installed strict sample family members were 64x64, 16,512-byte, one-level, uncompressed 32-bit BGRA with opaque alpha and the canonical masks; the installed `the_revolution_triumphant` triplet is a compressed legacy exception and was not copied or used as a runtime source.
- Existing Chaos Redux convention inspected in `interface/chaosx_achievements.gfx`: `GFX_achievement_<full_id>` aliases point to root-level `gfx/achievements/<full_id>{,_grey,_not_eligible}.dds` paths.

## Output paths

### Native ImageGen source PNGs

- `docs/assets/027_doctrine_research/source_png/027_doctrine_research_first_lesson_source.png` — 1254x1254 RGBA, alpha 0..255, SHA-256 `6994FC60F9F6C28B6B73534C128E59632484A61FE8C2E43DEC963BE072AB33F2`.
- `docs/assets/027_doctrine_research/source_png/027_doctrine_research_single_school_source.png` — 1254x1254 RGBA, alpha 0..255, SHA-256 `CF8D2E754C698C1BD1BD3BE5FB1C2B00E96EBAF942606ECAC0D240848A835CC0`.
- `docs/assets/027_doctrine_research/source_png/027_doctrine_research_joint_curriculum_source.png` — 1254x1254 RGBA, alpha 0..255, SHA-256 `39DC3CE14F6E40A8E72D05D9FC22FAC5DABEE10D52C37225EE1060DFC3D2AA69`.

The source masters were created with the official built-in ImageGen skill using native transparency in the initial call.

### Processed 64x64 RGBA source state layers

All paths below are exact 64x64 RGBA PNGs with alpha range 0..255.

- `docs/assets/027_doctrine_research/processed_png/source_layers/027_doctrine_research_first_lesson.png` — SHA-256 `ED3BD9DE007F7AE5786817F32A9870407C6701121D34A9999077F3581473076B`.
- `docs/assets/027_doctrine_research/processed_png/source_layers/027_doctrine_research_first_lesson_grey.png` — SHA-256 `72EA23597595351339FD607A1945DE5CB108F5C9288094371C806F4C3ADA5EC8`.
- `docs/assets/027_doctrine_research/processed_png/source_layers/027_doctrine_research_first_lesson_not_eligible.png` — SHA-256 `8A6770F3AAB9191055A0DEF52464E6DFF9704DE43FAD4E6596D91621C9CF4F3E`.
- `docs/assets/027_doctrine_research/processed_png/source_layers/027_doctrine_research_single_school.png` — SHA-256 `12C317FAE980F1E90080D7BF18294A96D16037A24D880BBA3C495AE6B3463F7B`.
- `docs/assets/027_doctrine_research/processed_png/source_layers/027_doctrine_research_single_school_grey.png` — SHA-256 `8214B5DB167F350BA47B2D4A1831ACCA491774CC9799F34C07964D920F247378`.
- `docs/assets/027_doctrine_research/processed_png/source_layers/027_doctrine_research_single_school_not_eligible.png` — SHA-256 `46DAD03936AB3A22315764E16CDFBCA4E37F276E20884EDC626F25F0B022EF53`.
- `docs/assets/027_doctrine_research/processed_png/source_layers/027_doctrine_research_joint_curriculum.png` — SHA-256 `2C0428E9429AA6E7BDF00E83401448FD6801E512A900C33FF2C4C112D49AAD86`.
- `docs/assets/027_doctrine_research/processed_png/source_layers/027_doctrine_research_joint_curriculum_grey.png` — SHA-256 `5F8F944396B8D9F522240F30125426D6C3999D21D9461DAB64CA555497290B6A`.
- `docs/assets/027_doctrine_research/processed_png/source_layers/027_doctrine_research_joint_curriculum_not_eligible.png` — SHA-256 `35FAE2B153DAEF91029EF5B3DFD85EAC64503172EDE5B6233A7940055779D69F`.

The base source layer was alpha-bounds fitted to a centered 52-pixel maximum width and 58-pixel maximum height with Lanczos resampling.

The grey layer is grayscale state treatment retaining the generated alpha.

The not-eligible layer is the grey state treatment composited with the unchanged canonical `overlay.png` red X.

The unchanged workflow inputs are `achievement_template.png`, `achievement_template_grey.png`, and `overlay.png` under the canonical reference folder.

### Composited review PNGs

These are the processor's decoded, template-composited review PNGs and are all exact 64x64 RGBA.

- `docs/assets/027_doctrine_research/processed_png/review/027_doctrine_research_first_lesson.png` — SHA-256 `3F3E292CBA7102BFBA2687B3F51CDCF38E92F36569EB7765325F661A3E33D7D5`.
- `docs/assets/027_doctrine_research/processed_png/review/027_doctrine_research_first_lesson_grey.png` — SHA-256 `D0FC6A70CEF03C7C73DABDD6712A2AC34A2E54A93B77C69DD4BA63FA15E09556`.
- `docs/assets/027_doctrine_research/processed_png/review/027_doctrine_research_first_lesson_not_eligible.png` — SHA-256 `5A98F0A92CC054D465317AFA1DF5130EFC5D6327F828CC7A29013AE77D1A0264`.
- `docs/assets/027_doctrine_research/processed_png/review/027_doctrine_research_single_school.png` — SHA-256 `2CB1F052C711D072635F4FA4C953900F5190358D17C85CB4F4E2A3C17320B71F`.
- `docs/assets/027_doctrine_research/processed_png/review/027_doctrine_research_single_school_grey.png` — SHA-256 `30C9383A34010DB6BA1380496319715780B9AB17A8899B8C08CAB393344DC463`.
- `docs/assets/027_doctrine_research/processed_png/review/027_doctrine_research_single_school_not_eligible.png` — SHA-256 `14643F66FA1E3ECE769C6B539F5E4156DBFC966226F5F3B65953D7CB06A60CF9`.
- `docs/assets/027_doctrine_research/processed_png/review/027_doctrine_research_joint_curriculum.png` — SHA-256 `045491FE49E1660946FC0BD86CFBF828EC33FABC9AABE89C983C8CAC638720E6`.
- `docs/assets/027_doctrine_research/processed_png/review/027_doctrine_research_joint_curriculum_grey.png` — SHA-256 `1C8FE8F28E4CCABBA4AFE7162543170F661CB358CFC252443E6499244AB5819A`.
- `docs/assets/027_doctrine_research/processed_png/review/027_doctrine_research_joint_curriculum_not_eligible.png` — SHA-256 `AF216D3A2F1B965AF7E7B4E51694ABB79A7AD72859A1E928C7F54AFDDA000515`.

### Final runtime DDS files

All nine files are exact 64x64, 16,512-byte, one-level legacy uncompressed BGRA DDS files with a 128-byte header, 32-bit pixel format flags 65, canonical BGRA masks, texture caps `0x1000`, and alpha range 254..255.

- `gfx/achievements/027_doctrine_research_first_lesson.dds` — SHA-256 `E2AB92E0066439BC85DF6D2B3E6A913E0E5A8EBCAA629F3C0E9C46215FC084CE`.
- `gfx/achievements/027_doctrine_research_first_lesson_grey.dds` — SHA-256 `7105734156BDE4C93F685A50A79DF817CB1134C99A2323E2F30DD2848EABB79B`.
- `gfx/achievements/027_doctrine_research_first_lesson_not_eligible.dds` — SHA-256 `1701448BDF01D64DF3123C7ABFE9D3F42BC84F798F0C49A935377E45116B721E`.
- `gfx/achievements/027_doctrine_research_single_school.dds` — SHA-256 `CD88A460F6BF4D4A461D4FB885E2AE08043A63BCAB0F4098008B2E6B49D766C1`.
- `gfx/achievements/027_doctrine_research_single_school_grey.dds` — SHA-256 `30D4637C8BEC116107C066BFD02C52FC764CD8D0F2FFCEF0BE08B725DF953C6F`.
- `gfx/achievements/027_doctrine_research_single_school_not_eligible.dds` — SHA-256 `33F9EBDE47D8394C2377815335D4E5575BE094A268B3866CAA0692285FEFB492`.
- `gfx/achievements/027_doctrine_research_joint_curriculum.dds` — SHA-256 `4EE3F0F20D0C716418450539D400412475977F41BED1A8C0D8F913E59DC4240F`.
- `gfx/achievements/027_doctrine_research_joint_curriculum_grey.dds` — SHA-256 `D80F96BE8D87290436B5B71CC7A811DACBFEF020C77A956418203009D7FF46AB`.
- `gfx/achievements/027_doctrine_research_joint_curriculum_not_eligible.dds` — SHA-256 `E4628A234F03D49C8D96A9C0DE6231FEEBE6B774625514FA7B06F8E14E15A2C9`.

### Contact sheet and package documentation

- `docs/assets/027_doctrine_research/contact_sheets/027_doctrine_research_achievement_icons_contact_sheet.png` — 1652x1097 review-only contact sheet, SHA-256 `5CB84043D848ACC4AECB0ACB47355079E9ADC2B87919844D9651AD7BF98DA272`.
- `docs/assets/027_doctrine_research/prompts/achievement_icon_prompts.md`.
- `docs/assets/027_doctrine_research/manifest.md`.
- `docs/assets/027_doctrine_research/gfx_handoff.md`.

## Validation

- The canonical `process_achievement_icons.py --audit` pass succeeded for all three triplets and verified strict 64x64 BGRA output equality against the supplied-template compositing contract.
- Header, length, dimensions, pixel-format masks, caps, and alpha-range checks succeeded for all nine final DDS files.
- The contact sheet was visually reviewed with enlarged smooth panels and a separate native-size triplet strip.
- No fallback background removal was used because native ImageGen transparency validated on all three masters and source layers.

## Parent-owned follow-up

The parent must add the nine sprite aliases to `interface/chaosx_achievements.gfx` and confirm the final achievement registry IDs and consumers.

No GFX, gameplay, localisation, GUI, or spreadsheet file was edited by this worker.

## Blockers

No art-production blocker remains.

GFX registration is intentionally pending and is not an asset-production blocker because the user explicitly prohibited GFX edits.
