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
- Event 006 Independence Wave
  - `cr_independence_without_patron`
  - `cr_five_small_flags`
  - `cr_suppression_failed`
  - `cr_brokers_exposed`
  - `cr_partition_without_war`
  - `cr_first_old_name`
  - `cr_old_name_modern_state`
  - `cr_local_land_congress`
  - `cr_railway_country`
  - `cr_impossible_recognition`
  - `cr_not_the_collapse`
  - `cr_charter_becomes_state`
  - `cr_charter_not_chains`
  - `cr_the_ledger_votes_back`
  - `cr_human_renunciation`
  - `cr_league_war_victory`
  - `cr_no_more_flags_needed`
  - `cr_capital_still_answers`
- Event 010 Death
  - `death_no_one_heard_the_first_boat`
  - `death_not_on_my_continent`
  - `death_the_names_do_not_come_back`
  - `death_last_ferry`
  - `death_counted_every_name`
  - `death_black_tide_reversed`
  - `death_no_witnesses`
  - `death_before_the_name`
  - `death_the_living_conference`
  - `death_six_continents_one_color`
- Event 012 Africa
  - `ACH_AFR_CHARTER_WITH_TEETH`
  - `ACH_AFR_CHARTER_WITHOUT_CHAINS`
  - `ACH_AFR_ARCHIVE_OF_OLD_SEATS`
  - `ACH_AFR_NO_COUNTERFEIT_CROWNS`
  - `ACH_AFR_BESTIARY_HAS_A_SEAT`
  - `ACH_AFR_THE_FOREST_SIGNED_BACK`
  - `ACH_AFR_NOT_PAPER_ANYMORE`
  - `ACH_AFR_NO_SECOND_SCRAMBLE`
  - `ACH_AFR_PAPER_TO_LIVING`
  - `ACH_AFR_ONE_BUT_NOT_ALONE`
  - `ACH_AFR_ALLIES_MADE_PEACE`
  - `ACH_AFR_RSA_THE_UNION_BREAKS`
  - `ACH_AFR_RETURN_PASSAGES`
  - `ACH_AFR_KILWA_TO_KUSH_LEDGER`
  - `ACH_AFR_BAOBAB_FILIBUSTER`
  - `ACH_AFR_OLD_SEATS_NEW_UNION`
  - `ACH_AFR_CHARTER_HAS_TOO_MANY_SIGNATURES`
  - `ACH_AFR_CONTINENTS_HAVE_A_CONGRESS`
  - `ACH_AFR_WORLD_IS_ONE_ONLY_AFTER_AFRICA`
- Event 013 Natural Disasters
  - `ACH_ND_RING_THE_BELL`
  - `ACH_ND_ENGINEERS_OF_THE_RUBBLE`
  - `ACH_ND_THE_TRAINS_ARRIVED`
  - `ACH_ND_NO_PORT_LEFT_BEHIND`
  - `ACH_ND_GRAIN_AGAINST_THE_DUST`
  - `ACH_ND_ASH_ON_THE_RUNWAY`
  - `ACH_ND_SKY_ARTILLERY_SURVIVOR`
  - `ACH_ND_THE_SEA_WALKED_BACK`
  - `ACH_ND_NOT_ONE_MORE_AFTERSHOCK`
  - `ACH_ND_DISASTER_LEDGER_CLOSED`
  - `ACH_ND_NO_WORLD_END_REQUIRED`
  - `ACH_ND_STILL_STANDING_IN_FOUR_SEASONS`

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
- `21_weaponize_the_end_achievement`
  - Complete a weaponized zombie project.
- `22_fight_fire_with_fire_achievement`
  - Create a weaponized zombie strain that can fight hostile outbreaks.
- `23_we_made_a_cure_then_made_it_worse_achievement`
  - Resolve the final strain into a cure-adapted variant.
- `24_containment_was_temporary_achievement`
  - Resolve the final strain into a containment-breach variant.
- `25_only_obeys_us_achievement`
  - Resolve the final strain into a controlled-loyalty variant.
- `26_a_friend_to_mankind_achievement`
  - Resolve the final strain into a purifier or semi-sapient variant.
- `27_the_wendigo_rises_achievement`
  - Trigger the Wendigo super event.
- `28_the_cure_is_real_achievement`
  - Be the country that triggers the first zombie-cure activation.
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

### Event 006 Independence Wave

- `cr_independence_without_patron`
  - As an Event 006 release, secure recognition while remaining independent and accepting no patron cabinet.
- `cr_five_small_flags`
  - As an Event 006 release, help the New States Congress build a five-link mutual guarantee network.
- `cr_suppression_failed`
  - As an Event 006 host, use hardline measures against a released committee, then lose two later breakaways in another wave.
- `cr_brokers_exposed`
  - As an Event 006 release, expose foreign brokers, secure recognition, remain independent, and never accept the patron-cabinet shortcut.
- `cr_partition_without_war`
  - As an Event 006 release, complete three peaceful Border Commission resolutions without issuing a dossier ultimatum.
- `cr_first_old_name`
  - Be the first Event 006 historical-return package country in the campaign; Event 005 origins are explicitly excluded.
- `cr_old_name_modern_state`
  - As a historical-return Event 006 release, complete a modern compromise integration route while never becoming a puppet or issuing a dossier ultimatum.
- `cr_local_land_congress`
  - As a local-polity Event 006 release, complete the current implemented land-congress/charter route, gain recognition, and accept no patron cabinet.
- `cr_railway_country`
  - As a railway package created by Event 006, proclaim the Timetable Authority, finish corridor integration, and remain independent.
- `cr_impossible_recognition`
  - As a strange Event 006 release, reveal or contain the impossible dossier and win recognition from another Event 006 country.
- `cr_not_the_collapse`
  - As Event 006 Old Great Bulgaria, complete the Volga-Bulgar Assembly route without any Soviet Collapse origin or breakaway flags.
- `cr_charter_becomes_state`
  - Complete an Event 006 formation integration route while tied to compact, congress, or League support.
- `cr_charter_not_chains`
  - Form the League of New States with the anti-puppet clause while founding members remain independent.
- `cr_the_ledger_votes_back`
  - Use a ledger or formation path after at least three Event 006 countries are counted in the League ledger.
- `cr_human_renunciation`
  - As a strange Event 006 release, lock the anti-mankind doctrine, control enough territory to matter, and bind cooperation with another strange state without restoring the public registry.
- `cr_league_war_victory`
  - As an Event 006 League founder, lead a qualifying League War against a major, host, or patron actor and keep the founding members free through victory.
- `cr_no_more_flags_needed`
  - As an Event 006 League founder, certify a final New States Congress settlement after proving mass-wave host survival, mutual guarantees, peaceful border resolutions, and anti-puppet compact terms.
- `cr_capital_still_answers`
  - As an Event 006 host, survive a severe release wave while still owning and controlling the capital.

### Event 010 Death

- `death_no_one_heard_the_first_boat`
  - Send a survey boat before Death publicly reveals itself, enter the containment war, and keep forbidden oath routes closed.
- `death_not_on_my_continent`
  - Help defeat a publicly revealed Death crisis before it consumes too many mainland states.
- `death_the_names_do_not_come_back`
  - After Death is defeated, build enough dead-zone outposts while the consumed population threshold has been crossed.
- `death_last_ferry`
  - Prepare five coastal states with `Keep the Port Lit` before Death publicly reveals itself.
- `death_counted_every_name`
  - Preserve the records through the telegraph/census decision path and defeat Death before the Chaos ceiling is crossed.
- `death_black_tide_reversed`
  - Answer Last Shores and help retake every Death world-end foothold.
- `death_no_witnesses`
  - Reach the whole-world-consumed end state.
- `death_before_the_name`
  - Find and defeat Death before the public reveal super-event.
- `death_the_living_conference`
  - Form a strong Living Compact with enough members and cohesion before Death is defeated.
- `death_six_continents_one_color`
  - Force Death's Last Shores branch to place footholds across six continent groups.

Queued but not active:

- `death_friend_of_zol`
  - Held until a full Black Oath/Herald route exists.
- `death_book_burner`
  - Held until a full Dark Methods route exists.

### Event 012 Africa

- `ACH_AFR_CHARTER_WITH_TEETH`
  - As Africa, create the Charter League and bind at least six regional authority subjects.
- `ACH_AFR_CHARTER_WITHOUT_CHAINS`
  - As Africa, take the Federal Charter route, open Integrated Regions, keep at least six unique African-capital countries as full Charter members, and avoid Charter resistance wars or the Nature Courts covenant outcome.
- `ACH_AFR_ARCHIVE_OF_OLD_SEATS`
  - As Africa, peacefully settle at least twelve historical Authority Atlas dossiers across five macro-regions without direct Archive settlement.
- `ACH_AFR_NO_COUNTERFEIT_CROWNS`
  - As Africa, complete Africa Is One through the respectful Archive route, complete the Archive guard mission, reach at least 48 Old-Seat Legitimacy, and avoid direct Archive settlement or any counterfeit crown exposure.
- `ACH_AFR_BESTIARY_HAS_A_SEAT`
  - As Africa, unlock at least six high-chaos packages, create six explicit Bestiary actors, secure the required Bestiary habitat seats, complete the required Bestiary actions, complete the Bestiary containment mission, and perform at least one explicit actor action.
- `ACH_AFR_THE_FOREST_SIGNED_BACK` (hidden)
  - As Africa, complete Africa Is One after recognizing Gorilla Highlands, Chimpanzee Telegraph, and Okapi Forest, binding all three actors to the Charter, securing habitat seats, and completing their actor actions without direct Archive settlement or counterfeit exposure.
- `ACH_AFR_NOT_PAPER_ANYMORE`
  - As Africa, complete at least twelve living-core integrations.
- `ACH_AFR_NO_SECOND_SCRAMBLE`
  - As Africa, trigger the Scramble super-event, open counter-dockets, settle every registered outside holder through the Scramble treaty mission, complete the Continental Register, and still control the capital before World Is One begins.
- `ACH_AFR_PAPER_TO_LIVING`
  - As Africa, complete the regional integration mission, reach twelve living cores, and keep Paper-Core Burden below the safe ceiling.
- `ACH_AFR_ONE_BUT_NOT_ALONE`
  - As Africa, complete Africa Is One through the autonomous regions route with the Continental Register and at least five regional authorities.
- `ACH_AFR_ALLIES_MADE_PEACE`
  - As the RSA continental side, win the RSA civil war and force Allied countries still at war with the Charter side to make peace.
- `ACH_AFR_RSA_THE_UNION_BREAKS`
  - As the RSA continental side, complete the Pretoria Deadline, win the civil war, force Allied peace, and control Transvaal, Cape, and Natal.
- `ACH_AFR_RETURN_PASSAGES`
  - As Africa, invite return cadres, build a return settlement, form diaspora officer schools, and hold the Pan-Atlantic Congress.
- `ACH_AFR_KILWA_TO_KUSH_LEDGER`
  - As Africa, complete the Archive guard mission and settle the Kush/Meroe, Aksum, Kilwa or Swahili Coast, and Great Zimbabwe dossier chain.
- `ACH_AFR_BAOBAB_FILIBUSTER` (hidden)
  - As Africa, complete Africa Is One after recognizing the Baobab Senate, binding it to the Charter, completing Bestiary containment, convening Baobab memory arbitration, and keeping the Baobab Senate intact without counterfeit exposure.
- `ACH_AFR_OLD_SEATS_NEW_UNION` (hidden)
  - As Africa, proclaim a dynamic cross-continent union while the respectful Archive route, Continental Register, at least 48 Old-Seat Legitimacy, and peaceful macro-regional dossier settlements remain intact without direct Archive settlement or counterfeit exposure.
- `ACH_AFR_CHARTER_HAS_TOO_MANY_SIGNATURES`
  - As Africa, enter World Is One with certified continent-unifier readiness, the historical dossier threshold, all Bestiary packages unlocked, and key impossible signatory outcomes recognized.
- `ACH_AFR_CONTINENTS_HAVE_A_CONGRESS`
  - As Africa, prepare the Middle East, Asia, Europe, and South Atlantic charter sponsorship routes, then proclaim a dynamic cross-continent union before World Is One begins.
- `ACH_AFR_WORLD_IS_ONE_ONLY_AFTER_AFRICA`
  - As Africa, prepare the World Is One gate in Totalen Chaos after Africa is complete, all four sponsor charters and the dynamic cross-continent union are certified, regional authority and living-core thresholds are met, and the required historical dossier and Bestiary thresholds are reached.

### Event 013 Natural Disasters

- `ACH_ND_RING_THE_BELL`
  - Complete mitigation decisions before impact for at least five Natural Disasters warnings, including at least one water-family warning.
- `ACH_ND_ENGINEERS_OF_THE_RUBBLE`
  - Fully recover repeated earthquake or landslide aftermaths without failing a disaster recovery mission.
- `ACH_ND_THE_TRAINS_ARRIVED`
  - Use relief train or railway repair responses across enough affected states, keep transport/supply proof intact, and avoid recovery mission failure.
- `ACH_ND_NO_PORT_LEFT_BEHIND`
  - Recover repeated storm, tsunami, or port-disaster aftermaths with port response work, no shoreline mission failure, and no affected-port control loss.
- `ACH_ND_GRAIN_AGAINST_THE_DUST`
  - Recover repeated drought aftermaths without failing the dry-belt mission.
- `ACH_ND_ASH_ON_THE_RUNWAY`
  - Recover repeated volcanic or meteor airfield aftermaths while avoiding ash-clearance failure.
- `ACH_ND_SKY_ARTILLERY_SURVIVOR`
  - In Evolution IV, survive and recover a meteor shower that marks multiple states while keeping the capital free of meteor scars.
- `ACH_ND_THE_SEA_WALKED_BACK`
  - Mitigate a seismic warning and recover the tsunami or coastal aftermath that follows with ports restored and civilian loss below the high threshold.
- `ACH_ND_NOT_ONE_MORE_AFTERSHOCK`
  - During Evolution III, complete chained aftermath recoveries before any chained aftermath escalates.
- `ACH_ND_DISASTER_LEDGER_CLOSED`
  - Launch Disaster Barrage at High or Maximum intensity and close all active aftermaths.
- `ACH_ND_NO_WORLD_END_REQUIRED`
  - Experience Evolution IV abnormal disaster pressure and recover affected core states without a world-end scenario while the Chaos Meter remains below the terminal threshold.
- `ACH_ND_STILL_STANDING_IN_FOUR_SEASONS`
  - Recover from earth, water, heat, and ash/sky disaster families in one campaign; manual Disaster Barrage recoveries can count for only one family.

## Icons And GFX

Place all achievement icons in:

- `gfx/achievements/`

Primary sprite definitions live in:

- `interface/chaosx_achievements.gfx`

The mod achievement system expects three files per achievement:

- normal unlocked icon: `gfx/achievements/<achievement_id>.dds`
- locked but eligible icon: `gfx/achievements/<achievement_id>_grey.dds`
- not eligible icon: `gfx/achievements/<achievement_id>_not_eligible.dds`

Event 006 Independence Wave icons use the same three-file pattern and are documented under:

- `docs/assets/006_independence_wave/achievement_icons/`

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
- `cr_league_war_victory`
  - Sprite key: `GFX_achievement_cr_league_war_victory`
  - Files:
    - `gfx/achievements/cr_league_war_victory.dds`
    - `gfx/achievements/cr_league_war_victory_grey.dds`
    - `gfx/achievements/cr_league_war_victory_not_eligible.dds`

The zombie special-project achievement icon sets `21` through `28` also use the same three-file pattern and have explicit sprite aliases in `interface/chaosx_achievements.gfx`.

Event 010 Death achievement icons use the same three-file pattern and are recorded in:

- `docs/assets/010_death/generated_art_manifest.md`

The non-Holy Realm achievement icon sets `00` through `28` have custom generated art, processed PNG previews, and DDS files recorded in:

- `docs/assets/achievement_icons_chaos_redux/manifest.md`

Holy Realm achievement icon sets use the same three-file pattern and are intentionally maintained separately:

- `29_the_lamps_remain_lit_achievement`
- `30_mandala_of_nations_achievement`
- `31_mountain_circle_by_vow_achievement`
- `32_mandate_without_a_sword_achievement`
- `33_register_without_edges_achievement`
- `34_empty_mandala_achievement`
