# Saunders Lewis source-locked portrait trial 01

Status: **candidate awaiting independent visual and provenance audit; not approved for runtime wiring**

This package contains one sourced real-male civic portrait candidate for IW-002 Wales. It contains no advisor, dossier, `_small`, female, fictional, flag, focus, decision, localisation, gameplay, interface, or runtime asset.

## Subject and role

- Event 006 package: IW-002, Wales (`WLS` vanilla carrier used additively).
- Stable role: `WLS_independence_wave_national_council`, civic/national country leader.
- Subject: Saunders Lewis (1893-1985), Welsh nationalist, writer, Great War veteran, and living Welsh self-government figure in 1936.
- Date caveat: the sourced portrait is from 1916 and shows Lewis as a young adult. The repaint preserves that sourced age and does not invent an unsourced 1936-age reconstruction.
- Ownership gate: accepted source research found no active vanilla or current Chaos Redux character owner. Independent audit must recheck before approval.

## Archival source

- Commons page: <https://commons.wikimedia.org/wiki/File:Saunders-lewis-y-drych-1916.jpg>.
- National Library of Wales page: <https://papuraunewydd.llyfrgell.cymru/view/3776384/3776392/60/>.
- Publication: `Y Drych`, 3 February 1916; photographer not stated.
- Rights basis recorded by the accepted source package: Commons Public Domain Mark and pre-1931 publication basis.
- Unchanged master: `source_masters/WLS_saunders_lewis_ydrych_1916.jpg`, `1016x2239`.
- Master SHA-256: `D1552EA79F34D162E972EBE0528C219755E52F851226D6E07EF560E8C29B80E3`.
- Explicit crop `(210, 200, 800, 994)`: `source_crops/WLS_saunders_lewis_ydrych_1916_head_shoulders.png`, `590x794`.
- Crop SHA-256: `EB0F03982A3D2B6B2C06DD766C21489B447D8488DB9F28645C666CA3C1A672AA`.

## Source-locked repaint

- Image 1: Saunders Lewis identity/clothing crop.
- Image 2 style-only reference: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/den_thorvald_stauning.png`.
- Prompt: `prompts/WLS_saunders_lewis_identity_preserve_trial_01.txt`.
- Retained ImageGen result: `imagegen_results/WLS_saunders_lewis_identity_preserve_trial_01.png`.
- ImageGen result SHA-256: `B4372C9BF01564507E1EE0770111FC3333A5D2BF417A2F8C01BBCE477B01E757`.
- Finish command: skill-local `advisor_icon_processing.py leader`, source kind `real`, explicit crop `(1, 0, 1081, 1454)`, canonical vanilla leader reference directory.
- Processed `156x210` candidate: `processed_png/portrait_WLS_independence_wave_national_council.png`.
- Processed candidate SHA-256: `3B184CE80E81246F2318F8A8221B958C78AFAD57E595B8BA5ADDA68DF44E63E0`.
- Full source/result sheet: `contact_sheets/WLS_saunders_lewis_full_source_result_comparison.png`.
- Processor/style sheet: `contact_sheets/WLS_saunders_lewis_processor_style_comparison.png`.
- Processor metadata: `metadata/WLS_saunders_lewis_processing.json`.

Independent review must decide whether the compact face, ears, hairline, deep-set asymmetric eyes, nose, narrow cheeks, mouth, expression, sourced age, and 1916 uniform remain recognizably Saunders Lewis at full and native size. Reject if the newspaper source is too weak, the large eyes become caricature, facial detail is invented, or the result reads as a generic young soldier.

## Runtime gate

Do not copy, convert, register, or wire this candidate before an independent PASS. IW-002 remains closed until this civic portrait and a rights-cleared sourced Welsh territorial/mountain commander portrait both pass independent review, exact runtime DDS files are pixel-verified, and a fresh full package audit passes. Robert Knox Ross remains `needs_user_review` pending exact institutional licence confirmation and is not bundled here.
