# Loop animation proof skill update handoff

Date: 2026-08-10
Mode: bounded skill-maintenance patch
Status: complete; changes left unstaged and uncommitted as requested

## Exact hunk

Updated `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md` in the skeletal-action validation paragraph (the `Every requested action must have...` paragraph). Loop actions now require first, quarter, middle, three-quarter, and last reimport samples; decoded-pixel or pose/bounds comparison proving the quarter phases differ as intended and loop endpoints return appropriately; and contact and actor-bounds checks at every sampled phase. Non-loop terminal actions retain start/mid/end or role-appropriate samples.

## Why

Three reimport screenshots can miss meaningful loop motion when the midpoint intentionally returns to neutral. The reusable proof rule now requires phase coverage and comparative evidence that can expose that failure mode without relying on event-specific context.

## Validation

- Ran `python C:\Users\klimp\.codex\skills\.system\skill-creator\scripts\quick_validate.py C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-3d-model-pipeline`.
- Reviewed the final diff to confirm the skill change is limited to the generic loop-proof paragraph and the handoff file; unrelated existing worktree hunks were preserved.

## Remaining issues

No gameplay, runtime wiring, asset, event, or event-specific design changes were made. Parent review remains required before relying on the updated skill guidance.
