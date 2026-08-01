# IW-058 ASY Shamoun Hanne Haydo portrait audit v92

Date: 2026-08-01 (Europe/Kyiv).

Reviewer: OpenAI Codex asset-source auditor `/root/event6_chu_bolgar_repaint_audit_v93b`.

Scope: independent review of the parent-produced v1 Haydo repaint and deterministic `156x210` candidate against the unchanged early-20th-century source master, the exact lossless crop, the retained source-locked prompt and processing record, and the canonical male country-leader references. I did not produce the repaint or candidate. No gameplay, characters, `.gfx`, localisation, DDS, central attestation, or catalog file was changed.

## Decision

**Overall verdict: HOLD; the candidate is not eligible for DDS promotion or runtime wiring.** The source-specific moustache, short side-parted hair, broad forehead, heavy brows, broad jaw, large ears, frontal stern presentation, double-breasted dark coat, and patterned neck scarf are retained without a material face substitution or unsupported insignia. The visual likeness gate passes with a source-resolution caveat, the HOI4 leader style/framing gate passes, and the processing/provenance chain is complete. Rights/date acceptance remains explicitly `needs_user_review`, so the candidate remains evidence-only and no runtime DDS exists.

Separate gate verdicts are **identity/likeness: PASS with source-resolution caveat**, **HOI4 leader style/framing: PASS**, **provenance/chain: PASS**, **rights/date: HOLD (`needs_user_review`)**, and **DDS/runtime promotion: BLOCKED**.

The identity pass is limited to the visible anchors that the low-detail source supports. The source does not justify confidence in every high-frequency eye, hair, or skin-plane detail invented by the repaint; those details must not be treated as newly verified biography or as permission to beautify, symmetrize, or further redesign the face.

## Evidence reviewed

| Artifact | Dimensions/mode | SHA-256 or proof | Review use |
| --- | --- | --- | --- |
| `docs/assets/006_independence_wave/asy_portrait_source_research_v91_2026_08_01/source_masters/ASY_shamoun_hanne_haydo_early_20c.png` | 950x1514 RGBA PNG | `2f34457778a84ae4e54f65dacedb588d97cce0e4fe78b1d52b46c61de992fe7b` | Unchanged early-20th-century full-body archival master; immutable identity evidence. |
| `docs/assets/006_independence_wave/asy_portrait_source_research_v91_2026_08_01/source_crops/ASY_levies_guardianship_shamoun_hanne_haydo_head_shoulders.png` | 730x735 RGBA PNG | `00ca79dd73e4a9d1596a2be7833b34a4560221894222f862ac112e49a73ef998` | Exact head-and-shoulders identity crop used for the source-locked repaint. |
| `docs/assets/006_independence_wave/asy_portrait_source_research_v91_2026_08_01/crop_metadata/ASY_levies_guardianship_shamoun_hanne_haydo_crop.json` | JSON evidence | `c81f09b7365b23f1b92baa8b4396ae82bd7216dc7d7318471a0e06074e4b3924` | Crop rectangle `(110,25,840,760)`; `decoded_pixels_equal: true`; equal decoded RGBA hash `310ba8b1fe8fd8103dd5b28b4b6ea886eed03f568fa2ebb48eb2a5d176f9583c`; Pillow 11.1.0 and utility v1.0 recorded. |
| `docs/assets/006_independence_wave/asy_portrait_source_research_v91_2026_08_01/repaints_raw/ASY_levies_guardianship_shamoun_hanne_haydo_hoi4_repaint_v1.png` | 1054x1492 RGB PNG | `99fbe008d7088f1306a1acad054f19a02104f6652e10f1f83834b3a147411fa5` | Parent-produced source-locked HOI4 repaint; evidence only. |
| `docs/assets/006_independence_wave/asy_portrait_source_research_v91_2026_08_01/repaints_processed/ASY_levies_guardianship_shamoun_hanne_haydo_156x210_candidate_v1.png` | 156x210 RGB PNG | `d3e66f378858e9f704d601124b52d4b3d3cf0b75781c9414ba989da930f40b2b` | Deterministic country-leader candidate at the native runtime canvas; not DDS. |
| `docs/assets/006_independence_wave/asy_portrait_source_research_v91_2026_08_01/repaints_processed/ASY_levies_guardianship_shamoun_hanne_haydo_156x210_processing_v1.md` | Processing record | `209336d56043bc3e0742e52d60750e2df4d41e957edaf21e7b707bf1654a7f0c` | Raw crop `(0,36,1054,1456)` to 1054x1420, Pillow `ImageOps.fit` LANCZOS to exact `156x210`, RGB, `optimize=false`. |
| `docs/assets/006_independence_wave/asy_portrait_source_research_v91_2026_08_01/prompts/ASY_levies_guardianship_shamoun_hanne_haydo_hoi4_repaint_v1.txt` | Prompt record | `470d76877d092ee56723aea896963e4f810a7f3c5b0aa2842faeb3fc2b8ccfa1` | Source-locked identity-preservation brief; it names the visible facial, hair, clothing, asymmetry, and no-insignia constraints. |
| `docs/assets/portraits/006_independence_wave/portrait_ASY_independence_wave_levies_guardianship.png` | 1054x1492 RGB PNG | `99fbe008d7088f1306a1acad054f19a02104f6652e10f1f83834b3a147411fa5` | Durable ComfyUI source pair; byte-identical to the raw repaint and not a runtime path. |
| `docs/assets/portraits/006_independence_wave/portrait_ASY_independence_wave_levies_guardianship.txt` | Prompt TXT | `e896fe68f001c4d43bb0ca91fafae99079670d8e8e1427e28463503050c15879` | Matching durable ComfyUI replacement prompt; only the prompt text is stored. |
| `docs/assets/006_independence_wave/portraits_generated_png/ASY_levies_guardianship_shamoun_hanne_haydo_hoi4_repaint_v1.png` | 1054x1492 RGB PNG | `99fbe008d7088f1306a1acad054f19a02104f6652e10f1f83834b3a147411fa5` | Flat evidence shelf copy; byte-identical to the raw repaint. |
| `docs/assets/006_independence_wave/asy_portrait_source_research_v91_2026_08_01/review/ASY_levies_guardianship_shamoun_hanne_haydo_full_chain_4x_v01.png` | 2400x1960 RGB PNG | `0e3212b0bdbefaf07a7ed0f336e5877d54ed2871fdd032443b13e04bce70ff23` | Evidence-only sheet of immutable master, exact crop, raw repaint, native/4x candidate, and two canonical leader references. |
| `docs/assets/006_independence_wave/asy_portrait_source_research_v91_2026_08_01/review/ASY_levies_guardianship_shamoun_hanne_haydo_face_geometry_close_v01.png` | 2640x1140 RGB PNG | `030ab69414510eaf22893d256336a3202e6cdbc1ae4bf0407b8662b042a5f28d` | Nearest-neighbour close review of source crop, raw repaint, and processed candidate faces. |
| `docs/assets/006_independence_wave/asy_portrait_source_research_v91_2026_08_01/review/ASY_levies_guardianship_leader_refs_native_4x_v01.png` | 2240x2320 RGB PNG | `117037e506cc125bdaa4e7d64a034172ccd75ef62a6439124fe1a9f83cb930fd` | Six curated male country-leader references at native and 4x nearest-neighbour scale; style controls only. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw058_asy_portrait_source_research_v91_2026_08_01.md` | Research handoff | `320b7f59ede8bdd3a3cc256ef580dbb9d73b30d111b9adb3ea38e9fe8240bcaf` | Source, role/date, URL, and rights-status ledger; the handoff keeps this subject at `needs_user_review`. |

The canonical role family was `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/leaders/`. The six native `156x210` references inspected were `afg_mohammed_zahir_shah.png` (`f606bc3c6204e0dbd35d8edceb21f87ae6f93a0ae7ad657382c7e9043e8907a0`), `den_thorvald_stauning.png` (`08732002182bdcb2bff3d78b142cc2b3d75adbdb29d4115f9e89ca5bdc6a21b6`), `eth_haile_selassie.png` (`e06bc1bd67ce70e1fb22e39d4c6d2732327d23a58efeb74b096b456318b7eb4b`), `fin_carl_mannerheim.png` (`7e78e33e0b691b96b584393f2d363c07a302320f7e6300bda0fff261aa98d49e`), `ice_sveinn_bjornsson.png` (`860726d268873f21ae0dbd6fb170482f50fad6393882b97b2b7b7a1814189d14`), and `ire_eamon_de_valera.png` (`ff5f8689f1e8ea75bf88bea4c4a87dcf60518b1e062ea53be4a9ceff3509dcb0`). The package-specific native/4x reference sheet is byte-identical to the previously reviewed six-reference sheet and is evidence only.

## Gate findings

### Identity and likeness - PASS with source-resolution caveat

At native and 4x nearest-neighbour scale, the candidate preserves the source-visible anchors that distinguish this subject: the broad high forehead, short side-parted dark hair, heavy broad handlebar moustache, thick brows, frontal head direction, large ears, broad lower face and jaw, stern-neutral expression, dark double-breasted coat, and patterned neck scarf. The moustache silhouette and hairline remain especially strong identity anchors. The raw repaint and the deterministic candidate agree, and neither shows a face substitution, generic officer redesign, modern object, medal, insignia, or unsupported costume.

The archival crop is low-detail and scratched, so the repaint necessarily reconstructs high-frequency eye, hair, skin, and brush texture that the source cannot verify pixel-for-pixel. The generated eyes are more fully delineated than the source, the hair has more volume and texture, and the nose and cheek planes are more modeled, but those changes do not produce a material contradiction in the visible broad geometry or expression. Treat this as a bounded likeness pass, not evidence for details hidden by the source; any further repaint must preserve the source's asymmetry and must not beautify or symmetrize the face.

### HOI4 leader style and framing - PASS

The candidate is an opaque RGB `156x210` country-leader portrait with centered head-and-shoulders framing, a restrained bust, a quiet warm-gray painted background, subdued period civilian clothing, and readable native-scale contrast. It sits within the canonical male country-leader family represented by the six inspected references. The brush texture is somewhat heavier than the quietest references, but it remains a presentation caveat rather than a style-gate failure. No text, watermark, UI, advisor frame, small-card border, modern prop, or invented insignia is present.

### Provenance and chain - PASS

The immutable source master, exact crop, decoded-pixel equality JSON, v1 raw repaint, deterministic `156x210` candidate, deterministic processing record, package-local prompt, durable ComfyUI PNG/TXT pair, byte-identical shelf copy, source-research rights/role handoff, and independent native/4x review sheets are present and hashable. The crop lineage is explicit and the processing record is internally consistent. The prompt records the source-locked identity constraints; no package-local manifest or DDS is required for this independent audit handoff, and no runtime promotion is implied by this provenance pass.

### Rights and date - HOLD (`needs_user_review`)

The source-research handoff identifies the historical subject as Shamoun Hanne Haydo (1870-1964), a Syriac/Assyrian village-defense leader of Sare and Bsorino whose leadership spans 1900 through his death and therefore fits the 1936 living-role window. The cited source is [Commons](https://commons.wikimedia.org/wiki/File:Syriac-Aramean_Warrior_and_Leader,_Shamoun_Hanne_Haydo.png) with [original PNG](https://upload.wikimedia.org/wikipedia/commons/8/87/Syriac-Aramean_Warrior_and_Leader%2C_Shamoun_Hanne_Haydo.png). Commons describes an early-20th-century image by an unknown author, labels it `PD-Turkey`, and points to Instagram, X, and Facebook social-source links; the description says it was sent by a friend close to the Haydo family. The exact photographer, capture date, first publication, and full rights chain are not identified.

Role/date fit is strong, but the public-domain assertion remains an unresolved rights question rather than an automatically accepted license. Keep the source, repaint, candidate, and durable pair as evidence-only until the parent explicitly accepts the Commons PD-Turkey basis and the unknown-author provenance for the intended release.

### DDS promotion and runtime wiring - BLOCKED

No DDS exists, no `.gfx` admission was made, and no character or runtime portrait reference was changed. Promotion is blocked by the rights/date HOLD even though the visual identity, style, and provenance gates pass. The stable intended consumer remains `ASY_independence_wave_levies_guardianship`, with the stable full civilian-large sprite name `GFX_portrait_ASY_independence_wave_levies_guardianship` if the parent later admits the portrait. The durable ComfyUI pair is not a runtime path.

## No-advisor-icon boundary

The reviewed asset is only a full `156x210` country-leader/civilian-large portrait candidate. No native `65x67` advisor, theorist, military-high-command, officer-corps, dossier, commander-small, operative, or `_small` derivative was created, reviewed as a substitute, or authorized. Do not infer any such asset from the existing character or route.

## Required next action

1. Keep the immutable master and exact crop unchanged; use the exact crop as the sole identity authority for any future source-locked repaint.
2. Record the parent decision on the Commons PD-Turkey/unknown-author rights basis and retain `needs_user_review` until that decision is explicit.
3. If rights are accepted, re-check the same identity anchors at native and 4x nearest-neighbour scale before converting the approved candidate to DDS; do not add advisor, high-command, commander-small, operative, or other unrequested portrait families.
4. Convert to DDS and wire the stable civilian-large sprite only after separate identity PASS, style PASS, provenance PASS, and rights/date acceptance; otherwise retain every local file as evidence-only.

**Final status: HOLD pending explicit rights/date review; candidate remains BLOCKED from DDS/runtime admission.**
