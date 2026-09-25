# Event 023 achievement-state asset audit handoff

## Disposition

- `implemented`: completed a static audit of all seven achievement triplets and all 21 final DDS files. No visual or wiring defect was proven, and runtime assets remain unchanged.
- `blocked`: achievement source PNG triplets and processed masters are absent, preventing source provenance and exact source-to-output composition verification.
- `needs_user_review`: live HOI4 consumer rendering and final in-game presentation sign-off remain pending; HOI4 was not launched.

## Family results

| Achievement triplet | Final dimensions | Alpha treatment | Visual defect status | Wiring status | Source / processed masters |
| --- | --- | --- | --- | --- | --- |
| `023_sov_nuclear_bombs_a_hundred_suns` | 3/3 are 64x64 | BGRA8 alpha 254-255; full-canvas opaque appearance | None observed | 3/3 aliases resolve to exact root-level DDS paths | Missing: 0 source PNGs, 0 processed masters |
| `023_sov_nuclear_bombs_the_bomb_never_fell` | 3/3 are 64x64 | BGRA8 alpha 254-255; full-canvas opaque appearance | None observed | 3/3 aliases resolve to exact root-level DDS paths | Missing: 0 source PNGs, 0 processed masters |
| `023_sov_nuclear_bombs_ultimatum_without_ash` | 3/3 are 64x64 | BGRA8 alpha 254-255; full-canvas opaque appearance | None observed | 3/3 aliases resolve to exact root-level DDS paths | Missing: 0 source PNGs, 0 processed masters |
| `023_sov_nuclear_bombs_scattered_arsenal` | 3/3 are 64x64 | BGRA8 alpha 254-255; full-canvas opaque appearance | None observed | 3/3 aliases resolve to exact root-level DDS paths | Missing: 0 source PNGs, 0 processed masters |
| `023_sov_nuclear_bombs_firebreak` | 3/3 are 64x64 | BGRA8 alpha 254-255; full-canvas opaque appearance | None observed | 3/3 aliases resolve to exact root-level DDS paths | Missing: 0 source PNGs, 0 processed masters |
| `023_sov_nuclear_bombs_first_and_last` | 3/3 are 64x64 | BGRA8 alpha 254-255; full-canvas opaque appearance | None observed | 3/3 aliases resolve to exact root-level DDS paths | Missing: 0 source PNGs, 0 processed masters |
| `023_sov_nuclear_bombs_the_last_telephone` | 3/3 are 64x64 | BGRA8 alpha 254-255; full-canvas opaque appearance | None observed | 3/3 aliases resolve to exact root-level DDS paths | Missing: 0 source PNGs, 0 processed masters |

Each family has normal, `_grey`, and `_not_eligible` states. All 21 runtime DDS files are placed directly under `gfx/achievements/`.

## Evidence and limits

The canonical achievement contact sheet was inspected first, followed by all 18 individual PNGs in that reference family. All 21 final DDS files were individually reviewed at native 64x64 and 4x nearest-neighbour scale. Static checks found 21/21 standard uncompressed 32-bit BGRA DDS files with exact 64x64 dimensions and 16,512-byte lengths, alpha values of 254-255, 21/21 exact DDS-to-existing-decoded-PNG pixel comparisons, 7/7 unique matching achievement definitions, and 21/21 exact sprite-alias-to-DDS mappings.

No decoded DDS PNG was used as a source master or processing input, and no reconstruction or replacement generation was performed. There are no retained Event 023 achievement-ID-matched source PNGs under `source_png/` and no processed masters under `processed_png/`; therefore source prompts/hashes, production-time template use, and source-to-output compositing equality remain unverified. No concrete visual defect was observed to justify replacement art.

The full family table, per-triplet state pixel-difference counts, alpha details, canonical reference scope, and static check results are in `docs/assets/023_sov_nuclear_bombs/notes/achievement_state_audit_2026-09-25.md`. Runtime DDS files, GFX, definitions, localisation, spreadsheets, and unrelated assets were not modified. Live HOI4 consumer validation remains outside this audit.

## Parent reconciliation, 2026-09-25

The seven missing source-master and 21 missing processed-input findings above are **superseded** by `023_achievement_source_recovery_2026-09-25.md`. That handoff records seven unchanged native ImageGen masters matching historical SHA-256 values, 21 derived subject-state inputs, 21 processed composites, and package DDS files byte-equal to runtime DDS files. The earlier absence finding remains an accurate dated snapshot and does not describe the recovered package.

The exact original `docs/assets/023_sov_nuclear_bombs/prompts/icon_prompt_set.md` is absent, so per-icon prompt provenance is **blocked** by that missing record; no prompt was inferred or reconstructed. Static source-to-output recovery is **implemented** within the recovery handoff's limits, while live achievement consumer rendering and visual sign-off remain `needs_user_review`.
