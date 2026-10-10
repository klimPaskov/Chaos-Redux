# Military Madness Asset Production

Produce the 2D asset package for Event 087, Military Madness.
Read Parts 1, 5 and 6 and the achievement prompt, then follow the repository rules and the `chaos-redux-event-assets` and `chaos-redux-subagents` skills.
This assignment produces assets and handoffs only; it changes no gameplay and creates no units, portraits or interfaces.

## Sources and routing

Every scene is fictional period documentary art and every icon is original symbolic art; no real person or historical photograph is requested.
Route the four report scenes to `chaosx_generated_event_art` and the spirit icon and achievement subjects to `chaosx_icon_artist`, each with a self-contained prompt per `chaos-redux-subagents`.
Use the image-generation route defined in the event-assets skill, with native transparency for icon subjects and no fake checkerboards or chroma backgrounds.
Read the reference library at `.claude/skills/chaos-redux-event-assets/assets/gfx_references/` (README, catalog and the contact sheets for ideas, achievements and report images) before production.

## Four report images

Generate full-canvas 1936–1945 period photographs first; do not ask for the finished card, frame or transparent corners.
No readable text, watermarks, interface fragments, modern optics or recognizable public figures.

1. `report_event_military_madness`: a close military test scene with an analog instrument driven past its range and a field exercise behind it, with no readable digits.
2. `report_event_military_insanity`: an implausibly successful combined exercise with one dominant action and a few supporting details, not a collage.
3. `report_event_impossible_warfare`: a period force moving with extraordinary ease through severe terrain or weather, suggesting possibility rather than a guaranteed roll.
4. `report_event_gods_of_war`: overwhelming coordinated movement across a vast period battlefield, with no gods, fantasy armor, modern electronics or new unit types.

Process each approved scene with `.claude/skills/chaos-redux-event-assets/tools/process_report_event_image.py` into the 210 × 176 black-and-white sepia card, convert with the skill's DDS converter, and place it at `gfx/event_pictures/087_military_madness/<name>.dds` with the sprite `GFX_<name>`.

## One national-spirit icon

`idea_military_madness`, 64 × 64, at `gfx/interface/ideas/087_military_madness/idea_military_madness.dds` with the sprite `GFX_idea_military_madness`.
A damaged military chronometer or overdriven mechanical gauge with a compact martial silhouette, reading as a temporary impossible advantage rather than a technology.
Aged material, strong value contrast, native alpha, no text, frame, digital display or tiny detail.
There is one icon for the combined effect; the package rows reuse it.

## Three achievement subjects

Read the objectives in Part 6 first.

- `087_military_madness_minor_major_offensive`: a small standard overcoming a much larger fortress or military symbol.
- `087_military_madness_core_recovery`: a damaged homeland shield restored around a planted standard.
- `087_military_madness_hold_after_expiry`: a stopped chronometer beside a still-held standard and intact position.

Follow the skill's [achievement contract](../../../.claude/skills/chaos-redux-event-assets/references/icon-and-ui-families.md#achievement-icons): one original transparent subject, the immutable templates and unchanged overlay, the full three-state source set and `process_achievement_icons.py`.
Final files sit directly in `gfx/achievements/` as `<id>.dds`, `<id>_grey.dds` and `<id>_not_eligible.dds`.

## Evidence

Keep source PNGs, prompts, candidate lineage, processed files and native-size contact sheets in `docs/assets/087_military_madness/`.
Verify the DDS format, exact dimensions, alpha and, for achievements, template and overlay integrity.
Return a `gfx_handoff.md` with each path, sprite or achievement ID, size, source mode and status, and the handoff under `docs/plans/087_military_madness_plans/subagent_handoffs/`.
All fourteen runtime textures need a coverage row; the parent wires them and the user validates them in game.
