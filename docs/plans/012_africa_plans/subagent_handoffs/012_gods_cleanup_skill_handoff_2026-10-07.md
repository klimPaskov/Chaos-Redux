# Cleanup lifecycle skill handoff

Disposition: implemented for the bounded skill update; parent review and commit remain pending.
Acceptance basis: the explicit 2026-10-07 instruction to update only section 17 and write this handoff.

## Problem and reusable guidance

The parent supplied the recurring finding: ordinary demand closure reused cleanup helpers for instalment schedules, diplomatic target arrays, and agreed terms, while authority-loss or participant cancellation duplicated only part of that cleanup and left temporary fields behind.
Native mission removal depended on a private active flag, allowing an orphan native mission to escape cleanup when that flag was stale.
This maintenance task did not independently audit the gameplay implementation.

The skill requires normal resolution and exceptional cancellation to cover the same temporary-term inventory, reuse appropriate existing cleanup helpers after one-use retirement and slot accounting, and remove obsolete native missions independently of stale private flags.
It explicitly preserves durable history and refund, settlement, and report receipts and excludes normal cooldown, reward, and failure logic from authority-loss cancellation.

## Exact bounded hunk

Changed file: `.agents\skills\chaos-redux-decisions-missions\SKILL.md`.
Section 17 begins at line 919 in the reviewed file.
Replaced the former standalone sentence at line 933 with one paragraph occupying lines 933-936; each sentence occupies one physical line.
The setup-receipt invariant remains unchanged at lines 938-942.
Line references describe the post-edit file reviewed during this handoff and may move if other agents insert text.

```diff
-Do not leave stale missions active after the system they refer to has ended.
+Compare normal resolution and exceptional cancellation against the same temporary-term inventory, including instalment schedules, diplomatic target arrays, and agreed terms.
+Reuse the appropriate existing cleanup helpers after one-use retirement and slot accounting.
+Remove obsolete native missions independently of stale private active flags, using actual mission state or documented idempotent removal; `remove_mission` skips completion and timeout effects.
+Preserve durable history and refund, settlement, and report receipts, and do not invoke normal cooldown, reward, or failure logic on authority-loss cancellation.
```

## Evidence, applicability, and validation limits

Read repository `AGENTS.md`, official `skill-creator`, the relevant `chaos-redux-subagents` maintenance boundaries, and the decision skill's existing cleanup, timer, duplicate-mission, receipt, and payment guidance.
Adjacent guidance did not already specify this cleanup parity and orphan-mission removal rule; the replacement extends the existing lifecycle paragraph without duplicating the setup-receipt invariant.
Read installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md`, lines 6083-6092, directly.
Its `remove_mission` entry documents COUNTRY scope and removal without complete or timeout effects.
Source revision fingerprint: SHA256 `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF`.
That entry does not establish removal idempotence or cancellation-callback behavior; the skill's idempotent-removal alternative requires separate documentation and does not assert those properties for `remove_mission`.

The paragraph applies to decision and mission systems with temporary terms and exceptional cancellation paths, including loss of authority or participant validity.
It does not authorize clearing durable receipts or running the ordinary resolution helper wholesale when that helper applies cooldowns, rewards, or failure consequences.
No event identifiers, event paths, or event-specific descriptions were added to the skill.
The edit read the current file under a write lock and copied every byte outside the replacement unchanged; post-edit section review confirmed the exact hunk and intact adjacent invariant.
No gameplay files, tests, other skills, Git/index operations, or game launch were involved, as requested.
This is documentation validation only; no engine execution, helper correctness, actual mission-presence behavior, or runtime cancellation result is claimed.

## Parent handoff

Used skills: `skill-creator`, `chaos-redux-decisions-missions`, and the maintenance-boundary guidance in `chaos-redux-subagents`.
Updated skill: `chaos-redux-decisions-missions` only.
Created skills: none; other skills left unchanged; no AGENTS.md or subagent-routing update is needed.
Completed: the bounded section-17 paragraph and this handoff.
Blocked work: none within the assigned scope.
Simplifications or omissions: none within the assigned scope; gameplay implementation and its validation belong to the parent task.
Parent should review and commit only the quoted skill hunk and this handoff alongside related completed work, preserving unrelated shared-tree edits.
