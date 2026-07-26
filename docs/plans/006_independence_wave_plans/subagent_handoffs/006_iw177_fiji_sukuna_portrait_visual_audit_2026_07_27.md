# Event 006 IW-177 Fiji Ratu Sir Lala Sukuna visual likeness, style, and provenance audit v18

Audit date: 2026-07-27.

Auditor scope: independent, read-only review of the retained Sukuna source crop, raw source-locked ImageGen repaint, deterministic `156x210` candidate, processor metadata and review sheet, and the canonical vanilla HOI4 country-leader reference family.

Overall disposition: **VISUAL GATES PASS (bounded) / PACKAGE `needs_user_review`; do not treat this handoff as runtime admission.**

This audit confirms a male head-and-shoulders country-leader/provisional-institution candidate with preserved source identity landmarks and a compatible HOI4 painted treatment.

The candidate remains held because the archival source is dated only to circa 1940s against Event 006's 1936-centered visual baseline, and the parent must explicitly accept that date before any final admission decision.

No DDS conversion, `.gfx` edit, gameplay edit, or localisation edit was performed by this audit.

## Evidence inspected

- Exact archival source crop: `docs/assets/006_independence_wave/fiji_source_clearance_2026_07_27/ratu_sir_lala_sukuna_crop.png`.
- Exact-crop equality record: `docs/assets/006_independence_wave/fiji_source_clearance_2026_07_27/ratu_sir_lala_sukuna_crop.json`.
- Raw source-locked repaint: `docs/assets/006_independence_wave/fiji_source_clearance_2026_07_27/imagegen_results/ratu_sir_lala_sukuna_identity_preserve.png`.
- Deterministic candidate: `docs/assets/006_independence_wave/fiji_source_clearance_2026_07_27/processed_png/ratu_sir_lala_sukuna_hoi4.png`.
- Processor metadata: `docs/assets/006_independence_wave/fiji_source_clearance_2026_07_27/metadata/ratu_sir_lala_sukuna_processing.json`.
- Processor comparison sheet: `docs/assets/006_independence_wave/fiji_source_clearance_2026_07_27/review_sheets/ratu_sir_lala_sukuna_processor_style_comparison.png`.
- Identity-preservation prompt: `docs/assets/006_independence_wave/fiji_source_clearance_2026_07_27/prompts/ratu_sir_lala_sukuna_identity_preserve_imagegen.md`.
- Source and rights ledger: `docs/assets/006_independence_wave/fiji_source_clearance_2026_07_27/source_manifest.json`.
- Existing asset handoff: `docs/assets/006_independence_wave/fiji_source_clearance_2026_07_27/gfx_handoff.md`.
- Canonical leader reference library and contact sheet: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/`.
- Processor-selected vanilla references: `den_thorvald_stauning.png` and `fin_carl_mannerheim.png`, both from the canonical leader directory.

The source master itself is retained and recorded by the manifest as `ratu_sir_lala_sukuna_source.jpg`; the visual comparison began from the immutable exact crop as required by the parent scope.

The retained crop, raw repaint, processed candidate, and canonical references were inspected at native scale, and the candidate plus canonical references were also inspected in a transient 4x nearest-neighbour enlargement for this audit; no transient inspection image was added to the repository.

## Separate gate results

| Gate | Result | Independent finding |
| --- | --- | --- |
| Grounded real-person source mode | **PASS** | Ratu Sir Josefa Lalabalavu Vanayaliyali Sukuna is a real historical Fijian statesman, so the package correctly uses an attributed archival photograph and a source-locked repaint rather than an invented portrait. |
| Source attribution and rights chain | **PASS, bounded** | The manifest identifies National Archives of Fiji as archive/author, Wikimedia Commons `File:Ratu Sir Lala Sukuna.jpg` as the preserved source page, and Commons `PD-Fiji` as the public-domain basis; the archive credit must remain attached to project documentation. |
| Source-date fit | **NEEDS_USER_REVIEW / BLOCKER** | The archive exposes only `circa 1940s`; this is later than the 1936 baseline and must not be described as a 1936 photograph. Parent acceptance of the date is required before runtime admission. |
| Exact source crop | **PASS** | The retained Pillow crop uses `(300,250)-(2220,2550)` from the `2520x3128` RGB master, produces a `1920x2300` RGB PNG, and records `decoded_pixels_equal: true` with matching decoded RGBA hashes in `ratu_sir_lala_sukuna_crop.json`. |
| Male-only identity | **PASS** | The source crop, raw repaint, and normalized candidate each show one male subject only, with no second person, female-presenting subject, institutional crowd, or advisor/dossier treatment. |
| Head-and-shoulders framing | **PASS** | The crop and repaint retain the full face, ears, neck, upper shoulders, dark suit, white shirt, and tie; the normalized candidate preserves a readable restrained bust at `156x210` without clipping the face or shoulders. |
| Identity likeness and preservation | **PASS, bounded** | Broad forehead, close-cropped hair, heavy brows, deep-set eyes, broad nose, thick moustache, strong jaw, cheek-fold geometry, ear exposure, facial asymmetry, slight head angle, source expression, and source-visible suit/shirt/tie remain recognizable from crop to raw repaint to native candidate. |
| Genericization or beautification | **PASS** | No clear face substitution, symmetry correction, beauty smoothing, age shift, ethnicity change, frontalized replacement, or generic officeholder face was observed at native or 4x inspection. The raw repaint adds painted color and texture but keeps the source-specific face structure. |
| Unsupported clothing, insignia, or hidden detail | **PASS, bounded** | The repaint retains the source-visible dark suit, white shirt, and tie without adding flags, medals, uniforms, ceremonial regalia, text, or unsupported symbols; the dark studio background is a style treatment rather than an identity claim. |
| HOI4 painted leader style | **PASS, bounded** | The raw and normalized outputs use subdued gouache/oil brushwork, controlled directional texture, muted brown-grey values, readable facial planes, and a quiet studio background consistent with the canonical leader family. The candidate is darker and warmer than the pale `Stauning` and `Mannerheim` references but remains in-family at `156x210`. |
| Native canvas and alpha | **PASS** | The normalized file is `156x210` RGBA with opaque alpha (`255..255`), matching the required full country-leader portrait surface; no dossier frame or small-portrait alpha construction is present. |
| Advisor/small derivatives | **PASS / none present** | The Fiji Sukuna package contains the full `156x210` candidate and review preview only; no `65x67`, `50x67`, `_small`, advisor, high-command, dossier, or other derivative was created or needed. The separate Vishnu Deo review assets are an alternate source candidate, not a Sukuna derivative. |
| Processor role evidence | **PASS** | `ratu_sir_lala_sukuna_processing.json` records `mode: leader`, `role_family: leader`, canonical `portraits/leaders` references, processor v5.0, render v2.0, and the expected `156x210` output. |
| Provenance continuity | **PASS, bounded** | The source master hash, exact crop coordinates/equality record, raw repaint hash, deterministic candidate hash, processor hash, prompt, review sheet, National Archives credit, and `PD-Fiji` basis are linked by `source_manifest.json`, the crop JSON, processor metadata, and `gfx_handoff.md`. The archive does not expose a precise capture date or photographer, and that uncertainty is retained rather than inferred away. |
| Ownership search evidence | **PASS for source package** | The manifest records searches for `Sukuna`, `Lala Sukuna`, `Josefa Lalabalavu`, `Vishnu Deo`, and `Vishnu_Deo` across current Chaos Redux and targeted vanilla roots with no existing character/leader/portrait ownership match returned. This visual audit does not create or transfer a character. |
| Runtime admission | **NOT AUTHORIZED** | The package currently records a provisional DDS/GFX consumer from parallel parent work, but this audit neither generated nor validated that runtime asset and does not promote it. The source-date decision, independent audit record, and parent route/package gates remain required. |

## Identity-preservation notes

The archival crop presents Sukuna in a slightly turned, asymmetrical head angle with a broad forehead, close-cropped hairline, heavy brow ridge, deep-set eyes, broad nose, thick moustache, strong jaw, visible cheek-fold geometry, and a distinctive ear/eye balance.

The raw repaint preserves those landmarks rather than replacing the face with a generic period statesman.

The moustache remains thick and dark, the broad nose keeps its source width and bridge, the jaw and cheek planes retain their relationship, and the slightly uneven eye/ear geometry remains readable after the painterly conversion.

The raw repaint keeps the source-visible dark suit, white shirt, and tie and does not invent a uniform, medals, flag, text, second person, or ceremonial prop.

The normalized candidate is darker at native size than the archival crop, but the moustache, brow silhouette, eye depth, nose, cheek fold, jaw, and head angle remain legible at `156x210` and in the 4x nearest-neighbour inspection.

The repaint necessarily converts a monochrome archival photograph into a muted brown-grey painted palette and softens some film grain and tooth/skin microtexture; this is a style conversion, not a face substitution.

## Vanilla style and framing notes

The processor review sheet contains the processor input crop, processed candidate, `den_thorvald_stauning`, and `fin_carl_mannerheim` in the canonical country-leader family.

The candidate follows the same full-portrait footprint and readable head-and-shoulders hierarchy as the two references, with a dark neutral background, controlled contrast, and visible brush texture instead of a raw or merely resized photograph.

The candidate is not an advisor or high-command card and must not be downsampled or recropped into a `65x67` or `50x67` surface.

## Provenance chain and date caveat

The preserved master is `docs/assets/006_independence_wave/fiji_source_clearance_2026_07_27/ratu_sir_lala_sukuna_source.jpg` (`2520x3128`, SHA-256 `8cf20454f59f8644b3c34dd9ea40a7e98cdf5b56113cd8bb918f893fc6cff5e5`).

The source ledger credits the National Archives of Fiji and the Wikimedia Commons file page `https://commons.wikimedia.org/wiki/File:Ratu_Sir_Lala_Sukuna.jpg`.

The direct original is recorded as `https://upload.wikimedia.org/wikipedia/commons/7/73/Ratu_Sir_Lala_Sukuna.jpg`, with the archive post retained as `https://www.facebook.com/NationalArchivesOfFiji/photos/a.124204611046400/124206027712925/`.

The rights basis is recorded as Commons `PD-Fiji` with `https://commons.wikimedia.org/wiki/Template:PD-Fiji`; preserve the National Archives of Fiji credit in any future durable documentation.

The source date remains `circa 1940s`; neither the archive record nor this audit upgrades it to 1936.

The source-date mismatch is the controlling blocker for admission even though Sukuna was active in Fiji politics in 1936 and the visual likeness/style gates pass.

If the parent requires strict contemporaneous 1936 imagery, retain the package as blocked and do not substitute a generated or wrong-era portrait.

## Hash and dimension record

| Artifact | Dimensions / mode | SHA-256 |
| --- | --- | --- |
| `ratu_sir_lala_sukuna_source.jpg` | `2520x3128` RGB | `8cf20454f59f8644b3c34dd9ea40a7e98cdf5b56113cd8bb918f893fc6cff5e5` |
| `ratu_sir_lala_sukuna_crop.png` | `1920x2300` RGB | `c19b8c31fcee03457645a4d35e5ad0453fffEEB76823a6da032fc14ac85faf7e` |
| `ratu_sir_lala_sukuna_crop.json` | exact-crop metadata JSON | `824e61ec0da9d71581d0d53505f0e5da5a6034d5084f65d92b4ba4d99c4fbf4b` |
| `ratu_sir_lala_sukuna_identity_preserve.png` | `1080x1456` RGB | `9fc14f99e64e7c32e34793fd1c2e71cc5cac94ce628f09047f64ce5ce324848a` |
| `ratu_sir_lala_sukuna_hoi4.png` | `156x210` RGBA, alpha `255..255` | `71062c2efe0e98d3de1de5e7d5600e2bc746b92f6560c44d62242c107b26951d` |
| `ratu_sir_lala_sukuna_processing.json` | processor metadata JSON | `e9390b1f9f65e1ebdcec36cadb94fc7f48c692f3391b25c2ab544a55d0228079` |
| `ratu_sir_lala_sukuna_processor_style_comparison.png` | `1344x464` RGBA | `872aa4eda2d2bc3fcb5910598ad57c682684b86efc7100798ff2a5e152dfde1a` |
| canonical leader `contact_sheet.png` | `1200x498` RGBA | `8966ae351d1fe8fc13d47ca1c59ec3d8a34da9101ce5fd65f7acff3421bd0401` |
| canonical `den_thorvald_stauning.png` | `156x210` RGBA | `08732002182bdcb2bff3d78b142cc2b3d75adbdb29d4115f9e89ca5bdc6a21b6` |
| canonical `fin_carl_mannerheim.png` | `156x210` RGBA | `7e78e33e0b691b96b584393f2d363c07a302320f7e6300bda0fff261aa98d49e` |
| `source_manifest.json` | source/provenance manifest JSON | `392970080a0b29582ab9698c6df33354ec1662d2b7f560c6e7a1a4e571a2bf96` |
| `gfx_handoff.md` | source/runtime handoff Markdown | `474e14557df29755d30fdd60fc9591f7bcde891dce97012102b3c36e7afe0166` |

The crop JSON records source master SHA-256 `8cf20454f59f8644b3c34dd9ea40a7e98cdf5b56113cd8bb918f893fc6cff5e5`, crop rectangle `(300,250)-(2220,2550)`, decoded pixel count `4416000`, and equal master-crop/output RGBA hashes.

The processor metadata records source-kind `real`, role family `leader`, processor SHA-256 `1adb521b43238ee971e093dae90007c4c44c600435ebb897c6482ba3b64b96ec`, Pillow `11.1.0`, CPython `3.9.12`, and `decode_after_save_pixel_equality: true` for the output and review sheet.

## Runtime boundary and blockers

The current source manifest and `gfx_handoff.md` record a provisional FIJ sprite/texture consumer from parent package work, including `GFX_portrait_FIJ_independence_wave_founding_congress_chair` and `gfx/leaders/006_independence_wave/portrait_FIJ_independence_wave_founding_congress_chair.dds`.

That provisional consumer is outside this read-only visual audit and is not evidence of final admission.

The provisional DDS hash recorded by the package is `31fea5eb5c7c4b6f34ec138ed6a3168a7c6c39755a992bd6abf0296c5838d2c6`; this audit did not generate, convert, decode, or approve that DDS.

The candidate must remain `candidate_requires_visual_approval` / `needs_user_review` until the parent accepts or rejects the circa-1940s source date for the 1936-centered IW-177 consumer and completes the parent country-package/formable route gates.

Do not create a second generated face, replace Sukuna with an invented officeholder, add an advisor/small derivative, or describe the provisional texture as runtime-admitted from this handoff.

## Changed files and validation

- Changed file in this subtask: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw177_fiji_sukuna_portrait_visual_audit_2026_07_27.md` only.
- No source master, exact crop, raw ImageGen repaint, processed PNG, processor metadata, review sheet, DDS, GFX, gameplay, or localisation file was changed by this audit.
- Read-only validation rechecked dimensions, image modes, alpha extrema, SHA-256 values, crop JSON equality evidence, processor role/reference metadata, and the current provisional runtime boundary recorded by the package.
- Native and 4x nearest-neighbour visual inspection confirmed source-specific facial landmarks, male head-and-shoulders framing, leader-family style, and the absence of advisor/small derivatives.

## Final handoff

The Sukuna candidate is visually acceptable as a source-locked male `156x210` HOI4 country-leader/provisional-institution portrait, with bounded PASS results for identity likeness, male-only framing, painted style, crop integrity, and National Archives of Fiji / `PD-Fiji` provenance continuity.

The circa-1940s source date remains a non-negotiable user/package decision against the 1936-centered Event 006 baseline.

Keep the source package and candidate held at `needs_user_review`; do not claim runtime admission, DDS approval, or final `.gfx` wiring from this audit.
