# Asset request and subject lineage skill handoff

Disposition: implemented and parent accepted under AGENTS.md section 9; published through the isolated shared-tree commit workflow.
Acceptance basis: parent-authorized bounded skill maintenance under AGENTS.md section 9, limited to the existing asset skill and this handoff.

## Scope and finding

Used `skill-creator` and `chaos-redux-event-assets` after reading repository `AGENTS.md`.
Updated only `.agents/skills/chaos-redux-event-assets/SKILL.md`, in `Candidate lineage and review`.
No new skill, routing change, generated agent-definition change, gameplay change, staging, or commit was made.
Other skill sections and files were left unchanged.

The existing skill already required exact prompts, immutable candidate sources, native generated subject art, and rejection of primitive substitutes.
It did not explicitly require request persistence before tool calls, source hashes in candidate records, per-subject source/frame/consumer verification, or honest handling of an unavailable historical request.
The change fills those concrete gaps without adding a provider, portrait, or fallback authorization.
Deterministic geometry remains subject to existing family contracts, including their stricter template and exact-map rules.

## Exact old/new hunk

```diff
@@ -944,13 +944,19 @@
 
 #### Candidate lineage and review
 
+Before each native ImageGen generation or edit, save the exact request arguments in a repo-contained prompt record: `prompt`, `transparent_background`, and supplied reference paths or recent-image count, with the actual referenced images identified and retained.
+
 While the asset workspace is active, keep the original generated source and every accepted intermediate immutable at distinct versioned paths. Keep source outputs separate from processed previews and runtime files. In the active manifest or linked prompt record, record for each generated candidate:
 
 - candidate id, parent candidate id or new-generation reason, and input paths with their declared roles
-- exact submitted prompt, focused edit delta, invariants, and background mode
-- tool-reported output path, retained workspace path, decoded dimensions, and alpha evidence
+- linked exact saved request, focused edit delta, invariants, and background mode
+- tool-reported output path, retained workspace path, source SHA-256, decoded dimensions, and alpha evidence
 - source-resolution and final-native-size review results, accepted/rejected status, and remaining defects
-- explicit final-selected candidate id, processed PNG path, and final runtime path after conversion
+- explicit final-selected candidate id, processed PNG path, final runtime path after conversion, and each subject's source-to-layer/frame-to-consumer mapping
+
+Before runtime promotion, review every newly generated or edited subject against its actual source and saved request; a correct-looking preview does not establish ImageGen lineage.
+Deterministic template/frame geometry and processing remain allowed under the applicable family contract, but cannot replace generated subject art.
+If an exact historical request is unavailable, mark it unavailable and preserve known source paths/hashes rather than reconstructing it; fresh generation or editing must remain within existing authorization and portrait/source-mode, provider, and fallback boundaries.
 
 Do not silently overwrite a prior accepted candidate or synchronize an older candidate into runtime. Before normal temporary-workspace cleanup, promote the lineage, prompts, final selection, and review facts into permanent documentation under the existing cleanup contract. Retain active image files until the required package review is complete; this rule does not create a second permanent asset archive.
 
```

## Validation and limits

The skill was reread immediately before applying the bounded hunk; the initial skill diff and status were empty.
Reviewed the resulting diff: one contiguous candidate-lineage hunk, preserving the existing cleanup contract and source-mode restrictions.
Reviewed instruction coherence against native generation, exact template composition, deterministic map geometry, focused edits, and portrait gates.
The official skill validator passed using `python -X utf8 -B C:\Users\klimp\.codex\skills\.system\skill-creator\scripts\quick_validate.py .agents\skills\chaos-redux-event-assets`.
Its initial default-encoding invocation failed on Python's Windows cp1252 decoding; UTF-8 mode resolved that execution issue without a validator or skill encoding rewrite.
The validator covers skill packaging, not future agent behavior or asset provenance; no new generation or runtime evidence is claimed here.

No simplifications or omissions were made in this bounded skill task.
No blockers remain for the skill edit; parent review and the isolated shared-tree commit remain the parent's responsibility.
No AGENTS.md or subagent-skill routing update is needed.
