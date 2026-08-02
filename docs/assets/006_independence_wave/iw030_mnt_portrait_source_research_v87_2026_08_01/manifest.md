# IW-030 Montenegro sourced male portrait research v87 (2026-08-01)

This package is source research and evidence only for the grounded male Montenegro roster used by Event 006 IW-030. It does not edit characters, history, events, localisation, `.gfx`, gameplay, spreadsheets, or runtime textures, and it does not authorize DDS conversion. Montenegro is a grounded historical polity, so every one-person portrait candidate remains on the sourced-real-person path.

The v6 source-locked HOI4 repaint and deterministic 156x210 candidate are retained below as evidence pending an independent likeness/style/provenance audit. Their presence does not change the parent-role, rights, identity-amendment, or package-attestation gates.

## Candidate disposition

| Intended consumer or role | Candidate | Status | Source and rights finding | Runtime boundary |
| --- | --- | --- | --- | --- |
| Possible explicit replacement for the blocked `MNT_kristo_popovic` role (not a relabel) | Mitar Martinovic (1870-1954), Montenegrin divisional general, former prime minister and minister of war; `Brigadir Mitar Martinovic.jpg` | `sourced_needs_parent_role_admission` | 1912 portrait extracted from *Ilustrovana ratna kronika Prvog balkanskog rata*, publisher Izdavacka knjizarnica Svetozara F. Ognjanovica, Novi Sad. Commons records the source as a 1912 Serbian National Library scan and applies `PD-collective-work|Serbia`; the work is over a century old. | Strong role-correct replacement candidate for a country-leader/corps-commander token, but the parent must explicitly change the character identity and localisation if used. Do not assign this face to `MNT_kristo_popovic` without an accepted design amendment. |
| Alternative commander candidate, not selected | Radomir Vesovic (1871-1938), Montenegrin general | `needs_user_review` | Commons has a clear bust image and `PD-Serbia`, but records the source only as own work and the author as unknown; provenance is weaker than the Mitar Martinovic chronicle source. | Research comparison only; no crop or runtime admission. |
| Political alternative, rejected for commander role | Sekula Drljevic (1884-1945), Montenegrin politician | `rejected_role_mismatch` | Commons file is dated by 1925 and marked `PD-Slovenia` from the Slovenian digital library, but Drljevic is a politician rather than a corps commander. | Do not use as a commander replacement; retain only as comparison evidence. |
| Historical figure, rejected for 1936 roster | Marko Miljanov (1833-1901), Montenegrin vojvoda | `rejected_era_role` | Commons cites a pre-1901 image from the Digital Library of Matica Srpska and marks it `PD-Serbia`, but the subject died decades before the 1936 start and is not a 1936-era country-leader/corps-commander consumer. | Do not substitute into the live MNT roster without an explicit historical-identity redesign. |
| Existing MNT consumers | Blažo Jovanovic and Blažo Dukanovic | `needs_user_review` | v68 package already has exact attributed source masters/crops, source-locked repaints, visual/style/source-crop PASS, and rights/provenance review pending because both Commons records involve unknown photographers. | Keep evidence-only; parent owns final rights decision and any later DDS/GFX wiring. |
| Existing MNT consumer | Krsto Zrnov Popovic | `blocked_provenance` | v68 Commons and Montenegrina leads lack a defensible image author/source/date/license chain. | Keep blocked; never relabel another person's portrait or generate a substitute. |

## Selected Mitar Martinovic source

- Commons file page: <https://commons.wikimedia.org/wiki/File:Brigadir_Mitar_Martinovi%C4%87.jpg>.
- Canonical image URL: <https://upload.wikimedia.org/wikipedia/commons/3/3e/Brigadir_Mitar_Martinovi%C4%87.jpg>.
- Source statement on Commons: extracted from *Ilustrovana ratna kronika III broj.pdf*, page 3, a 1912 publication by Izdavacka knjizarnica Svetozara F. Ognjanovica, Novi Sad.
- Underlying scan record: <https://commons.wikimedia.org/wiki/File:Ilustrovana_ratna_kronika_III_broj.pdf>.
- Serbian National Library digital record: <https://digitalna.nb.rs/view/URN:NB:RS:SD_5F9ABEA7946203201B672CD4AAF1F0F6>.
- Commons source metadata records `date=1912`, publisher as author/collective work, and `PD-collective-work|Serbia`. The publication is far beyond the Serbian 70-year term; retain the Commons attribution and the archive record. The NBS site itself displays a site-terms notice, so the handoff treats the underlying historical publication as the public-domain basis and does not claim that the NBS website terms are waived.
- Immutable downloaded master: `source_masters/mnt_mitar_martinovic_1912_chronicle.jpg` (684x1135 RGB JPEG, SHA-256 `202d349544bb4b36ee696120222c1ccfdb25e1a8c7213e65eef9ce910d185a76`).
- Exact head-and-shoulders crop: `source_crops/mnt_mitar_martinovic_1912_head_shoulders.png` (530x670 RGB PNG, crop rectangle `[left=80, top=90, right=610, bottom=760]`, SHA-256 `493846b7202b528ce81260a0227d5c4880575f97cc0cb45715b116390e37de2e`).
- Crop proof: `crop_metadata/mnt_mitar_martinovic_1912_crop.json`, generated by `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py` v1.0; `status=exact_source_crop_verified`, `decoded_pixels_equal=true`, equality hash `0c7f16cd55741be02cf693c2c0b6d5e92daee087ed873facb93ecb12a807b81f`.
- Contact sheet: `review/mnt_v87_source_candidates_contact_sheet.jpg` (review-only comparison of the selected source and rejected alternatives).

## v6 repaint evidence

- Raw identity-preserving ImageGen repaint: `generated_portraits/portrait_MNT_mitar_martinovic_hoi4_repaint_raw_v6.png`, 1114x1412 RGB, SHA-256 `b9f1c5e0e28f0a1e12ebce80b14b935cfe31c32232a784c249bfe15c3073b80a`.
- Deterministic native candidate: `generated_portraits/portrait_MNT_mitar_martinovic_hoi4_156x210_v6.png`, 156x210 RGB, SHA-256 `4165007d39d70f45780e3615e5e000ea2d12296141d8d79710fcaedf59e9fac7`.
- Processing record: `generated_portraits/portrait_MNT_mitar_martinovic_processing_v6.json`; the center crop is `[27, 0, 1086, 1412]`, followed by Pillow LANCZOS to 156x210, without padding or recolour.
- Durable ComfyUI source/prompt pair: `docs/assets/portraits/006_independence_wave/portrait_MNT_mitar_martinovic.png` and `portrait_MNT_mitar_martinovic.txt`.
- Gate: `needs_user_review_v7`; the independent v91 audit passes identity and source linkage, prefers v7 for HOI4 style, and still requires human style sign-off plus parent ownership/roster approval. No DDS, `.gfx`, character, localisation, or attestation promotion is authorized from this evidence alone.

The v7 style-only refinement keeps the v6 identity, uniform, and framing while using a lighter neutral painted background for closer HOI4 reference alignment. It is also evidence-only: raw `generated_portraits/portrait_MNT_mitar_martinovic_hoi4_repaint_raw_v7.png` (1080x1456 RGB, SHA-256 `d30891ac10f58dd080b2eeb85081efec9314d6e7e849ab91f8d01f9c05733b6d`) and native `generated_portraits/portrait_MNT_mitar_martinovic_hoi4_156x210_v7.png` (156x210 RGB, SHA-256 `6b14b6cb8ef48b9c2b256bc331026448450e6dfbd409f4a9d19da6a8c6254501`) are recorded by `generated_portraits/portrait_MNT_mitar_martinovic_processing_v7.json`. The v7 gate remains `pending_independent_audit_v7`; no DDS, `.gfx`, character, localisation, or attestation promotion is authorized.

## Role and era fit

Mitar Martinovic is a documented Montenegrin divisional general who served as prime minister and minister of war and commanded the Lovcen Detachment. Role/life-date references: <https://encyclopedia.1914-1918-online.net/histperson/mitar-martinovic-1870-1954/> and <https://www.worldstatesmen.org/Montenegro.html>. The 1912 image is an active-life military portrait with period Montenegrin uniform, medals, and head-and-shoulders framing. The image predates the 1936 scenario by 24 years but the subject lived until 1954 and remained a role-correct historical military/political figure; this is a deliberate source-era note, not a claim that the photograph was made in 1936.

The vanilla file `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/characters/MNT.txt` gives all three current MNT ids both country-leader and corps-commander consumers. `MNT_kristo_popovic` is specifically a 1936-1947 consumer with a generic portrait, so using Martinovic would require an explicit identity/roster design change and a new stable character key or accepted relabeling decision. The source-research agent does not make that gameplay change.

## Rejected comparison evidence

- `source_masters/mnt_mitar_martinovic_1912_webdizajn.jpg` (556x800, SHA-256 `f59610b460d29fe323ce9d4b4aa9f5fa4c30f79d87142a515b5325dc9e9c0c02`) is a visually clear duplicate-style portrait from <https://commons.wikimedia.org/wiki/File:Mitar_Martinovich_Min_of_Montenegro.jpg>, but Commons cites only a webdizajn page, an unknown author, and `PD-old`; the chronicle source above has the stronger dated archival chain and is selected instead.
- `source_masters/mnt_radomir_vesovic_circa1910.jpg` (426x600, SHA-256 `3ec3233227fdf3a0d974d95e3a1542614dfb34fbe00cc061f1268bc2445e9af7`) is <https://commons.wikimedia.org/wiki/File:Radomir_Ve%C5%A1ovi%C4%87.jpg>, circa 1910, marked `PD-Serbia`, but Commons records the source as own work and author unknown; it remains comparison evidence only.
- `source_masters/mnt_sekula_drljevic_by1925.jpg` (301x376, SHA-256 `9845456a8a3744e1e4fc6473ab56bc3bf0991cad45d7111182131ac53958bb5b`) is <https://commons.wikimedia.org/wiki/File:Sekula_Drljevi%C4%87.jpg>, sourced to the Slovenian digital library and marked `PD-Slovenia`; it is a political portrait without a documented corps-command role.
- `source_masters/mnt_marko_miljanov_pre1901.jpg` (629x974, SHA-256 `06c2e6026211e0a9ee70b93e229e598feb5e242ed702a2137f1c8520433a3bca`) is <https://commons.wikimedia.org/wiki/File:Vojvoda_Marko_Miljanov.jpg>, pre-1901, and marked `PD-Serbia`; the subject died in 1901 and is not a 1936-era roster candidate.
- `rejected_candidates/mnt_milutin_vucinic_1922.jpg` and `rejected_candidates/mnt_radomir_vesovic_lim_1912.jpg` are failed HTTP downloads (429 response HTML, not image files) and are retained only as audit traces of rejected retrieval attempts; they are not sources and must not be processed.

## Ownership and runtime boundary

No existing-character transfer is proposed. An exact/variant search for `Mitar Martinovic`, `Mitar Martinović`, and likely token forms returned no matches in the current Chaos Redux tree or installed vanilla `common/characters/`, `history/`, `gfx/leaders/`, `interface/`, and localisation roots. The parent must still rerun the normal identity-ownership check before any new character key or replacement is admitted. The v6 repaint and candidate are evidence-only and may not be wired directly or converted to DDS before an independent audit PASS and explicit roster decision. The selected archival crop remains source evidence and may not be wired directly or merely resized into runtime.
