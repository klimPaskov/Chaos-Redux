# IW-043 CHU Bolgar civic-presidium portrait v2 audit v94

Date: 2026-08-01 (Europe/Kyiv).

Reviewer: OpenAI Codex asset-source auditor `/root/event6_chu_bolgar_repaint_audit_v93b`.

Scope: independent review of the targeted v2 Karim Tinchurin repaint against the unchanged v90 master and exact crop, the v1 evidence context, and the canonical male country-leader references. I did not produce the v2 repaint or candidate. No gameplay, characters, `.gfx`, localisation, DDS, central attestation, or catalog file was changed, and v93 was not overwritten.

## Decision

**Overall verdict: HOLD; the v2 candidate remains blocked from DDS promotion and runtime wiring.** V2 materially improves the v1 scalp/hair drift and keeps the bald crown, but the eyes remain too regularized and open, the brow and mouth are stronger than the source, and the nose/lower-face geometry is still smoother and more idealized than the exact crop. Rights/date acceptance is still pending. The package-local v2 prompt has since been added and hashed, so the earlier provenance prompt-record caveat is closed; the identity and rights/date holds remain unchanged.

Separate gate verdicts are **identity/likeness: HOLD**, **HOI4 leader style/framing: PASS**, **provenance/chain: PASS**, **rights/date: HOLD**, and **DDS/runtime promotion: BLOCKED**.

## Evidence reviewed

| Artifact | Dimensions/mode | SHA-256 or proof | Review use |
| --- | --- | --- | --- |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/source_masters/karim_tinchurin_mug_shots_1937.jpg` | 1600x1086 RGB JPEG | `cc49680ff52c80b61f0198236e70c111f19bbabe20067c6246837c0484d04573` | Unchanged archival master; the frontal panel is the right-hand panel. |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/source_crops/karim_tinchurin_head_shoulders.png` | 745x1035 RGB PNG | `1f44b5b72318839a4ccdf6f922a5fc5be53a278aaca25e6621ed870d4cb7cadf` | Unchanged exact frontal identity crop. |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/crop_metadata/karim_tinchurin_crop.json` | JSON evidence | `bbaa5a25faf768c538497bd57c310518d69b72614c64d777d45577ad4266caac` | Rectangle `(760,45,1505,1080)`; `decoded_pixels_equal: true`; equal decoded RGBA hash `693e7e77897665cc5895195d528c4d1cc5b4c12e6f4dd23816356071b752e103`; Pillow utility v1.0. |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/repaints_raw/karim_tinchurin_hoi4_repaint_v1.png` | 1064x1478 RGB PNG | `e5b7236ea1a72ced0ae7a20d0116ee1414218a6eb1c49a94491984c2eb552fb3` | Prior v1 context; v93 audit recorded the hair/asymmetry identity HOLD. |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/repaints_processed/karim_tinchurin_156x210_candidate_v1.png` | 156x210 RGB PNG | `c60f4e292fbfbb8ea7a10edc46e8e908400e53e81d6ab5888f26a2446297d4be8` | Prior native context; not promoted. |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/repaints_raw/karim_tinchurin_hoi4_repaint_v2.png` | 1066x1476 RGB PNG | `d7c077a3ae82d3c0d1271ba937f1ae0faa152d5892cbf54c57b9ba5096d0b558` | Targeted v2 raw repaint under audit; evidence only. |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/repaints_processed/karim_tinchurin_156x210_candidate_v2.png` | 156x210 RGB PNG | `8db2849f750b765bf54ee20026720abcfee2eaa57866c68a999253602fc5db48` | Deterministic native v2 candidate; evidence only and not DDS. |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/repaints_processed/karim_tinchurin_156x210_processing_v2.md` | Processing record | `6cf485c44ec2964cb891b8ae92a82d29287813a87877405b25cf3a42d2e2a712` | Raw crop `(0,20,1066,1452)` to 1066x1432, Pillow `ImageOps.fit` LANCZOS to 156x210, RGB, `optimize=False`. |
| `docs/assets/006_independence_wave/portraits_generated_png/CHU_karim_tinchurin_hoi4_repaint_v2.png` | 1066x1476 RGB PNG | `d7c077a3ae82d3c0d1271ba937f1ae0faa152d5892cbf54c57b9ba5096d0b558` | Byte-identical flat original-size shelf copy; no native copy is stored there. |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/review/karim_tinchurin_v2_full_chain_4x_v94.png` | 2400x1960 RGB PNG | `f2f6d73ea7cc9bdf1c099430069d5a2468e6a324b01b73e3930b2b1fc7640b83` | Evidence-only source, v1, v2, native candidate, 4x candidate, and leader-style comparison sheet. |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/review/karim_tinchurin_v2_face_geometry_close_v94.png` | 3520x1140 RGB PNG | `18f8e73d2f9508109f4e0800e4b0266b5de29e46145646576dbf82772e00ff21` | Evidence-only nearest-neighbour close comparison of source, v1, v2, and v2 candidate faces. |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/review/karim_tinchurin_leader_refs_native_4x_v93.png` | 2240x2320 RGB PNG | `117037e506cc125bdaa4e7d64a034172ccd75ef62a6439124fe1a9f83cb930fd` | All six curated male country-leader references at native and 4x nearest-neighbour scale; reused as canonical v2 evidence. |

The v1 prompt remains at `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/prompts/karim_tinchurin_hoi4_repaint_v1.txt` with SHA-256 `579d1dade8b60984add037609a5e16bffdac1c2236bdd75931d92ceface254d3`. The package-local v2 prompt is now present at `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/prompts/karim_tinchurin_hoi4_repaint_v2.txt` with SHA-256 `162908b173cbdef6c07b8bece74c23004c3f0cb34794f67baf14eb8f836d49de`; `hashes.sha256` records that hash alongside the v2 raw and candidate hashes. The v2 prompt is the source-locked retry record and is not being inferred from the v1 text.

The canonical references were `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/leaders/` and its native contact sheet (`19320e58b96b1a5c2766392d5f332c1f56e8a3720aa0a47fa5970971b6b6a79e`). The six inspected native 156x210 references are `afg_mohammed_zahir_shah.png` (`f606bc3c6204e0dbd35d8edceb21f87ae6f93a0ae7ad657382c7e9043e8907a0`), `den_thorvald_stauning.png` (`08732002182bdcb2bff3d78b142cc2b3d75adbdb29d4115f9e89ca5bdc6a21b6`), `eth_haile_selassie.png` (`e06bc1bd67ce70e1fb22e39d4c6d2732327d23a58efeb74b096b456318b7eb4b`), `fin_carl_mannerheim.png` (`7e78e33e0b691b96b584393f2d363c07a302320f7e6300bda0fff261aa98d49e`), `ice_sveinn_bjornsson.png` (`860726d268873f21ae0dbd6fb170482f50fad6393882b97b2b7b7a1814189d14`), and `ire_eamon_de_valera.png` (`ff5f8689f1e8ea75bf88bea4c4a87dcf60518b1e062ea53be4a9ceff3509dcb0`).

## Gate findings

### Identity and likeness - HOLD

V2 is a meaningful correction over v1. The crown is now bald rather than carrying v1's invented top hair, the sparse side hair is restrained, the jacket/collar silhouette remains source-linked, and the overall head width, ears, forehead, frontal direction, and age band are closer to the exact crop. The strict identity gate still does not pass at native or 4x nearest-neighbour scale.

- **Hairline and crown: PASS for the v1 correction.** V2 removes the v1's obvious full crown hair drift and keeps a mostly bald crown with only subtle source-compatible side texture. This is no longer the primary identity blocker.
- **Eyes and asymmetry: HOLD blocker.** The source has small, uneven eye openings and a visibly asymmetric eyelid/gaze relationship. V2 keeps the eyes darker and less exaggerated than v1, but both eyes are still more open, more fully delineated, and closer to equal in shape/height than the source. The brows are also darker and heavier, changing the source's reserved expression into a stronger frown.
- **Nose: HOLD blocker.** V2 is closer than v1 in bridge width and tip placement, but the painted bridge remains narrower and more sculpted, with a cleaner pointed tip and regular nostril contour than the source's broad short nose and softer flat tip.
- **Mouth and lower face: HOLD blocker.** V2 keeps the closed neutral mouth direction, but the lips remain fuller and more modeled than the source's thin line. The cheeks and chin are smoother and broader, with reduced source-visible asymmetry and a more idealized oval lower face.
- **Age and pose: partial PASS.** The adult age band, frontal head direction, large ears, and stern-neutral presentation remain compatible, but they cannot compensate for the eye/nose/lower-face drift.
- **Clothing: partial PASS.** The open white collar, central button, and dark civilian jacket remain recognizable. The repaint darkens and stylizes the jacket relative to the grayscale source but does not add unsupported medals, insignia, hats, props, or modern objects.

V2 is therefore an improved, recognizable source-derived candidate, not yet an identity-preserving PASS. Request another source-locked pass from the unchanged crop that keeps the smaller unequal eyes, lighter brows, broad short nose, thin mouth, compact cheek/jaw planes, and source asymmetry without reintroducing hair drift.

### HOI4 leader style and framing - PASS

The v2 candidate is an opaque RGB 156x210 country-leader portrait with centered head-and-shoulders framing, a restrained bust, a quiet painted background, subdued period civilian clothing, and no text, watermark, UI, modern prop, advisor frame, or invented insignia. Native size remains readable and the matte painterly treatment sits within the canonical leader family. The v2 background is darker and the brush texture more pronounced than some references, but this is a presentation caveat rather than a style-gate failure; the current likeness HOLD still prevents runtime admission.

### Provenance and chain - PASS

The immutable master, exact crop, decoded-pixel equality JSON, v2 raw PNG, v2 deterministic 156x210 candidate, v2 processing record, byte-identical flat shelf copy, package-local v2 prompt, v2 prompt hash entry, v1 context, and independent review sheets are present and hashable. The processing record is internally consistent and the crop lineage is unchanged. The v2 prompt explicitly records the bald crown, eye asymmetry, nose, mouth, jaw, collar, jacket, and no-insignia constraints; this closes the prior package-local prompt-record gap. Provenance is complete for the evidence-only v2 retry, but the identity and rights/date gates still block promotion.

### Rights and date - HOLD

The unchanged Commons raw snapshot `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/source_metadata/commons_raw_file_page.txt` (SHA-256 `5f1777b3099269ca427f4960aaed06d9ea92b37ab8c9ce048c93a02aa859de8d` in the source package record) records `date=1937`, `author=NKVD`, source `tinchurinteatr.ru`, `{{Pd-old}}`, and `{{PD-RU-exempt|type=mug shots}}`. The official Tinchurin State Theatre role snapshot is `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/source_metadata/tinchurin_state_theatre_source_page.html` with SHA-256 `a9adbe5fc96fa41847a1cf4f5b92a6d37b187ccf998fb87a34af5b8ce38955c9` and remains the identity/civic-context evidence. The parent must still accept the Commons/Russian mug-shot basis for the intended mod release, and the source is one year after the 1936 baseline. Keep this gate on `needs_user_review`; do not infer legal acceptance from the v2 visual improvement.

### DDS promotion and runtime wiring - BLOCKED

No DDS conversion, `.gfx` admission, character edit, or runtime replacement is authorized. The existing stable `CHU_independence_wave_bolgar_civic_presidium` consumer remains unchanged. Promotion is blocked by the identity HOLD and rights/date HOLD even though the canvas/style and provenance gates pass.

## No-advisor-icon boundary

The reviewed asset is only a full `156x210` country-leader portrait candidate. No native `65x67` advisor, high-command, officer-corps, dossier, commander-small, operative, or `_small` derivative was created, reviewed as a substitute, or authorized. Preserve this boundary in any further repaint or runtime handoff.

## Required next action

1. Keep the immutable master and exact crop unchanged and use the crop as the sole identity authority for the next source-locked repaint.
2. Preserve the smaller unequal eyes, lighter brows, broad short nose, thin mouth, compact cheek/jaw proportions, bald crown, and source-visible jacket/collar; do not reintroduce v1's crown hair or symmetrize the face.
3. Re-run independent likeness/style review at native and 4x nearest-neighbour scale on the next raw repaint and deterministic 156x210 candidate.
4. Record the parent decision on the Commons rights basis and one-year post-baseline source date.
5. Convert to DDS and wire the existing leader sprite only after separate identity PASS, style PASS, provenance PASS, and rights/date acceptance.

**Final status: HOLD for another source-locked repaint; v2 remains BLOCKED from DDS/runtime admission.**
