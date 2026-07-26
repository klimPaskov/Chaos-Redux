# IW-173 HAW Samuel Wilder King source manifest

## Status

`source_ready_pending_portrait_pipeline` / `not_runtime_promoted`.

This is a grounded real-person source package for Event 006 IW-173 HAW only.
No gameplay, character, localisation, `.gfx`, advisor, commander, operative, dossier, DDS, or runtime file was changed.

## Candidate and accepted consumer boundary

- **Identity:** Samuel Wilder King (17 December 1886 – 24 March 1959).
- **Gender presentation:** male.
- **Place and role evidence:** born in Honolulu, Territory/Kingdom of Hawaiʻi; U.S. House of Representatives identifies him as a Delegate from the Territory of Hawaii for the 74th through 77th Congresses, January 3, 1935–January 3, 1943.
- **1936 fit:** he was the sitting territorial delegate during the 1936 package date, an authentic provisional territorial-government consumer rather than a generic or invented officeholder.
- **Grounded source mode:** `grounded_source_only`; unchanged attributed archival photograph.
- **Proposed consumer:** one full-size HAW civic/territorial-delegate or country-leader portrait after the parent explicitly accepts the identity and name mapping.
- **Not authorized:** do not automatically replace the vanilla David Kalakaua Kawananakoa roster entry, create an advisor or dossier icon, create `_small`, commander, or operative consumers, or use the image outside IW-173 HAW.

## Source provenance and rights

- **Canonical file record:** <https://commons.wikimedia.org/wiki/File:Samuel_Wilder_King_(PP-74-9-002).jpg>.
- **Canonical media URL:** <https://upload.wikimedia.org/wikipedia/commons/b/b5/Samuel_Wilder_King_%28PP-74-9-002%29.jpg>.
- **Retrieval URL used:** <https://i0.wp.com/upload.wikimedia.org/wikipedia/commons/b/b5/Samuel_Wilder_King_%28PP-74-9-002%29.jpg>.
- **Archive source and call number:** Hawaiʻi State Archives, PP-74-9-002, credited by the Commons record.
- **Author:** unknown.
- **Source date:** Commons records `between 1935 and 1943`; this brackets 1936 and is the best available date range.
- **Rights evidence:** the Commons record applies `PD-US-no notice` and states that the work was published in the United States between 1931 and 1977 without a copyright notice.
- **License interpretation:** this is a U.S. public-domain basis, not a Creative Commons grant, and attribution is not required by the Commons template.
- **Archive policy caveat:** Hawaiʻi State Archives public-use rules describe access and reproduction procedures but do not provide an image-specific licence for PP-74-9-002; retain the Commons public-domain rationale and call number with the source.
- **Production-safety disposition:** source is suitable for the normal grounded real-person pipeline under the U.S. public-domain rationale, with the archive-policy and exact-date caveat recorded for parent/legal review.

## Identity and role evidence

- **Primary role record:** U.S. House History, Art & Archives, [KING, Samuel Wilder](https://history.house.gov/People/Detail/16344).
- The House record lists him as a Hawaii delegate in the 74th (1935–1937), 75th (1937–1939), 76th (1939–1941), and 77th (1941–1943) Congresses and supplies his Honolulu birth and 1886–1959 dates.
- The House extended biography identifies his Hawaiian family connection and his advocacy for Hawaiian territorial rights and statehood; the candidate is therefore an authentic institutional consumer for the 1936 HAW package.
- The Commons caption and House record identify the same Samuel Wilder King; no father/son or namesake collision was found.

## Retained files and hashes

| File | Purpose | Dimensions/mode | SHA-256 |
| --- | --- | --- | --- |
| `source_png/HAW_samuel_wilder_king_PP-74-9-002_original.jpg` | Unchanged research master downloaded from the canonical Wikimedia image via the i0 proxy | 826x1206 RGB JPEG | `cba16c7d7b3e0efdd36240ec945663947ad727e0536757ea7cbd72156b0dcde3` |
| `crop/HAW_samuel_wilder_king_head_shoulders.png` | Exact lossless head-and-shoulders source crop | 693x1055 RGB PNG | `f36cc6c4a02b44605dd01412a25b2e50996006239eeb3f95f162ce6e6e0130ea` |
| `crop/HAW_samuel_wilder_king_head_shoulders_crop.json` | Crop command and decoded-pixel equality proof | JSON | `a763a27886e1a835269c8a0e02f8ce126bec56e51ce22043649137b25c099615` |

The crop was created with `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py` version 1.0, using half-open source coordinates `[105, 80, 798, 1135]`.

The crop metadata records `status=exact_source_crop_verified`, `decoded_pixels_equal=true`, 731115 pixels, and matching RGBA master-rectangle/output hashes `29fa8ce7a34f3dd49304d8d560ef37158890bf7c7ea8931df3e0456d83095a5f`.

## Visual and crop suitability

The source is a single adult male in a period formal suit and tie with a clear head, neck, collar, and both shoulders.

The face retains readable hairline, brows, eyes, nose, mouth, jaw, ear, and cheek structure at source resolution.

The forehead is bright and partially clipped, and the background has archival grain and a few scratches; these are recorded risks, not a substitute for identity evidence.

The 826x1206 source provides more than five-times the target 156x210 portrait dimensions and is suitable for an explicit source-locked repaint followed by deterministic HOI4 processing.

## Ownership and duplicate-use audit

Exact and variant searches were run in current Chaos Redux and installed vanilla roots covering `common/characters`, `history/countries`, `gfx/leaders`, `interface`, and `localisation` for `Samuel Wilder King`, `Samuel_Wilder_King`, `Wilder King`, and `Samuel King`.

Both current and vanilla scans returned `NO_MATCH`.

The existing vanilla HAW consumer remains David Kalakaua Kawananakoa at `history/countries/HAW - Hawaii.txt:60-62` and the generic Asia leader sprite; this candidate is not an existing HAW character clone.

No runtime ownership or transfer guard exists because no current consumer owns Samuel Wilder King.

## Downstream gates still required

The parent must preserve the unchanged master and exact crop, perform a source-locked identity-preserving ImageGen repaint, process a full `156x210` candidate, and obtain an independent likeness/style/provenance audit before any DDS conversion or runtime wiring.

No final processed PNG, DDS, contact sheet, or `.gfx` definition is claimed in this research-only tranche.

## Alternatives and rejected paths

Joseph B. Poindexter is retained only as a research comparison at `research/alternate_joseph_b_poindexter_1921.jpg`; the 1921 *Men of Hawaii* book scan is public domain and high-resolution, but it is a 15-year-old pre-delegate image and does not provide the same 1936-period visual fit as King.

The prior David Kalakaua Kawananakoa 1925 source remains blocked on clipped facial planes and failed likeness review, and Digital Archives record `ark:70111/47Nx` remains rights-unclear; neither is reused here.
