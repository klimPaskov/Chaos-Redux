# IW-173 HAW David Kalakaua Kawananakoa source-clearance retry 02

Date: 2026-07-24  
Asset owner: Chaos Redux sourced visual asset subagent  
Subject: David Kalākaua Kawānanakoa (1904–1953), male-presenting historical country leader  
Requested consumer: one guarded full-size country-leader portrait for the existing HAW leader token  
Disposition: **BLOCKED / NO-PASS**  

This package is export-only evidence. It contains no ImageGen result, no processed 156×210 portrait, no DDS, no `.gfx` edit, no gameplay edit, no localisation edit, and no `_small`, advisor, dossier, commander, or operative asset.

## Source and crop evidence

No new production-safe adult source was found. The retained archival evidence is the previously identified Commons photograph because it is the only identity- and rights-defensible candidate located, but its clipped facial highlights make it unsuitable for a source-locked portrait admission.

| Evidence | Path or URL | Dimensions | SHA-256 / disposition |
|---|---|---:|---|
| Unchanged archival master | `source_masters/HAW_david_kalakaua_kawananakoa_1925_original.jpg` | 1109×1700 | `E23304AFA45091FA6B7FF0179CAA688BCD7EE0027306B22E853A14C1344DA909`; byte-identical copy of the existing master |
| Commons file page | <https://commons.wikimedia.org/wiki/File:David_Kalakaua_Kawananakoa.jpg> | — | Attribution identifies David Kalākaua Kawānanakoa (1904–1953), 1925, George F. M. Nellist (ed.), *The Story of Hawaii and Its Builders*, Honolulu Star-Bulletin, p. 560, photographer unknown |
| Archived original URL | <https://upload.wikimedia.org/wikipedia/commons/archive/e/eb/20180819043404%21David_Kalakaua_Kawananakoa.jpg> | — | Source URL recorded for provenance; do not replace the local master |
| Exact head-and-shoulders crop | `source_crops/HAW_david_kalakaua_kawananakoa_1925_head_shoulders.png` | 700×942 | `2B4B96D2E1D3A2398E257A8104CCE4E082D169EFE0749EDB2603D68B4859149A` |
| Crop-box evidence | `metadata/HAW_david_kalakaua_kawananakoa_1925_head_shoulders.json` | — | Crop `(245,170,945,1112)`; decoded-pixel equality `true`; pixel count `659400`; both RGBA hashes `43d43df2f11f482ae845e343dd453bf5789d3b07c9dc4898cc6dad3765deab3b` |
| Rejected-candidate contact sheet | `research/rejected_adult_candidates_contact_sheet.jpg` | 800×800 | `C3363D21097DC9373A6BB319BE9316E531CA4F36E4EFB71CF0F447AB9EF21489`; research-only comparison of rights-unclear adult uploads and watermarked Alamy source |

The crop was produced with `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py` version `1.0` (SHA-256 `14fa178d6df999346874a7033e84f9b3ae988e7d845f3a4b2f8a44755e30641c`) using Pillow 11.1.0 and the required decoded-master equality check.

## Rights and identity basis

The Commons record attributes the image to the 1925 publication cited above and states United States public-domain status because the publication predates 1 January 1930. The photographer is unknown, so the package does not invent an individual photographer or a separate transfer of rights.

The target is the son David Kalākaua Kawānanakoa (1904–1953), not his father David Kawānanakoa (1868–1908). The Commons title and attribution identify the 1904–1953 subject, while Digital Archives of Hawaiʻi records `ark:70111/1BD0`, `ark:70111/1BCX`, and `ark:70111/1CP4` explicitly identify the older 1868–1908 father and were rejected as wrong-person sources.

## Search and rejection record

| Candidate | Exact source | Finding | Disposition |
|---|---|---|---|
| 1937 adult photograph | <https://www.alamy.com/nephew-of-hawaiis-last-king-detained-following-wifes-death-david-kalakaua-kawananakoa-33-year-old-grandnephew-of-king-david-kalakaua-last-male-monarch-of-hawaii-and-son-of-the-princess-kawananakoa-has-been-detained-by-the-honolulu-police-during-investigations-into-the-death-of-his-asserted-common-law-wife-r-ville-kinslea-the-22-year-old-girl-was-found-dead-with-a-deep-gash-in-the-neck-and-several-facial-lacerations-after-a-party-at-her-home-1-november-1937-2BW2A3C.jpg> | Exact target at age 33 and visually stronger, but the available image carries an Alamy watermark and the page is rights-managed stock without a public-domain or reusable licence basis. | Rejected; not ownership-clear. |
| Find a Grave adult front-facing upload | <https://images.findagrave.com/photos/2024/64/157092616_8373900f-5e22-4b24-b8f7-8a2ea3db33a1.jpeg> | Strong adult likeness candidate, but the memorial page and image provide no photographer, publication, archive, or reuse licence evidence. | Rejected; user-uploaded rights unclear. |
| Find a Grave adult side/three-quarter upload | <https://images.findagrave.com/photos/2016/14/157092616_1452868137.jpg> | Adult target candidate, but the image is a user upload with no defensible provenance or reuse basis. | Rejected; rights unclear. |
| Find a Grave copy of the 1925 portrait | <https://images.findagrave.com/photos/2024/59/157092616_3106e6e7-eae3-4cce-a79b-bcfc3da8e65d.jpeg> | Same clipped Commons portrait, not a stronger source and no independent provenance improvement. | Rejected; does not solve the likeness gate. |
| 1908 children group photograph | <https://commons.wikimedia.org/wiki/File:The_Three_Children_Of_The_Late_Prince_And_The_Princess_Kawananakoa,_1908.jpg> | Public-domain period image from *The Pacific Commercial Advertiser* (1908), but the target appears as a child in a three-child group and cannot serve as the adult leader identity master. | Rejected as production source; retained only as identity corroboration. |
| Digital Archives adult photographs | <https://digitalarchives.hawaii.gov/item/ark:70111/1BD0>, <https://digitalarchives.hawaii.gov/item/ark:70111/1BCX>, <https://digitalarchives.hawaii.gov/item/ark:70111/1CP4> | Metadata names David Kawānanakoa (1868–1908), the father, or otherwise shows the older generation. | Rejected as wrong identity. |

The sharper adult candidates were compared in the research-only contact sheet. The sheet is not a source master, is not rights-cleared, and must not ship or enter runtime. No candidate satisfies both the exact identity gate and the ownership-clearance gate.

## Why the retained source is not admitted

The 1925 source is the correct person and meets the source-attribution and public-domain evidence gate, but the forehead and central facial planes are blown out or clipped nearly white. The prior source-locked trial reconstructed missing brow, eye, nose, cheek, jaw, and hair information and failed independent likeness review as a generic adult rather than a verifiable exact likeness. The exact crop is therefore retained as evidence only and is not an approved ImageGen identity source for promotion.

## Ownership and consumer scan

The exact vanilla consumer is `history/countries/HAW - Hawaii.txt:60-62`, where the vanilla country leader is named `David Kalakaua Kawananakoa` and uses `GFX_portrait_David_Kalakaua_Kawananakoa`. Vanilla maps that token at `interface/_leader_portraits.gfx:7961-7963` to `gfx/leaders/Asia/Portrait_Asia_Generic_land_5.dds`.

The current Event 006 preservation trigger at `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt:37-44` keeps the ruling-only vanilla HAW leader and does not recruit, promote, retire, or replace HAW leaders. The current mod has no HAW character, portrait, `.gfx`, DDS, `_small`, advisor, dossier, commander, or operative override for this person.

The approved Kaiserreich workshop scan found only the unrelated Lydia Lili'uokalani Kawānanakoa leader material. Approved workshop IDs `2265420196` and `1458561226` contain no exact David Kalakaua Kawananakoa character or portrait owner. No duplicate or ownership transfer is authorized.

## Promotion status

Keep the vanilla generic HAW leader portrait active. Do not run ImageGen, resize to 156×210, convert to DDS, add a sprite, edit `.gfx`, edit vanilla history, change the character roster, or broaden the consumer boundary from the single guarded full-size leader token. A future retry requires a new attributed, rights-clear adult photograph with sufficient un-clipped facial geometry and a fresh exact crop before any source-locked repaint can be considered.
