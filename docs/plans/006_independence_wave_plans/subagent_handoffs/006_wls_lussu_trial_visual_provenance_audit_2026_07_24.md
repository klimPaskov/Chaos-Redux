# Event 006 Saunders Lewis trial 02 and Emilio Lussu trial 01 independent portrait audit

Date: 2026-07-24.

This handoff records a read-only, fail-closed audit of the two source-locked real-person country-leader portrait candidates requested for Event 006 Independence Wave.

The audit compares each unchanged archival master, explicit archival crop, raw ImageGen result, processed `156x210` candidate, processor sheet, and canonical leader-role references. Identity/likeness is evaluated separately from HOI4 style and is non-compensable.

No source master, crop, ImageGen result, processed PNG, DDS, `.gfx`, character, history, scripted effect, localisation, flag, advisor, focus, decision, map, or gameplay file was changed. The only owned change is this handoff.

## Decision summary

`PASS` means that the named gate is acceptable for this audit only. It does not authorize DDS conversion or runtime wiring. A single likeness failure closes the candidate even when style, framing, provenance, ownership, and role fit pass.

| Candidate | Provenance and rights | Likeness / identity | HOI4 leader style | Framing | Ownership | Role fit | Consumer boundary | Male-only scope | Runtime authorization | Disposition |
|---|---|---|---|---|---|---|---|---|---|---|
| Saunders Lewis, `wales_saunders_lewis_trial_02` | **PASS.** Attributed 1916 *Y Drych* source with Commons Public Domain Mark and pre-1931 publication basis. | **FAIL.** Trial 02 removes the glaring enlarged/bright eye failure from trial 01 but still regularizes and near-symmetrizes the eyes and face enough to lose confident source-specific likeness at native size. | **PASS.** Restrained painted political-leader treatment with period palette and no UI/text. | **PASS.** Full head-and-shoulders `156x210` leader frame; no advisor crop. | **PASS.** Current token is the intended consumer; no vanilla owner; Kaiserreich same-person hit is disclosure-only. | **PASS.** Male Welsh civic country-leader role in the existing civilian-large slot. | **PASS.** One full-size sprite only; no advisor, dossier, `_small`, commander, operative, alternate-country, or unrelated derivative. | **PASS.** Current character is explicitly male and uses no opposite-gender pool or metadata. | **FAIL.** Candidate remains `candidate_requires_visual_approval`; likeness is closed and no candidate DDS was made. | **FAIL, blocked on likeness.** Do not convert or wire. |
| Emilio Lussu, `sardinia_emilio_lussu_trial_01` | **PASS with jurisdiction caveat.** Commons records Archivio Brigata Sassari 1916, Giovanni Battista Diana, and a United States public-domain tag; the page warns that status may differ outside the United States. | **FAIL.** The source-soft/blurred viewer image-right eye is rendered as a defined dark eye with a light/contoured spot, which is impermissible reconstruction rather than preserved ambiguity; the face is also frontalized and regularized. | **PASS.** Restrained painted leader treatment with period tunic/high collar and no UI/text. | **PASS.** Full head-and-shoulders `156x210` leader frame; no advisor crop. | **PASS.** Current ARX consumer is the intended owner; vanilla has no exact owner; Kaiserreich `SRI_emilio_lussu` is disclosure-only. | **PASS.** Male Sardinian civic/military-political country-leader role in the existing civilian-large slot. | **PASS.** One full-size sprite only; no advisor, dossier, `_small`, commander, operative, alternate-country, or unrelated derivative. | **PASS.** Current character is explicitly male and uses no opposite-gender pool or metadata. | **FAIL.** Candidate remains `candidate_requires_visual_approval`; likeness is closed and no candidate DDS was made. | **FAIL, blocked on likeness and source-ambiguity handling.** Do not convert or wire. |

### Direct answers to the requested visual questions

Saunders trial 02 is a meaningful improvement over trial 01: the eyes are darker, smaller, less open, and no longer dominated by bright sclera or round catchlights. It does not fully fix the non-compensable identity failure. The candidate still opens and equalizes the small deep-set eyes, reduces the source's eye-height/shape asymmetry, fronts the face, and smooths weakly evidenced cheek, nose, and ear planes. Once hair, coat, and age are discounted, native-size output can still read as a generic young soldier. Style cannot compensate for that residual likeness failure.

Lussu trial 01 does not preserve the source ambiguity. The viewer image-right eye is visibly soft/blurred and partly occluded in the archival crop. In the repaint and processed candidate it reads as a deliberately drawn eye with defined geometry and a small light mark. Under the real-person gate this is impermissible reconstruction, not a safe interpretation of the blur. The candidate also reduces the source's slight three-quarter asymmetry through frontalization and face/eye regularization.

## Audited packages and intended consumers

The Saunders package is `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_24/wales_saunders_lewis_trial_02/`.

Its intended current consumer is the dynamically generated male token `WLS_independence_wave_national_council`, displayed through `GFX_portrait_WLS_independence_wave_national_council` as a civilian-large country-leader portrait.

The Lussu package is `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_24/sardinia_emilio_lussu_trial_01/`.

Its intended current consumer is `ARX_emilio_lussu` on Sardinia (`ARX`), displayed through `GFX_portrait_ARX_independence_wave_emilio_lussu` as a civilian-large country-leader portrait.

Both packages are explicitly male real-person candidates. Neither package authorizes an advisor, dossier, `_small`, commander, operative, alternate-country, female, or unrelated consumer.

## Source provenance, rights, and immutable identity evidence

### Saunders Lewis

The unchanged primary archival master is `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/wales_saunders_lewis_trial_01/source_masters/WLS_saunders_lewis_ydrych_1916.jpg`, RGB `1016x2239`, SHA-256 `d1552ea79f34d162e972ebe0528c219755e52f851226d6e07ef560e8c29b80e3`.

The unchanged source record is the *Y Drych* issue of 3 February 1916, hosted by the National Library of Wales at <https://papuraunewydd.llyfrgell.cymru/view/3776384/3776392/60/> and represented by the Commons record at <https://commons.wikimedia.org/wiki/File:Saunders-lewis-y-drych-1916.jpg>.

The source attribution is `Y Drych`; the photographer is not stated. The Commons record retains a Public Domain Mark, a pre-1931 United States publication basis, and the public-domain-in-country-of-origin/life-plus-70 discussion. This audit records that rights basis without upgrading it to a named photographer or a broader licence.

The explicit identity crop is `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/wales_saunders_lewis_trial_01/source_crops/WLS_saunders_lewis_ydrych_1916_head_shoulders.png`, RGB `590x794`, SHA-256 `eb0f03982a3d2b6b2c06dd766c21489b447d8488db9f28645c666ca3c1a672aa`, extracted from source pixels `(210, 200, 800, 994)`.

The crop retains the compact narrow face, short dark hair, ear placement, long narrow nose, thin mouth, young-adult age band, small deep-set asymmetric eyes, Great War coat, collar, and shoulder line. The source does not support inventing bright sclera, large irises, catchlights, or hidden facial planes.

### Emilio Lussu

The source page is <https://commons.wikimedia.org/wiki/File:Emilio_Lussu_WWI.jpg>.

The unchanged primary master is `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/mediterranean_volga_assyria/source_masters/sardinia/arx_emilio_lussu_commons_original.jpg`, RGB `861x1107`, SHA-256 `b91efc1de64c98ec591a97e41fc79d1823d35ee8be0797ce5525920736ba633a`.

The Commons record identifies the 1916 Archivio Brigata Sassari source and Giovanni Battista Diana as creator. It carries a United States public-domain tag and explicitly warns that the image may not be public domain outside the United States. This audit therefore records provenance as PASS with a jurisdiction caveat and does not claim universal public-domain clearance.

The explicit identity crop is `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_24/sardinia_emilio_lussu_trial_01/source_crops/ARX_emilio_lussu_1916_head_shoulders.png`, RGB `535x720`, SHA-256 `24a8f9272a73614cc03f150518a03daecf8171383c2a466e16fa87ba0fd1bba8`, extracted from source pixels `(175, 20, 710, 740)`.

The crop retains the narrow rectangular face, high forehead, short center-parted hair, prominent ears, straight narrow nose, small mouth, compact moustache/short boxed beard, slight three-quarter pose, serious expression, high collar, and shoulder line. The viewer image-right eye is visibly soft/blurred and partly occluded; that ambiguity is identity evidence and must not be replaced with invented iris or eyelid detail.

## Processing and evidence hashes

The processor is `.agents/skills/chaos-redux-event-assets/tools/advisor_icon_processing.py` version `5.0`, processor SHA-256 `c6e78c01c025ad57fef8dc25eb79bd216ff9809df27e4c758eb9ec72594a3963`. Both metadata records use `mode = leader`, `source_kind = real`, the candidate raw-result crop `(3, 0, 1080, 1450)`, and the canonical leader reference directory. Both retain `portrait_provenance = null` and `status = candidate_requires_visual_approval`.

| Candidate | Raw ImageGen result | Processed candidate | Processor metadata | Processor sheet |
|---|---|---|---|---|
| Saunders trial 02 | `imagegen_results/WLS_saunders_lewis_identity_preserve_trial_02.png`, RGB `1083x1452`, SHA-256 `4c81e29529006ebfe80aeeef2f2d30985e812c36b32d137d54dfee8bd42e5835` | `processed_png/portrait_WLS_independence_wave_national_council.png`, RGBA `156x210`, SHA-256 `dd5946c65458fb85d4a136a768f9b0b946f0a9a1b5380505ad5b17652e163a3d` | `metadata/WLS_saunders_lewis_trial_02_processing.json`, SHA-256 `78b6881254afb23456c819f1a540c055c5ebf35daf850c8b9fe7fa77899cfa12` | `review_sheets/WLS_saunders_lewis_trial_02_processor_style_comparison.png`, RGBA `1344x464`, SHA-256 `d6bcaf653e1816da5eca2054ea8d1e9498ea17f8f170cd239d238c4a88ecb43d` |
| Emilio Lussu trial 01 | `imagegen_results/ARX_emilio_lussu_identity_preserve_trial_01.png`, actual RGB `1082x1454`, SHA-256 `2913582d0dff6159651486a58be1987cb38bf5dcb087519cc6fdf6bac7c7f85c` | `processed_png/portrait_ARX_independence_wave_emilio_lussu.png`, RGBA `156x210`, SHA-256 `8ae82fe2cdc1f6f4d129dd1fea8603c90d479d324c1be5b382ff8539958111a1` | `metadata/ARX_emilio_lussu_trial_01_processing.json`, SHA-256 `ed8df6b38d195cff822b4b13e7ac8b242c5cde3dd2a2d979b964087ddfd68bdb` | `review_sheets/ARX_emilio_lussu_trial_01_processor_style_comparison.png`, RGBA `1344x464`, SHA-256 `614ce42410af8210e599e785c4a56d7db1041e00d27bd74d73293709025dca4f` |

The Lussu manifest states `1083x1452` for the raw result at `.../sardinia_emilio_lussu_trial_01/manifest.md:37`, but the unchanged file decodes as `1082x1454`. The file hash and processor crop metadata agree with the actual file. This stale dimensional statement is a documentation/evidence defect that must be reconciled before any later admission; it does not turn the candidate into a runtime-approved asset.

The processor sheets are not sufficient archival identity evidence by themselves. Each sheet labels its first panel as an explicit source crop even though that panel is the crop of the raw ImageGen result, not the immutable archival crop. The Saunders manifest names Stauning and Zahir as style-only references while the sheet visibly labels Stauning and Mannerheim; the Lussu manifest names De Valera and Stauning while its sheet also visibly labels Stauning and Mannerheim. The immutable masters and exact crops were reviewed separately, so this mismatch is recorded as a review-evidence limitation rather than silently accepted.

The canonical style-only references inspected were `den_thorvald_stauning.png` (`156x210`, SHA-256 `08732002182bdcb2bff3d78b142cc2b3d75adbdb29d4115f9e89ca5bdc6a21b6`), `afg_mohammed_zahir_shah.png` (`156x210`, SHA-256 `f606bc3c6204e0dbd35d8edceb21f87ae6f93a0ae7ad657382c7e9043e8907a0`), and `ire_eamon_de_valera.png` (`156x210`, SHA-256 `ff5f8689f1e8ea75bf88bea4c4a87dcf60518b1e062ea53be4a9ceff3509dcb0`). Their canonical leader-family copies are under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/`; the canonical leader contact sheet SHA-256 is `8966ae351d1fe8fc13d47ca1c59ec3d8a34da9101ce5fd65f7acff3421bd0401`.

## Independent visual review

### Saunders Lewis trial 02

The unchanged newspaper master and crop show the source-specific narrow face, compact jaw and chin, short swept hair, visible ear positions, long narrow nose, thin lips, young-adult age, Great War collar and coat, and notably small deep-set eyes with unequal shadow and height. The viewer image-left eye is darker/deeper; the viewer image-right eye is lower and more oblique.

Trial 02 materially improves trial 01. It suppresses the glaring bright whites, round/open eyes, and catchlight-like treatment that caused trial 01 to fail. The raw result and processed candidate retain the coat/collar/button, hair mass, young age band, quiet background, and overall silhouette without medals, insignia, straps, weapons, modern objects, text, or watermark.

The likeness gate still fails. Relative to the exact crop, both eyes remain more open and legible, their shape and height are closer to equal, the gaze is more frontal, and the source's dark/oblique asymmetry is weakened. The candidate also fronts and smooths the cheeks, nose, ears, and jaw into facial planes that the halftone source does not establish. At native `156x210`, the portrait can still read as a generic young soldier when the hair, coat, and age cues are discounted. This is a source-faithfulness failure, not a style or framing failure.

The HOI4 style gate passes. The candidate is a restrained painted political-leader portrait with muted charcoal/olive/umber toning, a quiet neutral background, modeled but not photorealistic planes, and no text, border, UI, watermark, or raw photographic finish.

The framing gate passes. The output is a full opaque `156x210` head-and-shoulders civilian-large leader portrait and does not use an advisor card, dossier frame, or `_small` crop.

### Emilio Lussu trial 01

The unchanged source and crop show a narrow rectangular face, high forehead, short center-parted dark hair, prominent ears, straight narrow nose, compact moustache/short beard, serious expression, high collar, shoulders, and slight three-quarter pose. The viewer image-right eye is soft and partly obscured in the archival material.

The raw result and processed candidate broadly retain the hair, ears, moustache/beard, tunic/high collar, shoulders, period age band, and muted painted leader framing. No medals, rank marks, weapons, modern objects, text, or watermark were added.

The likeness gate fails closed. The face is more frontal and regularized than the source, eye geometry is made more equal and readable, and facial planes around the nose, mouth, beard, and cheeks are sharpened beyond the archival evidence. Most importantly, the viewer image-right source-soft eye is rendered as a defined dark eye with a small light/contoured mark. That is an unsupported reconstruction of the obscured eye, not preservation of source ambiguity. A style pass cannot compensate for this identity failure.

The HOI4 style gate passes. The candidate is a restrained painted country-leader portrait in the canonical full-size leader family, with period clothing, muted palette, quiet background, and no UI/text/photographic treatment.

The framing gate passes. The output is a full opaque `156x210` head-and-shoulders civilian-large leader portrait and does not use an advisor card, dossier frame, or `_small` crop.

## Current-project ownership and package integration

### Saunders Lewis current consumer

`common/scripted_effects/006_independence_wave_scotland_wales_package_effects.txt:257-272` creates `WLS_independence_wave_national_council` when absent, declares `gender = male`, and assigns `GFX_portrait_WLS_independence_wave_national_council` as the civilian-large portrait. The same token is promoted on the Wales routes at the surrounding scripted-effect calls. The display name and description are `localisation/english/006_independence_wave_scotland_wales_l_english.yml:5-6`.

The stable sprite declaration is `interface/006_independence_wave_region_01_portraits.gfx:63-64`, mapping `GFX_portrait_WLS_independence_wave_national_council` to `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_national_council.dds`.

### Emilio Lussu current consumer

`common/characters/006_independence_wave_mediterranean_characters.txt:91-97` defines `ARX_sardinian_provisional_assembly`, names it `ARX_emilio_lussu`, declares `gender = male`, and assigns only the civilian-large `GFX_portrait_ARX_independence_wave_emilio_lussu` portrait. `history/countries/ARX - Sardinia.txt:17` recruits the assembly character.

The stable sprite declaration is `interface/006_independence_wave_mediterranean_portraits.gfx:19-21`, mapping `GFX_portrait_ARX_independence_wave_emilio_lussu` to `gfx/leaders/006_independence_wave/portrait_ARX_independence_wave_emilio_lussu.dds`.

### Vanilla and approved reference ownership scan

Exact and variant searches across installed vanilla `common`, `history`, `interface`, and `localisation` found no Saunders Lewis character, recruitment, portrait, GFX, or localisation owner and no Emilio Lussu character, recruitment, portrait, GFX, or localisation owner. Vanilla's incidental `Lussu` surname name-pool entry is not character ownership and was excluded.

Kaiserreich `1521695605` has an active same-person Saunders owner: `common/characters/WLS characters.txt:97-120`, `history/countries/WLS - Wales.txt:36`, `interface/kaiserreich/portraits/WLS_portraits.gfx:31-40`, and `localisation/english/KR_country_specific/WLS - Wales l_english.yml:208-210`. It also has an active same-person Emilio owner: `common/characters/SRI characters.txt:181-203`, `history/countries/SRI - Socialist Republic of Italy.txt:256`, `interface/kaiserreich/portraits/SRI_portraits.gfx:67-72`, and `localisation/english/KR_country_specific/SRI - Socialist Republic of Italy l_english.yml:1043-1045`. These are disclosure-only under the accepted mutually-exclusive-mod policy; no Kaiserreich source, portrait, or art was copied.

No exact same-person owner was found in approved reference mods `2265420196` or `1458561226`. Generic surname/name-pool hits were excluded as non-ownership. Current-project and vanilla ownership gates therefore pass for the intended consumers, with the cross-mod disclosures retained.

## Runtime and consumer boundary

The current repository contains one full-size runtime DDS for each intended consumer. `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_national_council.dds` is `156x210`, 131,168 bytes, SHA-256 `12ca49ed34c4d84b4135e580baa1c36994dc391baade62d02dbd80e1fd1fed05`. `gfx/leaders/006_independence_wave/portrait_ARX_independence_wave_emilio_lussu.dds` is `156x210`, 131,168 bytes, SHA-256 `92c4e49dd66d083f27fb455fa0dc2fa09949e8d40bdc2d7473aa6b957e99d445`.

Those DDS files are existing earlier treatments at the stable paths, not the two audited candidates. Their presence and current `.gfx` mappings do not approve trial 02 or trial 01. No candidate DDS was produced or overwritten by this audit.

The exact consumer boundary is one civilian-large full-size leader sprite per subject. No matching advisor, dossier, `_small`, commander, operative, alternate-country, or unrelated consumer was found or authorized. Male-only scope passes for both current character definitions; no female metadata or opposite-gender name-pool pairing is present.

Runtime authorization is FAIL for both candidates because likeness is FAIL, metadata remains `candidate_requires_visual_approval` with `portrait_provenance = null`, and the requested candidate textures have not been independently admitted. Do not convert, register, replace, or wire either candidate. No fallback identity or copied cross-mod art is authorized.

## Country-package and file-surface checklist

| Surface | Audit status | Evidence or boundary |
|---|---|---|
| Country/tag/current portrait token consistency | **PASS for the portrait-bound surfaces.** | `WLS_independence_wave_national_council` resolves through the Wales scripted effect and GFX sprite; `ARX` recruits `ARX_sardinian_provisional_assembly`, which names `ARX_emilio_lussu` and resolves through the Sardinia GFX sprite. |
| State ownership, controller, cores, claims, capital, victory points, supply, rail, ports, resources, buildings | **NOT AUDITED.** | No map/state write or gameplay admission was requested; this visual handoff makes no claim about map safety. |
| Politics, ruling party, elections, stability, war support, laws, diplomacy, faction, subjects | **NOT AUDITED except portrait-bound leader metadata.** | Both current portrait-bound definitions are male civilian-large leaders; broader politics remains parent scope. |
| Flags, advisors, high command, commanders, operative, dossier, and portrait derivatives | **PASS for consumer exclusion only.** | No matching advisor/dossier/`_small`/commander/operative derivative is authorized or present for these candidates; flags and unrelated advisors were not re-audited. |
| Focus tree, decisions, missions, ideas, and promised unlocks | **NOT AUDITED.** | No focus/decision/idea edit was made; candidate admission is independent of those systems. |
| Starting army, navy, air force, templates, equipment, manpower, technology, research, production, convoys, trains, fuel, industry, supply | **NOT AUDITED.** | No military/technology/industry change was made. |
| AI strategy, templates, diplomacy behavior, focus choices, survival/playability | **NOT AUDITED.** | No AI or playability claim is made by this portrait audit. |
| Localisation and asset manifest coverage | **PASS for current names and candidate evidence, with stale package notes.** | Current display keys resolve; candidate manifests, metadata, prompts, raw/candidate hashes, role refs, and review sheets were inspected. Lussu raw dimensions and both processor-sheet source/reference labels need reconciliation before any future admission. |

The audited file surface included both candidate manifests, prompts, raw results, processed PNGs, metadata JSON files, processor sheets, immutable masters/crops, canonical leader references/contact sheets, current character/history/scripted-effect/localisation/GFX files, stable DDS files, installed vanilla ownership surfaces, and Kaiserreich/approved-reference ownership surfaces. No file outside this handoff was edited.

## Validation performed and skipped

Read-only validation recomputed the listed SHA-256 hashes and raster dimensions/modes with Pillow, inspected metadata processor/source-kind/status fields, scanned current/vanilla/reference ownership with exact and variant terms, enumerated matching runtime/GFX surfaces, and visually reviewed the archival master, exact crop, raw result, processed candidate, processor sheet, and role references at native and enlarged high-detail display scale.

A disposable nearest-neighbour review sheet was generated outside the repository at a common `624x840` panel scale for both subjects, inspected, and deleted after review. The source masters/crops and candidate assets were not altered, and no review derivative was retained. This satisfies the requested native and at-least-4x nearest-neighbour comparison without changing package images. The comparison confirms the Saunders eye improvement but residual regularization, and confirms the Lussu image-right-eye reconstruction. Both candidates therefore remain closed on the non-compensable likeness gate.

DDS conversion, final `.gfx` replacement, in-game rendering, map inspection, country-package admission, and broad focus/decision/AI/military/playability validation were skipped because candidate likeness is blocked and those systems are outside this read-only visual handoff. No fallback or simplification was silently substituted.

## Simplifications, omissions, blockers, and parent action

Both candidates are incomplete and blocked. Saunders trial 02 needs another source-locked identity pass that preserves the small unequal deep-set eyes, oblique gaze, narrow face, and source asymmetry without frontalization or generic young-soldier regularization. Emilio Lussu trial 01 needs another source-locked pass that preserves the viewer image-right eye's blur/occlusion instead of drawing an iris, highlight, eyelid contour, or unsupported geometry; the slight three-quarter asymmetry must also remain.

The Lussu manifest's raw-result dimensions disagree with the unchanged file (`1083x1452` stated versus actual `1082x1454`), and both processor sheets mislabel the raw crop as the archival crop and show reference labels that do not match their manifests. These documentation/evidence defects should be reconciled before a future audit; this handoff does not edit those files.

The existing stable DDS files are older treatments and are not approval of either audited candidate. The metadata provenance fields remain null and candidate status remains pending by design. No source, art, fallback, derivative, DDS, wiring, or gameplay change was made.

Parent handoff path: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_wls_lussu_trial_visual_provenance_audit_2026_07_24.md`.
