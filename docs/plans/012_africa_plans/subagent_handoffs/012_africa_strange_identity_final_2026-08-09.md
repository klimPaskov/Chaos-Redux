# Event 012 strange-force identity final handoff — 2026-08-09

## Outcome

The eight strange-force units have complete static identity packages for technology, decision, focus/goal, large division emblem, and small division emblem surfaces. Existing bespoke vanilla-green large and on-map counters for the same eight units were re-audited and accepted from their prior counter manifests. No visual motif required regeneration after contact-sheet review.

The completed units are Gorilla Heavy Infantry, Pan Sappers, Stone Cohorts, Riverborn, Forest Giants, Oracle Recon, Disaster Wardens, and Plague Carriers.

## Changed or created asset evidence

- `docs/assets/012_africa/strange_force_identity_icons/manifest.json` records all 40 identity files, all 16 counter files, SHA-256 hashes, target dimensions, source/intermediate alpha information, DDS headers, decoded round trips, reference families, runtime paths, sprite IDs, and consumer crosswalks.
- `docs/assets/012_africa/strange_force_identity_icons/contact_sheet.png` is the processed identity overview.
- `docs/assets/012_africa/strange_force_identity_icons/contact_sheet_sources_roundtrip.png` compares source/alpha-intermediate and target identity families.
- `docs/assets/012_africa/strange_force_identity_icons/contact_sheet_emblems_roundtrip.png` compares emblem source, alpha-intermediate, and final target surfaces.
- `docs/assets/012_africa/strange_force_identity_icons/contact_sheet_counters_roundtrip.png` compares counter source, processed, and decoded DDS evidence.
- `docs/assets/012_africa/strange_force_identity_icons/prompts/identity_icon_prompt_record.md` documents reconstructed visual intent and explicitly records that original prompt files were unavailable.
- `docs/assets/012_africa/strange_force_identity_icons/gfx_handoff.md` provides exact runtime roots, sprite IDs, consumer IDs, and parent-owned registration boundaries.

## Validation evidence

Every identity DDS has the exact requested dimensions: technology 64x64, decision 32x32, focus 94x86, large emblem 76x42, and small emblem 30x12. Every identity DDS uses the validated legacy uncompressed BGRA 32-bit header with DDS magic, 124-byte header, 32-byte pixel format, RGB masks `0xff0000/0xff00/0xff`, alpha mask `0xff000000`, texture caps `0x1000`, and exact `128 + width*height*4` length. Decoded identity PNGs equal their exact-size processed PNGs pixel-for-pixel.

The sixteen existing counter DDS files decode pixel-for-pixel to the prior round-trip previews. Their per-unit manifests record the installed vanilla counter definition, two-frame canvas and frame order, sampled dominant green `(73,106,73)`, green range `(20,34,21)` through `(154,175,147)`, and neutral grayscale map family. The canonical reference contact sheets and individual references were inspected before accepting the counters.

Alpha-intermediate files retain source-scale canvases by design; exact target-size processed PNGs are the runtime inputs. Source PNGs are retained native ImageGen/chroma-key assets and all target alpha extrema are recorded in the manifest.

## Parent promotion roots

Promote or verify the runtime DDS files under these exact roots:

- `gfx/interface/technologies/012_africa/`
- `gfx/interface/decisions/012_africa/`
- `gfx/interface/goals/012_africa/`
- `gfx/interface/division_template_emblems/012_africa/`
- `gfx/interface/counters/divisions_large/`
- `gfx/interface/counters/divisions_small/`

Retain the review/manifests under `docs/assets/012_africa/strange_force_identity_icons/` and the prior counter evidence under `docs/assets/012_africa/models_3d/<unit>/counters/` until parent promotion is complete. These are the exact evidence roots referenced by the handoff.

## Parent-owned integration and remaining review

No gameplay, localisation, or `.gfx` file was edited. Parent must register the technology, decision, goal, and emblem sprites in the proposed `interface/012_africa_strange_force_icons.gfx` and validate consumer references. Existing counter registration remains in `interface/012_africa_strange_force_counters.gfx`.

Original provider prompt files were absent, so the prompt record is an audit reconstruction rather than provenance recovery. Focus and some decision/emblem sprites are reserved package surfaces with no current direct consumer; the parent should keep them registered only where the gameplay/UI integration requires them. Model/entity, audio, and final runtime acceptance remain parent-owned gates.

No simplification was made to the requested icon dimensions or DDS surfaces. The only explicit limitation is unavailable original prompt provenance and parent-owned final `.gfx` wiring.
