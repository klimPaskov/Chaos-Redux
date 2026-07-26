# IW-007 Frisia Pieter Reenalda portrait trial 02

Status: `approved_and_promoted`.

This is the approved grounded real-person portrait for the existing AGX maritime commander consumer. It follows the required unchanged archival master -> exact head-and-shoulders crop with equality JSON -> source-locked ImageGen repaint -> deterministic 156x210 processing -> independent audit -> DDS promotion sequence. The stable `.gfx` consumer path was preserved.

| Field | Value |
| --- | --- |
| Subject | Pieter Reenalda, real male Frisian KPM first officer |
| Stable consumer | `AGX_friesland_coastal_commander` / `GFX_portrait_AGX_friesland_coastal_commander` |
| Source master | `source_masters/AGX_pieter_reenalda_1919_uniform_master.jpg` |
| Source master SHA-256 | `8F93840B12ECDCB313279C6F0FD4027863F8C1C4C9232E699AA7A0A9D46668CE` |
| Exact crop | `source_crops/AGX_pieter_reenalda_1919_head_shoulders.png`; `(203,130,1003,1207)`; equality JSON retained beside it |
| Raw ImageGen result | `imagegen_results/AGX_pieter_reenalda_identity_preserve_trial_02.png`; SHA-256 `3C9D6D44410D9001C791AC6A700689A94FC61FC6B62E7DE06947FF1E67145E4D` |
| Processed candidate | `processed_png/portrait_AGX_friesland_coastal_commander.png`; exact `156x210`; SHA-256 `840e5708fa1c9f5424d5524bb93d661c39a5d888f85a34cad96d74cbcedbf856` |
| Style family | `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/` and curated male commander references |
| Prompt | `identity_repaint_prompt.md` |
| Review sheet | `review/AGX_pieter_reenalda_commander_style_sheet.png` |
| Metadata | `processed_png/portrait_AGX_friesland_coastal_commander.png.json` |
| Independent audit | `docs/plans/006_independence_wave_plans/subagent_handoffs/006_agx_portrait_trial2_independent_audit_2026_07_26.md`; separate provenance, crop, likeness, style, framing, role, ownership, and forbidden-derivative PASS |
| Promoted DDS | `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_commander.dds`; uncompressed BGRA `156x210`, 131168 bytes; SHA-256 `E84D790AB245F5E14BAADB71D0C66438DCB04586131F4B98893B0A4CBC8E8137`; package copy retained under `review/` |
| Previous runtime DDS | Retained under `review/previous_runtime_portrait_AGX_friesland_coastal_commander.dds`; SHA-256 `07689A7045C145401E5AA7A2CFC1AE0949D59C62D4B64F144714E20197558BBA` |

The source crop is the sole identity authority. The prompt forbids face substitution, beautification, symmetrization, unsupported medals or insignia, colored shoulder-board invention, and hidden-detail invention. The independent audit approved the candidate before DDS conversion; no advisor, dossier, `_small`, female, or alternate-person derivative was created.
