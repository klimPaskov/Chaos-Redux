# Event 010 Death focus icon regeneration handoff

Date: `2026-06-15`
Scope: accepted icon subagent output for the Death focus tree icon family

## Files changed

- `gfx/interface/goals/death/focus_death_*.dds`
- `docs/assets/010_death/source_png/focus_death_*_source.png`
- `docs/assets/010_death/processed_png/focus_death_*.png`
- `docs/assets/010_death/source_png/overlay_focus_frame_ledger_source.png`
- `docs/assets/010_death/source_png/overlay_focus_frame_round_source.png`
- `docs/assets/010_death/source_png/overlay_focus_frame_shield_source.png`
- `docs/assets/010_death/contact_sheets/death_focus_icons_contact.png`
- `docs/assets/010_death/generated_art_manifest.md`
- `docs/assets/010_death/generated_art_gfx_handoff.md`

## Asset list and final dimensions

- `focus_death_the_first_silence`
- `focus_death_country_on_the_island`
- `focus_death_shroud_whispers`
- `focus_death_no_mail_before_spring`
- `focus_death_weather_on_paper`
- `focus_death_island_pattern`
- `focus_death_hunger_shore`
- `focus_death_lowest_names_first`
- `focus_death_ports_without_voices`
- `focus_death_mainland_smell`
- `focus_death_black_census`
- `focus_death_no_graves_needed`
- `focus_death_first_ghost_muster`
- `focus_death_public_death`
- `focus_death_tide_learns_roads`
- `focus_death_another_shoreline`
- `focus_death_no_ferry_returns`
- `focus_death_wasteland_roads`
- `focus_death_every_road_slows`
- `focus_death_empty_supply`
- `focus_death_state_without_state`
- `focus_death_mourning_host`
- `focus_death_ruin_host`
- `focus_death_orders_without_breath`
- `focus_death_last_shores`
- `focus_death_world_consumed`

Final focus format: `100x88` DDS, `srgba`/ARGB8888, transparent outer alpha, existing `gfx/interface/goals/death/` paths preserved.

## Source mode and processing notes

- Rebuilt all 26 active Death focus icons from the earlier square-thumbnail presentation into a coherent HOI4-style focus set.
- The accepted pass uses transparent outer alpha, visible dark-metal or bronze badge framing, and a central painted motif sized for national focus readability.
- Existing sprite names and texture paths remain valid. No `.gfx` edit is required.

## Validation performed

- Verified all 26 focus DDS files exist.
- Verified every focus DDS is `100x88`.
- Verified all 26 focus source PNGs and processed PNGs exist.
- Verified `docs/assets/010_death/contact_sheets/death_focus_icons_contact.png` exists and reflects the accepted regenerated badge set.
- Verified no byte-identical duplicate focus DDS outputs.
- Ran `git diff --check` with no reported issues.

## Remaining blockers or uncertainties

- No blockers in the accepted focus icon scope.
