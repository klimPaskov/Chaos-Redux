# Repo Explorer Handoff

## Scope read

- Parent task: map touched files, Chaos Redux precedents, vanilla precedents, risks, and validation order for implementing Event 010 Death.
- Explicit constraints: report only; do not edit gameplay, localisation, GUI, GFX, assets, country, history, decision, focus, scripted effect, scripted trigger, on-action, achievement, docs, or spreadsheet implementation files. Event 010 completely replaces Spirit of War/Peace.
- Corrected scenario ID: `SCN-006` is the active triggerable scenario ID. Earlier prompt wording used a stale alternate scenario number, but the source prompts now match the parent correction and `docs/specs/010_death_specs/specs/010_death_spec_part_2_mechanics.md:413`.
- Files or ids requested: `chaosx.nr10`, event ID `10`, Death tag `DTH`, leader `Zol`, Death country package, special chaos/nonhuman classification, state consumption helpers, decisions/missions, triggerable scenario `SCN-006`, super-events, assets, achievements, docs, spreadsheet, old Spirit references, validation commands.
- Skills and docs read: `AGENTS.md`, `CHAOS_REDUX_MECHANICS.md`, `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-event-assets`, `chaos-redux-super-events`, `hoi4-decisions-missions`, `hoi4-focus-trees`, all requested Event 010 Death specs, matrices, and coding prompt.
- Offline wiki pages consulted before Chaos Redux implementation-file inspection: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Country creation, State modding, Map modding, Achievement modding, National focus modding, Interface modding, Scripted GUI modding, Graphical asset modding, Unit modding, Division modding.
- Vanilla docs/examples consulted or searched under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`: `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, `documentation/script_concept_documentation.md`, `documentation/loc_objects_documentation.md`, `common/script_constants/documentation.md`, plus vanilla `events`, `common/decisions`, `common/achievements`, `common/country_tags`, `common/countries`, `common/national_focus`, and `history/units`.

## Primary findings

Event 010 is still the old Spirit of War/Peace implementation in active files. It already sits in the fire-once event category, but its event script, localisation, event-name mapping, news comments, old ideas, and catalog-facing details are stale for Death.

The Death spec and the parent correction require triggerable scenario `SCN-006`; the active implementation should not create another Death scenario id.

No `DTH`/`Zol` country package exists in the mod search surface. A partial Death asset staging directory exists, but only the `Country Without Breath` idea source/processed PNG and Zol contact sheets were found. Death super-event text and audio research docs do exist under `docs/super_events/`.

There is already a scripted-system architecture handoff at `docs/plans/010_death_plans/subagent_handoffs/scripted_system_architect_handoff.md`. It is report-only, not implementation, and it agrees with `SCN-006`.

## Relevant files

| Path | Why it matters | Evidence |
| --- | --- | --- |
| `events/010_war_or_peace_symbol.txt` | Active Event 010 script to replace or rename into Death. | `add_namespace = chaosx.nr10` at line 1; root `chaosx.nr10.1` at lines 22-35; old option event `chaosx.nr10.2` uses `GFX_report_event_war_or_peace` and adds `symbol_of_war`/`symbol_of_peace` at lines 39-80. |
| `localisation/english/010_war_or_peace_symbol_l_english.yml` | Active Event 010 localisation is entirely old War/Peace text. | `chaosx.nr10.1.t: "Symbol of War/Peace"` at line 2; old news keys `chaosx.news.7`/`.8` at lines 27-33. |
| `events/_chaosx_news.txt` | Old Event 010 news event comments and images remain. | Lines 159-183 label `chaosx.nr10` as War or Peace Symbol and wire `GFX_news_symbol_of_war`/`GFX_news_symbol_of_peace`. |
| `localisation/english/chaosx_event_names_l_english.yml` | Event picker/log name source. | `chaosx.event_name.10: "War or Peace Symbol"` at line 12. |
| `common/scripted_effects/chaosx_logic_effects.txt` | Event category registration. | `global.fire_once_events = 10` at line 156; comment is old but category matches Death's minor fire-once requirement. |
| `common/scripted_localisation/chaosx_scripted_localisation_debug.txt` | Debug/event-name selector. | `GetEventName` maps ID 10 to `chaosx.event_name.10` at line 62. |
| `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` | Event log names, event-detail text selectors, evolution detail selectors. | Search found `chaosx.event_name.10` mappings at lines 7955 and 9481; Death needs event-detail/evolution branches and loc keys. |
| `common/scripted_effects/chaosx_events_log_effects.txt` | History/event-detail/evolution arrays and default actor handling. | Skill contract places event details, evolution preview rows, actor sanitizing, and history entries here. Death needs actor mapping to `DTH`/origin/reveal actor and five evolution milestones. |
| `localisation/english/chaosx_gui_l_english.yml` | Scenario UI text, event detail text, evolution detail localisation. | Existing scenario loc is at lines 80-167; event details for current events are lines 530-536. Death needs scenario name/ID/type/impact/result plus event-detail/evolution text. |
| `common/script_constants/chaosx_triggerable_scenarios_constants.txt` | Scenario IDs, sort values, type constants. | IDs currently run 1-5 at lines 9-20. Death should add `triggerable_scenario_id.death = 6` and Death type constants. |
| `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt` | Scenario registry, sorting, type cycling, launch dispatch. | Defaults at lines 9-43; registry at lines 46-89; hardcoded sort view begins lines 91-140; type cycling at lines 394-478; launch dispatch at lines 480-544. |
| `common/scripted_triggers/chaosx_triggerable_scenarios_triggers.txt` | Scenario launch enablement. | `triggerable_scenario_can_launch_selected` has explicit branches for IDs 1-5 at lines 16-48. Add a Death branch that blocks only impossible/conflicting `SCN-006` setups. |
| `common/scripted_guis/chaosx_scripted_gui_settings.txt` | Scenario window scripted GUI controls. | Existing scenario buttons use generic selected/type/intensity state; no layout change appears required unless Death needs custom blocked-reason display. |
| `common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt` | Scenario name, entry ID, description, type, warning/impact text. | `GetTriggerableScenarioSelectedName` lines 1-30, entry name/id lines 32-92, description lines 120-180, type/warning branches lines 360-509 are explicit lists. |
| `docs/systems/triggerable_scenarios.md` | Scenario documentation and acceptance boundary. | Current docs list `SCN-001` through `SCN-004` at lines 47-73 and describe the launch gate at lines 36-43. Add `SCN-006`; do not renumber existing scenarios. |
| `docs/plans/010_death_plans/subagent_handoffs/scripted_system_architect_handoff.md` | Existing Death helper architecture map. | Lines 1-6 mark report-only and active `SCN-006`; lines 32-55 list recommended files; lines 124-167 map `SCN-006`; lines 244-287 give edit/risk order. |
| `common/scripted_triggers/chaosx_dynamic_triggers.txt` and `.md` | Special chaos and nonhuman classification. | `is_special_chaos_country` lines 101-119 and `is_actual_nonhuman_country` lines 121-131 do not include Death. |
| `common/scripted_effects/chaosx_dynamic_effects.txt` and `.md` | World-threat aggregator. | `refresh_world_threat_state` counts zombies, Holy Realm, Mengele, and Fury at lines 462-489. Add `world_threat_source_death` and update docs. |
| `common/scripted_triggers/chaosx_world_threat_triggers.txt` | World-threat source query triggers. | Existing triggers cover zombies, Holy Realm, and Mengele; Death needs `has_world_threat_source_death`. Fury source also exists in effects but appears not mirrored here, so check whether to add both missing query triggers or only Death. |
| `docs/systems/world_threat_mechanic.md` | World-threat docs. | Lines 17-19 list existing source flags; lines 50-54 describe `refresh_world_threat_state`; lines 93-95 list query triggers. |
| `common/script_constants/chaos_meter_constants.txt` | Death reason and reduced chaos contribution. | `chaos_meter_deaths.million_for_chaos = 1000000` and `zombie_outbreak_decay_chaos_weight = 0.10` at lines 346-354; reason constants at lines 362-380. |
| `common/scripted_effects/chaos_meter_effects.txt` | Shared deaths and state-population pipeline. | `chaos_meter_register_state_civilian_deaths_percent` lines 2879-2997 calculates state deaths, applies state population loss, and calls `chaos_meter_register_deaths`. Death should add an exact-consumption helper/reason rather than parallel casualty accounting. |
| `common/scripted_effects/002_zombie_outbreak_effects.txt` | Closest state-population precedent. | `zombie_apply_state_population_decay` lines 238-247 sets death parameters and calls the shared pipeline. |
| `docs/biological_warfare/zombie_state_decay_and_civilian_deaths.md` | Documents the 10:1 chaos contribution model. | Lines 79-92 state the shared pipeline reduces state population, logs deaths, and zombie occupation deaths contribute at `10:1`. Death spec asks the same reduced model for consumed population. |
| `common/ideas/chaosx_ideas.txt` and `localisation/english/chaosx_ideas_l_english.yml` | Old Spirit ideas still exist. | `symbol_of_peace` and `symbol_of_war` definitions are at `chaosx_ideas.txt:333` and `:359`; loc at `chaosx_ideas_l_english.yml:26-29`. They may be left if reused elsewhere, but Event 010 must stop granting/referencing them. |
| `interface/chaosx_pictures.gfx` | Old War/Peace sprites still registered and reused by Event 004. | `GFX_news_symbol_of_war`, `GFX_news_symbol_of_peace`, and `GFX_report_event_war_or_peace` are at lines 44-57. Event 004 still uses `GFX_report_event_war_or_peace`, so do not delete the sprite blindly. |
| `common/achievements/chaos_redux_achievements.txt` | Custom achievement definitions. | `unique_id = chaos_redux_achievements` at line 8; comments at line 6 say icon art resolves from `gfx/achievements/<achievement_id>*.dds`. |
| `localisation/english/chaosx_achievements_l_english.yml` | Achievement names/descriptions/tooltips. | Existing achievement loc uses triplets such as Fury keys at lines 344-373. Death achievements need matching keys. |
| `interface/chaosx_achievements.gfx` | Achievement sprite aliases. | Existing pattern is `GFX_achievement_<id>` with normal/grey/not-eligible variants; Death icon files need matching aliases if the UI requires them. |
| `docs/specs/010_death_specs/specs/010_death_assets_super_events_achievements.md` | Source-of-truth asset/super-event/achievement requirements. | Lists required Death report/news/super-event images, icons, and first-priority achievements; acceptance criteria include triggerable scenario, docs, and spreadsheet. |
| `docs/super_events/010_death_super_event_text_research.md` | Researched Death super-event text source. | Contains final/backup title, button, and quote selections for Death roles. Use this rather than inventing final text. |
| `docs/super_events/010_death_super_event_audio_research.md` | Researched Death super-event audio source. | Lines 35-39, 63-67, 91-95, and 119-123 specify final `.ogg` paths and suggested music/sound IDs for reveal, world-end, defeat aftermath, and world consumed. |
| `docs/assets/010_death/` | Partial asset staging. | Found only Zol contact sheets and `idea_country_without_breath` source/processed PNGs. No final DDS, flags, report/news/super-event images, or achievement icons were found in the searched Death asset folders. |
| `docs/spreadsheets/chaos_redux_events_catalog.xlsx` | Event catalog spreadsheet. | `chaos-redux-events` skill names it as required after implementation. Update Event 010 row only after final Event Details/evolution wording exists. |

## Existing patterns

The nearest Death implementation pattern is a combination of Zombie Outbreak, Fury, Holy Realm/Final Silence, and the triggerable scenario framework.

Zombie Outbreak provides the state-population/deaths precedent. `common/scripted_effects/002_zombie_outbreak_effects.txt:238-247` sets death-percent variables and calls `chaos_meter_register_state_civilian_deaths_percent`; `common/scripted_effects/chaos_meter_effects.txt:2879-2997` handles state population reduction and the deaths ledger. Death should not create a separate deaths UI or chaos pipeline. Add a Death reason and 0.10 chaos-weight branch parallel to zombie decay.

Fury provides the best scenario/intensity pattern. `common/scripted_effects/007_fury_effects.txt:1821-1825` translates scenario intensity into actor count, and `:2204-2265` stores launch globals, marks scenario flags, creates actors, and handles pact/hostile type behavior. Death can mirror this with `trigger_death_scenario`, type globals, intensity scale, and cleanup flags.

Holy Realm/Final Silence and Zombie Outbreak provide world-end and world-threat patterns. `refresh_world_threat_state` is intentionally a shared aggregator; Death should set/clear `world_threat_source_death` only at reveal/world-end/defeat boundaries, then call the shared refresh. Avoid daily threat polling.

The Event Log system is centralized. Event name mappings in `chaosx_event_names_l_english.yml`, debug name selectors, event-detail localisation, event-detail previews, and evolution details must all be updated together. Death has five mutation/evolution milestones in the spec; baseline stages should not be logged as evolutions.

The triggerable scenario system is only partly data-driven. Arrays and scripted localisation are generic, but registry, sort order, selected name, entry ID, descriptions, type cycling, warning text, launch dispatch, and launch enablement are explicit branch lists. Death must be added to every list or the UI will show a partial/broken scenario.

The scripted-system architect handoff is highly relevant and should be read immediately before patching. It proposes `common/script_constants/010_death_constants.txt`, `common/scripted_effects/010_death_effects.txt`, `common/scripted_triggers/010_death_triggers.txt`, `common/on_actions/010_death_on_actions.txt`, `common/modifiers/010_death_modifiers.txt`, and `events/010_death.txt`, plus shared updates. It also warns against broad daily scans and validates `SCN-006`.

## Vanilla or reference precedents

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`: authoritative references for `save_event_target_as`, `transfer_state_to`, `add_core_of`, `remove_building`, `set_building_level`, `add_extra_state_shared_building_slots`, `modify_building_resources`, `create_country_leader`, and `load_focus_tree`. These are the key effects for Death country creation, state consumption, wasteland stripping, leader setup, and runtime focus loading.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`: authoritative references for `has_event_target`, resource triggers, custom achievement checks, and variable comparison forms.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md` and `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/script_constants/documentation.md`: required source for `script_constants`; use `constant:category.key` for shared Death tuning where supported.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/country_tags/00_countries.txt`, `/common/countries/`, `/history/countries/`: vanilla country package layout. A targeted vanilla/mod search found no `DTH` tag assignment; only unrelated `Zoltan/Zoltán` localisation hits, so `DTH` appears available but still needs a final exact tag check during implementation.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/events/`: vanilla `add_namespace`, `country_event`, hidden triggered event, and news-event structure. Death should keep `chaosx.nr10.1` as the hidden root entry and move public reveal/terminal popups into separate events.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/`: vanilla category/decision/available/visible/fire-only-once patterns. Death decisions should use ordinary decisions and targeted decisions, not a separate mission layer unless the spec changes.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/achievements/`: vanilla achievement syntax precedent, but Chaos Redux custom achievements already provide the stronger local pattern in `common/achievements/chaos_redux_achievements.txt`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/national_focus/generic.txt` and other focus files: vanilla focus-tree syntax and icon expectations. For `DTH`, prefer runtime loading from Death creation if the tree is not available at game start.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/units/`: vanilla OOB and division-template syntax. Death should have no normal starting units; ghost hosts should be spawned by scripted helpers when the stage/scenario calls for them.

No Kaiserreich or other large-mod reference was needed for the repo map; vanilla docs and existing Chaos Redux patterns answer the touched systems.

## Likely edit order for the parent

1. Keep every live implementation surface on `SCN-006`; do not create another Death scenario id.
2. Replace the old Event 010 script surface: move/rework `events/010_war_or_peace_symbol.txt` into a Death event file while preserving namespace `chaosx.nr10` and root event `chaosx.nr10.1`.
3. Add Death constants and shared reason IDs: Death tuning constants, scenario type/scale constants, `triggerable_scenario_id.death = 6`, and Death deaths reason/0.10 chaos weight.
4. Add Death country package before helpers that target `DTH`: country tag, country definition/color, history file, leader/portrait references, flags, country loc, empty/no-unit starting posture, and runtime focus loading if used.
5. Add Death triggers and effects: origin selection, country creation, consumption, wasteland stripping, death registering, spread pressure, wither, coastal jumps, ghost hosts, defeat cleanup, and world-threat refresh.
6. Add narrow hooks only: specific `on_state_control_changed`/capitulation-style wrappers for recapture/defeat, plus scheduled hidden `DTH` events for spread pulses. Do not add broad daily/weekly/monthly world scans without explicit parent/user approval.
7. Wire entry event, hidden pulse events, reveal event, defeat event, terminal world-end event, and final world-consumed event to the helper layer.
8. Register special classifications: `is_special_chaos_country`, `is_actual_nonhuman_country`, world-threat source/triggers/docs, and any normal-civilian-system exclusions.
9. Add decisions and state decisions: containment, quarantine, wither blocking/purification, Dark Methods, Black Oath if implemented; otherwise hide/queue clearly rather than shipping placeholder buttons.
10. Add `SCN-006` integration: constants, registry, sorting, GUI branch lists, scripted localisation, launch trigger, launch effect, result event `chaosx.triggerable_scenarios.6`, docs, and settings export/import if scenario type persistence matters.
11. Wire event log and evolution details: event name, debug selector, default actor mapping, event-details body, five mutation/evolution rows, evolution detail titles/bodies, and history/evolution logging calls.
12. Wire super-events from research docs: allocate unused slots, add localisation, sprite(s), music/sound definitions, scripted localisation selectors, display effects, audio IDs, quote-source/audio docs, and final image/audio files or explicit blockers.
13. Wire assets: `.gfx` sprites for report/news/super-event images, ideas, decisions, focus icons, achievements, leaders/flags; produce/copy placeholders only where required by repo asset rules.
14. Add achievements and achievement flags after gameplay facts exist: definitions, loc triplets, icon variants, `.gfx` if required, and scenario/world-end/containment trigger flags.
15. Update docs after implementation facts stabilize: `docs/events/010_death.md`, world threat docs, triggerable scenario docs, asset manifests, super-event audio/quote docs, helper docs if shared dynamic helpers changed.
16. Update `docs/spreadsheets/chaos_redux_events_catalog.xlsx` last, using final in-game Event Details/evolution wording and the `xlsx` workflow.

## Validation checks

Run these after implementation, in this order:

```bash
rg -n "War or Peace|War/Peace|Spirit of War|Spirit of Peace|010_war_or_peace|WAR OR PEACE|symbol_of_war|symbol_of_peace" events common localisation docs interface
```

```bash
rg -n "SCN-006|triggerable_scenario_id\\.death|triggerable_scenarios_death|death_scenario" common docs localisation interface events
```

```bash
rg -n "add_namespace = chaosx\\.nr10|id = chaosx\\.nr10\\.|chaosx\\.event_name\\.10|event_id = 10|global\\.fire_once_events = 10" events common localisation
```

```bash
rg -n "^\\s*DTH\\s*=|\\bDTH\\b|Zol" common/country_tags common/countries history/countries common/characters localisation/english
rg -n "^\\s*DTH\\s*=|\\bDTH\\b|Zol" "C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/country_tags" "C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/countries" "C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries" "C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/characters" "C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/localisation/english"
```

```bash
rg -n "is_special_chaos_country|is_actual_nonhuman_country|is_death_country|DTH|world_threat_source_death|has_world_threat_source_death|refresh_world_threat_state" common/scripted_triggers common/scripted_effects docs/systems
```

```bash
rg -n "death_consume|death_consumed|death_wither|death_coastal|death_ghost|death_reveal|death_world_end|death_defeat|death_country_created|death_publicly_revealed" common events localisation docs
```

```bash
rg -n "death_consumption|chaos_meter_deaths_reason|zombie_outbreak_decay_chaos_weight|death_.*chaos_weight|chaos_meter_register_deaths|chaos_meter_register_state_civilian_deaths_percent" common/script_constants common/scripted_effects common/scripted_localisation localisation/english docs
```

```bash
rg -n "chaosx.events_log.*death|death.*evolution|chaosx.event_name.10|events_log.*10|GetEventName" common/scripted_localisation common/scripted_effects localisation/english/chaosx_gui_l_english.yml localisation/english/chaosx_event_names_l_english.yml
```

```bash
find gfx/achievements gfx/event_pictures/010_death gfx/super_events/010_death gfx/interface gfx/leaders/010_death docs/assets/010_death -iname '*death*' -o -iname '*zol*' | sort
rg -n "GFX_.*death|super_event_death|report_event_death|news_event_death|decision_death|idea_.*death|leader_zol|DTH" interface common localisation docs
```

```bash
rg -n "death_before_the_name|death_not_on_my_continent|death_the_names_do_not_come_back|death_black_tide_reversed|death_no_witnesses|achievement_.*death" common/achievements localisation/english interface gfx/achievements docs
```

```bash
rg -n "<=|>=" events common localisation interface docs/events docs/systems docs/specs/010_death_specs
```

```bash
rg -n "on_daily|on_weekly|on_monthly|every_country|every_state|all_state|random_state" common/on_actions common/scripted_effects/010_death* common/scripted_triggers/010_death* events/010_death*
```

For spreadsheet validation after the final workbook edit, use the `xlsx` skill if available and at minimum run:

```bash
unzip -t docs/spreadsheets/chaos_redux_events_catalog.xlsx
libreoffice --headless --convert-to xlsx --outdir C:/Users/klimp/AppData/Local/Temp/chaosx_catalog_validate_010 docs/spreadsheets/chaos_redux_events_catalog.xlsx
```

Manual scenario checks to document after patching:

- Natural Event 010 creates `DTH`, consumes a remote origin, and does not show the public reveal immediately.
- `SCN-006` has since been superseded by one Instant Outbreak type. It launches without chaos, date, report, or evolution gates.
- Instant Outbreak consumes a hidden island origin, intensity-scaled extra islands, at least one mainland reveal state, and intensity-scaled starting hosts. It sets the normal public reveal through shared consumption without starting world-end.
- Consumed state population is removed, deaths are visible in the deaths UI with a Death cause, and chaos contribution follows the intended 10:1 rate.
- Recapture changes active wasteland to recaptured wasteland and does not leave stale wither targets.
- Death defeat clears world-threat state, stops pulse events, and does not leave active `DTH` ghosts or global event targets.

## Risks and blockers

Confirmed blockers:

- Earlier prompt wording used a stale scenario number. Active implementation must use `SCN-006`.
- No `DTH`/`Zol` country package was found in the mod search surface. Implementation must add it before helper/event code can safely target Death.
- Death final asset coverage is incomplete in searched folders. Found only `docs/assets/010_death/source_png/idea_country_without_breath_source.png`, processed variants, and Zol contact sheets; no final Death DDS/report/news/super-event/achievement/flag package was found.

Ordinary risks:

- Event 010 old Spirit references are spread across event script, localisation, news events, event-name loc, old ideas, and picture sprites. Deleting old sprites/ideas blindly is unsafe because `events/004_random_war.txt` still uses `GFX_report_event_war_or_peace`.
- Scenario UI branch lists are easy to miss. Adding only a constant will not make Death usable in the scenario window.
- State consumption is high-risk script: building/resource removal, population loss, transfer/core/controller order, state modifiers, arrays, and death ledger calls must stay in one helper to avoid divergent behavior.
- Direct resource removal and dynamic building removal may be unsupported or limited. Validate against vanilla docs and use explicit building blocks/modifiers where needed.
- Division presence in a state for wither blocking needs exact scope validation before writing final triggers.
- Global event targets persist and must be cleared. Prefer regular event targets for short chains and arrays/flags for long-lived active state tracking.
- Broad daily/weekly/monthly world scans conflict with AGENTS.md unless explicitly approved. Death should schedule pulses from `DTH` and react to scoped on-actions.
- Death achievements depend on final gameplay flags. Add achievement definitions only after the flag-setting points are real.
- Event Details and spreadsheet text must not expose mechanics or implementation history. Update spreadsheet last so it mirrors final in-game wording.

## Recommended next action

Start implementation from the scripted-system architecture handoff and the `SCN-006` correction: add the Death constants/country package and replace the old Event 010 root with helper-backed Death setup before touching decisions, scenario UI, super-events, or achievements.
