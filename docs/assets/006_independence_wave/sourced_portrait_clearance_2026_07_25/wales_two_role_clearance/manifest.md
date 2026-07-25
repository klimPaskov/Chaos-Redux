# IW-002 Wales alternative sourced portrait clearance - 2026-07-25

Status: J. H. Thomas is source-ready through immutable source master and exact crop. The IWM HU 126780 image is retained only as blocked namesake evidence because it depicts Second Lieutenant Gervase Thorpe Spendlove, who died in 1914, rather than the requested Major-General Gervase Thorpe (1877-1962). Robert Ross is retained as blocked research evidence because his exact crop leaves insufficient facial resolution. Lewis Valentine is retained as rejected active Kaiserreich ownership evidence, Thomas Wynford Rees is rejected for scene scale and Kaiserreich ownership, W. J. Gruffydd is blocked as postwar, and Lewis Pugh Evans is retained only as duplicate failed-source evidence.

This package stops at immutable source masters, decoded PNG masters and exact decoded-pixel crops. It contains no ImageGen result, processed `156x210` portrait, DDS, `.gfx` edit, localisation edit, gameplay edit, advisor asset, dossier asset, `_small` derivative or fallback.

## Requirement and runtime crosswalk

| Requirement | New candidate | Reserved consumer | Status | Downstream boundary |
| --- | --- | --- | --- | --- |
| WLS civic or national leader | James Henry J. H. Thomas | `GFX_portrait_WLS_independence_wave_national_council` -> `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_national_council.dds` | `source_ready_for_parent_pipeline` | Parent owns identity/localisation reconciliation, source-locked repaint, independent review and DDS conversion. Preserve the circa-1920 source-visible age exactly. |
| WLS military, territorial or mountain commander | Requested Major-General Gervase Thorpe; IWM HU 126780 is a different Second Lieutenant Gervase Thorpe Spendlove | `GFX_portrait_WLS_independence_wave_mountain_commandant` -> `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant.dds` | `blocked_identity_mismatch` | Do not pass HU 126780 to ImageGen, processing, DDS conversion or runtime wiring. The source remains provenance evidence only; a correctly identified Major-General Gervase Thorpe photograph is required. |

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
- Era fit: The source predates the 1936 start date. Preserve the source-visible age and identity exactly; downstream treatment must not invent age progression or describe the image as a 1936 photograph.
- Visual notes: The high-resolution archival portrait has clear eyes, ears, brow, nose, moustache, mouth, jaw, bow tie and both shoulders. The exact crop removes source margins while retaining the full head-and-shoulders identity geometry; no hidden facial detail needs reconstruction.
- Ownership: The exact and variant terms `James Henry Thomas`, `J. H. Thomas`, `James_Henry_Thomas` and `JH Thomas` found no meaningful identity or portrait owner in current Chaos Redux, installed vanilla, Kaiserreich `1521695605`, or approved mods `2265420196` and `1458561226`.
- Comparison source: `source_masters/j_h_thomas_underwood_1924_rejected.jpg` is retained only as a comparison record. Its circular halftone/newspaper reproduction is softer and less crop-grade than the Bain photograph despite the closer date.

## Candidate B - IWM HU 126780 namesake (commander source blocked)

- Requested identity: Major-General Gervase Thorpe (1877-1962), GOC of the 53rd (Welsh) Infantry Division from 1935 to 1939 and alive in 1936.
- IWM source identity: Second Lieutenant Gervase Thorpe Spendlove, 2nd Battalion The Prince of Wales' Volunteers (South Lancashire Regiment), killed 17 November 1914.
- Identity evidence: [Gervase Thorpe biography](https://en.wikipedia.org/wiki/Gervase_Thorpe) and the [IWM object 205388980](https://www.iwm.org.uk/collections/item/object/205388980), whose page title and object description identify the distinct 1914 namesake.
- Source page: [IWM HU 126780 object record](https://www.iwm.org.uk/collections/item/object/205388980).
- Direct unchanged source: `source_masters/gervase_thorpe_spendlove_iwm_hu126780.jpg`, `612x800` RGB JPEG, SHA-256 `7cdb3a70f983105f579c5f141cecc631c665eae16cdb71e2ee7266b924d7041d`.
- Lossless decoded master: `source_master_png/gervase_thorpe_commander_master.png`, `612x800`, SHA-256 `cb76ddba4dba74304db6a1fd16933bc6d712c85de6b16f287f6feae572487bbe`.
- Exact identity crop: `source_crops/gervase_thorpe_commander_crop.png`, rectangle `(left=10, top=80, right=602, bottom=720)`, `592x640`, SHA-256 `016c1d5977507b01ba96e2326152ddd0f8517f813f7a85e70348b13867919f01`.
- Crop proof: `source_crops/gervase_thorpe_commander_crop.json` reports `decoded_pixels_equal: true` and matching RGBA SHA-256 `3f4666b6918993d3d2b2634cd24c9f6a3cad575f5f18301c7ec1134c45370fbf` for the decoded master rectangle and output PNG.
- Source attribution: Imperial War Museums Bond of Sacrifice - First World War Portraits Collection, object `205388980`, collection `HU 126780`; the metadata snapshot is `source_page_snapshots/gervase_thorpe_iwm_hu126780_page.md`. Required attribution for permitted use is `Image: IWM (HU 126780)`.
- Photograph date: IWM does not state an exact date and classifies the source as First World War production/content. The object record records the namesake's death on 17 November 1914. Do not describe the source as a 1936 photograph or as the requested major-general.
- License: IWM Non-Commercial licence, https://www.iwm.org.uk/corporate/policies/non-commercial-licence. The licence permits low-resolution downloads/embeds for listed non-commercial uses and requires the stated attribution; commercial use, high-resolution copies or other uses require a separate IWM licence. No public-domain claim is made.
- Role fit: The crop is a clear adult male head-and-shoulders image, but the subject is the wrong person. It is not usable for a 1936 WLS mountain commandant identity master. The previous Welsh-formation role statement was a conflation of two distinct people and is withdrawn.
- Era fit: The source subject died in 1914, so the source cannot support a commander alive in 1936. Preserve the source-visible age and identity exactly and do not invent an age progression or identity substitution.
- Identity disposition: `blocked_identity_mismatch`. Retain master, decoded PNG, exact crop and crop JSON for provenance evidence only; do not send them downstream.
- Visual notes: The single-person archival portrait has clear eyes, ears, brow, nose, mouth, jaw, hairline, cap, collar and both shoulder tops. The exact crop removes the lower-right IWM watermark while retaining head-and-shoulders geometry; the source halftone pattern is inherent and must be disclosed.
- Ownership: The exact and variant terms `Gervase Thorpe`, `Gervase Thorpe Spendlove`, `Major-General Gervase Thorpe`, `Thorpe Spendlove`, `Gervase_Thorpe`, `gervase_thorpe` and `Spendlove` found no meaningful identity or portrait owner in current Chaos Redux, installed vanilla, Kaiserreich `1521695605`, or approved mods `2265420196` and `1458561226`.

## Blocked research evidence - Major-General Robert Knox Ross (commander)

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
- Blocked reason: The exact crop is only `310x300` and leaves roughly `60-80 px` of usable facial geometry. Retain the master and crop for provenance evidence only; do not send this source downstream.
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
- Field Marshal Sir Archibald Montgomery-Massingberd was not admitted despite a clear 14 December 1927 Bassano/National Portrait Gallery portrait and a documented 53rd (Welsh) Division command connection. The Commons page combines a public-domain tag with an NPG copyright claim and unauthorised-reproduction notice, so the source is rights-uncertain.

## Contact sheet

The comparison sheet is `contact_sheets/wales_two_role_clearance_contact_sheet_v7.png` and labels the IWM HU 126780 namesake as blocked for identity mismatch. It shows the J. H. Thomas source-ready master beside its exact crop, the blocked HU 126780 namesake master beside its exact crop, and the blocked Ross master/crop. Its SHA-256 is `7f8ff4ef015e234324a4bd22a44d140f8d6621567793159d3e3ae3e22870273a`.

The older `contact_sheets/wales_two_role_clearance_contact_sheet_v6.png` is retained only as superseded evidence because it labelled the namesake as source-ready before the identity mismatch was resolved. Use v7 for all review and wiring decisions.

## Exact crop and downstream boundary

The source-ready Thomas crop and the blocked IWM HU 126780 namesake crop were made with `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py` using Pillow as the only decode and crop backend. The crop JSON files are committed beside the PNGs and prove exact decoded-pixel equality. Only the Thomas candidate may proceed to the parent-owned identity-preserving pipeline; HU 126780 is blocked and must not be used to depict Major-General Gervase Thorpe. Ross is blocked and must not enter the pipeline.
