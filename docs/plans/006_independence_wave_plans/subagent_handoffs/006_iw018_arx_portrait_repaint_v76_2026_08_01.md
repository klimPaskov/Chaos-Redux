# IW-018 ARX sourced HOI4 portrait repaint and runtime handoff v76/v77

Date: 2026-08-01

## Scope

This handoff records the source-locked, identity-preserving HOI4 repaint chain for the three promoted ARX consumers and the separate rights-gated Sardinian commander evidence candidate. The promoted roster is Emilio Lussu for the provisional assembly, Luigi Arborio Mella di Sant'Elia for the crown consultative council, and Vittorio Verne for the Sardinia-linked guard command. The stable internal `ARX_gavino_piras` script key remains for compatibility while its visible name is Verne. Exact Vittorio Pala and Gavino Piras identities remain blocked and are not relabelled. No advisor icons are created.

## Files produced

- `docs/assets/006_independence_wave/iw018_arx_portrait_repaint_v76_2026_08_01/repaints_raw/ARX_*_hoi4_repaint_v1.png`
- `docs/assets/006_independence_wave/iw018_arx_portrait_repaint_v76_2026_08_01/repaints_processed/portrait_ARX_*_156x210_candidate.png`
- `docs/assets/006_independence_wave/iw018_arx_portrait_repaint_v76_2026_08_01/processing_metadata/portrait_ARX_*_156x210.json`
- `docs/assets/006_independence_wave/iw018_arx_portrait_repaint_v76_2026_08_01/review/ARX_emilio_lussu_source_raw_candidate_references_full_chain_4x.png`
- `docs/assets/006_independence_wave/iw018_arx_portrait_repaint_v76_2026_08_01/review/ARX_mella_verne_source_raw_candidate_references_full_chain_4x.png`
- `docs/assets/006_independence_wave/iw018_arx_portrait_repaint_v76_2026_08_01/review/ARX_solinas_source_raw_candidate_commander_reference_full_chain_4x.png`
- `docs/assets/006_independence_wave/iw018_arx_portrait_repaint_v76_2026_08_01/tools/normalize_arx_sourced_portraits.py`
- `docs/assets/006_independence_wave/iw018_arx_portrait_repaint_v76_2026_08_01/manifest.md`
- `docs/assets/006_independence_wave/iw018_arx_portrait_repaint_v76_2026_08_01/gfx_handoff.md`
- `docs/assets/006_independence_wave/iw018_arx_portrait_repaint_v76_2026_08_01/audit_v76.md`
- `docs/assets/006_independence_wave/portraits_generated_png/portrait_ARX_*_hoi4_master.png`
- `docs/assets/portraits/006_independence_wave/portrait_ARX_*_source.*` and matching prompts
- `gfx/leaders/006_independence_wave/portrait_ARX_independence_wave_emilio_lussu.dds`
- `gfx/leaders/006_independence_wave/portrait_ARX_luigi_mella_santelia.dds`
- `gfx/leaders/006_independence_wave/portrait_ARX_vittorio_verne.dds`

## Evidence and validation

Lussu and Mella carry CC BY 3.0 IT source records. Verne carries PD-Italy plus PD-1996 evidence. Solinas carries PD-Italy-only evidence and remains rights-gated. Each promoted subject has an explicit head-and-shoulders crop, source-locked ImageGen repaint, deterministic 156x210 RGBA output, independent v77 likeness/style/provenance review, corrected consumer sprite, and byte-matched runtime DDS. DDS files are 156x210 BGRA with 131168-byte headers and non-zero alpha. The flat shelf contains only original-size masters; no 156x210 shelf derivatives or advisor/small/dossier derivatives are authorized.

## Admission status

The explicit Mella and Verne identity/role replacements are wired in `common/characters/006_independence_wave_mediterranean_characters.txt`, `interface/006_independence_wave_mediterranean_portraits.gfx`, and localisation. IW-018 is included in `has_independence_wave_runtime_package_content_attestation_for_execution_id`; the post-wire country-package audit and exact allocator audit are the current admission authority. Solinas has no runtime DDS. The exact Pala/Piras identities remain blocked rather than silently renamed.

## No advisor assets

No advisor icon or other advisor visual is created, referenced, or inferred by this handoff.
