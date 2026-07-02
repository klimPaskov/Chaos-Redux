# Repo Explorer Handoff

## Scope read
- Parent task: read-only map for implementing Event 014 Cannibalism from `docs/specs/014_cannibalism_specs/`, especially `prompts/014_cannibalism_coding_prompt.md` and sibling prompts.
- Explicit constraints: no gameplay, localisation, GUI, GFX, asset, spreadsheet, or doc patching except this handoff. Event 014 must be Minor Fire-Once, open as war-horror discipline/supply collapse, resolve locally per country, use Evo I ritual ideology, Evo II organized cults/islands/communes/CBL, Evo III global cult network/future Hannibal hooks, and gate world-end behind chaos threshold plus Hannibal or an accepted unifier. Decision costs must be concrete resources, not a PP store. If CBL can appear, CBL needs a complete country package.
- Files or ids requested: Event 014, `chaosx.nr14.*`, old direct calls to `chaosx.nr14.2`, CBL, decisions/missions, country package, focus tree, super-events, achievements, assets, event log.
- Skills or docs read: `chaos-redux-events`, `chaos-redux-subagents`, `hoi4-decisions-missions`, `hoi4-focus-trees`, `chaos-redux-super-events`, `chaos-redux-event-assets`, `chaos-redux-frame-animation`; required AGENTS rules; targeted offline wiki pages for events, decisions, focuses, achievements, GUI/GFX, country creation, data structures, triggers/effects/localisation/scopes/on_actions; vanilla documentation for script constants, effects, triggers, missions, focus loading, event targets, meta effects, and achievements.

## Primary findings
- Current tracked `events/014_cannibalism.txt` is still the old two-event implementation. It directly picks any war country and fires `chaosx.nr14.2`, then adds the old `cannibalism` idea/news with no containment, local outbreak state, evolutions, CBL, world threat, achievements, or event log detail.
- The worktree already contains untracked partial Event 014 infrastructure: constants, triggers, ideas, dynamic state modifiers, super-event research, and a super-event text handoff. Treat these as in-progress user work and integrate rather than overwrite.
- Hard classification conflict: `common/script_constants/014_cannibalism_constants.txt` has `event_type = 3` and `event_system_event_type.fire_once = 3`, but `common/scripted_effects/chaosx_logic_effects.txt:198` still registers Event 014 in `global.repeatable_events`. The parent must move it to `global.fire_once_events` and keep logs/settings aligned.
- Old direct calls to `chaosx.nr14.2` exist in Event 070 and will bypass the new bootstrap, actor capture, event log, and target validation unless redirected.
- CBL is referenced by untracked triggers/specs but no CBL country tag/package files exist. Do not let any path spawn or release CBL until the full package is implemented.
- The event report picture reference is currently broken: `events/014_cannibalism.txt:43` uses `GFX_report_event_cannibalism`, but `rg` found only `GFX_news_cannibalism` registered in `interface/chaosx_pictures.gfx:120`.

## Relevant files
| Path | Why it matters | Evidence |
| --- | --- | --- |
| `events/014_cannibalism.txt` | Primary event file; currently old implementation and must become the event map `chaosx.nr14.1` through `.14` from the spec. | `chaosx.nr14.1` at lines 23-33 directly fires `.2`; `chaosx.nr14.2` at lines 40-78 only adds old idea/news. |
| `events/070_africa_gods.txt` | Contains old direct callers that must not keep entering the new chain at `.2`. | Lines 286, 314, and 348 call `country_event = { id = chaosx.nr14.2 ... }`. |
| `events/_chaosx_news.txt` | Existing news event for old Event 014. | `chaosx.news.17` at lines 140-154, picture `GFX_news_cannibalism`. |
| `localisation/english/014_cannibalism_l_english.yml` | Old player-facing event/news text. Needs replacement with war-horror opening, local response, evolutions, decisions/missions, CBL, super-events, achievements. | Keys only cover `chaosx.nr14.1.t`, `chaosx.nr14.2.*`, and `chaosx.news.17.*`. |
| `common/scripted_triggers/014_cannibalism_triggers.txt` | Untracked partial trigger set. Useful but must be reviewed because it assumes CBL and future Hannibal flags. | Defines `cannibalism_can_be_origin`, `is_cannibal_commune_country`, concrete cost gates, and `cannibalism_world_end_route_available`. |
| `common/script_constants/014_cannibalism_constants.txt` | Untracked partial tuning source. Good basis for centralization. | Defines `cannibalism_event_log.event_type = 3`, meters, decision costs, CBL package values, world-end thresholds, super-event IDs `141-144`. |
| `common/ideas/014_cannibalism_ideas.txt` | Untracked staged Event 014 ideas. Needs integration with old `common/ideas/chaosx_ideas.txt` idea removal/replacement. | Defines `cannibalism_field_collapse`, `cannibalism_ritual_hunger`, `cannibalism_commune_country_spirit`, `cannibalism_last_table_discipline`. |
| `common/dynamic_modifiers/014_cannibalism_state_modifiers.txt` | Untracked state pressure package for local spread/island/commune mechanics. | Defines `cannibalism_field_disappearances_state`, `cannibalism_silent_garrison_state`, `cannibalism_commune_state`, `cannibalism_hunting_ground_state`. |
| `common/scripted_effects/chaosx_logic_effects.txt` | Event registration arrays and existing settings discovery. Dirty shared file. | Line 198 currently `add_to_array = { global.repeatable_events = 14 }  # CANNIBALISM`. |
| `common/scripted_effects/chaosx_settings_effects.txt` | Event firing helper and super-event audio helper. Dirty shared file. | `fire_event_by_id` around line 1749; `fire_event_by_temp_id_no_cluster` around 4539; `play_current_super_event_audio` around 4667. |
| `common/scripted_effects/chaosx_events_log_effects.txt` | History/evolution/event details logging. Dirty shared file. | `record_events_log_history_entry` at line 257; `record_events_log_evolution_entry` at line 491; default actor helper at line 103. |
| `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` | Event Log and Event Details text selectors. Dirty shared file. | Existing generic name branches include event id 14, but no Event 014 detail/evolution implementation found. |
| `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt` | Super-event title/quote/button loc selector. Dirty shared file. | Current values include many slots but no visible 141-144 Event 014 branches found in targeted search. |
| `localisation/english/chaosx_event_names_l_english.yml` | Event name keys and future super-event name keys. Dirty shared file. | `chaosx.event_name.14: "Cannibalism"` at line 16; debug/settings already have branches for 140-149 but loc keys must exist if used. |
| `interface/chaosx_pictures.gfx` | Existing report/news GFX registration surface. | Registers only `GFX_news_cannibalism` at lines 120-121; no `GFX_report_event_cannibalism` registration found. |
| `gfx/event_pictures/014_cannibalism/report_event_cannibalism.dds` | Existing report art file. Needs `.gfx` registration or event picture will fail. | Present in `rg --files`; no corresponding sprite registration found. |
| `gfx/event_pictures/014_cannibalism/news_cannibalism.dds` | Existing news art file. | Registered by `GFX_news_cannibalism`. |
| `docs/super_events/014_cannibalism_super_event_research.md` | Untracked super-event text research. | Covers titles, quotes, button remarks; explicitly says audio selection/license verification is still out of scope. |
| `docs/plans/014_cannibalism_plans/subagent_handoffs/014_cannibalism_super_event_text_handoff.md` | Existing untracked subagent handoff for super-event text. | Says Role 2 remains blocked until Hannibal package exists and Role 4 remains blocked unless global/near-global scale is reached. |
| `music/super_events/014_cannibalism/*` | Existing audio files for four super-event roles. | Files exist for islands reveal, Hannibal network, world-end, defeat aftermath plus source files. They are not yet proven wired in `music/chaosx_super_event_music.*` or `sound/chaosx_sound.asset`. |
| `common/achievements/chaos_redux_achievements.txt` | Achievement registration. Dirty shared file. | No Event 014 achievement ids found outside the spec matrix. |
| `gfx/achievements/` | Required DDS triplets for custom achievements. | No Event 014 achievement DDS triplets found by id search. |
| `common/decisions/014_cannibalism_decisions.txt` and `common/decisions/categories/014_cannibalism_categories.txt` | Required decision/mission implementation surfaces. | Both missing. |
| `common/scripted_effects/014_cannibalism_effects.txt` | Required implementation helper surface for target selection, meters, spread, CBL, super-events, cleanup. | Missing. |
| `common/national_focus/014_cannibalism_focus_tree.txt` | Required if CBL can appear. | Missing. |
| `common/ai_strategy/014_cannibalism.txt` | Required if CBL, cannibal countries, or response AI exist. | Missing. |
| `common/countries/CBL.txt`, `history/countries/CBL - Cannibal Commune.txt` | Required if CBL can appear. | Missing. |
| `docs/assets/014_cannibalism/manifest.md`, `docs/assets/014_cannibalism/gfx_handoff.md` | Required Event 014 asset tracking/handoff surfaces. | Missing. |

## Existing patterns
- Event registration and firing: mirror `common/scripted_effects/chaosx_logic_effects.txt` for event arrays, but correct Event 014 from repeatable to fire-once. `common/scripted_effects/chaosx_settings_effects.txt` resolves major/repeatable/fire-once event type and fires through `fire_event_by_temp_id_no_cluster`; Event 014 should not be clustered.
- Event log/evolution log: use `record_events_log_history_entry = yes` and `record_events_log_evolution_entry = yes` from `common/scripted_effects/chaosx_events_log_effects.txt`. Event 014 should set event id 14, fire-once type, affected actor, and evolution stage/type before logging. The `chaos-redux-events` skill requires Event Details and evolution details to describe premise/world state, not raw effects.
- World threat: mirror the per-event refresh pattern from `common/scripted_effects/002_zombie_outbreak_effects.txt:1079` and `common/scripted_effects/010_death_effects.txt:840`, which set/clear a `world_threat_source_*` flag and call `refresh_world_threat_state = yes` from `common/scripted_effects/chaosx_dynamic_effects.txt:462`. Event 014 needs its own source flag only at Evo III/world-threat scale, not during local containment.
- Special chaos country classification: `is_special_chaos_country` and `is_actual_nonhuman_country` are shared triggers. CBL should be special chaos country if implemented. It should not be actual nonhuman until Evo III/Hannibal transformation explicitly crosses that line.
- Country package precedent: `docs/events/002_zombie_outbreak.md` documents dynamic hostile country creation, OOB/template setup, world-threat refresh, and cleanup. `docs/events/010_death.md` documents a full hostile package with constants/effects/triggers/ideas/dynamic modifiers/AI/decisions/units/focus/super-events. Event 014 CBL should mirror the completeness standard, not spawn as a tag-only shortcut.
- Super-event precedent: `common/scripted_effects/013_natural_disasters_effects.txt:2755-2818` sets `super_event_visible`, `global.current_super_event_audio_id`, then calls `play_current_super_event_audio = yes`. `common/scripted_effects/010_death_effects.txt:796-836` does the same for hostile/world-end variants. Event 014 constants currently reserve slots `141-144`, but current localisation/GFX/audio registry must be reconciled with dirty Event 015 super-event slots.
- Triggerable scenario precedent: use `common/scripted_guis/chaosx_scripted_gui_settings.txt` and `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt` for scenario registration/launch. Do not add broad daily/weekly world scans.
- Animated GUI precedent: `interface/003_holy_realm.gfx` uses `frameAnimatedSpriteType` with `play_on_show = yes`. Event 014 animated assets must follow `chaos-redux-frame-animation`: real source frames, horizontal sheet DDS, static fallback, no GIF-only or transform-only mockups.
- Achievement precedent: use `common/achievements/chaos_redux_achievements.txt`, localisation `*_NAME`/`*_DESC`, and DDS triplets directly under `gfx/achievements/`. Event 014 achievement ids currently exist only in the spec matrix.

## Vanilla or reference precedents
- `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`: country event syntax, triggered-only events, delayed `country_event = { id = ... days = ... random_days = ... }`, and the 20-day auto-event check caveat.
- `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`: missions are decisions with `days_mission_timeout`; `visible` does nothing for missions; `available` defaults to true and can instantly complete missions if omitted; `activate_mission` is recommended for controlled activation.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`: `activate_mission`, `remove_mission`, `add_days_mission_timeout`, `save_event_target_as`, `load_focus_tree`, and `meta_effect`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`: event target and trigger syntax references, including `has_event_target`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md` and `common/script_constants/documentation.md`: `constant:` script constants are global; `@` constants are file scoped.
- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`: regular event targets auto-clear with the effect chain and can carry into events fired from that chain; global event targets persist and need cleanup.
- `paradox_wiki/Country creation - Hearts of Iron 4 Wiki.md`: a country package needs tag, country file, history file, localisation, and OOB; no OOB can cause broken building application.
- `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md` and vanilla focus files: CBL focus work should use a real shared focus tree, not a placeholder branch.
- `paradox_wiki/Achievement modding - Hearts of Iron 4 Wiki.md`: custom achievements need `common/achievements`, three DDS files under `gfx/achievements/`, `possible`, `happened`, and `*_NAME`/`*_DESC` loc.
- `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`: `spriteType` and `frameAnimatedSpriteType` syntax for static and frame-sheet assets.
- Kaiserreich was not needed for this map because vanilla docs/wiki plus existing Chaos Redux Event 002/010/013 patterns answered the structural questions.

## Likely edit order for the parent
1. Protect dirty worktree state first. Read and preserve user/in-progress changes in dirty shared files before editing: `common/scripted_effects/chaosx_logic_effects.txt`, `chaosx_settings_effects.txt`, `chaosx_events_log_effects.txt`, `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`, `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`, `localisation/english/chaosx_event_names_l_english.yml`, `localisation/english/chaosx_gui_l_english.yml`, `common/achievements/chaos_redux_achievements.txt`, `common/countries/cosmetic.txt`, `music/chaosx_super_event_music.asset`, `music/chaosx_super_event_music.txt`, and `sound/chaosx_sound.asset`.
2. Decide whether to adopt the untracked partial Event 014 files as the implementation base. They already contain useful constants/triggers/ideas/modifiers, but they do not include effects, events, decisions, CBL package, focus tree, AI, achievements, or asset manifests.
3. Fix registration/classification early: move Event 014 from `global.repeatable_events` to `global.fire_once_events`, keep event type `constant:event_system_event_type.fire_once`, and make `chaosx.nr14.1` the only generic bootstrap entry.
4. Replace or redirect all external `.2` callers. Event 070 should call the new bootstrap/helper, not `chaosx.nr14.2`.
5. Build `common/scripted_effects/014_cannibalism_effects.txt` around the spec architecture: target selection, target/event targets, meter initialization, per-country containment/spread, evolution logging, CBL gate/spawn only when package is ready, world-threat refresh, super-event firing, and cleanup.
6. Rewrite `events/014_cannibalism.txt` to the spec map: `.1` hidden bootstrap, `.2` first report, `.3` investigation, `.4` public leak/news, `.5` failed containment, `.6` successful containment, `.7` spread exposure, `.8` Evo I, `.9` Evo II, `.10` country declaration, `.11` Evo III gateway, `.12` Hannibal reveal blocked until valid, `.13` world-end, `.14` defeat aftermath.
7. Implement decisions/missions after core effects exist. Use `common/decisions/categories/014_cannibalism_categories.txt` and `common/decisions/014_cannibalism_decisions.txt`; use concrete equipment/manpower/fuel/CP/XP/stability costs from constants and avoid PP-store design.
8. If any path can create CBL, implement the complete package in the same tranche: tag/country/history/OOB/units/leader/ideas/AI/focus tree/assets/localisation/cleanup and register `is_special_chaos_country`. Otherwise block all CBL formation decisions/events behind missing-package gates and report that simplification.
9. Wire event log, event details, evolution details, settings/debug names, and spreadsheet-facing text after the event map stabilizes. Keep detail text premise-focused.
10. Wire super-events only after slots/audio/assets are reconciled. Use existing text research and audio files, but confirm license/source notes, add `super_event_visible` branches, images, music/sound assets, and guarded triggers.
11. Implement achievements last, once flags/variables for containment, spread prevention, exploitation, islands, terror units, archives, CBL, Last Table, Hannibal link, world-threat defeat, and aftermath cleanup exist.
12. Run focused audits: event completion, decision/mission, country package, focus tree, localisation, asset/super-event, and achievement checks before any completion claim.

## Validation checks
- Existing old direct calls: `rg -n "chaosx\\.nr14\\.2" events common localisation interface`
- Event registration conflict: `rg -n "global\\.(repeatable_events|fire_once_events).*14|event_type = 3|event_id = 14" common/scripted_effects common/script_constants common/scripted_localisation`
- Missing Event 014 implementation surfaces: test paths for `common/scripted_effects/014_cannibalism_effects.txt`, decisions/category files, CBL country/history/OOB, `common/national_focus/014_cannibalism_focus_tree.txt`, `common/ai_strategy/014_cannibalism.txt`, `docs/assets/014_cannibalism/manifest.md`, and `docs/assets/014_cannibalism/gfx_handoff.md`.
- CBL completeness if enabled: `rg -n "\\bCBL\\b|is_cannibal_commune_country|cannibalism_commune_country" common history events localisation interface`
- Event picture wiring: `rg -n "GFX_report_event_cannibalism|report_event_cannibalism|GFX_news_cannibalism|news_cannibalism" interface events gfx`
- Super-event slots/audio wiring: `rg -n "141|142|143|144|014_cannibalism|current_super_event_audio_id|super_event_visible" common/scripted_effects common/scripted_localisation interface music sound localisation`
- Event log/detail wiring: `rg -n "event_id = 14|evolution_type = 14|record_events_log_history_entry|record_events_log_evolution_entry|chaosx.event_name.14|chaosx.event_name.14[1-4]" common/scripted_effects common/scripted_localisation localisation/english`
- Decision cost design: `rg -n "political_power|cost =|days_mission_timeout|activate_mission|remove_mission|cannibalism_can_pay" common/decisions common/scripted_triggers common/scripted_effects`
- No broad on_action scan without explicit permission: `rg -n "cannibal|nr14" common/on_actions common/scripted_effects events`
- Achievement registration/assets: `rg -n "cannibalism_clean_mess|cannibalism_no_second_table|cannibalism_silent_island|cannibalism_do_not_feed_the_front|cannibalism_trial_without_panic|cannibalism_black_larder|cannibalism_last_ship_home|cannibalism_burn_the_cookbooks|cannibalism_hunger_of_hannibal|cannibalism_the_living_are_not_cattle|cannibalism_empty_larder|cannibalism_table_for_one|cannibalism_after_the_feast" common/achievements localisation/english gfx/achievements`
- Asset manifest and final DDS checks: `rg --files gfx interface docs/assets/014_cannibalism | rg "014_cannibalism|cannibalism|CBL|achievement"`
- Dirty shared files before commit: `git status --short -- common/scripted_effects/chaosx_logic_effects.txt common/scripted_effects/chaosx_settings_effects.txt common/scripted_effects/chaosx_events_log_effects.txt common/scripted_localisation/chaosx_scripted_localisation_events_log.txt common/scripted_localisation/chaosx_scripted_localisation_super_events.txt common/achievements/chaos_redux_achievements.txt localisation/english/chaosx_event_names_l_english.yml music/chaosx_super_event_music.asset music/chaosx_super_event_music.txt sound/chaosx_sound.asset`

## Risks and blockers
Confirmed blockers:
- Event 014 is still registered as repeatable at `common/scripted_effects/chaosx_logic_effects.txt:198`, contradicting the nonnegotiable Minor Fire-Once classification.
- CBL is referenced but not implemented. Missing files include `common/countries/CBL.txt`, `history/countries/CBL - Cannibal Commune.txt`, focus tree, AI strategy, decisions, OOB, flags, leader package, and localisation. Any CBL appearance path is incomplete until this package exists.
- `common/scripted_effects/014_cannibalism_effects.txt` is missing, so current constants/triggers have no core implementation owner.
- `GFX_report_event_cannibalism` is referenced but not registered.
- Event 014 achievements exist only in the spec matrix; no achievement registration or DDS triplets were found.
- Hannibal final route is not implementable as a complete route from current repo evidence. Existing Event 014 material correctly treats Hannibal as a hook, but world-end must remain gated behind `hannibal_exists` or an explicit accepted unifier flag/spec.

Ordinary risks:
- The shared files most likely needed for registration, logs, super-events, audio, achievements, and names are already dirty. The parent must merge carefully and avoid overwriting unrelated Event 013/Event 015 work.
- Event 070 direct calls can bypass actor capture and local containment if not redirected.
- The old `cannibalism` idea in `common/ideas/chaosx_ideas.txt` and `localisation/english/chaosx_ideas_l_english.yml` conflicts with staged Event 014 ideas and should be retired or isolated carefully.
- Decisions/missions need explicit `available`/`activation` handling. Missions without guarded `available` can complete instantly.
- World-threat and spread mechanics can be tempting to solve with daily/weekly global scans. AGENTS forbids whole-world daily/weekly style on_actions unless explicitly requested.
- Super-event slots `141-144` in Event 014 constants must be reconciled with the current dirty super-event localisation/GFX/audio registries before wiring.
- Audio files exist, but the existing super-event text handoff says no audio research. License/source verification and final `music`/`sound` wiring are still required.
- Event 014 asset requirements are large. Generated fictional gore is required; no real atrocity/victim gore should be sourced.

## Recommended next action
Start by adopting or explicitly rejecting the untracked partial Event 014 constants/triggers/ideas/modifiers, then fix Event 014 registration to Fire-Once and build the missing `014_cannibalism_effects.txt` helper layer before rewriting events or decisions. This gives every later surface a stable contract and prevents `.2` direct callers, CBL hooks, and world-end gates from diverging.
