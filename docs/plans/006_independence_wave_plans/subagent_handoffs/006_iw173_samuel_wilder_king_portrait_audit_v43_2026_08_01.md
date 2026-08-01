# IW-173 HAW Samuel Wilder King portrait audit v43

**Date:** 2026-08-01

**Owner:** Independent Chaos Redux sourced visual asset auditor

**Scope:** Audit only the existing IW-173 HAW Samuel Wilder King grounded real-person portrait package at `docs/assets/006_independence_wave/hawaii_samuel_wilder_king_source_clearance_2026_07_26`.

**Runtime boundary:** No DDS, `.gfx`, localisation, gameplay, character, or roster file was created or changed by this audit.

## Outcome

**BLOCKED — not independently admitted and not runtime-promoted.** The archival source, rights/date/identity dossier, exact lossless crop proof, source-locked repaint, native candidate dimensions, and ownership search are supported. The full portrait gate remains blocked because the package does not retain the required 4x nearest-neighbour comparison evidence, the only review sheet is a producer-style native strip that omits the unchanged archival master, and the candidate metadata names a retired processor without an explicit face-placement/manual export record. No DDS exists, as expected for this evidence-only package.

## Gate matrix

| Gate | Status | Evidence and finding |
| --- | --- | --- |
| Grounded identity/source mode | **PASS** | The package correctly classifies Samuel Wilder King as a grounded real male officeholder and uses an attributed archival photograph rather than an invented portrait. |
| Rights, archive, and date | **PASS** | Commons API and page wikitext for `https://commons.wikimedia.org/wiki/File:Samuel_Wilder_King_(PP-74-9-002).jpg` identify Hawaiʻi State Archives call number PP-74-9-002, unknown author, date `between 1935 and 1943`, and `PD-US-no notice`/public-domain status. The U.S. public-domain rationale is retained; the archive reproduction-policy caveat remains and is not an image-specific licence. |
| Identity and role fit | **PASS** | U.S. House History, Art & Archives `https://history.house.gov/People/Detail/16344` identifies Samuel Wilder King (1886–1959) as a Honolulu-born Delegate from the Territory of Hawaii in the 74th–77th Congresses (1935–1943), which brackets the 1936 package date. |
| Immutable source master | **PASS** | `source_png/HAW_samuel_wilder_king_PP-74-9-002_original.jpg`, 826x1206 RGB JPEG, SHA-256 `cba16c7d7b3e0efdd36240ec945663947ad727e0536757ea7cbd72156b0dcde3`. The retained image is a period adult male in suit and tie with no modern or synthetic source artefact. |
| Exact decoded crop | **PASS** | `crop/HAW_samuel_wilder_king_head_shoulders.png`, 693x1055 RGB PNG, SHA-256 `f36cc6c4a02b44605dd01412a25b2e50996006239eeb3f95f162ce6e6e0130ea`; rectangle `[105, 80, 798, 1135]`. `crop/HAW_samuel_wilder_king_head_shoulders_crop.json`, SHA-256 `a763a27886e1a835269c8a0e02f8ce126bec56e51ce22043649137b25c099615`, records Pillow utility v1.0, `status=exact_source_crop_verified`, `decoded_pixels_equal=true`, 731115 pixels, and equal RGBA hash `29fa8ce7a34f3dd49304d8d560ef37158890bf7c7ea8931df3e0456d83095a5f`. Independent Pillow re-decode reproduced the equality and hash. |
| Source-locked HOI4 repaint | **PASS (native visual spot-check; provisional)** | `imagegen_results/HAW_samuel_wilder_king_identity_preserve.png`, 1018x1545 RGB PNG, SHA-256 `1e4c62368cb92103d1666991b8dcc087051aa19008ca45bec756a6d99ba76da6`. At native review scale it preserves the source three-quarter pose, combed dark hair/hairline, heavy brows, long nose, mouth, jaw/ear structure, civilian suit and tie, while using a restrained painted HOI4-like dark blue-gray background without added insignia, lei, flags, text, or modern props. Identity remains a separate non-compensable gate pending enlarged evidence. |
| Native style comparison | **PASS (provisional)** | `review_sheets/HAW_samuel_wilder_king_processor_style_comparison.png`, 1344x464 RGBA PNG, SHA-256 `0a23fd563d229990bf824319dda45087cd516c83b576c99f1c97dbfb6630beeb`, compares the generated input crop and 156x210 candidate against `portraits/leaders/den_thorvald_stauning.png` (SHA-256 `08732002182bdcb2bff3d78b142cc2b3d75adbdb29d4115f9e89ca5bdc6a21b6`) and `portraits/leaders/fin_carl_mannerheim.png` (SHA-256 `7e78e33e0b691b96b584393f2d363c07a302320f7e6300bda0fff261aa98d49e`). The candidate reads as a painted leader portrait at native size. |
| Deterministic 156x210 candidate | **BLOCKED (evidence incomplete)** | `processed_png/portrait_HAW_samuel_wilder_king.png` is 156x210 RGBA PNG, opaque alpha extrema `(255,255)`, SHA-256 `7eaec0ac8a6c8d5a9c3e623c1e56aa97b1b25ec1adc71070ab02c407e4539ad4`. `metadata/HAW_samuel_wilder_king_processing.json` is SHA-256 `06604964fd26bc50697fefcdc861c40229b8cc62146c3f83bcfc306b04c0c48d`, and its output decode-equality/hash evidence is internally consistent. However, its processor is recorded as `retired_advisor_card_processor_REMOVED`, `face_box` is `null`, and the command contains no explicit task-specific/manual crop or face-placement record. The size is correct, but this is not sufficient provenance for final admission under the current portrait workflow. |
| Required 4x nearest-neighbour review | **BLOCKED** | No enlarged review image, contact sheet, or audit sheet exists in the package. The only review file is the 1344x464 native strip above; it shows the generated input crop, not the unchanged archival master and exact crop as separate audit panels, and contains no 4x nearest-neighbour proof. |
| Independent likeness/style/provenance audit | **BLOCKED** | This v43 handoff is independent of the producer, but a complete PASS cannot be issued until the unchanged master, exact crop, raw repaint, processed candidate, and leader references are compared and retained at native and at least 4x nearest-neighbour. Native visual review found no obvious face substitution, genericization, unsupported clothing, or modern artefact; that observation does not waive the missing evidence gate. |
| Ownership/collision scope | **PASS** | Targeted exact/variant searches for `Samuel Wilder King`, `Samuel_Wilder_King`, `Wilder King`, and `Samuel King` across current project and installed-vanilla `common/characters`, `history/countries`, `gfx/leaders`, `interface`, and `localisation` returned no matches. Vanilla HAW still owns David Kalakaua Kawananakoa at `history/countries/HAW - Hawaii.txt:60,62` with `GFX_portrait_David_Kalakaua_Kawananakoa` at `interface/_leader_portraits.gfx:7961`; no Samuel owner or transfer guard was found. Do not clone or silently replace that roster entry. |
| Durable ComfyUI source/prompt pair | **BLOCKED / missing** | No `docs/assets/portraits/006_independence_wave/` durable queue or `portrait_HAW_samuel_wilder_king.png`/`.txt` pair is present. This does not change the source-rights result, but it is required before a grounded portrait proceeds through the full current workflow. |
| DDS and runtime admission | **BLOCKED / intentionally absent** | The package contains zero `.dds` files and its manifest/gfx handoff explicitly describe the PNG as evidence-only. DDS conversion and parent-owned `.gfx` wiring must wait for a complete independent audit PASS and an explicit HAW consumer decision. |

## Visual audit notes

The unchanged source is a single adult male with readable hairline, brows, eyes, nose, mouth, jaw, ear, neck, collar, shoulders, and period suit/tie. Bright forehead clipping and archival grain are visible source risks but do not invalidate the attribution or exact crop.

The raw repaint and candidate retain the source-visible pose, facial proportions, hairline, heavy brows, long nose, tight mouth, jaw, ear, and civilian clothing silhouette. The repaint is visibly painterly rather than a raw photograph or simple resize. I found no invented medals, Hawaiian lei, tropical prop, flag, text, watermark, or modern clothing in the retained raw/candidate views.

The existing native strip is useful style evidence but is not a complete likeness audit: it does not show the unchanged photograph and exact archival crop as separate panels, and it is not enlarged nearest-neighbour evidence. No 4x claim is made here.

## Required next action

1. Preserve the source master, crop, crop JSON, raw repaint, candidate, and current hashes unchanged.
2. Create the durable ComfyUI source/prompt pair using the eventual runtime portrait basename, if the parent keeps King as an accepted HAW consumer.
3. Replace or supplement the retired-processor metadata with a reproducible current task-specific/manual `156x210` export record that states crop, face placement, canvas operation, tool/version, and hashes.
4. Retain an independent audit sheet containing the unchanged master, exact crop, raw repaint, processed candidate, and `portraits/leaders/` references at native and at least 4x nearest-neighbour, then rerun the likeness/style/provenance review.
5. Only after that PASS and an explicit parent-owned HAW identity/consumer decision may the parent run the repository DDS converter and wire `.gfx`; this audit does not perform either operation.

**Simplifications, omissions, and blockers:** No source or rights substitution was made. The portrait remains incomplete for runtime use because the required 4x review evidence, complete current processing provenance, durable ComfyUI pair, final DDS, and parent-owned consumer decision are not present.
