# Handoff 11: focus trees, country packages and standalone decisions

Read `00_common_rules.md` in this folder first. This handoff can run at the same time as all the others.

## Why

Same reason as the event audits, for the content that is not owned by one event file set.

## Tasks

1. **Focus trees.** For every Chaos Redux focus tree, compare today's tree with its history over the last 1 month. Restore focuses, branches, rewards, mutual exclusions, icons and descriptions that were removed, merged or made generic without an owner request. The one known owner request is removing "Last Fury Standing" (done in the small-fixes round; do not bring it back). Read `.claude/skills/chaos-redux-focus-trees/SKILL.md` first.
2. **Country packages.** For every Chaos Redux country (history files, leaders, portraits, flags, parties, ideas, advisors, units, names): restore anything replaced or removed without request. Portraits and flags are compared byte for byte with their earlier versions.
3. **Standalone decisions and categories** not owned by an event (chemical, biological, raids, camps, condemnation, Chaos Meter, debug): restore removed decisions and earlier costs, visibility and tooltips; category icons are category icons and decision icons are decision icons.
4. **Ideas and modifiers:** restore earlier values and descriptions changed in bulk; idea icons are idea-size.
5. **AI.** Where a restore brings back a decision, focus or ability, restore its AI weights from the same commit.

## Deliverable

`docs/plans/content_regression_audit_2026-10-13.md`: per tree, country and decision group, what was found, restored or kept and why, with commits.
