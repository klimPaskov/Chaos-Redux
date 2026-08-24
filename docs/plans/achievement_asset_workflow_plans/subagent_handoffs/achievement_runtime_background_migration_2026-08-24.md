# Achievement Runtime Background Migration Handoff

Status: complete for deterministic runtime texture migration and audit. In-game completion is not claimed because live HOI4 validation remains parent/user-owned.

## Scope and exact composition contract

The existing 1,005 runtime DDS files under `gfx/achievements/` were copied into an immutable temporary source snapshot, decoded at their native 64x64 canvas, and recomposed with the supplied backgrounds beneath the unchanged state layers.

- Completed output: `achievement_template.png` beneath the exact decoded `<id>.dds` completed layer.
- Grey output: `achievement_template_grey.png` beneath the exact decoded `<id>_grey.dds` grey layer.
- Not-eligible output: `achievement_template_grey.png` beneath the exact decoded `<id>_not_eligible.dds` not-eligible layer.

Normal alpha compositing is the only interaction. No source state was resized, cropped, alpha-trimmed, grayscaled, recolored, redrawn, filtered, or otherwise modified. A fully opaque custom state background remains pixel-identical and can completely hide the supplied bottom layer.

The approved processor was `.agents/skills/chaos-redux-event-assets/tools/process_achievement_icons.py`. It used strict parsing for canonical inputs and its approved Pillow fallback for valid mixed legacy inputs, while every staged and promoted output was written and validated as one-level uncompressed legacy BGRA DDS.

## Inputs and staged evidence

- Completed background: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/achievements/achievement_template.png`, SHA-256 `248DB006611EB3942550C43DF83802AA6FB24761035FC928B5D34586C0C4C5BA`.
- Grey/not-eligible background: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/achievements/achievement_template_grey.png`, SHA-256 `70E073694C1A7D9FE40C63B1EB2E987A8A45B3FFD15CCF789EEAA5B843B90022`.
- Immutable source snapshot: `C:\Users\klimp\AppData\Local\Temp\chaosx_achievement_runtime_backgrounds_20260824\source\`.
- Staged DDS outputs: `C:\Users\klimp\AppData\Local\Temp\chaosx_achievement_runtime_backgrounds_20260824\output\`.
- Staged decoded review PNGs: `C:\Users\klimp\AppData\Local\Temp\chaosx_achievement_runtime_backgrounds_20260824\output\review\`.
- Review contact sheet: `C:\Users\klimp\AppData\Local\Temp\chaosx_achievement_runtime_backgrounds_20260824\review\achievement_runtime_backgrounds_contact_sheet.png`.
- Contact-sheet metadata: `C:\Users\klimp\AppData\Local\Temp\chaosx_achievement_runtime_backgrounds_20260824\review\achievement_runtime_backgrounds_contact_sheet_metadata.tsv`.

The contact sheet contains 15 representative achievement IDs and 45 labelled state rows at native 64x64 and nearest-neighbour 192x192 review sizes. It includes fully opaque examples, alpha-backed examples, all four source byte-length classes, strict and Pillow-fallback decode classes, source lengths, alpha ranges, and whether the supplied bottom layer is visible.

The source snapshot contains 1,005 DDS files and 335 complete triplets. Source byte-length classes are 2,872 bytes (20 files), 16,511 bytes (47 files), 16,512 bytes (885 files), and 21,972 bytes (53 files). The approved processor decoded 885 states strictly and 120 states through the approved Pillow fallback. The source aggregate SHA-256 over sorted per-file SHA-256 values is `69700C852F9F3D9802588C847E88EE4E6AA1DDDFD8DA2D75C10D8F8696FBC571`.

## Processing and audit evidence

- Dry-run: exit 0, all 335 complete triplets accepted.
- Staging: exit 0, 335 triplets written as 1,005 DDS outputs and 1,005 decoded review PNGs.
- Staging audit: exit 0, all 335 triplets passed strict 64x64 BGRA and source-layer equality checks.
- Promoted output aggregate SHA-256: `FE964B6C81C3562A13666D41B642F76DAB9C605D57DCF03F8D64F6AD570ECBDD`.
- Final runtime inventory: exactly 1,005 DDS files and 335 complete triplets.
- Final strict DDS validation: 0 failures; every file is 64x64, one-level legacy BGRA, and exactly 16,512 bytes.
- Final decoded alpha range: 254..255, matching the supplied background contract.
- Full source recomposition comparison: 0 failures across all 1,005 state outputs.
- Fully opaque source-state identity checks: 648 checks, 0 failures.
- Staged-to-runtime SHA-256 promotion comparison: 0 mismatches.

## Registered and legacy coverage

The 314 IDs registered in `common/achievements/chaos_redux_achievements.txt` all retain complete runtime triplets, with 0 registered IDs missing.

The 21 legacy/runtime extras were retained as complete triplets: `005_soviet_collapse_dead_are_citizens`, `005_soviet_collapse_last_tsar_in_snow`, `005_soviet_collapse_no_discharge_from_grave`, `005_soviet_collapse_pale_timetable`, `005_soviet_collapse_star_iron_over_tunguska`, `015_utopia_all_useful_arts`, `015_utopia_friends_without_treaties`, `015_utopia_inland_island`, `015_utopia_league_of_need`, `015_utopia_marked_bounds_survivor`, `015_utopia_need_not_greed`, `015_utopia_new_utopia`, `015_utopia_no_bloody_glory`, `015_utopia_paper_no_more`, `015_utopia_renounced_bounds`, `015_utopia_six_hour_country`, `015_utopia_storehouses_abroad`, `chaos_warfare_air_still_breathable`, `chaos_warfare_antidote_arrived`, `chaos_warfare_no_wind_is_friendly`, and `chaos_warfare_unbroken_supply_corridor`.

The existing `interface/chaosx_achievements.gfx` was read-only audited. All 633 currently named achievement texture paths exist after promotion, with 0 missing paths. No interface or GFX registry file was edited by this migration.

## Runtime-folder cleanup and ownership

An unauthorized untracked `gfx/achievements/000_chaos_redux_00_calm_before_the_storm.png` was found during final review and moved out of the runtime folder to `C:\Users\klimp\AppData\Local\Temp\chaosx_achievement_runtime_backgrounds_20260824\review\accidental_runtime_root_png_removed.png` for evidence. `gfx/achievements/` now contains no PNG review artifacts and exactly the promoted 1,005 DDS files.

The complete temporary job root is intentionally retained for parent review at `C:\Users\klimp\AppData\Local\Temp\chaosx_achievement_runtime_backgrounds_20260824\`. No repository path was recursively deleted.

## Skipped meaningful validation and remaining risks

- Live HOI4 loading, in-game achievement rendering, and save-state consumer validation were not run because this migration is asset-only and the parent/user owns live validation.
- No ImageGen or background-removal fallback was used because the user supplied existing state layers and deterministic bottom-layer compositing was the authorized workflow.
- The 120 Pillow-fallback source states are legacy/noncanonical input encodings accepted by the approved processor; their decoded pixels are preserved in the recomposition audit, while all final runtime files are strict canonical BGRA DDS.
- Contact-sheet review is evidence only and is not a runtime consumer.
