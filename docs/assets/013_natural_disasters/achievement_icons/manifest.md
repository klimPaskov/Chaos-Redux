# Event 013 Natural Disasters Achievement Icon Manifest

Package scope: generated achievement icons for Event `013` `natural_disasters`, including normal, grey, and not-eligible DDS variants for each registered achievement.

Production note:
- A dedicated achievement-icon subagent was started, but it did not return a usable package before final integration.
- The package was produced locally from the existing Event 013 generated art sources and processed with `docs/assets/013_natural_disasters/process_achievements.py`, using the same final filenames and sprite aliases planned for the subagent handoff.
- Final DDS files were produced with `convert -define dds:compression=none` from the processed PNGs.

Reference inputs:
- `docs/specs/013_natural_disasters_specs/prompts/013_natural_disasters_achievement_prompt.md`
- `docs/assets/013_natural_disasters/manifest.md`
- Event 013 generated report/news/super-event art under `docs/assets/013_natural_disasters/source_png/`

Review file:
- `docs/assets/013_natural_disasters/achievement_icons/ACH_ND_contact_sheet.png`

## Icons

All final files live in `gfx/achievements/`. Sprite aliases are registered in `interface/chaosx_achievements.gfx`.

- `ACH_ND_RING_THE_BELL`
  - Source PNG: `docs/assets/013_natural_disasters/achievement_icons/source_png/ACH_ND_RING_THE_BELL_source.png`
  - Processed PNG: `docs/assets/013_natural_disasters/achievement_icons/processed_png/ACH_ND_RING_THE_BELL.png`
  - Final DDS: `gfx/achievements/ACH_ND_RING_THE_BELL.dds`
- `ACH_ND_ENGINEERS_OF_THE_RUBBLE`
  - Source PNG: `docs/assets/013_natural_disasters/achievement_icons/source_png/ACH_ND_ENGINEERS_OF_THE_RUBBLE_source.png`
  - Processed PNG: `docs/assets/013_natural_disasters/achievement_icons/processed_png/ACH_ND_ENGINEERS_OF_THE_RUBBLE.png`
  - Final DDS: `gfx/achievements/ACH_ND_ENGINEERS_OF_THE_RUBBLE.dds`
- `ACH_ND_THE_TRAINS_ARRIVED`
  - Source PNG: `docs/assets/013_natural_disasters/achievement_icons/source_png/ACH_ND_THE_TRAINS_ARRIVED_source.png`
  - Processed PNG: `docs/assets/013_natural_disasters/achievement_icons/processed_png/ACH_ND_THE_TRAINS_ARRIVED.png`
  - Final DDS: `gfx/achievements/ACH_ND_THE_TRAINS_ARRIVED.dds`
- `ACH_ND_NO_PORT_LEFT_BEHIND`
  - Source PNG: `docs/assets/013_natural_disasters/achievement_icons/source_png/ACH_ND_NO_PORT_LEFT_BEHIND_source.png`
  - Processed PNG: `docs/assets/013_natural_disasters/achievement_icons/processed_png/ACH_ND_NO_PORT_LEFT_BEHIND.png`
  - Final DDS: `gfx/achievements/ACH_ND_NO_PORT_LEFT_BEHIND.dds`
- `ACH_ND_GRAIN_AGAINST_THE_DUST`
  - Source PNG: `docs/assets/013_natural_disasters/achievement_icons/source_png/ACH_ND_GRAIN_AGAINST_THE_DUST_source.png`
  - Processed PNG: `docs/assets/013_natural_disasters/achievement_icons/processed_png/ACH_ND_GRAIN_AGAINST_THE_DUST.png`
  - Final DDS: `gfx/achievements/ACH_ND_GRAIN_AGAINST_THE_DUST.dds`
- `ACH_ND_ASH_ON_THE_RUNWAY`
  - Source PNG: `docs/assets/013_natural_disasters/achievement_icons/source_png/ACH_ND_ASH_ON_THE_RUNWAY_source.png`
  - Processed PNG: `docs/assets/013_natural_disasters/achievement_icons/processed_png/ACH_ND_ASH_ON_THE_RUNWAY.png`
  - Final DDS: `gfx/achievements/ACH_ND_ASH_ON_THE_RUNWAY.dds`
- `ACH_ND_SKY_ARTILLERY_SURVIVOR`
  - Source PNG: `docs/assets/013_natural_disasters/achievement_icons/source_png/ACH_ND_SKY_ARTILLERY_SURVIVOR_source.png`
  - Processed PNG: `docs/assets/013_natural_disasters/achievement_icons/processed_png/ACH_ND_SKY_ARTILLERY_SURVIVOR.png`
  - Final DDS: `gfx/achievements/ACH_ND_SKY_ARTILLERY_SURVIVOR.dds`
- `ACH_ND_THE_SEA_WALKED_BACK`
  - Source PNG: `docs/assets/013_natural_disasters/achievement_icons/source_png/ACH_ND_THE_SEA_WALKED_BACK_source.png`
  - Processed PNG: `docs/assets/013_natural_disasters/achievement_icons/processed_png/ACH_ND_THE_SEA_WALKED_BACK.png`
  - Final DDS: `gfx/achievements/ACH_ND_THE_SEA_WALKED_BACK.dds`
- `ACH_ND_NOT_ONE_MORE_AFTERSHOCK`
  - Source PNG: `docs/assets/013_natural_disasters/achievement_icons/source_png/ACH_ND_NOT_ONE_MORE_AFTERSHOCK_source.png`
  - Processed PNG: `docs/assets/013_natural_disasters/achievement_icons/processed_png/ACH_ND_NOT_ONE_MORE_AFTERSHOCK.png`
  - Final DDS: `gfx/achievements/ACH_ND_NOT_ONE_MORE_AFTERSHOCK.dds`
- `ACH_ND_DISASTER_LEDGER_CLOSED`
  - Source PNG: `docs/assets/013_natural_disasters/achievement_icons/source_png/ACH_ND_DISASTER_LEDGER_CLOSED_source.png`
  - Processed PNG: `docs/assets/013_natural_disasters/achievement_icons/processed_png/ACH_ND_DISASTER_LEDGER_CLOSED.png`
  - Final DDS: `gfx/achievements/ACH_ND_DISASTER_LEDGER_CLOSED.dds`
- `ACH_ND_NO_WORLD_END_REQUIRED`
  - Source PNG: `docs/assets/013_natural_disasters/achievement_icons/source_png/ACH_ND_NO_WORLD_END_REQUIRED_source.png`
  - Processed PNG: `docs/assets/013_natural_disasters/achievement_icons/processed_png/ACH_ND_NO_WORLD_END_REQUIRED.png`
  - Final DDS: `gfx/achievements/ACH_ND_NO_WORLD_END_REQUIRED.dds`
- `ACH_ND_STILL_STANDING_IN_FOUR_SEASONS`
  - Source PNG: `docs/assets/013_natural_disasters/achievement_icons/source_png/ACH_ND_STILL_STANDING_IN_FOUR_SEASONS_source.png`
  - Processed PNG: `docs/assets/013_natural_disasters/achievement_icons/processed_png/ACH_ND_STILL_STANDING_IN_FOUR_SEASONS.png`
  - Final DDS: `gfx/achievements/ACH_ND_STILL_STANDING_IN_FOUR_SEASONS.dds`

Each ID also has:
- `gfx/achievements/<ID>_grey.dds`
- `gfx/achievements/<ID>_not_eligible.dds`
- matching processed PNG variants under `docs/assets/013_natural_disasters/achievement_icons/processed_png/`

## Status

All Event 013 achievement icons are wired to the live achievement IDs and are ready for replacement by preserving the same filenames and sprite aliases.
