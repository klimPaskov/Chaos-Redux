# Event 006 overlay-watch permanent-identity-loss re-audit

Date: 2026-08-03.

Scope: read-only decision and mission re-audit of the parent bounded-lifecycle repair for IW-022 Dalmatia, IW-025 Vojvodina, and IW-035 Livonia.

Disposition: SOURCE PASS with one P3 cleanup residue and one runtime-evidence boundary.

The obsolete pasted flag log was excluded and was not used as evidence.

No gameplay, localisation, GUI, asset, focus, spreadsheet, or event file was changed by this audit.

## Reviewed parent patch

The repair changes the three package duration-constant files, trigger files, and scripted-effect files listed in `006_overlay_watch_permanent_identity_loss_cleanup_2026_08_03.md`.

Each package defines `watch_suspension_grace_days = 30` beside the existing `watch_mission_timeout = 135` and `watch_pause_daily_extension = 1` values.

Each exact route trigger now also rejects its own permanent-loss country flag.

The patch also replaces the three `divisions_in_state.size` script-constant tokens with file-scoped `@CR_SC_...GUARD_DIVISION_SIZE_EXCLUSIVE = 0` values that exactly mirror the pre-existing authoritative zero-valued script constant.

This is a parser-compatible injection for the known non-dynamic field and does not change the one-or-more-division garrison requirement.

## Issues sorted by severity

### P3 — permanent cleanup retains the hold-progress variable

Affected identifiers are `independence_wave_iw022_dalmatia_cancel_watch_permanent_identity_loss`, `independence_wave_iw025_vojvodina_cancel_watch_permanent_identity_loss`, and `independence_wave_iw035_livonia_cancel_watch_permanent_identity_loss`.

The terminal helper removes the active mission, clears its suspension counter and all runtime overlay flags, and blocks route resumption, but it does not reset `*_watch_hold_days`.

The residue is inert because the mission is gone and `*_permanent_identity_loss` makes every route-active and overlay-active trigger false.

It is nevertheless stale per-mission state and differs from ordinary watch failure, which resets the same variable to the package minimum.

Recommended local follow-up: before the terminal helper returns, add `set_variable = { <package>_watch_hold_days = constant:<package>_value.minimum }` to each of the three helpers.

### P3 — exact mission-timeout ordering is not source-provable

The first suspended daily hook extends the active mission before it increments the suspension counter, and the 30th counted hook extends then removes it.

This is source-correct under the documented contract and uses vanilla-supported `add_days_mission_timeout` and `remove_mission` effects.

The exact engine order between daily on-action execution and an expiring mission's timeout remains a live-engine and save/load validation question, particularly if identity loss is first observed with only one timeout day remaining.

No live, save/load, or UI claim is made by this audit.

No P1 or P2 source defect was found.

## Decision-category lifecycle notes

Every ordinary action and active watch mission is visible only through its package's `is_independence_wave_iwNNN_<route>_overlay_active` trigger.

That trigger composes the exact carrier identity and the new permanent-loss gate, so permanent cleanup makes the whole decision surface unavailable without leaving a route-visible action or restart path.

Before the threshold, the route-active trigger remains true as soon as the exact identity returns, `resume_overlay` restores the overlay flags and ideas, resets the suspension counter to zero, and the next active refresh clears `*_watch_interrupted` when the named mission is still active.

After the threshold, the permanent-loss flag prevents both initialization and resumption even if the former carrier later recovers the cosmetic identity.

The paid start decision remains non-repeatable while `*_watch_running`, `*_watch_interrupted`, or `*_watch_completed` is set, and permanent cleanup removes the active mission before clearing `*_watch_running`.

## Mission quality notes

| Owner and category | Mission and region | Requirement and duration | Success, failure, and duplicate risk |
| --- | --- | --- | --- |
| CRO-origin dynamic Dalmatia, `independence_wave_iw022_dalmatia_category` | `independence_wave_iw022_hold_adriatic_watch`; Dalmatian anchor and Zara route context | Existing paid coastwatch prerequisite, active exact-overlay gate, 45 hold progress, 135-day base timeout, then one added timeout day per suspended hook for at most 30 counted hooks | Existing success and ordinary timeout failure stay unchanged; permanent loss removes the mission without timeout effects; duplicate activation remains blocked by the running/interrupted/completed flags. |
| HUN-origin dynamic Vojvodina, `independence_wave_iw025_vojvodina_category` | `independence_wave_iw025_hold_vojvodina_border_watch`; state 45 border anchor | Existing paid reserve prerequisite, active exact-overlay gate, 45 hold progress, 135-day base timeout, then the same bounded one-day suspension extension | Existing success and ordinary timeout failure stay unchanged; permanent cancellation removes the sole named mission and blocks restart. |
| LIT Livonia cosmetic carrier, `independence_wave_iw035_livonia_category` | `independence_wave_iw035_hold_livonian_corridor_watch`; Baltic anchor states 12 and 191 | Existing paid coastal-watch prerequisite, active exact-overlay gate, 45 hold progress, 135-day base timeout, then the same bounded one-day suspension extension | Existing success and ordinary timeout failure stay unchanged; permanent cancellation removes the sole named mission and blocks restart. |

## Cost and requirement clarity

The patch does not alter the paid mobilisation costs, garrison requirements, target validity, or ordinary success and failure effects.

The new terminal path adds no refund, equipment, manpower, unit, core, claim, or war-goal effect.

The replaced garrison threshold remains strict `size > 0`, so it still requires at least one division in the required state or valid stated alternative.

## AI validity and route-lock notes

No new AI target selection or weight is introduced.

Existing AI mobilisation can only reach the watch while the exact route is active and the normal action prerequisites are met.

The permanent-loss gate is package-local and is present in each package's exact route trigger, so no dead, transformed, or reverted carrier can resume the prior watch after its grace window is exhausted.

The three terminal helpers only remove their own named mission and package ideas, then clear the shared overlay-active flag that their package itself owns.

## Localisation and tooltip gaps

No new player-facing decision, mission, or tooltip identifier is introduced by the repair, so no localisation key is missing from the changed surface.

The terminal cleanup is a background identity-loss consequence and removes the exact-overlay decision category with the mission, rather than exposing a stale mission with an unavailable trigger.

If a later UX pass wants an explicit player notice for terminal identity loss, it needs an approved event or notification design rather than a fabricated fallback tooltip in this lifecycle helper.

## Cleanup and exploit-risk notes

The fixed terminal path clears the active mission, runtime running/interrupted/active/suspended/shared-overlay flags, package ideas, and the suspension counter before route lockout.

The `has_active_mission` condition around `remove_mission` prevents repeat removal, and the pause guard requires suspended, interrupted, running, and active mission state, preventing post-cancellation counter growth or timeout farming.

The permanent route gate eliminates reactivation and repeat paid-watch rewards after the terminal cleanup.

The remaining `*_watch_hold_days` residue is not exploitable but should be normalized as the P3 cleanup follow-up above.

## Static validation

The targeted three-route contract check passed eight assertions per package: 30-day constant, one-day pause increment, permanent route gate, start reset, timeout extension and counter increment, exact mission removal, terminal runtime cleanup, and resume reset.

The touched source files have balanced braces, and `git diff --check` reported no diff errors for the nine parent-patched files.

`python -B .tools/audit_event6_allocator.py` also passed on the current worktree, but it is allocator coverage rather than a mission-engine parser.

The vanilla effect documentation was consulted for `activate_mission`, `add_days_mission_timeout`, `has_active_mission`, and `remove_mission`; the latter confirms terminal removal does not execute mission completion or timeout effects.

Meaningful validation not run: no game launch, live game, save/load, or runtime UI validation was run because that evidence is outside this audit scope and belongs to the user.

## Changed files and handoff

Changed by this subagent: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_overlay_watch_permanent_identity_loss_reaudit_2026_08_03.md` only.

Reviewed gameplay identifiers are `independence_wave_iw022_dalmatia_cancel_watch_permanent_identity_loss`, `independence_wave_iw025_vojvodina_cancel_watch_permanent_identity_loss`, `independence_wave_iw035_livonia_cancel_watch_permanent_identity_loss`, `independence_wave_iw022_hold_adriatic_watch`, `independence_wave_iw025_hold_vojvodina_border_watch`, and `independence_wave_iw035_hold_livonian_corridor_watch`.

No additional plan handoff is required because the only source finding is a three-line local cleanup follow-up.
