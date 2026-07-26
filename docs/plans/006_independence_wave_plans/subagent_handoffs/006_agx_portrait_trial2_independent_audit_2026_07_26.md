# Event 006 AGX Frisia trial-02 independent portrait audit

Date: 2026-07-26
Reviewer: independent sourced-visual audit subagent (producer-separate)
Scope: only the two AGX/Frisia trial-02 real-male portrait candidates; no source, PNG, DDS, `.gfx`, gameplay, localisation, character, or runtime file was edited.
Disposition: **PASS for both candidate PNGs; parent may convert and wire after reviewing this handoff.** The existing runtime DDS files were not replaced and remain outside this trial's approval evidence.

## Evidence reviewed

I inspected the unchanged archival masters, exact crops and equality JSON, raw ImageGen repaints, deterministic `156x210` candidates, both trial manifests, prompts, processor metadata, review sheets, canonical role references, and the curated male quick-reference sheets at native size and at a disposable nearest-neighbour `4x` inspection scale.

The canonical role references were `.../assets/vanilla_reference/portraits/leaders/den_thorvald_stauning.png`, `.../assets/vanilla_reference/portraits/leaders/fin_carl_mannerheim.png`, `.../assets/vanilla_reference/portraits/commanders/eng_bernard_montgomery.png`, and `.../assets/vanilla_reference/portraits/commanders/ger_erwin_von_witzleben.png`; the curated male pack sheets were `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/leaders/contact_sheet.png` and `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/commanders/contact_sheet.png`.

The trial-02 workspaces contain no generated subject substitute, female asset, advisor card, dossier card, `_small` derivative, or DDS output.

### Douwe Kalma civic leader

| Artifact | Path | Facts / SHA-256 |
|---|---|---|
| Immutable source master | `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_26/frisia_douwe_kalma_trial_02/source_masters/AGX_douwe_kalma_1917_master.jpg` | JPEG RGB `691x1013`, `87,040` bytes, `38dafcbff7c3a67b6b29b9b637e69ff4c2f9d8caae076361200919a6bb36dbdf`. |
| Exact source crop | `.../source_crops/AGX_douwe_kalma_1917_head_shoulders.png` and adjacent JSON | RGB `590x796`, crop `(50,80,640,876)`, `decoded_pixels_equal = true`, equal master-crop/output RGBA hashes `247524909d5b9cb82661b35a9f5f7b70f4411bd9b32b59f7b65ac1f74cbd94b4`. |
| Raw repaint | `.../imagegen_results/AGX_douwe_kalma_identity_preserve_trial_02.png` | PNG RGB `1080x1456`, `2,269,561` bytes, `c6a4419f7604d939548831fcab520039c6440b9f964592b9de8fa08ec5192ea1`. |
| Processed candidate | `.../processed_png/portrait_AGX_friesland_coastal_council.png` | PNG RGBA `156x210`, fully opaque alpha, `53,443` bytes, `dec3eb32366e500da0b4016df6bc7a96d3a02686ab57858944790f1e83233f3c`. |
| Metadata / review | `.../processed_png/portrait_AGX_friesland_coastal_council.png.json`; `.../review/AGX_douwe_kalma_leader_style_sheet.png` | Processor v5.0, role family `leader`, source kind `real`, status `candidate_requires_visual_approval`; review sheet `1344x464`, SHA-256 `e6fca35b5ecfe75485a32fdedfc9b96a472ce71426c7748c4c4c5c68c5ca762a`. |

The source-rights ledger is `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/northwestern_europe/manifest.md` and the retry-02 source manifest at `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/frisia_retry_02/manifest.md`.

Those records identify the circa-1917 F. O. Strüppert/Tresoar portrait, the [Wikimedia Commons file page](https://commons.wikimedia.org/wiki/File:Portret_fan_Douwe_Kalma,_1917_ca._archiefnr_1990.jpg), the [unchanged original upload](https://upload.wikimedia.org/wikipedia/commons/d/d6/Portret_fan_Douwe_Kalma%2C_1917_ca._archiefnr_1990.jpg), the [Tresoar collection record](https://tresoar.nl/zoeken/collectie/cf64b17f-5d0c-46f9-9209-a7f60c185068), and the archive/Commons public-domain basis.

### Pieter Reenalda maritime commander

| Artifact | Path | Facts / SHA-256 |
|---|---|---|
| Immutable source master | `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_26/frisia_pieter_reenalda_trial_02/source_masters/AGX_pieter_reenalda_1919_uniform_master.jpg` | JPEG grayscale `1206x1765`, `145,425` bytes, `8f93840b12ecdcb313279c6f0fd4027863f8c1c4c9232e699aa7a0a9d46668ce`. |
| Exact source crop | `.../source_crops/AGX_pieter_reenalda_1919_head_shoulders.png` and adjacent JSON | grayscale `800x1077`, crop `(203,130,1003,1207)`, `decoded_pixels_equal = true`, equal master-crop/output RGBA hashes `c78c6344d50152e9a51303f0c495fcb0035fdb5afbe80e2f94348ebbbcece0db`. |
| Raw repaint | `.../imagegen_results/AGX_pieter_reenalda_identity_preserve_trial_02.png` | PNG RGB `1082x1454`, `2,461,468` bytes, `3c9d6d44410d9001c791ac6a700689a94fc61fc6b62e7de06947ff1e67145e4d`. |
| Processed candidate | `.../processed_png/portrait_AGX_friesland_coastal_commander.png` | PNG RGBA `156x210`, fully opaque alpha, `61,642` bytes, `840e5708fa1c9f5424d5524bb93d661c39a5d888f85a34cad96d74cbcedbf856`. |
| Metadata / review | `.../processed_png/portrait_AGX_friesland_coastal_commander.png.json`; `.../review/AGX_pieter_reenalda_commander_style_sheet.png` | Processor v5.0, role family `commander`, source kind `real`, status `candidate_requires_visual_approval`; review sheet `1344x464`, SHA-256 `a11e1fc4a23b911f264c87e511dacde611ca86a0eb61704f1eeca8fc4d512bb8`. |

The source-rights ledger is `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/northwestern_europe/manifest.md` and the retry-02 source manifest at `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/frisia_retry_02/manifest.md`.

Those records identify the 1919 Tresoar family-archive photograph of Pieter Reenalda in maritime uniform, unknown maker, collection GUID `4fddaece-1058-470b-be2a-29e4e9e236ac`, and the archive/Commons public-domain basis.

## Separate gate verdicts

### Douwe Kalma: `AGX_friesland_coastal_council`

| Gate | Verdict | Evidence and finding |
|---|---|---|
| Provenance / rights | **PASS** | The unchanged attributed source, exact crop, raw repaint, processed candidate, metadata, prompt, and review sheet are retained in distinct paths. The sourced retry manifest supplies archive attribution, Commons/Tresoar links, public-domain basis, and the immutable source hash. ImageGen is used only as a source-locked repaint of the sourced crop. |
| Crop equality | **PASS** | The Pillow crop JSON declares `status = exact_source_crop_verified`, `decoded_pixels_equal = true`, matching equality hashes, and the exact rectangle `(50,80,640,876)` within the `691x1013` master. |
| Male / civic role fit | **PASS** | Master, crop, repaint, and candidate show one male subject. `common/characters/006_independence_wave_wallonia_frisia_characters.txt:81-103` declares `gender = male` and the civilian `large` portrait for `AGX_friesland_coastal_council`; no `female = yes` or opposite-gender pool is involved. The period civilian suit, collar, tie, and civic identity fit the AGX country-leader role. |
| Exact likeness (non-compensable) | **PASS** | Native and `4x` comparisons preserve the distinctive long narrow face and pointed taper, narrow unequal heavy-lidded eyes, direct gaze, long straight nose, thin asymmetric lips, unequal ear exposure, center-parted uneven hairline, young-adult age, neck/shoulder slope, and source clothing silhouette. The isolated forehead pinhole is removed as explicitly authorized surface-damage cleanup; no material face substitution, genericization, beautification, or symmetrization is visible. |
| HOI4 country-leader style | **PASS** | The raw repaint and candidate use a restrained olive-brown/charcoal painted finish, controlled contrast, quiet dark vignette, visible brush texture, and a readable face matching the leader-family references `den_thorvald_stauning.png` and `fin_carl_mannerheim.png`. No text, watermark, UI frame, modern prop, or raw-photo-only finish is present. |
| Framing / native canvas | **PASS** | Candidate is fully opaque RGBA `156x210`, with one centered head-and-shoulders subject, safe head/shoulder margins, visible collar and tie, and no dossier/card or small-portrait treatment. |
| Ownership / stable consumer | **PASS (consumer mapping only)** | Exact and variant searches for `Douwe Kalma`, `Kalma, Douwe`, `Douwe_Kalma`, and `DouweKalma` found no competing vanilla or project character/portrait owner. `history/countries/AGX - Frisia.txt:17` recruits the token; `common/characters/006_independence_wave_wallonia_frisia_characters.txt:81-103` owns the male country leader; `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml:5` names him; `interface/006_independence_wave_region_01_portraits.gfx:19-20` maps `GFX_portrait_AGX_friesland_coastal_council` to `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_council.dds`. |
| Forbidden derivatives | **PASS** | The trial workspace has no advisor, high-command, operative, dossier, `50x67`, `_small`, generated-generic, or alternate-person derivative. The candidate is an ImageGen repaint followed by deterministic full-size processing, not a raw photograph or a simple resize. |

### Pieter Reenalda: `AGX_friesland_coastal_commander`

| Gate | Verdict | Evidence and finding |
|---|---|---|
| Provenance / rights | **PASS** | The unchanged attributed 1919 uniform source, exact crop, raw repaint, processed candidate, metadata, prompt, and review sheet are retained in distinct paths. The sourced retry manifest supplies the Tresoar family-archive record, unknown-maker note, public-domain basis, and immutable source hash. ImageGen is used only as a source-locked repaint of the sourced crop. |
| Crop equality | **PASS** | The Pillow crop JSON declares `status = exact_source_crop_verified`, `decoded_pixels_equal = true`, matching equality hashes, and the exact rectangle `(203,130,1003,1207)` within the `1206x1765` master. |
| Male / maritime commander role fit | **PASS** | Master, crop, repaint, and candidate show one male subject. `common/characters/006_independence_wave_wallonia_frisia_characters.txt:109-126` declares `gender = male`, the `army.large` portrait slot, and the corps-commander consumer; no `female = yes` or opposite-gender pool is involved. The source-visible high maritime collar, buttons, pocket chain, and shoulder board directly support the Frisian coastal-commander role. |
| Exact likeness (non-compensable) | **PASS** | Native and `4x` comparisons preserve the high forehead, side-parted hair and hairline, unequal eyes and ears, broad oval/tapering face, long straight nose, small chin, direct gaze, exact very long horizontal waxed moustache with its source asymmetry and width, head angle, neck, both shoulders, and source-visible maritime uniform. No material face substitution, genericization, beautification, or symmetrization is visible. The shoulder board remains source-visible neutral geometry rather than an invented colored rank system. |
| HOI4 commander style | **PASS** | The raw repaint and candidate use a restrained grey-olive-brown painted finish, quiet vignette, controlled contrast, visible brush texture, and readable face/moustache matching the commander family references `eng_bernard_montgomery.png` and `ger_erwin_von_witzleben.png`. No text, watermark, UI frame, modern prop, or raw-photo-only finish is present. |
| Framing / native canvas | **PASS** | Candidate is fully opaque RGBA `156x210`, with one centered head-and-shoulders subject, safe head/shoulder margins, visible high collar and uniform, and no dossier/card or small-portrait treatment. |
| Ownership / stable consumer | **PASS (consumer mapping only)** | Exact and variant searches for `Pieter Reenalda`, `Reenalda, Pieter`, `Pieter_Reenalda`, and `Reenalda` found no competing vanilla or project character/portrait owner. `history/countries/AGX - Frisia.txt:18` recruits the token; `common/characters/006_independence_wave_wallonia_frisia_characters.txt:109-126` owns the male corps commander; `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml:6` names him; `interface/006_independence_wave_region_01_portraits.gfx:23-24` maps `GFX_portrait_AGX_friesland_coastal_commander` to `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_commander.dds`. |
| Forbidden derivatives | **PASS** | The trial workspace has no advisor, high-command, operative, dossier, `50x67`, `_small`, generated-generic, or alternate-person derivative. The candidate is an ImageGen repaint followed by deterministic full-size processing, not a raw photograph or a simple resize. |

## Existing runtime and promotion boundary

The current runtime DDS files are unchanged evidence only: `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_council.dds` SHA-256 `2A98ECB576B331915E2B626C9CCC6DC03AF4012A411717B73D2F5253358E15A2` and `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_commander.dds` SHA-256 `07689A7045C145401E5AA7A2CFC1AE0949D59C62D4B64F144714E20197558BBA`.

Both trial-02 candidates pass the separate identity, provenance, style, framing, ownership, role, and forbidden-derivative gates, so the parent may convert the approved PNGs with the repository DDS tool and update the existing stable sprite paths after parent-side review.

No trial-02 DDS, `.gfx` edit, runtime replacement, gameplay edit, localisation edit, advisor asset, dossier card, `_small` derivative, or fallback was created by this audit.

## Validation and skipped checks

- Recomputed the listed source, raw, candidate, review, and reference file hashes and confirmed the metadata-recorded dimensions and hashes match the files on disk.
- Reopened both candidates with Pillow and confirmed exact `156x210` RGBA dimensions and alpha extrema `(255,255)`.
- Reopened both crop JSON records and confirmed `exact_source_crop_verified`, `decoded_pixels_equal = true`, matching equality hashes, and the recorded rectangles.
- Rechecked exact and variant subject ownership terms in installed vanilla and project character/history/interface/localisation roots and found only the intended AGX consumers and display names.
- Inspected the immutable source, crop, raw repaint, candidate, review sheet, canonical role references, and curated male quick-reference sheets at native size and a separate nearest-neighbour `4x` scale.
- Confirmed the trial folders contain no DDS or `_small` derivative and that the existing runtime DDS hashes did not change during this audit.
- Skipped DDS conversion, `.gfx` edits, runtime replacement, live HOI4 loading, and consumer acceptance because those are parent-owned promotion steps and this audit must not perform them.

No simplification or fallback was used. Retain the source-rights links and attribution from the 2022-07-22 Frisia source ledger when promoting either candidate.
