# Event 013 dynamic API and geographic-target audit handoff

Date: 2026-07-26.

Audit mode: read-only scripted-system architecture review.

Conclusion: no gameplay patch is justified by the current contract. Event 013 already routes the requested family, target, severity, notification, aftermath, follow-up, and scale inputs through one reusable runtime. The delayed queue and geography gates satisfy the checked invariants. No GUI, scripted GUI, shared super-event, or map source was edited.

## Scope reviewed

The audit covered `common/scripted_effects/013_natural_disasters_effects.txt`, `common/scripted_triggers/013_natural_disasters_triggers.txt`, `common/scripted_triggers/013_natural_disasters_geography_triggers.txt`, `common/script_constants/013_natural_disasters_constants.txt`, `common/scripted_effects/chaosx_dynamic_effects.txt`, `events/013_natural_disasters.txt`, `events/099_desert_storm.txt`, `common/scripted_effects/chaosx_event_cluster_effects.txt`, and `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt`.

The actual public callers are the canonical Event 013 entry, the Event 099 compatibility bridge, the event-cluster member path, and the Disaster Barrage scenario path. No second public disaster implementation or copied damage/report/aftermath path was found.

## Reusable helper map

| Helper | Scope | Inputs | Outputs and side effects | Verified call sites |
| --- | --- | --- | --- | --- |
| `call_natural_disaster` | country | documented `natural_disaster_call_*` temporary inputs and regular target scopes | delegates to `natural_disaster_call`, then resets public inputs while leaving result/proof outputs available | Event 013, Event 099, Cluster 5, SCN-007 |
| `natural_disaster_call` | country | normalized family/group, target mode, origin proof, severity, sequence, policies, scales, and private continuation proof | validates, allocates one sequence, resolves the first target, queues delayed jobs, records outputs, and restores the global sequence counter on zero-hit rejection | public wrapper and internal physical continuation |
| `natural_disaster_resolve_target` | country with state/country/region subscopes | exact family and fixed target domain | applies target-mode selection without widening a pinned state/country/region domain and rechecks family geography | sequence planner and physical-chain continuation |
| `natural_disaster_is_valid_family_target` | state | current family, origin context, path basin, heat overlap state | fail-closed physical and runtime eligibility gate | all target selection, spread, repeat, and delayed-state revalidation paths |
| `natural_disaster_enqueue_state_job` / `natural_disaster_process_due_job` | state/country | job type, delay, state payload, aligned metadata arrays | reserves a unique due date, clamps worker delay to at least one day, pops aligned rows, and dispatches warning/impact/report/news/follow-up/reassessment | all delayed Event 013 subevents |
| `natural_disaster_fire_family_report` and `natural_disaster_activate_aftermath_for_state` | impacted state with controller/caller subscopes | immutable job snapshots, report policy, aftermath policy | snapshots the report, sends the affected controller report for every enabled policy, adds caller/global recipients when requested, and raises controller aftermath visibility/unread flags | every physical impact and external caller path |

## API coverage

The live API supports a specific family, random family, or family group; `random_valid`, `selected_state`, `selected_country`, `selected_region`, `coast`, `nearby_enemy`, `dense_state`, and `caller_provided` target modes; severity; sequence mode/count; news policy; report policy; aftermath policy; follow-up policy; evolution/scenario context; and independent death, building, warning, recovery, and supply scales. `natural_disaster_call_damage_scale` remains a compatibility alias for `natural_disaster_call_building_scale` when the explicit building scale is omitted.

The result contract initializes `natural_disaster_call_result`, `natural_disaster_call_reject_reason`, `natural_disaster_call_sequence_id`, `natural_disaster_call_primary_job_count`, `natural_disaster_call_skipped_primary_count`, the resolved-family value, numeric target-proof values, and the selected-region echo before every call. The first accepted primary hit saves `natural_disaster_call_resolved_primary_state` and `natural_disaster_call_resolved_primary_country` as regular event targets. Callers are expected to test the numeric proof outputs because regular targets can remain present from an earlier request in the same effect chain.

## Delay and cleanup proof

`natural_disaster_set_next_gap` chooses a first impact in the two-to-four-day band and later sequence gaps from the evolution tuning table. Warning scheduling subtracts one day and clamps to `minimum_job_delay_days`. Reports use the one-to-two-day report band. News uses the one-day minimum. Physical follow-ups use family-specific minimums of at least two days. Reassessment uses recovery constants of 14 days or more. `natural_disaster_enqueue_state_job` converts the absolute due date to a normal delay variable, clamps the worker to at least one day, and reserves same-sequence calendar dates. `natural_disaster_process_due_job` only pops due rows and removes every aligned array row before dispatching a new job. Therefore the audited delayed warning, impact, report, news, follow-up, and reassessment paths cannot intentionally execute on the call or impact date.

Regular event targets are short-lived chain targets. Persistent state is carried in state variables and controller-owned aligned queue arrays. The reviewed code does not introduce global event targets for concurrent sequence payloads, and the existing state-control transfer hook moves future queue rows to the new controller and re-schedules the worker.

## External report and aftermath behavior

`natural_disaster_fire_family_report` writes immutable report snapshots on the impacted state before dispatch. The affected controller receives the family report for the default, caller, global, silent, and delayed-batch policies; caller policy additionally dispatches to the persisted caller country, and global policy additionally dispatches to every existing country. `silent` suppresses only additional distribution in the live contract and does not suppress the affected controller report. `natural_disaster_activate_aftermath_for_state` independently raises the current controller's aftermath category visibility and unread flags, adds the aftermath idea where applicable, and keeps the card on the affected state even when the event caller has already returned.

## Geography findings

`natural_disaster_is_valid_family_target` composes the immutable geography registry, origin-dependent proof, initiating context, locked path basin, owner/population/runtime guards, and the Event 051 heat-overlap exclusion. The geography registry maps volcanic eruption to the reviewed vent-state list, massive eruption and lahar to strict subsets, ashfall to a plume receptor domain plus a validated volcanic origin, heat wave to the positive heat allowlist minus the cold allowlist, dust and sandstorm to the arid domain, tsunami to an exposed coast plus a saved compatible seismic/volcanic/ocean origin and basin, storm surge to coastal surge domains, and slope families to the shared reviewed slope registry plus separate dry/wet initiating context. Spread, repeat, path, and delayed-state checks call the same physical predicates again.

## Region-scope nuance

The older architecture plan described a possible optional `target_country` constraint for `selected_region`. The live `selected_region` implementation searches only the supplied strategic region and does not additionally constrain that search to an optional supplied country. The current call matrix, live dynamic-effect documentation, and 2026-07-11 geography handoff describe `selected_region` as a region-only fixed domain, and no current caller supplies both a selected-region mode and a target-country scope. This is therefore recorded as an unresolved contract choice rather than patched speculatively. If a future caller needs region-plus-country intersection, the public contract and validation must be amended first, then both region selectors (`natural_disaster_select_suitable_state_from_target_region` and `natural_disaster_select_ocean_impact_proxy`) should receive the same bounded ownership predicate.

## Constants and tuning

No constants were added or changed. The relevant shared values remain in `common/script_constants/013_natural_disasters_constants.txt`, including family/target/report/aftermath/chain enums, first-impact and report delay bands, same-sequence reservation guards, minimum worker delay, family-specific follow-up bands, scale bounds, and the maximum strategic-region id.

## Migration and call-site status

No migration was required. All live callers already use `call_natural_disaster`; Event 099 remains a narrow bridge; Cluster 5 and SCN-007 pass explicit target and policy context; internal physical follow-ups use the private validated continuation fields and do not create a second public history row. No duplicated caller-side Deaths, building damage, report dispatch, aftermath activation, or follow-up implementation was found.

## Validation evidence

The offline Paradox wiki core pages and relevant vanilla documentation for effects, triggers, event timing, scopes, event targets, delayed events, and script constants were consulted before this audit.

Read-only HOI4 MCP Event inspection was run with selector `chaosx.nr13.1` and helper expansion. The scan returned a partial whole-game inventory and linked artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/40dcb76aebb6b4689efde69fa0018d31196cb608469498f2fa61a25ee70965d0/9348c7789033dd938fd026103e29a4e62e4102c683f9e13383125d02518237c3/event-scan-482294e452ad.json`.

Read-only HOI4 MCP map inspection sampled states `115`, `64`, `366`, `637`, `563`, `514`, `890`, `383`, `138`, `147`, `148`, `149`, `150`, `151`, `255`, and `266`, plus regions `127`, `134`, `147`, `148`, `149`, `150`, `151`, `255`, `256`, `257`, and `266`. State-region membership passed and the linked artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1ad78ef952f643616ee1bf5a2fb70885f1c3d1896e580c6a94309f298d2d4991/8ed5643f57d342afa1f30f4410dab44aad0e5f46ab143078e779b87a9f2054a8/map-inspect.15b01578cf3785a8.json`. The MCP also reported unrelated project-wide map locator and localisation diagnostics; none were introduced or changed by this audit.

Static source review confirmed no Event 013 delayed `days = 0` or `hours = 0` dispatch, no whole-world periodic on-action added by this surface, and no geography fallback that widens an explicit family or pinned target. No in-game run was performed, as required by repository policy.

## Known limitations and follow-up

The MCP Event scan is a whole-game partial scan rather than a complete inline Event 013 proof. The MCP map result includes unrelated global diagnostics. Live-engine behavior for Clausewitz scope resolution, delayed-event wakeup ordering, and the external caller's player-facing notification remains a user-owned runtime validation step. The selected-region plus optional-country contract must be resolved before adding any caller that depends on that intersection.

No gameplay simplification, fallback, GUI change, super-event change, or unrequested helper was introduced.
