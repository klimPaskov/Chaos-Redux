# Event 097 Collaboration: Scripted Architecture Plan

Role: `chaosx_scripted_system_architect`, plan mode granted by the parent for this task. Date: 2026-10-06.
Disposition: `unresolved`. This plan proposes scripted architecture for the accepted-for-planning design in `docs/specs/097_collaboration_specs/`. It records no user decision and no parent acceptance, and the parent decides which parts become accepted design.
Evidence class: source review of the repository at commit `5212636e`, the newer skill texts in the session upload folder, the offline wiki snapshot in `paradox_wiki/`, and the Event 097 specs.
Spec parts 1, 2, 3, 4, and 5 and the Chaos impact and edge case matrices changed on disk during this pass, and the latest versions were re-read before writing (part 4 at 14:53).
No gameplay, script, localisation, interface, decision, event, on_action, constant, or idea file was edited. This file is the only write.

Every repository identifier below was seen in the cited file at the cited line. Identifiers written in `collaboration_*`, `chaosx.nr97.<n>`, or `097_collaboration_*` form that are not followed by a citation are proposals of this plan and do not exist yet.

## Recorded blockers

1. The `hoi4_agent_tools` MCP server failed to connect in this session because its executable `cmd.exe` is not available on Linux. No `hoi4.event_inspect`, `hoi4.probability_inspect`, render, sweep, or compare evidence exists. Every event chain, MTTH entry, `ai_chance`, and `ai_will_do` surface proposed here still needs the mandatory MCP pass and a `chaosx_ai_probability_auditor` baseline, and this source review does not substitute for either.
2. Vanilla game files and the installed `documentation/` folder are not present in the container. Every engine claim marked "verify" rests on the offline wiki snapshot and repository precedent only. Section 7 lists each one with the design consequence if verification fails.
3. The upload copy of `chaosx_dynamic_effects.md` documents `chaosx_convert_days_to_date_offset` and `chaosx_convert_date_offset_to_days`, but neither helper exists in repository source (a search of `common/` for `date_offset` returns nothing). This plan therefore stores due days as `global.num_days` counters (offline `Data structures` line 1470, repository precedent `common/scripted_effects/035_great_depression_effects.txt:2283-2295`) and never uses encoded dates.

## 0. Key recommendations at a glance

1. Run the application pass as a self-scheduling hidden event chain in one stored owner country, with a beneficiary-outer and host-inner loop. The outer loop is a bounded `for_loop_effect` over the batch slice only, which stays far below the 1,000-iteration cap, and the inner loop is `for_each_scope_loop` over host arrays, which the offline wiki documents as equivalent to an `every_` scope with no iteration cap (`Data structures` line 1217, cap note only on lines 1219-1220).
2. Group hosts by their stance so each beneficiary performs three host sweeps with one precomputed layer value per sweep. Per-pair work is then one native call and one self-exclusion check, and a `meta_effect` fallback (if `add_collaboration` rejects a variable `value`) costs three injections per beneficiary instead of one per pair.
3. Keep the depth ledgers O(N) per firing. Outgoing depth is written once per beneficiary in its batch, and incoming depth once per host at pass completion.
4. Arm evolution MTTH clocks from a new `collaboration_on_chaos_changed` call placed beside the existing `black_friday_on_chaos_changed = yes` call inside `add_chaos_meter_value` (`common/scripted_effects/chaos_meter_effects.txt:4592`), plus 097's own firing and war hooks. Each activation is delivered by one delayed hidden event per evolution. Nothing attaches to the shared host pulse.
5. After an evolution is active, gate its behavior with `has_disabled_current_evolution` only. `is_current_evolution_enabled` (`common/scripted_triggers/chaosx_settings_triggers.txt:55-58`) also tests the Chaos tier through `has_reached_current_evolution_tier` (`:60`), and the spec keeps active evolutions alive when Chaos falls (part 2, Shared pacing and logging).
6. Measure "wars between participants" through an event-driven belligerent registry, because the engine exposes no war object or war counter in the offline wiki. This changes the measured quantity and needs parent acceptance (Q1).
7. Implement every "once per war" guard with small arrays held by the guarded country and cleared in `on_peace`, and every "once per N days" guard with timed flags. Nothing then needs to enumerate targeted flags or variables for cleanup.
8. Route every write to native collaboration through one gate helper that checks the Fallout transition and active flags, so the Fallout clean-world proof can never be blocked by Event 097 (part 5, Fallout).
9. Store installed-government rows as variables on the government, a live global array, and aligned global history arrays. Every creation goes through one installation helper shared by the capitulation offer, B1, and the public API.
10. Charge installation costs only after the vanilla route proves it created a government, because the dynamic-country pool is finite and creation may fail (Section 7, rows V10 and V11).

## 1. File map

### 1.1 New event-owned files

Each new script file starts with a banner overview in the style of `common/scripted_effects/chaosx_logic_effects.txt` (AGENTS.md section 4, rule 12).

| Path | Purpose |
| --- | --- |
| `common/script_constants/097_collaboration_constants.txt` | Identity, shared values, layers, stances, bands, timing, pass budget, MTTH anchors, Chaos magnitudes |
| `common/script_constants/097_collaboration_occupation_constants.txt` | Seats, Open Ministries, prepared cadres, Fifth Column tables, Open Gates |
| `common/script_constants/097_collaboration_government_constants.txt` | Installation thresholds, installer score, routes, auxiliaries, lifecycle, Turned Regime, competing orders, restoration pressure |
| `common/script_constants/097_collaboration_decision_constants.txt` | A1 to A5, B1, and B2 cost anchors, durations, cooldowns, AI anchors |
| `common/scripted_effects/097_collaboration_effects.txt` | Root, opening report, stance capture, owner resolution, application pass, ledgers, belligerent registry, evolution clocks and entries, Chaos rows |
| `common/scripted_effects/097_collaboration_occupation_effects.txt` | Seat helper, seat end, Collaborators Unmasked, Open Ministries, Fifth Column evaluator, Open Gates, prepared cadres, capitulation handler |
| `common/scripted_effects/097_collaboration_government_effects.txt` | Installer selector, installation helper, registry, lifecycle, Contested evaluation, Turned Regime, competing orders, restoration pressure |
| `common/scripted_effects/097_collaboration_decision_effects.txt` | Cost quotes, payment and refund, A1 to A5, B1, B2, Collaborators Unmasked options |
| `common/scripted_effects/097_collaboration_api_effects.txt` | Public write surface with caller proof (part 5) |
| `common/scripted_effects/097_collaboration_api_effects.md` | Owner API reference for writes, listed in the `owner_owned_apis` index of `chaosx_dynamic_effects.md` |
| `common/scripted_triggers/097_collaboration_triggers.txt` | Participant and host classifiers, gates, evolution behavior gates, pass state, band triggers |
| `common/scripted_triggers/097_collaboration_api_triggers.txt` | Public read surface (part 5) |
| `common/scripted_triggers/097_collaboration_api_triggers.md` | Owner API reference for reads |
| `common/scripted_triggers/097_collaboration_decision_triggers.txt` | Category visibility caches, phase triggers, inclusive affordability predicates |
| `common/on_actions/097_collaboration_on_actions.txt` | Native hooks listed in Section 4.1 |
| `common/mtth/097_collaboration_mtth.txt` | Evolution clocks, Open Gates, Turned Regime, and AI weight entries for surfaces S2 to S9 of the probability matrix |
| `common/dynamic_modifiers/097_collaboration_dynamic_modifiers.txt` | Fifth Column, vetting family, administration stages, A3 and A4 timed penalties, purge penalty, prepared cadres (state scope) |
| `common/decisions/categories/097_collaboration_categories.txt` | Divided Loyalties and Prepared Governments categories |
| `common/decisions/097_collaboration_decisions.txt` | A1 to A5, B1, B2 |
| `common/scripted_localisation/097_collaboration_scripted_localisation.txt` | Band words in plain and coloured variants, ideology registers for Cultivate and Screen, stage names, provisional-administration wording, Event Details current-state line, category header lines |
| `interface/097_collaboration.gfx` | Spirit, decision, category, and report sprites named by the asset prompt |
| `docs/events/097_collaboration/overview.md` | Mechanic document required by AGENTS.md section 4, rules 3 and 4 |

No ideas file is proposed because every spirit in the spec has tuning values or durations that this plan keeps in script constants, and repository dynamic modifiers accept `constant:` and `var:` values (`common/dynamic_modifiers/020_black_plague_dynamic_modifiers.txt:36`, `common/dynamic_modifiers/014_cannibalism_dynamic_modifiers.txt:78`). The offline wiki confirms that country dynamic modifiers appear in the national spirit list (`Modifiers` line 161).
No AI strategy file is proposed because part 6 forbids strategies that start wars or change targets.
No scripted GUI is proposed because part 4 selects a simple category.

### 1.2 Existing Event 097 files to rewrite

| Path | Current state | Change |
| --- | --- | --- |
| `events/097_collaboration.txt` | Stub root `chaosx.nr97.1` at line 23 adds to `global.collaboration` (line 31) and fans `chaosx.nr97.2` to every country (line 33). Option of `chaosx.nr97.2` (line 41) runs `every_other_country = { add_collaboration = ... }` (lines 49-50). | Replace wholesale with the event ids in Section 4.4. Retire `global.collaboration`, which has no reader in `common/` or `events/`. |
| `localisation/english/097_collaboration_l_english.yml` | Four stub keys with BOM. | Rewrite in place, keep UTF-8 with BOM. |

### 1.3 Shared files that need registration edits

| File | Existing identifier and line | Proposed edit |
| --- | --- | --- |
| `common/scripted_effects/chaosx_logic_effects.txt` | `add_to_array = { global.repeatable_events = 97 }  # COLLABORATION` at line 333 inside `initialize_event_categories` (line 232) | Replace the raw 97 with `constant:collaboration_event.event_id`. |
| same | `evaluate_event_pool_candidate_unavailability` (line 588), event-specific precedent branch for Event 027 at lines 827-833 | Add one 097 branch: Fallout gate, pass running, fewer than two participants. |
| same | `get_event_weight` (line 516) with the Event 009 dynamic cap branch | Optional wartime factor branch, only if the parent accepts Q3. |
| `common/scripted_triggers/chaosx_settings_triggers.txt` | `event_log_event_is_reworked_default_enabled` (lines 10-40) | Add the 097 id in the same change that completes registration and log wiring (edge matrix row on the rework queue). |
| `common/script_constants/event_system_constants.txt` | `event_system_event_unavailability_reason` (line 91), last event reason `doctrine_research_no_valid_participant = 43` (line 140), `unknown = 99` (line 141) | Add `collaboration_too_few_participants`, `collaboration_pass_running`, and `collaboration_fallout` from the next free id at implementation time (44 today). |
| `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` | `GetEventsLogEventAvailabilityReason` (line 13582), `GetEventsLogClusterMemberAvailabilityReason` (line 13421) | One row per new reason. |
| `localisation/english/chaosx_gui_l_english.yml` | Reason key family, for example `chaosx.events_log.events.na_reason.doctrine_research_no_valid_participant` (line 595) | Event and cluster-member reason keys for the three new reasons. |
| `common/scripted_effects/chaosx_settings_effects.txt` | `fire_event_by_temp_id_no_cluster` (line 4542), gate precedent for Event 3 (lines 4561-4567), manual-trigger precedent for Event 017 (lines 4704-4712) | Add a 097 prefire block that sets `event_single_fire_allowed = 0` when a pass is running, Fallout is active, or fewer than two participants exist, and sets `collaboration_forced_setup` when `events_log_manual_event_detail_trigger > 0` or the dispatcher holds `temp_bypass_checks` (set at line 1727, manual temp at line 1761). |
| `common/scripted_effects/chaosx_events_log_effects.txt` | `events_log_rebuild_open_event_details_view` (line 1914), `events_log_add_event_detail_evolution_preview` (line 2868), Event 008 preview block (lines 2538-2559) | Four preview rows with type 97, stages 1 to 4, tiers `constant:chaos_meter_tier_id.tier_1` to `tier_4`. |
| `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` | `GetEventsLogEventDetailDescription` (line 5717) | 097 premise row pointing to a key in the 097 yml. |
| same | Evolution selectors `GetEventsLogEvolutionTypeView` (918), `GetEventsLogEvolutionNameView` (2171), `GetEventsLogSelectedHistoryEvolutionTypeView` (3073), `GetEventsLogSelectedHistoryEvolutionNameView` (3302), `GetEventsLogEventDetailEvolutionTypeView` (4192), `GetEventsLogEventDetailEvolutionTitle` (6869), `GetEventsLogSelectedEvolutionTitle` (7662), `GetEventsLogSelectedEvolutionBody` (8455) | Type label row and four stage rows in each selector. |
| `common/script_constants/chaos_meter_constants.txt` | `chaos_meter_history_reason.special` (lines 166-199), last id `murder_mystery_defeat = 221` (line 198) | Event 097 reasons from the next free id at implementation time (Section 3.18). |
| `common/scripted_localisation/chaosx_scripted_localisation_chaos_meter.txt` | `GetChaosMeterHistoryReason` (line 812), Event 008 row at lines 1559-1563 | One row per new reason, keys kept in the 097 yml. |
| `common/scripted_effects/chaos_meter_effects.txt` | `add_chaos_meter_value` (line 4514), `black_friday_on_chaos_changed = yes` (line 4592) under the nonzero-change guard | Add `collaboration_on_chaos_changed = yes` under the same guard (Q2). |
| Cluster files, only if the parent builds the Intelligence cluster in this tranche | `event_cluster_id` (`event_cluster_constants.txt:9-24`), `initialize_event_cluster_definitions` (`chaosx_event_cluster_effects.txt:203`), `event_belongs_to_cluster` (623), `load_event_cluster_members` (1311), `event_cluster_check_cluster_gates` (2040), `mark_event_cluster_fired_state` (3850), `event_cluster_prepare_runtime_context` (4107) | Full cluster build per part 5, or ship without membership and list it as open (part 5, Runtime state of the Intelligence cluster). |
| `common/scripted_effects/chaosx_dynamic_effects.md` | `owner_owned_apis` index | One index row pointing to the 097 API documents. |
| `docs/events/README.md` | Documented events table | One 097 row. |
| `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`, `interface/chaosx_super_events.gfx` | Slot 97 is already used by `GFX_super_event_015_common_table` (line 267), highest used slot is 116 | Competing Orders slot chosen through the super-event workflow, never slot 97. |
| `common/achievements/chaos_redux_achievements.txt` | Single root registry | 097 section per part 6, reading the tracking records in Section 2. |

Name rows for 97 already exist and need only review: `chaosx.event_name.97` (`localisation/english/chaosx_event_names_l_english.yml:98`), debug selector (`chaosx_scripted_localisation_debug.txt:409`), events log rows (`chaosx_scripted_localisation_events_log.txt:2142`, `:11442`, `:13186`), and settings rows (`chaosx_scripted_localisation_settings.txt:2025`, `:6025`).

### 1.4 Shared surfaces 097 must not edit

- The global host pulse in `common/on_actions/chaosx_on_actions_chaos_meter.txt` (`on_daily`, lines 10-87). Part 1 forbids attaching the pass to it, and AGENTS.md section 1, rule 8 forbids new periodic world iteration without permission.
- The shared classifiers in `common/scripted_triggers/chaosx_dynamic_triggers.txt` (`is_special_chaos_country` line 10, `is_actual_nonhuman_country` line 45, `uses_normal_civilian_systems` line 70). Event 097 creates no special country, and installed governments are ordinary dynamic countries.
- `common/ideologies/00_ideologies.txt`. A change to `can_create_collaboration_government` (line 33) or `can_collaborate` (lines 120 and 184) is one of the user-level directions in part 3 and must not be chosen by implementation.
- Fallout source. The Fallout coverage question in row V9 is reported to the parent, not patched by 097.

## 2. Runtime state model

All names are proposals. Points mean percentage points from 0 to 100. Fractions mean the native 0 to 1 collaboration scale used by `add_collaboration` (offline `Effects` line 1246).

### 2.1 Global records

| Record | Kind | Writer | Main readers |
| --- | --- | --- | --- |
| `global.collaboration_owner` | country variable | `collaboration_resolve_owner` | Pass steps, evolution clocks |
| `collaboration_pass_running` | global flag | Root, pass completion, abort | Prefire gate, availability, cluster skip, API queue |
| `collaboration_pass_step_scheduled` | timed global flag | Step scheduler | Stall repair |
| `global.collaboration_pass_mode` | variable | Root or tranche start | Step, completion |
| `global.collaboration_pass_participants` | array of countries | Root freeze | Opening fan-out, steps |
| `global.collaboration_pass_hosts_accept`, `_cultivate`, `_screen` | arrays of countries | Pass start | Steps, completion |
| `global.collaboration_pass_cursor`, `_batch_size`, `_base_points`, `_next_step_day`, `_last_step_day` | variables | Pass start and steps | Steps |
| `global.collaboration_firing_seq`, `global.collaboration_firings_applied`, `global.collaboration_last_layer_points` | variables | Root, completion | Opening variants, MTTH, Event Details line |
| `collaboration_tranche_queued`, `collaboration_tranche_applied` | global flags | Deep Networks entry, tranche completion | Pass completion, Chaos guard |
| `global.collaboration_belligerents` | array of countries | War hooks, bootstrap | MTTH factors, evolution entries, weight factor |
| `collaboration_evolution_<n>_active`, `_logged`, `_prefire` for n from 1 to 4 | global flags | Activation events | Behavior gates, entries, opening variants |
| `global.collaboration_evolution_<n>_due_day`, `_active_day` | variables | Clock arming, activation | Activation events, Event Details |
| `global.collaboration_live_governments` | array of countries | Installation, retirement | Competing orders, B1 uniqueness, API |
| `global.collaboration_history_ids`, `_governments`, `_originals`, `_installers`, `_routes`, `_install_days`, `_retire_days`, `_retire_reasons` | aligned arrays | Retirement | Achievements, Event 095 |
| `global.collaboration_government_seq`, `global.collaboration_installers_with_two_count` | variables | Installation, retirement | Registry ids, competing orders |
| `global.collaboration_firing_chaos_total`, `global.collaboration_seated_host_count`, `global.collaboration_turned_chaos_count` | variables | Chaos rows | Chaos guards |
| `global.collaboration_collapsing_chaos_days`, `_amounts` | aligned arrays | Collapsing Chaos row | Rolling 365-day cap |
| `global.collaboration_depth_requests_hosts`, `_callers`, `_sequences` | aligned arrays | API while a pass runs | Pass completion |
| `global.collaboration_last_capitulation_day`, `collaboration_participant_capitulated` | variable and flag | Capitulation handler | MTTH factors |
| `collaboration_first_seat_recorded`, `collaboration_seats_5_recorded`, `collaboration_seats_15_recorded`, `collaboration_competing_orders_reached`, `collaboration_forced_setup`, `collaboration_belligerents_bootstrapped`, `collaboration_occupation_hooks_live` | global flags | Owning helpers | Guards, achievements, cheap hook gate |

### 2.2 Country records

| Record | Purpose |
| --- | --- |
| `collaboration_stance`, `collaboration_stance_firing`, `collaboration_last_stance` | Stance for the current firing, firing id guard, AI memory |
| `collaboration_screen_count`, `collaboration_cultivate_count`, flag `collaboration_ever_screened` | Achievement and AI history |
| `collaboration_incoming_depth`, `collaboration_outgoing_depth`, `collaboration_incoming_band`, `collaboration_outgoing_band` | Ledgers in points and cached band ids |
| flag `collaboration_pass_host` | Owned at least one state when the firing froze |
| flag `collaboration_divided_loyalties_eligible` | Category visibility cache |
| `collaboration_fc_band`, `collaboration_fc_network_band`, `collaboration_fc_strongest` | Fifth Column state and tooltip pointer |
| `collaboration_fc_surrender_limit`, `_war_support`, `_stability`, `_factory_output`, `_recruitable`, `_occupied_compliance`, `_occupied_resistance` | Dynamic modifier inputs |
| `collaboration_fc_highest_band`, `collaboration_fc_highest_strongest` | Highest band this war, read at capitulation |
| timed flag `collaboration_fc_eval_pending` | Debounce with watchdog |
| `collaboration_open_gates_due_day`, `collaboration_open_gates_war_count`, timed flag `collaboration_open_gates_cooldown` | Open Gates timer and caps |
| `collaboration_vetting_form`, `collaboration_vetting_expiry_day` | Vetting family state |
| `collaboration_a3_until_day`, `collaboration_a4_until_day`, flags for cooldowns | Response state |
| flag `collaboration_exile_chartered` | A5, cleared at peace |
| arrays `collaboration_unmasked_enemies`, `collaboration_open_ministries_controllers`, `collaboration_seat_reported_owners` | Per-war pair guards, cleared at peace |
| flags `collaboration_collapsing_chaos_done`, `collaboration_fc_capitulation_chaos_done` | Per-war Chaos guards, cleared at peace |
| `collaboration_gov_installer`, `_original`, `_route`, `_install_day`, `_id`, `_stage`, `_stage_since_day`, `_entrench_due_day`, `_b2_uses`, flags `collaboration_installed_government`, `collaboration_gov_original_chartered`, `collaboration_gov_turned_this_war` | Installed-government row |
| flag `collaboration_former_collaboration` | Marker after retirement by independence or abandonment expiry |
| `collaboration_live_government_count`, `collaboration_b1_ready_day`, flags `collaboration_has_installed`, `collaboration_installed_three_recorded` | Installer state |
| array `collaboration_sphere_owners` with aligned `collaboration_sphere_callers` | External sphere registrations held by the host |

### 2.3 State records

| Record | Purpose |
| --- | --- |
| flag `collaboration_seated`, `collaboration_seat_controller`, `collaboration_seat_day` | Live seat marker |
| timed targeted flag `collaboration_seat_guard_@<controller>` | 180-day seat guard per state and controller, which expires without cleanup |
| timed flag `collaboration_open_gates_guard` | 180-day Open Gates guard per state |
| flag `collaboration_cadres_active`, `collaboration_cadres_occupier` | Prepared cadre marker for early removal |

Timed targeted flags combine two documented forms, targeted flags (offline `Data structures` line 125, repository precedent `independence_wave_charter_war_authorized_@PREV` at `common/decisions/006_independence_wave_decisions.txt:3308`) and timed flags (precedent `fallout_consolidated_effects.txt:39971-39974`). No repository file uses both together, so this is verification row V25.

## 3. Helper map

### 3.1 Conventions

- Scripted effects take inputs through temporary variables and regular event targets, because HOI4 scripted effects do not take parameters (`chaos-redux-events` skill, section 7).
- Every temporary output and temporary array consumed after a helper returns is preinitialized by the caller, because temporaries first created inside a scripted effect may not survive the return (offline `Data structures` line 440). Each helper contract below names its outputs and their required initial values.
- A stored country pointer is validated with `exists = yes` in the real country scope, never with `scope_exists`.
- Regular event targets carry into events fired from the same chain. Any input that must survive a nested helper that can launch other work is copied into normal variables on the receiving country first, as the events skill requires.
- Native collaboration writes happen only inside helpers that first pass `collaboration_native_writes_allowed`.

### 3.2 Gates and classifiers

| Helper | Kind and scope | Definition and notes |
| --- | --- | --- |
| `collaboration_native_writes_allowed` | trigger, any | `fallout_world_rewrite_callbacks_are_allowed = yes` (`fallout_consolidated_triggers.txt:31589`) and `NOT = { has_global_flag = fallout_active }` (flag set at `fallout_consolidated_effects.txt:39725` and `:44193`). |
| `collaboration_event_is_enabled` | trigger, any | `NOT = { is_in_array = { global.disabled_events = constant:collaboration_event.event_id } }`, mirroring `026_black_friday_triggers.txt:19`. |
| `collaboration_is_participant` | trigger, country | `exists = yes`, `uses_normal_civilian_systems = yes`, `NOT = { is_special_chaos_country = yes }`, and either owns a state or `is_government_in_exile = yes`. Classifiers stay inside `hidden_trigger` when shown to players. |
| `collaboration_is_host` | trigger, country | `collaboration_is_participant = yes` and owns at least one state. This splits part 1's two statements about exiled governments (Q5). |
| `collaboration_has_event_networks` | trigger, country | `check_variable = { collaboration_incoming_depth > 0 }`. Every evolution behavior checks it before any pair read (part 2). |
| `collaboration_world_has_two_participants` | trigger, any | `any_country = { collaboration_is_participant = yes any_other_country = { collaboration_is_participant = yes } }`. It short-circuits on the first pair and is evaluated only at selection time, like the Event 027 availability branch. |
| `collaboration_pass_is_running` | trigger, any | `has_global_flag = collaboration_pass_running`. |
| `collaboration_deep_networks_live`, `collaboration_administrations_live`, `collaboration_fifth_column_live`, `collaboration_governments_live` | triggers, any | Active flag for that evolution, the shared evolution context set inside the trigger (temporaries may be set in triggers, offline `Data structures` line 441), `NOT = { has_disabled_current_evolution = yes }` (`chaosx_settings_triggers.txt:42`), and `collaboration_native_writes_allowed = yes`. They deliberately omit the tier check (recommendation 5). |
| `collaboration_sphere_allows_installation` | trigger, host country | Installer `PREV` is in `collaboration_sphere_owners` and `collaboration_administrations_live = yes`. It opens the offer and B1 from Evolution II for that installer only (part 5, Tordesillas contract). |

### 3.3 Layer computation

| Helper | Scope | Inputs | Outputs (caller preinitializes to 0) | Notes |
| --- | --- | --- | --- | --- |
| `collaboration_get_stance_multipliers` | country | none, reads `collaboration_stance` | `collaboration_layer_outgoing`, `collaboration_layer_incoming` | Reads `constant:collaboration_stance_multiplier.*`. A country whose `collaboration_stance_firing` does not match `global.collaboration_firing_seq` reads Accept. In tranche mode both outputs are 1. |
| `collaboration_get_pass_base_points` | any | `global.collaboration_pass_mode` | `collaboration_layer_base_points` | Firing mode returns the frozen `global.collaboration_pass_base_points` (15 or 25). Tranche mode returns `constant:collaboration_layer.tranche`. |
| `collaboration_compute_group_value` | any | `collaboration_layer_base_points`, `collaboration_layer_outgoing`, temp `collaboration_layer_group_incoming` | `collaboration_layer_value` (fraction) | Multiplies, then multiplies by `constant:collaboration_scale.unit_per_point`. Values stay at or below 0.47 with the spec anchors, so the native 0 to 1 range is respected. |

The base layer is frozen at the root, following the part 1 flow (step 1 says the root decides the layer). Part 1's layer table says "at the moment of application", so Q4 asks the parent to confirm.

### 3.4 Batched application pass

Event chain, all hidden except the report:

1. `chaosx.nr97.1` root, dispatcher scope. Gates were already applied by the prefire block. It calls `collaboration_start_firing`.
2. `collaboration_start_firing` increments `global.collaboration_firing_seq`, resolves the owner, bootstraps the belligerent registry once, freezes participants, freezes the base layer, sets `collaboration_pass_running`, sends `chaosx.nr97.2` to every participant with `for_each_scope_loop` over the frozen array, and schedules `chaosx.nr97.3` in the owner after the response window plus one day.
3. `chaosx.nr97.2` opening report, participant scope, `timeout_days = @COLLABORATION_RESPONSE_WINDOW_DAYS`. Accept is the first option, so timeouts and hidden-choice cases resolve to Accept (offline `Event modding` lines 186-188). Each option calls `collaboration_record_stance` with a temp stance input. Screen also calls the vetting helper.
4. `chaosx.nr97.3` pass start, owner scope. It builds the three stance host arrays and the batch size, then runs the first step immediately.
5. `chaosx.nr97.4` pass step, owner scope. It processes one batch and schedules itself one day later until the cursor reaches the end, then runs completion.

Freeze, once per firing (this `every_country` runs once per firing and is not periodic):

```txt
# COUNTRY scope (dispatcher). Proposal, not final source.
collaboration_freeze_participants = {
	clear_array = global.collaboration_pass_participants
	every_country = {
		limit = { collaboration_is_participant = yes }
		add_to_array = { global.collaboration_pass_participants = THIS }
		set_variable = { collaboration_stance = constant:collaboration_stance.accept }
		set_variable = { collaboration_stance_firing = global.collaboration_firing_seq }
		if = {
			limit = { collaboration_is_host = yes }
			set_country_flag = collaboration_pass_host
		}
		else = { clr_country_flag = collaboration_pass_host }
	}
}
```

Batch size, computed at pass start from live hosts H: `ceil(constant:collaboration_pass.pairs_per_step / max(H, 1))`, clamped to `constant:collaboration_pass.min_batch` and `max_batch`. Ceiling uses divide, add one half, and `round_temp_variable`, which is exact enough for a batch count.

Step body:

```txt
# COUNTRY scope (pass owner), immediate of chaosx.nr97.4. Proposal.
collaboration_pass_run_step = {
	if = {
		limit = { collaboration_pass_step_is_current = yes } # owner is THIS, running flag, due day reached, not already run today
		set_variable = { global.collaboration_pass_last_step_day = global.num_days }
		clr_global_flag = collaboration_pass_step_scheduled
		if = {
			limit = { collaboration_native_writes_allowed = no }
			collaboration_pass_abort = yes
		}
		else = {
			# Caller-owned temp arrays, built in this body so they survive.
			clear_temp_array = collaboration_step_hosts_accept
			clear_temp_array = collaboration_step_hosts_cultivate
			clear_temp_array = collaboration_step_hosts_screen
			for_each_scope_loop = {
				array = global.collaboration_pass_hosts_accept
				if = { limit = { collaboration_is_host = yes } add_to_temp_array = { collaboration_step_hosts_accept = THIS } }
			}
			# Same for cultivate and screen.
			set_temp_variable = { collaboration_step_end = global.collaboration_pass_cursor }
			add_to_temp_variable = { collaboration_step_end = global.collaboration_pass_batch_size }
			clamp_temp_variable = { var = collaboration_step_end max = global.collaboration_pass_participants^num }
			for_loop_effect = {
				start = global.collaboration_pass_cursor
				end = collaboration_step_end
				value = collaboration_step_index
				var:global.collaboration_pass_participants^collaboration_step_index = {
					if = {
						limit = { collaboration_is_participant = yes }
						collaboration_pass_apply_beneficiary = yes
					}
				}
			}
			set_variable = { global.collaboration_pass_cursor = collaboration_step_end }
			if = {
				limit = { check_variable = { global.collaboration_pass_cursor < global.collaboration_pass_participants^num } }
				collaboration_pass_schedule_next_step = yes
			}
			else = { collaboration_pass_complete = yes }
		}
	}
}

# COUNTRY scope (beneficiary). One sweep per host stance group.
collaboration_pass_apply_beneficiary = {
	set_temp_variable = { collaboration_layer_outgoing = 0 }
	set_temp_variable = { collaboration_layer_incoming = 0 }
	set_temp_variable = { collaboration_layer_base_points = 0 }
	set_temp_variable = { collaboration_layer_value = 0 }
	collaboration_get_stance_multipliers = yes
	collaboration_get_pass_base_points = yes
	set_temp_variable = { collaboration_layer_group_incoming = constant:collaboration_stance_multiplier.accept_incoming }
	collaboration_compute_group_value = yes
	for_each_scope_loop = {
		array = collaboration_step_hosts_accept
		if = {
			limit = { NOT = { tag = PREV } }
			PREV = { add_collaboration = { target = PREV value = collaboration_layer_value } }
		}
	}
	# Repeat for cultivate and screen with their incoming multipliers.
	collaboration_ledger_add_outgoing = yes
}
```

Scope notes for the pair write:
- Inside `for_each_scope_loop`, `PREV` is the scope the loop runs in, which is the beneficiary (offline `Data structures` line 1217).
- Inside `PREV = { ... }`, the current scope is the beneficiary and `PREV` is the host one level out, matching the wiki `controller` example (offline `Scopes` lines 262 and 316-327).
- The result is "scoped beneficiary gains collaboration inside target host", which is the orientation of `fallout_consolidated_effects.txt:41863-41877`, where the inner scope writes `set_collaboration = { target = PREV }`.
- If `value` rejects a temporary variable (row V3), each of the three sweeps is wrapped in one `meta_effect` that injects `[?collaboration_layer_value|.3]`, the formatting pattern of `006_independence_wave_decision_effects.txt:324`.

Scheduling and stall repair:
- `collaboration_pass_schedule_next_step` sets `global.collaboration_pass_next_step_day`, sets the timed global flag `collaboration_pass_step_scheduled` with `days = @COLLABORATION_PASS_WATCH_DAYS`, and fires `chaosx.nr97.4` in `var:global.collaboration_owner` with `days = collaboration_pass_step_days`. Variable delays are proven by `013_natural_disasters_effects.txt:1930-1933`, and the timed watch flag mirrors `fallout_schedule_current_transition_phase` (`fallout_consolidated_effects.txt:39963-39975`).
- A delayed event sent to a country that no longer exists waits until that tag exists again (offline `Event modding` line 35). The step therefore checks that `global.collaboration_owner` is the receiving country, the running flag, the due day, and the last-step day before doing anything, so a late backlog delivery exits harmlessly.
- `collaboration_pass_repair_if_stalled` runs when `collaboration_pass_running` is set and `collaboration_pass_step_scheduled` is not. It resolves a new owner and reschedules. It is called from the 097 `on_annex` block when FROM is the owner, from the 097 `on_state_control_changed` block after its one-flag gate, from stance option clicks, and from `collaboration_on_chaos_changed`. No periodic watcher is added.
- `collaboration_resolve_owner` keeps the stored owner while `var:global.collaboration_owner = { exists = yes }` holds. Otherwise it picks the country with `is_global_host` through one `random_country`, and falls back to the current country. The scan runs only when the owner is lost.

Completion (`collaboration_pass_complete`):
1. Adds incoming depth once per valid host from the three global host arrays.
2. Increments `global.collaboration_firings_applied` in firing mode and stores `global.collaboration_last_layer_points`.
3. Applies the firing or tranche Chaos row.
4. Copies `collaboration_stance` into `collaboration_last_stance`, increments the stance counters, and clears the current stance (part 1, Cleanup and persistence).
5. Runs pending pre-fire follow-ups (Administrations sweep, Fifth Column evaluations), then queued API depth requests, then a queued tranche.
6. Clears `collaboration_pass_running` unless a queued tranche starts, and re-arms evolution clocks because the firing count factor changed.

`collaboration_pass_abort` clears running and watch flags and the cursor without applying another batch, as the edge matrix requires for the Fallout transition.

Selection is blocked for the whole window and pass through the prefire gate and the unavailability branch, and a cluster burst skips 097 with the established cluster skip reason (part 5).

### 3.5 Ledgers and bands

| Helper | Scope | Inputs | Outputs and side effects |
| --- | --- | --- | --- |
| `collaboration_ledger_add_outgoing` | beneficiary | `collaboration_layer_base_points`, `collaboration_layer_outgoing` | Adds base times outgoing to `collaboration_outgoing_depth`, clamps to `constant:collaboration_layer.depth_cap`, refreshes `collaboration_outgoing_band`. |
| `collaboration_ledger_add_incoming` | host | `collaboration_layer_base_points`, host incoming multiplier | Adds base times incoming to `collaboration_incoming_depth`, clamps, refreshes `collaboration_incoming_band`, sets `collaboration_divided_loyalties_eligible` when the host is a belligerent. |
| `collaboration_refresh_depth_band` | country | temp `collaboration_band_input_points` | Temp `collaboration_band_result` (caller preinitializes to 0) using `constant:collaboration_depth_band.*`. |
| `collaboration_read_pair_band` | reader (occupier) | Regular target `collaboration_pair_host` with temp proof `collaboration_pair_host_supplied = 1` | Temp `collaboration_pair_band` (preinit 0) and, when row V8 passes, `collaboration_pair_points` (preinit 0). Fails closed without proof, without `collaboration_has_event_networks` on the host, or when the reader controls no host core. |

Incoming depth adds the Accept-equivalent layer for each host (base times host incoming multiplier). Part 1 calls incoming depth "after incoming multipliers", and the beneficiary's outgoing multiplier differs per pair, so an O(N) ledger can only mirror the host side (Q6).

The pair band ladder reads `NOT = { has_collaboration = { target = event_target:collaboration_pair_host value < X } }`, which gives "at least X" from a trigger that accepts only `<` and `>` (offline `Triggers` line 642). X comes from `@` band edges if the field rejects `constant:` (row V7).
If the numeric game variable is unavailable (row V8), exact points come from a seven-step binary search of `meta_trigger` thresholds at one-point resolution. That is a measurement method, not a changed mechanic, but it costs seven trigger evaluations per read, so the parent should know (Q22).

### 3.6 Belligerent registry

The engine exposes no war object, war count, or war-relation removal hook in the offline wiki (the `On actions` war table has `on_war_relation_added` at line 250 and no removal counterpart). The registry tracks participants at war with at least one participant enemy.

| Helper | Scope | Behavior |
| --- | --- | --- |
| `collaboration_belligerents_bootstrap` | any | Once per campaign behind `collaboration_belligerents_bootstrapped`. One `every_country` pass adds participants at war with a participant enemy. Called from the first root, the first clock arming, and the first evolution activation. |
| `collaboration_belligerents_add` | country | Adds THIS if missing. Called for ROOT and FROM in `on_war_relation_added` when both are participants. |
| `collaboration_belligerents_remove` | country | Removes THIS. Called from `on_peace` and from `on_annex` for FROM. |
| `collaboration_belligerents_compact` | any | Removes entries that no longer exist, no longer participate, or have no participant enemy. Called before any read. Bounded by the array size. |
| `collaboration_belligerents_count` | any | Temp output `collaboration_belligerent_count` (preinit 0) after compaction. |

The registry supplies the war factors of every evolution MTTH, the Administrations and Fifth Column active-event entries, and the optional wartime selection factor. Part 2 speaks of "three or more wars between participants", so the registry needs a threshold anchor such as six belligerents, and that definitional change is Q1.

### 3.7 Evolution context, behavior gates, and clocks

| Helper | Scope | Behavior |
| --- | --- | --- |
| `collaboration_set_evolution_context` | any | Input temp `collaboration_evolution_stage_input`. Sets `events_log_evolution_event_id`, `_type`, `_stage`, and `_tier` from `constant:collaboration_event.*`. Stages and tiers are both 1 to 4, because 200, 400, 600, and 800 Chaos are tiers 1 to 4 in `has_reached_current_evolution_tier`. |
| `collaboration_try_arm_evolution_clocks` | any | For each inactive evolution, sets the context and requires `is_current_evolution_enabled = yes`, `collaboration_event_is_enabled = yes`, and `collaboration_native_writes_allowed = yes`. It computes the delay from the evolution's MTTH entry and stores `global.collaboration_evolution_<n>_due_day` when none is stored or the new day is earlier. It then fires `chaosx.nr97.1<n>` in the owner with `days = collaboration_evolution_delay`. A clock only ever moves earlier. |
| `collaboration_on_chaos_changed` | any | Cheap gate on the lowest unarmed threshold, then `collaboration_try_arm_evolution_clocks` and `collaboration_pass_repair_if_stalled`. |
| `collaboration_activate_evolution_<n>` | owner | Runs inside `chaosx.nr97.1<n>`. Requires not active, due day reached, the full enable check with tier, the event enabled, and the Fallout gate. Sets the active flag and day, clears the due day, records the log entry, sets `_prefire` when no firing has been applied, and runs the entry path. If eligibility failed at the due day, it clears the due day so the next hook can re-arm. |
| `collaboration_record_evolution_log` | any | Context set first, then `limit` with `is_current_evolution_enabled = yes` and `NOT = { has_global_flag = collaboration_evolution_<n>_logged }`, then the logged flag and `record_events_log_evolution_entry = yes` (`chaosx_events_log_effects.txt:967`). No actor is set, so the shared default `events_log_evolution_has_actor = 0` applies (events skill rule). |

Entry paths:

| Evolution | Active-event entry | Pre-fire entry |
| --- | --- | --- |
| I Deep Networks | Starts the tranche pass in mode 2, or sets `collaboration_tranche_queued` while a pass runs. Tranche Chaos and the human-only report `chaosx.nr97.5` run at tranche completion. | Sets `_prefire`. The next root freezes the 25-point layer and the opening report uses the pre-fire variant. |
| II Administrations | `collaboration_seat_sweep_belligerents` iterates the compacted registry, then each host's owned core states that a participant enemy controls, and calls the seat helper with the controller. | Sets a flag that pass completion consumes once after the first firing. |
| III Fifth Column | Schedules one debounced evaluation per belligerent. | Same through pass completion. |
| IV Collaboration Governments | Sets the Prepared Governments visibility cache for occupiers of capitulated or exiled belligerents. No offer event fires (part 2). | Sets `_prefire` for the opening line only. |

### 3.8 Seat helper

`collaboration_seat_on_control_changed` is called from the 097 `on_state_control_changed` block in callback scope, where ROOT is the new controller, FROM the old controller, and FROM.FROM the state (offline `On actions` line 450, events skill section on Country activation and ROOT).

```txt
# Called with ROOT = new controller. Proposal.
collaboration_seat_on_control_changed = {
	if = {
		limit = { has_global_flag = collaboration_occupation_hooks_live }
		FROM.FROM = {
			if = {
				limit = { has_state_flag = collaboration_seated }
				collaboration_seat_end = yes # removes resistance target id, clears marker, may queue Unmasked
			}
			if = {
				limit = {
					is_core_of = owner # wording verified per row V26 alternatives
					collaboration_administrations_live = yes
					owner = { collaboration_is_host = yes collaboration_has_event_networks = yes }
					ROOT = { collaboration_is_participant = yes }
					NOT = { has_state_flag = collaboration_seat_guard_@ROOT }
				}
				owner = { save_event_target_as = collaboration_seat_owner }
				ROOT = { save_event_target_as = collaboration_seat_controller }
				collaboration_seat_try_install = yes
			}
		}
		collaboration_schedule_affected_evaluations = yes # Fifth Column for the owner, Contested for affected governments
	}
	collaboration_pass_repair_if_stalled = yes
}
```

`collaboration_seat_try_install`, state scope, inputs are the two regular targets above with proof temps `collaboration_seat_owner_supplied` and `collaboration_seat_controller_supplied`:
1. Requires the controller at war with the owner and an Ordinary or better pair band read through `collaboration_read_pair_band` from the controller.
2. Compliance gain is points times `constant:collaboration_seat.compliance_ratio`, capped at `compliance_cap`. With the Fifth Column active on the owner it uses `fifth_column_compliance_factor` and `fifth_column_compliance_cap`. With Loyalty Commissions on the owner it multiplies by `commissions_compliance_factor`. It applies `add_compliance` with a variable (offline `Effects` line 3734).
3. Resistance uses `add_resistance_target = { id = @COLLABORATION_SEAT_RESISTANCE_ID amount = <negative variable> occupier = event_target:collaboration_seat_controller }` (offline `Effects` line 3737). Row V17 covers the negative amount.
4. Sets the seat marker and the timed targeted guard flag with `days = @COLLABORATION_SEAT_GUARD_DAYS`.
5. Increments seat milestones: the first seat, and the owner's first seat ever (host flag) for the 5 and 15 host rows.
6. Sends the first-seat report `chaosx.nr97.20` to the controller when the owner is not yet in its `collaboration_seat_reported_owners` array.
7. Runs Open Ministries when the state is the owner's capital and the band is Strong or better, guarded by the owner's `collaboration_open_ministries_controllers` array. It adds `constant:collaboration_seat.open_ministries_compliance` to every other owner core state the controller holds, applies the war support loss, and sends `chaosx.nr97.21` to the owner.

Outputs: temp `collaboration_seat_result` (preinit 0) is 1 on a new seat, so Open Gates and sweeps can count.

`collaboration_seat_end` removes the resistance target with `remove_resistance_target = @COLLABORATION_SEAT_RESISTANCE_ID` (offline `Effects` line 3743) and clears the marker. When the new controller is the owner or not at war with the owner, it queues `chaosx.nr97.22` Collaborators Unmasked to the owner, guarded by `collaboration_unmasked_enemies`. The seating enemy travels as a normal variable on the owner (`collaboration_unmasked_pending_enemy`), because the event fires later and regular targets would not be frozen.

The resistance id is one constant per state. Only one seat is live per state, and `remove_resistance_target` acts on the scoped state, so a single id is enough. No repository file uses `add_resistance_target`, so the id range needs no reservation beyond 097.

### 3.9 Fifth Column evaluator

Scheduling: `collaboration_schedule_fifth_column_evaluation`, host scope, sets the timed flag `collaboration_fc_eval_pending` with `days = @COLLABORATION_FC_EVAL_WATCH_DAYS` and fires `chaosx.nr97.30` in the host with `days = collaboration_fc_eval_delay`. If the flag is already set, nothing happens, which is the part 2 debounce. Callers are the seat hook for the state owner, `on_war_relation_added` for both participant sides, `on_peaceconference_ended` for both sides, `on_uncapitulation`, and the Evolution III entry.

`collaboration_evaluate_fifth_column`, host scope, inside `chaosx.nr97.30`:
1. Clears the pending flag. If `collaboration_fifth_column_live` fails, the host is not a participant at war, or `collaboration_has_event_networks` fails, it calls `collaboration_fifth_column_clear` and stops.
2. Strongest network: iterates `every_enemy_country` (bounded by enemies) with a limit of participant and `any_controlled_state = { is_owned_by = ROOT is_core_of = ROOT }`, reads the pair band from each, and keeps the highest band. ROOT is the host because `chaosx.nr97.30` is received by the host, while `PREV` inside the state scope would be the enemy. Ties keep the first valid candidate. It stores `collaboration_fc_strongest` and `collaboration_fc_network_band`. With no Ordinary or better enemy, it clears.
3. Target band from `surrender_progress` against `constant:collaboration_fifth_column.wavering_floor`, `defecting_floor`, and `collapsing_floor`. Surrender progress accepts constants in repository precedent (`012_africa_effects.txt:93`).
4. Hysteresis: if the current band is higher than the target, it drops only when progress is below the current floor minus `constant:collaboration_fifth_column.hysteresis`.
5. Responses: Loyalty Commissions or A3 lower the effective band by one, with at most one reduction in total. A4 zeroes the factory and recruitable inputs.
6. Writes the seven modifier variables from `constant:collaboration_fifth_column_effect.*` times the network factor. Adds `collaboration_fifth_column` if missing and calls `force_update_dynamic_modifier = yes` (offline `Effects` line 346).
7. Records the highest band this war. On the first Collapsing this war it applies the Collapsing Chaos row.
8. Open Gates timer: at Defecting or Collapsing, when neither A3 nor A4 suspends it and no timer is pending, it calls `collaboration_schedule_open_gates`.
9. Sets the flag `collaboration_fifth_column_active` for stronger seats.

`collaboration_fifth_column_clear` removes the modifier, clears the variables, the flag, and the Open Gates due day. It does not clear the highest-band record, which `on_peace` and the capitulation handler consume.

Dynamic modifier `collaboration_fifth_column` maps the inputs to `surrender_limit`, `war_support_factor`, `stability_factor`, `industrial_capacity_factory`, the recruitable population token, `compliance_growth_on_our_occupied_states`, and `resistance_target_on_our_occupied_states` (offline `List of modifiers` lines 328, 321, 314, 444, 333 or 335, 384, and 392). Token choice and units are row V15 and V16.

### 3.10 Open Gates

`collaboration_schedule_open_gates`, host scope, computes the delay from `mtth:collaboration_open_gates_interval`, stores `collaboration_open_gates_due_day`, and fires `chaosx.nr97.31` in the host.

`collaboration_open_gates_incident`, host scope, inside `chaosx.nr97.31`:
1. Requires the due day reached, band Defecting or higher, no suspension, no `collaboration_open_gates_cooldown` flag, and `collaboration_open_gates_war_count` below `constant:collaboration_open_gates.per_war_cap`. Otherwise it reschedules or stops.
2. Selector `collaboration_open_gates_select_state` iterates `every_owned_state` with a limit of controlled by the host, core of the host, `is_capital = no`, `any_neighbor_state` controlled by the stored strongest country, no `collaboration_open_gates_guard`, and no host or ally divisions. Division presence uses `divisions_in_state = { state = collaboration_og_candidate size > 0 }` on the host and on each `every_allied_country` (offline `Triggers` line 1279, precedent `011_secret_alliance_effects.txt:3670`). Among qualifying states it keeps the lowest state variable `victory_points` (precedent `014_cannibalism_triggers.txt:1366`). Output is temp `collaboration_og_selected` (preinit 0) with temp proof `collaboration_og_selected_found`.
3. Transfer: the selected state runs `set_state_controller_to` the strongest country (offline `Effects` line 3375, precedent `015_utopia_manifesto_effects.txt:2141`). If row V13 confirms that this fires `on_state_control_changed`, the seat follows through the ordinary hook. Otherwise the incident calls the seat helper directly.
4. Sets the timed state guard and the host cooldown flag, increments the war count, applies the Open Gates Chaos row, and sends `chaosx.nr97.32` to the host and `chaosx.nr97.33` to the enemy.
5. With no qualifying state it reschedules (part 3).

"Allies" here follows the engine meaning of `every_allied_country`, which covers faction members, subjects, and the overlord (offline `Scopes` line 521 and `Data structures` line 1797). Co-belligerents outside the faction are not covered, which is row V14.

### 3.11 Prepared cadres

`collaboration_apply_prepared_cadres`, host scope, called from the capitulation handler when `collaboration_deep_networks_live` holds. For each participant enemy that controls host core states with a Strong or Total pair band, every such state receives `collaboration_prepared_cadres_strong` or `_total` through `add_dynamic_modifier` with `days = collaboration_cadres_days` (precedent `020_black_plague_response_action_effects.txt:630`) and the marker. The seat hook removes the modifier and marker when the controller changes. It applies once per capitulation per occupier and host through the capitulation handler, which runs once per capitulation. The exiled host receives `chaosx.nr97.23`.

### 3.12 Installer selector

`collaboration_select_installer`, host scope, inputs are the capitulation winner as regular target `collaboration_capitulation_receiver` with proof temp. Outputs are temp `collaboration_installer_found` (preinit 0) and temp country pointer `collaboration_installer_best` (preinit 0).

```txt
# Deterministic maximum with first-valid acceptance. Proposal.
set_temp_variable = { collaboration_installer_best_score = -1 }
every_enemy_country = {
	limit = { collaboration_is_participant = yes }
	set_temp_variable = { collaboration_installer_candidate_ok = 0 }
	collaboration_installer_evaluate_candidate = yes # core control, threshold, no living government for the original tag
	if = {
		limit = {
			check_variable = { collaboration_installer_candidate_ok > 0 }
			check_variable = { collaboration_installer_candidate_score > collaboration_installer_best_score }
		}
		set_temp_variable = { collaboration_installer_best_score = collaboration_installer_candidate_score }
		set_temp_variable = { collaboration_installer_best = THIS }
		set_temp_variable = { collaboration_installer_found = 1 }
	}
}
```

Score is band times `constant:collaboration_installer_score.band_weight` (1000), plus host cores controlled, plus `constant:collaboration_installer_score.receiver_bonus` (0.5) for the capitulation receiver. The weight keeps the spec order: band first, then cores, then the receiver. A strict greater-than keeps the first valid candidate on full ties.

Threshold per part 3: `constant:collaboration_installation.threshold_ordinary`, or `threshold_collapsing` when the host's highest band this war was Collapsing, plus `exile_charter_add` when the host chartered, minus `sphere_reduction` inside a registered sphere for that candidate, clamped to `threshold_floor` and `threshold_ceiling`. The comparison uses the numeric pair read, or a `meta_trigger` that injects the threshold.

### 3.13 Shared installation helper

`collaboration_install_government`, installer scope. Every route calls it.

Inputs (all caller-set, temp proof values must be 1):
- regular target `collaboration_install_host` and temp `collaboration_install_host_supplied`
- temp `collaboration_install_route` from `constant:collaboration_route.*`
- temp `collaboration_install_caller` (0 for 097's own routes, an API caller id otherwise)

Outputs (caller preinitializes): temp `collaboration_install_result` from `constant:collaboration_install_result.*` (0 none, 1 success, plus one rejection id per failed guard) and temp `collaboration_install_government` (country pointer, preinit 0).

Steps:
1. Guards in order, each failing closed with its own result id: native writes allowed, behavior gate (`collaboration_governments_live`, or `collaboration_sphere_allows_installation` for the sphere route), host and installer participants, installer controls a host core, threshold met, no living government for the host's original tag (`any_of_scopes = { array = global.collaboration_live_governments original_tag = event_target:collaboration_install_host }`, offline `Triggers` line 640 and `Scopes` line 747), and B1 cooldown when the route is the decision.
2. Snapshot the installer's current subjects that match the host's original tag and are dynamic, into a temp array.
3. Vanilla route: `set_temp_variable = { country_to_initiate = event_target:collaboration_install_host }`, then `instantiate_collaboration_government = yes` (offline `Effects` line 4723). Row V10 must confirm the input shape and behavior first.
4. Identify the new government. Prefer an output the vanilla effect provides (row V10). Otherwise find the one subject of the installer with `is_dynamic_country = yes` (offline `Triggers` line 652), the host's original tag, `has_autonomy_state = autonomy_collaboration_government`, and absence from the pre-call snapshot.
5. If none is found, return the creation-failed result and change nothing else. Costs have not been charged yet.
6. Write the row on the government, append it to `global.collaboration_live_governments`, raise the installer's live count and the two-government counter, and set `collaboration_gov_original_chartered` from the host's charter flag.
7. Set stage Imposed through `collaboration_set_administration_stage`.
8. Raise auxiliaries through `collaboration_raise_auxiliaries` with the count rule from part 3, debit the installer's infantry equipment through `remove_infantry_equipment_from_stockpile` (`chaosx_dynamic_effects.txt:747`), and create the template and units in the government, following `events/095_occupation_revolt.txt:38-58`.
9. Apply the installation Chaos rows, run `collaboration_check_installer_system` and `collaboration_check_competing_orders`, and send reports.

B1's political power is charged in `complete_effect` before the helper. On a failed result the decision refunds every debited cost and leaves the installer cooldown unset, as the decisions skill requires for paid actions that reject after payment.

### 3.14 Registry

| Helper | Scope | Behavior |
| --- | --- | --- |
| `collaboration_registry_retire` | government | Inputs temp `collaboration_retire_reason`. Appends one row to every aligned history array, removes the government from the live array, lowers the installer's count and the two-government counter, removes the stage modifier, sets `collaboration_former_collaboration` for independence and abandonment expiry, applies the matching restoration Chaos row, and calls `collaboration_check_competing_orders` (milestones never refund). Idempotent through the provenance flag. |
| `collaboration_registry_compact` | any | Retires live rows whose government no longer exists, with reason annexed. Called before counts. |
| `collaboration_registry_find_original` | any | Input regular target of an original country. Output temp pointer and found flag. Bounded by the live array. |

Retirement reasons: independence, annexed by installer, restoration by uprising, restoration by liberation, abandonment expiry, Fallout. The restoration reasons come from the caller (Event 095 through the API) or from the `on_annex` hook, when ROOT has the government's original tag.

### 3.15 Installed Administration lifecycle

| Helper | Scope | Behavior |
| --- | --- | --- |
| `collaboration_set_administration_stage` | government | Input temp stage. Removes the other three stage modifiers, adds the new one, sets the stage and since-day. Imposed schedules the Entrenched timer `chaosx.nr97.42` with `days = remaining`. Contested remembers the prior stage. Abandoned schedules the expiry timer. |
| `collaboration_schedule_contested_evaluation` | government | Debounced like the Fifth Column, timed flag plus `chaosx.nr97.43`. Callers: the seat hook when the state owner is a live government, the seat hook for the installer's live governments (iterated with `every_subject_country` and the provenance flag) when a state owned by the installer changes controller, `on_war_relation_added` and `on_peace` for the government or installer. |
| `collaboration_evaluate_contested` | government | Contested when the installer is at war past `constant:collaboration_lifecycle.contested_installer_surrender`, or a rival participant at war with the installer occupies government territory with a Strong or better band. It restores the prior stage when neither holds. Entering Contested arms Turned Regime. |
| `collaboration_entrench_timer` | government, `chaosx.nr97.42` | Moves Imposed to Entrenched when the due day is reached and the stage is still Imposed. B2 moves the due day earlier by `constant:collaboration_timing.b2_entrench_advance` and reschedules. Stale timers exit on the due-day check. |
| `collaboration_abandon_governments_of` | installer | Moves every live government of the installer to Abandoned unless `collaboration_gov_turned_this_war` marks a Turned Regime transfer. Called from the capitulation handler and the `on_annex` handler for FROM. |

The spec has two readings of a freed government. The lifecycle table makes "stops being the overlord for any reason other than Turned Regime" Abandoned, while registry cleanup, part 5 (Event 063), and the edge matrix retire a freed government with an independence record. This plan follows the latter in `on_subject_free` and asks the parent to confirm (Q8).

### 3.16 Turned Regime

`collaboration_schedule_turned_regime`, government scope, runs when Contested begins and the conditions in part 3 hold. It stores a due day from `mtth:collaboration_turned_regime_interval` and fires `chaosx.nr97.44`.

`collaboration_turned_regime_incident`, government scope, re-checks every condition, the per-war flag, and row V12, then calls `collaboration_transfer_installed_government`:
1. Set the transaction flag so 097's own `on_subject_free` handler does not retire or abandon the row.
2. Old installer runs `end_puppet` on the government (offline `Effects` line 1442).
3. Rival runs `puppet = { target = <government> end_wars = no end_civil_wars = no }` (line 1441), then `set_autonomy` to `autonomy_collaboration_government` (line 1445) if the default autonomy differs.
4. Government runs `add_to_war = { targeted_alliance = <rival> enemy = <old installer> }` (line 1505) if it is not already on the rival's side.
5. Update the row (installer, route Turned Regime), reset to Imposed, adjust both installers' counts, apply the Turned Regime Chaos row within its campaign cap, run competing orders, and send `chaosx.nr97.45` and `chaosx.nr97.46`.

Every step depends on row V12. If the engine cannot do this cleanly, part 3 requires the variant to stay unimplemented with the reason recorded.

### 3.17 Competing orders

`collaboration_check_installer_system` applies the "installer reaches three" row once per installer.
`collaboration_check_competing_orders` requires `global.collaboration_installers_with_two_count` at or above `constant:collaboration_competing_orders.min_powers` and the milestone flag unset. It then sets the flag, applies the +5 row, and starts the super-event through the super-event workflow. The counter changes only when an installer's live count crosses from one to two or from two to one, so the check never iterates.

### 3.18 Chaos helpers

`collaboration_add_chaos`, any scope. Inputs: temp `collaboration_chaos_amount` (signed points) and temp `collaboration_chaos_reason`. An optional actor is saved by the caller as `chaos_history_actor` in the actor's scope. It sets `chaos_change`, `chaos_history_reason`, and `chaos_history_reason_custom = 1`, then calls `add_chaos_meter_value` (`chaos_meter_effects.txt:4514`), the pattern of `apply_tensions_rising_stage_chaos` (`008_tensions_rising_effects.txt:219-238`). The shared block for a disabled meter stays in force.

| Row helper | Guard | Proposed reason key |
| --- | --- | --- |
| `collaboration_chaos_firing` | `global.collaboration_firing_chaos_total` below the lifetime cap, adds the remainder only | `collaboration_firing` |
| `collaboration_chaos_tranche` | `collaboration_tranche_applied` | `collaboration_deepening` |
| `collaboration_chaos_first_seat`, `_seats_five`, `_seats_fifteen` | Global flags and the seated host counter | `collaboration_first_seat`, `collaboration_seat_spread` |
| `collaboration_chaos_collapsing` | Host flag per war, rolling 365-day cap from the aligned day and amount arrays, pruned on write | `collaboration_collapsing` |
| `collaboration_chaos_open_gates` | Shares the incident cap | `collaboration_open_gates` |
| `collaboration_chaos_fifth_column_capitulation` | Host flag per war | `collaboration_internal_capitulation` |
| `collaboration_chaos_installation` | Once per installation, plus the first-government bonus | `collaboration_installation` |
| `collaboration_chaos_installer_system` | Installer flag | `collaboration_installer_system` |
| `collaboration_chaos_competing_orders` | Global flag | `collaboration_competing_orders` |
| `collaboration_chaos_turned_regime` | Government flag per war and the campaign counter | `collaboration_turned_regime` |
| `collaboration_chaos_collapsing_survived` | Host flag per war, run from `on_peace` when the highest band was Collapsing and the host did not capitulate in that war | `collaboration_collapsing_survived` |
| `collaboration_chaos_restoration` | Once per government, amount by retire reason | `collaboration_restoration` |

Ids start at the next free special id at implementation time (222 today). Major-power factors read `is_major = yes`. The installation row reads the result of row V30 to decide whether the generic puppet source already counted that installation (part 3).

### 3.19 Decision support helpers

| Helper | Scope | Contract |
| --- | --- | --- |
| `collaboration_divided_loyalties_visible` | trigger, country | `collaboration_is_participant` and the cached flag `collaboration_divided_loyalties_eligible`, set by the war hooks and ledger and cleared in `on_peace`. It does no world reads per frame. |
| `collaboration_prepared_governments_visible` | trigger, country | `collaboration_governments_live` or a sphere registration with Administrations live, and either the cached target flag or a positive live count. |
| `collaboration_quote_action` | country | Input temp `collaboration_action_id`. Outputs preinitialized to 0: `collaboration_quote_political_power`, `_manpower`, `_infantry_equipment`, `_trains`, `_trucks`, `_command_power`, `_army_experience`, `_convoys`, `_spirit_stability`, `_spirit_consumer_goods`, `_spirit_factory_output`. Minor or major anchors use `is_major`, and situation factors come from part 4. Command power is clamped to the 60 cap from the decisions skill. |
| `collaboration_action_quote_is_affordable` | trigger, country | The single inclusive predicate used by both `available` and `custom_cost_trigger`, as the decisions skill requires. It runs the quote inside the trigger. |
| `collaboration_pay_action_quote` | country | Debits once with the existing helpers `remove_infantry_equipment_from_stockpile` (line 747), `remove_trains_from_stockpile` (737), `remove_motorized_equipment_from_stockpile` (727), and `remove_convoys_from_stockpile` (732) in `chaosx_dynamic_effects.txt`, plus native resource effects. |
| `collaboration_refund_action_quote` | country | Credits the same quote back when a post-payment guard rejects. |
| `collaboration_divided_loyalties_slot_rules` | trigger, country | Encodes the four-button cap. A2 hides first when all five qualify, and running or cooling actions never show as buttons (part 4). |

Targeted decisions use game arrays held by ROOT (offline `Decision modding` lines 525-534 and `Data structures` lines 1797-1803): A2 uses `target_array = enemies` with a `target_trigger` that FROM controls a seated owned state of ROOT, B1 uses `target_array = occupied_countries`, and B2 uses `target_array = subjects` with the provenance flag. Per-installer and per-government cooldowns that cross targets are variables (`collaboration_b1_ready_day`, `collaboration_gov_b2_uses`), because `days_re_enable` applies per decision clone (offline `Decision modding` line 514).

The B1 compliance threshold compares `core_compliance = { occupied_country_tag = FROM value > X }` (offline `Triggers` line 1158, repository precedent with a literal tag at `common/decisions/formable_nation_decisions.txt:1198-1210`) with a dynamic X injected by `meta_trigger` (row V26).

A1's capitulation clause (each occupier's capitulation compliance reduced by a quarter of its collaboration) needs the numeric pair read in the capitulation handler (row V8).

### 3.20 Public API

Read surface, `097_collaboration_api_triggers.txt`:

| Fact | Form |
| --- | --- |
| Is a participant | Trigger `collaboration_api_is_participant` |
| Incoming and outgoing band | Country variables `collaboration_incoming_band` and `collaboration_outgoing_band`, documented as read-only, plus triggers per band |
| Fifth Column band and strongest country | Variables `collaboration_fc_band` and `collaboration_fc_strongest` |
| Is an installed government and its record | Trigger `collaboration_api_is_installed_government` and documented row variables |
| Restoration pressure band | Effect `collaboration_api_get_restoration_band`, government scope, output temp `collaboration_restoration_band_result` preinitialized to 0 |
| Evolution states | Triggers `collaboration_api_evolution_<name>_active` reading the active flags |

Write surface, `097_collaboration_api_effects.txt`. Every write requires temp `collaboration_api_caller_id` registered in `constant:collaboration_api_caller.*`, temp `collaboration_api_caller_sequence`, and the proof temps for each saved target. Each returns temp `collaboration_api_result` (preinit 0). Unknown callers, missing proof, contradictory proof, closed Fallout gates, or a replayed caller sequence fail closed and change nothing.

| Write | Scope and targets | Bound and receipt |
| --- | --- | --- |
| `collaboration_api_burn_networks` | any, targets `collaboration_api_beneficiary` and `collaboration_api_host` | Amount capped at the current base layer and written as a negative `add_collaboration` (row V4). The receipt is the caller and sequence stored on the host per beneficiary in two small aligned arrays. |
| `collaboration_api_add_network_depth` | any, target `collaboration_api_host` | At most half the current base layer for every live participant beneficiary in one `every_country` pass per call. Queued to the request arrays while a pass runs and processed at completion. Receipt arrays on the host. |
| `collaboration_api_register_sphere` | any, target `collaboration_api_sphere_owner`, temp array `collaboration_api_sphere_hosts` | Appends the owner and caller to each host's sphere arrays, without duplicates. |
| `collaboration_api_retire_government` | any, target `collaboration_api_government` | Calls `collaboration_registry_retire` with the caller's reason. |
| `collaboration_api_install` | any, targets installer and host | Calls `collaboration_install_government` in the installer with route and caller recorded. |

Caller ids proposed: 39, 52, 63, 95, and one id for the cluster runtime. The Tordesillas owner has no catalog id yet (part 5 says 163 is the only free id below 167), so its caller stays unregistered and fails closed until that owner exists (Q20).

### 3.21 Cleanup

| Moment | Cleanup |
| --- | --- |
| Pass completion | Current stances cleared, counters kept, step arrays discarded with the effect chain |
| `on_peace` for a country | Fifth Column clear, Open Gates due day and war count reset, highest-band record consumed by the survived row, per-war arrays and flags cleared, A5 charter cleared, belligerent removed, eligibility flag cleared |
| Capitulation of a host | Fifth Column read, then cleared after Evolution IV processing |
| Annex of FROM | Registry retirement if FROM was a government, abandonment of FROM's governments, owner repair, belligerent removal |
| Seat change | Seat marker and resistance id, prepared cadres of the old controller |
| Fallout transition | Pass abort at the next step, no new native writes anywhere, records kept |
| Disabled evolution | Behavior gates fail at the next evaluation, and the Fifth Column evaluator clears its own modifier when its gate fails |

## 4. Hooks

### 4.1 Native on_actions

All blocks go into the new `common/on_actions/097_collaboration_on_actions.txt`, following the event-owned pattern (`008_tensions_rising_on_actions.txt`, `035_great_depression_on_actions.txt`). The repository has no 097 on_actions file today, and the shared `chaosx_on_actions.txt` is reserved for hooks that belong to no event (events skill, section 2). Every block starts with a cheap flag gate.

| Hook | Scopes per offline `On actions` page | 097 use |
| --- | --- | --- |
| `on_state_control_changed` | ROOT new controller, FROM old controller, FROM.FROM state (line 450) | Seat start and end, Unmasked queue, prepared cadre removal, Fifth Column and Contested scheduling, pass stall repair |
| `on_capitulation` | ROOT capitulated country, FROM winner, units already deleted and equipment transferred (line 254) | Fifth Column capitulation Chaos, A1 compliance reduction, prepared cadres, installer selector and offer, abandonment of the capitulated installer's governments, capitulation records |
| `on_capitulation_immediate` | ROOT capitulated country, FROM winner, beginning of the process (line 255) | Not used unless row V20 shows that reads must happen before engine processing |
| `on_war_relation_added` | ROOT attacker, FROM defender (line 250) | Belligerent registry, eligibility cache, Fifth Column and Contested scheduling, clock re-arm |
| `on_peace` | THIS country no longer at war (line 253) | Per-war cleanup, survived Collapsing row, belligerent removal |
| `on_peaceconference_ended` | ROOT winner, FROM loser, also fired by `white_peace` and accepted conditional surrender (line 216) | Partial peace re-evaluation of both sides |
| `on_annex` | ROOT winner, FROM annexed (line 257) | Registry retirement or abandonment, restoration route detection, owner repair |
| `on_subject_free` | ROOT subject, FROM previous overlord (line 435) | Retirement with independence record unless a Turned Regime transfer is running |
| `on_subject_annexed` | ROOT subject, FROM overlord (line 434) | Retirement with annexed record |
| `on_government_exiled` | ROOT exile, FROM host country (line 442) | Restoration pressure input, Prepared Governments target cache for occupiers |
| `on_exile_government_reinstated` | ROOT exile, FROM former host country (line 444) | Restoration pressure input. Restoration retirement happens through `on_annex` or the API |
| `on_uncapitulation` | ROOT country affected (line 256) | Fifth Column re-evaluation |

`on_puppet` (line 260) and `on_release_as_puppet` (line 263) are not 097 hooks. Their only role is row V30, which decides the installation Chaos overlap.

No `on_daily`, `on_weekly`, or `on_monthly` block is proposed, and no tag-specific `on_daily_<TAG>` is needed unless the parent asks for a CXT package (Q13). That block would mirror `039_murder_mystery_on_actions.txt:9-30`.

### 4.2 Capitulation hook choice

`on_capitulation` is recommended. It matches the generic Chaos source (`chaos_meter_on_capitulation`, `chaos_meter_effects.txt:6480`) and every repository capitulation hook, and the values 097 reads (enemy control of host cores, the stored Fifth Column record, the native pair value) are not documented as changing between the two callbacks.
`on_capitulation_immediate` is used by only one repository file (`006_independence_wave_on_actions_registry.txt`). It becomes necessary only if row V20 shows that capitulation processing changes state control, exiles the government, or converts collaboration before `on_capitulation` runs in a way that breaks the installer selector.

### 4.3 The Chaos-change hook

`add_chaos_meter_value` already calls an event-owned helper on every nonzero change (`black_friday_on_chaos_changed = yes`, `chaos_meter_effects.txt:4592`, defined at `026_black_friday_effects.txt:2777`), with a comment that this avoids another recurring world scan. A sibling call for 097 lets evolution clocks arm when Chaos crosses 200, 400, 600, or 800 without a periodic hook.

Two paths change Chaos without this function: the settings value setter (`chaosx_settings_effects.txt:3666`) and the Event 020 scenario floor (`020_black_plague_scenario_effects.txt:788`). Arming then waits for the next ordinary change, at latest the monthly decay call in the host's `on_monthly` block (`chaosx_on_actions_chaos_meter.txt`, monthly decay added through `add_chaos_meter_value`), or for 097's own firing and war hooks. That delay is small against 60 to 120 day MTTH windows.

### 4.4 Event ids

| Id | Kind | Scope | Purpose |
| --- | --- | --- | --- |
| `chaosx.nr97.1` | hidden root | dispatcher | Starts a firing |
| `chaosx.nr97.2` | report | participant | Opening report with stances |
| `chaosx.nr97.3` | hidden | owner | Pass start after the window |
| `chaosx.nr97.4` | hidden | owner | Pass step |
| `chaosx.nr97.5` | report | human participants | Deep Networks tranche report |
| `chaosx.nr97.11` to `chaosx.nr97.14` | hidden | owner | Evolution activation clocks |
| `chaosx.nr97.20` | report | controller | First seat report |
| `chaosx.nr97.21` | report | owner | Open Ministries report |
| `chaosx.nr97.22` | choice | owner | Collaborators Unmasked |
| `chaosx.nr97.23` | report | exiled host | Prepared cadres report |
| `chaosx.nr97.30` | hidden | host | Fifth Column evaluation |
| `chaosx.nr97.31` | hidden | host | Open Gates timer |
| `chaosx.nr97.32`, `chaosx.nr97.33` | reports | host, enemy | Open Gates reports |
| `chaosx.nr97.40` | choice | installer | Prepared Government offer, FROM is the host |
| `chaosx.nr97.42` to `chaosx.nr97.44` | hidden | government | Entrenched timer, Contested evaluation, Turned Regime timer |
| `chaosx.nr97.45`, `chaosx.nr97.46` | reports | former installer, new master | Turned Regime reports |

The offer is fired from the host's scope into the installer, so FROM inside `chaosx.nr97.40` is the host (offline `Scopes` line 263, FROM in events is the sender).

### 4.5 Iteration inventory

| Iteration | Frequency | Bound |
| --- | --- | --- |
| Participant freeze, `every_country` | Once per firing | All countries, one cheap trigger each |
| Opening fan-out, `for_each_scope_loop` | Once per firing | Participants |
| Pass steps | Once per day during a pass | Batch slice times hosts |
| Tranche pass | Once per campaign | Same as a firing pass |
| Belligerent bootstrap, `every_country` | Once per campaign | All countries |
| Owner resolution, `random_country` | Only when the owner is lost | Stops at the first match |
| Availability, `any_country` with `any_other_country` | Each selection evaluation | Stops at the first pair |
| Add-depth API, `every_country` | Once per accepted caller sequence | All countries |
| Seat sweeps at Evolution II entry | Once | Belligerents' owned core states |
| Fifth Column evaluation | Debounced per host per triggering event | Host's enemies and their controlled states, short-circuited |
| Open Gates selection | At most once per host per timer | Host's owned states |
| Contested scheduling from installer state changes | Per installer state change while the installer has live governments | Installer's subjects |

Nothing runs from `on_daily`, `on_weekly`, or `on_monthly`, and nothing is added to the global host pulse.

## 5. Evolution pacing

### 5.1 Precedents found

| Event | Mechanism | Evidence |
| --- | --- | --- |
| 035 Great Depression | Country-scope MTTH due day stored on first eligibility, activation when `global.num_days` reaches it, log behind global `_logged` flags | `great_depression_try_evolution_activation` at `035_great_depression_effects.txt:2269` (due day lines 2283-2295), `great_depression_record_enabled_evolution_milestones` at line 2222, MTTH at `common/mtth/035_great_depression_mtth.txt:9`. Its check runs from the weekly registry pulse reached through the host pulse (`great_depression_process_active_registry`, line 4282). |
| 018 Resources Found | Separate pre-fire and active MTTH clocks run as engine missions with the MTTH value as timeout | `resources_found_schedule_evolution_paths` at `018_resources_found_decision_effects.txt:2622`, entries at `common/mtth/018_resources_found_mtth.txt:10`, Chaos tier factors through `has_global_flag = { flag = chaos_tier value = ... }` |
| 008 Tensions Rising | No MTTH. Stage recomputed at each firing and logged once per stage | `record_tensions_rising_evolution_if_needed` at `008_tensions_rising_effects.txt:240` |
| 013 Natural Disasters | Delayed hidden job events with variable `days` | `chaosx.nr13.2` at `events/013_natural_disasters.txt:69-76`, scheduling at `013_natural_disasters_effects.txt:1930-1933` |

Event 035 is the closest MTTH precedent, but its due-day check depends on the host pulse. Event 097 keeps the due-day model and replaces the polling pulse with one delayed event per evolution, which is the Event 013 delivery pattern.

### 5.2 Proposed 097 pacing

1. Eligibility arms a clock. Arming runs from `collaboration_on_chaos_changed`, firing completion, `on_war_relation_added` between participants, and the capitulation handler.
2. Arming evaluates the evolution's MTTH entry once, stores the due day, and sends one delayed hidden event to the owner.
3. Later arming calls may only move the due day earlier, for example when a firing completes and the "fired once" factor applies. The superseded later event finds the evolution already active and exits.
4. At delivery the event re-checks enablement, the Chaos tier, the event-disabled state, and Fallout. If eligibility lapsed, it clears the due day, and the next hook re-arms when eligibility returns.
5. Activation sets the active flag, records the log entry with no actor, and runs the entry path from Section 3.7. It never changes Chaos.

The design is dynamic at arming points but does not re-evaluate continuously. That is the 035 behavior too, which stores its due day once on first eligibility.

### 5.3 MTTH entries in `common/mtth/097_collaboration_mtth.txt`

| Entry | Scope | Base and modifiers | Probability surface |
| --- | --- | --- | --- |
| `collaboration_evolution_deep_networks_interval` | any | Base `constant:collaboration_mtth.deep_networks_days`. Factors: one firing applied, two or more firings, belligerent count at the war-proxy threshold, never fired. | S7 |
| `collaboration_evolution_administrations_interval` | any | Base `administrations_days`. Factors: Deep Networks active, `collaboration_participant_capitulated`, empty belligerent registry. | S7 |
| `collaboration_evolution_fifth_column_interval` | any | Base `fifth_column_days`. Factors: Administrations active, any belligerent past the near-defeat threshold through `any_of_scopes`, empty registry. | S7 |
| `collaboration_evolution_governments_interval` | any | Base `governments_days`. Factors: Administrations and Fifth Column both active, capitulation within the recent window, empty registry. | S7 |
| `collaboration_open_gates_interval` | host | Base by band, Defecting or Collapsing. Factor for Loyalty Commissions (half speed). | S8 |
| `collaboration_turned_regime_interval` | government | Base `constant:collaboration_turned_regime.mtth_days`. | S9 |
| `collaboration_ai_stance_accept_weight`, `_cultivate_weight`, `_screen_weight` | participant | Actor-group factors from part 6, with Accept never near zero. | S2 |
| `collaboration_ai_offer_install_weight`, `_keep_weight` | installer | Part 6 offer ordering. | S3 |
| `collaboration_ai_unmasked_purge_weight`, `_amnesty_weight` | owner | | S4 |
| `collaboration_ai_a1_weight` to `collaboration_ai_a5_weight` | host | Part 4 ordering. | S5 |
| `collaboration_ai_b1_weight`, `collaboration_ai_b2_weight` | installer | Part 4 ordering. | S6 |

MTTH `base` and `factor` accept `constant:` tokens in repository precedent (`035_great_depression_mtth.txt:10` and `:12`). The `ai_will_do` injection follows the `chaos-redux-mtth` skill. Every entry needs the `chaosx_ai_probability_auditor` baseline and compare pass, which is currently blocked by the MCP failure.

## 6. Script constants

Every group begins with `schema`. Category names were checked against `common/script_constants/`, and no `collaboration_*` category exists today.

### 6.1 Proposed groups

| Category | Schema | Keys |
| --- | --- | --- |
| `collaboration_event` | int | `event_id` 97, `evolution_type` 97, `stage_deep_networks` 1, `stage_administrations` 2, `stage_fifth_column` 3, `stage_governments` 4, `tier_deep_networks` 1 to `tier_governments` 4, `min_participants` 2 |
| `collaboration_value` | int | `zero`, `one`, `two`, `three` |
| `collaboration_scale` | fixed_point | `points_per_unit` 100, `unit_per_point` 0.01 |
| `collaboration_layer` | fixed_point | `base` 15, `deep` 25, `tranche` 10, `depth_cap` 100, `api_burn_max_ratio` 1, `api_depth_max_ratio` 0.5, `a2_reduction` 15, `unmasked_reduction` 10 |
| `collaboration_stance` | int | `accept` 1, `cultivate` 2, `screen` 3 |
| `collaboration_stance_multiplier` | fixed_point | `accept_outgoing` 1, `accept_incoming` 1, `cultivate_outgoing` 1.5, `cultivate_incoming` 1.25, `screen_outgoing` 0.75, `screen_incoming` 0.5 |
| `collaboration_depth_band` | fixed_point | `established` 20, `deep` 40, `pervasive` 70 |
| `collaboration_depth_band_id` | int | `scattered` 0, `established` 1, `deep` 2, `pervasive` 3 |
| `collaboration_network_band` | fixed_point | `ordinary` 0.15, `strong` 0.40, `total` 0.70 |
| `collaboration_network_band_id` | int | `thin` 0, `ordinary` 1, `strong` 2, `total` 3 |
| `collaboration_timing` | int | `response_window` 14, `pass_step` 1, `pass_watch` 5, `fc_eval_delay` 1, `fc_eval_watch` 5, `gov_eval_watch` 5, `seat_guard` 180, `open_gates_state_guard` 180, `open_gates_host_cooldown` 90, `vetting_peace` 120, `vetting_war` 180, `a1_duration` 180, `a1_cooldown` 90, `a2_cooldown` 120, `a3_duration` 120, `a3_cooldown` 180, `a4_duration` 90, `a4_cooldown` 180, `unmasked_penalty` 90, `b1_cooldown` 180, `b2_cooldown` 180, `b2_entrench_advance` 90, `imposed_to_entrenched` 365, `abandoned_expiry` 730, `cadres_duration` 365, `collapsing_chaos_window` 365, `recent_capitulation` 365 |
| `collaboration_pass` | int | `pairs_per_step` 2000, `min_batch` 5, `max_batch` 40 |
| `collaboration_mtth` | fixed_point | `deep_networks_days` 90, `administrations_days` 90, `fifth_column_days` 90, `governments_days` 120, `fired_once_factor`, `fired_twice_factor`, `never_fired_factor`, `wars_factor`, `no_war_factor`, `prior_evolution_factor`, `capitulation_factor`, `near_defeat_factor`, `near_defeat_progress` 0.40 |
| `collaboration_war_proxy` | int | `belligerents_for_three_wars` (Q1) |
| `collaboration_selection` | fixed_point | `war_weight_factor` 1.5 (Q3) |
| `collaboration_fifth_column` | fixed_point | `wavering_floor` 0.20, `defecting_floor` 0.40, `collapsing_floor` 0.60, `hysteresis` 0.05, `network_factor_ordinary` 0.5, `network_factor_strong` 1, `network_factor_total` 1.5 |
| `collaboration_fifth_column_band` | int | `none` 0, `wavering` 1, `defecting` 2, `collapsing` 3 |
| `collaboration_fifth_column_effect` | fixed_point | Per band: `<band>_surrender_limit`, `<band>_war_support`, `<band>_stability`, `<band>_factory_output`, `<band>_recruitable`, `<band>_occupied_compliance`, `<band>_occupied_resistance`, with part 3 values in the units row V16 confirms |
| `collaboration_seat` | fixed_point | `compliance_ratio` 0.5, `compliance_cap` 40, `fifth_column_compliance_factor` 1.5, `fifth_column_compliance_cap` 50, `commissions_compliance_factor` 0.5, `resistance_ratio` 0.25, `resistance_cap` 25, `open_ministries_compliance` 15, `open_ministries_war_support` -0.10, `commissions_capitulation_ratio` 0.25 |
| `collaboration_prepared_cadres` | fixed_point | `strong_compliance_growth` 0.25, `strong_resistance_target` -10, `total_compliance_growth` 0.5, `total_resistance_target` -20 |
| `collaboration_open_gates` | fixed_point | `defecting_days` 60, `collapsing_days` 30, `commissions_factor` 2, `per_war_cap` 3 |
| `collaboration_installation` | fixed_point | `threshold_ordinary` 0.40, `threshold_collapsing` 0.30, `exile_charter_add` 0.10, `sphere_reduction` 0.10, `threshold_floor` 0.25, `threshold_ceiling` 0.60, `vanilla_compliance` 80, `compliance_ratio` 0.5, `compliance_floor` 50 |
| `collaboration_installer_score` | fixed_point | `band_weight` 1000, `receiver_bonus` 0.5 |
| `collaboration_install_result` | int | `none` 0, `success` 1, then one id per rejection reason |
| `collaboration_route` | int | `offer` 1, `decision` 2, `external_sphere` 3, `api` 4, `turned_regime` 5 |
| `collaboration_retire_reason` | int | `independence` 1, `annexed` 2, `restoration_uprising` 3, `restoration_liberation` 4, `abandoned_expired` 5, `fallout` 6 |
| `collaboration_admin_stage` | int | `imposed` 1, `entrenched` 2, `contested` 3, `abandoned` 4 |
| `collaboration_admin_stage_effect` | fixed_point | Stage modifier values from part 3 |
| `collaboration_auxiliaries` | fixed_point | `states_per_division` 2, `minimum` 1, `maximum` 6, `b2_divisions` 2, `b2_max_uses` 3, `start_experience` 0.1 |
| `collaboration_lifecycle` | fixed_point | `contested_installer_surrender` 0.40 |
| `collaboration_turned_regime` | fixed_point | `mtth_days` 120, `installer_surrender` 0.40, `campaign_chaos_cap` 2 |
| `collaboration_competing_orders` | int | `min_powers` 2, `min_governments` 2, `installer_system` 3 |
| `collaboration_restoration` | fixed_point | Input weights and band edges (Q15) |
| `collaboration_vetting` | fixed_point | `stability` -0.10, `consumer_goods` 0.10, `collapsing_stability` -0.15, `minimum_stability` |
| `collaboration_chaos` | int | `firing_base` 1, `firing_deep` 2, `firing_lifetime_cap` 10, `tranche` 1, `first_seat` 1, `seats_five` 2, `seats_fifteen` 3, `seat_hosts_tier_one` 5, `seat_hosts_tier_two` 15, `collapsing` 1, `major_bonus` 1, `collapsing_rolling_cap` 5, `open_gates` 2, `capitulation_defecting` 2, `capitulation_collapsing` 3, `installation` 2, `first_installation_bonus` 1, `installer_system` 3, `competing_orders` 5, `turned_regime` 3, `collapsing_survived` -1, `restoration_uprising` -2, `restoration_liberation` -1 |
| `collaboration_decision_cost` | int | Minor and major anchors per action from part 4, plus situation factors |
| `collaboration_api_caller` | int | `event_039` 39, `event_052` 52, `event_063` 63, `event_095` 95, `cluster_runtime` |

The `points_per_unit` and `unit_per_point` pair keeps a single conversion between ledger points and native fractions. Without it, the formulas would hide the factor 100 as a magic number.

### 6.2 File-scoped `@` constants

These fields either reject `constant:` and variables in repository precedent or are unproven. Each `@` value is mirrored by the named script constant and both change in the same edit (events skill, section 7).

| Constant | File | Field | Mirror |
| --- | --- | --- | --- |
| `@COLLABORATION_RESPONSE_WINDOW_DAYS` | `events/097_collaboration.txt` | `timeout_days` of `chaosx.nr97.2` | `collaboration_timing.response_window` |
| `@COLLABORATION_PASS_WATCH_DAYS` | `097_collaboration_effects.txt` | `set_global_flag` `days` | `collaboration_timing.pass_watch` |
| `@COLLABORATION_FC_EVAL_WATCH_DAYS`, `@COLLABORATION_GOV_EVAL_WATCH_DAYS` | occupation and government effects | `set_country_flag` `days` | `fc_eval_watch`, `gov_eval_watch` |
| `@COLLABORATION_SEAT_GUARD_DAYS`, `@COLLABORATION_OPEN_GATES_STATE_GUARD_DAYS`, `@COLLABORATION_OPEN_GATES_HOST_COOLDOWN_DAYS` | occupation effects | timed state and country flags | matching timing keys |
| `@COLLABORATION_SEAT_RESISTANCE_ID` | occupation effects | `add_resistance_target` `id` and `remove_resistance_target` | none, it is an identifier |
| `@COLLABORATION_BAND_ORDINARY`, `@COLLABORATION_BAND_STRONG`, `@COLLABORATION_BAND_TOTAL` | `097_collaboration_triggers.txt` | `has_collaboration` `value`, if row V7 rejects constants | `collaboration_network_band.*` |
| `@COLLABORATION_A1_*`, `@COLLABORATION_A2_*`, and the other decision timing values | `097_collaboration_decisions.txt` | `days_re_enable`, `days_remove`, `ai_hint_pp_cost` | `collaboration_timing.*`, `collaboration_decision_cost.*` |

Fields that accept variables in repository precedent use temporary variables loaded from constants: `country_event` `days` (`013_natural_disasters_effects.txt:1932`), `add_dynamic_modifier` `days` (`020_black_plague_response_action_effects.txt:630`), `add_compliance` (offline `Effects` line 3734), and decision `cost` (offline `Decision modding` line 286). The auxiliary experience factor sits inside the `create_unit` division string, so it is injected with `meta_effect`.

## 7. Engine verification list

Each row must be checked in the installed `documentation/` files (`effects_documentation.md`, `triggers_documentation.md`, `dynamic_variables_documentation.md`, `script_concept_documentation.md`, `common/script_constants/documentation.md`) and in a vanilla precedent before implementation. No failed row may be replaced silently. Every failure is reported to the parent, and outcome-changing fallbacks need acceptance.

| Row | Behavior to verify | Needed by | Current evidence | If verification fails |
| --- | --- | --- | --- | --- |
| V1 | `add_collaboration` orientation: scoped country gains collaboration inside `target`, `value` on the 0 to 1 scale | Pass, API, A2, Unmasked | Offline `Effects` line 1246, Fallout orientation at `fallout_consolidated_effects.txt:41863-41877` | Swap the two scopes in the pair write. No design change. |
| V2 | A pair value written without occupation persists and later drives surrender limit, capitulation compliance, and recipient score | Whole baseline | Offline `Defines` lines 480-482, stub behavior unverified | Blocker for the entire event design. Report before any other work. |
| V3 | `add_collaboration` `value` accepts a temporary variable or `constant:` | Pass | Fallout passes only `@` constants | Use the three-per-beneficiary `meta_effect` wrapper. No design change. |
| V4 | Negative `add_collaboration` values are accepted and clamp at zero | A2, Unmasked purge, Burn networks API | None in repository | Blocker for those three surfaces (part 4). No absolute `set_collaboration` substitute. |
| V5 | Native cap at 1.0 | Repeated firings | Part 1 relies on it | Blocker for the cap semantics, because outside occupation the value cannot be read to clamp it. |
| V6 | `has_collaboration` reads the pair value in occupation contexts, including when the reader occupies only some host cores, and what it returns without occupation | Every evolution read | Offline `Triggers` line 642 says the target is occupied by the current scope | Record the observed behavior as part 3 requires. If it reads zero in partial occupation, Strong and Total reads in seats and the Fifth Column become unreliable, which is a design blocker. |
| V7 | `has_collaboration` `value` accepts `constant:` or variables | Pair band ladder | Fallout uses `@` | Use `@` band edges and `meta_trigger` for dynamic thresholds. |
| V8 | Numeric game variable `has_collaboration@<country>`, its exact syntax with `PREV`, `ROOT`, or `var:` targets, and its occupation scope | Seat formula, installation threshold, A1 capitulation clause, B1 threshold | Offline `Data structures` line 1512, targeted read precedent `opinion@ROOT` at `018_resources_found_decision_effects.txt:1989` | Seven-step `meta_trigger` binary search at one-point resolution (Q22). |
| V9 | Fallout coverage. `fallout_reset_old_world_diplomacy` resets a pair only `if has_collaboration > 0` (`fallout_consolidated_effects.txt:41866-41875`), and the clean-world proof uses the same trigger (`fallout_consolidated_triggers.txt:32158-32162`) | Part 5 Fallout promise | Row V6 | If `has_collaboration` reads zero without occupation, Event 097 pairs survive the Fallout reset and the proof passes vacuously. Report to the Fallout owner as a cross-system blocker. 097 must not patch Fallout. |
| V10 | `instantiate_collaboration_government`: defining file, `country_to_initiate` input shape, ideology rules `can_create_collaboration_government` and `can_collaborate`, DLC checks, states transferred, autonomy state, leader, any output pointer | Installation | Offline `Effects` line 4723, mod ideology rules at `00_ideologies.txt:33`, `:120`, `:184` | Ideology refusal is the part 3 user decision among three directions. A missing output pointer uses the snapshot difference in Section 3.13. A DLC gate is reported as an exact limitation. |
| V11 | Dynamic country pool size and failure behavior when full | Installation | Offline `Data structures` line 1785 mentions 50 dynamic countries | The helper already fails closed before charging. Report capacity as a balance risk shared with civil wars, Fallout fractures, and Event 039 carriers. |
| V12 | Mid-war overlord transfer: `end_puppet`, `puppet` with `end_wars = no`, `set_autonomy` from the new overlord, `add_to_war`, and which on_actions fire | Turned Regime | Offline `Effects` lines 1441, 1442, 1445, 1505 | Part 3 requires the variant to stay unimplemented with the reason recorded. |
| V13 | `set_state_controller_to` gives control without ownership and fires `on_state_control_changed` | Open Gates | Repository precedents at `015_utopia_manifesto_effects.txt:2141` and `021_random_civil_war_parent_effects.txt:4113` prove the effect exists | If no callback fires, the incident calls the seat helper directly. If the effect fails on an owned and controlled host state, Open Gates is blocked (part 3). |
| V14 | `divisions_in_state` counts only the scoped country's divisions, accepts a temporary state variable, and `every_allied_country` is the right ally set | Open Gates | Offline `Triggers` line 1279, precedent `011_secret_alliance_effects.txt:3670` | If co-belligerents outside the faction must count, the parent decides between a war-side check and the engine ally set. If presence cannot be read reliably, Open Gates is blocked (part 3). |
| V15 | Modifier tokens in the right scope: `surrender_limit`, `war_support_factor`, `stability_factor`, `industrial_capacity_factory`, `conscription_factor` versus `recruitable_population_factor`, `compliance_growth_on_our_occupied_states`, `resistance_target_on_our_occupied_states`, the consumer goods token, `political_power_factor`, and the state tokens `compliance_growth` and `resistance_target` | All spirits and cadres | Offline `List of modifiers` lines 312-392 and 444 | A missing token is reported, and a replacement token needs parent acceptance because it changes the effect. |
| V16 | Units of those modifiers (fraction versus points) | Constant values | Repository uses fractional `resistance_target` at `001_communism_spread_dynamic_modifiers.txt:50` | Constant values change, the design does not. |
| V17 | `add_resistance_target` with `id`, negative `amount` from a variable, `occupier` filter, and per-state `remove_resistance_target` | Seats | Offline `Effects` lines 3737 and 3743 | Use a state dynamic modifier with variable `resistance_target`, removed at seat end. Outcome is equivalent, but the parent should accept it because the spec names a removable identifier. |
| V18 | `add_compliance` and `add_war_support` accept variables | Seats, Open Ministries | Offline `Effects` line 3734 for compliance | `meta_effect` injection. |
| V19 | DLC boundary of collaboration value, defines, operations, and creation route | Whole event | Part 6 table | Report the exact limitation. A `has_dlc` gate needs parent acceptance. |
| V20 | Ordering of `on_capitulation` and `on_capitulation_immediate` relative to collaboration-to-compliance conversion, exile, and control changes | Capitulation handler | Offline `On actions` lines 254-255 | Move the reads to `on_capitulation_immediate`. |
| V21 | `on_peace` fires only when a country leaves its last war, and `on_peaceconference_ended` covers partial peace | Per-war cleanup, re-evaluation | Offline `On actions` lines 216 and 253 | If partial peace is not covered, the Fifth Column re-evaluation for the edge matrix row needs another event-driven trigger, which the parent must approve. |
| V22 | `timeout_days` accepts an `@` constant, and the timeout picks the first option | Opening report | Offline `Event modding` line 186 | Literal in the event with a mirrored constant comment. |
| V23 | An event option whose `trigger` fails is hidden, not shown greyed with a tooltip | Screen requirement | HOI4 options have no documented disabled state in the offline page | The part 1 "blocked tooltip" for Screen cannot be shown natively (Q11). |
| V24 | Nested `PREV = { ... target = PREV }` resolves to beneficiary scope and host target inside `for_each_scope_loop` | Pass | Offline `Scopes` lines 262 and 316-327 | Use `target = var:` with the host pointer kept in a temporary variable. |
| V25 | Targeted timed flags on states and countries (`flag = name_@ROOT` with `days`) | Seat guard, cooldowns | Targeted flags and timed flags exist separately in repository | Per-state arrays of controller and day, pruned on write. |
| V26 | `core_compliance` with `occupied_country_tag = FROM` and a `meta_trigger` value, and the core and capital predicates in state scope (`is_core_of = owner` form, `is_capital`) | B1, seats | Offline `Triggers` lines 1158 and 1841, repository use only with a literal tag | `meta_trigger` with the target tag injected, and `owner = { capital_scope = { ... } }` comparisons. |
| V27 | `create_unit` consumes stockpile equipment or creates it | Auxiliaries, B2 exploit guard | Event 095 stub pattern only | If units are created with free equipment, the installer debit stays the cost and the government's stockpile is not credited twice. |
| V28 | `ai_hint_pp_cost` accepts only literals | B1, A actions | Decisions skill warning | Use the `@` constant of the anchor and document the gap. |
| V29 | `for_each_scope_loop` has no iteration cap, and temporary arrays built in the same effect block are usable by it | Pass | Offline `Data structures` lines 1217-1220, temp array precedent `020_black_plague_response_action_effects.txt:1805-1809` | Split the inner loop into capped slices, which raises the step count. |
| V30 | Whether `on_puppet`, `on_release_as_puppet`, or another generic Chaos source fires for a scripted collaboration government | Installation Chaos row | Offline `On actions` lines 260 and 263 | Part 3 already defines the outcome: the installation amount drops to zero for that installation. |
| V31 | `has_war_with`, `every_enemy_country`, and `any_controlled_state` behave for governments in exile with no owned state | Fifth Column, participants | Offline `Scopes` lines 375 and 392 | Exclude stateless exiles from host-side reads, which part 1 already does. |

## 8. Performance

Ordered pairs are N times (N minus 1).

| Participants | Pairs per pass | Batch at 2,000 pairs per step | Steps | Days from firing to completion with a 14-day window |
| --- | --- | --- | --- | --- |
| 80 | 6,320 | 26 | 4 | about 19 |
| 100 | 9,900 | 21 | 5 | about 20 |
| 150 | 22,350 | 14 | 11 | about 26 |
| 200 | 39,800 | 11 | 19 | about 34 |

Per step cost is about 2,000 native writes, about 2,000 self-exclusion checks, three loop setups per beneficiary, and one O(N) host compaction. The full pair set in one tick is the scale of the Fallout one-time sweep (`fallout_consolidated_effects.txt:41863-41877`), which the repository accepts once per campaign at a dramatic transition. A repeatable minor event should not stall the game for one tick, so the 2,000-pair budget spreads the work over days.

The Deep Networks tranche is one more full pass with the same costs, once per campaign. It queues behind a running firing pass, so two passes never overlap.

The ledger costs O(N) per firing. The opening fan-out sends one event per participant, and AI participants resolve immediately.

The `on_state_control_changed` block is the hottest path. Before any occupation evolution is active, and while no seat or cadre exists, it costs one global flag check (`collaboration_occupation_hooks_live`) plus the pass stall check. After activation it adds participant flags and at most a few pair reads per control change. Fifth Column and Contested evaluations are debounced to one pending evaluation per country.

Recommended starting values: `pairs_per_step` 2000, `min_batch` 5, `max_batch` 40, `pass_step` 1 day. These are tuning anchors. Live frame-time evidence belongs to the user's in-game validation.

## 9. Risks

1. Row V9 can leave Event 097 collaboration alive after the Fallout reset if `has_collaboration` reads zero outside occupation. The fix belongs to the Fallout owner.
2. The mod's ideology rules (`00_ideologies.txt:33`, `:120`, `:184`) make a democratic or non-aligned refusal of `instantiate_collaboration_government` likely. Part 3 already reserves that decision for the user.
3. The dynamic-country pool is shared and finite (V11). A competing-orders world may exhaust it alongside civil wars and Fallout fractures.
4. A delayed event to a dead country is backlogged, not dropped (offline `Event modding` line 35). Without the owner check and repair path, a re-released former owner would replay stale steps.
5. Several Chaos Redux systems already write compliance or resistance from `on_state_control_changed` and occupation mechanics (Event 007 Fury, CBRN occupation, genocide crisis, camp repression). Seats stack on top of them, which the balance pass must measure.
6. Settings and Event 020 can set Chaos directly (Section 4.3), which delays clock arming until the next ordinary change.
7. The Intelligence cluster has no runtime id, and Event 039 is registered as repeatable at runtime while its spec treats it as Fire-Once (part 5). Cluster hooks stay dormant until the cluster exists.
8. The probability and MTTH surfaces S1 to S10 cannot be audited in this environment because of the MCP failure.
9. Event options cannot show a greyed Screen option (V23), so the part 1 requirement text needs another presentation.
10. The vanilla collaboration-government decision stays available. Deeper networks raise compliance at capitulation, so vanilla governments will appear more often and outside the 097 registry.

## 10. Open questions for the parent

Q1. Accept the belligerent registry as the measure for "wars between participants", with a belligerent-count threshold standing in for "three or more wars", or name another measure.
Q2. Accept the shared edit that adds `collaboration_on_chaos_changed = yes` beside the Event 026 call in `add_chaos_meter_value`.
Q3. Implement the wartime selection factor in `get_event_weight`, where the Event 009 branch proves an event-owned hook exists, or keep the ordinary weight. Part 1 asks for the factor only if a hook exists, and one does.
Q4. Confirm that the base layer is frozen at the root (part 1 flow, step 1) rather than at application (part 1 layer table).
Q5. Confirm the two classifiers: a participant owns a state or is an exiled government, and a host owns a state. Part 1 requires owning a state and also keeps stateless exiles as beneficiaries.
Q6. Confirm that incoming depth adds the Accept-equivalent layer per host, because the per-pair value depends on each beneficiary's stance.
Q7. Confirm that burns, A2, and the Unmasked purge leave the depth ledgers unchanged, since the ledgers mirror what Event 097 added.
Q8. Resolve the freed-government conflict between the lifecycle table (Abandoned) and registry cleanup, part 5, and the edge matrix (retired as independent).
Q9. Confirm that a host which is itself a live installed government cannot receive a new installed government, which follows from the one-per-original-tag rule.
Q10. Decide whether governments created by the vanilla decision count toward the one-per-original-tag rule.
Q11. Choose how the Screen requirement is shown, given V23.
Q12. Confirm that "per war" means a continuous war period that ends when the country is fully at peace, because the engine exposes no war identity.
Q13. Decide whether Event 097 registers a CXT test package under the AGENTS.md section 4, rule 11 "general system" clause, following `039_murder_mystery_on_actions.txt:9-30`.
Q14. Decide whether 097 custom costs are quoted through the universal cost framework (`common/scripted_effects/chaosx_universal_cost_effects.md`) so Event 026 sales apply.
Q15. Set the restoration pressure weights and band edges, which part 5 states only as directions.
Q16. Set the A3 rule for "trains or trucks", for example trains when the stockpile covers the quote and trucks otherwise.
Q17. After V12 passes, accept the Turned Regime transfer sequence in Section 3.16.
Q18. Choose the Competing Orders super-event slot through the super-event workflow (not 97).
Q19. Build the Intelligence cluster in the 097 tranche, or ship 097 without cluster membership as part 5 allows.
Q20. Reserve a caller id for the future Tordesillas owner now, or leave it unregistered until that owner exists.
Q21. Confirm that A1's capitulation clause runs only against occupiers that hold host cores at the moment of capitulation.
Q22. If V8 fails, accept the seven-step binary search pair read or reduce seat and threshold formulas to band steps.

## 11. Recommendations

1. Verify V1, V2, V4, V6, V8, V9, and V10 first, because each one can block or reshape the design before any helper is written.
2. Implement in this order: constants, gates and classifiers, firing and pass with ledgers, registration and log wiring, evolution clocks and entries, seats, Fifth Column and Open Gates, prepared cadres, installation and registry, lifecycle and Turned Regime, decisions, API, Chaos rows, presentation.
3. Keep the pass budget, batch limits, and watch durations as constants so the user's live evidence can tune them in one place.
4. Run the `chaosx_ai_probability_auditor` baseline for S1 to S10 as soon as the MCP server connects, before writing any `ai_chance`, `ai_will_do`, or MTTH value.
5. Route the Fallout coverage question in V9 to the Fallout owner even if 097 is deferred, because the stub already writes collaboration between non-occupying pairs.
6. Document the API in the two paired `.md` files and add one owner index row to `chaosx_dynamic_effects.md`, instead of copying contracts into the shared registry.
