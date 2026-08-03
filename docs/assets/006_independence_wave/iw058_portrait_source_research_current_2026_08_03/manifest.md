# IW-058 ASY grounded portrait source package (2026-08-03)

This source-only package records a newly researched archival candidate for the IW-058 Assyria Concordat Council roster. It contains no DDS, GFX edit, character edit, or runtime admission. The candidate is deliberately held at `needs_user_review` because the public-domain assertion is source-platform metadata rather than a jurisdiction-independent legal opinion.

## Primary candidate

| Field | Value |
|---|---|
| Subject | Yousef VI Emmanuel II Thomas (Mar Yousef VI Emmanuel II Thomas) |
| Historical role | Chaldean Catholic Patriarch of Babylon, 1900-1947 |
| IW-058 fit | Possible Concordat Council institutional/civic seat; parent must confirm roster semantics |
| Baseline fit | Alive and serving in 1936; Catholic-Hierarchy records the 1900 selection/confirmation and 1947 death |
| Source mode | `sourced_real_person` |
| Status | `needs_user_review` |
| Runtime authorized | `false` |
| Runtime basename | Not supplied by parent; no runtime basename is invented in this source-only pass |

## Source provenance

| Item | Evidence |
|---|---|
| Commons file | [His Beatitude the Chaldean, Patriarch of Babylon.jpg](https://commons.wikimedia.org/wiki/File:His_Beatitude_the_Chaldean,_Patriarch_of_Babylon.jpg) |
| Source scan | [Shall this nation die? (1921), HathiTrust/Library of Congress scan](https://babel.hathitrust.org/cgi/pt?id=loc.ark:/13960/t6nz91c0r) |
| Commons metadata date | `1920` image date; book publication is 1921 |
| Commons credit | Joseph Naayem is recorded as publisher of the book; the underlying image maker is not identified |
| Commons rights assertion | `PD-US-expired` / public-domain metadata; this is not a universal legal clearance |
| Primary master | `source_masters/ASY_concordat_council_yousef_emmanuel_ii_thomas_1920_hathitrust.jpg` |
| Master dimensions | `1344x2123`, RGB |
| Master SHA-256 | `ad3f489e9cb2b98f89afe72e831607c03b4440cac70f4fc0a9c6a3b47cf01151` |
| Source file SHA-1 from Commons API | `874962ad8d6fbb55cfebe4e59cc1ee9558e50c98` |

The caption printed beneath the archival plate identifies the subject as "His Beatitude the Chaldean, Patriarch of Babylon." The biographical dates and active office are cross-checked against [Catholic-Hierarchy's Yousef VI Emmanuel II Thomas entry](https://www.catholic-hierarchy.org/bishop/bthomg.html), which records birth on 8 August 1852, selection and confirmation as Patriarch of Babylon in 1900, and death on 21 July 1947.

## Crop and preview evidence

| Item | Value |
|---|---|
| Exact crop | `source_crops/ASY_concordat_council_yousef_emmanuel_ii_thomas_1920_exact_crop.png` |
| Crop rectangle | `(left=217, top=250, right=1127, bottom=1475)` in decoded master pixels |
| Crop dimensions | `910x1225` (exact `26:35` portrait ratio) |
| Crop SHA-256 | `d93040eb00bc2ddfe26223fabcab64efb5391a521876d6b6199d84bf43ace4ba` |
| Equality record | `crop_metadata/ASY_concordat_council_yousef_emmanuel_ii_thomas_1920_exact_crop.json` |
| Equality verdict | Pillow decoded-pixel equality `true`; master and crop RGBA SHA-256 values match in the JSON evidence |
| Deterministic preview | `processed_png/ASY_concordat_council_yousef_emmanuel_ii_thomas_156x210_source_placeholder.png` |
| Preview dimensions | `156x210`, RGB |
| Preview SHA-256 | `381f35369c7a25bdfb4b809b7f947ccd03752b61ffbd086fc29c4e456ba97711` |
| Preview processing record | `crop_metadata/ASY_concordat_council_yousef_emmanuel_ii_thomas_156x210_processing.json` |
| Processing | Pillow `ImageOps.fit`, `Image.Resampling.LANCZOS`, `centering=(0.5, 0.5)`, `bleed=0`, with no enhancement, recolouring, retouching, or alpha conversion |
| DDS | Not created; source-only work stops before conversion and runtime wiring |

The portrait crop is a faithful source placeholder showing the head, shoulders, vestments, medals, and hat visible in the archival plate. It is not a repaint or style replacement.

## Alternative retained for comparison

`source_masters/ASY_concordat_council_yousef_emmanuel_ii_thomas_1925_commons.jpg` is the Commons file [Mar Emmanuel II.jpg](https://commons.wikimedia.org/wiki/File:Mar_Emmanuel_II.jpg), described as a 1925 photograph. It is visually strong but has an unknown author and a Commons `PD-old` assertion based on an "own work" upload, so it remains an unselected `needs_user_review` alternative. It is `544x800`, RGB, SHA-256 `626ead387e45ef1f1c5b334166940d466ea72ec9ae08c40f99d2d23a242226be`. The comparison sheet is `review/ASY_yousef_emmanuel_ii_thomas_source_candidates_contact_sheet.png` and is evidence only.

The lower-resolution [Yousef Emmanuel II Thomas.jpg](https://commons.wikimedia.org/wiki/File:Yousef_Emmanuel_II_Thomas.jpg) (Gallica 1914 credit) and [Jose VI Manuel II.jpg](https://commons.wikimedia.org/wiki/File:Jos%C3%A9_VI_Manuel_II.jpg) (anonymous Iraq public-domain assertion) were reviewed but not retained as primary candidates because their small/oval scans lose materially more facial and clothing detail.

## Ownership and collision scan

No exact `Yousef VI`, `Yousef Emmanuel`, `Emmanuel II Thomas`, `Mar Emmanuel II`, or `Patriarch of Babylon` owner was found in the current Chaos Redux `common`, `history`, `gfx`, `interface`, or `localisation` trees. The same exact-name scan found no match in the checked vanilla Hearts of Iron IV and Kaiserreich reference trees. This is a source-package collision check, not permission to wire the portrait.

## Parent decision required

The parent should independently accept or reject the candidate's rights chain and confirm whether a Chaldean Catholic patriarch belongs in the IW-058 Concordat Council roster. If accepted, the parent owns the runtime basename, DDS conversion, `.gfx`, character definition, and localisation wiring. Until that decision, keep `runtime_authorized=false` and `needs_user_review`.
