# Receipt-generation skill maintenance

Date: 2026-10-08.
Role: `chaosx_skill_maintainer`.
Disposition: `implemented` for the bounded skill maintenance; parent review and selective commit remain parent-owned.
Acceptance basis: the standing full-goal user instruction remains active, and the explicit bounded parent/user assignment authorizes these generic receipt-publication and membership-cleanup lessons without a new permission request.
This acceptance covers the skill update and this handoff; it does not establish acceptance or completion of additional gameplay work.

## Owned files and intake

The October 9 parent review found that subsequent owner maintenance had replaced the earlier placement, so the October 8 byte receipts and OWNEDPATCH below are historical.
The parent reapplied the same generic publication and separate-owner generation rules in the current Event anatomy owner section, under `Generation receipts and cleanup`.
Its final cleanup wording distinguishes rejection of a frozen row from an explicitly accepted direct retirement of stale local receipts, which never authorizes world-relation removal.
Only that current additive section belongs to publication; the broader current skill rewrite remains another owner's work.
No event-specific identifier, variable, path or example is introduced in the maintained skill.

- Updated `.agents/skills/chaos-redux-events/SKILL.md` with three generic paragraphs in two additive hunks.
- Created `docs/plans/006_independence_wave_plans/subagent_handoffs/receipt_generation_skill_20261008.md`.

`HEAD` captured by direct metadata reads: `ec33fb3be8bb12385bb04b61219cefdec5e52542` (`ref: refs/heads/master`).
The complete working-intake skill bytes were captured in session memory before editing; the intake includes existing foreign dirty changes and is the comparison baseline, not HEAD.
Intake: 102647 bytes; SHA-256 `88037fc7f66e0d02c766ece6f381f12fc82cbdb4314caa4ce0bf909952c78f4a`; UTF-8 without BOM; 901 CRLF and 88 LF-only endings.
Result at write verification: 104004 bytes; SHA-256 `e2fa9277b37d37619296ada9ae95ad72c326f4dd63b891f27f39ae9c2b3479bd`; 906 CRLF and 94 LF-only endings.
Owned delta: 1357 bytes and 11 added physical lines, comprising eight sentence lines and three blank lines; the zero-context OWNEDPATCH has 15 lines including its headers.
Removing exactly the two inserted byte sequences reproduced the captured intake byte-for-byte and its SHA-256, preserving all foreign intake content and existing mixed endings.
No Git command or index access was used; no commit, mirror synchronization, workbook/export, engine-source edit, game/log access, paid model operation, RunPod operation, or visual generation was performed.

## Confirmed lessons and source limits

[Publication source audit](d34_dynamic_target_source_audit_20261008.md), lines 141–178, records the parent-applied publication-generation correction and its 26 actual-source assertions.
The reusable lesson is that an immutable provenance tuple owns a publication-generation receipt independently of mutable cache membership: same-generation row repair preserves the tuple, partial receipt loss rejects reconstruction, and a validated genuine newer generation can publish a new tuple.
The first-publication condition requires a validated unpublished identity with all tuple receipts absent; a missing cache row alone cannot authorize it.
The cited source-model results were read, not rerun here, and do not establish native engine behavior or probability completion.

[Member-generation cleanup review](form48_member_generation_cleanup_20261008.md), lines 9–66 and 79–88, confirms the wrong-owner generation comparison and destructive cleanup occurring before adequate frozen-row identity proof.
The reusable lesson is to match each entity to its own generation snapshot, validate the counterpart separately, and verify the actual country, matching frozen generation row, and exact binding before every destructive response, idea, flag, or relation clear.
Exact owned relation directions must be undone before their ownership/binding receipts are cleared, while failed validation retains precise recovery evidence and unowned relations remain intact.
That handoff records its owner correction as accepted and queued; this maintenance neither applies it nor promotes it to implemented.

## Unchanged guidance and skill dispositions

The existing helper-output lifetime, fresh-consumption receipt, bounded queue retention, ROOT/PREV tracing, frozen nested transaction inputs, nonce validation, and dead-actor cleanup guidance remain byte-for-byte unchanged.
The additions extend the existing `Helper output lifetime` and `Country activation and ROOT` sections without duplicating their tests or inventing a registry API.
Skills used: `chaos-redux-events`, `chaos-redux-subagents`, and official `skill-creator`.
Skill updated: `chaos-redux-events`; skills created: none; `chaos-redux-subagents`, `skill-creator`, and the existing skill references were left unchanged.
No routing contract changed, so no AGENTS.md or subagent-skill update is required.
Existing event-specific material elsewhere in the dirty skill was preserved rather than expanded or cleaned up outside the owned hunks.

## Validation and parent handoff

`python -B C:\Users\klimp\.codex\skills\.system\skill-creator\scripts\quick_validate.py .agents\skills\chaos-redux-events` returned `Skill is valid!`.
Reviewed each added sentence against the cited confirmed findings, the existing receipt/scope guidance, and the bounded generic-only instruction.
The additions contain no event/country identifiers, tags, one-off variable names, paths, examples, or fabricated APIs.
Only the captured-intake-to-result OWNEDPATCH below belongs to this skill-maintenance change; do not attribute or commit the entire existing dirty skill diff to this subagent.
The parent should review these two hunks and this handoff, then make the authorized selective commit under its existing shared-tree procedure.
Completed: the requested generic guidance and handoff.
Blocked work: none within the granted maintenance scope.
Uncertainty: native behavior, gameplay correction status beyond the cited handoffs, and probability evidence remain parent-owned and were not revalidated here.
Simplifications, omissions, and fallbacks: none within this bounded assignment.

## OWNEDPATCH against captured working intake

```diff
--- a/.agents/skills/chaos-redux-events/SKILL.md
+++ b/.agents/skills/chaos-redux-events/SKILL.md
@@ -191,0 +192,5 @@
+Give every immutable birth/provenance tuple its own publication-generation receipt and publish the complete tuple together.
+Mutable array/cache row presence or absence is not first-publication authority; first publication requires a validated unpublished identity with all tuple receipts absent.
+Same-generation missing or stale row repair must preserve the old tuple rather than restamp it from mutable current fields.
+Partial receipt loss fails closed rather than reconstructing from mutable fields; renewal may publish a new tuple only for a genuine validated newer generation proven against the publication receipt.
+
@@ -571,0 +577,6 @@
+
+Match each entity's current generation to its own birth or installation snapshot, and validate the counterpart's generation separately against that counterpart's snapshot.
+Never compare member generation to carrier generation as proof of shared identity, or infer a missing member receipt from the carrier snapshot.
+
+Before every destructive response, idea, flag, or relation clear during bounded frozen-member cleanup, verify the actual member country, its matching frozen generation row, and the exact current binding.
+Undo only the exact owned relation directions before clearing their ownership and binding receipts; failed validation must preserve the receipts needed for precise recovery and leave unowned relations intact.
```
