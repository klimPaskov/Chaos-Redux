# Event 6 Wallonia alternative sourced-portrait clearance

This package is a source-only clearance tranche for the Event 6 Wallonia AFX commander alternative. It contains unchanged archival masters, exact-pixel PNG crops, crop-equality JSON evidence, source snapshots, a comparison contact sheet, and ownership findings. Jules Destrée remains the independently approved and runtime-wired AFX civic leader; this package does not replace him. No ImageGen output, DDS conversion, GFX edit, localisation edit, character edit, or runtime wiring is included.

## Selected new source: Fernand Jacquet

- Status: `needs_user_review` at source-clearance stage because the archive record names an unknown photographer and the public-domain statement is a Commons template rather than an archive-issued licence certificate.
- Selected role: AFX commander alternative only.
- Identity and 1936 fit: Fernand Maximillian Leon Jacquet (2 November 1888, Petite-Chapelle - 12 October 1947, Beaumont) was a Belgian captain-commandant and First World War flying ace. Petite-Chapelle is in Wallonia, and he was alive in 1936.
- Identity evidence: [Fernand Jacquet biography](https://en.wikipedia.org/wiki/Fernand_Jacquet).
- Archival source page: [Commons file: Fernand Jacquet vers 1915](https://commons.wikimedia.org/wiki/File:Fernand_Jacquet_vers_1915.jpg).
- Underlying archive source: [Heuvel/Memorix IIIF image](https://images.memorix.nl/heu/iiif/139408cf-33f3-40a1-263f-b94d9468700a/full/full/0/default.jpg).
- Archive metadata: circa 1915, unknown photographer, source identifier `139408cf-33f3-40a1-263f-b94d9468700a`, with a period Belgian military uniform and aircraft context.
- Rights record: Commons marks the file Public domain for the European Union and United States, but the source record does not name the photographer. Treat the rights as usable for review, not as a substitute for final legal sign-off.
- Unchanged master: `source_masters/fernand_jacquet_1915_memorix_heu_139408cf.jpg` with dimensions 4579x3521 and SHA-256 `1c9ab5216e175fc7c47d4571810ba97f599f53dc510a6bd3330366aac036fcf6`.
- Selected exact tight head-and-shoulders crop: `source_crops/fernand_jacquet_1915_head_shoulders_tight_crop.png` using half-open decoded-pixel rectangle `(1500, 500, 3600, 2600)`, dimensions 2100x2100, and SHA-256 `9bf20613f007bb6291d456caa88f67f4ec3651c7604adefdcd437ac5adead33d`.
- Crop proof: `source_crops/fernand_jacquet_1915_head_shoulders_tight_crop.json` records `decoded_pixels_equal: true` and matching RGBA crop/output digest `ad643ebc4f30c9ea4349671ac2e0725c56f9899ae353cbafb863aff58c9f92e6`.
- Visual fit: The tight unchanged frame contains complete hair and head, eyes and eyelids, nose, jaw, moustache, both ears, neck, both shoulders, and only the upper chest of the period uniform. The aircraft remains contextual background and no identity pixels were reconstructed.
- Superseded evidence: The earlier `source_crops/fernand_jacquet_1915_head_shoulders_crop.png` crop at `(1750, 600, 3550, 3050)` remains committed for provenance, but its torso/waist framing is superseded by the tight crop and is not the selected handoff asset. Its SHA-256 is `7c64d4bd8f4390abd3da328b88357a6aaf7e9c215093b2119e386f5448c0b46a`.
- Exact-owner audit: No exact Fernand Jacquet or Jacquet character/portrait owner was found in Chaos Redux, vanilla HOI4, Kaiserreich `1521695605`, reference `2265420196`, or reference `1458561226` in the audited character, country-history, leader-GFX, interface, and English-localisation paths.

## Alternate research only: Charles de Broqueville

- Status: `alternate_research`; not selected, not recommended as the civic portrait, and not wired. Jules Destrée remains the approved AFX civic owner.
- Possible future role if separately requested: Belgian civic backup research only. No active sprite suggestion is made by this package.
- Identity and 1936 fit: Charles Marie Pierre Albert de Broqueville (4 December 1860, Postel - 5 September 1940, Brussels) was a Belgian Catholic politician and Prime Minister in 1932-1934. He was alive in 1936 and is a defensible French-speaking Belgian civic identity, although he was not born in Wallonia proper.
- Identity evidence: [Charles de Broqueville biography](https://en.wikipedia.org/wiki/Charles_de_Broqueville).
- Archival source page: [Commons file: Comte de Broqueville](https://commons.wikimedia.org/wiki/File:Comte_de_Broqueville.jpg).
- Primary archive record: [Library of Congress item 2016821826](https://www.loc.gov/pictures/item/2016821826/) and [catalogue record](https://lccn.loc.gov/2016821826).
- Underlying archive master: [LOC National Photo Company TIFF](https://cdn.loc.gov/master/pnp/npcc/20200/20275u.tif). The selected master is the border-free unchanged Commons JPEG mirror of the same LOC item.
- Archive metadata: Henri Manuel (1874-1947), National Photo Company Collection, dated between 1909 and 1920. The LOC record states that the item has no known restrictions on publication; Commons marks the file Public domain.
- Unchanged master: `source_masters/charles_de_broqueville_1909_1920_commons.jpg` with dimensions 3258x4451 and SHA-256 `f64289e92afaf0a9e2581b4d6aacf669b2f0c37fb78922345f9273c64f71057c`.
- Exact head-and-shoulders crop retained for comparison: `source_crops/charles_de_broqueville_commons_head_shoulders_crop.png` using half-open decoded-pixel rectangle `(150, 200, 3150, 4400)`, dimensions 3000x4200, and SHA-256 `beb0d257ec1a09a9750032a441638adf540d57cc6ba15ea1e464e105c39c76c3`.
- Crop proof: `source_crops/charles_de_broqueville_commons_head_shoulders_crop.json` records `decoded_pixels_equal: true` and matching RGBA crop/output digest `3ecb926db6fdcf90e6d0093ad8cc37f9116f236efcb9398fe062f1d8234434cd`.
- Visual fit and uncertainty: The unchanged frame shows the complete hairline, eyes and eyelids, nose, jaw, prominent moustache, right ear and ear-side contour, neck, both shoulders, and period suit. The frontal pose partly occludes the left ear, and the subject is not Wallonia-born. These are reasons to retain it only as alternate research.
- Exact-owner audit: No exact Charles de Broqueville or de Broqueville character/portrait owner was found in Chaos Redux, vanilla HOI4, Kaiserreich `1521695605`, reference `2265420196`, or reference `1458561226` in the audited character, country-history, leader-GFX, interface, and English-localisation paths.

## Current approved civic owner

- Jules Destrée is the current approved and runtime-wired Chaos Redux AFX Walloon civic leader in `common/characters/006_independence_wave_wallonia_frisia_characters.txt:25-30`, `history/countries/AFX - Wallonia.txt:17`, and `interface/006_independence_wave_region_01_portraits.gfx`.
- This source package does not replace, duplicate, or rewire Destrée. The rejected Destrée research images remain under `research/rejected/` only as provenance evidence.

## Blocked and rejected comparison candidates

- Albert Devèze is source-quality and alive in 1936, but vanilla owns `BEL_albert_deveze` in `common/characters/BEL.txt` at lines 1318, 1334, 1355, 1362, 1377, and 1395, recruits it in `history/countries/BEL - Belgium.txt:344`, and localises it at `localisation/english/WUW_characters_l_english.yml:246`. He is blocked from additive transfer and is retained only as comparison evidence.
- Gérard Leman has excellent public-domain imagery, but he died in 1920 and cannot represent a living 1936 commander. His masters are retained under `research/rejected/` as rejected research evidence.
- Henri Denis is blocked by an exact Kaiserreich owner as recorded in the parent audit and was not transferred.
- Fernand Jacquet's restored 1914 group image was not used. The selected master is the unchanged circa-1915 Memorix frame only.

## Package status

Fernand Jacquet is the only selected new source and is the commander candidate pending the unknown-photographer rights review. Jules Destrée remains the approved civic owner. Charles de Broqueville is alternate research only and is not a recommended civic replacement or runtime source. Albert Devèze remains blocked by the vanilla owner. Parent-owned follow-up is final legal and identity acceptance, creation of the repository-standard DDS if Jacquet is accepted, `.gfx` registration, and commander wiring; no civic replacement is requested by this package.
