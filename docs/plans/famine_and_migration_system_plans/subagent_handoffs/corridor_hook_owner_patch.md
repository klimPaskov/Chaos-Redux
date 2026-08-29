# Corridor hook owner patch

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

## Scope and result

This bounded patch wires the existing famine/migration callbacks to the exact corridor contract without adding a recurring world scan. State-control, war/peace, peace-conference, and nuclear callbacks now reach corridor-owned helpers from the existing `common/on_actions/chaosx_famine_migration_on_actions.txt` surface.

Control transfer is treated only as persisted-origin/front invalidation with `famine_migration_corridor_reason.control_change`. It never writes attack proof. War and peace callbacks validate only the named countries' mirrored origin rows and the stored route relation. The nuclear callback uses the documented receipt (`ROOT` launcher, `FROM` nuked state) and fails closed when the exact corridor identity cannot be resolved.

## Files changed

- `common/on_actions/chaosx_famine_migration_on_actions.txt` calls the corridor state-control, sparse country, and nuclear helpers from existing hooks.
- `common/scripted_effects/famine_migration_corridor_effects.txt` adds the narrow callback and revalidation helpers listed below.
- `common/scripted_effects/famine_migration_corridor_effects.md` documents the callback contract, sparse bounds, cleanup behavior, and engine blockers.
- `docs/plans/famine_and_migration_system_plans/subagent_handoffs/corridor_hook_owner_patch.md` records this handoff.

No decisions, localisation, mapmodes, assets, workbook, specs, constants, or relief helper files were edited. No commit was created.

## Helper map

| Helper | Scope | Inputs | Outputs | Side effects | Call sites |
| --- | --- | --- | --- | --- | --- |
| `famine_migration_corridor_handle_state_control_change` | State | Exact callback state in `FROM.FROM`; persisted origin/front IDs in sparse mirrors | Invalidated terminal status and `control_change` reason when identity matches | Calls idempotent corridor cleanup; never sets attack receipt; loops only `global.famine_migration_active_displacement_countries` | `on_state_control_changed` |
| `famine_migration_corridor_revalidate_changed_state` | Country | `event_target:famine_migration_corridor_changed_state`, mirrored offer/active front and origin IDs | Exact front-to-origin invalidation | Calls control-change cleanup on each matching origin; no owned-state or country scan | Sparse loop inside the state-control helper |
| `famine_migration_corridor_revalidate_sparse_country` | Country | One callback-named registered country and its offer/active origin mirror | Route remains live or becomes `invalidated` with `route_closed` | Resolves at most one pending-offer row and one active row; delegates relation/front validation to the state helper | `on_war_relation_added`, `on_peace`, `on_peaceconference_ended` |
| `famine_migration_corridor_revalidate_route_relation` | State | Persisted front, counterpart, origin controller, and relation | Exact relation validity | Checks only the stored route and relation predicate; invalid routes call idempotent cleanup | Sparse country helper |
| `famine_migration_corridor_handle_nuke_drop` | State | `event_target:famine_migration_corridor_nuke_launcher`, exact nuked state, persisted origin identity | Attack receipt on exact origin or a sparse front match | Sets receipt proof and launcher country ID only before calling existing disqualification helper | `on_nuke_drop` |
| `famine_migration_corridor_submit_nuke_front_attack_receipt` | Country | Sparse registered country, persisted active or pending-offer front/origin IDs, launcher and nuked-state targets | Authoritative launcher receipt on the resolved origin | Calls existing disqualification/cleanup only when the persisted front is exact and valid | Sparse loop inside the nuke helper |
| `famine_migration_corridor_invalidate_for_control_change` | State | Caller-proven exact origin | `invalidated` status and `control_change` reason | Idempotent cleanup; does not touch population, cohorts, or attack evidence | State-control direct and front-resolution branches |

## Constants and tuning

No new constants were needed. Existing `famine_migration_corridor_status.invalidated`, `famine_migration_corridor_status.disqualified`, `famine_migration_corridor_reason.control_change`, `famine_migration_corridor_reason.route_closed`, and `famine_migration_corridor_runtime.one` are reused. The route relation ladder remains the existing `enemy_front`, `neutral_border`, `faction_partner`, and `neighbor` contract table.

## Event targets and cleanup

- `famine_migration_corridor_changed_state` persists the exact state-control callback state while the sparse active-country registry is traversed.
- `famine_migration_corridor_nuke_launcher` captures `ROOT` before `FROM` is entered, preserving the authoritative launcher identity.
- `famine_migration_corridor_nuked_state` captures the exact `FROM` state during front resolution.
- `famine_migration_corridor_relation_origin_controller` supplies the current origin controller to the relation-specific checks.

All four targets are regular event targets scoped to the originating effect chain. No global event target or target registry was added. Terminal branches call the existing `famine_migration_corridor_cleanup`, which clears active IDs, counterpart/requester mirrors, mission flags, and route bindings while preserving terminal status/reason and measured transaction/attack audit evidence. Repeated state-control, relation, or nuke callbacks therefore remain idempotent.

## Migration and scope proof

The existing generic famine state-control, country reassessment, and nuclear-pressure effects remain in place. The new calls are additive at the exact existing callback sites. The existing host-only `on_daily_CXT` sparse processor and `famine_migration_corridor_sparse_country_pulse` remain the maintenance owners; this patch did not add another periodic hook or alter their registry boundary.

The only explicit loop added by this patch iterates `global.famine_migration_active_displacement_countries`, which is the package's existing registered-country array. The control callback compares the changed state against persisted `front_state_id` and `origin_state_id`; the nuke callback uses the same sparse mirrors. No `every_state`, `every_country`, `any_owned_state`, or war-graph search was added to the hook path.

## Validation and evidence

- Read the prepared scripted-system prompt, complete famine specification folder, existing corridor architecture/attack-owner handoffs, sparse registry source, relief source, offline on-actions/data-structures/triggers/effects references, and vanilla effects/triggers documentation before editing.
- Confirmed the documented callback scopes used by the patch from `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md`: `FROM.FROM` is the changed state for `on_state_control_changed`; `ROOT` is the launcher and `FROM` is the nuked state for `on_nuke_drop`; `ROOT`/`FROM` are the named countries for `on_war_relation_added` and `on_peaceconference_ended`; `THIS` is the country that is no longer at war for `on_peace`, so the peace hook intentionally revalidates its ambient country only.
- Reviewed the changed helper blocks and call sites with `rg` and PowerShell source inspection; the added hook path contains only the sparse active-country registry loop and no recurring global callback.
- No live game launch was performed, as required by repository instructions.

No fresh in-scope HOI4 MCP route was available in this runtime, and this patch introduces no focus, event, GUI, technology, doctrine, or map surface requiring an MCP inspection. Existing corridor handoff artifact references remain historical evidence and are not claimed as fresh engine validation.

## Known blockers and limitations

- Vanilla does not expose a generic ordinary land-combat callback carrying exact corridor origin/front state and attacker identity in the reviewed source surface. No ordinary combat attack receipt was fabricated.
- Vanilla does not expose a strategic-bombing callback carrying the exact attacker for a corridor front. `days_since_last_strategic_bombing` remains insufficient and is not used as proof.
- The nuclear path is authoritative only when the origin or front identity is present in the sparse registered-country mirrors and the origin's persisted front remains valid. Missing/stale mirrors fail closed.
- Existing runtime concerns about save/reload resolution of `var:<database_id>` state/country scopes and counterpart ordinary-decision visibility remain documented blockers outside this hooks patch.
