# Emilio Lussu source-locked portrait trial 01

Status: `rejected_identity_runtime_hold`

## Immutable archival source

- Subject: Emilio Lussu (1890–1975), real male Sardinian soldier, politician, writer, and living Sardinian autonomy figure in 1936.
- Source page: <https://commons.wikimedia.org/wiki/File:Emilio_Lussu_WWI.jpg>.
- Source archive/date: Archivio Brigata Sassari, 1916.
- Creator: Giovanni Battista Diana.
- Rights record: Commons United States public-domain tag retained from the accepted source package.
- Unchanged source master: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/mediterranean_volga_assyria/source_masters/sardinia/arx_emilio_lussu_commons_original.jpg`.
- Source dimensions: `861x1107`.
- Source SHA-256: `B91EFC1DE64C98EC591A97E41FC79D1823D35EE8BE0797CE5525920736BA633A`.

## Explicit head-and-shoulders crop

- Crop rectangle in source pixels, left/top/right/bottom: `(175, 20, 710, 740)`.
- Crop: `source_crops/ARX_emilio_lussu_1916_head_shoulders.png`.
- Crop dimensions: `535x720`.
- Crop SHA-256: `24A8F9272A73614CC03F150518A03DAECF8171383C2A466E16FA87BA0FD1BBA8`.
- The crop is immutable identity evidence and is not a runtime portrait.

## Ownership and consumer boundary

- Current consumer: `ARX_emilio_lussu` through full-size sprite `GFX_portrait_ARX_independence_wave_emilio_lussu`.
- Installed vanilla scan: no Emilio Lussu character, recruitment, portrait, or localisation owner found.
- Kaiserreich has a same-person `SRI_emilio_lussu` owner. This is disclosure-only under the accepted mutually-exclusive-mod policy; no Kaiserreich source, portrait, or art was copied.
- Proposed runtime texture: `gfx/leaders/006_independence_wave/portrait_ARX_independence_wave_emilio_lussu.dds`.
- No advisor, dossier, `_small`, commander, operative, alternate-country, or unrelated consumer is authorized by this package.

## Source-locked repaint

- Prompt: `prompts/ARX_emilio_lussu_identity_preserve_trial_01.md`.
- Identity input: exact crop above.
- Style-only references: `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/leaders/ire_eamon_de_valera.png` and `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/leaders/den_thorvald_stauning.png`.
- Raw ImageGen result: `imagegen_results/ARX_emilio_lussu_identity_preserve_trial_01.png`, actual decoded dimensions `1082x1454`, RGB, SHA-256 `2913582D0DFF6159651486A58BE1987CB38BF5DCB087519CC6FDF6BAC7C7F85C`.
- Deterministic processing used `retired_advisor_card_processor_REMOVED` in `leader` mode, source kind `real`, raw-result crop `(3, 0, 1080, 1450)`, and the canonical leader reference directory.
- Deterministic candidate: `processed_png/portrait_ARX_independence_wave_emilio_lussu.png`, `156x210`, RGBA, SHA-256 `8AE82FE2CDC1F6F4D129DD1FEA8603C90D479D324C1BE5B382FF8539958111A1`.
- Processor metadata: `metadata/ARX_emilio_lussu_trial_01_processing.json`, SHA-256 `ED8DF6B38D195CFF822B4B13E7AC8B242C5CDE3DD2A2D979B964087DDFD68BDB`.
- Processor style sheet: `review_sheets/ARX_emilio_lussu_trial_01_processor_style_comparison.png`, `1344x464`, SHA-256 `614CE42410AF8210E599E785C4A56D7DB1041E00D27BD74D73293709025DCA4F`.
- Evidence limitation: the processor sheet labels its first panel as an explicit source crop, but that panel is the crop of the raw ImageGen result. Independent review must separately compare the immutable archival master and exact archival crop recorded above.
- Independent audit: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_wls_lussu_trial_visual_provenance_audit_2026_07_24.md`.
- Provenance with the recorded United States public-domain jurisdiction caveat, HOI4 style, framing, ownership, role, consumer-boundary, and male-only gates: `PASS`.
- Likeness/identity gate: `FAIL`.
- Runtime authorization: `FAIL`.
- The archival viewer image-right eye is soft, blurred, and partly occluded, but the repaint draws unsupported eye geometry and also frontalizes and regularizes the face.
- No candidate DDS was created or wired.
- Further work requires a stronger archival source whose identity-bearing facial geometry is visible; this rejected result must not be used as an identity source.

This candidate remains unwired and may not be converted, resized into a fallback, or substituted for the existing stable runtime texture.
