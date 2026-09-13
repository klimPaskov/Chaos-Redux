# Event 021 SCN parent deterministic review

Date: 2026-09-01.

Owner: parent implementation pass.

Status: current-source deterministic evidence with SCN-01 and SCN-03 targeting preference pending the exact probability-auditor baseline.

## Findings and patch

SCN-018 uses verified triggerable-scenario ID 18, exposes Political Fracture, Independence Cascade, Command Collapse, and Universal Fragmentation, and exposes Low, Medium, High, and Maximum intensities.

The Maximum path previously evaluated eligibility during the same `every_country` block that committed crises. A country created by an earlier commit could therefore become visible to a later iteration. Maximum now freezes every eligible normal-human country into a confirmation-time pool and commits that fixed pool immediately, so no newly created opposition actor can join the same scenario run.

The scenario adapter previously materialized same-tag evidence only for Political Fracture and then selected legal or ideological evidence first. Unsafe one-state or all-island topology is now a scenario-wide preflight, route, evidence, and selection override for all four types; multi-state continental countries retain their type-specific precedence.

High and Maximum manual setup previously forced stronger severity but could not enter the multi-front transaction unless Evolution I was already active globally. The host now exposes a setup-only multi-front gate while a High or Maximum manual launch and its country bypass are both live. Ordinary campaign openings continue to require active Evolution I, and the scenario branch disappears when setup clears its bypass.

Low, Medium, and High compute their requested count from the frozen eligible count, apply centralized shares of 10, 25, and 50 percent, round the result, retain a minimum of one when the pool is nonempty, cap the request to the pool size, and sample without replacement.

## Named matrix disposition

| Scenario | Current deterministic disposition |
| --- | --- |
| SCN-01 | Political Fracture Low requests about ten percent and forces Limited severity with one opponent. The present source samples eligible majors and minors uniformly, so the required mostly-minor preference is pending the exact weighted baseline and same-scenario owner/auditor patch cycle. |
| SCN-02 | Medium requests about twenty-five percent, forces Serious severity, and allows the ordinary Evolution I second-front contract when route and cap proof exists. |
| SCN-03 | High requests about fifty percent, forces Severe severity, and activates the bounded multi-front transaction during manual setup even when Evolution I is not globally active. The present source samples eligible majors and minors uniformly, so the required major-common preference is pending the exact weighted baseline and same-scenario owner/auditor patch cycle. |
| SCN-04 | Universal Fragmentation Maximum freezes every eligible normal-human country at confirmation, immediately commits each frozen member through the ordinary transaction, and cannot enroll countries created during the run. |
| SCN-05 | `random_civil_war_is_normal_human_country` rejects `is_actual_nonhuman_country`; the scenario eligibility predicate inherits that exact exclusion. |
| SCN-06 | Any type materializes same-tag evidence for a one-state or all-island target and gives it precedence for that unsafe topology without duplicating a tag. The selected type remains recorded as scenario provenance. |
| SCN-07 | Setup is immediate and one-shot. No delayed branch exists because no measured one-frame performance failure authorizes the permitted seven-day fallback. |

## Release boundary

`event021_parent_initialize_global_runtime` deliberately clears `random_civil_war_rework_ready`, so SCN-018 remains unavailable until every release blocker is resolved. This review does not authorize opening that gate.

## MCP and runtime boundary

The focused parent-effects lint refreshed after the frozen-pool, same-tag, multi-front, and single-dispatch changes and returned partial workspace analysis with no Event 021 blocker: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2abcc7ecfe74432c9e3b393f7c8aedc5df3b208f51d550ae72b8c7af8414c048/79ff633d3ecc06b0cbeffc50a07e5d8cecd1ed8c681f5e55c6c4b4bb0f39242f/event-lint-b8b928ac6119.json`.

The focused scenario-trigger lint returned partial workspace analysis with no Event 021 blocker: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/257a2837b443c6f752b3d7099af0c3408954301b5800a4d4678c0b1523498ff6/3123be819230e2cc2a8a044c9b38bf48035978cd421d70f214470a7a584a2cce/event-lint-b8b928ac6119.json`.

No one-frame timing measurement or live scenario sequence is claimed.
