# Event 016 final Singularity construction transaction handoff

Status: implementation-ready and frozen for parent integration.

Date: 2026-09-02.

## Scope

This tranche adds only the payment and callback transaction wrappers for the existing command-core and power-link construction decisions.

It does not edit the decisions, physical-site ledger, project triggers, project effects, constants, lifecycle hooks, localisation, AI weights, costs, durations, facility definitions, models, events, or GUI.

The parent owns the target-decision conversion, callback target setup, custom-cost wiring, lifecycle hooks, MCP probability evidence, and final integration.

## Files added

- `common/scripted_effects/016_brilliant_scientist_singularity_construction_effects.txt`
- `common/scripted_effects/016_brilliant_scientist_singularity_construction_effects.md`

The new effect file depends on the already-owned physical-site interfaces in `016_brilliant_scientist_singularity_site_effects.txt` and `016_brilliant_scientist_singularity_site_triggers.txt`, and on existing Event 016 project pay/affordability helpers.

## Exact public effects

Begin wrappers:

- `brilliant_scientist_singularity_construction_begin_command_node`
- `brilliant_scientist_singularity_construction_begin_power_link`

Finish wrappers:

- `brilliant_scientist_singularity_construction_finish_command_node`
- `brilliant_scientist_singularity_construction_finish_power_link`

Callback-cancel wrappers:

- `brilliant_scientist_singularity_construction_cancel_command_node`
- `brilliant_scientist_singularity_construction_cancel_power_link`

Authoritative lifecycle cleanup:

- `brilliant_scientist_singularity_construction_cleanup`

Private cores and metadata helpers are in the same file and are not intended as additional decision IDs.

## Caller inputs and outputs

The parent caller runs in the paying country scope and supplies regular event target `brilliant_scientist_singularity_site_selected_state` plus temporary `brilliant_scientist_singularity_site_selected_role` and `brilliant_scientist_singularity_site_selected_quantity = 1`.

Each role wrapper sets only a temporary expected role and leaves the caller's selected inputs unchanged.

Begin output is temporary `brilliant_scientist_singularity_construction_begin_applied`, one only after reservation, receipt creation, four-resource payment, PP payment, and shared-stage ownership succeed.

Finish outputs are temporary `brilliant_scientist_singularity_construction_finish_applied` and `brilliant_scientist_singularity_construction_finish_refunded`.

Callback-cancel outputs are temporary `brilliant_scientist_singularity_construction_cancel_applied` and `brilliant_scientist_singularity_construction_cancel_refunded`.

Lifecycle outputs are temporary `brilliant_scientist_singularity_construction_cleanup_applied` and `brilliant_scientist_singularity_construction_cleanup_refunded`.

## Receipt fields

The active private receipt is country-owned:

- Flag `brilliant_scientist_singularity_construction_receipt_active`.
- `brilliant_scientist_singularity_construction_receipt_state` state-scope pointer copied from the selected event target.
- `brilliant_scientist_singularity_construction_receipt_role` exact command-core or power-link role ID.
- `brilliant_scientist_singularity_construction_receipt_quantity` exact one-per-paid-row quantity.
- `brilliant_scientist_singularity_construction_receipt_political_power` positive PP quote.
- `brilliant_scientist_singularity_construction_receipt_support_equipment` positive support-equipment quote.
- `brilliant_scientist_singularity_construction_receipt_trucks` positive motorized-equipment/truck quote.
- `brilliant_scientist_singularity_construction_receipt_fuel` positive fuel quote.
- `brilliant_scientist_singularity_construction_receipt_manpower` positive manpower quote.

There is deliberately no CIC receipt field.

The native decision's existing `civilian_factory_use` modifier remains the only CIC occupation/release mechanism.

## Transaction ordering

Begin first checks `brilliant_scientist_project_board_is_ready`, exact role/quantity, and absence of this receipt.

It calls `brilliant_scientist_singularity_site_reserve_construction` before evaluating the existing role-specific affordability trigger.

If reservation succeeds but affordability fails, it cancels the physical pending row and charges nothing.

On affordability success it snapshots the exact constants into ordinary receipt variables, sets the private receipt flag, calls the existing four-resource pay helper, debits PP exactly once, and then sets `brilliant_scientist_project_stage_in_progress`.

The shared stage flag is set only after this construction receipt owns the paid transaction.

Finish and callback cancel first require this construction receipt's exact state, expected/selected role, quantity, active flag, and all five stored resource amounts.

If a physical pending row still exists, its physical callback identity must also match; if a lifecycle hook already consumed that row, physical-row absence still permits the matching private receipt to take the refund path.

Wrong-state or wrong-role callbacks are strict no-ops and cannot clear another receipt or the shared stage flag.

For a matching callback, the effect snapshots the five positive receipt amounts and clears the private receipt before any physical completion/cancellation output.

Finish grants physical completion only when the current Event 016 host context and physical callback validity both hold and the physical completion output is one.

A successful finish clears the shared stage flag and awards no refund.

An invalid host, captured/lost state, missing facility, terminal context, missing physical pending row, or unexpected physical completion-zero output cancels and refunds the exact stored snapshot once, with no completion reward.

Callback cancellation always refunds the exact stored snapshot once after identity validation.

Lifecycle cleanup requires only this receipt's active flag, so it can run after capture, annexation, terminal shutdown, or loss of callback state.

It clears and cancels only this construction receipt, refunds its stored snapshot once, and clears the shared flag only because this receipt was active.

It does nothing when the private receipt flag is absent, so it cannot cancel an unrelated board stage.

## Cost and duration source lock

The exact cost constants are in `common/script_constants/016_brilliant_scientist_project_constants.txt` under `brilliant_scientist_project_board`.

The requested `_project_board_constants.txt` path is not present in the repository; no replacement constants were added.

The command core uses node PP/support/trucks/fuel/manpower quotes and the existing `brilliant_scientist_pay_singularity_command_node` helper.

The power link uses link PP/support/trucks/fuel/manpower quotes and the existing `brilliant_scientist_pay_singularity_power_link` helper.

The existing native construction durations remain `brilliant_scientist_singularity.core_construction_days` for command core and `brilliant_scientist_singularity.delivery_construction_days` for power link.

No CIC amount is recomputed or refunded by these effects.

The frozen numeric profiles are command core: 100 PP, 1200 support equipment, 150 trucks, 5000 fuel, 1500 manpower, 5 occupied civilian factories, and 1080 days; power link: 100 PP, 1000 support equipment, 100 trucks, 7500 fuel, 1000 manpower, 6 occupied civilian factories, and 720 days.

## Scenario traces for parent review

### Ordinary successful command-core or power-link construction

A valid selected state/role/quantity reserves one pending site row, passes the existing strict affordability checks, stores the quote, pays support/trucks/fuel/manpower through the existing helper, debits 100 PP, and sets the shared stage flag exactly once.

The matching finish callback clears the receipt before site completion, marks the exact physical row live and historically constructed, clears the shared flag, and gives no refund.

### Duplicate begin

While the receipt or shared stage is active, board-ready fails; no second physical row or resource debit is created.

### Wrong role or wrong state callback

A command wrapper supplied a power-link role, or either wrapper supplied another state target, fails the construction-receipt identity guard before receipt clearing, physical mutation, refund, or shared-flag clearing.

The original receipt remains active for its legitimate callback.

### Captured state or invalid facility at expiry

If identity matches but the host/context, ownership/control, actual qualifying facility, or physical pending row is invalid, finish clears the private receipt first, cancels the pending physical row if present, refunds the stored five-value snapshot exactly once, clears the shared stage flag, and grants no physical completion.

### Lifecycle capture/annexation cleanup

The owner cleanup does not need a selected callback target or current facility.

With the active receipt flag it clears private metadata, invokes authoritative physical cancellation, refunds the exact stored quote once, and clears the shared stage flag.

### Repeated stale callback

After successful finish, callback cancellation, or lifecycle cleanup, the private active flag and receipt fields are gone; a repeated callback is a no-op.

### Malformed receipt

If a receipt amount is missing, finish and callback cancellation fail closed before settlement and snapshot completeness becomes zero.

Cleanup still clears the private receipt and physical pending state but does not invent a new cost or issue a partial refund.

## Validation and known limits

Source review covered the existing project-board readiness trigger, strict affordability triggers, role-specific pay helpers, exact constants, native CIC/duration fields, and physical-site reservation/completion/cancellation interfaces.

The new effect file has balanced Clausewitz braces and no unsupported `<=` or `>=` operators.

No game process, live save, or log was used; no engine acceptance claim is made.

No existing caller is edited in this tranche, so integration is intentionally pending the parent decision owner.

No commit or staging was performed.

## Post-integration read-only review — 2026-09-02

The parent integration was reviewed source-only after the state-targeted decision conversion.

Reviewed decision blocks are `common/decisions/016_brilliant_scientist_directorate_project_board.txt:3862-3980` at SHA-256 `C16BABFE46636C5EF4ADA5427BDB55EFF48DFCA34035C0F0266CD6C9FB4DBC76`.

The related lifecycle and physical-ledger sources reviewed were `common/on_actions/016_brilliant_scientist_project_on_actions.txt:24-116` at SHA-256 `0B202FA1D0943B29DE3BE5331FA56ED0C64FCFC38561483F4D751F620B799540`, `common/scripted_effects/016_brilliant_scientist_singularity_construction_effects.txt:92-439`, `common/scripted_effects/016_brilliant_scientist_singularity_site_effects.txt:93-343` at SHA-256 `C44307D454E36C151D336FECD00AF17902D4077773D1168747122F40F6C9B4E0`, `common/scripted_triggers/016_brilliant_scientist_singularity_site_triggers.txt:1-343` at SHA-256 `EED47E7E3A8C5CB483CA84EE5B77C596EC905C4F2D6D061FD851C81A55C3FE31`, `common/scripted_effects/016_brilliant_scientist_country_effects.txt:954-1013`, `common/scripted_effects/016_brilliant_scientist_effects.txt:2933-3037` and `:3886-3904`, plus the inclusive affordability changes in `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt:1918-1935` at SHA-256 `A91291D5D96D7748092ABD9CC75357D293C0619F4EC26E10D0A65ED726F9BC86`.

### Disposition

The exact payment layer is correct: the inclusive affordability triggers cover PP, support equipment, trucks, fuel, and manpower; the existing pay effects debit only the four physical resources; the construction wrapper debits PP once from its snapshot; and the decision's `civilian_factory_use` modifier remains the only CIC reservation and automatic release path.

The decision uses `custom_cost_trigger` and has no native `cost` field, so there is no source-visible second PP charge.

The exact finish and cancel identity checks run before receipt clearing, and the private finalizer clears its receipt before physical output; invalid completion refunds the saved positive quote once and does not award a physical row.

The terminal ordering is correct: `brilliant_scientist_cleanup_transient_targets_after_world_end` calls construction cleanup before `brilliant_scientist_singularity_site_retire_all` and the generic project close at `common/scripted_effects/016_brilliant_scientist_effects.txt:3888-3904`.

The split-sovereignty host-to-KRG path cancels the former host's paid construction before moving permanent site rows with `brilliant_scientist_singularity_site_migrate_registry_to_krg` at `common/scripted_effects/016_brilliant_scientist_country_effects.txt:1000-1007`; this is a move rather than a copy and therefore does not duplicate live infrastructure or payment.

The atomic transfer path intentionally cancels construction and retires the old host's physical rows at `common/scripted_effects/016_brilliant_scientist_effects.txt:3029-3034`; no payment orphan is introduced there.

Vanilla targeted state decisions use `FROM` in their `remove_effect` and `cancel_effect` blocks, and the offline decision documentation defines `complete_effect` as selection-time and `remove_effect` as timer-expiry settlement.

The parent callbacks re-save their current `FROM` state target immediately before each wrapper call, so settlement does not depend solely on the regular target saved at selection.

This establishes the intended callback scope from repository and vanilla precedents, but no HOI4 engine launch or live-save callback test was performed.

### Required owner fixes

1. P1 lifecycle orphan: `on_annex` and `on_civil_war_end_before_annexation` currently clean Mengele and foreign receipts only at `common/on_actions/016_brilliant_scientist_project_on_actions.txt:99-115`.

Vanilla on-action comments establish `ROOT` as the annexer and `FROM` as the annexed country, so an annexed owner with an active construction receipt can disappear before the native decision callback runs.

That path strands the private receipt, pending physical row, shared stage flag, and already-debited resources with no refund.

Add `FROM = { brilliant_scientist_singularity_construction_cleanup = yes }` to both participant-owned hooks before the country is discarded.

The cleanup is already authoritative and owner-scoped, requires only its own active receipt, snapshots the exact amounts, clears the receipt, cancels the pending row if present, refunds once, and does not clear an unrelated board stage.

Do not add this call to ordinary `brilliant_scientist_clear_foreign_relationships`; that effect runs during successful transfers and assassinations and must not cancel a live operation or construction merely because relationship cleanup is in progress.

2. P2 begin-failure timer: each decision's `complete_effect` starts the native `days_remove` timer even when `brilliant_scientist_singularity_construction_begin_core` fails after its revalidation.

The begin core can reserve and then cancel the physical row without creating a receipt when board readiness, affordability, or another race check fails.

The current `cancel_trigger` at decision lines `3901-3905` and `3961-3965` does not test receipt ownership, so that failed start can leave a dead 1080-day or 720-day decision whose expiry callback is a no-op.

Add `NOT = { has_country_flag = brilliant_scientist_singularity_construction_receipt_active }` as an OR branch in each `cancel_trigger`, and add the same receipt-absence guard to `available` if malformed state could leave a receipt without the shared stage flag.

The guard cancels only a timer that never acquired this construction receipt; the matching `cancel_effect` then remains a no-op and issues no refund.

3. P2 AI budgeting hint: after conversion from native `cost` to `custom_cost_trigger`, neither decision defines `ai_hint_pp_cost`.

The offline decision documentation states that custom PP cost is not automatically represented to AI budgeting.

Add a 100-PP `ai_hint_pp_cost` to both existing decisions using the already-locked node/link PP constants or the supported literal form, without changing `ai_will_do`, costs, durations, or probability factors.

This is an AI planning correction only; it does not alter the scripted debit.

4. P2 stale cap and visibility: the new command and power-link decisions still gate `target_root_trigger` and `visible.hidden_trigger` on the legacy country counters at lines `3866-3869`, `3872-3878`, `3926-3930`, and `3932-3938`.

The physical reconstruction helper is used by deployment readiness, KRG arming, final commit, and state-control reconciliation, but it is not used by either construction decision or by the begin core's capacity guard.

On a legacy or malformed save where live rows and counters disagree, two live command rows with a stale zero counter can expose and permit an over-cap third payment, while a stale full counter can hide valid physical capacity.

Add a bounded role-specific physical live-row room trigger, or equivalent exact reconstruction in the begin core, and use it in both target/visibility gates and immediately before reservation.

Normal new construction remains reconciled by completion, cancellation, and state-control hooks, so this finding is specifically the stale/imported-ledger path rather than an ordinary successful-flow defect.

### Scenario traces

Ordinary success: a valid country selects a state through `FROM`; complete-time setup re-saves that state and sets the literal role/quantity; begin reserves the physical row, snapshots and debits the exact five direct payments, sets the receipt and shared stage flag, and the remove callback re-saves the same `FROM` state before finish; matching identity plus current host/facility validity completes one physical row without refund.

Wrong-state or wrong-role callback: the callback wrapper sets the fixed role and re-saves the supplied `FROM` state, then the private guard compares state, role, quantity, active flag, and stored amounts before any clear, physical mutation, refund, or shared-flag clear; the current receipt remains untouched.

Repeated callback after finish, cancel, cleanup, or terminal retirement: the active receipt flag and fields are absent, so the helper is a no-op and cannot replay a reward or refund.

Same-state same-role replay caveat: the receipt has exact state/role/quantity/amount identity but no generation token, so an externally replayed old callback could theoretically match a newly opened identical receipt; native decision cancellation/removal semantics provide no source evidence that such a callback is emitted, so this remains an engine-uncertainty note rather than a proven path.

Begin race/failure: complete-time invocation can fail its board or affordability recheck after the target was visible; the helper cancels the reserved row and creates no payment receipt, but the current timer needs the receipt-absence cancel branch above to end immediately.

Capture or control loss: `on_state_control_changed` reconciles both the new `ROOT` and old `FROM` countries using vanilla's documented `ROOT=new controller`, `FROM=old controller`, `FROM.FROM=state` ordering; the active decision's physical `FROM` check then cancels/refunds on the surviving owner if its timer is reevaluated, but there is no engine proof of callback timing.

Do not add unconditional cleanup to the state-control hook, because an unrelated state change while the selected site remains valid would refund a still-valid transaction; an immediate hook would require a proven exact comparison of `FROM.FROM` to the stored receipt state.

Annexation or civil-war loss: the current on-actions omit construction cleanup and therefore leave the receipt orphaned; the required `FROM` cleanup hook fixes this without changing ordinary relationship cleanup.

Terminal: both Event 016 terminal paths call the shared cleanup helper, which refunds and clears the paid construction before retiring physical rows and closing generic transient project state; repeated terminal callbacks are idempotent.

Host-to-KRG formation: the former host cleanup settles any paid receipt before permanent rows move to KRG; KRG reconciliation counts only current valid facilities, and non-transferred historical rows do not become live until the receiving country actually controls a valid site.

### Active-site lifecycle and evidence limits

The physical-site invalidation helpers exist for an explicit destroyed or disarmed row, but repository search found no current Event 016 writer for a destruction/disarmament flag and no call site for `brilliant_scientist_singularity_site_invalidate_selected_state` or `...invalidate_selected_row`.

The current physical predicate already excludes captured or zero-level facilities, while reacquisition intentionally reactivates an intact historical row; a future explicit destruction consumer must wire the narrow invalidation helper rather than changing that capture/reacquisition rule.

No specific active-site lifecycle is otherwise unwired in the reviewed parent paths: construction completion/cancel, state-control reconciliation, split sovereignty migration, atomic old-host retirement, and terminal retirement are all present.

No MCP, map mutation, HOI4 process, live save, or log inspection was run in this postpatch review.

This review is source reasoning only and makes no engine acceptance claim.

Only this handoff was updated; no gameplay source, staging, or commit was performed.

## Parent resolution of review findings

The parent resolved the P1 annexation orphan by calling `brilliant_scientist_singularity_construction_cleanup` on `FROM` in both `on_annex` and `on_civil_war_end_before_annexation` before the former owner is discarded.

Both construction decisions cancel when their begin-time revalidation creates no private receipt, preventing an empty native timer from persisting after a failed start.

Both decisions now declare `ai_hint_pp_cost = 100`, matching the exact scripted PP debit without changing the existing score factors.

New role-specific `brilliant_scientist_singularity_site_needs_command_node` and `brilliant_scientist_singularity_site_needs_power_link` queries rebuild physical live quantities from aligned state rows and replace every legacy counter gate in target and visibility checks.

Arming, fail-deadly authorization, final commitment, and the Fallout handoff use `brilliant_scientist_singularity_site_has_minimum_live_network`; the duplicated legacy live-network flag gates were removed from those terminal paths.

The explicit destruction/disarmament invalidation helper remains a documented future consumer because the current package has no facility-destruction callback, while captured or zero-level facilities are excluded immediately by every live reconstruction and readiness query.

The weighted MCP postpatch pass preserved the frozen score pattern of 10 in peace, 20 in war, and zero while construction is pending. Formal source comparison remained blocked by the adapter's historical candidate binding, so this is scenario-linked postpatch evidence rather than a normalized probability or engine-execution claim.
