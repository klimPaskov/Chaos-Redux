# Event 023 achievement icon replacement candidate handoff

Date: 2026-09-26.

Disposition: seven replacement candidate triplets are staged and processor-audited; all seven remain `needs_user_review`. No candidate was promoted, and no commit was created.

## Authorization and provenance boundary

The previously referenced `docs/assets/023_sov_nuclear_bombs/prompts/icon_prompt_set.md` was absent from the checkout and `git log --all -- docs/assets/023_sov_nuclear_bombs/prompts/icon_prompt_set.md` returned no history. The user explicitly authorized new prompts and replacement candidates after that absence was confirmed. No original prompt was recovered, inferred, reconstructed, or claimed.

The exact new prompts are recorded verbatim in `docs/assets/023_sov_nuclear_bombs/prompts/icon_prompt_set_replacement_2026-09-26.md`. Seven separate built-in ImageGen generation calls created one original transparent subject per stable achievement ID. Four focused edit calls were also retained as candidate lineage: two edits for A Hundred Suns, one for Scattered Arsenal, and one for Firebreak. No CLI/API path was used. Each original and edit request asked ImageGen for genuine transparency at the time of generation.

The canonical reference family was inspected from its required contact sheet first, followed by `30_minutes_of_hel.png`, `britzkrieg.png`, `crusader_kings_2.png`, and `the_revolution_triumphant.png` under `.agents/skills/chaos-redux-event-assets/assets/gfx_references/icons/achievements/`. The three immutable template inputs were inspected at their exact canonical paths. The current Event 023 achievement sheets `achievement_source_recovery_contact_sheet.png`, `achievement_package_runtime_dds_contact_sheet.png`, and `achievement_full_chain_contact_sheet.png` were viewed as context only; none was supplied to ImageGen or copied into candidate art.

## Source lineage and native PNG evidence

All paths below are relative to the mod root unless a full ImageGen output path is shown. Every retained source is a 1254x1254 RGBA PNG. Native source alpha extrema are 0..255, with genuine zero-alpha pixels. The visible-bound values use `alpha > 8` and `[left, top, right, bottom)` coordinates. ImageGen tool outputs were copied into the versioned source directory without changing their bytes; the original tool outputs were left in place.

ImageGen output directory reported by the tool: `C:\Users\klimp\.codex\generated_images\01a0dc8d-e110-7c02-9946-ce907803a652\`.

| Achievement / lineage | Tool-reported output path | Retained source path | SHA-256 | Candidate use and source alpha visible bounds |
| --- | --- | --- | --- | --- |
| `023_sov_nuclear_bombs_a_hundred_suns`, `GEN-01` | `C:\Users\klimp\.codex\generated_images\01a0dc8d-e110-7c02-9946-ce907803a652\exec-6d4fb3d3-1769-4dc1-a87c-f8acf05aa371.png` | `docs/assets/023_sov_nuclear_bombs/source_png/achievements/replacement_2026-09-26/023_sov_nuclear_bombs_a_hundred_suns_native_source.png` | `f41b86389147744de7ca50aebd51a9174f123ea86b03afa7077a361a156c5bf9` | Selected for staging; bounds `[61,71,1199,1174)`. A red Soviet star appeared despite not being requested. |
| `023_sov_nuclear_bombs_a_hundred_suns`, `EDIT-01` | `C:\Users\klimp\.codex\generated_images\01a0dc8d-e110-7c02-9946-ce907803a652\exec-7271822c-8488-43af-9df5-e6f21c9585f9.png` | `docs/assets/023_sov_nuclear_bombs/source_png/achievements/replacement_2026-09-26/023_sov_nuclear_bombs_a_hundred_suns_candidate_v2_edit.png` | `7386ec0e1c66628ec355744af9ac9dc5a050fe0080563ef4a887be4419444587` | Rejected edit branch; improved padding but did not remove the star. |
| `023_sov_nuclear_bombs_a_hundred_suns`, `EDIT-02` | `C:\Users\klimp\.codex\generated_images\01a0dc8d-e110-7c02-9946-ce907803a652\exec-b9e9abf1-af1d-4fbc-b6ba-4ed45a89a2cf.png` | `docs/assets/023_sov_nuclear_bombs/source_png/achievements/replacement_2026-09-26/023_sov_nuclear_bombs_a_hundred_suns_candidate_v3_edit.png` | `d9e4ae38434c05285ed3b6bcd164b7317f1100d02de1c44ca6397b59951f1f89` | Rejected edit branch; the requested star removal still did not occur. The original generation remains the staged source pending parent review. |
| `023_sov_nuclear_bombs_the_bomb_never_fell`, `GEN-02` | `C:\Users\klimp\.codex\generated_images\01a0dc8d-e110-7c02-9946-ce907803a652\exec-cc412e19-2707-4938-9305-4576402cf06a.png` | `docs/assets/023_sov_nuclear_bombs/source_png/achievements/replacement_2026-09-26/023_sov_nuclear_bombs_the_bomb_never_fell_native_source.png` | `9eb57d476045db484bffa1f78d466c883e6b20cbc5a788dbcd12c15859f93e48` | Selected for staging; bounds `[43,58,1223,1233)`. |
| `023_sov_nuclear_bombs_ultimatum_without_ash`, `GEN-03` | `C:\Users\klimp\.codex\generated_images\01a0dc8d-e110-7c02-9946-ce907803a652\exec-730fff84-7627-40da-a374-80840b194f89.png` | `docs/assets/023_sov_nuclear_bombs/source_png/achievements/replacement_2026-09-26/023_sov_nuclear_bombs_ultimatum_without_ash_native_source.png` | `7f728bd694f3f101465718beb40b82c02f9b4b762533590d25d128146af346d3` | Selected for staging; bounds `[40,200,1215,1043)`. |
| `023_sov_nuclear_bombs_scattered_arsenal`, `GEN-04` | `C:\Users\klimp\.codex\generated_images\01a0dc8d-e110-7c02-9946-ce907803a652\exec-10349320-c760-48ed-aae9-c9614a3279aa.png` | `docs/assets/023_sov_nuclear_bombs/source_png/achievements/replacement_2026-09-26/023_sov_nuclear_bombs_scattered_arsenal_native_source.png` | `7a1a17e19751ff29db97944bdf6abf2e9d94514fbdc87df5774deea2f0595f6f` | Retained parent candidate; initial rail yard was too crowded at icon size. |
| `023_sov_nuclear_bombs_scattered_arsenal`, `EDIT-04A` | `C:\Users\klimp\.codex\generated_images\01a0dc8d-e110-7c02-9946-ce907803a652\exec-35fd07b7-bcf6-4507-aa3f-2b8564592638.png` | `docs/assets/023_sov_nuclear_bombs/source_png/achievements/replacement_2026-09-26/023_sov_nuclear_bombs_scattered_arsenal_candidate_v2_edit.png` | `7b79f931cb6f427dd24dbd8e91480546ee5a14a4bebf1f20459026f80ea42266` | Selected for staging; bounds `[20,148,1231,1115)`. The edit simplified the scene to one closed depot, converging rails, three crates, and one guard. |
| `023_sov_nuclear_bombs_firebreak`, `GEN-05` | `C:\Users\klimp\.codex\generated_images\01a0dc8d-e110-7c02-9946-ce907803a652\exec-0c56a99d-ba6d-4388-b5b1-2c2f3967900f.png` | `docs/assets/023_sov_nuclear_bombs/source_png/achievements/replacement_2026-09-26/023_sov_nuclear_bombs_firebreak_native_source.png` | `ec0d5d0035654ea8183c8635592d1435dafe6f5653ce3d66c17314ea78f00c79` | Retained parent candidate; its cable stayed severed and crossed the source edge. |
| `023_sov_nuclear_bombs_firebreak`, `EDIT-05A` | `C:\Users\klimp\.codex\generated_images\01a0dc8d-e110-7c02-9946-ce907803a652\exec-915fe30d-2608-42cd-a751-38c90cd648a0.png` | `docs/assets/023_sov_nuclear_bombs/source_png/achievements/replacement_2026-09-26/023_sov_nuclear_bombs_firebreak_candidate_v2_edit.png` | `5b5706d974f970e8dfe8d313a6de99c1107d3cf797e61bef3969a427a64871fa` | Selected for staging; bounds `[110,216,1209,1048)`. The splice is visible and the subject is inside the frame. |
| `023_sov_nuclear_bombs_first_and_last`, `GEN-06` | `C:\Users\klimp\.codex\generated_images\01a0dc8d-e110-7c02-9946-ce907803a652\exec-102beb06-a9ea-4acc-819b-7e20a3c54386.png` | `docs/assets/023_sov_nuclear_bombs/source_png/achievements/replacement_2026-09-26/023_sov_nuclear_bombs_first_and_last_native_source.png` | `424f0239757db57e15654d053f4ce747a861c44027258db5555bc6da1c5ea76b` | Selected for staging; bounds `[71,205,1232,1100)`. |
| `023_sov_nuclear_bombs_the_last_telephone`, `GEN-07` | `C:\Users\klimp\.codex\generated_images\01a0dc8d-e110-7c02-9946-ce907803a652\exec-b8cbc435-209d-453d-a058-84edd9a8b5e3.png` | `docs/assets/023_sov_nuclear_bombs/source_png/achievements/replacement_2026-09-26/023_sov_nuclear_bombs_the_last_telephone_native_source.png` | `4a2a47d4b8f0414e7b661adffcd5884b989ce0a6600eb89270b34838015167e3` | Selected for staging; bounds `[64,124,1182,1135)`. |

Prompt path: `docs/assets/023_sov_nuclear_bombs/prompts/icon_prompt_set_replacement_2026-09-26.md`; SHA-256 `1f0d9ca04a05b7b4396b05299a1eb847b5f598471ee853491c0731b7461eb16a`. It contains the exact seven generation prompts and every focused edit prompt. The SHA-256 of the retained candidate masters and rejected edit branches is listed above.

## Template integrity and processing

The immutable canonical 64x64 template files remained byte-identical before and after processing:

| Template input | Canonical path | SHA-256 |
| --- | --- | --- |
| Completed background | `.agents/skills/chaos-redux-event-assets/assets/gfx_references/icons/achievements/template/achievement_template.png` | `248DB006611EB3942550C43DF83802AA6FB24761035FC928B5D34586C0C4C5BA` |
| Grey/not-eligible background | `.agents/skills/chaos-redux-event-assets/assets/gfx_references/icons/achievements/template/achievement_template_grey.png` | `70E073694C1A7D9FE40C63B1EB2E987A8A45B3FFD15CCF789EEAA5B843B90022` |
| Red-cross overlay | `.agents/skills/chaos-redux-event-assets/assets/gfx_references/icons/achievements/template/overlay.png` | `89BC80C6AC975BF6F1FF000FF3070B20C337BFB8B8AE966AE35A5540C004D6DD` |

Each selected native source was smoothly contained with LANCZOS within a centered 62x62 maximum on a transparent 64x64 RGBA canvas, following the current Event 023 source-processing precedent. Grey inputs were computed from the color subject with canvas, position, and alpha preserved. Not-eligible inputs were built by compositing the unchanged canonical overlay above that grey layer. No three-state artwork was separately generated, no cross-family image was reused, and no background-removal fallback was used.

The exact processor command pattern run from the mod root was:

```powershell
$ids = @(
  '023_sov_nuclear_bombs_a_hundred_suns',
  '023_sov_nuclear_bombs_the_bomb_never_fell',
  '023_sov_nuclear_bombs_ultimatum_without_ash',
  '023_sov_nuclear_bombs_scattered_arsenal',
  '023_sov_nuclear_bombs_firebreak',
  '023_sov_nuclear_bombs_first_and_last',
  '023_sov_nuclear_bombs_the_last_telephone'
)
$triplets = 'docs/assets/023_sov_nuclear_bombs/processed_png/achievements/replacement_2026-09-26/source_triplets'
$out = 'docs/assets/023_sov_nuclear_bombs/dds_candidates/achievements/replacement_2026-09-26'
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

The processor wrote exactly 21 candidate DDS files and 21 composited review PNGs. The retained stdout is `docs/assets/023_sov_nuclear_bombs/notes/achievement_replacement_2026-09-26/processor_output.log`, SHA-256 `be36553ac9d3fec24da050b4e2178c4d0093995f3ea12a5b024a15184a29557c`. The final audit returned `AUDIT OK` for all seven IDs, confirming strict 64x64 BGRA triplets and source-layer equality.

The subject-source triplets under `docs/assets/023_sov_nuclear_bombs/processed_png/achievements/replacement_2026-09-26/source_triplets/` have these SHA-256 values, with state order color / grey / not-eligible:

| Achievement ID | Color input | Grey input | Not-eligible input |
| --- | --- | --- | --- |
| `023_sov_nuclear_bombs_a_hundred_suns` | `023_sov_nuclear_bombs_a_hundred_suns.png` — `faa0eea86673b6b133d82e97930a8ac1720977baa636a7725b736855e1cc16a7` | `023_sov_nuclear_bombs_a_hundred_suns_grey.png` — `1c49704cb5b2e6b39f948ac072d78065f4853e234c8d2eec5e2b254b356fd7e8` | `023_sov_nuclear_bombs_a_hundred_suns_not_eligible.png` — `dd2f521651daca51ccdc0330e39082adb40adf314f0f3e202b6977ca73cdc547` |
| `023_sov_nuclear_bombs_the_bomb_never_fell` | `023_sov_nuclear_bombs_the_bomb_never_fell.png` — `ffcc05e853aa0ced6359fe4cb407acb01a271f985d5cd9da3e67cc0aeb0220f0` | `023_sov_nuclear_bombs_the_bomb_never_fell_grey.png` — `602c62d9773f940130891f5447003f5a136a74749a47a3d04d2b807540c498d2` | `023_sov_nuclear_bombs_the_bomb_never_fell_not_eligible.png` — `215646601a21e2586837d15dca60acb2a5a3dd91758afc8b44fa8e43c63d67df` |
| `023_sov_nuclear_bombs_ultimatum_without_ash` | `023_sov_nuclear_bombs_ultimatum_without_ash.png` — `bbfc8ad98af2d8923f5c0ac8cc121ed349464776f363c15deb676e8de7e147c4` | `023_sov_nuclear_bombs_ultimatum_without_ash_grey.png` — `dc33f29cee2a9d12cffacae6daa02d01d64679eec4a6f95ed8aa489c98f69423` | `023_sov_nuclear_bombs_ultimatum_without_ash_not_eligible.png` — `367765ffe3189d90a359415d4321b09e2a994eb5f9feb97e8cc622bfaee03fc8` |
| `023_sov_nuclear_bombs_scattered_arsenal` | `023_sov_nuclear_bombs_scattered_arsenal.png` — `1b47b2346e31f49d7e364a09142f465c789d421d84f6ee5f30336df86fbf8030` | `023_sov_nuclear_bombs_scattered_arsenal_grey.png` — `540a2f4e91441d87e5ecd7cd158e4f6ea6b058400b495f90930af3cc474f2889` | `023_sov_nuclear_bombs_scattered_arsenal_not_eligible.png` — `fdee28332150c481122584bf48382a75b7fce9f5c29f38b4377588633b6629fd` |
| `023_sov_nuclear_bombs_firebreak` | `023_sov_nuclear_bombs_firebreak.png` — `9bcf9d562bd91cc1de940e0f52fbb0ac6eb3045fd3e96cc78f732045265d8705` | `023_sov_nuclear_bombs_firebreak_grey.png` — `61998c2f12d962fd08b74ca7cb67701a2dd8fc41906ceab0ae42098ab57a2d5a` | `023_sov_nuclear_bombs_firebreak_not_eligible.png` — `64ecaba454d6f34572a04dacfaa23b9d7f081c2bbe04adfc06e27b2c22fd9c3d` |
| `023_sov_nuclear_bombs_first_and_last` | `023_sov_nuclear_bombs_first_and_last.png` — `ee9b2978d6dbfb57b5900a21e5bd5844b18924a26057d73f36841a2b7c326424` | `023_sov_nuclear_bombs_first_and_last_grey.png` — `6ccc1daf0f61b17ba31dba1228b54cec5547eb799e9c5d029d2c8f79bae5b090` | `023_sov_nuclear_bombs_first_and_last_not_eligible.png` — `d9faa34ad317ec1695dc04f7b4f49782321c619b610d206137af40ef7565e893` |
| `023_sov_nuclear_bombs_the_last_telephone` | `023_sov_nuclear_bombs_the_last_telephone.png` — `edccec2a5d1f590b912690176aa56399cef6d7a55707ee718d512ab4e527a7a4` | `023_sov_nuclear_bombs_the_last_telephone_grey.png` — `282c2df640e7138200fb50714301df0554f582a78dfdc9dacf1f2b218f707c38` | `023_sov_nuclear_bombs_the_last_telephone_not_eligible.png` — `0e1ae6c03b766bd30b16d6d2281bbe2468458dd248c9b290b7ce57f792fdd484` |

The canonical processor review PNGs under `docs/assets/023_sov_nuclear_bombs/dds_candidates/achievements/replacement_2026-09-26/review/` have these SHA-256 values, in color / grey / not-eligible order:

| Achievement ID | Color review PNG | Grey review PNG | Not-eligible review PNG |
| --- | --- | --- | --- |
| `023_sov_nuclear_bombs_a_hundred_suns` | `023_sov_nuclear_bombs_a_hundred_suns.png` — `1eca62244b03da81c3f350745c5065e8002f60a6cbf7501a3812a0e516049f45` | `023_sov_nuclear_bombs_a_hundred_suns_grey.png` — `75b189088c8f8184a7f34b54928fa5072e4493d712a8ee28ca6e0b9b6008f382` | `023_sov_nuclear_bombs_a_hundred_suns_not_eligible.png` — `c0d40823c7addd1658f26097dad636d344eb95e35fd05455d798942c228ead24` |
| `023_sov_nuclear_bombs_the_bomb_never_fell` | `023_sov_nuclear_bombs_the_bomb_never_fell.png` — `f25b6df86615407649c9c8ac20f89c143099044d25c80aea45942e09faaa23e6` | `023_sov_nuclear_bombs_the_bomb_never_fell_grey.png` — `d3519f90a47b4758bb807e582f67133eb0d3ebd5f3589feb729c0e11aea2444c` | `023_sov_nuclear_bombs_the_bomb_never_fell_not_eligible.png` — `d14bf58a2698a8cda97c710be96ddd861a526d2b0e4c6d75bea3199b433f1eb2` |
| `023_sov_nuclear_bombs_ultimatum_without_ash` | `023_sov_nuclear_bombs_ultimatum_without_ash.png` — `8a296f81f22290d2cfed28ee0f1b443598c02fd2aa8061c2e111ec194428c629` | `023_sov_nuclear_bombs_ultimatum_without_ash_grey.png` — `1143737bc9a01f4d9f4c0b82e273fdc713830e531f4d84c5ff7b51335833549b` | `023_sov_nuclear_bombs_ultimatum_without_ash_not_eligible.png` — `4c4be388cf7ade8a7d69ad50a06b4be412f957bd1e8e545a29b719c4361da262` |
| `023_sov_nuclear_bombs_scattered_arsenal` | `023_sov_nuclear_bombs_scattered_arsenal.png` — `ddf63def8871c2fcb5d61d7409bbf8cd28d1a284dc83de0533d3627ad530b157` | `023_sov_nuclear_bombs_scattered_arsenal_grey.png` — `71014445e17b4d6ee3de63282acb9b8bcecde0952d8a8286bac2e9fd76fe9b02` | `023_sov_nuclear_bombs_scattered_arsenal_not_eligible.png` — `35f46f0c32b844c272e3bd78157e6fdf309822bfed60b0c47d24b4837ec4d4c0` |
| `023_sov_nuclear_bombs_firebreak` | `023_sov_nuclear_bombs_firebreak.png` — `2277bf85cbf0863bf43701830d2087426ee61d860c85dd244a0a18afadaef34c` | `023_sov_nuclear_bombs_firebreak_grey.png` — `58a1fcb50f1070b8baf9f4891993ac64ad2a7fcea28cc43385efcfe2bc803036` | `023_sov_nuclear_bombs_firebreak_not_eligible.png` — `51dd56c2351fa4d425b24cce281ad8d5ca1513eba28e14d3d8e04ce20303a6b0` |
| `023_sov_nuclear_bombs_first_and_last` | `023_sov_nuclear_bombs_first_and_last.png` — `deb3c31b30ef48d2d2cd5512ccfcb2d785806a9a7275aae840f3d4eb463cb5b9` | `023_sov_nuclear_bombs_first_and_last_grey.png` — `6bfc75eb5442edf3461516da0b9eb5d68fd473dfe4cdac2e2b64bed041965f37` | `023_sov_nuclear_bombs_first_and_last_not_eligible.png` — `c5702d263fd2f6424e1ed058f82ee83b4caa90e05e50f8a6a551aa8a77437e40` |
| `023_sov_nuclear_bombs_the_last_telephone` | `023_sov_nuclear_bombs_the_last_telephone.png` — `947f0670d1af866a4fedf480b03444c1cf8842e2811c2c23e9c42f6fe71105e5` | `023_sov_nuclear_bombs_the_last_telephone_grey.png` — `5580a4c60804cb6ec4654278615e7b867bc41d680c3b474830b8ca1d70eb34b9` | `023_sov_nuclear_bombs_the_last_telephone_not_eligible.png` — `9b512095fb98c57e16fc92a0c01236a58cff15acd37817722d7c19f4e0b95b8d` |

The candidate DDS files are directly under `docs/assets/023_sov_nuclear_bombs/dds_candidates/achievements/replacement_2026-09-26/`, with these SHA-256 values, in color / grey / not-eligible order:

| Achievement ID | Color candidate DDS | Grey candidate DDS | Not-eligible candidate DDS |
| --- | --- | --- | --- |
| `023_sov_nuclear_bombs_a_hundred_suns` | `023_sov_nuclear_bombs_a_hundred_suns.dds` — `9fb700ca57dc74ef365852603cd5931a9578200fc9e7c980fc0a3e6d4366fa71` | `023_sov_nuclear_bombs_a_hundred_suns_grey.dds` — `c96526d1d46060247957d3c3dbe96d77dbafc4a9292827adf43c60fc22ecb5b2` | `023_sov_nuclear_bombs_a_hundred_suns_not_eligible.dds` — `bb47aaa30ce3e367dfef2e4c2c8a7025bddc962aa0101bceade05fe7a591e77e` |
| `023_sov_nuclear_bombs_the_bomb_never_fell` | `023_sov_nuclear_bombs_the_bomb_never_fell.dds` — `c5911684da155acecbf35afca97e795d0266cbab4b968f1650de462860949b39` | `023_sov_nuclear_bombs_the_bomb_never_fell_grey.dds` — `dccafbd8fb7a72e799b1db9d3a3ab7ac006500df53d341db0012acb26def475e` | `023_sov_nuclear_bombs_the_bomb_never_fell_not_eligible.dds` — `545130e8d616f06997bb65d566b47c3e251d491de63372b797480c215f5bd7e7` |
| `023_sov_nuclear_bombs_ultimatum_without_ash` | `023_sov_nuclear_bombs_ultimatum_without_ash.dds` — `04b7fbcb68eaaefe601c2086291068785b0e56fc59944d0566f2468a5068dd6b` | `023_sov_nuclear_bombs_ultimatum_without_ash_grey.dds` — `560e355d088541160a2fae3895d96d49e3bace3e87a6a37405975e191c7f121c` | `023_sov_nuclear_bombs_ultimatum_without_ash_not_eligible.dds` — `299f29a66c530853ed98238c7cf092d16113ac53bec8f610701d51b89bf8327d` |
| `023_sov_nuclear_bombs_scattered_arsenal` | `023_sov_nuclear_bombs_scattered_arsenal.dds` — `f7a2d87b9602d48683ce2c9dcc88bb6507901ff4fd706d1434c2df1ad94eda51` | `023_sov_nuclear_bombs_scattered_arsenal_grey.dds` — `db1cb50b714b7d2c8cb51312370caded29067ef95bf4b55170fc95aebbce3352` | `023_sov_nuclear_bombs_scattered_arsenal_not_eligible.dds` — `a3131f5e7f02d5c240103ce5cd0e8699a4cf0d749959764e201719262fbbc433` |
| `023_sov_nuclear_bombs_firebreak` | `023_sov_nuclear_bombs_firebreak.dds` — `3c2551abc75b3a046b9e8f40c0782609f9f92b34dbcf4b761def73cab1fde449` | `023_sov_nuclear_bombs_firebreak_grey.dds` — `8ebce2006c5c2d4498b29fa887c97266e11a20f62646fdf0664253a9e4772e26` | `023_sov_nuclear_bombs_firebreak_not_eligible.dds` — `3d008cbe5da0bb2b732d76cee85c1fa76dc122e1ac2ba539f1076f7a46be1c0a` |
| `023_sov_nuclear_bombs_first_and_last` | `023_sov_nuclear_bombs_first_and_last.dds` — `1c8612e92c2c86dd3a626de53fa95a67eaedcea3ac459dfd6af14325211fb9ff` | `023_sov_nuclear_bombs_first_and_last_grey.dds` — `39105290f4c1ab5ecf24511d8769091fc74629a6201875e7ad5c7b1fd4c9a5c1` | `023_sov_nuclear_bombs_first_and_last_not_eligible.dds` — `fcb379a26db28377787ff34bae3f109046bc0fb6bafeb8483b4b7eceba5d7632` |
| `023_sov_nuclear_bombs_the_last_telephone` | `023_sov_nuclear_bombs_the_last_telephone.dds` — `beef77295ba7f8c5a76330416c87fec1258f17564cb30095f5fba380f8b9f13d` | `023_sov_nuclear_bombs_the_last_telephone_grey.dds` — `e09f29dacf083d8cd15b7bd23fc758913394c4652ed9f0933501e02c07ae2887` | `023_sov_nuclear_bombs_the_last_telephone_not_eligible.dds` — `9e731fb8fcfb15524a7e886c2b03f71b995d58e271b9c3d32b56d184d06cca39` |

## Contact sheets and runtime mapping

The contact-sheet SHA-256 values are:

| Review sheet | Path | SHA-256 |
| --- | --- | --- |
| Native-size color/grey/not-eligible triplets, 64x64 per state | `docs/assets/023_sov_nuclear_bombs/contact_sheets/achievement_replacement_2026-09-26/replacement_native_triplets.png` | `ea526ec68395ebaf3605ec0f1d01559b703a4afb73736dbab4d8807254802946` |
| 4x nearest-neighbour final-state review | `docs/assets/023_sov_nuclear_bombs/contact_sheets/achievement_replacement_2026-09-26/replacement_4x_nearest.png` | `dd583873e7ef450429c067e9da6acb8e86fe4db150d80c79d5f7674f91c34bba` |
| Native alpha source, processed transparency, smooth preview, and DDS decode | `docs/assets/023_sov_nuclear_bombs/contact_sheets/achievement_replacement_2026-09-26/replacement_pipeline_alpha_roundtrip.png` | `fabf2c36aabbf08c96e77c07d26285fc6e4bb751957ad523ab9456559dabdb3d` |
| Original and focused-edit source lineage with selected/rejected labels | `docs/assets/023_sov_nuclear_bombs/contact_sheets/achievement_replacement_2026-09-26/replacement_source_lineage.png` | `9fda3ff4b0cbf1cd11f7c028a918dc383748e8dff3e615ab443ba7f4d4b12376` |

Each stable achievement ID still maps to `common/achievements/chaos_redux_achievements.txt`, three existing aliases in `interface/chaosx_achievements.gfx`, and root-level runtime targets `gfx/achievements/<achievement_id>.dds`, `gfx/achievements/<achievement_id>_grey.dds`, and `gfx/achievements/<achievement_id>_not_eligible.dds`. The crosswalk at `docs/assets/023_sov_nuclear_bombs/notes/achievement_requirement_runtime_crosswalk_replacement_2026-09-26.md` lists every exact ID, alias family, current runtime target, candidate source, triplet, and staged DDS family. No runtime path or alias was modified.

## Findings, review status, and ownership boundary

- The final candidate package has seven complete source triplets, 21 canonical processor review PNGs, 21 staged DDS files, and native-size plus 4x nearest-neighbour contact sheets.
- All seven candidate IDs remain `needs_user_review`. Parent review must choose or reject each subject before any runtime promotion.
- A Hundred Suns includes an unrequested red Soviet star. Two focused edits attempted its removal but the model retained the emblem, so the original GEN-01 source was used for staging. This is explicitly flagged for parent selection; it is not presented as recovered or accepted art.
- The original Scattered Arsenal image was crowded at native size. Its retained focused edit simplifies the yard to the gate, converging rails, three sealed crates, and a guard.
- The original Firebreak image left the cable severed and off-frame. Its retained focused edit shows a wrapped splice and keeps the subject in frame.
- No background-removal fallback was used. There is no fake checkerboard, opaque source canvas, generated text, or alpha-key cleanup in the art. Checker patterns exist only as contact-sheet inspection backgrounds.
- The final DDS output alpha extrema are 254..255 because the canonical supplied achievement backgrounds are composited beneath the transparent subject layers. The generated subject and source triplet alpha remain present in their PNG inputs.
- Independent parent visual selection, final crosswalk review, runtime DDS promotion, live HOI4 consumer review, and the overall Event 023 completion claim remain with the parent/user. HOI4 was not launched and live validation was not attempted.

Protected existing Event 023 native masters, processed images, package/runtime DDS, GFX, achievement definitions, localization, and IDs were not written by this candidate pass. The only existing documentation file updated was `docs/assets/023_sov_nuclear_bombs/manifest.md`; the replacement-specific crosswalk and this handoff were added. No GFX/GUI/gameplay/localization/workbook/CSV file was edited. No commit was created.

At handoff time, `git status` reports `common/achievements/chaos_redux_achievements.txt` as modified; its current diff adds Event 042 achievements and contains no Event 023 changes. This pass did not edit that registry. The repository ignores `docs/assets/` at `.gitignore:80`, so the source art, prompts, processed layers, contact sheets, staged DDS files, manifest update, and crosswalk are present in the shared workspace but are not shown as tracked Git changes. Nothing was force-added.
