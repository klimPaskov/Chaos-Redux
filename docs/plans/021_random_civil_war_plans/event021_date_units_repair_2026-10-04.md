# Event 021 date-unit repair

Disposition: implemented and committed source repair, live confirmation pending.
Acceptance basis: the orchestrator acting for the user reported on 2026-10-03 at 20:00 that one game hour is 0.00001 in date variables and explicitly requested every Event 021 day-addition site to be repaired and committed.

## Implementation

All 41 date-duration additions use `event021_days_to_date_offset` with caller-owned temporary storage before the final date write.
The five affected source files are the base, parent, decision, evidence, and treaty Event 021 effects.
The new calendar constants define 24 hours per day, 100,000 hours per encoded date unit, and a one-hour rounding step.
Whole-day durations convert exactly and fractional-hour durations round upward, with less than one hour of additional delay.
The original day inputs, native `days =` operands, mission timers, configured duration bands, MTTH values and clamps remain unchanged.
Copied recurrence and treaty date anchors are not converted again.
No new periodic review, actor, asset, GUI, or fallback is introduced.

The independent architectural audit inspected 62 Event 021/shared-consumer runtime files and found no additional Event 021 date arithmetic or date-difference value feeding a native day field.
Its 41-site count is 13 base writes, 12 parent writes, three decision writes, 12 evidence writes, and one treaty fallback.
See [`event021_date_units_audit_2026-10-03.md`](subagent_handoffs/event021_date_units_audit_2026-10-03.md) for operands, line maps, source identities, references, and coverage limits.

## Verification and publication boundary

The implementation is published in commit `015a7820a22727a72cc567ea54abd2abed35f303`, tree `118e66db36f76dcaa818cc24955ba37d85ed2945`.
The six calendar regressions also pass against that exact committed object.

Six source-backed calendar tests pass against isolated proposed tree `c9b68609121636dc2cb678a2b40f04cda18edf75`, based on `b60528470e00464641edf2e99f591e1599d33a8a`.
They cover two days as 48 hours instead of 200,000 hours, exact whole-day durations, fractional MTTH durations resolving no earlier than intended, one-hour deadline boundaries and copied anchors, all 41 caller-owned converter sites, and preserved native day fields and MTTH source.
The independent reviewer reproduced all six calendar and twelve metadata methods from that tree's test blobs and verified inverse-AST equality for all five complete effects files after reversing only the 41 unit conversions.
Twelve committed evolution-log source regressions also pass against that proposed tree.
Three unpublished front-ledger contract tests pass in the working tree, but are not part of this date-only commit.
The tests interpret the specified source arithmetic and storage contract and do not establish live game behavior.

The date-only patch is built from HEAD with only the 41 owned substitutions, the helper, constants, and their tests and documentation.
It excludes unfinished ledger, external-war, mission redesign, and MTTH-eligibility work from mixed files.
The shared-tree isolated index, compare-and-swap publication, and path-specific index reconciliation preserve unrelated staged and unstaged work.

The pre-edit working parent source is archived under `probability_snapshots/event021_date_units_before_2026-10-03/` with SHA-256 `0DBD60BF8259F6848413F84DB79F988D6D29CABB26FA09C283066A7A03E1DF61`.
Its companion MTTH snapshot is SHA-256 `7982F0768B8ED04AE7154BCFF8CBDAC33589F8F7B031CFE12353F625891881C1` and matches the unchanged working MTTH source.
These are before evidence, not staged gameplay.

## Evidence limits and remaining goal work

The received [`probability audit`](subagent_handoffs/event021_date_units_probability_audit_2026-10-03.md) verifies the published commit and records valid MTTH and parent-effect comparison attempts returning `PROBABILITY_SURFACE_EMPTY`.
It does not certify numerical timing or a full clock trace.
Its shared-worktree MTTH difference belongs to the separate uncommitted actor-eligibility migration.
The date-fix base and commit both retain MTTH Git blob `123c4f6f4964715be173c1dd580aae53ff1f0d62`, and the original tuning file is unchanged across that commit.
The independent inverse-AST review likewise isolates the complete parent-effects delta to the date substitutions.
The audit's disabled-stage resampling and predecessor-gating findings are separate scheduler issues, not resolved by the unit correction.
The broader scheduler work must suppress disabled-stage sampling without recording disabled evolution history and resolve later-stage dependency behavior against the accepted evolution design before changing that policy.
No independent progression or disabled-stage fallback has been implemented by this report reconciliation.
The current MCP adapter did not classify scripted MTTH, an inspected random-list pool was incomplete, and lifecycle inspection/render coverage remains incomplete.
No clean live error.log or full Event 021 completion is claimed.
The broader active-war evolution, native tag capacity, inherited package/assets, full probability, performance, and final acceptance work retains its existing unfinished status.
The approved relation-only external-war fallback is unchanged by this repair.
No gameplay simplification or new placeholder was introduced by the calendar fix.

Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-mtth`, `chaos-redux-subagents`, and `chaos-redux-shared-git-commit`.
