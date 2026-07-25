# Event 6 Wallonia alternative sourced-portrait clearance

This package is a source-only clearance tranche for Event 6 Wallonia AFX civic and commander roles. It contains unchanged archival masters, exact-pixel PNG crops, crop-equality JSON evidence, source snapshots, a comparison contact sheet, and ownership findings. No ImageGen output, DDS conversion, GFX edit, localisation edit, character edit, or runtime wiring is included.

## Candidate 1: Fernand Jacquet

- Status: `needs_user_review` at source-clearance stage because the archive record names an unknown photographer and the public-domain statement is a Commons template rather than an archive-issued licence certificate.
- Proposed role: AFX commander.
- Identity and 1936 fit: Fernand Maximillian Leon Jacquet (2 November 1888, Petite-Chapelle – 12 October 1947, Beaumont) was a Belgian captain-commandant and First World War flying ace. Petite-Chapelle is in Wallonia, and he was alive in 1936.
- Identity evidence: [Fernand Jacquet biography](https://en.wikipedia.org/wiki/Fernand_Jacquet).
- Archival source page: [Commons file: Fernand Jacquet vers 1915](https://commons.wikimedia.org/wiki/File:Fernand_Jacquet_vers_1915.jpg).
- Underlying archive source: [Heuvel/Memorix IIIF image](https://images.memorix.nl/heu/iiif/139408cf-33f3-40a1-263f-b94d9468700a/full/full/0/default.jpg).
- Archive metadata: circa 1915, unknown photographer, source identifier `139408cf-33f3-40a1-263f-b94d9468700a`, with a period Belgian military uniform and aircraft context.
- Rights record: Commons marks the file Public domain for the European Union and United States, but the source record does not name the photographer. Treat the rights as usable for review, not as a substitute for a final legal sign-off.
- Unchanged master: `source_masters/fernand_jacquet_1915_memorix_heu_139408cf.jpg` with dimensions 4579x3521 and SHA-256 `1c9ab5216e175fc7c47d4571810ba97f599f53dc510a6bd3330366aac036fcf6`.
- Exact head-and-shoulders crop: `source_crops/fernand_jacquet_1915_head_shoulders_crop.png` using half-open decoded-pixel rectangle `(1750, 600, 3550, 3050)`, dimensions 1800x2450, and SHA-256 `7c64d4bd8f4390abd3da328b88357a6aaf7e9c215093b2119e386f5448c0b46a`.
- Crop proof: `source_crops/fernand_jacquet_1915_head_shoulders_crop.json` records `decoded_pixels_equal: true` and matching RGBA crop/output digest `baca6367035db1703f69c6a9b14010545be09854660ff0b3f3469f7a893c0cb8`.
- Visual fit: The unchanged frame shows the complete hairline, eyes and eyelids, nose, jaw, moustache, both ears, neck, both shoulders, and period captain-commandant uniform at usable resolution. The aircraft remains contextual background and no identity pixels were reconstructed.
- Exact-owner audit: No exact Fernand Jacquet or Jacquet character/portrait owner was found in Chaos Redux, vanilla HOI4, Kaiserreich `1521695605`, reference `2265420196`, or reference `1458561226` in the audited character, country-history, leader-GFX, interface, and English-localisation paths.

## Candidate 2: Charles de Broqueville

- Status: `sourced` for source clearance, with ordinary final legal review still advisable before public redistribution.
- Proposed role: AFX civic leader or assembly/advisor portrait.
- Identity and 1936 fit: Charles Marie Pierre Albert de Broqueville (4 December 1860, Postel – 5 September 1940, Brussels) was a Belgian Catholic politician and Prime Minister in 1932–1934. He was alive in 1936 and is a defensible French-speaking Belgian civic identity, although he was not born in Wallonia proper.
- Identity evidence: [Charles de Broqueville biography](https://en.wikipedia.org/wiki/Charles_de_Broqueville).
- Archival source page: [Commons file: Comte de Broqueville](https://commons.wikimedia.org/wiki/File:Comte_de_Broqueville.jpg).
- Primary archive record: [Library of Congress item 2016821826](https://www.loc.gov/pictures/item/2016821826/) and [catalogue record](https://lccn.loc.gov/2016821826).
- Underlying archive master: [LOC National Photo Company TIFF](https://cdn.loc.gov/master/pnp/npcc/20200/20275u.tif). The selected master is the border-free unchanged Commons JPEG mirror of the same LOC item.
- Archive metadata: Henri Manuel (1874–1947), National Photo Company Collection, dated between 1909 and 1920. The LOC record states that the item has no known restrictions on publication; Commons marks the file Public domain.
- Unchanged selected master: `source_masters/charles_de_broqueville_1909_1920_commons.jpg` with dimensions 3258x4451 and SHA-256 `f64289e92afaf0a9e2581b4d6aacf669b2f0c37fb78922345f9273c64f71057c`.
- Exact head-and-shoulders crop: `source_crops/charles_de_broqueville_commons_head_shoulders_crop.png` using half-open decoded-pixel rectangle `(150, 200, 3150, 4400)`, dimensions 3000x4200, and SHA-256 `beb0d257ec1a09a9750032a441638adf540d57cc6ba15ea1e464e105c39c76c3`.
- Crop proof: `source_crops/charles_de_broqueville_commons_head_shoulders_crop.json` records `decoded_pixels_equal: true` and matching RGBA crop/output digest `3ecb926db6fdcf90e6d0093ad8cc37f9116f236efcb9398fe062f1d8234434cd`.
- Visual fit: The unchanged frame shows the complete hairline, eyes and eyelids, nose, jaw, prominent moustache, right ear and ear-side contour, neck, both shoulders, and period suit. The frontal pose leaves the left ear partly occluded by the hairline; this is the only visual caveat for a strict two-ear portrait gate.
- Exact-owner audit: No exact Charles de Broqueville or de Broqueville character/portrait owner was found in Chaos Redux, vanilla HOI4, Kaiserreich `1521695605`, reference `2265420196`, or reference `1458561226` in the audited character, country-history, leader-GFX, interface, and English-localisation paths.

## Blocked and rejected comparison candidates

- Albert Devèze is source-quality and alive in 1936, but vanilla owns `BEL_albert_deveze` in `common/characters/BEL.txt` at lines 1318, 1334, 1355, 1362, 1377, and 1395, recruits it in `history/countries/BEL - Belgium.txt:344`, and localises it at `localisation/english/WUW_characters_l_english.yml:246`. He is blocked from additive transfer and is retained only as comparison evidence.
- Jules Destrée is already the current Chaos Redux AFX civic owner in `common/characters/006_independence_wave_wallonia_frisia_characters.txt:25-30`, `history/countries/AFX - Wallonia.txt:17`, and `interface/006_independence_wave_region_01_portraits.gfx`. His sourced images are retained under `research/rejected/` and are not an additive alternative.
- Gérard Leman has excellent public-domain imagery, but he died in 1920 and cannot represent a living 1936 commander. His masters are retained under `research/rejected/` as rejected research evidence.
- Henri Denis is blocked by an exact Kaiserreich owner as recorded in the parent audit and was not transferred.
- Fernand Jacquet's restored 1914 group image was not used. The selected master is the unchanged circa-1915 Memorix frame only.

## Package status

The recommended clear pair is Jacquet for commander and de Broqueville for civic. Jacquet remains `needs_user_review` only for the unknown-photographer rights uncertainty. De Broqueville is source-cleared with LOC no-known-restrictions evidence. Parent-owned follow-up is final legal acceptance, creation of the repository-standard DDS if accepted, `.gfx` registration, and runtime wiring.
