# Event 014 Static GUI and Non-Portrait Animation Manifest

Status: complete from measured final outputs.

## Source policy

- All new sources: built-in `image_gen`.
- Retained one-use sources: the three explicitly accepted Event 014 eight-frame packages, copied with hashes and provenance.
- No real atrocity photographs or real-person likenesses.

Leader portraits are maintained separately in `../leader_portraits_refresh/`, which is the authoritative source for the ordinary and transformed portrait packages.

## Final inventory

The package contains:

- 26 exact static GUI PNG/DDS pairs and 26 two-layer OpenRaster masters;
- 12 non-portrait animation packages built from 114 distinct source frames, each with processed frames, static fallback, horizontal PNG/DDS sheet, GIF, contact sheet, manifest, and per-frame hash inventory;
- 100 runtime files across the static GUI and non-portrait animation surfaces.

The machine-checked runtime inventory and per-file SHA-256 hashes are recorded in `validation/final_inventory.tsv`. Exact GFX identifiers, paths, frame counts, rates, and gates are recorded in `validation/gfx_handoff.tsv`.

Supporting proof:

- static GUI hashes and native text-safe review: `validation/static_gui_inventory.tsv` and `validation/static_gui_text_safe_native_contact.png`;
- non-portrait runtime hashes: `validation/nonportrait_animation_inventory.tsv`;
- per-animation source/processed hashes and review files inside each retained animation package.

All runtime DDS files use one-image-level uncompressed 32-bit BGRA. Runtime PNG/DDS payloads match the documented package finals. The early and network surfaces contain no visible Hannibal Lecter face, title, unique silhouette, or transformed symbol.
