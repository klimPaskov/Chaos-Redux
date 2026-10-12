# Random Terror callback helpers

The incident, response, actor and terminal systems are described in [the event overview](../../docs/events/031_random_terror/overview.md).
These contracts cover the global callback recovery helpers in `031_random_terror_effects.txt`.

## `random_terror_reconcile_pending_callbacks`

Purpose: deliver overdue global callbacks when a delayed event's original recipient has ceased to exist and its native delayed-event clock has paused.
Scope: country, called by the existing single global-host coordinator after `global.date` is current.
Inputs: the existing dispatch, evolution, revelation candidate and terminal commit pending flags, their absolute due dates, and their original country targets.
Outputs: an immediate `chaosx.nr31.99`, `.92`, `.94` or `.95` on the corresponding absent original country, only when its current deadline has arrived.
Defaults: no pending receipt, missing deadline or missing country target produces no callback.
Side effects: no direct changes to pressure, activity, MTTH, candidate weights, history, victim selection or terminal outcome rules.
The receiving event validates the current pending receipt, native earliest-date bound and exact recipient, then the existing processor consumes it.
Recovery requires the original recipient to be absent, so a living recipient retains its native callback timing and ordering.
An immediate effect-fired event can run on an absent country, while a delayed event waits for that country's return.
Callbacks before the replacement timer's earliest native window and callbacks without a current pending receipt fail their event trigger, and a callback on an old recipient cannot consume a replacement recipient's clock.
An old callback on the same recipient after the current timer reaches that window is indistinguishable from valid delivery, so this contract does not claim immutable event-instance generation receipts.
Evolution processing also retains its existing candidate-stage and predecessor-stage checks.
When the final command has ceased to exist, the helper calls the existing defeat check because its terminal strength pulse has also stopped.
The exact unresolved-network predicate still prevents defeat while another actor, active cell or affected-country pressure survives.

The call belongs once in each of the existing global-host coordinator branches of `common/on_actions/chaosx_on_actions_chaos_meter.txt`.
It introduces no independent periodic hook or country effect iteration.

```text
random_terror_reconcile_pending_callbacks = yes
```

## `random_terror_get_callback_earliest_due`

Purpose: calculate the earliest plausible native callback date without changing the actual scheduled delay.
Scope: any.
Inputs: caller-owned temporary `random_terror_callback_delay_days`, the original positive MTTH delay.
Output: caller-owned temporary `random_terror_callback_earliest_due_date`, declared by the caller before the helper runs.
Defaults: none, each scheduler provides its delay and creates the output.
Side effects: temporary arithmetic scratch only.
The helper removes the fractional day through modulo-one arithmetic, converts the whole-day lower bound with the existing shared date helper and adds the result to `global.date`.
The evolution and revelation schedulers store that lower bound separately from their canonical ceil-hour recovery deadlines.
The native callback guard therefore admits whole-day truncation, fractional-hour delivery or rounding, while the absent-host coordinator waits for the canonical deadline.
The actual `country_event` delay and every MTTH modifier stay unchanged.

```text
set_temp_variable = { random_terror_callback_delay_days = random_terror_evolution_delay_days }
set_temp_variable = { random_terror_callback_earliest_due_date = global.date }
random_terror_get_callback_earliest_due = yes
```

## `random_terror_schedule_revelation_commit`

Purpose: enqueue the False Revelation's initial commit or Chaos-low recheck and retain an absolute recovery deadline for that same enqueue.
Scope: any scope with `random_terror_final_actor` available as the global country target.
Input: caller-owned temporary `random_terror_world_end_delay`, computed from the existing initial or recheck tuning before the call.
Output: `global.random_terror_revelation_commit_due_date`, calculated with the shared calendar conversion helper, and the existing delayed `.95` event on the final command.
Defaults: none, both callers supply the existing delay and final-command target.
Side effects: only the deadline receipt and native event enqueue.
The finalizer consumes the deadline before checking the current commit gates.
A Chaos-low recheck installs its own deadline through the same helper.
Withdrawal, commit and defeat cleanup remove the receipt.

Call sites: `random_terror_promote_final_command` and the Chaos-low branch of `random_terror_finalize_false_revelation`.

```text
set_temp_variable = { random_terror_world_end_delay = constant:random_terror_tuning.world_end_delay_days }
random_terror_schedule_revelation_commit = yes
```

## Scope targets and cleanup

`random_terror_dispatch_host` remains the original wave dispatcher and is cleared with its dispatch deadline when `.99` settles.
`random_terror_evolution_clock_host` is saved when an evolution candidate is queued and cleared before processing can schedule its successor.
`random_terror_revelation_clock_host` is saved when a revelation candidate is queued, replaced with the actor receiving an authorized accelerated callback, and cleared on candidate processing, invalidation or repeatable-cycle reset.
The terminal commit retains the existing `random_terror_final_actor` pointer and does not replace it with the coordinator or another country.
No victim, actor-parent or state authority target is changed by callback recovery.

`random_terror_refresh_priority_state` declares its temporary selected-state output before calling `random_terror_consider_priority_state`.
The selector still ranks controlled active states and occupied active cores by stage, then activity, keeps the first exact tie, and uses its existing recovery fallback when there is no active state.

## References and verification

Offline `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`, line 35, documents immediate effect-fired events on absent countries and paused delayed-event clocks.
Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, lines 435-443, documents unscoped temporary storage and declaring a returned temporary before calling its scripted helper.
Installed `documentation/effects_documentation.md`, lines 2943-2967 and 7820-7827, defines country-event dispatch and `set_temp_variable`.
The task's exact source revisions, scenarios and validation limits are recorded in [the C5 handoff](../../docs/plans/031_random_terror_plans/subagent_handoffs/c5_bug_fix_2026-10-13.md).
