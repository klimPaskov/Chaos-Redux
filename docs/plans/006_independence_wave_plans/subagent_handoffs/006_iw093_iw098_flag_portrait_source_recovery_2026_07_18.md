# IW-093 / IW-098 — flag and portrait source recovery handoff

**Date:** 2026-07-18
**Scope:** source-only follow-up for Event 006 Independence Wave, IW-093 Asante
and IW-098 Sokoto. This note records archival evidence, rights status, rejected
substitutes, and the remaining blockers. It does not create or wire a flag,
portrait, DDS, sprite, `.gfx`, or gameplay asset.

## Executive status

| Request | Status | Finding |
|---|---|---|
| Hasan dan Mu'azu Ahmadu face-visible archival portrait | **blocked / needs permission** | The only authoritative identity match found is Northwestern's E.H. Duckworth postcard. Its catalog says `In Copyright - Educational Use Permitted` and prohibits further distribution/commercial use. The scan also leaves the face substantially veiled. Commons' Nigerian-public-domain assertion conflicts with the owning institution's terms. |
| Better Prempeh II source | **cleared source retained; improved candidate conditional** | The National Archives UK CO 1069/44-12 source already in the repository is OGL v1.0 and has clear face/shoulders, but is monochrome. A frontal 1938 book image is visually stronger but has unresolved German publication/photographer rights; Met/Morehead postcard imagery has no clear reuse grant. No replacement was approved. |
| Exact Asante restored-1935 flag | **blocked** | The primary 1935 restoration report was checked page-by-page and contains no flag image or stripe/device description. It documents the National/Golden Stool as a national emblem and state umbrellas only. No exact stripe order, proportions, fimbriation, or device can be asserted. |
| Exact Sokoto 1936 flag | **blocked** | Scholarly and period evidence describes several Caliphate-era/local standards, not one standardized 1936 state flag. A c.1853 white vizier banner and a 1903 captured white Attahiru banner are useful historical references but are not proof of Hasan's 1936 court standard. |

Do not promote any blocked item to a final asset. The existing Prempeh
processed PNG is already documented as rejected for visual style and has no
runtime DDS; it must not be wired as a fallback.

## IW-098 — Hasan dan Mu'azu Ahmadu

### Identity-matched archive record

The narrowest and most authoritative result is Northwestern University Digital
Collections, E.H. Duckworth Photograph Collection:

- Item: [Sultan of Sokoto and others on a carpeted dais](https://dc.library.northwestern.edu/items/ac89793d-6016-42b0-8f66-ac86cf7bd51f).
- Northwestern item id: `ac89793d-6016-42b0-8f66-ac86cf7bd51f`.
- The catalog description identifies Hasan dan Mu'azu Ahmadu as Sultan of
  Sokoto, 1931–1938, and notes that the usual face was uncovered. This scan,
  however, has a white veil/scarf across the face, so it is not a dependable
  face-visible portrait source.
- File-set download (do not redistribute without permission):
  `https://api.dc.library.northwestern.edu/api/v2/file-sets/1c3dba64-fc18-49b0-9883-eeb45778bfca/download`.
- Catalog image dimensions: 1519 × 2323; catalog date range is `1930 to
  1972`, not a precise exposure date.
- Rights statement: **In Copyright – Educational Use Permitted**. Terms allow
  research consultation/scholarly use but state that further distribution and
  commercial use are not permitted. The owning-institution statement controls
  this handoff; a Wikimedia relicense claim is not enough to clear a mod asset.

The Wikimedia copy, [File:Sultan Hasan dan Muazu.jpg](https://commons.wikimedia.org/wiki/File:Sultan_Hasan_dan_Muazu.jpg),
is the same E.H. Duckworth image and is correctly associated with the
1930–1938 Sultan, but its uploader's Nigerian-public-domain rationale conflicts
with Northwestern's item-level rights statement. It is therefore research
only. No copy was added to the repository and no portrait processing is
authorized.

### Other candidates checked and rejected

- [Getty/Hulton Archive, 2 July 1934](https://www.gettyimages.co.uk/detail/news-photo/west-african-royals-hasan-dan-muazu-ahmadu-sultan-of-sokoto-news-photo/1772784818)
  is a rights-managed commercial image. It requires a Getty license and is
  not a rights-compatible source master.
- [Commons London Zoo group image](https://commons.wikimedia.org/wiki/File:The_sultan_of_Sokoto_and_the_emirs_of_Gwandu_and_Kano_at_the_London_Zoological_Gardens_with_Frederick_Lugard.png)
  was rejected as an identity/date substitute. The Guardian's source caption
  identifies it as Lord Lugard with West African chiefs at London Zoo in **1924**
  and credits Fox Photos/Getty, not a June 1934 Hasan portrait. The Commons
  label is not sufficient evidence for this event.

No second face-visible, rights-compatible 1930s Hasan-specific archive source
was located. Resolution requires written Northwestern permission, a separately
licensed public-domain/CC source with a clear face, or a new authoritative
archive record. Do not substitute Siddiq Abubakar III (post-17 June 1938), a
generic Hausa/Fulani portrait, the veiled crop, or the misidentified group
photograph.

## IW-093 — Prempeh II source comparison

### Retained rights-cleared source

The repository already contains the best fully documented source:

- [The National Archives UK / Africa Through a Lens, CO 1069-44-12](https://www.flickr.com/photos/nationalarchives/5416372614),
  31 January 1935, Colonial Office photographic collection.
- Commons record: [Nana Otumfuo Agyeman Prempeh II](https://commons.wikimedia.org/wiki/File:Nana_Otumfuo_Agyeman_Prempeh_II.jpg).
- Open Government Licence v1.0 with TNA attribution; the package records VRT
  ticket `2012050210007172`.
- Existing source master:
  `docs/assets/006_independence_wave/iw093_asante_prempeh_ii_2026_07_18/source_image/CO_1069-44-12_prempeh_ii_1935.jpg`
  (393 × 563).
- Lossless decode:
  `docs/assets/006_independence_wave/iw093_asante_prempeh_ii_2026_07_18/source_png/CO_1069-44-12_prempeh_ii_1935.png`.
- Existing hashes: JPEG
  `98a1109e23751f0ad64d970044c1c1eca3040333d7e16da357804b484587f144`;
  PNG `0ed4560bab1a38d5ba20f55c56b5ee9e7bb5afba66ca0ddb40589c357806a699`.

The face and shoulders are clear and the date exactly matches the restoration,
but the photograph is grayscale. The prior deterministic candidate remains
`blocked`: parent visual review rejected its sharpened monochrome treatment as
not matching the painted/color country-leader family. See the existing package
manifest and `validation/visual_review.md`; no DDS or sprite is authorized.

### Visually stronger but conditional references

| Candidate | Evidence and visual value | Rights/use disposition |
|---|---|---|
| [PrempehII.jpg](https://commons.wikimedia.org/wiki/File:PrempehII.jpg) | Gustav Adolf Gedat, *Was wird aus diesem Afrika?* (Stuttgart, 1938); frontal head/shoulder detail and better tonal separation than CO 1069/44-12. | Commons gives a Ghana public-domain rationale, but the German publication, author, and unknown photographer were not independently cleared. **Conditional research reference only; do not copy into runtime package.** |
| [Morehead State Methodist Book Depots postcard](https://scholarworks.moreheadstate.edu/still_postcards/22/) / [record 1027](https://scholarworks.moreheadstate.edu/still_postcards/1027/) and [Met DP251913 image](https://images.metmuseum.org/CRDImages/ao/web-large/DP251913.jpg) | Sepia postcard portrait with clear face/shoulders and printed Asantehene title; visually useful for comparison. | No explicit reuse grant was found on the Morehead record or Met hotlink. **Rights unclear; not a source master.** |
| [British Museum image 47975004](https://www.britishmuseum.org/collection/image/47975004) / [EA_Af-A14-40](https://www.britishmuseum.org/collection/object/EA_Af-A14-40) | Mary S.R. Sinclair, 2 March 1936; useful period identity cross-check but procession framing is not a clean portrait. | CC BY-NC-SA 4.0 (noncommercial/share-alike with credit); commercial/runtime redistribution would require a separate license. **Reference only.** |

No fully cleared color/tonal replacement was found. Retain the TNA source as
the only rights-cleared candidate, and keep the final portrait requirement
open rather than silently using a conditional image.

## IW-093 — Asante restoration flag evidence

### Primary check

The University of Ghana scan, [A Full and Illustrated Report of the Restoration
of the Ashanti Confederacy](https://ugspace.ug.edu.gh/server/api/core/bitstreams/2141daaf-b7ac-454c-8306-9bb400a21db5/content),
31 January–4 February 1935, was downloaded and checked across all 39 scanned
pages. It contains photographs and appendices about the **National Stool**
(the report's preferred wording), state umbrellas, regalia, and the restoration
ceremony. It has no `flag`, `standard`, or `banner` description and no flat
flag plate. The report therefore supports the Stool as an emblematic court/
national object, but it does **not** establish a flag's stripe order, band
heights, white fimbriation, central device, lettering, or proportions.

### Motif separation

| Motif/design claim | Evidence class | Safe treatment |
|---|---|---|
| Gold/black/green Asanteman palette | Later/secondary flag references, including [FOTW's Asante survey](https://www.fotw.info/flags/gh_asa.html) | Historical context only; palette alone is not proof of the 1935 geometry. |
| National/Golden Stool | Explicitly described as a national emblem in the 1935 restoration report | May explain court symbolism, but does not prove a flag device. Treat sacred/cultural imagery carefully. |
| Modern Asantehene car/royal flags, narrow white separators, Gyemirekutu (“hat”) device | Modern/late royal usage documented by secondary flag surveys | Do not back-project as the restored-1935 flat flag without a period plate. |
| Cocoa/porcupine/green-and-gold nationalist compositions | Later c.1950s nationalist material | Not an IW-093 1935 restoration flag. Keep separate from royal/court identity. |
| Gold Coast colonial Blue Ensign or generic West African tricolor | Colonial/unrelated or generic | Exclude. |
| “1935 Ashanti flag” with unverified stripe/device proportions | Secondary claim without primary geometry | **Blocked; do not draw or generate.** |

The exact restored-1935 flag remains blocked pending a dated flag photograph,
archive catalog entry, period newspaper plate, court record, or other source
that actually shows/describes the geometry. No generated flag or reconstructed
Golden Stool seal was made.

## IW-098 — Sokoto flag evidence

### What the sources establish

The best historical source is Murray Last, *The Sokoto Caliphate*, via the
International African Institute [book page](https://www.internationalafricaninstitute.org/publishing/sokoto_caliphate)
and [permission-hosted PDF](https://www.internationalafricaninstitute.org/downloads/sokoko_caliph.pdf),
printed p. 53. Last describes multiple expedition/local standards: a c.1853
Vizier `Abd al-Qadir b. Gidado banner was white, approximately 6 feet tall by
3 feet wide, assembled from two square pieces on a wooden pole, with small
Arabic inscriptions near the pole and otherwise plain cloth. He also records
smaller blue and white variants, including a later white damask example. This
is evidence of plural Caliphate-era banners, not a single standardized state
flag in 1936.

Additional period evidence:

- [1902 Northern Nigeria annual report](https://libsysdigi.library.illinois.edu/ilharvest/Africana/Books2011-05/3064634/3064634_1902_northern_nigeria/3064634_1902_northern_nigeria_opt.pdf)
  records a press story about an “ancient banner of Dan Fodio” and a green
  flag, then explicitly says there were no grounds for the report. This is a
  warning against treating a green banner as attested Sultanate geometry.
- [1905–06 Northern Nigeria annual report](https://libsysdigi.library.illinois.edu/ilharvest/Africana/Books2011-05/3064634/3064634_1905_1906_northern_nigeria/3064634_1905_1906_northern_nigeria_opt.pdf)
  mentions Satiru religious rebels planning to hoist a green flag. That is a
  Mahdist/rebel plan, not a Sokoto Sultan's official 1936 standard.
- [Burmi flag artifact record](https://commons.wikimedia.org/wiki/File:Flag_of_the_Sokoto_Caliphate_used_during_the_Battle_of_Burmi.png)
  identifies a white cloth captured beside Caliph Attahiru at Burmi on 27 July
  1903 and returned to the Sultan in 1960. The surviving photograph is faded
  and framed; its markings cannot support a reliable flat redraw. It is a
  specific 1903 artifact, not proof of Hasan's 1936 court flag.
- [Commons “Flag of the Sokoto Caliphate” reconstruction](https://commons.wikimedia.org/wiki/File:Flag_of_the_Sokoto_Caliphate.svg)
  explicitly says its insignia is unconfirmed, lacks source information, and
  is own work/self-made. It is rejected as historical evidence.

### 1936 conclusion and exclusions

In 1936 Hasan was Sultan in the post-1903 colonial successor sultanate/native-
administration setting. No authoritative source found an exact 1936 court/state
flag, fixed proportions, seal, or Arabic calligraphy. Keep all of the following
out of a final asset unless separately proven: modern Sokoto State flag
(post-1976), generic black jihad banners, generic green Mahdist flags, the
Commons self-made reconstruction, and invented Arabic inscriptions.

The exact IW-098 flag is therefore **blocked**. A museum/archive object record
or a period photograph showing Hasan's 1930s court standard is required before
any flat design can be treated as historical.

## Source ledger and rights/use disposition

| Source | Date/era | Rights/source status | Intended use in this task |
|---|---|---|---|
| TNA CO 1069-44-12, [official Flickr](https://www.flickr.com/photos/nationalarchives/5416372614) | 31 Jan 1935 | OGL v1.0, TNA attribution; source already pinned in repository | Cleared Prempeh source; final portrait still blocked by rejected visual treatment. |
| [PrempehII.jpg](https://commons.wikimedia.org/wiki/File:PrempehII.jpg) | Book published 1938 | Commons Ghana-PD rationale, but photographer/publication rights unresolved | Conditional visual reference only. |
| [Met/Morehead Prempeh postcard](https://scholarworks.moreheadstate.edu/still_postcards/22/) | c.1930 | No explicit reuse grant located | Conditional visual reference only. |
| [British Museum 47975004](https://www.britishmuseum.org/collection/image/47975004) | 2 Mar 1936 | CC BY-NC-SA 4.0; noncommercial/share-alike | Identity/era cross-check only. |
| [Northwestern Duckworth Hasan item](https://dc.library.northwestern.edu/items/ac89793d-6016-42b0-8f66-ac86cf7bd51f) | catalog range 1930–1972; subject 1931–38 | In Copyright – Educational Use Permitted; no further distribution/commercial reuse | Exact identity match, but veiled and rights-blocked. |
| [Getty Hasan image](https://www.gettyimages.co.uk/detail/news-photo/west-african-royals-hasan-dan-muazu-ahmadu-sultan-of-sokoto-news-photo/1772784818) | 2 Jul 1934 | Rights-managed; purchase license required | Excluded. |
| [UG 1935 restoration report](https://ugspace.ug.edu.gh/server/api/core/bitstreams/2141daaf-b7ac-454c-8306-9bb400a21db5/content) | 31 Jan–4 Feb 1935 | Research source; no flag plate found | Primary Asante emblem/context check, not flag geometry. |
| [Murray Last / IAI PDF](https://www.internationalafricaninstitute.org/downloads/sokoko_caliph.pdf) | historical synthesis, printed 1967 | IAI CC BY-NC-ND 3.0 by permission | Documents plural Sokoto banner forms; not a 1936 standard. |
| [1902 Northern Nigeria report](https://libsysdigi.library.illinois.edu/ilharvest/Africana/Books2011-05/3064634/3064634_1902_northern_nigeria/3064634_1902_northern_nigeria_opt.pdf) | 1902 | Period government report | Rejects unsupported “green flag” press claim. |
| [1905–06 Northern Nigeria report](https://libsysdigi.library.illinois.edu/ilharvest/Africana/Books2011-05/3064634/3064634_1905_1906_northern_nigeria/3064634_1905_1906_northern_nigeria_opt.pdf) | 1905–06 | Period government report | Distinguishes Satiru rebel green-flag plan from Sultanate standard. |
| [Burmi artifact photo](https://commons.wikimedia.org/wiki/File:Flag_of_the_Sokoto_Caliphate_used_during_the_Battle_of_Burmi.png) | 1903 artifact | Commons claims Nigerian-government public domain; artifact image is poor | Historical white-banner context only; not 1936 geometry. |
| [FOTW Asante survey](https://www.fotw.info/flags/gh_asa.html) | modern/secondary survey | Secondary research; no primary 1935 plate | Variant context only; not proof of restoration geometry. |

## Repository and handoff disposition

- No new rights-cleared Hasan source master was added: the Northwestern file is
  permission-restricted and the face is veiled.
- No conditional Prempeh image was copied into the asset package. The existing
  TNA source remains the only cleared source master; the processed candidate is
  rejected and remains without runtime DDS.
- No flag art, portrait art, DDS, contact sheet, `.gfx`, interface,
  localisation, or gameplay file was created or edited in this follow-up.
- The parent may continue implementation with these source requirements open,
  but must not silently substitute the rejected portrait, a generic portrait,
  a modern flag, or an invented flag geometry/calligraphy.
