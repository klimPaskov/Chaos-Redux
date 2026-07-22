# Event 006 Scotland, Wales, and Wallonia civic portrait visual/provenance audit

Date: 2026-07-22  
Scope: independent source, provenance, identity, style, ownership, and runtime-consumer audit of the three named sourced civic portrait packages.  
Owned change: this handoff only. No source master, crop, ImageGen result, processed PNG, DDS, `.gfx`, character, gameplay, localisation, or package manifest outside this file was changed.

## Decision summary

`PASS` below means that the named gate is acceptable only; it is not a claim that a DDS was created or that the parent has completed package admission. Every candidate remains closed to automatic runtime wiring until the parent performs the normal conversion and the complete country/package audit.

| Subject / candidate | Source, role, and date gate | Full-size and native visual gate | Ownership gate | Final audit status | Runtime action |
|---|---|---|---|---|---|
| Robert Bontine Cunninghame Graham, `scotland_cunninghame_trial_02` | **PASS with deliberate source-age caveat.** HathiTrust/Commons pre-1931 source (`PD-US-expired` basis) plus a Rijksmuseum CC0 same-person cross-check; exact Scottish civic identity, alive at the January 1936 boundary. The sources show a younger/middle-aged man and the repaint intentionally does not invent an 83-year-old 1936 reconstruction. | **Needs revision.** Trial 02 is materially better than rejected trial 01 and retains the unusual hair, long face, nose, curled moustache, pointed beard, collar, and cravat. It still opens/symmetrises the eyes, broadens and smooths the face, and changes moustache/beard geometry enough that the native image can read as a generic Victorian bearded man when the hair and beard are discounted. | **PASS.** The current Chaos Redux token is the intended dynamic consumer, not a second historical owner; no exact Cunninghame Graham owner was found in vanilla or the approved reference mods. | **`NEEDS_REVISION` (closed)** | Do not convert or wire. Retain both source masters and the candidate; make a more source-faithful face pass, then repeat full/native review. No fallback is authorised. |
| Saunders Lewis, `wales_saunders_lewis_trial_01` | **PASS with weak-source/date caveat.** `Y Drych`, 3 February 1916, National Library of Wales/Commons Public Domain Mark and pre-1931 publication basis; exact Welsh nationalist/civic identity, alive in 1936. The portrait deliberately preserves the young-adult 1916 appearance rather than inventing a 1936-age reconstruction. | **FAIL closed.** The output has a coherent HOI4 painted finish and keeps the period overcoat, collar, oval face, hairline, nose, mouth, and young age, but the eyes are materially larger, rounder, brighter, and more symmetric than the halftone source. Ear/cheek planes are regularised and the result reads as a generic young soldier at native size. The single weak newspaper source does not support accepting those invented details. | **PASS for current scope; disclosure recorded.** The current Chaos Redux token is the intended dynamic consumer and vanilla has no exact owner. Kaiserreich actively owns `WLS_saunders_lewis`, but the accepted mutually-exclusive-mod policy makes that same-person hit disclosure-only when no source or art was copied. | **`FAIL` (blocked on likeness)** | Do not convert or wire. Keep the unchanged newspaper source and mark the candidate blocked pending a tighter identity-preserving finish or a separately defensible sourced candidate. No fallback is authorised. |
| Jules Destrée, `wallonia_destree_trial_01` | **PASS with rights uncertainty recorded.** Direct Commons historical press source from *Le Patriote Illustré*, 12 January 1936, author unknown; the package records a public-domain historical-press basis and the exact Walloon civic identity is alive in January 1936. The unknown-author/territorial rights caveat remains attached; it is not silently upgraded to a named licence. | **PASS.** The strict left profile remains source-faithful at full and `156x210`: long curved nose, heavy brow and lowered eye, hair wave/receding temple, ear, short moustache, cheek/jowl/chin, thick neck, collar, bow tie, shoulder line, and elderly age are all retained. Minor halftone smoothing is painterly abstraction; no frontal reconstruction, pose rotation, hidden-face invention, genericisation, or advisor framing was observed. | **PASS.** `AFX_walloon_provisional_assembly` is the existing intended current-project consumer carrying Destrée's name; no separate current, vanilla, Kaiserreich, or approved-reference historical Destrée owner was found. | **`PASS` (visual/provenance candidate only)** | Parent may proceed to repository-standard DDS conversion after retaining the Commons/publication attribution and rights caveat. This audit did not create or wire a DDS; final country/package admission is still required. |

## Common package and processing evidence

The three packages were inspected directly, including each `manifest.md`, `gfx_handoff.md`, source master, explicit crop, ImageGen result, processed PNG, prompt, metadata JSON, and both comparison sheets. The canonical reference root used for the style comparison was:

- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/`
- leader contact sheet and the canonical `den_thorvald_stauning.png` / `fin_carl_mannerheim.png` leader-family examples shown in the package processor sheets

All three metadata records use `advisor_icon_processing.py` v5.0, `leader` mode, `source_kind = real`, a full-portrait crop, canonical leader references, and `status = candidate_requires_visual_approval`. No metadata status was rewritten. Each processed PNG is exactly `156x210`, RGBA, and fully opaque (`alpha = 255` for every pixel):

| Package | ImageGen result | Native processed PNG | Full comparison sheet | Processor/style sheet |
|---|---|---|---|---|
| Scotland | `1081x1455`, SHA-256 `b0ab6c888e123c8f60b1cf6822ed3d1ddb0817edf827a79760a6dd6a1b44dd32` | `portrait_SCO_independence_wave_civic_convention.png`, SHA-256 `83efe010ccc536bc0de51a12d474bdabc6b4e34220958c233e13c6e656d7ff03` | `1560x458`, SHA-256 `2dc7530381690b4c09b99002a4c9576d359d447edab21d352cc37a4bf0a175f8` | `1344x464`, SHA-256 `069bf03d3b1efcb846707fcfa28919bd66050a556396b23e7a88ba5b6abb10ae` |
| Wales | `1082x1454`, SHA-256 `b4372c9bf01564507e1ee0770111fc3333a5d2bf417a2f8c01bbce477b01e757` | `portrait_WLS_independence_wave_national_council.png`, SHA-256 `3b184ce80e81246f2318f8a8221b958c78afad57e595b8ba5adda68df44e63e0` | `1440x458`, SHA-256 `6765d1b5b45a440faddea2c0ae3f4c97e900d8b5c0cb46b00410a016385cf20f` | `1344x464`, SHA-256 `c1020418aa104a527dafc0707b21f9738a48cf067765fdb42164a4c07a7330be` |
| Wallonia | `1080x1456`, SHA-256 `b07ef2d6a77c6d4f86314638b7f352d3488b9f396e566e8b04d21298e49922b7` | `portrait_AFX_walloon_provisional_assembly.png`, SHA-256 `7f1d43f8d3b350040b59630e44f1d7f8a7635883e7a067dcc5901abde2fc75be` | `1440x458`, SHA-256 `c145e1ad9a5bf34a4172c661b8dbdd82750f3c002504b6f0341e15770c5f37de` | `1344x464`, SHA-256 `07dcd14f90eebe0d4bb267c8c77e1d0f592412ca956295ad72bb63afaf894992` |

No package contains a final DDS. The absence is intentional review gating, not a missing conversion to overlook.

## Robert Bontine Cunninghame Graham — Scotland trial 02

### Source and provenance

- Primary source: `source_masters/SCO_cunninghame_graham_hathitrust_1907.jpg`, JPEG/RGB `813x1101`, SHA-256 `401cc30d278122a6cc99b691e913a63c568a2ef82e1e0ae0513dc93f303d4fbb`. The package links the Commons record and the HathiTrust scan, records publication no later than 1907, photographer not stated, and a Commons `PD-US-expired` / pre-1931 publication basis.
- Primary review crop: `source_crops/SCO_cunninghame_graham_hathitrust_head_shoulders.png`, RGB `580x780`, SHA-256 `bc30ee3ccf31d8e31656678bf8b703658189e83cb300889e3461bfba9a73b56a`.
- Same-person cross-check: `source_masters/SCO_cunninghame_graham_rijksmuseum.jpg`, JPEG/RGB `3846x4852`, SHA-256 `5d646596028a8a069651207e2058e8b59bdf7276d28921fd2a1ddefe2ff7abe7`; Rijksmuseum circa 1881–1891, anonymous Bassano cliche maker, CC0/public-domain record.
- Cross-check crop: `source_crops/SCO_cunninghame_graham_rijksmuseum_identity_crop.png`, RGB `1910x2575`, SHA-256 `49cb8464cb15a451c16fc0728e60963b93e3e4742c86f07bc923c35b83586069`.

Robert Bontine Cunninghame Graham (1852–1936) is an exact Scottish political/writing identity and was alive at the January 1936 start boundary. Both sources show him younger than the scenario-year endpoint. Preserving that source age is deliberate and defensible; an invented 1936-age face would be a prohibited reconstruction. The source, date, photographer, and public-domain/CC0 uncertainty remain part of the attribution record.

### Full-size and native visual review

Trial 02 improves materially on the rejected `scotland_civic` trial 01: the HathiTrust face is now the primary identity input, the Rijksmuseum image cross-checks the same unusual subject, and the result retains the source's high swept-up wavy hair, high forehead, long narrow face, close-set eyes, long thin nose, curled moustache, full pointed beard, visible ears, wing collar, and narrow cravat. The source-age band is not shifted toward 1936.

The remaining gap is visible in the full `1081x1455` result and native output. The repaint opens and partially symmetrises the eyes, fills and smooths the cheeks/jaw, softens the source's narrow nose plane, and changes the moustache/beard mass and hair crest. At native `156x210`, the silhouette and hair/beard combination remain legible, but once those strong period cues are mentally discounted the face is not yet as source-specific as the HathiTrust crop; it can read as a generic Victorian bearded man. This is a visual-fidelity deficiency, not a missing source or a role error.

### Ownership and runtime consumer

- Current Chaos Redux creates `SCO_independence_wave_civic_convention` dynamically in `common/scripted_effects/006_independence_wave_scotland_wales_package_effects.txt:210-225`, assigns `GFX_portrait_SCO_independence_wave_civic_convention`, and promotes that same token on the Scotland routes. The localisation at `localisation/english/006_independence_wave_scotland_wales_l_english.yml:2` is the intended consumer label; it is not a second historical Cunninghame Graham owner.
- Installed vanilla had no exact or variant `Cunninghame Graham` / `Robert Bontine Cunninghame Graham` character, recruitment, portrait, or localisation owner.
- Kaiserreich `1521695605`, approved reference `2265420196`, and approved reference `1458561226` had no exact Cunninghame Graham owner. Generic `Graham` name-pool entries and unrelated Graham surnames were excluded as false positives. No reference-mod source or art was copied.
- Stable sprite consumer: `interface/006_independence_wave_region_01_portraits.gfx:54-55` maps `GFX_portrait_SCO_independence_wave_civic_convention` to `gfx/leaders/006_independence_wave/portrait_SCO_independence_wave_civic_convention.dds`.
- Existing runtime DDS is stale historical treatment, not trial 02: `portrait_SCO_independence_wave_civic_convention.dds` is `156x210`, 131,168 bytes, uncompressed BGRA with opaque alpha, SHA-256 `d2fa024af32069dd83aedc13190772fb0c02cccf0947af83c4a1317767cc245b`; it decodes pixel-identically to the previously rejected photographic/sepia `docs/assets/006_independence_wave/sourced_portrait_treatments_2026_07_22/processed_png/SCO_cunninghame_graham.png` (decoded RGBA SHA-256 `8153e9ebcc8cfb60befd1e18000865702d59cdcb6d86a86a977b92e4ab443767`). It is not approval of trial 02.

### Cunninghame Graham disposition

**`NEEDS_REVISION` (closed); no runtime advancement.** The source chain, role, age disclosure, male-only framing, and HOI4-style direction are acceptable, and trial 02 is a substantial improvement over trial 01. A final source-faithful eye/face/beard pass is still required before conversion. Do not substitute a generic or generated Scottish officeholder.

## Saunders Lewis — Wales trial 01

### Source and provenance

- Primary source: `source_masters/WLS_saunders_lewis_ydrych_1916.jpg`, JPEG/RGB `1016x2239`, SHA-256 `d1552ea79f34d162e972ebe0528c219755e52f851226d6e07ef560e8c29b80e3`.
- Source record: Commons file page and National Library of Wales *Y Drych* page, issue 3 February 1916, photographer/author not stated. The package records a Commons Public Domain Mark and pre-1931 publication basis. The newspaper caption identifies “Lieut. J. Saunders Lewis”; the literal crop excludes the caption, border, and page field.
- Explicit crop: `source_crops/WLS_saunders_lewis_ydrych_1916_head_shoulders.png`, RGB `590x794`, SHA-256 `eb0f03982a3d2b6b2c06dd766c21489b447d8488db9f28645c666ca3c1a672aa`.

Saunders Lewis (1893–1985) is an exact Welsh nationalist/civic identity and Great War veteran, alive in 1936. The source is twenty years earlier than the scenario start and shows him as a young adult; the package correctly preserves that appearance rather than inventing a 1936 face. The halftone is strong enough to establish the broad face, hairline, ears, eyes, nose, mouth, overcoat, and collar, but it is a weak basis for invented high-detail eye rendering.

### Full-size and native visual review

The full `1082x1454` result and native `156x210` output have a quiet warm-grey painted background, restrained brushwork, opaque canvas, and correct leader-family framing. The coat, broad collar, central button, compact oval face, short swept hair, direct gaze, and young-adult age remain period coherent. No text, watermark, emblem, extra person, advisor card, or modern/fantasy item was added.

The identity gate nevertheless fails. Relative to the unchanged crop, the result makes both eyes substantially larger and rounder, adds bright sclera/iris highlights not recoverable from the halftone, reduces the source's deep-set/asymmetric eye structure, regularises the ears and cheek planes, and smooths the compact facial geometry. At native size the eye treatment dominates and the portrait reads as a generic young soldier rather than a confidently identifiable Saunders Lewis. The result is a painted reconstruction of uncertain facial details, not merely a restrained finish of the source.

### Ownership and runtime consumer

- Current Chaos Redux creates `WLS_independence_wave_national_council` dynamically in `common/scripted_effects/006_independence_wave_scotland_wales_package_effects.txt:257-272`, assigns `GFX_portrait_WLS_independence_wave_national_council`, and promotes that same token on the Wales routes. The localisation at `localisation/english/006_independence_wave_scotland_wales_l_english.yml:5-6` is the intended consumer label.
- Installed vanilla had no exact or variant Saunders Lewis character, recruitment, portrait, or localisation owner.
- Kaiserreich `1521695605` has an active same-person owner: `common/characters/WLS characters.txt:97-120` defines `WLS_saunders_lewis` with civilian, army-large, and army-small portraits; `history/countries/WLS - Wales.txt:36` recruits it; `interface/kaiserreich/portraits/WLS_portraits.gfx:31-40` maps the portrait surfaces; and localisation `KR_country_specific/WLS - Wales l_english.yml:208-210` names/describes the identity. The reference images `gfx/leaders/WLS/WLS_saunders_lewis_civilian.png` and `WLS_saunders_lewis_army.png` are respectively 45,055 bytes/SHA-256 `a6276ae60e1c60b7cbe3dd31d34479770cef13007b5f21c857e7738fa4cfa9af` and 46,715 bytes/SHA-256 `da2ffafd281caf1455505b2cbf08daa50a1e08682b7041b2ed5fb2aa78600879`. Under the accepted policy, this mutually-exclusive-mod same-person hit is disclosure-only when no Kaiserreich source or art was copied; it is not a binding collision. Vanilla/current Chaos Redux active-person ownership remains binding.
- Approved references `2265420196` and `1458561226` had no exact Saunders Lewis owner. No reference-mod source or art was copied.
- Stable sprite consumer: `interface/006_independence_wave_region_01_portraits.gfx:63-64` maps `GFX_portrait_WLS_independence_wave_national_council` to `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_national_council.dds`.
- Existing runtime DDS is stale historical treatment, not trial 01: `portrait_WLS_independence_wave_national_council.dds` is `156x210`, 131,168 bytes, uncompressed BGRA with opaque alpha, SHA-256 `12ca49ed34c4d84b4135e580baa1c36994dc391baade62d02dbd80e1fd1fed05`; it decodes pixel-identically to the previously rejected photographic/sepia `docs/assets/006_independence_wave/sourced_portrait_treatments_2026_07_22/processed_png/WLS_saunders_lewis.png` (decoded RGBA SHA-256 `2decda45498c11b4e53300a0f9b74e5933870bc96a4162b46840529711f33838`). It is not approval of the new candidate.

### Saunders Lewis disposition

**`FAIL` (blocked on likeness); no runtime advancement.** The rights/role/date chain is usable, but the candidate does not clear the direct full/native identity gate. Retain the unchanged newspaper master and its caption/provenance record. Do not convert, register, copy, or wire this candidate, and do not use the Kaiserreich portrait as a visual source or a fallback.

## Jules Destrée — Wallonia trial 01

### Source and provenance

- Primary source: `source_masters/AFX_jules_destree_1936.jpg`, JPEG/RGB `891x1216`, SHA-256 `8eb02adfc33a4fb0ba5d2750b342993c0ea81139c48cedbee54516555eeeea27`.
- Source record: Commons file `Jules Destrée (1863–1936)`, *Le Patriote Illustré*, 12 January 1936, author unknown. The package records a public-domain historical-press basis and retains exact publication/date evidence; the unknown-author and territorial rights question remains a caveat rather than an invented named licence. The direct original and publication evidence are also retained in the adjacent Wallonia source ledger.
- Explicit head-and-shoulders/profile crop: `source_crops/AFX_jules_destree_1936_head_shoulders.png`, RGB `891x1200`, SHA-256 `0ebfa04ee442de9971db2f3584b0434682111166ff1173890d3c0c76cfa8502f`.

Jules Destrée (1863–1936) is an exact Walloon Movement/civic identity, lawyer, minister, and living Walloon figure in January 1936. The source date is unusually strong for this package: it matches the scenario month rather than requiring an age-band exception.

### Full-size and native visual review

The full `1080x1456` result and native `156x210` output retain the strict left-facing profile instead of inventing a frontal face. The long curved nose, heavy brow and lowered eye, swept-back grey hair with the high side wave/receding temple, large exposed ear, short grey moustache, cheek folds, heavy jowl/double chin, thick neck, white collar, black bow tie, shoulder line, and elderly age all remain visible. The output uses a muted warm-grey painted background and restrained brushwork consistent with the leader references; it is not a raw photograph, sepia filter, or advisor card.

The painterly finish smooths some halftone and skin texture, but it does not shorten the nose, slim the jowl, rotate the head, thicken/redesign the moustache, reveal the unseen side, add glasses, or replace the source profile with a generic elderly statesman. The native profile remains identifiable without relying on a logo, text, or symbol.

### Ownership and runtime consumer

- Current Chaos Redux defines `AFX_walloon_provisional_assembly` in `common/characters/006_independence_wave_wallonia_frisia_characters.txt:25-30`, recruits it in `history/countries/AFX - Wallonia.txt:17`, assigns the existing `GFX_portrait_AFX_walloon_provisional_assembly`, and localises the same identity at `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml:3`. This is the intended same consumer for the candidate, not a second Destrée character or a transfer request.
- Installed vanilla had no exact or variant Jules Destrée / Jules Destree character, recruitment, portrait, or localisation owner.
- Kaiserreich `1521695605`, approved reference `2265420196`, and approved reference `1458561226` had no exact Destrée owner. No reference-mod source or art was copied.
- Stable sprite consumer: `interface/006_independence_wave_region_01_portraits.gfx:10-11` maps `GFX_portrait_AFX_walloon_provisional_assembly` to `gfx/leaders/006_independence_wave/portrait_AFX_walloon_provisional_assembly.dds`.
- Existing runtime DDS is stale historical treatment, not trial 01: `portrait_AFX_walloon_provisional_assembly.dds` is `156x210`, 131,168 bytes, uncompressed BGRA with opaque alpha, SHA-256 `3bf60a4fbb7904e300c31ea0e0ce3741813bfe54089eee88bbf7e592211d3565`; it decodes pixel-identically to the previously rejected photographic/sepia `docs/assets/006_independence_wave/sourced_portrait_treatments_2026_07_22/processed_png/AFX_jules_destree.png` (decoded RGBA SHA-256 `6391cbb55ab8b1ee6ebc431e42ed93d6a22a9a8298aa6920edbbdb979f27a685`). It is not approval of the new candidate.

### Jules Destrée disposition

**`PASS` for visual/provenance candidate status; no audit-side runtime change.** Preserve the source URL, publication/date, unknown-author note, Commons public-domain basis, and exact candidate hash. The parent may run the repository-standard `convert_to_dds.py` flow and then complete the final country/package admission audit. No separate `_small`, advisor, dossier, high-command, or alternate-country derivative is authorised.

## Runtime and wiring boundary

1. The parent owns all `.gfx`, character, scripted-effect, localisation, gameplay, and final runtime wiring. This audit only records evidence and verdicts.
2. Convert only a candidate that remains independently admitted after this handoff. The existing Scotland, Wales, and Wallonia DDS files are stale earlier treatments and must not be mistaken for the named trial packages.
3. Keep each subject on one full `156x210` leader consumer. No `_small`, advisor, dossier, theorist, high-command, female, or alternate-country derivative is authorised by these packages.
4. Keep the Kaiserreich Saunders Lewis owner as disclosure-only under the accepted mutually-exclusive-mod policy; no Kaiserreich source/art was copied. Continue to enforce vanilla/current Chaos Redux active-person ownership for any future identity reuse.
5. Preserve all source masters, explicit crops, prompts, ImageGen results, processor metadata, rights/date notes, and candidate hashes when a parent-side conversion is approved.

## Simplifications, omissions, and blockers

- Scotland trial 02 is held at `NEEDS_REVISION` for remaining full/native face fidelity; it is not a generic fallback and no DDS was created by this audit.
- Wales trial 01 is blocked on over-open/symmetrised eyes, invented high-detail facial planes, and generic young-soldier readability at native size; the Kaiserreich same-person owner is disclosure-only and not the blocker.
- Wallonia trial 01 passes the visual/provenance candidate gate with an explicit unknown-author/territorial-rights caveat; it is not runtime-complete until the parent converts and wires it and the full IW-006 package audit passes.
- No simplification, replacement identity, generated substitute, source/art copy from another mod, gameplay change, GFX edit, localisation change, final DDS, or `_small`/advisor asset was made by this audit.
