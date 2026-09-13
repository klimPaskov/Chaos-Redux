# Event 35 idea readability repair handoff

## Result

Repaired only `legacy_public_works` and `post_depression_recovery` for the installed vanilla national-spirit consumer at exactly 60x68.

Both replacements are source-specific Event 35 ImageGen edits with genuine transparent runtime corners after the documented fallback transparency process.

The two assets are `ready_for_parent_review` and remain pending the parent-owned live national-spirit surface review; no GFX or gameplay wiring change is required.

## Consumer and canonical references

The consumer is the installed vanilla `interface/countrydiplomacyview.gui` block `national_spirit_ideas_grid`, with `slotsize = { width = 60 height = 68 }`.

The matching canonical reference family inspected before generation was `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/ideas`, starting with `contact_sheet.png` and then the individual idea references `generic_wall_line.png`, `idea_generic_constitutional_guarantee.png`, `idea_den_danish_produce.png`, and `idea_generic_flexible_foreign_policy.png`.

The existing stable sprites and runtime texture paths remain unchanged in `interface/035_great_depression.gfx`.

## Source and processing provenance

Each existing source master was copied unchanged to `docs/assets/035_great_depression/audit/idea_canvas_repair/original_source_masters/` before replacement.

ImageGen was used once per requested icon with the corresponding existing source as the edit target and a genuine transparent background requested in the initial call.

The bridge initial ImageGen output and its targeted transparency-edit output both returned opaque RGB checkerboards, so the verified local `rembg` fallback was used with `alpha_matting=False`; the opaque outputs and fallback cutout are retained under `docs/assets/035_great_depression/audit/idea_canvas_repair/generation_evidence/`.

The recovery initial ImageGen output returned an opaque RGB checkerboard, so the verified local `rembg` fallback was used with `alpha_matting=False`; its opaque output and fallback cutout are retained under `docs/assets/035_great_depression/audit/idea_canvas_repair/generation_evidence/`.

The exact ImageGen prompts and fallback notes are recorded in `docs/assets/035_great_depression/audit/idea_canvas_repair/generation_evidence/imagegen_prompts.md`.

The processed previews use the existing Event 35 fit convention: alpha greater than 8 bounds with a two-source-pixel edge guard, aspect-preserving premultiplied-alpha Lanczos fitting into a centered 56x64 inner box on a transparent 60x68 canvas.

## Runtime inventory and hashes

All hashes below are SHA-256 in uppercase hexadecimal.

| Asset | Source master | Processed PNG | Runtime DDS | Decoded DDS |
|---|---|---|---|---|
| `legacy_public_works` | `docs/assets/035_great_depression/source/conditions/idea_035_great_depression_legacy_public_works.png`, 1181x1331, 1,562,635 bytes, `8649CFF91B72A5B97754B5D06408DC023433BCEF007C880FE22C235B9FE87D7F` | `docs/assets/035_great_depression/processed/conditions/idea_035_great_depression_legacy_public_works.png`, 60x68, 6,409 bytes, bounds `[2,4,58,64]`, `69A7E3DA3EB427A28F4624F67E08EEBAA07FE806350A057F59B1AF3AF32D1F29` | `gfx/interface/ideas/035_great_depression/idea_035_great_depression_legacy_public_works.dds`, 60x68, 16,448 bytes, `57220E4EBD26AAD4D35F2E95392DE6A7ADF198F3A147ADB063F226FEDB1CF1E1` | `docs/assets/035_great_depression/audit/idea_canvas_repair/decoded_runtime_dds/idea_035_great_depression_legacy_public_works.png`, 60x68, 6,409 bytes, `69A7E3DA3EB427A28F4624F67E08EEBAA07FE806350A057F59B1AF3AF32D1F29` |
| `post_depression_recovery` | `docs/assets/035_great_depression/source/conditions/idea_035_great_depression_post_depression_recovery.png`, 1180x1333, 1,790,114 bytes, `4034795C8F6F3E73185DFB0BAE766E344720506D2D8C29AB14901E2AC4C3ADFE` | `docs/assets/035_great_depression/processed/conditions/idea_035_great_depression_post_depression_recovery.png`, 60x68, 7,817 bytes, bounds `[2,4,58,63]`, `5466796483FB824C2329DC3C8810003A297BBDE9FA7835D9C435695F7EC6DD69` | `gfx/interface/ideas/035_great_depression/idea_035_great_depression_post_depression_recovery.dds`, 60x68, 16,448 bytes, `6DAB01CE77134F98005B2AB122982AA6752D9083E48D0EC02664DE2FCB3DE038` | `docs/assets/035_great_depression/audit/idea_canvas_repair/decoded_runtime_dds/idea_035_great_depression_post_depression_recovery.png`, 60x68, 7,817 bytes, `5466796483FB824C2329DC3C8810003A297BBDE9FA7835D9C435695F7EC6DD69` |

The replacement source alpha ranges are 0-255 and the processed/runtime decoded corners are `[0,0,0,0]` for both icons.

The source alpha-greater-than-8 bounds are `[15,35,1173,1267]` for `legacy_public_works` and `[35,111,1159,1286]` for `post_depression_recovery`.

The previous source-master hashes were `7F33636273609F0C68045D3DAC73635A32FE4F6BEEF64D54186A7D75D2C1F368` and `FDA8B22F44695BACB064CF4B4C1ABB3B07F711C09EA61813F6E86C68FB34F976` and remain available under `original_source_masters/`.

The previous processed 60x68 hashes were `12651F0E126BAF1F31D410239F028B1E10D75CA63056C53B0167B5166041B99E` and `1E9DFB7227553453A3343361BA22B585D5049ED3404C1AFBDDB3C19ED88EC3CC` and remain available under `previous_processed_60x68/`.

The previous runtime DDS hashes were `A478BF1699221873FA35C32D730B22BD4D7422F209464BEBA19F32134DD1CBBE` and `5309222FFFB5BBF7F8F1AD6B3C3C6C83ADFA2E9FD4CAE8349191B50A7086E89D` and remain available under `previous_runtime_dds/`.

## Readability evidence

The bridge replacement raises native visible-content luma mean/p95 from `29.66/89.08` to `61.55/134.92` and increases pixels above luma 120 from `5` to `204`.

The recovery replacement changes alpha-greater-than-8 visible bounds from `[2,27,57,45]` to `[2,4,58,63]`, giving the workers full visible height and a larger locomotive silhouette.

The refreshed review sheets are `docs/assets/035_great_depression/audit/idea_canvas_repair/native_contact_sheet.png`, `enlarged_review_sheet.png`, and `contrast_review_sheet.png`.

The native processed previews and decoded DDS round-trips were inspected individually and as paired columns over checkerboard, dark solid, and light solid backgrounds.

## Exact validation

The standard conversion command was run separately for each processed PNG using `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` with `--width 60 --height 68`.

The existing validator was run against the final runtime folder with `CR_IDEA_REPAIR_DDS_DIR` pointed at `gfx/interface/ideas/035_great_depression`, `CR_IDEA_REPAIR_DECODED_DIR` pointed at `docs/assets/035_great_depression/audit/idea_canvas_repair/decoded_runtime_dds`, and `CR_IDEA_REPAIR_REPORT_PATH` pointed at `docs/assets/035_great_depression/audit/idea_canvas_repair/post_promotion_validation.json`.

The validator returned `count: 12`, `all_technical_pass: true`, `all_gfx_texture_paths_present: true`, and no missing texture paths.

Both repaired DDS headers are strict one-level legacy BGRA: magic `DDS `, header size `124`, flags `4111`, width `60`, height `68`, pitch `240`, mip count `0`, pixel format `(32,65,0,32,16711680,65280,255,4278190080)`, caps `4096`, and caps2 through caps5 `0`.

Both processed PNGs and decoded DDS PNGs are byte-identical after round trip, with matching alpha ranges and exact 16,448-byte DDS lengths.

## Changed files

Runtime/source/processed files changed only for these two icons:

- `docs/assets/035_great_depression/source/conditions/idea_035_great_depression_legacy_public_works.png`
- `docs/assets/035_great_depression/source/conditions/idea_035_great_depression_post_depression_recovery.png`
- `docs/assets/035_great_depression/processed/conditions/idea_035_great_depression_legacy_public_works.png`
- `docs/assets/035_great_depression/processed/conditions/idea_035_great_depression_post_depression_recovery.png`
- `gfx/interface/ideas/035_great_depression/idea_035_great_depression_legacy_public_works.dds`
- `gfx/interface/ideas/035_great_depression/idea_035_great_depression_post_depression_recovery.dds`

Scoped evidence and documentation updated or added under Event 35 include the refreshed contact sheets, decoded DDS previews, `post_promotion_validation.json`, `visual_review.md`, `icon_manifest.json`, `icon_manifest.md`, preserved prior candidates and sources, generation evidence, `generation_evidence/imagegen_prompts.md`, and this handoff.

No gameplay, GFX, GUI, localisation, workbook, event, or unrelated file was edited by this repair.

## Remaining risks and review state

The native ImageGen transparency request failed for both assets and the bridge's targeted transparency edit also failed, so both final source masters depend on the recorded local `rembg` fallback; this is not a hidden or unrecorded background-removal step.

The fallback output retains a dark painted outline and subtle shadow as part of the icon subject, but native and contrasting-background review showed no checkerboard, opaque square, clipped visible edge, coloured spill, or unintended transparent hole at the processed runtime size.

The parent must perform the final live `national_spirit_ideas_grid` review; the worker does not claim in-game acceptance.

Skills used: `chaos-redux-event-assets` and the official `imagegen` skill.
