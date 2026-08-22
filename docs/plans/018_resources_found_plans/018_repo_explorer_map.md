# Event 018 Resources Found — Repository Explorer Map

Date: 2026-07-11  
Mode: read-only repository/precedent mapping  
Implementation status: not started; the current two-event prototype must be replaced  
Source of truth: `docs/specs/018_resources_found_specs/`

## Superseded map notice

This is a 2026-07-11 planning snapshot, not a current implementation queue. The implemented and audited state is recorded in `docs/events/018_resources_found/`, `docs/super_events/018_resources_found/`, `docs/achievements/018_resources_found/`, `docs/systems/3d_model_pipeline/resources_found_cave_monster_model.md`, `018_static_acceptance_report.md`, and the current Event 018 handoffs. The event-scoped `docs/assets/018_resources_found/` folder is temporary evidence rather than a runtime dependency. A bounded cave-monster reconstruction tranche is retained there while final evidence gates remain open; historical tranche instructions must not recreate deleted production material, and the retained workspace must be removed only after genuine goal closure.

## 1. Purpose and constraints

This map identifies the exact repository surfaces, stable identifiers, collision-free reservations, reusable Chaos Redux patterns, vanilla precedents, ownership boundaries, and implementation order needed to implement Event 018 in full.

No gameplay, localisation, asset, workbook, or shared-system file was edited during this exploration. The only output is this plan. The worktree was already heavily dirty from unrelated camp-repression/system work, including shared super-event, achievement, localisation, audio, and workbook files. Every implementation tranche must re-read and merge around those changes; none may be overwritten.

Required references consulted:

- all Event 018 specifications, matrices, prompts, research notes, focus graph, manifest, and README;
- the repository skills `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-super-events`, and `chaos-redux-event-assets`;
- the required offline wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on-actions, events, decisions, ideas, AI, interface/scripted GUI, country creation, focuses, equipment, divisions/units, technology, states/resources, achievements, sound, and music;
- vanilla official documentation for effects, triggers, dynamic variables, script concepts/constants, focus inlays, localisation formatters, decisions, and on-actions;
- live Chaos Redux and vanilla implementations listed below.

## 2. Stable identifiers and collision reservations

Reserve these before implementation and re-run the collision scan immediately before each shared registry edit.

| Surface | Reservation | Evidence and rule |
|---|---:|---|
| Event namespace | `chaosx.nr18` | Existing namespace and dynamic dispatcher contract. Do not rename to `nr018`. |
| Entry event | `chaosx.nr18.1` | Required canonical entry root. Replace the prototype meaning. |
| Event ordinals | `.1-.15`, `.20-.32`, `.40-.44`, `.50-.59`, `.60-.73`, `.80-.89`, `.90-.99` | Reserved by the event chain matrix. Only `.1` and `.2` currently exist; all other ordinals are free. |
| Event ID | `18` | Existing repeatable-event ID. |
| Evolution type | `18` | Existing evolution types found are 1–11, 13, and 17. |
| Cluster ID | `7` | IDs 1–6 are currently occupied. Define `economy_positive = 7`. |
| Cave country tag | `DHO` | Recommended fixed tag, working expansion “Deep Host.” Unused across Chaos Redux, vanilla, Kaiserreich 1521695605, and approved mods 2265420196/1458561226. |
| Super-event display slots | `82`, `83`, `84` | A later live scan found that concurrent Event 014 needs slots 78 through 81. Use emergence, world end, global defeat in that order. |
| Super-event audio IDs | `54`, `55`, `56` | A later live scan found Event 014 audio claims on 49, 50, 52, and 53. IDs 54 through 56 are the Event 018 reservation. |
| Achievement block | 15 IDs beginning `018_resources_found_` | All 15 semantic stems in the prompt are unused. Achievements use semantic IDs, not a mandatory global numeric ordinal. |
| Death-reason enum | `resource_field_incident = 15` | Existing shared causes end at 14. Reserve a distinct cause rather than misclassifying deaths as natural disasters. |

### Country tag recommendation

Use fixed tag `DHO`, not a dynamic country, because the cave host is persistent, playable, has a bespoke focus tree, has tag-specific on-actions, needs stable assets/parties/history, and participates in achievements and terminal checks.

Avoid at least:

- `DTH` — Death;
- `DHC` — Don Host Emergency Circle;
- `THO` — occupied in approved reference mods;
- `HST` — occupied in an approved reference mod.

`DHO` is a technical reservation, not approval of final player-facing naming. Final country name, leader name, leader presentation, party names, and ideology forms remain design decisions in the specification. Because fallbacks are forbidden, do not ship a generic “Cave Country” or placeholder leader merely to unblock scripting. The fixed tag and internal keys can be implemented before final localisation/art, but the country package is incomplete until those decisions are supplied.

## 3. Current Event 018 implementation and direct replacements

### Existing files

- `events/018_random_resource.txt`
  - namespace `chaosx.nr18` at line 1;
  - `.1` at line 22 selects a random country and schedules `.2`;
  - `.2` at line 38 selects a random owned-and-controlled state and adds a hardcoded 200 of one of the six standard resources at lines 54–86;
  - `.2` fires `chaosx.news.20` at line 89;
  - no ledger, duplicate handling, valid-state filtering, actor context, AI, transfers, contracts, evolution state, exact closure, or cave route exists.
- `localisation/english/018_random_resource_l_english.yml`
  - only the old “Random Resource” event/news text; `.2` has a blank description.
- `events/_chaosx_news.txt:247-263`
  - `chaosx.news.20` and `GFX_news_random_resource`.
- `gfx/event_pictures/018_random_resource/report_event_random_resource.dds`
- `gfx/event_pictures/018_random_resource/news_random_resource.dds`
- `interface/chaosx_pictures.gfx:103`
  - registers the news sprite only. The report event asks for `GFX_report_event_random_resource`, but it is not registered.

### Replacement rule

Replace the meanings of `.1` and `.2`; do not retain them as a legacy path. Keep the namespace and canonical `.1` entry so the generic dispatcher can continue to construct `chaosx.nr[EVENT_ID].1` in `chaosx_settings_effects.txt:4648-4655`.

The two current DDS files are prototypes, not an approved fallback asset package. They may be superseded only through the Event 018 asset workflow and manifest.

## 4. Recommended owned-file layout

Create Event 018 logic in event-owned files so shared edits remain small and reviewable.

### Core field system

- `common/script_constants/018_resources_found_constants.txt`
- `common/scripted_effects/018_resources_found_effects.txt`
- `common/scripted_triggers/018_resources_found_triggers.txt`
- `common/decisions/categories/018_resources_found_categories.txt`
- `common/decisions/018_resources_found_decisions.txt`
- `common/on_actions/018_resources_found_on_actions.txt`
- `common/dynamic_modifiers/018_resources_found_state_modifiers.txt`
- `common/ideas/018_resources_found_ideas.txt`
- `common/opinion_modifiers/018_resources_found_opinion_modifiers.txt`
- `common/ai_strategy/018_resources_found.txt`
- `common/scripted_localisation/018_resources_found_scripted_localisation.txt`
- `common/scripted_guis/018_resources_found_scripted_gui.txt`
- `interface/018_resources_found.gui`
- `interface/018_resources_found.gfx`
- `events/018_random_resource.txt` (replace contents but retain path/namespace)
- `localisation/english/018_resources_found_l_english.yml` (preferred replacement name; remove or deliberately empty the obsolete file only in the same complete localisation change)

### Cave-country package

- `common/countries/Deep Host.txt` or final approved country filename;
- `history/countries/DHO - Deep Host.txt` or final approved filename;
- `common/characters/DHO.txt`;
- `common/country_leader/018_resources_found_traits.txt` if bespoke traits are required;
- `common/national_focus/018_resources_found_cave_focus_tree.txt`;
- `common/units/018_resources_found_cave_hosts.txt`;
- `history/units/DHO_1936.txt` only if an OOB file is used rather than fully scripted creation;
- country/focus/party/leader/idea/decision localisation in the Event 018 localisation package;
- flags and portraits under the standard game paths.

### Documentation and assets

- `docs/events/018_resources_found/overview.md`;
- `docs/events/018_resources_found/assets.md` as the durable runtime inventory after temporary-workspace cleanup;
- permanent specialist evidence in `docs/plans/018_resources_found_plans/subagent_handoffs/`;
- Event 018 super-event text/audio research files under `docs/super_events/`;
- Event 18 detail, evolution, and cluster fields in `docs/spreadsheets/chaos_redux_events_catalog.xlsx` after implementation facts and final localisation exist.

## 5. Field record and resource-ledger architecture

### Source of truth

Use one state-scoped Event 018 field record per state. Repeated discoveries in that state enrich the existing record; they do not append duplicate state references. The state record survives owner/controller changes and contains the geology/history. Countries maintain only unique arrays/pointers needed for current responsibility, UI, and decisions.

Minimum state data:

- marker and lifecycle flags: field exists, closed, fully sealed, cave origin, anchor pending, anchor active;
- unique discovery sequence, discoverer, current owner/controller presentation data, discovery date/count;
- exact six-resource ledgers: oil, aluminium, rubber, tungsten, steel, chromium;
- derived total, distinct-resource count, and largest-resource amount/type;
- Yield, Depth, Safety, Pressure;
- later Disturbance and Breach;
- posture/presentation/status;
- closure, transport, security, labour strain, concession, smuggling, contracts, deaths, exploitation;
- partner, claimant, saboteur, and former-owner/controller references where the scope must persist.

Use state normal variables for persistent numerical data and flags for Boolean state. Use event targets only for a firing/transfer chain; use global event targets only where persistence is genuinely necessary and provide explicit cleanup.

### Country-side indices

Maintain a unique `resources_found_active_fields` state array for the responsible country. Follow the Event 013 array pattern:

- one global/history record list if historical display requires it;
- one current-owner/controller unique array for actionable fields;
- a selected field index with clamp/rebuild logic;
- remove/cancel old missions and pointers before adding to the new responsible country;
- never re-run field initialization or add resources during migration.

Recommended policy from the specification’s ownership/control split:

- controller: guarding, suspension, access denial, emergency/occupation posture;
- legal owner: contracts, compensation, concessions, final commercial choices;
- actions that permanently remove the field ledger require owner and controller to coincide, or an explicit spec-approved settlement/transfer rule;
- transfer must trigger contract/rights review and mission cleanup.

### Exact add/remove helpers

Create one Event-owned deposit effect with explicit input type enum and amount. Because `add_resource.type` is a static token, use six explicit branches (or a documented meta effect only if architecture proves it safer). Each branch must:

1. call `add_resource` with the matching static type and dynamic amount;
2. increment only the matching Event 018 state ledger;
3. recompute total/distinct/largest values;
4. mark enrichment versus first discovery without adding a duplicate state record.

Closure/full seal must subtract each of the six recorded ledger values separately. Copy each value into a temporary variable, multiply the temporary variable by `-1`, then pass it to `add_resource`. Do not use unary `-variable`, do not remove the state’s total visible resources, and do not clear the ledger until its inverse operation has run once.

Vanilla exact inverse precedent: `common/ideas/czechoslovakia.txt:5924-5975`, where `CZE_bata_corporation` adds 6 rubber on add and removes exactly 6 on removal. Official effect docs confirm negative `add_resource` removes production.

Risk requiring a targeted scripted test during implementation: no vanilla precedent demonstrates removing a recorded mod-owned amount after an unrelated system has reduced the same state resource below that amount. The intended invariant is that Event 018 owns and reverses only its ledger. Do not silently clamp or leave a remainder as a fallback; if engine behaviour makes exact inversion unsafe, stop for design direction.

## 6. Entry selection, dispatcher, event log, and cluster integration

### Prefire context

Add a narrow Event 018 branch in `fire_event_by_temp_id_no_cluster` in `common/scripted_effects/chaosx_settings_effects.txt`, beside the Event 013/011/017 prefire branches:

1. set `resources_found_prefire_ready = 0`;
2. call `resources_found_prepare_random_event_fire`;
3. block `event_single_fire_allowed` when no valid actor/state exists;
4. preserve regular event targets for the selected actor and state through the dispatched `.1` chain.

The canonical `.1` should consume this context. A direct/manual `.1` may defensively prepare context when absent, but it must never select a second state after a valid prefire selection.

Selection must exclude at least closed/sealed states, the cave-origin state, invalid/impassable/ownerless states, nonhuman countries, and terminal/world-end conditions. It must support enrichment of an existing eligible field and discovery of a new eligible state according to the tuning matrix.

### Active pool and enable gate

- `common/scripted_effects/chaosx_logic_effects.txt:148-250`: Event 18 is already classified repeatable at line 205. Add a firing-availability branch to the active-pool calculation so Event 18 cannot be selected when preconditions are impossible.
- `common/scripted_triggers/chaosx_settings_triggers.txt:10-25`: Event 18 is intentionally absent from the reworked-default allowlist. Add it only after all required gameplay, UI, AI, assets, localisation, docs, workbook fields, audits, and terminal routes are complete.

### Event history payload

`events_log_set_default_actor_for_current_event` at `chaosx_events_log_effects.txt:178-341` has no Event 18 branch. Add one using the prepared field owner/controller actor.

The generic history record stores event ID/type/actor/secondary actor but not field state, resource type, or discovery/enrichment status. Event 018 requires all four. Follow Event 017’s history-sequence binding model:

- bind Event-owned parallel history arrays to `global.events_log_history_sequence` after the generic entry is created;
- store state ID/scope, primary resource type, amount/ledger summary, and new-versus-enrichment status;
- do not broaden every generic history entry with Event 018-only fields unless the shared architecture explicitly chooses a generic typed-payload system;
- clear pending payload flags/variables whether dispatch succeeds or is cancelled.

Add Event 18 detail localisation to `GetEventsLogEventDetailDescription` in `chaosx_scripted_localisation_events_log.txt` (currently it falls through to generic text), plus four evolution preview rows using `events_log_add_event_detail_evolution_preview` in `chaosx_events_log_effects.txt`.

### Economy-positive cluster

Create cluster ID 7, `economy_positive`, because the required catalog cluster does not exist. Required integration:

- `common/script_constants/event_cluster_constants.txt`: ID and tuning;
- `common/scripted_effects/chaosx_event_cluster_effects.txt`: definition, membership, severity/participation weight, cooldown state, candidate/loading paths, firing/marking branches, and details data;
- `common/scripted_localisation/chaosx_scripted_localisation_settings.txt`: name and settings selectors;
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`: log/detail selectors;
- `localisation/english/chaosx_gui_l_english.yml`: player-facing cluster text;
- event catalog workbook: matching cluster detail text.

Initial recommendation while Event 18 is the only implemented member: unlock 0, cooldown 120 days, Event 18 participation weight 100, medium severity. Treat these as architecture/tuning recommendations, not immutable values. Do not add unreworked future economy events merely to populate the cluster.

The existing cluster UI is data-driven; no geometry edit should be necessary unless implementation proves the label/layout exceeds the current dynamic list.

## 7. Decisions, missions, and scripted GUI

Use Event 013 as the primary multi-record GUI precedent:

- `common/scripted_guis/013_natural_disasters_scripted_gui.txt:11-176` for player context, card/detail state, and static/animated toggles;
- `interface/013_natural_disasters.gui:7` for layout;
- `common/decisions/013_natural_disasters_decisions.txt:65` for an opener decision;
- `common/scripted_effects/013_natural_disasters_effects.txt:6811-7246` for history/current arrays, unique state registration, view rebuild, and selected-index clamping.

Use state-target decision precedents:

- `common/decisions/001_communism_spread_decisions.txt:61`, `:148`, `:232` for `state_target = any_controlled_state`;
- `common/decisions/003_holy_realm_decisions.txt:3922`, `:3968`, `:4013`, `:4079` for `state_target = any_owned_state`;
- vanilla `common/decisions/AST.txt:114-178` for a working selectable state target with target/root triggers and state-scoped `FROM`;
- `common/decisions/010_death_decisions.txt:600-628` and `017_random_faction_decisions.txt:208-237` for mission activation/cancel/timeout lifecycles.

Implementation warning: vanilla decision documentation calls one field `state_trigger`, while working vanilla and the offline wiki use `state_target`; follow the working scripts. No vanilla example was found combining `state_target = yes` and `days_mission_timeout` in one block. If a timed field action needs both, validate that exact combination or separate selection from mission activation.

The compact GUI header must display/cycle the owner’s unique active-field list; AI must evaluate all fields directly rather than relying on the player’s selected index.

## 8. Transfer, resource rights, and border conflict

### Control/ownership changes

Use an Event-owned `on_state_control_changed` hook gated on an Event 018 state marker. Scope contract is `ROOT` new controller, `FROM` old controller, `FROM.FROM` state.

Primary repository precedents:

- `common/on_actions/013_natural_disasters_on_actions.txt:14-29` and `013_natural_disasters_effects.txt:4264-4535` for transfer-context capture, old mission/array cleanup, new registration, and state-control handling;
- `common/on_actions/017_random_faction_on_actions.txt:180-183` for saving `FROM.FROM` and routing old-controller cleanup;
- `common/on_actions/010_death_on_actions.txt:6-13` for a marker-gated control hook.

Never use a global daily/monthly world iterator to find transfers.

### Resource rights

Store contract grantor, receiver, state, resource set, start/end/status, and transfer-review status. Rights provide resources only while the grantor controls the state, so control changes must suspend/review/regrant rather than assuming continuity.

Vanilla precedents:

- `events/NSB_Soviet.txt:5072-5130` grants SOV resource rights in state 618;
- `events/NSB_Soviet.txt:6441-6469` removes them with `remove_resource_rights = 618`;
- official effect docs at `give_resource_rights` and `remove_resource_rights`;
- the offline Effects page notes the control requirement.

Chaos Redux has only a static bespoke precedent in `common/decisions/005_soviet_collapse_decisions.txt:12986-13021`; it is not reusable infrastructure. Do not grant contracts to `DHO` or any actual nonhuman country.

### Border conflicts

Do not reuse `events/078_border_war.txt` as infrastructure. It hardcodes province IDs, uses `change_state_after_war = yes`, and owns its own callbacks. It does not satisfy the specification’s conditional reuse clause.

Use these patterns instead:

- `common/scripted_effects/008_tensions_rising_effects.txt:1171-1253` for stored actor/state pairs, validity checks, callbacks, and `change_state_after_war = no`;
- `common/scripted_effects/011_secret_alliance_effects.txt:4294-4445` for dynamic preparation, confirmation, cancellation, and cleanup;
- vanilla `common/decisions/WTT_border_conflicts.txt:363-694` for start, timeout cancellation, escalation, conversion to war, and manual finalization.

Event 018 must store the exact field state, adjacent combat state, claimant, and active-conflict marker. Use `change_state_after_war = no`; the success callback explicitly transfers the intended field state, then invokes the ordinary Event 018 transfer handler so ledger, contracts, missions, GUI arrays, and history stay coherent. Cancel/invalid paths clear every stored reference and marker.

The field must actually border a valid claimant-controlled state. If not, the border-war route is unavailable; do not substitute a remote border conflict.

## 9. Civilian deaths and shared cause tracking

Use the shared state-death helper `chaos_meter_register_state_civilian_deaths_percent`, as Event 013 does around `013_natural_disasters_effects.txt:3288-3380`. Capture its `chaos_deaths_change` output for field-level death totals and achievement history.

Add a dedicated `resource_field_incident = 15` cause. This requires coordinated shared updates to the cause constants, cause aggregation/storage arrays, sanitization/view sync, scripted localisation, and GUI localisation. Reusing “natural disaster” would be a misleading fallback and is not acceptable.

## 10. Cave country, forces, anchors, and continent logic

### Setup and focus loading

Use fixed-tag setup based on:

- `common/scripted_effects/010_death_effects.txt:274-365`, `death_setup_country` and cleanup;
- `common/countries/Death.txt`;
- `history/countries/DTH - Death.txt`;
- `common/characters/DTH.txt`;
- `common/national_focus/010_death_focus_tree.txt`;
- `common/units/010_death_ghost_hosts.txt`;
- `common/scripted_effects/005_soviet_collapse_effects.txt:8926-9049` for guarded focus loading on event-created incarnations.

At emergence, load `018_resources_found_cave_focus_tree` with `keep_completed = no` only for the Event 018-created `DHO` incarnation. The 45–65 focus package must implement the three hierarchy routes and three doctrine routes in the supplied graph; it is not complete if replaced by a generic tree.

### Nonhuman classification

Extend:

- `is_special_chaos_country` in `common/scripted_triggers/chaosx_dynamic_triggers.txt:101-122`;
- `is_actual_nonhuman_country` at lines 124-137;
- documentation in `common/scripted_triggers/chaosx_dynamic_triggers.md`.

Check both `original_tag = DHO` and an Event-owned cave-country marker so cosmetic/lifecycle states remain classified. `uses_normal_civilian_systems` will then exclude DHO automatically.

### Units and recruitment

Primary patterns:

- `002_zombie_outbreak_effects.txt:1779-1802` for locking templates;
- `010_death_effects.txt:1315+` for individually locked special templates;
- vanilla `common/scripted_effects/ETH_scripted_effects.txt:581-615` for deleting/recreating a locked template and dynamic `create_unit.count`;
- official `create_unit` and runtime division-template documentation.

No vanilla land subunit without both equipment `need` and `essential` was found. Even `fake_intel_unit` needs one equipment. Therefore the specification’s truly equipmentless combat subunit is an engine-risk area, not a proven vanilla pattern. Implement it in an Event-owned `common/units` definition with `manpower = 0` and no equipment need only after a focused schema/runtime precedent check. Do not quietly give it infantry equipment as a fallback.

Do not add a new equipment archetype: the specification says no equipment, and a bespoke subunit is sufficient if supported. Consequently, `common/script_enums.txt` should not change. If architecture later adds equipment, that decision changes the scope and requires `script_enum_equipment_bonus_type` integration.

DHO must not recruit/train normal divisions. Lock all templates and generate only scripted cave hosts. Do not force-allow the template for player recruitment merely because the zombie precedent does so. Validate whether a zero template cap blocks scripted `create_unit`; use the least invasive proven lock/cap combination.

### Spawn capacity

- emergence creates 6–30 opening divisions from exploitation history;
- each captured non-origin state becomes an anchor only after 30 continuous days of DHO ownership and control;
- contribution is `floor(total six standard state resources / 10)`, capped at 10;
- store the contribution when the anchor matures unless the final architecture explicitly defines recalculation;
- origin state never contributes;
- sum active anchor contributions into total brood capacity;
- spawn sequentially through a paced queue; never create the whole deficit in one tick;
- loss of capacity applies the overcapacity debuff and does not delete divisions.

Use a narrow `on_daily_DHO`, following `common/on_actions/010_death_on_actions.txt:19-23`, for 30-day maturation, paced spawning, and new-neighbour refresh. This is tag-specific and does not violate the prohibition on global daily iteration. Use `on_state_control_changed` to reset/start state timers and trigger immediate adjacency updates.

### Neighbor wars

Official/vanilla patterns prove dynamic neighbor discovery and subsequent war, but no single blanket `every_neighbor_country = { declare_war_on = ... }` block was found. Build a two-stage helper: collect/validate current land neighbors, then declare or create the intended war relation one target at a time. Re-run after territorial changes and exclude allies, subjects, DHO itself, invalid/nonexistent targets, and already-shared wars.

### Continent terminal progress

Store the origin continent at emergence. Define the eligible-state predicate explicitly: same continent, valid land state, not impassable, not the removed/terminal exception set, and has a legitimate owner/controller. Terminal progress requires DHO to both own and control every eligible state.

Vanilla achievement precedent uses `all_state` with an OR filter to ignore states outside the target set while requiring control inside it (`common/achievements.txt:2478-2503`). Event 018 may use the same idiom or maintain validated eligible/controlled counts. Do not infer continent completion from state count alone without applying the exact eligibility predicate.

The world-end gate also requires chaos strictly greater than 1000, no prior `world_end`, no disabled terminal state, and a delayed verification event to prevent same-chain ownership/control races.

## 11. World threat, terminal routes, and cleanup

Add `world_threat_source_resources_found_caves` to:

- `common/scripted_triggers/chaosx_world_threat_triggers.txt`;
- `refresh_world_threat_state` in `common/scripted_effects/chaosx_dynamic_effects.txt:462-493`;
- `common/scripted_effects/chaosx_dynamic_effects.md`.

Create an Event-owned refresh effect that sets/clears its source then calls the shared aggregate refresh. Follow `death_refresh_world_threat_source` at `010_death_effects.txt:842+`.

Terminal precedents:

- `010_death_effects.txt:2754-2805` for defeat detection/cleanup;
- `010_death_effects.txt:2807-2994` for world end, shared terminal flags, super-event, and footholds;
- `010_death_on_actions.txt:25` and `:53`, plus corresponding effects at `:3037-3072`, for puppet/capitulation cleanup.

Required Event 018 terminal behaviour:

- full seal prevents Evolution IV and clears/suspends all Event 018 paths exactly as specified;
- cave emergence sets the Event 018 threat source and fires display slot 82/audio 54;
- cave world end uses slot 83/audio 55 only after delayed terminal verification;
- global cave defeat uses slot 84/audio 56 when the global or near-global history gate is met;
- defeat clears the Event 018 threat source, all DHO timers/queues/targets, wars/contracts/temporary modifiers, and terminal-only UI state;
- cross-continent footholds are resource-weighted and follow the spec, not a generic random-state fallback.

## 12. Super-event, achievement, and asset registries

### Super-events

Reserve:

| Meaning | Display slot | Audio ID |
|---|---:|---:|
| Cave emergence | 82 | 54 |
| Cave world end | 83 | 55 |
| Global cave defeat | 84 | 56 |

Shared files to merge carefully:

- `interface/chaosx_super_events.gfx`;
- `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`;
- `sound/chaosx_sound.asset`;
- `sound/chaosx_sound.asset`;
- `sound/chaosx_sound.asset`;
- `localisation/english/chaosx_music_l_english.yml`;
- `music/chaosx_music_track_list.html`;
- `docs/super_events/super_event_audio_packages.md`.

Use script constants and `global.current_super_event_audio_id`, with the settings-aware shared playback wrapper. Each super-event requires unique 457×328 art, researched quotation/source notes, a licensed/sourced 44.1 kHz audio package, WAV registrations, localisation, and documentation. Do not reuse the default super-event image or audio.

### Achievements

Implement all 15 concepts in the prompt, in this order, using stable `018_resources_found_*` semantic IDs:

1. One Vein to Rule the Market
2. The Whole Periodic Table, Figuratively
3. Every Worker Came Home
4. Seal It While We Still Can
5. Contract of the Century
6. No Claims Left Unsettled
7. Thirty From Below
8. The Last Shaft Closed
9. Ten From One State
10. No Men, No Guns
11. The Moving Mountain
12. The Front Has a Floor
13. The Hills Begin to Move
14. Continental Appetite
15. The Ground Is Quiet Again

Wire one section in `common/achievements/chaos_redux_achievements.txt`, sprite aliases in `interface/chaosx_achievements.gfx`, localisation in `chaosx_achievements_l_english.yml`, and three 64×64 DDS files per achievement in root `gfx/achievements/` (45 files total). Preserve current dirty achievement edits. Follow `docs/systems/custom_achievements.md`.

### Asset inventory (historical planning baseline)

At the time of this map, no Event 018 asset package existed. The Event 018 asset prompt required at least:

- 10 report images (210×176);
- 6 news images (397×153);
- 3 super-event images (457×328);
- cave leader portrait and 8–12 real source animation frames;
- base and world-end flags in all required sizes;
- six-state field GUI family, with five animated/static pairs;
- decision/category icons;
- 16 idea icons;
- the complete 45–65 focus-tree icon family;
- 45 achievement DDS variants;
- unit/commander assets;
- source images, processed PNGs, final DDS/TGA, manifests, contact sheets, previews, static fallbacks, and `.gfx`/`.gui` handoff notes.

Pre-register stable filenames and sprite IDs before asset production. For animations follow `interface/013_natural_disasters.gfx` (`frameAnimatedSpriteType`, frame count, FPS, loop, static fallback) and the frame-animation skill: final animation must use distinct planned source frames, not transformed copies of one still.

## 13. Minimal shared-file edit set

The implementation should concentrate feature logic in Event-owned files. The following shared edits are the minimum expected integration surface; some may be grouped by tranche, but none can be omitted from a complete implementation.

| Shared file/surface | Minimal Event 018 edit |
|---|---|
| `common/scripted_effects/chaosx_logic_effects.txt` | Availability exclusion in the active repeatable pool; retain repeatable classification. |
| `common/scripted_effects/chaosx_settings_effects.txt` | Event 18 prefire preparation/block branch only. |
| `common/scripted_triggers/chaosx_settings_triggers.txt` | Add 18 to the completed/reworked default allowlist last. |
| `common/script_constants/event_cluster_constants.txt` | Cluster ID 7 and tuning. |
| `common/scripted_effects/chaosx_event_cluster_effects.txt` | Cluster 7 definition, membership, runtime/cooldown/detail integration. |
| cluster scripted localisation and `chaosx_gui_l_english.yml` | Economy-positive selectors/text. |
| `common/scripted_effects/chaosx_events_log_effects.txt` | Event 18 actor/payload integration and four evolution previews. |
| `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` | Event detail, payload, evolution, and cluster text selectors. |
| `localisation/english/chaosx_event_names_l_english.yml` | Rename key 18 to final “Resources Found” wording. Existing name selectors already reference key 18. |
| `events/_chaosx_news.txt` | Register the final Event 018 news events/images; preserve `chaosx.news.20` only if retained by the final chain. |
| `common/scripted_triggers/chaosx_dynamic_triggers.txt` and `.md` | DHO special/nonhuman classification and docs. |
| `common/scripted_triggers/chaosx_world_threat_triggers.txt` | Event 018 cave threat source. |
| `common/scripted_effects/chaosx_dynamic_effects.txt` and `.md` | Aggregate Event 018 threat source; add/document a generic helper only if architecture truly reuses it. |
| shared chaos-meter constants/effects/scripted localisation/GUI loc | Cause 15, aggregation, view sync, and player-facing incident-death text. |
| `common/country_tags/chaosx_countries.txt` | Register `DHO`. |
| shared country/party name localisation | DHO country forms and parties. |
| shared super-event GFX/scripted loc/sound/catalog/docs | Slots 82–84 and audio 54–56. |
| shared achievement registry/GFX/localisation/docs | Fifteen semantic IDs and icon triplets. |
| `docs/spreadsheets/chaos_redux_events_catalog.xlsx` | Final Event 18 event/evolution/cluster/detail alignment after implementation. |

Files that should **not** change under the recommended architecture:

- `common/script_enums.txt`, because no new equipment type is proposed;
- `events/078_border_war.txt`, because it is not reusable infrastructure;
- a global daily/monthly on-action file, because Event-owned marker hooks and `on_daily_DHO` are sufficient;
- generic settings/events-log GUI geometry, unless a measured layout defect proves a change is needed.

## 14. Vanilla and Chaos Redux precedent index

| Need | Primary precedent |
|---|---|
| Exact resource add/remove | Vanilla `common/ideas/czechoslovakia.txt:5924-5975`; effects docs `add_resource`. |
| Resource rights lifecycle | Vanilla `events/NSB_Soviet.txt:5072-5130`, `:6441-6469`. |
| Dynamic border war | Vanilla `common/decisions/WTT_border_conflicts.txt:363-694`; Event 008/011 effects. |
| State-target decision | Vanilla `common/decisions/AST.txt:114-178`; Event 001/003 decisions. |
| Mission lifecycle | Event 010 decisions `:600-628`; Event 017 `:208-237`. |
| State-control hook | Vanilla `common/on_actions/12_wuw_on_actions.txt:2575-2639`; Event 013/017 hooks. |
| Multi-record state GUI | Event 013 scripted GUI/effects/GUI. |
| Dynamic locked template/unit count | Vanilla `ETH_scripted_effects.txt:581-615`; Event 002/010 units. |
| Runtime focus load | Vanilla `events/France.txt:983-991`, `events/BFTB_Greece.txt:3212-3225`; Event 005/010 effects. |
| Dynamic neighboring war | Vanilla `events/WTT_PRC.txt:802-932`, communist China focus `:1512-1552`. |
| Continent all-state gate | Vanilla `common/achievements.txt:2478-2503` and official `all_state`/`is_on_continent` docs. |
| Achievement registry | Chaos Redux root registry/docs; offline custom-achievement wiki requirements. |
| World threat lifecycle | Event 010 Death source/defeat/world-end effects. Vanilla has no generic equivalent. |
| Tag-specific pulse | `common/on_actions/010_death_on_actions.txt:19-23` (`on_daily_DTH`). |
| Frame animation registration | `interface/013_natural_disasters.gfx`. |

## 15. Implementation order and ownership boundaries

### Tranche 1 — reservations and architecture

1. Re-scan `DHO`, cluster 7, evolution 18, super slots 82–84, audio 54–56, achievement semantic IDs, and death cause 15 against the then-current dirty worktree.
2. Freeze final internal names, field record schema, owner/controller policy, contract lifecycle, and terminal eligibility predicate in an architecture handoff/spec addendum.
3. Obtain final cave country/leader/party naming direction before player-facing package completion.

### Tranche 2 — baseline field system

1. Add Event-owned constants, triggers, effects, exact ledger helpers, field selection, prefire context, history payload, and transfer handler.
2. Replace `.1/.2` with first-discovery and enrichment flow.
3. Add baseline decisions/missions, compact GUI, AI evaluation, dynamic modifiers, localisation, report/news images, and exact closure.
4. Validate duplicate-state enrichment, two simultaneous fields, owner/control transfer, suspension, closure, and exact ledger removal.

### Tranche 3 — economy and escalation

1. Add contracts/rights, smuggling/espionage, commission, demilitarization, staged border conflict, and transfer cleanup.
2. Implement Evolutions I–III, incident deaths, containment, evacuation, and full seal.
3. Bind all event/evolution history and Event Details content.

### Tranche 4 — cave country

1. Build DHO history/country/character/ideas/AI/focus/unit/flag/portrait package.
2. Implement emergence, 6–30 initial forces, anchor maturation, capacity contribution, sequential spawning, overcapacity debuff, neighbor wars, anti-cave responses, and focus mechanics.
3. Add nonhuman classification and world threat.
4. Implement continent gate, >1000 chaos requirement, delayed world-end verification, cross-continent footholds, and defeat cleanup.

### Tranche 5 — presentation and registries

1. Produce/wire the complete asset manifest, animations/static fallbacks, report/news/super-event art, flags, portraits, ideas, decisions, focuses, units, and 45 achievement files.
2. Complete super-event text/audio research and register slots/audio.
3. Implement all 15 achievements with route history/disqualifiers.
4. Finish shared name/cluster/log selectors, docs, and workbook alignment using final in-game localisation wording.

### Tranche 6 — audits and enablement

Run the custom decision/mission, country-package, focus-tree, localisation, and event-completion auditors. Resolve every missing route, AI behaviour, asset, log row, workbook field, or terminal cleanup issue. Only then add Event 18 to the default reworked-event allowlist and create the plan commit(s).

Main-agent ownership:

- final architecture choices;
- all shared-file merges;
- gameplay/localisation/GFX wiring;
- reviewing subagent assets/research/audits;
- validation and completion claim.

Subagent-safe bounded work after architecture freezes identifiers:

- super-event text/audio research;
- generated/sourced art and icon production through the asset skills;
- focus/decision/country/localisation/event-completion audits;
- workbook/doc alignment after implementation facts exist.

## 16. Required validation scenarios

The implementation is not complete until it exercises the specification’s scenarios, especially:

- baseline discovery with a valid actor/state and no eligible-state case;
- repeat enrichment in the same state without duplicate records;
- multiple fields and selected-index cycling;
- owner/controller transfer with missions, contracts, rights, UI arrays, and history intact;
- border conflict success, loss, timeout, invalidation, and cleanup;
- Evolution II deaths using the correct shared cause;
- full seal exact six-ledger removal and Evolution IV prevention;
- initial cave force results at exploitation extremes, including max 30;
- anchor contribution totals 0, 9, 10, 48, 100, and over 100, including cap/floor behaviour;
- 30 continuous days reset on loss of owner/control;
- sequential spawning and capacity-loss debuff without division deletion;
- no cave manpower/equipment/training/trade/faction/navy/air escape paths;
- current and newly created neighbor wars;
- all three hierarchy and all three doctrine focus routes;
- continent owned-and-controlled eligibility with chaos strictly above 1000;
- delayed world-end verification and no duplicate terminal firing;
- DHO defeat, threat cleanup, aftermath, achievements, Event Details, cluster, docs, and workbook parity.

## 17. Open blockers and architecture decisions

These are genuine unresolved decisions or engine-risk items; they must not be hidden behind fallbacks:

1. final DHO country name, leader identity/name/presentation, party names, and ideology forms;
2. exact owner-versus-controller authority for irreversible closure and contracts;
3. whether anchor resource contribution snapshots on maturation (recommended) or recalculates dynamically;
4. the final eligible-state predicate for continent completion and exceptions;
5. engine support/behaviour for a truly equipmentless land subunit with no `need`/`essential` entry;
6. behaviour of exact negative `add_resource` if another system has reduced the visible resource below the Event 018 ledger;
7. global-defeat super-event eligibility remains conditional on global or near-global history; slot 84/audio 56 are reserved for it;
8. final research-backed quotes and licensed audio sources for all retained super-events;
9. exact unit statistics, spawn pacing, AI weights, and economy-positive cluster tuning after scenario balance tests;
10. later Event 018 breach behaviour when a DHO country already exists elsewhere.

No simplification or fallback is authorized by this map. If any blocker prevents the full specified behaviour, implementation must stop for design direction and report the goal incomplete.
