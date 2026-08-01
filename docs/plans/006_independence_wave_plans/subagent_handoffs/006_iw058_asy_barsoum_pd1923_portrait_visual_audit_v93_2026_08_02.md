# IW-058 ASY Barsoum alternate PD-1923 portrait audit v93

Date: 2026-08-02 (Europe/Kyiv).

Reviewer: OpenAI Codex asset-source auditor `/root/event6_chu_bolgar_repaint_audit_v93b`.

Scope: independent review of the parent-produced Barsoum v1 repaint and deterministic `156x210` candidate from the alternate 1921 Paris-delegation source. The review compares the unchanged group-photo master, the exact lossless crop, the raw repaint, the native candidate, the package-local prompt and processing record, the durable ComfyUI pair, and the canonical male country-leader references. I did not produce the repaint or candidate. No DDS, `.gfx`, character, localisation, attestation, or runtime file was changed.

## Decision

**Overall verdict: HOLD as evidence-only; no DDS, GFX, or runtime promotion is authorized by this audit.** The candidate preserves the distinctive black rounded clerical hat, large dark beard and moustache, deep viewer-right eye shadow, three-quarter head direction, dark ecclesiastical clothing, and source-specific face silhouette. The visual likeness gate passes with a low-resolution/group-context caveat, the HOI4 leader style/framing gate passes, the provenance chain passes, and the alternate source record supplies explicit 1921 publication and `PD-1923` evidence. The candidate remains outside runtime because the source/candidate package is an alternate evidence retry, the parent explicitly requested no wire, and the source-rights record still needs the parent’s release acceptance rather than being treated as an automatic runtime grant.

Separate gate verdicts are **identity/likeness: PASS with low-resolution/group-context caveat**, **HOI4 leader style/framing: PASS**, **provenance/chain: PASS**, **rights/date: PASS with PD-1923/source-ledger caveat**, and **DDS/runtime promotion: BLOCKED by the no-wire scope**.

The visual pass is bounded to the source-visible anchors. The `320x385` crop is a small, soft panel extracted from a ten-person delegation photograph, so the repaint’s eye, nose, skin, and beard texture details are reconstructions rather than independently verified pixels. This does not show a material face substitution, but it does limit confidence in micro-geometry and requires the exact crop to remain the sole identity authority.

## Evidence reviewed

| Artifact | Dimensions/mode | SHA-256 or proof | Review use |
| --- | --- | --- | --- |
| `docs/assets/006_independence_wave/asy_portrait_source_retry_v92_2026_08_01/source_masters/ASY_ignatius_afram_barsoum_paris_1921.png` | 1728x1314 RGBA PNG | `ed5473dab88a27d4dd5736ab5b6136a95e1e9fef1622eff7005dd0e17ed7d9d9` | Unchanged 1921 Paris-delegation group master; Barsoum is the upper-row clerical figure with black hat and beard. |
| `docs/assets/006_independence_wave/asy_portrait_source_retry_v92_2026_08_01/source_crops/ASY_concordat_council_ignatius_afram_barsoum_paris_head_shoulders.png` | 320x385 RGBA PNG | `c91d7e97dc8fa06ed9dc3f7fa70b01b09be71ef53a60e07c29737728999d1555` | Exact head-and-shoulders identity crop used for the source-locked repaint. |
| `docs/assets/006_independence_wave/asy_portrait_source_retry_v92_2026_08_01/crop_metadata/ASY_concordat_council_ignatius_afram_barsoum_paris_crop.json` | JSON evidence | `2e1abb6d5194b4e3e1b2c1fab23befe6e0b500bc8d188e8af9602a24e13bef4a` | Crop rectangle `(650,85,970,470)`; `decoded_pixels_equal: true`; matching decoded RGBA hash `bfd331133613a2d62e4adf8e1267391ae55c6d003403e97679985dbd4b7e5e89`; Pillow 11.1.0 and utility v1.0 recorded. |
| `docs/assets/006_independence_wave/asy_portrait_source_retry_v92_2026_08_01/repaints_raw/ASY_concordat_council_ignatius_afram_barsoum_hoi4_repaint_v1.png` | 1144x1375 RGB PNG | `8b0251b0638340ef85fe4610efd2cafa70b561e6297490dcd07cac8d2707ef35` | Parent-produced source-locked HOI4 repaint; evidence only. |
| `docs/assets/006_independence_wave/asy_portrait_source_retry_v92_2026_08_01/repaints_processed/ASY_concordat_council_ignatius_afram_barsoum_156x210_candidate_v1.png` | 156x210 RGB PNG | `220e81c29b35963668bcc2de3d8340aec3047a74da6655fabcda07f26d59d595` | Deterministic native country-leader candidate; not DDS. |
| `docs/assets/006_independence_wave/asy_portrait_source_retry_v92_2026_08_01/repaints_processed/ASY_concordat_council_ignatius_afram_barsoum_156x210_processing_v1.md` | Processing record | `561f2e9d9953069fa329c49a9326313b4304a5b491126c7b607efa65f5c52df8` | Pillow `ImageOps.fit` LANCZOS, centered `(0.5,0.5)`, `bleed=0`, no enhancement, sharpening, grading, or alpha conversion. |
| `docs/assets/006_independence_wave/asy_portrait_source_retry_v92_2026_08_01/prompts/ASY_concordat_council_ignatius_afram_barsoum_hoi4_repaint_v1.txt` | Prompt record | `0643f7f9cc1368a68607932205c4d9c8e159f5f4a1019e76070499487641590e` | Source-locked prompt preserving hat, beard, shadow/asymmetry, clothing, framing, and the no-cross/no-insignia boundary. |
| `docs/assets/portraits/006_independence_wave/portrait_ASY_independence_wave_concordat_council_v2.png` | 1144x1375 RGB PNG | `8b0251b0638340ef85fe4610efd2cafa70b561e6297490dcd07cac8d2707ef35` | Durable ComfyUI source PNG; byte-identical to the raw repaint and not runtime storage. |
| `docs/assets/portraits/006_independence_wave/portrait_ASY_independence_wave_concordat_council_v2.txt` | Prompt TXT | `45def3f3b7fed575d70afffaa778d2ba261629dfcfd93b8c05137825b5937446` | Matching durable replacement prompt; queue state remains `comfyui_replacement_pending`. |
| `docs/assets/006_independence_wave/portraits_generated_png/ASY_concordat_council_ignatius_afram_barsoum_hoi4_repaint_v2.png` | 1144x1375 RGB PNG | `8b0251b0638340ef85fe4610efd2cafa70b561e6297490dcd07cac8d2707ef35` | Flat original-size shelf copy; byte-identical to raw v1 and evidence only. |
| `docs/assets/006_independence_wave/asy_portrait_source_retry_v92_2026_08_01/review/ASY_concordat_council_ignatius_afram_barsoum_full_chain_4x_v01.png` | 2400x1960 RGB PNG | `39e5d28088b63359968e6634e39220a9b0c4dfe5b587c976887dc7f55e0f8150` | Evidence-only sheet of source master, exact crop, raw repaint, native/4x candidate, and three canonical male leader references. |
| `docs/assets/006_independence_wave/asy_portrait_source_retry_v92_2026_08_01/review/ASY_concordat_council_ignatius_afram_barsoum_face_geometry_close_v01.png` | 2640x1140 RGB PNG | `27e8364181455ed67915e25731439cdaa24f4f2c7665a5a096f1b94af785b18f` | Nearest-neighbour close comparison of the source crop face, raw repaint face, and processed candidate face. |
| `docs/assets/006_independence_wave/asy_portrait_source_retry_v92_2026_08_01/review/ASY_concordat_council_leader_refs_native_4x_v01.png` | 2240x2320 RGB PNG | `8c7cd2c593e79f2e9a2c065ef34953de1ccb3d33e2e454ed2f74470e60e38317` | Six curated male country-leader references at native and 4x nearest-neighbour scale; style controls only. |
| `docs/assets/006_independence_wave/asy_portrait_source_retry_v92_2026_08_01/manifest.md` | Package manifest | `00d0c204ba0f9ac84c649b6392110c6ffbcf06d906ac4cdb645875850d5dff50` | Alternate source, rights, crop, repaint, durable-pair, and no-wire ledger. |
| `docs/assets/006_independence_wave/asy_portrait_source_retry_v92_2026_08_01/hashes.sha256` | Hash ledger | `9be705f21288fc024009fadb04d0d5c6ddb8926947f7bb509f8ec1b3dac9d47d` | Package hashes for source, crop, raw, candidate, prompt, processing record, durable PNG, and shelf copy. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw058_asy_portrait_source_retry_v92_2026_08_01.md` | Source-research handoff | `3b3a9eb196b5da75a3d9315c607b11655513efc0c36c53a83e02c73c6f1a2ca1` | Role/date, source URL, explicit 1921 publication, `PD-1923` record, and group-photo caveat. |

The canonical role family was `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/leaders/`. The six inspected native `156x210` references were `afg_mohammed_zahir_shah.png` (`f606bc3c6204e0dbd35d8edceb21f87ae6f93a0ae7ad657382c7e9043e8907a0`), `den_thorvald_stauning.png` (`08732002182bdcb2bff3d78b142cc2b3d75adbdb29d4115f9e89ca5bdc6a21b6`), `eth_haile_selassie.png` (`e06bc1bd67ce70e1fb22e39d4c6d2732327d23a58efeb74b096b456318b7eb4b`), `fin_carl_mannerheim.png` (`7e78e33e0b691b96b584393f2d363c07a302320f7e6300bda0fff261aa98d49e`), `ice_sveinn_bjornsson.png` (`860726d268873f21ae0dbd6fb170482f50fad6393882b97b2b7b7a1814189d14`), and `ire_eamon_de_valera.png` (`ff5f8689f1e8ea75bf88bea4c4a87dcf60518b1e062ea53be4a9ceff3509dcb0`). They were used as family/style controls only.

## Gate findings

### Identity and likeness - PASS with low-resolution/group-context caveat

At native and 4x nearest-neighbour scale, the repaint and candidate retain the source-specific black rounded clerical hat, large dark beard and moustache, deep shadow over the viewer-right eye and cheek, slight three-quarter head direction, narrow visible cheek planes, broad nose silhouette, dark ecclesiastical clothing, and the same restrained head-and-shoulders presentation. The hat/beard/shadow combination is distinctive enough to prevent genericization or face substitution, and the raw and candidate agree on those anchors. No cross, medal, insignia, jewelry, text, flag, logo, additional face, modern prop, or advisor frame was introduced.

The exact crop is only `320x385` and comes from a soft ten-person group photograph. The repaint necessarily reconstructs eye, nose, skin, and beard texture that the source cannot prove pixel-for-pixel, and it smooths some source grain while making the visible eye and mouth planes more legible. The source’s asymmetric shadow is retained rather than symmetrized, and I found no material contradiction in hat shape, beard silhouette, pose, age band, or clothing. Treat this as a bounded likeness pass; the exact crop remains the sole identity authority for any future work.

### HOI4 leader style and framing - PASS

The candidate is an opaque RGB `156x210` country-leader portrait with centered restrained-bust framing, a quiet muted warm-gray painted background, controlled contrast, readable native-scale face, and a period ecclesiastical presentation that sits within the canonical male leader family. The heavy beard and clerical hat are source-linked subject features, not a dossier frame or generic advisor card. No text, watermark, UI, modern object, or unsupported insignia is present.

### Provenance and chain - PASS

The immutable master, exact crop, decoded-pixel equality JSON, raw repaint, deterministic native candidate, package-local prompt, processing record, durable ComfyUI PNG/TXT pair, shelf copy, package manifest, hash ledger, source-research handoff, and independent native/4x review sheets are all present and hashable. The raw repaint and durable PNG are byte-identical, the crop record reports exact decoded-pixel equality, and the candidate’s `ImageOps.fit` operation is recorded without hidden enhancement or recolouring. This is a complete evidence chain; it does not imply runtime admission.

### Rights and date - PASS with PD-1923/source-ledger caveat

The source-research handoff identifies Ignatius Aphrem I Barsoum (Ayoub Barsoum, 1887-1957) as a Syriac Orthodox church leader who was Archbishop of Syria and Lebanon from 1918 and Patriarch from 1933, making the 1921 delegation role and a 1936 concordat-council consumer historically compatible. The cited source is [Commons](https://commons.wikimedia.org/wiki/File:Assyro-Chaldean_delegation_to_the_Paris_Peace_Conference.png) with [original PNG](https://upload.wikimedia.org/wikipedia/commons/4/40/Assyro-Chaldean_delegation_to_the_Paris_Peace_Conference.png). Commons records `Babylon`, volume 2, number 14, 3 February 1921 as the publication source and labels the reproduction `PD-1923`; the source description identifies the figure as “Metran Afrem Barsoom” in the Assyro-Chaldean delegation. The publication date is pre-1936 and the rights record is materially stronger than the prior PD-Syria lead.

The unknown photographer and reproduced group-photo chain remain source-ledger caveats, and the parent must accept the `PD-1923` basis and the caption-to-crop mapping before any release promotion. This audit records the source basis as a visual/provenance PASS with caveat, not as a legal opinion or automatic runtime grant.

### DDS promotion and runtime wiring - BLOCKED

No DDS conversion, `.gfx` change, character edit, or runtime replacement was made. The stable consumer remains `ASY_independence_wave_concordat_council`, with sprite `GFX_portrait_ASY_independence_wave_concordat_council` and existing runtime path `gfx/leaders/006_independence_wave/portrait_ASY_independence_wave_concordat_council.dds`; that existing DDS remains untouched. The alternate Barsoum v1 candidate is evidence-only and cannot replace the current DDS under this no-wire audit scope.

## No-advisor-icon boundary

The reviewed asset is only a full `156x210` civilian-large country-leader portrait candidate. No native `65x67` advisor, theorist, military-high-command, officer-corps, dossier, commander-small, operative, or `_small` derivative was created, reviewed as a substitute, or authorized. Do not infer any such asset from the concordat-council consumer.

## Required next action

1. Keep the 1921 master and exact crop immutable and use the exact crop as the sole identity authority for any future pass.
2. Preserve the group-source caption and `PD-1923` publication record with the candidate; obtain the parent’s explicit release acceptance before any promotion.
3. If the parent later admits this alternate candidate, retain the durable ComfyUI pair, re-check the low-resolution face at native and 4x scale, and reconcile the candidate against the existing runtime DDS before conversion.
4. Convert to DDS and replace the stable civilian-large sprite only after the parent authorizes wiring and all independent gates remain accepted; otherwise retain every file as evidence-only.

**Final status: HOLD as evidence-only pending parent release acceptance and no-wire scope; no DDS, GFX, or runtime promotion is authorized.**
