# Utopia Balance to Choice — Production Manifest

## Delivery status

- Event: `015_utopia_manifesto`
- Asset slug: `utopia_balance_to_choice`
- Status: `handed_off`
- Use: state-driven scripted-GUI threshold transition toward Choice in the Commonwealth Ledger.
- Source method: 8 separate accepted built-in ImageGen outputs; no transform-only motion states.
- Runtime frame: `158x24` pixels.
- Runtime sheet: `1264x24` pixels, horizontal, 8 frames.
- Playback: `5 fps`, `looping = no`, `play_on_show = yes`, center anchor.
- Reached-state companion: frame 007. This is delivered alongside, not instead of, the requested animation.
- Opaque backing: RGBA alpha 255 throughout, using the approved charcoal ledger backing.

## Runtime files

| Role | Path | SHA-256 |
| --- | --- | --- |
| Animated sheet DDS | `gfx/interface/015_utopia_manifesto/utopia_balance_to_choice_sheet.dds` | `cd0440db72fce608ee20cd0f5496ede0f9396ed1756aed72c694c9586f2ca13c` |
| Reached-state DDS | `gfx/interface/015_utopia_manifesto/utopia_balance_to_choice_static.dds` | `126081178829c4e7092e72b52c774e07388c39b9626518a4eee4c414bca0b953` |
| Review sheet PNG | `sheets/utopia_balance_to_choice_sheet.png` | `dff316ffbe43955127c2cc2bedd0ccd4fe61749d79288465c38042d3022e5236` |
| Reached-state PNG | `sheets/utopia_balance_to_choice_static.png` | `40b0bc5d9bf48f026dacd08a1fd617a1d93a506bbaf5319b5b36ee205fde832e` |
| Review GIF | `previews/utopia_balance_to_choice_preview.gif` | `d81355c5583cdc56eb7a21ee882395f0265294acd0f38440cda399b7b8405b37` |

## Package inventory

- Direction and review: `brief.md`, `frame_plan.md`, `prompts.md`, `manifest.md`, `gfx_gui_handoff.md`, `visual_review.md`.
- Provenance and validation: `metadata/frame_provenance.md`, `metadata/processing_report.json`, `metadata/validation_report.json`, `metadata/binary_checksums.sha256`.
- Reproducible mechanical tooling: `notes/build_animation.py`, `notes/validate_animation.py`, `notes/rejected_drafts.md`.
- Accepted sources: `source_frames/utopia_balance_to_choice_000_source.png` through `source_frames/utopia_balance_to_choice_007_source.png`.
- Runtime-sized frames: `processed_frames/utopia_balance_to_choice_000.png` through `processed_frames/utopia_balance_to_choice_007.png`.
- Review/final PNGs: `sheets/utopia_balance_to_choice_sheet.png`, `sheets/utopia_balance_to_choice_static.png`.
- Review aids: `previews/utopia_balance_to_choice_preview.gif`, `previews/utopia_balance_to_choice_contact.png`, `previews/utopia_balance_to_choice_source_contact.png`.

## Parent-owned wiring

- Sprite names: `GFX_utopia_balance_to_choice_animated`, `GFX_utopia_balance_to_choice_static`.
- Target GFX: `interface/015_utopia_manifesto.gfx`.
- Target layout: `interface/015_utopia_manifesto_ledger.gui`.
- Exact registration and layout guidance: `gfx_gui_handoff.md`.

## Evidence

- Per-frame ImageGen lineage and hashes: `metadata/frame_provenance.md`.
- Processing measurements and crop boxes: `metadata/processing_report.json`.
- Sheet, GIF, frame-difference, DDS-header, alpha, and pixel-match checks: `metadata/validation_report.json`.
- Human visual inspection: `visual_review.md`.

No requested animation state, source frame, runtime file, review aid, or provenance surface was omitted or replaced with a simplification.
