# IW-173 HAW Kawananakoa sourced portrait handoff - retry 03

Date: 2026-07-26

Owner: Chaos Redux sourced visual asset subagent

## Outcome

No production-safe source was found. The Digital Archives of Hawaii record `ark:70111/47Nx` is an exact adult visual match and has ample source resolution, but its provenance is a Star-Bulletin negative with no capture date or photographer. The record and archive site provide no public-domain, Creative Commons, or other reuse licence; the site footer states all rights reserved. This fails the required ownership-clearance gate.

The prior 1925 Commons image remains blocked on likeness because facial planes are clipped and the previous source-locked trial failed independent review. I did not reuse it.

## Files created

- `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_26/hawaii_kawananakoa_source_retry_03/research/ark_70111_47Nx.0.jpeg` - unchanged research download, 8639x6311 RGB, SHA-256 `5BB8B1E9BBDA5397B87F329DE1B4D0B6CD07FB5FD7F5D751BAFD48D03B2BEDB3`.
- `.../metadata/ark_70111_47Nx_research.json` - exact record, provenance, dimensions, hash, and rights uncertainty.
- `.../research/archive_candidate_contact_sheet.jpg` - research-only comparison of the exact target candidate and neighbouring father records, SHA-256 `FC532249A905E08995D6DDBF488C5C67DFF954121C691E078EDA15A7F243596B`.
- `.../research/source_clearance.md` - bounded search, rights checks, candidate hashes, identity dispositions, and restart conditions.
- `.../manifest.md` - blocked manifest entry with source, provenance, licence status, era fit, paths, sprite disposition, and uncertainty.
- `.../gfx_handoff.md` - explicit no-runtime handoff; keep vanilla generic mapping.

## Validation and gates

- The exact target record and image URL were independently fetched from the Hawaii State Archives Digital Archives.
- The image was visually inspected at large source resolution; it shows an adult man at right with clear facial geometry and Princess Abigail at left.
- Neighbouring Digital Archives records were visually compared and rejected as the older father, David Kawananakoa (1868-1908), or unrelated group images.
- Rights pages were checked at <https://portal.ehawaii.gov/page/terms-of-use/>, <https://ags.hawaii.gov/archives/about-us/archives-research/public-use-of-archives/>, and <https://ags.hawaii.gov/administrative-rules/public-use-of-archives/>. None grants a blanket reuse licence for `47Nx`.
- No crop, ImageGen edit, deterministic processing, independent likeness audit, DDS conversion, `.gfx` edit, gameplay edit, or localisation edit was performed.

## Parent action

Mark this candidate **needs_user_review / blocked** unless written permission or a clear image-specific public-domain/licence statement is obtained. If clearance arrives, restart from the unchanged source and rerun every required gate before any runtime promotion. Until then, leave `GFX_portrait_David_Kalakaua_Kawananakoa` mapped to the vanilla generic HAW portrait.

No simplification was made; the requested real-leader portrait is incomplete because no defensible rights-cleared adult source exists.
