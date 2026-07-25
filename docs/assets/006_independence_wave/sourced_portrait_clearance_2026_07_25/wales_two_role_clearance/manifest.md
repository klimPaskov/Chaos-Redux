# IW-002 Wales alternative sourced portrait clearance - 2026-07-25

Status: two materially different archival candidates are complete through source master and exact crop and remain `needs_user_review` before downstream portrait treatment. J. H. Thomas is the civic candidate and Major-General Robert Ross is the commander candidate. Lewis Valentine is retained as rejected active Kaiserreich ownership evidence, Thomas Wynford Rees is rejected for scene scale and Kaiserreich ownership, W. J. Gruffydd is blocked as postwar, and Lewis Pugh Evans is retained only as duplicate failed-source evidence.

This package stops at immutable source masters, decoded PNG masters and exact decoded-pixel crops. It contains no ImageGen result, processed `156x210` portrait, DDS, `.gfx` edit, localisation edit, gameplay edit, advisor asset, dossier asset, `_small` derivative or fallback.

## Requirement and runtime crosswalk

| Requirement | New candidate | Reserved consumer | Status | Downstream boundary |
| --- | --- | --- | --- | --- |
| WLS civic or national leader | James Henry J. H. Thomas | `GFX_portrait_WLS_independence_wave_national_council` -> `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_national_council.dds` | `needs_user_review` | Parent owns identity/localisation reconciliation, source-locked repaint, independent review and DDS conversion. |
| WLS military, territorial or mountain commander | Major-General Robert Knox Ross | `GFX_portrait_WLS_independence_wave_mountain_commandant` -> `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant.dds` | `needs_user_review` | Parent owns the alternate-history appointment decision, source-locked repaint, independent review and DDS conversion. |

## Candidate A - James Henry Thomas (J. H. Thomas) (civic)

- Identity: James Henry Thomas (1874-1949), Welsh-born Newport trade-union leader and Labour politician who served as Secretary of State for the Colonies from 1935 to 1936.
- Identity evidence: [J. H. Thomas biography](https://en.wikipedia.org/wiki/J._H._Thomas) and the [Commons source record](https://commons.wikimedia.org/wiki/File:James_Henry_Thomas_(1874-1949)_portrait.jpg).
- Source page: [James Henry Thomas (1874-1949) portrait.jpg](https://commons.wikimedia.org/wiki/File:James_Henry_Thomas_(1874-1949)_portrait.jpg).
- Direct unchanged source: `source_masters/j_h_thomas_bain_ggbain_29625_circa_1920.jpg`, `3674x4977` grayscale JPEG, SHA-256 `4f70ef8f6f2f970f5cd9216e15f65348dd92330be390389f2e2e717d0cec8cf5`.
- Lossless decoded master: `source_master_png/j_h_thomas_civic_master.png`, `3674x4977`, SHA-256 `14e085120d40257ce06f8f0abe4c8c9bbf4f20d0a1092636e3d9958d5e5581bc`.
- Exact identity crop: `source_crops/j_h_thomas_civic_crop.png`, rectangle `(left=350, top=200, right=3350, bottom=4200)`, `3000x4000`, SHA-256 `0b0b8e8ca7807939391a29c64a04f241c56e47e84ba649060f418fe71ef087be`.
- Crop proof: `source_crops/j_h_thomas_civic_crop.json` reports `decoded_pixels_equal: true` and matching RGBA SHA-256 `58acbfea5a056c43490682a10cca063828dfa0268a092092a346c307c67368f6` for the decoded master rectangle and output PNG.
- Source attribution: Commons records Bain as author and the Library of Congress George Grantham Bain Collection digital ID `ggbain.29625`; the source-page snapshot is `source_page_snapshots/j_h_thomas_commons_file_page.html`.
- Photograph date: Commons records circa 1920, before the 1936 scenario start date and within Thomas's adult public life.
- License: Commons `PD-Bain` and Library of Congress no-known-copyright-restrictions records; no attribution is required by the Commons record, but retain the LOC digital ID in provenance.
- Role fit: Thomas's Welsh birth, Newport connection, trade-union leadership and 1935-1936 Colonial Secretary service give the existing WLS national-council role a direct Welsh institutional and interwar political connection.
- Era fit: The source predates the 1936 start date. Any downstream treatment must age the face only while preserving source geometry and must not be described as a 1936 photograph.
- Visual notes: The high-resolution archival portrait has clear eyes, ears, brow, nose, moustache, mouth, jaw, bow tie and both shoulders. The exact crop removes source margins while retaining the full head-and-shoulders identity geometry; no hidden facial detail needs reconstruction.
- Ownership: The exact and variant terms `James Henry Thomas`, `J. H. Thomas`, `James_Henry_Thomas` and `JH Thomas` found no meaningful identity or portrait owner in current Chaos Redux, installed vanilla, Kaiserreich `1521695605`, or approved mods `2265420196` and `1458561226`.
- Comparison source: `source_masters/j_h_thomas_underwood_1924_rejected.jpg` is retained only as a comparison record. Its circular halftone/newspaper reproduction is softer and less crop-grade than the Bain photograph despite the closer date.

## Candidate B - Major-General Robert Knox Ross (commander)

- Identity: Major-General Robert Knox Ross CB DSO MC (1893-1951), commander of the 160th Infantry Brigade and the 53rd (Welsh) Infantry Division in the Second World War.
- Identity evidence: [Robert Ross biography](https://en.wikipedia.org/wiki/Robert_Ross_(British_Army_officer,_born_1893)) and Imperial War Museums object `205497134`.
- Source page: [Negative H24742.jpg](https://commons.wikimedia.org/wiki/File:Negative_H24742.jpg).
- Direct unchanged source: `source_masters/robert_ross_iwm_negative_h24742_1942.jpg`, `800x582` RGB JPEG, SHA-256 `1d05da1867e3b31e431f9a3d7e512d44eab1d5ea14d6c10c3ea00de109161621`.
- Lossless decoded master: `source_master_png/robert_ross_commander_master.png`, `800x582`, SHA-256 `941efc477dfe904ee93bd1f2950a1aa1757536b10ad717edd6108b84e78b4ae2`.
- Exact identity crop: `source_crops/robert_ross_commander_crop.png`, rectangle `(left=220, top=85, right=530, bottom=385)`, `310x300`, SHA-256 `de218e083de97c54fa0b250a22d2c62fe8810fab000c5b7dfca602bf5d10273e`.
- Crop proof: `source_crops/robert_ross_commander_crop.json` reports `decoded_pixels_equal: true` and matching RGBA SHA-256 `6db001ff152d9bd894b8d6e6d8d83ed0e08b954e0f4dae03f7b66245b69b1a87` for the decoded master rectangle and output PNG.
- Source attribution: Imperial War Museums object `205497134`, War Office Second World War Official Collection, dated 20 October 1942; the source-page snapshot is `source_page_snapshots/robert_ross_commons_file_page.html`.
- License: Commons `PD-UKGov` public-domain record for the IWM/War Office source. The Commons page does not name a separate photographer, so no personal author is inferred.
- Role fit: Ross is not Welsh-born, but he directly commanded the 160th Brigade and the 53rd (Welsh) Infantry Division. That documented Welsh-formation command supports the existing WLS territorial-commandant abstraction without claiming a historical Welsh mountain command.
- Era fit: The official source is directly within the WWII setting. Ross was alive and serving in the 53rd (Welsh) Division at the time; the uniform, rank details and facial geometry are period-valid for the requested grounded military role.
- Visual notes: The single-person official portrait has clear eyes, ears, nose, jaw, cap, tunic, medal bars and both shoulders. The unchanged master retains the IWM frame and watermark; the tight exact crop removes the frame, hands and waist while preserving head, neck and shoulder geometry.
- Ownership: The exact and variant terms `Robert Ross`, `Robert Knox Ross`, `Major-General Robert Ross`, `R. L. Ross` and `53rd Welsh Division` found no meaningful identity or portrait owner in current Chaos Redux, installed vanilla, Kaiserreich `1521695605`, or approved mods `2265420196` and `1458561226`.
- Uncertainty: The Commons record identifies the IWM object and War Office collection but does not name a photographer. Preserve IWM object `205497134` and the Commons PD-UKGov record rather than inferring a personal author. Ross was not Welsh-born, so the role fit rests on documented command of the 53rd (Welsh) Division and 160th Welsh Brigade.

## Rejected and blocked comparison leads

- Lewis Valentine is retained in the package as a complete source and crop, but Kaiserreich `1521695605` actively defines `WLS_lewis_valentine`, recruits him and owns civilian portrait/localisation consumers. It is `rejected_subject_owned` and must not be cloned without an explicit guarded transfer contract.
- Thomas Wynford Rees SE3459 was rejected because the 19 March 1945 source is a wide scene with a small face rather than a crop-grade portrait, and Kaiserreich `1521695605` owns `RAJ_thomas_wynford_rees` and its portrait/localisation consumers.
- W. J. Gruffydd remains as source evidence, but the attributed photograph is postwar (1946) and is `blocked_postwar_source` for a WWII-setting identity master unless the user explicitly reopens it.
- Lewis Pugh Evans HU 93411 remains for provenance traceability only. It is the same source already used by the two failed Evans repaint trials in `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/wls_lewis_pugh_evans_source_retry/` and is `rejected_duplicate_failed_source`.
- David Rhys Grenfell and George Cornwallis-West remain excluded because the parent reported repeated likeness failures on their earlier photographs, including enlarged or regularised eyes, broadened or frontalised faces and altered moustaches.
- Aneurin Bevan remains excluded because Kaiserreich `1521695605` actively owns `ENG_aneurin_bevan` and its portrait consumers.
- William Ambrose Bebb remains excluded because Kaiserreich `1521695605` owns `WLS_ambrose_bebb` and its portrait/localisation consumers.
- Saunders Lewis remains excluded because the only defensible prewar Commons photograph is the 1916 `Y Drych` image already rejected by the existing Saunders age gate, and Kaiserreich `1521695605` owns the same identity.

## Contact sheet

The comparison sheet is `contact_sheets/wales_two_role_clearance_contact_sheet_v5.png`, SHA-256 `d25308ecd1f20696b423f0770b436b4fdcef920d2c39d228912b12108dfb87f8`. It shows the J. H. Thomas and Robert Ross source masters beside their exact crops.

## Exact crop and downstream boundary

Both accepted review candidates were cropped with `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py` using Pillow as the only decode and crop backend. The crop JSON files are committed beside the PNGs and prove exact decoded-pixel equality. The parent may use either candidate only after accepting the era, provenance and ownership notes, then must use the exact crop as the sole identity input for source-locked identity-preserving ImageGen, compare the raw result and deterministic `156x210` portrait against canonical vanilla references, obtain an independent likeness/style/provenance audit, and convert to DDS only after PASS.
