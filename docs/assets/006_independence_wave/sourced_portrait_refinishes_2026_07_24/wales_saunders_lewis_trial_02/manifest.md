# Saunders Lewis source-locked portrait trial 02

Status: `rejected_identity_runtime_hold`

## Immutable archival source

- Subject: Saunders Lewis (1893–1985), real male Welsh nationalist, writer, Great War veteran, and living Welsh self-government figure in 1936.
- Unchanged source master: `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/wales_saunders_lewis_trial_01/source_masters/WLS_saunders_lewis_ydrych_1916.jpg`.
- Source dimensions: `1016x2239`.
- Source SHA-256: `D1552EA79F34D162E972EBE0528C219755E52F851226D6E07EF560E8C29B80E3`.
- Source record: *Y Drych*, 3 February 1916, photographer not stated; National Library of Wales newspaper page and Commons Public Domain Mark/pre-1931 publication basis retained in trial 01.
- Explicit identity crop: `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/wales_saunders_lewis_trial_01/source_crops/WLS_saunders_lewis_ydrych_1916_head_shoulders.png`.
- Crop rectangle in source pixels: `(210, 200, 800, 994)`.
- Crop dimensions: `590x794`.
- Crop SHA-256: `EB0F03982A3D2B6B2C06DD766C21489B447D8488DB9F28645C666CA3C1A672AA`.

## Trial purpose

Trial 01 passed its HOI4 style gate but failed independent likeness review because it enlarged, rounded, brightened, and symmetrized the eyes and regularized weakly evidenced facial planes.

Trial 02 uses the exact same immutable source and crop, explicitly preserves the small deep-set asymmetric eyes and source ambiguity, and forbids reconstructed eye whites, irises, highlights, or hidden facial detail.

## Source-locked repaint

- Prompt: `prompts/WLS_saunders_lewis_identity_preserve_trial_02.md`.
- Identity input: exact crop above.
- Style-only references: `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/leaders/den_thorvald_stauning.png` and `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/leaders/afg_mohammed_zahir_shah.png`.
- Raw ImageGen result: `imagegen_results/WLS_saunders_lewis_identity_preserve_trial_02.png`, `1083x1452`, RGB, SHA-256 `4C81E29529006EBFE80AEEEF2F2D30985E812C36B32D137D54DFEE8BD42E5835`.
- Deterministic processing used `retired_advisor_card_processor_REMOVED` in `leader` mode, source kind `real`, raw-result crop `(3, 0, 1080, 1450)`, and the canonical leader reference directory.
- Deterministic candidate: `processed_png/portrait_WLS_independence_wave_national_council.png`, `156x210`, RGBA, SHA-256 `DD5946C65458FB85D4A136A768F9B0B946F0A9A1B5380505AD5B17652E163A3D`.
- Processor metadata: `metadata/WLS_saunders_lewis_trial_02_processing.json`, SHA-256 `78B6881254AFB23456C819F1A540C055C5EBF35DAF850C8B9FE7FA77899CFA12`.
- Processor style sheet: `review_sheets/WLS_saunders_lewis_trial_02_processor_style_comparison.png`, `1344x464`, SHA-256 `D6BCAF653E1816DA5ECA2054EA8D1E9498EA17F8F170CD239D238C4A88ECB43D`.
- Evidence limitation: the processor sheet labels its first panel as an explicit source crop, but that panel is the crop of the raw ImageGen result. Independent review must separately compare the immutable archival master and exact archival crop recorded above.
- Independent audit: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_wls_lussu_trial_visual_provenance_audit_2026_07_24.md`.
- Provenance, HOI4 style, framing, ownership, role, consumer-boundary, and male-only gates: `PASS`.
- Likeness/identity gate: `FAIL`.
- Runtime authorization: `FAIL`.
- Trial 02 materially improves trial 01's enlarged and bright eyes, but it still regularizes and near-symmetrizes the source's small deep-set asymmetric eyes, frontalizes the face, smooths weakly evidenced facial planes, and can read as a generic young soldier at native size.
- No candidate DDS was created or wired.
- Further work requires a stronger archival source or a new source-locked pass from archival evidence; this rejected result must not be used as an identity source.

## Consumer boundary

The only proposed consumer is `WLS_independence_wave_national_council` through the existing full-size sprite `GFX_portrait_WLS_independence_wave_national_council`.

No advisor, dossier, `_small`, commander, operative, alternate-country, or unrelated consumer is authorized.

This candidate remains unwired and may not be converted, resized into a fallback, or substituted for the existing stable runtime texture.
