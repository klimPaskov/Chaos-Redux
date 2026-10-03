# Participant-country and state-loss scope skill handoff

Disposition: superseded by `012_participant_scope_skill_rule_review_2026-10-03.md`, which corrects the original paragraph's categorical targeted-decision ROOT claim using exact local references.
The patch and hashes below record the initial insertion rather than the final rule.
Acceptance basis: the explicit parent assignment authorizes one reusable participant-scope rule in the events skill and this handoff, preserving existing edits and prohibiting gameplay and Git mutations.
MCP reference validation is blocked by stalled retrieval, and no parent-feature completion is claimed.

## Changed files and owned patch

- `.agents/skills/chaos-redux-events/SKILL.md`: four sentences in `#### Country activation and ROOT`.
- `docs/plans/012_africa_plans/subagent_handoffs/012_participant_scope_skill_rule_2026-10-03.md`: this handoff.

The initial insertion grouped country events and targeted decisions under an assumed initiating-owner ROOT.
The corrected replacement and its owned patch are recorded in the linked review handoff.

Existing guidance explains ROOT and callback-specific PREV contracts but does not cover capturing the iterated participant before entering a state-loss helper.
The addition covers that exact gap without changing those contracts or adding another section, event identifiers, names, private variables, or event-specific facts.
The generic event-target token `participant` is illustrative rather than a new runtime identifier.
The parent-provided actual bugfinding traces an owner callback through owner tick, participant iteration, failure or defiance, and punishment, where ROOT still denotes the owner.
The parent reports that `gods_apply_population_wave` captures a regular participant target and uses it for the supplied country and report flag after the exact helper.
Those findings are explicitly parent-provided source evidence, not an independently executed engine test or speculation about a pre-existing project defect.

## Initial hash and preserved edits

Initial working-file SHA-256: `c38b0fd3ff89279ff465ccf1c5e4e848ee9dbb7ce6e652baaca0b5d9013dd777`.
Working-file SHA-256 immediately after this worker's insertion: `aad544e7c1207f412b7a7e48c83a572d8c3be926cca4033680cd7d263ac717ee`.
Initial and post-edit index blob: `295345df7453152785028ed4da72c229d072997d`.
The initial staged diff for this skill was empty, so no staged skill hunk was changed.
The existing unstaged hunk `@@ -352,6 +352,8 @@` was preserved verbatim.
It adds the event-option audit paragraph covering parent-qualified reused option identifiers, complete local candidate pools, connected schemas, top-level scenario dates, explicit state-controller maps and typed scopes, `poolComplete`, `unresolved`, `candidateOverrides`, and firing-conditional option shares.
At insertion time, removing only the owned addition reproduced the initial byte hash, proving preservation of that hunk, all remaining text, original encoding, and mixed LF/CRLF line endings.
During final review, another agent concurrently added the unstaged `### Helper output lifetime` subsection (`@@ -160,6 +160,15 @@`).
That entire subsection was left intact and is not owned or substantively audited by this worker.
Its exact added-byte SHA-256 is `c5bec7040180c073eaf2b76f9098c984982ec900f42df0ae3905c5ceddbbd6e9`.
The final shared-file SHA-256 is `4b06bbcc69374923757ff07d9b3ed6273fd8ba6de1f81d8f865b247924c3324f`.
Removing only this worker's addition from that shared file yields `3eb83a282b33a82a322c18cf18eb1680165967632f6227683921b7db249386df`, which includes the concurrent helper-output subsection.
Removing both additions in memory reproduces the initial hash exactly, demonstrating that no original bytes were lost and the concurrent addition is retained.
The final staged diff remained empty and the index blob remained unchanged.
The owned unified hunk above is relative to the insertion-time working-file baseline, while the concurrent subsection shifts its final location to line 497.
The first insertion attempt stopped on an anchor assertion before writing because the section uses LF inside a mostly CRLF file.
The final insertion follows the section's local line endings and preserves every original byte.
No gameplay, AGENTS.md, other skill, generated runtime file, prior native-clock handoff, or parent report was edited.
No Git mutation or commit was performed, and the earlier native mission timer rule was not revisited.

## References and route limits

Connected metadata exposes `hoi4.reference_context`, `hoi4.reference_search`, and revision-bound `hoi4.reference_read`.
Initial requests were event context with limit 2 and question about participant iteration, state scopes, ROOT, and regular target lifetime, plus `save_event_target_as` search with sources `[game_doc, wiki]` and limit 3.
Both reached explicit 45-second client wait timeouts without tool results.
A narrower `hoi4.reference_search` retry used the same exact token, sources `[game_doc]`, and limit 1, and also reached the 45-second client wait timeout.
These are orchestration wait timeouts, not claimed server-generated timeout messages.
No MCP citation id, revision, coverage, artifact, or source-health result was returned.
A revision-bound reference read could not be constructed from a returned id, so no successful `reference_read` is claimed and no document id was invented.
The user-authorized local fallback was read directly with current file hashes:

- `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md`, lines 6496-6511, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`: Regular and global save-event-target effects accept any scope.
- `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md`, lines 260-269, revision `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49`: ROOT belongs to the initiating block, THIS is current scope, PREV follows nesting, FROM carries the targeted decision target, and event targets work as scope pointers.
- `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md`, lines 263-305, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`: Event targets hold a scope pointer and regular targets last through the effect chain and events fired within it, then clear automatically.

Installed documentation remains the primary effect syntax authority and the offline wiki supplies parallel ROOT and target-lifetime evidence.
No online Paradox source was used.

## Validation and handoff

The official `quick_validate.py` passed with `python -X utf8` for `.agents\skills\chaos-redux-events` after the final edit.
Byte-preservation and index-blob comparisons passed at insertion and after accounting for the concurrent helper-output hunk.
The actual existing scope section and every ROOT/event-target/receipt reference in the skill were checked for overlap.
The rule retains helpers whose documented callback contract legitimately requires ROOT and adds explicit participant attribution only for this iterator-to-state workflow.
No gameplay implementation, live engine scenario, report accounting execution, event trace, or user session was validated in this bounded maintenance task.
No HOI4 launch or log request occurred.
The parent retains gameplay review, attribution and receipt validation, and any domain MCP evidence for the bugfix.
No AGENTS.md or subagent routing update is required.

Skills used: official `skill-creator`, `chaos-redux-subagents`, and `chaos-redux-events`.
Updated: `chaos-redux-events` only.
Created: no new skill.
Left unchanged: official `skill-creator`, `chaos-redux-subagents`, and every other skill.
No requested design simplification or omitted part of the reusable rule.
Remaining limits are the blocked MCP retrieval and unobserved engine behavior.
