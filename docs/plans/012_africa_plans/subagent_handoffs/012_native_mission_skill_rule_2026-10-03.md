# Native mission timer skill handoff

Disposition: implemented for the bounded skill patch, using verified local reference fallback; MCP reference validation is blocked by stalled retrieval.
Acceptance basis: the explicit parent assignment authorizes this reusable timer rule and handoff, requires preservation of concurrent edits, and prohibits gameplay changes and Git mutations.
This handoff does not establish completion of the parent feature.

## Changed files and exact added hunk

- `.agents/skills/chaos-redux-decisions-missions/SKILL.md`: one subsection under `## 9. Mission duration`.
- `docs/plans/012_africa_plans/subagent_handoffs/012_native_mission_skill_rule_2026-10-03.md`: this handoff.

Only the following addition belongs to this worker:

```diff
@@ -322,6 +328,14 @@ Emergency missions can be shorter only when the event story clearly justifies im

 Do not give every mission the same timer.

+### Synchronizing native mission timers
+
+`activate_mission` initializes the native `days_mission_timeout` from the static mission definition; changing a separate stored deadline does not update it.
+Immediately after activation and every accepted deadline extension, synchronize in the mission owner's country scope, guarded by the active contract, an existing deadline, and `has_active_mission`.
+Compute remaining days as `deadline - global.num_days`, then pass the signed difference `remaining_days - days_mission_timeout@mission_id` to `add_days_mission_timeout = { mission = mission_id days = var:timeout_delta }`; this can shorten or extend the native timer and is idempotent.
+Partial payments must leave the running mission and deadline intact rather than remove and reactivate the mission.
+If the deadline is already expired, use the guarded timeout resolver; the native timeout callback and any owner recovery pass must share an active-contract guard and clear it on resolution so failure cannot resolve twice.
+
 ## 10. Success, failure, and partial success

 Success and failure must use distinct effect logic.
```

Before: duration and receipt-lifecycle guidance lacked native timer synchronization.
After: activation and accepted extensions synchronize the native timer to a stored deadline, with signed deltas, contract/deadline/mission guards, uninterrupted partial payments, and shared guarded timeout resolution.
No event identifiers, narrative facts, tuning values, or private implementation history were added to the skill.

## Preserved staged and unstaged hunks

The initial staged diff for this skill was empty.
The index blob `6db45ae020fa6dcaa13c3b8fe31174f19edf0d2c` remained unchanged through the edit.
The pre-existing unstaged hunk `@@ -231,6 +231,12 @@` contains the fractional dynamic quote paragraph and the `### Paid finite-registry release receipts` heading and paragraph; all were preserved verbatim.
Removing the sole new timer subsection from the final bytes reproduces the original SHA-256 `18ffa92586b944cd5e03f32a23e61760760696a00dd2a671446096ee1b493dd7`.
All surrounding content, original encoding, and original line endings were preserved.
The hunk is safely separable, so no parent-only patch fallback was required.
No Git mutation, gameplay write, AGENTS.md edit, routing change, or generated-runtime sync was performed.
The parent report `docs/plans/012_africa_plans/subagent_handoffs/012_africa_gods_timer_and_text_2026-10-03.md` was read and left unchanged.

## Reference evidence

Connected metadata exposes `hoi4.reference_context`, `hoi4.reference_search`, and revision-bound `hoi4.reference_read`.
Decision context was requested with limit 2, and `add_days_mission_timeout` was searched in installed documentation and offline wiki with limit 3.
Neither initial call returned a result before the orchestration wait was terminated.
A separate revision-bound, three-line `hoi4.reference_read` attempt for installed `dynamic_variables_documentation.md:238-240` also stalled and was terminated; the supplied path was not confirmed as a resolved MCP document id.
The narrow retry used `hoi4.reference_search` with query `add_days_mission_timeout`, sources `[game_doc]`, and limit 1.
It reached an explicit 45-second client wait timeout with no tool result.
This is an orchestration timeout, not a claimed server-generated 600-second timeout.
No citation IDs, coverage, revisions, omittedSources, or artifacts were returned, so none are claimed as MCP evidence.
The local cited fallback below supplies source evidence; connected service health and MCP retrieval remain unresolved.
Exact local sections were also read directly:

- `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md`, lines 1051-1065, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`: Country-scoped timeout adjustment and mission/days fields.
- `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\dynamic_variables_documentation.md`, lines 238-240; 996-998, revision `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda`: Mission-targeted remaining timeout and current total days.
- `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Effects - Hearts of Iron 4 Wiki.md`, lines 1908-1927, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`: Activation ignores decision triggers; timeout adjustment accepts an integer or variable.
- `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md`, lines 3022-3029, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`: Country-scoped has_active_mission.
- `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\YUG.txt`, lines 1227-1229, revision `856d7e22c378a11d6fec8b584f84543b45169f9bfc7e3c32a176cf622e7c7451`: Vanilla signed negative days = -15 precedent.

The first three hashes match the parent-supplied revisions, and the trigger hash matches the parent report.
The static-definition/deadline mismatch and guarded recovery lesson are the explicit parent-provided implementation finding, corroborated by the read-only parent report; the reference sections establish adjustment syntax, dynamic remaining-time access, guards, and the signed vanilla precedent rather than observed runtime execution.
No online Paradox source was used.

## Validation, limits, and parent follow-up

The official `quick_validate.py` passed with `python -X utf8` against `.agents\skills\chaos-redux-decisions-missions`.
The default Windows encoding attempt hit `UnicodeDecodeError` on existing Unicode text; UTF-8 mode resolved the validator environment issue without changing that text.
A byte-preservation comparison and final diff inspection show that only the timer subsection was added and the existing cost/receipt hunk survives.
Source-contract arithmetic: a native 180-day anchor with 45 days remaining receives delta -135; 210 days remaining receives delta +30; repeating synchronization after either adjustment yields delta zero.
Partial payment leaves the mission running, and an already resolved contract prevents the competing timeout/recovery path from publishing another failure.
These are documentation and source-contract checks, not executed engine scenarios.
No HOI4 launch, log request, or live-game validation was performed.
The parent retains gameplay integration, full feature validation, and the parent report; review this exact new hunk independently of the existing cost/receipt edits.
No AGENTS.md or subagent routing update is needed.

Skills used: `skill-creator`, `chaos-redux-subagents`, and `chaos-redux-decisions-missions`.
Updated: `chaos-redux-decisions-missions` only; no new skill was created.
Left unchanged: `chaos-redux-subagents`, official `skill-creator`, AGENTS.md, and all other skills.
No requested rule was simplified or omitted.
MCP reference validation is blocked by the stalled initial calls and 45-second narrow-retry client timeout.
The user-authorized local fallback was completed; no implementation or design simplification was made.
Unobserved engine behavior remains an evidence limit, and the parent retains any required runtime and domain MCP validation.
