# FORM-12/13 state-puzzle state-833 asset audit

Date: 2026-08-13

Owner: `/root/form12_form13_state_asset_audit`

Scope: the FORM-12 and FORM-13 state-puzzle consumer specs, manifests, generated source and processed PNGs, final DDS state pieces, and the generated FORM-12/13 GFX, grouped GUI, scripted-GUI, and scripted-localisation surfaces. No gameplay, trigger, decision, GUI, localisation, specification, or central-admission files were edited.

## Result

The state-256-to-state-833 rebind is asset-complete and runtime-reference consistent for both formables. The current consumers and manifests declare `[249, 397, 399, 651, 833]`, use the shared 440x180 projection, and name state 833 as `STATE_833` / installed `history/states/833 - Mari El.txt`. State 256 is no longer referenced by FORM-12 or FORM-13 runtime wiring.

## Exact installed-map evidence

The canonical source was the generated universal geometry registry under `docs/formables/state_registry/generated/`, backed by the installed vanilla map and state history. The inspected state-833 record is:

- source: `history/states/833 - Mari El.txt`
- source-state SHA-256: `ace766770df08d3fee6877d2e3726c31063bb86bb4f27012462272348e620822`
- provinces: 282, 325, 3315, 3361, 6307, 6372, 6403, 9270, 9280, 9305, 9381, 9390, 9402, 11255, 11263, 11286, 11387 (17)
- source geometry: 1,705 pixels, 42 rows, 49 runs
- installed-map tight bounds: `[3517, 369, 3581, 410]`
- circular interval: `start_x=3517`, `length=65`, `end_x_unwrapped=3581`, no seam crossing
- geometry SHA-256: `1989142ebf1a644fc2164e94c1d9bb23003f36a4e88de91a745b75de3ef230bb`

The registry records map width 5,632, installed `map/provinces.bmp` SHA-256 `e131d30e5dcb13d9c2a8598f820a2de0ae9828f3a24f2bddc1bcfff40f71660a`, and registry content SHA-256 `9777af66b45f2539296e2cc1efaf5b0a8d6146b087f31b2bc1a4c646cc0cc6c5`. The registry QA artifact reports exact state-id coverage, row-run reconstruction, province-membership reconstruction, monotonic runs, and wrap metadata as passing. The state-registry contact sheet was inspected before reviewing the individual 833 piece. The canonical vanilla decision-category picture contact sheet was also inspected as the nearest vanilla presentation reference; it is review material only and is not used as runtime art.

The package projection is identical in both manifests and geometry artifacts:

```text
canvas       440x180
source_bbox  [3517, 176, 3723, 476]
scale        0.5448504983388704
offset       [163.6079734219269, 8.0]
wrap_start   3517
wrap_length  207
wraps seam   false
```

Independent reconstruction of state-833 from the registry row runs produced the same projected alpha mask as both state-833 processed PNGs. The projected piece is 37x24 at GUI position `(163, 113)`; the manifest stores the inclusive visual bounds `[163, 113, 199, 136]`.

## Consumer and manifest consistency

Both consumer specs are complete and agree on the state set, threshold, group, projection, output directories, and state-833 helper:

- `docs/formables/state_registry/consumers/006_form12_state_puzzle.json`
- `docs/formables/state_registry/consumers/006_form13_state_puzzle.json`
- state-833 helpers: `independence_wave_formable_state_puzzle_form12_state_833_qualifies` and `independence_wave_formable_state_puzzle_form13_state_833_qualifies`
- threshold: `summary_required_count = 4` over five visible candidates

Both manifests contain ten assets (five states × unresolved/qualifying), have matching registry/map hashes and projection data, and have valid self-hashes:

- FORM-12 manifest SHA-256: `1a83f62b5e09d0c7f3343fb778966c13bb20f9b03fd8d43e4c70bb1e68e9a8fd`
- FORM-13 manifest SHA-256: `66ea20336c527ebcb0a4b59b5192526b52b3177a47e3caf3bd6ce22240391107`

For both packages, every manifest source path equals its processed PNG content, every declared PNG SHA-256 matches the file, every declared DDS SHA-256 matches the file, and every manifest state id is represented in the corresponding consumer spec and runtime surfaces.

## DDS and round-trip evidence

All twenty final state DDS files (two formables × five states × two variants) were parsed directly. Every file has the required legacy one-level uncompressed BGRA header (`DDS ` magic, header size 124, pixel-format size 32, flags 65, fourCC 0, 32-bit masks `00FF0000/0000FF00/000000FF/FF000000`, and `DDSCAPS_TEXTURE`), exact length `128 + width*height*4`, declared dimensions matching the processed PNG, and direct BGRA payload equality after decoding.

| State | FORM-12 and FORM-13 unresolved | FORM-12 and FORM-13 qualifying | Alpha range |
|---|---:|---:|---:|
| 249 | 55x29 | 55x29 | 0..230 / 0..255 |
| 397 | 104x72 | 104x72 | 0..230 / 0..255 |
| 399 | 34x34 | 34x34 | 0..230 / 0..255 |
| 651 | 49x46 | 49x46 | 0..230 / 0..255 |
| 833 | 37x24 | 37x24 | 0..230 / 0..255 |

The unresolved and qualifying colors are the compiler's declared `(190,150,40,230)` and `(40,180,80,255)` values. Transparent pixels remain real alpha-zero pixels; there is no opaque background. For state 833 specifically, both packages' unresolved and qualifying DDS payloads round-trip exactly to their processed PNGs, with alpha maxima 230 and 255 respectively.

## Runtime wiring audit

The following generated runtime surfaces were checked against the manifests:

- `interface/chaosx_formable_state_puzzles.gfx`: all twenty FORM-12/13 sprite names exist and point to the exact manifest DDS paths.
- `interface/chaosx_formable_state_puzzle_group_independence_wave_formables.gui`: all ten state nodes per formable use the manifest positions; the state-833 nodes are at `(163,113)` and start on the unresolved sprite.
- `common/scripted_guis/chaosx_formable_state_puzzles.txt`: every state-piece binding exists, including `...form12_state_833_piece` and `...form13_state_833_piece`.
- `common/scripted_localisation/chaosx_formable_state_puzzles.txt`: every unresolved/qualifying state sprite selector exists for both formables, including state 833.
- `localisation/english/chaosx_formable_state_puzzles_l_english.yml`: state-833 hover keys exist for FORM-12 and FORM-13 and dereference `[833.GetName]` plus the live ownership/controller/core/qualification helpers.

A focused search found no `independence_wave_form12_state_256`, `independence_wave_form13_state_256`, or equivalent FORM-12/13 `state_256` reference in the current consumer, generated interface, GFX, scripted-GUI, scripted-localisation, or localisation surfaces. The historical handoff `006_form12_form13_mel_state256_fail_closed_hardening_2026_08_14.md` explicitly labels the prior state-256 guard as superseded and is documentation evidence, not a runtime reference.

## Contact-sheet and stale-file review

The canonical registry contact sheet and the composed 440x180 unresolved/qualifying previews are present and consistent with state-833's projected mask. The two package folders do not contain a package-specific contact sheet; the generated projection previews are the current composed review artifacts. This is sufficient for the exact state-puzzle geometry audit, but a parent visual-review pass may add a labeled package contact sheet if the asset acceptance record requires one.

Unreferenced legacy state-256 files remain in both package workspaces:

- `docs/formables/state_puzzles/006_form12_state_puzzle/source|processed/independence_wave_form12_state_256_{unresolved,qualifying}.png`
- `docs/formables/state_puzzles/006_form13_state_puzzle/source|processed/independence_wave_form13_state_256_{unresolved,qualifying}.png`
- `gfx/interface/formables/state_puzzles/006_form12_state_puzzle/states/independence_wave_form12_state_256_{unresolved,qualifying}.dds`
- `gfx/interface/formables/state_puzzles/006_form13_state_puzzle/states/independence_wave_form13_state_256_{unresolved,qualifying}.dds`

They are not listed by either manifest and no runtime file points to them. They are stale generated artifacts rather than stale runtime references. I did not delete them because this task is an audit handoff and the parent explicitly prohibited source edits; cleanup can be handled as a separate asset-workspace maintenance decision.

## Blockers and disposition

- **No state-833 geometry, manifest, DDS, or runtime wiring blocker found.**
- **No stale FORM-12/13 state-256 runtime reference found.**
- **Needs parent review:** decide whether to remove the eight unreferenced state-256 source/processed/DDS artifacts and whether to add a labeled package-specific contact sheet beyond the composed projection previews.
- No gameplay or live in-game validation claim is made; HOI4 was not launched.

