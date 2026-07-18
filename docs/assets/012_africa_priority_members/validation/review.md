# Event 012 Priority Member Icon Review

Review date: 2026-07-18

## Source inventory

- 40 PNG files inspected.
- 38 sources are 1254x1254.
- 1 source is 1430x1100.
- 1 source is 1536x1024.
- All 40 source files are RGB24 with an opaque magenta production matte.
- No embedded provenance metadata was found.

## Visual review

The shared, force, and mechanic families were reviewed separately at source scale and at the final 32x32 gameplay scale. All 40 accepted icons retain a readable central silhouette and distinct package function after reduction. The force family reads as formations, logistics, equipment, or command. The mechanic family reads as law, production, trade, administration, infrastructure, or political institutions. The eight shared surfaces remain visually distinct from both package-specific families.

The magenta matte was not accepted as transparency. Chroma extraction was tuned against representative shared, force, and mechanic samples, then applied consistently to all 40. Removed pixels were zeroed before an alpha-only edge filter so resampling could not reintroduce magenta spill.

## Runtime checks

- 40 processed PNGs: 32x32 RGBA.
- 40 final DDS files: 32x32, 4,224 bytes each.
- DDS magic: `DDS `.
- FourCC: unset, confirming uncompressed output.
- Pixel layout: 32-bit BGRA with an 8-bit alpha mask.
- Registered priority-member decision references: 56.
- Registered references with a final file: 40.
- Registered references still missing: 16 post-settlement icons.

## Completion boundary

This review approves the 40 listed decision assets as technically game-ready. It does not approve the missing priority-member visuals, resolve the absent source provenance record, or close any row in the broader 239-item Event 012 matrix that is not explicitly represented in the manifest.
