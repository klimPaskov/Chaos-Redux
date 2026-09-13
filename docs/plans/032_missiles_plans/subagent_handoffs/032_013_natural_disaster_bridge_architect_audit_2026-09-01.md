# Event 032 / Event 013 Natural-Disaster Bridge Audit

Disposition: implemented and reconciled by the parent. The findings below are the pre-patch audit snapshot; the current source and `docs/plans/032_missiles_plans/032_missiles_test_results.md` supersede its recommended-patch section.

Audit date: 2026-09-01.

Audit mode: read-only architecture review.

Worktree note: the four gameplay targets are currently uncommitted or dirty in the shared worktree, so this handoff deliberately does not claim ownership of or alter those edits.

## Scope and outcome

The audited bridge is `missiles_natural_disaster_damage_site` in `common/scripted_effects/032_missiles_operations_effects.txt:2825-3021`, called by four state-scoped Event 013 impact paths.

The normal queued Event 013 path supplies the correct state/current-controller relationship for the bridge, and operation abort/cleanup is ordered before natural-disaster mutation.

The bridge is not safe as an unconstrained generic state helper because its country-side helpers rely on `ROOT` being the current controller's program country.

The audit found two concrete custody/receipt defects, one capacity-recovery gap, and two lifecycle/scope risks that should be resolved before treating the bridge as complete.

No gameplay file was edited.

## Reviewed source and reference evidence

| Surface | Current references | Audit use |
| --- | --- | --- |
| Natural-disaster bridge | `common/scripted_effects/032_missiles_operations_effects.txt:2825-3021` | Severity mapping, site damage, capacity loss, reserve debit, destruction, incident state, cleanup. |
| Canonical scuttle | `common/scripted_effects/032_missiles_operations_effects.txt:1184-1231` | ROOT-owned scuttle receipt and custody cleanup precedent. |
| Current-controller scuttle adapter | `common/scripted_effects/032_missiles_operations_effects.txt:1233-1292` | Existing state-to-controller scuttle helper for callers whose `ROOT` is not the site owner. |
| Operation damage precedent | `common/scripted_effects/032_missiles_operations_effects.txt:2772-2795` | Already calls `missiles_scuttle_site_from_current_controller` at `:2787-2790`. |
| Reserve helpers | `common/scripted_effects/032_missiles_effects.txt:472-568` and `common/scripted_effects/032_missiles_operations_effects.txt:731-740` | Accepted/rejected reserve transaction contracts. |
| Custody rebalance | `common/scripted_effects/032_missiles_operations_effects.txt:657-682` | Site reserve is an allocation view rebuilt from the controller operational reserve. |
| Operation cleanup | `common/scripted_effects/032_missiles_operations_effects.txt:3722-3803` | Abort/refund and committed-operation cleanup behavior. |
| Capacity recovery | `common/scripted_effects/032_missiles_effects.txt:790-868` and `common/scripted_triggers/032_missiles_triggers.txt:196-214` | Existing repair/reinforcement path and its strategic-level gate. |
| Event 013 call sites | `common/scripted_effects/013_natural_disasters_effects.txt:8581-8761`, `:9109-9168`, `:9227-9317`, and `:9402-9507` | State scope and severity temporary-variable setup for all four bridge calls. |
| Event 013 queue worker | `common/scripted_effects/013_natural_disasters_effects.txt:1854-1944` and `:2083-2202`; `events/013_natural_disasters.txt:68-75` | Country-worker root, state target handoff, and delayed impact execution. |
| Event 013 validity | `common/scripted_triggers/013_natural_disasters_triggers.txt:390-407` | Owner and scheduled-state checks, including the missing controller guard. |
| Missile constants | `common/script_constants/032_missiles_constants.txt:196-228` and `:634-676` | Destruction threshold, capacity bands, disaster severity ladder, and loss tuning. |

The required offline Paradox wiki pages were consulted, including Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.

The relevant vanilla documentation was consulted at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, and `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/script_constants/documentation.md`.

## Findings

### F-01 — High: captured-site reserve receipt is orphaned on natural-disaster scuttle

`missiles_state_has_registered_site` accepts captured and compromised sites at `common/scripted_triggers/032_missiles_triggers.txt:528-540`.

When the bridge reaches the destruction threshold, `common/scripted_effects/032_missiles_operations_effects.txt:2940-2952` clears the captured flag and site reserve/identity variables but never clears `missiles_site_captured_reserve` or decrements the current controller's `missiles_captured_reserve_held` ledger.

Captured-site transfer code stores the captured receipt in `missiles_site_captured_reserve` and credits the controller held ledger while setting ordinary `missiles_site_reserve` to zero at `common/scripted_effects/032_missiles_operations_effects.txt:3994-4065`.

Therefore a captured site can enter the bridge with an ordinary site reserve of zero, take no ordinary reserve debit, become scuttled, and still leave a positive held captured-reserve ledger with no recoverable state.

The existing `missiles_scuttle_site_from_current_controller` helper explicitly clears the held ledger and captured state receipt at `common/scripted_effects/032_missiles_operations_effects.txt:1237-1256` and then clears the site receipt at `:1280-1292`.

Recommended action: use the current-controller scuttle path for bridge destruction, or extract its captured-ledger cleanup into a shared destruction helper, while preserving one and only one ordinary-reserve debit.

### F-02 — High: the bridge can erase a site receipt without recording or rejecting an unpaid reserve loss

The bridge computes a percentage loss from the site reserve at `common/scripted_effects/032_missiles_operations_effects.txt:2884-2894`, subtracts that amount from the site allocation at `:2934-2937`, and adds the remaining site allocation to the destruction loss at `:2940-2942`.

The country debit at `common/scripted_effects/032_missiles_operations_effects.txt:2954-2960` only subtracts when `missiles_operational_reserve` is greater than or equal to the full loss, with no rejected result, shortfall receipt, or applied-amount output when that condition fails.

The adapter then reports `missiles_disaster_adapter_result = completed` at `:3017` and performs final recalculation at `:3010-3013` regardless of whether the country debit occurred.

Under the intended invariant that site allocations are backed by the same controller operational reserve, the normal path debits the expected amount once and rebalance reconstructs the remaining allocation view.

The helper itself does not prove that invariant, so stale ownership, a short operational reserve, a missing initialized program, or a wrong current controller can produce destruction of the state receipt without an equal controller debit.

The existing accepted/rejected transaction helpers are `missiles_remove_reserve` at `common/scripted_effects/032_missiles_effects.txt:494-509` and `missiles_destroy_reserve` at `common/scripted_effects/032_missiles_operations_effects.txt:731-740`, but the natural-disaster bridge bypasses both.

Important ordering warning: replacing the bridge destruction block with `missiles_scuttle_site_from_current_controller` without changing the later ledger block will double-debit the remaining site allocation, because the current-controller helper already debits `missiles_site_reserve` at `common/scripted_effects/032_missiles_operations_effects.txt:1258-1265` and the bridge currently adds that remainder into `missiles_disaster_reserve_loss` before the later country debit.

Recommended action: separate the percentage loss from the remaining destruction loss, settle the percentage through an accepted/rejected country reserve receipt, let the current-controller scuttle helper settle the remaining ordinary allocation and captured held receipt, and do not debit the augmented total a second time.

The current-controller helper repeats the same insufficient-reserve conditional at `:1260-1264`, so it fixes custody cleanup but does not by itself complete the fail-closed receipt contract.

### F-03 — Medium: strategic sites can retain permanent capacity loss

The bridge records actual capacity removed in `missiles_site_capacity_loss` at `common/scripted_effects/032_missiles_operations_effects.txt:2922-2932`, capping the take to current capacity and clamping the result to the configured bounds.

The only decrement of that loss is in `missiles_reinforce_one_site` at `common/scripted_effects/032_missiles_effects.txt:827-835`.

The only caller found for that recovery helper is `missiles_reinforce_network_from_firing` at `common/scripted_effects/032_missiles_effects.txt:840-868`, whose site selection requires `missiles_site_can_upgrade = yes` at `:845-851`.

`missiles_site_can_upgrade` rejects a site at strategic level through the level-less-than-strategic condition at `common/scripted_triggers/032_missiles_triggers.txt:210-213`.

The repair mission path restores damage and status through `missiles_restore_readiness` and `missiles_repair_site` at `common/scripted_effects/032_missiles_operations_effects.txt:755-766` and `:872-895`, but does not reduce `missiles_site_capacity_loss`.

The constants permit strategic capacity of 10 and disaster capacity losses up to 4 at `common/script_constants/032_missiles_constants.txt:218-228` and `:645-649`.

Result: a strategic-level site hit by a severe-or-higher disaster can lose capacity permanently even after its damage is repaired.

Recommended action: add a small `missiles_recover_site_capacity_loss` state helper with a constant recovery step, and call it from repair completion or allow the firing recovery selector to admit a non-scuttled site with positive capacity loss even when its level is strategic.

### F-04 — Medium: normal Event 013 scope is correct, but the bridge has an implicit ROOT contract

Event 013 queues state targets from the state's controller country at `common/scripted_effects/013_natural_disasters_effects.txt:1890-1943` and fires hidden country event `chaosx.nr13.2` at `events/013_natural_disasters.txt:68-75`.

The worker saves the queued state into `natural_disaster_impact_state` at `common/scripted_effects/013_natural_disasters_effects.txt:2138-2140` and invokes the impact or chain follow-up while the country worker remains the root at `:2175-2189`.

The ordinary impact then enters that saved state at `common/scripted_effects/013_natural_disasters_effects.txt:9430-9452`, so inside `missiles_natural_disaster_damage_site` the current scope is the state, `PREV` inside `event_target:missiles_disaster_controller` is the state, and `ROOT` is the controller country on the normal queued path.

That makes the operation identity check and `missiles_abort_operation` plus `missiles_cleanup_operation` calls at `common/scripted_effects/032_missiles_operations_effects.txt:2896-2912` structurally valid for the four current Event 013 call sites.

The same root relationship makes the country-side recalculation, rebalance, and status refresh at `:2954-3013` operate on the intended program country.

The helper does not validate that contract, so a direct caller with a different country root or a state-rooted invocation can make `ROOT`-based operation cleanup and custody helpers inspect or mutate the wrong program.

Recommended action: document the adapter as state scope with `ROOT = current controller country`, validate controller existence and controller identity before mutation, and use the existing current-controller scuttle adapter for destruction callers whose root is not the site owner.

### F-05 — Medium: missing controller or uninitialized-program paths can leave stale registry state

The Event 013 scheduled-state trigger checks `OWNER = { exists = yes }` but has no controller existence check at `common/scripted_triggers/013_natural_disasters_triggers.txt:390-407`.

The bridge saves `missiles_disaster_controller` only through `controller = { save_event_target_as = ... }` at `common/scripted_effects/032_missiles_operations_effects.txt:2896-2900`.

The destruction branch removes the state from `missiles_launch_site_states` only inside the controller target and initialized-program branch at `:2954-2973`.

If the controller target is unavailable or lacks `missiles_program_initialized`, the state can be marked scuttled and its IDs cleared without registry removal, country recalculation, held captured-reserve cleanup, or a rejected adapter result.

This is likely an edge path because ordinary owned states have a controller, but the source contract does not close it and the validity trigger does not prove it.

Recommended action: fail closed before site mutation when no controller exists, or provide a state-local cleanup path that is explicitly safe without a country root.

### F-06 — Low/Medium: regular receipt variable is reset but not cleared, and severity defaults fail soft

The bridge resets the regular state variable `missiles_disaster_reserve_loss` at `common/scripted_effects/032_missiles_operations_effects.txt:2884`, consumes it through `PREV` during the controller ledger block, and never clears it at the end where `missiles_site_damage_request` and `missiles_disaster_site_operation_id` are cleared at `:3017-3019`.

The current search found no other consumer of `missiles_disaster_reserve_loss`, so this is not an observed cross-system leak, but retaining a state-scoped receipt after the chain increases future-caller risk and obscures whether a receipt was settled.

All four current callers seed `natural_disaster_current_severity` immediately before the bridge at `common/scripted_effects/013_natural_disasters_effects.txt:8685`, `:9159`, `:9293`, and `:9452`, while the bridge silently falls back to local severity defaults at `common/scripted_effects/032_missiles_operations_effects.txt:2837-2843` when the input is absent or unrecognized.

Recommended action: clear the regular receipt after settlement and either make missing/unsupported severity reject the adapter or document the local default as an intentional fail-soft contract.

## Operation cleanup and event-target lifetime

The operation path is correct on the normal queued Event 013 route.

The bridge snapshots the site's operation ID and saves a regular event target for the current controller at `common/scripted_effects/032_missiles_operations_effects.txt:2896-2900`.

It aborts and cleans up a matching active operation before applying natural-disaster site damage at `:2901-2912`.

`missiles_abort_operation` refunds an active uncommitted operation through `missiles_refund_operation_reserve` at `common/scripted_effects/032_missiles_operations_effects.txt:3722-3731` and `common/scripted_effects/032_missiles_effects.txt:556-568`.

Committed operations do not refund after commitment, and `missiles_cleanup_operation` clears site operation IDs and allocations, operation arrays, operation flags, and the reserved reserve receipt at `common/scripted_effects/032_missiles_operations_effects.txt:3733-3803`.

The bridge uses `save_event_target_as`, not a global event target, at `:2897`, and no delayed event depends on `missiles_disaster_controller` after the effect chain, so manual global-target cleanup is not required.

The existing `missiles_site_scuttle_controller` target in `missiles_scuttle_site_from_current_controller` is also a regular target at `common/scripted_effects/032_missiles_operations_effects.txt:1237-1241` and has the same safe short lifetime for its current callers.

The remaining lifetime risk is not target persistence but scope misuse if the adapter is invoked outside the country-worker root contract.

## Exact helper-use assessment

The bridge correctly uses `missiles_state_has_registered_site`, `missiles_refresh_site_flags`, `missiles_abort_operation`, `missiles_cleanup_operation`, `missiles_clamp_program_values`, `missiles_recalculate_network`, `missiles_rebalance_site_custody`, and `missiles_refresh_program_status_idea`.

The bridge should reuse `missiles_scuttle_site_from_current_controller` at `common/scripted_effects/032_missiles_operations_effects.txt:1233-1292` for destruction cleanup because it is the existing state-to-current-controller precedent and is already used by `missiles_apply_operation_site_damage` at `:2787-2790`.

`missiles_scuttle_site` at `:1184-1231` is appropriate when `ROOT` is the custody owner, but it is not the safe choice for a state impact whose root may be the attacking country.

`missiles_cleanup_site` at `:1294-1304` clears site variables and removes the state from the ROOT registry, but it does not settle the captured held ledger and therefore is not a complete replacement for captured-site destruction.

`missiles_remove_reserve` and `missiles_destroy_reserve` provide the existing accepted/rejected debit contract, but their country-scope inputs must be staged in the current controller target and must not be combined with a second scuttle debit.

`missiles_repair_site` and `missiles_restore_readiness` are the existing recovery path, but neither currently repairs capacity loss.

Scope clarification: no `remove_building` effect appears in the audited bridge or scuttle paths, so "site destruction" currently means logical custody/registry retirement rather than removal of the vanilla `rocket_site` building.

If physical building removal is intended, that is an unconfirmed design requirement and needs an explicit state-scope decision before adding it; this audit does not silently introduce that behavior.

## Proposed helper map

| Helper | Scope | Inputs | Outputs | Side effects | Call sites |
| --- | --- | --- | --- | --- | --- |
| `missiles_natural_disaster_damage_site` | STATE | `natural_disaster_current_severity`; registered site; current controller | Adapter result plus settled damage, capacity, reserve, readiness, control, guidance, and warning changes | Existing state and controller ledger mutations; should fail closed on invalid ownership/receipt | Four existing Event 013 calls at `013_natural_disasters_effects.txt:8761`, `:9168`, `:9317`, and `:9507`. |
| `missiles_scuttle_site_from_current_controller` | STATE with current-controller target | Current state and its `controller` scope | No explicit result today; destroys state custody | Clears ordinary and captured site receipts, decrements held captured ledger, removes registry entry, clears flags/IDs, recalculates controller | Reuse from natural-disaster destruction; retain operation impact use at `032_missiles_operations_effects.txt:2787-2790`. |
| `missiles_remove_reserve` or a narrow receipt wrapper | COUNTRY | Positive `missiles_reserve_delta` staged in current controller | Existing accepted/rejected payment result | One controller operational-reserve debit and clamp | Natural-disaster percentage-loss settlement inside `missiles_disaster_controller`. |
| `missiles_recover_site_capacity_loss` | STATE | Positive `missiles_site_capacity_loss`; non-scuttled site | One applied recovery unit or rejected/no-op result | Decrements loss, increases capacity, clamps to minimum/strategic bounds, refreshes flags | Repair completion and/or firing recovery path. |
| `missiles_clear_natural_disaster_receipt` | STATE | Temporary/regular receipt variables after settlement | Cleared receipt state | Clears `missiles_disaster_reserve_loss`, request, operation snapshot, and any future-added receipt variables | End of bridge and rejected early-exit paths. |

The first three entries can be implemented by reusing existing helpers if the parent preserves the debit ordering described in F-02.

The capacity helper is the only new gameplay helper materially justified by this audit, and it requires matching documentation if implemented.

## Constants and tuning-table plan

| Constant group | Current values/reference | Use or proposed treatment |
| --- | --- | --- |
| `missiles_reserve.site_destroyed_threshold` | 90 at `032_missiles_constants.txt:200-203` | Keep as the single scuttle threshold. |
| `missiles_site_capacity` | Initial 4, reinforced 6, expanded 8, strategic 10, minimum 0 at `:218-228` | Keep as the capacity clamp range and use the strategic value for recovery bounds. |
| `missiles_natural_disaster.site_damage_*` | 10, 24, 40, 60, 80 at `:640-644` | Keep the existing severity ladder. |
| `missiles_natural_disaster.capacity_loss_*` | 0, 1, 2, 3, 4 at `:645-649` | Keep the existing loss ladder and settle only actual capacity removed. |
| `missiles_natural_disaster.reserve_loss_*` | 15, 25, 40, 60, 80 percent at `:650-654` | Keep as the percentage component and do not merge it with a second scuttle debit without an explicit receipt split. |
| Readiness/control/backlog/warning loss bands | `:655-675` | No tuning change is implied by this audit; continue clamping through the existing program clamp helper. |
| `missiles_reserve.site_repair_step` | 20 at `032_missiles_constants.txt:187-203` | Keep damage repair tuning separate from capacity recovery. |
| Capacity recovery step | No dedicated constant currently exists; the firing helper uses `missiles_event.one` at `032_missiles_effects.txt:832-834` | If repair recovery is added, introduce one package-owned constant such as `missiles_natural_disaster.capacity_loss_recovery_step = 1` or deliberately reuse the existing one-unit event constant and document that choice. |

No constants were changed by this audit.

## Event-target and cleanup plan

Use a regular `missiles_disaster_controller` target for the duration of the current state impact chain, as the bridge already does at `common/scripted_effects/032_missiles_operations_effects.txt:2896-2900`.

Do not convert this target to a global target because no delayed consumer requires persistence beyond the current chain.

Before mutation, require a live controller, an initialized program when country ledgers are expected, and a controller identity compatible with `missiles_site_controller_id` when that variable exists.

Settle or reject the percentage receipt before clearing the site allocation, then let the current-controller scuttle helper settle the remaining ordinary allocation and captured held receipt exactly once on destruction.

Keep operation abort/refund and cleanup before site destruction, as the current bridge does at `:2901-2912`.

Clear the regular disaster receipt variables after the country ledger has consumed them, including the currently uncleared `missiles_disaster_reserve_loss`.

Remove destroyed states from `missiles_launch_site_states` even when the controller is not program-initialized, or fail closed before marking the state scuttled if a safe owner scope is unavailable.

Clear or clamp any stale capacity-loss value on permanent scuttle according to the selected custody model, because a scuttled state must not be recoverable through later reinforcement.

## Migration plan

1. Preserve the four Event 013 call sites and their state scope; do not move disaster history, deaths, reports, or aftermath into Event 032.

2. Add explicit bridge preconditions for current controller existence and program ownership, then retain the current operation-ID match using `PREV` for the state and `ROOT` for the queued controller country.

3. Split the natural-disaster percentage receipt from the remaining site allocation receipt before adopting `missiles_scuttle_site_from_current_controller`.

4. Route the percentage component through the existing accepted/rejected reserve helper and make the adapter result reflect rejection or a documented shortfall policy.

5. Replace the duplicated destruction flag/ID/custody block with the current-controller scuttle helper after the receipt ordering is corrected, while avoiding a second debit of the same remaining site reserve.

6. Add capacity-loss recovery to repair completion or broaden only the narrow firing recovery selector, with a constant-backed one-unit recovery step and a clamp test at strategic capacity.

7. Clear the regular disaster receipt variables and update the matching helper documentation if a new helper or contract is introduced.

8. Re-run the four Event 013 call-site checks and the Event 032 operation-impact precedent check after the parent applies the patch.

## Validation and unsupported analysis

The four bridge call sites were cross-referenced with their immediate severity setup and queue/worker scope path.

The reserve, captured-custody, operation cleanup, scuttle, rebalance, and capacity-recovery call graphs were traced from source and the required offline/vanilla references.

Read-only `hoi4.event_inspect` queries for `chaosx.nr13.1`, `chaosx.nr13.2`, and `chaosx.nr32.1` returned `EVENT_INSPECTED_PARTIAL` in workspace `mod_chaos_redux_ea3b2d67c2c0`; helper/lifecycle passes were deferred and the inline file inventory was truncated.

The Event 013 worker lint artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0b6b948114085b4793c5d3b2f070b93aabdc9128eb0e0c69f001b27aa0bc3f27/2ed9de711412dff47405dc376745d401db8368d5fd290405cb5018692249f136/event-lint-afac304472e1.json`.

Read-only `hoi4.event_render` queries returned `EVENT_RENDERED_PARTIAL`; the Event 013 bounded render selected two nodes, while the exact Event 032 selector selected zero nodes in the bounded viewer.

The delayed Event 013 worker scope render also returned `EVENT_RENDERED_PARTIAL` with zero selected nodes in the bounded viewer; its manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b235aceba8f38977f97a1bba1cd1ba1e82636910d10e0383bba3b5fca092a618/bb27c51732a7f70ba92328ca87c736ef4733a5abbe45dabaeb2723142200d947/event-scope-afac304472e1-manifest.json` and its JSON is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7256e4b22a25a9b84e94e57c459b8e8dea21b162219d2a60e38663da3cdf9094/c8631c44672e400d3d7105d985ae772d8c9fda49c6d23ddd4086250de834813b/event-scope-afac304472e1.json`.

The exact Event 013 state-flow inspection returned `INTERNAL_ERROR` and produced no artifact.

Event 013 render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0b5c9169d1e53e0759750304b86ba50dfaa3ecde751ab2ccb32c5709bb878c89/3ef33dc1067d97ba04cbccb43a04cf843c06775086029013a80f80345f8074e4/event-scope-a1603c71494f-manifest.json`.

Event 013 render JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/42053a10e745840409b39e1e187588532f35b280ae3cdaadfe6989a51869d1d5/1868c3af7248c91978270a58cf2112fb19c497a84fd3511b162e2eb9ec438ce0/event-scope-a1603c71494f.json`.

Event 032 render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2f2df6ec026cd9176656d3add52a4ee1b6fb36a157d993a6876fdf5f90a9ea98/af13bf90412b79917a78a6a3c049959d60a09c1f960b388fcad31a8df8be18f0/event-scope-a1603c71494f-manifest.json`.

Event 032 render JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7e9f215aca8abcfe0f573776cb6c2d85894c6679b64290e496e6d0bec8f971b7/4de22240564994337b21e02a63b9484ce5297b7809701cc1fe02b26338965f93/event-scope-a1603c71494f.json`.

The bridge itself contains deterministic severity selection and no weighted or probability-bearing block, so `hoi4.probability_inspect` and `chaosx_ai_probability_auditor` were not invoked and this handoff makes no probability or balance claim about the upstream Event 013 random selection.

No GUI or map surface is in scope, so no GUI/map inspection was substituted or omitted.

No game launch or live consumer validation was performed, consistent with repository instructions.

## Recommended patch and blockers

Parent resolution: hardened the reserve receipt contract, reused the current-controller scuttle helper with corrected debit ordering, cleared captured-held custody on natural-disaster destruction, added constant-backed capacity-loss recovery for repairs, made the current-controller/program gate explicit, retired scuttled capacity, and cleared bridge receipts on accepted and rejected exits.

No gameplay patch was applied by this subagent; the parent applied the resolution in the current Event 032 operation files.

The historical evidence blockers remain the partial Event MCP helper/lifecycle passes, the Event 013 state-flow `INTERNAL_ERROR`, and the earlier bounded Event 032 render resolving no selected node. The current parent rerun returned a bounded Event 032 artifact; the current limitation is still the service's deferred workspace-wide helper/lifecycle analysis.

The line references above describe the shared worktree snapshot at audit time and may shift if another agent edits the uncommitted gameplay files.
