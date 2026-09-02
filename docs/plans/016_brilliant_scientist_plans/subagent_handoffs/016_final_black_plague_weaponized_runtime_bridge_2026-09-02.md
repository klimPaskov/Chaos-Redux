# Event 016 Black Plague weaponized runtime bridge — 2026-09-02

## Status

Implemented and parent-integrated the bounded shared STATE-scope bridge requested for Event 016 closure. Event 016 and native weaponization now call the shared bridge, while their payload and attribution transactions remain separate. The existing Event 020 scheduler uses the parent-repaired `black_plague_scheduler_due_num_days` and `global.num_days` fields in the current worktree.

No existing gameplay file was edited by this subagent. No files were staged or committed.

## Files changed

- `common/scripted_effects/020_black_plague_weaponized_runtime_effects.txt`
- `common/scripted_effects/020_black_plague_weaponized_runtime_effects.md`
- `common/scripted_triggers/020_black_plague_weaponized_runtime_triggers.txt`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_final_black_plague_weaponized_runtime_bridge_2026-09-02.md`

## Reusable helper map

| Identifier | Scope | Inputs | Output | Side effects |
| --- | --- | --- | --- | --- |
| `black_plague_apply_weaponized_exposure_runtime` | STATE, actor in `ROOT` | Required weaponized `black_plague_exposure_provenance`; optional existing exposure amount and route temps | Exact temporary `black_plague_weaponized_runtime_bridge_result`, zero or one | Safe one-time runtime bootstrap, one existing exposure call, and post-acceptance scheduler reconciliation. |
| `black_plague_weaponized_runtime_bridge_ensure_scheduler` | STATE | Accepted shared exposure and Event 020 runtime | None | Reuses valid anchor/receipt, repairs an invalid active receipt once, or replaces an absent/invalid reachable anchor with the accepted state and schedules once. |
| `black_plague_weaponized_runtime_bridge_target_is_valid` | STATE trigger | Current state inputs and `ROOT` actor | Boolean | Geography/population/controller gate, weaponized provenance gate, world-end/terminal gate, and runtime readiness gate. |
| `black_plague_weaponized_runtime_scheduler_anchor_is_active` | Any trigger scope | Existing global scheduler target | Boolean | Read-only check of reachable state plus anchor flag. |
| `black_plague_weaponized_runtime_scheduler_receipt_is_valid` | Any trigger scope | Reachable anchor and shared generation/ticket/due fields | Boolean | Read-only validation of active unsuppressed receipt using elapsed `global.num_days`. |

## Before and after boundary

Before this bridge, Event 016's `brilliant_scientist_dispatch_black_plague_release` called the ordinary biological lifecycle dispatch and then called `black_plague_apply_exposure` without bootstrapping Event 020 or scheduling `.900`. Native weaponization bootstrapped the runtime earlier but likewise called the exposure effect directly and did not own a missing scheduler anchor.

Each authorized caller sets its existing amount, route, and weaponized provenance inputs and calls `black_plague_apply_weaponized_exposure_runtime` in the exact target state. Event 016 gates its history on the bridge result of one. Native weaponization keeps its existing native transaction and pays only after the bridge accepts the state.

## Safety contract

- Exposure is attempted only for a live state passing `black_plague_state_can_receive_exposure` and an explicit weaponized provenance input.
- The actor must exist, not be capitulated, and not be in world end or an active/completed terminal takeover.
- A started-but-inactive runtime fails closed.
- An unstarted runtime bootstraps only when pulse suppression is absent, because the existing initializer clears `black_plague_pulses_suppressed` on first initialization.
- An active suppressed runtime may accept exposure, but scheduler reconciliation does nothing and does not clear suppression or replace the scenario anchor.
- `black_plague_system_eradicated` is not used as a blanket lock, preserving the documented weaponized return after natural eradication.
- The bridge calls `black_plague_apply_exposure` exactly once after validation and never calls the natural outbreak root, ordinary `bio_lifecycle` dispatch, native public delivery, or payload accounting.
- The shared `black_plague_exposure_result` is copied immediately to the private bridge result in the same effect chain. Both are temporary variables and therefore scope-less; callers read `black_plague_weaponized_runtime_bridge_result` directly after the nested state block instead of qualifying it through `ROOT`, `PREV`, or another scope.

## Scheduler and cleanup contract

The bridge validates the existing global `black_plague_scheduler_anchor_state` target, its state anchor flag, runtime generation, scheduler ticket, and `black_plague_scheduler_due_num_days >= global.num_days` receipt.

A valid receipt is left unchanged. An active anchor with a missing or invalid receipt is scheduled once in place through `black_plague_schedule_next_pulse`. An absent or invalid anchor target clears only the reachable old state pointer/receipt, clears the global target, binds the accepted current state, sets the anchor flag, and schedules once. No `every_state` world scan is used for repair.

Queued stale `.900` events remain handled by the shared generation/ticket checks. The bridge does not claim unsupported cancellation semantics for an unreachable stale state flag or a queued event after target transfer/destruction.

## Constants and tuning

No constants or weighted surfaces were added. The bridge uses existing `black_plague_value.zero`, `black_plague_value.one`, `black_plague_provenance.weaponized`, `black_plague_timing.pulse_days` through the shared scheduler, and the parent-repaired elapsed-day field `black_plague_scheduler_due_num_days`.

## Parent integration completed

1. `common/scripted_effects/016_brilliant_scientist_biological_operations_effects.txt` retains the ordinary plague lifecycle proof as its first gate, calls the bridge, and records Black Plague provenance and delivery history only on exact acceptance.
2. `common/scripted_effects/020_black_plague_weaponization_effects.txt` calls the bridge and performs its native payment, attribution, history, cooldown, condemnation, and report effects only on exact acceptance.
3. `common/scripted_effects/020_black_plague_effects.txt` stores scheduler and devastation due receipts on `global.num_days`; no `global.date` arithmetic remains in these elapsed timers.
4. Parent review corrected the bootstrap ordering so the caller snapshots are restored before the post-initialization validity check.
5. Parent review removed invalid scope-qualified copies of `black_plague_weaponized_runtime_bridge_result`. The single temporary result now survives the nested state block according to the documented scope-less temporary-variable contract.
6. Parent-owned focused Event Inspector and source/runtime review remain the acceptance evidence step for this tranche.

## Validation and evidence

Read-only Event Inspector evidence was collected before implementation for `chaosx.nr16.1` and `chaosx.nr20.900` with workspace `mod_chaos_redux_ea3b2d67c2c0`.

- Event 016 artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/25ce725dc6002b93e25efcf491813449788c7c6ceed92a9b6137604e74368952/19c808909c5c5c6d9b381417b85b9c649017cce3c8a885065c4bbf78f098748f/event-lint-efbe0ca7016c.json`.
- Event 020 callback artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d2bec7b1f8e6bcec1f686649343c1edd0853c8094aaac99cd9322737aba06225/63ecd04b3a5aca61f4cfe2c173fc9485ec2d031d21a5504059c1c917b1b765b8/event-trace-efbe0ca7016c.json`.
- Both focused calls returned `status = ok`, `analysisMode = focused`, and no MCP blockers. They reported partial large-workspace analysis with deferred helper/lifecycle passes and nonzero unresolved diagnostics, so they are source-linked evidence rather than complete engine proof.
- The initial workspace scan returned `status = ok` but 3,948 blocking event diagnostics across the full graph; this baseline was not treated as bridge-specific evidence.
- A fresh post-integration focused trace for `chaosx.nr20.900` returned `EVENT_INSPECTED_PARTIAL`, `status = ok`, and no blocker. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/78d8189ca26fa6767751079e828d4b7be0877b12d6b60b8701439df75b03c7ce/5a1bea62ec7b566974994c2ced291cd6555285adb4c52e23a70c87b107b5dbe3/event-trace-58c35aacdc89.json`.
- A fresh post-integration timing render returned `EVENT_RENDERED_PARTIAL`, `status = ok`. Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ac6408f097bdae89aaae1327fbf28718b6c2d374163102de9e5aec26dc1ce2fc/84e228ce0947eab714f44d7ab4413c73bc8ca6eea738c083e0c74eb71689519d/event-timing-58c35aacdc89-manifest.json`; JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0acab3095f66ba4ba3ec1d184dc711be59c874ba01cde85f441cb7230aed8c49/7d8be55eee5bfc136992560dc724040809b74e0c005b8c2a5f8fe917a72d6a6d/event-timing-58c35aacdc89.json`; SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a698c89ed1a35632e1c173be8d13bf06b27efa4af06ae2a53fd22581a0e79c2e/59d79400a58d90abbcf9ab4a58e6419c700198a84d3597277d5891c2bb9664b7/event-timing-58c35aacdc89.svg`; PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/94f6fd42a55c09251787fe07eabc344a7e1db58f6825819f0efdabf967bc8ae9/23f9f92014beb8dc82834fc1f3ece02863e3265e2f36519b2d4dad6ed4543724/event-timing-58c35aacdc89.png`.
- The historical-to-current `hoi4.event_compare` attempt could not run because the older baseline artifact uses an unsupported schema version. MCP returned `EVENT_GRAPH_ARTIFACT_INVALID`; this is an exact comparison blocker, not a successful before/after comparison.

Task-specific local validation after writing the files should confirm the three new script blocks are balanced, identifiers match parent call-site migration, and no legacy due-day token appears in the new bridge. Full game launch, logs, staging, commit, and live in-game acceptance were intentionally skipped per task boundary.

## Unsupported analysis and remaining risks

The source and MCP event views do not prove engine ordering or behavior of an already queued state event after its state is transferred or destroyed. The bridge follows the documented scope-less temporary-variable contract and does not create scope-qualified mirrors. Parent live acceptance remains required.

The bridge deliberately does not sweep the world to clear an anchor flag when the global pointer is missing, and it does not invent a cancellation effect for queued state events. These are bounded limitations, not substitutions.
