# Implement and produce Event 078 achievements

Read `docs/specs/078_border_conflict_specs/achievements/078_border_conflict_spec_part_6_achievement_design.md`, the core and frontier specifications, the asset brief, and the current shared achievement implementation.
Follow `AGENTS.md`, the events, event-assets, dynamic-effect, debugging, and relevant specialist skills.
These are difficult multi-condition achievements based on genuine Event 078 results.
The planning package contains no final player-facing localization or generated icons.

Implement `cr_078_many_fronts` for five distinct defeated neighboring countries in one wave, both attacking and defending victories, no Event 078 state loss in that wave, and a 30-day continuous hold of all gains after wave closure.
Implement `cr_078_unbroken_frontier` for five or more captures in one chain and a 90-day continuous hold of all of that chain's gains after it ends.
Implement `cr_078_recovered_frontier` for stopping an enemy chain that took at least five states, recovering its first five captured states through later Event 078 victories against the original opponent, and holding all five for 90 days.
Use the detailed attempt and failure rules in the source specification.

Validate exact country identities, historical targets, wave and chain identity, attribution, continuous ownership and control, and save/load persistence.
Repeated callbacks, technical cancellation, debug-forced results, unrelated state transfers, and reused country tags must not create progress.
Hold objectives must not keep a closed wave eligible for evolution.
Use the existing shared achievement progress and notification surface.

The parent owns the shared registry at `common/achievements/chaos_redux_achievements.txt` and its existing root-level unique identifier structure.
Inspect the actual current file before changing it.
Do not create a parallel achievement registry.
Keep the three achievement IDs aligned exactly with their texture identities and localization keys.

Assign subject art and canonical icon processing to `chaosx_icon_artist` with a bounded self-contained handoff.
Produce one distinct subject source for each achievement and derive its normal, grey, and unavailable states through the canonical templates and processing script.
Inspect `achievement_template.png`, `achievement_template_grey.png`, `overlay.png`, and the current `process_achievement_icons.py` workflow before final production.
All nine final textures are 64 by 64 and follow the shared flat-root naming convention.
Do not hand-generate unrelated alternate-state treatments.

Write final names and descriptions from the design purposes rather than treating the internal handles as approved visible text.
Return exact progress conditions, failure cases, source and asset paths, native-size previews, actual registry validation, persistence tests, and consumer evidence.
Do not report an achievement as complete until its gameplay and icon states both pass the relevant tests.
