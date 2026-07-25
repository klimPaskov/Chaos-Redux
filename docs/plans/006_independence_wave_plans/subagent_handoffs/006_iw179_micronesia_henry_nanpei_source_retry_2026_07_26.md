# IW-179 FSM Micronesia Henry Nanpei source-retry handoff

Status: **BLOCKED / no production-safe sourced real male portrait**.

## Scope and runtime boundary

This handoff covers only sourced visual research for `FSM_independence_wave_inter_island_congress_chair` / `GFX_portrait_FSM_independence_wave_inter_island_congress_chair`. The current fictional Elias Kihleng portrait remains untouched. No character, localisation, interface, GFX, event, gameplay, ImageGen, crop, processed PNG, DDS, contact sheet, or runtime file changed.

## Research result

The requested Micronesian Seminar record PN01036 is a strong identity and date lead, but its image is unavailable. The closest visible Henry Nanpei object is a small thumbnail whose attribution is promising but whose source-resolution and rights chain are not sufficient for the real-person portrait gate. No other researched candidate cleared identity, era fit, and reuse evidence together.

### 1. Preferred lead: Micronesian Seminar PN01036 — blocked at source access

- **Subject / identity:** Henry Nanpei.
- **Repository:** Micronesian Seminar, Pohnpei Islands Collection.
- **Catalog date:** c1920.
- **Catalog classification:** Black & White Photo, Photograph, **Not Restricted**.
- **Catalog result:** [PN01036 result record](https://micsem.org/library/search-photos-results?region=Pohnpei&subject=Henry%20Nanpei).
- **Observed source state:** the result serves `https://micronesian.matrixmarketers.com/library_img/photo/no_image.gif` instead of an image. The result HTML still identifies the object as “Henry Nanpei … Pohnpei Islands Collection. Pohnpei. c1920. [PN01036]”.
- **Source file / hash:** none; no image bytes were available to preserve.
- **Era fit:** potentially strong for the 1936 runtime, but untestable without the object.
- **Rights uncertainty:** “Not Restricted” is catalog metadata, not an explicit downloadable license statement. The repository's site footer also states © 2010–2019 all rights reserved. No production use is permitted while the image and rights wording remain unresolved.
- **Disposition:** **BLOCKED**. Do not substitute the no-image placeholder or invent a crop.

### 2. Closest visible lead: Micronesian Seminar HF01005 — thumbnail-only and rights-ambiguous

- **Subject / identity:** “Portrait of Henry Nanpei”.
- **Repository:** Micronesian Seminar, Hawley Family Collection.
- **Catalog date:** 1933.
- **Catalog classification:** Black & White Photo, Digital, Photograph, **Not Restricted**.
- **Catalog result:** [HF01005 result within the Nanpei search](https://micsem.org/library/search-photos-results?region=Pohnpei&eras=japanese&subject=Nanpei).
- **Only retrievable image:** [HF01005 thumbnail](https://micsem.org/library_img/photo/thumbnails/hf/01/hf_01_005_tmb.jpg).
- **Downloaded evidence:** JPEG, 120×168 RGB, SHA-256 `9f3e4ee25e6294dea68cb042593a257bdcf71d195dbf5ff979e33036f92861bc`.
- **Source-resolution problem:** the 120×168 thumbnail is not sufficient for the unchanged-source exact-pixel crop plus source-locked identity-preserving repaint and independent likeness audit required for a 156×210 leader portrait. All tested original/full-size path families returned 404; no larger source was discoverable from the live catalog result.
- **Rights uncertainty:** the record says “Not Restricted,” but the same site footer states © 2010–2019 all rights reserved. No explicit asset license or reuse permission was found. Treat the catalog label as a lead for rights clarification, not as a final license grant.
- **Era fit:** strong (1933, immediately before the event's 1936 world state).
- **Disposition:** **BLOCKED / needs repository-provided original and explicit reuse confirmation**. Do not upscale or feed the thumbnail to ImageGen as a grounded-source substitute.

Other visible Nanpei search results (COM01038, COM01071, HF01001/HF01003/HF01004, PM01028, PN01002, PN01020) were not promoted: they are family/group/unclear framing or lacked a retrievable production-sized image. The exact requested PN01036 record remains the priority if Micronesian Seminar can supply the scan.

### 3. Rejected alternative: UHM item 6754 — “native chief, Mok”

- **Object:** [University of Hawaiʻi at Mānoa Digital Collections item 6754](https://digital.library.manoa.hawaii.edu/items/show/6754).
- **Caption identity:** “The native chief, Mok,” at Ulithi Atoll, Western Caroline Islands; Pfc. R. Estes, U.S. Marine Corps; dated 12 December 1944.
- **Original files:** [front image](https://digital.library.manoa.hawaii.edu/files/original/2d812e718520908ae0fbd63a56da5ecf.jpg) (792×665 RGB; SHA-256 `41a2c9a39f2d2e040cf68f861c01ac3fa4310ddeb9557820802e2f79c78ae247`) and [caption card](https://digital.library.manoa.hawaii.edu/files/original/82a29f8a5f30702954e65f7858bd4189.jpg) (662×792 RGB; SHA-256 `8b3035d251bdc3f16b02ff27c9e99f717e09897b834e7870f53bdbde6d106be4`).
- **Provenance:** U.S. Marine Corps / Pfc. R. Estes is a plausible U.S. government source, but the repository gives no explicit public-domain statement on the object. UHM's [copyright policy](https://manoa.hawaii.edu/library/research/scholarly-communication/repositories/policies-guidelines/copyright-policy/) warns that collection materials remain subject to copyright and that users must obtain permission where required.
- **Identity and era failure:** only the one-word caption “Mok” is supplied; no full name, birth/death dates, or 1936 role continuity was found. The photograph is four years after the target event date and shows an adult chief in a wartime aircraft context, not a documented 1936 civic leader. The image is also a contextual scene rather than a clean, attributable head-and-shoulders portrait.
- **Disposition:** **REJECTED** for IW-179. No crop, repaint, PNG, or DDS was produced.

## Gate outcome

| Gate | PN01036 | HF01005 | UHM “Mok” |
|---|---|---|---|
| Attributable identity | Catalog identity, image unavailable | Catalog identity, thumbnail visible | One-word caption only |
| Source bytes | **No image** | 120×168 thumbnail only | 792×665 original |
| Date / era fit | c1920 (good if verified) | 1933 (strong) | 1944 (weak for 1936) |
| Reuse basis | “Not Restricted” metadata; unresolved | “Not Restricted” metadata; unresolved | U.S. Marine Corps provenance; no explicit PD statement |
| Exact crop + JSON equality | Not possible | Not production-safe at thumbnail size | Identity/era gate fails |
| Package status | **BLOCKED** | **BLOCKED / needs source clearance** | **REJECTED** |

## Required next input

The package can resume only when one of the following is supplied:

1. A full-resolution PN01036 scan from Micronesian Seminar (or an equivalent attributable Henry Nanpei original) together with written reuse permission or an explicit license; or
2. A different named adult male Pohnpeian/Carolinian civic or traditional figure with an attributable archival portrait, documented date near 1936, and a defensible reuse basis.

After that input arrives, preserve the unchanged source, run `extract_portrait_source_crop.py` with exact crop coordinates and decoded-pixel equality JSON, obtain an independent likeness/style/provenance PASS, then process the 156×210 leader PNG and repository-standard DDS. Until then, leave the current fictional Elias Kihleng asset and runtime wiring unchanged.

## Outputs

- **No accepted source package:** no source copy, crop, processed PNG, DDS, contact sheet, or `gfx_handoff.md` was created because all candidates failed at least one mandatory identity, source-resolution, era-fit, or rights gate.
- **Research evidence retained:** URLs, dimensions, hashes, and failure reasons are recorded above so the parent agent can resume without guessing.

