# Event 014 GUI, Animation, and Portrait Manifest

Status: complete from measured final outputs.

## Source policy

- All new sources: built-in `image_gen`.
- Retained one-use sources: the three explicitly accepted Event 014 eight-frame packages, copied with hashes and provenance.
- Both leader portrait packages use complete independently generated frame sequences; their stale calm source starts were replaced.
- No real atrocity photographs or real-person likenesses.

## Final inventory

The package contains:

- 26 exact static GUI PNG/DDS pairs and 26 two-layer OpenRaster masters;
- 12 non-portrait animation packages built from 114 distinct source frames, each with processed frames, static fallback, horizontal PNG/DDS sheet, GIF, contact sheet, manifest, and per-frame hash inventory;
- one 12-frame ordinary revealed Hannibal Lecter portrait package with a progressive skull-licking action;
- one 16-frame transformed portrait package with a separate inhuman claw/jaw/lunge/recoil loop;
- 104 runtime files across the static GUI, non-portrait animation, and portrait surfaces.

The machine-checked runtime inventory and per-file SHA-256 hashes are recorded in `validation/final_inventory.tsv`. Exact GFX identifiers, paths, frame counts, rates, and gates are recorded in `validation/gfx_handoff.tsv`.

Supporting proof:

- static GUI hashes and native text-safe review: `validation/static_gui_inventory.tsv` and `validation/static_gui_text_safe_native_contact.png`;
- non-portrait runtime hashes: `validation/nonportrait_animation_inventory.tsv`;
- per-animation source/processed hashes and review files inside each animation package;
- portrait manifests, validation, hashes, source/final contacts, and GIFs inside `animations/leader_CBL_hannibal/` and `animations/leader_ZZZ_hannibal_wendigo/`.

All runtime DDS files use one-image-level uncompressed 32-bit BGRA. Runtime PNG/DDS payloads match the documented package finals. The early and network surfaces contain no visible Hannibal Lecter face, title, unique silhouette, or transformed symbol. The transformed package contains no antlers, horns, runes, regalia, feathers, sacred motif, or living-cultural claim.
