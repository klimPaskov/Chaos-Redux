# Event 6 Saar (AJX) two-role grounded portrait source clearance

Date: 2026-07-24.

Scope owner: sourced visual asset research only.

Parent consumers: `AJX_friedrich_hoffmann` civic/municipal/neutral/constitutional and `AJX_karl_becker` genuine military/territorial command.

No runtime, gameplay, interface, localisation, advisor, dossier, `.gfx`, `_small`, ImageGen, or DDS changes were made.

## Decision summary

`AJX_friedrich_hoffmann` has a PASS source candidate: Walter Simons.

`AJX_karl_becker` has a rights/identity-safe archival candidate but remains HOLD / `needs_user_review`: Hans von Salmuth in a 1947–1948 NARA High Command Trial portrait.

The military HOLD is intentional because the only defensible rights-clear likeness located is postwar courtroom clothing rather than a 1936 military-uniform portrait.

Do not silently alter clothing, erase the courtroom context, or claim the image is a 1936 portrait.

## PASS civic candidate: Walter Simons

Walter Simons (1861–1937) was born in Elberfeld in the Prussian Rhine Province and was an independent constitutional civic figure.

His documented roles include Foreign Minister of the Weimar Republic in 1920–1921, president of the Reichsgericht in 1922–1929, and acting head of state in 1925, leaving him alive and period-defensible in the 1936 setting.

Identity and role evidence: [Walter Simons](https://en.wikipedia.org/wiki/Walter_Simons).

Archive/object: [Bundesarchiv Bild 102-12279, Walter Simons](https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_102-12279,_Walter_Simons.jpg).

Direct original: `https://upload.wikimedia.org/wikipedia/commons/d/de/Bundesarchiv_Bild_102-12279%2C_Walter_Simons.jpg`.

Archive date: September 1931.

Rights/publication basis: German Federal Archive / Wikimedia Commons cooperation, CC BY-SA 3.0 DE.

Required attribution: `Bundesarchiv, Bild 102-12279 / CC-BY-SA 3.0`.

Unchanged master: `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_24/ajx_two_role/source_masters/AJX_walter_simons_bundesarchiv_1931.jpg`.

Master evidence: 558×800 RGB, 29,319 bytes, SHA-256 `789961BC6505993F4A6441979CA4D1F247609531D23CFB8D7088CCC2D4A170B3`.

Exact crop: `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_24/ajx_two_role/source_crops/AJX_friedrich_hoffmann_walter_simons_1931_head_shoulders.png`.

Crop rectangle: half-open decoded pixels `(55, 45, 520, 650)`; output 465×605 RGB, no resize or retouch.

Crop evidence: SHA-256 `2B1C394DA30F31F0E81B35CD6740CC0E0235A71326FDC976CCE9F0217688EFD7`; metadata `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_24/ajx_two_role/metadata/AJX_friedrich_hoffmann_walter_simons_1931_head_shoulders.json`; `decoded_pixels_equal: true`; master/output RGBA digest `9bebecbd0362fa5dc39ec8b1ce4271671c32ced58db3a7b8eec078410161bdc7`.

Suggested parent sprite name after normal conversion: `GFX_portrait_AJX_friedrich_hoffmann_civic_large`.

## HOLD military candidate: Hans von Salmuth

Hans Eberhard Kurt von Salmuth (1888–1962) was born in Metz and was a genuine German Army officer.

His documented 1934–1937 role as chief of staff of II Corps and later command of XXX Corps and multiple armies satisfy the military/territorial command identity gate, with no police, SS, or security-administration mismatch.

Identity and role evidence: [Hans von Salmuth](https://en.wikipedia.org/wiki/Hans_von_Salmuth).

Archive/object: [NARA Catalog 167824751](https://catalog.archives.gov/id/167824751) and [Commons High Command Trial portrait](https://commons.wikimedia.org/wiki/File:Hans_von_Salmuth,_defendant_in_High_Command_Trial.jpg).

Direct original: `https://upload.wikimedia.org/wikipedia/commons/1/11/Hans_von_Salmuth%2C_defendant_in_High_Command_Trial.jpg`.

Archive date: between 1947 and 1948.

Archive credit: Office of Military Government for Germany, United States.

Rights/publication basis: United States federal-government work, public domain under 17 U.S.C. §105; Commons carries PD US Government and Public Domain Mark metadata.

Unchanged master: `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_24/ajx_two_role/source_masters/AJX_hans_von_salmuth_nara_high_command_trial_1947_48.jpg`.

Master evidence: 2248×2953 RGB, 3,938,157 bytes, SHA-256 `62690D60390673D6D9312C6123513D7F886B0BF2115C0A22228BC2E9C59CA816`.

Exact crop: `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_24/ajx_two_role/source_crops/AJX_karl_becker_hans_von_salmuth_nara_1947_48_head_shoulders.png`.

Crop rectangle: half-open decoded pixels `(340, 190, 1910, 2340)`; output 1570×2150 RGB, no resize, retouch, recolour, or clothing alteration.

Crop evidence: SHA-256 `B2E3B1E498C8B85837F77006D523BF6922D743CF024F4DC9138572FEB56D8236`; metadata `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_24/ajx_two_role/metadata/AJX_karl_becker_hans_von_salmuth_nara_1947_48_head_shoulders.json`; `decoded_pixels_equal: true`; master/output RGBA digest `0cbc1ea42c2673a02f1aa0cd02cf2a4db0de4945ec637f93742d12294548f20e`.

Suggested sprite name only if the parent explicitly resolves HOLD: `GFX_portrait_AJX_karl_becker_commander_large`.

## Rejected and ownership findings

Karl Jarres was rejected because approved Kaiserreich `1521695605` owns `GER_karl_jarres`, its portrait, recruit, and localisation in `common/characters/GER characters.txt:85-101`, `history/countries/GER - Germany.txt:286`, `interface/kaiserreich/portraits/GER_portraits.gfx:15-16`, and `localisation/english/KR_country_specific/GER - Germany l_english.yml:38-39`.

The current Chaos Redux, vanilla, and approved-mod ownership scan found no live character, portrait, recruit, or localisation ownership for Walter Simons or Hans von Salmuth.

The exact and variant name terms scanned were `Walter Simons`, `Walter_Simons`, `AJX_walter_simons`, `Hans von Salmuth`, `Hans_von_Salmuth`, `Hans Eberhard Kurt von Salmuth`, `Hans_Eberhard_Kurt_von_Salmuth`, and `AJX_hans_von_salmuth` across current `common/characters`, `history/countries`, `interface`, `gfx/leaders`, `gfx/portraits`, and `localisation`, vanilla, and approved mod roots `1521695605`, `2265420196`, and `1458561226`.

The 1943 Commons image [Hans von Salmuth.jpg](https://commons.wikimedia.org/wiki/File:Hans_von_Salmuth.jpg) is preserved as `source_masters/Hans_von_Salmuth.jpg` with SHA-256 `1BBA8A6AD8E01CB621FEDDC3889382F0F5049803843AF35FAD517C2C8E695BA9`, but is research-only because its author is unknown and its Britannica / Georg Friedrich Lorenz collection provenance is not archive-grade for this gate.

Ernst Busch remains rejected because its clear portrait has secondary-source/unknown-author attribution, while the Bundesarchiv alternative is only 173×260.

Friedrich Herrlein remains rejected because the available 1925 image is a damaged group photograph and cannot be cropped into a single-person identity-safe portrait.

## Files delivered

The source package is `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_24/ajx_two_role/`.

The package manifest is `manifest.md` and `manifest.json`.

The source-only GFX note is `gfx_handoff.md`.

The comparison sheet is `research/ajx_two_role_source_candidates_contact_sheet.png`.

The package includes unchanged archival masters, lossless exact crops, and JSON decoded-pixel equality proofs for both roles.

## Parent action

The parent may proceed with Walter Simons after normal licence attribution review.

The parent must explicitly accept or reject Hans von Salmuth for the 1936 setting before any commander runtime wiring or DDS conversion.

If the parent rejects the Salmuth HOLD, the `AJX_karl_becker` role remains blocked pending a new rights-clear, period-fit military source.
