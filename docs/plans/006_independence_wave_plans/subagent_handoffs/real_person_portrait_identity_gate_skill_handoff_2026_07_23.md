# Real-person portrait identity-gate skill handoff

Date: 2026-07-23
Owner: chaosx_skill_maintainer
Scope: reusable real-person portrait workflow discovered during Event 006 review; no Event 006 rule was added to the skill.

## Updated skill

`.agents/skills/chaos-redux-event-assets/SKILL.md` now requires the fail-closed sequence of unchanged attributed archival source master, explicit head-and-shoulders crop, source-locked identity-preserving ImageGen repaint in the matching HOI4 family, deterministic `156x210` processing, independent likeness/style/provenance audit by a reviewer other than the producer, and DDS conversion or runtime wiring only after PASS.

Identity preservation is a separate non-compensable gate from style quality, with native and enlarged comparisons of the unchanged master, crop, raw ImageGen result, processed candidate, and role-specific canonical references.

The manifest, requirement-to-runtime audit, section 21, advisor handoff boundary, required workflow, and final checklist now require source hashes, crop and processor evidence, reviewer independence, separate likeness/style/provenance verdicts, and post-PASS conversion evidence.

Raw or merely resized sourced images remain evidence only and never final runtime portraits.

## Validation and coordination

Validated with `python -B C:\Users\klimp\.codex\skills\.system\skill-creator\scripts\quick_validate.py .agents/skills/chaos-redux-event-assets`.

The concurrent technology-inspection hunk in the same skill file was preserved outside this commit and remains available for its owner.

No gameplay, localisation, asset, `.gfx`, advisor processor, or spreadsheet files were changed.
