# Asset coverage skill handoff

Date: 2026-10-03.
Disposition: implemented within the user's explicitly authorized skill-maintenance scope.

## Changed files and ownership

- `.agents/skills/chaos-redux-event-assets/SKILL.md`: two paragraphs added at lines 980-982 within `Requirement-to-runtime coverage audit`.
- `docs/plans/014_cannibalism_plans/subagent_handoffs/2026-10-03_asset_coverage_skill_handoff.md`: this handoff.

No skill was created.
The portrait-production reference, subagents skill, events skill, routing, source-mode rules, and AGENTS.md were left unchanged.
No gameplay, assets, runtime identifiers, or consumer wiring were changed, and no files were staged or committed.
No parent routing update is needed.

## Existing coverage and new rule basis

The existing asset skill already requires every accepted requirement row to link its source package, runtime registration, live consumer, conditional binding, and current audit evidence.
It rejects count-only completion proof, requires a refreshed crosswalk after accepted requirement changes, and keeps source placeholders pending final acceptance.
The portrait reference already locks runtime identifiers and distinguishes source-placeholder and styled-final states.
These rules remain intact.

The demonstrated missing gate was the substitution of a partial source-archive/crop receipt for a full current consumer inventory before changing wiring or completion counts.
The user's task reports a 16-package receipt extrapolated into the full consumption count, followed by a fresh registry audit showing 64 aliases resolving to 56 distinct runtime textures, all wired.
The inspected `2026-10-03_regional_portrait_consumption_audit.md` lines 3-15 and 25-27 report the complete matrix, shared base/European aliases, 56 distinct file hashes and decoded-pixel hashes, and source-placeholder status rather than accepted finals.
That handoff is the evidence basis, not an independently rerun inventory by this maintainer.
Its inspected SHA-256 is `6d873ece6252c35dc6ac942d450b1fd25879abf4afa80224332ff12b0d334db2`.

The addition requires the full current required logical-slot-to-registered-alias-to-runtime-path matrix before a wiring or completion-count change, including conditional/regional variants and shared-path aliases.
It requires preserving source revisions/hashes, runtime file hashes, and declared coverage bounds before the change.
It separates file inventory, alias consumption, source provenance/archive packages, and final acceptance, with separate unique runtime-path, whole-file-hash, and decoded-pixel-hash counts.
Partial receipts and historical totals cannot substitute for current consumer evidence.
No event names, event counts, or task history were added to the skill.

## Validation and limits

Reviewed the exact target diff: one insertion hunk with two paragraphs and no other skill edits.
Compared the final file against an in-memory snapshot of the inspected pre-edit bytes with only that insertion applied, confirming every pre-existing byte is preserved.
The pre-edit skill SHA-256 was `e896c152bb35487595af0c34f8f8f0abb962f01d0414d7c99d8953ad11bb3d76`.
The post-edit skill SHA-256 is `7a728ccbab2ccf3483b1932a99ba971622f5086767bd2cfa76c313a4ef02b279`.

Official validation passed with `python -X utf8 -B C:/Users/klimp/.codex/skills/.system/skill-creator/scripts/quick_validate.py .agents/skills/chaos-redux-event-assets`.
The first invocation used Windows' default cp1252 and failed decoding the skill, so it was rerun in UTF-8 mode without changing file encoding or the validator.
Manual review against the reported failure confirms that a partial archive receipt cannot establish consumer coverage, shared aliases do not inflate the unique-path count, and wiring does not establish final acceptance.
The validator checks skill structure, not agent behavior or runtime asset coverage.
No engine validation or asset re-audit was performed because this assignment changes skill instructions only.

Required guidance used: AGENTS.md, official `skill-creator`, `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-event-assets`, and the relevant portrait-production reference.
No simplifications or omissions were made in the authorized update.
No blocked work or additional user review is required for this skill change.
The underlying portrait acceptance and source-provenance findings remain with the parent and their audit evidence.
