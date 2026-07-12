# Repo Explorer Handoff

> Superseded exploration snapshot. This file records the repository state before Event 014 implementation. It is retained for provenance and must not be used as current implementation status. Current facts live in `docs/specs/014_cannibalism_specs/`, `docs/events/014_cannibalism.md`, and the final reconciliation handoffs.

## Scope read

This is a read-only implementation map for Event 014, Cannibalism. It does not
change gameplay, localisation, UI, assets, or the event workbook.

The exploration covered:

- every file in `docs/specs/014_cannibalism_specs/`, including the twelve-part
  source specification, matrices, focus graphs, asset inventory, acceptance
  criteria, anti-spoiler audit, research, and orchestration prompts;
- `docs/assets/014_cannibalism/manifest.md` and the actual source, processed,
  animation, DDS, flag, portrait, event-picture, idea, achievement, and
  super-event files currently present in the repository;
- the Event 014 row and relevant scenario/cluster rows in
  `docs/spreadsheets/chaos_redux_events_catalog.xlsx`;
- the shared event registry, settings dispatcher, event log, evolution log,
  event-details UI, triggerable-scenario registry, super-event framework,
  achievement framework, Deaths API, Chaos Meter API, world-threat API,
  special-country classifications, and the existing Wendigo package;
- existing Event 002, 005, 007, 008, 010, 011, 013, 017, and 018 patterns;
- the offline wiki core pages required by `AGENTS.md`: Data structures,
  Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event
  modding, Decision modding, Idea modding, and AI modding;
- the offline wiki pages for Interface Modding, Scripted GUI Modding, Country
  creation, National focus modding, Division modding, Technology modding,
  Achievement modding, Sound modding, and Music modding;
- relevant official files under the installed game's `documentation/`,
  including `script_concept_documentation.md`, `effects_documentation.md`,
  `triggers_documentation.md`, `modifiers_documentation.md`, dynamic-variable
  documentation, localisation object/formatter documentation, and
  `common/script_constants/documentation.md`;
- installed vanilla country tags and vanilla implementations of
  `change_tag_from`, `create_dynamic_country`, `load_focus_tree`, country
  annexation with troop transfer, national-focus selection, decisions,
  characters, units, technologies, achievements, and audio registration.

## Primary findings

### 1. Event 014 is reserved, but it is not implemented or dispatchable

- There is no `events/014_cannibalism.txt`, no `chaosx.nr14` event namespace,
  and no Event 014 gameplay subsystem.
- `common/scripted_effects/chaosx_logic_effects.txt:148-249` skips ID 14 in
  both the fire-once and repeatable event-category lists. The event is
  therefore absent from `global.all_events`, not merely disabled by a setting.
- `common/scripted_triggers/chaosx_settings_triggers.txt:10-25` already treats
  ID 14 as a default-enabled reworked event. Once registered, it should follow
  the normal event settings contract.
- `localisation/english/chaosx_event_names_l_english.yml:16` still exposes
  `chaosx.event_name.14: "Event 014 Placeholder"`.
- The workbook row is likewise a removed/reserved placeholder. There is no
  actor mapping, no detail view, no evolution mapping, no category membership,
  no auto-fire eligibility, and no manual-dispatch context.
- The specification intentionally gives Event 014 no event cluster. Do not add
  it to a cluster as a substitute for registering it as a standalone fire-once
  event.

### 2. Two global-ID collisions must be handled explicitly

#### Triggerable scenario

- The specification proposes scenario ID 8, but
  `common/script_constants/chaosx_triggerable_scenarios_constants.txt:9-24`
  already assigns ID 8 to `africa_is_one` and ID 9 to
  `coalition_unmasked`.
- `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt:58-135`
  registers those IDs and the GUI/selection/launch code assumes the registry is
  unique.
- `docs/systems/triggerable_scenarios.md:97-103` also reserves SCN008 for
  Africa Is One and documents SCN009 as Coalition Unmasked.
- A concurrent, currently untracked draft at
  `common/script_constants/014_cannibalism_scenario_constants.txt` assigns the
  Cannibalism scenario registry ID **10**. ID 10 is the correct next free
  integer in the inspected registry, but that draft is not registration or
  implementation by itself. The parent should preserve IDs 8 and 9 and wire 10
  consistently through every scenario selector.

#### Super events

- The current registered super-event space contains 1-22, 51, and 59-77.
- Super-event ID 51 is already the Holy Realm's **Mandala of Nations**:
  `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`
  maps it and `localisation/english/003_the_holy_realm_l_english.yml:898-901`
  provides the text.
- Concurrent Event 014 audio uses proposed IDs 49, 50, 51, and 52. ID 51 must
  not be reused. IDs **49, 50, 52, and 53** were free at inspection time, so a
  safe assignment is reveal 49, ordinary world end 50, defeat/aftermath 52,
  and Wendigo-Hannibal world end 53. The authoritative super-event constants,
  sprite selectors, localisation selectors, music/sound registrations, and
  filenames must all use the same final assignment.

### 3. The existing Wendigo is a dynamic ZZZ-derived country, not a fixed tag

The Event 014 crossover must extend the canonical Event 002 Wendigo package.
Creating a second fixed-tag approximation would lose gameplay systems and is
not an acceptable fallback.

Canonical contract:

- `common/scripted_effects/zombie_special_project_effects.txt:2412-2451`
  defines `initialize_wendigo_incident_outbreak_country`.
- `common/scripted_effects/zombie_special_project_effects.txt:2453-2488`
  defines `spawn_wendigo_incident_from_completion`.
- The country is created dynamically with `original_tag = ZZZ` and
  `copy_tag = ZZZ`.
- Identity flags include
  `zombie_outbreak_dynamic_country`,
  `weaponized_zombie_outbreak_country`,
  `weaponized_zombie_type_wendigo`,
  `weaponized_zombie_archetype_wendigo`,
  `weaponized_zombie_attack_other_zombies`, and
  `weaponized_zombie_independent_outbreak`; the shared global marker is
  `weaponized_zombie_wendigo_exists`.
- `weaponized_zombie_refresh_country_leader` at approximately lines 2558-2569
  supplies the existing Wendigo leader and portrait
  `GFX_portrait_ZZZ_weaponized_wendigo`.
- The Wendigo template unlock at approximately lines 2635-2650 uses the
  `wendigo_zombies` subunit and the `"Wendigo Pack"` template. The subunit is
  defined in `common/units/zombies.txt:497+`; locked OOB templates live in
  `history/units/ZZZ_weaponized_1936.txt:181+` and its hardened counterpart.
- `common/ideas/zombie_weaponized_ideas.txt:544+` defines
  `weaponized_zombie_wendigo`; the terminal variant begins around line 565.
- `weaponized_zombie_copy_outbreak_profile` at approximately lines 2929-3008
  is the preservation precedent for the Wendigo identity flags.
- `common/scripted_effects/zombie_special_project_effects.txt:3011-3143`
  contains normal dynamic spawning, division creation, and the existing
  Wendigo super-event path.
- `trigger_wendigo_super_event` at lines 3839-3866 uses existing super-event
  ID 6; `events/002_zombie_outbreak.txt:884-901` owns terminal
  `world_end_wendigo` behavior.

Event 014 should find an existing live Wendigo by country existence,
ZZZ-derived/dynamic identity, Wendigo type/archetype flags, and meaningful
territory or units. The global marker alone can be stale. At convergence it
should preserve all Event 002 identity flags, recruitment, templates, OOB,
technology/counterstrain hooks, ideas, and world-end readiness; then add the
Hannibal character, portrait, focus overlay, Event 014 variables, and cosmetic
identity. If the player controls the Wendigo, that country remains the merge
host.

### 4. The Deaths API already owns exact state-population removal

- `common/scripted_effects/chaos_meter_effects.txt:2421-2487` defines
  `chaos_meter_register_deaths`.
- For an exact one-time consumption from state scope, set a positive person
  count in `chaos_deaths_change`, assign `chaos_deaths_reason`, set
  `chaos_deaths_is_civilian = 1`, set `chaos_deaths_apply_state_pop = 1`, set
  `chaos_deaths_target_country = OWNER`, set
  `chaos_deaths_has_target_country = 1`, and call
  `chaos_meter_register_deaths`.
- At approximately lines 2489-2495 the API applies the corresponding negative
  state manpower change and updates state deaths. Event 014 must not also call
  `add_manpower` or `modify_state_population_by_percent` for the same people,
  or the population will be removed twice.
- `common/scripted_effects/010_death_effects.txt:394-403`
  (`death_register_consumed_population_deaths`) is the nearest exact precedent.
- The generic percent wrapper
  `chaos_meter_register_state_civilian_deaths_percent` at approximately
  `chaos_meter_effects.txt:3198-3315` includes randomisation/caps and is not a
  safe replacement for an exact Larder transaction without an explicit design
  change.
- `common/script_constants/chaos_meter_constants.txt:363-383` currently ends
  the death-reason table at ID 14 (`natural_disaster`). A dedicated
  `cannibalism` cause should use the next free reason and be wired through all
  per-country total initialisation/rebuild, sorted and unsorted cause arrays,
  aggregate selectors, history rows, scripted-localisation reason selectors,
  and `localisation/english/chaosx_chaos_meter_l_english.yml`. Reusing a
  semantically wrong cause is an unapproved fallback.

### 5. Use the shared Chaos and world-threat APIs

- `common/scripted_effects/chaos_meter_effects.txt:3998+` defines
  `add_chaos_meter_value`. Event 014 should set `chaos_change` and a dedicated
  history reason before calling it; if supplying an explicit history reason,
  set `chaos_history_reason_custom = 1` in the established pattern.
- `common/scripted_effects/chaosx_dynamic_effects.txt:462-493` defines
  `refresh_world_threat_state`. It counts source flags for zombies, the Holy
  Realm, Mengele, Fury, and Death and then owns `world_in_threat`.
- Event 014 needs one new source flag, for example
  `world_threat_source_cannibalism`, an Event 014 refresh effect that sets or
  clears it from actual network/warlord/Hannibal state, and one count branch in
  `refresh_world_threat_state`.
- Add the matching shared trigger to
  `common/scripted_triggers/chaosx_world_threat_triggers.txt` and update
  `docs/systems/world_threat_mechanic.md`.
- Do not create an Event 014-only parallel “world cooperation” boolean. The
  specification calls for the shared threat/cooperation contract.

### 6. Special-country classification is the cross-event integration point

- `common/scripted_triggers/chaosx_dynamic_triggers.txt:101-121` defines
  `is_special_chaos_country`. Add Event 014 human warlord and united-host
  identification here using stable country flags and/or original fixed tags.
- `common/scripted_triggers/chaosx_dynamic_triggers.txt:124-136` defines
  `is_actual_nonhuman_country`. Only a transformed Wendigo-Hannibal country
  belongs here; ordinary human cannibal warlords do not.
- `uses_normal_civilian_systems` at lines 139-141 inherits the nonhuman
  classification.

Those shared predicates already protect Event 014 countries from several
unrelated random systems:

- Event 008 actor/world-tension selection:
  `common/scripted_triggers/008_tensions_rising_triggers.txt:36-46`;
- Event 011 alliance founder/member/target selection:
  `common/scripted_triggers/011_secret_alliance_triggers.txt:10-28`;
- Event 017 random-faction selection:
  `common/scripted_triggers/017_random_faction_triggers.txt:10-20,74-86`;
- Event 018 resource-contract and claimant selection:
  `common/scripted_triggers/018_resources_found_triggers.txt:91-103,126-133`.

Event 004 Random War and any other selector that does not use the shared
predicate still needs a direct eligibility audit. Event 007 Fury countries may
remain valid Event 014 origin hosts only while they are ordinary human
countries, as required by the Event 014 specification.

### 7. The asset manifest describes outputs that are not actually wired

The current `docs/assets/014_cannibalism/manifest.md` cannot be used as proof
of implementation. It claims several live outputs that were absent at
inspection time:

- `interface/014_cannibalism.gfx`;
- `interface/014_cannibalism_frontline_hunger.gui`;
- `common/scripted_guis/014_cannibalism_scripted_gui.txt`;
- `gfx/interface/animated/014_cannibalism/`;
- `gfx/interface/decisions/014_cannibalism/`;
- `gfx/super_events/014_cannibalism/`;
- `gfx/leaders/014_cannibalism/CBL_table_council.dds`.

Material actually present:

- 14 Event 014 event/news DDS files under
  `gfx/event_pictures/014_cannibalism/`;
- 18 idea DDS files under `gfx/interface/ideas/014_cannibalism/`;
- `gfx/leaders/014_cannibalism/hannibal.dds` and
  `hannibal_wendigo.dds`; the manifest identifies the ordinary Hannibal image
  as protected source art;
- one tracked Wendigo-Hannibal super-event DDS, currently misplaced under
  `gfx/super_events/002_zombie_outbreak/super_event_wendigo_hannibal.dds`;
- source/processed art for four super-event directions under
  `docs/assets/014_cannibalism/`, but not four correctly converted and wired
  runtime DDS files;
- six legitimate eight-frame animation packages with source frames,
  processed frames, sheets, GIF previews, contact sheets, and static material
  under `docs/assets/014_cannibalism/`; none has a live runtime DDS sequence or
  `.gfx`/GUI definition yet;
- partial CBL and `CBL_LAST_TABLE` flag sets. Medium and small variants are
  substantially present; the large/root set is incomplete.

All 37 tracked Event 014 focus-icon DDS files under
`gfx/interface/goals/014_cannibalism/` are deleted in the current dirty
worktree. Their deletion belongs to concurrent/user work and must not be
silently restored or committed by an Event 014 gameplay tranche. The parent
must resolve ownership before focus wiring can be considered complete.

The achievement asset set is also stale relative to the specification. The
repository has 13 old triplets (39 DDS files) with names such as
`clean_mess`, `silent_island`, `hunger_of_hannibal`, and `after_the_feast`.
Part 11 specifies 18 achievements with a different internal contract. The
final implementation therefore needs an approved mapping or a regenerated
complete 18-by-three sprite set; the old 13 cannot be declared complete by
renaming localisation alone.

### 8. Fixed tags have a viable allocation, but country packages do not exist

The repository, installed vanilla tags, and approved reference set were
checked for collisions:

- `CBA` through `CBH` are free and form a coherent eight-slot warlord range;
- `CBL` is free and is already the intended unified identity in the existing
  flag/asset material;
- no fixed Wendigo tag is needed or recommended because the actual Wendigo is
  dynamic and ZZZ-derived.

The likely package is therefore CBA-CBH for fixed warlord slots and CBL for the
ordinary united host. Register each fixed tag in a dedicated Event 014 tag
file, create the matching `common/countries/` and `history/countries/` files,
and provide complete flags, characters, leaders, AI, OOB/templates, and
localisation. The transformed Wendigo route should retain the dynamic country
and apply an Event 014 cosmetic tag only if a complete cosmetic flag and
localisation set is supplied.

### 9. Player transfer has a vanilla-safe ordering contract

There is no repository precedent for `change_tag_from`, so the official
effects documentation and vanilla are authoritative here.

- `documentation/effects_documentation.md:2663-2670` documents
  `change_tag_from` as changing the player from another country to the current
  country.
- Vanilla `events/LaR_France.txt:3995-4004` first scopes the future host,
  checks whether `FROM` is human, executes `change_tag_from = FROM`, and only
  then annexes `FROM` with `transfer_troops = yes`.

For Hannibal convergence, persist the chosen source and host as event targets,
prefer the human country when the specification allows it, and execute on the
host in this order:

1. copy or transfer persistent Event 014 state and achievement progress;
2. if the source is human, call `change_tag_from = event_target:<source>` from
   the host scope;
3. annex the source with `transfer_troops = yes`;
4. reconcile states, units, stockpiles, characters, ideas, focus-tree state,
   wars, factions, puppets, and Event 014 arrays/targets;
5. clear old slot references only after the host is fully valid.

If the player is the Wendigo, Wendigo remains the host. Do not annex or delete
the player-controlled country before `change_tag_from`, and do not rely on a
fixed-tag swap for the dynamic Wendigo route.

## Relevant files

| System | Existing file(s) | Parent implementation touchpoint |
|---|---|---|
| Event constants | `common/script_constants/` | Add `014_cannibalism_constants.txt` for event ID 14, stages, evolution IDs, route IDs, thresholds, costs, cooldowns, pulse delays, balance tables, tag-slot counts, death/chaos reasons, and super-event IDs. Keep scenario constants separate if the current draft is retained. |
| Event registration | `common/scripted_effects/chaosx_logic_effects.txt` | Register ID 14 exactly once as a fire-once event; add valid-origin eligibility to `evaluate_random_event_active_pool_candidate`. |
| Settings/manual dispatch | `common/scripted_effects/chaosx_settings_effects.txt:1639-1697,4542-4677` | Add Event 014 prefire context selection, manual-trigger handling, and safe abort when no wartime origin exists. Preserve the generic `chaosx.nr[ID].1` dispatch and fire-once bookkeeping. |
| Settings eligibility | `common/scripted_triggers/chaosx_settings_triggers.txt` | Default-enabled status already includes ID 14; add only Event 014-specific eligibility if the shared contract needs it. |
| Event script | `events/` | Add `014_cannibalism.txt` with namespace, visible entry event `chaosx.nr14.1`, hidden pulses, evolution/reveal/merge/aftermath events, and self-scheduling. Do not use broad daily/weekly/monthly on-actions. |
| Event effects | `common/scripted_effects/` | Add `014_cannibalism_effects.txt`: origin selection, network state, larder/death transactions, containment, spread, warlords, Hannibal identity/reveal, convergence, merge, Wendigo crossover, world end/defeat, achievement hooks, cleanup, and scenario setup. |
| Event triggers | `common/scripted_triggers/` | Add `014_cannibalism_triggers.txt`: valid origin/state, host status, route locks, evolution readiness, larder eligibility, Death exclusion, anti-spoiler visibility, merge readiness, world-end readiness, cleanup, AI, and GUI can-click/cost predicates. |
| Dynamic helpers | `common/scripted_effects/chaosx_dynamic_effects.txt` and `.md` | Reuse existing helpers first. Add only genuinely reusable country-selection/merge helpers; document purpose, scope, inputs, defaults, outputs, side effects, and example in the companion markdown. Extend shared world-threat counting here. |
| Shared classification | `common/scripted_triggers/chaosx_dynamic_triggers.txt` | Add human Event 014 special-country classification and transformed Wendigo nonhuman classification. |
| World threat | `common/scripted_triggers/chaosx_world_threat_triggers.txt`; `docs/systems/world_threat_mechanic.md` | Add Cannibalism source predicate and documentation; Event 014 owns set/clear logic, shared refresh owns `world_in_threat`. |
| Deaths | `common/scripted_effects/chaos_meter_effects.txt`; `common/script_constants/chaos_meter_constants.txt`; `common/scripted_localisation/chaosx_scripted_localisation_chaos_meter.txt`; `localisation/english/chaosx_chaos_meter_l_english.yml` | Add dedicated cause, all aggregate/rebuild/sort/history mappings, and exact state-population registration. Avoid double-removal. |
| Chaos history | Same Chaos Meter files | Add a dedicated Event 014 chaos-history reason and scripted/localised label if the spec requires a distinct history row. |
| Ideas/modifiers | `common/ideas/`; `common/dynamic_modifiers/`; `common/modifiers/`; `interface/` | Add route/stage/host ideas and dynamic state/country modifiers; register all 18 present idea icons and any additional required sprites. Follow the lifecycle matrix and remove obsolete stage ideas deterministically. |
| Fixed countries | `common/country_tags/chaosx_countries.txt` or a dedicated Event 014 tag file; `common/countries/`; `history/countries/` | Add collision-audited CBA-CBH warlords and CBL united host with complete identity packages. Prefer a dedicated tag file to reduce conflicts. |
| Characters | `common/characters/`; `common/country_leader/`; `interface/chaosx_characters.gfx`; Event 014 leader sprites | Add Hannibal and any warlord/council leaders, traits, advisor availability, retirement/death/transfer rules, and transformed portrait. Protect anti-spoiler visibility before reveal. |
| Units/OOB | `common/units/`; `common/unit_leader/`; `history/units/`; `interface/chaosx_subuniticons.gfx` | Add only spec-required human warlord/united units. For transformed Wendigo, reuse and preserve `wendigo_zombies` and existing ZZZ weaponized templates. Update `common/script_enums.txt` only if a genuinely new equipment/archetype/category is added. |
| Technologies | `common/technologies/`; Event 002 weaponized-zombie files | Wire any Event 014 human technology unlocks. Do not duplicate or strip Wendigo technology/counterstrain state during merge. |
| Focus trees | `common/national_focus/` | Add local-warlord, united-Hannibal, and Wendigo-overlay trees described by the three focus graphs. `load_focus_tree` only for Event 014-created identities; preserve or explicitly copy completed focuses where the design calls for it. |
| Focus selection/AI | focus `country`/`continuous_focus_position` blocks; `common/ai_strategy/`; `common/ai_strategy_plans/` if needed | Restrict trees by stable Event 014 flags/tags, provide route weights and cancellation/availability logic, and cover player plus AI convergence. |
| Decisions/missions | `common/decisions/`; Event 010/011/013 patterns | Add containment, network, larder, warlord, Hannibal, convergence, resistance, and world-reaction decisions/missions from the matrix. Every visible effect needs trigger/effect tooltips and AI weights. |
| Scripted GUI | `common/scripted_guis/`; `interface/`; `localisation/english/chaosx_gui_l_english.yml` | Add the Frontline Hunger UI and animation sprites. Each GUI button must use the same scripted trigger and effect/cost path as its decision equivalent; no duplicate cost logic. |
| Event log actor | `common/scripted_effects/chaosx_events_log_effects.txt:178-341` | Add ID 14 actor resolution using the prefire origin/host target, then the revealed/unified host where appropriate. |
| Evolution log | `common/scripted_effects/chaosx_events_log_effects.txt:1250-1555`; `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` | Add exactly three Event 014 evolutions and record each once with `record_events_log_evolution_entry`. Event 010 around `010_death_effects.txt:911-918` is the compact precedent. |
| Event details | `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`; `localisation/english/chaosx_gui_l_english.yml` | Add description, title, stage, body, summary, portrait, history-row, and actor-name selectors. Guard all Hannibal text/portrait behind reveal state. |
| Event name | `localisation/english/chaosx_event_names_l_english.yml`; settings/debug scripted-localisation selectors | Replace placeholder with the final public name and ensure settings, debug, event-log, and last-fired selectors resolve ID 14. |
| Super events | `interface/chaosx_super_events.gfx`; `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`; `localisation/english/chaosx_gui_l_english.yml` and/or Event 014 loc | Register four non-colliding entries: reveal, ordinary world end, Wendigo-Hannibal world end, and global defeat/aftermath. Keep unrevealed UI spoiler-safe. |
| Super-event audio | `music/chaosx_super_event_music.asset`; `music/chaosx_super_event_music.txt`; `music/chaosx_music_track_list.html`; `sound/chaosx_sound.asset`; Event 014 audio folders | Register the same resolved IDs in music and sound. Never reuse Holy Realm ID 51. Review concurrent dirty edits instead of overwriting them. |
| Achievements | `common/achievements/chaos_redux_achievements.txt`; `interface/chaosx_achievements.gfx`; `localisation/english/chaosx_achievements_l_english.yml` | Implement all 18 exact spec contracts, three sprites each, stable progress flags/counters, tag-transfer preservation, anti-spoiler text, and explicit scenario eligibility. Existing 13 old triplets are insufficient. |
| Triggerable scenario | `common/script_constants/chaosx_triggerable_scenarios_constants.txt`; `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt`; `common/scripted_triggers/chaosx_triggerable_scenarios_triggers.txt`; `common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt`; scenario GUI and loc; `docs/systems/triggerable_scenarios.md` | Register ID 10, add sorted selector, display text, type/scale controls, validation, launch effect, notifications, and docs. Do not replace SCN008 or SCN009. |
| Event workbook | `docs/spreadsheets/chaos_redux_events_catalog.xlsx` | After gameplay wording is final, replace row 14 placeholder with the exact Event 014 description/details/evolutions/world-end text and add scenario ID 10. Do not add cluster membership. Use the spreadsheet worker after implementation facts exist. |
| Mechanic docs | `docs/` and source specs | Add the required implementation doc with step-by-step mechanics, integration map, tuning variables, AI, assets/sprites, future plans, and known limits. Fold accepted design changes back into the source specs rather than leaving them only in plans. |

## Existing patterns

### Entry event and prefire context

- Event 011 (`events/011_secret_alliance.txt:1-25`) consumes a preselected
  cross-country context and is the closest pattern for a target-sensitive
  entry event.
- Event 013 (`events/013_natural_disasters.txt:1-55`) shows event-specific
  prefire preparation plus safe entry handling.
- The Event 014 prefire should select a living human wartime country and a
  valid origin state, save both as event targets, and leave a clear abort flag
  if selection fails. The visible event should consume that context rather
  than rerolling a different country/state.

### Self-scheduled progression

- Event 010 schedules its own hidden spread/pulse events
  (`events/010_death.txt:59-68` and its scripted effects). This avoids a
  world-wide periodic on-action.
- Event 014 should use the same bounded country-event pulse model, with
  constants for delay ranges. Narrow annexation/capitulation/state-control
  on-actions are acceptable only if required for cleanup or state transfer;
  broad `on_daily`, `on_weekly`, or `on_monthly` iteration is forbidden without
  explicit user permission.

### Complete country packages

- Event 010's DTH country is the fixed-tag special-country precedent.
- Event 018's DHO package is a useful dormant-country package precedent:
  `common/country_tags/018_resources_found_cave_country.txt`,
  `common/countries/The Oth-Kesh Host.txt`, the corresponding
  `history/countries/`, `history/units/`, character, trait, focus, idea, and AI
  files. DHO is Event 018 and must not be reused for Event 014.
- Event 005 contains repeated successor creation and `load_focus_tree`
  precedents, but Event 014 should use a small audited tag slot table rather
  than copying its large regional implementation.

### Decisions and state queues

- Event 010 is the best pattern for special-country decisions and global
  counterplay.
- Event 011 is the best pattern for deep decision/mission chains with explicit
  route and AI gating.
- Event 013 is the best current pattern for queued state targets and a scripted
  GUI backed by scripted effects/triggers.

### Cross-system guards

- Event 010 `death_active_wasteland` and Death state predicates must disqualify
  a state from becoming a Larder. Event 014 must never convert Death's consumed
  population into free Larder value.
- Actual zombie/nonhuman states are not valid human Larders. The Event 002
  crossover occurs at Hannibal convergence, not by treating zombies as
  consumable civilians.
- Natural-disaster state damage may affect supply and recovery, but it is not
  free Larder. Event 014 should read the resulting state conditions without
  rewriting Event 013.
- Prison/camp exploitation should consume Event 014-owned prisoner/Larder
  state and call public Deaths/evidence/condemnation hooks. It must not delete
  or take ownership of camp-repression/genocide responsibility state. Those
  files are concurrently dirty and require a reviewed integration tranche.

## Vanilla or reference precedents

| Need | Precedent | Use |
|---|---|---|
| Player-safe country merge | Vanilla `events/LaR_France.txt:3995-4004` | Execute `change_tag_from` on the future host before annexing the human source; annex with troop transfer. |
| `change_tag_from` semantics | Installed `documentation/effects_documentation.md:2663-2670` | Confirms scope and player-transfer direction. |
| Dynamic country | Repo `zombie_special_project_effects.txt:2412-3143`, backed by vanilla `create_dynamic_country` examples | Preserve the actual Wendigo identity and variables; do not create a parallel fixed tag. |
| Focus replacement | Installed effects documentation for `load_focus_tree`; Event 005 repo use | Set `keep_completed`/`copy_completed_from` deliberately and only on Event 014 identities. |
| Exact consumed-population deaths | `010_death_effects.txt:394-403` plus `chaos_meter_register_deaths` | One API transaction removes people and records country/state Deaths totals. |
| Fire-once event dispatch | Events 011 and 013 plus shared settings effects | Preselect context, fire `chaosx.nr14.1`, then call standard fire-once bookkeeping. |
| Deep missions/AI | Event 011 | Explicit route state, deadlines, abort/bypass outcomes, AI weights, and cleanup. |
| Scripted GUI | Event 013 | Use shared triggers/effects for GUI and decision parity. |
| Fixed special country | Event 010 DTH; Event 018 DHO | Complete tag, country, history, OOB, character, focus, idea, AI, flag, and loc package. |
| Super-event package | Event 010 Death and Event 013 Natural Disasters | Constants, effect, picture selector, text selector, audio ID, sprite, and cleanup all wired together. |

Kaiserreich and the other approved reference mods were not necessary to settle
the key contracts because vanilla plus existing Chaos Redux implementations
were sufficient. If the merge's faction/puppet edge cases remain unclear
during implementation, a narrowly scoped approved-mod comparison would be the
next reference step.

## Likely edit order for parent

1. **Freeze shared IDs and ownership.** Confirm scenario ID 10 and super-event
   IDs 49/50/52/53, audit the concurrent audio/scenario drafts, resolve the 37
   deleted focus icons, and assign ownership of dirty shared files.
2. **Create the Event 014 constants and state vocabulary.** Centralise every
   stage, threshold, route, cost, delay, death cause, chaos reason, tag slot,
   and super-event/scenario ID before writing effects.
3. **Implement origin selection and the base state machine.** Add Event 014
   triggers/effects/events, self-scheduled pulses, safe cleanup, and standalone
   fire-once registration/dispatch. Validate human wartime origins and Death/
   zombie exclusions first.
4. **Wire exact Deaths, Chaos, world-threat, and special-country APIs.** These
   are foundational and should be in place before Larder/spread balance is
   tuned.
5. **Build the fixed country packages.** Register CBA-CBH and CBL, then add
   complete country/history/flag/character/OOB/AI foundations. Do not create a
   fixed Wendigo replacement.
6. **Implement the three evolution tranches.** Record each evolution once,
   update actor/details state, and validate state/array ownership after
   annexation or country death.
7. **Implement Hannibal reveal, convergence, and player-safe merge.** Keep
   anti-spoiler state until the reveal transaction commits; handle ordinary
   CBL and dynamic Wendigo hosts as separate, fully tested merge branches.
8. **Implement decisions, missions, focus trees, route ideas, AI, and scripted
   GUI.** Use the matrices as checklists and route all GUI actions through the
   same validated scripted effects.
9. **Wire four super events and the audio package.** Use the frozen IDs and
   convert/source all four correct pictures; preserve existing ID 51.
10. **Implement all 18 achievements and the scenario.** Preserve progress
    through tag transfer and explicitly define whether each achievement is
    valid in scenario starts.
11. **Complete localisation, event log, evolutions, details, assets, sprites,
    and docs.** Run the anti-spoiler audit after all selectors exist.
12. **Update the workbook from final in-game wording.** Then run focus,
    decision/mission, localisation, country-package, and event-completion audit
    subagents before any completion claim.

## Validation checks

These are task-specific acceptance checks, not generic syntax hygiene.

### Dispatch and lifecycle

- ID 14 appears once in `global.all_events` and is a standalone fire-once
  event with no cluster membership.
- Random and manual dispatch use the same valid-origin predicate and cannot
  fire without a living human wartime origin and eligible origin state.
- A failed prefire does not consume the fire-once event or leave stale event
  targets.
- Hidden pulses stop after defeat, world end, host deletion, or event cleanup.

### Population and Larder accounting

- Every consumed person is removed once, logged once in state and country
  Deaths totals, assigned the Cannibalism cause, and converted to Larder once.
- Death wastelands, actual nonhuman/zombie population, and natural-disaster
  damage never become free Larder.
- Larder cannot go negative; caps, decay, spoilage, capture, and transfer use
  central constants and retain accounting across country merges.

### Country creation and merge

- Each fixed tag is registered once and has a complete country/history/flag/
  character/OOB/focus/AI/localisation package.
- Tag slots are not reused while the prior country still exists or retains
  owned states/units.
- Human-source convergence transfers the player before annexation and retains
  troops, wars, controlled/owned states, stockpile policy, achievements, Event
  014 state, and intended puppets/faction relationships.
- Player-controlled Wendigo remains the host and retains all Event 002
  identity flags, templates, ideas, tech/counterstrain hooks, recruitment, and
  world-end readiness.
- No stale event target, slot variable, warlord count, or host pointer remains
  after annexation/capitulation.

### Cross-event behavior

- Human cannibal warlords/united hosts are excluded from unrelated Event 008,
  011, 017, 018, and Random War selections through shared classification.
- Only transformed Wendigo-Hannibal is nonhuman; ordinary cannibal countries
  still use normal civilian systems where the specification requires them.
- Fury countries remain eligible origins only while human and otherwise valid.
- Camp/genocide integration records evidence/deaths without corrupting camp
  ownership, responsibility, release, condemnation, or cleanup state.

### UI, localisation, and spoilers

- Before reveal, no event name, detail row, evolution row, focus tooltip,
  decision tooltip, character, portrait, flag, achievement text, scenario
  text, debug selector, or super-event selector exposes Hannibal.
- After reveal, the correct actor, portrait, focus tree, country name, route,
  super event, and achievement conditions become visible exactly once.
- Decision buttons and scripted-GUI buttons have identical availability,
  cost, effect, cooldown, AI, and failure behavior.
- All six animated assets use the real eight-frame packages, have static
  fallbacks, and are wired through valid `.gfx`/GUI definitions.

### Global registries

- Scenario 10 is unique and IDs 8/9 still launch Africa Is One/Coalition
  Unmasked.
- Super events 49/50/52/53 resolve the intended picture, title, quote, button,
  description, music, and sound. Holy Realm ID 51 is unchanged.
- Cannibalism Deaths and Chaos reasons appear correctly in aggregate totals,
  sorted/unsorted lists, history rows, tooltips, and save/rebuild paths.
- The world-threat source sets and clears from actual Event 014 state and does
  not leave `world_in_threat` stuck after defeat.

### Completion surfaces

- All three evolution entries are recorded once and their workbook wording
  matches in-game localisation.
- All 18 achievements have complete scripted conditions, localisation, and
  three-state sprite sets; progress survives ordinary and Wendigo merges.
- All focus-tree nodes in the three graphs are implemented, localised, given
  valid icons, balanced, and AI-routed; none silently falls back to a generic
  tree.
- The final four super-event pictures are the four specified narrative beats,
  not the stale island direction unless the source spec is explicitly revised.

## Risks and blockers

1. **Dirty shared files.** The worktree contains concurrent/user changes in
   achievement registries, super-event selectors and sprites, GUI and decision
   localisation, music/sound registries, camp/genocide systems, and the event
   workbook. Event 014 implementation must merge narrowly and review each
   shared diff; broad file replacement would overwrite unrelated work.
2. **Deleted focus icons.** Thirty-seven tracked Event 014 focus DDS files are
   currently deleted. Their ownership must be resolved before focus completion
   can be claimed.
3. **Stale asset manifest.** It records missing runtime outputs and incomplete
   flag/achievement packages as complete. Asset validation must use filesystem
   evidence, not the manifest status text, until the manifest is corrected.
4. **Achievement mismatch.** Thirteen old achievement triplets do not satisfy
   the current eighteen-achievement specification. A mapping or regenerated
   set is required; silent reuse is a simplification and needs user approval.
5. **Super-event collision.** Concurrent audio's ID 51 conflicts with Holy
   Realm content. Rename that Event 014 entry everywhere before registration.
6. **Scenario spec drift.** Source part 11 says ID 8, while the live registry
   requires ID 10. Once accepted, update the source spec and package manifest
   so the plan does not remain the only record of the design change.
7. **Merge complexity.** The ordinary CBL and dynamic Wendigo branches have
   different identity/focus/character requirements. A single generic annex
   effect is unsafe unless it explicitly preserves both packages and player
   state.
8. **No fallback permission.** A generic focus tree, substitute achievement
   art, fixed-tag Wendigo, reused Deaths cause, reduced animation, missing
   country package, or omitted route is forbidden unless discussed and
   approved by the user.

## Recommended next action

Freeze the shared registry decisions and worktree ownership first: retain
scenario ID 10, allocate Event 014 super events to 49/50/52/53, resolve the
deleted focus-icon tranche, and assign narrow owners for the dirty achievement,
super-event, audio, camp/genocide, and workbook files. Then have the scripted
system architect produce the constants/state/merge API contract before the
main agent implements the entry event and base state machine. That ordering
prevents the two global-ID collisions, double population removal, and loss of
the real Wendigo/player country during later convergence work.
