# Event 6 western-gap portrait retry handoff

Date: 2026-07-22
Scope: source research and unchanged archival master acquisition only. No gameplay, localisation, `.gfx`, crop, processing, PNG, DDS, or runtime wiring changes.

The full role-by-role evidence is in [the bounded source manifest](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/western_gap_retry/manifest.md).

## First source-ready tranche

These are unchanged full-resolution originals with face-visible subjects, exact local bytes/dimensions/hashes, and a documented archive/licence basis:

- **WLS civic/national leader — Saunders Lewis**
  - Local: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/western_gap_retry/source_masters/WLS/WLS_saunders_lewis_ydrych_1916.jpg`
  - Source: [Y Drych / National Library of Wales scan](https://papuraunewydd.llyfrgell.cymru/view/3776384/3776392/60/), via [Commons original](https://upload.wikimedia.org/wikipedia/commons/a/ab/Saunders-lewis-y-drych-1916.jpg)
  - Date/author: 3 February 1916; Y Drych, author not stated; Public Domain Mark/pre-1931 publication basis.
  - 1016x2239, 1,499,841 bytes, SHA-256 `d1552ea79f34d162e972ebe0528c219755e52f851226d6e07ef560e8c29b80e3`.
  - Full newspaper-page framing is preserved; the source was not cropped.

- **BAY civic leader — Heinrich Held**
  - Local: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/western_gap_retry/source_masters/BAY/BAY_heinrich_held_keystone_1933.jpg`
  - Source: [Polish National Digital Archive record](https://www.szukajwarchiwach.gov.pl/en/jednostka/-/jednostka/6270998/obiekty/473188), via [Commons original](https://upload.wikimedia.org/wikipedia/commons/0/03/Heinrich_Held%2C_1933.jpg)
  - Date/author: circa 1933; Agencja Keystone View Company; Commons states CC0 1.0.
  - 2471x3623, 1,664,336 bytes, SHA-256 `35d1ee399c8c86efd024e8226a8effe97afc5fc0114c4a1186ad9cd4d6c3560d`.
  - The archive watermark band is part of the unchanged source.

- **BAY commander — Franz Ritter von Epp**
  - Local: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/western_gap_retry/source_masters/BAY/BAY_franz_von_epp_nara_1920s_1930s.jpg`
  - Source: [NARA catalog item 162122527](https://catalog.archives.gov/id/162122527), via [Commons original](https://upload.wikimedia.org/wikipedia/commons/f/f5/242-HF-0533_001_Franz_Ritter_von_Epp_%281868-1947_WWI_German_Army_Freikorps_1919_Reichswehr_Generalmajor_1922_BVP_1919-28_NSDAP_Reichstag_1928-45_Reichsstatthalter_Bavaria_1933-45_etc%29_Undated_1920-30s_NARA_Unrestricted_Unknown_copyright.jpg)
  - Date/author: undated, probably 1920s–early 1930s; uncredited photographer; NARA describes unrestricted access/use. Commons also records CC BY-SA 4.0, Public Domain Mark, and US-government-PD notices.
  - 3500x4652, 1,833,478 bytes, SHA-256 `b8b67179e548cdd2e495e0e175a4001e3ead6d7c39717036ac5a3e1a38ff0ca7`.
  - Exact Bavarian Army/Freikorps commander identity; civilian dress and Nazi/Freikorps historical-context caveats remain for review.

- **RHI river/army commander — Josef Harpe**
  - Local: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/western_gap_retry/source_masters/RHI/RHI_josef_harpe_bundesarchiv_original.jpg`
  - Source: [Bundesarchiv attribution/accession page](https://commons.wikimedia.org/wiki/File%3ABundesarchiv_Bild_146-1981-104-30%2C_Josef_Harpe.jpg), [direct Bundesarchiv original](https://bild.bundesarchiv.de/device_barch/dev1/2022/11-28/b2/97/file7nthh588rkij6p2a22kj.jpg)
  - Date/author: 1943; Heinrich Hoffmann; CC BY-SA 3.0 Germany, `Bundesarchiv, Bild 146-1981-104-30 / Hoffmann, Heinrich / CC-BY-SA 3.0`.
  - 4637x7455, 7,356,362 bytes, SHA-256 `5353200abd3584c52a4938f2a79bf62c15d1be6aad22d70e0c45f1a4181c1384`.
  - Actual German Army General der Panzertruppe; born Buer (now Gelsenkirchen), a defensible Rhineland-Westphalia connection. If the RHI role is interpreted as strictly Cologne-specific, use parent review before processing.

## Review-gated alternatives

- **RHI alternate — Günther Korten**: direct Bundesarchiv original is present at `source_masters/RHI/RHI_gunther_korten_bundesarchiv_original.jpg` (2599x4047, 2,500,878 bytes, SHA-256 `769e6272df1286c48807c1d888d3583098b37ea3fd73512576572894fc7e98a4`). He was born in Cologne and was a real Luftwaffe General der Flieger, but the branch is air force rather than army/river command. Status `needs_review`; do not silently replace Harpe with him.
- **AJX civic leader — Johannes Hoffmann**: two identical local files (`AJX_johannes_hoffmann_brazilian_immigration_1941.jpg` and `AJX_johannes_hoffmann_saar_nostalgie_1941.jpg`), each 306x408, 67,510 bytes, SHA-256 `9f9032681cd7cb2f087d2b89cd7932c8702e1fe872e33533cd754d19819416cf`. The 2 June 1941 anonymous Brazilian Immigration Agency image is identity-accurate, but Commons' Brazilian-PD claim is paired with a URAA warning and Saar-Nostalgie identifies the Hoffmann family estate. Status `needs_review` until rights are resolved.

## Blocked roles and explicit non-substitutions

- **AFX Walloon commander**: Jules-Joseph Pire is the role-accurate lead (Belgian Army lieutenant-general from Hannut/Wallonia), but available image references do not expose a clear reuse licence and no defensible original was acquired. Albert Devèze is rejected as a civilian politician.
- **WLS military/mountain commander**: Sir Charles John Cecil Grant (GOC 53rd Welsh Division) is role-accurate, but the National Portrait Gallery image is not a free/original source suitable for this handoff. David Lloyd George is rejected as a civilian politician.
- **BRI Morvan Marchal and Célestin Lainé**: Ouest-Eclair/BnF Commons pages explicitly warn that the deprecated PD-BNF rationale does not establish current public-domain status; no rights-defensible original was downloaded. Lainé's collaborationist/Bezen Perrot record remains a required caveat if a future source is found.
- **AJX security/military commander**: Saar role research found Willy Schmelcher and Anton Dunckern, but no attributable, face-visible, rights-defensible original. Max Braun is rejected because the available portrait is political/civilian and does not meet the requested security/military role.

The smaller Harpe and Korten Wikimedia derivatives already in the bounded folder are marked `rejected_derivative` in the manifest; process the direct archive originals only. BAY Rupprecht and RHI Josef Friedrich Matthes remain untouched. No generated face, generic substitute, proxy, or re-encoded fallback was used.

## Parent action

The parent may independently review and send only selected `source_ready` masters through the normal identity-preserving portrait pipeline. This source retry does not create processed PNGs or DDS files and does not provide independent visual approval. `needs_review` and `blocked` rows must remain out of runtime wiring until their stated issues are resolved.
