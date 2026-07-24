# Event 006 HAW David Kalākaua Kawānanakoa trial 01 independent portrait audit

Date: 2026-07-24  
Reviewer: country-package audit subagent  
Package commit reviewed: `23e9b464d73935187a751b854fae467d9777bf39` (`Add source-locked Hawaiian leader portrait trial`)  
Disposition: **blocked; do not convert to DDS or wire at runtime**.

## Verdict summary

| Gate | Verdict | Evidence and disposition |
|---|---|---|
| Archival provenance and rights | **PASS with documentation caveats** | The Commons page identifies David Kalākaua Kawānanakoa, 1925, Nellist (ed.), *The Story of Hawaii and Its Builders*, p. 560, unknown photographer, and United States public-domain status. The local master and crop hashes are stable. The manifest says “before 1 January 1931”; the current Commons statement says the 1925 publication predates 1 January 1930. The date is safe either way, but the wording should be reconciled before final publication. Metadata has `portrait_provenance: null`, so the attribution is not carried into the processor record. |
| Exact identity / likeness | **FAIL (non-compensable)** | The archival photograph is the correct 1904–1953 son, not the older David Kawānanakoa (1868–1908), but its forehead and most facial planes are clipped nearly white. The raw repaint reconstructs those missing planes, eye definition, gaze, cheeks, nose, jaw, and hair detail. At native and 4× nearest-neighbour review the result is a plausible adult male, not a verifiable exact likeness. |
| HOI4 painted leader style | **PASS visually** | Native `156×210` candidate is a restrained matte-painted country-leader portrait with a dark neutral background, readable head and shoulders, controlled palette, and no text, watermark, modern object, cinematic lighting, caricature, or meme treatment. This style pass does not override the identity failure or review-sheet evidence gaps. |
| Framing and output geometry | **PASS** | Source crop is exactly `(245,170,945,1112)` in source pixels (`700×942`), with head, both shoulders, collar, and tie. Candidate is clean vertical `156×210`. No extra person or gender ambiguity was observed. |
| Male-only / gender metadata | **PASS** | Source, raw result, and processed candidate show one adult male-presenting subject. The existing vanilla leader has no female metadata. No female pool or opposite-gender pairing is involved. |
| Role and consumer boundary | **PASS for the proposed boundary; no current runtime consumer** | Vanilla HAW history already creates the exact ruling leader name `David Kalakaua Kawananakoa` with picture token `GFX_portrait_David_Kalakaua_Kawananakoa`. Event 006 preserves the vanilla roster and does not recruit, promote, retire, or replace HAW leaders. The only safe proposed consumer is a package-gated full-size country-leader override during exact IW-173 HAW setup. No advisor, dossier, `_small`, commander, operative, or unrelated HAW use is authorized. |
| Runtime authorization | **HOLD** | Runtime admission requires every non-compensable gate to pass. Identity fails; the processor sheet is not compliant evidence; no DDS or `.gfx` override exists. Keep the vanilla generic portrait active and the candidate export-only. |

## Source, crop, and provenance evidence

Package root: `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_24/hawaii_kawananakoa_trial_01/`.

- Immutable source: `source_crops/../sourced_portrait_replacements_2026_07_22/pacific_asante_sokoto/HAW_david_kalakaua_kawananakoa_1925_original.jpg`; dimensions `1109×1700`; SHA-256 `E23304AFA45091FA6B7FF0179CAA688BCD7EE0027306B22E853A14C1344DA909`.
- Canonical source page: <https://commons.wikimedia.org/wiki/File:David_Kalakaua_Kawananakoa.jpg>.
- Archived original URL recorded in the manifest: <https://upload.wikimedia.org/wikipedia/commons/archive/e/eb/20180819043404%21David_Kalakaua_Kawananakoa.jpg>.
- Commons attribution identifies the target as David Kalākaua Kawānanakoa (1904–1953), published in George F. M. Nellist (ed.), *The Story of Hawaii and Its Builders*, Honolulu Star-Bulletin, 1925, p. 560, photographer unknown. The Commons page currently describes the work as United States public domain because the 1925 publication predates 1 January 1930. The manifest’s 1931 cutoff wording is stale but does not change the 1925 result.
- Target identity cross-check: <https://en.wikipedia.org/wiki/David_Kal%C4%81kaua_Kaw%C4%81nanakoa> records the target as born in 1904 and deceased in 1953. The older father is separately documented as David Kawānanakoa (1868–1908): <https://en.wikipedia.org/wiki/David_Kaw%C4%81nanakoa>. The archival caption and Commons record point to the target, so this is not a wrong-father substitution.
- Exact crop file: `source_crops/HAW_david_kalakaua_kawananakoa_1925_head_shoulders.png`; crop rectangle `(245,170,945,1112)`; dimensions `700×942`; SHA-256 `A17E6323055F7490DB7DEB768C409A466D501888FD242B3CECC390A4AF22F6E2`.
- Independent pixel comparison confirmed that the crop file is the exact source-pixel rectangle. The crop is source evidence only and must not be treated as a runtime portrait.
- Prompt: `prompts/HAW_david_kalakaua_kawananakoa_trial_01.md`. It correctly makes the exact crop the identity input and names the AFG Mohammed Zahir Shah and IRE Eamon de Valera images as style-only references. It explicitly forbids beautification, slimming, aging, de-aging, symmetrization, genericization, invented facial details, invented insignia, and extra consumers.
- The prompt is a written source lock, not a provider-side generation log. The processor metadata has no generation provenance object (`portrait_provenance: null`) or render configuration. Treat provider-level source-lock evidence as incomplete even though the package manifest and prompt are clear.

## Artifact and deterministic-processing evidence

- Raw ImageGen result: `imagegen_results/HAW_david_kalakaua_kawananakoa_identity_preserve_trial_01.png`; `1073×1466`; SHA-256 `84CBE0D5083EC2C2E7F361874867DAE0E05C06F528F000DE435D274CB1576F01`.
- Deterministic processor: `.agents/skills/chaos-redux-event-assets/tools/advisor_icon_processing.py`, version `5.0`, SHA-256 `c6e78c01c025ad57fef8dc25eb79bd216ff9809df27e4c758eb9ec72594a3963`; render version `2.0`; Python `3.9.12`; Pillow `11.1.0`; mode `leader`; source kind `real`; raw crop `(0,10,1073,1455)`; canonical leader reference directory `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders`.
- Candidate: `processed_png/portrait_HAW_david_kalakaua_kawananakoa.png`; `156×210`; file SHA-256 `88EA77261859DE81D1E5082802EA83DA3C79C646C2E200CA0495C9401887F607`; decoded RGBA SHA-256 `93378ed10b29fcac1df50290aca2e01f105df465bdfe0ac0bf8f812867f47038`.
- Metadata: `metadata/HAW_david_kalakaua_kawananakoa_processing.json`; file SHA-256 `0C6D9AB93845841A5C66A4B8DFA0622E2AC369E5E81915E01B68BA33E081FDBE`; canonical metadata payload SHA-256 `f4be4dad182579b74c9a16c1bc8f0ad78d69f5555614e73d05d1274b170c9d0c`; normalized command arguments SHA-256 `f234f104f20a657f4b98f2b2010ce406d704c85e584c25ab21fccc5ac0ac716a`; raw decoded seed hash `5d550ba59aefe4678e10f7ad3beac4fbf8f169a428c33c8c3b2f346150280a1c`. Recomputed file, decoded-pixel, processor, command, and metadata-integrity hashes matched the recorded values.
- Processor review sheet: `review_sheets/HAW_david_kalakaua_kawananakoa_processor_style_comparison.png`; file SHA-256 `710B281C326101FE643D35DE5D9079036F17DBF6A5441AB91C923C16355862A4`; decoded RGBA SHA-256 `176e83820bc696d9eb24d066f8d2e3dbc3a5e645b52ff02bb7b6a7429dbd1a50`.

## Native and 4× nearest-neighbour visual review

The immutable source, exact crop, raw result, processed candidate, review sheet, and the package’s AFG/IRE style references were inspected at native resolution. Temporary 4× nearest-neighbour enlargements of the source full page, exact crop, raw result, processed candidate, and all four reference candidates were inspected outside the repository and then removed; no package image was altered.

- The source full page and exact crop show the correct photographed man with swept dark hair, brows, eyes, nose, mouth, jaw, high white collar, light formal shirt, and dark tie. The forehead and almost all central facial modelling are blown out to white. The mouth, nose edge, eye placement, and hairline remain the strongest source cues.
- The raw result is a coherent painted adult male with the expected swept hair, high collar, dark tie, and quiet dark background. It necessarily invents or reconstructs forehead/skin planes, brows, eye openings and gaze, nose shading, cheeks, jaw modelling, and hair fill that are not recoverable from the clipped source.
- The native candidate remains readable as an HOI4-style country leader with head and both shoulders. At 4× nearest-neighbour, the painted texture is stable and there is no extra person or gender ambiguity, but the face reads as a generic reconstruction because the source cannot prove the reconstructed planes. This is an identity/likeness failure, not merely a small-resolution artifact.
- The AFG/IRE references are visibly restrained HOI4 painted leader portraits. The candidate is stylistically within that family, but those references must remain style-only and cannot repair identity evidence.
- No invented uniform, medal, jewelry, insignia, facial hair, scar, modern prop, text, border, watermark, or cinematic lighting was observed in the candidate. The white collar and dark tie are source-visible clothing cues.

## Review-sheet evidence defect

The package review sheet is not sufficient as an independent source-lock/style comparison artifact.

- `advisor_icon_processing.py:3978-4001` hard-codes leader references `den_thorvald_stauning.png` and `fin_carl_mannerheim.png`, uses `scale = 2`, and enlarges leader panels with Lanczos. It does not use the manifest/prompt’s AFG/IRE style references and does not provide the required 4× nearest-neighbour leader evidence.
- `advisor_icon_processing.py:4089-4093` loads and crops the processor `--source` input; the package metadata records the raw ImageGen result as that input. Therefore the review sheet’s panel labelled `explicit source crop` is a crop of the raw painted result, not the immutable archival source crop. The archival crop was inspected separately above, but the sheet label is misleading.
- This is an audit-evidence defect, not an instruction to patch the processor or regenerate the package in this handoff. A future trial must produce a review sheet that visibly includes the immutable crop, the candidate, the declared style-only references, and the mandated native/4× NN views with accurate labels.

## Country package and consumer crosswalk

| Surface | Finding |
|---|---|
| Vanilla HAW history | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/HAW - Hawaii.txt:60-62` creates `David Kalakaua Kawananakoa` with `picture = GFX_portrait_David_Kalakaua_Kawananakoa`. No vanilla history edit is authorized. |
| Current vanilla sprite | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/_leader_portraits.gfx:7961-7963` maps that token to `gfx/leaders/Asia/Portrait_Asia_Generic_land_5.dds`; this generic sprite remains active while the trial is blocked. |
| Event 006 HAW preservation | `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt:37-44` requires the ruling-only vanilla leader name and states Event 006 never recruits, promotes, retires, or replaces HAW leaders. |
| Mod character roster | `common/characters/006_independence_wave_pacific_characters.txt:8-9` keeps the complete vanilla HAW legacy roster untouched; custom characters are HBX/FSM only. |
| Mod portrait interface | `interface/006_independence_wave_pacific_portraits.gfx:1-19` defines HBX/FSM portraits only. `rg` found no HAW override, DDS, `_small`, advisor, dossier, commander, or operative consumer. |
| Package docs | `docs/events/006_independence_wave/pacific_country_packages.md`, `docs/specs/006_independence_wave_specs/quality/simplifications_omissions_and_blockers.md`, and the Event 006 source-of-truth/resume docs consistently record HAW as gameplay-retained but visual admission withdrawn pending a sourced actual-man portrait. |

## Country-package coverage checklist

- Tag and exact leader identity: **covered** (`HAW`; existing vanilla name and picture token).
- History, state, capital, politics, parties, and roster: **preserved and out of scope for this portrait trial**; no edits made.
- Portrait role mapping: **covered for the proposed single full-size country-leader consumer only**; no other HAW portrait role is authorized.
- Localisation, advisor names, focus/decision/idea hooks, flags, map setup, army/technology/industry/supply, and AI: **unchanged and not implicated by the candidate**.
- Runtime `.gfx`/DDS asset: **intentionally absent while blocked**.

## Final authorization and remaining risks

This candidate is **not runtime-authorized**. Do not convert it to DDS, add an HAW `.gfx` override, change vanilla HAW history, or broaden the consumer set. The main blocker is exact likeness: the source’s clipped facial highlights leave too little geometry for a source-locked repaint to prove the target identity, and the generated result reconstructs the missing face. The processor review sheet also needs a compliant evidence rebuild before any future trial can be considered.

No gameplay, localisation, interface, vanilla, or package image files were changed by this audit. No broad identity redesign or plan handoff was written; the candidate remains export-only under the existing package-gated boundary.
