# Event 020 RTX terminal-operation audit handoff

## Scope and result

This pass audited `black_plague_rat_king_close_the_harbors` and `black_plague_rat_king_silence_the_capitals`, their direct state-target triggers, and their terminal-operation effects.

Both operations remain state-targeted decisions in `black_plague_rat_king_court_category` and use no new tag, model, category, mission, or scripted GUI.

## Patch applied

| File | Identifiers | Before | After |
| --- | --- | --- | --- |
| `common/decisions/020_black_plague_rat_decisions.txt` | `black_plague_rat_king_close_the_harbors`, `black_plague_rat_king_silence_the_capitals` | `complete_effect` both paid costs and immediately applied their terminal state result, while `days_remove` only held the factory modifier. Cancellation had no effect. | `complete_effect` starts and pays the operation, `remove_effect` resolves its result after the 60-day timer, and `cancel_effect` clears its reservation and emits the existing invalidation report. |
| `common/scripted_triggers/020_black_plague_rat_triggers.txt` | `black_plague_rat_king_terminal_campaign_country_can_continue`, `black_plague_rat_king_terminal_campaign_country_is_ready` | One readiness trigger was also used during cancellation, but it would need active-operation flags to block parallel decisions. | Continuation checks the live route, war, target-continent, and terminal-state contract, while readiness adds the no-active-operation checks used only before commitment. |
| `common/scripted_effects/020_black_plague_rat_effects.txt` | `black_plague_rat_king_start_terminal_harbor_campaign`, `black_plague_rat_king_complete_terminal_harbor_campaign`, `black_plague_rat_king_cancel_terminal_harbor_campaign`, `black_plague_rat_king_start_terminal_capital_campaign`, `black_plague_rat_king_complete_terminal_capital_campaign`, `black_plague_rat_king_cancel_terminal_capital_campaign` | Completion helpers mixed payment, immediate success, and failure reporting. The declared active flags were never written and division-cap expenditure did not refresh the current cap. | Start helpers debit all declared reserves, refresh the division cap, and set global operation plus operation-specific active flags. Completion helpers resolve only a still-valid timer, clamp terminal preparation, clear flags, and report success. Cancellation clears flags and fires `chaosx.nr20.85` or `chaosx.nr20.86` outside world-end cleanup. |

## Issue list sorted by severity

1. Resolved high — Both operations stated that their results occur after 60 days, but the results occurred immediately when the decision was selected because `complete_effect` runs on selection.

2. Resolved high — Both operations had `cancel_trigger` without `cancel_effect`, so a lost target, war, or route silently ended the timer and did not emit the documented failure reports.

3. Resolved medium — The existing readiness trigger checked three active-operation flags that were never set, so the terminal-operation reservation did not actually prevent a parallel harbor or capital operation.

4. Resolved medium — Military allocation debited `black_plague_rat_division_cap_bonus` without refreshing `black_plague_rat_division_cap`, leaving the effective force ceiling stale until a later Rat runtime refresh.

## State target, route, cost, and AI notes

Both operations use the documented `state_target = any` selector, and `FROM` is consistently the selected state.

Harbor targets must be selected-continent, coastal, port-bearing, exposure-eligible states controlled by a live human enemy at war with RTX and not rat-controlled.

Capital targets use the same contract plus the existing designated-capital marker.

The start helpers charge Dominion, Brood Mass, and military allocation immediately after the matching affordability checks and reserve the decision's civilian factory for the full 60-day timer.

The committed resources are intentionally not refunded on invalidation, while the active flags and the selected operation's reservation are always cleared.

State cooldowns prevent immediate retargeting after success, and the country reservation prevents the two operation types from running in parallel.

AI weights remain `high` for Harbor and `maximum` for Capital.
Every legal AI target must pass the same human-enemy, live-war, selected-continent, route, and state-cooldown gates as a player target.

## Cleanup, localisation, and mission notes

The continuation gate closes an active operation if RTX loses its king status, the Evolution V route, its completed route, its selected continent, its war, or enters terminal/world-end state.

The cancellation helpers clear both active flags before firing the existing invalidation reports, and world-end cleanup remains report-free.

Existing localisation already describes delayed completion, exact dynamic costs, targeted geography, and invalidation behavior, so no player-facing localisation key changed.

These two operations are timed decisions, not missions; no mission lifecycle was added or changed.

No decision-owned scripted GUI exists in this scope, so no GUI inspection artifact or unresolved GUI fidelity finding applies.

## Meaningful validation

Consulted the offline Decision Modding reference and the vanilla timed-decision precedents before patching.
The reference confirms that `complete_effect` fires when a decision is selected, `remove_effect` fires when `days_remove` expires, and `cancel_effect` is required for cancellation cleanup.

Confirmed both operation definitions use `state_target = any`, dedicated target triggers, a start helper, expiry helper, cancellation helper, active flags, and their existing success or failure report IDs.

Confirmed readiness uses no-active-operation checks while active-timer cancellation uses the separate continuation check, preventing self-cancellation as soon as the reservation is written.

No weighted-logic simulation was run because no AI factor or custom random pool changed.

No Hearts of Iron IV session was launched, in accordance with repository policy.

## Remaining risks

No local defect remains in the audited target, cost, timer, cancellation, cleanup, or AI-validity paths.

No plan handoff was written because the repaired behavior implements the existing Event 020 route contract rather than changing its design.

No simplification was made.
