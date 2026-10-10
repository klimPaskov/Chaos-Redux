# Achievement implementation brief

Use the current `chaos-redux-events`, `chaos-redux-event-assets`, and `chaos-redux-subagents` skills for Event 048 achievements.
Read `CLAUDE.md` and the package README for authority and evidence boundaries.
Read `../matrices/048_old_great_bulgaria_achievement_matrix.csv`, `../specs/048_old_great_bulgaria_spec_part_6_assets_super_events_achievements.md`, and the parent's exact tracking consumers, files, acceptance basis, and handoff path.
Preserve unrelated work and report every missing dependency or omitted requirement.

Implement the achievement matrix as real route challenges with stable tracking, disqualifiers, localisation, and the full normal/grey/not-eligible icon triplets. Do not convert difficult route conditions into automatic formation rewards.

## Ownership and handoff

The parent owns achievement scripting and final integration.
Route only the bounded icon package to `chaosx_icon_artist`; it does not own gameplay, localisation, or workbook edits.
All specialists receive self-contained prompts with no inherited context.
Write the bounded handoff under `docs/plans/048_old_great_bulgaria_plans/subagent_handoffs/` at the exact path supplied by the parent.
