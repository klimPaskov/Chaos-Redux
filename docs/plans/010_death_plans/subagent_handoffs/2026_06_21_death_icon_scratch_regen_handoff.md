# Death Icon Scratch Regeneration Handoff

Date: `2026-06-21`

Parent task:

- Correct the Death icon asset pass so the needed Death focus and achievement icons are regenerated from scratch rather than modified from existing art.

Subagent use:

- Spawned `chaosx_icon_artist` with `fork_context=false`.
- Subagent produced fresh source PNGs for the eight requested focus icons, then was interrupted after a long run before processing, achievements, DDS conversion, manifests, and handoff writing.
- Parent completed processing, achievement generation, DDS conversion, validation, and documentation.

Files changed:

- `gfx/interface/goals/death/focus_death_empty_supply.dds`
- `gfx/interface/goals/death/focus_death_every_road_slows.dds`
- `gfx/interface/goals/death/focus_death_last_shores.dds`
- `gfx/interface/goals/death/focus_death_mourning_host.dds`
- `gfx/interface/goals/death/focus_death_orders_without_breath.dds`
- `gfx/interface/goals/death/focus_death_ruin_host.dds`
- `gfx/interface/goals/death/focus_death_state_without_state.dds`
- `gfx/interface/goals/death/focus_death_world_consumed.dds`
- `gfx/achievements/death_*` completed, `_grey`, and `_not_eligible` DDS families for all thirteen Death achievements
- `docs/assets/010_death/death_icon_scratch_regen_2026_06_21/`
- `docs/assets/010_death/generated_art_manifest.md`
- `docs/assets/010_death/generated_art_gfx_handoff.md`
- `docs/assets/achievement_regeneration/manifest.md`
- `docs/assets/achievement_regeneration/gfx_handoff.md`

Changed ids and sprite surfaces:

- Focus sprites in `interface/010_death.gfx`: `GFX_focus_death_empty_supply`, `GFX_focus_death_every_road_slows`, `GFX_focus_death_last_shores`, `GFX_focus_death_mourning_host`, `GFX_focus_death_orders_without_breath`, `GFX_focus_death_ruin_host`, `GFX_focus_death_state_without_state`, `GFX_focus_death_world_consumed`.
- Achievement families in `interface/chaosx_achievements.gfx`: `death_before_the_name`, `death_black_apostolate`, `death_black_tide_reversed`, `death_book_burner`, `death_counted_every_name`, `death_friend_of_zol`, `death_last_ferry`, `death_no_one_heard_the_first_boat`, `death_no_witnesses`, `death_not_on_my_continent`, `death_six_continents_one_color`, `death_the_living_conference`, and `death_the_names_do_not_come_back`.

Before and after behavior:

- Before: the live Death focus and achievement DDS files existed, but the latest correction required fresh source provenance rather than modified or reused source packages.
- After: every listed Death focus and achievement icon has fresh generated source PNGs, processed PNGs, package DDS copies, live DDS outputs, contact sheets, and validation notes.

Validation:

- Focus live DDS files decode to `94x86`, have transparent corners, and have zero opaque-white pixels.
- Achievement live DDS files decode to `64x64`; completed, `_grey`, and `_not_eligible` variants are fully opaque.
- Representative `file` output reports 32-bit `ARGB8888` DDS format for focus and achievement outputs.
- Source PNG byte comparisons against the previous Death focus and achievement source packages were all non-identical.

Remaining issues:

- None for the listed Death focus and achievement icons.
