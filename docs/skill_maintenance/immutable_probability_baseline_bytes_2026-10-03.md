# Immutable probability baseline byte preservation

Disposition: implemented.
Acceptance basis: explicit user authorization for one generic paragraph in the existing immutable probability baseline guidance and this handoff, with a commit containing only the owned changes.

## Scope and behavior

Updated `.agents/skills/chaos-redux-subagents/SKILL.md` immediately after the existing audit-patch-compare baseline paragraph.
Before: the workflow retained a physical source copy and its SHA-256, but did not require checking that a durable Git blob retained those same bytes.
After: committed snapshots must preserve bytes across attributes and filters, explicitly refresh cached normalization when attributes change or use no-filter blob promotion, and pass a raw committed-blob SHA-256 comparison.
The physical original remains preserved and any mismatch and dependent comparison proof remain unresolved until repair and reverification.

Used `skill-creator`, `chaos-redux-subagents`, and `chaos-redux-shared-git-commit`.
No skills were created.
The shared commit skill already covers isolated indexes, mixed ownership, guarded publication, and reconciliation, so it remains unchanged.
No AGENTS.md, subagent routing, generated runtime, gameplay, asset, binary, tooling, or configuration update is needed.

## Exact owned skill patch

```diff
--- a/.agents/skills/chaos-redux-subagents/SKILL.md
+++ b/.agents/skills/chaos-redux-subagents/SKILL.md
@@ -216,6 +216,11 @@
 
 Any patch to an AI weight, probability-bearing modifier, MTTH-backed score, random-selection weight, strategy factor, or weighted target check requires an audit-patch-compare cycle. Run `chaosx_ai_probability_auditor` first to establish named baseline scenarios. Before editing, the parent or patch owner must preserve an immutable copy of each affected pre-edit source at a real filesystem path, plus the exact scenario fixture and a SHA-256 hash of the copied bytes; give these identities to the auditor. The owner applies the bounded change, then the auditor runs `hoi4.probability_compare` against the same scenarios. The probability auditor remains read-only, does not choose the intended balance target, and does not patch source.
 
+If immutable probability snapshots are committed as durable before-source evidence, preserve the copied bytes through narrowly scoped Git attributes and any clean filters.
+When attributes change after staging, plain `git add` may reuse cached normalization; force path-specific `git add --renormalize` under byte-preserving attributes and filters, or explicitly promote a blob using `git hash-object -w --no-filters` and a path-specific index update.
+Verify that the raw committed blob's SHA-256 matches the recorded copied-byte hash, reading it without text decoding, newline conversion, or checkout filters.
+Preserve the physical original and keep any mismatch and dependent comparison proof unresolved until repaired and reverified.
+
 Active small patches do not include:
 
 - creating or expanding a whole mechanic
```

## Verification and commit handoff

A focused installed-Git behavior check passed: an in-memory sample with mixed CRLF/LF produced a different object under text normalization, while a no-filter blob read through a binary stream retained the original SHA-256.
The skill ownership check passed: removing only the added paragraph restored the exact pre-edit physical skill bytes, including the other agent's existing unstaged hunk.
The official skill validator accepted the updated skill.
The user-reported cached-normalization incident is the evidence for the refresh rule; this task did not recreate that historical staging sequence or audit existing probability snapshots.

Commit only the exact skill patch above and this handoff through the shared commit skill's isolated-index workflow.
Review the proposed tree before publication, prepare reconciliation from the captured real-index state, guard publication against a changed HEAD or affected index entry, and verify the committed patch and retained unrelated staged and unstaged state afterwards.
Return the commit identifier and publication verification to the parent inline; do not stage the whole mixed-ownership skill or discard other agents' changes.

## Risks and limits

Concurrent edits to the same paragraph or relevant index entries require rebuilding the isolated patch or coordination.
Scoped attributes must also account for clean filters; disabling newline conversion alone does not prove byte identity.
Raw blob verification must use a binary stream because text pipelines can normalize newlines or encoding.
No engine-facing source changed, so HOI4 MCP, wiki, vanilla, game, and desktop testing are outside this task.
No simplifications or omissions were made in the requested skill guidance; historical snapshot integrity remains outside this maintenance scope.
