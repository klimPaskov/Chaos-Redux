# IW-018 ARX Emilio Lussu portrait repaint v76

This package records the source-locked, identity-preserving HOI4 repaint chain for the promoted ARX consumers: real Sardinian statesman Emilio Lussu, Sardinian-born royal-court statesman Luigi Arborio Mella di Sant'Elia, and Sardinia-linked Italian commander Vittorio Verne. Gioacchino Solinas remains a separate Sardinian-born evidence candidate under a PD-Italy-only rights hold. The promoted three-consumer chain is now aligned with ARX gameplay and exact IW-018 attestation.

## Source and processing chain

| Stage | Path | Status |
| --- | --- | --- |
| Immutable archival master | `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_29/arx_sardinia_sources_v15/source_masters/emilio_lussu_senate_pre1958.jpg` | CC BY 3.0 IT, source-ledger ready, SHA-256 recorded in processing metadata |
| Exact source crop | `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_29/arx_sardinia_sources_v15/source_crops/emilio_lussu_senate_pre1958_crop.png` | Full decoded-pixel equality proof retained by the v15 crop JSON |
| Raw ImageGen repaints | `repaints_raw/ARX_*_hoi4_repaint_v1.png` | Lussu 1054×1492 RGB, Mella 1116×1409 RGB, Vernè 1081×1455 RGB, and Solinas 1084×1451 RGB, each source-locked to an exact crop |
| Original-size flat masters | `docs/assets/006_independence_wave/portraits_generated_png/portrait_ARX_*_hoi4_master.png` | Byte-identical copies of the raw repaints; no 156×210 derivative is stored on the flat shelf |
| Deterministic candidates | `repaints_processed/portrait_ARX_*_156x210_candidate.png` | Full 156×210 RGBA candidates from the reproducible shared ffmpeg processor |
| Review sheets | `review/ARX_emilio_lussu_source_raw_candidate_references_full_chain_4x.png`, `review/ARX_mella_verne_source_raw_candidate_references_full_chain_4x.png`, and `review/ARX_solinas_source_raw_candidate_commander_reference_full_chain_4x.png` | Native and enlarged source, repaint, candidate, and vanilla leader/commander reference comparisons |
| Processing metadata | `processing_metadata/portrait_ARX_*_156x210.json` | Per-subject hashes, dimensions, crop rectangle, processor, references, and status |

## Review disposition

The parent visual review passes likeness and HOI4-style appearance for all four candidates at native and enlarged scale. The source ledger and exact-crop JSON pass provenance and crop equality. Lussu, Mella, and Verne have independent v77 subject-level visual review and are promoted to their role-correct runtime consumers; Solinas remains evidence-only with PD-Italy-only rights requiring review. Exact Vittorio Pala and Gavino Piras identities remain blocked and are not relabelled.

No advisor icon, dossier portrait, operative portrait, commander derivative, or `_small` derivative is created by this package.

## Durable prompt pair

The archival source copy and matching prompt are retained at `docs/assets/portraits/006_independence_wave/portrait_ARX_independence_wave_emilio_lussu_source.jpg` and `docs/assets/portraits/006_independence_wave/portrait_ARX_independence_wave_emilio_lussu.txt`. The pair is source evidence and does not authorize runtime promotion by itself.

## Runtime handoff boundary

The promoted runtime consumers are `ARX_emilio_lussu`, `ARX_luigi_mella_santelia`, and `ARX_vittorio_verne`, with byte-matched DDS files under `gfx/leaders/006_independence_wave/`. `ARX_gioacchino_solinas` remains evidence-only and has no runtime DDS. Character names, `.gfx` sprites, localisation, and the exact IW-018 package attestation are aligned. No advisor, dossier, operative, commander derivative, or `_small` derivative is created by this package.
