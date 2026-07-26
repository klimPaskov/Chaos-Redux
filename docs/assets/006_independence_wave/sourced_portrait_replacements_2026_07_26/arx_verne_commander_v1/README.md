# IW-018 ARX Vittorio Vernè commander candidate

This package is a source-preserving portrait candidate for the Sardinian-linked Event 006 commander role. It is not runtime admission. No DDS, `.gfx` edit, character edit, advisor icon, small portrait, or generated replacement was created.

## Evidence chain

- Source: `source/ARX/Vittorio_Verne_source.jpg`, unchanged 200x250 Commons binary, SHA-256 `de94df14318398914a51aa0fb6601f9c31f916cc98d3803b313fe33be15f1417`.
- Attribution: [Vittorio Vernè, Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Vittorio_Vern%C3%A8.jpg), source credited to Generals.dk / Regio Esercito, anonymous 1930s photograph.
- Rights: the source audit records both `PD-Italy` and `PD-1996`; retain the source page and audit evidence with any later promotion.
- Role evidence: Vernè is recorded as an Italian major-general active in 1936 and linked to the 176th Legion “Cacciatori Guide di Sardegna.” The current country-package research handoff accepts this as Sardinia-linked command evidence, not Sardinian birth.
- Exact crop: `crops/ARX/Vittorio_Verne_archival_crop.png` with equality JSON at `metadata/ARX/Vittorio_Verne_archival_crop.json`; rectangle `(7, 0, 193, 250)` and `decoded_pixels_equal = true`.
- ImageGen repaint: `repaints/ARX/Vittorio_Verne_identity_preserve_imagegen.png`, SHA-256 `dfd8d452b41f92ba56f685deb3c982eda0c89503a2ddeeb96508d1f6c5ff0569`.
- Deterministic candidate: `processed/ARX/Vittorio_Verne_156x210.png`, SHA-256 `d1ca3e6161b5e84acc509ec0d2a2c03b7907ec4f064d2b4641d121e1f32cacd8`, role family `commander`, status `candidate_requires_visual_approval`.
- Processor evidence: `processed/ARX/Vittorio_Verne_156x210.png.json` and `review/Vittorio_Verne_processor_review.png`.

## Required gate before wiring

An independent reviewer must compare the unchanged source, exact crop, raw repaint, processed 156x210 candidate, and the commander references, then record separate likeness, HOI4-style, provenance, ownership, and role-fit results. The candidate must remain fail-closed until every gate is `PASS` and the parent re-audits the complete ARX package. The candidate does not authorize changing the existing fictional `ARX_gavino_piras` consumer or adding a runtime DDS.
