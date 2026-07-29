# Event 006 CHU grounded portrait candidates — independent visual and provenance audit

Reviewer: Codex independent asset-audit subagent `/root/event6_chu_portrait_visual_audit`.
Review date: 2026-07-29 (Europe/Kyiv).
The reviewer did not produce either source photograph, ImageGen repaint, or deterministic processor output.
No DDS, `.gfx`, localisation, character, country, event, or gameplay file was created or edited by this audit.

## Decision

Both processed `156x210` portraits pass the direct visual gates for likeness, HOI4 leader-family style, framing/artifacts, and male identity.
Neither package is runtime-approved because source-rights/provenance and route-role decisions remain separate unresolved gates.
Keep both candidates as evidence only and do not convert, wire, or promote them from this audit.

| Candidate | Role family | Likeness | HOI4 painted style | Framing/artifacts | Male identity | Source/provenance | Era/role fit | Overall disposition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ahmet Zeki Velidi Togan / CHU river security directorate | leader | `PASS` | `PASS` | `PASS` | `PASS` | `NEEDS_USER_REVIEW` | `NEEDS_USER_REVIEW` | `NEEDS_USER_REVIEW`; visual pass only, no promotion |
| Musa Dzhalil / CHU Bolgar civic presidium | leader | `PASS` | `PASS` | `PASS` | `PASS` | `NEEDS_USER_REVIEW` | `PASS` with broad-date uncertainty retained | `NEEDS_USER_REVIEW`; visual pass only, no promotion |

Identity is a separate non-compensable gate, and the visual passes above do not override an unresolved rights, source-authority, ownership, or route-role gate.

## Scope and method

I compared each unchanged source master, exact decoded-pixel crop, raw original-size repaint, deterministic `156x210` candidate, and processor review sheet at native size and at a 4x nearest-neighbour inspection scale.
The review sheet was treated as supporting evidence only and not as a substitute for the direct source-to-candidate comparison.
I also read the crop-equality JSON, processing metadata, dedicated grounded-repaint provenance JSON where present, repaint prompt, current asset manifest/hash ledger, and the canonical leader reference README, catalog, contact sheet, and selected references under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/`.
The canonical references supplied only HOI4 brush, value, palette, and framing controls and did not supply either subject's face.

## Candidate evidence

### Ahmet Zeki Velidi Togan — river security directorate

| Evidence | Path | Dimensions / mode | SHA-256 | Evidence state |
| --- | --- | --- | --- | --- |
| Immutable source master | `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/med_eurasia_gap_retry/source_masters/volga/chu_validi_bashkortostan.jpg` | `709x945` RGB JPEG | `23d3403f15b766107458361891ff3e010b5cfde3f85ff80c0efaf204b4bc6026` | Reopened unchanged; archival male source |
| Exact source crop | `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/source_crops/CHU_river_security_directorate_validi_togan_head_shoulders.png` | `490x660` RGB PNG | `176605c568311b75dcc515a405906fc2e5de0b08f61b7e368ed92db3ef529c5c` | Crop `(130,70,620,730)`; `decoded_pixels_equal: true` |
| Raw ImageGen repaint | `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/repaints_raw/CHU_river_security_directorate_validi_togan_hoi4_repaint_v1.png` | `1080x1456` RGB PNG | `b806376672a5ce9b36dc24f34ad00f7b0d114cec1839da300136484758328a1b` | Original-size source-locked repaint retained |
| Deterministic candidate | `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/repaints_processed/CHU_river_security_directorate_validi_togan_156x210_candidate.png` | `156x210` opaque RGBA PNG | `12df637dcb7302f7d7ad9b752e6a3bfde29f438a4575fd65779cea5af3fd57f8` | Processor output; alpha extrema `(255,255)` |
| Processor review sheet | `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/review/CHU_river_security_directorate_validi_togan_processing_review.png` | actual `1344x464` opaque RGBA PNG | `36319395ae6899fb12d0e0b6d37fc548b20218a9447c7c759b2d73c0dc915f8b` | Review evidence only |

The crop metadata is `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/crop_metadata/CHU_river_security_directorate_validi_togan_crop.json`.
The deterministic processor record is `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/processing_metadata/CHU_river_security_directorate_validi_togan_156x210.json`.
The grounded source-to-raw record is `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/processing_metadata/CHU_river_security_directorate_validi_togan_repaint_v1_provenance.json`.
The identity-preserving prompt is `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/repaint_plans/CHU_river_security_directorate_validi_togan_hoi4_repaint_v1_prompt.md`.

### Musa Dzhalil — Bolgar civic presidium

| Evidence | Path | Dimensions / mode | SHA-256 | Evidence state |
| --- | --- | --- | --- | --- |
| Immutable source master | `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/med_eurasia_gap_retry/source_masters/volga/chu_musa_dzhalil_commons_1930s.jpg` | `594x931` RGB JPEG | `c7e92f3b1e939cfcfcc67a06ab455ab101b8f04509aab75a245d7da97a74869f` | Reopened unchanged; archival male source |
| Exact source crop | `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/source_crops/CHU_bolgar_civic_presidium_musa_dzhalil_head_shoulders.png` | `472x825` RGB PNG | `9a50cda37b2be6754c1722c4379eb9272adf36a8dd0f12cb11f2108922d64eb0` | Crop `(58,15,530,840)`; `decoded_pixels_equal: true` |
| Raw ImageGen repaint | `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/repaints_raw/CHU_bolgar_civic_presidium_musa_dzhalil_hoi4_repaint_v1.png` | `948x1659` RGB PNG | `491726ea93d4507d8327a4505fa0aaa14dfb13fb62b5b1be53490fa86d1a2b13` | Original-size source-locked repaint retained |
| Deterministic candidate | `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/repaints_processed/CHU_bolgar_civic_presidium_musa_dzhalil_156x210_candidate.png` | `156x210` opaque RGBA PNG | `669ccdc9d345659f260b5f4f03c8786f0b06eac2d5c9ce84c4bf8ae13b272015` | Processor output; alpha extrema `(255,255)` |
| Processor review sheet | `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/review/CHU_bolgar_civic_presidium_musa_dzhalil_processing_review.png` | `1344x464` opaque RGBA PNG | `9ce81849f48ec386fd7db2a5d79a3d313c386c7c8aceefcd3587777a74069d69` | Review evidence only |

The crop metadata is `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/crop_metadata/CHU_bolgar_civic_presidium_musa_dzhalil_crop.json`.
The deterministic processor record is `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/processing_metadata/CHU_bolgar_civic_presidium_musa_dzhalil_156x210.json`.
The grounded source-to-raw record is `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/processing_metadata/CHU_bolgar_civic_presidium_musa_dzhalil_repaint_v1_provenance.json`.
The identity-preserving prompt is `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/repaint_plans/CHU_bolgar_civic_presidium_musa_dzhalil_hoi4_repaint_v1_prompt.md`.

## Visual findings

### Togan likeness and male identity — `PASS`

The source-visible high forehead and receding close-cropped hair, round wire spectacles, narrow moustache, serious closed mouth, asymmetrical eye placement, head angle, and dark period collar remain identifiable in the raw repaint and deterministic candidate.
The face is slightly warmed and rounded by the painted treatment, but the repaint does not substitute a different face, erase the source asymmetry, beautify into a generic official, or invent hidden facial detail.
The candidate remains clearly male at native `156x210` and at the 4x inspection scale.

### Togan HOI4 style, framing, and artifacts — `PASS`

The raw repaint has visible restrained brush texture rather than a filtered photograph, with a quiet olive/charcoal background and controlled contrast compatible with the canonical leader family.
The candidate is a full head-and-shoulders/upper-bust leader portrait with readable spectacles, collar, and face at native size.
No text, watermark, border, extra person, modern prop, unsupported insignia, dossier frame, transparent fringe, or clipping artifact is visible.
The processed PNG is fully opaque, which is appropriate for a full leader portrait texture.

### Musa likeness and male identity — `PASS`

The source-visible young face, swept side-parted hairline, rounded cheeks, dark eyes, nose and mouth geometry, head angle, light suit, white collar, and dark tie remain present in the raw repaint and candidate.
The painterly result slightly enlarges the eyes and softens the cheek transitions, but preserves the source gaze, hair silhouette, facial asymmetry, and expression closely enough to remain the same identifiable man rather than a generic replacement.
The candidate remains clearly male at native `156x210` and at the 4x inspection scale.

### Musa HOI4 style, framing, and artifacts — `PASS`

The raw repaint has an unmistakably painted surface with muted slate, cream, and charcoal values that fit the canonical leader family without copying a reference face.
The candidate keeps a clean centered head-and-shoulders/upper-bust frame, readable suit and tie, and no invented route emblem or military mark.
No text, watermark, border, extra person, modern prop, advisor/dossier treatment, transparent fringe, or clipping artifact is visible.
The processed PNG is fully opaque, as expected for a leader portrait.

## Source, provenance, and route-role gates

### Togan — `NEEDS_USER_REVIEW`

The grounded source chain is structurally complete: the provenance record pins the archival master hash, exact crop and crop metadata, external ImageGen output evidence, raw repaint hash, deterministic candidate hash, processor, leader reference family, and evidence-only runtime status.
The source ledger attributes the photograph to the Bashkortostan State Assembly/Kurultai museum source and a Commons public-domain mark, but the photographer is unknown and the date is only estimated as the 1920s.
The separate rights/source gate therefore remains `NEEDS_USER_REVIEW`; this is not a visual failure and the candidate must not be promoted until the parent confirms the rights disposition.
The subject is Ahmet Zeki Velidi Togan, a Bashkir political and military leader alive in the 1936 baseline, so the era fit is good.
The route-role gate remains `NEEDS_USER_REVIEW` because the fictional CHU river directorate is a Volga/Tatar/Bashkir continuity route and the parent must explicitly accept this Bashkir-to-CHU transfer rather than assuming a narrowly Tatar identity.
No unsupported Bashkir/Tatar flag, religious symbol, or military insignia was introduced by the repaint.
The current 2026-07-28 package manifest records the review sheet as `1344x504`, while the decoded file is `1344x464`; correct this metadata mismatch before promotion.
The shared `hashes.sha256` ledger records the Togan source and crop but not the newly retained raw repaint, processed candidate, or review-sheet hashes; the dedicated provenance and processing records are present but the package ledger should still be reconciled.

### Musa — `NEEDS_USER_REVIEW`

The grounded source chain is structurally complete: the dedicated provenance record pins the Commons source page and original, museum credit, source date label, master and exact-crop hashes, generation evidence, raw repaint hash, processed candidate hash, processor, leader reference family, and evidence-only runtime status.
The source is a clearly attributable male photograph of Musa Dzhalil, a Tatar poet and political worker who lived through the 1936 baseline and is regionally direct for the Bolgar civic-presidium route.
The source ledger records a Wikimedia Commons public-domain designation and `collections.museum.tatar.ru` credit, but the author is unknown and the underlying museum page does not provide a separate explicit reuse license in the retained evidence.
The rights/source gate therefore remains `NEEDS_USER_REVIEW`; this is separate from the visual `PASS` and should be resolved before any DDS conversion or runtime wiring.
The era/role fit is `PASS` with the broad `1930s` source-date uncertainty retained because the subject is alive in the baseline, the suit is source-visible and period-appropriate, and the civic/political role is direct.
The current 2026-07-28 package `manifest.md` and `hashes.sha256` do not yet contain a Musa candidate row or raw/candidate/review hashes, although the dedicated provenance JSON does; append the candidate to the durable asset ledger and record the required subject-ownership search evidence before promotion.

## Canonical reference evidence

The leader-family references used by the processor and this audit are `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/den_thorvald_stauning.png` (`156x210`, SHA-256 `08732002182bdcb2bff3d78b142cc2b3d75adbdb29d4115f9e89ca5bdc6a21b6`) and `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/fin_carl_mannerheim.png` (`156x210`, SHA-256 `7e78e33e0b691b96b584393f2d363c07a302320f7e6300bda0fff261aa98d49e`).
Both candidates use these references for painted leader-family style only; neither reference supplies identity, clothing, or route symbolism.

## Parent follow-up and no-wire boundary

1. Resolve the Togan museum/Commons rights status and explicitly approve or reject the Bashkir-to-CHU river-directorate role transfer.
2. Resolve the Musa Commons/museum rights status and record the exact source-authority and subject-ownership search evidence for the Bolgar civic-presidium consumer.
3. Reconcile `manifest.md` and `hashes.sha256` with both candidates, including actual review-sheet dimensions and raw/candidate/review hashes.
4. Keep both processed PNGs, raw masters, crops, metadata, and review sheets in distinct evidence paths while the source gates remain open.
5. Only after the applicable source gates are independently resolved may the parent run the repository-standard DDS converter and wire the reserved leader sprite paths.

No DDS/GFX/gameplay wiring was performed by this audit, and no visual fallback or generated substitute was used.
