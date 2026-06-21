# Natural Disaster Achievement Icon Manifest

Package: `docs/assets/achievement_icon_regen_hoi4_style_natural_disaster_2026_06_21/`

Scope:
- Event `013`
- Event slug: `natural_disasters`
- Asset type: achievement icon families
- Intended in-game use: HOI4 64x64 achievement tiles
- Source mode: `$imagegen`
- Variant rule: completed tile -> grey -> not eligible
- Final live DDS folder: `gfx/achievements/`

References inspected:
- `.agents/skills/chaos-redux-event-assets/assets/achievements/`
- `~/projects/Hearts of Iron IV/gfx/achievements/`
- `docs/specs/013_natural_disasters_specs/prompts/013_natural_disasters_achievement_prompt.md`

Review assets:
- `contact_sheets/source_selection_contact_sheet.png`
- `contact_sheets/family_variants_contact_sheet.png`

Common processing:
- source PNG copied from the built-in `$imagegen` cache into `source_png/`
- processed PNG resized to `64x64`
- grey variant derived from the processed completed tile
- not-eligible variant derived from the grey tile with a red X overlay
- DDS copies written to `dds/`
- final DDS families copied to `gfx/achievements/`

## Asset ledger

- `ACH_ND_ASH_ON_THE_RUNWAY`
  - Prompt ref: `prompts/natural_disaster_achievement_prompts.md#ach_nd_ash_on_the_runway`
  - Source PNG: `source_png/ACH_ND_ASH_ON_THE_RUNWAY_source.png`
  - Processed PNGs: `processed_png/ACH_ND_ASH_ON_THE_RUNWAY.png`, `processed_png/ACH_ND_ASH_ON_THE_RUNWAY_grey.png`, `processed_png/ACH_ND_ASH_ON_THE_RUNWAY_not_eligible.png`
  - Package DDS: `dds/ACH_ND_ASH_ON_THE_RUNWAY.dds`, `dds/ACH_ND_ASH_ON_THE_RUNWAY_grey.dds`, `dds/ACH_ND_ASH_ON_THE_RUNWAY_not_eligible.dds`
  - Final DDS: `gfx/achievements/ACH_ND_ASH_ON_THE_RUNWAY.dds`, `gfx/achievements/ACH_ND_ASH_ON_THE_RUNWAY_grey.dds`, `gfx/achievements/ACH_ND_ASH_ON_THE_RUNWAY_not_eligible.dds`
  - Target size: `64x64`
  - Status: `complete`

- `ACH_ND_DISASTER_LEDGER_CLOSED`
  - Prompt ref: `prompts/natural_disaster_achievement_prompts.md#ach_nd_disaster_ledger_closed`
  - Source PNG: `source_png/ACH_ND_DISASTER_LEDGER_CLOSED_source.png`
  - Processed PNGs: `processed_png/ACH_ND_DISASTER_LEDGER_CLOSED.png`, `processed_png/ACH_ND_DISASTER_LEDGER_CLOSED_grey.png`, `processed_png/ACH_ND_DISASTER_LEDGER_CLOSED_not_eligible.png`
  - Package DDS: `dds/ACH_ND_DISASTER_LEDGER_CLOSED.dds`, `dds/ACH_ND_DISASTER_LEDGER_CLOSED_grey.dds`, `dds/ACH_ND_DISASTER_LEDGER_CLOSED_not_eligible.dds`
  - Final DDS: `gfx/achievements/ACH_ND_DISASTER_LEDGER_CLOSED.dds`, `gfx/achievements/ACH_ND_DISASTER_LEDGER_CLOSED_grey.dds`, `gfx/achievements/ACH_ND_DISASTER_LEDGER_CLOSED_not_eligible.dds`
  - Target size: `64x64`
  - Status: `complete`

- `ACH_ND_ENGINEERS_OF_THE_RUBBLE`
  - Prompt ref: `prompts/natural_disaster_achievement_prompts.md#ach_nd_engineers_of_the_rubble`
  - Source PNG: `source_png/ACH_ND_ENGINEERS_OF_THE_RUBBLE_source.png`
  - Processed PNGs: `processed_png/ACH_ND_ENGINEERS_OF_THE_RUBBLE.png`, `processed_png/ACH_ND_ENGINEERS_OF_THE_RUBBLE_grey.png`, `processed_png/ACH_ND_ENGINEERS_OF_THE_RUBBLE_not_eligible.png`
  - Package DDS: `dds/ACH_ND_ENGINEERS_OF_THE_RUBBLE.dds`, `dds/ACH_ND_ENGINEERS_OF_THE_RUBBLE_grey.dds`, `dds/ACH_ND_ENGINEERS_OF_THE_RUBBLE_not_eligible.dds`
  - Final DDS: `gfx/achievements/ACH_ND_ENGINEERS_OF_THE_RUBBLE.dds`, `gfx/achievements/ACH_ND_ENGINEERS_OF_THE_RUBBLE_grey.dds`, `gfx/achievements/ACH_ND_ENGINEERS_OF_THE_RUBBLE_not_eligible.dds`
  - Target size: `64x64`
  - Status: `complete`

- `ACH_ND_GRAIN_AGAINST_THE_DUST`
  - Prompt ref: `prompts/natural_disaster_achievement_prompts.md#ach_nd_grain_against_the_dust`
  - Source PNG: `source_png/ACH_ND_GRAIN_AGAINST_THE_DUST_source.png`
  - Processed PNGs: `processed_png/ACH_ND_GRAIN_AGAINST_THE_DUST.png`, `processed_png/ACH_ND_GRAIN_AGAINST_THE_DUST_grey.png`, `processed_png/ACH_ND_GRAIN_AGAINST_THE_DUST_not_eligible.png`
  - Package DDS: `dds/ACH_ND_GRAIN_AGAINST_THE_DUST.dds`, `dds/ACH_ND_GRAIN_AGAINST_THE_DUST_grey.dds`, `dds/ACH_ND_GRAIN_AGAINST_THE_DUST_not_eligible.dds`
  - Final DDS: `gfx/achievements/ACH_ND_GRAIN_AGAINST_THE_DUST.dds`, `gfx/achievements/ACH_ND_GRAIN_AGAINST_THE_DUST_grey.dds`, `gfx/achievements/ACH_ND_GRAIN_AGAINST_THE_DUST_not_eligible.dds`
  - Target size: `64x64`
  - Status: `complete`

- `ACH_ND_NOT_ONE_MORE_AFTERSHOCK`
  - Prompt ref: `prompts/natural_disaster_achievement_prompts.md#ach_nd_not_one_more_aftershock`
  - Source PNG: `source_png/ACH_ND_NOT_ONE_MORE_AFTERSHOCK_source.png`
  - Processed PNGs: `processed_png/ACH_ND_NOT_ONE_MORE_AFTERSHOCK.png`, `processed_png/ACH_ND_NOT_ONE_MORE_AFTERSHOCK_grey.png`, `processed_png/ACH_ND_NOT_ONE_MORE_AFTERSHOCK_not_eligible.png`
  - Package DDS: `dds/ACH_ND_NOT_ONE_MORE_AFTERSHOCK.dds`, `dds/ACH_ND_NOT_ONE_MORE_AFTERSHOCK_grey.dds`, `dds/ACH_ND_NOT_ONE_MORE_AFTERSHOCK_not_eligible.dds`
  - Final DDS: `gfx/achievements/ACH_ND_NOT_ONE_MORE_AFTERSHOCK.dds`, `gfx/achievements/ACH_ND_NOT_ONE_MORE_AFTERSHOCK_grey.dds`, `gfx/achievements/ACH_ND_NOT_ONE_MORE_AFTERSHOCK_not_eligible.dds`
  - Target size: `64x64`
  - Status: `complete`

- `ACH_ND_NO_PORT_LEFT_BEHIND`
  - Prompt ref: `prompts/natural_disaster_achievement_prompts.md#ach_nd_no_port_left_behind`
  - Source PNG: `source_png/ACH_ND_NO_PORT_LEFT_BEHIND_source.png`
  - Processed PNGs: `processed_png/ACH_ND_NO_PORT_LEFT_BEHIND.png`, `processed_png/ACH_ND_NO_PORT_LEFT_BEHIND_grey.png`, `processed_png/ACH_ND_NO_PORT_LEFT_BEHIND_not_eligible.png`
  - Package DDS: `dds/ACH_ND_NO_PORT_LEFT_BEHIND.dds`, `dds/ACH_ND_NO_PORT_LEFT_BEHIND_grey.dds`, `dds/ACH_ND_NO_PORT_LEFT_BEHIND_not_eligible.dds`
  - Final DDS: `gfx/achievements/ACH_ND_NO_PORT_LEFT_BEHIND.dds`, `gfx/achievements/ACH_ND_NO_PORT_LEFT_BEHIND_grey.dds`, `gfx/achievements/ACH_ND_NO_PORT_LEFT_BEHIND_not_eligible.dds`
  - Target size: `64x64`
  - Status: `complete`

- `ACH_ND_NO_WORLD_END_REQUIRED`
  - Prompt ref: `prompts/natural_disaster_achievement_prompts.md#ach_nd_no_world_end_required`
  - Source PNG: `source_png/ACH_ND_NO_WORLD_END_REQUIRED_source.png`
  - Processed PNGs: `processed_png/ACH_ND_NO_WORLD_END_REQUIRED.png`, `processed_png/ACH_ND_NO_WORLD_END_REQUIRED_grey.png`, `processed_png/ACH_ND_NO_WORLD_END_REQUIRED_not_eligible.png`
  - Package DDS: `dds/ACH_ND_NO_WORLD_END_REQUIRED.dds`, `dds/ACH_ND_NO_WORLD_END_REQUIRED_grey.dds`, `dds/ACH_ND_NO_WORLD_END_REQUIRED_not_eligible.dds`
  - Final DDS: `gfx/achievements/ACH_ND_NO_WORLD_END_REQUIRED.dds`, `gfx/achievements/ACH_ND_NO_WORLD_END_REQUIRED_grey.dds`, `gfx/achievements/ACH_ND_NO_WORLD_END_REQUIRED_not_eligible.dds`
  - Target size: `64x64`
  - Status: `complete`

- `ACH_ND_RING_THE_BELL`
  - Prompt ref: `prompts/natural_disaster_achievement_prompts.md#ach_nd_ring_the_bell`
  - Source PNG: `source_png/ACH_ND_RING_THE_BELL_source.png`
  - Processed PNGs: `processed_png/ACH_ND_RING_THE_BELL.png`, `processed_png/ACH_ND_RING_THE_BELL_grey.png`, `processed_png/ACH_ND_RING_THE_BELL_not_eligible.png`
  - Package DDS: `dds/ACH_ND_RING_THE_BELL.dds`, `dds/ACH_ND_RING_THE_BELL_grey.dds`, `dds/ACH_ND_RING_THE_BELL_not_eligible.dds`
  - Final DDS: `gfx/achievements/ACH_ND_RING_THE_BELL.dds`, `gfx/achievements/ACH_ND_RING_THE_BELL_grey.dds`, `gfx/achievements/ACH_ND_RING_THE_BELL_not_eligible.dds`
  - Target size: `64x64`
  - Status: `complete`

- `ACH_ND_SKY_ARTILLERY_SURVIVOR`
  - Prompt ref: `prompts/natural_disaster_achievement_prompts.md#ach_nd_sky_artillery_survivor`
  - Source PNG: `source_png/ACH_ND_SKY_ARTILLERY_SURVIVOR_source.png`
  - Processed PNGs: `processed_png/ACH_ND_SKY_ARTILLERY_SURVIVOR.png`, `processed_png/ACH_ND_SKY_ARTILLERY_SURVIVOR_grey.png`, `processed_png/ACH_ND_SKY_ARTILLERY_SURVIVOR_not_eligible.png`
  - Package DDS: `dds/ACH_ND_SKY_ARTILLERY_SURVIVOR.dds`, `dds/ACH_ND_SKY_ARTILLERY_SURVIVOR_grey.dds`, `dds/ACH_ND_SKY_ARTILLERY_SURVIVOR_not_eligible.dds`
  - Final DDS: `gfx/achievements/ACH_ND_SKY_ARTILLERY_SURVIVOR.dds`, `gfx/achievements/ACH_ND_SKY_ARTILLERY_SURVIVOR_grey.dds`, `gfx/achievements/ACH_ND_SKY_ARTILLERY_SURVIVOR_not_eligible.dds`
  - Target size: `64x64`
  - Status: `complete`

- `ACH_ND_STILL_STANDING_IN_FOUR_SEASONS`
  - Prompt ref: `prompts/natural_disaster_achievement_prompts.md#ach_nd_still_standing_in_four_seasons`
  - Source PNG: `source_png/ACH_ND_STILL_STANDING_IN_FOUR_SEASONS_source.png`
  - Processed PNGs: `processed_png/ACH_ND_STILL_STANDING_IN_FOUR_SEASONS.png`, `processed_png/ACH_ND_STILL_STANDING_IN_FOUR_SEASONS_grey.png`, `processed_png/ACH_ND_STILL_STANDING_IN_FOUR_SEASONS_not_eligible.png`
  - Package DDS: `dds/ACH_ND_STILL_STANDING_IN_FOUR_SEASONS.dds`, `dds/ACH_ND_STILL_STANDING_IN_FOUR_SEASONS_grey.dds`, `dds/ACH_ND_STILL_STANDING_IN_FOUR_SEASONS_not_eligible.dds`
  - Final DDS: `gfx/achievements/ACH_ND_STILL_STANDING_IN_FOUR_SEASONS.dds`, `gfx/achievements/ACH_ND_STILL_STANDING_IN_FOUR_SEASONS_grey.dds`, `gfx/achievements/ACH_ND_STILL_STANDING_IN_FOUR_SEASONS_not_eligible.dds`
  - Target size: `64x64`
  - Status: `complete`

- `ACH_ND_THE_SEA_WALKED_BACK`
  - Prompt ref: `prompts/natural_disaster_achievement_prompts.md#ach_nd_the_sea_walked_back`
  - Source PNG: `source_png/ACH_ND_THE_SEA_WALKED_BACK_source.png`
  - Processed PNGs: `processed_png/ACH_ND_THE_SEA_WALKED_BACK.png`, `processed_png/ACH_ND_THE_SEA_WALKED_BACK_grey.png`, `processed_png/ACH_ND_THE_SEA_WALKED_BACK_not_eligible.png`
  - Package DDS: `dds/ACH_ND_THE_SEA_WALKED_BACK.dds`, `dds/ACH_ND_THE_SEA_WALKED_BACK_grey.dds`, `dds/ACH_ND_THE_SEA_WALKED_BACK_not_eligible.dds`
  - Final DDS: `gfx/achievements/ACH_ND_THE_SEA_WALKED_BACK.dds`, `gfx/achievements/ACH_ND_THE_SEA_WALKED_BACK_grey.dds`, `gfx/achievements/ACH_ND_THE_SEA_WALKED_BACK_not_eligible.dds`
  - Target size: `64x64`
  - Status: `complete`

- `ACH_ND_THE_TRAINS_ARRIVED`
  - Prompt ref: `prompts/natural_disaster_achievement_prompts.md#ach_nd_the_trains_arrived`
  - Source PNG: `source_png/ACH_ND_THE_TRAINS_ARRIVED_source.png`
  - Processed PNGs: `processed_png/ACH_ND_THE_TRAINS_ARRIVED.png`, `processed_png/ACH_ND_THE_TRAINS_ARRIVED_grey.png`, `processed_png/ACH_ND_THE_TRAINS_ARRIVED_not_eligible.png`
  - Package DDS: `dds/ACH_ND_THE_TRAINS_ARRIVED.dds`, `dds/ACH_ND_THE_TRAINS_ARRIVED_grey.dds`, `dds/ACH_ND_THE_TRAINS_ARRIVED_not_eligible.dds`
  - Final DDS: `gfx/achievements/ACH_ND_THE_TRAINS_ARRIVED.dds`, `gfx/achievements/ACH_ND_THE_TRAINS_ARRIVED_grey.dds`, `gfx/achievements/ACH_ND_THE_TRAINS_ARRIVED_not_eligible.dds`
  - Target size: `64x64`
  - Status: `complete`
