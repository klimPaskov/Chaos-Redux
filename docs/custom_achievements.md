# Custom Achievements

This mechanic adds a first pass of Chaos Redux custom achievements using HOI4's mod achievement system.

## What It Adds

Three internal rarity groups are now represented in the achievement list order:

- Legendary
  - `00_calm_before_the_storm_achievement`
  - `01_world_collapse_ahead_of_schedule_achievement`
  - `02_full_spectrum_terror_achievement`
  - `03_poisoned_skies_achievement`
  - `04_a_billion_dead_achievement`
- Common
  - `10_maximum_chaos_achievement`
  - `11_gas_gas_gas_achievement`
  - `12_tainted_air_achievement`
  - `13_hundred_million_dead_achievement`
  - `14_ten_percent_ceiling_achievement`
  - `15_global_pariah_achievement`
- Epic
  - `20_end_of_the_living_achievement`

HOI4 custom achievements do not expose a native tier field in the file format, so tiering is preserved through internal grouping, naming, and docs rather than a dedicated engine-side rarity value.

## How It Works

1. `common/achievements/chaos_redux_achievements.txt` registers the mod achievement set with `unique_id = chaos_redux_achievements`.
2. All achievements are available for any player country.
3. Most conditions read directly from existing system state:
   - `global.chaos_meter_value`
   - `global.air_contamination_bp`
   - `global.chaos_meter_deaths_total`
   - `world_end_zombies`
   - researched technologies
4. Three lightweight tracking hooks were added so achievements can express historical conditions cleanly:
   - `achievement_chaos_reached_gathering_storm_pre_1940`
     - Set when the live chaos meter reaches `Gathering Storm` or higher before January 1, 1940.
   - `achievement_contamination_reached_10_pre_1945`
     - Set when global contamination reaches `10%` or higher before January 1, 1945.
   - `achievement_used_chemical_ability`
     - Set when a chemical cylinder ability is used.
5. Achievement art is wired in two layers:
   - HOI4 mod achievement UI looks for icon files in `gfx/achievements/`.
   - `interface/chaosx_achievements.gfx` adds stable sprite aliases for the primary icon of each achievement for any future custom UI use.

## Achievement Conditions

### Legendary

- `00_calm_before_the_storm_achievement`
  - Keep the chaos meter below `Gathering Storm` until January 1, 1940.
- `01_world_collapse_ahead_of_schedule_achievement`
  - Reach `1000+` chaos before January 1, 1940.
- `02_full_spectrum_terror_achievement`
  - Research every biowarfare and chemical-warfare tech that is manually available from the start of a normal campaign.
  - Excludes special-project-locked techs (`anthrax/plague/tularemia/smallpox bomb delivery`, `sarin`, `soman`) and hidden doctrine unlock techs.
- `03_poisoned_skies_achievement`
  - Reach `100%` global contamination.
- `04_a_billion_dead_achievement`
  - Reach `1,000,000,000` total global deaths.

### Common

- `10_maximum_chaos_achievement`
  - Reach `1000+` chaos.
- `11_gas_gas_gas_achievement`
  - Use a chemical cylinder ability for the first time.
- `12_tainted_air_achievement`
  - Reach `25%` global contamination.
- `13_hundred_million_dead_achievement`
  - Reach `100,000,000` total global deaths.
- `14_ten_percent_ceiling_achievement`
  - Keep global contamination below `10%` until January 1, 1945.
- `15_global_pariah_achievement`
  - Reach `100+` international condemnation on the player country.

### Epic

- `20_end_of_the_living_achievement`
  - Trigger the zombie apocalypse world-end scenario (`world_end_zombies`).

## Icons And GFX

Place all achievement icons in:

- `gfx/achievements/`

Primary sprite definitions live in:

- `interface/chaosx_achievements.gfx`

The mod achievement system expects three files per achievement:

- normal unlocked icon: `gfx/achievements/<achievement_id>.dds`
- locked but eligible icon: `gfx/achievements/<achievement_id>_grey.dds`
- not eligible icon: `gfx/achievements/<achievement_id>_not_eligible.dds`

Registered primary sprite aliases:

- `00_calm_before_the_storm_achievement`
  - Sprite key: `GFX_achievement_00_calm_before_the_storm_achievement`
  - Files:
    - `gfx/achievements/00_calm_before_the_storm_achievement.dds`
    - `gfx/achievements/00_calm_before_the_storm_achievement_grey.dds`
    - `gfx/achievements/00_calm_before_the_storm_achievement_not_eligible.dds`
- `01_world_collapse_ahead_of_schedule_achievement`
  - Sprite key: `GFX_achievement_01_world_collapse_ahead_of_schedule_achievement`
  - Files:
    - `gfx/achievements/01_world_collapse_ahead_of_schedule_achievement.dds`
    - `gfx/achievements/01_world_collapse_ahead_of_schedule_achievement_grey.dds`
    - `gfx/achievements/01_world_collapse_ahead_of_schedule_achievement_not_eligible.dds`
- `02_full_spectrum_terror_achievement`
  - Sprite key: `GFX_achievement_02_full_spectrum_terror_achievement`
  - Files:
    - `gfx/achievements/02_full_spectrum_terror_achievement.dds`
    - `gfx/achievements/02_full_spectrum_terror_achievement_grey.dds`
    - `gfx/achievements/02_full_spectrum_terror_achievement_not_eligible.dds`
- `03_poisoned_skies_achievement`
  - Sprite key: `GFX_achievement_03_poisoned_skies_achievement`
  - Files:
    - `gfx/achievements/03_poisoned_skies_achievement.dds`
    - `gfx/achievements/03_poisoned_skies_achievement_grey.dds`
    - `gfx/achievements/03_poisoned_skies_achievement_not_eligible.dds`
- `04_a_billion_dead_achievement`
  - Sprite key: `GFX_achievement_04_a_billion_dead_achievement`
  - Files:
    - `gfx/achievements/04_a_billion_dead_achievement.dds`
    - `gfx/achievements/04_a_billion_dead_achievement_grey.dds`
    - `gfx/achievements/04_a_billion_dead_achievement_not_eligible.dds`
- `10_maximum_chaos_achievement`
  - Sprite key: `GFX_achievement_10_maximum_chaos_achievement`
  - Files:
    - `gfx/achievements/10_maximum_chaos_achievement.dds`
    - `gfx/achievements/10_maximum_chaos_achievement_grey.dds`
    - `gfx/achievements/10_maximum_chaos_achievement_not_eligible.dds`
- `11_gas_gas_gas_achievement`
  - Sprite key: `GFX_achievement_11_gas_gas_gas_achievement`
  - Files:
    - `gfx/achievements/11_gas_gas_gas_achievement.dds`
    - `gfx/achievements/11_gas_gas_gas_achievement_grey.dds`
    - `gfx/achievements/11_gas_gas_gas_achievement_not_eligible.dds`
- `12_tainted_air_achievement`
  - Sprite key: `GFX_achievement_12_tainted_air_achievement`
  - Files:
    - `gfx/achievements/12_tainted_air_achievement.dds`
    - `gfx/achievements/12_tainted_air_achievement_grey.dds`
    - `gfx/achievements/12_tainted_air_achievement_not_eligible.dds`
- `13_hundred_million_dead_achievement`
  - Sprite key: `GFX_achievement_13_hundred_million_dead_achievement`
  - Files:
    - `gfx/achievements/13_hundred_million_dead_achievement.dds`
    - `gfx/achievements/13_hundred_million_dead_achievement_grey.dds`
    - `gfx/achievements/13_hundred_million_dead_achievement_not_eligible.dds`
- `14_ten_percent_ceiling_achievement`
  - Sprite key: `GFX_achievement_14_ten_percent_ceiling_achievement`
  - Files:
    - `gfx/achievements/14_ten_percent_ceiling_achievement.dds`
    - `gfx/achievements/14_ten_percent_ceiling_achievement_grey.dds`
    - `gfx/achievements/14_ten_percent_ceiling_achievement_not_eligible.dds`
- `15_global_pariah_achievement`
  - Sprite key: `GFX_achievement_15_global_pariah_achievement`
  - Files:
    - `gfx/achievements/15_global_pariah_achievement.dds`
    - `gfx/achievements/15_global_pariah_achievement_grey.dds`
    - `gfx/achievements/15_global_pariah_achievement_not_eligible.dds`
- `20_end_of_the_living_achievement`
  - Sprite key: `GFX_achievement_20_end_of_the_living_achievement`
  - Files:
    - `gfx/achievements/20_end_of_the_living_achievement.dds`
    - `gfx/achievements/20_end_of_the_living_achievement_grey.dds`
    - `gfx/achievements/20_end_of_the_living_achievement_not_eligible.dds`

## Future Plans

- Add a second pass of achievements built around cleanup and restraint, not only escalation.
- Add meta-achievements that require completing several system achievements in the same run.
- Add per-system art direction so chemistry, contamination, zombies, and low-chaos survival have distinct visual language.
- If you later want visible rarity in UI, build a dedicated scripted GUI section or badge overlays using the new sprite aliases; the stock mod achievement UI does not expose rarity badges.
