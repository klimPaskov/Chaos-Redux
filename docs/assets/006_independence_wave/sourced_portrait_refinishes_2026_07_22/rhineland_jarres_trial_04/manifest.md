# Karl Jarres source-locked portrait trial 04

Status: **candidate awaiting independent visual and provenance audit; not approved for runtime wiring**

This package retries the sourced real-male civic portrait for IW-008 Rhineland after three earlier ImageGen versions failed identity review. It contains no advisor, dossier, `_small`, female, fictional, flag, focus, decision, localisation, gameplay, interface, or runtime asset.

## Subject and role

- Event 006 package: IW-008, Rhineland (`RHI` carrier).
- Stable role: `RHI_independence_wave_provisional_directorate`, civic/constitutional/patron country leader.
- Subject: Karl Jarres (1874-1951), born in Remscheid, Rhine Province; mayor of Remscheid and Duisburg, Reich Interior Minister, and a living civic figure in 1936.
- Ownership gate: exact and variant scans in the accepted source package found no active vanilla or current Chaos Redux character owner. Independent audit must recheck this before approval.

## Archival sources

### Primary period attire source

- Attribution page: <https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_102-01175,_Karl_Jarres.jpg>
- Credit: `Bundesarchiv, Bild 102-01175 / CC-BY-SA 3.0`.
- Date: 1925; photographer recorded as unknown.
- Unchanged local master: `source_masters/RHI_karl_jarres_bundesarchiv_1925.jpg`, `562x800`.
- Master SHA-256: `72C952B0F1A1E3C08A16B20C123466B4BFC737D7C03AE63594CF7E6332C2C8D6`.
- Explicit identity/attire crop: `(145, 80, 430, 465)`.
- Crop: `source_crops/RHI_karl_jarres_hat_coat_reference.png`.
- Crop SHA-256: `EEE97623C3AD294A14A933B1AB6C896CADAAC2E225AB95A8CEB68C7F3BA9FB9B`.

### Facial identity cross-check

- Library of Congress record: <https://www.loc.gov/pictures/item/2014716741/>.
- Title: `Dr. Jarres`; Bain News Service collection. The accepted source package records the LOC no-known-restrictions route and an undated/approximately 1920 metadata context.
- Unchanged local master: `source_masters/RHI_karl_jarres_loc_undated.jpg`, `1024x734`.
- Master SHA-256: `D07EB103F4C5FDF13CA06C9D58FDEA2F626C14F82060D2B2D92B740DF633B36E`.
- Explicit face-and-shoulders crop: `(310, 35, 730, 565)`.
- Crop: `source_crops/RHI_karl_jarres_face_reference.png`.
- Crop SHA-256: `8B59E9B4975E0738411D2B35A860E6B07EF0A1FE72CA3ED86559D32FCF07CDCC`.

## Source-locked repaint

- Image 1: LOC facial identity crop.
- Image 2: Bundesarchiv hat/coat identity cross-check.
- Image 3 style-only reference: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/den_thorvald_stauning.png`.
- Prompt: `prompts/RHI_karl_jarres_identity_preserve_trial_04.txt`.
- Retained ImageGen result: `imagegen_results/RHI_karl_jarres_identity_preserve_trial_04.png`.
- ImageGen result SHA-256: `18C8A1F1D543A4817DC738750AE119D4DAC09F118F192695BF0EBAE88DB970D1`.
- Finish command: skill-local `advisor_icon_processing.py leader`, source kind `real`, explicit crop `(1, 0, 1081, 1454)`, canonical vanilla leader reference directory.
- Processed `156x210` candidate: `processed_png/portrait_RHI_independence_wave_provisional_directorate.png`.
- Processed candidate SHA-256: `AE34E21CF3B35AD034E222191313BD77E52EEAD12D26A6D2379B1FD064B9FA69`.
- Full source/result sheet: `contact_sheets/RHI_karl_jarres_full_source_result_comparison.png`.
- Processor/style sheet: `contact_sheets/RHI_karl_jarres_processor_style_comparison.png`.
- Processor metadata: `metadata/RHI_karl_jarres_processing.json`.

Trial 04 deliberately uses the clearer LOC view as the facial identity lock and the full-length Bundesarchiv view only for the same man's hat and coat. Earlier trials remain rejected. Independent review must decide whether the long/narrow face, hooded asymmetric eyes, long nose, lean jaw, guarded expression, age, and hat/coat survive recognizably at both full size and `156x210`. Reject on genericization or facial drift.

## Runtime gate

Do not copy, convert, register, or wire this candidate before an independent PASS. IW-008 remains closed until both Jarres and Josef Harpe pass independent source/visual review, the exact runtime DDS files are pixel-verified, protected Matthes remains hash-identical, and a fresh full package audit passes.
