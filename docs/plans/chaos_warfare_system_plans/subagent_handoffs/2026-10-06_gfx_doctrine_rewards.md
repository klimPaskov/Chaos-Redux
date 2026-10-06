# Chaos Warfare mastery reward art

Disposition: implemented, parent accepted under the graphics-repair task.
Four existing 1000x88 reward strips retain ten 100x88 frames each, with five colour rewards followed by their five matching greyscale states.
Twenty original equipment objects replace opaque plaques, full map tiles and other backgrounds that covered the native mastery medallion.
The objects remain isolated and inset so the underlying laurel/state frame can show through.
The parent reviewed all four strips at native and four-times size.
One detached fragment above the Toxic Armor fourth vehicle was confirmed as exterior residue and removed only from the processed source mask, preserving raw source art.
The parent approved the refreshed strip before DDS promotion.
Every grey state retains its colour counterpart's alpha and placement, and final DDS decoding matches the processed strips exactly.

Sources, prompts and per-object previews remain under `docs/assets/chaos_warfare_system/2026-10-06_gfx_primary/` while the larger asset package is active.
Reviewed sheets are the four `contact_sheets/cbrn_doctrine_*_reward_strip_native.png` and `_4x.png` pairs.
Final frame evidence is `notes/doctrine_runtime_alpha_final.json`, with the focused residue mask in `notes/toxic_armor_frame4_detached_residue_mask.png`.
The existing sprite identities, frame count, mastery order and gameplay bonuses are preserved.

The orchestrator should inspect all twenty rewards in active and grey/locked states and verify that the native medallion remains visible, no square backdrop covers it, and every object stays inside its reward frame.

Before commit, the parent caught four unconsumed exports whose names had been derived from sprite IDs.
The producer corrected promotion to the existing unprefixed texture filenames, removed only its verified generated duplicates, and retained the path-correction evidence in `notes/doctrine_texture_path_correction.md`.
The final inventory lists the exact consumed paths.
