# IW-043 CHU Gayaz Ishaki portrait independent visual/provenance audit v02

Audit date: 2026-08-03 (Europe/Kyiv).  Reviewer: independent Chaos Redux asset subagent (not the repaint producer).

This is an independent read-only audit of the existing source-to-candidate chain for the proposed `CHU_independence_wave_federal_presidium` full country-leader portrait.  It does not create DDS, edit `.gfx`, edit characters/gameplay, or promote the CHU consumer.  The overall package remains `needs_user_review` because the photographer and first-publication rights chain is unresolved.

## Scope and evidence inspected

The following files were opened at native resolution and the supplied review sheet was inspected at its native and 4x nearest-neighbour panels:

| Stage | Path | Native facts / SHA-256 |
| --- | --- | --- |
| Unchanged source master | `docs/assets/006_independence_wave/iw043_chu_portrait_source_research_2026_08_02/source_masters/gayaz_ishaki_book_plate.jpg` | 2361x3393 RGB; `e2cc555c9a6fb63f0707b77038195d41aafa1d01e6a9be584116f2582245803e` |
| Exact identity crop | `docs/assets/006_independence_wave/iw043_chu_portrait_source_research_2026_08_02/source_crops/gayaz_ishaki_book_plate_head_shoulders.png` | 2170x3050 RGB; `a276710b8816b218941040329ea34c8ca57b55f47b65c18998836f8f25fdef11` |
| Crop equality record | `docs/assets/006_independence_wave/iw043_chu_portrait_source_research_2026_08_02/source_metadata/gayaz_ishaki_book_plate_crop.json` | Pillow crop `(80,0,2250,3050)`; `decoded_pixels_equal: true`; master/output RGBA equality hash `b1d90ab0abb3cea11b8206ef228f10301d5d9c0585c2757a95dd584c1b271a1c` |
| Raw source-locked repaint | `docs/assets/006_independence_wave/iw043_chu_portrait_repaint_2026_08_03/repaints_raw/CHU_independence_wave_federal_presidium_hoi4_repaint_v1.png` | 1080x1456 RGB; `c0e57e15fee66fc6b8c83194f0dd71ce7d8d8016af338466096c321a1023825b` |
| Original-size repaint evidence | `docs/assets/006_independence_wave/iw043_chu_portrait_repaint_2026_08_03/repaints_processed/CHU_independence_wave_federal_presidium_hoi4_original_size_master.png` | 1080x1456; byte-identical to raw (`c0e57e15fee66fc6b8c83194f0dd71ce7d8d8016af338466096c321a1023825b`) |
| Deterministic candidate | `docs/assets/006_independence_wave/iw043_chu_portrait_repaint_2026_08_03/repaints_processed/portrait_CHU_independence_wave_federal_presidium_156x210_candidate.png` | 156x210 RGBA; alpha extrema 255/255; `8d6ac363e8b90a14d153c7648ec1bc09bcfb611c1cbd3d258a682216ac362a36` |
| Full-chain review sheet | `docs/assets/006_independence_wave/iw043_chu_portrait_repaint_2026_08_03/review/CHU_independence_wave_federal_presidium_full_chain_native_4x_review.png` | 1928x3666 RGB; `266e959a39816d2a4974301d3058c55681b22f153eb501893958096c1b4ee4b0`; native family panels plus 4x nearest-neighbour panels |

The review sheet includes the unchanged master, exact crop, raw repaint, candidate, and the two style references used by the prompt.  I also inspected the complete canonical leader reference folder under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/`: the 8 leader PNGs and its contact sheet.  All individual leader references are 156x210 RGBA.  The closest role/style comparisons in the chain are `den_thorvald_stauning.png` (`08732002182bdcb2bff3d78b142cc2b3d75adbdb29d4115f9e89ca5bdc6a21b6`) and `ire_eamon_de_valera.png` (`ff5f8689f1e8ea75bf88bea4c4a87dcf60518b1e062ea53be4a9ceff3509dcb0`).

## Separate gate findings

| Gate | Verdict | Independent finding |
| --- | --- | --- |
| Identity likeness | **PASS** | At native 156x210 and 4x, the repaint and candidate retain the identity-bearing side-parted hair and hairline, heavy dark moustache, three-quarter head direction, eyelid/squint asymmetry, eye spacing, nose bridge/tip, mouth and jaw contour, rounded cheek volume, neutral stern expression, visible ear, and source-visible collar/tie/suit.  The repaint is a real source-locked transformation rather than a raw resize or a generic replacement face.  Minor painterly smoothing and eye/skin colourization do not erase the source geometry; no beautification, symmetrization, age shift, hidden detail, medals, hat, or unsupported uniform/insignia is visible. |
| HOI4 leader style | **PASS** | The candidate is a readable head-and-shoulders 156x210 portrait with restrained gouache/oil brush planes, muted parchment/charcoal background, controlled contrast, face-first framing, and no frame, UI, watermark, or text.  The collar, tie, shoulders, and neutral studio background are coherent with the supplied Stauning/de Valera and wider canonical leader family.  Fully opaque candidate alpha is acceptable for this painted leader surface; there are no fringe or cutout defects to reject. |
| Provenance chain | **PASS as evidence-chain integrity** | Immutable master, exact Pillow crop, crop JSON equality proof, raw ImageGen output, byte-identical original-size copy, deterministic processor metadata/script hash, 156x210 candidate, prompt, style-reference hashes, full native/4x review sheet, package manifest, and source/role/ownership records are distinct and retained.  The raw and candidate paths are not conflated.  This verdict does not waive the separate rights gate below. |
| Role/date fit | **PASS with parent-owned scope caveat** | Package research identifies Muhammad Ayaz Ishaki/Gayaz Ishaki (1878–1954) as a Tatar journalist, author, publisher, and political organiser, including 1918 Idel-Ural State secretary-of-state and 1931 Independence Committee leadership; he was alive in the 1936 baseline.  Those facts support a civic-national/federal-presidium reading and the civilian suit/tie is role-compatible.  The primary book plate has no verified capture date, and the evidence does not prove a literal 1936 CHU appointment, Chuvash ethnicity, Bolgar descent, or military command.  The proposed fictional office transfer remains a parent-owned design decision. |
| Rights / attribution | **NEEDS_USER_REVIEW** | The retained Commons metadata and wikitext report `PD-old-70-1923` / public-domain status, unknown author, and source credit to Ahmet Kanlidere's 1997 *Reform within Islam* reproduction; the corroborating 1911 plate reports `PD-old` and unknown author.  However, the photographer, first-publication jurisdiction, and chain from later book scans to original negatives are not established.  Upload/revision timestamps are not image creation dates.  Preserve this status and obtain project owner rights sign-off; do not silently convert the candidate to a rights-cleared asset. |

Identity is a separate non-compensable gate: the PASS above is not being granted because of style quality.  Rights uncertainty also does not downgrade the observed likeness/style evidence; it blocks promotion independently.

## Chain and processing checks

- `source_metadata/gayaz_ishaki_book_plate_crop.json` records the required Pillow backend, exact decoded-pixel equality, and the half-open crop rectangle.  No ffmpeg/ImageMagick crop or retouch is used.
- The repaint prompt records the exact crop as the sole identity authority and the Stauning/de Valera files as style-only references.  The raw result preserves the civilian collar/tie/suit and does not borrow a reference face.
- `tools_normalize_156x210.py` performs only the documented `(0,0,1080,1454)` two-pixel lower trim, one Lanczos resize, and RGBA conversion to 156x210; it does not redraw the face, frame, paper, or insignia.
- The review sheet is producer-prepared evidence, but this audit is independent and inspected the underlying source/crop/raw/candidate/reference files directly at native and enlarged scales.  The sheet's labels contain harmless mojibake punctuation only; the visual panels and asset paths remain unambiguous.
- No final DDS exists.  The proposed runtime path `gfx/leaders/006_independence_wave/portrait_CHU_independence_wave_federal_presidium.dds` and sprite `GFX_portrait_CHU_independence_wave_federal_presidium` remain proposals in the package handoff, not live wiring.

## Disposition and parent handoff

Overall disposition: **`needs_user_review` — likeness/style/provenance evidence passes, but rights sign-off and the parent-owned fictional office assignment remain open.**

1. Keep the source master, exact crop, raw repaint, candidate, review sheet, metadata, prompt, and hashes immutable and in their current distinct paths.
2. Preserve the source package's `grounded_identity` / `grounded_source_only` classification and rerun the ownership preflight immediately before any runtime character/token is created.
3. Obtain explicit project-owner review of photographer and first-publication uncertainty.  If that review does not clear the chain, mark the portrait blocked rather than substituting a generated or generic person.
4. Only after rights clearance and parent role approval may the main agent independently decide whether to convert the approved candidate to DDS and wire the proposed sprite/runtime path.  This audit does not authorize either action.

No fallback, alternate face, generated officeholder, DDS, `.gfx` edit, character edit, gameplay edit, or CHU promotion was created or approved in this audit.
