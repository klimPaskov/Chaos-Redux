# Event 006 DM-58 participant invalidation repair

Date: 2026-07-28.

Scope: narrow scripted-system repair for the P2 lifecycle gap identified by `006_decision_mission_reaudit_2026_07_28.md`. No staged or committed files were created by this subagent.

## Policy

DM-58 uses a strict shared-operation cancellation policy. If a country leaving the league is still present in the frozen `global.independence_wave_reclamation_front_members` witness array while `independence_wave_reclamation_fronts_coordinated` is active, the entire operation is cleaned up. This includes a non-coordinator participant. The existing league-minimum guard remains unchanged.

This policy clears stale member, state, and owner rows before the scheduled expiry callback can consume them. It does not create replacement or fallback targets. It does not remove already-issued finite `take_state_focus` war goals. Those war goals retain their existing timed expiry. The coordinator and normal league lifecycle remain intact because the coordinator-origin cleanup path still runs before coordinator unregister, and the new member-array guard is evaluated only from the existing unregister/revalidation call path.

## Files and identifiers

- `common/scripted_effects/006_independence_wave_effects.txt`
  - `independence_wave_revalidate_reclamation_front_operation` now enters the shared `independence_wave_cleanup_reclamation_front_operation` path when the current scope is in `global.independence_wave_reclamation_front_members`, in addition to the existing league-minimum failure condition.
  - The cleanup comment now records participant-exit invalidation and preserves the finite-war-goal expiry rule.
- `common/scripted_effects/006_independence_wave_effects.md`
  - Documents the revalidation inputs, scope, participant-exit cleanup behavior, no-fallback policy, and finite war-goal retention.

## Before and after behavior

Before this repair, `independence_wave_unregister_league_member` removed the generation-matched league row and called revalidation, but revalidation only cancelled DM-58 when the surviving league count fell below the formation minimum. A recorded non-coordinator participant could therefore leave while enough unrelated members remained, leaving a stale frozen row until another lifecycle transition or expiry callback.

After this repair, the same revalidation call sees the departing scope in the frozen member array and clears the shared operation. The cleanup clears the coordination flag, coordinator target, state receipts, readiness fields, aligned witness arrays, and count. It does not issue targets or reverse finite war goals that have already been created.

## Why this is bounded and generation-safe

The offline Data structures reference defines `is_in_array` as an exact element check and documents arrays as persistent scope collections. The vanilla trigger documentation supports `is_in_array` in any scope and the vanilla effects documentation supports scope-valued array entries. DM-58 writes the witness members only after the current-generation league ledger has produced a complete distinct-member and distinct-owner witness. All generation reset and operation reset paths clear the witness array. The check therefore targets the single active operation ledger instead of scanning the world or manufacturing a new assignment.

## Validation

- Focused PowerShell assertions confirmed the revalidation effect, active-operation guard, witness-member array check, shared cleanup call, and absence of `remove_wargoal` from operation cleanup.
- A source brace and quote scan passed for `common/scripted_effects/006_independence_wave_effects.txt`.
- `git diff --check` passed for the touched source and helper documentation.
- Offline array and event-target semantics were read from `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`, and `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`.
- Vanilla `triggers_documentation.md` and `effects_documentation.md` were read for `is_in_array`, `exists`, `has_event_target`, `add_to_array`, `remove_from_array`, `save_global_event_target_as`, and `clear_global_event_target`.

## Skipped meaningful validation

No Hearts of Iron IV process was launched. No runtime country-exit, mid-operation expiry, save/load, or finite-war-goal consumer scenario was executed. No MCP artifact was produced because this narrow source repair does not change a GUI, map, focus, or probability surface.

## Remaining runtime evidence

The parent still needs live evidence for a non-coordinator participant exit while three or more unrelated league members remain, coordinator exit, member exit below the minimum, an already-issued finite war goal after early cleanup, natural callback expiry, save/load during the active window, and AI selection. The source policy is strict cancellation on any recorded participant invalidation. A later runtime pass should verify that cleanup happens once and that no fallback witness or replacement war goal is emitted.

No fallback or simplification was used.
