# Event 006 pre-event surface and dormant release fix — 2026-08-15

## Scope

This bounded repair removes dormant-country capital lookups from Event 006 package availability checks, preserves capital validation for live post-release package readiness, and allows a partially implemented but source-complete candidate pool to execute when the nominal wave band is larger than the available pool.

## Source changes

- `common/scripted_triggers/006_independence_wave*_package_triggers.txt`: exact dormant-carrier availability gates now use fixed anchor/host ownership checks without `capital_scope`; runtime/setup gates retain capital checks after release. The FER dormant gate no longer calls its live capital-anchor helper.
- `common/scripted_effects/006_independence_wave_execution_effects.txt`: execution metadata validates the reserved carrier as dormant before the release effect instantiates it. The sponsorship country remains an existing-country validation.
- `common/scripted_effects/006_independence_wave_package_allocator_effects.txt`: when the pool is exhausted after selecting one or more valid candidates, the plan commits that selected subset instead of discarding the whole incident; exact configured counts remain unchanged when available.
- `.tools/audit_event6_allocator.py`: the static contract now distinguishes the dormant release carrier from the existing sponsorship country.

## Pre-event presentation contract

The live source contains no `independence_wave_crisis_category`, `independence_wave_open_host_crisis`, or `independence_wave_cost_pre_wave_crisis` decision/localisation surface. Event `chaosx.nr6.1` is hidden and triggered-only; the public report is emitted only after a committed release. The retired crisis compatibility files remain inert/non-player-facing for parser and historical cleanup safety.

## Evidence and limits

- `python .tools/audit_event6_allocator.py` passes with the current 149 publishers, 40 adapters, 32 attestations, 29 reservation groups, and 3/4/5/7/10 automatic ladder.
- A global exact-package scan found no dormant availability block containing `capital_scope` or a capital-anchor helper.
- Targeted `hoi4.event_inspect` on `events/006_independence_wave.txt` returned `EVENT_INSPECTED_PARTIAL`, no selected blockers, and deferred workspace-wide helper/lifecycle projections. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8a3a2ae0708266a1343290560c045c9b911895221b839029063cbb789fbd33e0/5c7b81722c3c668eb810e18d1fd7e3076480fc5b57b4133beddb1d602a4672e9/event-state_flow-a0d209ec728f.json`.
- The matching read-only `hoi4.event_render` returned `EVENT_RENDERED_PARTIAL` with no selected blockers. State artifacts: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/28253f669271fa2f86825b99f5728bdbcc4908fda2d0ed75f51acfb0f82303f6/c020129ccc5f1844a7d77279b31ec85a7a59985f44876f53afc6eaac939e7e1f/event-state-a0d209ec728f.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3a4eb14b9745d6e63e068fca8f2d7b73d5d224521c4e1f5893ca043d9194e154/d2fd236c5ecc964c6a8fe3146fe2c1b7696e295ecfa4228aa1b878c80bae55c0/event-state-a0d209ec728f.png`.
- Live-game triggering remains parent/user validation; no game process was launched.

## Remaining boundary

Unimplemented or unattested package IDs remain excluded by the adapter/content-attestation gates. This repair does not invent fallback country content or widen central admission/Join lists.
