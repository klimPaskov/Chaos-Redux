# Event 013 cluster and Disaster Barrage handoff

> Superseded tranche snapshot, 2026-07-12: the three API gaps and Event 099 boundary recorded below were closed afterward. Full Catalogue, intensity-aware family pools, manual evolution/abnormal authority, type-compatible exhaustive targeting, and the narrow Event 099 dust bridge are live. Evolution cluster roles use tiers 1, 2, and 3 for Wider Disaster Seasons, Regional Cascades, and Abnormal Paths. Current authority is `docs/events/013_natural_disasters/overview.md`, `common/scripted_effects/chaosx_dynamic_effects.md`, and `013_event_completion_final_audit.md`.

## Scope

This tranche owns only the shared Natural Disasters cluster and triggerable-scenario integration. It does not edit the Event 013 engine, events, decisions, GUI, assets, achievements, workbook, or related-event files.

## Files changed

- `common/script_constants/event_cluster_constants.txt`
- `common/scripted_effects/chaosx_event_cluster_effects.txt`
- `common/script_constants/chaosx_triggerable_scenarios_constants.txt`
- `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt`
- `common/scripted_triggers/chaosx_triggerable_scenarios_triggers.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_settings.txt`
- `localisation/english/chaosx_gui_l_english.yml`
- `docs/systems/event_clusters.md`
- `docs/systems/triggerable_scenarios.md`
- this handoff

## Natural Disasters cluster

Fresh cluster id `constant:event_cluster_id.natural_disasters = 5` is registered as a repeatable tier-0 cluster with a 120-day cooldown. The cluster maps only Event 013 and contains five logical Event 013 season slots:

| Slot | Minimum tier | Role | Participation | Display danger |
| --- | --- | --- | --- | --- |
| Opening local season | 0 | Required | 100% | Low |
| Additional early season | 0 | Optional | 85% | Low |
| Varied season | 2 | Optional | 60% | Medium |
| Regional season | 3 | Optional | 60% | High |
| Abnormal season | 4 | Optional | 35% | Severe |

Events 046, 051, 099, 043, and 120 are not members. The shared duplicate-member promotion now claims only the first matching trigger member. Later duplicate Event 013 rows retain their optional role and participation chance.

`event_cluster_prepare_runtime_context` performs Event 013 preflight, rejects a cluster that cannot prepare a valid first target, and records the prepared affected country as the cluster actor. Each fired logical slot sets explicit cluster caller, random family, local-season mode, meaningful news, affected-country report, normal aftermath, family follow-up, and Event 013 history policy before calling `call_natural_disaster`. Each accepted slot therefore owns one Event 013 history row while the cluster owns one separate cluster row.

## Disaster Barrage

Scenario id `constant:triggerable_scenario_id.disaster_barrage = 7` replaces the reserved slot and is registered in all id/name sort views. `triggerable_scenarios_disaster_barrage_type` cycles these accepted Event 013 values:

- Random Barrage
- Geological Crisis
- Weather Crisis
- Skyfall Crisis
- Full Catalogue

`trigger_disaster_barrage_scenario` calls the Event 013 public API once from the launching country. It supplies an explicit random family request, selected-country target, barrage sequence mode, affected-country report policy, news policy, aftermath policy, follow-up policy, scenario type, shared four-stop intensity, and `scenario_history` log mode. Full Catalogue uses major-only news. Medium uses regional severity and full aftermath, High uses catastrophic severity and emergency aftermath, and Maximum requests abnormal severity, emergency aftermath, and abnormal-path follow-ups. Maximum grants `natural_disaster_manual_abnormal_access` only for the API call and removes it afterwards when the scenario added it.

The launch gate blocks only an active terminal `world_end` state or the absence of a valid controlled impact state. The Disaster Barrage helper does not set `world_end`, does not call copied damage logic, and does not add a periodic on-action.

## Localisation keys added

- `chaosx.event_cluster.natural_disasters.name`
- `chaosx.events_log.window.cluster_details.description.natural_disasters`
- `chaosx.scenarios.entry.id.disaster_barrage`
- `chaosx.scenarios.disaster_barrage.name`
- five `chaosx.scenarios.disaster_barrage.desc.*` keys
- four `chaosx.scenarios.disaster_barrage.impact.*` keys
- five `chaosx.scenarios.type.disaster_barrage.*` keys

Cluster name mappings were added to History, catalogue, selected details, and Settings. Event 013 was added to the cluster-member event-name selector.

## Focused validation

- Cluster definition id is unique and registry arrays remain aligned.
- The Natural Disasters member branch contains five Event 013 rows, one required role, four optional roles, and no Event 043, 046, 051, 099, or 120 row.
- Scenario registry contains eight ids and each of the four sort views contains eight rows.
- Disaster Barrage has one public API call and no `world_end` mutation.
- Script brace counts match in every touched script and scripted-localisation file.
- Added localisation keys are unique and the English localisation file remains UTF-8 with BOM.

## Required Event 013 engine follow-up

The shared integration exposes three existing Event 013 API gaps that cannot be corrected inside this tranche's ownership boundary:

1. `natural_disaster_resolve_random_family` has explicit Geological, Weather, and Skyfall branches, but no explicit Full Catalogue branch. Full Catalogue therefore still inherits the live evolution pool instead of its accepted broad, minimally restricted pool.
2. Geological, Weather, and Skyfall weights include abnormal families without checking scenario intensity. Below Maximum, the current resolver can downgrade an abnormal selection to `meteor_impact`, which can also make a Weather Crisis produce a skyfall family. The engine needs intensity-aware family eligibility before the weighted roll.
3. Maximum grants manual abnormal access, but `natural_disaster_abnormal_family_is_allowed` still rejects while the global abnormal cooldown is active. The scenario launch also passes through `natural_disaster_refresh_evolution_state`, which can record a normal Evolution III milestone for a manual scenario bypass. The Event 013 API needs a tightly scoped scenario-bypass input that ignores the abnormal cooldown for this launch and suppresses normal evolution milestone logging without changing live automatic behavior.

Until these three engine hooks are patched, the registry, controls, policies, history ownership, and non-terminal launch wrapper are wired, but Full Catalogue and Maximum cannot be claimed fully spec-complete in every campaign state.

## Event 099 boundary

Event 099 remains a harmless placeholder and is not part of this cluster. Its three Event 070 callsites still target that placeholder. A narrow Event 099-to-Event 013 dust bridge requires a separate accepted history-ownership and caller-cost decision, plus explicit authority to edit Event 099 or Event 070. No Event 099 fallback or duplicate dust damage was added here.

## Skills used

- `chaos-redux-events`
- `chaos-redux-subagents`
- `chaos-redux-improvement-loop`
- `hoi4-mtth` for timing guidance review. No MTTH entry was needed because this tranche uses existing cluster cooldown and scenario intensity controls.

No commit was created.
