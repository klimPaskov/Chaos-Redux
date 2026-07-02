# Repo Explorer Handoff

## Scope read
- Parent task: map Event 011 Secret Alliance implementation surfaces before full implementation.
- Explicit constraints: read-only exploration; no gameplay, localisation, GUI, GFX, asset, doc, spreadsheet, history, country, focus, decision, scripted effect, scripted trigger, on_action, or event edits. This report is the only write.
- Files or ids requested: Event 011, `Secret Alliance`, `chaosx.nr11.1`, specs under `docs/specs/011_secret_alliance_specs/`, decisions/missions/UI, achievements, assets, animated UI assets, reveal super-event, audio, event log/details.
- Skills or docs read: `AGENTS.md`; `chaos-redux-events`; `chaos-redux-subagents`; `hoi4-decisions-missions`; `chaos-redux-event-assets`; `chaos-redux-super-events`; `chaos-redux-frame-animation`; `xlsx`. Offline wiki pages consulted include Data structures, Event modding, Decision modding, On actions, Scripted GUI modding, Graphical asset modding. Vanilla docs consulted include `documentation/effects_documentation.md` and `documentation/triggers_documentation.md`.

Parent note: this handoff records the pre-implementation map that guided Event 011. Later parent and subagent handoffs in this folder supersede the initial "missing file" observations.

## Primary findings
- The Event 011 design package exists only under `docs/specs/011_secret_alliance_specs/`. I found no alternate imported package location outside that folder.
- Event 011 is already reserved in the event system as a minor fire-once event: `common/scripted_effects/chaosx_logic_effects.txt:164` has `add_to_array = { global.fire_once_events = 11 }  # SECRET ALLIANCE`.
- At exploration time, no implementation file existed for Event 011. The parent implementation later added `events/011_secret_alliance.txt`, `chaosx.nr11.*` event ids, Event 011 decisions, effects/triggers/constants, assets, achievements, super-event/audio wiring, and `docs/events/011_secret_alliance.md`.
- At exploration time, the only Event 011 localisation was generic/reserved: `localisation/english/chaosx_event_names_l_english.yml:13` had `chaosx.event_name.11: "Event 011"`.

## Relevant files
| Path | Why it matters | Evidence |
| --- | --- | --- |
| `docs/specs/011_secret_alliance_specs/manifest.json` | Source package inventory. | Lists event id `011`, slug `secret_alliance`, all specs/prompts/matrices. |
| `docs/specs/011_secret_alliance_specs/specs/011_secret_alliance_spec_part_1_core.md` | Core opening, founder selection, secrecy ladder, baseline incidents. | Defines exactly three valid non-war founders or unavailable; prefer factionless minors; hidden compact, target pressure, visibility ladder. |
| `docs/specs/011_secret_alliance_specs/specs/011_secret_alliance_spec_part_2_evolutions_and_reveal.md` | Baseline/Evo I/Evo II/Evo III and reveal rules. | Requires active evolutions, pre-fire openings, war reveal, public pact crisis. |
| `docs/specs/011_secret_alliance_specs/specs/011_secret_alliance_spec_part_3_decisions_missions_ui.md` | Decision, mission, and UI design source. | Maps investigation, protection, diplomacy, border, exposure, crisis, war, and war-support actions. |
| `docs/specs/011_secret_alliance_specs/specs/011_secret_alliance_spec_part_4_systems_ai_assets_achievements.md` | AI, assets, achievements, ideas, super-event, docs/spreadsheet alignment. | Defines target values: evidence, counter-readiness, secrecy, cohesion, readiness, member confidence. |
| `docs/specs/011_secret_alliance_specs/prompts/*.md` | Imported implementation/asset/super-event/achievement/decision prompts. | Includes `secret_alliance_coding_prompt.md`, `asset_prompt`, `super_event_prompt`, `achievement_prompt`, `decision_mission_prompt`. |
| `docs/specs/011_secret_alliance_specs/matrices/*.md` | Detailed acceptance and system maps. | Includes scripted architecture, decision map, AI matrix, asset matrix, achievement matrix, localisation handoff. |
| `common/scripted_effects/chaosx_logic_effects.txt` | Event registration, type, weight, random pool filters. | `initialize_event_categories` registers 11 as fire-once; `get_event_weight` starts at line 427; `evaluate_random_event_active_pool_candidate` starts at line 491; `get_event_type` starts at line 1045. |
| `common/scripted_effects/chaosx_settings_effects.txt` | Manual/random event dispatch path. | `fire_selected_event` builds `chaosx.nr[EVENT_ID].1`; `fire_event_by_temp_id_no_cluster` has pre-fire gates for events 3, 7, 8, 9, 10, 14, 15 but not 11. |
| `localisation/english/chaosx_event_names_l_english.yml` | Event name key. | At exploration time the key was generic/reserved as `chaosx.event_name.11: "Event 011"`. |
| `common/scripted_localisation/chaosx_scripted_localisation_debug.txt` | Debug event-name selector. | `GetEventName` maps id 11 to `chaosx.event_name.11`. |
| `common/scripted_localisation/chaosx_scripted_localisation_settings.txt` | Settings and last-fired event-name selectors. | `GetSettingsEventName` and `GetLastEventName` both map id 11 to `chaosx.event_name.11`. |
| `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` | Event log/evolution/detail text dispatch. | Generic id 11 name exists, but no Secret Alliance evolution/detail selector branches. |
| `common/scripted_effects/chaosx_events_log_effects.txt` | History/evolution recording and Event Details previews. | Default actor map at lines 103-155 omits 11; preview patterns exist for 7/8/9/10/13 around lines 1304-1424. |
| `events/011_secret_alliance.txt` | Primary event script to add. | Missing. Must use `add_namespace = chaosx.nr11` and entry `id = chaosx.nr11.1`. |
| `common/script_constants/011_secret_alliance_constants.txt` | Central tuning for thresholds, weights, roles, costs, timers. | Missing. Spec matrix requires constant groups. |
| `common/scripted_effects/011_secret_alliance_effects.txt` | Pact initialization, invitations, incidents, reveal, faction/war, cleanup. | Missing. |
| `common/scripted_triggers/011_secret_alliance_triggers.txt` | Valid target/founder/member, visibility, decision, AI, reveal conditions. | Missing. |
| `common/on_actions/011_secret_alliance_on_actions.txt` or `common/on_actions/chaosx_on_actions.txt` | War reveal hook. | Missing. Existing repo uses `on_war_relation_added` in `chaosx_on_actions.txt` and `on_declare_war` in `003_holy_realm_on_actions.txt`. |
| `common/decisions/011_secret_alliance_decisions.txt` | Player and AI decisions/missions. | Missing. |
| `common/decisions/categories/011_secret_alliance_categories.txt` | Dossier/category registration and optional scripted GUI link. | Missing. |
| `common/scripted_guis/011_secret_alliance_scripted_gui.txt` and `interface/011_secret_alliance.gui` | Animated dossier/readiness UI if implemented as custom decision-category UI. | Missing. |
| `common/ideas/011_secret_alliance_ideas.txt` | Dossier pressure, counter-network, protocol discipline, patron offices, exposed signatory, pact war coordination, restored credibility. | Missing. |
| `common/factions/templates/011_secret_alliance_pact.txt`, `common/factions/rules/*`, `common/factions/goals/*` | Anti-[target] Pact faction template, rules, goals. | Missing. Existing templates use `common/factions/templates/anti_zombie_league.txt` and `holy_realm_mandala_of_nations.txt`. |
| `interface/011_secret_alliance.gfx` | Event pictures, decisions, ideas, dossier UI, animated frame sheets, super-event sprite. | Missing. Event-specific pattern exists in `interface/015_utopia_manifesto.gfx`. |
| `gfx/event_pictures/011_secret_alliance/`, `gfx/interface/decisions/011_secret_alliance/`, `gfx/interface/ideas/011_secret_alliance/`, `gfx/interface/secret_alliance/`, `gfx/super_events/011_secret_alliance/` | Final DDS asset locations implied by current repo style. | Missing. |
| `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`, `interface/chaosx_super_events.gfx`, `localisation/english/chaosx_super_events_l_english.yml` | Reveal super-event slot, image, title/desc/quote/action. | Existing selectors use numeric `super_event_visible` slot values; no Secret Alliance branch. |
| `music/chaosx_super_event_music.asset`, `music/chaosx_super_event_music.txt`, `sound/chaosx_sound.asset`, `localisation/english/chaosx_music_l_english.yml` | Licensed reveal audio registration and settings-aware playback. | No Secret Alliance audio found. |
| `common/achievements/chaos_redux_achievements.txt`, `interface/chaosx_achievements.gfx`, `localisation/english/chaosx_achievements_l_english.yml`, `gfx/achievements/` | Achievement logic, sprite wiring, loc, icons. | No `secret_alliance` hits. |
| `docs/events/011_secret_alliance.md` | Required event/mechanic documentation. | Missing. |
| `docs/spreadsheets/chaos_redux_events_catalog.xlsx` | Event catalog update after final implementation wording exists. | Existing package says spreadsheet should be updated only from final in-game facts. |

## Existing patterns
- Event namespace/id: mirror `events/010_death.txt` and neighboring event files. Current convention is `add_namespace = chaosx.nr10`, not zero-padded `nr010`; Event 011 should use `chaosx.nr11.1`.
- Event registration: `common/scripted_effects/chaosx_logic_effects.txt` already has Event 011 in `global.fire_once_events`. Do not duplicate it; add availability/weight/pre-fire filtering instead.
- Random/manual dispatch: `common/scripted_effects/chaosx_settings_effects.txt` has event-specific pre-fire checks for Holy Realm, Fury, Tensions, White Peace, Death, Cannibalism, and Utopia. Event 011 needs a similar gate so it becomes unavailable when three valid founders cannot be selected.
- Event details/logs: use `common/scripted_effects/chaosx_events_log_effects.txt` for default actor, history entry, evolution entry, and Event Details evolution previews. Use `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` for Secret Alliance title/body/summary selector branches.
- Dynamic helpers: check `common/scripted_effects/chaosx_dynamic_effects.txt` and `.md` before adding shared dynamic effects. Event-specific helpers belong in `011_secret_alliance_effects.txt` and triggers in `011_secret_alliance_triggers.txt` unless they are genuinely shared.
- Decision/scripted GUI: `015_utopia_manifesto` is the closest full custom UI pattern: `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt` uses `context_type = decision_category`, and `interface/015_utopia_manifesto.gfx` wires static plus `frameAnimatedSpriteType` fallbacks.
- Faction template: `common/factions/templates/holy_realm_mandala_of_nations.txt` plus `common/scripted_effects/003_holy_realm_effects.txt:1347` (`holy_realm_establish_mandala_of_nations`) show template-backed faction creation, global leader target, rules, goals, and member refresh. `anti_zombie_league` shows a threat-response coalition.
- War hook: `common/on_actions/chaosx_on_actions.txt` uses `on_war_relation_added`; `common/on_actions/003_holy_realm_on_actions.txt:41` uses `on_declare_war`. Event 011 should prefer a narrow war on_action hook, not daily/weekly polling.
- Super-event: `common/scripted_guis/chaosx_scripted_gui_super_events.txt` shows `super_event_visible` and close behavior. `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt` maps numeric slots to image/title/desc/action/quote keys. `common/scripted_effects/chaosx_settings_effects.txt` has the settings-aware audio helper `play_current_super_event_audio`.
- Achievements: `common/achievements/chaos_redux_achievements.txt`, `interface/chaosx_achievements.gfx`, and `localisation/english/chaosx_achievements_l_english.yml` are the three required script/GFX/loc surfaces; existing Event 014/015 blocks show multi-achievement event packages.

## Vanilla or reference precedents
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`: `create_faction` is documented as deprecated; prefer `create_faction_from_template` (around line 3105). Relevant effects include `add_to_faction` (2293), `add_to_war` (2359), `create_faction_from_template` (3115), `declare_war_on` (3467), `save_event_target_as` (6496), and `set_faction_name` (6995).
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`: relevant triggers include `can_declare_war_on` (1935), `has_active_mission` (3022), `has_event_target` (3844), `has_war_with` (5051), `is_in_faction` (5686), `is_in_faction_with` (5695), `is_major` (5881).
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/events/Germany.txt`: vanilla diplomacy/faction precedents include Little Entente and other `create_faction_from_template` plus `add_to_faction` flows around lines 2854, 8946, and 11503.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/national_focus/japan.txt`: has faction naming/template examples, including `set_faction_name` around line 9370 and `create_faction_from_template` examples for Japanese pact paths.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/events/AAT_nordic.txt`, `BBA_AfricanUnion_events.txt`, `AAT_Finland.txt`: vanilla `add_to_war` examples for joining existing wars.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/on_actions/00_on_actions.txt`: vanilla on_action hooks include `on_declare_war`, `on_war_relation_added`, `on_peace`, and `on_capitulation`.
- Offline wiki: `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:224` documents `scripted_gui = my_scripted_gui` for decision categories; line 546 recommends using on_actions to activate targeted decisions instead of broad automatic target arrays when possible.
- Offline wiki: `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md:95` documents `frameAnimatedSpriteType`; mirror this plus the repo's Event 015 frame-sheet usage for animated dossier warnings.

## Likely edit order for the parent
1. Lock source of truth: read all four Event 011 spec parts, all matrices, and prompts; reject or queue any conflicting design before writing script.
2. Add constants/triggers/effects first: `011_secret_alliance_constants.txt`, `011_secret_alliance_triggers.txt`, `011_secret_alliance_effects.txt`; include target/founder/member validity, scoring, role assignment, values, invitation, incident, reveal, faction/war, cleanup.
3. Add Event 011 pre-fire availability in the event system: random pool candidate filter and dispatch pre-fire context so Event 011 is unavailable unless exactly three valid non-war founders can be resolved.
4. Add `events/011_secret_alliance.txt` with `chaosx.nr11.1` opening plus follow-up/reveal/evolution events, using event targets where needed and persistent flags/arrays for membership.
5. Add decisions/missions/categories and AI equivalents; wire costs, visibility, target restrictions, cooldowns, and mission expiry effects.
6. Add on_action war reveal hook for member-vs-target wars; keep it event-specific and gated by Secret Alliance flags/targets.
7. Add faction template/rules/goals and dynamic Anti-[target] Pact localisation; test faction creation, member transfer, and all-live-member war join.
8. Add ideas, scripted localisation, event log actor/evolution/detail dispatch, and player-facing localisation.
9. Add GUI/GFX/assets, including static fallbacks and real frame-sheet animated assets; wire super-event image/audio/text.
10. Add achievements and achievement assets after gameplay flags are stable.
11. Add `docs/events/011_secret_alliance.md`, update asset manifests/handoffs, then update spreadsheet/catalog from final in-game wording.
12. Run audits: decision/mission, localisation, event completion, spreadsheet/doc worker, asset/super-event audio review.

## Validation checks
- Spec/package presence: `rg --files docs/specs/011_secret_alliance_specs | sort`.
- Implementation footprint: `rg -n "chaosx\\.nr11|secret_alliance|chaosx.event_name.11" events common localisation interface docs --glob "!docs/specs/011_secret_alliance_specs/**"`.
- Event file/id: `rg -n "add_namespace = chaosx\\.nr11|id = chaosx\\.nr11\\.1|chaosx\\.nr11\\." events/011_secret_alliance.txt`.
- Registration/filtering: `rg -n "global\\.fire_once_events = 11|event_id = 11|secret_alliance.*automatic|secret_alliance.*pre_fire|secret_alliance.*valid_founder" common/scripted_effects common/scripted_triggers common/script_constants`.
- Founder invariant: grep for selection helpers and ensure only non-major/non-war valid founder scopes can be added, exactly three are required, and Event 011 sets unavailable instead of firing if fewer than three resolve.
- Reveal/war: `rg -n "on_war_relation_added|on_declare_war|secret_alliance_reveal_pact_by_war|has_war_with|add_to_war|declare_war_on|create_faction_from_template|set_faction_name|add_to_faction" common/on_actions common/scripted_effects events common/factions`.
- Event logs/details: `rg -n "events_log.*11|secret_alliance.*evolution|GetEventsLog.*SecretAlliance|record_events_log_evolution_entry|chaosx.event_name.11" common/scripted_effects/chaosx_events_log_effects.txt common/scripted_localisation/chaosx_scripted_localisation_events_log.txt localisation/english`.
- Decisions/missions/AI: `rg -n "secret_alliance_dossier|trace_courier_routes|audit_foreign_payments|watch_suspect_frontier|expose_secret_protocol|issue_counter_ultimatum|strike_first|ai_will_do" common/decisions common/decisions/categories common/scripted_guis localisation/english`.
- Assets: `rg --files gfx interface docs/assets | rg "011_secret_alliance|secret_alliance"` and `rg -n "GFX_.*secret_alliance|frameAnimatedSpriteType" interface`.
- Super-event/audio: `rg -n "GFX_super_event_secret_alliance_reveal|super_event_secret_alliance|current_super_event_audio_id|chaosx_super_event\\." common/scripted_localisation interface localisation/english music sound common/scripted_effects`.
- Achievements: `rg -n "secret_alliance|GFX_achievement_011_secret_alliance" common/achievements interface/chaosx_achievements.gfx localisation/english/chaosx_achievements_l_english.yml`.
- Missing loc/assets: for every event/decision/idea/achievement/super-event id, confirm matching localisation key and GFX sprite exists.
- Spreadsheet/doc alignment: after implementation, compare final Event Details/event log localisation against `docs/spreadsheets/chaos_redux_events_catalog.xlsx`; do not import planning text as final wording.

## Pre-Implementation Gaps Recorded By Explorer

- Event 011 gameplay implementation had not yet been written beyond registration and the reserved event name.
- Secret Alliance final assets, animated frame sheets, achievement icons, and licensed reveal audio were not present at exploration time.
- No researched super-event text/audio handoff was found outside the spec package at exploration time.
- No Event 011 docs/events page or spreadsheet final row update existed at exploration time.

Ordinary risks:
- Event 011 is already in `global.fire_once_events`; without a pre-fire availability gate it can dispatch via generic `chaosx.nr11.1` even when three founders cannot be selected.
- Founder/member arrays can desynchronize if roles, confidence, readiness, and member status are stored in parallel arrays without a single refresh/cleanup path.
- Dynamic Anti-[target] Pact naming may need careful `create_faction_from_template` plus `set_faction_name`/scripted localisation validation.
- War reveal must be hooked through `on_war_relation_added` or `on_declare_war`; do not solve with broad daily/weekly world iteration unless the user explicitly approves.
- Localisation must preserve secrecy stages; early event logs/details must not leak hidden founders/members.
- Super-event slot collision is possible. Pick an unused `super_event_visible` value only after scanning all branches in `chaosx_scripted_localisation_super_events.txt`.
- Decision GUI buttons need equivalent AI paths; scripted GUI click effects are player-only unless separate AI decisions/effects exist.
- Achievements need stable flags for eligibility, disqualifiers, and completion. Do not key them only off transient event targets.

## Recommended next action
Start implementation with the scripted architecture tranche: constants, triggers, effects, and the random/manual pre-fire availability gate. Do not add event text, decisions, assets, achievements, or spreadsheet rows until founder selection, member persistence, reveal, cleanup, faction creation, and war-join helpers are stable.
