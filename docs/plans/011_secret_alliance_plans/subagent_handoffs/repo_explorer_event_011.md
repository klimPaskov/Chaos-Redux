# Repo Explorer Handoff

## Scope read
- Parent task: read-only file and pattern map for implementing Event 011 Secret Alliance.
- Explicit constraints: no gameplay, localisation, GUI, GFX, asset, docs, spreadsheet, history, country, focus, decision, scripted effect, scripted trigger, on_action, or event edits. The only write is this report.
- Files or ids requested: Event 011 package under `docs/specs/011_secret_alliance_specs/`, root event `chaosx.nr11.1`, Event 011 Secret Alliance systems, and report path `docs/plans/011_secret_alliance_plans/subagent_handoffs/repo_explorer_event_011.md`.
- Skills or docs read: `chaos-redux-events`, `chaos-redux-subagents`, Event 011 spec package, `docs/super_events/011_secret_alliance_super_event_research.md`, offline wiki pages for events, decisions, on_actions, scripted GUI, effects, triggers, localisation, graphical assets/interface, and vanilla HOI4 documentation for effects/triggers. `AGENTS.md` was required but not found by `rg --files -g AGENTS.md ..`.

## Primary findings
- Current Event 011 is still the old Anti-Player Pact: `events/011_anti_player_pact.txt` creates an immediate faction and wars. It conflicts with the new hidden-compact design and should be replaced rather than extended.
- Event 011 is already registered as fire-once in `common/scripted_effects/chaosx_logic_effects.txt`, but event name, faction loc, event log details, decisions, assets, achievements, scripted GUI, and docs are missing or stale.
- The closest Chaos Redux implementation precedents are Event 010 Death for reveal/evolution/scripted GUI/event-log patterns, Event 013 Natural Disasters for long stateful sequences and missions, Event 005 Soviet Collapse for patron/targeted decision/AI patterns, and Event 007 Fury for response decisions and timed missions.
- Vanilla docs mark raw `create_faction` as deprecated when faction templates are available. Existing Chaos Redux Event 002 and 003 already use `create_faction_from_template`, Event 011 should mirror that for the public pact.

## Relevant files
| Path | Why it matters | Evidence |
| --- | --- | --- |
| `events/011_anti_player_pact.txt` | Current Event 011 root implementation to replace or rename carefully. | Contains `add_namespace = chaosx.nr11`, `chaosx.nr11.1`, immediate random member selection, `create_faction = "anti_player_pact"`, and immediate `declare_war_on`. |
| `localisation/english/011_anti_player_pact_l_english.yml` | Stale Event 011 visible event text. | Defines `chaosx.nr11.1.t`, `chaosx.nr11.2.t`, `.2.d`, `.2.a` for Anti-Player Pact. |
| `localisation/english/chaosx_event_names_l_english.yml` | Event selector/display name. | `chaosx.event_name.11: "Anti-Player Pact"` is stale for Secret Alliance. |
| `localisation/english/chaosx_factions_l_english.yml` | Existing faction loc key. | `anti_player_pact: "Secret Alliance"` conflicts with required public `Anti-[target country] Pact` naming. |
| `common/scripted_effects/chaosx_logic_effects.txt` | Shared event registration, random pool evaluation, fired-event bookkeeping. | `global.fire_once_events = 11`, `evaluate_random_event_active_pool_candidate`, `on_fire_once_event_fired`. |
| `common/scripted_effects/chaosx_events_log_effects.txt` | Event log actor, details, and evolution rows. | `events_log_set_default_actor_for_current_event` has no Event 011 branch, evolution/detail rows need Event 011 additions. |
| `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` | Event log and detail scripted localisation. | Event 011 currently maps only through `chaosx.event_name.11` name selectors. |
| `common/scripted_localisation/chaosx_scripted_localisation_debug.txt` | Debug event-name selector. | Event id 11 maps to `chaosx.event_name.11`. |
| `common/scripted_localisation/chaosx_scripted_localisation_settings.txt` | Settings/last-fired event-name selectors. | Event id 11 maps to `chaosx.event_name.11`. |
| `common/on_actions/chaosx_on_actions.txt` | War-caused reveal hook. | Existing `on_war_relation_added` handles Event 010 Death and other systems, Event 011 should add an idempotent reveal helper here. |
| `common/on_actions/chaosx_on_actions_system.txt` | Daily system pulse surface. | Use only if needed for low-frequency maintenance, avoid heavy all-country scans for member scoring. |
| `common/scripted_triggers/chaosx_dynamic_triggers.txt` | Shared exclusions for invalid countries. | Existing `is_special_chaos_country` and `is_actual_nonhuman_country` should be reused in Event 011 candidate validity. |
| `common/scripted_effects/010_death_effects.txt` | Best reveal/evolution pattern. | `death_reveal_from_current_state`, `death_emit_reveal_super_event`, `death_record_evolution_stage`. |
| `common/scripted_triggers/010_death_triggers.txt` | War-pull and reveal validity pattern. | `death_country_can_be_pulled_into_death_war` shows guarded war participant selection. |
| `common/decisions/010_death_decisions.txt` and `common/decisions/categories/010_death_categories.txt` | Scripted GUI category plus response decisions. | Death category uses `scripted_gui = death_black_atlas_scripted_gui`. |
| `common/scripted_guis/010_death_black_atlas_scripted_gui.txt` and `interface/010_death_black_atlas.gui` | Existing custom board UI pattern. | Visible gate uses `death_publicly_revealed`, GUI separates interaction from gameplay helpers. |
| `common/scripted_effects/013_natural_disasters_effects.txt` | Long lifecycle and cleanup model. | `natural_disasters_start_sequence`, `natural_disasters_cleanup_sequence_context`, mission success/failure helpers. |
| `common/decisions/013_natural_disasters_decisions.txt` | Timed mission model. | Uses `days_mission_timeout`, selectable missions, and success/failure effects. |
| `common/scripted_triggers/005_soviet_collapse_triggers.txt` | Major patron candidate precedent. | `is_soviet_collapse_foreign_patron_candidate` checks major, war state, and chaos exclusions. |
| `common/decisions/005_soviet_collapse_decisions.txt` | Targeted diplomacy/patron decisions. | Uses `target_array`, `target_root_trigger`, `target_trigger`, custom costs, and AI modifiers. |
| `common/ai_strategy/005_soviet_collapse.txt` | AI route precedent. | `soviet_collapse_foreign_patron_response` uses `enable` and `abort_when_not_enabled`. |
| `common/decisions/007_fury_decisions.txt` | Counter-play and timed response pattern. | Existing response decisions and missions for an event-specific threat. |
| `common/factions/templates/anti_zombie_league.txt` | Faction template precedent. | Used by Event 002 instead of raw `create_faction`. |
| `common/factions/templates/holy_realm_mandala_of_nations.txt` | More complex faction template precedent. | Used by Event 003 Mandala faction path. |
| `docs/events/011_secret_alliance.md` | Missing Event Details doc target. | No Event 011 event doc exists under `docs/events/`. |
| `docs/specs/011_secret_alliance_specs/` | Source-of-truth package for implementation. | Contains mechanics, decisions/missions, AI/localisation, asset, achievement, and routing specs. |
| `docs/super_events/011_secret_alliance_super_event_research.md` | Existing super-event research. | Recommends title `Anti-[Target Country] Pact`, Thucydides quote, and reveal framing. |
| `interface/chaosx_decisions.gfx`, `interface/chaosx_pictures.gfx`, `interface/chaosx_news_event_pictures.gfx`, `interface/chaosx_ideas.gfx`, `interface/chaosx_achievements.gfx`, `interface/chaosx_super_events.gfx` | Existing sprite registries likely touched by assets, ideas, achievements, and super event. | No `secret_alliance` GFX entries currently found. |
| `docs/spreadsheets/chaos_redux_events_catalog.xlsx` | Spreadsheet alignment surface after final text. | Spec manifest identifies row 11 as Secret Alliance but current loc/doc files remain stale. |

## Existing patterns
Event 010 Death is the primary model for hidden-to-public reveal. Inspect `death_reveal_from_current_state` and `death_emit_reveal_super_event` in `common/scripted_effects/010_death_effects.txt`, then mirror its idempotent reveal flagging, actor capture, super-event emission, and post-reveal scheduling. Its `death_record_evolution_stage` helper is the best model for Event 011 Evolution I, II, and III event-log records.

Event 010 also provides the closest Dossier Board precedent through `common/decisions/categories/010_death_categories.txt`, `common/scripted_guis/010_death_black_atlas_scripted_gui.txt`, and `interface/010_death_black_atlas.gui`. Keep gameplay logic in scripted effects/triggers and let the GUI expose state through variables and scripted loc.

Event 013 Natural Disasters is the best lifecycle precedent for a multi-stage system with cleanup and missions. Use its sequence start, cleanup, and mission success/failure helpers as patterns for hidden compact creation, evolution pulses, invalid-member cleanup, and crisis missions.

Event 005 Soviet Collapse is the best patron and targeted-decision precedent. Its foreign patron candidate trigger and targeted decision arrays map well to Event 011 major patron, known member pressure, face-saving exit, and counter-diplomacy decisions.

Event 002 Zombie Outbreak and Event 003 Holy Realm show the preferred faction-template route. Event 011 should add a new pact template instead of using the current raw `create_faction` call.

## Vanilla or reference precedents
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`: `create_faction` is documented as deprecated in favor of `create_faction_from_template`, `add_to_faction` and `declare_war_on` are documented country-scope effects.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`: `can_declare_war_on` is the relevant pre-war validity trigger.
- `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`: confirms namespace/id rules, `is_triggered_only`, `hidden = yes`, delayed events, and `immediate` usage.
- `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`: confirms category `scripted_gui`, custom cost behavior, missions, `days_mission_timeout`, targeted decisions, `target_array`, `target_root_trigger`, and `target_trigger`.
- `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md`: `on_war_relation_added` has ROOT as attacker and FROM as defender, so Event 011 reveal logic must check both member-target directions.
- `paradox_wiki/Scripted GUI modding - Hearts of Iron 4 Wiki.md`: supports `context_type`, `visible`, `effects`, `triggers`, `click_enabled`, and `dirty`, recommends separating GUI from gameplay through scripted effects/triggers.
- `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`: confirms UTF-8-BOM localisation format, dynamic country names such as `[ROOT.GetName]`, and scripted localisation use.
- `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md` and `paradox_wiki/Interface modding - Hearts of Iron 4 Wiki.md`: confirm `.gfx` sprite registrations, `textureFile`, `noOfFrames`, `frameAnimatedSpriteType`, and `.gui` container/button/text patterns.

## Likely edit order for the parent
1. Decide file naming strategy: replace `events/011_anti_player_pact.txt` in place or rename to `events/011_secret_alliance.txt` while preserving namespace `chaosx.nr11`.
2. Add foundational constants, triggers, and effects: candidate validity, candidate scoring, member arrays/flags, target variables, cleanup, reveal idempotence, public faction creation, member war-call validity, and event-log evolution helpers.
3. Update shared event pool gating in `chaosx_logic_effects.txt` so Event 011 is unavailable unless three valid founding minors exist.
4. Replace root event behavior with hidden compact creation and scheduled evolutions. Do not keep the current immediate war/faction behavior.
5. Add `on_war_relation_added` reveal routing through a centralized Event 011 helper that handles ROOT/FROM in both directions and prevents duplicate reveal/war calls.
6. Add decisions, missions, category, and Dossier Board or equivalent scripted GUI after core variables and helpers are stable.
7. Add AI strategy and decision AI weights after all validity triggers exist.
8. Add event-log actor/default branch, Event Details rows, evolution text, scripted localisation, and user-facing localisation.
9. Add assets, sprite registrations, ideas, achievements, and super-event wiring only after helper names and final text are stable.
10. Update `docs/events/011_secret_alliance.md` and spreadsheet alignment last, after implementation wording and keys stop moving.

## Validation checks
- Current/stale Event 011 search: `rg -n "chaosx\\.nr11|anti_player_pact|secret_alliance|chaosx.event_name.11" events common localisation interface docs`
- Event registration and log rows: `rg -n "global.fire_once_events = 11|event_id = 11|value = 11" common/scripted_effects/chaosx_logic_effects.txt common/scripted_effects/chaosx_events_log_effects.txt common/scripted_localisation`
- State variable and flag coverage: `rg -n "secret_alliance_member|secret_alliance_founder|secret_alliance_patron|pact_suspicion|pact_evidence|pact_public_reveal" common events localisation interface docs`
- War reveal routing: `rg -n "on_war_relation_added|secret_alliance.*reveal|reveal.*secret_alliance" common/on_actions common/scripted_effects`
- Asset registration: `rg -n "GFX_.*secret_alliance|report_event_secret_alliance|news_event_secret_alliance|super_event_secret_alliance" interface gfx docs/assets`
- Achievement coverage: `rg -n "secret_alliance_" common/achievements localisation/english/chaosx_achievements_l_english.yml interface/chaosx_achievements.gfx`
- Localisation duplicates/missing selectors: `rg -n "chaosx.nr11|secret_alliance|Anti-\\[" localisation/english common/scripted_localisation`
- Verify expected new files exist after implementation: scripted constants/effects/triggers, decisions/category, scripted GUI/interface, ideas, AI strategy, faction template, docs, and asset handoff.
- No repo-local parser or lint script was found by `rg --files | rg -i "(parser|validate|validator|lint|hoi4|syntax|check).*\\.(ps1|py|js|ts|bat|cmd)$"`. Parent should use the project owner's normal HOI4 syntax/log validation and in-game error log pass.

## Risks and blockers
Confirmed blockers:
- `AGENTS.md` is required by the prompt but absent in this checkout and immediate parent search. Reproduced with `rg --files -g AGENTS.md ..`.
- No current `secret_alliance` gameplay/assets implementation exists beyond specs and stale Anti-Player Pact localisation/faction naming.

Risks:
- Current Event 011 immediately declares wars and creates a raw faction. Leaving any of that path in place will violate the hidden compact requirement.
- Candidate selection must guarantee exactly three valid minor founders and exclude target, subjects, countries at war with target, special chaos countries, nonhuman countries, dead countries, and temporary diplomacy-invalid countries.
- `on_war_relation_added` exposes ROOT/FROM as attacker/defender, not target/member. The reveal helper must check both directions and be idempotent.
- War-caused reveal should only call valid public members into the target war, do not blindly add hidden, dead, subject, same-faction, or already-at-war countries.
- Dynamic public faction naming is a design risk. Static faction localisation may not preserve a per-target `Anti-[target country] Pact` name in all UI contexts, so parent should test whether `create_faction_from_template` name localisation can carry the target cleanly.
- Event log history may be recorded by shared fire-once bookkeeping before event `immediate` state is fully built. Because ROOT is the target this is probably workable, but Event 011 still needs an explicit default actor branch and evolution helpers.
- Decision custom costs do not subtract automatically, each decision must subtract resources in `complete_effect`.
- Targeted decisions scope FROM as the target country. Member-pressure and patron decisions must keep ROOT/FROM assumptions explicit.
- GUI and AI should avoid daily all-country scans. Use arrays, scheduled pulses, event-driven recalculation, and dirty GUI refreshes where possible.
- Assets, achievements, super-event wiring, docs, and spreadsheet rows are absent/stale and should not be marked complete until separately validated.

## Recommended next action
Have the parent implement the foundation first: Event 011 constants, triggers, and scripted effects for candidate validity/scoring, compact state, reveal idempotence, public faction creation, valid war joins, cleanup, and evolution logging. Then replace `events/011_anti_player_pact.txt` and wire `on_war_relation_added` before adding decisions, GUI, AI, assets, achievements, and final documentation.
