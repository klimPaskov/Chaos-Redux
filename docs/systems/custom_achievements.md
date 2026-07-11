# Custom Achievements

This mechanic adds Chaos Redux custom achievements using HOI4's mod achievement system.

## What It Adds

The achievement registry is root-only because it owns the single `chaos_redux_achievements` unique id. Inside that registry, achievements are grouped by global or event section, and each engine-facing achievement id is also the root DDS filename stem and localisation key stem.

Event-owned ids use the event prefix form, for example `010_death_no_witnesses`. Global Chaos Redux ids use the shared prefix form, for example `000_chaos_redux_10_maximum_chaos`.

HOI4 custom achievements do not expose a native tier field in the file format, so tiering is preserved through internal grouping, naming, and docs rather than a dedicated engine-side rarity value.

## How It Works

1. `common/achievements/chaos_redux_achievements.txt` registers the mod achievement set with `unique_id = chaos_redux_achievements`. Keep this registry root-only so the mod remains one achievement set, and organize event achievements inside it by event section.
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
   - `interface/chaosx_achievements.gfx` adds stable sprite aliases for the eligible, grey, and not-eligible variants for custom UI reuse.

## Achievement Conditions

### Legendary

- `000_chaos_redux_00_calm_before_the_storm`
  - Keep the chaos meter below `Gathering Storm` until January 1, 1940.
- `000_chaos_redux_01_world_collapse_ahead_of_schedule`
  - Reach `1000+` chaos before January 1, 1940.
- `000_chaos_redux_02_full_spectrum_terror`
  - Research every biowarfare and chemical-warfare tech that is manually available from the start of a normal campaign.
  - Excludes special-project-locked techs (`anthrax/plague/tularemia/smallpox bomb delivery`, `sarin`, `soman`) and hidden doctrine unlock techs.
- `000_chaos_redux_03_poisoned_skies`
  - Reach `100%` global contamination.
- `000_chaos_redux_04_a_billion_dead`
  - Reach `1,000,000,000` total global deaths.

### Common

- `000_chaos_redux_10_maximum_chaos`
  - Reach `1000+` chaos.
- `000_chaos_redux_11_gas_gas_gas`
  - Use a chemical cylinder ability for the first time.
- `000_chaos_redux_12_tainted_air`
  - Reach `25%` global contamination.
- `000_chaos_redux_13_hundred_million_dead`
  - Reach `100,000,000` total global deaths.
- `000_chaos_redux_14_ten_percent_ceiling`
  - Keep global contamination below `10%` until January 1, 1945.
- `000_chaos_redux_15_global_pariah`
  - Reach `100+` international condemnation on the player country.

### Epic

- `002_zombie_outbreak_20_end_of_the_living`
  - Trigger the zombie apocalypse world-end scenario (`world_end_zombies`).
- `002_zombie_outbreak_21_weaponize_the_end`
  - Complete a weaponized zombie project.
- `002_zombie_outbreak_22_fight_fire_with_fire`
  - Create a weaponized zombie strain that can fight hostile outbreaks.
- `002_zombie_outbreak_23_we_made_a_cure_then_made_it_worse`
  - Resolve the final strain into a cure-adapted variant.
- `002_zombie_outbreak_24_containment_was_temporary`
  - Resolve the final strain into a containment-breach variant.
- `002_zombie_outbreak_25_only_obeys_us`
  - Resolve the final strain into a controlled-loyalty variant.
- `002_zombie_outbreak_26_a_friend_to_mankind`
  - Resolve the final strain into a purifier or semi-sapient variant.
- `002_zombie_outbreak_27_the_wendigo_rises`
  - Trigger the Wendigo super event.
- `002_zombie_outbreak_28_the_cure_is_real`
  - Be the country that triggers the first zombie-cure activation.
- `003_holy_realm_29_the_lamps_remain_lit`
  - As the Holy Realm, complete `THR_vow_against_annihilation`, renounce Final Silence, and keep Chaos below `600`.
- `003_holy_realm_30_mandala_of_nations`
  - As the Holy Realm, lead the Mandala of Nations and complete the three kindness acts.
- `003_holy_realm_31_mountain_circle_by_vow`
  - As the Holy Realm, unify the Himalayan circle peacefully and receive `holy_realm_himalayan_unity`.
- `003_holy_realm_32_mandate_without_a_sword`
  - As the Holy Realm, reach the Buddha Mandate with Compassion Drift below `1` and without arming Final Silence.
- `003_holy_realm_33_register_without_edges`
  - As the Holy Realm, complete Northern Indian and Eastern Mandala staged integration, then unlock `The World Is Asked to Kneel`.
- `003_holy_realm_34_empty_mandala`
  - As the Holy Realm, complete the Final Silence world-end scenario.

### Camp Repression System

- `000_chaos_redux_60_inherit_the_ledger_close_the_ledger`
  - Inherit a large dormant network, dismantle every active site during wartime, complete reform, and avoid severe discovery or tribunal exposure.
- `000_chaos_redux_61_papers_for_the_liberated`
  - As a democratic major, document the required number of liberated severe sites without operating a radicalized site.
- `000_chaos_redux_62_the_doctor_loses_his_war`
  - As Germany, authorize the Mengele program, survive its attempted seizure of power, defeat it, dismantle Auschwitz, and close every experiment site.
- `000_chaos_redux_63_no_pingfang_shadow`
  - As Japan, expose the program internally, remove Ishii, shut down prisoner experimentation, close every experiment site, and avoid a major outbreak.
- `000_chaos_redux_64_grain_before_fear`
  - As the Soviet Union, restore or disband the Union Crisis apparatus without reaching the critical famine event.
- `000_chaos_redux_65_dominion_without_chains`
  - As the United Kingdom, complete the Raj review and close the network while the Raj remains a subject and no colonial revolt has occurred.
- `000_chaos_redux_66_redress_before_victory`
  - As the United States, terminate relocation authority and complete redress before the recorded victory threshold.
- `000_chaos_redux_67_congo_reformed`
  - As Belgium, reform the Congo concessions and close every active site before the colonial crisis is publicly exposed.
- `000_chaos_redux_68_roads_without_camps`
  - As Italy, close the desert camp network while retaining defended infrastructure in Libya.
- `000_chaos_redux_69_gurs_closed`
  - As democratic France, close the camp legacy and every active site without reaching severe tribunal exposure.

Each of these ten achievements has a `64x64` eligible icon plus grey and not-eligible variants in `gfx/achievements/`. Their sprite aliases use `GFX_achievement_<achievement_id>` in `interface/chaosx_achievements.gfx`.

### Event 010 Death

- `010_death_no_one_heard_the_first_boat`
  - Send a survey boat before Death publicly reveals itself, enter the containment war, and keep forbidden oath routes closed.
- `010_death_not_on_my_continent`
  - Help defeat a publicly revealed Death crisis before it consumes too many mainland states.
- `010_death_the_names_do_not_come_back`
  - After Death is defeated, build enough dead-zone outposts while the consumed population threshold has been crossed.
- `010_death_last_ferry`
  - Prepare five coastal states with `Keep the Port Lit` before Death publicly reveals itself.
- `010_death_counted_every_name`
  - Preserve the records through the telegraph/census decision path and defeat Death before the Chaos ceiling is crossed.
- `010_death_black_tide_reversed`
  - Answer Last Shores and help retake every Death world-end foothold.
- `010_death_no_witnesses`
  - Reach the whole-world-consumed end state.
- `010_death_before_the_name`
  - Find and defeat Death before the public reveal super-event.
- `010_death_the_living_conference`
  - Form a strong Living Compact with enough members and cohesion before Death is defeated.
- `010_death_six_continents_one_color`
  - Force Death's Last Shores branch to place footholds across six continent groups.
- `010_death_friend_of_zol`
  - Take the Black Oath, remain a Herald into Last Shores, and keep the capital outside Death's control for one year.
- `010_death_book_burner`
  - Open the Black Book, bind a name, burn the book before scandal breaks, avoid the Black Oath, and defeat Death.
- `010_death_black_apostolate`
  - As a Herald, serve Zol through sacrifices and favor during Last Shores, then proclaim the Black Apostolate.
