# Event 006 portrait archive count reconciliation — 2026-09-05

## Disposition

Implemented documentation reconciliation only.

## Evidence

The physical archive at `docs/assets/portraits/006_independence_wave/` currently has exactly one child directory, `processed/`, 59 direct original image files, and no filename containing `156x210` anywhere in the archive. The flat `processed/` directory currently contains 72 crop, review, metadata, provenance, and manifest files and has no child directory. Runtime checks found no reference from `common/`, `events/`, `interface/`, `gfx/`, or `history/` into `docs/assets/portraits/006_independence_wave/`.

## Changes

`docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` now records the 2026-09-05 physical counts and points to the parent README and 2026-09-03 layout handoff as the archive contract. `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md` now carries the current 2026-09-05 layout date and links the parent README for the source-input boundary and counts.

The tracked parent README remains the user-facing workflow index: direct parent files are ComfyUI source inputs, `processed/` is evidence only, and no additional folders or runtime DDS files belong in the archive.

## Scope boundary

No source image, crop, runtime DDS, GFX definition, portrait consumer, gameplay file, or admission gate was changed. The counts describe the current local shelf snapshot; they do not authorize any unresolved portrait, rights, identity, or package admission.
