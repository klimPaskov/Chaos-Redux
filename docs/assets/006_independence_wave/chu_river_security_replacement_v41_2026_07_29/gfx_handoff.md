# IW-043 CHU River Security Directorate source handoff v41

Date: 2026-07-29 (Europe/Kyiv).
This is a sourced portrait replacement handoff. The independent v45 portrait audit passed and the existing `.gfx`/character consumer now points to the repository-standard DDS replacement. The wider IW-043 package remains outside central content attestation until its separate country-package gates pass.

## Reserved consumer

| Consumer | Existing sprite | Reserved runtime texture path | Source evidence | State |
| --- | --- | --- | --- | --- |
| `CHU_independence_wave_river_security_directorate` | `GFX_portrait_CHU_independence_wave_river_security_directorate` in `interface/006_independence_wave_iw043_iw058_portraits.gfx` | `gfx/leaders/006_independence_wave/portrait_CHU_independence_wave_river_security_directorate.dds` | `source_files/chu_luka_spasov_1938_ogoniok.jpg`; 900x1218 RGB, SHA-256 `C707F7F9C50DAE4F4EC0F91865E0DE97875367F95D0659039BC52F17B5799457`; Commons 1938 `Ogoniok` scan; `PD-Russia-1996` public-domain record | `portrait_audit_pass_runtime_promoted`; exact crop, repaint, 156x210 candidate, metadata, 4x sheet, DDS, and durable pair complete; wider IW-043 package remains unadmitted |

## Runtime boundary and remaining package work

1. Preserve the exact source master and hash; do not overwrite it.
2. Keep the explicit identity-preserving head-and-shoulders crop and equality JSON evidence immutable.
3. Use Spasov as a sourced male grounded officeholder; do not generate or substitute a real-person likeness.
4. Complete the source-locked HOI4 repaint, independent likeness/style/provenance audit, deterministic 156×210 candidate, and repository-standard DDS conversion under the existing sprite/path contract.
5. Continue the wider IW-043/IW-058 country-package admission work separately; this portrait PASS does not admit those packages.

## Current evidence package

- Export metadata: `processing_metadata/CHU_river_security_directorate_luka_spasov_156x210_v2.json`.
- Reproducible export script: `tools/normalize_leader_portrait.py`.
- Full-chain review sheet: `review/CHU_luka_spasov_source_raw_candidate_references_full_chain_4x.png`.
- Durable ComfyUI source/prompt pair: `docs/assets/portraits/006_independence_wave/portrait_CHU_independence_wave_river_security_directorate.png` and the matching `.txt` file; both use the runtime DDS basename.
- Runtime DDS: `gfx/leaders/006_independence_wave/portrait_CHU_independence_wave_river_security_directorate.dds` (`d4d6204767fcfda3a992d33d0c046c4df22546c8db2833857da96ee3261e0213`), 156x210 BGRA.

## Handoff uncertainty

The image is a halftone magazine scan rather than a glass-plate negative or museum master. Commons nevertheless records a clear `PD-Russia-1996` public-domain status, and the native 900×1218 scan is sufficiently detailed for the crop gate. Photographer identity remains unknown; do not add an attribution beyond `Ogoniok` no. 3 (1938) and the Commons public-domain record. The package treats Spasov as an official of the Chuvash ASSR and Middle Volga administrator/military veteran, not as an ethnicity claim.
