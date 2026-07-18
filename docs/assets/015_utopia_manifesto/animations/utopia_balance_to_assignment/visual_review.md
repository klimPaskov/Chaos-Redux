# Utopia Balance to Assignment — Visual Review

## Inspected artifacts

- Accepted high-resolution sources: `previews/utopia_balance_to_assignment_source_contact.png` and all eight files under `source_frames/`.
- Runtime-sized frames: `previews/utopia_balance_to_assignment_contact.png` and all eight files under `processed_frames/`.
- Playback aid: `previews/utopia_balance_to_assignment_preview.gif` at 4x nearest-neighbour review scale.
- Final runtime sheet and reached state: both PNGs under `sheets/`; DDS parity is recorded in `metadata/validation_report.json`.

## Observed progression

1. Five irregular tokens begin on an open rail with the comb retracted.
2. The comb engages the loose arrangement.
3. Guide hardware creates the first measured positions.
4. The tokens form an aligned row.
5. Cross-dividers rise into a two-by-three matrix.
6. Five tokens settle into separate cells, leaving one intentional empty cell.
7. Retainers close and the central gauge levels.
8. The final measured matrix presents a stable Assignment reached state.

## Review findings

- Camera, center anchor, instrument identity, materials, palette, and backing remain coherent across all eight accepted sources.
- The final 158-by-24 silhouettes remain readable; progressive ordering, matrix formation, and the empty cell survive reduction.
- The sequence is people-free and text-free. It contains exactly five tokens, no watermark, labels, numerals, modern electronics, or interface text.
- Every visual beat is a separately generated physical mechanism state. The runtime builder performs only crop, resize, mild shared resampling sharpen, assembly, and format conversion.
- All seven consecutive processed-frame comparisons are materially different; mean RGB RMS values range from `7.3938` to `19.8503`.
- Frame 007 is exactly the reached-state PNG and DDS pixel payload.

## Handoff risk

The charcoal backing is intentionally opaque and should be placed over the existing dark Ledger threshold strip. Live scripted-GUI placement and state timing remain parent-owned and were not exercised in this asset-only subtask.
