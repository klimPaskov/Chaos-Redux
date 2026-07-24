# AJX two-role sourced portrait clearance

This package covers only the two grounded stable consumers requested for Event 6 Saar (AJX): `AJX_friedrich_hoffmann` as civic/municipal/constitutional and `AJX_karl_becker` as military/territorial command.

No ImageGen output, DDS conversion, runtime wiring, `.gfx` edit, localisation edit, advisor edit, dossier edit, or `_small` portrait edit is included.

## Gate summary

| Consumer | Grounded identity | Gate | Runtime disposition |
| --- | --- | --- | --- |
| `AJX_friedrich_hoffmann` | Walter Simons (1861–1937) | PASS | Source-ready after parent wiring and final licence attribution review |
| `AJX_karl_becker` | Hans Eberhard Kurt von Salmuth (1888–1962) | HOLD / `needs_user_review` | Do not wire until the parent explicitly accepts a 1947–48 postwar courtroom likeness for the 1936 setting |

## PASS: `AJX_friedrich_hoffmann` → Walter Simons

Walter Simons was born in Elberfeld in the Prussian Rhine Province, remained an independent politician, served as Foreign Minister of the Weimar Republic in 1920–1921, served as president of the Reichsgericht from 1922–1929, briefly acted as head of state in 1925, and was alive in the 1936 scenario year.

This is a civic, legal, and constitutional match for the stable consumer, with no police, SS, or security-administration implication.

The identity and biographical evidence is [Walter Simons](https://en.wikipedia.org/wiki/Walter_Simons).

The archival source is [Bundesarchiv Bild 102-12279, Walter Simons](https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_102-12279,_Walter_Simons.jpg).

The direct original download used for the unchanged master is `https://upload.wikimedia.org/wikipedia/commons/d/de/Bundesarchiv_Bild_102-12279%2C_Walter_Simons.jpg`.

The archive metadata dates the photograph to September 1931 and describes it as a portrait of Reichsgerichtspräsident Dr. Simons.

The source is supplied through the German Federal Archive / Wikimedia Commons cooperation and is marked CC BY-SA 3.0 DE with the required attribution `Bundesarchiv, Bild 102-12279 / CC-BY-SA 3.0`.

The licence deed is [Creative Commons Attribution-ShareAlike 3.0 Germany](https://creativecommons.org/licenses/by-sa/3.0/de/deed.en).

The unchanged archival master is `source_masters/AJX_walter_simons_bundesarchiv_1931.jpg` with decoded dimensions 558×800, RGB mode, 29,319 bytes, and SHA-256 `789961BC6505993F4A6441979CA4D1F247609531D23CFB8D7088CCC2D4A170B3`.

The explicit head-and-shoulders crop is `source_crops/AJX_friedrich_hoffmann_walter_simons_1931_head_shoulders.png`.

The crop rectangle in decoded master pixels is half-open `(left=55, top=45, right=520, bottom=650)`, producing 465×605 pixels without resizing, retouching, recolouring, or clothing alteration.

The crop has SHA-256 `2B1C394DA30F31F0E81B35CD6740CC0E0235A71326FDC976CCE9F0217688EFD7`.

The exact decoded-pixel equality proof is `metadata/AJX_friedrich_hoffmann_walter_simons_1931_head_shoulders.json`, whose `decoded_pixels_equal` field is `true` and whose master/output RGBA digest is `9bebecbd0362fa5dc39ec8b1ce4271671c32ced58db3a7b8eec078410161bdc7`.

The source-crop command and tool digest are recorded by the JSON evidence: `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py`, tool SHA-256 `14fa178d6df999346874a7033e84f9b3ae988e7d845f3a4b2f8a44755e30641c`.

Suggested stable large sprite name for parent wiring is `GFX_portrait_AJX_friedrich_hoffmann_civic_large`.

The source crop is deliberately not converted to DDS in this subtask.

## HOLD: `AJX_karl_becker` → Hans von Salmuth

Hans Eberhard Kurt von Salmuth was born in Metz in 1888, was a German Army officer rather than a police or SS official, served as chief of staff of II Corps from 1934–1937, commanded XXX Corps in 1941, and later commanded several armies.

This is a genuine military command identity with a Saar/Rhenish-border birth connection, but the only rights-clear archival likeness located for this package is a 1947–1948 postwar courtroom photograph.

The identity, life dates, and command history are [Hans von Salmuth](https://en.wikipedia.org/wiki/Hans_von_Salmuth).

The archival source is [Hans von Salmuth, defendant in High Command Trial](https://commons.wikimedia.org/wiki/File:Hans_von_Salmuth,_defendant_in_High_Command_Trial.jpg).

The direct original download used for the unchanged master is `https://upload.wikimedia.org/wikipedia/commons/1/11/Hans_von_Salmuth%2C_defendant_in_High_Command_Trial.jpg`.

The source/object record is [National Archives Catalog 167824751](https://catalog.archives.gov/id/167824751).

The object describes Salmuth as a defendant in the High Command Trial at Nuremberg between 30 December 1947 and 28 October 1948 and credits the Office of Military Government for Germany, United States.

The source is a United States federal-government work and is marked public domain under 17 U.S.C. §105; the Commons page carries `PD US Government` and Public Domain Mark metadata.

The unchanged archival master is `source_masters/AJX_hans_von_salmuth_nara_high_command_trial_1947_48.jpg` with decoded dimensions 2248×2953, RGB mode, 3,938,157 bytes, and SHA-256 `62690D60390673D6D9312C6123513D7F886B0BF2115C0A22228BC2E9C59CA816`.

The explicit head-and-shoulders crop is `source_crops/AJX_karl_becker_hans_von_salmuth_nara_1947_48_head_shoulders.png`.

The crop rectangle in decoded master pixels is half-open `(left=340, top=190, right=1910, bottom=2340)`, producing 1570×2150 pixels without resizing, retouching, recolouring, removal of the source name card below the crop, or clothing alteration.

The crop has SHA-256 `B2E3B1E498C8B85837F77006D523BF6922D743CF024F4DC9138572FEB56D8236`.

The exact decoded-pixel equality proof is `metadata/AJX_karl_becker_hans_von_salmuth_nara_1947_48_head_shoulders.json`, whose `decoded_pixels_equal` field is `true` and whose master/output RGBA digest is `0cbc1ea42c2673a02f1aa0cd02cf2a4db0de4945ec637f93742d12294548f20e`.

The source-crop command and tool digest are recorded by the JSON evidence: `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py`, tool SHA-256 `14fa178d6df999346874a7033e84f9b3ae988e7d845f3a4b2f8a44755e30641c`.

Suggested stable large sprite name, only if the parent accepts the era/role caveat, is `GFX_portrait_AJX_karl_becker_commander_large`.

The source crop is deliberately not converted to DDS in this subtask.

## Commander-era evidence and explicit uncertainty

The subject was alive in 1936 and his documented 1934–1937 II Corps staff role and later XXX Corps/army commands make the identity period-defensible as a military figure.

The photograph itself is not period-matching to 1936 and shows him as a civilian courtroom defendant after the war, so it must not be silently treated as a 1936 uniform portrait.

The Commons file [Hans von Salmuth.jpg](https://commons.wikimedia.org/wiki/File:Hans_von_Salmuth.jpg) records a 1943 uniform image from the Britannica biography / Georg Friedrich Lorenz collection, but the author is unknown and the publication/object provenance is not archive-grade for this clearance.

That 1943 file remains `source_masters/Hans_von_Salmuth.jpg` as research-only evidence with SHA-256 `1BBA8A6AD8E01CB621FEDDC3889382F0F5049803843AF35FAD517C2C8E695BA9` and is not selected for runtime.

## Rejected candidates and ownership findings

Karl Jarres was rejected despite a clean 1925 Bundesarchiv source because the ownership scan found a live `GER_karl_jarres` character, portrait, recruit, and localisation in approved Kaiserreich `1521695605` (`common/characters/GER characters.txt:85-101`, `history/countries/GER - Germany.txt:286`, `interface/kaiserreich/portraits/GER_portraits.gfx:15-16`, and `localisation/english/KR_country_specific/GER - Germany l_english.yml:38-39`).

The unchanged Jarres master is retained only for this rejection audit at `source_masters/AJX_karl_jarres_bundesarchiv_1925.jpg` with SHA-256 `72C952B0F1A1E3C08A16B20C123466B4BFC737D7C03AE63594CF7E6332C2C8D6`.

Its audit-only exact crop is `source_crops/AJX_friedrich_hoffmann_karl_jarres_1925_head_shoulders.png` with evidence `metadata/AJX_friedrich_hoffmann_karl_jarres_1925_head_shoulders.json`; it is not assigned to any consumer and must not be wired because of the ownership collision.

The prior Event 6 research record already rejects Johannes Hoffmann because the available 1955 CC0 photograph is too late for a strict 1936 likeness and the earlier pre-1940 source was rights/quality blocked.

The prior Event 6 research record rejects Willy Schmelcher because his documented police/SS security role does not fit a neutral civic or military territorial commander consumer.

The prior Event 6 research record rejects the exact historical Karl Becker because vanilla owns the character/portrait identity and its role evidence is not a defensible match for this consumer.

The prior Event 6 research record rejects Wilhelm Fahrmbacher because no sufficiently clear rights-safe face source was found at usable portrait quality.

Ernst Busch is retained only as rejected research evidence because the clear 1940 portrait is attributed through a secondary news source with an unknown author, while the Bundesarchiv alternative is only 173×260 pixels.

Friedrich Herrlein is retained only as rejected research evidence because the available 1925 image is a damaged group photograph and cannot be cropped into an identity-safe single-person portrait.

The ownership scan covered exact and variant forms for both selected subjects and the rejected Jarres candidate across the current Chaos Redux ownership paths (`common/characters`, `history/countries`, `interface`, `gfx/leaders`, `gfx/portraits`, and `localisation`), vanilla, and approved mod roots `1521695605`, `2265420196`, and `1458561226`.

The scan found no current, vanilla, or approved-mod live character/portrait/recruit/localisation ownership for Walter Simons or Hans von Salmuth.

## Review assets

The candidate comparison sheet is `research/ajx_two_role_source_candidates_contact_sheet.png`.

The machine-readable copy of this manifest is `manifest.json`.
