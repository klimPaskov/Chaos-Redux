# Utopia Balance to Choice — Visual Review

## Inspected artifacts

- Accepted high-resolution sources: `previews/utopia_balance_to_choice_source_contact.png` and all eight files under `source_frames/`.
- Runtime-sized frames: `previews/utopia_balance_to_choice_contact.png` and all eight files under `processed_frames/`.
- Playback aid: `previews/utopia_balance_to_choice_preview.gif` at 4x nearest-neighbour review scale.
- Final runtime sheet and reached state: both PNGs under `sheets/`; DDS parity is recorded in `metadata/validation_report.json`.

## Observed progression

1. The common carriage begins closed with three tokens retained on one rail.
2. The first latch and gate physically release.
3. A second route opens and the lead token leaves its detent.
4. Three route channels become distinct as tokens separate.
5. The divider folds away and the three branch mouths become usable.
6. Route leaves extend and the tokens advance independently.
7. The tokens settle on three separate, unclamped rests.
8. The final open fork presents a stable Choice reached state.

## Review findings

- Camera, center anchor, instrument identity, materials, palette, and backing remain coherent across all eight accepted sources.
- The final 158-by-24 silhouettes remain readable; the branch opening and independent token destinations survive reduction.
- The sequence is people-free and text-free. It contains no figure-like pictograms, watermark, labels, numerals, modern electronics, or interface text.
- Every visual beat is a separately generated physical mechanism state. The runtime builder performs only crop, resize, mild shared resampling sharpen, assembly, and format conversion.
- All seven consecutive processed-frame comparisons are materially different; mean RGB RMS values range from `6.3465` to `17.9497`.
- Frame 007 is exactly the reached-state PNG and DDS pixel payload.

## Handoff risk

The charcoal backing is intentionally opaque and should be placed over the existing dark Ledger threshold strip. Live scripted-GUI placement and state timing remain parent-owned and were not exercised in this asset-only subtask.
