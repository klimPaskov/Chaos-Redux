# Event 014 CBE-CBH warlord portrait image-generation handoff

Date: 2026-07-15
Owner: `/root/event014_portraits_efgh`
Mode: patch-capable asset production
Status: complete for the bounded CBE-CBH portrait package

## Delivered result

Regenerated the complete 28-portrait CBE-CBH warlord set: CBE, CBF, CBG, and CBH across Europe/default, Africa, Asia, Middle East, North America, South America, and Oceania. Every portrait is a separate fictional built-in image-generation output with a unique bald or hairless warlord, distinct anatomy and field clothing, and its own close-up macabre but non-graphic action.

The exact existing filenames were preserved. Each accepted source master was copied into the package, cropped and processed to an opaque 156x210 PNG, converted to an uncompressed 32-bit BGRA DDS, and placed over the corresponding live texture in `gfx/leaders/014_cannibalism/`.

Twenty-seven safe prompts succeeded on their first accepted wording. CBF Africa required one softer retry and succeeded on attempt two. A separate exploratory prompt before the safe pass was blocked and produced no file. No local artwork, sourced-photo fallback, procedural substitute, or reused portrait was used.

## Changed files and surfaces

- Replaced 28 source masters under `docs/assets/014_cannibalism/leader_portraits_refresh/cbe_cbh/source_png/`.
- Rebuilt 28 processed portraits under `docs/assets/014_cannibalism/leader_portraits_refresh/cbe_cbh/processed_png/`.
- Rebuilt 28 crop/processor records under `docs/assets/014_cannibalism/leader_portraits_refresh/cbe_cbh/metadata/`.
- Rebuilt 28 vanilla-reference comparison sheets under `docs/assets/014_cannibalism/leader_portraits_refresh/cbe_cbh/contact_sheets/reviews/`.
- Rebuilt the labelled source and processed contact sheets under `docs/assets/014_cannibalism/leader_portraits_refresh/cbe_cbh/contact_sheets/`.
- Added 28 verbatim accepted prompt files under `docs/assets/014_cannibalism/leader_portraits_refresh/cbe_cbh/prompts/generated/`.
- Replaced the action prompt matrix at `docs/assets/014_cannibalism/leader_portraits_refresh/cbe_cbh/prompts/prompt_matrix.md`.
- Added built-in generation provenance at `docs/assets/014_cannibalism/leader_portraits_refresh/cbe_cbh/source_generation_metadata.md`.
- Updated the package manifest, validation record, GFX handoff, and SHA-256 inventory in the same package.
- Replaced the 28 live DDS files matching `gfx/leaders/014_cannibalism/leader_CB[EFGH]_warlord*.dds`.

No gameplay script, `.gfx`, `.gui`, localisation, spreadsheet, or event specification file was edited. `interface/014_cannibalism.gfx` already contains all 32 required sprite registrations at lines 199-230, including the four base/Europe aliases.

## References and workflow

- Used the `imagegen`, `chaos-redux-event-assets`, and `chaos-redux-subagents` skills.
- Consulted the required offline HOI4 wiki core pages and portrait/interface pages before asset changes.
- Reviewed the Event 014 country package, portrait prompt, regional name pools, dynamic portrait selection, and existing GFX registrations.
- Used the canonical vanilla leader portraits `den_thorvald_stauning.png`, `ire_eamon_de_valera.png`, and `fin_carl_mannerheim.png` only as framing, value-range, and paint-finish references.
- Used `.tools/process_hoi4_portrait.py` version 2.0 with explicit in-bounds 26:35 crops and `.tools/convert_to_dds.py` for the live textures.

## Validation evidence

- 28 source PNGs, 28 accepted prompts, 28 processor records, 28 per-portrait review sheets, 28 processed PNGs, and 28 live DDS files are present with exact filename coverage.
- Source, processed, and DDS sets each have 28 unique SHA-256 hashes.
- All processed portraits are opaque 156x210 images.
- Every DDS has the expected legacy 124-byte header, 156x210 dimensions, uncompressed 32-bit BGRA masks, opaque alpha, one texture level, and a 131,168-byte file size.
- DDS payloads are pixel-identical to their corresponding processed PNGs.
- All 32 expected CBE-CBH sprite-to-texture registrations remain present in `interface/014_cannibalism.gfx`.
- The closest pair in the final 64-bit difference-hash audit remains 13 bits apart.
- Native-scale review of both aggregate contact sheets confirmed that all 28 are bald, visually distinct, HOI4-readable, and retain their individual action or prop after cropping. No prison, confinement, modern, actor-likeness, antler, sacred-motif, or copied-portrait imagery appears.

## Simplifications, omissions, and blockers

None. The bounded 28-portrait package is complete. No fallback or placeholder was used, and no asset remains unresolved.

## Parent integration note

The parent can retain the existing `.gfx` wiring unchanged and include this package directly in the Event 014 completion review. No git commit was created by this subagent.
