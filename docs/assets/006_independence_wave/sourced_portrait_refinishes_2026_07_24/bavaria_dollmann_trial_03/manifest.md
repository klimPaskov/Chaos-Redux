# IW-009 Bavaria Friedrich Dollmann trial 03

Status: `independently_approved_converted_and_runtime_wired`.

The independent audit at `../../../../plans/006_independence_wave_plans/subagent_handoffs/006_bavaria_dollmann_trial03_independent_portrait_audit_2026_07_24.md` passes likeness, HOI4 commander style, provenance, rights, ownership, evidence integrity, role fit, stable-consumer fit, and the forbidden advisor/`_small` boundary.

Parent integration reconciled the stable token's display identity from Eugen Ritter von Schobert to Friedrich Dollmann before conversion and runtime promotion.

This portrait approval does not by itself grant IW-009 package content attestation.

## Grounded subject and stable consumer

- Subject: Friedrich Karl Albert Dollmann.
- Presentation: male.
- Historical role fit: Würzburg-born Royal Bavarian Army officer used as Bavaria's alternate-history emergency passes-and-depots commandant.
- Stable character token: `BAY_independence_wave_mountain_commandant`.
- Stable sprite: `GFX_portrait_BAY_independence_wave_mountain_commandant`.
- Reserved runtime texture: `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_mountain_commandant.dds`.
- Ownership gate: PASS in `../../sourced_portrait_replacements_2026_07_24/bavaria_dollmann_source_retry/ownership_scan.md`; no same-person current project, vanilla, or approved-reference-mod character owner was found.

## Archival identity evidence

- Source archive: German Federal Archive.
- Accession: `Bundesarchiv, Bild 101I-052-1435-20`.
- Source page: <https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_101I-052-1435-20,_Oberrhein,_Befestigung_am_Isteiner_Klotz.jpg>.
- Official archive search record: <https://www.bild.bundesarchiv.de/dba/de/search/?query=Bild+101I-052-1435-20>.
- License: `CC BY-SA 3.0 Germany`.
- Required attribution: `Bundesarchiv, Bild 101I-052-1435-20 / CC-BY-SA 3.0`.
- Unchanged master: `../../sourced_portrait_replacements_2026_07_24/bavaria_dollmann_source_retry/source_masters/BAY_friedrich_dollmann_bundesarchiv_1940_original_533x800.jpg`.
- Unchanged master SHA-256: `15D387707C22E7B73B513961AAE7EB42F40E3E296FF4A68E8AAB6B5DA6E82E12`.
- Exact source crop: `../bavaria_dollmann_trial_02/source_crops/BAY_friedrich_dollmann_exact_head_shoulders_300_120_500_450.png`.
- Exact source crop coordinates: `(300,120)-(500,450)` against the unchanged `533x800` master.
- Exact source crop SHA-256: `D3A70235D56B6E8255AF31BD8330975BD1FC42370D1278272262EE210B9CDF97`.
- Equality evidence: `../bavaria_dollmann_trial_02/source_crops/BAY_friedrich_dollmann_exact_head_shoulders_300_120_500_450.json`.
- Equality-evidence SHA-256: `6D87A0BA4C7494069D16F16A7D58AA7D62574266629F4A431AA0F0DF861991D8`.
- Decoded-pixel equality: PASS; reopened crop and decoded master rectangle share RGBA SHA-256 `1C910471860E2EDE9F5B446613FD419C24AFED8F60CC500337645181240FBFE9`.
- Master/crop comparison evidence: `../../sourced_portrait_replacements_2026_07_24/bavaria_dollmann_source_retry/evidence/BAY_friedrich_dollmann_source_master_crop_comparison.png`.

## Source-locked ImageGen repaint

- Input: the exact source crop above and no other identity image.
- Prompt record: `identity_repaint_prompt.md`.
- Raw result: `imagegen_results/BAY_friedrich_dollmann_identity_preserve_trial_03.png`.
- Raw result dimensions: `977x1609`.
- Raw result SHA-256: `47D143EE3537DF7060B43EAE88C23CFBF03BDCDB900DBF9CF500949784EAD64D`.
- Identity constraints: preserve the source-visible male face, age, proportions, spectacles, expression, and pose; replace the source's later political-era insignia with an unmarked early-1930s Bavarian territorial-command uniform.

The raw result is evidence and processor input only.

It is not an approved runtime portrait.

## Deterministic commander processing

- Processor: `.agents/skills/chaos-redux-event-assets/tools/advisor_icon_processing.py`.
- Processor version: `5.0`.
- Processor SHA-256: `1ADB521B43238EE971E093DAE90007C4C44C600435EBB897C6482BA3B64B96EC`.
- Python: `3.9.12`.
- Pillow: `11.1.0`.
- Role family: `commander`.
- Source kind: `real`.
- Processor crop: `(70,80)-(954,1270)` against the raw ImageGen result.
- Processed candidate: `processed_png/portrait_BAY_independence_wave_mountain_commandant.png`.
- Processed dimensions: `156x210`.
- Processed SHA-256: `485F725555C9D6C71FCFA62742F6B724630E8573F874590C552643B6DF63D9E9`.
- Processed decoded RGBA SHA-256: `4F5D42E55CE9183996BE4FCB26E6EC8873510783CC7D2D65E2A600AFBBD484C8`.
- Processor metadata: `processed_png/portrait_BAY_independence_wave_mountain_commandant.png.json`.
- Processor metadata SHA-256: `7EEFCE17170EE5180A1CC1D09D39B2622D47FFBAE1424E6836A68C81914EA43C`.
- Commander-family review sheet: `review/BAY_friedrich_dollmann_commander_style_sheet.png`.
- Review-sheet SHA-256: `DFE235A21279B827218A6D9F8C805A7D653289E20B0FD9B58C10032C8145E965`.
- Canonical style controls: Montgomery SHA-256 `39B03871D7451CA96712A5CCF3C056528693F82642776E6C5E297E041943944E` and Witzleben SHA-256 `10F4A1108F9D440213F70FB5802349A2291F298F9D132644241119561577D5B6`.

The processor records the required pre-audit state `candidate_requires_visual_approval`.

The independent audit subsequently passes the candidate.

## Required independent audit

An auditor other than the producer must compare the unchanged master, exact archival crop, raw ImageGen result, processed `156x210` candidate, and commander references at native size and at least `4x` nearest-neighbour inspection.

The auditor must issue separate verdicts for:

- likeness and identity preservation;
- HOI4 commander-family painted style;
- provenance, ownership, attribution, and evidence integrity;
- role and stable-consumer fit;
- forbidden advisor and small-portrait assets;
- readiness for DDS conversion and runtime wiring.

Style quality cannot compensate for a likeness or provenance failure.

All mandatory gates passed in the independent audit.

## Final DDS and stable runtime wiring

- Evidence DDS: `final_dds/portrait_BAY_independence_wave_mountain_commandant.dds`.
- Runtime DDS: `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_mountain_commandant.dds`.
- Dimensions: `156x210`.
- Evidence/runtime SHA-256: `332D8578F4BDEDE1A9FEAD234B361AA8C9FD786D5261CB45DBEA56475754DBAB`.
- Converter: `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`.
- Sprite: `GFX_portrait_BAY_independence_wave_mountain_commandant`.
- Existing sprite owner: `interface/006_independence_wave_region_01_portraits.gfx`.
- Character token: `BAY_independence_wave_mountain_commandant`.
- Character consumer: full-size civilian-large and army-large commander portrait only.
- Localisation: `localisation/english/006_independence_wave_rhineland_bavaria_l_english.yml` names Friedrich Dollmann and describes the emergency passes-and-depots role.

The stable `.gfx` definition already pointed at the reserved runtime texture, so no sprite-name or texture-path edit was necessary.

No advisor, high-command, dossier-card, operative, `_small`, or fabricated `50x67` asset was created.

Protected `portrait_BAY_rupprecht_of_bavaria.dds` remains SHA-256 `7F0AF64FDF4FECD49DF454D1198935BB3CE6A8F74AFC1AC82F8223704EAAAD2B`.

Protected `portrait_RHI_josef_friedrich_matthes.dds` remains SHA-256 `AA61CC3A12FB6670B690C7685FEB9383383CE58599C9E6D6E7C14F20FAB3BCE2`.
