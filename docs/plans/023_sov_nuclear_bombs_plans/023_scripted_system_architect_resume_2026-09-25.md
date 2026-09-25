# Event 23 scripted-system architect handoff, 2026-09-25

Disposition: implemented for two bounded source defects. Event 23 as a whole remains under parent review, with native runtime and save/reload behavior unverified.

## Files and exact identifiers

- `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt`: `sov_nuclear_bombs_execute_shared_action` now sets `sov_nuclear_bombs_shared_accident_context` for the existing `sov_nuclear_bombs_action.accident` type. A test whose outcome is an accident already used that flag.
- `common/scripted_triggers/023_sov_nuclear_bombs_runtime_triggers.txt`: `sov_nuclear_bombs_native_delivery_country_is_valid` accepts an already pending native callback after shared Fallout or Final Silence activates. The new-request gate `sov_nuclear_bombs_action_context_is_valid` still rejects terminal states.
- This handoff is the only documentation file changed. No constants, event targets, decisions, events, localisation, assets, AI weights, or probability-bearing helpers changed.

## Helper and call-site map

| Existing helper or hook | Scope and inputs | Output and side effects | Direct call sites and disposition |
| --- | --- | --- | --- |
| `sov_nuclear_bombs_record_major_exchange_receipt` | SOV country, two candidate country IDs from a confirmed detonation | Persists first actor/target IDs, accepts only their reciprocal pair as the second receipt, sets answered/count flags, calls the one-shot presentation | `sov_nuclear_bombs_record_action_receipt` and both SOV owner/controller branches of `common/on_actions/023_sov_nuclear_bombs_on_actions.txt`. Reviewed, unchanged. |
| `sov_nuclear_bombs_event_major_exchange_receipt_gate` | SOV country, Evolution III, Chaos threshold, receipt count and answered flag | Read-only gate for `sov_nuclear_bombs_open_major_exchange` | `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt`, reviewed, unchanged. |
| `sov_nuclear_bombs_execute_shared_action` | Event 23 country action context, exact state, native stockpile and reserved device | Stages the shared profile flags and a single pending `launch_nuke`, or commits a non-detonating demolition | `sov_nuclear_bombs_begin_action` and the prepared-test completion in the event-effects file. Accident profile branch changed. |
| `sov_nuclear_bombs_native_delivery_country_is_valid` | Country with pending flag, reservation, nonce, weapon, route, exact state and target | Read-only callback gate before one-device commit | Exact-state `on_nuke_drop` Event 23 hook, `sov_nuclear_bombs_confirm_native_delivery`, and `sov_nuclear_bombs_commit_reserved_device`. Terminal-state check removed only here. |
| `chaos_meter_on_nuke_drop` and humanitarian `on_nuke_drop` | ROOT launcher and FROM struck state, Event 23 profile flags when present | Shared Chaos, deaths, contamination, condemnation, Fallout, famine and migration pressure | `common/on_actions/chaosx_on_actions_chaos_meter.txt` and `common/on_actions/humanitarian_runtime_on_actions.txt`. Reviewed, unchanged. |

## Receipt and consequence evidence

The first confirmed major receipt stores actor and target country IDs. The second receipt must reverse both IDs while the count is below `sov_nuclear_bombs_tuning.major_receipt_minimum`; duplicate, one-sided, and non-major callbacks cannot reach the answered flag through the reviewed call sites. The SOV strike callback obtains its target from the selected country and an exact state that passed the nuclear-major target check. The foreign strike hook requires a major launcher with nuclear technology and an exact state owned or controlled by SOV. The presentation gate reads the persisted receipt count and answered flag, with no `num_of_nukes` test. A last-bomb native stockpile snapshot can equal zero because `sov_nuclear_bombs_native_stockpile_delta_is_valid` compares the observed count with `before - one`. The one-shot super-event flag prevents duplicate publication.

The Event 23 adapter explicitly requests `nuke_type = nuclear_bomb` and sets `sov_nuclear_bombs_atomic_delivery_context` before native launch. Both thermonuclear branches in `chaos_meter_on_nuke_drop` and the condemnation multiplier exclude that context. Existing test, partial-yield, demonstration and test-accident flags select their shared profiles. The changed branch closes the remaining standalone accident-profile gap. Failed tests and demolition commit without a native detonation, so neither invokes a second shared consequence path. The Event 23 runtime helper contains no direct Chaos Meter or Fallout effect call.

## Constants, targets, cleanup and migration

The action IDs, `one`, receipt minimum, and native timeout already live in `common/script_constants/023_sov_nuclear_bombs_constants.txt`. No tuning table or new constant is needed. No call-site migration or new helper extraction is needed because the existing adapter is the single transaction boundary.

The action context uses scoped variables and flags, with no new event target. `sov_nuclear_bombs_clear_action_context` clears nonpending requests. The exact state-pending flag and nonce clear on confirmation or disputed timeout. `sov_nuclear_bombs_reconcile_unreturned_native_delivery` moves an unresolved reservation to missing once, and `sov_nuclear_bombs_cleanup_annexed_actor` uses that same disputed closeout if SOV disappears. Selected global event targets and stand-down pointers have explicit cleanup helpers. The Event 5 bridge retains its state snapshot and ownership reconciliation paths; this patch changes none of its ledgers.

## Validation and limits

Source review followed the launch, native callback, confirmation, receipt, shared consequence, humanitarian profile, timeout, annexation and terminal guards, including the two direct adapter call sites. The changed accident branch uses a preexisting shared flag consumed by Chaos Meter and humanitarian pressure and cleared after the native callback. The changed receipt validator remains restricted to a pending reservation, action nonce, supported native profile and exact state. `git diff --check` found no patch formatting error.

The read-only Event Chain Viewer trace for `chaosx.nr23.1` returned `EVENT_INSPECTED_PARTIAL` at source revision `cc097d15c00f15159a92e4fc4de590cfe2b67224170be81d9d17e55e0c16c587`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a3bcccbfb840b9c76b04729ef865d2fff368482b9a4e850b4e0d5c64eb219df6/8aee1c08bb9990b001fc6658b5d0cf3e1efb2c51286a6470819741bd03dc4191/event-trace-cc097d15c00f.json`. Its focused analysis indexed zero helpers and deferred lifecycle passes. The targets render likewise returned `EVENT_RENDERED_PARTIAL` with `selectedNodes = 0`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/09d5c59e6664cb13ffc7ec343f824866205341d8ea4af7917f2729f91f9475aa/395a2d2b5512e186871a782a6bd119e8b01ab1c87c63802fe282df85f5c9a3aa/event-targets-cc097d15c00f.json`. The installed `event_inspect` schema does not expose `helper_expansion`. These artifacts provide neither helper coverage nor post-change engine validation.

Meaningful runtime checks remain unresolved: reciprocal confirmed detonations with the answering major spending its last bomb, save/reload during a pending native delivery, timeout followed by a late callback, custody transfer while pending, and Fallout or Final Silence activation between launch and callback. The installed vanilla callback documents ROOT as launcher and FROM as struck state but does not echo Event 23's nonce or action type. Event 23 therefore relies on its one-pending-request, state nonce and stockpile-delta correlation. The order of separate `on_nuke_drop` blocks consuming and clearing profile flags also needs live evidence. No game session was launched by this subagent.
