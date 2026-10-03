# Parallel portrait receipt skill handoff

Disposition: implemented; parent review and shared commit remain pending.
Acceptance basis: the parent's explicit bounded request for two reusable portrait-workflow paragraphs.

Updated `.agents/skills/chaos-redux-event-assets/references/portrait-production.md`, lines 29-39, by adding one heading and exactly two paragraphs.
Lines 31-35 require worker reports to stay within their tranche's files and independent acceptance evidence, reserve global counts for the parent or a revision/time-cited current parent inventory, leave unreadable or absent other-owner receipts unknown, and preserve truthful historical snapshots and concurrent disjoint changes without resets.
Lines 37-39 separate DDS byte matching from art acceptance, require an explicit selected source/version and processed PNG -> candidate DDS -> runtime paths mapping despite retained alternates, and require receipt relocation pointers to be updated while preserving immutable original lineage and original receipt path/revision.

Rationale: parallel workers can otherwise repeat stale parent totals, misclassify concurrent owners' work, rewrite historical observations from later totals, or review an unselected candidate because its filename sorts first.
The addition captures the recurring workflow without event identifiers, regional counts, or one-off production history inside the skill.

Used `skill-creator`, `chaos-redux-subagents`, and `chaos-redux-event-assets`, plus the existing portrait-production reference.
Left `.agents/skills/chaos-redux-event-assets/SKILL.md` unchanged, including the consumer-inventory rule identified by the parent as `c87ea738`.
Created no skill; changed no routing contract or AGENTS.md instruction, so no subagent-skill or AGENTS.md follow-up is required.
No gameplay identifiers, assets, spreadsheets, or other files were edited beyond this handoff and the named reference.

Reviewed the focused diff and exact added line positions against the requested constraints.
No tools, tests, or report generators were added; no tests or production workflows were run, and no commit was made, as instructed.
This documentation review does not establish portrait acceptance or current global completion counts.
No simplifications, omissions, or blockers remain in the requested skill patch; parent review and the shared commit are the remaining handoff actions.
