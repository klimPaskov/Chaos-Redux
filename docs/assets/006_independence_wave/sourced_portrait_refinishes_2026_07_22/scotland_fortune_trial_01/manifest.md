# Victor Morven Fortune source-locked portrait trial

Status: **candidate awaiting independent visual and provenance audit; not approved for runtime wiring**

This package contains one sourced real-male Scottish territorial-command portrait candidate. It creates no advisor, dossier, `_small`, female, fictional, flag, focus, decision, localisation, gameplay, interface, or runtime asset.

## Subject and role

- Event 006 package: IW-001, Scotland (`SCO` vanilla carrier with additive Event 006 content only).
- Stable role and consumer: `SCO_independence_wave_territorial_commandant`, emergency head and army corps commander.
- Subject: Major-General Sir Victor Morven Fortune (1883–1949).
- Role basis: Scottish-born Black Watch officer; commanded the 52nd (Lowland) Division in 1935–36 and later the 51st (Highland) Division.
- Ownership gate: the Event 006 source-research handoff reports no active vanilla or current Chaos Redux character ownership hit. Reference-mod same-person use, if any, is disclosure-only and grants no permission to copy art or sources.

## Archival sources and rights

- Commons close-portrait page: <https://commons.wikimedia.org/wiki/File:Fortune_Victor_Morven.jpg>
- 51st Highland Division archive/context page: <https://51hd.co.uk/photos/img110>
- Direct Commons upload: <https://upload.wikimedia.org/wikipedia/commons/b/bc/Fortune_Victor_Morven.jpg>
- Credit: Imperial War Museum, War Office Second World War Official Collection, RML 342.
- Date: 12 June 1940.
- Rights basis: UK-government public-domain scan (`PD-scan`/`PD-UKGov`) as recorded by Commons and the source-research ledger.
- Close master: `source_masters/SCO_victor_fortune_iwm_1940_portrait.jpg`, `200x250`, SHA-256 `830F175712988C825A604E48464584DC0B71CD61B51AB423E2BADC0C1A46D049`.
- Same-person context master: `source_masters/SCO_victor_fortune_51hd_mid_1940.jpg`, `580x609`, SHA-256 `6F2A686283BB796B6CD81003EFD12A4C40135709EAFEE3C0E4E50E438F5F3392`.
- Explicit head-and-shoulders crop: the complete close archival portrait `(0, 0, 200, 250)`, retained as `source_crops/SCO_victor_fortune_head_shoulders.jpg`, same SHA-256 as the unchanged close master.

The 1940 source is later than the 1936 start and remains disclosed. It is not used to claim an earlier uniform photograph.

## Source-locked repaint

- Identity inputs: only the close archival portrait and the same-person 51st Highland Division context image above.
- Style-only reference: `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/commanders/eng_bernard_montgomery.png`.
- Prompt: `prompts/SCO_victor_fortune_identity_preserve_trial_01.txt`.
- ImageGen result: `imagegen_results/SCO_victor_fortune_identity_preserve_trial_01.png`, `1086x1448`, SHA-256 `A9033E201A25A3D8412FEAB6D4B50480729E2ADF3EB811820967C357F972E16F`.
- Finish command: skill-local `advisor_icon_processing.py leader`, source kind `real`, explicit result crop `(0, 0, 1086, 1448)`, canonical vanilla leader review directory.
- Processed `156x210` PNG: `processed_png/portrait_SCO_independence_wave_territorial_commandant.png`, SHA-256 `AA9A8E267444DC01B49C942E2C2D74C4ED9C90FB12F7F38F5C0FCF26941CFB7D`.
- Processor sheet: `contact_sheets/SCO_victor_fortune_source_result_reference.png`, SHA-256 `A940C3B0B1D6585FF2AAC934111D8F282ED67B5252919D19E7FF50357F0DB86D`.
- Archival/result comparison: `contact_sheets/SCO_victor_fortune_archival_result_comparison.png`, SHA-256 `0E10380DE0A9B1021996C4FE7165801CBEFC3339B50AA0DEBCDE266A55554F2B`.
- Processor metadata: `metadata/SCO_victor_fortune_processing.json`.

The candidate preserves Fortune's broad face, compact moustache, narrowed eyes, straight nose, firm mouth, jaw, 1940 cap, service dress, and serious expression. Independent review must reject it if the low-resolution evidence cannot support identity at native size, if the cap or insignia have been materially invented, or if the finish reads as generic military art rather than the same man.

## Runtime gate

Do not copy this candidate into `gfx/leaders/006_independence_wave/`, convert it to DDS, register or change a sprite, edit the character, or reopen IW-001 on this package alone. Scotland also needs an independently approved R. B. Cunninghame Graham civic portrait, exact runtime wiring, and a fresh full country-package audit.
