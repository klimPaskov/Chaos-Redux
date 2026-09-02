# Event 016 final project-stage receipt review

Review date: 2026-09-02.

Review mode: read-only architecture review; no gameplay source, balance, model, GUI, event, or probability files were changed.

Owner boundary: this handoff is the only file owned by this review; the parent owns implementation and commit.

## Scope and contract basis

The bounded review covers `common/scripted_effects/016_brilliant_scientist_project_effects.txt` helpers `brilliant_scientist_begin_project_stage`, `brilliant_scientist_cancel_project_stage`, `brilliant_scientist_finish_project_stage`, `brilliant_scientist_complete_native_prototype_stage`, their 45 timed stage-decision callers and 15 native-prototype integration callers in `common/decisions/016_brilliant_scientist_directorate_project_board.txt`, the four native synchronization branches in the same project-effects file, `common/on_actions/016_brilliant_scientist_project_on_actions.txt`, and the stage advance and project input triggers in `common/scripted_effects/016_brilliant_scientist_effects.txt` and `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt`.

The required completion contract is explicit: every timed wrapper, including native-prototype integration, owns an exact family-and-stage receipt; finish and cancellation callbacks may clear or refund only a matching receipt; a native Prototype transition charges Capacity only on a genuine Theory-to-Prototype advance; native completion during an integration timer yields one reward and one Capacity charge; and invalid host, facility, terminal, or world-end state cannot produce a delayed stage reward (`docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md:124-131`).

The review does not redesign the 45 cost profiles, durations, priorities, native project payments, family rewards, probabilities, or the shared inheritance/advance semantics.

## Verdict

The ordinary live selection gates are mostly correct, but final closure is not receipt-safe until the owner adds identity checks to every delayed finalizer and makes native Prototype charging conditional on a successful stage change.

The highest-risk ordinary path is Rocketry or Biological Weapons integration after one of its qualifying native projects is complete, followed by completion of the second qualifying native project while the integration timer is active. The `on_project_completion` synchronization bridge advances the family to Prototype, invalidates the integration decision's visible Theory state, and should cancel the remaining timer; the current shared flag has no family/stage identity and the integration remove callback can still call the native helper if a stale callback survives that cancellation boundary.

The minimum safe owner patch is:

1. Persist a fixed callback identity for every timed stage and integration decision, and make cancellation, finish, and terminal cleanup compare that identity to the active receipt before touching any flag, variable, Capacity value, ledger entry, reward, or output.
2. Move all `brilliant_scientist_finish_project_stage` cleanup inside its matching-receipt branch, and use the canonical ledger-to-gross Capacity rebuild after a matching receipt is settled rather than blindly clearing a reservation.
3. Make `brilliant_scientist_complete_native_prototype_stage` validate the family, current host, primary facility, no world-end state, exact current Theory stage, and enough Capacity before advancing, then rebuild Capacity only after `stage_changed = one`; a changed=false or invalid call must do nothing.
4. Give all 15 integration decisions a normal family/Prototype receipt, clear only a matching integration receipt on cancel, and let remove resolve the native helper only while that receipt still matches and the ledger is still exactly Theory.
5. Add the world-end guard to active decision visibility/cancellation and close any active stage/integration receipt from the existing Event 016 terminal cleanup before facility targets are cleared.

Do not add `NOT = { has_country_flag = brilliant_scientist_project_stage_in_progress }` to the native synchronization helper. That would suppress the contract-required native completion during an active integration timer; the lock must remain while the integration receipt is cancelled after the native sync wins.

## Source helper map

| Helper | Scope and inputs | Current writes and side effects | Current callers and ownership note |
| --- | --- | --- | --- |
| `brilliant_scientist_begin_project_stage` (`project_effects:9-46`) | COUNTRY; temporary `brilliant_scientist_project_family` and `brilliant_scientist_requested_project_stage`; cost loader must mark the request ready | Sets the shared in-progress flag, stores active family/stage and active Capacity delta, subtracts the reservation, clamps Capacity, and spends the loaded equipment, fuel, manpower, experience, and other costs | The 45 Theory/Deployment/Weaponization `complete_effect` blocks in `016_brilliant_scientist_directorate_project_board.txt`; the caller availability triggers normally gate host, facility, exact predecessor, incident, cost, and Capacity, but the helper itself is not fail-closed |
| `brilliant_scientist_cancel_project_stage` (`project_effects:48-58`) | COUNTRY; currently no callback family/stage input | Refunds whichever active Capacity delta happens to exist, then unconditionally clears the shared flag and all active receipt variables | All 45 wrapper `cancel_effect` blocks call it without inputs; this is the direct stale-callback hazard |
| `brilliant_scientist_finish_project_stage` (`project_effects:60-86`) | COUNTRY; temporary callback family/stage | Its reward/advance branch matches the active shared flag and active family/stage, advances and applies outputs only when changed, but lines 82-85 clear the shared flag and active receipt unconditionally outside that match | All 45 wrapper `remove_effect` blocks set fixed temporary family/stage and call it; reward guarding is present, cleanup guarding is not |
| `brilliant_scientist_complete_native_prototype_stage` (`project_effects:88-106`) | COUNTRY; temporary family; requested stage is set internally to Prototype | Currently subtracts and clamps `capacity_prototype` before calling the generic advance helper, then applies outputs only if `stage_changed = one` | 15 integration `remove_effect` blocks, four synchronization branches (`project_effects:1112-1150`), ten new native family project output bridges through `record_new_project_prototype` (`project_effects:1153-1169`), and the six-component Singularity registration bridge (`project_effects:1183-1192`) |
| `brilliant_scientist_advance_project_to_requested_stage` (`016_brilliant_scientist_effects.txt:1119-1144`) | COUNTRY; temporary family/stage and loaded index | Initializes `project_stage_changed` to zero, validates family/stage inputs, and writes any upward stage jump below the requested stage | Shared by normal finalizers, native completion, and inheritance-related code; its upward semantics are broader than this receipt correction and must not be tightened globally |
| `brilliant_scientist_refresh_project_capacity_from_gross` (`016_brilliant_scientist_effects.txt:1032-1074`) | COUNTRY; reads the canonical gross ceiling, 15 stage entries, suspension state, and any still-live active reservation | Rebuilds available Capacity from gross minus cumulative burden and clamps it; while the active flag and active delta exist it includes that reservation | Existing transfer/reinitialization reconciliation already uses it; if a receipt finalizer uses it, clear the matching receipt first and call it after all family-dependent output work because its 15-family loop overwrites temporary `brilliant_scientist_project_family` |

The 45 normal wrapper callers are the 15 families `computation`, `electronics`, `materials`, `rocketry`, `high_energy`, `biomedical`, `teleportation`, `cloning`, `robotics`, `paleogenetics`, `xenobiological_synthesis`, `biological_weapons`, `alien_arms`, `temporal`, and `singularity`, each at Theory, Deployment, and Weaponization. They occupy the decision-file ranges beginning at lines 836, 995, 1154, 1313, 1472, 1631, 1790, 1949, 2108, 2267, 2420, 2573, 2726, 2879, and 3032 respectively, with repeated `complete_effect`, `cancel_effect`, and `remove_effect` blocks.

The 15 integration decisions are `brilliant_scientist_integrate_computation_prototype`, `integrate_materials_prototype`, `integrate_biomedical_prototype`, `integrate_teleportation_prototype`, `integrate_cloning_prototype`, `integrate_robotics_prototype`, `integrate_paleogenetics_prototype`, `integrate_xenobiological_synthesis_prototype`, `integrate_alien_arms_prototype`, `integrate_temporal_prototype`, `integrate_singularity_prototype`, `integrate_electronics_prototype`, `integrate_rocketry_prototype`, `integrate_high_energy_prototype`, and `integrate_biological_weapons_prototype`.

## Concrete failure paths

### Ordinary stage timer and stale cancel/finish callbacks

At selection, a normal wrapper calls `begin_project_stage`, which stores active family/stage and the incremental Capacity reservation before spending the ordinary stage resources.

If that timer is cancelled normally, the current inputless `cancel_project_stage` refunds the current active delta and clears the current receipt, so a clean single-timer path is arithmetically correct.

The source does not make the callback identity durable at the decision boundary. A stale callback can therefore arrive after a newer wrapper has replaced the shared active receipt.

The concrete stale-cancel path is: timer A for family X/stage Y starts; A becomes invalid or its callback is delayed; timer B for family Z/stage W starts and overwrites `active_project_family`, `active_project_stage`, and `active_project_capacity_delta`; A's `cancel_effect` calls the inputless cancel helper; the helper refunds B's delta, clears B's receipt, and clears the shared lock; B later has no matching receipt and cannot settle its stage, while B's reservation has been returned prematurely.

The concrete stale-finish path is: timer A starts; B later owns the shared receipt; A's delayed `remove_effect` sets A's fixed temporary family/stage; the reward guard correctly fails because the active receipt is B, but lines 82-85 still clear B's flag and active variables; B's eventual finalizer then sees no receipt, cannot reward, and loses the active reservation unless another reconciliation repairs it.

A stale finish arriving after A was already settled can also clear an unrelated B lock because the unconditional cleanup is independent of whether A matched.

The existing source gates prevent normal simultaneous selection: `brilliant_scientist_project_board_is_ready` requires current host, valid primary facility, no shared stage flag, and no active incident (`016_brilliant_scientist_project_triggers.txt:55-60`), and each `can_begin_*` trigger adds the exact predecessor, cost, native prerequisite, and Capacity checks. They do not prevent delayed, duplicated, transferred, reinitialized, or otherwise stale callbacks from crossing a newer receipt.

### Final stage changed=false

The generic stage advance helper deliberately initializes `brilliant_scientist_project_stage_changed` to zero and only sets it to one when the array entry is strictly below the requested stage.

If a matching normal finish callback observes that another authoritative path already reached the requested stage, the current finish helper applies no output, which is correct, but then clears the active Capacity delta without returning it and without rebuilding from the now-current ledger.

The minimum safe behavior is to settle the matching receipt exactly once, apply no reward when changed=false, and rebuild available Capacity from the canonical gross ceiling after clearing the receipt. A local delta add-back is equivalent only in a clean arithmetic state; the canonical rebuild also corrects any pre-existing divergence between available Capacity and the canonical gross ledger without changing the Capacity scaling design.

Do not call the rebuild before family-dependent output, accident, force, recognition, or threat work has consumed the temporary family/stage inputs. The rebuild loop overwrites the temporary family while iterating the 15 entries; either run it last or restore the callback inputs before any subsequent family-dependent call.

### Native Prototype changed=false and duplicate charge

`brilliant_scientist_complete_native_prototype_stage` subtracts `capacity_prototype` at lines 90-91 before setting the requested stage or asking the advance helper whether the family genuinely changed.

If the current ledger is already Prototype or higher, the advance helper returns changed=false but the Capacity debit has already happened. A second integration remove callback, a stale callback after native synchronization, or a repeated completion notification therefore consumes another Prototype reservation without another ledger transition or output.

If the temporary family is invalid, the same pre-advance subtraction still occurs before the family input guard in the shared advance helper can fail closed. The named source callers normally provide valid family constants, but the helper should not rely on that for delayed safety.

The generic advance helper can make any upward jump below the requested stage, including a malformed none-to-Prototype call. The owner should add an exact current Theory guard in the native Prototype wrapper itself, not change the generic helper, because inheritance and other existing consumers rely on its broader upward semantics.

### Ordinary sync-mid-integration path

The 15 integration decisions set only the shared `brilliant_scientist_project_stage_in_progress` flag in `complete_effect`, clear that flag unconditionally in `cancel_effect`, and set a family temporary only in `remove_effect` before calling the native helper (`016_brilliant_scientist_directorate_project_board.txt:488-827` and `3185-3307`). No integration family/stage receipt is persisted.

Rocketry exposes the ordinary race because its integration is visible when either `sp_rockets_flying_bomb` or `sp_air_jet_engine` is complete (`decision board:3216-3245`). Biological Weapons has the same shape with Anthrax, Tularemia, or Plague (`decision board:3278-3307`).

The ordinary Rocketry sequence is: the ledger is Theory; one qualifying native project completes; the integration decision is selected and its shared timer lock starts; before the timer ends, the second qualifying native project completes; `on_project_completion` calls `brilliant_scientist_sync_native_project_prototypes`; the Rocketry branch sees Theory plus enough Capacity and advances Rocketry to Prototype; the integration's Theory visibility becomes false; `cancel_if_not_visible = yes` should cancel the remaining timer and run its cancel effect; the native sync owns the single Prototype output and Capacity charge.

Biological Weapons follows the same path when a second one of the three OR-qualified native projects completes during the timer.

Electronics and High Energy each name one native project in their visibility and sync branch, so a same-family completion after selection is less ordinary because the required project is already complete. They still need the same identity and changed=false protections for repeated, stale, reloaded, or reordered callbacks.

The source ordering of the on-action callback, decision visibility cancellation, and a possible stale remove callback is not established by the available offline documentation or the bounded MCP artifact. The safe design therefore makes either order converge: if sync wins, the later integration remove sees a non-Theory ledger and does nothing; if integration remove wins, the later sync sees a non-Theory ledger and does nothing.

Do not suppress native synchronization merely because the shared integration lock is present. Synchronization must remain authoritative during an active integration timer, while the integration receipt prevents its remaining timer from awarding a second result.

### Invalid host, facility, and world-end state

Normal wrapper decisions have current-host checks in `visible`, explicit current-host/primary-facility cancellation triggers, and `cancel_if_not_visible = yes`. The primary facility trigger validates the event target, state existence, control, core ownership, primary marker, and current-host ownership (`common/scripted_triggers/016_brilliant_scientist_triggers.txt:314-350`). These callers normally prevent a live invalid host/facility completion.

The delayed finalizers themselves do not check current host, primary facility, or world-end state. A final callback can therefore run after host loss, facility destruction/control loss, or world-end unless the decision engine has already delivered the cancellation callback.

Integration visibility checks current host, Theory stage, and native completion, but not primary facility or world-end, and there is no integration-specific `cancel_trigger`. A facility can become invalid while the integration timer remains visible, allowing its remove callback to call the unguarded native helper.

The four native synchronization branches check only stage Theory, available Capacity, and their native completion predicate (`project_effects:1116-1149`). The `on_project_completion` wrapper checks only `brilliant_scientist_is_current_host` (`common/on_actions/016_brilliant_scientist_project_on_actions.txt:11-21`), so it does not prevent a sync after facility invalidation or after world-end if the callback is delivered in that state.

Event 016 terminal marks set the all-actions lock, but the existing terminal cleanup clears transient targets and facility pointers without clearing `brilliant_scientist_project_stage_in_progress` or the active stage receipt (`common/scripted_effects/016_brilliant_scientist_effects.txt:3856-3912`; called from `common/scripted_effects/016_brilliant_scientist_super_event_effects.txt:677-710`). This leaves delayed stage/integration callbacks relying on the current helper behavior after world-end.

The owner patch should add a no-world-end and valid-host/primary-facility guard to delayed finalization and native synchronization, add the same invalidation to integration visibility or an explicit integration cancellation trigger, and close active receipts from the existing terminal cleanup. A matching invalid callback should clear/refund its reservation through the canonical rebuild and produce no stage reward; a mismatched invalid callback must remain a no-op so it cannot touch a newer receipt.

### Transfer and reinitialization interaction

The transfer input trigger validates transfer readiness, the recipient target, current host, no world-end, and the recipient's eligibility before mutation (`common/scripted_triggers/016_brilliant_scientist_triggers.txt:121-159`). An invalid transfer therefore leaves the current obligations untouched, as required by the contract.

On a valid transfer, the old-host reconciliation intentionally clears the stage lock and active receipt, reconstructs the old host's ledger/capacity state, and clears facility targets (`common/scripted_effects/016_brilliant_scientist_effects.txt:1254-1301` and `2970-3046`). Recipient inheritance also clears any active receipt before rebuilding the carried portfolio (`common/scripted_effects/016_brilliant_scientist_effects.txt:1970-2070`). A delayed old callback must therefore see no matching receipt and do nothing; the identity guard preserves that behavior without letting the stale callback clear a new transaction.

Transfer/reinitialization is the existing legitimate use of canonical gross reconstruction. The receipt correction should not add an independent capacity scaling pass or replay stage costs.

## Minimum safe owner patch recipe

### 1. Add an identity-aware stage receipt predicate and settle helpers

Add a narrow scripted trigger in `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt`, or an equivalent inline guard in the owner effects, with COUNTRY scope and temporary callback family/stage inputs.

The predicate should require the shared in-progress flag, both active receipt variables, valid callback family/stage inputs, and equality of active family to callback family and active stage to callback stage.

Change every one of the 45 normal wrapper `cancel_effect` blocks to set its fixed family and requested stage temporary values before calling `brilliant_scientist_cancel_project_stage`; the callback identity is created inside the callback effect and does not depend on temporary variables surviving the timer.

Change `brilliant_scientist_cancel_project_stage` so all refund/clear operations are inside the matching predicate. A mismatched or absent receipt must not change Capacity, the shared flag, or any active variable.

Change `brilliant_scientist_finish_project_stage` so reward/advance/output work and all cleanup are inside the matching predicate. On changed=true, clear the matching receipt after output work and rebuild Capacity from canonical gross. On changed=false, apply no reward, clear the matching receipt, and rebuild Capacity from canonical gross so the reservation is removed exactly once. On invalid host/facility/world-end, do not advance or reward; close only a matching receipt and rebuild Capacity.

The existing `begin_project_stage` may keep its current normal caller contract and resource costs. For defense in depth, the owner may add a valid-family/stage and idle-receipt guard before overwriting the active receipt, but this is secondary to making every finalizer identity-safe.

### 2. Make native Prototype settlement atomic with the ledger change

Set requested stage to Prototype before any Capacity mutation.

Require valid family input, current host, valid primary facility, no world-end/terminal state, current ledger exactly Theory, and Capacity at least `capacity_prototype` before invoking the generic advance helper.

Invoke `brilliant_scientist_advance_project_to_requested_stage` only inside that guard.

If `brilliant_scientist_project_stage_changed = one`, apply the existing stage output/incident/force/recognition work, then call `brilliant_scientist_refresh_project_capacity_from_gross` once so the new Prototype burden is charged exactly once.

If changed=false or any guard fails, do not subtract Capacity and do not apply output.

Run the gross rebuild after family-dependent work or restore the temporary family/stage inputs before any subsequent consumer because the 15-entry loop changes the temporary family variable.

Leave `brilliant_scientist_advance_project_to_requested_stage` unchanged for inheritance and other upward transitions.

### 3. Give all native integration timers an identity receipt

The 15 integration `complete_effect` blocks should call one narrow owner helper or equivalent repeated local sequence that stores normal `brilliant_scientist_active_native_integration_family = <family>` and `brilliant_scientist_active_native_integration_stage = prototype`, and sets the shared lock.

The integration receipt is a transaction identity, not another meter and not a Capacity reservation. It must remain separate from `active_project_capacity_delta` so `refresh_project_capacity_from_gross` never counts an integration timer as a stage reservation.

The 15 `cancel_effect` blocks should clear the shared lock and integration variables only if the active integration family/stage matches the fixed decision identity.

The 15 `remove_effect` blocks should first verify that the integration receipt matches and the current family ledger is exactly Theory and that host/facility/world-end validation still passes. Only then should they call `brilliant_scientist_complete_native_prototype_stage`; afterward they should clear the matching integration receipt and shared lock.

If native synchronization already advanced the family to Prototype, a later integration remove callback must clear only its matching integration receipt and perform no native helper call. If the integration remove wins first, the later synchronization branch sees Prototype and performs no charge. Either ordering therefore produces one Prototype reward and one Capacity charge.

The shared lock must not be cleared by a stale callback from another family. This is the key difference from the current unconditional integration `clr_country_flag` lines.

### 4. Keep synchronization authoritative but fail closed

Retain the four family branches and their native OR predicates. Add current-host, primary-facility, and no-world-end validation at the sync owner boundary and retain the same checks inside the native helper.

Do not add a global no-active-timer guard to sync. Rocketry and Biological Weapons require sync to settle a second native completion during an integration timer.

The native branch source callers already prevent the normal duplicate path by checking current ledger Theory and enough Capacity before each helper call. They do not prevent a stale integration remove or an invalid delayed callback, so the helper-level changed guard remains mandatory.

### 5. Close receipts in terminal cleanup

Extend the existing Event 016 world-end terminal cleanup with a dedicated idempotent active-receipt close that runs before primary/secondary facility targets are cleared.

For an active normal stage receipt, clear/refund only the current receipt and rebuild Capacity from canonical gross; for an active native integration receipt, clear only its integration identity and shared lock because it has no Capacity reservation.

After terminal cleanup clears the receipt, delayed callbacks see no matching identity and cannot produce a reward, clear a newer lock, or charge Capacity. Do not rely only on `all_actions_locked_after_world_end`, because the project-board wrappers and integration blocks do not currently use that flag as their callback identity.

## Capacity conservation decision

The canonical source is `brilliant_scientist_project_capacity_gross` minus ledger burdens reconstructed by `brilliant_scientist_refresh_project_capacity_from_gross`.

For a successful normal stage finish, the current direct subtraction is mathematically equivalent to rebuilding from the new ledger in a clean state, but canonical rebuild is safer after receipt matching because it removes the active reservation exactly once and exposes any pre-existing available/gross drift instead of preserving it silently.

For a normal cancellation or matching changed=false finish, rebuild after clearing the matching receipt rather than adding the active delta manually. Adding the delta can be used as a local arithmetic explanation, but it is not sufficient as the canonical owner behavior when prior Capacity drift exists.

For native Prototype settlement, never subtract before the changed guard. Advance first, then rebuild only on changed=true; changed=false and invalid calls leave Capacity untouched.

This recommendation is a receipt correction, not a Capacity cap or total-cost redesign. `brilliant_scientist_change_project_capacity` separately changes both available and gross Capacity and clamps both (`016_brilliant_scientist_effects.txt:548-553`), so a canonical rebuild may visibly correct historical divergence between those values. The parent should report that observable correction rather than claiming every pre-existing save retains its exact pre-patch available value.

## Helper and documentation map for the owner

| Proposed narrow helper | Scope and inputs | Outputs and side effects | Call sites |
| --- | --- | --- | --- |
| `brilliant_scientist_project_stage_receipt_matches` | COUNTRY; temporary callback family/stage | Trigger-only identity result; no writes | `cancel_project_stage`, `finish_project_stage`, and any explicit terminal close wrapper |
| `brilliant_scientist_native_integration_receipt_matches` | COUNTRY; temporary fixed family and Prototype stage | Trigger-only identity result; no writes | 15 integration cancel/remove callbacks and terminal close |
| `brilliant_scientist_close_active_project_receipt` | COUNTRY; no callback input, only an explicit terminal/reconciliation owner | Idempotently closes the current active stage or integration receipt; rebuilds Capacity only after removing a stage reservation; does not award output | Existing Event 016 terminal cleanup and, if needed, valid transfer/reinitialization closure |
| `brilliant_scientist_complete_native_prototype_stage` (corrected owner effect) | COUNTRY; temporary family; internal requested stage Prototype | Exact Theory-to-Prototype transition, one output, one canonical Capacity rebuild; no-op for invalid family, invalid context, changed=false, or insufficient Capacity | Four native sync branches, 15 integration resolvers, ten new native project output bridges, and six Singularity component bridges |

If the parent adds these helpers, document purpose, scope, inputs, outputs, defaults, and side effects in `docs/events/016_brilliant_scientist/systems/projects.md` or the owner-specific scripted-effects documentation if that file is introduced by the parent. Do not put Event 016-specific receipt state into the shared `chaosx_dynamic_effects` registry.

## Event targets and cleanup plan

The active stage and integration receipts should remain normal country variables and flags; no new event target is needed for a family/stage identity.

`brilliant_scientist_primary_facility` and `brilliant_scientist_secondary_facility` remain global event targets and must be validated with `has_event_target`, `scope_exists`, state validity, control, and owner checks before delayed completion. The existing transfer and terminal code clears those global targets, so finalizers must not dereference them after cleanup.

Valid transfer keeps its existing pre-mutation validation and old-host reconciliation. Invalid transfer must continue to leave all current obligations intact.

World-end terminal cleanup must close active stage/integration receipts before or atomically with clearing facility targets. Permanent project ledger/history arrays, learned technologies, and completed outputs remain untouched.

## Source caller prevention matrix

| Path | Existing source prevention | Remaining gap |
| --- | --- | --- |
| 45 normal stage selection | Board-ready gate, current host, valid primary facility, no active stage/incident, exact predecessor, cost/resource/experience/Capacity checks | `begin_project_stage` itself can overwrite a receipt if called outside those callers; no callback identity in cancel path |
| 45 normal stage cancel | `cancel_if_not_visible`, explicit host/facility cancel trigger, and normal decision lifecycle | Inputless cancel can refund and clear a newer receipt if a stale/duplicate callback arrives |
| 45 normal stage finish | Fixed family/stage temporary values and active family/stage guard protect reward/advance | Cleanup is outside the guard; changed=false loses the active reservation |
| 15 integration selection | Current host, exact Theory ledger, native completion predicate, no shared lock/incident, enough Prototype Capacity | No primary-facility/world-end gate and no persisted family/stage receipt |
| Four native sync branches | Exact family index, Theory ledger, enough Capacity, native completion predicate; on-action outer current-host gate | No facility/world-end gate; current helper charges before changed guard; OR branches permit sync during Rocketry/Biological integration as an ordinary case |
| New native project output bridge | Native project visibility/availability triggers require current host, valid primary facility, no active incident, exact Theory and enough Capacity | Delayed output helper itself has no final host/facility/world-end guard |
| Valid transfer | `brilliant_scientist_transfer_inputs_are_valid` validates before mutation; old-host and recipient reconciliation clear active receipt and rebuild | Stale callbacks after reconciliation require identity no-op; current unconditional cleanup is unsafe without the patch |
| World-end terminal | Terminal marks set an all-actions lock and cleanup clears facility pointers | Existing cleanup does not clear stage/integration receipts or shared stage lock; delayed callbacks can still reach current finalizers |

## Constants and tuning table plan

No new tuning constants are required for the receipt correction.

Reuse `constant:brilliant_scientist_project_board.capacity_prototype` for the native transition, existing stage capacity values for the canonical rebuild, and existing world-end/terminal flags.

The 45 cost profiles, durations, AI priorities, and native special-project payments are explicitly outside this review and must remain unchanged.

## Migration plan

First add the identity predicates and corrected owner effects in the project-effects/triggers files.

Second mechanically stamp fixed family/stage values into the 45 normal `cancel_effect` blocks and replace their inputless cancellation behavior with identity-aware calls.

Third stamp the 15 integration receipt writes and matching cancel/remove guards while preserving their existing days, costs, AI values, visibility text, and native family mappings.

Fourth add host/facility/world-end gates to the sync owner and delayed finalizers, and add terminal receipt closure to the existing world-end cleanup.

Finally run source-only checks for helper call counts, fixed family/stage mapping, no unguarded `clr_country_flag = brilliant_scientist_project_stage_in_progress` in the in-scope 45/15 callbacks, exactly one native Capacity settlement branch, and unchanged cost/duration/priority tokens.

## Validation and evidence

Required local references were read before review: `AGENTS.md`; `.agents/skills/chaos-redux-events/SKILL.md`; `.agents/skills/chaos-redux-decisions-missions/SKILL.md`; `.agents/skills/chaos-redux-subagents/SKILL.md`; `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md`; and `docs/events/016_brilliant_scientist/systems/projects.md`.

The offline Paradox wiki references consulted were `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, `Triggers - Hearts of Iron 4 Wiki.md`, `Effects - Hearts of Iron 4 Wiki.md`, `Scopes - Hearts of Iron 4 Wiki.md`, `Event modding - Hearts of Iron 4 Wiki.md`, and `Decision modding - Hearts of Iron 4 Wiki.md`, including event-target persistence, scoped variables, scripted effects/triggers, decision `complete_effect`, `days_remove`, `remove_effect`, `cancel_trigger`, `cancel_if_not_visible`, and `cancel_effect` behavior.

The vanilla documentation references consulted were `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md`, `effects_documentation.md`, and `triggers_documentation.md`, including script constants, `save_event_target_as`, `clear_global_event_target`, `has_event_target`, `scope_exists`, `check_variable`, decision effects, and target validity.

A bounded read-only Event 016 MCP inspection was attempted through `hoi4.event_inspect` with selector `{kind: event, eventId: chaosx.nr16.1}`, trace mode, both directions, depth 2, 40 nodes, 80 edges, and helper expansion disabled. It returned `EVENT_INSPECTED_PARTIAL`, revision `65f53c2f4a099c16d11d6ab9960f409df2c881e6ad4b02f663cc098b6d5137bd`, focused analysis, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cd14c1addf292816533fbae2f831bf8ee45eaff3f94d374e5b9706200579058e/30212a2eb7fa52ee0a45878e7982748f1c3826e754572c2d84b321f1afa1c402/event-trace-65f53c2f4a09.json`.

The MCP report explicitly deferred workspace-wide helper/lifecycle passes, reported zero projected helpers, and truncated the inline source inventory at 64 of 368 paths (`MCP_INLINE_FILES_TRUNCATED`). It is useful as bounded Event 016 event-surface evidence but does not prove scripted decision callback ordering, native project timer ordering, or live host/facility/world-end transitions; those findings remain source-only.

No probability inspection or `chaosx_ai_probability_auditor` pass was run because this review makes no weight, AI priority, MTTH, random, or probability claim and the user explicitly prohibited broadening into that surface.

No live game launch, model regeneration, GUI inspection, event rendering, or gameplay mutation was performed.

## Known limitations and follow-up ownership

The parent must choose the exact Clausewitz syntax for the identity predicates, receipt variable names, and terminal close helper, then own implementation and post-patch validation.

The review cannot establish whether a particular engine build invokes `cancel_effect` before a stale `remove_effect` after a visibility change; the proposed idempotent guards make either order safe without relying on that undocumented ordering.

The review does not audit the other project-board decisions that also use the shared stage lock, except where their direct lock clearing could be a future broader surface. Their cost profiles, balance, AI priorities, rewards, and probabilities remain unreviewed by this handoff.

No gameplay simplification, fallback, new family, new evolution, new country, new focus, new meter, new GUI, new event, or new model was introduced.

## Postpatch source review (2026-09-02)

Status: pass for the requested narrow receipt correction, with one explicitly bounded capacity-reservation limitation recorded below. The owner patch was reviewed read-only against the retained baseline; no gameplay files were edited and no commit was made by this subagent.

### Receipt ownership and callback guards

`brilliant_scientist_begin_project_stage` now writes the exact normal family/stage receipt and its active Capacity delta only after the board-ready, input, cost, predecessor, and resource checks in `common/scripted_effects/016_brilliant_scientist_project_effects.txt:9–55`.

The private finalizer at `:57–66` clears the shared stage flag, active family/stage, and active delta, then rebuilds available Capacity from canonical gross Capacity last. Keeping the rebuild last is required because `refresh_project_capacity_from_gross` iterates the 15-family ledger and overwrites its temporary family input (`common/scripted_effects/016_brilliant_scientist_effects.txt:1028–1074`).

Normal cancellation at `:68–77` and normal finishing at `:80–128` first require `brilliant_scientist_project_callback_matches_active_stage` plus the timed-stage filter. A stale or duplicate callback for another family/stage therefore leaves the current receipt, flag, Capacity, and ledger untouched. Normal finish additionally requires a valid current context and the exact predecessor ledger stage before calling the shared advance helper; changed output remains inside the `changed = 1` branch. The old unconditional cleanup outside that guard is gone, so a changed=false or invalid callback cannot close a newer receipt.

The 45 normal decision wrappers now stamp fixed family/stage inputs in complete, cancel, and remove paths. A source count found exactly 45 `brilliant_scientist_begin_project_stage`, 45 `brilliant_scientist_cancel_project_stage`, and 45 `brilliant_scientist_finish_project_stage` calls, with the family and stage values matching each wrapper. Existing costs, durations, visibility text, and AI fields remain in place.

### Native integration ownership and native settlement

The 15 prototype integration wrappers now stamp the fixed family and Prototype stage. `brilliant_scientist_begin_native_prototype_integration`, `cancel_native_prototype_integration`, and `finish_native_prototype_integration` at `common/scripted_effects/016_brilliant_scientist_project_effects.txt:130–161` use the shared active family/stage receipt with `active_project_capacity_delta` absent. This is the correct distinction from a paid normal timed stage: current normal wrappers accept only Theory, Deployment, or Weaponization, while `brilliant_scientist_native_integration_matches_active_stage` requires Prototype and no active delta (`common/scripted_triggers/016_brilliant_scientist_project_triggers.txt:85–98`).

The native helper at `:163–192` checks current host, valid primary facility, terminal/world-end exclusions, exact family input, exact Theory ledger stage, and Prototype Capacity before advancing. It does not debit Capacity before the guard. Rewards, incident/force/recognition/threat output, and the gross-based Capacity rebuild are emitted only when the shared advance reports `changed = 1`. A repeated native notification after the ledger is already Prototype therefore produces no reward and no second Prototype Capacity burden.

The 15 integration wrappers now have exactly 15 begin, 15 cancel, and 15 finish calls, with 15 unchanged `days_remove` values and the correct family mapping across computation, materials, biomedical, teleportation, cloning, robotics, paleogenetics, xeno synthesis, alien arms, temporal, singularity, electronics, rocketry, high energy, and biological weapons. A source comparison of all 60 target wrapper blocks found no metadata changes to cost, duration, or AI fields.

### Ordinary synchronization during an integration timer

For the ordinary Rocketry or Biological Weapons case, an integration timer can begin while that family is at Theory. The four native synchronization branches at `:1198–1237` remain independent and are intentionally allowed to run while a timer is active; each still requires its exact family ledger index, Theory stage, sufficient Capacity, and the corresponding native completion predicate.

If the synchronization callback settles first, the native helper advances Theory to Prototype once, applies the family output once, and rebuilds Capacity from gross. The integration receipt remains present because the native helper does not clear active fields. The now-hidden integration decision subsequently routes its cancellation callback to the fixed family/Prototype cancel helper; the identity guard matches and the private finalizer closes the timer without refund or second reward.

If the integration remove callback settles first, the native helper performs the one Theory-to-Prototype transition and the private finalizer closes the receipt. The later synchronization callback sees Prototype rather than Theory and no-ops. If the visibility cancellation callback arrives before remove, it closes the same receipt and a later remove is an identity no-op. Thus either source-level callback order converges to one native output and one Prototype ledger burden, with no live integration receipt after closure. The earlier bounded MCP inspection did not establish engine callback ordering, so this is source/control-flow evidence rather than engine-order evidence.

The same guard handles cross-family native synchronization during an integration timer. Such a synchronization can consume available Capacity and leave the integration receipt intact; the integration later settles only if its exact Theory and Capacity preconditions still hold. If another native transition exhausts the required Capacity first, the integration settles fail-closed with no reward and the receipt is then closed. This preserves conservation and prevents over-capacity, but it does not reserve Capacity for an already-started integration; changing that policy would be a separate capacity-design surface outside this review.

### Terminal, transfer, and KRG interactions

`brilliant_scientist_project_context_is_valid` now excludes invalid host/facility state and all terminal/world-end markers (`common/scripted_triggers/016_brilliant_scientist_project_triggers.txt:55–83`). Delayed normal and native callbacks therefore cannot reward after loss of the host, primary facility, or world-end state. The terminal-only closer at `common/scripted_effects/016_brilliant_scientist_project_effects.txt:80–95` does not require live context: legal normal receipts are cancelled through the identity-checked cancel path, while a legal Prototype-without-delta integration receipt is closed through the private finalizer. The existing terminal callers set their terminal markers before invoking cleanup (`common/scripted_effects/016_brilliant_scientist_super_event_effects.txt:677–710`), so the closer remains able to clear receipts after context has become invalid without granting output.

Transfer/formation reconciliation still clears the shared stage flag and active family/stage/delta before canonical gross reconstruction (`common/scripted_effects/016_brilliant_scientist_effects.txt:1254–1309`). Stale callbacks against the old receipt consequently fail the exact identity guard. The KRG interruption snapshot at `common/scripted_effects/016_brilliant_scientist_country_effects.txt:909–920` requires an active Capacity delta; the absent-delta Prototype integration receipt is intentionally not serialized as a paid interrupted project. No in-scope consumer treats Prototype plus absent delta as an interrupted normal stage. Storing numeric zero instead would incorrectly satisfy that `has_variable` test and expose a false KRG interruption snapshot, so omission is safer and matches the shared-receipt contract.

### Evidence boundary and remaining ownership

This postpatch section is source-only. No new MCP inspection, GUI/render pass, live game launch, or gameplay mutation was performed, as requested. The prior bounded Event 016 MCP artifact remains partial and does not prove callback ordering or live terminal/transfer timing.

The owner patch preserves the 45/15 cost, duration, priority, and AI surfaces and does not redesign reward profiles or probabilities. Parent ownership remains final diff review, syntax/load validation, and commit. The only remaining design note is the explicitly fail-closed, non-reserved Capacity behavior for a native integration that competes with another native transition during its timer; it is not a receipt-identity defect and should not be expanded in this closure patch.
