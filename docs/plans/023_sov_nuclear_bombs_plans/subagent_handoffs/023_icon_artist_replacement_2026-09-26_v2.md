# Event 023 achievement icon replacement candidate handoff — v2

Date: 2026-09-26.

Disposition: three fresh v2 triplets are generated, staged, and processor-audited. All remain `needs_user_review`; none is promoted to runtime. No commit was created.

## Scope and lineage

This v2 pass covers exactly `023_sov_nuclear_bombs_a_hundred_suns`, `023_sov_nuclear_bombs_the_bomb_never_fell`, and `023_sov_nuclear_bombs_first_and_last`. The parent’s visual review found that the v1 A Hundred Suns subject included a red star, The Bomb Never Fell showed a bomb in the cradle, and First and Last did not have a discernible cloud reflection at 64x64. The user authorized fresh source generations for those three IDs.

The original `docs/assets/023_sov_nuclear_bombs/prompts/icon_prompt_set.md` remains absent from the checkout and Git history. No original prompt was recovered or reconstructed. The v1 replacement prompt file remains byte-identical at SHA-256 `1f0d9ca04a05b7b4396b05299a1eb847b5f598471ee853491c0731b7461eb16a`. The v1 source PNGs, triplets, candidate DDS, review sheets, and rejected edit branches were not overwritten or deleted. The exact additional v2 prompts are recorded separately in `docs/assets/023_sov_nuclear_bombs/prompts/icon_prompt_set_replacement_2026-09-26_v2.md`, SHA-256 `7f96fe933c8027401ae5193f8459e01d67ef94f9f00bf84db0b44e97d6645bb5`.

Each v2 source is one fresh built-in ImageGen call with genuine transparency requested in the initial prompt. No old source was supplied as an edit target, and no edit calls were made. The three fresh subjects are labeled `GEN-08`, `GEN-09`, and `GEN-10` in the v2 lineage contact sheet.

## Fresh source paths, ImageGen output paths, and alpha

All three retained masters are 1254x1254 RGBA PNGs with alpha extrema 0..255 and actual zero-alpha pixels. Visible bounds use `alpha > 8` and `[left, top, right, bottom)` coordinates.

| Candidate | Tool-reported ImageGen output path | Retained source path | SHA-256 | Native visible bounds |
| --- | --- | --- | --- | --- |
| `GEN-08` — `023_sov_nuclear_bombs_a_hundred_suns` | `C:\Users\klimp\.codex\generated_images\01a0dc8d-e110-7c02-9946-ce907803a652\exec-b7dc187b-4ee6-46b6-8afe-da3a46f48ffd.png` | `docs/assets/023_sov_nuclear_bombs/source_png/achievements/replacement_2026-09-26_v2/023_sov_nuclear_bombs_a_hundred_suns_native_source.png` | `c8cfcd258de4f60c2cb2a9d9826d79b0c2343cbc13b4750d4bff080f1859bccf` | `[92,84,1169,1180)` |
| `GEN-09` — `023_sov_nuclear_bombs_the_bomb_never_fell` | `C:\Users\klimp\.codex\generated_images\01a0dc8d-e110-7c02-9946-ce907803a652\exec-50b8c0d9-356e-4ec5-b119-9608656643e0.png` | `docs/assets/023_sov_nuclear_bombs/source_png/achievements/replacement_2026-09-26_v2/023_sov_nuclear_bombs_the_bomb_never_fell_native_source.png` | `99d5c6bdd4749497dca4f3c71abcf67649bef1b98b2414707d2e21ac6600f07b` | `[35,121,1240,1132)` |
| `GEN-10` — `023_sov_nuclear_bombs_first_and_last` | `C:\Users\klimp\.codex\generated_images\01a0dc8d-e110-7c02-9946-ce907803a652\exec-219cc1ce-3b2f-4a51-8935-861c8853c808.png` | `docs/assets/023_sov_nuclear_bombs/source_png/achievements/replacement_2026-09-26_v2/023_sov_nuclear_bombs_first_and_last_native_source.png` | `d9dcb6b896b5a3f7436dc1f6a72752d8df7e54876c3d3f6d696314beb5d82ef0` | `[74,88,1219,1146)` |

At full source size the cabinet has no symbol or insignia, the cradle is visibly empty with no munition present, and the single pale cloud shape appears within the polished wrench jaw only. The cloud reflection remains discernible in the 64x64 triplet review. These are candidate observations, not parent approval.

## Immutable achievement template inputs

The canonical templates and overlay remain 64x64 and byte-identical to the required SHA-256 values:

| Input | Canonical path | SHA-256 |
| --- | --- | --- |
| Completed background | `.agents/skills/chaos-redux-event-assets/assets/gfx_references/icons/achievements/template/achievement_template.png` | `248DB006611EB3942550C43DF83802AA6FB24761035FC928B5D34586C0C4C5BA` |
| Grey/not-eligible background | `.agents/skills/chaos-redux-event-assets/assets/gfx_references/icons/achievements/template/achievement_template_grey.png` | `70E073694C1A7D9FE40C63B1EB2E987A8A45B3FFD15FC789EEAA5B843B90022` |
| Not-eligible overlay | `.agents/skills/chaos-redux-event-assets/assets/gfx_references/icons/achievements/template/overlay.png` | `89BC80C6AC975BF6F1FF000FF3070B20C337BFB8B8AE966AE35A5540C004D6DD` |

Each source was smoothly contained with LANCZOS within a centered 62x62 maximum on a transparent 64x64 RGBA canvas. Grey was deterministically derived from the v2 color subject with canvas, position, and alpha preserved. Not-eligible source layers use the unchanged canonical overlay composited above the grey source. No background-removal fallback was used.

## Canonical processor commands and audit

The exact processor pattern, run from the mod root, was:

```powershell
$ids = @(
  '023_sov_nuclear_bombs_a_hundred_suns',
  '023_sov_nuclear_bombs_the_bomb_never_fell',
  '023_sov_nuclear_bombs_first_and_last'
)
$triplets = 'docs/assets/023_sov_nuclear_bombs/processed_png/achievements/replacement_2026-09-26_v2/source_triplets'
$out = 'docs/assets/023_sov_nuclear_bombs/dds_candidates/achievements/replacement_2026-09-26_v2'
foreach ($id in $ids) {
  python -B .agents/skills/chaos-redux-event-assets/tools/process_achievement_icons.py `
    --completed "$triplets/$id.png" `
    --grey "$triplets/$($id)_grey.png" `
    --not-eligible "$triplets/$($id)_not_eligible.png" `
    --achievement-id $id `
    --output-dir $out `
    --write-png
}
python -B .agents/skills/chaos-redux-event-assets/tools/process_achievement_icons.py `
  --audit `
  --input $triplets `
  --output-dir $out
```

All three `--audit` runs returned `AUDIT OK`, confirming strict 64x64 BGRA triplets and source-layer equality. The retained stdout is `docs/assets/023_sov_nuclear_bombs/notes/achievement_replacement_2026-09-26_v2/processor_output.log`, SHA-256 `6f491261b58984825d773a48680def1caa5644ccb41385c3cd301ef8605fe7c5`.

Independent pixel verification confirmed exact grayscale derivation, exact unchanged overlay compositing, and for all nine states equality between `alpha_composite(canonical_template, source_layer)`, the processor review PNG, and the Pillow-decoded candidate DDS. The DDS files are 64x64, 16,512 bytes, and have alpha extrema 254..255 from the canonical achievement backgrounds.

## V2 triplet-input hashes

The files are under `docs/assets/023_sov_nuclear_bombs/processed_png/achievements/replacement_2026-09-26_v2/source_triplets/`. SHA-256 values are listed color / grey / not-eligible.

| Achievement ID | Color source layer | Grey source layer | Not-eligible source layer |
| --- | --- | --- | --- |
| `023_sov_nuclear_bombs_a_hundred_suns` | `023_sov_nuclear_bombs_a_hundred_suns.png` — `952cf92b538d9a3d87399ca454fcdc140bd70ba0d2aa9a4251c31958d3376228` | `023_sov_nuclear_bombs_a_hundred_suns_grey.png` — `52b736a38ab53ce319310c593eb738d1bd6dbdafbd1dee078f00605ca55697c0` | `023_sov_nuclear_bombs_a_hundred_suns_not_eligible.png` — `1353eb5f261e8f8076beff85560d813cf730741be03184d0c2ab1b0c9e81efbf` |
| `023_sov_nuclear_bombs_the_bomb_never_fell` | `023_sov_nuclear_bombs_the_bomb_never_fell.png` — `be5d1acce72808f2632e012659f9a7264d9dc1ad6e68a984dc36a2890f6ab3bb` | `023_sov_nuclear_bombs_the_bomb_never_fell_grey.png` — `e50192ff7e9e61a0dd3bf6dc46d69eaee73b115836314eed606fe65d64f8144b` | `023_sov_nuclear_bombs_the_bomb_never_fell_not_eligible.png` — `1f1c561cc2f55d97d34dba18e18b382811c61bec3f1b9bfaca250ffe1c0e32ff` |
| `023_sov_nuclear_bombs_first_and_last` | `023_sov_nuclear_bombs_first_and_last.png` — `211bd5f20d8ee11841443a21452ba857f7176fff608818b7ef47632549a2b655` | `023_sov_nuclear_bombs_first_and_last_grey.png` — `c2b1b3829cba5cfc4a7823c85fd65e0b9545fa44a87883f2b8bc56b42670ea25` | `023_sov_nuclear_bombs_first_and_last_not_eligible.png` — `794086b75a2a878ac20aa651142e847da6e6e1aaaf7e7405a2881dbdd54b261f` |

## V2 processed PNG and DDS hashes

The processed review PNGs are under `docs/assets/023_sov_nuclear_bombs/dds_candidates/achievements/replacement_2026-09-26_v2/review/`. The DDS candidates are directly under `docs/assets/023_sov_nuclear_bombs/dds_candidates/achievements/replacement_2026-09-26_v2/`. Values in each row are color / grey / not-eligible.

| Achievement ID | Processed review PNG hashes | Candidate DDS hashes |
| --- | --- | --- |
| `023_sov_nuclear_bombs_a_hundred_suns` | `023_sov_nuclear_bombs_a_hundred_suns.png` `e50a4ae868614b34d1a95685720f498c4c3e7e71aacc04bf0797fc30f8b2774b`; `023_sov_nuclear_bombs_a_hundred_suns_grey.png` `ca4eb270e02fc29c28ae4d3b18b66402e618bcbf61675f6c58d6677a0e524b2b`; `023_sov_nuclear_bombs_a_hundred_suns_not_eligible.png` `6effd9d6ffe5ae49d28acda4137d93bbcb5718c2430316f421ba866b13e048ab` | `023_sov_nuclear_bombs_a_hundred_suns.dds` `a13a5635246279fca5258dbd677b22a3290e47d3024660590a759b670f7af3aa`; `023_sov_nuclear_bombs_a_hundred_suns_grey.dds` `3314797ebe370f95b036a6bfa151f78dd7cbda14443601ac93117682a3c7d5d1`; `023_sov_nuclear_bombs_a_hundred_suns_not_eligible.dds` `9afcba785fe96a703ffa34a626b8091d0a736d19b954ccf4b4cf3ccbc64d4d3a` |
| `023_sov_nuclear_bombs_the_bomb_never_fell` | `023_sov_nuclear_bombs_the_bomb_never_fell.png` `821eac9a9281a797619e53731581144aed74d6a1402e607d80f7a27d00976bbf`; `023_sov_nuclear_bombs_the_bomb_never_fell_grey.png` `a2467980c976174507c723385815a4f44d4bc8f4537df723bd1a368d74537334`; `023_sov_nuclear_bombs_the_bomb_never_fell_not_eligible.png` `41c8141c8c14a930758f187e35d8b20eacf987569d19537617c3d685e23dccf6` | `023_sov_nuclear_bombs_the_bomb_never_fell.dds` `7e0e5d39b369be3ba2ce4c3b2267bb8807e6367627cfadba38820d5c26633fed`; `023_sov_nuclear_bombs_the_bomb_never_fell_grey.dds` `43d8597ee4ad65ccf1f5a2a5f1b0b50779463f694290745d83580205f7c07b95`; `023_sov_nuclear_bombs_the_bomb_never_fell_not_eligible.dds` `bc958219a0d3a0f4e6d4fcf6e13dfdbf4b3a90d1babf5ea0b5bd835e343d9c6e` |
| `023_sov_nuclear_bombs_first_and_last` | `023_sov_nuclear_bombs_first_and_last.png` `f90f9ebfcd0d1d25a8bf1be8114b978d6de127337736e30d875f4eefd3108bc6`; `023_sov_nuclear_bombs_first_and_last_grey.png` `ef0906518d57decd3fd6968a099f6cfcdc40c78e4f07c3b2299a31a80253179e`; `023_sov_nuclear_bombs_first_and_last_not_eligible.png` `97477cef48d1e7e8a07a3f045b764edfaf11d9e1dd014cab124d3045a206e4c3` | `023_sov_nuclear_bombs_first_and_last.dds` `d171832c24222f5c363541eebc98a0f764ca8acbaff257b23106a31f6417e786`; `023_sov_nuclear_bombs_first_and_last_grey.dds` `e48ae89f03a47c3099962ed0b4801b018abdd88668ebdc00bcf4fe2f1a2242de`; `023_sov_nuclear_bombs_first_and_last_not_eligible.dds` `3467ee5ee33493a8f8c0f30c37937018858a138381d9730d6edb5f4ce9789260` |

## V2 contact sheets and consumer crosswalk

| Sheet | Path | SHA-256 |
| --- | --- | --- |
| Native 64x64 triplets | `docs/assets/023_sov_nuclear_bombs/contact_sheets/achievement_replacement_2026-09-26_v2/v2_native_triplets.png` | `42889d2c1bded3fc4dff64325b9821721c9c7f8342100a57e62accaaee85be4c` |
| 4x nearest-neighbour triplets | `docs/assets/023_sov_nuclear_bombs/contact_sheets/achievement_replacement_2026-09-26_v2/v2_4x_nearest.png` | `9b9a22fe80dbe1cd8a45ce2ddc697a08c69c1bc92a6d19f3e6240d8d9f8291c7` |
| Native-alpha source, smooth preview, and DDS decode | `docs/assets/023_sov_nuclear_bombs/contact_sheets/achievement_replacement_2026-09-26_v2/v2_pipeline_alpha_roundtrip.png` | `3b7aa6530745e1121c98ce88c9885e12e258cc572d910a5a96a94cd6cde3c1c5` |
| V1-to-v2 source lineage | `docs/assets/023_sov_nuclear_bombs/contact_sheets/achievement_replacement_2026-09-26_v2/v2_source_lineage.png` | `a82d5f4586361090279ecd3fa959c3b325bd5e1a392b6db2c0be4eca8dde98ac` |

The v2 requirement-to-runtime crosswalk is appended at `docs/assets/023_sov_nuclear_bombs/notes/achievement_requirement_runtime_crosswalk_replacement_2026-09-26.md` and is also retained as `docs/assets/023_sov_nuclear_bombs/notes/achievement_requirement_runtime_crosswalk_replacement_2026-09-26_v2.md`. The stable IDs, aliases, root-level runtime targets, achievement definitions, and localization remain unchanged. All v2 rows are `needs_user_review`; the parent owns final visual selection and any later runtime promotion.

No live HOI4 consumer validation was run. No runtime GFX, GUI, DDS, registry, localization, gameplay, workbook, CSV, or ID was edited. The v1 handoff and all v1 candidate files remain at their original paths. No commit was created.

The repository ignores `docs/assets/` at `.gitignore:80`, so the v2 sources, prompt supplement, processed layers, contact sheets, DDS candidates, manifest append, and crosswalk append are present in the shared workspace but do not appear as tracked Git changes. Nothing was force-added. The current `common/achievements/chaos_redux_achievements.txt` worktree diff contains Event 042 additions and no Event 023 changes; this pass did not edit it.
