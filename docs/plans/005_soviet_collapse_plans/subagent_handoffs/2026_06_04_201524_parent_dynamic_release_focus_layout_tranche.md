# Event005 Dynamic Release and Focus Layout Tranche

Timestamp: 2026-06-04 20:15:24 UTC

## Scope

Parent-agent implementation tranche for the Soviet Collapse release pacing and focus-tree cleanup request.

No `gfx/flags` files were touched.

## Files Changed

- `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/national_focus/005_soviet_collapse_republics.txt`

## Implemented

- Added `has_soviet_collapse_nonbase_republic_release_pressure`.
  - Non-base/internal republics now require live crisis pressure before entering progressive release pools.
  - The gate checks release pressure, release-level component pressure, failed release pressure, regional cascade pressure, war pressure, compound MTTH pressure, total collapse threat, release urgency, sustained progressive release pressure, and failed release months.
- Replaced chaos-tier-only internal progressive release eligibility with the new dynamic pressure trigger.
- Terminal internal republic release now checks the same dynamic pressure trigger instead of opening solely from chaos tier.
- Follow-on release attempts now explicitly zero internal/non-base attempts when the pressure trigger is not true.
- Kazakhstan layout: moved four early route nodes to reduce pathline crossings while keeping the tree compact.
- Belarus layout: moved the evacuation/timetable lane into a cleaner corridor, reducing crossings without widening the tree.

## Validation

- Brace balance:
  - `common/scripted_triggers/005_soviet_collapse_triggers.txt`: depth 0, no early closes.
  - `common/scripted_effects/005_soviet_collapse_effects.txt`: depth 0, no early closes.
  - `common/national_focus/005_soviet_collapse_republics.txt`: depth 0, no early closes.
- Unsupported operators:
  - No `<=` or `>=` in touched files.
- Whitespace:
  - `git diff --check` passed for touched files.
- Focus geometry audit after this tranche:
  - Ukraine: 20 prerequisite-line crossings, 0 duplicate coordinates.
  - Belarus: 34 prerequisite-line crossings, 0 duplicate coordinates.
  - Kazakhstan: 74 prerequisite-line crossings, 0 duplicate coordinates.

## Remaining Work

- Kazakhstan still has too many crossings and needs a broader route-lane cleanup.
- Ukraine remains compact but still has visible pathline issues around the early political/industry split and military/foreign lanes.
- The remaining focus reward spam is helper-layer repetition, not direct focus-level `add_ideas`.
- Custom splinter and factory successor layouts still need separate passes, especially BAC, NLC, UWD, OGB, MFR, and ancient restoration trees.
