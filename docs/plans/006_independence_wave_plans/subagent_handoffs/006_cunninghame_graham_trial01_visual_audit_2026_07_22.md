# Event 006 Cunninghame Graham trial 01 visual audit

Date: 2026-07-22  
Auditor: `chaosx_generated_event_art` (read-only visual audit)  
Disposition: **FAIL / blocked; do not convert to DDS or wire**

## Scope and files inspected

Named package files:

- `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/northwestern_europe/source_masters/SCO/SCO_cunninghame_graham_rijksmuseum.jpg`
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/scotland_civic/manifest.md`
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/scotland_civic/imagegen_sources/SCO_cunninghame_graham_hoi4_trial_01.png`
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/scotland_civic/processed_png/SCO_cunninghame_graham_hoi4_trial_01.png`

Canonical leader reference family inspected:

- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/README.md`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/CATALOG.md`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/contact_sheet.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/afg_mohammed_zahir_shah.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/africa_generic_1.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/den_thorvald_stauning.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/eth_haile_selassie.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/fin_carl_mannerheim.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/ice_sveinn_bjornsson.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/ire_eamon_de_valera.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/lux_charlotte.png`

No other project, runtime, GFX, gameplay, localisation, manifest, or skill files were edited. The offline Paradox wiki core pages required by `AGENTS.md` were loaded; no engine/script behavior was changed by this audit.

## File and provenance checks

- Source JPEG decodes as RGB `3846x4852`; SHA-256 matches the package manifest (`5d646596028a8a069651207e2058e8b59bdf7276d28921fd2a1ddefe2ff7abe7`).
- ImageGen master decodes as RGB `1080x1457`; SHA-256 matches the manifest (`bd291f5cfd259b11f735200aef53d6287cea46fa78a76744ba3ca3c8bb9a95aa`).
- Native review PNG decodes as RGB/opaque `156x210`; SHA-256 matches the manifest (`3ec22e6e17bf88f3a4e52d490f0aafc96bc6efe82b5bcbe96d538ce5e37556cb`).
- The native PNG is a deterministic crop/resize of the ImageGen master as described in the manifest (the independent in-memory Lanczos check differed only by <=3 channel values).
- The package manifest identifies Rijksmuseum object `RP-F-2001-7-67-30`, Alexander Bassano, circa 1881–1891, public-domain/CC0 access, and records the source path, dimensions, and hash. This is adequate provenance traceability for the candidate, although the direct public URL is only delegated to the uninspected upstream source manifest.
- No DDS is present; the package is explicitly `review_candidate_not_wired`, so this is a review-state limitation rather than a missing runtime conversion to overlook.

## Visual criteria

| Criterion | Verdict | Evidence |
| --- | --- | --- |
| Same-person likeness | **FAIL** | The broad identity cues survive (long straight nose, direct eyes, high wavy hair, full curled moustache, pointed beard, high collar/cravat), but ImageGen has reconstructed the real face: eye shape/gaze, facial proportions, hair volume, moustache/beard geometry, and skin/feature rendering are materially changed from the archival source. Under the event-assets portrait gate, this is not acceptance-grade identity preservation and cannot be rescued by the otherwise plausible resemblance. |
| Source-age fidelity | **PASS visually** | The output reads as a young adult in the same apparent circa-1881–1891 age band as the source; it does not age him to the 1936 start or de-age him into a modern-looking subject. This does not override the source-mode failure. |
| Male-only compliance | **PASS** | One male subject only; no female or additional person appears in either generated view or the native crop. |
| Head-and-shoulders crop | **PASS** | Native output is exactly `156x210`, centered on the head and shoulders with the jacket/waistcoat and collar retained; no album page, handwriting, border, or neighboring image remains. |
| Vanilla HOI4 painted style (full master) | **PASS visually** | The full master uses a quiet pale painted background, controlled period clothing, readable silhouette, subdued contrast, and restrained painterly texture matching the leader family’s visual direction. It is still an ImageGen reconstruction of a real face, which is disallowed independently of style quality. |
| Vanilla HOI4 painted style (native `156x210`) | **PASS visually** | At native size the face, beard, collar, and shoulders remain legible and the pale background/portrait framing match the canonical `156x210` leader family. No text, watermark, UI artifact, or modern prop is visible. |
| No invented culturally generic/fantasy features | **PASS** | The edit retains plain late-19th-century Western civilian dress from the source and adds no tartan, pseudo-Celtic motif, sacred object, uniform insignia, flag, fantasy element, stereotype, or meme treatment. |
| Rights/source traceability | **PASS with residual risk** | Rijksmuseum object/artist/date/CC0 basis plus source path, dimensions, and matching hash are recorded in the manifest. A direct link is not repeated in this package manifest, so the upstream source-manifest entry should remain available for durable provenance. |

## Blocking finding

This is a grounded real person in a plausibly historical Scottish polity. The package manifest explicitly calls the candidate an **“identity-preserving ImageGen edit”** and stores an ImageGen master. `chaos-redux-event-assets` requires the unchanged attributed source master followed by a deterministic, identity-preserving HOI4 finish for real people; it explicitly forbids using ImageGen to reconstruct, stylize, beautify, or fill a real face. The output therefore fails the portrait source-mode gate even though its crop, age band, male-only presentation, style direction, and provenance are otherwise usable.

Do not create a DDS, register `GFX_portrait_SCO_independence_wave_civic_convention`, or treat this PNG as a runtime portrait. The accepted path is a new deterministic local HOI4 painted finish from the unchanged Rijksmuseum source master, followed by a fresh likeness audit. Do not use this generated face as a fallback for Scotland’s unresolved territorial-command portrait.

## Residual risks and handoff

- Identity acceptance is unresolved and fail-closed; visual plausibility is not sufficient to authorize a generated real-person likeness.
- No runtime DDS, `.gfx` registration, or final sprite handoff was audited because the candidate is not eligible for conversion/wiring in its current form.
- The source provenance claim is strong (Rijksmuseum object id, artist, date band, CC0, path/hash), but durable documentation should retain the direct Rijksmuseum/IIIF/persistent-handle URL from the upstream source record.
- The parent agent should keep Scotland’s civic portrait status blocked until a deterministic source-derived HOI4 finish passes an independent same-person review at both full and `156x210` size.

