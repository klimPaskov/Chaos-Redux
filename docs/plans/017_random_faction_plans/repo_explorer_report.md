# Event 017 Random Faction repository explorer report

Date: 2026-07-10

Role: read-only repository exploration and implementation handoff

> Cleanup status, 2026-08-22: This report remains a historical exploration snapshot. The launcher list below predates the retirement of `holy_realm_prepare_final_silence`; the surviving `holy_realm_complete_terminal_final_silence` helper now requests the shared Fallout aftermath before the shared world-end lock is written. Do not use the old Holy Realm launcher entries as current call-site evidence.

## Executive finding

Event 017 has a complete four-part design package and a preserved final asset package. The committed branch at the start of this exploration still contained the inert Event 017 placeholder. A concurrent implementation pass populated the Event 017 gameplay files and many shared registries while this report was being prepared. Those concurrent files are mapped below, but this report does not treat them as audited or complete.

The implementation must remain a dynamic faction system. It must select an eligible independent minor, build one to four distinct options from living faction leaders, let a selected human choose without a decline option, use the same saved options for AI, apply pressure memory, support three evolutions, expose Bloc Pressure decisions and missions, record history and evolution details, join Diplomatic Panic as a low-severity member, wire six achievements, and keep the workbook and documentation synchronized. No reduced substitute or fallback implementation is proposed here.

Two specific historical defects must not return:

1. Do not clean `FROM` unconditionally in faction and subject lifecycle callbacks. The removed implementation could erase a valid faction leader's pressure state when another country left that leader's faction.
2. Do not set a general `random_faction_prefer_current_dispatch_target` flag inside `fire_event_by_temp_id_no_cluster`. That shared helper is used by automatic firing, cluster member firing, event-detail triggering, and manual settings. The old approach could make the caller, often the player country, replace the weighted random target.

One-off `every_country` scans inside an Event 017 dispatch are acceptable for weighted pool construction. Periodic `on_daily`, `on_weekly`, `on_monthly`, or similar all-country scans are not acceptable. Cleanup should remain on narrow lifecycle hooks and exact terminal launchers.

## Source hierarchy used

The implementation should resolve questions in this order:

1. `AGENTS.md` and the Event 017 specification package
2. Current Chaos Redux patterns
3. Vanilla documentation and vanilla script precedents
4. The removed Event 017 implementation as a defect and naming reference only

The old Event 017 code is not completion evidence. It was implemented in `3c6672ed`, received load and dispatch fixes in `deba0b73` and `2d3a7750`, and was deliberately removed in `1258e1d0`. The removal commit does not explain why. Reusing old blocks without reviewing them against the current specification and current repository patterns would be unsafe.

## Specification contract

### Identity and registration

- Event id: `17`
- Event name: `Random faction`
- Type: `Minor Repeatable`
- Entry event: `chaosx.nr17.1`
- Cluster: preferred existing `Diplomatic Panic`, id `constant:event_cluster_id.diplomatic_panic`
- Cluster severity: low
- Evolution I: `Regional Bloc Race`
- Evolution II: `Pressured Neutrality`
- Evolution III: `Collapse of Neutrality`

The historical localisation used `Neutrality Collapse` for stage III. The current specification uses `Collapse of Neutrality`, so the historical wording should not be copied blindly.

### Required event chain

| Event | Required role |
| --- | --- |
| `chaosx.nr17.1` | entry and runtime preparation |
| `chaosx.nr17.10` | selected human minor choice |
| `chaosx.nr17.20` | selected AI minor resolver |
| `chaosx.nr17.30` | pressured neighbor follow-up |
| `chaosx.nr17.40` | faction leader reaction |
| `chaosx.nr17.50` | Evolution I regional bloc race follow-up |
| `chaosx.nr17.60` | Evolution II pressured neutrality incident |
| `chaosx.nr17.70` | Evolution III cascade resolver |
| `chaosx.nr17.80` | regional cascade report |

Supplemental timer or achievement events may use additional namespace ids, but they need a documented purpose. The removed version used `.81`, `.82`, `.83`, `.84`, and `.86`. Those ids are historical hints, not specification requirements.

### Required shared trigger contract

- `is_random_faction_eligible_country`
- `is_random_faction_allowed_faction_leader`
- `can_random_faction_join_faction`
- `is_random_faction_pressure_neighbor`
- `has_random_faction_active_pressure`
- `is_random_faction_wartime_candidate`
- `random_faction_region_can_cascade`

The live implementation also benefits from narrowly named helpers for current-country tracked state, option validity, option count, AI scoring, category visibility, decision costs, mission objectives, and faction-leader target validation.

### Required shared effect contract

- `random_faction_prepare_runtime_context`
- `random_faction_collect_faction_options`
- `random_faction_ai_choose_option`
- `random_faction_join_selected_faction`
- `random_faction_apply_alignment_shock`
- `random_faction_apply_regional_pressure`
- `random_faction_schedule_neighbor_followup`
- `random_faction_run_evo2_pressure`
- `random_faction_run_evo3_cascade`
- `random_faction_cleanup_country_pressure`
- `random_faction_cleanup_dead_faction_targets`

The player option, AI resolver, cascade resolver, and commitment decision must call the same option and join helpers. They must not contain four independent versions of faction validation.

### Required regular event targets

- `random_faction_target_country`
- `random_faction_option_1_leader`
- `random_faction_option_2_leader`
- `random_faction_option_3_leader`
- `random_faction_option_4_leader`
- `random_faction_selected_leader`
- `random_faction_pressure_source_country`

Regular event targets fit the initial selection and choice chain because they carry into events fired from the same effect chain and clear automatically. Persistent Bloc Pressure cases should use country variables, flags, scoped variables, or carefully maintained arrays. Global event targets should be reserved for state that must outlive the event chain and must have explicit cleanup.

### Required decisions and missions

| Identifier | Actor and form |
| --- | --- |
| `random_faction_stabilize_alignment` | newly aligned minor decision |
| `random_faction_request_liaison` | newly aligned minor decision |
| `random_faction_quiet_opposition` | newly aligned minor risky decision |
| `random_faction_convene_neutrality_council` | pressured neutral decision |
| `random_faction_reinforce_border_posts` | pressured neutral mission |
| `random_faction_invite_observers` | pressured neutral targeted decision |
| `random_faction_publish_neutrality` | pressured neutral cooldown decision |
| `random_faction_offer_staff_mission` | faction leader targeted decision |
| `random_faction_radio_networks` | faction leader regional decision |
| `random_faction_guarantee_corridor` | faction leader targeted decision and mission |
| `random_faction_demand_commitment` | faction leader high-pressure decision |

The decision matrix requires concrete equipment, convoy, command, stability, war support, relations, controlled-state, and stationed-division conditions where appropriate. Political power alone is not a complete cost model.

### Required achievements

- `017_random_faction_four_doors`
- `017_random_faction_hold_the_line`
- `017_random_faction_crowded_border`
- `017_random_faction_liaison_web`
- `017_random_faction_frontier_commitment`
- `017_random_faction_not_everyone`

All six need registry entries, name and description localisation, custom tooltip localisation, triplet sprites, runtime proof flags or variables, expiry checks, and disqualifier cleanup.

## Current file map

### Core Event 017 files

These are the intended Event 017-owned surfaces. They appeared as modified or new files in the concurrent working tree at report time.

| Path | Ownership |
| --- | --- |
| `events/017_join_faction.txt` | namespace, entry, choice, follow-up, cascade, report, and timer events |
| `common/scripted_effects/017_random_faction_effects.txt` | selection, weighting, joining, pressure, evolution, decisions, achievements, cleanup |
| `common/scripted_triggers/017_random_faction_triggers.txt` | eligibility, option validation, AI gates, decision and mission gates |
| `common/script_constants/chaosx_random_faction_constants.txt` | event ids, stages, thresholds, durations, weights, costs, caps |
| `common/ideas/017_random_faction_ideas.txt` | alignment shock, border pressure, polarization, neutrality exhaustion, liaison |
| `common/decisions/categories/017_random_faction_categories.txt` | Bloc Pressure category and category picture |
| `common/decisions/017_random_faction_decisions.txt` | actor-specific decisions and missions |
| `common/on_actions/017_random_faction_on_actions.txt` | narrow lifecycle reconciliation only |
| `common/scripted_localisation/017_random_faction_scripted_localisation.txt` | option leader names, pressure status, dynamic decision text |
| `localisation/english/017_join_faction_l_english.yml` | all Event 017 player-facing text |
| `interface/017_random_faction.gfx` | report, decision, idea, static, and animated sprites |
| `docs/events/017_random_faction/overview.md` | current mechanic documentation |

Every new script file needs an overview header. The localisation file must remain UTF-8 with BOM and use keys without `:0`.

### Shared registration and dispatch surfaces

| Path and identifier | Exact Event 017 work |
| --- | --- |
| `common/scripted_effects/chaosx_logic_effects.txt`, `initialize_event_categories` | add id `17` to the repeatable array between `13` and `18` only when the full implementation is ready |
| `common/scripted_effects/chaosx_settings_effects.txt`, `fire_event_by_temp_id_no_cluster` | prepare Event 017 context before history recording, reject unavailable context, then dispatch `.1` in `event_target:random_faction_target_country` |
| `common/scripted_triggers/chaosx_settings_triggers.txt`, `event_log_event_is_reworked_default_enabled` | id `17` is already default-enabled in the committed baseline |
| `common/scripted_localisation/chaosx_scripted_localisation_settings.txt` | id `17` already maps through `chaosx.event_name.17` in selected and last-fired name selectors |
| `common/scripted_localisation/chaosx_scripted_localisation_debug.txt` | id `17` already maps through `chaosx.event_name.17` in debug display |
| `localisation/english/chaosx_event_names_l_english.yml` | replace `Event 017 Placeholder` with the final event name |

The default-enabled allowlist is a latent activation risk. Once id `17` enters `initialize_event_categories`, automatic firing can begin. Registration should be the last gameplay step, or all dispatch and availability plumbing must land atomically with it.

The current concurrent settings implementation prepares the weighted runtime context without the removed `random_faction_prefer_current_dispatch_target` flag. It then dispatches `chaosx.nr17.1` in the selected target scope. This is the correct direction. Preserve it.

### Event log, detail, and evolution surfaces

| Path and identifier | Exact work |
| --- | --- |
| `common/scripted_effects/chaosx_events_log_effects.txt`, `events_log_set_default_actor_for_current_event` | map Event 017 history actor to the valid `random_faction_target_country` |
| `common/scripted_effects/chaosx_events_log_effects.txt`, `events_log_rebuild_open_event_details_view` | add three Event 017 evolution preview rows with correct type, stage, and tier |
| `common/scripted_effects/chaosx_events_log_effects.txt`, live event weight rebuild | mark Event 017 unavailable when no eligible target and valid faction option can be prepared |
| `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` | add Event 017 selectors for every main, history-detail, event-detail, selected-evolution title, type, and body surface |
| `interface/chaosx_events_log_popup.gui` | generic rows should be reusable, change only if the existing layout cannot show the Event 017 content |
| `localisation/english/017_join_faction_l_english.yml` | define the detail body, evolution type, three stage titles, three stage bodies, and event-detail title and body |

The Event 011 pattern is the closest current integration model:

- `secret_alliance_prepare_random_event_fire` prepares its target before generic history recording.
- `events_log_set_default_actor_for_current_event` validates `secret_alliance_target` and converts it to `events_log_default_actor`.
- `secret_alliance_record_evolution` sets `events_log_evolution_event_id`, `events_log_evolution_type`, `events_log_evolution_stage`, `events_log_evolution_tier`, `events_log_evolution_has_actor`, and `events_log_evolution_actor` before calling `record_events_log_evolution_entry`.
- `secret_alliance_record_open_evolutions_if_needed` prevents duplicate stage records.
- `chaosx_scripted_localisation_events_log.txt` repeats the three stage selectors across main evolution, history detail, event detail, selected title, and selected body views.

Event 017 should follow that full pattern. Adding only the main evolution names leaves blank history or event-detail rows.

### Cluster surfaces

| Path | Exact work |
| --- | --- |
| `common/script_constants/event_cluster_constants.txt` | add the Event 017 participation constant if the optional-member route is selected |
| `common/scripted_effects/chaosx_event_cluster_effects.txt`, `event_belongs_to_cluster` | map Event 017 to Diplomatic Panic |
| `common/scripted_effects/chaosx_event_cluster_effects.txt`, `load_event_cluster_members` | append an aligned Event 017 row to the Diplomatic Panic member arrays |
| `docs/systems/event_clusters.md` | list Event 017 and describe its diplomatic pressure role |
| `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, `Clusters` | change the Diplomatic Panic member cell from `8` to the established multi-member string `8, 17` |

The specification requires a low-severity diplomacy member. It leaves required versus optional to the cluster design. The removed implementation used an optional low-severity tier-zero row and `event_cluster_member_participation.random_faction = 65`. That `65` is historical tuning, not a value mandated by the specification. If retained, it should be reviewed against Event 008 cadence and documented as the chosen value.

All member arrays in `load_event_cluster_members` must remain index-aligned for event id, role, chance, minimum tier, and danger.

### Achievement surfaces

| Path | Exact work |
| --- | --- |
| `common/achievements/chaos_redux_achievements.txt` | add all six achievement definitions |
| `interface/chaosx_achievements.gfx` | add normal, grey, and not-eligible sprites for all six |
| `localisation/english/chaosx_achievements_l_english.yml` | add `_NAME`, `_DESC`, and custom tooltip text |
| `common/scripted_effects/017_random_faction_effects.txt` | implement proof, timer, expiry, and disqualifier logic |
| `events/017_join_faction.txt` | host delayed checks only where a flag duration cannot prove the full condition |

Event 013 and the current root achievement files are the best active registry pattern. The removed Event 017 achievement block is useful for identifiers and intended proof direction, but it must be checked against the current achievement specification.

### Asset surfaces

The preserved package already contains final report images, decision icons, idea icons, six achievement triplets, two static animation fallbacks, two eight-frame sheets, source frames, contact sheets, GIF previews, and DDS copies.

Runtime paths:

- `gfx/event_pictures/017_random_faction/`
- `gfx/interface/decisions/017_random_faction/`
- `gfx/interface/ideas/017_random_faction/`
- `gfx/interface/animated/017_random_faction/`
- `gfx/achievements/017_random_faction_*.dds`

Source and review package:

- `docs/assets/017_random_faction/manifest.md`
- `docs/assets/017_random_faction/gfx_handoff.md`
- `docs/assets/017_random_faction/source/`
- `docs/assets/017_random_faction/processed_png/`
- `docs/assets/017_random_faction/animations/`
- `docs/assets/017_random_faction/contact_sheets/`

At the committed placeholder baseline, `docs/assets/017_random_faction/gfx_handoff.md` claimed that `interface/017_random_faction.gfx` and the achievement sprites were already registered, but the Event 017 GFX file and achievement entries were absent. The concurrent implementation has created and modified those registries. The final asset audit must validate the live files rather than relying on the stale handoff sentence.

No duplicate art production is needed unless an asset review finds a concrete defect.

### Documentation and workbook surfaces

| Path | Required final state |
| --- | --- |
| `docs/events/017_random_faction/overview.md` | full current mechanic, flow, eligibility, memory, decisions, evolutions, logs, cluster, achievements, assets, cleanup, tuning, future plans |
| `docs/systems/event_clusters.md` | Event 017 membership and role |
| `docs/assets/017_random_faction/manifest.md` | exact final sprite and runtime wiring state |
| `docs/assets/017_random_faction/gfx_handoff.md` | no stale registration claims |
| `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, `Events!18` | final name, detail text, Evo I to III, type, cluster id, severity, and status |
| `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, `Clusters!4` | member list `8, 17` and final status if implementation completes the cluster |

At exploration time, `Events!18` still held `Event 017 Placeholder`, placeholder detail text, type `Placeholder`, and status `Removed`. `Clusters!4` still listed member `8` only. The workbook was not modified by the concurrent gameplay pass at the time of this report. The spreadsheet worker must use final in-game localisation wording, not an independent paraphrase.

## Weighted selection architecture

### Country pool

Build a temporary weighted ticket array in `random_faction_prepare_runtime_context`:

1. Refresh only Event 017 tracked arrays.
2. Run a one-off `every_country` scan.
3. Require `is_random_faction_eligible_country`, or the explicit Evolution II wartime candidate route.
4. Calculate the current country's dynamic ticket weight from size, war pressure, geography, recent pressure, neutrality resilience, prior alignment, and human eligibility.
5. Append the country scope once per positive ticket.
6. Use `random_scope_in_array` with a validity limit to save `random_faction_target_country`.
7. Clear the temporary pool after selection.

Human countries remain eligible but receive no unconditional preference. A manual settings trigger should still run the same weighted selection unless a separate, explicit debug-only current-country path is designed and documented.

### Faction option pool

In the selected country scope:

1. Run a one-off scan of living faction leaders.
2. Require `is_random_faction_allowed_faction_leader`.
3. Revalidate that the selected country can join and is not at war with that leader or a member of that leader's faction.
4. Score ideology, proximity, common enemies, active war help, relations, faction military strength, region pressure, rivalry, and neutrality resilience.
5. Save up to four distinct leader targets.
6. Store an exact option count.

The selected human and AI resolver must use those same saved targets. AI must not rebuild a different pool after the player-facing path has already been prepared.

### Click-time revalidation

Every option must validate its saved leader when selected. If one leader becomes invalid, rebuild the remaining complete option set for the same country. This is recovery within the specified mechanic, not a weaker substitute. If no valid leaders remain, cancel the dispatch cleanly without recording a false history row or applying partial pressure state.

The specification calls the old recovery branch a “safe fallback event.” Repository rules forbid an unapproved fallback implementation. Name and implement it as full revalidation and reselection, with no alternate reduced behavior.

## Narrow lifecycle and special-chaos integration

### Current Event 017 on-action direction

The concurrent `common/on_actions/017_random_faction_on_actions.txt` uses narrow callbacks and avoids recurring global scans. Its current structure is substantially safer than the removed version:

- `on_join_faction` recognizes `random_faction_join_in_progress`, clears only that guard, and otherwise reconciles tracked external joins.
- `on_leave_faction` cleans only `ROOT` and does not clean `FROM` unconditionally.
- `on_assume_faction_leadership` uses a named successor target and transfers tracked leader state deliberately.
- `on_capitulation`, `on_uncapitulation`, `on_puppet`, `on_release_as_puppet`, `on_release_as_free`, `on_subject_free`, `on_subject_autonomy_level_change`, `on_subject_annexed`, and `on_government_exiled` act only when the current country has Event 017 state.
- `on_annex` inspects the annexed `FROM` scope specifically.
- `on_government_change` cleans tracked state only when the country no longer passes the Event 017 base-valid trigger.

This pattern should be preserved. Consider `on_civil_war_end` only if a concrete Event 017 pointer can remain stale through that callback. Do not copy Event 011's entire hook list mechanically when Event 017 has no state that needs a given callback.

### Historical `FROM` cleanup defect

The removed `common/on_actions/017_random_faction_on_actions.txt` called `random_faction_cleanup_after_country_lifecycle_change` on both `ROOT` and `FROM` in `on_leave_faction`, capitulation, puppet, release, subject, and annex callbacks.

That is unsafe. In `on_leave_faction`, `FROM` can be the faction leader that the leaving member just departed. Cleaning it could clear valid supported-minor arrays, liaison state, corridor missions, and leader decision state even though the leader still exists and still leads its faction. Subject and annex callbacks also have hook-specific `FROM` meanings. Each callback must follow documented scope semantics and clean only the country whose Event 017 state became invalid.

Event 011 provides the safer precedent. Its on-actions usually call `secret_alliance_handle_country_state_change` in `ROOT`. Its `on_annex` path uses the annexed `FROM` only for a purpose-specific callback before running the shared reconciliation.

### Special-chaos eligibility source

`common/scripted_triggers/chaosx_dynamic_triggers.txt` defines `is_special_chaos_country` from:

- zombie and weaponized zombie identities
- `REV` and communist rebel flags
- `ZIN`
- Holy Realm tags and `is_holy_realm_country`
- Mengele civil-war and post-coup flags
- `fury_actor`
- `DTH` and `death_country`

Event 017 eligibility and leader validation must require both ordinary civilian behavior and `NOT = { is_special_chaos_country = yes }`.

### Special-chaos transition activation locations

Two existing-country transitions need direct Event 017 cleanup because a periodic scan is forbidden and a government callback is not guaranteed to represent the identity change:

| Path and effect | Activation | Required Event 017 action |
| --- | --- | --- |
| `common/scripted_effects/007_fury_effects.txt`, `fury_apply_package` | `set_country_flag = fury_actor` | immediately reconcile or clear Event 017 tracked state after the flag is set |
| `common/scripted_effects/003_holy_realm_effects.txt`, `holy_realm_setup_country` | `save_global_event_target_as = holy_realm_country`, which makes `is_holy_realm_country` true | immediately reconcile or clear Event 017 tracked state after the Holy Realm target is established |

Other special identities are lower stale-state risks:

- `common/scripted_effects/010_death_effects.txt`, `death_setup_country`, initializes the fixed DTH identity, which Event 017 already excludes.
- `common/scripted_effects/001_communism_spread_effects.txt` creates new rebel-country scopes before setting `communist_rebel_state` and `communist_state_control_rebel`.
- `common/scripted_effects/zombie_special_project_effects.txt`, `initialize_wendigo_incident_outbreak_country` and `weaponized_zombie_copy_profile_to_outbreak`, initialize new outbreak scopes.
- `ZIN`, `ZZZ`, and `DTH` fixed tags are invalid from the beginning.
- The Mengele special flags are present in the shared trigger, but no active setter was found during this exploration. If a future implementation sets either flag on an ordinary tracked country, that exact transition must call Event 017 cleanup.

The current `on_government_change` cleanup remains useful, but it should not be the only protection for Fury or Holy Realm identity activation.

### World-end cleanup locations

There is no single world-end on-action. Exact launchers must call `random_faction_cleanup_after_world_end` after setting `world_end`:

- `events/002_zombie_outbreak.txt`, zombie and wendigo terminal branches
- Historical only: `common/scripted_effects/003_holy_realm_effects.txt`, `holy_realm_prepare_final_silence`, was removed after exact reference checks proved it superseded and uncalled.
- `common/scripted_effects/003_holy_realm_effects.txt`, `holy_realm_complete_terminal_final_silence`, is no longer a direct shared `world_end` setter; it hands the terminal consequence to the Fallout coordinator.
- `common/scripted_effects/007_fury_effects.txt`, `fury_start_world_end`
- `common/scripted_effects/010_death_effects.txt`, `death_try_start_world_end`
- `common/scripted_effects/germany_mengele_effects.txt`, `mengele_clone_world_order_launch`
- `events/chemical_warfare_events.txt`, fallout world-end branch
- `common/scripted_effects/chaosx_settings_effects.txt`, manual world-end trigger

The concurrent implementation has already modified these terminal surfaces. Final review should confirm every current `set_global_flag = world_end` call has Event 017 cleanup exactly once and that the cleanup clears only Event 017 arrays, missions, ideas, flags, and persistent targets.

## Historical generic-dispatch defect

Commit `2d3a7750` introduced `random_faction_prefer_current_dispatch_target`. The old `fire_event_by_temp_id_no_cluster` set that flag on its current country before preparing Event 017 context.

That shared helper is called by:

- `fire_event_by_id` in the settings UI
- automatic event firing after a cluster roll does not replace the selected event
- `events_log_trigger_open_event_detail_entry`
- `event_cluster_fire_current_member`

The flag therefore did not describe only a manual debug action. It could force the current caller to become Event 017's target during cluster and other generic dispatches. When the current caller was the player country, Event 017 appeared to always prefer the player instead of using the weighted global pool.

The current concurrent settings code no longer sets that flag. It calls `random_faction_prepare_runtime_context`, blocks dispatch if context is unavailable, and fires `.1` in `event_target:random_faction_target_country`. Keep this structure.

## Chaos Redux precedents

### Event 004 Random War

Use:

- `common/scripted_effects/004_random_war_effects.txt`
- `common/scripted_triggers/004_random_war_triggers.txt`
- `events/004_random_war.txt`

Relevant patterns:

- one-off dynamic country selection
- regular event targets for paired countries
- special prefire context before generic history recording
- `random_war_fire_current_context` for dispatch in the selected actor scope

### Event 008 Tensions Rising

Use:

- `events/008_tensions_rising.txt`
- `common/scripted_effects/008_tensions_rising_effects.txt`
- `common/scripted_triggers/008_tensions_rising_triggers.txt`
- `common/script_constants/008_tensions_rising_constants.txt`
- `common/on_actions/008_tensions_rising_on_actions.txt`
- `common/ideas/008_tensions_rising_ideas.txt`
- `common/scripted_localisation/008_tensions_rising_scripted_localisation.txt`
- `localisation/english/008_world_tension_rises_l_english.yml`

Relevant patterns:

- minor repeatable diplomatic event
- evolution recording
- Diplomatic Panic membership
- event-detail and history-detail localisation selectors
- achievements tied to repeated diplomatic pressure

### Event 011 Secret Alliance

Use:

- `events/011_secret_alliance.txt`
- `common/scripted_effects/011_secret_alliance_effects.txt`
- `common/scripted_triggers/011_secret_alliance_triggers.txt`
- `common/decisions/011_secret_alliance_decisions.txt`
- `common/decisions/categories/011_secret_alliance_categories.txt`
- `common/ideas/011_secret_alliance_ideas.txt`
- `common/on_actions/011_secret_alliance_on_actions.txt`
- `common/script_constants/011_secret_alliance_constants.txt`
- `common/scripted_localisation/011_secret_alliance_scripted_localisation.txt`
- `localisation/english/011_secret_alliance_l_english.yml`
- `interface/011_secret_alliance.gfx`

Relevant patterns:

- weighted ticket arrays and `random_scope_in_array`
- scoped target validation
- persistent arrays with reconciliation
- narrow lifecycle callbacks
- targeted decisions and concrete costs
- prefire target and event-log actor integration
- complete evolution selectors across every log view

Event 011 uses global event targets because much of its system persists across a long scenario. Event 017's initial one-choice chain should prefer regular event targets.

### Existing dynamic helpers

`common/scripted_effects/chaosx_dynamic_effects.txt` and `chaosx_dynamic_effects.md` do not currently expose a generic helper that replaces Event 017's country and leader pool logic. Event-specific selection belongs in `017_random_faction_effects.txt` unless a genuinely reusable cross-event interface is designed and documented.

Existing shared systems to call rather than duplicate:

- repeatable firing and history recording in `chaosx_logic_effects.txt`
- event history and evolution records in `chaosx_events_log_effects.txt`
- cluster selection in `chaosx_event_cluster_effects.txt`
- settings dispatch in `chaosx_settings_effects.txt`
- shared `is_special_chaos_country` and ordinary-country triggers in `chaosx_dynamic_triggers.txt`

## Vanilla precedents

### Faction leader resolution and joining

`C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/events/AAT_Finland.txt`, around lines 663 to 682, validates that `FROM` is in a faction. If `FROM` is the faction leader, it uses `FROM = { add_to_faction = ROOT }`. Otherwise it finds a country that is both in the same faction and the faction leader, then executes `add_to_faction = ROOT` in that leader scope.

`C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/events/Germany.txt`, around lines 2449 to 2463, selects a valid faction leader with `random_country`, requires that leader to be in the same faction as `ROOT`, and calls `add_to_faction = CZE` from the leader scope.

These precedents support Event 017's required direction: resolve and validate the actual leader scope, then call `add_to_faction` from that leader scope with the selected minor as the target.

### Documentation rules applied

- Regular event targets carry into events fired from the same chain and then clear automatically.
- Global event targets persist and require explicit `clear_global_event_target` cleanup.
- `add_to_faction` is a supported country-scope effect with a country target.
- `random_scope_in_array` supports a validity limit and is suitable for weighted ticket arrays.
- Temporary variables are unscoped.
- Script constants are global but are not accepted by every field. Duration and opinion-value exceptions need documented file constants or an intermediate variable.
- Scripted GUI can use event targets as scope pointers. Persistent GUI targets must still use the appropriate regular or global lifetime, clear global targets explicitly, and guard against stale or invalid scopes; variables, flags, and arrays remain suitable for non-pointer state.

## Concrete implementation order

1. Freeze the accepted specification names, especially `Collapse of Neutrality`, achievement ids, decision ids, cluster role, and final constants.
2. Finish and review `chaosx_random_faction_constants.txt`, Event 017 triggers, and the shared option and join effects.
3. Verify the weighted one-off country and leader pools for zero, one, two, three, and four-or-more option cases.
4. Finish the event chain and make human and AI choice routes call the same saved-option helpers.
5. Finish pressure memory, ideas, decisions, missions, AI use, and concrete costs.
6. Finish the narrow on-action reconciliation. Add direct Fury and Holy Realm transition cleanup.
7. Finish all world-end launcher calls and verify Event 017-only cleanup.
8. Finish event log actor mapping, evolution recording, previews, availability, and every scripted-localisation view.
9. Finish Diplomatic Panic arrays and documentation with index alignment.
10. Finish six achievement proof paths, disqualifiers, timers, sprites, and localisation.
11. Verify the Event 017 GFX registry against every preserved DDS and animation sheet.
12. Update the event doc, asset handoff, catalog `Events!18`, and cluster `Clusters!4` from final localisation.
13. Run Event 017 completion, decision and mission, and localisation audits.
14. Add id `17` to the repeatable event array only after all automatic dispatch requirements are valid.

## Task-specific validation scenarios

### Entry and target selection

- No eligible minor or no valid faction leader leaves Event 017 unavailable and creates no history row.
- A human minor is eligible but receives no unconditional player preference.
- Manual settings, automatic firing, event-detail firing, and cluster firing all use the same weighted target preparation unless an explicit debug-only route says otherwise.
- No selection or option logic contains Axis, Comintern, or other hardcoded faction assumptions.

### Option counts and invalidation

- Worlds with exactly one, two, three, and four-or-more valid factions show exactly one, two, three, and four distinct human options.
- AI reads the same saved leader targets as the human event route.
- A leader that disappears between opening and selection cannot be joined.
- Reselection uses the same country and complete validity rules.
- If all leaders disappear, no partial pressure, cooldown, achievement, or false history state remains.

### Joining and history actor

- `add_to_faction` executes from the selected valid leader scope.
- The selected minor is the history actor for automatic, manual, and cluster firing.
- The selected faction leader is retained only where a later persistent mechanic needs it.
- Event 017's own `on_join_faction` guard prevents immediate cleanup of the join it just performed.

### Evolution behavior

- Evolution-disabled settings prevent stage activation and evolution history records.
- Evolution I schedules at most one intended delayed neighbor response per firing.
- Evolution II validates wartime minors, direct enemies, faction reach, and border mission targets.
- Evolution III selects only two to five capped regional candidates and leaves at least a possible neutral survivor.
- Evolution III does not create arbitrary wars or pull every eligible country into a faction.
- Stage, tier, type, and actor are correct in main evolution, history detail, event detail, selected title, and selected body views.

### Decisions, missions, and AI

- Every decision has a concrete visible cost, available trigger, completion effect, cancellation condition, AI weight, and effect tooltip.
- Border Posts validates the named state or capital objective and equipment reserve.
- Corridor Guarantee validates target, route, convoy reserve, and mission expiry.
- AI cannot farm repeated staff missions, radio networks, corridors, or commitments against invalid or friendly targets.
- Pressure and neutrality values clamp to documented ranges.

### Lifecycle and special countries

- A tracked member leaving a faction loses only invalid aligned state.
- The former faction leader keeps valid support and decision state when a member leaves.
- Leadership transfer preserves valid leader memory and clears the predecessor only after transfer.
- Capitulation, uncapitulation, subject changes, annexation, exile, and government change leave no stale Event 017 arrays or missions.
- A tracked ordinary country becoming the Fury actor or Holy Realm immediately loses incompatible Event 017 state.
- World-end launchers clear Event 017 state exactly once without touching other event systems.

### Cluster and achievements

- Diplomatic Panic arrays remain aligned when Event 017 is appended.
- Event 017 fires as low severity and does not create a cluster war goal.
- `four_doors` requires four live options, a completed join, and the full survival period.
- `hold_the_line` requires the council, successful border mission, continued independence, no faction, and no capitulation through the full period.
- `crowded_border` counts three distinct factions, not three members of one faction.
- `liaison_web` counts three distinct supported minors and revalidates them at expiry.
- `frontier_commitment` revalidates capital and all required core border states through the full period.
- `not_everyone` requires an Evolution III cascade and a valid eligible regional survivor outside factions.

### Assets and catalog

- Every `spriteType` resolves to an existing DDS with the expected dimensions.
- Both animations use their eight real source frames and retain a static fallback.
- All six achievement triplets are registered and match their ids.
- `Events!18` mirrors final in-game event and evolution wording.
- `Clusters!4` lists `8, 17` in the established string format.

## Remaining integration risks at report time

1. The working tree is changing concurrently. Review the final diff as one Event 017 plan before any commit.
2. Direct cleanup at `fury_apply_package` and `holy_realm_setup_country` was not present in the observed concurrent diff and remains a concrete special-chaos lifecycle gap.
3. The catalog workbook still held placeholder Event 017 data at the last read.
4. Repeatable registration can expose incomplete content immediately because id `17` is already default-enabled.
5. The old `FROM` cleanup and current-country dispatch shortcuts are easy to reintroduce when mining historical code.
6. The historical stage III title conflicts with the current specification title.
7. The historical cluster participation value is tuning evidence only and needs an explicit current balance decision.
8. Asset handoff prose was stale before the concurrent GFX rebuild. Runtime registries and manifests need final readback.
9. Event log localisation must be checked across every view, not only the main Events tab.
10. A passing load is not evidence that weighted selection, AI, missions, disqualifiers, and cleanup satisfy the design.

## Specification package read record

Every file under the requested Event 017 specification package was read:

### Root and research

- `docs/specs/017_random_faction_specs/README.md`
- `docs/specs/017_random_faction_specs/research/017_random_faction_research_notes.md`
- `docs/specs/017_random_faction_specs/source_review/full_read_manifest.md`

### Specifications

- `docs/specs/017_random_faction_specs/specs/017_random_faction_spec_part_1_core.md`
- `docs/specs/017_random_faction_specs/specs/017_random_faction_spec_part_2_bloc_pressure_and_decisions.md`
- `docs/specs/017_random_faction_specs/specs/017_random_faction_spec_part_3_evolutions_ai_balance.md`
- `docs/specs/017_random_faction_specs/specs/017_random_faction_spec_part_4_implementation_assets_acceptance.md`

### Matrices

- `docs/specs/017_random_faction_specs/matrices/017_random_faction_ai_matrix.md`
- `docs/specs/017_random_faction_specs/matrices/017_random_faction_catalog_handoff.md`
- `docs/specs/017_random_faction_specs/matrices/017_random_faction_decision_map.md`
- `docs/specs/017_random_faction_specs/matrices/017_random_faction_scripted_system_architecture.md`

### Main prompts

- `docs/specs/017_random_faction_specs/prompts/017_random_faction_achievement_prompt.md`
- `docs/specs/017_random_faction_specs/prompts/017_random_faction_asset_prompt.md`
- `docs/specs/017_random_faction_specs/prompts/017_random_faction_coding_prompt.md`
- `docs/specs/017_random_faction_specs/prompts/017_random_faction_decision_mission_prompt.md`
- `docs/specs/017_random_faction_specs/prompts/017_random_faction_goal_prompt.md`

### Subagent prompts

- `docs/specs/017_random_faction_specs/prompts/subagents/017_random_faction_subagent_routing.md`
- `docs/specs/017_random_faction_specs/prompts/subagents/chaosx_decision_mission_auditor_prompt.md`
- `docs/specs/017_random_faction_specs/prompts/subagents/chaosx_documentation_curator_prompt.md`
- `docs/specs/017_random_faction_specs/prompts/subagents/chaosx_event_completion_auditor_prompt.md`
- `docs/specs/017_random_faction_specs/prompts/subagents/chaosx_icon_artist_prompt.md`
- `docs/specs/017_random_faction_specs/prompts/subagents/chaosx_localisation_auditor_prompt.md`
- `docs/specs/017_random_faction_specs/prompts/subagents/chaosx_repo_explorer_prompt.md`
- `docs/specs/017_random_faction_specs/prompts/subagents/chaosx_scripted_system_architect_prompt.md`
- `docs/specs/017_random_faction_specs/prompts/subagents/chaosx_spreadsheet_doc_worker_prompt.md`

## Explorer handoff

This report changes no gameplay, asset, localisation, interface, or workbook file. It proposes no fallback, placeholder, omitted route, or reduced system. Its purpose is to keep the full Event 017 implementation ordered, expose the exact shared touchpoints, and prevent the known historical scope and dispatch defects from surviving the rebuild.
