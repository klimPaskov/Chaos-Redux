# Event 006 portrait archive layout reconciliation

Date: 2026-08-14.

## Scope

This docs-only reconciliation records the user-approved portrait archive layout for Event 006. The single parent is `docs/assets/portraits/006_independence_wave/`. Original source images remain directly in that parent; the only child directory is `processed/`, which contains crop, review, metadata, and other processed evidence. Provenance records are stored in `processed/` as well, so the parent is an image-only ComfyUI source shelf.

No `156x210` files are retained in the parent archive or in `processed/`. Runtime DDS files remain in engine-facing `gfx/leaders/006_independence_wave/` paths and are not treated as ComfyUI source inputs.

## Documentation updates

- `docs/events/006_independence_wave/overview.md` now describes the consolidated parent/`processed` layout in the current portrait policy and asset-wiring sections.
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` now records the consolidated layout as current authority before dated historical portrait-shelf snapshots.
- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md` now records the same layout in its current authority block.

These edits do not change portrait identity, source rights, runtime DDS/GFX, character definitions, package attestation, Join order, or gameplay. Older dated handoffs may retain their original package paths for traceability; the current archive layout above is authoritative for ComfyUI source selection.

## Validation

The current archive contains 46 original source images directly at the root and one `processed` directory containing 240 derived/evidence/provenance files. The 46 root sources have unique SHA-256 hashes; ComfyUI should use only image files directly in the parent and should not scan `processed/`. A current filesystem audit confirms no `156x210` filenames or 156x210 image dimensions in either archive location. No runtime path points into `docs/assets/portraits/006_independence_wave/`.
