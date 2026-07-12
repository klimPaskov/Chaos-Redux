# Event 018 localisation audit handoff

Date: 2026-07-11  
Subagent: `chaosx_localisation_auditor`  
Audit status: **passes static localisation reconciliation and chronology-gated Event Details spoiler checks**

## Scope and references

This audit covered every Event 018 player-facing or dynamically selected string reachable through events, decisions and missions, the selected-field GUI, focuses, ideas, dynamic modifiers, country identity, characters, traits, units, opinion modifiers, achievements, news, super-events, music, event-name/settings mappings, history rows, Event Details, Evolution Details, and the economy-positive cluster description.

Required project guidance was read before the audit:

- `AGENTS.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- all 26 files under `docs/specs/018_resources_found_specs/`
- offline wiki pages for Localisation, Data structures, Scopes, Event modding, Decision modding, AI modding, Triggers, Effects, Modifiers, On actions, Idea modding, Interface Modding, Scripted GUI Modding, Focus modding, Country creation, Achievements, and Music
- vanilla documentation for localisation formatters and objects, decisions, scripted GUI, on actions, script concepts, effects, triggers, and custom tooltips, together with vanilla scripted-localisation, prospecting, resource-discovery, and achievement precedents

No web copy of the Paradox wiki was used.

## Files changed

### `localisation/english/018_random_resource_l_english.yml`

Small wording corrections were made without changing event structure or effects:

- `chaosx.nr18.15.a.tt` no longer reveals a cave emergence before that route is public.
- Repetitive or implementation-like casualty wording was replaced in the Event 57, 62, 64, 67, and 69 text families. Their tooltips still state the real population loss.
- `chaosx.nr18.68.a.tt` no longer names a cave host before emergence.
- `chaosx.nr18.85.d` now reads grammatically as making recapture the first priority.
- `chaosx.nr18.92.d` and the `chaosx.nr18.94` text family describe the continental danger, distant sounding, and 60-day proof of rule without terminal-gallery or protected-state language.
- `chaosx.nr18.95.d` and `chaosx.nr18.95.a.tt` describe the World Below and its distant footholds in-world instead of describing terminal inputs or a state transition.
- `chaosx.nr18.96.d` uses an in-world distant gallery instead of a terminal gallery.

### `localisation/english/018_resources_found_decisions_l_english.yml`

- `resources_found_refresh_evolution_clocks`, `_desc`, and `_tt` now describe field assessments rather than an Event 018 process.
- `resources_found_emergency_suspension_tt`, `resources_found_field_project_mission_tt`, and `resources_found_trade_project_mission_tt` no longer expose hidden disturbance, breach, cave-origin, or cave-conversion information during the ordinary field phase.
- Commission, stabilization, partial-closure, full-seal, ordinary-closure, continent-verification, distant-rupture, and World Below strings were changed from engine/callback/evolution/gate language to current-world outcomes.
- `resources_found_begin_full_sealing_desc`, `_tt`, and `resources_found_close_ordinary_field_exactly_tt` now state that the registered discovery deposits are the resources removed.
- `resources_found_cave_choose_stone_spawn_tt`, `resources_found_cave_choose_burrow_spawn_tt`, and `resources_found_cave_choose_scree_spawn_tt` now identify their actual preferred brood types instead of sharing an indistinguishable sentence.
- Three unused cost-preview families were removed: `resources_found_project_estimate_c12_d4`, `resources_found_project_estimate_c12_d5`, and `resources_found_project_estimate_c8_d1`, including each `_blocked` and `_tooltip` variant. They had no live `custom_cost_text` reference anywhere in the repository.

### `localisation/english/018_resources_found_system_l_english.yml`

- `resources_found.gui.animation.tt` describes the intentional still presentation rather than calling it a fallback.
- The active-anchor and `DHO_activate_resource_anchors_tt` capacity text uses the actual maximum of 10 without implementation-history language.
- Focus tooltips under `DHO_*` were rewritten where they described AI behavior, candidate arrays, route completion, enabled settings, exact internal state rebuilds, or terminal gates. The affected groups include the first-breach, hierarchy, command, vault/network, doctrine-capstone, continental verification, distant-shore, first-rupture, and World Below branches.
- `resources_found.evolution.stage_1.body` and `resources_found.evolution.stage_2.body` describe the in-world ledger and lower workings instead of duplicate rolls or an incident chain.

### `localisation/english/chaosx_achievements_l_english.yml`

Five achievement condition tooltips were made mechanically complete:

- `resources_found_achievement_thirty_from_below_tooltip`
- `resources_found_achievement_last_shaft_closed_tooltip`
- `resources_found_achievement_ten_from_one_state_tooltip`
- `resources_found_achievement_continental_appetite_tooltip`
- `resources_found_achievement_ground_quiet_again_tooltip`

The revised text exposes the actual thresholds and end-state requirements, including 30 starting divisions, three cleanup contributions, maximum 10-anchor capacity, the World Below foothold requirement, and global reconstruction after all Host territory/chambers are cleared.

No gameplay, assets, interface layout, workbook, or unrelated localisation was edited. No commit was created from the shared dirty worktree.

### Root follow-up patch re-audited

The parent subsequently patched the previously reported Event Details spoiler path. This subagent re-audited, but did not modify, the following implementation files:

- `common/scripted_triggers/018_resources_found_triggers.txt`
- `common/scripted_triggers/chaosx_settings_triggers.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `localisation/english/018_resources_found_system_l_english.yml`

The re-audit found no remaining small Event 018-local defect. Only this handoff was changed during the follow-up pass.

## Coverage and reconciliation evidence

### Primary localisation accounting

| Surface | Defined keys | Live coverage result |
| --- | ---: | --- |
| Event script | 562 | 77 unique Event 018 IDs produce 562 unique title, description, option, and tooltip references. Missing 0, orphaned 0. |
| Decisions and missions | 486 | 123 rendered IDs each have a name and description, 119 operational tooltip keys are live, 40 live cost bases have all 120 base/blocked/tooltip variants, and one research-bonus name is live. Missing 0, orphaned 0. |
| System/local UI | 469 | Exact accounting below. Missing 0 within each automatic or explicit consumer set. |
| **Primary total** | **1,517** | **1,517 unique keys, duplicate definitions 0.** |

The 132 top-level Event 018 decisions/missions consist of 123 rendered entries and nine internal evolution clock missions. The nine clock IDs have `visible = { always = no }` inside the permanently hidden clock category and deliberately have no localisation.

The 469 system keys reconcile as follows:

- 26 country, cosmetic-country, and party identity keys
- 2 ideology keys
- 5 character name/description keys
- 14 leader-trait keys for 7 traits
- 10 subunit keys for 5 brood types
- 10 decision-category keys for 5 visible categories
- 49 selected-field GUI/band keys: 19 GUI references and 30 dynamically selected band labels
- 12 super-event keys for display slots 82, 83, and 84
- 54 idea keys for 27 ideas
- 34 dynamic-modifier keys for 17 modifiers
- 12 opinion-modifier names
- 196 focus-tree/focus keys, including 65 focus names, 65 descriptions, 65 effect tooltips, and the tree name
- 27 event-detail, history-payload, evolution-detail, and unrevealed-stage mask keys
- 18 news keys for 6 news events

Additional shared-file coverage:

- 15 achievements have all 30 `_NAME`/`_DESC` keys and all 18 unique eligibility/condition tooltips.
- `chaosx.event_name.18` is defined as `Resources Found` and is selected by the event list, settings/detail, and log mappings.
- The economy-positive cluster description identifies Resources Found as a medium-severity repeatable event and reveals only its safe economic premise.
- Super-event display slots 82/83/84 map to the Event 018 image, title, quote, remark, and body keys. Audio IDs 54/55/56 each have all six volume-variant music names localised, and the playlist entries select the `_1_5` variants.
- The `DHO_WORLD_BELOW` cosmetic tag is used by the transformation and has name, definite-name, and adjective localisation.

### Dynamic localisation and formatting

- All nine `GetResourcesFound*` calls used by Event 018 localisation resolve to defined scripted-localisation blocks.
- `018_resources_found_scripted_localisation.txt` contains seven defined-text blocks and 37 unique mapped localisation keys. Missing mappings: 0.
- The resource-name mappings cover oil, aluminium, rubber, tungsten, steel, chromium, and an explicit default unknown label. The history-mode mapping covers discovery and enrichment.
- The six selected-field values use five ordered bands each. Their checks are top-down at values greater than 80, 60, 40, and 20, followed by the lowest band.
- The 561 numeric preview tokens in decision localisation all use integer formatting (`|0` or `|Y0`). The 16 numeric selected-field/history tokens in system localisation use `|0`. The remaining `[?scope.GetName]` tokens are scope-name lookups, not numbers.
- The Event Details history row uses the recorded state, resource, added amount, and post-find ledger total. Amount and total are integer-formatted.
- Square-bracket and colour-control pairs are balanced on all Event 018 strings. HOI4 icon tokens use the normal single-leading icon-marker form.
- All seven relevant localisation files are UTF-8 with BOM. There are no `:0` keys. Event 018 final text contains no em dash or semicolon sentences.

### Spoiler and prose checks

- The 114 localisation lines for baseline events `chaosx.nr18.1` through `.15` contain no cave, Host, Oth-Kesh, monster, breach, emergence, chamber, or World Below reveal.
- `resources_found.event_details.description`, the history row, and the economy-positive cluster description remain premise-safe.
- The primary Event 018 strings contain no player-facing `capped`, `fallback`, `hardcoded`, `reworked`, `newly added`, `implementation`, `callback`, `Event 018`, `Evolution I-IV`, candidate-array, route-completion, enabled-setting, or terminal-state/gate language.
- Exact duplicate values longer than 20 characters occur in seven pairs only. Each is an intentional shared semantic label: domestic charter option text, regional-defeat event/news title, mission/decision title pairs, the selected-field header, and idea/focus names for Interlocking Carapaces and Urban Cellar Networks.
- The repeated casualty-result prose and three indistinguishable brood-preference tooltips were replaced with specific text.

### Mechanics-to-wording spot checks

- Achievement thresholds match the scripted constants and triggers: one-vein 400, maximum emergence 30, cleanup contribution 3, full anchor capacity 10, large cave army 25 divisions and 4 anchors, and the Scree Tide milestone of 5 states and 2 defeated countries.
- Focus/idea descriptions retain the implemented hierarchy, doctrine, adaptation, anchor-capacity, spawn-timing, 120-day Burrow disruption, chaos strictly above 1000, and 60-day verification values.
- Full-seal and ordinary-closure text correctly distinguishes removal of Event 018's six registered discovery deposits from unrelated state resources.
- The selected-field GUI is evaluated in decision-category context. Disturbance and breach rows remain hidden until their respective reveal flags are present.

## Resolved finding: chronology-gated Event Details masking

The parent patch resolves the previously reported spoiler without removing the Event Details settings catalog:

1. `events_log_rebuild_open_event_details_view` still appends exactly four Event 018 preview rows, one for each stage. The preview builder contains no chronology gate.
2. `events_log_add_event_detail_evolution_preview` still derives each checkbox state only from the matching disabled-evolution flag. Both enabled and disabled checkbox branches remain visible as appropriate, and both click-enabled triggers remain `always = yes`.
3. `resources_found_selected_evolution_is_public` maps stages I, II, III, and IV one-to-one to `resources_found_evolution_i_chronology_recorded`, `_ii_`, `_iii_`, and `_iv_` respectively. It also requires the Event 018 event ID and evolution type.
4. `GetEventsLogEventDetailEvolutionTitle` places four chronology-negative mask branches above the four authored title branches. Scripted localisation selects the first matching branch, so an unrecorded row shows `Unrecorded Development I-IV`. Once that stage's chronology flag exists, its mask branch fails and its real title is the first matching result.
5. `GetEventsLogSelectedEvolutionTitle` uses the same stage-specific order for the opened detail title.
6. `GetEventsLogSelectedEvolutionBody` and `GetEventsLogSelectedEvolutionSummary` place a `NOT = { resources_found_selected_evolution_is_public = yes }` mask before the authored body and summary mappings. Before the matching flag they show the generic unrecorded body/summary. After the flag they show the real stage body and Event 018 evolution summary.
7. The six unrevealed localisation keys contain no cave, Oth-Kesh, Host, breach, emergence, monster, chamber, attack, World Below, subsurface, or underground terminology.
8. Portrait eligibility starts at zero. The Event 018 branch in `has_events_log_selected_evolution_authored_portrait` requires both public chronology and stage IV, and `GetEventsLogSelectedEvolutionPortrait` repeats the Event 018 ID, type, stage-IV, and public-chronology checks before selecting `GFX_portrait_DHO_vhorruk_animated`. Stages I-III never receive this portrait. Stage IV receives it only after `resources_found_evolution_iv_chronology_recorded`.

Static truth table:

| Stage | Before matching chronology flag | After matching chronology flag | Authored portrait |
| --- | --- | --- | --- |
| I | Masked row title, opened title, body, and summary | `Veins Without End`, stage-I body, authored summary | Never |
| II | Masked row title, opened title, body, and summary | `The Workings Turn Sick`, stage-II body, authored summary | Never |
| III | Masked row title, opened title, body, and summary | `The Breach Takes Shape`, stage-III body, authored summary | Never |
| IV | Masked row title, opened title, body, summary, and no portrait | `The Oth-Kesh Emerge`, stage-IV body, authored summary | Vhorruk portrait only after the stage-IV flag |

The chronology flags are set by their matching `resources_found_record_evolution_*_from_field` helpers before the shared evolution record call, so the reveal boundary aligns with the public chronology record. The original spoiler blocker is resolved in the inspected source path.

## Simplifications, omissions, fallbacks, and risks

- **Style risk:** 85 decision/mission tooltips retain the common functional envelope `Starts a/an ... project` or `Starts the exact-duration ... project shown above`. Their consequence clauses are specific and the exact-value duplicate audit is clean, but a strict interpretation that any repeated queue sentence is generic boilerplate would require a broad rewrite beyond the small-defect authority of this audit.
- **Live validation skipped:** HOI4 was not launched. No live font wrapping, tooltip expansion, scripted-localisation evaluation, event-log click path, or super-event/music presentation was tested. This is a static source audit only.
- **Workbook unchanged:** spreadsheet/event-detail workbook alignment was not edited. A spreadsheet worker should copy final in-game wording only after the parent accepts these strings and resolves the Event Details gate.
- **Unrelated localisation left untouched:** global duplicate keys and placeholder text belonging to other events were observed in shared files but were not changed.
- **No fallback introduced:** no substitute text, placeholder, hidden mechanic, or alternate implementation was added.

The previously reported Event Details spoiler blocker is resolved. Within the audited source surfaces, Event 018 localisation definitions, live-key reconciliation, chronology masks, post-chronology authored reveals, and stage-IV portrait gating pass static review. This does not replace the parent completion audit or live in-game presentation testing.

## Skill report

Skills used:

- `chaos-redux-subagents`
- `chaos-redux-events`

No skill was created or updated during this audit.
