# IW-018 ARX portrait audit v77

Date: 2026-08-01.

Scope: read-only audit of the Emilio Lussu, Luigi Arborio Mella di Sant'Elia, and Vittorio Vernè archival masters, exact crops, raw HOI4 repaints, deterministic 156x210 candidates, and the native/enlarged comparison sheets in `docs/assets/006_independence_wave/iw018_arx_portrait_repaint_v76_2026_08_01/`.

No gameplay, character, `.gfx`, DDS, or source-image files were changed. Exact Vittorio Pala and Gavino Piras remain blocked placeholder identities.

## Disposition

| Candidate | Portrait gate | Runtime/package disposition | Decision basis |
| --- | --- | --- | --- |
| Emilio Lussu (`ARX_emilio_lussu`) | **PASS** | **HOLD** pending parent package admission, attribution carry-through, DDS conversion, and final `.gfx`/character review | The source is an unobstructed male head-and-shoulders Senate portrait; the repaint and 156x210 candidate preserve glasses, moustache, goatee, hairline, pose, and period suit. The existing ARX consumer is already a civilian country-leader role. |
| Luigi Arborio Mella di Sant'Elia (proposed replacement for `ARX_vittorio_pala`) | **PASS** | **HOLD** pending explicit placeholder replacement, attribution carry-through, DDS conversion, and final `.gfx`/character review | The source is a clear formal court portrait; the repaint and 156x210 candidate preserve the bald crown, long face, ears, nose, court sash, and decorations. Sassari birth and royal-court service fit the crown consultative council role. The Senate source is small and dated only `before 1955-06-26`, so the final package should retain that uncertainty. |
| Vittorio Vernè (proposed replacement for `ARX_gavino_piras`) | **HOLD; BLOCKED under a strict Sardinian-born requirement** | **HOLD** and do not relabel the placeholder | The source and repaint are suitable for an Italian army commander and the source-ledger role evidence links Vernè to 1936 command and a Sardinia-linked formation, but he was born in Rome. The current `ARX_gavino_piras` character has both civilian and army portraits plus a country-leader record, while this candidate is commander-family only; a package decision is required before promotion. |

## Evidence chain

### Emilio Lussu

- Archival master: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_29/arx_sardinia_sources_v15/source_masters/emilio_lussu_senate_pre1958.jpg` (180x253, SHA-256 `23b0f650f56cb7aeeb017bcad7cde5186d190cb05f6bab99f8656efd895489a0`).
- Exact crop: `.../source_crops/emilio_lussu_senate_pre1958_crop.png` with equality proof in `.../source_crops/emilio_lussu_senate_pre1958_crop.json` (`decoded_pixels_equal: true`).
- Repaint: `docs/assets/006_independence_wave/iw018_arx_portrait_repaint_v76_2026_08_01/repaints_raw/ARX_emilio_lussu_hoi4_repaint_v1.png` (SHA-256 `2a97390107e5913e91d0dc546f6cc1ed6843496cdcec6d1daa6ea38c9e217a8d`).
- Candidate: `.../repaints_processed/portrait_ARX_independence_wave_emilio_lussu_156x210_candidate.png` (SHA-256 `ce55b8db3567a2a665436519fdf7d9f2536ab38581c3898544c91c2bf4bf60c6`).
- Review sheet: `.../review/ARX_emilio_lussu_source_raw_candidate_references_full_chain_4x.png`; native and enlarged panels remain readable against `.../portraits/leaders/den_thorvald_stauning.png` and `.../portraits/leaders/fin_carl_mannerheim.png`.
- Source record: `.../source_records/emilio_lussu_senate_pre1958.md` records Senate attribution via `CC BY 3.0 IT` (`senato.it` attribution required) and a `before 1958` date bound.

### Luigi Arborio Mella di Sant'Elia

- Archival master: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_29/arx_sardinia_sources_v15/source_masters/luigi_mella_santelia_senate.gif` (153x193, SHA-256 `7ada408f2c89d94cd54e19ff9d6914311881df964b434b2aaf8a89a84148802e`).
- Exact crop: `.../source_crops/luigi_mella_santelia_crop.png` with equality proof in `.../source_crops/luigi_mella_santelia_crop.json` (`decoded_pixels_equal: true`).
- Repaint: `docs/assets/006_independence_wave/iw018_arx_portrait_repaint_v76_2026_08_01/repaints_raw/ARX_luigi_mella_santelia_hoi4_repaint_v1.png` (SHA-256 `5846498cfd7a3b5c550557ef19a6d3eebe7b4473c2bff536233d52866ed468ae`).
- Candidate: `.../repaints_processed/portrait_ARX_luigi_mella_santelia_156x210_candidate.png` (SHA-256 `654f63c265154bf777538f0bd6eea50b126ad6a44bed4c6e6c5f22387d3dcb0b`).
- Review sheet: `.../review/ARX_mella_verne_source_raw_candidate_references_full_chain_4x.png`; the Mella panels are readable at native and enlarged scale against the leader-reference family.
- Source and role records: `.../source_records/luigi_mella_santelia_senate.md` and `.../research/role_evidence.md` record `CC BY 3.0 IT` (`senato.it` attribution required), Sassari birth, court service, and life through the 1936 start window; they do not call him a 1936 senator.

### Vittorio Vernè

- Archival master: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_29/arx_sardinia_sources_v15/source_masters/vittorio_verne_commander_commons.jpg` (200x250, SHA-256 `de94df14318398914a51aa0fb6601f9c31f916cc98d3803b313fe33be15f1417`).
- Exact crop: `.../source_crops/vittorio_verne_commander_crop.png` with equality proof in `.../source_crops/vittorio_verne_commander_crop.json` (`decoded_pixels_equal: true`). The v15 JSON points to the earlier copied source path but carries the same master hash; canonicalize that path in the final attribution record.
- Repaint: `docs/assets/006_independence_wave/iw018_arx_portrait_repaint_v76_2026_08_01/repaints_raw/ARX_vittorio_verne_hoi4_repaint_v1.png` (SHA-256 `8eda9fa779b0668ace9b5c277333f56a5bb672bfa9748acb85e685952554f6c5`).
- Candidate: `.../repaints_processed/portrait_ARX_vittorio_verne_156x210_candidate.png` (SHA-256 `3c699067912e15df3469c6ceda1a82e12326f808ef838fd896589a5cee2fe1d9`).
- Review sheet: `.../review/ARX_mella_verne_source_raw_candidate_references_full_chain_4x.png`; the candidate is visually legible against the commander reference panel, but the low-resolution side-profile source limits identity confidence more than the Lussu and Mella sources.
- Source and role records: `.../source_records/vittorio_verne_commander.md` and `.../research/role_evidence.md` record an anonymous `anni 30` photograph, `PD-Italy` plus `PD-1996`, 1936 major-general command, and a Sardinia-linked formation connection. They also explicitly record Rome birth.

## Cross-package findings and remaining gates

- The candidate hashes and dimensions match the v76 processing metadata, and all three exact-crop JSON files prove decoded-pixel equality to their archival masters.
- Manual native/enlarged review confirms restrained gouache/oil treatment, readable facial landmarks, period clothing, and no text, UI, or modern props.
- The canonical vanilla references used by the sheets are under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/`: leader references `leaders/den_thorvald_stauning.png` and `leaders/fin_carl_mannerheim.png`, and the commander reference `commanders/ita_pietro_badoglio.png`.
- The Vernè processing JSON lists `reference_dir: .../portraits/commanders` with `selected_references: [fin_carl_mannerheim.png]`, but that file exists only under `portraits/leaders`; the visible review sheet uses the commander-family panel. Correct this metadata crosswalk before promoting the package.
- Lussu has an existing target consumer at `common/characters/006_independence_wave_mediterranean_characters.txt:91-98` and localisation `ARX_emilio_lussu`. Mella and Vernè are proposed replacements only; current `ARX_vittorio_pala` and `ARX_gavino_piras` names and sprites remain unchanged.
- Runtime policy still requires the source attribution (`senato.it` for Lussu/Mella; Commons PD-Italy/PD-1996 record for Vernè) to be carried into the durable release manifest, followed by parent-owned DDS conversion, `.gfx` validation, and character/localisation alignment.
- No advisor, `_small`, operative, dossier, or commander derivative is cleared by this audit.

## Validation and limitations

- Reviewed all three archival masters/crops, raw repaints, 156x210 candidates, both full-chain review sheets, per-subject processing metadata, source records, ownership/role evidence, and the current ARX character/GFX consumer blocks.
- No game launch or in-game validation was performed, as required.
- This is a portrait-package audit, not country-package admission. The Sardinian-born versus Sardinia-linked role decision for Vernè, the replacement of the two blocked placeholders, attribution promotion, and all runtime wiring remain with the parent.
