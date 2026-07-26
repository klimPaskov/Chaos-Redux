# Event 006 DM-58 Exact Witness Resolver

Date: 2026-07-26.

Status: Narrow source-level implementation complete for the DM-58 witness-preserving execution tranche.

This handoff does not claim Event 006 completion.

## Scope and finding

The activation trigger already proved an existential three-member, three-distinct-owner contract, but the paid resolver selected a fresh random state for each member. A valid matching could therefore pass activation while greedy execution failed to stage the same contract.

The resolver now searches the frozen member ledger for one complete three-member, three-state, three-distinct-owner witness before applying any claim, state marker, wargoal, country flag, or material cost. The decision calls the resolver once at the activating country scope, and the cost effects remain after the count gate.

## Helper map

| Identifier | Scope | Inputs | Outputs | Side effects | Call site |
| --- | --- | --- | --- | --- | --- |
| `independence_wave_execute_reclamation_front` | Activating Event 006 country | `global.independence_wave_league_member_country_entries`; existing DM-58 constants and triggers | Exactly three aligned member, state, and owner array rows plus a zero or three count | Clears prior staging arrays and temporary search values, then performs a mutation-free nested witness search | `common/decisions/006_independence_wave_decisions.txt`, DM-58 `complete_effect` |
| `independence_wave_apply_reclamation_front_witness` | Activating Event 006 country and saved state/member targets | The three aligned arrays written by the resolver | State used markers, transaction-created claims, finite `take_state_focus` wargoals, staged and timed-ready country flags, count | Revalidates every row before mutation and sets claim and wargoal provenance receipts | Called once by `independence_wave_execute_reclamation_front` |
| `is_valid_independence_wave_reclamation_front_witness_slot` | State | Saved member and owner event targets | Boolean row-validity result | None | Called by `independence_wave_apply_reclamation_front_witness` |
| `independence_wave_rollback_reclamation_front_staging` | Activating Event 006 country | Aligned arrays and transaction receipts | Empty staging arrays and zero count | Removes only transaction-created claims and wargoals, clears used, staged, ready, and provenance flags | Existing DM-58 failure branch |

The planner uses three nested `for_each_scope_loop` blocks over the member ledger and three guarded `every_state` searches. The first complete witness appends exactly three rows to each array and raises the three break variables, so later scans do not mutate or append a second witness.

## Constants and tuning

No new constants were added. The resolver reuses `independence_wave_decision_gate.formation_member_minimum`, `independence_wave_value.minimum`, `independence_wave_plan.loop_increment`, and `independence_wave_decision_duration.reclamation_front` from the existing Event 006 constant files.

The three-slot search remains coupled to the accepted minimum of three members. If that contract changes, the trigger and effect must be expanded together rather than silently truncating or generalizing the witness.

## Event target and cleanup plan

The `independence_wave_reclamation_front_witness_member_one`, `..._member_two`, `..._member_three`, `..._state_one`, `..._state_two`, `..._state_three`, `..._owner_one`, `..._owner_two`, and `..._owner_three` targets are regular effect-chain targets used only while the planner runs. The generic `independence_wave_reclamation_front_member`, `..._target`, and `..._state` targets are also transient and are restored after nested probes before the containing state predicate is reused.

Persistent operation state is carried by the aligned global arrays, the count variable, state used markers, country staged and ready flags, and `independence_wave_dm58_reclamation_front_claim_added` and `independence_wave_dm58_reclamation_front_wargoal_added` state receipts. No global event target is introduced, so save and load do not depend on transient target names.

The existing shared `independence_wave_cleanup_reclamation_front_operation` now clears the wargoal provenance receipt with the other state receipts while intentionally leaving successful finite war goals to their existing explicit expiry. The pre-cost rollback clears the same receipts and removes only the effects marked as transaction-created.

## Migration from duplicated logic

The DM-58 decision no longer loops over every member and invokes the old random resolver. It clears stale state receipts once, calls the root planner once, gates payment on the resulting minimum count, and retains the existing success, failure, crisis, timeout, and league-delta branches.

The old per-member random-state selection, immediate array append, and unconditional rollback wargoal removal were removed from `independence_wave_execute_reclamation_front`. Existing shared cleanup and successful finite-wargoal expiry semantics remain unchanged.

## Files changed

- `common/scripted_triggers/006_independence_wave_decision_triggers.txt`
- `common/scripted_effects/006_independence_wave_decision_effects.txt`
- `common/decisions/006_independence_wave_decisions.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `docs/events/006_independence_wave/reclamation_front_lifecycle.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_dm58_witness_resolver_2026_07_26.md`

The lifecycle document is the matching helper documentation surface because the repository has no dedicated markdown file for `006_independence_wave_decision_effects.txt`.

## Validation evidence

- Ran a source brace, quote, and unsupported-operator scan over the four touched Clausewitz files. Each file reported zero brace imbalance, no open quote, and no unsupported `<=` or `>=` operator.
- Ran `git diff --check` over the five source and lifecycle paths. No whitespace errors were reported.
- Ran a focused source-contract audit that confirmed one root resolver call, no `random_state` in the DM-58 resolver, exactly three member rows, exactly three state rows, exactly three owner rows, count mutation only in the apply helper, and the complete wargoal-receipt lifecycle.
- Ran `python .tools\\audit_event6_allocator.py`; the Event 006 allocator audit passed with publishers `149`, automatic or high-chaos selectable packages `126`, and SCN-008 ranked selectable packages `138`.
- Read the offline effects, triggers, scopes, and data-structure references and the vanilla effects, triggers, script-concept, and script-constant documentation for `every_state`, `for_each_scope_loop`, `while_loop_effect`, arrays, event targets, and meta effects.

## Skipped meaningful validation

No live HOI4 run, save/load scenario, or in-game AI observation was performed because live consumer validation belongs to the user and agents must not launch the game.

No GUI, map, focus, or event-render inspection was needed because this tranche changes only DM-58 decision execution and its shared cleanup receipt.

## Risks and limitations

The effect-side search is deterministic and consumes the first complete witness in ledger order, but a no-witness case can scan every state for each nested member tuple. The offline documentation confirms the loop and array primitives, but no live engine parser or runtime performance proof was available.

The state-slot revalidation uses the existing `can_declare_war_on`, current-owner, controller, claim-or-border, current-war, and same-type finite-wargoal guards. `remove_wargoal` remains type-and-target based, so the new state receipt is required to avoid removing an unrelated matching wargoal during rollback.

Successful finite war goals remain subject to the existing 365-day expiry policy after shared cleanup. This tranche does not add a new cancellation-specific wargoal removal path.

No fallback, generic target, unconditional war, or mechanic simplification was introduced.

## Follow-up

The parent should review the static scope assumptions around nested `every_state` and saved event targets, then obtain live scenarios for three distinct owners, an only-two-owner collision, post-activation target invalidation, timeout, save/load persistence, and low-resource AI behavior before making an Event 006 completion claim.
