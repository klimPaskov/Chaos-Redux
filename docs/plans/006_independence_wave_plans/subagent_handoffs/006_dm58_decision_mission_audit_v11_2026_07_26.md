# Event 006 DM-58 Decision and Mission Audit v11

Date: 2026-07-26.

Audited commit: `0b6289c4bbc557a61e4706d9c9a66bd0befb7a6e` (`fix(event006): bind DM-58 witness before cost`).

Status: **PARTIAL**.

Scope: read-only audit of `independence_wave_coordinate_reclamation_fronts` (DM-58), its exact-witness resolver, mutation-time revalidation, rollback, lifecycle hooks, costs, AI, and player-facing text.

No gameplay, GUI, or localisation source was edited.

The current `HEAD` differs from the audited commit only in Event 006 documentation, and the four DM-58 gameplay files are byte-identical between the two revisions.

## Overall disposition

The core DM-58 correction passes source review.

The activation preflight proves an exact three-member, three-state, three-distinct-owner witness before the mission can be selected.

The `complete_effect` calls `independence_wave_execute_reclamation_front` once, applies the selected witness only after live-state revalidation, checks the resulting count, and only then calls `independence_wave_decision_pay_strategic` and `independence_wave_decision_pay_security_major`.

If the witness disappears before application, the partial claims, finite wargoals, staging flags, aligned arrays, and count are rolled back before those material costs run.

The remaining PARTIAL result is driven by an unhandled natural-expiry cleanup path and an unresolved source-level performance risk, not by a witness-before-cost failure.

## Issue list, sorted by severity

### High: Natural expiry has no shared-operation cleanup hook

`independence_wave_reclamation_fronts_coordinated` is a 365-day global flag set by DM-58, but its only source readers are the decision guard, the mission cancellation trigger, and the member-count revalidator.

No source path invokes `independence_wave_cleanup_reclamation_front_operation` when that timed global flag naturally expires.

The three global witness arrays, `global.independence_wave_reclamation_front_count`, and the state receipt flags therefore remain after the active window ends unless a league phase transition, origin reset, dissolution, or member-count failure happens first.

This is not an immediate cost or rollback exploit because the next DM-58 `complete_effect` clears the old arrays and receipts before it searches again, and the successful finite wargoals and readiness flags use the same 365-day duration.

It is nevertheless a real lifecycle and save/load observability gap, since an expired operation is still represented by persistent reservations and receipts in a save until another unrelated lifecycle path happens.

Recommended fix: route the expiry through an existing Event 006 runtime cadence or explicit operation-expiry handler that calls `independence_wave_cleanup_reclamation_front_operation` exactly once after the coordination flag ends, without adding a global `on_daily` loop.

Affected identifiers: `independence_wave_reclamation_fronts_coordinated`, `independence_wave_cleanup_reclamation_front_operation`, `independence_wave_revalidate_reclamation_front_operation` in [006_independence_wave_effects.txt](../../../../common/scripted_effects/006_independence_wave_effects.txt).

### Medium: Exact-witness search can be expensive in a rare valid activation

The preflight uses nested `any_of_scopes` and `any_state`, while the paid resolver uses three nested `for_each_scope_loop` blocks and three nested `every_state` scans.

The operation is bounded by the small league ledger and runs only after the radical high-chaos gates pass, but `every_state` has no direct early-break field.

Once a witness is found, the completion and loop-break variables stop new mutation and outer member loops, while the currently-entered `every_state` scans still enumerate their remaining world states with a failed limit.

The no-witness case is normally rejected during activation, but the same broad existential search is itself evaluated daily for eligible high-chaos carriers.

Recommended follow-up: profile the three-owner and near-miss cases in a live campaign before accepting this as final, and only replace the world-state scans if an existing bounded state-pool helper can preserve the exact member, owner, claim-or-border, controller, and war-legality contract.

Affected identifiers: `has_independence_wave_reclamation_front_preflight`, `independence_wave_execute_reclamation_front`, `is_valid_independence_wave_reclamation_front_state`.

### Low: Cost presentation is accurate but not compact or icon-first

The custom cost text correctly names the paid stability, war-support, command-power, convoy-or-train, manpower, army-XP, infantry-equipment, and support-equipment package.

It is a long sentence without the short icon-first presentation required by the decision skill, so the actual requirement is harder to scan in a dense category.

The source does not expose raw triggers, and the separate preflight tooltip clearly states the three-member and three-owner requirement.

Recommended follow-up: retain the current values and payment behavior, but convert `independence_wave_cost_reclamation_front`, `_blocked`, and `_tooltip` to a compact icon-first summary with the full detail retained in the tooltip.

Affected keys: `independence_wave_cost_reclamation_front`, `independence_wave_cost_reclamation_front_blocked`, `independence_wave_cost_reclamation_front_tooltip` in [006_independence_wave_decisions_l_english.yml](../../../../localisation/english/006_independence_wave_decisions_l_english.yml).

## Decision category lifecycle notes

| Stage | Source behavior | Audit disposition |
| --- | --- | --- |
| Category reveal | `independence_wave_high_chaos_category` requires a regional power with the high-chaos unlock. DM-58 adds radical-sovereignty and open-evolution gates. | Pass |
| Mission activation | The daily activation gate requires an active, compliant radical league member, no crisis or existing operation, the authorizing focus, reserve threshold, and exact preflight witness. | Pass |
| Selection | `selectable_mission = yes` means selection immediately runs `complete_effect`; the 180-day mission timer is a deadline to select, not a 365-day implementation delay. | Pass |
| Success | Resolver freezes and applies exactly three aligned rows, charges costs only after count reaches three, gives finite wargoals and a 365-day operation window, then the coordinated flag cancels the selected mission. | Pass |
| Pre-cost failure | A missing or invalid mutation-time row produces fewer than three successes, invokes provenance-aware rollback, sets the failure flag, applies failure deltas, and opens league crisis. | Pass |
| Timeout without selection | `timeout_effect` sets the failure flag, applies major-loss deltas, and opens crisis. No targets, claims, wargoals, or material costs exist at this point. | Pass |
| Cancellation before selection | The `cancel_trigger` has no `cancel_effect`, which is safe because no resolver, cost, claim, or wargoal has run. | Pass |
| Cancellation after success | The coordinated flag intentionally makes `cancel_trigger` true after the successful transaction. No cancellation rollback is appropriate because the fronts are the intended persistent result. | Pass, subject to expiry gap |
| Invalidation and reset | Member exit invokes `independence_wave_revalidate_reclamation_front_operation`; phase transitions and generation reset invoke shared cleanup. Natural timed expiry does not. | Partial |
| Save/load | Persistent global arrays and receipts carry active state. Resolver event targets are regular effect-chain targets only and are not relied on after return. No save/load consumer test was run. | Source pass, runtime unresolved |

## Mission quality notes

| Mission | Owner | Category | Region | Requirement | Duration | Success | Failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `independence_wave_coordinate_reclamation_fronts` | Active Event 006 radical league member | `independence_wave_high_chaos_category` | Dynamic league frontier, one distinct external owner per member | Focus authorization, high-chaos route, reserve, exact three-member and three-owner legal witness, material cost | 180-day selection deadline, then 365-day finite fronts | Three claim-connected or border-connected finite fronts, finite `take_state_focus` wargoals, league milestone and deltas | Unselected timeout or pre-cost witness loss creates league crisis and failure deltas | Low, as this is the sole DM-58 synchronized-front mission |

This is an action-based mission rather than a passive store button.

The unique-owner requirement, war legality, live controller, claim-or-border test, and finite-wargoal guard make its objective meaningful and prevent the old greedy target mismatch.

## Cost and requirement clarity notes

The cost source is centralized in `independence_wave_decision_cost` and is not a flat political-power purchase.

The availability and custom-cost checks require the strategic package, the major security package, and shared reserve before selection.

The actual custom cost has no engine deduction, as documented by the offline Decision modding reference, so the explicit payment effects are correctly required in `complete_effect`.

The resolver and count gate precede those payment effects at decision lines 3587 and 3599 respectively.

The diplomatic component selects convoy payment when available and otherwise train payment, while the cost trigger requires at least one of those two resources.

No material refund is needed on cancellation or timeout because neither path can run the resolver or payment effects before selection.

## AI validity and route-lock notes

DM-58 has one `ai_will_do` score, `base = constant:independence_wave_decision_ai.high` (25).

AI selection remains gated by the same activation and availability requirements as the player, including the exact non-mutating witness, resource package, reserve, compliant membership, radical route, and crisis lock.

The decision has no country target selector, so an AI cannot choose a dead or closed target directly.

The resolver rejects dead owners, current wars, league members, client-locked members, prior finite wargoals, and owner collisions before it can produce the count that unlocks payment.

`hoi4.probability_inspect` recorded one complete candidate for the current source, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/52c889cb0759d4dfe227fa5c89c4200324bd3fa59bcffb7ff6a9b0e8e9e1904d/8e4a486f9b2013cd1474924c7c83b1d89f2ed56594ab5c8f86ce4a3fb4536dc2/probability-inspect-dc29bd4fdb4d.json`.

The blank-state MCP evaluation was intentionally reported as partial with nine unresolved campaign inputs, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1e2681a4c9c19de82dd6209deaf746bac104b3780aab5fae8b71da3b4c86359c/84a6dc2a4fb42fdc423856446f8465dca4e509bad7ece7bb56958aef9c947c19/probability-057d594c29f63b5cbe625017.json`.

That result is not a click probability and does not establish whether score 25 is the desired campaign-level AI priority.

## Localisation and tooltip gaps

The decision title, description, preflight, success, pre-cost failure, timeout, cost, blocked-cost, and cost-tooltip keys all exist.

The current description accurately explains that three compliant members must reach three external powers before material costs are paid.

No cancellation-specific tooltip exists because cancellation is neutral before selection and a successful selection deliberately uses the coordinated flag to end the mission row.

The only player-facing gap found is the compact cost presentation noted above.

## Cleanup and exploit-risk notes

The resolver contains no `random_state` selection and writes three member, state, and owner arrays only after the full witness is found.

`independence_wave_apply_reclamation_front_witness` revalidates each aligned row before setting receipts or applying a claim and finite wargoal.

`independence_wave_rollback_reclamation_front_staging` removes only transaction-marked claims and finite wargoals, avoiding removal of an unrelated claim or matching wargoal.

There is no free unit, equipment, claim, core, or war-goal loop in the audited selection path.

The repeat gate is both `fire_only_once = yes` and root-specific complete or failed flags, while the global coordinated flag prevents simultaneous league operations.

The natural-expiry receipt issue remains the one cleanup risk that must be addressed before a full completion claim.

## Meaningful validation performed

- Verified commit identity and that the DM-58 gameplay sources are identical between `0b6289c4b` and current `HEAD`, whose subsequent changes are documentation-only.
- Ran a focused source-contract check against the audited commit: one root resolver call, zero `random_state` uses in the resolver, three member rows, three state rows, three owner rows, one mutation-time witness validator, one rollback call, and the strategic payment after the resolver and count gate.
- Traced source references for the coordinated flag, all state receipts, shared cleanup, revalidation, origin reset, member exit, timeout, and cancellation.
- Read the required offline Decision, Effects, Triggers, Scopes, Data structures, Modifiers, Localisation, On actions, Event modding, Idea modding, and AI modding pages, plus vanilla decision documentation, effects and trigger documentation, script constants documentation, and vanilla decision precedents.
- Inspected vanilla documentation for mission selection semantics, custom-cost behavior, `for_each_scope_loop`, `while_loop_effect`, `every_state`, active-mission cleanup, global event-target lifetime, and targeted-decision performance boundaries.

## Skipped meaningful validation and why

- No live HOI4 scenario was run. Repository policy assigns live consumer validation to the user.
- No save/load execution, target-capture, owner-change, or mid-operation member-exit runtime scenario was available to prove the persistent-array behavior.
- No measured performance trace exists for the nested world-state scans.
- No decision-owned scripted GUI surface exists for DM-58, so `hoi4.gui_inspect` and `hoi4.gui_render` were not applicable.

## Concrete follow-up for the parent

1. Resolve the natural 365-day expiry cleanup gap through an existing Event 006 lifecycle hook, without introducing a broad `on_daily` iteration.

2. Obtain live validation for a valid three-owner witness, a two-owner collision, mutation-time owner or controller invalidation, unselected timeout, cancellation before selection, member exit below minimum, natural operation expiry, and save/load while fronts are active.

3. Measure the near-miss preflight and successful witness resolver before deciding whether the exact search needs a bounded existing state pool.

4. Optionally tighten the cost localisation to the repository's icon-first standard after gameplay lifecycle correctness is settled.

## Files reviewed

- `common/decisions/006_independence_wave_decisions.txt`
- `common/scripted_triggers/006_independence_wave_decision_triggers.txt`
- `common/scripted_effects/006_independence_wave_decision_effects.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/script_constants/006_independence_wave_decision_constants.txt`
- `localisation/english/006_independence_wave_decisions_l_english.yml`
- `docs/events/006_independence_wave/reclamation_front_lifecycle.md`

## Changed files

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_dm58_decision_mission_audit_v11_2026_07_26.md`

No gameplay, localisation, scripted GUI, or asset files were changed.
