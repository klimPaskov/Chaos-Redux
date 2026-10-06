# Event 097 Collaboration repo exploration handoff

Role: `chaosx_repo_explorer`, read-only. Date: 2026-10-06.
Evidence class: source review of the repository, the newer skill texts in the upload folder, and the offline wiki snapshot in `paradox_wiki/`.
No HOI4 Agent Tools MCP evidence exists for this handoff and no vanilla game file was readable. Both blockers are recorded under Risks and blockers.
Disposition of this document: implementation evidence and unresolved proposals only. Nothing here records user acceptance of any design.

## Scope read

- `AGENTS.md` at the repo root, plus the newer uploaded `AGENTS.md`. The upload adds that `while_loop_effect` and `for_loop_effect` stop after 1,000 iterations and that `scope_exists` is always true on a variable scope.
- Upload skill texts `chaos-redux-events.md` (read fully), `chaos-redux-subagents.md` (routing and explorer sections), and `chaos-redux-mtth.md`. The upload `chaosx_dynamic_effects.md` and `chaosx_dynamic_triggers.md` were diffed against the repo copies.
- Event files `events/097_collaboration.txt`, `events/095_occupation_revolt.txt`, `events/093_portugal_galicia.txt`, `events/094_half_gone.txt`, `events/052_intelligence_leak.txt`, `events/008_tensions_rising.txt`, and the head of `events/039_murder_mystery.txt`.
- Shared systems: event registration, selection, dispatch, event log, clusters, Chaos Meter, on_actions, achievements, super-event selectors, decision categories, AI strategy, occupation laws, ideologies, autonomous states, Fallout collaboration handling.
- Docs: `docs/events/`, `docs/systems/event_system/`, `docs/specs/052_intel_leaked_specs/`, `docs/specs/039_murder_mystery_specs/`, `docs/spreadsheets/*.csv`, `docs/achievements/`, `docs/super_events/`.
- Wiki snapshot pages: Effects, Triggers, Data structures, On actions, Defines, Ideology modding, Autonomy state modding, List of modifiers, Localisation.

## Primary findings (short)

1. 097 is registered and named but otherwise a stub. It has a raw `97` in `global.repeatable_events`, name rows in six selectors plus the names yml, a two-event stub file, and four localisation keys. It has no constants, effects, triggers, on_actions, ideas, decisions, achievements, evolution wiring, Event Details text, default-enable entry, cluster membership, docs, or spec. When this exploration read them, `docs/specs/097_collaboration_specs/` and `docs/plans/097_collaboration_plans/subagent_handoffs/` were empty folders. New spec files appeared in the specs folder during the run and were not read.
2. The Intelligence cluster does not exist in runtime source. The catalog and `docs/systems/event_system/event_clusters.md` call it cluster 8 with members 39 and 52, but `common/script_constants/event_cluster_constants.txt` registers only ids 1 to 8 and 12, and runtime id 8 is Diseases. The documented v2 renumbering (Intelligence 8, Diseases 13, Random Stuff 19) is not present in source. The 052 spec calls the same cluster 10.
3. A Medium cluster row gets an effective minimum tier of 1 (200+ Chaos) through `event_cluster_get_member_effective_min_tier`, even when the event itself is Chaos level 1.
4. Repeatable weight decays hard. Each firing halves the event's cap (`reduce_cap_factor = 0.5`), so natural repeated firings fall roughly 1000, 500, 250, 125, about 63. Any "repeated firings deepen it" design must say how many natural firings it expects.
5. Evolutions at 200, 400, 600, and 800 Chaos map exactly to `events_log_evolution_tier` 1 to 4 in `has_reached_current_evolution_tier`. The convention is `evolution_type = event id`, so 97.
6. The only native collaboration code in the repo is Fallout. Fallout snapshots collaboration, then resets every ordered country pair to zero with `set_collaboration`, and its transition verification fails if any pair still has `has_collaboration value > 0`. Event 097 must stand down while `fallout_transition_active` is set.
7. Per the wiki, `has_collaboration` and `core_compliance` read collaboration only within the target's cores that the scoped country currently occupies. A global symmetric layer between non-occupying countries may have no gameplay reading until occupation exists. This is unverified in-game and vanilla docs were not available.
8. Super-event slot 97 is already used by Event 015 `GFX_super_event_015_common_table`. The highest used slot is 116. Slot numbers are independent of event ids.
9. `Treaty of Tordesillas` appears nowhere in the repo. The catalog has no row for it. The only free catalog id below 167 is 163.
10. Event 095 and Event 093 are stubs. Event 052's accepted spec already expects a stable "Collaboration public contract" from 097 and says 052 must not create its own collaboration system.
11. Safest existing precedents for bounded world work are Event 021's cursor-based review through the global host pulse, Event 035's active-country registry, and Event 008's capped recipient selection. The only nested `every_country` plus `every_other_country` collaboration sweep is Fallout's one-time transaction.

## Relevant files

| Path | Why it matters | Evidence |
| --- | --- | --- |
| `events/097_collaboration.txt` | Current stub. Hidden root fires `chaosx.nr97.2` in every country, option runs `every_other_country = { add_collaboration = { target = ROOT value = 0.1 } }`. | Lines 22-56. TODO says it gives many errors. Picture sprite `GFX_report_event_molotov_ribentrop_handshake` is not defined in the repo. |
| `localisation/english/097_collaboration_l_english.yml` | Four stub keys. | `chaosx.nr97.1.t`, `chaosx.nr97.2.t/.d/.a`. |
| `common/scripted_effects/chaosx_logic_effects.txt` | Registration, chaos level registry, pool availability, weight recovery, fired handlers, `get_event_type`. | `:232` categories, `:333` raw 97, `:159` chaos registry, `:356` default-disabled seeding, `:588` unavailability chain, `:1023` recovery, `:1163` repeatable fired, `:1444` type resolver. |
| `common/script_constants/event_system_constants.txt` | Weight defaults and N/A reason ids. | `event_system_defaults :33` weight 1000, cap factor 0.5, recovery 20. Reason ids `:91` end at 43 (`:140`) then `unknown = 99` (`:141`). |
| `common/scripted_triggers/chaosx_settings_triggers.txt` | Reworked default-enable allowlist, evolution enable and tier gates, chaos level gate. | `:10-40`, `:42`, `:55`, `:60`, `:353`. |
| `common/scripted_effects/chaosx_settings_effects.txt` | Manual and automatic dispatch, prefire gates, weighted selection. | `:1640` trigger_selected_event, `:4344` candidate evaluation, `:4398` weighted pick, `:4525` and `:4542` dispatch, `:4938-4950` default `chaosx.nr[EVENT_ID].1`. |
| `common/scripted_effects/chaosx_events_log_effects.txt` | Default actor, history and evolution recorders, Event Details evolution previews, events tab weights. | `:198`, `:668`, `:967`, `:1914`, `:2542-2560` (008 previews), `:2868`, `:4590-4660`. |
| `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` | Name, detail, evolution, availability selectors. | See pattern 1 and 3. 097 name rows at `:2138`, `:11438`, `:13182`. |
| `common/scripted_localisation/chaosx_scripted_localisation_debug.txt` and `..._settings.txt` | Debug and settings name selectors. | Debug `:23`/`:409`. Settings `:1638`/`:2024` and `:5639`/`:6025`. |
| `localisation/english/chaosx_event_names_l_english.yml` | `chaosx.event_name.97: "Collaboration"`. | Line 98. |
| `localisation/english/chaosx_gui_l_english.yml` | Event Details keys, N/A reasons, cluster names and descriptions. | `:558-596`, `:639`, `:699`, `:432`, `:910`. |
| `common/script_constants/event_cluster_constants.txt` | Cluster ids, types, roles, severities, row ids, cooldowns, tuning groups. | `event_cluster_id :9`, `event_cluster_type :26`, `event_cluster_member_role :37`, `event_cluster_cooldown_days :67`, `event_cluster_member_danger :97`, `event_cluster_member_row_id :122`, `event_cluster_member_severity_floor :154`, `event_cluster_diseases :280`. |
| `common/scripted_effects/chaosx_event_cluster_effects.txt` | Cluster registry and rules. | `:203` definitions, `:623` belongs, `:886-910` severity floor, `:1311` member rows, `:2040` gates, `:2125` can fire, `:3850` fired state, `:4107` runtime context, `:4969` automatic firing. |
| `common/script_constants/chaos_meter_constants.txt` | Tier ranges, tier ids, history reasons, deltas. | Tier ranges `:8`, tier ids `:29`, history reasons `:43` (special block `:166`, ends at `murder_mystery_defeat = 221` on `:198`), deltas `:208`. |
| `common/scripted_effects/chaos_meter_effects.txt` | Chaos add API and generic sources. | `:4514` add, `:4287` history record, `:5939` annex, `:5960` puppet, `:6480` capitulation, `:6515` exile, `:5523` monthly occupation-law deaths. |
| `common/on_actions/chaosx_on_actions_chaos_meter.txt` | Generic Chaos hooks and the global-host daily pulse. | `on_daily :10`, `on_puppet :149`, `on_capitulation :327`, `on_annex :137`. |
| `common/scripted_effects/008_tensions_rising_effects.txt` and `common/script_constants/008_tensions_rising_constants.txt` | Minor repeatable evolution precedent with chaos add, previews, bounded pair selection. | `:62`, `:93`, `:219`, `:240`, `:491`. Constants `:9-25`. |
| `common/scripted_effects/035_great_depression_effects.txt` and `common/mtth/035_great_depression_mtth.txt` | MTTH due-day evolution pacing and registry processing. | `:2222`, `:2269`, `:4282`. |
| `common/scripted_effects/021_random_civil_war_parent_effects.txt` | Bounded cursor scheduler through the host pulse. | `:378-440`. |
| `common/scripted_effects/018_resources_found_decision_effects.txt` and `common/mtth/018_resources_found_mtth.txt` | Separate pre-fire and active MTTH evolution clocks. | `:2622`. |
| `common/scripted_effects/fallout_consolidated_effects.txt` | Only native collaboration code. | `:40187` snapshot, `:40320` has_collaboration, `:41788` reset, `:41867-41875` set_collaboration to zero, `:42004` reset flag. |
| `common/scripted_triggers/fallout_consolidated_triggers.txt` | Clean-world proof that forbids any collaboration pair. | `:31589`, `:32104`, `:32160`. |
| `common/occupation_laws/chaosx_occupation_laws.txt` | Chaos Redux occupation laws. | `cbrn_protected_occupation_administration`, `cbrn_coercive_security_occupation`, hidden `concentration`. |
| `common/ideologies/00_ideologies.txt` | Collaboration rules by ideology group. | `:33`, `:120`, `:184`. |
| `common/autonomous_states/012_africa_autonomy.txt` | Only mod autonomy states. Both set `can_create_collaboration_government = no`. | `:35`, `:83`. |
| `common/scripted_effects/012_africa_rsa_effects.txt` and `..._triggers.txt` | Snapshot and restore of `autonomy_collaboration_government`. | Effects `:56`, `:86`, `:120`. Triggers `:28`. |
| `common/achievements/chaos_redux_achievements.txt` | Single root registry. | `:1733` Event 008 section. Tail holds 035. |
| `localisation/english/chaosx_achievements_l_english.yml`, `interface/chaosx_achievements.gfx`, `gfx/achievements/` | Achievement name, tooltip, sprite triplets. | `:364-366`, `.gfx :1073-1083`. |
| `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt` | Slot to image, title, quote, remark, description. | Image selector rows to slot 116. |
| `common/decisions/categories/fallout_consolidated_categories.txt`, `condemnation_sanctions_categories.txt`, `famine_decision_category.txt`, `migration_decision_category.txt` | Global category gating. | See pattern 17. |
| `docs/specs/052_intel_leaked_specs/specs/052_intel_leaked_spec_part_5_evolutions_repeatability_and_connections.md` | Expects a 097 public contract. | `:331-335`. Matrix row in `matrices/052_intel_leaked_cluster_and_interaction_matrix.md:11`. |
| `docs/spreadsheets/chaos_redux_events_catalog.csv` and `chaos_redux_clusters_catalog.csv` | Readable catalog snapshots. The xlsx is an LFS pointer. | Row 97 line 220. Cluster 8 row. |

## Existing patterns

### 1. Event registration

What 097 has:
- Raw `add_to_array = { global.repeatable_events = 97 }  # COLLABORATION` at `common/scripted_effects/chaosx_logic_effects.txt:333`. Most tail registrations are raw integers, for example 82 to 87, 94, 95, and 97. Events with identity constants use `constant:<name>.id`.
- `get_event_type` (`:1444`) scans major, then repeatable, then fire-once arrays and returns `constant:event_system_event_type.repeatable` (2) for 097.
- Chaos level 1 is the default. `initialize_event_chaos_level_registry` (`:159`) assigns `tier_0` to every event except white peace, acid rain, and black friday. `event_required_chaos_level_is_met` is at `chaosx_settings_triggers.txt:353`. No change is needed for 097.
- Name loc `chaosx.event_name.97` at `chaosx_event_names_l_english.yml:98`.
- Name rows in `GetEventName` (debug `:23`, row `:409`), `GetEventsLogEvolutionSourceEventNameView` (events log `:1164`, row `:2138`), `GetEventsLogHistoryEventName` (`:9558`, row `:11438`), `GetEventsLogClusterMemberEventName` (`:12227`, row `:13182`), `GetSettingsEventName` (settings `:1638`, row `:2024`), `GetLastEventName` (`:5639`, row `:6025`).

What 097 lacks:
- Per-event availability. `evaluate_event_pool_candidate_unavailability` (`:588-847`) is an `else_if` chain keyed on `event_id`. 097 has no branch, so it can only show N/A for chaos level, disabled, already fired, or zero weight.
- Adding a new N/A reason needs five edits together: a constant in `event_system_event_unavailability_reason` (next free id 44), a branch in the chain, rows in `GetEventsLogEventAvailabilityReason` (events log `:13582`) and `GetEventsLogClusterMemberAvailabilityReason` (`:13421`), and keys `chaosx.events_log.events.na_reason.<reason>` and `chaosx.events_log.cluster.member.na_reason.<reason>` (`chaosx_gui_l_english.yml:446-449`, `:558-596`). The events tab builder at `chaosx_events_log_effects.txt:4590-4660` writes weight `-1` when a reason exists.
- Prefire readiness. `fire_event_by_temp_id_no_cluster` (`chaosx_settings_effects.txt:4542`) holds per-event blocks that set `event_single_fire_allowed = 0`, for example `tensions_rising_prepare_random_event_fire`. History and actor rows are recorded by `on_repeatable_event_fired` before the root event's `immediate` runs, so any actor or context must be prepared in a prefire helper. 097 needs no actor, but any chosen scope data would need this route.
- Default actor. `events_log_set_default_actor_for_current_event` (`chaosx_events_log_effects.txt:198`) has no 097 branch, so history rows carry no actor.
- Event Details text. `GetEventsLogEventDetailDescription` (events log `:5717`) has no 097 row, so Event Details shows `chaosx.events_log.window.event_details.entry_placeholder.generic` (selector fallback `:6814`, text at `chaosx_gui_l_english.yml:639`). The 008 pattern is a row at `:6741` pointing to `chaosx.events_log.window.event_details.tensions_rising`, defined in the event-owned yml `008_world_tension_rises_l_english.yml:72`.
- Default enable. `event_log_event_is_reworked_default_enabled` (`chaosx_settings_triggers.txt:10-40`) does not list 97. `initialize_default_disabled_events_for_rework_queue` (`chaosx_logic_effects.txt:356`, called at `:142`) therefore seeds 97 into `global.disabled_events`. Add `check_variable = { event_id = <constant or 97> }` to the allowlist in the same change that finishes registration and log wiring.

Repeatable weight recovery:
- `global.default_event_weight` is 1000. `on_repeatable_event_fired` (`:1163`) halves the event's cap (`reduce_cap_factor = 0.5`, then `round_temp_variable`) and sets weight to 0, then to the floor 1.
- `update_repeatable_event_weights` (`:1023`) runs on every minor firing and adds `global.minor_event_recovery_rate` (20) up to the cap, only while the event's chaos level is met.
- Selection in `evaluate_random_event_selection_candidate` (`chaosx_settings_effects.txt:4344`) rejects a candidate whose weight times 100 rounds below 1.
- Settings can override recovery and cap reduction (`chaosx_settings_effects.txt:122-125`, `:4219-4231`).

### 2. Event clusters

- Registered runtime ids (`event_cluster_constants.txt:9-19`): wars 1, liberations 2, diplomatic_panic 3, peace 4, natural_disasters 5, formables 6, economy_positive 7, diseases 8, random_stuff 12. There is no `intelligence` key and neither 39 nor 52 appears in any runtime member list (`grep` of `chaosx_event_cluster_effects.txt` returns nothing).
- Catalog (`chaos_redux_clusters_catalog.csv`) row 8: Intelligence, members `39, 52`, severities `Medium, Low`, `Minor Fire-Once`, Chaos level 1, status Needs Testing. `docs/systems/event_system/event_clusters.md:269` says runtime v2 reassigns ids 8 to 12 and puts Diseases at 13 and Random Stuff at 19. Source contains no such remap (`event_cluster_probability_state.version = 1`, no migration code). Treat the numeric Intelligence id as unresolved. `052_intel_leaked_catalog_alignment.md:27` uses id 10.
- Adding a cluster (per skill and the file header at `chaosx_event_cluster_effects.txt:1-14`):
  1. Add a key to `event_cluster_id` that is free. Ids 9, 10, 11 and 13+ are free in source. Id 8 is taken.
  2. Add a tuning group, for example `event_cluster_intelligence = { schema... unlock_tier = 0 }`, copying `event_cluster_diseases` (`event_cluster_constants.txt:280`).
  3. Append to `initialize_event_cluster_definitions` (`:203`) the id, `constant:event_cluster_type.one_time`, and the unlock tier.
  4. Add an `else_if` branch to `load_event_cluster_members` (`:1311`) using `event_cluster_append_member_definition` (`:1294`). Each row sets `event_cluster_member_event_id`, `_role`, `_min_tier`, `_severity`, `_row_id`, `_primary_trigger`.
  5. Add stable row ids to `event_cluster_member_row_id` (`event_cluster_constants.txt:122`). Existing ids use cluster id times 1000 plus a sequence. Ids 9001, 10001, 11001 and 12000+ (Random Stuff base 12000) constrain the choice.
  6. Add cooldown handling. Cooldown flags are hard-coded per cluster in `event_cluster_check_cluster_gates` (`:2040-2120`), `evaluate_event_cluster_unavailability_reason` (`:2353-2400`), and `mark_event_cluster_fired_state` (`:3850-3950`), plus `event_cluster_cooldown_days.<cluster>`.
  7. Add the cluster name, type, and description selectors and keys. For Diseases the touchpoints are 5 rows in events log scripted loc (`:596`, `:11550`, `:11680`, `:11772`, `:11940`), 1 row in settings scripted loc (`:526`), keys `chaosx.event_cluster.diseases.name` (`chaosx_gui_l_english.yml:910`) and `chaosx.events_log.window.cluster_details.description.diseases` (`:432`).
- Medium severity: `event_cluster_get_member_severity_floor` maps Medium to floor 1 and `event_cluster_get_member_effective_min_tier` (`:902`) takes the larger of the declared tier and the floor. `event_cluster_member_check_availability` (`:1701`) rejects a row below that tier unless `event_cluster_member_event_system_only >= 1`. A Medium 097 row therefore joins cluster activations only from tier 1 (200+ Chaos), while the event itself still fires alone from Chaos level 1.
- Fire-Once cluster with a repeatable member: `event_cluster_check_cluster_gates` blocks a `one_time` cluster once its id is in `global.fired_event_clusters`. `try_fire_event_cluster_for_selected_event` (`:4969`) runs only when `automatic_event_firing_context > 0`. If no cluster fires, `fire_event_by_temp_id` (`chaosx_settings_effects.txt:4525`) falls through to `fire_event_by_temp_id_no_cluster`, so a consumed Fire-Once cluster does not stop 097 from firing alone. Member events keep their own repeatable behavior because `on_repeatable_event_fired` and the cluster pacing flag `event_cluster_member_fire_context` are separate. The catalog already pairs a Fire-Once cluster with a repeatable member: 052 is `Minor Repeatable` in the catalog and runtime.
- Catalog drift for the other members: runtime registers 39 as repeatable (`chaosx_logic_effects.txt:301`) while the 039 spec, its event header, and the catalog treat it as Minor Fire-Once.
- Catalog edit for 097: Cluster ID column from blank to 8, and the cluster row members to `39, 52, 97` with severities `Medium, Low, Medium`. The workbook is the only editable source (see blockers).

### 3. Evolution logging

Shared context (`record_events_log_evolution_entry`, `chaosx_events_log_effects.txt:967`):
- Temp variables `events_log_evolution_event_id`, `events_log_evolution_type`, `events_log_evolution_stage`, `events_log_evolution_tier`, `events_log_evolution_has_actor`, plus regular event target `events_log_evolution_actor` when the milestone has an actor. Optional input `events_log_evolution_date_override`.
- Gate with `is_current_evolution_enabled` (`chaosx_settings_triggers.txt:55`). It combines `has_disabled_current_evolution` (global flag `events_log_disabled_evolution_<event>_<type>_<stage>`, `:42`) and `has_reached_current_evolution_tier` (`:60`). That second trigger maps `events_log_evolution_tier` 1, 2, 3, 4, 5 to `global.chaos_meter_value` at least 200, 400, 600, 800, 1000 through `constant:chaos_meter_tier_range.tier_N.min`. Evolutions at 200, 400, 600, and 800 therefore use tiers 1 to 4.
- Evolution type ids follow event ids (`008_tensions_rising_constants.txt:16` is 8, 013 is 13, and so on), so 097 would use `evolution_type = 97`.

Event-details catalog rows: `events_log_add_event_detail_evolution_preview` (`:2868`) is called once per stage from the per-event blocks in `events_log_rebuild_open_event_details_view` (`:1914`). The 008 block at `:2542-2560` sets `events_log_event_detail_preview_type/_tier/_stage` four times and appends to `global.events_log_event_detail_evolution_type/tier/stage/enabled_entries`.

Display selectors carrying 008's stage rows (all in `chaosx_scripted_localisation_events_log.txt`): `GetEventsLogEvolutionTypeView` (`:1021`), `GetEventsLogEvolutionNameView` (`:2479`), `GetEventsLogSelectedHistoryEvolutionTypeView` (`:3169`), `GetEventsLogSelectedHistoryEvolutionNameView` (`:3610`), `GetEventsLogEventDetailEvolutionTypeView` (`:4286`), `GetEventsLogEventDetailEvolutionTitle` (`:7240`), `GetEventsLogSelectedEvolutionTitle` (`:8033`), `GetEventsLogSelectedEvolutionBody` (`:8834`). Type label keys look like `chaosx.events_log.evolution.type.tensions_rising` (`008_world_tension_rises_l_english.yml:71`).

Precedents:
- Event 008 (Minor Repeatable, cluster 3). Stage is recomputed at every firing from the `chaos_tier` global flag in `get_tensions_rising_stage` (`008_tensions_rising_effects.txt:62`). `record_tensions_rising_evolution_if_needed` (`:240`) sets the shared context, tests `is_current_evolution_enabled`, calls `record_events_log_evolution_entry`, then sets `tensions_rising_stage_N_recorded` so each milestone logs once. An evolved opening is instant because the first firing already reads the current tier. No MTTH is used. Chaos gain is a separate concrete consequence in `apply_tensions_rising_stage_chaos` (`:219`).
- Event 013 (Minor Repeatable). `natural_disaster_refresh_evolution_state` (`013_natural_disasters_effects.txt:981`) sets `events_log_evolution_tier/stage` per level and tests the enable trigger. `natural_disaster_record_reached_evolutions` (`:1018`) logs once per level behind `natural_disaster_evolution_N_logged` global flags and skips manual bypass calls.
- Event 009 (`009_white_peace_effects.txt:1150`) uses the same enable gate and records when newly reached.
- Event 035 (Minor Repeatable) uses MTTH pacing. `great_depression_try_evolution_activation` (`035_great_depression_effects.txt:2269`) reads `mtth:great_depression_financial_contagion_activation_interval` into a due day (`global.num_days` plus delay), stores it on the country, and applies the floor when `global.num_days` reaches it. `great_depression_record_enabled_evolution_milestones` (`:2222`) logs each enabled milestone once behind global `*_logged` flags. MTTH entries are in `common/mtth/035_great_depression_mtth.txt:8-60`. The day-based check runs from the registry pulse (pattern 16), never from a new world scan.
- Event 018 (Minor Repeatable). Separate pre-fire and active paths exist for each evolution. `common/mtth/018_resources_found_mtth.txt` defines `resources_found_evolution_N_prefire_interval` and `_active_interval`, and `resources_found_schedule_evolution_paths` (`018_resources_found_decision_effects.txt:2622`) starts engine missions as hidden clocks with the MTTH value as the timeout. `docs/events/018_resources_found/overview.md:87-115` states that a game entering at a higher evolution still starts the earlier visible chain gradually.
- Skill rule (`chaos-redux-events.md`): evolved incidents pace through MTTH with a base near 90 days unless the event has not fired yet. Evolution state itself gives zero Chaos.
- Disabled-evolution rule: do not set `*_recorded` or follow-up flags unless `is_current_evolution_enabled = yes` was part of the same `limit`, and keep a clean alternate route.

### 4. Chaos Meter API

Inputs and call pattern (`add_chaos_meter_value`, `chaos_meter_effects.txt:4514`):
```
set_temp_variable = { chaos_change = <signed amount> }
set_temp_variable = { chaos_history_reason = constant:chaos_meter_history_reason.special.<name> }
set_temp_variable = { chaos_history_reason_custom = 1 }
add_chaos_meter_value = yes
```
- Negative `chaos_change` removes Chaos. The effect rounds the value, clamps at 0, updates the tier, and records history. The effect is blocked while `settings_chaos_meter_disabled` is set and above 1000 except for the singularity reason.
- Optional inputs: `save_event_target_as = chaos_history_actor` in the actor's scope and `chaos_history_target_count`. Reasons under `generic`, `settings`, and `world_state.world_tension_rise..deaths_rise` ignore the actor (`record_chaos_meter_history_entry :4287`).
- Reasons live in `chaos_meter_constants.txt` under `chaos_meter_history_reason.special` (`:166`, ids 190 to 221, the last is `murder_mystery_defeat` on `:198`). The next free special id is 222. Each reason needs a branch in `GetChaosMeterHistoryReason` (`chaosx_scripted_localisation_chaos_meter.txt:812`, for example the 008 row at `:1559`) and a loc key `chaos_meter.history.reason.special.<name>`. 008 keeps its key in its own yml (`008_world_tension_rises_l_english.yml:70`), 039 in `chaosx_chaos_meter_l_english.yml:501-505`.
- Event-owned amounts live in event constants (for example `tensions_rising_chaos_gain.stage_N`), not in `chaos_meter_delta`.
- Generic sources (all in `chaosx_on_actions_chaos_meter.txt`, bodies in `chaos_meter_effects.txt`):

| Hook | Source effect | Default delta |
| --- | --- | --- |
| `on_war_relation_added`, `on_peace`, `on_nuke_drop` | `chaos_meter_on_war_relation_added`, `_on_peace`, `_on_nuke_drop` | war 1 or 5, peace -1 or -3, nuke ladder |
| `on_capitulation` (`:327`) | `chaos_meter_on_capitulation` (`:6480`) | +3 major, +1 minor, only when `uses_normal_civilian_systems` |
| `on_uncapitulation` | `_on_uncapitulation` | -1 |
| `on_annex` (`:137`) | `_on_annex` (`:5939`) | +10 major, +2 minor |
| `on_subject_annexed`, `on_subject_free` | `_on_subject_annexed`, `_on_subject_free` | +2 and -1 or -3 |
| `on_puppet` (`:149`) | `_on_puppet` (`:5960`) | +3 major, +1 minor |
| `on_liberate`, `on_release_as_free` | `_on_liberate`, `_on_release_as_free` | -2 or -5 and -3 |
| `on_stage_coup`, `on_coup_succeeded` | `_on_stage_coup`, `_on_coup_succeeded` | +1 each |
| `on_government_exiled`, `on_exile_government_reinstated` | `_on_government_exiled` (`:6515`), `_on_exile_reinstated` (`:6528`) | +1 and -1 |
| `on_join_faction`, `on_leave_faction`, `on_create_faction`, `on_guarantee`, `on_join_allies`, `on_wargoal_expire`, `on_ruling_party_change` | matching helpers | small signed values |
| `on_monthly` host pulse | monthly decay | -1 |

- Puppet and subject creation: per the wiki (`On actions - Hearts of Iron 4 Wiki.md:260`), `on_puppet` fires only for puppeting in a peace conference, and `on_release_as_puppet` is not hooked by any generic Chaos source. A collaboration government created by `instantiate_collaboration_government` (wiki Effects `:4723`) is a script effect, so no generic puppet or subject-creation source is documented to fire for it. Whether the engine also fires `on_puppet` for it is unconfirmed. What would fire later: `on_capitulation`, `on_annex`, `on_subject_annexed`, `on_subject_free`.
- Event-owned Chaos must come from a concrete consequence and must not copy those sources. Also note the wiki scope for `on_puppet` is ROOT = puppeted nation and FROM = overlord, while `chaos_meter_on_puppet` logs "FROM was puppeted by THIS". Direction is unverified in source.

### 5. On_actions that matter

Generic Chaos hooks are listed in pattern 4. Other shared hooks:
- `common/on_actions/chaosx_on_actions_system.txt`: `on_startup` (initialization, per-country timers) and `on_daily` (per-country event timers, tag-switch detection). `on_daily` fires `select_weighted_random_event_id` then `fire_event_by_temp_id` when the country timer reaches 0.
- `chaosx_on_actions.txt`: `on_startup` startup history grants and `on_state_control_changed` CBRN mask ledger transfer. Header notes that `on_daily`, `on_weekly`, `on_monthly` evaluate for all countries.
- Event-owned files attach per-event logic to native hooks. Examples: `008_tensions_rising_on_actions.txt` (`on_war_relation_added`), `091_the_great_revolution_on_actions.txt` (`on_capitulation`, `on_uncapitulation`, `on_monthly_REV`), `039_murder_mystery_on_actions.txt` (`on_startup` plus `on_daily_CXT`).
- Hooks that react to capitulation, annex, puppet, state control, exile, or government change already used by other systems and likely to fire around a collaboration layer: `genocide_crisis_on_actions.txt`, `humanitarian_runtime_on_actions.txt`, `fallout_consolidated_on_actions.txt`, `condemnation_sanctions_on_actions.txt`, `cbrn_occupation_on_actions.txt`, `biological_facility_capture_on_actions.txt`, and event files 001, 002, 003, 006, 010, 011, 012, 014, 015, 016, 017, 018, 020, 021, 023, 027, 029, 032, 033, 035.
- `on_state_control_changed` has ROOT = new controller, FROM = old controller, FROM.FROM = state (wiki `:450`). `on_capitulation` has ROOT = capitulated country, FROM = winner (`:254`). `on_government_exiled` has ROOT = exile, FROM = host (`:442`).
- Rule: do not add new periodic all-country on_actions without permission (AGENTS.md section 1, rule 8). The existing host pulse is the only sanctioned periodic route (pattern 16) and extending it is still a world-iteration decision for the user.

### 6. Occupation, compliance, resistance

- Occupation laws: `common/occupation_laws/chaosx_occupation_laws.txt` is the only mod file. It defines hidden `concentration`, `cbrn_coercive_security_occupation`, and `cbrn_protected_occupation_administration` (icon 3, visible and available behind `cbrn_occupation_protected_administration_authorized`, `fallback_law = military_governor_occupation`). Constants for these laws mirror `cbrn_occupation_constants.txt`. Vanilla laws such as `foreign_civilian_oversight` are read but not redefined (`chaos_meter_effects.txt:5620-5656`, `famine_core_effects.txt:893-960`).
- Resistance and compliance modifiers: dynamic modifiers using `resistance_target`, `compliance_growth`, or `compliance_gain` in `cbrn_occupation_dynamic_modifiers.txt`, `014_cannibalism_dynamic_modifiers.txt`, `015_utopia_manifesto_state_modifiers.txt`, `genocide_crisis_dynamic_modifiers.txt`, `fallout_consolidated_dynamic_modifiers.txt`.
- Effects that write them: `add_compliance` and `add_resistance` in `007_fury_effects.txt:987-1700`, `012_africa_gods_effects.txt:2167`, `019_infantry_spawn_derivative_package_effects.txt:6976-7122`. `set_compliance` and `set_resistance` in `003_holy_realm_effects.txt` and `common/national_focus/003_holy_realm.txt`, `germany_mengele_clone_army.txt`. `events/053_mysterious_man.txt:49` uses `add_resistance = 100` on non-core controlled states.
- Triggers: state `compliance >` gates in `007_fury_triggers.txt:233-244` and `016_brilliant_scientist_kruger_state_decision_triggers.txt:394`. The native country trigger `core_compliance = { occupied_country_tag = LIT value > 80 }` appears once, in `common/decisions/formable_nation_decisions.txt:1198-1210`. `core_resistance` is a repo constant name only. No Chaos Redux file reads `has_collaboration` outside Fallout.
- Monthly Deaths pass: `air_contamination_monthly_update` (`chaos_meter_effects.txt:5523`) already applies occupation-law civilian deaths for resistance-bearing occupied states, so occupation changes feed an existing monthly pass.
- Systems with their own occupation logic that a collaboration layer will touch: Event 007 Fury occupation pressure, CBRN occupation, camp repression rework (`camp_repression_rework_*`), genocide crisis. See the wiki `Defines` entries under pattern 7 for engine effects of collaboration at capitulation.

### 7. Collaboration governments and autonomy

- Autonomous states: `common/autonomous_states/012_africa_autonomy.txt` defines only `autonomy_africa_federal_member` and `autonomy_africa_integrated_region`, both with `can_create_collaboration_government = no` (`:35`, `:83`). There is no override of vanilla `autonomy_collaboration_government`.
- Africa RSA only snapshots and restores that vanilla state: flag `africa_rsa_autonomy_collaboration_government` (`012_africa_rsa_effects.txt:56`, `:86`), restore `set_autonomy = { ... autonomy_state = autonomy_collaboration_government end_wars = no end_civil_wars = no }` (`:120`), and `has_autonomy_state = autonomy_collaboration_government` in `012_africa_rsa_triggers.txt:28`. The snapshot lists many Kaiserreich-style autonomy states, so other mods' states are expected.
- Ideologies: `common/ideologies/00_ideologies.txt` is a full copy of the vanilla file name (281 lines, first present in git history in commit `23c48bb2`) with Chaos Redux additions (for example the `ritual_predation` neutrality subideology at `:221`). Collaboration rules inside it: `democratic` has `can_create_collaboration_government = no` (`:33`), `communism` has `can_collaborate = yes` (`:120`), `fascism` has `can_collaborate = yes` (`:184`), and `neutrality` has neither. Wiki: `can_create_collaboration_government` is an ideology rule and `can_collaborate` marks ideologies that can create collaboration governments (Ideology modding `:44`, `:73`). Whether `add_collaboration` itself checks them is not documented in the snapshot.
- Not used anywhere in the repo: `instantiate_collaboration_government`, `country_to_initiate`, `operation_collaboration_government`, and `set_autonomy` to `autonomy_collaboration_government` for creation. `create_dynamic_country` is used by Fallout fractures, zombie projects, Mengele, triggerable scenarios, and the 039 dynamic carriers (`common/country_tags/039_murder_mystery_countries.txt`). The repo holds no `dynamic_tags` pool and no collaboration carrier tags. The wiki says collaboration governments are dynamic countries (`Triggers :652`) and that the `country_to_initiate` temp variable names the target (`Effects :4723`). The vanilla tag pool used by that scripted effect could not be inspected.
- Wiki effect semantics (`Effects :1246-1247`, `:1320-1335`): `add_collaboration` and `set_collaboration` take `target = <country>` and `value = <0-1>` and add or set "collaboration in TAG with the scoped country". Trigger `has_collaboration` is "the current scope has a collaboration level in the target scope", with the note that the target is occupied by the current scope, and the Data structures variable reads only within the target's cores currently occupied by the scope (`Data structures :1512`). Fallout's calls read as scope = occupier and target = occupied. The stub's `every_other_country = { add_collaboration = { target = ROOT } }` therefore gives every other country collaboration inside ROOT.
- Wiki defines (`Defines :480-482`): `SURRENDER_LIMIT_REDUCTION_PER_COLLABORATION` 0.3, `SURRENDER_RECIPIENT_SCORE_PER_COLLABORATION` 1.0, `COMPLIANCE_PER_COLLABORATION` 1.0. If those values hold in the installed version, global collaboration lowers surrender limits, biases who receives a capitulation, and becomes compliance at capitulation. `common/defines/chaos_redux_defines.lua` is empty and overrides none of them.

### 8. Fallout collaboration handling

- `fallout_take_world_snapshot` (`fallout_consolidated_effects.txt:40187`) walks `every_other_country` from each source and records a bilateral memory row (`fallout_record_bilateral_memory :40159`) when `has_collaboration = { target = PREV value > 0 }`. Constant `fallout_diplomacy_memory_type.collaboration = 8` (`fallout_consolidated_constants.txt:9065`). Pair dedup uses `THIS.id` comparisons (`source_id < target_id`) for symmetric relations.
- `fallout_reset_old_world_diplomacy` (`:41788`) is a one-time, retry-safe coordinator transaction. It first waits for any peace conference, then sweeps `every_country = { every_other_country = { if has_collaboration ... set_collaboration = { target = PREV value = 0 } } }` (`:41867-41875`). Order is exiles, volunteers, purchase contracts, collaboration, civil-war links and white peace, truces, subjects, factions, then guarantees, access, docking rights, market access, non-aggression pacts, embargoes, and finally resource rights.
- `fallout_old_world_diplomacy_proven_surfaces_are_clean` (`fallout_consolidated_triggers.txt:32104`) includes `NOT = { any_country = { any_other_country = { has_collaboration = { target = PREV value > 0 } } } }` (`:32160`). If it fails, `fallout_transition_diplomacy_validation_failed` and error `old_world_diplomacy_incomplete` are set. On success `fallout_transition_collaboration_reset_complete` is set (`:42004`). A leftover 097 pair would block the proof.
- Gates: `fallout_world_rewrite_callbacks_are_allowed = { NOT = { has_global_flag = fallout_transition_active } }` (`:31589`). Chaos hooks already use it for uncapitulation, ruling-party change, nuke, and exile reinstatement. Event 023's achievement trigger also excludes `fallout_active`, `fallout_transition_active`, `world_end_final_silence`, and `world_end_final_silence_completed`.
- Plan record: `docs/plans/air_cleanliness_fallout_plans/BLOCKERS_AND_DECISIONS.md:224` lists collaboration among surfaces the transaction clears.
- Pair-processing note: Fallout uses scope iterators for ordered pairs, which have no 1,000-iteration cap. Any `for_loop_effect` or `while_loop_effect` over pairs would hit that cap.

### 9. Intelligence

- No Chaos Redux file defines or overrides `operation_collaboration_government`. `common/operations/chaosx_bioweapon_operations.txt` and `common/operation_phases/chaosx_bioweapon_operation_phases.txt` define only bioweapon operations. `on_operative_captured` is hooked in `chaosx_on_actions_biological_operations.txt`.
- Agency creation and upgrades appear in Event 003 effects (`003_holy_realm_effects.txt:645-664`), `common/national_focus/iceland.txt`, and Event 016 focus effects. `common/ai_strategy/011_secret_alliance.txt` sets `intelligence_agency_usable_factories`. Event 052 stub gives every country `add_intel` 100 per branch (`events/052_intelligence_leak.txt:42-62`).
- Event 039 Murder Mystery: implemented (`events/039_murder_mystery.txt`, `common/scripted_effects/039_*`, `common/on_actions/039_murder_mystery_on_actions.txt` with `on_startup` provider registration and `on_daily_CXT`, Chaos reasons 217 to 221, super-event slots 111 to 113, dynamic country carriers). Spec package `docs/specs/039_murder_mystery_specs/` says Minor Fire-Once, Chaos level 1, Intelligence cluster Medium member (`..._package_index.md`, `..._spec_part_11_scenario_cluster_integrations.md:140-160`). No `docs/events/039*` page exists.
- Event 052 Intel Leaked: stub only. Spec package `docs/specs/052_intel_leaked_specs/` is accepted planning source. It keeps 052 as the Low repeatable member, uses a public helper contract (read-only facts plus bounded request effects) for other events, and gives 097 a hook: exposed contact chains may endanger collaboration networks and "Event 52 should not create a new collaboration system" (`..._spec_part_5...md:331-335`).
- Unavailable catalog placeholders that touch this theme: 111 Resistance, 128 Autonomy, 142 Partisans, 145 The Book, 146 Add operative, 147 Counterintelligence.

### 10. Event 095 Occupation revolt

- Source: `events/095_occupation_revolt.txt:22-63`. Hidden root picks `random_country` with `is_government_in_exile = yes`, transfers every enemy-controlled core state back, builds a "Revolt Division" template, spawns one division per owned state, and fires `chaosx.nr95.2` (report, +0.15 war support, +50 political power, news 76). There is no trigger or availability check. If no exile exists the root silently does nothing. Registered as raw `95` in `global.repeatable_events` (`:332`).
- Localisation `095_occupation_revolt_l_english.yml` has six keys.
- Catalog row 95 describes more than the source does: "An exiled country launches a revolt from occupied territory. When no occupation exists, a dormant claimant can appear before any war begins." The dormant-claimant branch is not implemented.
- No spec, plan, or `docs/events/095*` exists. The only prose mention is `docs/plans/famine_and_migration_system_plans/subagent_handoffs/event043_050_051_095_adapter_owner_patch.md`, which says Event 095 has no exact local famine, deportation, forced-labor, or protected-administration facts and must not call occupation adapters from its root or transfer loop. Related but separate catalog rows are 63 End Subject Status (To Be Reworked) and the Unavailable placeholders 111 Resistance and 142 Partisans.
- Link points for 097: 095 reads exile governments and enemy-controlled cores only. It does not read collaboration, compliance, or resistance.

### 11. Achievements

- One root registry, `common/achievements/chaos_redux_achievements.txt` (`unique_id = chaos_redux_achievements`, 4,294 lines). Event sections use banner comments such as `# EVENT 008 - TENSIONS RISING ACHIEVEMENTS` (`:1733`). Block form: `possible = { custom_override_tooltip = { tooltip = achievement_available_as_any_tag_tooltip always = yes } }` and `happened = { custom_override_tooltip = { tooltip = <key> <condition> } }`, optional `hidden = yes`. Ids use `<id>_<slug>_<name>`, for example `008_tensions_rising_thin_wire`.
- Localisation: `localisation/english/chaosx_achievements_l_english.yml` (`<id>_NAME`, `<id>_DESC`, and a tooltip key, `:364-366`), or event-owned files such as `012_africa_achievements_l_english.yml`. Art: three DDS per id in `gfx/achievements/` (`<id>.dds`, `_grey`, `_not_eligible`), sprites `GFX_achievement_<id>`, `_grey`, `_not_eligible` in `interface/chaosx_achievements.gfx` (`:1073-1083`). Docs: either the event overview (008) or `docs/achievements/<id>_<slug>/achievements.md` (006, 011, 014, 016, 018, 019).
- Forced-setup disqualifiers (no single shared trigger). The common set is `is_ai = no`, `NOT = { is_debug = yes }`, `NOT = { has_country_flag = force_trigger_mode_enabled }`, `NOT = { has_country_flag = chaosx_test_country_initialized }`, an event-specific manual-disqualified global flag, and a triggerable-scenario-launched flag. Examples: `023_sov_nuclear_bombs_achievement_triggers.txt:8-27`, `028_asteroid_incoming_achievement_triggers.txt:9-20`, `012_africa_achievement_triggers.txt:12`, `020_black_plague_achievement_triggers.txt:20`, `021_random_civil_war_achievement_effects.txt:14`. Settings set `events_log_manual_event_detail_trigger` when an event is fired from Event Details (`chaosx_settings_effects.txt:1761`, `:4707`), and `force_trigger_selected_event` sets `temp_bypass_checks` (`:1640-1700`).
- Achievement conditions should read durable evidence and disqualifiers, not the event firing flag (`docs/events/018_resources_found/overview.md:157` and the `chaos-redux-events` skill: do not convert hard achievements into automatic unlocks).

### 12. Special-country exclusions

- `common/scripted_triggers/chaosx_dynamic_triggers.txt`: `is_special_chaos_country` (`:10`), `is_actual_nonhuman_country` (`:45`), `uses_normal_civilian_systems` (`:70`, equals `is_actual_nonhuman_country = no`). Bodies are inside `hidden_trigger`. New event-created chaos countries are registered in these triggers and in `chaosx_dynamic_triggers.md`. The upload copy of the md differs from the repo copy (wording only plus migration cross references).
- There is no shared "valid ordinary country" trigger. Each world-wide event builds its own on top of `exists = yes` and the classifiers, for example `is_tensions_rising_valid_diplomatic_country` (`008_tensions_rising_triggers.txt:36`, also excludes subjects and capitulated), `is_tensions_rising_world_tension_source_country` (`:43`), `random_civil_war_is_normal_human_country` (`021_random_civil_war_triggers.txt:37`), and `doctrine_research_country_has_valid_action`.
- Usage scale: 144 matching lines for the special-country exclusion and 153 for `uses_normal_civilian_systems = yes` across `common` and `events`. Decision categories use both inside `hidden_trigger` (pattern 17). Skill rule: player-facing callers must give a custom tooltip instead of exposing the classifier.

### 13. Super-event slots

- Slots are global integers carried in the `super_event_visible` global flag value. `chaosx_scripted_localisation_super_events.txt` holds five selectors, each with 75 rows: `GetSuperEventImage`, `GetSuperEventTitle`, `GetSuperEventQuote`, `GetSuperEventRemark`, `GetSuperEventDesc`. The scripted GUI is `common/scripted_guis/chaosx_scripted_gui_super_events.txt` (`chaosx_super_events`, close click clears the flag). Sprites live in `interface/chaosx_super_events.gfx`. Audio uses `global.current_super_event_audio_id` and `play_current_super_event_sound`.
- Used slots: 1 to 3, 5 to 24, 49 to 53, 59 to 77, 82 to 87, 90 to 104, 108, 111 to 116. Highest is 116 (`GFX_super_event_116_asteroid_impact`). Free gaps include 4, 25 to 48, 54 to 58, 78 to 81, 88, 89, 105 to 107, 109, 110, and everything above 116.
- Slot 97 is taken: `GFX_super_event_015_common_table` (image) and keys `chaosx_super_event.97.t/.q/.a/.d`. A 097 super-event cannot use slot 97.
- Minor repeatable events that own super-events: 013 (slots 67 to 72), 018 (82 to 84), and 039 (111 to 113, while registered repeatable at runtime). Event 008 explicitly has none. Research docs sit under `docs/super_events/<id>_<slug>/`.

### 14. Conventions

Event-owned file names (examples from 008, 033, 039):

| Surface | Path pattern | Example |
| --- | --- | --- |
| Events | `events/<id>_<slug>.txt` | `events/008_tensions_rising.txt` |
| Constants | `common/script_constants/<id>_<slug>_constants.txt` plus topic files | `008_tensions_rising_constants.txt`, `039_murder_mystery_constants.txt` |
| Scripted effects and triggers | `common/scripted_effects/<id>_<slug>_effects.txt`, `common/scripted_triggers/<id>_<slug>_triggers.txt` plus topic files | `033_acid_rain_achievement_effects.txt`, `039_murder_mystery_integration_triggers.txt` |
| Ideas | `common/ideas/<id>_<slug>_ideas.txt` | `008_tensions_rising_ideas.txt` (hidden ideas) |
| Decisions and categories | `common/decisions/<id>_<slug>_decisions.txt`, `common/decisions/categories/<id>_<slug>_categories.txt` | 033 and 039 |
| On_actions | `common/on_actions/<id>_<slug>_on_actions.txt` | 008, 033, 039 |
| Opinion modifiers | `common/opinion_modifiers/<id>_<slug>_opinion_modifiers.txt` | 008 |
| Dynamic modifiers | `common/dynamic_modifiers/<id>_<slug>_dynamic_modifiers.txt` | 033 |
| MTTH | `common/mtth/<id>_<slug>_mtth.txt` | 018, 035 |
| Scripted GUIs and loc | `common/scripted_guis/<id>_<slug>_scripted_guis.txt`, `common/scripted_localisation/<id>_<slug>_scripted_localisation.txt` | 033, 008 |
| Localisation | `localisation/english/<id>_<slug>_l_english.yml` | 097 already exists |
| Docs | `docs/events/<id>_<slug>/overview.md` plus a row in `docs/events/README.md` | `docs/events/008_tensions_rising/overview.md` |
| Specs and plans | `docs/specs/<id>_<slug>_specs/`, `docs/plans/<id>_<slug>_plans/subagent_handoffs/` | both were empty at read time for 097 |

- There is no `common/script_constants/052_*`. The repo has 052 only as a stub event file and loc.
- Constant group patterns: `<slug>_event_log = { schema... event_id evolution_type stage_N }` (008) or `<slug>_event = { id evolution_type evolution_N_tier evolution_N_stage }` (013). Keep category ids unique across files.
- Each new script file starts with a banner overview in the style of `chaosx_logic_effects.txt` (AGENTS.md rule 12). Document new reusable dynamic effects in `common/scripted_effects/chaosx_dynamic_effects.md`. The upload copy of that md lists three helpers (`chaosx_convert_days_to_date_offset`, `chaosx_convert_date_offset_to_days`, `cbrn_debit_motorized_stockpile_oldest_first`) that do not exist in repo `common/`.
- `docs/events/README.md` lists documented events only. 097 needs its own row.
- News events share `events/_chaosx_news.txt` and ids `chaosx.news.N`. Existing ids run in several blocks, with the ordinary block ending at 315 and further blocks at 4401 to 4406, 5002 to 5004, and 7007. Event 097 has no news id today and any new one must be checked against these blocks.

### 15. Spain and Portugal

- `Tordesillas` does not appear in any tracked text file. `git grep -i tordesillas` and `grep -rIi` over the tree return nothing, and neither does the upload folder. The `.xlsx` files are Git LFS pointers (130 bytes), so workbook contents could not be searched, but the CSV exports have no match. The catalog has no row for it. Catalog ids run 1 to 166 with 163 absent (blank), so id 163 or any id above 166 is unreserved. IDs 167+ would also need new registry rows, loc, and selector rows.
- Event 093 Portugal wants land (`events/093_portugal_galicia.txt`): fire-once, Chaos level 1, no cluster, To Be Reworked. Root fires `chaosx.nr93.2` in POR. Option A adds a core of state 171 to POR and fires `chaosx.nr93.3` in every country owning 171. That owner either defies, which makes POR declare a `take_core_state` war on the owner, or hands state 171 to POR with `transfer_state_to` and news 74. Separately, `common/on_actions/091_the_great_revolution_on_actions.txt:36-40` fires `chaosx.nr93.1` in every other country from `on_monthly_REV` when REV exists and `all_country` is communist. That fires Event 093's Portugal root once per country and looks like a stale cross-wire, so it is a risk for any monthly 093 reading. The 093 loc has empty descriptions for `.2.d` and `.3.d`.
- Event 006 Iberian package: `common/scripted_effects/006_independence_wave_iberian_package_effects.txt` (650 lines) covers IW-013 Basque (NAV) and IW-015 Galicia (GLC) with ledgers, paid projects, focus framework, host settlement, and cleanup. State 171 and Galicia are shared surfaces between 093 and 006.
- `docs/spreadsheets/chaos_redux_events_catalog.csv` has no Spain or Portugal colonial event. Event 22 (Spain Antisemitism) is the only other Spain row.

### 16. Performance precedents

Safest existing patterns, in order:
1. Event 021 scheduler (`event021_parent_global_scheduler_pulse`, `021_random_civil_war_parent_effects.txt:378-440`): entered from the existing `is_global_host` pulse, guarded by a once-per-date check, registers a bounded sample of countries, and reviews a persistent array with `global.random_civil_war_review_cursor` and a maximum scan count. Each country carries its own due date. `docs/events/021_random_civil_war/overview.md:45-50` states it avoids an unrestricted world scan.
2. Event 035 registry: `great_depression_process_active_registry` (`035_great_depression_effects.txt:4282`) iterates `global.great_depression_active_countries` from the same host pulse and runs a per-country weekly pulse that also handles evolution due days.
3. Event 008 capped recipients: `apply_tensions_rising_distributed_world_tension` uses `random_select_amount` with file constants for the recipient cap, and `select_tensions_rising_relation_pairs` (`:491`) selects only a small random number of pairs per firing with `random_country` plus a recent-actor flag.
4. Event 013 delayed jobs: hidden `chaosx.nr13.2` processes one due job with a global reservation ledger so no two jobs in a sequence share a due date (`docs/events/013_natural_disasters/overview.md:14-19`).
5. Fallout one-time pair sweep: `fallout_take_world_snapshot` and `fallout_reset_old_world_diplomacy` do full ordered-pair sweeps with scope iterators, guarded by transition flags and retry receipts. This is the only repo precedent for a full N-squared collaboration sweep and it runs once per campaign.
- The host pulse that the first two precedents use is `on_daily` in `chaosx_on_actions_chaos_meter.txt:10-102`, which calls `fallout_reconcile_coordinator`, the Great Depression processors, `humanitarian_process_registered_runtime`, `event021_parent_global_scheduler_pulse`, and `black_friday_daily_pulse` once per day from the global host country. Adding any call to it is a new periodic world step and needs the user's permission under AGENTS.md rule 8.
- `for_loop_effect` and `while_loop_effect` stop at 1,000 iterations (upload AGENTS.md rule 15). Use scope iterators for country pairs.

### 17. Global decision categories

- `air_cleanliness_treaty_category` (`fallout_consolidated_categories.txt:12`): `visible` requires `air_cleanliness_treaty_country_is_live_member = yes` and `NOT` of `fallout_transition_active`, `fallout_active`, and `fallout_air_cleanliness_disabled`. It sets `icon`, `picture`, and `priority = 101`.
- `condemnation_target_response_category` and `condemnation_participant_action_category` (`condemnation_sanctions_categories.txt`): `visible_when_empty = no`, role-based `visible` using `condemnation_has_public_record`, `condemnation_has_active_sanctions`, or `any_country = { exists = yes condemnation_is_formally_censured = yes }`.
- `famine_decision_category` and `migration_decision_category`: `visible` begins with `hidden_trigger = { NOT = { is_special_chaos_country = yes } uses_normal_civilian_systems = yes }`, then a problem-active trigger, with `visible_when_empty = no`, a header `scripted_gui`, and a priority constant.
- All four hide themselves unless the country has an active role in the system, which is the gating idiom a mod-wide category should follow. Decisions still need the usual cost and tooltip rules in `chaos-redux-decisions-missions`.

### 18. AI strategy

- Event-owned strategy files exist for 003, 005, 006, 010, 011, 012, 014, 015, 016, 018, 019, 020, 021, plus `ZZZ.txt`, `anti_zombie_league.txt`, and the CBRN and genocide files. Types used across them: `equipment_production_factor`, `build_building`, `build_army`, `avoid_starting_wars`, `research_weight_factor`, `role_ratio`, `front_*`, `garrison`, `garrison_reinforcement_priority`, `conquer`, `contain`, `invade`, `antagonize`, `send_volunteers_desire`, `diplo_action_desire`, `diplo_action_acceptance`, `intelligence_agency_usable_factories`, `force_defend_ally_borders`, `rush`, `careful`.
- Related to occupation: `garrison` in `019_infantry_spawn_derivative_ai_strategy.txt`, `018_resources_found_ai_strategy.txt:246-251` (with `garrison_reinforcement_priority`), and `ZZZ.txt`. `invade` in `anti_zombie_league.txt`. `conquer` and `contain` in `005_soviet_collapse.txt` and `018_resources_found_ai_strategy.txt:452-461`.
- No strategy in the repo targets capitulation pursuit, occupation law choice, or collaboration. Occupation law AI is inside the law definitions (`cbrn_occupation_law_ai`).
- Any 097 AI weight, MTTH, `ai_chance`, or strategy factor needs the baseline, patch, and `hoi4.probability_compare` pass through `chaosx_ai_probability_auditor`.

## Vanilla or reference precedents

Vanilla files: unavailable. `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/` is not present in this Linux container, so no vanilla event, autonomous state, ideology, occupation law, operation, defines, or documentation markdown file (`effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`) was read. Kaiserreich and the other approved reference mods are not present either.

Offline wiki snapshot sections found (`paradox_wiki/`):
- `Effects - Hearts of Iron 4 Wiki.md`: `add_collaboration` `:1246`, `set_collaboration` `:1247`, examples `:1320-1335`, `instantiate_collaboration_government` `:4723`.
- `Triggers - Hearts of Iron 4 Wiki.md`: `has_collaboration` `:642` (target must be occupied by the scope, value uses `<` or `>`), `is_dynamic_country` `:652`.
- `Data structures - Hearts of Iron 4 Wiki.md`: country variables `core_compliance`, `core_resistance`, `has_collaboration` `:1510-1512`, temp-variable lifetime `:440`.
- `On actions - Hearts of Iron 4 Wiki.md`: `on_capitulation` `:254`, `on_annex` `:257`, `on_puppet` `:260` (peace conference only), `on_release_as_puppet` `:263`, `on_subject_*` `:434-436`, `on_government_exiled` `:442`, `on_state_control_changed` `:450`.
- `Defines - Hearts of Iron 4 Wiki.md`: three collaboration defines `:480-482`.
- `Ideology modding`, `Autonomy state modding`, `Idea modding`, `Faction modding`: rule `can_create_collaboration_government`, ideology key `can_collaborate`.
- `List of modifiers`: `operation_collaboration_government_cost`, `_outcome`, `_risk` `:50`.
- `Localisation` `:258` and `Ideology modding :120`: collaboration government names use `$NONIDEOLOGY$`, `COUNTRY_autonomy_collaboration_government`.
- `Intelligence agency modding` page exists for operation questions.

Approved in-repo precedents to mirror instead: Event 008 (stage resolver, evolution logging, bounded pairs), Event 035 (MTTH due day plus registry), Event 021 (bounded scheduler), Event 013 (job events), Fallout (collaboration snapshot and reset).

## Likely edit order for a future implementation agent

1. Parent writes the spec in `docs/specs/097_collaboration_specs/` and records acceptance. Resolve the open decisions listed below before code.
2. Constants: `common/script_constants/097_collaboration_constants.txt` with event id, evolution type 97, stage and tier ids 1 to 4, tuning, timing, and Chaos amounts. Add `chaos_meter_history_reason.special` entries from 222.
3. Triggers: valid country, availability, gates for `world_end`, `fallout_transition_active`, and `fallout_active`, plus public read-only facts for Event 052.
4. Effects: opening transaction, deepening, evolution scheduling and recording, cleanup, and Fallout stand-down. Use scope iterators for pairs.
5. Registration: switch the array entry to a constant, add the reworked allowlist entry, add the N/A reason chain only if the event has a real availability condition, and add a prefire helper only if context must exist before history is recorded.
6. Rewrite `events/097_collaboration.txt` and localisation. Hidden root first, then reports and any news.
7. Event log: Event Details description row and key, evolution preview rows in `events_log_rebuild_open_event_details_view`, the eight evolution selectors, type label key, stage keys.
8. Cluster: create the Intelligence cluster in runtime (id and member rows, cooldown flags, name and description selectors and keys), then catalog CSV through the workbook worker.
9. Ideas, opinion modifiers, dynamic modifiers, MTTH, decisions and categories, AI strategy, achievements, and super-event or news only if the spec maps them.
10. Docs: `docs/events/097_collaboration/overview.md`, README row, dynamic effects md if new helpers, handoffs, spreadsheet export.
11. Audits through the routed subagents. Probability audit, localisation audit, event completion audit.

## Validation checks

- Source checks that could fail: unique ids for chaos reasons (222+), unavailability reasons (44+), cluster id (not 8 or 12), cluster row ids, `evolution_type 97`, achievement ids, and no reuse of super-event slot 97.
- Every evolution stage appears in all eight selectors, the preview rows, the type label, and the enable and disable flags. Disabled evolutions leave the baseline layer playable.
- Pair processing contains no `for_loop_effect` or `while_loop_effect` over pairs and no new periodic all-country on_action.
- A Fallout-style check that no pair holds collaboration when `fallout_transition_active` is set, and that 097 does not re-apply during or after the transition.
- Probability evidence for weights, MTTH, and any `ai_chance` through `chaosx_ai_probability_auditor` with the same named scenarios before and after.
- Engine semantics to be confirmed by the user in a live new save: where `add_collaboration` works without occupation, whether ideology rules gate it, and what the player sees.

## Risks and blockers

### Confirmed blockers

- The `hoi4_agent_tools` MCP server failed to connect (error: executable `cmd.exe` not found, the container is Linux). No `hoi4.event_inspect`, `hoi4.probability_inspect`, `hoi4.reference_*`, `hoi4.source_lookup`, or render result was produced. Everything above is source review only and does not replace the required MCP evidence for event chains and weighted logic.
- Vanilla game files and installed documentation are not present. Native collaboration semantics, ideology rule behavior, tag pools, and vanilla precedents for collaboration governments could not be checked beyond the wiki snapshot.
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx` and `doctrines.xlsx` are Git LFS pointer files (130 bytes). The workbook cannot be opened here. The CSV exports are readable snapshots only and must not be edited.
- No accepted 097 design existed in `docs/specs/097_collaboration_specs/` when this exploration read it. Spec files written there during the run were not read, so nothing in this handoff checks them against source.

### Ordinary risks

- Cluster numbering is inconsistent across surfaces: catalog and `event_clusters.md` say Intelligence is 8, the 052 spec says 10, runtime id 8 is Diseases, and the documented v2 renumbering is not in source. Adding 097 to the cluster means building the whole Intelligence cluster, and 39 and 52 are not registered either.
- Event 039 is registered as repeatable at runtime but treated as Fire-Once by its spec and header. Resolve before it joins the same cluster.
- A Medium cluster member needs 200+ Chaos for cluster participation.
- Natural repeated firings decay quickly because the cap halves per firing. A design that deepens per firing must state its expected count or decouple depth from firings.
- The Fallout proof fails on any leftover collaboration pair, so 097 needs an explicit stand-down and clean-up route.
- Event 052's spec expects a stable 097 public contract and forbids 052 from owning collaboration logic. Design the read-only facts and bounded requests early.
- The stub's picture sprite `GFX_report_event_molotov_ribentrop_handshake` has no repo definition and its spelling looks like a typo, so it may be one source of the errors the TODO mentions. This is a hypothesis. Another plausible cause is the `add_collaboration` call over every ordered pair when no occupation exists. Neither was confirmed.
- The wiki says `on_puppet` fires only in peace conferences. Whether a scripted collaboration government triggers any Chaos hook is unconfirmed. `chaos_meter_on_puppet` also assumes FROM is the puppet while the wiki says ROOT is.
- Uploaded newer docs (`chaosx_dynamic_effects.md`) describe helpers absent from repo source. Do not rely on them without checking.
- No decision exists on whether 097 respects `can_collaborate` and `can_create_collaboration_government`, which only communism and fascism allow.
- Event 095 has no spec and a thinner implementation than its catalog text. Any 097 to 095 link has nothing stable to attach to yet.

### Open decisions for the parent or user

- Whether the Intelligence cluster is built now with all three members or whether 097 stays standalone for the first pass.
- Whether adding a 097 call to the global host pulse is permitted, or whether all 097 timing must come from existing event or country-scope hooks.
- How many natural firings the design assumes and how depth is stored.
- Which id the future Tordesillas event takes (163 or 167+).

## Recommended next action

The parent should write the 097 specification first and settle the open decisions above, then route cluster creation, evolution wiring, and the Chaos reasons as one registration tranche before touching gameplay effects. Use Event 008 for the evolution and chaos pattern, Event 035 or 021 for MTTH and bounded scheduling, and the Fallout code as the contract for collaboration clean-up. Ask the user to verify native `add_collaboration` behavior in a live new save before the spec depends on it.
