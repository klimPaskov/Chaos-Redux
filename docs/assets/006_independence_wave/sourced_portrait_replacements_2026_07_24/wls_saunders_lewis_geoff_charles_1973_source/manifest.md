# Saunders Lewis archival source package — Geoff Charles, 4 October 1973

Status: `needs_user_review`.

This package records a stronger, rights-clear identity source for the Event 6 Wales civic leader, but it is not an era-matched 1936 portrait. The source is an archival National Library of Wales photograph released on Wikimedia Commons under CC BY-SA 4.0. It is supplied only as an identity-geometry reference; no ImageGen result, deterministic PNG, DDS, GFX edit, or gameplay edit is included.

## Consumer

- Event: IW-002 / Wales independence wave.
- Stable character token: `WLS_independence_wave_national_council`.
- Stable sprite: `GFX_portrait_WLS_independence_wave_national_council`.
- Runtime target, if later admitted: `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_national_council.dds`.

## Selected source

| Field | Record |
| --- | --- |
| Subject | Saunders Lewis (John Saunders Lewis, 1893–1985), Welsh writer, nationalist, and Plaid Cymru leader |
| Source page | [Wikimedia Commons — File:Saunders Lewis (1520393).jpg](https://commons.wikimedia.org/wiki/File:Saunders_Lewis_(1520393).jpg) |
| Direct original used | [Wikimedia upload original](https://upload.wikimedia.org/wikipedia/commons/5/50/Saunders_Lewis_%281520393%29.jpg) |
| Archive record | [National Library of Wales IIIF manifest](https://iiif.llyfrgell.cymru/manifests/2.0/1520392/manifest.json); permalink [hdl:10107/1520392](http://hdl.handle.net/10107/1520392) |
| Archive / collection | National Library of Wales (Llyfrgell Genedlaethol Cymru) |
| Photographer | Geoff Charles (1909–2002) |
| Capture date | 4 October 1973 |
| Archive description | One of six black-and-white 35mm negatives in the NLW record; the selected Commons original is 1200×1828 pixels. |
| License | Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0). Attribution must name Geoff Charles and the National Library of Wales, link the source/license, and disclose modifications. |
| Source file | `source_masters/WLS_saunders_lewis_geoff_charles_1973_commons_1520393.jpg` |
| Source dimensions | 1200×1828 JPEG, unchanged after download |
| Source SHA-256 | `8cf79afdfc31b93a5ee3ba5a25432c39fad899c63ea3ba9b82ed1b9534c4b245` |

The source is an attributed archival photograph of the correct real person, with the ears, long narrow nose, mouth, jaw, hairline, and shoulder silhouette resolved far more clearly than the halftone 1916 Y Drych source. The direct frontal pose is useful for identity-preserving work, but the eyes are an elderly 1973 expression rather than the smaller, deep-set, asymmetrical 1936-era appearance requested by the likeness audit.

## Explicit source-pixel crop

The crop is a mechanical source-pixel extraction from the unchanged master. Coordinates use the source's top-left origin, with the right and bottom edges exclusive: `(x0, y0, x1, y1) = (20, 30, 1180, 1090)`. No repainting, retouching, sharpening, upscaling, colorization, or face synthesis was applied.

| Field | Record |
| --- | --- |
| Crop file | `source_crops/WLS_saunders_lewis_geoff_charles_1973_head_shoulders.png` |
| Crop box | `(20, 30, 1180, 1090)` |
| Crop dimensions | 1160×1060 RGB PNG |
| Crop content | Head, neck, tie, and both shoulder lines; hands and lower torso excluded |
| Crop SHA-256 | `dca92cd001d2db973c7bfb8b9881dcdd69f55dda6e88e9459bb31061aa15b1c9` |

## Era and likeness disposition

The scenario starts in 1936, while this capture is from 1973, when Lewis was approximately eighty years old. It therefore cannot be described as a period-matching 1936 portrait and must not be wired without explicit user approval of a later-life identity source and a controlled age reconstruction. The package is `needs_user_review`, not `approved_for_runtime`.

The source is still a stronger identity reference than the failed 1916 Y Drych trials because it supplies clean facial geometry and both shoulders at useful resolution. It does not, by itself, repair the prior likeness failure: the 1973 eye shape is broad and bright, and a later identity-preserving generation step would have to age the face toward 1936 without inventing a generic face. That step was intentionally not performed in this source-only handoff.

## Candidate review ledger

| Candidate | Disposition | Reason |
| --- | --- | --- |
| Geoff Charles / NLW, 4 Oct 1973, Commons 1520393 | `needs_user_review` | Clear CC BY-SA 4.0 provenance and strong facial resolution; postwar age/date mismatch for 1936. |
| *Y Drych*, 3 Feb 1916, NLW/Commons | Rejected for this retry | Rights basis is defensible, but trials 01 and 02 failed the independent likeness gate: halftone detail was too weak and the generated eyes became generic. Existing source remains in its prior package; it is not copied here. |
| Dr Gwent Jones photograph, October 1936 | Rejected / rights unclear | The caption in *The Story of Plaid Cymru* identifies the strongest era-matched composition, but the 1990 Plaid Cymru reprint states “All rights reserved” and no direct rights-cleared original was located. No image was copied. |
| 1960s People’s Collection Wales group photographs | Rejected | Noncommercial or unclear reuse terms and not a clean head-and-shoulders source. |
| 2007 Geograph plaque crop | Rejected | Modern memorial/plaque image, not a photograph of Lewis; explicitly outside the source rules. |

## Processing boundary

This source-only package stops after the immutable master and explicit crop. Do not infer a generated portrait or runtime DDS from the presence of these files. Future source-locked ImageGen, deterministic 156×210 processing, independent likeness audit, attribution/share-alike review, DDS conversion, and GFX wiring remain separate gates.
