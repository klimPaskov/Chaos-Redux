# Deferred source-locked repaint plans

These notes define the source-locked handoff. The Galimzhan row has since been advanced by a parent-authorized producer through v1 and v2 ImageGen HOI4-style repaints and deterministic leader processing; v2 has passed the independent likeness/style/provenance audit, while all other rows remain planning-only unless their status gate is explicitly advanced. A raw original-size master belongs in the single flat `portraits_generated_png/` shelf, while normalized candidates and review evidence remain in the package workspace. No row is runtime-approved without an independent likeness/style/provenance pass.

## Shared HOI4 leader-family contract

Use the exact crop in `source_crops/` as the identity reference and compare the raw repaint, processed `156x210` candidate, and review sheet against the unchanged source and the canonical leader references at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/`. Keep a restrained head-and-shoulders or upper-bust frame, subdued HOI4-painted finish, quiet period background, and no text, watermark, modern UI, invented symbols, or genericized facial features. Preserve age, pose, asymmetry, eye/nose/mouth geometry, hair and facial hair, visible hat, spectacles, uniform, and medals exactly as supported by the source. Do not invent hidden clothing, rank marks, religious emblems, or route insignia.

## CHU federal presidium — Galimzhan Ibrahimov

Use `source_crops/CHU_federal_presidium_galimzhan_ibrahimov_head_shoulders.png` as the source-locked identity reference. Retain the distinctive brimmed hat, moustache, three-quarter angle, overcoat collar, and monochrome source texture while translating the image into the canonical country-leader family. The setting may suggest a restrained Volga civic chamber through a soft neutral background, but no Tatar or Soviet emblem should be added unless it is visible in the source. The role remains a Tatar federal-presidium office, not a claim that Ibrahimov historically held this fictional body.

The superseded v1 raw repaint is `repaints_raw/CHU_federal_presidium_galimzhan_ibrahimov_hoi4_repaint_v1.png`, and the audited v2 raw repaint is `repaints_raw/CHU_federal_presidium_galimzhan_ibrahimov_hoi4_repaint_v2.png`; both are copied byte-for-byte to the flat event shelf. The v2 processor candidate is `repaints_processed/CHU_federal_presidium_galimzhan_ibrahimov_156x210_v2_candidate.png`, with review sheet `review/CHU_federal_presidium_galimzhan_ibrahimov_v2_processing_review.png`, prompt record `repaint_plans/CHU_federal_presidium_galimzhan_ibrahimov_hoi4_repaint_v2_prompt.md`, and provenance record `processing_metadata/CHU_federal_presidium_galimzhan_ibrahimov_repaint_v2_provenance.json`. The v2 audit handoff records PASS for likeness, style, crop, artifacts, and provenance with the archival-source uncertainties retained. DDS conversion and runtime wiring remain parent-owned promotion steps.

## CHU river security directorate — Ahmet Zeki Velidi Togan

Use `source_crops/CHU_river_security_directorate_validi_togan_head_shoulders.png` as the identity reference only after the separate source institution/date/role review passes. Preserve the round spectacles, close-cropped hair, narrow moustache, dark collar, and direct gaze. Keep the repaint civilian or plainly administrative; do not add a Bashkir/Tatar flag, religious symbol, or unsupported military insignia. If the reviewer rejects the Bashkir-to-CHU transfer, keep the row blocked rather than substituting Musa Dzhalil or a generic river officer.

## ASY civic national assembly — Naum Faiq

Use `source_crops/ASY_civic_national_assembly_naum_faiq_head_shoulders.png` as the identity reference only if the parent accepts a legacy/memorial continuity reading despite Faiq's 1930 death. Preserve the parted hair, moustache, suit, tie, frontal pose, and source-visible expression. Use a quiet civic chamber background with no invented church symbols, flags, or modern clothing. If a living-1936 Assyrian civic source is required, this candidate returns to `needs_user_review` and must not be cosmetically updated into a different person.

## ASY Levies guardianship — Agha Petros

Use `source_crops/ASY_levies_guardianship_agha_petros_head_shoulders.png` as the identity reference only if the parent accepts a legacy/memorial continuity reading despite Petros's 1932 death. Preserve the moustache, seated pose, Levies-era uniform, medals, and visible shoulder details. Repaint into the HOI4 leader family without adding unsupported British rank insignia, extra medals, modern weapons, or invented Assyrian symbols. The route may use a faint administrative/security-room background, but the person must remain the focal identity.

## Blocked rows

No repaint plan may advance the Shamil Usmanov crop until a higher-resolution redistributable master is found. No repaint plan may advance the Mar Benyamin Shimun crop because the subject died in 1918; Mar Eshai Shimun XXIII and Malik Ismail II leads remain rights-blocked. Do not generate or cosmetically alter a different real person to fill either slot.
