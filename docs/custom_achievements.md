# Custom Achievements

This mechanic adds Chaos Redux custom achievements using HOI4's mod achievement system.

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
  - `21_weaponize_the_end_achievement`
  - `22_fight_fire_with_fire_achievement`
  - `23_we_made_a_cure_then_made_it_worse_achievement`
  - `24_containment_was_temporary_achievement`
  - `25_only_obeys_us_achievement`
  - `26_a_friend_to_mankind_achievement`
  - `27_the_wendigo_rises_achievement`
  - `28_the_cure_is_real_achievement`
  - `29_the_lamps_remain_lit_achievement`
  - `30_mandala_of_nations_achievement`
  - `31_mountain_circle_by_vow_achievement`
  - `32_mandate_without_a_sword_achievement`
  - `33_register_without_edges_achievement`
  - `34_empty_mandala_achievement`

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
- `29_the_lamps_remain_lit_achievement`
  - As the Holy Realm, complete `THR_vow_against_annihilation`, renounce Final Silence, and keep Chaos below `600`.
- `30_mandala_of_nations_achievement`
  - As the Holy Realm, lead the Mandala of Nations and complete the three kindness acts.
- `31_mountain_circle_by_vow_achievement`
  - As the Holy Realm, unify the Himalayan circle peacefully and receive `holy_realm_himalayan_unity`.
- `32_mandate_without_a_sword_achievement`
  - As the Holy Realm, reach the Buddha Mandate with Compassion Drift below `1` and without arming Final Silence.
- `33_register_without_edges_achievement`
  - As the Holy Realm, complete Northern Indian and Eastern Mandala staged integration, then unlock `The World Is Asked to Kneel`.
- `34_empty_mandala_achievement`
  - As the Holy Realm, complete the Final Silence world-end scenario.

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

The zombie special-project achievement icon sets `21` through `28` also use the same three-file pattern and have explicit sprite aliases in `interface/chaosx_achievements.gfx`. Sets `21` through `27` currently use placeholder copies until dedicated art is supplied.

Holy Realm achievement icon sets use the same three-file pattern and are currently placeholder copies until dedicated art is supplied:

- `29_the_lamps_remain_lit_achievement`
- `30_mandala_of_nations_achievement`
- `31_mountain_circle_by_vow_achievement`
- `32_mandate_without_a_sword_achievement`
- `33_register_without_edges_achievement`
- `34_empty_mandala_achievement`

Needed final achievement art:

- `29_the_lamps_remain_lit_achievement`: a calm lamp or butter-lamp line in snow, hopeful gold/white, no weapons.
- `30_mandala_of_nations_achievement`: a peaceful mandala/faction circle with small banners or open hands.
- `31_mountain_circle_by_vow_achievement`: Tibet, Nepal, and Bhutan passes unified by prayer flags or a sealed mountain ring.
- `32_mandate_without_a_sword_achievement`: Buddha Mandate seal with an empty scabbard, dove/white banner, or hands lowered.
- `33_register_without_edges_achievement`: an Arhat ledger extending across India/China border maps, administrative rather than apocalyptic.
- `34_empty_mandala_achievement`: a dark empty mandala, ash-white ring, silent world ledger; clearly Final Silence.
