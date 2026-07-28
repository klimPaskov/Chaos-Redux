# Event 006 CHU Galimzhan Ibrahimov v2 runtime promotion

Date: 2026-07-28.

Scope: parent-owned final promotion of the independently audited CHU federal-presidium country-leader portrait. This handoff does not admit CHU to the Event 006 runtime pool and does not create an advisor, commander, dossier, or alternate portrait.

## Promotion evidence

- Independent visual/provenance audit: `006_galimzhan_portrait_v2_independent_audit_2026_07_28.md` — visual likeness, HOI4 country-leader style, framing, crop integrity, artifact, and provenance gates PASS with the recorded KSU/photographer uncertainty.
- Input candidate: `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/repaints_processed/CHU_federal_presidium_galimzhan_ibrahimov_156x210_v2_candidate.png`, 156x210 RGBA, SHA-256 `5f54733be97f4008e265e4b21da2716e211533d56cfc4589612db089cb74c094`.
- Conversion command: `python -B .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --input docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/repaints_processed/CHU_federal_presidium_galimzhan_ibrahimov_156x210_v2_candidate.png --output gfx/leaders/006_independence_wave/portrait_CHU_independence_wave_federal_presidium.dds --width 156 --height 210`.
- Final runtime DDS: `gfx/leaders/006_independence_wave/portrait_CHU_independence_wave_federal_presidium.dds`, 131168 bytes, legacy uncompressed BGRA 156x210, SHA-256 `977e0f8d359930f75e01e380a36893ef6a8f25a5b1ce5bbd8cc3c2f3abf6b5f5`.
- Stable sprite retained: `interface/006_independence_wave_iw043_iw058_portraits.gfx` maps `GFX_portrait_CHU_independence_wave_federal_presidium` to the unchanged runtime texture path. `common/characters/006_independence_wave_iw043_iw058_characters.txt` remains the sole character consumer.

## Validation

- Runtime DDS was converted only after the independent audit PASS and was compared against the temporary conversion candidate byte-for-byte before promotion.
- DDS dimensions/header and exact file length were checked through the repository conversion workflow; no alternate `_small`, `50x67`, advisor, or dossier derivative exists in the promotion.
- The flat pre-DDS shelf remains unchanged: 51 original-size RGB repaint masters directly under `docs/assets/006_independence_wave/portraits_generated_png/`, no child directories, and no 156x210 PNGs in that shelf.
- No `.gfx`, localisation, character, focus, decision, country, flag, or runtime-attestation file was broadened by this promotion.

## Remaining boundary

CHU remains outside content attestation and automatic selection until the complete grounded roster, package setup/final validation/cleanup, host and anchor evidence, and country-package re-audit pass. The other five CHU/ASY rows remain source-only, blocked, or needs-user-review. This promotion is a single approved portrait consumer update, not a fallback or a package-readiness assertion.
