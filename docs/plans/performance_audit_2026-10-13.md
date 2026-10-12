# Performance audit, 13 October 2026

The owner authorized C4 in `chaos_redux_restore_plan_2026-10-12.md`: audit recurring work and optimize it without changing gameplay results.
This is the current C4 report and also records the related C7 engine limitation.
The rankings below describe source cost, not measured frame times or campaign benchmarks.
No game was launched.

## Ranked findings and implementation

| Rank | Surface and cost | Result and preservation basis |
| --- | --- | --- |
| 1a | Final Silence `chaosx.nr3.84` repeats hourly and checks the world pending-state set before each random strike. Its current strike budget is 9,999, subject to the existing native loop limit, so one large wave repeats many existence scans. | Count pending flags once per pulse, then decrement that local count after the same random-state strike helper clears its selected flag. Keep the event trigger, candidate filter, selector calls, native loop bound, strike budget and hourly continuation. No persistent registry or new invalidation system is introduced. |
| 1 | Global coordinator in `common/on_actions/chaosx_on_actions_chaos_meter.txt`. Several `any_country` searches run inside an already per-country daily hook, making host lookup quadratic as countries proliferate. | Remove three logically redundant host-existence tests, evaluate local human/host checks before world searches, and cache the valid host scope. A cached country is accepted only while it exists and retains the authoritative host flag. A missing or retired host uses the original search. Daily pulse order, duplicate-host retirement, player switches, AI fallback and monthly outcomes stay identical. |
| 2 | Daily active Death, zombie and world crisis work: unit withering, country casualties, state deaths, economic totals, migration/famine registered state work and active event country pulses. Their native unit counts and registry sizes grow after events fire. | Retain native gameplay cadence. Zombie daily core grants use `every_controlled_state`, which is exactly the previous world-state predicate `is_controlled_by = ROOT`, with the same non-core predicate. Withering, civilian deaths, native engine unit growth and state transfers are real daily outcomes and cannot be moved weekly without changing results. |
| 3 | Event 080 repeats seven controlled-state loops to add airship resistance bands. It also checks aircraft counts by airship region and divisional AA during war. | Fuse the seven resistance passes into one regional controlled-state pass with all seven original bands. The daily crash draw stays before recalculation, each band adds the original one point, and the plane/division/opinion/weather/stability calculations and RNG calls stay unchanged. Regional aircraft and AA checks remain live because war and deployments can change daily. |
| 4 | Scripted GUI properties default to tick updates. The resource-field panel's visibility performs an owned-state scan even when its selected-field pointer already proves a valid active owned field. | Add the already used selected-field validity predicate before the original scan. Its exact trigger includes `resources_found_is_active_field` and `is_owned_by = PREV`, so it is a positive proof of the old condition. Missing, closed, converted, transferred or invalid selection falls back to the original scan. No geometry, art, text, click regions or visibility results change. |
| 5 | Event 044 leader-idea removal iterates all countries for each trailing contender daily and calls removal even on countries without the idea. | Gate removal by `has_idea = leading_space_race`. Countries without the idea need no removal. Ties, leader selection, score maximum and contender membership remain unchanged. The world scan itself stays because replacing it with an incomplete contender cache could miss a holder. |
| 6 | Large historical arrays and event registries: Event 021 review/critical queues, Event 035 active/recovery/global-pressure ledgers, humanitarian active states/countries and historical anchors. | Existing Event 021 registration and review batches have bounds and preserve queue cursors. Depression uses registered countries and pulse dates. Humanitarian processing uses registered states, not daily world-state discovery. Keep those guards, sparse registries and dates. Batching daily migrations/deaths further would alter transfer/death dates. |
| 7 | Event 006 daily carrier overlays and CXT registration hooks. | Existing hooks are country-specific and identity-gated. CXT hooks only register pending carrier tokens, with one-shot guards and no periodic grants. Retain those narrow scopes. |
| 8 | Clone weekly reserve reconciliation, Mengele weekly production, ZIN daily/monthly effects, MON monthly effects, SOV daily reservation, DHO daily pulse and the Master daily player-only update. | Existing scoped or flag guards restrict active work. Clone stocks may arrive by capture or transfer so a never-used cache would miss real content. ZIN deliberately creates three units each wartime day and performs strikes. MON adds its existing monthly units. Reducing those outcomes would change gameplay. |
| 9 | Native automatic-event/MTTH evaluation. | Six files contain sixteen MTTH blocks. No literal one-day MTTH exists. Keep triggers, distributions and the distinction between automatic events and triggered-only one-day dispatches. |

## History and exact-restore scope

C4 is an authorized efficiency fix, not a prose or asset restoration.
The host scans first appear in `c11750f18` and are expanded in `f564e3cdf` and `0720c135c`.
The airship resistance bands exist in the initial `45ccea608` commit.
The hourly Final Silence strike loop was introduced in `dcdb52cb1`.
`ada01f1e2` moved event hooks into their event-owned files without causing these costs.
No text, asset, chance, amount, date, threshold or newly dynamic value was restored or reinterpreted for C4.
The source diffs were reviewed against the current behavior rather than reverting genuinely new mechanics.

## Complete periodic-hook inventory

The source inventory finds 118 active periodic hook blocks in `common/on_actions`, including ten generic per-country daily/weekly/monthly blocks.
Commented hooks are excluded.
The fifty identical independence carrier hook names are grouped below but remain individually present in the inventory.
Helper expansion follows every referenced scripted effect, including guarded branches.
Such reachability is an upper bound on possible work, not a claim that all branches run every day.
In particular, event selection can reach one-shot country creation and world-end transitions that must not be counted as unconditional daily loops.

| Source | Active hooks | Direct helper work or disposition |
| --- | --- | --- |
| `common/on_actions/002_zombie_outbreak_on_actions.txt` | `on_daily`, `on_weekly` | annex_neighboring_dynamic_zombie_outbreaks_to_main, attempt_dynamic_zombie_outbreak, attempt_zombie_mass_evacuation, azl_absorb_smaller_factions, calculate_total_zombie_strength, calculate_zombie_continent_presence, check_main_zombie_continent_rejoin_pressure, force_emergency_anti_zombie_league_formation, play_current_super_event_audio, refresh_dynamic_zombie_country_leader, refresh_zombie_world_threat_source, relocate_isolated_zombie_capital, review_anti_zombie_league_membership_pressure, update_all_zombie_outbreak_chances, weaponized_zombie_expand_against_neighbors, weaponized_zombie_resolve_canonical_standard_neighbor_merges, weaponized_zombie_turn_hostile_to_humans_if_at_war, zombie_process_controlled_state_decay |
| `common/on_actions/003_holy_realm_on_actions.txt` | `on_daily_TIB`, `on_daily_BHU`, `on_daily_NEP` | holy_realm_daily_doctrine_balance_pulse |
| `common/on_actions/006_independence_wave_on_actions_registry.txt` | `on_daily_BEL`, `on_daily_LIT`, `on_daily_KUR`, `on_daily_IRQ`, `on_daily_SYR`, `on_daily_PAL`, `on_daily_EGY`, `on_daily_KUW`, `on_daily_LEB`, `on_daily_ASY`, `on_daily_LBA`, `on_daily_COG`, `on_daily_TNE`, `on_daily_HAI`, `on_daily_DOM`, `on_daily_PUE`, `on_daily_CUB`, `on_daily_JAM`, `on_daily_BAH`, `on_daily_GDL`, `on_daily_BAS`, `on_daily_CHL`, `on_daily_D01 through on_daily_D50` | independence_wave_iw005_refresh_flanders_overlay, independence_wave_iw022_dalmatia_refresh_overlay, independence_wave_iw025_vojvodina_refresh_overlay, independence_wave_iw035_livonia_refresh_overlay, independence_wave_iw059_mesopotamia_refresh_overlay, independence_wave_iw085_cyrenaica_refresh_overlay, independence_wave_iw101_kongo_refresh_overlay, independence_wave_iw102_kuba_refresh_overlay, independence_wave_iw105_loango_refresh_overlay, independence_wave_iw156_moluccan_refresh_overlay, independence_wave_iw196_antilles_refresh_overlay, independence_wave_iw197_mapuche_refresh_overlay, independence_wave_iw204_restoration_refresh_overlay |
| `common/on_actions/006_independence_wave_signature_modules_cxt_on_actions.txt` | `on_daily_CXT` | CXT carrier registration only |
| `common/on_actions/010_death_on_actions.txt` | `on_daily_DTH` | death_run_daily_public_pressure |
| `common/on_actions/012_africa_gods_cxt_on_actions.txt` | `on_daily_CXT` | CXT carrier registration only |
| `common/on_actions/014_cannibalism_on_actions.txt` | `on_daily_CXT` | CXT carrier registration only |
| `common/on_actions/016_alien_infantry_cxt_on_actions.txt` | `on_daily_CXT` | CXT carrier registration only |
| `common/on_actions/016_mengele_paleogenetics_staff_cxt_on_actions.txt` | `on_daily_CXT` | CXT carrier registration only |
| `common/on_actions/018_resources_found_on_actions.txt` | `on_daily_DHO` | resources_found_cave_daily_pulse |
| `common/on_actions/021_random_civil_war_cxt_on_actions.txt` | `on_daily_CXT` | CXT carrier registration only |
| `common/on_actions/023_sov_nuclear_bombs_cxt_on_actions.txt` | `on_daily_CXT` | CXT carrier registration only |
| `common/on_actions/023_sov_nuclear_bombs_on_actions.txt` | `on_daily_SOV` | sov_nuclear_bombs_achievement_refresh_receipts, sov_nuclear_bombs_ai_request_phase_review, sov_nuclear_bombs_apply_routine_maintenance, sov_nuclear_bombs_reconcile_unreturned_native_delivery, sov_nuclear_bombs_refresh_ledger_reconciliation, sov_nuclear_bombs_refresh_strategic_losses, sov_nuclear_bombs_roll_false_warning |
| `common/on_actions/024_video_game_in_sweden_cxt_on_actions.txt` | `on_daily_CXT` | CXT carrier registration only |
| `common/on_actions/026_black_friday_cxt_on_actions.txt` | `on_daily_CXT` | CXT carrier registration only |
| `common/on_actions/027_doctrine_research_cxt_on_actions.txt` | `on_daily_CXT` | CXT carrier registration only |
| `common/on_actions/028_asteroid_incoming_cxt_on_actions.txt` | `on_daily_CXT` | CXT carrier registration only |
| `common/on_actions/029_riches_found_cxt_on_actions.txt` | `on_daily_CXT` | CXT carrier registration only |
| `common/on_actions/031_random_terror_cxt_on_actions.txt` | `on_daily_CXT` | CXT carrier registration only |
| `common/on_actions/032_missiles_cxt_on_actions.txt` | `on_daily_CXT` | CXT carrier registration only |
| `common/on_actions/033_acid_rain_on_actions.txt` | `on_daily_CXT` | CXT carrier registration only |
| `common/on_actions/035_great_depression_cxt_on_actions.txt` | `on_daily_CXT` | CXT carrier registration only |
| `common/on_actions/037_mysterious_population_on_actions.txt` | `on_daily_CXT` | CXT carrier registration only |
| `common/on_actions/039_murder_mystery_on_actions.txt` | `on_daily_CXT` | CXT carrier registration only |
| `common/on_actions/042_equipment_from_heavens_cxt_on_actions.txt` | `on_daily_CXT` | CXT carrier registration only |
| `common/on_actions/044_space_race_on_actions.txt` | `on_daily` | Active major/human technology scores, contender registration and leader-idea cleanup. |
| `common/on_actions/068_zin_on_actions.txt` | `on_daily_ZIN`, `on_monthly_ZIN` | Wartime unit creation and enemy strikes. Monthly enemy reports. |
| `common/on_actions/073_mongols_rise_on_actions.txt` | `on_monthly_MON` | Legacy-of-Khan neighbor wargoals and configured-template monthly unit creation. |
| `common/on_actions/079_the_master_on_actions.txt` | `on_daily` | Human fight-for-minor country popularity snapshot. |
| `common/on_actions/080_airship_on_actions.txt` | `on_daily` | Active airship crash draw and regional resistance, planes, divisional AA, opinion, stability and weather contributions. |
| `common/on_actions/cbrn_project_equipment_cxt_on_actions.txt` | `on_daily_CXT` | CXT carrier registration only |
| `common/on_actions/cbrn_special_project_cxt_on_actions.txt` | `on_daily_CXT` | CXT carrier registration only |
| `common/on_actions/chaosx_3d_model_pilot_showcase_on_actions.txt` | `on_daily_GER` | chaosx_3d_model_pilot_showcase_activate_country |
| `common/on_actions/chaosx_on_actions_chaos_meter.txt` | `on_daily`, `on_monthly` | add_chaos_meter_value, air_contamination_monthly_update, asteroid_incoming_monthly_dust_update, asteroid_incoming_update_achievements, black_friday_daily_pulse, chaos_meter_daily_update, doctrine_research_evolution_pulse, doctrine_research_reconcile_country_lifecycle, equipment_from_heavens_evolution_pulse, event021_parent_global_scheduler_pulse, fallout_reconcile_coordinator, genocide_initialize_system_if_needed, genocide_monthly_global_pulse, great_depression_play_worldwide_audio_for_player, great_depression_process_active_registry, great_depression_process_global_episode, great_depression_process_recovery_watch, great_depression_update_global_pressure, humanitarian_process_registered_runtime |
| `common/on_actions/chaosx_on_actions_system.txt` | `on_daily` | black_friday_on_event_system_resumed, black_friday_refresh_active_cost_modifier, check_event_timer, fire_event_by_temp_id, log_event_system_debug, random_terror_achievement_daily_tick, random_terror_achievement_record_tag_switch, select_weighted_random_event_id, update_timer_window_dynamic_range |
| `common/on_actions/chaosx_test_country_package_formation_on_actions.txt` | `on_daily_CXT` | CXT carrier registration only |
| `common/on_actions/chaosx_test_country_unit_extension_on_actions.txt` | `on_daily_CXT` | CXT carrier registration only |
| `common/on_actions/clone_system_on_actions.txt` | `on_weekly` | clone_refresh_reserve_manpower |
| `common/on_actions/genocide_crisis_on_actions.txt` | `on_daily_CXT` | CXT carrier registration only |
| `common/on_actions/germany_mengele_clone_on_actions.txt` | `on_weekly` | germany_mengele_weekly_clone_equipment_production |
| `common/on_actions/humanitarian_runtime_on_actions.txt` | `on_daily_CXT` | CXT carrier registration only |
| `common/on_actions/zombie_cure_payload_cxt_on_actions.txt` | `on_daily_CXT` | CXT carrier registration only |

## GUI and MTTH inventory

The GUI audit covers all thirty-three `common/scripted_guis` files, including fixture bindings, event-owned windows, shared settings/log/details surfaces, state-map puzzles and report headers.
Existing dirty bindings belong to the cannibalism network, disease containment board and fallout blackout panel.
Their effects invalidate the dirty variables at corresponding mutations.
Dirty updates govern properties, while visibility still evaluates independently, so adding a dirty token would not eliminate the resource-panel visibility scan.
No blind global dirty binding was added: settings, costs, selected targets, flags, arrays and native values require complete invalidation or controls can become stale.
The resource panel's go-to enabled trigger already has the selected-field fast path that visibility lacked.
Its fallback scan remains to preserve valid fields whose selection needs reconciliation.
Indirect trigger expansion finds conditional scans in the camp ledger, settings scenario controls, event-log fireability and formable category checks.
Camp availability reaches controlled-state and registered-site array checks.
Scenario launch checks can reach up to twelve state-capacity count queries for cannibalism and up to fifteen sponsor-country checks for the secret alliance, but only for the selected scenario menu branch.
Random-faction fireability can nest country and controlled-state queries while its detail is selected.
Some formable category checks search country cosmetic identities.
These exact availability predicates remain live because country ownership, war, rosters and operational sites can change outside the GUI.
Replacing them with an incompletely invalidated negative cache would change player choices.
The disease-containment GUI is currently hidden, so its reachable scan helpers are not counted as an active presentation cost.

## Recurring event jobs

The specialist's corrected literal event scan found 4,308 top-level event definitions and 2,263 literal event-dispatch edges.
Its direct delayed-recursion roots are grouped here, with option-only transitions separated from unconditional polling.
The parent also traces registered jobs and delayed scheduling through scripted effects rather than treating the literal graph as complete helper coverage.

| Root | Scope, guard and cadence |
| --- | --- |
| `chaosx.nr3.82`, `.84` | Active, uninterrupted Final Silence. Wave-days gameplay pulse and hourly pending-strike pulse. The hourly repeated existence scans are optimized above. |
| `chaosx.nr7.20`, `chaosx.nr8.20`, `chaosx.nr38.5` | A continuing Fury, thin-wire or Malta actor. Existing weekly/configured actor cadence retained. |
| `chaosx.nr12.307`, `africa_world_package.106/.206/.760` | A pending AI overlay, player-selected prolonged review or one retained confidence partner pair. No global polling added. |
| `chaosx.nr15.150`, `chaosx.nr16.902` | Utopia actor reconciliation and pending actor-target cleanup while the super-event is visible. |
| `chaosx.nr23.181/.120`, `chaosx.nr28.12` | Pending reactor construction/ultimatum or one raised repair-cost state. Existing stop conditions and delays retained. |
| `bio_countermeasure.1`, `cbrn_bio_safety.1`, `cbrn_delivery.1` through `.4`, `cbrn_protection.1` | Local border cleanup, arsenal monitor, state expiry/recovery/evidence/deaths or country protection maintenance. These are scheduled local jobs guarded by active state or equipment/program context. |
| `germany_mengele.20/.32/.36/.38` and `.17` with `.20` | Conditional program retries. `.20` can dispatch `.17` after one day, but `.17` returns after ninety days and `.20` self-retries use longer variable delays. This is not daily polling. |
| Event 021, 026, 027, 031, 035, 042 and humanitarian helper-scheduled jobs | Existing host pulses and registered actors/states, as described in the hook and registry audit. Terror's global callback stall is repaired separately by C5. |

Dynamic `meta_effect` event IDs and non-event callbacks are not literal graph edges.
The direct recurrence analysis initially misclassified nested dispatch payloads as definitions, was corrected to top-level event blocks, and only the corrected results above are accepted.

The sixteen MTTH blocks are zombie `chaosx.nr2.3/.4/.5/.7/.8/.11`, missile evolutions `chaosx.nr32.201` through `.205`, Ireland `chaosx.nr72.4`, two Germany-Mengele events, one easter egg and the weaponized-zombie accident.
Event 032's two-day base multiplied by 0.5 retains its existing variable median, so it is unchanged.
The one-day triggered-only dispatches in Events 041, 043, 044 and 045 are not daily polling and retain their delays.

## Helper-scheduled callback inventory

The effect-expanded source inventory finds 133 event roots with a reachable delayed dispatch back to the same event ID.
This includes conditional retries, finite presentation queues and clock transitions that share a scheduler, so it is a candidate inventory rather than 133 unconditional polls.
Each original delay is retained.
Actor/state maintenance jobs use their package active/pending conditions, and finite queue jobs stop when the queue is empty or their phase advances.
This supplements the direct event graph and includes communism maintenance, progressive release, independence statehood incidents, Death spreading, secret alliance operations, cannibalism actor/hoard checks, infantry compaction, plague/acid-rain workers, camp monitors, country resource pulses, sanctions and Fallout phase dispatch.
The hourly Final Silence existence scan is the changed helper-free job.
Fallout's phase callbacks already use phase state and scheduled flags, and replacing those guarded terminal jobs with a different cadence would change their output timing.
The following exact event/helper map records all candidate roots so future profiling can select a concrete package without rediscovering them.

| Event root | Owning source and reachable self-dispatch helpers |
| --- | --- |
| `chaosx.nr1.20` | `events/001_communism_spread.txt:956`: `queue_communism_spread_maintenance` |
| `chaosx.nr3.82` | `events/003_the_holy_realm.txt:1011`: `country_event` |
| `chaosx.nr3.84` | `events/003_the_holy_realm.txt:1056`: `country_event` |
| `chaosx.nr5.128` | `events/005_soviet_collapse.txt:305`: `soviet_collapse_queue_objective_refill` |
| `chaosx.nr5.129` | `events/005_soviet_collapse.txt:327`: `soviet_collapse_schedule_next_progressive_release_check` |
| `chaosx.nr006.9810` | `events/006_independence_wave_iw098_succession_events.txt:12`: `independence_wave_iw098_queue_succession_check` |
| `chaosx.nr6.150` | `events/006_independence_wave_statehood_incident_events.txt:20`: `independence_wave_queue_statehood_incident_pulse` |
| `chaosx.nr6.40` | `events/006_independence_wave_support_events.txt:75`: `independence_wave_join_schedule_retry` |
| `chaosx.nr7.20` | `events/007_fury.txt:82`: `country_event`, `fury_apply_package` |
| `chaosx.nr8.20` | `events/008_tensions_rising.txt:324`: `country_event` |
| `chaosx.nr10.10` | `events/010_death.txt:146`: `death_schedule_spread_pulse_early_max`, `death_schedule_spread_pulse_early_mid`, `death_schedule_spread_pulse_early_min`, `death_schedule_spread_pulse_initial_max`, `death_schedule_spread_pulse_initial_mid`, `death_schedule_spread_pulse_initial_min`, `death_schedule_spread_pulse_late_max`, `death_schedule_spread_pulse_late_mid`, `death_schedule_spread_pulse_late_min`, `death_schedule_spread_pulse_mid_max`, `death_schedule_spread_pulse_mid_mid`, `death_schedule_spread_pulse_mid_min`, `death_schedule_spread_pulse_revealed`, `death_schedule_spread_pulse_world_end` |
| `chaosx.nr11.2` | `events/011_secret_alliance.txt:59`: `secret_alliance_schedule_next_concealed_pulse` |
| `chaosx.nr11.54` | `events/011_secret_alliance.txt:691`: `secret_alliance_verify_liaison_objective` |
| `chaosx.nr11.55` | `events/011_secret_alliance.txt:692`: `secret_alliance_verify_courier_objective` |
| `chaosx.nr11.56` | `events/011_secret_alliance.txt:693`: `secret_alliance_verify_clerk_objective` |
| `chaosx.nr11.57` | `events/011_secret_alliance.txt:694`: `secret_alliance_verify_envoy_objective` |
| `chaosx.nr11.58` | `events/011_secret_alliance.txt:695`: `secret_alliance_verify_safehouse_objective` |
| `chaosx.nr11.59` | `events/011_secret_alliance.txt:696`: `secret_alliance_verify_manhunt_objective` |
| `chaosx.nr11.60` | `events/011_secret_alliance.txt:697`: `secret_alliance_verify_rumor_objective` |
| `chaosx.nr11.190` | `events/011_secret_alliance.txt:711`: `secret_alliance_schedule_revealed_war_pulse` |
| `chaosx.nr12.1211` | `events/012_african_union.txt:543`: `africa_load_continental_focus_tree` |
| `chaosx.nr12.307` | `events/012_african_union.txt:978`: `country_event` |
| `chaosx.nr12.313` | `events/012_africa_diaspora_protocol.txt:109`: `africa_diaspora_open_withdrawal_review` |
| `chaosx.nr12.400` | `events/012_africa_evolutions.txt:4`: `africa_schedule_next_evolution_clock` |
| `chaosx.nr12.600` | `events/012_africa_gods_of_africa.txt:13`: `gods_of_africa_schedule_current_clock` |
| `chaosx.nr12.606` | `events/012_africa_gods_of_africa.txt:116`: `gods_of_africa_schedule_current_clock` |
| `chaosx.nr12.607` | `events/012_africa_gods_of_africa.txt:127`: `gods_of_africa_schedule_current_clock` |
| `africa_world_package.106` | `events/012_africa_world_package_crossroads_europe.txt:236`: `country_event` |
| `africa_world_package.206` | `events/012_africa_world_package_crossroads_europe.txt:489`: `country_event` |
| `africa_world_package.760` | `events/012_africa_world_package_union_war.txt:1019`: `country_event` |
| `chaosx.nr13.2` | `events/013_natural_disasters.txt:68`: `natural_disaster_enqueue_state_job` |
| `chaosx.nr13.5` | `events/013_natural_disasters.txt:124`: `natural_disaster_cleanup_super_event_target`, `natural_disaster_dispatch_queued_super_event` |
| `chaosx.nr13.8` | `events/013_natural_disasters.txt:146`: `natural_disaster_schedule_super_event_retry` |
| `chaosx.nr13.100` | `events/013_natural_disasters.txt:223`: `natural_disaster_schedule_report_dispatch` |
| `chaosx.nr14.10` | `events/014_cannibalism.txt:81`: `cannibalism_schedule_current_pulse_after_delay` |
| `chaosx.nr14.82` | `events/014_cannibalism.txt:1384`: `cannibalism_schedule_hoard_review` |
| `chaosx.nr15.207` | `events/015_utopia_manifesto.txt:4188`: `utopia_manifesto_schedule_association_review` |
| `chaosx.nr15.150` | `events/015_utopia_manifesto.txt:6339`: `country_event` |
| `chaosx.nr16.6` | `events/016_brilliant_scientist_directorate_outcomes.txt:89`: `brilliant_scientist_dispatch_next_breakthrough_report` |
| `chaosx.nr16.90` | `events/016_brilliant_scientist_evolutions.txt:793`: `brilliant_scientist_schedule_next_evolution_check` |
| `chaosx.nr16.300` | `events/016_brilliant_scientist_super_events.txt:9`: `brilliant_scientist_schedule_super_event_queue_retry` |
| `chaosx.nr16.901` | `events/016_brilliant_scientist_super_events.txt:21`: `brilliant_scientist_mengele_schedule_singularity_fallout_retry`, `brilliant_scientist_schedule_singularity_fallout_retry` |
| `chaosx.nr16.902` | `events/016_brilliant_scientist_super_events.txt:60`: `country_event` |
| `chaosx.nr16.52` | `events/016_dhrondan_country_events.txt:264`: `dhrondan_schedule_compact_expiry` |
| `chaosx.nr18.82` | `events/018_random_resource.txt:2531`: `resources_found_cave_attack_adjacent_state_actors` |
| `chaosx.nr19.900` | `events/019_infantry_spawn.txt:743`: `infantry_spawn_run_country_pulse`, `infantry_spawn_schedule_country_pulse` |
| `chaosx.nr19.901` | `events/019_infantry_spawn.txt:755`: `infantry_spawn_schedule_achievement_continuity_pulse` |
| `chaosx.nr19.916` | `events/019_infantry_spawn.txt:831`: `infantry_spawn_schedule_annex_cleanup_retry` |
| `chaosx.nr19.954` | `events/019_infantry_spawn_scenario.txt:88`: `infantry_spawn_scenario_retry_pending_rollback_cleanup` |
| `chaosx.nr19.955` | `events/019_infantry_spawn_scenario.txt:98`: `infantry_spawn_scenario_schedule_same_tag_rollback_retry` |
| `chaosx.nr20.900` | `events/020_black_death.txt:90`: `black_plague_schedule_next_pulse` |
| `chaosx.nr22.3` | `events/022_concentration_camps.txt:395`: `concentration_camps_monitor_tick` |
| `chaosx.nr23.180` | `events/023_soviet_nukes.txt:66`: `sov_nuclear_bombs_schedule_evolution_check` |
| `chaosx.nr23.181` | `events/023_soviet_nukes.txt:84`: `country_event` |
| `chaosx.nr23.182` | `events/023_soviet_nukes.txt:105`: `sov_nuclear_bombs_ai_route_existing_phase` |
| `chaosx.nr23.120` | `events/023_soviet_nukes.txt:783`: `country_event` |
| `chaosx.nr24.90` | `events/024_hearts_of_iron.txt:3559`: `video_game_in_sweden_maintenance` |
| `chaosx.nr24.91` | `events/024_hearts_of_iron.txt:3571`: `video_game_in_sweden_start_runtime_watch` |
| `chaosx.nr25.280` | `events/025_alien_technology_in_antarctica.txt:648`: `chaosx_nr25_schedule_participant_pulse` |
| `chaosx.nr25.281` | `events/025_alien_technology_in_antarctica.txt:1225`: `chaosx_nr25_schedule_holder_pulse` |
| `chaosx.nr27.14` | `events/027_doctrine_research.txt:25`: `doctrine_research_schedule_country_batch_wake` |
| `chaosx.nr28.9` | `events/028_asteroid_impact.txt:1200`: `asteroid_incoming_schedule_next_fragment_visual` |
| `chaosx.nr28.10` | `events/028_asteroid_impact.txt:1212`: `asteroid_incoming_schedule_news_delivery` |
| `chaosx.nr28.11` | `events/028_asteroid_impact.txt:1220`: `asteroid_incoming_present_impact_super_event` |
| `chaosx.nr28.12` | `events/028_asteroid_impact.txt:1230`: `country_event` |
| `chaosx.nr29.900` | `events/029_riches_found.txt:277`: `riches_found_schedule_controller_pulse` |
| `chaosx.nr29.910` | `events/029_riches_found.txt:393`: `riches_found_queue_report` |
| `chaosx.nr30.30` | `events/030_time_traveler.txt:1473`: `time_traveler_next_rival_turn`, `time_traveler_start_rival_chain` |
| `chaosx.nr30.40` | `events/030_time_traveler.txt:1857`: `time_traveler_next_rumor` |
| `chaosx.nr30.100` | `events/030_time_traveler_evolutions.txt:19`: `time_traveler_try_ambition` |
| `chaosx.nr30.200` | `events/030_time_traveler_figures.txt:14`: `time_traveler_figure_tick` |
| `chaosx.nr31.13` | `events/031_terrorist_attack.txt:417`: `random_terror_ask_dominant_actor` |
| `chaosx.nr31.92` | `events/031_terrorist_attack.txt:669`: `random_terror_schedule_next_evolution` |
| `chaosx.nr31.95` | `events/031_terrorist_attack.txt:705`: `random_terror_schedule_revelation_commit` |
| `chaosx.nr31.98` | `events/031_terrorist_attack.txt:797`: `random_terror_schedule_terminal_check` |
| `chaosx.nr31.96` | `events/031_terrorist_attack.txt:811`: `random_terror_schedule_country_pulse` |
| `chaosx.nr31.97` | `events/031_terrorist_attack.txt:825`: `random_terror_schedule_recovery_check` |
| `chaosx.nr32.192` | `events/032_missiles_evolution_events.txt:137`: `missiles_notify_evolution_change` |
| `chaosx.nr32.190` | `events/032_missile_crisis.txt:62`: `missiles_queue_evolution_job` |
| `chaosx.nr32.82` | `events/032_missile_crisis.txt:502`: `missiles_schedule_warning_response` |
| `chaosx.nr32.90` | `events/032_missile_crisis.txt:537`: `chaosx_032_achievement_record_long_reach_snapshot` |
| `chaosx.nr33.20` | `events/033_acid_rain.txt:72`: `acid_rain_bind_host_and_schedule_worker` |
| `chaosx.nr33.41` | `events/033_acid_rain.txt:356`: `acid_rain_033_achievement_schedule_deadline`, `acid_rain_project_country_obligations` |
| `chaosx.nr34.4` | `events/034_industrial_boom.txt:110`: `industrial_boom_deliver_collapse_snapshot` |
| `chaosx.nr34.5` | `events/034_industrial_boom.txt:126`: `industrial_boom_schedule_pulse` |
| `chaosx.nr35.7` | `events/035_great_depression.txt:158`: `great_depression_schedule_civilian_commitment_review` |
| `chaosx.nr36.80` | `events/036_chemical_and_biological_weapons_convention.txt:688`: `cbrn_convention_start_pulse` |
| `chaosx.nr37.6` | `events/037_mysterious_population.txt:32`: `mysterious_people_schedule_pulse` |
| `chaosx.nr38.5` | `events/038_malta_crusaders.txt:224`: `country_event` |
| `chaosx.nr39.90` | `events/039_murder_mystery.txt:783`: `murder_mystery_schedule_pulse` |
| `chaosx.nr40.5` | `events/040_lawrence_of_arabia.txt:148`: `lawrence_schedule_pulse` |
| `chaosx.nr40.6` | `events/040_lawrence_of_arabia.txt:160`: `lawrence_try_next_target` |
| `chaosx.nr40.27` | `events/040_lawrence_of_arabia.txt:172`: `lawrence_watchdog` |
| `chaosx.nr40.140` | `events/040_lawrence_of_arabia_federation.txt:284`: `lawrence_federal_tick` |
| `chaosx.nr42.9` | `events/042_equipment_from_heavens.txt:66`: `equipment_from_heavens_dispatch_next_report` |
| `chaosx.nr42.30` | `events/042_equipment_from_heavens.txt:245`: `equipment_from_heavens_achievement_tiny_pulse` |
| `chaosx.nr42.31` | `events/042_equipment_from_heavens.txt:256`: `equipment_from_heavens_achievement_nightmare_pulse` |
| `bio_countermeasure.1` | `events/biological_countermeasure_events.txt:14`: `country_event` |
| `cbrn_bio_facility.1` | `events/biological_facility_capture_events.txt:13`: `bio_facility_capture_schedule_hazard_check` |
| `cbrn_bio_lifecycle.21` | `events/biological_lifecycle_events.txt:97`: `bio_strategic_raid_decay_attempt_evidence` |
| `cbrn_bio_safety.1` | `events/biological_stockpile_safety_events.txt:16`: `country_event` |
| `camp_administration_country.2` | `events/camp_administration_country_events.txt:13`: `camp_rework_schedule_country_timer` |
| `cbrn_delivery.1` | `events/cbrn_chemical_delivery_events.txt:15`: `state_event` |
| `cbrn_delivery.2` | `events/cbrn_chemical_delivery_events.txt:77`: `state_event` |
| `cbrn_delivery.3` | `events/cbrn_chemical_delivery_events.txt:115`: `state_event` |
| `cbrn_delivery.4` | `events/cbrn_chemical_delivery_events.txt:155`: `state_event` |
| `cbrn_occupation.2` | `events/cbrn_occupation_events.txt:27`: `cbrn_occupation_decay_state_trauma` |
| `cbrn_protection.1` | `events/cbrn_protection_events.txt:14`: `cbrn_start_protection_maintenance_job`, `country_event` |
| `chaosx.event_clusters.2` | `events/chaosx_event_clusters.txt:9`: `event_cluster_schedule_next_pending_member` |
| `condemnation_sanctions.1` | `events/condemnation_sanctions_events.txt:11`: `condemnation_monthly_human_pulse_internal`, `condemnation_start_targeted_pulse_apply` |
| `chaosx.fallout.62` | `events/fallout_world_end_events.txt:16251`: `fallout_orientation_dispatch_selected_event` |
| `chaosx.fallout.63` | `events/fallout_world_end_events.txt:16301`: `fallout_orientation_dispatch_selected_event` |
| `chaosx.fallout.66` | `events/fallout_world_end_events.txt:16412`: `fallout_orientation_dispatch_selected_event` |
| `chaosx.fallout.67` | `events/fallout_world_end_events.txt:16462`: `fallout_orientation_dispatch_selected_event` |
| `chaosx.fallout.70` | `events/fallout_world_end_events.txt:16544`: `fallout_orientation_dispatch_selected_event` |
| `chaosx.fallout.71` | `events/fallout_world_end_events.txt:16595`: `fallout_orientation_dispatch_selected_event` |
| `chaosx.fallout.74` | `events/fallout_world_end_events.txt:16680`: `fallout_orientation_dispatch_selected_event` |
| `chaosx.fallout.75` | `events/fallout_world_end_events.txt:16731`: `fallout_orientation_dispatch_selected_event` |
| `chaosx.fallout.78` | `events/fallout_world_end_events.txt:16789`: `fallout_orientation_dispatch_selected_event` |
| `chaosx.fallout.79` | `events/fallout_world_end_events.txt:16858`: `fallout_orientation_dispatch_selected_event` |
| `chaosx.fallout.82` | `events/fallout_world_end_events.txt:16906`: `fallout_orientation_dispatch_selected_event` |
| `chaosx.fallout.83` | `events/fallout_world_end_events.txt:17092`: `fallout_orientation_dispatch_selected_event` |
| `chaosx.fallout.1001` | `events/fallout_world_end_events.txt:20917`: `fallout_schedule_current_transition_phase` |
| `chaosx.fallout.1002` | `events/fallout_world_end_events.txt:20931`: `fallout_schedule_current_transition_phase` |
| `chaosx.fallout.1003` | `events/fallout_world_end_events.txt:20945`: `fallout_schedule_current_transition_phase` |
| `chaosx.fallout.1004` | `events/fallout_world_end_events.txt:20959`: `fallout_schedule_current_transition_phase` |
| `chaosx.fallout.1005` | `events/fallout_world_end_events.txt:20973`: `fallout_schedule_current_transition_phase` |
| `chaosx.fallout.1006` | `events/fallout_world_end_events.txt:20987`: `fallout_schedule_current_transition_phase` |
| `chaosx.fallout.1007` | `events/fallout_world_end_events.txt:21001`: `fallout_schedule_current_transition_phase` |
| `germany_mengele.20` | `events/germany_mengele.txt:583`: `country_event` |
| `germany_mengele.32` | `events/germany_mengele.txt:794`: `country_event` |
| `germany_mengele.36` | `events/germany_mengele.txt:880`: `country_event` |
| `germany_mengele.38` | `events/germany_mengele.txt:917`: `country_event` |

## Evidence and validation

The host lookup model compared original and optimized branch conditions for 9,100 cases with one to five countries, human/AI combinations, absent/duplicate hosts and valid/missing/stale cached pointers.
It also removes each possible host and compares the fallback dispatch order.
The optimized and original branches dispatch the same countries in the same order.
For a representative one-human-host/99-AI country pass with a valid cache, the three host-lookup predicates perform 298 world searches before this change and zero after it.
The host's original duplicate-retirement pass remains, as do all gameplay scans.
This is an operation-count model, not an observed speed measurement.
Forty-two regional/resistance boundary cases preserve the exact seven-band airship contribution.
Final Silence's local count follows the selected helper's exact single-flag removal, so every random selection has the original pending set and every continuation has the original remaining-state condition.
The original native loop cap is retained, including a wave with more than one thousand pending states.
One hundred thirty-five modeled Final Silence scenarios compare selected-state sequences and continuation with pending counts from zero through twelve hundred, budgets from zero through 9,999 and three fixed seeds.
They retain the same random selection calls and the same native limit.
The independent probability reviewer accepted the five initial C4 changes from the owned commit diff.
Its direct-random analysis gave 1%, 7% and 37% for matching `as_crash_chance` inputs, with no change to that chance expression.
The scenario/source artifact identities are retained in the task's temporary evidence and do not represent observed engine outcomes.
The field-visibility equivalence follows from the exact selected-state active/ownership predicate, with the original scan retained for negative cache results.

Reference tools were confirmed exposed before use.
`reference_context`, `reference_search`, `reference_read` and `source_lookup` were requested for relevant installed/offline rules and precedents.
Slow or unavailable optional checks do not establish runtime validation.
The C4 file-mode `script_validate` request timed out after 600 seconds, as did the C5 file-mode request.
The C5 worker owns the single corrected retry against its narrow country-scope reconciliation body.
The C4 effect/source-lookup request and the optional array-trigger search also timed out after 600 seconds.
The global-target wiki section read timed out, so its relevant local lines were read directly.
Installed target/controlled-state sections and both periodic-hook source kinds did return through reference reads.
No failed request is counted as passed, and those failures are not retried under another tool or file name.
A future retry requires a recovered route or a change that addresses the failing input or service condition.

Required source evidence:

- Offline `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md`, lines 96–101, revision `6822adc85a374a1c1364f2def6f32c6d66da9fb0280319ddd6af4b84b33d882a`: generic periodic hooks run for every country, tagged hooks run only their country.
- Installed `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/on_actions/_documentation.md`, lines 7–19, revision `876be96cab02a3eaa9a133891bea5f963f8980aa4a794f759c1b30f87d2663c4`: supported daily/weekly/monthly tagged hooks.
- Installed `documentation/effects_documentation.md`, lines 3800–3819, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`: country-scoped `every_controlled_state` visits controlled states satisfying its limit.
- Offline `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`, lines 811–814, revision `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49`: controlled-state iterator is the optimized equivalent of the world-state controller predicate.
- Installed `documentation/effects_documentation.md`, lines 6505–6513, same effects revision: global event targets preserve a scope pointer.
- Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, lines 270–302, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`: global targets persist and require lifecycle care.
- Installed `common/scripted_guis/_documentation.md`, lines 102–105, revision `43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838`: tick property updates and dirty-variable invalidation.
- Offline `paradox_wiki/Scripted GUI modding - Hearts of Iron 4 Wiki.md`, lines 165–173: dirty updates do not cache visibility.
- Offline `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`, lines 130–132: automatic event trigger and MTTH evaluation.
- Vanilla `common/on_actions/00_on_actions.txt`, lines 5717–5727: a controlled-state iterator applies scoped effects to states satisfying its limit.

## Remaining limits

No live-game profiling or wall-clock speedup is claimed.
There are no timing reductions or gameplay simplifications in the implemented C4 changes.
Expensive actual unit simulation, battle AI, daily unit creation and native state effects remain because the owner explicitly requires identical gameplay results.
Additional cadence or population reductions are outside this task.
No new icons, portraits, textures, audio or localisation were required.
The event catalogue wording and gameplay design are unchanged.
Code commit `343417bd35b9505ecabce62b25d402b15e9a11ab` contains the five initial performance surfaces and excludes the preexisting equipment-evolution and nonhuman changes in the shared working tree.
Its command-line title was truncated during publication.
A guarded title-only correction was refused because another agent had already advanced HEAD, so published shared ancestry was preserved.
Skills used: `chaos-redux-shared-git-commit`, `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-scripted-gui`, `chaos-redux-super-events`, and the probability review's `chaos-redux-ai-strategies` and `chaos-redux-mtth` guidance.
No skills were created or changed.

## C7 audio cancellation evidence

Disposition: unresolved.
The sound-only routing change is `99f0b18dda24febf6fc233b61b4b0b1cd0eaea90`.
Its exact parent diff deletes `play_dynamic_super_event_music`, removes the music-mode branch and routes every super-event through sound effects.
The prior music helper used `scoped_play_song = "chaosx_super_event_[SUPER_EVENT_ID]_[VOLUME_SUFFIX]"`.
The later `a65b6cce6` removes unused OGG assets, while `89e9d2d9f` restores only the default and world-revolution music tracks.
The A3 `10292700c22304f1181b96733b797d2faf681a25` recording restoration does not change playback routing.

The present `play_dynamic_super_event_sound` chooses a distinct wrapper for each audio ID and volume in `sound/chaosx_sound.asset`.
Each wrapper has its own `max_audible = 1` and `max_audible_behaviour = fail`.
Those limits apply per soundeffect, so a second ID or volume can overlap the first cue.
Reusing the same wrapper rejects the next instance and leaves the first running.
The x0 branch performs no action, so a muted next event also cannot cancel an existing cue.
The super-event close GUI clears visibility and the selected audio ID without stopping playback.
The shared settings-aware helper is called from more than thirty event/system files, so a fix needs to cover the shared channel rather than one event.

Required audio evidence:

- Offline `paradox_wiki/Sound modding - Hearts of Iron 4 Wiki.md`, lines 40–119, revision `904c1909fcb8a6ac3d3f6bb5286eca216bb996513a3bc0788f12f96ab7cc6e4f`: per-soundeffect instance limits and the documented fail behavior.
- Installed `documentation/effects_documentation.md`, lines 6514–6531 and 7981–7989, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`: song and sound playback APIs, without a stop/cancel operation.
- `reference_search` for `stop_sound` returned no results, and a completed `source_lookup` returned no definitions or usages at index revision `44bd95178aef31c89c49ef3bd36b4642b62bc8243332b205ae0c5560fcbd7e23`.
- Vanilla and the available approved Workshop sound assets did not provide a replacement/cancel behavior for `max_audible_behaviour`.
- Vanilla and Kaiserreich `scoped_play_song` precedents establish playback, but do not establish immediate replacement, same-ID restart or the muted-next-event case.

No exact supported cancellation mechanism was found in the inspected engine references.
The old music route cannot stop a running SFX and is not source evidence for the complete C7 behavior.
No audio files, images, sound definitions or routes were replaced as an unverified substitute.
C7 remains incomplete because immediate cancellation of a currently playing sound effect needs an evidenced engine capability that these sources do not supply.
No live audio interruption check was performed and neither game was launched.
