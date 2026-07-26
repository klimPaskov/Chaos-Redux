# IW-007 Frisia Douwe Kalma portrait trial 02

Status: `approved_and_promoted`.

This is the approved grounded real-person portrait for the existing AGX civic-leader consumer. It follows the required unchanged archival master -> exact head-and-shoulders crop with equality JSON -> source-locked ImageGen repaint -> deterministic 156x210 processing -> independent audit -> DDS promotion sequence. The stable `.gfx` consumer path was preserved.

| Field | Value |
| --- | --- |
| Subject | Douwe Kalma, real male Frisian writer and nationalist |
| Stable consumer | `AGX_friesland_coastal_council` / `GFX_portrait_AGX_friesland_coastal_council` |
| Source master | `source_masters/AGX_douwe_kalma_1917_master.jpg` |
| Source master SHA-256 | `38DAFCBFF7C3A67B6B29B9B637E69FF4C2F9D8CAAE076361200919A6BB36DBDF` |
| Exact crop | `source_crops/AGX_douwe_kalma_1917_head_shoulders.png`; `(50,80,640,876)`; equality JSON retained beside it |
| Raw ImageGen result | `imagegen_results/AGX_douwe_kalma_identity_preserve_trial_02.png`; SHA-256 `C6A4419F7604D939548831FCAB520039C6440B9F964592B9DE8FA08EC5192EA1` |
| Processed candidate | `processed_png/portrait_AGX_friesland_coastal_council.png`; exact `156x210`; SHA-256 `dec3eb32366e500da0b4016df6bc7a96d3a02686ab57858944790f1e83233f3c` |
| Style family | `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/` and curated male leader references |
| Prompt | `identity_repaint_prompt.md` |
| Review sheet | `review/AGX_douwe_kalma_leader_style_sheet.png` |
| Metadata | `processed_png/portrait_AGX_friesland_coastal_council.png.json` |
| Independent audit | `docs/plans/006_independence_wave_plans/subagent_handoffs/006_agx_portrait_trial2_independent_audit_2026_07_26.md`; separate provenance, crop, likeness, style, framing, role, ownership, and forbidden-derivative PASS |
| Promoted DDS | `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_council.dds`; uncompressed BGRA `156x210`, 131168 bytes; SHA-256 `85240FF6700BBEBAED9EEBA838F9B503D9D42A7E55CEF6DF2D8C71DC86C33D1E`; package copy retained under `review/` |
| Previous runtime DDS | Retained under `review/previous_runtime_portrait_AGX_friesland_coastal_council.dds`; SHA-256 `2A98ECB576B331915E2B626C9CCC6DC03AF4012A411717B73D2F5253358E15A2` |

The source crop is the sole identity authority. The prompt forbids face substitution, beautification, symmetrization, frontalization, unsupported clothing or insignia, and hidden-detail invention. The independent audit approved the candidate before DDS conversion; no advisor, dossier, `_small`, female, or alternate-person derivative was created.
