# Utopia Balance to Assignment — Production Manifest

## Delivery status

- Event: `015_utopia_manifesto`
- Asset slug: `utopia_balance_to_assignment`
- Status: `handed_off`
- Use: state-driven scripted-GUI threshold transition toward Assignment in the Commonwealth Ledger.
- Source method: 8 separate accepted built-in ImageGen outputs; no transform-only motion states.
- Runtime frame: `158x24` pixels.
- Runtime sheet: `1264x24` pixels, horizontal, 8 frames.
- Playback: `5 fps`, `looping = no`, `play_on_show = yes`, center anchor.
- Reached-state companion: frame 007. This is delivered alongside, not instead of, the requested animation.
- Opaque backing: RGBA alpha 255 throughout, using the approved charcoal ledger backing.

## Runtime files

| Role | Path | SHA-256 |
| --- | --- | --- |
| Animated sheet DDS | `gfx/interface/015_utopia_manifesto/utopia_balance_to_assignment_sheet.dds` | `cfb74421c21b650b061042f738cd735aeb338e0c3cb96d2624aceb0d46ca8241` |
| Reached-state DDS | `gfx/interface/015_utopia_manifesto/utopia_balance_to_assignment_static.dds` | `202a9ab4120cec445d07ef4b0509a57baff8e8ef9272a722c9be204d281efd62` |
| Review sheet PNG | `sheets/utopia_balance_to_assignment_sheet.png` | `3eb356d65c30ae14d14b715d30321ef38148bcdce9ca9986d064048703e9520a` |
| Reached-state PNG | `sheets/utopia_balance_to_assignment_static.png` | `e39f205f4a4c7fa1af2cf9179f4d68149bb9f774bb5d3f7e6248449640052fc9` |
| Review GIF | `previews/utopia_balance_to_assignment_preview.gif` | `23ac73a9d5b63fd2593528091a99435d828b2c35fc12c252164d373d1b94bd72` |

## Package inventory

- Direction and review: `brief.md`, `frame_plan.md`, `prompts.md`, `manifest.md`, `gfx_gui_handoff.md`, `visual_review.md`.
- Provenance and validation: `metadata/frame_provenance.md`, `metadata/processing_report.json`, `metadata/validation_report.json`, `metadata/binary_checksums.sha256`.
- Reproducible mechanical tooling: `notes/build_animation.py`, `notes/validate_animation.py`, `notes/rejected_drafts.md`.
- Accepted sources: `source_frames/utopia_balance_to_assignment_000_source.png` through `source_frames/utopia_balance_to_assignment_007_source.png`.
- Runtime-sized frames: `processed_frames/utopia_balance_to_assignment_000.png` through `processed_frames/utopia_balance_to_assignment_007.png`.
- Review/final PNGs: `sheets/utopia_balance_to_assignment_sheet.png`, `sheets/utopia_balance_to_assignment_static.png`.
- Review aids: `previews/utopia_balance_to_assignment_preview.gif`, `previews/utopia_balance_to_assignment_contact.png`, `previews/utopia_balance_to_assignment_source_contact.png`.

## Parent-owned wiring

- Sprite names: `GFX_utopia_balance_to_assignment_animated`, `GFX_utopia_balance_to_assignment_static`.
- Target GFX: `interface/015_utopia_manifesto.gfx`.
- Target layout: `interface/015_utopia_manifesto_ledger.gui`.
- Exact registration and layout guidance: `gfx_gui_handoff.md`.

## Evidence

- Per-frame ImageGen lineage and hashes: `metadata/frame_provenance.md`.
- Processing measurements and crop boxes: `metadata/processing_report.json`.
- Sheet, GIF, frame-difference, DDS-header, alpha, and pixel-match checks: `metadata/validation_report.json`.
- Human visual inspection: `visual_review.md`.

No requested animation state, source frame, runtime file, review aid, or provenance surface was omitted or replaced with a simplification.
