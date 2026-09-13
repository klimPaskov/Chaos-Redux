# Repo Explorer Handoff

> Historical implementation map only. Its primary findings describe the preimplementation legacy package and are superseded by the current source and `../final_audit.md`. The file is retained as an audit trail, not as a current runtime claim.

## Scope read

- Parent task: Read-only implementation map for Event 028, Asteroid Incoming, including event registration and pacing, target and adjacency logic, exact population and Deaths accounting, Air Cleanliness, Event 013 adapters, crater and wasteland state effects, armour, decisions and missions, on-actions, achievements, super-event and sound wiring, assets and GFX, localisation, and the event catalog.
- Explicit constraints: No gameplay, localisation, asset, GFX, GUI, audio, or workbook edits were made. The only write from this exploration is this handoff. The worktree was already dirty and changed during exploration; all files outside this handoff were left untouched, and Hearts of Iron IV was not launched.
- Files or ids requested: The accepted package uses numeric event id `28`, root `chaosx.nr28.1`, three country-state target pairs plus a miss, a two-day target lock, Global Fragmentation at 600 Chaos, Extraordinary Minerals at 800 Chaos, and the working recovery ids listed in the Event 028 decision specification.
- Skills or docs read: All 23 files under `docs/specs/028_asteroid_incoming_specs/`; `AGENTS.md`; `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-state-ledgers`, `chaos-redux-super-events`, `chaos-redux-event-assets`, `chaos-redux-mtth`, `chaos-redux-subagents`, `chaos-redux-improvement-loop`, and `xlsx` skills; the required offline wiki core pages plus map, state, building, graphical asset, sound, interface, scripted GUI, and achievement pages; and the relevant installed vanilla documentation including `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `dynamic_variables_documentation.md`, `script_concept_documentation.md`, `script_math_functions.md`, `loc_formatter_documentation.md`, `loc_objects_documentation.md`, and `common/script_constants/documentation.md`.
- MCP evidence boundary: The installed package and repository configurations were inspected, but no callable `mcp__hoi4_agent_tools__*` namespace was exposed in this runtime. No engine artifact URI, scenario hash, render, comparison, probability result, or map result was produced. Source review below is not an engine-equivalent substitute.

## Primary findings

1. The accepted Event 028 design is a global major fire-once event, but the live event source is still the old minor prediction event. `common/scripted_effects/chaosx_logic_effects.txt:274-326` places id `28` in `global.repeatable_events`, while the major and fire-once arrays do not contain it.

2. The current event is legacy and unsafe to reuse unchanged. `events/028_asteroid_impact.txt:22-247` uses duplicated country-only prediction options, an unlocked `random_owned_state`, direct `launch_nuke` calls, `add_manpower = -100000`, stale flags, and `brilliant_scientist_record_asteroid_impact`; it does not implement the accepted target-state transaction, rings, dust, craters, fragments, recovery decisions, or modern event details.

3. Partial Event 028 scaffolding does exist. `common/script_constants/028_asteroid_incoming_constants.txt` defines runtime, target, profile, population-loss, building-loss, dust, and mineral tuning groups. `common/scripted_triggers/028_asteroid_incoming_triggers.txt` defines target validity, lock validity, fragment-site validity, decision-pointer validity, registry alignment, and transaction-state predicates. `common/scripted_effects/028_asteroid_incoming_effects.txt` currently reaches through transaction initialization, target locking, profile deduplication, and bounded main/fragment breadth-first planning, but stops before physical receipts, crater modifiers, dust, Air Cleanliness, minerals, reports, and terminal cleanup. All three 028 scaffolding files were untracked in the final worktree status and were not created or edited by this exploration.

4. Shared exact-population and Deaths infrastructure is reusable, but Event 028 must add its reason mapping and call contract. `chaosx_dynamic_effects.txt:596` owns `apply_exact_state_civilian_population_loss`, and `chaos_meter_effects.txt:2853` owns `chaos_meter_register_deaths`. The accepted event must use one measured state debit per affected state, the seven asteroid-specific reason profiles, and no direct negative manpower or nuclear effect.

5. Air Cleanliness already has a monthly coordinator and a natural-disaster source adapter, but no asteroid source adapter exists. Event 028 should feed a purpose-specific bounded reservoir into the existing coordinator rather than masquerading as an Event 013 wildfire or ash family.

6. The event-log framework already has generic Event 028 name/detail branches, but the event-specific payload, current title, evolution entries, detail snapshots, and localisation are absent or stale. `chaosx.event_name.28` still says `Asteroid Impact` instead of the accepted `Asteroid Incoming`.

7. Recovery decision art and event/super-event art exist as evidence and runtime DDS candidates, but consumer definitions are missing. The super-event numeric slot `28` is already occupied by Holy Realm audio wrappers, so Event 028 must use a different unique slot and add its own base sound, wrapper, music row, localisation cases, and sprite definition.

8. The authoritative workbook still has the old Event 028 row, and the export CSV repeats that stale row. The workbook, not the CSV, is the source of truth; the parent must update the workbook and run the exporter in the same implementation pass.

## Relevant files

| Path | Why it matters | Evidence |
| --- | --- | --- |
| `docs/specs/028_asteroid_incoming_specs/` | Complete accepted design package. | 23 files cover core rules, targeting, impact, dust, evolutions, decisions, AI, logs/text, assets/audio, achievements, tuning, and catalog reconciliation. |
| `events/028_asteroid_impact.txt` | Current Event 028 gameplay source. | `chaosx.nr28.1` at `:23`; hidden `chaosx.nr28.2` at `:111`; duplicated option layouts at `:55-107`; `launch_nuke` at `:131-135` and `:183-187`; legacy result helper at `:171` and `:247`. |
| `common/script_constants/028_asteroid_incoming_constants.txt` | Partial Event 028 tuning contract. | Defines `asteroid_incoming_runtime`, `asteroid_incoming_target`, `asteroid_incoming_profile`, `asteroid_incoming_population_loss`, `asteroid_incoming_building_loss`, `asteroid_incoming_dust`, and `asteroid_incoming_mineral`; dust includes the 0-100 thresholds and accepted armour factors. |
| `common/scripted_triggers/028_asteroid_incoming_triggers.txt` | Partial target, lock, ring, decision, and registry predicates. | Key ids include `asteroid_incoming_state_is_valid_target`, `asteroid_incoming_country_is_valid_target`, `asteroid_incoming_target_pair_is_valid`, `asteroid_incoming_locked_transaction_is_valid`, `asteroid_incoming_state_is_valid_fragment_site`, `asteroid_incoming_decision_target_pointer_is_valid`, and `asteroid_incoming_registry_arrays_are_aligned`. |
| `common/scripted_effects/028_asteroid_incoming_effects.txt` | Partial transaction and adjacency implementation. | `asteroid_incoming_initialize_transaction`, `asteroid_incoming_lock_candidate_pair`, `asteroid_incoming_fail_closed_transaction`, `asteroid_incoming_mark_transaction_resolved`, `asteroid_incoming_record_footprint_profile`, `asteroid_incoming_plan_main_footprint`, `asteroid_incoming_plan_fragment_footprint`, and `asteroid_incoming_plan_next_land_ring` are present; the file ends at 409 lines before impact receipts or dust application. It was untracked in the final worktree status and was not created or edited by this exploration. |
| `common/scripted_effects/chaosx_logic_effects.txt` | Shared event registration, pools, pacing, and type mapping. | `initialize_event_categories` is `:223-326`; id `28` is in `global.repeatable_events` at `:285`; fire-once, major, and rework behavior is handled around `:1086-1190`; `get_event_type` is `:1390-1431`. |
| `common/scripted_triggers/chaosx_settings_triggers.txt` | Default rework enablement and evolution gates. | `event_log_event_is_reworked_default_enabled` is `:10-33` and lacks Event 028; `is_current_evolution_enabled` and tier gates are `:48-102`. The existing baseline handoff reports that the missing allowlist entry places Event 028 in the default disabled queue. |
| `common/scripted_effects/chaosx_settings_effects.txt` | Global event-pool traversal and weighted selection. | The active-candidate, scaled-weight, random-roll, and cumulative-selection path is around `:4329-4442`; it must be rechecked after Event 028 changes from repeatable to major/fire-once. |
| `common/on_actions/chaosx_on_actions_system.txt` | Shared event scheduler and startup/daily hooks. | The shared scheduler and daily hooks are at `:1-166`; no Event 028-specific on-action exists. Avoid adding an unrestricted daily or monthly world scan. |
| `common/scripted_effects/chaosx_dynamic_effects.txt` | Exact state population mutation. | `apply_state_population_loss_without_recruitable_manpower_gain` starts at `:507`; `apply_exact_state_civilian_population_loss` starts at `:596` and consumes the requested loss, minimum floor, reason, logging, target-country, and contract inputs. |
| `common/scripted_effects/chaos_meter_effects.txt` | Deaths registration and Air Cleanliness monthly processing. | `chaos_meter_register_deaths` is at `:2853`; `air_contamination_register_source_activity` is at `:4691`; `air_contamination_monthly_update` is at `:5453`, with natural-source consumption around `:5635-5646`. |
| `common/script_constants/chaos_meter_constants.txt` | Current Deaths reason and Air source classifications. | Death reason constants are around `:381-413`; asteroid-specific main/ring/fragment/rescue reasons are not present. Air source class constants are around `:626-638`. |
| `common/on_actions/chaosx_on_actions_chaos_meter.txt` | Existing monthly Air Cleanliness host. | The monthly host calls `air_contamination_monthly_update` around `:65-75`; Event 028 should register its global dust input once and let this host consume it. |
| `common/scripted_effects/fallout_consolidated_effects.txt` | Existing natural-source adapter pattern. | `air_contamination_register_natural_disaster_source` is `:140-264`; aftermath and monthly preparation follow at `:270-435`. It expects Event 013 family/severity inputs and is not an asteroid adapter by itself. |
| `common/scripted_effects/013_natural_disasters_effects.txt` | Main reference for bounded disasters, state damage, aftermath, event history, evolutions, and Air adapter calls. | Event 013 has target validation, impact profiles, building/population handling, `natural_disaster_record_call_history` at `:1181`, and Air source calls at `:9152`, `:9301`, and `:9484`. Reuse only the supported secondary wildfire, landslide, flood, debris, and ash-like adapter boundary from the Event 028 package. |
| `common/scripted_triggers/013_natural_disasters_triggers.txt` | State-target validation precedent. | `natural_disaster_is_valid_impact_state` at `:12` checks non-impassable state, population, and owner. Event 028 needs stricter owner/controller, nonhuman, crater, and meaningful-settlement predicates already partly scaffolded in its own trigger file. |
| `events/013_natural_disasters.txt` | Event/subevent and report/news wiring precedent. | Root `chaosx.nr13.1` and hidden/report/news branches demonstrate bounded event dispatch, but Event 028 must own its own major history and impact reports. |
| `common/dynamic_modifiers/013_natural_disasters_state_modifiers.txt` | Dynamic state modifier syntax and state marker pattern. | Provides family-specific state effects and icons; no Event 028 crater modifiers are defined. |
| `common/dynamic_modifiers/010_death_state_modifiers.txt` and `common/scripted_effects/010_death_effects.txt` | Existing wasteland/state-category precedent. | Death uses active/recaptured wasteland markers and changes state category around `010_death_effects.txt:943-948`; this is not a safe semantic reuse for the required nonradioactive asteroid crater. |
| `common/dynamic_modifiers/nuclear_state_modifiers.txt` | Nuclear fallout state marker to avoid. | It defines nuclear fallout semantics; Event 028 explicitly forbids nuclear fallout, nuclear Deaths, and nuclear history ownership. |
| `common/ideas/098_new_ore_ideas.txt` and `events/098_new_ore.txt` | Closest Chaos Redux site-bonus and armour precedent. | `special_iron_ore` combines a state dynamic modifier with a country idea and `equipment_bonus` armour; the source comment explicitly says dynamic modifiers cannot carry `equipment_bonus`. `events/098_new_ore.txt` registers the state and owner effects. |
| `common/script_enums.txt` | Equipment bonus enum boundary. | `script_enum_equipment_bonus_type` at `:152` already includes `armor`; Event 028 adds no new equipment type, but any new category would require this enum update. |
| `common/decisions/categories/018_resources_found_categories.txt` | Ordinary category presentation precedent. | Uses `icon`, `picture`, `visible`, `visible_when_empty`, and `priority`; Event 028 should use this ordinary pattern and not introduce a dedicated GUI. |
| `common/decisions/018_resources_found_decisions.txt` | Decision costs, custom triggers/text, completion effects, and AI scoring precedent. | Uses `custom_cost_trigger`, `custom_cost_text`, hidden cost effects, and `ai_will_do` blocks. Event 028 must keep each phase within the accepted visible-action and cost limits. |
| `common/decisions/013_natural_disasters_decisions.txt` | State-targeted decision precedent. | Shows `state_target`, target triggers, map highlighting, state requirements, costs, completion, and AI behavior for aftermath actions. |
| `common/decisions/011_secret_alliance_decisions.txt` | Mission lifecycle precedent. | Mission around `:233-301` uses `selectable_mission`, `days_mission_timeout`, target highlighting, `cancel_effect`, `complete_effect`, `remove_effect`, and timeout handling. |
| `common/scripted_effects/chaosx_events_log_effects.txt` | Shared event history, actor, detail, and evolution registries. | `record_events_log_history_entry` is around `:659+`; `record_events_log_evolution_entry` is around `:958-1090`; shared arrays require aligned payloads and actor flags. |
| `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` | Shared event-name/detail/evolution localisation dispatch. | Existing Event 028 cases occur near `:1372`, `:10301`, and `:12013`, but they point at the old name/detail model and need payload/localisation alignment. |
| `interface/chaosx_events_log_popup.gui` | Shared event-log and event-details UI. | Shared event list/details windows are around `:752`, `:861`, and `:1263`; no Event 028 GUI is needed if payload arrays and localisation are supplied correctly. |
| `localisation/english/chaosx_event_names_l_english.yml` | Event name mapping. | `chaosx.event_name.28` at `:30` is currently `Asteroid Impact`; accepted package name is `Asteroid Incoming`. |
| `events/_chaosx_news.txt` and `localisation/english/028_asteroid_impact_l_english.yml` | Legacy news and event text consumers. | `_chaosx_news.txt:377-417` uses old Event 028 news entries and `GFX_news_asteroid`; the Event 028 localisation file still contains prediction options, research windfall text, and old `.29/.30/.32` news keys. |
| `common/scripted_effects/016_brilliant_scientist_context_effects.txt` | Existing Event 016 adapter called by the legacy event. | `brilliant_scientist_record_asteroid_impact` begins at `:624` and records bounded external pressure once; retain or retire it only by an explicit Event 016/Event 028 integration decision. |
| `common/scripted_effects/016_brilliant_scientist_super_event_effects.txt` | Shared super-event queue and dispatch precedent. | Queueing is around `:15-25`; dispatch, `global.current_super_event_audio_id`, and `play_current_super_event_audio` are around `:69-103`. |
| `common/scripted_guis/chaosx_scripted_gui_super_events.txt` | Shared super-event close/audio/image consumer. | The shared close action clears visible/audio state around `:14-27`; the image property uses `[GetSuperEventImage]` around `:30-33`. |
| `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt` | Shared super-event image/title/quote/remark/description dispatch. | `GetSuperEventImage`, `GetSuperEventTitle`, `GetSuperEventQuote`, `GetSuperEventRemark`, and `GetSuperEventDesc` begin at `:2`, `:405`, `:666`, `:927`, and `:1188`; no Event 028 cases exist. |
| `interface/chaosx_super_events.gfx` | Super-event sprite registry. | No `GFX_super_event_028_asteroid_impact` entry exists. |
| `sound/chaosx_sound.asset` and `music/chaosx_music_track_list.html` | Sound definitions and music documentation. | `chaosx_super_event_28_sound_0_5` through `_3_0` at `sound/chaosx_sound.asset:211-216` belong to Holy Realm audio at `:539`; no Event 028 base sound or music row exists. |
| `interface/chaosx_pictures.gfx` and `interface/chaosx_decision_category_pictures.gfx` | Event report/news and decision category sprite registries. | Old Event 028 sprites are registered at `chaosx_pictures.gfx:124-129` and `:160-161`; the new Event 028 report/news/category names from `docs/assets/028_asteroid_incoming/gfx_handoff.md` are not wired. |
| `common/achievements/chaos_redux_achievements.txt` | Chaos Redux achievement registry. | This is the root-only registry; no Event 028 achievement ids are present. The five accepted achievements still need exact ids, possible/happened blocks, and localisation. |
| `docs/assets/028_asteroid_incoming/manifest.md` and `gfx_handoff.md` | Asset evidence and proposed consumer names. | Report/news/super/category and 29 state/idea/decision candidates have source, processed, DDS, and roundtrip evidence; consumer paths and five achievement ids remain blocked. Proposed names include `GFX_report_event_028_asteroid_tracking`, `GFX_news_event_028_asteroid_close_passage`, `GFX_super_event_028_asteroid_impact`, and `GFX_decision_cat_picture_028_asteroid_recovery`. |
| `gfx/event_pictures/028_asteroid_incoming/`, `gfx/super_events/028_asteroid_incoming/`, `gfx/interface/decisions/028_asteroid_incoming/`, and `sound/028_asteroid_incoming/` | Existing runtime candidate files. | New DDS and audio files are physically present, but no matching GFX/sound/localisation consumers are registered. Legacy DDS remain under `gfx/event_pictures/028_asteroid_impact/`. |
| `docs/plans/028_asteroid_incoming_plans/subagent_handoffs/chaosx_ai_probability_auditor_baseline.md` | Existing weighted-logic baseline artifact. | It records the same unavailable probability/event routes, the repeatable classification, stale hidden entry, missing recovery AI, and required post-patch probability comparison. |
| `events/070_africa_gods.txt` | Cross-system stale callers. | Direct `chaosx.nr28.2` calls are at `:284`, `:311`, and `:341`; they bypass the accepted target transaction and must be guarded or rerouted. |
| `docs/plans/famine_and_migration_system_plans/subagent_handoffs/owner_callback_census.md` and `event_boundary_adapter_final_audit.md` | Stale legacy ownership documentation. | These documents treat Event 028's `launch_nuke` path and `on_nuke_drop` callback as authoritative; they must be reconciled when the event stops using nuclear semantics. |
| `docs/spreadsheets/chaos_redux_events_catalog.xlsx` | Authoritative catalog source. | Excel row 29 has id `28`, name `Asteroid incoming`, old prediction text, type `Minor Repeatable`, Chaos level `1`, and status `To Be Reworked`; evolution columns are blank. |
| `docs/spreadsheets/chaos_redux_events_catalog.csv` | Export-only stale catalog. | Line `115` repeats the old minor-repeatable prediction row; do not edit it directly. |
| `docs/events/028_asteroid_incoming/overview.md` | Required event overview surface. | No Event 028 overview file was found; the event skill requires a docs overview before completion. |

## Existing patterns

- Registration and pacing: Add Event 028 to the existing major/fire-once classification and use the shared fired handlers. The accepted package says the event remains default-disabled while it is `To Be Reworked`; the rework allowlist, event type mapping, active pool, and fired-state arrays must agree.

- Target persistence and adjacency: The partial Event 028 helpers already establish useful names for `global.asteroid_incoming_footprint_states`, `_profiles`, `_rings`, planner frontiers, seen states, and the candidate/locked event targets. Their `every_neighbor_state` plus seen-array approach is the closest local breadth-first pattern, but engine adjacency and duplicate behavior remain unverified because `hoi4.map_inspect` was unavailable.

- Physical population and Deaths: Use `apply_exact_state_civilian_population_loss` once per affected state with measured debit and `chaos_meter_register_deaths` enabled for the accepted asteroid reasons. The current Deaths constants have no asteroid reason ids, so an owner-defined reason mapping and localisation/detail mapping are required.

- Impact profile and crater state: Use the Event 013 state-profile/building-damage structure and the 098 state-site marker pattern, but create Event 028-specific dynamic modifiers and state flags. Do not reuse nuclear fallout or Death's wasteland semantics. Preserve owner/control explicitly and make the main crater nonradioactive and non-reconstructible according to the accepted contract.

- Air Cleanliness and Event 013: Reuse the monthly Air coordinator and the duplicate-guard/reservoir pattern in `fallout_consolidated_effects.txt`. Add a bounded asteroid source adapter for dust and call Event 013 only for the specifically accepted secondary disaster families; Event 028 must retain ownership of the main impact, history, reports, and aggregate aftermath.

- Armour: `common/ideas/098_new_ore_ideas.txt` proves the country-idea plus state-site pattern and also documents that `equipment_bonus` cannot be placed in a dynamic modifier. The Event 028 mineral constants are only tuning inputs at present; the owner must settle a fixed/idempotent country-idea or another engine-supported application for +100% main-crater and +20% per fragment existing land-division armour, with refresh on controller/owner/annex/civil-war/peace/release/cease changes.

- Decisions and missions: Use an ordinary category like `018_resources_found_categories.txt`, state-targeted action structure like Event 013, and mission lifecycle like `011_secret_alliance_decisions.txt`. The accepted package has four phases, 14 working action ids, and five working mission labels, but no final Event 028 decision file, category, AI scores, or exact mission ids.

- Event logs and evolutions: Use shared history/detail/evolution arrays and the existing actor/name dispatch. Set the shared evolution variables `events_log_evolution_event_id`, `_type`, `_stage`, `_tier`, `_actor`, and `_has_actor`, gate with `is_current_evolution_enabled = yes`, and record the major row once. Global Fragmentation and Extraordinary Minerals must be logged as the two accepted evolution entries; no visible fragment locations are required.

- Super-event and audio: Queue the impact presentation through the shared super-event dispatcher, set `global.current_super_event_audio_id`, and call `play_current_super_event_audio = yes`. Use a unique Event 028 slot because numeric slot 28 is occupied. The miss uses close-passage news and must not queue the impact super-event.

- Assets: The event asset package supplies source, processed, DDS-candidate, and roundtrip evidence for five report/news/super/category families plus state, idea, decision, and mission icons. It intentionally leaves consumer sprite names and achievement triplets to the parent, so the parent must wire them and then update the manifest/handoff status.

- Catalog and docs: Treat `chaos_redux_events_catalog.xlsx` as authoritative, update Event 028 and its two evolution fields after the implementation facts are fixed, then run `.tools/export_event_catalog_csv.py`. Keep the new event overview, event spec, asset handoff, super-event research, and stale legacy adapter documents consistent.

## Vanilla or reference precedents

| Path | Relevant construct | Why it applies |
| --- | --- | --- |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:3997-4015` | `every_neighbor_state` | Documents one-hop state adjacency and `limit`/`random_select_amount`; useful for the bounded planner, but not proof of Event 028's multi-ring runtime behavior. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:6496-6503` | `save_event_target_as` | Supports short-lived scope pointers; the offline wiki and repository guidance distinguish it from persistent global event targets that require cleanup. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:7681-7689` | `set_state_category` | Documents state-category mutation; Event 028 needs a dedicated crater policy rather than blindly converting to generic wasteland. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md` | `damage_building`, `remove_building`, `set_building_level`, `set_capital`, `add_dynamic_modifier`, `set_state_flag`, `set_variable`, and event/news effects | Provides the supported effect signatures the parent must mirror for the impact, relocation, state marker, modifier, and presentation layers. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/AFG.txt:144-154` | Mission category and `days_mission_timeout` | Shows an ordinary decision category with a timed mission and an activation trigger. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/SOV.txt:2129-2144` | Add/remove state dynamic modifier on a state and `every_neighbor_state` | Useful syntax for applying and cleaning a bounded state modifier set; Event 028 still needs its own marker and ownership rules. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/events/AAT_NewsEvents.txt:11-24` | Major `news_event`, triggered-only, title/desc/picture/options | Direct precedent for the close-passage miss news surface. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/dynamic_modifiers/aat_dynamic_modifiers.txt:1-45` | Dynamic modifier schema, icon, enable/remove trigger, and variable-backed modifier values | Confirms the shape of a dedicated state/country dynamic modifier definition. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/achievements.txt:1-45` | Root achievement `possible` and `happened` blocks | Vanilla precedent for achievement conditions; Chaos Redux additionally requires its own root registry and custom tooltips. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/raids/nuclear_raids.txt` | Variable-backed `launch_nuke` target syntax | Useful only to understand the legacy adapter boundary. It is not an approved implementation precedent for Event 028 because the accepted design forbids nuclear ownership and fallout semantics. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/map/definition.csv`, `map/adjacencies.csv`, `map/supply_nodes.txt`, and `map/railways.txt` | Installed province, adjacency, supply, and railway data | These are the static map sources relevant to validating land rings, logistics destruction, and supply/rail recovery; MCP map inspection is still required for engine-level evidence. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/modifiers_documentation.md:1752-1778` | `armor_factor` and `army_armor_attack_factor`/`army_armor_defence_factor`/`army_armor_speed_factor` | Documents armour modifier names. It does not prove that a dynamic modifier can supply the accepted equipment-bonus armour behavior; the Chaos Redux 098 precedent warns against that assumption. |

## Likely edit order for the parent

1. Reconcile the accepted spec with the legacy source and choose final identifiers for decisions, missions, achievements, evolution types, event-detail fields, and a unique super-event audio slot. Preserve the old files for audit until every reference is mapped.

2. Repair shared Event 028 registration: move id `28` out of the repeatable array, classify it as major/fire-once, align the default rework gate and event weight, and ensure the shared fired/history handlers receive the accepted root.

3. Complete the bounded target builder around the existing constants/triggers/effects. Build exactly three valid country-state pairs and a miss, enforce chooser exclusion, nonhuman/empty/wasteland/crater exclusion, meaningful settlement, country/state diversity, and protected relation rules, then persist the selected pair and two-day lock. Fail closed if fewer than three pairs or if the locked state becomes invalid.

4. Replace the legacy option and hidden `.2` flow with the accepted root/subevent contract. Audit or reroute `events/070_africa_gods.txt` direct hidden calls so no caller can bypass the transaction or invoke a missing scope context.

5. Implement main and fragment footprint resolution using the existing aligned arrays and shortest land-adjacency rings. Apply strongest-overlap profile selection, capital relocation before destruction, exact buildings/infrastructure/rail/supply/strategic destruction, owner/control preservation, crater state flags/categories, and one exact population/Deaths transaction per state.

6. Add the dust ledger and Air Cleanliness adapter. Keep `Atmospheric Dust Load` bounded at 0-100, apply the opening hold/decay/mitigation/protection rules from the spec, register Air Cleanliness once through the monthly coordinator, and ensure miss outcomes do not create dust.

7. Add the bounded Event 013 secondary-disaster adapter and preserve Event 013 history ownership boundaries. Decide explicitly whether the existing Event 016 brilliant-scientist receipt remains a one-time terminal impact side effect.

8. Define Event 028 state and country dynamic modifiers, ideas, and decision category/actions/missions. Keep the category ordinary, state-targeted, cost-limited, and AI-scored; do not create a dedicated GUI.

9. Implement and gate Global Fragmentation and Extraordinary Minerals. Before wiring armour, resolve the dynamic-modifier versus equipment-bonus limitation and implement idempotent site registration plus controller/owner/peace-state refresh and cleanup.

10. Wire the major event log row, event-detail payload arrays, current/after snapshots, evolution preview/history, report/news text, and all player-facing localisation. Update the shared Event 028 name from `Asteroid Impact` to `Asteroid Incoming` and remove prediction/research-windfall wording.

11. Wire report/news/category/super-event sprites, sound base/wrappers/music row, and the shared super-event localisation cases. Promote only the validated asset candidates; add achievement IDs and their 15 required triplet files after the parent locks the registry names.

12. Add `docs/events/028_asteroid_incoming/overview.md`, reconcile the Event 016/famine-migration legacy documents, update the authoritative workbook row and evolution fields, export the CSVs with the repository tool, and run the static and MCP validation below before parent-owned live verification.

## Validation checks

- Registration: Search `common/scripted_effects/chaosx_logic_effects.txt` and `common/scripted_triggers/chaosx_settings_triggers.txt` to prove id `28` appears in the accepted major/fire-once/rework locations, not `global.repeatable_events`, and that the active-pool/type/history paths agree.

- Event roots and stale callers: Search for `chaosx.nr28`, `launch_nuke`, `add_manpower = -100000`, `brilliant_scientist_record_asteroid_impact`, `asteroid_location_options_`, and `random_owned_state`. Confirm every surviving caller either belongs to the accepted transaction or has an explicit compatibility mapping.

- Target and ring contract: Verify all candidate and locked event targets have definitions and cleanup, three distinct pairs plus miss are constructible, invalid targets fail closed, aligned arrays have equal lengths, main/fragment overlaps keep the strongest profile, and no maritime adjacency is admitted.

- Population and Deaths: Trace every affected state through `apply_exact_state_civilian_population_loss`, verify the requested amount, actual debit, floor, target country, reason, and one Deaths receipt, and confirm no direct negative manpower or nuclear callback duplicates the transaction.

- Dust and Air: Check initial dust, cap, stage thresholds, opening hold, monthly decay, mitigation cap, protection reduction, secondary-event increments, duplicate guards, and exactly one monthly Air Cleanliness reservoir consumption path.

- State and armour: Confirm crater/impact/fragment state flags and modifiers are unique and nonradioactive, owner/control are preserved as designed, buildings and logistics use supported effects, and mineral armour refresh removes or replaces stale site contributions rather than stacking duplicates.

- Decisions and missions: Check category visibility, phase gates, state-target validity, max visible actions, cost-type limits, mission timeout/cancel/complete/remove paths, dynamic tooltips, and nonzero meaningful `ai_will_do` scoring for the named recovery scenarios.

- Logs and localisation: Check major row cardinality, actor flags, payload-array alignment, event-detail current/after data, evolution arrays, all option/effect/trigger tooltips, UTF-8 BOM localisation files, and no old prediction or nuclear wording remains in active Event 028 text.

- Assets and audio: Verify every proposed GFX name resolves to an existing validated DDS at the intended consumer dimensions, every state/idea/decision icon has its definition, the five achievement triplets match final ids, the super-event sprite and sound use a unique slot, and the music/documentation row matches the actual runtime file.

- Catalog/docs: Confirm workbook row 29 says `Asteroid Incoming`, `Major`, `Calm World`, no cluster/scenario, repeatable no, fire-once yes, and the two evolution fields match the final event-detail wording. Run `python .tools/export_event_catalog_csv.py` only after the workbook update and review all three exports.

- Required MCP follow-up when the production namespace is available: start weighted review with `hoi4.probability_inspect`, route the detailed pass through `chaosx_ai_probability_auditor`, then use the same named AST_AI_01 through AST_AI_10 and recovery scenarios for evaluate/sweep/simulate/sequence/render and post-patch `hoi4.probability_compare`. Use `hoi4.event_inspect`, `hoi4.event_render`, and `hoi4.event_compare` for the event flow, and `hoi4.map_inspect` plus `hoi4.map_render` for state adjacency, supply, railway, and crater evidence. The installed package does not register `hoi4.map_compare`, despite repository guidance mentioning map compare, so record that route mismatch if it remains unavailable.

## Risks and blockers

### Confirmed blockers

- Production HOI4 MCP routes are not callable in this session. The installed/configured route names are `hoi4.event_inspect`, `hoi4.event_render`, `hoi4.event_compare`, `hoi4.map_inspect`, `hoi4.map_render`, `hoi4.map_rewrite`, `hoi4.probability_inspect`, `hoi4.probability_evaluate`, `hoi4.probability_sweep`, `hoi4.probability_simulate`, `hoi4.probability_sequence`, `hoi4.probability_compare`, `hoi4.probability_render`, and technology/focus/GUI routes. Direct callable checks returned undefined and the exposed tool inventory contained no `mcp__hoi4_agent_tools__*` route. Therefore the mandatory first probability inspection, detailed probability audit, event inspection/render, and map inspection/render could not run, and no artifact URIs exist.

- The installed package has no Technology Tree Viewer. Event 028 has no accepted technology surface, so no technology route was invented or substituted.

- The legacy source/register conflict is confirmed: `events/028_asteroid_impact.txt` is repeatable prediction/nuclear code while the accepted package requires a major fire-once transaction. The current default rework gate also lacks Event 028.

- Event 028 gameplay, decision/category, dynamic-modifier, achievement, event-localisation, super-event, sound, and GFX consumer layers are incomplete or absent. Constants, triggers, and footprint-planning effects are scaffolding, not a complete implementation.

- Super-event numeric slot `28` is occupied by the Holy Realm track and wrappers. The Event 028 audio files do not establish a safe unique registry slot.

- Achievement IDs and final triplets are not locked. The asset manifest correctly leaves those five achievement families blocked rather than guessing filenames.

- `docs/spreadsheets/chaos_redux_events_catalog.xlsx` and its export are stale. The CSV cannot be repaired independently because it is export-only.

- No `docs/events/028_asteroid_incoming/overview.md` was found.

### Ordinary implementation risks

- `every_neighbor_state` is only a one-hop primitive; nested or looped use can duplicate states unless the aligned seen/profile arrays remain authoritative. Engine behavior and installed-map adjacency were not MCP-verified.

- The existing exact-loss helper can be gated by Chaos Meter settings and target-country flags. The parent must document which settings still record civilian Deaths and verify that actual debit, survivors, and destination/owner scope are not inferred from requested values.

- The global Air reservoir is shared state. Duplicate source guards, cap handling, source class, and monthly consumption must be explicit or multiple impact/secondary paths can multiply Air Cleanliness penalties.

- Owner/controller/annex/civil-war/peace/release transitions can leave stale state pointers or armour contributions. Global event targets must be cleared and mineral site registration must be idempotent.

- The 098 precedent confirms a dynamic modifier cannot contain the required `equipment_bonus` armour block. A fixed country-idea or another engine-supported aggregate is a design decision requiring validation, not a safe assumption.

- Reusing old nuclear or Death wasteland helpers would import forbidden fallout, history, reconstruction, or callback semantics. The stale famine/migration handoffs must be updated with the new ownership boundary.

- Shared event-log arrays are parallel registries. A missing actor/detail/evolution value can shift later rows even when the gameplay transaction is correct.

- The accepted decision package has multiple phases and many actions. Category clutter, high cost-type count, missing reserve floors, and zero AI scores are likely if the phase gates are not enforced.

- Old `events/070_africa_gods.txt` hidden-event calls can bypass the new lock and fail-closed path. Leaving them unchanged creates a second entry point to the transaction.

- The worktree contained unrelated changes across Event 024-029 sources, shared systems, assets, audio, and documentation, including deletions and untracked files. The final status was not clean; none of those files were touched by this exploration.

## Recommended next action

The parent should first reconcile the Event 028 source/register conflict and complete the existing target-lock/footprint scaffolding into one owner-controlled transaction, while preserving the exact-population helper and adding a purpose-specific Air adapter. In parallel, lock final decision, achievement, event-detail, and super-event identifiers so the missing gameplay, presentation, catalog, and asset consumers can be implemented as one synchronized pass. The parent should rerun the mandatory HOI4 event, probability, and map inspections when a callable production MCP namespace is available; until then, this report and the existing probability baseline are source-only evidence.
