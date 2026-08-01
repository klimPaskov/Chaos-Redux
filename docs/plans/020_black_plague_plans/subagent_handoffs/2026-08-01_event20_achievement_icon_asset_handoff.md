# Event 20 achievement icon asset handoff

The Event 020 achievement presentation package is complete for the fourteen registered achievement IDs. Each ID has a unique completed emblem and matching grey and not-eligible states.

## Runtime files

- `gfx/achievements/020_black_plague_*.dds` contains 42 final files: fourteen IDs multiplied by completed, grey, and not-eligible states.
- `interface/chaosx_achievements.gfx` owns the 42 stable sprite aliases `GFX_achievement_<id>`, `GFX_achievement_<id>_grey`, and `GFX_achievement_<id>_not_eligible`.
- Every DDS is a 64x64 legacy one-level uncompressed BGRA32 texture with a 16,512-byte payload and the expected header masks.

## Source evidence

The ignored asset workspace retains the source PNGs, processed RGBA previews, prompt record, contact sheet, and machine-readable validation record under `docs/assets/020_black_plague/`. The validation record is `metadata/achievement_validation.json`; it records SHA-256 hashes, alpha ranges, dimensions, and DDS header checks for all 42 runtime files.

The generated images are fictional symbolic achievement emblems, not copied flags or reused event art. Not-eligible states use the canonical achievement overlay and grey states preserve the completed alpha channel.

## Verification

- Fourteen achievement IDs in `common/achievements/chaos_redux_achievements.txt` each have a completed, grey, and not-eligible texture path.
- The 42 texture paths referenced by `interface/chaosx_achievements.gfx` exist in the root achievements directory.
- No gameplay, model, flag, spreadsheet, localisation, or event script was changed by the asset worker.

The broader Event 020 goal remains incomplete because accepted narrative, route-depth, source-frame animation, black-fog verification, and live consumer validation still require separate work. Rat unit model production remains explicitly out of scope.
