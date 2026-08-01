# IW-043 CHU Bolgar civic-presidium portrait audit v93

Date: 2026-08-01 (Europe/Kyiv).

Reviewer: OpenAI Codex asset-source auditor `/root/event6_chu_bolgar_repaint_audit_v93`.

Scope: independent evidence-only review of the Karim Tinchurin source-locked repaint candidate for the existing `CHU_independence_wave_bolgar_civic_presidium` country-leader consumer. I did not produce the master, crop, ImageGen repaint, or 156x210 candidate. No gameplay, characters, `.gfx`, localisation, DDS, central attestation, or catalog file was changed.

## Decision

**Overall verdict: HOLD; the current candidate is blocked from DDS promotion and runtime wiring.** The source identity and provenance chain are defensible, but the present repaint does not clear the non-compensable real-person likeness gate, and the parent still needs to accept the Commons rights basis and one-year post-baseline source date. A further source-locked repaint may be reviewed from the same immutable crop; no generated substitute or generic person is authorized.

Separate gate verdicts are **identity/likeness: HOLD**, **HOI4 leader style/framing: PASS**, **provenance/chain: PASS**, **rights/date: HOLD**, and **DDS/runtime promotion: BLOCKED**.

## Evidence reviewed

| Artifact | Dimensions/mode | SHA-256 or proof | Review use |
| --- | --- | --- | --- |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/source_masters/karim_tinchurin_mug_shots_1937.jpg` | 1600x1086 RGB JPEG | `cc49680ff52c80b61f0198236e70c111f19bbabe20067c6246837c0484d04573` | Immutable 1937 NKVD mug-shot sheet; the frontal panel is the right-hand panel. |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/source_crops/karim_tinchurin_head_shoulders.png` | 745x1035 RGB PNG | `1f44b5b72318839a4ccdf6f922a5fc5be53a278aaca25e6621ed870d4cb7cadf` | Exact frontal head-and-shoulders identity/composition authority. |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/crop_metadata/karim_tinchurin_crop.json` | JSON evidence | `bbaa5a25faf768c538497bd57c310518d69b72614c64d777d45577ad4266caac` | Rectangle `(760,45,1505,1080)`; `decoded_pixels_equal: true`; equal decoded RGBA hash `693e7e77897665cc5895195d528c4d1cc5b4c12e6f4dd23816356071b752e103`; Pillow 11.1.0 crop utility v1.0. |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/repaints_raw/karim_tinchurin_hoi4_repaint_v1.png` | 1064x1478 RGB PNG | `e5b7236ea1a72ced0ae7a20d0116ee1414218a6eb1c49a94491984c2eb552fb3` | Raw source-locked ImageGen repaint; evidence only. |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/repaints_processed/karim_tinchurin_156x210_candidate_v1.png` | 156x210 RGB PNG | `c60f4e292fbfbb8ea7a10edc46e8e908400e53e81d6ab5888f26a2446297d4be8` | Deterministic native candidate; evidence only and not DDS. |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/repaints_processed/karim_tinchurin_156x210_processing_v1.md` | Processing record | `6b5b1187f6ed4fbc3093c42b45ab1bb193f4f00d33b6cd3100cc23537e8e938f` | Raw crop `(0,23,1064,1455)` to 1064x1432, Pillow `ImageOps.fit` LANCZOS to 156x210, RGB, `optimize=False`. |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/prompts/karim_tinchurin_hoi4_repaint_v1.txt` | Text prompt | `579d1dade8b60984add037609a5e16bffdac1c2236bdd75931d92ceface254d3` | Repaint prompt records the crop as identity authority and canonical leaders as style-only inputs. |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/review/karim_tinchurin_full_chain_4x_v93.png` | 2200x1960 RGB PNG | `49cef0efb1e23efdaf7702747757fdc690600ef5e8738f7c08c6dd81fde12d34` | Evidence-only sheet with master, exact crop, raw repaint, native candidate, selected leader references, and 4x nearest views. |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/review/karim_tinchurin_leader_refs_native_4x_v93.png` | 2240x2320 RGB PNG | `117037e506cc125bdaa4e7d64a034172ccd75ef62a6439124fe1a9f83cb930fd` | All six curated male country-leader references at native and 4x nearest-neighbour scales. |
| `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/review/karim_tinchurin_face_geometry_close_v93.png` | 2640x1140 RGB PNG | `4fae89913873e8e6d905c360e74d4512fd2c72a1c64f55d84e08aea88a49a2bc` | Evidence-only nearest-neighbour close crops for source face, raw repaint face, and processed candidate face. |
| `docs/assets/portraits/006_independence_wave/portrait_CHU_independence_wave_bolgar_civic_presidium.png` | 1064x1478 RGB PNG | `e5b7236ea1a72ced0ae7a20d0116ee1414218a6eb1c49a94491984c2eb552fb3` | Durable ComfyUI queue source; `comfyui_replacement_pending`; not runtime storage. |
| `docs/assets/portraits/006_independence_wave/portrait_CHU_independence_wave_bolgar_civic_presidium.txt` | Text prompt | `e5e3f716df77daef42416ddaded1d6d2e50eaa92bac08df3dfd790c8cb6fdd6c` | Matching durable prompt pair; no runtime reference. |

The role-specific canonical reference folder was `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/leaders/`. All six references are native 156x210 PNGs and were inspected at native and 4x nearest-neighbour scale: `afg_mohammed_zahir_shah.png` (`f606bc3c6204e0dbd35d8edceb21f87ae6f93a0ae7ad657382c7e9043e8907a0`), `den_thorvald_stauning.png` (`08732002182bdcb2bff3d78b142cc2b3d75adbdb29d4115f9e89ca5bdc6a21b6`), `eth_haile_selassie.png` (`e06bc1bd67ce70e1fb22e39d4c6d2732327d23a58efeb74b096b456318b7eb4b`), `fin_carl_mannerheim.png` (`7e78e33e0b691b96b584393f2d363c07a302320f7e6300bda0fff261aa98d49e`), `ice_sveinn_bjornsson.png` (`860726d268873f21ae0dbd6fb170482f50fad6393882b97b2b7b7a1814189d14`), and `ire_eamon_de_valera.png` (`ff5f8689f1e8ea75bf88bea4c4a87dcf60518b1e062ea53be4a9ceff3509dcb0`). The supplied native quick-reference contact sheet is `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/leaders/contact_sheet.png` with SHA-256 `19320e58b96b1a5c2766392d5f332c1f56e8a3720aa0a47fa5970971b6b6a79e`.

## Gate findings

### Identity and likeness - HOLD

The source and repaint are recognizably related: the frontal pose, adult male presentation, large ears, high forehead, neutral-stern expression, open white collar, central button, and dark civilian jacket remain present. The candidate still fails the strict source-locked real-person likeness gate at both native and 4x inspection because several identity-bearing structures are changed rather than repainted.

- **Scalp and hairline: HOLD blocker.** The source frontal panel is essentially bald across the crown with only minimal side hair; the raw repaint and candidate add a visible brown-gray hair layer across the crown and a defined receding hairline. This is unsupported hidden detail and materially changes the silhouette.
- **Eyes and asymmetry: HOLD blocker.** The source has uneven eyelid openings and eye shapes with visible side-to-side asymmetry. The repaint opens and levels both eyes, thickens/darkens the brows, and regularizes the gaze into a more generic symmetrical stare.
- **Nose: HOLD blocker.** The source nose reads broader and shorter with a flatter, less sculpted tip. The repaint narrows and lengthens the bridge and gives the tip/nostrils a sharper modeled contour.
- **Mouth and lower face: HOLD blocker.** The source has a thinner, flatter mouth and a compact angular lower face. The repaint gives fuller lips, a softer broader chin, and smoother cheek/jaw planes, reducing source-visible asymmetry.
- **Age and expression: partial PASS only.** The apparent age and reserved stern expression remain broadly compatible with the 1937 source, but these positives cannot compensate for the geometry drift.
- **Pose and clothing: partial PASS only.** The centered frontal head direction, open collar, buttoned jacket, and civilian presentation are retained. The jacket is substantially darkened and simplified, but no unsupported medal, insignia, hat, prop, or modern object was added.

The current repaint is therefore a recognizable source-derived face but not an identity-preserving likeness at the required threshold. This is a remediable candidate HOLD rather than a finding that the archival source is unusable; request another repaint from the immutable crop and do not substitute another person.

### HOI4 leader style and framing - PASS

The processed file is exactly 156x210 RGB and reads as a country-leader portrait at native size. It uses centered head-and-shoulders framing, restrained bust depth, a quiet warm-gray painted background, subdued period clothing, controlled contrast, and a matte painted finish without text, watermark, UI, modern props, or invented insignia. Against the six canonical male leader references, the framing and painterly treatment are within the country-leader family, with the frontal pose acceptable alongside the canonical frontal examples. The broad brush texture is more visible than in some references, but it is not the style gate blocker; a future identity repaint should preserve the same restrained presentation while reducing any texture that muddies the face.

### Provenance and chain - PASS

The immutable master, exact crop, decoded-pixel equality JSON, raw repaint, deterministic 156x210 candidate, processing record, prompt, durable source/prompt pair, canonical references, and independent review sheets are all present at distinct paths with reproducible hashes. The crop uses the required Pillow-only utility and records the rectangle and equality proof. The durable pair is marked `comfyui_replacement_pending` and is not a runtime path. Provenance PASS means the evidence chain is auditable; it does not override the likeness or rights/date holds.

### Rights and date - HOLD

The immutable Commons raw snapshot `docs/assets/006_independence_wave/iw043_bolgar_civic_presidium_source_v90/source_metadata/commons_raw_file_page.txt` (SHA-256 `5f1777b3099269ca427f4960aaed06d9ea92b37ab8c9ce048c93a02aa859de8d`) records `date=1937`, `author=NKVD`, source `tinchurinteatr.ru`, `{{Pd-old}}`, and `{{PD-RU-exempt|type=mug shots}}`. The official Tinchurin State Theatre biography snapshot `source_metadata/tinchurin_state_theatre_source_page.html` (SHA-256 `a9adbe5fc96fa41847a1cf4f5b92a6d37b187ccf998fb87a34af5b8ce38955c9`) supports the subject's identity and Tatar civic/cultural roles. The legal record is explicit enough for parent review, but the parent must still accept that Commons/Russian mug-shot basis for the intended mod release, and the source is one year after the 1936 scenario baseline. Keep `needs_user_review` until both decisions are recorded; do not present this as an unconditional rights PASS.

### DDS promotion and runtime wiring - BLOCKED

No DDS conversion, `.gfx` admission, character edit, or runtime replacement is authorized. The existing stable consumer remains `GFX_portrait_CHU_independence_wave_bolgar_civic_presidium` and its existing runtime path from the source package. Promotion is blocked by the current likeness HOLD and the unresolved rights/date HOLD even though style and provenance pass.

## No-advisor-icon boundary

The reviewed asset is only a full `156x210` country-leader portrait candidate. No native `65x67` advisor, high-command, officer-corps, dossier, commander-small, operative, or `_small` derivative was created, reviewed as a substitute, or authorized. Preserve this boundary in any follow-up repaint and runtime handoff.

## Required next action

1. Keep the immutable master and exact crop unchanged and use the crop as the sole identity authority for the next source-locked repaint.
2. Preserve the source's bald crown, uneven eyelids and gaze, broad short nose, thin mouth, compact lower-face proportions, and source-visible jacket/collar instead of adding hair or beautifying/symmetrizing the face.
3. Re-run the independent likeness/style review at native and 4x nearest-neighbour scale on the next raw repaint and deterministic 156x210 candidate.
4. Record the parent's Commons rights acceptance and the one-year post-baseline date decision before any DDS conversion.
5. Convert to DDS and wire the existing leader sprite only after a separate identity PASS, style PASS, provenance PASS, and rights/date acceptance.

**Final status: HOLD for source/repaint continuation; current portrait candidate is BLOCKED from DDS/runtime admission.**
