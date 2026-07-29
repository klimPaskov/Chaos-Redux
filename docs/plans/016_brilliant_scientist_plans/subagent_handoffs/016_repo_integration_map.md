# Event 016: Brilliant Scientist repository integration map

## Handoff purpose

This is the bounded, read-only repository map requested for Event 016. It identifies the current implementation, exact integration surfaces, reusable Chaos Redux and vanilla patterns, ownership boundaries, collision risks, unresolved reservations, and safest implementation order. It does not implement gameplay.

The accepted Event 016 specification package under docs/specs/016_brilliant_scientist_specs is the design source of truth. This handoff is an implementation map, not a replacement specification.

## Follow-up reconciliation, 2026-07-14

Event 016 remains default-disabled and gameplay-incomplete. The original implementation snapshot below remains useful baseline evidence, but these later facts control presentation integration:

- Event 015 occupies visible super-event IDs 85 through 89.
- Event 016 uses visible IDs 90 recognition, 91 formation, 92 global threat, 93 Laboratory World, 94 Strategic Singularity, and 95 qualifying defeat.
- Event 016 world-end IDs remain 11 and 12.
- Six final Event 016-owned OGGs are complete at IDs 90 through 95. Shared music, sound, settings, event, GUI, and localisation wiring remains absent.
- The exact stage-0 leader or scientist DDS and advisor DDS are complete and registered. Stage I through IV sprite contracts are pre-registered, but the referenced later assets remain missing.
- Event 020 separately declares world-end ID 10 and visible IDs 85 through 87 in its own constants. Its visible overlap with Event 015 is external to Event 016.
- Fallout is an independent unnumbered system under `chaosx.fallout`. It owns its request coordinator, blackout GUI, transition events, assets, and audio wrappers.

## Executive verdict

At the original map snapshot, Event 016 was only a three-file placeholder. The entry event remains incomplete, and a complete implementation cannot be produced by expanding the entry event and idea alone. The accepted design is a cross-system package spanning the random-event dispatcher, four evolution records, a persistent character/scientist, a decision-led directorate, fifteen project families, a conditional country, a large focus tree, custom forces, two world-end scenarios, six super-events, seventeen achievements, assets, documentation, and workbook alignment.

Two architecture problems must be resolved before ordinary content work:

1. The random-event system records the fire-once history row in the dispatch effect chain, before the scheduled country event's immediate block can choose a host. Event 016 therefore needs a prefire host resolver and a regular event target. Leaving host selection inside chaosx.nr16.1 produces an incorrect or missing event-log actor.
2. Strategic Singularity must keep its Event 016-specific super-event separate from the dedicated Fallout handoff. Event 016 needs a verified request-source mapping into `fallout_request_aftermath`, while Fallout retains ownership of its blackout transition and audio.

No fallback, substitute tree, generic audio, placeholder asset, transform-only animation, generic country setup, or reduced achievement list is authorized.

## Required references consulted

The following required source families were read before this map was written:

- Repository AGENTS.md.
- Repository skills chaos-redux-subagents and chaos-redux-events.
- Offline wiki core pages: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.
- Offline wiki relevant system pages: Interface Modding, Scripted GUI Modding, Country creation, Cosmetic tag, National focus, Equipment, Division, Unit, Technology, Achievement, Graphical asset, Portrait, Sound, and Music.
- Vanilla documentation for script concepts and script constants, effects, triggers, modifiers, localisation, decisions, on actions, characters, scripted GUI, scientist traits, equipment, units, special-project specializations/projects/rewards, AI strategies, and AI templates.
- All ten Event 016 specification parts, all eight Event 016 matrices, acceptance files, package manifest, repo inspection note, continuation/routing handoffs, and implementation prompts.
- Chaos Redux precedents cited below, especially the implemented Event 018 prefire, evolution-log, country, focus, AI, scripted-GUI, world-end, achievement, and asset integrations.

## Fixed scope and identifiers

These items are fixed by the accepted package and should be treated as invariants:

| Item | Fixed value |
| --- | --- |
| Source event | Event 16 |
| Event type | Fire-once minor event |
| Entry root | chaosx.nr16.1 |
| Cluster membership | None |
| Named character | Doctor Warren Kruger |
| Opening gameplay anchor | Exactly +100% research speed |
| Evolutions | I National Institution; II International Contest; III Forbidden or Autonomous Science; IV Sovereign or Global |
| Project families | Fifteen |
| Conditional country | Kruger State |
| Working country tag | KRG, subject to final whole-load-order conflict check |
| Kruger State focus target | 85 to 115 manually authored, route-specific focuses |
| Super-event roles | Six |
| World-end scenarios | Laboratory World and Strategic Singularity |
| Fallout relationship | Strategic Singularity commits the canonical Fallout state |
| Achievements | Seventeen working keys |
| Evolution V | Excluded |
| Ordinary host focus tree replacement | Excluded; the host phase is decision-led and additive |

KRG has no match in the repository or vanilla country-tag/country/history files inspected for this map. It remains a working reservation rather than a final guarantee because active mods and concurrent branches can still introduce a conflict.

## Current live implementation

| File or identifier | Current state | Required disposition |
| --- | --- | --- |
| events/016_brilliant_scientist.txt | chaosx.nr16.1 selects a random major or human country internally and fires chaosx.nr16.2; .2 adds one idea and fires chaosx.news.18 | Rebuild as a preselected-host chain while preserving chaosx.nr16.1 as the entry root |
| common/ideas/016_brilliant_scientist_ideas.txt | One country idea, research_speed_factor = 0.5 | Replace with the specified +100% opening anchor and staged idea/advisor lifecycle; prevent accidental stacking |
| localisation/english/016_brilliant_scientist_l_english.yml | Placeholder event text | Replace with the complete UTF-8 BOM event, option, tooltip, project, decision, character, country, and aftermath wording or split into clearly owned Event 016 localisation files |
| events/_chaosx_news.txt | chaosx.news.18 is the placeholder opening news event | Retain only if the final opening chain needs it; otherwise replace its role without colliding with other news IDs |
| localisation/english/chaosx_ideas_l_english.yml | brilliant_scientist name and an alien-speculation description | Move or rewrite to the final idea lifecycle; do not assert alien origin by default |
| localisation/english/chaosx_event_names_l_english.yml | chaosx.event_name.16 already maps to Brilliant Scientist | Keep stable unless the accepted display title changes |
| common/scripted_localisation/chaosx_scripted_localisation_debug.txt | Event ID 16 already maps to chaosx.event_name.16 | No new route is needed for the base event-name lookup |
| common/scripted_localisation/chaosx_scripted_localisation_events_log.txt | Event 16 already has base source-name mappings, but no evolution/detail/world-end package | Extend all applicable Event 016 evolution, detail, selected-row, history, portrait, and world-end selectors |

At the original map snapshot there were no live Warren Kruger character definitions, Event 016 directorate decisions, Event 016 projects, KRG country package, KRG focus tree, Event 016 AI, project units, achievements, Event 016 super-events, or final Event 016 asset registrations. The later stage-0 GFX registration and pre-registered portrait contracts supersede only the asset-registration portion of that snapshot. They do not prove gameplay or later asset completion.

## Recommended Event 016-owned files

The names below are recommended stable ownership boundaries. The implementing agent may split a very large file by subsystem, but should not scatter Event 016 logic through unrelated shared files.

### Core event and tuning

- events/016_brilliant_scientist.txt
- events/016_brilliant_scientist_project_events.txt
- events/016_brilliant_scientist_foreign_events.txt
- events/016_brilliant_scientist_country_events.txt
- events/016_brilliant_scientist_aftermath_events.txt
- common/script_constants/016_brilliant_scientist_constants.txt
- common/scripted_triggers/016_brilliant_scientist_triggers.txt
- common/scripted_effects/016_brilliant_scientist_effects.txt
- common/scripted_effects/016_brilliant_scientist_prefire_effects.txt
- common/scripted_effects/016_brilliant_scientist_log_effects.txt

If the constants file becomes unreviewably broad, split it by named subsystem, for example directorate, projects, country, AI, terminal, and achievements. Shared values must use script_constants and explicit constant:category.key access. File-scoped at-sign constants are appropriate only where the receiving field cannot parse script constants.

### Character, ideas, decisions, and UI

- common/scientist_traits/016_brilliant_scientist_traits.txt
- common/ideas/016_brilliant_scientist_ideas.txt
- common/decisions/categories/016_brilliant_scientist_categories.txt
- common/decisions/016_brilliant_scientist_decisions.txt
- common/scripted_guis/016_brilliant_scientist_scripted_gui.txt
- interface/016_brilliant_scientist.gui
- interface/016_brilliant_scientist.gfx

### Projects and technology

- common/special_projects/projects/016_brilliant_scientist_projects.txt
- common/special_projects/prototype_rewards/016_brilliant_scientist_prototype_rewards.txt
- common/technologies/016_brilliant_scientist_technologies.txt

### Conditional country and military package

- common/country_tags/016_brilliant_scientist_country.txt
- common/countries/Kruger State.txt
- history/countries/KRG - Kruger State.txt
- history/units/KRG_1936.txt
- common/scripted_effects/016_brilliant_scientist_country_effects.txt
- common/scripted_triggers/016_brilliant_scientist_country_triggers.txt
- common/national_focus/016_brilliant_scientist_kruger_state_focus_tree.txt
- common/ai_strategy/016_brilliant_scientist_ai_strategy.txt
- common/ai_templates/016_brilliant_scientist_ai_templates.txt
- common/units/016_brilliant_scientist_project_units.txt
- common/units/equipment/016_brilliant_scientist_project_equipment.txt

### Achievements and bounded hooks

- common/scripted_triggers/016_brilliant_scientist_achievement_triggers.txt
- common/scripted_effects/016_brilliant_scientist_achievement_effects.txt
- common/on_actions/016_brilliant_scientist_on_actions.txt

The Event 016 on-action file may use bounded hooks such as on_nuke_drop, state-control changes, capitulation, annexation, puppet changes, and peace outcomes. It must not introduce an all-country on_daily, on_weekly, or on_monthly hook. Prefer self-scheduled targeted events and missions. A tag-specific on_daily_KRG is permitted by repository policy only when genuinely necessary and should not be the default design.

### Localisation and documentation

- localisation/english/016_brilliant_scientist_l_english.yml
- localisation/english/016_brilliant_scientist_country_l_english.yml
- localisation/english/016_brilliant_scientist_focus_l_english.yml
- localisation/english/016_brilliant_scientist_special_projects_l_english.yml
- localisation/english/016_brilliant_scientist_units_l_english.yml
- docs/016_brilliant_scientist.md
- docs/plans/016_brilliant_scientist_plans/ for accepted addenda, implementation handoffs, and audit follow-up

All Event 016 localisation files must be UTF-8 with BOM. On-screen text must describe the world and choices rather than implementation or tuning history.

## Integration surface map

### 1. Fire-once registration, default enablement, availability, and dispatch

#### Existing registration

common/scripted_effects/chaosx_logic_effects.txt already registers Event 16 in initialize_event_categories:

- global.fire_once_events contains 16.
- No cluster registration exists or should be added.
- get_event_type therefore already resolves Event 16 through the fire-once array.

#### Default-disabled rework queue

common/scripted_effects/chaosx_logic_effects.txt: initialize_default_disabled_events_for_rework_queue checks event_log_event_is_reworked_default_enabled.

common/scripted_triggers/chaosx_settings_triggers.txt: event_log_event_is_reworked_default_enabled does not include Event 16. This correctly keeps the placeholder disabled by default.

Ownership rule:

- Add Event 16 to event_log_event_is_reworked_default_enabled only in the final accepted implementation tranche, after gameplay, AI, localisation, assets, log details, evolutions, and documentation are complete.
- Do not enable it merely because the entry event fires.

#### Automatic availability

common/scripted_effects/chaosx_logic_effects.txt: evaluate_random_event_active_pool_candidate contains explicit event-specific eligibility branches. Add an Event 016 branch that rejects the candidate when brilliant_scientist_automatic_event_is_available is false.

Recommended Event 016 triggers:

- brilliant_scientist_is_eligible_host
- brilliant_scientist_has_any_eligible_host
- brilliant_scientist_automatic_event_is_available

The shared trigger should encode the accepted host matrix once and be reused by:

- random-pool availability;
- the prefire resolver;
- manual Events-tab impossible-state display;
- entry-event safety trigger;
- any debugging or audit view.

Do not leave a weaker random-country limit in chaosx.nr16.1. The resolver must handle existence, capitulation, usable controlled core territory, and every other accepted host exclusion consistently.

#### Prefire selection and actor ownership

Create common/scripted_effects/016_brilliant_scientist_prefire_effects.txt with a single authoritative resolver, recommended identifier:

- brilliant_scientist_prepare_random_event_fire

Recommended outputs:

- temporary flag/value brilliant_scientist_prefire_ready;
- regular event target brilliant_scientist_prefire_host.

The regular event target is intentional. It survives into events fired by the same effect chain and auto-clears after the chain. A global event target is unnecessary for the initial dispatch and would create cleanup obligations.

Concrete precedent:

- common/scripted_effects/018_resources_found_prefire_effects.txt
- resources_found_prepare_random_event_fire
- resources_found_prefire_owner
- resources_found_prefire_state

#### Automatic and manual dispatcher

common/scripted_effects/chaosx_settings_effects.txt: fire_event_by_temp_id_no_cluster owns both automatic and manual no-cluster dispatch. Add Event 016 beside the existing Event 018 prefire block:

1. Reset brilliant_scientist_prefire_ready.
2. Call brilliant_scientist_prepare_random_event_fire.
3. Set event_single_fire_allowed = 0 when the resolver failed or the host target is absent.
4. In the dispatch chain, scope to event_target:brilliant_scientist_prefire_host and fire chaosx.nr16.1.
5. Leave event_fire_dispatched false on failure so the event is not recorded as fired.

The generic meta_effect branch must not dispatch Event 16 in the current caller country scope.

#### Event-log actor timing

fire_event_by_temp_id_no_cluster schedules the country event, then calls on_fire_once_event_fired. That handler calls record_events_log_history_entry. The scheduled event's immediate block is not a safe place to establish the actor for this history row.

common/scripted_effects/chaosx_events_log_effects.txt: events_log_set_default_actor_for_current_event must therefore add an Event 16 branch that uses brilliant_scientist_prefire_host.

This is the reason prefire selection is an architectural requirement rather than a convenience.

#### Events-tab impossible state

common/scripted_effects/chaosx_events_log_effects.txt: rebuild_events_log_events_view assigns a live weight of -1 to event-specific impossible cases. Add Event 16:

- if event_id is the Event 016 constant and brilliant_scientist_has_any_eligible_host is false, set events_log_events_live_weight = -1.

Use the same eligibility trigger as the automatic pool. Do not invent a looser UI-only check.

### 2. Event script and chain ownership

Rebuild events/016_brilliant_scientist.txt around the preselected country scope:

- chaosx.nr16.1 remains the required entry root.
- The root verifies the prefire host context, creates or recovers Doctor Warren Kruger exactly once, applies the opening package, and offers the accepted player/AI choice structure.
- AI acceptance remains deterministic as specified.
- Sending Kruger away must enter the transfer/removal chain rather than silently deleting the persistent identity.
- Later chains should use Event 016-owned namespaces and targeted events. Do not use a global polling on action.

The current chaosx.nr16.2 and chaosx.news.18 may be retained only if their final roles remain coherent. Their placeholder IDs do not create an obligation to preserve placeholder text or structure.

### 3. Four evolution records and Event Details

#### Constants and wrappers

Create a constant category in common/script_constants/016_brilliant_scientist_constants.txt, recommended shape:

- brilliant_scientist_event.id = 16
- brilliant_scientist_event.evolution_type = 16
- named constants for stages I to IV
- named constants for each tier

Create common/scripted_effects/016_brilliant_scientist_log_effects.txt with:

- brilliant_scientist_record_evolution_from_temp
- brilliant_scientist_record_evolution_i
- brilliant_scientist_record_evolution_ii
- brilliant_scientist_record_evolution_iii
- brilliant_scientist_record_evolution_iv

Concrete precedent:

- common/scripted_effects/018_resources_found_log_effects.txt
- resources_found_record_field_evolution_from_temp
- resources_found_record_evolution_i_from_field through resources_found_record_evolution_iv_from_field
- common/script_constants/018_resources_found_constants.txt

Each wrapper must:

- set events_log_evolution_event_id, type, stage, and tier;
- set regular event target events_log_evolution_actor to the actual current host or KRG actor;
- set events_log_evolution_has_actor = 1;
- call record_events_log_evolution_entry;
- guard chronology with an Event 016-specific once-only flag;
- avoid recording a disabled evolution as completed.

#### Shared details builder

common/scripted_effects/chaosx_events_log_effects.txt: events_log_rebuild_open_event_details_view must add an Event 16 branch with four calls to events_log_add_event_detail_evolution_preview.

The four rows must be stable even before completion, and completed rows must resolve to their recorded actor and route-aware text.

#### Scripted localisation selectors

Extend common/scripted_localisation/chaosx_scripted_localisation_events_log.txt in every applicable Event 016 branch, not only the visible title selectors. The concrete selectors are:

- GetEventsLogEvolutionSourceEventNameView
- GetEventsLogEvolutionNameView
- GetEventsLogEvolutionStageView
- GetEventsLogEvolutionTierView
- GetEventsLogSelectedHistoryEvolutionTypeView
- GetEventsLogSelectedHistoryEvolutionNameView
- GetEventsLogSelectedHistoryEvolutionStageView
- GetEventsLogSelectedHistoryEvolutionTierView
- GetEventsLogEventDetailEvolutionTypeView
- GetEventsLogEventDetailEvolutionStageView
- GetEventsLogEventDetailEvolutionTierView
- GetEventsLogEventDetailEvolutionMeta
- GetEventsLogSelectedEvolutionStageView
- GetEventsLogSelectedEvolutionTierView
- GetEventsLogEventDetailDescription
- GetEventsLogEventDetailEvolutionTitle
- GetEventsLogSelectedEvolutionTitle
- GetEventsLogSelectedEvolutionBody
- GetEventsLogSelectedEvolutionSummary
- GetEventsLogSelectedEvolutionPortrait
- GetEventsLogHistoryRowText
- GetEventsLogHistoryEventName

Add the matching keys to localisation/english/chaosx_gui_l_english.yml. The premise, preview, recorded title, body, summary, tier, meta, and portrait routing must agree with the Event 016 workbook wording.

### 4. World-end registry and world threat

#### Stable world-end IDs

common/script_constants/world_end_scenario_registry_constants.txt is append-only and save-facing. Concurrent Event 020 reserves scenario ID 10. Event 016 therefore reserves:

- world_end_scenario_id.laboratory_world = 11
- world_end_scenario_id.strategic_singularity = 12
- world_end_scenario_owner_event.brilliant_scientist = 16

Do not renumber any existing scenario. The earlier Event 016 proposal of IDs 10 and 11 is superseded by the whole-worktree collision scan dated 2026-07-14.

#### Registry rows and activation

Extend common/scripted_effects/chaosx_events_log_effects.txt:

- initialize_world_end_scenario_registry: append two public Event 016 rows;
- events_log_evaluate_world_end_scenario_active: map the two scenario IDs to their terminal global flags;
- availability and selected-row rebuilding: use the standard world-end rules and the two independent settings gates.

Recommended terminal flags:

- world_end_laboratory_world
- world_end_strategic_singularity

Strategic Singularity also sets the canonical world_end_fallout flag through the shared Fallout commit path.

Add independent gates to common/scripted_triggers/chaosx_world_end_scenario_triggers.txt:

- world_end_laboratory_world_scenario_enabled
- world_end_strategic_singularity_scenario_enabled

Extend the world-end selectors in common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:

- GetEventsLogWorldEndScenarioRowTitle
- GetEventsLogSelectedWorldEndScenarioTitle
- GetEventsLogWorldEndScenarioRowOwnerName
- GetEventsLogSelectedWorldEndScenarioOwnerName
- GetEventsLogWorldEndScenarioRowStatus
- GetEventsLogSelectedWorldEndScenarioStatus
- GetEventsLogSelectedWorldEndScenarioDetails

Add the corresponding localisation to chaosx_gui_l_english.yml.

#### World threat source

common/scripted_effects/chaosx_dynamic_effects.txt: refresh_world_threat_state has an explicit list of threat-source flags. Add an Event 016 source only when the accepted existential conditions are true.

Recommended identifiers:

- global flag world_threat_source_brilliant_scientist
- trigger has_world_threat_source_brilliant_scientist
- Event 016-owned effect brilliant_scientist_refresh_world_threat_source

Extend:

- common/scripted_effects/chaosx_dynamic_effects.txt
- common/scripted_effects/chaosx_dynamic_effects.md
- common/scripted_triggers/chaosx_world_threat_triggers.txt

Do not set world threat merely because Kruger is appointed or KRG exists. Use the specified autonomy, strategic weapon, conquest, and terminal thresholds.

### 5. Strategic Singularity to the dedicated Fallout system

The live Fallout ownership path is:

- `common/scripted_effects/fallout_world_end_effects.txt` for request intake and transition control
- `common/scripted_triggers/fallout_world_end_triggers.txt` for request validation
- `common/script_constants/fallout_world_end_constants.txt` for source and intensity identities
- `events/fallout_world_end_events.txt` under the `chaosx.fallout` namespace

Required Event 016 bridge:

1. Event 016 verifies Strategic Singularity readiness and saves the source actor through its existing terminal preparation helper.
2. Event 016 applies its required Chaos, Deaths, Condemnation, and Air Contamination consequences through the normal shared APIs.
3. Event 016 shows and records super-event `94` as its own Strategic Singularity presentation before the Fallout handoff.
4. Event 016 supplies Fallout-owned request source and intensity inputs, passes the verified actor when needed, and calls `fallout_request_aftermath`.
5. The Fallout coordinator validates the request, sets `world_end` and `world_end_fallout`, and owns the `chaosx.fallout.*` blackout and rewrite sequence.
6. Event 016 sets `world_end_strategic_singularity` and its terminal, evolution, and achievement state only after the Fallout request is accepted.
7. Event 016 clears its request context on success, cancellation, invalid ownership, disarmament, and every aborted attempt.

Fallout does not use the Strategic Singularity image or track. Strategic Singularity does not replace the Fallout blackout GUI, dedicated sound wrappers, sound wrappers, or final audio files. The exact Event 016 request-source constant remains parent-owned because the current Fallout source enum has no Event 016-specific entry.

Canonical shared effects to call rather than reimplement:

- common/scripted_effects/chaos_meter_effects.txt: air_contamination_apply_delta_bp
- add_chaos_meter_value
- chaos_meter_register_deaths, or the documented exact state civilian-loss helper where it fits
- common/scripted_effects/condemnation_sanctions_effects.txt: condemnation_add_source
- common/scripted_effects/chaos_meter_effects.txt: world_end_scenario_triggered

If Strategic Singularity needs a new Deaths reason or Condemnation context, add stable constants and full UI/localisation/filter routing in:

- common/script_constants/chaos_meter_constants.txt
- common/script_constants/condemnation_sanctions_constants.txt
- the associated scripted-localisation and GUI files

Do not label the event as an ordinary thermonuclear attack when its source is a Strategic Singularity.

### 6. Doctor Warren Kruger as one persistent visible identity

Create a single dynamic scientist and add roles to that same character.

Concrete repository precedent:

- common/scripted_effects/chaosx_startup_history_effects.txt uses generate_scientist_character, random_scientist, set_character_name, and set_portraits to create named persistent scientists.
- common/scripted_effects/chaosx_dynamic_effects.md documents the named scientist pattern.
- Vanilla effects documentation confirms add_advisor_role and add_country_leader_role can be applied in CHARACTER scope.

Recommended creator:

- brilliant_scientist_create_warren_kruger

Recommended persistent character marker:

- brilliant_scientist_warren_kruger

The creator should:

1. Mark existing scientists in the selected host.
2. Generate one scientist with all six actual project specializations.
3. Select the newly generated character deterministically.
4. Set the fixed localised name doctor_warren_kruger.
5. Apply the stage-0 portraits.
6. Set the persistent character flag.
7. Add and activate the political-advisor role in the same character scope.
8. Clear temporary discovery markers.

The six actual project specialization tokens in this repository/game are:

- specialization_nuclear
- specialization_naval
- specialization_air
- specialization_land
- specialization_biowarfare
- specialization_cw

The last two are defined in common/special_projects/specialization/chaosx_specializations.txt.

Add Event 016 scientist traits in common/scientist_traits/016_brilliant_scientist_traits.txt. If a single trait cannot honestly express all-field effects, use a compact trait family with explicit specializations rather than fake generic tokens.

When Kruger becomes a ruler, use add_country_leader_role on the same character when the engine permits the needed transfer. Do not create a second visible Kruger. Persistent lookup should rely on the character flag and current ownership, not an uncleaned global event target.

The specified base visual is complete from the exact `portrait_generic_biowarfare_europe_male_01` source. The preserved source package, `156x210` runtime leader or scientist DDS, `65x67` advisor DDS, provenance record, hashes, and two stage-0 sprite registrations now exist. External redistribution rights remain unresolved, while internal Event 016 use is explicitly user-authorized.

### 7. Ideas and staged identity

The existing brilliant_scientist idea provides +50% research speed and does not satisfy the accepted opening package.

The Event 016 idea lifecycle must:

- provide the fixed +100% opening research speed anchor;
- represent advisor/scientist visibility;
- stage institutional, security, dependence, and route consequences;
- avoid uncontrolled additive stacking between country idea, advisor trait, scientist trait, project reward, and focus reward;
- remove or transform the host package correctly on transfer, removal, KRG formation, takeover, death, and defeat;
- keep tuning in Event 016 script constants.

The stage-0 leader or scientist and advisor sprites are registered in `interface/016_brilliant_scientist.gfx`. Later portrait contracts are also pre-registered, but their referenced files remain missing. Do not reuse a focus icon as an idea icon and do not treat pre-registration as completed asset production.

### 8. Host directorate decisions and scripted GUI

Create:

- common/decisions/categories/016_brilliant_scientist_categories.txt
- common/decisions/016_brilliant_scientist_decisions.txt
- common/scripted_guis/016_brilliant_scientist_scripted_gui.txt
- interface/016_brilliant_scientist.gui
- interface/016_brilliant_scientist.gfx

Recommended scripted-GUI identifiers:

- brilliant_scientist_directorate_scripted_gui
- brilliant_scientist_directorate_window
- context_type = decision_category
- ai_enabled = always no

Concrete precedents:

- common/scripted_guis/018_resources_found_scripted_gui.txt: resources_found_field_scripted_gui
- interface/018_resources_found.gui
- common/scripted_guis/014_cannibalism_scripted_gui.txt for a denser decision-category surface and dynamic list patterns

The GUI exposes:

- visible Mandate;
- visible Dependence;
- visible Exposure;
- visible Project Capacity;
- project and facility state;
- foreign contacts and operations;
- sovereignty/confrontation state;
- Strategic Singularity state when unlocked.

Independent Capacity and Grievance remain hidden causal variables but must have player-readable consequences and tooltips. Project Capacity is visible.

Gameplay belongs in decisions and scripted effects. The GUI may display and invoke valid actions, but AI must use the same effects through decisions/event weights rather than GUI clicks.

Recommended decision-category ownership:

- host directorate;
- foreign competition and countermeasures;
- KRG sovereignty/projects;
- hidden scheduled clocks only when a mission or targeted event is insufficient.

### 9. Fifteen project families and existing-system reuse

Create Event 016 project/reward/technology files for the fifteen specified families:

1. computational mathematics;
2. electronics and guidance;
3. advanced materials;
4. rocketry and propulsion;
5. atomic and high energy;
6. biomedical acceleration;
7. teleportation;
8. cloning;
9. robotics and AI;
10. paleogenetics;
11. xenobiological synthesis;
12. biological weapons;
13. alien arms;
14. temporal mechanics;
15. strategic singularity.

Every family needs theory, prototype, deployment, and weaponization/autonomy state; prerequisite and synergy gates; cost and burden; accidents; foreign operations; AI priorities; KRG inheritance; countermeasures; localisation; icons; and relevant achievement hooks.

Concrete precedents and reusable content:

- common/special_projects/projects/mengele_cloning_projects.txt: structure for cloning, not its Germany-specific availability or flags.
- common/special_projects/projects/biowarfare_main_projects.txt: zombie cure, anthrax, plague, tularemia, and smallpox projects.
- common/special_projects/projects/chemical_warfare_nerve_projects.txt.
- common/special_projects/projects/chemical_special_projects.txt.
- common/special_projects/projects/zombie_weaponized_projects.txt.
- common/special_projects/prototype_rewards/generic_biowarfare_prototype_rewards.txt.
- common/special_projects/prototype_rewards/generic_chemical_prototype_rewards.txt.
- common/technologies/chaosx_technologies.txt and the existing zombie/CBRN technology files.

Biological-weapons integration rule:

- Reuse the existing biowarfare projects, contamination, deaths, and Condemnation consequences where their semantics match.
- Event 016 may grant access, add route-specific portfolio state, and record Event 016 consequences.
- Do not clone anthrax, plague, smallpox, or equivalent systems under new parallel IDs.

Shared registry:

- common/scripted_effects/chaosx_dynamic_effects.txt: grant_random_chaos_special_project_available_tech
- common/scripted_effects/chaosx_dynamic_effects.md

Extend that helper only for new broadly available chaos bio/chemical projects. Do not add purely Event 016 physics or sovereign-only projects to the generic random pool.

Strategic Singularity is a late sovereign route. It must not be available during the ordinary host phase without the complete accepted prerequisites.

### 10. KRG country creation, territory, cosmetics, and classification

#### Static country package

Create:

- common/country_tags/016_brilliant_scientist_country.txt with KRG = countries/Kruger State.txt
- common/countries/Kruger State.txt
- history/countries/KRG - Kruger State.txt as a dormant history entry
- history/units/KRG_1936.txt
- country localisation and three-size flags

common/countries/cosmetic.txt is the repository's cosmetic-tag definition file. Add only the accepted route identities after their final tag names and flag filenames are reserved.

Recommended cosmetic families:

- human technocracy;
- replicated sovereignty;
- machine ascendancy;
- temporal Continuum;
- xenobiological ascendancy;
- synthesis.

The base KRG identity remains valid until an actual route transformation occurs.

#### Formation logic

Create brilliant_scientist_form_kruger_state and route-specific helpers in common/scripted_effects/016_brilliant_scientist_country_effects.txt.

Concrete structural precedent:

- common/country_tags/018_resources_found_cave_country.txt
- common/countries/The Oth-Kesh Host.txt
- history/countries/DHO - Oth-Kesh Host.txt
- common/scripted_effects/018_resources_found_cave_effects.txt: resources_found_cave_setup_country
- runtime load_oob and load_focus_tree in the DHO setup

Event 016 has four distinct formation modes:

- peaceful charter;
- violent rebellion;
- partial enclave;
- host takeover.

Territory, buildings, supply, conventional forces, project forces, technology, relations, war state, and former-host handling must derive from actual recorded host/project history. A one-state generic release is not a permissible fallback.

#### Special/nonhuman classification

Extend common/scripted_triggers/chaosx_dynamic_triggers.txt and its companion Markdown documentation:

- add is_brilliant_scientist_kruger_country;
- include it in is_special_chaos_country;
- add is_brilliant_scientist_actual_nonhuman_country;
- include that trigger in is_actual_nonhuman_country only when the route has truly transformed the population/government.

Base KRG and human technocracy remain human special-chaos countries. Machine-majority and qualifying clone/xenobiological/synthesis outcomes become nonhuman only under their explicit route flags. Do not classify the tag itself as permanently nonhuman.

### 11. Kruger State focus tree and AI

Create common/national_focus/016_brilliant_scientist_kruger_state_focus_tree.txt:

- focus_tree id 016_brilliant_scientist_kruger_state_focus_tree;
- 85 to 115 manually authored focuses;
- country selection for original_tag = KRG and the appropriate formation flag;
- runtime load_focus_tree during KRG setup;
- route visibility, bypass, available, mutually exclusive, completion, and AI logic aligned with the focus architecture matrix.

Concrete precedent:

- common/national_focus/018_resources_found_cave_focus_tree.txt
- 018_resources_found_cave_focus_tree
- original_tag = DHO
- common/ai_strategy/018_resources_found_ai_strategy.txt

Required route coverage:

- formation/opening survival;
- human technocracy/scientific commonwealth;
- replicated sovereignty;
- machine ascendancy;
- temporal Continuum;
- xenobiological/bestiary;
- synthesis;
- laboratory economy and supply;
- conventional and project military;
- diplomacy, recognition, recruitment, and submission;
- former-host and expansion handling;
- Laboratory World;
- Strategic Singularity.

The ordinary host does not receive this tree. Its national focus tree remains intact and Event 016 is additive through decisions, events, ideas, projects, and AI.

AI ownership:

- common/ai_strategy/016_brilliant_scientist_ai_strategy.txt
- common/ai_templates/016_brilliant_scientist_ai_templates.txt
- decision ai_will_do blocks
- project AI
- focus ai_will_do
- event option weights

Implement host, foreign, KRG political, military, expansion, anti-snowball, and singularity behavior from docs/specs/016_brilliant_scientist_specs/matrices/016_ai_behavior_matrix.md. Do not reduce AI to deterministic route flags or generic focus weights.

### 12. Project-derived units, equipment, and OOB

Create Event 016-owned unit and equipment definitions for actual operational project outcomes, including qualifying:

- clone formations;
- robotic formations;
- dinosaur/bestiary formations;
- xenobiological monsters;
- portal units or support;
- temporal guard/recovery units;
- exotic/alien-armed guards.

Concrete patterns:

- common/scripted_effects/018_resources_found_cave_effects.txt for dynamic create_unit construction and OOB loading;
- common/scripted_effects/germany_mengele_effects.txt for clone unit/template/stockpile patterns;
- common/scripted_effects/zombie_special_project_effects.txt for route template locking, cleanup, and spawning;
- common/units/018_resources_found_cave_broods.txt and existing custom unit files;
- common/units/equipment/bioweapons.txt, zombie_special_bombs.txt, coal_golems.txt, and existing CBRN equipment.

Every new equipment archetype/type must be added to common/script_enums.txt under script_enum_equipment_bonus_type in the same implementation tranche.

Starting forces must be derived from recorded project deployment/weaponization and formation mode. Repeatable production and reinforcement require real industry, resources, medical capacity, power, feed, containment, paradox, or other route burdens. Do not express all project forces as national modifiers.

### 13. Seventeen achievements

Add all Event 016 achievements to the existing single registry:

- common/achievements/chaos_redux_achievements.txt
- unique_id = chaos_redux_achievements

Do not create a second achievement registry.

Required working keys:

1. 016_brilliant_scientist_borrowed_century
2. 016_brilliant_scientist_every_door
3. 016_brilliant_scientist_public_method
4. 016_brilliant_scientist_the_one_who_left
5. 016_brilliant_scientist_clean_break
6. 016_brilliant_scientist_approve_everything
7. 016_brilliant_scientist_the_former_host
8. 016_brilliant_scientist_combined_arms_redefined
9. 016_brilliant_scientist_clever_girl
10. 016_brilliant_scientist_the_machine_continues
11. 016_brilliant_scientist_population_one
12. 016_brilliant_scientist_yesterday_sent_help
13. 016_brilliant_scientist_not_from_here
14. 016_brilliant_scientist_no_second_sun
15. 016_brilliant_scientist_the_last_calculation
16. 016_brilliant_scientist_the_world_is_the_laboratory
17. 016_brilliant_scientist_ordinary_people_won

The parent rejected the proposed merge. Exactly seventeen working keys are binding. `public_method` and `clean_break` remain distinct achievements and neither may be silently dropped.

Concrete precedent:

- Event 018 achievement entries in common/achievements/chaos_redux_achievements.txt
- Event 018-owned achievement triggers and lifecycle flags

Track original/final host, transfer/removal state, project routes, KRG formation mode, former-host outcome, mixed project formations, dinosaur capture, machine continuation, clone status, temporal rescue, alien evidence, nuclear disqualification, singularity state, Laboratory World, and ordinary-people defeat through Event 016-owned flags and bounded hooks.

Art:

- gfx/achievements/016_brilliant_scientist_<slug>.dds
- matching _grey.dds
- matching _not_eligible.dds

Add name and description keys to localisation/english/chaosx_achievements_l_english.yml.

### 14. Super-events, audio, and world-end presentation

Event 016 requires six distinct super-event roles:

1. international recognition;
2. Kruger State formation;
3. global threat;
4. Laboratory World;
5. Strategic Singularity;
6. defeat aftermath.

Shared registration surfaces:

- interface/chaosx_super_events.gfx
- common/scripted_localisation/chaosx_scripted_localisation_super_events.txt
- common/scripted_guis/chaosx_scripted_gui_super_events.txt
- interface/chaosx_super_events.gui
- localisation/english/chaosx_gui_l_english.yml
- localisation/english/chaosx_music_l_english.yml
- music/chaosx_super_event_music.asset
- music/chaosx_super_event_music.txt
- the repository super-event sound asset registry
- common/scripted_effects/chaosx_settings_effects.txt audio playback helpers

Live Event 015 wiring occupies IDs 85 through 89. The earlier Event 016 proposals of 85 through 90 and 88 through 93 are superseded. Event 016 uses this contiguous block in the established package order:

| Visible super-event ID | Event 016 role |
| ---: | --- |
| 90 | International recognition |
| 91 | Kruger State formation |
| 92 | Global Kruger threat |
| 93 | Laboratory World |
| 94 | Strategic Singularity |
| 95 | Qualifying defeat aftermath |

Re-scan all shared super-event selectors, GFX, music, sound, settings, specs, and concurrent work immediately before live registration. Event 020 separately declares IDs 85 through 87 in its own constants, which overlap Event 015 and require resolution outside Event 016.

Each role needs a unique image and track. The six Event 016-owned tracks are complete at IDs 90 through 95. Their shared playback definitions and the six unique images remain missing. Generic audio is forbidden. Use:

- global.current_super_event_audio_id;
- play_current_super_event_audio;
- super_event_visible;
- the existing user settings and volume path.

Recommended Event 016-owned asset roots:

- gfx/super_events/016_brilliant_scientist/
- music/016_brilliant_scientist/
- sound/016_brilliant_scientist/
- docs/super_events/016_brilliant_scientist_<role>_research.md

The terminal roles must use their distinct Event 016 IDs even though Strategic Singularity shares the canonical Fallout state.

### 15. Portraits, icons, UI art, flags, and animation

The final inventory is docs/specs/016_brilliant_scientist_specs/matrices/016_asset_inventory.md. Key required families are:

- completed and registered Kruger stage 0, plus missing stages I to IV.
- route-specific clone, machine, temporal, xenobiological, and synthesis stage-IV portraits;
- advisor and scientist portrait families;
- directorate background, profile frames, visible meters, control states, project/facility/contact cards, sovereignty panel, and singularity indicator;
- report images, news images, super-event images, defeat/remnant images;
- focus, idea, decision, category, technology, special-project, achievement, filter, faction, equipment, and unit icons;
- base and route KRG flags at normal, medium, and small sizes.

Recommended asset roots:

- gfx/event_pictures/016_brilliant_scientist/
- gfx/interface/016_brilliant_scientist/
- gfx/interface/ideas/016_brilliant_scientist/
- gfx/interface/goals/016_brilliant_scientist/
- gfx/interface/technologies/016_brilliant_scientist/
- gfx/interface/equipmentdesigner/016_brilliant_scientist/ where appropriate
- gfx/leaders/KRG/
- gfx/flags/, gfx/flags/medium/, and gfx/flags/small/
- gfx/achievements/

Stable stage I through IV static and animated sprite contracts are pre-registered in `interface/016_brilliant_scientist.gfx`. Asset workers must produce the exact missing files named by those contracts and must not infer that registration means the assets exist.

Animation ownership:

- Use chaos-redux-event-assets for all final visual assets.
- Use chaos-redux-frame-animation for clone, machine, temporal, xenobiological, synthesis, warning, active-project, and singularity animation packages.
- Each animation needs separately generated, sourced, or provided source frames, a static fallback, manifest, contact sheet, preview, final frame sheet, and GFX/GUI handoff.
- Moving, scaling, rotating, warping, blurring, recolouring, or filtering one still image is not a valid final animation.

The main agent owns final GFX/GUI wiring and verification even when an asset subagent produces files.

### 16. Localisation, docs, event catalog, and completion surfaces

Gameplay, Event Details, evolutions, assets, documentation, and the workbook must use the same final wording.

Shared localisation surfaces:

- localisation/english/chaosx_event_names_l_english.yml
- localisation/english/chaosx_gui_l_english.yml
- localisation/english/chaosx_achievements_l_english.yml
- localisation/english/chaosx_music_l_english.yml

Event-owned localisation should carry ordinary event/decision/focus/project/country/unit text. The exact split may follow file size and ownership, but every file must retain UTF-8 BOM.

Final mechanic documentation should live at docs/016_brilliant_scientist.md and include:

- system overview;
- step-by-step lifecycle;
- variables, flags, event targets, and constants;
- directorate and project rules;
- foreign interaction;
- KRG formation and routes;
- AI;
- units and equipment;
- world threat and terminal paths;
- achievement hooks;
- asset inventory and exact sprite/file wiring;
- future plans and depth suggestions;
- known interactions with biowarfare, contamination, Deaths, Condemnation, Chaos, world-end settings, and Event Details.

Spreadsheet:

- docs/spreadsheets/chaos_redux_events_catalog.xlsx

Use chaosx_spreadsheet_doc_worker only after final implementation facts and in-game localisation exist. Event detail, evolution detail, and cluster-related columns must match in-game text exactly. Event 016 has no cluster.

Do not let a workbook pass overwrite concurrent edits. Re-check its Git status and coordinate ownership immediately before spreadsheet work.

## Shared hot spots and ownership boundaries

The following files are high-collision shared surfaces. The Event 016 implementer should make narrow identifier-based edits and re-read the live file immediately before patching:

| Shared file | Event 016 responsibility |
| --- | --- |
| common/scripted_effects/chaosx_logic_effects.txt | Availability branch only; Event 16 is already registered |
| common/scripted_triggers/chaosx_settings_triggers.txt | Final default-enable allowlist entry |
| common/scripted_effects/chaosx_settings_effects.txt | Prefire and scoped dispatch; shared super-event audio only as needed |
| common/scripted_effects/chaosx_events_log_effects.txt | Actor, four preview rows, world-end registry and active mapping, Events-tab impossible state |
| common/scripted_localisation/chaosx_scripted_localisation_events_log.txt | Complete Event 016 evolution/detail/history/world-end routing |
| common/script_constants/world_end_scenario_registry_constants.txt | Append scenario IDs 11 and 12, owner 16, and super-event mappings 93 and 94 |
| common/scripted_effects/chaosx_dynamic_effects.txt and .md | Threat source and only genuinely cross-event helpers |
| common/scripted_triggers/chaosx_dynamic_triggers.txt and .md | Special/nonhuman classification |
| common/scripted_triggers/chaosx_world_threat_triggers.txt | Event 016 world-threat source |
| common/scripted_triggers/chaosx_world_end_scenario_triggers.txt | Two independent scenario gates |
| common/scripted_effects/chaos_meter_effects.txt | Canonical Chaos and Air Contamination consequence calls only |
| common/scripted_effects/fallout_world_end_effects.txt | Fallout-owned request intake called by the Event 016 terminal bridge |
| common/script_constants/fallout_world_end_constants.txt | Event 016 request-source identity only if the parent confirms a dedicated source entry |
| common/script_constants/chaos_meter_constants.txt | New Deaths reason only if required |
| common/script_constants/condemnation_sanctions_constants.txt | New singularity context only if required |
| common/scripted_effects/condemnation_sanctions_effects.txt | Call existing public entry effect; do not bypass it |
| common/special_projects/specialization/chaosx_specializations.txt | Reuse existing bio/chemical fields; no duplicate specialization |
| common/script_enums.txt | Every new equipment bonus type |
| common/countries/cosmetic.txt | KRG route cosmetics |
| common/achievements/chaos_redux_achievements.txt | Seventeen entries in the one registry |
| interface/chaosx_super_events.gfx | Six final sprites for visible IDs 90 through 95 |
| common/scripted_localisation/chaosx_scripted_localisation_super_events.txt | Six full selector routes |
| music/chaosx_super_event_music.asset and .txt | Six final tracks |
| localisation/english/chaosx_gui_l_english.yml | Details/evolutions/world-end/super-event shared keys |
| docs/spreadsheets/chaos_redux_events_catalog.xlsx | Final exact text alignment only |

Parent/main agent ownership:

- final design interpretation;
- final tag, event ID, super-event ID, cosmetic tag, sprite, and localisation-key reservations;
- all shared-file wiring;
- review of every subagent patch;
- final Event 016 to Fallout request-source mapping.
- final AI and balance integration;
- final asset and audio registration;
- final workbook merge;
- final audits, validation, completion claim, and Git history.

Subagent boundaries:

- Repo explorer: evidence and path/precedent map only.
- Scripted system architect: reusable helpers, source contexts, event targets, constants, and dynamic effect/trigger design; no broad gameplay implementation unless explicitly granted.
- Decision/mission worker: directorate and foreign decision surfaces within fixed effects/contracts.
- Country/focus worker: KRG package, focus tree, route AI, units where granted.
- Asset workers: source, generated, processed, DDS, manifest, contact sheet, preview, and handoff; no final shared GFX wiring.
- Super-event text and audio research workers: completed their bounded research and Event 016-owned audio outputs. They did not implement shared selectors or playback wiring.
- Spreadsheet worker: post-implementation workbook alignment only.
- Auditors: report or narrow in-scope fixes according to parent-granted mode; they do not redefine the accepted design.

## Concurrent-work and dirty-worktree risks

At the final pre-write status check, unrelated tracked and untracked changes were present. They include work on:

- Event 005 Soviet collapse;
- Event 006 Independence Wave assets/plans;
- Event 014 scenario constants;
- Event 015 plans and super-event research;
- Event 019 constants;
- triggerable scenarios;
- air-cleanliness winter effects, triggers, UI, assets, plans, and documentation;
- fallout_world_end_events.txt and the dedicated Fallout effects, triggers, constants, GUI, music, and sound files.
- localisation/english/chaosx_gui_l_english.yml;
- numerous chemical-air visual assets.

This list is descriptive, not ownership. Re-run git status --short before every implementation tranche. Never restore, reset, format, stage, or commit unrelated files.

Most important collision risks:

1. chaosx_gui_l_english.yml is already shared by concurrent world-end/UI work.
2. Fallout and triggerable-scenario files are active work areas. Design the Strategic Singularity request bridge against the live post-merge version.
3. Super-event IDs are not reserved by an apparent gap.
4. KRG is free in the inspected repository and vanilla, but needs a final whole-load-order check.
5. The event catalog workbook may change independently; spreadsheet work must be serialized.
6. The default-enabled allowlist must be the final tranche, not the first.

## Safest implementation order

### Tranche 0: reservations and contracts

- Re-scan KRG, event/news namespace IDs, super-event IDs, cosmetic tags, sprite names, technology/project IDs, unit/equipment IDs, and achievement keys.
- Preserve Event 020 scenario ID 10 and reserve Event 016 world-end scenario IDs 11 and 12.
- Preserve Event 016 IDs 90 to 95 in the fixed six-role order. Event 015 occupies 85 through 89. Treat Event 020's separate 85 through 87 declarations as an external overlap to report, not as the Event 016 allocation reason.
- Decide and document the Event 016 request-source mapping into the dedicated Fallout coordinator.
- Freeze Event 016 constants categories, persistent flags, event targets, and helper contracts.
- Merge accepted architectural decisions into the Event 016 source spec where needed.

### Tranche 1: random-event foundation and persistent Kruger

- Add Event 016 constants, eligibility triggers, prefire resolver, scoped dispatch, Events-tab unavailable state, and event-log actor mapping.
- Rebuild chaosx.nr16.1 entry flow.
- Create the single all-field Kruger scientist, advisor role, opening +100% idea, removal/transfer safety, and base localisation.
- Keep Event 16 disabled by default.

### Tranche 2: directorate and ordinary host loop

- Implement variables, staged ideas, decisions, missions, targeted clocks, scripted GUI, tooltips, and AI.
- Deliver visible Mandate, Dependence, Exposure, and Project Capacity plus hidden Independent Capacity and Grievance consequences.
- Implement safe removal, foreign transfer, assassination/security, publication, replication, and ordinary resolution.

### Tranche 3: project portfolio and world interaction

- Implement the fifteen families in reviewed groups.
- Reuse bio/chemical shared systems.
- Add accidents, foreign operations, counters, AI, project assets, and project-derived technologies/equipment/units.
- Record exact implementation facts in docs after each family group.

### Tranche 4: evolutions and Event Details

- Add four once-only evolution wrappers.
- Add four preview rows and the complete scripted-localisation selector surface.
- Ensure actor, chronology, tier gating, disabled-evolution behavior, and workbook-ready wording are correct.

### Tranche 5: KRG country package and focus tree

- Implement all four formation modes and actual history-derived starting state.
- Add country, history, OOB, cosmetics, classifications, focus tree, AI strategies/templates, route forces, former-host handling, and defeat behavior.
- Run country-package and focus-tree audits before terminal work.

### Tranche 6: terminal systems and super-events

- Implement world-threat gates, Laboratory World, Strategic Singularity, the dedicated Fallout request bridge, Deaths, Condemnation, Chaos consequences, aftermath, two world-end registry rows, and six final super-events.
- Preserve the collision-audited Event 016 IDs 90 through 95 and re-scan before shared registration.
- Preserve the completed audio licences, source docs, and Event 016-owned OGGs. Finish shared settings-aware playback.

### Tranche 7: achievements, assets, docs, and workbook

- Wire all seventeen achievements and three-state icon sets.
- Complete every portrait, UI, report, news, flag, focus, decision, idea, project, unit, equipment, achievement, and super-event asset.
- Finish animation packages with real source frames and static fallbacks.
- Update docs/016_brilliant_scientist.md and exact sprite wiring inventory.
- Run the spreadsheet worker only after final localisation is stable.

### Tranche 8: audits and enablement

- Run decision/mission, country-package, focus-tree, localisation, and Event 016 completion audits.
- Reconcile audit findings and any accepted improvement addendum.
- Verify route coverage, AI, balance/exploits, terminal paths, asset registration, event log/details/evolutions, workbook, and documentation.
- Only then add Event 16 to event_log_event_is_reworked_default_enabled.
- Commit each complete tranche separately and never bundle unrelated concurrent work.

## Missing decisions that require explicit resolution

These are not permission to guess:

- Final KRG tag confirmation against the whole enabled load order.
- Event 016 reservations are fixed at world-end IDs 11 and 12 plus visible super-event IDs 90 to 95. Re-scan for later concurrent collisions before live registration.
- Exact event/news sub-ID plan beyond the fixed chaosx.nr16.1 root.
- Exact route cosmetic-tag tokens and sprite names.
- Exact character-transfer strategy when Kruger changes countries or becomes KRG leader.
- Final Event 016 request-source mapping into `fallout_request_aftermath`.
- Whether Strategic Singularity requires a new shared Deaths reason and Condemnation context.
- Final mapping of existing biowarfare projects into the Event 016 portfolio.
- Exact project/technology/unit/equipment identifiers and balance values.
- Exact country-state derivation rules for the four KRG formation modes.
- Achievement count is resolved at exactly seventeen; `public_method` and `clean_break` are distinct.
- External redistribution status for the completed `portrait_generic_biowarfare_europe_male_01` copy. Internal Event 016 use is user-authorized.
- Final workbook ownership window.

## Completion boundary

This handoff completes only the requested repository integration map. It does not establish that Event 016 is implemented or ready to enable.

No implementation simplifications were introduced in this map. Every accepted route and subsystem remains in scope, including four evolutions, fifteen project families, the full 85-to-115-focus KRG tree, six super-events, two world-end scenarios, the dedicated Fallout request bridge, and seventeen achievements.
