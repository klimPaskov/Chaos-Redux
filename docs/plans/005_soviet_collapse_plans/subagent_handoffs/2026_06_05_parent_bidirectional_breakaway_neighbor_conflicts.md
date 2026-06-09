# Parent Handoff: Bidirectional Breakaway Neighbor Conflicts

## Scope

Event005 Soviet Collapse breakaway setup and local breakaway-vs-breakaway hostility.

## Files Changed

- `common/scripted_effects/005_soviet_collapse_effects.txt`

## Change

- `soviet_collapse_setup_breakaway_country` now refreshes `soviet_collapse_apply_breakaway_neighbor_conflict_plan` for the newly set up breakaway and for each existing neighboring Soviet Collapse breakaway.
- This makes later releases and high-chaos successor spawns update local hostility from both sides instead of relying on only the newly released country to notice older neighbors.

## Behavior

- Normal breakaways still gain claims, conquer/antagonize AI, and wargoals against neighboring non-allied breakaways.
- High-chaos successors, terminal collapse, and triggerable collapse paths still escalate the same neighbor conflict helper into direct wars when declaration checks pass.
- Existing neighboring breakaways now also receive their own refreshed conflict plan when a new breakaway appears beside them.

## Validation

- `python3` brace balance check:
  - `common/scripted_effects/005_soviet_collapse_effects.txt`: `brace_balance=0`, `early_closes=0`
  - `common/national_focus/005_soviet_collapse_republics.txt`: `brace_balance=0`, `early_closes=0`
- `git diff --check -- common/scripted_effects/005_soviet_collapse_effects.txt common/national_focus/005_soviet_collapse_republics.txt`: passed.
- `git diff --name-only -- gfx/flags interface/flags`: no output; no flag assets were touched.

## Remaining Risk

- This is a script-level validation only. Live game verification is still needed to confirm exact AI declaration timing after simultaneous multi-country releases.
