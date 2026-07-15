# Event 014 Non-Portrait Animation Manifest

Twelve non-portrait UI animation packages are final and wired at the stems frozen in `docs/plans/014_cannibalism_plans/014_gui_dimension_ledger.md`:

- `cannibalism_early_warning_seal` — 8 frames at 64x64, 8 FPS;
- `cannibalism_cult_cohesion_emblem` — 8 frames at 64x64, 8 FPS;
- `cannibalism_network_threads` — 12 frames at 824x120, 8 FPS;
- `cannibalism_island_alert` — 8 frames at 64x64, 8 FPS;
- `cannibalism_selected_target_overlay` — 6 frames at 374x64, 6 FPS;
- `cannibalism_critical_larder_glow` — 8 frames at 64x64, 8 FPS;
- `cannibalism_frenzy_border` — 8 frames at 142x54, 8 FPS;
- `cannibalism_warlord_route_emblem` — 8 frames at 94x86, 8 FPS;
- `cannibalism_unification_seal` — 12 frames at 94x86, 8 FPS;
- `cannibalism_ordinary_terminal_frame` — 12 frames at 438x40, 8 FPS;
- `cannibalism_wendigo_anchor_pulse` — 12 frames at 64x64, 8 FPS;
- `cannibalism_wendigo_terminal_frame` — 12 frames at 438x40, 8 FPS.

Every package retains separate generated or accepted semantic source frames, exact processed frames, a horizontal PNG/DDS sheet, a PNG/DDS static fallback, an animated GIF preview, a processed-frame contact sheet, a per-frame hash inventory, and a package manifest. All source and processed frame hashes are unique within their package. The final DDS files are uncompressed one-image-level 32-bit BGRA and the runtime copies are byte-identical to the package finals.

Cross-package output hashes and the exact GFX handoff live in:

- `../validation/nonportrait_animation_inventory.tsv`
- `../validation/gfx_handoff_nonportrait.tsv`

The retained semantic animation families are each used exactly once. The remaining families were independently generated as real source-frame sequences. No final animation is a transform-only derivation of one still.
