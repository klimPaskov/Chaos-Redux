# Event 006 IW-002 Wales Lewis Pugh Evans trial 01 visual audit

Audit date: 2026-07-24
Auditor: independent Chaos Redux country-package subagent
Scope: read-only audit of the immutable Evans source master and exact crop, raw ImageGen result, `156x210` processed candidate, source/trial manifests, canonical commander references, ownership evidence, stable WLS consumer, and live portrait surface. No source, processed art, DDS, GFX, gameplay, localisation, or fallback file was changed.

## Verdict

**FAIL closed — `blocked`; do not convert to DDS or wire.**

The archival identity, male role, Welsh connection, explicit crop, and broad HOI4 painted treatment are usable evidence, but the raw repaint and native candidate do not preserve Evans's identity tightly enough. The face becomes more frontal and generic: the source's narrow deep-set asymmetric eyes are opened and brightened, the asymmetric ear exposure is regularised, the long straight narrow nose becomes shorter and rounder, the thin horizontal moustache becomes thicker and wider, the lean long face and pointed chin become broader and softer, and the source age lines, off-centre gaze, and restrained alert expression are smoothed or changed. Style quality cannot compensate for this separate likeness failure.

The package also has a commander-reference evidence failure. `processing_metadata.json` records `mode: leader` and `reference_dir: .../portraits/leaders`; the generated review sheet uses `den_thorvald_stauning` and `fin_carl_mannerheim` leader references, while this consumer is a corps commander and the prompt's style-only inputs are the separate commander references Montgomery and Witzleben. This is not commander-family proof and must be corrected in a future trial before any PASS claim.

## Gate checklist

| Gate | Verdict | Evidence and finding |
|---|---|---|
| Provenance and rights | **PASS with disclosed caveat** | Immutable IWM `HU 93411` master and direct crop are retained and hash-verified. The source manifest records Commons Public Domain/Public Domain Mark, IWM/Barnett credit, source links, and the territorial Crown-copyright/non-commercial caveat. Preserve the credit and re-check target-territory treatment before release. |
| Male-only compliance | **PASS** | The source, raw result, and candidate each show one male-presenting subject only. No female, second person, advisor, dossier, or institutional body appears. |
| Historical/role fit | **PASS with role caveat** | Lewis Pugh Evans was Welsh-born and commanded the 159th Welsh Border Infantry Brigade from 1933 through January 1938, so he was alive in the 1936 start and fits a Welsh territorial commander. `mountain_frontier` is a package terrain/defence abstraction, not evidence of specialist mountain-branch service. The circa-1918 source age is retained rather than invented forward-aging. |
| Explicit head-and-shoulders crop | **PASS** | The direct source crop is `(95,25)-(540,505)`, `445x480`, and contains cap, unobstructed face, neck, both shoulders, collar, and upper tunic without unrelated people or text. |
| Likeness and identity preservation | **FAIL** | Eyes, ears/asymmetry, nose, moustache, face shape/chin, age texture, gaze, and expression drift materially in the raw repaint and remain visible at native `156x210`. The candidate is recognisably inspired by Evans but is not acceptance-grade exact identity preservation. |
| HOI4 painted commander style | **PASS visually; evidence gate FAIL** | The raw and candidate are genuinely painted, subdued, period-military, vignetted, and readable at `156x210`, with no text, watermark, modern prop, or meme treatment. The retained style sheet is leader-family evidence, not commander-family evidence, so the role-specific style gate is not complete. |
| Head-and-shoulders framing | **PASS** | The candidate is exactly `156x210`, keeps both shoulders and upper tunic readable, and leaves a small margin above the cap. |
| Ownership | **PASS** | The source package's exact/variant search found no Evans person, portrait, recruitment, or localisation owner in current Chaos Redux, installed vanilla, or approved reference mods. No transfer guard is needed. |
| Stable WLS consumer | **PASS for declaration** | `WLS_independence_wave_mountain_commandant` is generated as a male corps commander in `common/scripted_effects/006_independence_wave_scotland_wales_package_effects.txt:276-300`; `GFX_portrait_WLS_independence_wave_mountain_commandant` is declared at `interface/006_independence_wave_region_01_portraits.gfx:66-69` and is assigned to civilian and army `large` only. |
| Advisor/dossier/`_small`/fallback absence | **PASS for trial/source packages; stale runtime risk disclosed** | Both named packages contain no DDS, GFX, advisor, dossier, `_small`, alternate, female, or fallback derivative. Current live WLS registration also has no `_small` sprite/file. Historical handoffs mention removed old dossier work, but those are not current package files. |
| Runtime readiness | **FAIL** | No current trial DDS or wiring exists, as required while blocked. A legacy full DDS remains at `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant.dds`; it decodes to an unrelated dark-haired generated man and must not be counted as Evans approval or used as a fallback. |

## Visual comparison record

I inspected the unchanged master and exact crop directly against the raw ImageGen result and processed candidate at native size and with 4x nearest-neighbour enlargements. The transient inspection files were created under `%TEMP%\\wls_evans_audit_4x` only and were not added to the repository or used as runtime art.

At native size, the candidate remains readable and painterly, but the face reads as a generic British officer when compared beside the source crop. At 4x nearest-neighbour, the source's narrow, deep-set eyes and uneven lids become rounder and brighter in the repaint; the source head turn and ear imbalance become near-frontal and more symmetrical; the source long, straight nose becomes shorter and bulbous at the tip; the source pencil moustache becomes a denser, broader moustache; the cheek planes and pointed chin become fuller and softer; and the source's age lines and slight off-centre alert gaze are reduced or replaced by a smooth direct expression. These are identity changes, not a mere colour-grade or crop difference.

The candidate's plain side cap and undecorated British/Welsh field tunic follow the prompt's deliberate insignia-removal boundary and do not introduce unsupported political symbols. That clothing simplification does not cure the face gate.

## Exact evidence inspected

### Required instructions and references

- `AGENTS.md`.
- `.agents/skills/chaos-redux-event-assets/SKILL.md` in full, including the grounded real-person gate, ownership gate, commander `156x210` requirement, and canonical reference rules.
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/README.md`.
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/CATALOG.md` commander rows.
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/contact_sheet.png` and the curated commander contact sheet.
- `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/README.md` and `REFERENCE_MANIFEST.md`.
- Required offline Paradox wiki core pages were consulted; no engine/script behavior was changed by this visual audit.

### Source and trial packages

- `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/wls_lewis_pugh_evans_source_retry/manifest.md`.
- `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/wls_lewis_pugh_evans_source_retry/ownership_scan.md`.
- `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/wls_lewis_pugh_evans_source_retry/processing_handoff.md`.
- `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/wls_lewis_pugh_evans_source_retry/gfx_handoff.md`.
- `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/wls_lewis_pugh_evans_source_retry/source_hashes.sha256`.
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_24/wales_lewis_pugh_evans_trial_01/manifest.md`.
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_24/wales_lewis_pugh_evans_trial_01/identity_repaint_prompt.md`.
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_24/wales_lewis_pugh_evans_trial_01/processing_metadata.json`.
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_24/wales_lewis_pugh_evans_trial_01/hashes.sha256`.
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_24/wales_lewis_pugh_evans_trial_01/review/WLS_lewis_pugh_evans_style_sheet.png`.

### Image dimensions and hashes

| Evidence | Dimensions/mode | SHA-256 |
|---|---:|---|
| `source_masters/WLS_lewis_pugh_evans_iwm_hu93411_c1918.jpg` | `605x800` RGB | `FDFDE87660F50EB9A2112186878FB8EE93B7C1F0E2CB9F533CA9B2C41C26012C` |
| `source_crops/WLS_lewis_pugh_evans_iwm_hu93411_head_shoulders.png` | `445x480` RGB | `B16812C1B58AF568EAC7E74EC64E592CC34DD793CC2DB3A8D261D85168A2C064` |
| `imagegen_results/WLS_lewis_pugh_evans_identity_preserve_trial_01.png` | `1023x1537` RGB | `EBEDCB468C4BB724324277C922605BA538F6762230159025AABA04771BC4CFB8` |
| `processed_png/portrait_WLS_independence_wave_mountain_commandant.png` | `156x210` RGBA, alpha `255..255` | `EC90604F265225A6ED65BEC91612F4C7191D9AFEBDAF742C1F3F039D189D0091` |
| `review/WLS_lewis_pugh_evans_style_sheet.png` | `1344x464` RGBA | `23B03C86CB9FF0B76F74888BE32B7A52B926E38435CD5CB0F60269E4340B5970` |

The trial master and crop are byte-identical to the corresponding source-package copies. The processor file hash `C6E78C01C025AD57FEF8DC25EB79BD216FF9809DF27E4C758EB9EC72594A3963` matches the recorded metadata, but its leader-mode metadata and review references are the wrong role family for this commander.

### Commander references

- `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/commanders/eng_bernard_montgomery.png`, `156x210`, SHA-256 `39B03871D7451CA96712A5CCF3C056528693F82642776E6C5E297E041943944E`.
- `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/commanders/ger_erwin_von_witzleben.png`, `156x210`, SHA-256 `10F4A1108F9D440213F70FB5802349A2291F298F9D132644241119561577D5B6`.
- Canonical commander contact sheets are `930x900`; the vanilla sheet hash is `1A64051C0EF9C8A67A4E2FFD12A150F27A8A208F0AFFD37DC5964F8E2606227F` and the curated sheet hash is `AB02FAEF684F7B8B62806EC98EDB671B61A37DD806762D604155DB3119C3C8DE`.

The ImageGen prompt names Montgomery and Witzleben as style-only inputs, but the processor metadata and generated review sheet instead point at leader-family `den_thorvald_stauning` and `fin_carl_mannerheim`. The mismatched role evidence remains a blocking package-quality issue even though the painted candidate is broadly plausible.

## Ownership and runtime surface

The source package's ownership scan and independent exact/variant searches found no Evans owner in current Chaos Redux, installed vanilla, or the three approved reference mods. The stable WLS token is a generated male corps commander, not a cloned existing historical character.

The current full runtime sprite declaration is correct for the intended consumer, but the existing DDS is not this trial. `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant.dds` is a valid legacy `156x210` one-level BGRA texture (`131168` bytes; header dimensions `156x210`; SHA-256 `39B165970C8067F5E19BCCD756C2A9D90641F51632BDE68AF738E9CCB808DC4F`) that decodes to a dark-haired, unrelated generated man. It predates this trial and is not an approved Evans portrait. No `_small` DDS or `_small` GFX registration is present in the current runtime search.

## Required next step

Keep the immutable source and this trial blocked. A future candidate must preserve the source eye lids and asymmetry, ear exposure, long narrow nose, thin moustache, lean cheek/jaw shape, source age texture, head angle, and restrained gaze while retaining only the requested painted treatment. Rebuild the visual evidence against the canonical commander family rather than the leader-family processor references, then repeat the independent native and 4x nearest-neighbour likeness/style/provenance audit. Do not use the legacy runtime DDS as a fallback and do not create advisor, dossier, `_small`, female, generic, or alternate derivatives.

## Changed files and validation

- Changed documentation: this handoff and the trial `manifest.md` status/verdict line only.
- No source master, crop, raw ImageGen result, processed PNG, DDS, GFX, gameplay, localisation, or fallback asset was changed.
- Meaningful validation: SHA-256 and dimensions were rechecked for the master, crop, raw result, processed candidate, style sheet, and canonical commander references; master/crop byte equality between trial and source packages was verified; current WLS consumer and absence of live `_small` registration were searched; the legacy runtime DDS was decoded read-only for disposition.
- No DDS conversion, runtime load test, or gameplay test was run because the likeness and commander-reference gates fail and conversion/wiring are expressly prohibited for a blocked candidate.

Final disposition: **`blocked` / `FAIL`; no runtime advancement.**
