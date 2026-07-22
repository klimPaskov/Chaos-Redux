# NZL Lifeboat State icon generation record

Source mode for every newly made icon in this record is the Codex official ImageGen built in tool. Each source master is retained as its own PNG. The source masters use a flat green chroma key for focus, idea, decision, mission, and category icons. Achievement source masters use an opaque achievement badge surface.

## Focus masters retained from interrupted work

The 24 focus masters in `source_masters/focus/` were retained after visual review because each has a distinct maritime, civic, agricultural, navigation, or security subject. The interrupted package did not retain the original per prompt text. They are recorded as retained WIP ImageGen source masters and were processed to the fixed `94x86` target without cross family reuse.

## Idea prompts

Each row is a separate prompt and source master. The subject is designed as a compact HOI4 national spirit symbol with strong outline, painterly aged texture, no text, no flag copy, no protected humanitarian emblem, and readability at `64x64`.

| Source master | Subject brief |
| --- | --- |
| `idea_fallout_nzl_empty_harbors_source.png` | Empty wharf, unlit harbor lamps, slack mooring rope |
| `idea_fallout_nzl_broken_breakwaters_source.png` | Cracked breakwater, beacon lantern, sharp sea spray |
| `idea_fallout_nzl_storm_ports_source.png` | Storm battered port, lit beacon, wave against pilings |
| `idea_fallout_nzl_lifeboat_morality_source.png` | Open lifeboat, balance scale, four star navigation mark |
| `idea_fallout_nzl_open_berth_covenant_source.png` | Open harbor gate, paired lamps, civic rope knot |
| `idea_fallout_nzl_last_berth_doctrine_source.png` | Closed iron gate, guarded beacon, silver four star cross |
| `idea_fallout_nzl_berth_riots_source.png` | Splintered berth board, crossed dock hooks, warning flare |
| `idea_fallout_nzl_dairy_rations_source.png` | Milk can, ration scoop, rail token |
| `idea_fallout_nzl_dairy_relief_fleet_source.png` | Small cargo boat carrying milk cans and a rescue pennant |
| `idea_fallout_nzl_spoiled_stores_source.png` | Dented milk can, dark leak, wilted grain sprig |
| `idea_fallout_nzl_improvised_sea_guard_source.png` | Battered patrol cutter, signal lamp, rope shield |
| `idea_fallout_nzl_splintered_patrols_source.png` | Cracked compass, separated signal flags, broken wake |
| `idea_fallout_nzl_lifeboat_navy_source.png` | Rescue cutter, bright wave, silver four star mark |
| `idea_fallout_nzl_two_island_supply_ring_source.png` | Two linked islands, rope and rail loop, crane hook |

## Decision and mission prompts

Each row is a separate prompt and source master. The subject is simplified for `32x32` readability with a dark outline and no generated text.

| Source master | Subject brief |
| --- | --- |
| `decision_fallout_nzl_wellington_breakwater_works_source.png` | Stone seawall block, repair hammer, wave crest |
| `decision_fallout_nzl_auckland_storm_port_works_source.png` | Harbor crane hook, rain slash, wave |
| `decision_fallout_nzl_milk_rail_assignments_source.png` | Milk can, rail wheel, short track line |
| `decision_fallout_nzl_fishery_quota_compact_source.png` | Fish, tied net, brass tally token |
| `decision_fallout_nzl_weather_station_chain_source.png` | Radio mast, cloud, angled signal rays |
| `decision_fallout_nzl_port_militia_drill_source.png` | Harbor shield, training oar, lifeboat bell |
| `decision_fallout_nzl_convoy_volunteer_corps_source.png` | Escort cutter, white wake, volunteer band shape |
| `decision_fallout_nzl_armed_rescue_cutters_source.png` | Rescue boat, spotlight, protective prow plate |
| `decision_fallout_nzl_refugee_fleet_admission_source.png` | Two lifeboats approaching an open harbor lamp |
| `decision_fallout_nzl_last_berth_closure_source.png` | Closed iron gate, guarded harbor lamp |
| `decision_fallout_nzl_offer_rescue_passage_source.png` | Lifebuoy, blue wave, rope toward a second boat |
| `decision_fallout_nzl_anti_piracy_bearing_source.png` | Compass needle, hostile wake, signal lamp |

## Dedicated dormant-pilot decision prompts

These six source masters were generated independently for the dormant New Zealand Lifeboat State Fallout pilot. Each uses the built-in ImageGen workflow on a flat `#00ff00` chroma-key field, then receives mechanical alpha removal, square framing, and `32x32` Lanczos processing. No existing NZL decision icon is reused.

| Source master | Subject brief |
| --- | --- |
| `decision_fallout_nzl_mobilize_home_guard_state_source.png` | Steel defensive shield, coastal watchtower, upright infantry rifle, and stacked ammunition crates; controlled home-guard mobilization and state defense. |
| `decision_fallout_nzl_dispatch_dairy_relief_convoy_source.png` | Cargo launch carrying a bright milk can in a strapped relief crate, with paired blue/red convoy pennants; bilateral dairy aid and convoy dispatch. |
| `decision_fallout_nzl_rebuild_partner_relief_port_source.png` | Brass crane lifting a stone pier block above a damaged seawall, with relief crate and lifebuoy; engineering and humanitarian port rebuilding. |
| `decision_fallout_nzl_guarantee_relief_partner_source.png` | Large protective shield around an open lifeboat, interlocking brass rings, and navigation star; guarantee and partner protection. |
| `decision_fallout_nzl_revoke_raider_access_source.png` | Barred iron harbor gate, snapped chain, hooked pirate grapnel, and crimson cancellation bar; revoke a stored raider's access. |
| `decision_fallout_nzl_quiet_seas_patrol_source.png` | Armored patrol cutter circling calm water, searchlight sweeping one hostile wake; bounded anti-piracy surveillance patrol. |

## Decision category prompt

`decision_category_fallout_nzl_lifeboat_source.png` combines a brass harbor lantern, a folded ration ledger, and a small four star navigation mark. It is a separate category composition and is processed to `52x40`.

## Achievement prompts

The three completed masters are separate opaque HOI4 achievement badge compositions at `64x64`. Grey variants are grayscale conversions of their own completed source. Not eligible variants use the canonical red cross overlay from `assets/vanilla_reference/icons/achievements/overlay.png` over the grey variant.

| Source master | Subject brief |
| --- | --- |
| `achievement_chaosx_fallout_nzl_open_harbors_source.png` | Two open harbor lights, two rescue craft, four star navigation mark |
| `achievement_chaosx_fallout_nzl_closed_seas_source.png` | Closed harbor gate, patrol wake, silver four star cross |
| `achievement_chaosx_fallout_nzl_two_islands_one_lifeboat_source.png` | Two linked islands, milk rail, harbor crane, four star mark |
