# IW-173 HAW Samuel Wilder King source manifest

## Status

`portrait_audit_pass_runtime_promoted_additive_role`.

This is a grounded real-person source package for Event 006 IW-173 HAW only.
The additive Event 006 HAW character, localisation, `.gfx`, and DDS consumer are wired after the independent v45 portrait PASS. The vanilla David Kalakaua Kawananakoa ruling roster remains untouched. No advisor, commander, operative, dossier, or `_small` surface was created.

## Accepted consumer boundary

- **Identity:** Samuel Wilder King (17 December 1886 – 24 March 1959).
- **Gender presentation:** male.
- **Place and role evidence:** born in Honolulu, Territory/Kingdom of Hawaiʻi; U.S. House of Representatives identifies him as a Delegate from the Territory of Hawaii for the 74th through 77th Congresses, January 3, 1935–January 3, 1943.
- **1936 fit:** he was the sitting territorial delegate during the 1936 package date, an authentic provisional territorial-government consumer rather than a generic or invented officeholder.
- **Grounded source mode:** `grounded_source_only`; unchanged attributed archival photograph.
- **Accepted consumer:** `HAW_independence_wave_territorial_delegate` as an additive non-ruling civilian-large role, with runtime sprite `GFX_portrait_HAW_independence_wave_territorial_delegate` and DDS `gfx/leaders/006_independence_wave/portrait_HAW_independence_wave_territorial_delegate.dds`.
- **Not authorized:** do not automatically replace the vanilla David Kalakaua Kawananakoa roster entry, create an advisor or dossier icon, create `_small`, commander, or operative consumers, or use the image outside IW-173 HAW.

## Source provenance and rights

- **Canonical file record:** <https://commons.wikimedia.org/wiki/File:Samuel_Wilder_King_(PP-74-9-002).jpg>.
- **Canonical media URL:** <https://upload.wikimedia.org/wikipedia/commons/b/b5/Samuel_Wilder_King_%28PP-74-9-002%29.jpg>.
- **Retrieval URL used:** <https://i0.wp.com/upload.wikimedia.org/wikipedia/commons/b/b5/Samuel_Wilder_King_%28PP-74-9-002%29.jpg>.
- **Archive source and call number:** Hawaiʻi State Archives, PP-74-9-002, credited by the Commons record.
- **Historical archive record URL:** <http://gallery.hawaii.gov/gallery2/main.php?g2_itemId=56613> (the legacy gallery endpoint was unavailable during retrieval, so the Commons record and call number are retained as the stable citation).
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
| `imagegen_results/HAW_samuel_wilder_king_identity_preserve.png` | Source-locked HOI4-style ImageGen repaint master retained before deterministic normalization | 1018x1545 RGB PNG | `1e4c62368cb92103d1666991b8dcc087051aa19008ca45bec756a6d99ba76da6` |
| `processed_png/portrait_HAW_samuel_wilder_king.png` | Deterministic full-size HOI4 leader portrait candidate | 156x210 RGBA PNG | `25f4be028f9e68b17fc51afd19a0d3ee9400c8a7a23612e46f9ef8f397600285` |
| `metadata/HAW_samuel_wilder_king_manual_export_v1.json` | Current task-specific export, source-lock, reference, decoded-pixel, and review-sheet evidence | JSON | `output_file_sha256=25f4be028f9e68b17fc51afd19a0d3ee9400c8a7a23612e46f9ef8f397600285` |
| `tools/normalize_leader_portrait.py` | Reproducible 156x210 crop-grade export script | Python | `e437e1d26e73d612dc6d20aec8abc6d1a378ebddd06b144d42cf0345322bbf9e` |
| `tools/create_review_sheet.py` | Reproducible native-context and 4x nearest-neighbour review-sheet script | Python | retained beside the package |
| `review_sheets/HAW_samuel_wilder_king_source_raw_candidate_references_4x.png` | Unchanged source/crop/raw context plus exact 4x candidate and vanilla leader references | review PNG | `e8ef39ee88184eda8899903b2fba2db390ebdcbc6d7aa781cfcd83ffa56ff8c1` |
| `docs/assets/portraits/006_independence_wave/portrait_HAW_independence_wave_territorial_delegate.png` | Durable lossless PNG copy of the immutable archival source master for the ComfyUI input | 826x1206 RGB PNG | `64a6049946e3603e0a67ee14950f87253dd651a9dce6eedfeb8f6d4ff5833e22` |
| `docs/assets/portraits/006_independence_wave/portrait_HAW_independence_wave_territorial_delegate.txt` | Durable one-line ComfyUI/ImageGen prompt paired to the runtime DDS basename | UTF-8 text | retained in the flat portrait shelf |
| `prompts/HAW_samuel_wilder_king_identity_preserve_imagegen.md` | Identity-preserving ImageGen prompt and generation record | Markdown | evidence record |

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

The runtime consumer is owned by the IW-173 HAW package only; the setup and cleanup effects recruit and retire the additive Event 006 role without replacing or retiring any vanilla HAW leader.

## Source and runtime evidence

The unchanged master and exact crop remain preserved, the raw repaint and normalized candidate remain in the event evidence workspace, and the archival-source PNG and matching prompt remain in the durable portrait shelf. The independent v46 likeness/style/provenance audit passed before the DDS conversion and runtime wiring; its package-local export metadata, all-source review sheet, durable pair, and runtime basename alignment are retained as evidence.

The processed PNG is the approved source candidate for the runtime DDS, and the `.gfx`, character, localisation, and DDS chain is now wired. The review sheet remains evidence and is not a runtime asset.

## Alternatives and rejected paths

Joseph B. Poindexter is retained only as a research comparison at `research/alternate_joseph_b_poindexter_1921.jpg`; the 1921 *Men of Hawaii* book scan is public domain and high-resolution, but it is a 15-year-old pre-delegate image and does not provide the same 1936-period visual fit as King.

The prior David Kalakaua Kawananakoa 1925 source remains blocked on clipped facial planes and failed likeness review, and Digital Archives record `ark:70111/47Nx` remains rights-unclear; neither is reused here.
