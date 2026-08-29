# Event 021 and Event 033 adapter-owner handoff

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

Status: API-only and intentionally unpatched because the live event owners do not expose the exact proof required by the shared famine and migration contracts.

Date: 2026-08-25 Europe/Kyiv.

Scope: Event 021 Random Civil War and Event 033 Acid Rain only.

The famine and migration mechanics remain separate. Food, crop, water, and Air Cleanliness consequences may enter famine only through a proven state-local receipt. Displacement, evacuation, trapped population, and return consequences may enter migration only through a proven cohort and route receipt. No implicit combined call is valid.

## Files changed

Only this handoff was added:

- `docs/plans/famine_and_migration_system_plans/subagent_handoffs/event021_033_adapter_owner_patch.md`

No event source, `021_*` or `033_*` owner helper, localisation, asset, central famine/migration source, workbook, pool row, pacing pulse, event log entry, probability weight, or event ID was changed.

## Live owner evidence

### Event 021 Random Civil War

`events/021_random_civil_war.txt:22-70` resolves a `random_country` and then runs one ideology branch of `start_civil_war`.

Each branch supplies only an ideology and `size = 0.5`; there is no `states` list, capital, affected-state target, actor target, amount, cohort, route, or transaction/replay proof.

The `size` field is the civil-war partition factor and is not a people-denominated civilian amount. The event source has no exact civilian loss, food loss, displacement cohort, trapped cohort, destination, or return receipt, and it does not mutate a Deaths ledger or invoke a central movement transfer.

The current owner surface also has no stable callback that exposes the actual rebel country together with the original country, affected state, current owner/controller, and war-state facts. The country-level war reassessment hook does not supply that state-local transaction.

Therefore `famine_migration_request_war_pressure` and `famine_migration_request_event_pressure` are not safe calls from the civil-war root, its ideology branches, or the generic war reassessment path.

### Event 033 Acid Rain

`events/033_acid_rain.txt:22-181` selects a continent, adds `acid_clouds_state` to every state on that continent, selects one `random_state` and its neighboring states for `acid_rain_state`, and schedules a report event.

The selected state and neighboring scopes are used only while adding modifiers. No per-state event target or impact ledger persists the selected state, and no exact food, water, crop, civilian, cohort, actor, contamination, destination, route, shelter, or return proof is recorded.

`common/scripted_effects/033_acid_rain_effects.txt:1-54` derives `global.acid_clouds_time` from the number of states in the selected continent. That duration is not a population amount or contamination receipt.

`common/on_actions/033_acid_rain_on_actions.txt:7-31` performs an existing daily owned-state scan and applies building and unit damage. It does not expose an exact food or water loss, actor, cohort, or route, and it is not a safe famine or migration adapter callback. Adding another scan or calling an adapter from this repeated effect would violate the bounded owner contract.

`common/dynamic_modifiers/033_acid_rain_dynamic_modifiers.txt:4-42` exposes only state modifiers such as local resources, local supplies, attrition, and production penalties. It does not prove an applied civilian amount or responsible actor.

The event source has no direct Deaths mutation. Any future direct environmental or chemical mortality remains owned by that owner and must not be debited again by a famine adapter.

## Public API review and proposed helper map

The existing public contract was inspected in `common/scripted_effects/chaosx_famine_migration_effects.txt` and `common/scripted_effects/famine_migration_adapter_effects.txt`.

| Owner seam | Required scope and proof | Existing public operation | Current result |
| --- | --- | --- | --- |
| Event 021 war-to-famine | Affected state, actual rebel and original countries, current war/controller facts, positive people amount, responsible actor, causal transaction proof, and replay guard. | `famine_migration_request_war_pressure` or a source-specific pressure request after setting `famine_migration_pressure_request_proven`, `famine_migration_pressure_request_amount`, and `famine_migration_pressure_request_actor_proven`. | No exact source callsite exists; no helper added. |
| Event 021 displacement/flight | Exact origin state and country, actual rebel/original relationship, positive cohort amount, destination or border route, transport/safety/actor proof, and route replay guard. | `famine_migration_request_internal_displacement`, `famine_migration_request_cross_border_flight`, and `famine_migration_transfer_civilians_exact`. | No exact source callsite exists; no movement or Deaths call added. |
| Event 033 contaminated food/water/crops | Exact affected state, owner-applied amount, acid-rain actor, contamination and Air Cleanliness proof, and one-shot impact receipt. | `famine_migration_request_air_cleanliness_pressure` or another source-specific pressure request after the exact proof fields are set. | Modifier presence and duration are insufficient; no helper added. |
| Event 033 evacuation/shelter | Exact origin state and cohort, evacuation amount, destination shelter or reception state, route/border/transport/safety/actor proof, and one-shot transaction guard. | `famine_migration_request_organized_evacuation` followed by `famine_migration_transfer_civilians_exact`. | No exact source callsite exists; no route created. |
| Event 033 delayed return | Existing cohort ID, original-state resolution, positive returned amount, contamination-clear and food/housing/host/route proof. | `famine_migration_request_voluntary_return` or `famine_migration_request_forced_return` followed by the validated return transfer. | No exact cohort or return facts exist in the event source; no return helper added. |

The shared pressure validator requires a valid state, a positive people amount, non-unknown source, and actor proof. The route validator additionally requires border, transport, safety, and actor proof plus a persisted valid destination. Neither event currently supplies those inputs.

## Deaths and movement ownership

Event 021 currently creates a civil war but does not apply civilian Deaths. If a future owner callback applies a direct loss, that owner retains the existing Deaths reason and the adapter registers only the delayed famine consequence from the exact applied amount. Forced movement is not death; the origin-state debit, route deaths, and survivor destination credit belong to `famine_migration_transfer_civilians_exact` and must not be duplicated by a pressure adapter.

Event 033 currently applies environmental modifiers and infrastructure/unit damage but no civilian Deaths. If a future acid-rain or chemical owner applies direct mortality, that owner retains its Deaths reason. A famine adapter may register later hunger or contaminated-food pressure only from an exact food/water/crop receipt and must never create a second environmental mortality debit. Evacuation and delayed return use the central movement transaction, with route deaths remaining movement-owned.

## Event-target, cleanup, and migration plan

No event target, persistent flag, global variable, recurring action, or cleanup helper was added because neither event has a proven transaction to persist.

A future exact owner callback may use a regular `save_event_target_as` for an immediate state, actor, or destination handoff within one effect chain. It must clear temporary proof and request fields after the shared API returns and must use a transaction-specific one-shot guard. A global target is not justified by the current event surfaces.

Event 021 needs an owner-side callback that captures the actual rebel/original pair, affected state, controller/owner facts, and a concrete state-local war or displacement receipt before calling the existing public APIs. The `start_civil_war` root alone is not sufficient.

Event 033 needs an owner-side per-impact callback that captures the exact state, actor, amount, cohort, and contamination or route receipt at the operation that actually resolves food/water pressure or evacuation. The existing continent-wide modifier setup and daily damage scan must not be repurposed as an adapter transaction.

No new constants or tuning table is justified by this pass. No probability-bearing helper was touched, so the probability workflow is not applicable.

## Missing owner inputs

The exact missing facts are listed separately by mechanic seam.

| Event | Famine inputs still missing | Migration inputs still missing |
| --- | --- | --- |
| 021 | Affected state, current owner/controller, actual rebel and original countries, positive food/front/route pressure amount, responsible actor, causal war-state receipt, and replay guard. | Origin state, actual rebel/original countries, positive displaced/trapped/return cohort amount, destination or border route, transport/safety/actor proof, and replay guard. |
| 033 | Per-state contaminated food/water/crop amount, affected state, responsible acid-rain actor, contamination/Air Cleanliness proof, and one-shot impact receipt. | Evacuated or shelter cohort ID and amount, exact origin and destination, route/transport/safety/actor proof, contamination-clear and reception proof for return, and replay guard. |

No generic civil-war proxy, continent modifier, fixed history total, global scan, or `size = 0.5` interpretation can substitute for these inputs.

## MCP evidence

Required offline wiki pages, vanilla documentation, and vanilla precedents were reviewed before source decisions. The relevant vanilla precedents explicitly provide state context when a civil war consequence needs it, for example `events/AAT_Sweden.txt:4902-4905` supplies an explicit `states` list and `events/BBA_Ethiopia.txt:50-78` resolves a capital before `start_civil_war`; Event 021 supplies neither.

Preflight `hoi4.event_inspect` calls were run with `state_flow` and `lint` for both `chaosx.nr21.1` and `chaosx.nr33.1`, using `expandHelpers = true`, `refresh = true`, and bounded depth/node/edge limits. All four returned `status = ok`, code `EVENT_INSPECTED_PARTIAL`, workspace `mod_chaos_redux_ea3b2d67c2c0`, and no blocking diagnostics. Each reported `MCP_INLINE_FILES_TRUNCATED` and validation false because workspace-wide helper projections were deferred. The authoritative artifacts were:

- Event 021 state flow: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b0e8e53a0f849961763c39e5f5e4a46985bf6abb2060bc82151f30ce52c2611c/623feb45999459f90870633d4c50785ce93ac65fb0a092c7fac178b170c6f6f4/event-state_flow-59143acd4a23.json`
- Event 021 lint: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6cac1fe59d0c54a9f1bc9cf5efb93f25cbf65d633ef31060ea4bbe924856175/5aa66799804e3b2a87016b1b6432f0a350ab03330a8023ad2c9d6ce0801ccc37/event-lint-59143acd4a23.json`
- Event 033 state flow: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8234d93e1b5425701e9b757aa95996f20779d2456f6a50b6fdf75c11e61dce12/25d70e1e39792501509a2f3fa591715889467b194fbe7cd022b534750c7a2641/event-state_flow-59143acd4a23.json`
- Event 033 lint: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b25c5e28dcb4c3c1c9ea36acadf89c3761bb24a6a6c14a68790da197741063d9/e172e9f1fa953ed431149e73c793ac2cd762b962b5073b523d8c6af56cf23bef/event-lint-59143acd4a23.json`

Relevant `hoi4.event_render` views (`overview`, `state`, `scope`, `targets`, and `unresolved`) were requested for both event roots with bounded depth and node limits. Every render call failed with the exact blocker `tool call failed for hoi4_agent_tools/hoi4.event_render: timed out awaiting tools/call after 180s`; no render artifact was produced.

The post-pass bounded `hoi4.event_inspect` re-inspection for both roots also failed with the exact blocker `tool call failed for hoi4_agent_tools/hoi4.event_inspect: timed out awaiting tools/call after 180s`. Since no gameplay source was edited, no source compare artifact exists; the preflight artifacts and local post-pass source check remain the authoritative evidence for this no-op owner pass.

## Validation and limitations

The in-scope event and owner files were reread after the inspection. A repository search found no existing `famine_migration` callsite in Event 021, Event 033, or existing `021_*`/`033_*` owner files. The inspected event sources therefore retain their original structure, with no accidental central API call, Deaths mutation, route transaction, whole-world scan, or probability change.

No game launch or live save validation was performed, as required by repository policy. No adapter implementation can be claimed complete until an event owner supplies the missing exact facts above. This is a deliberate fail-closed omission, not a fallback or simplification.
