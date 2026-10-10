# Event 085 — Visual Asset Production Prompt

Produce the Ten Plagues visual package from [Part 16](085_ten_plagues_of_egypt_spec_part_16_visual_presentation_and_assets.md), which holds the inventory, scene directions and icon subjects.
Read the README and Parts 7, 16, 17 and 18 first, then follow the repository rules and the `chaos-redux-event-assets` and `chaos-redux-subagents` skills.
Read the skill's reference library (`.claude/skills/chaos-redux-event-assets/assets/gfx_references/README.md`, `CATALOG.md` and the matching contact sheets) and the native consumer definitions before production.

## Scope

- 16 report pictures, 6 news pictures, 4 super-event pictures and 12 category pictures: original generated period scenes, each its own composition.
- 3 national spirit icons, 14 decision icons and 12 achievement subjects: original symbolic art with genuine transparency.
- 91 static outputs in total; the Darkness presentation is resolved separately by the parent (Part 7).
- No flags, portraits, focus icons, formable puzzles, 3D animals or skeletal animation.

## Sizes and processing

- Reports 210 × 176 with the skill's report-card processing; news 397 × 153 black and white; super-events 457 × 328; ideas 64 × 64; decisions 32 × 32; achievements 64 × 64 per state.
- Category pictures: inspect the actual category consumer and lock its canvas before production.
- Convert ordinary outputs with `.claude/skills/chaos-redux-event-assets/tools/convert_to_dds.py` and verify the DDS format, size and alpha.
- Achievement triplets: one subject per Part 18 icon direction, then the template-based colored, grey and not-eligible sources processed with `.claude/skills/chaos-redux-event-assets/tools/process_achievement_icons.py`; runtime files go directly in `gfx/achievements/` under the final IDs supplied by the parent.

## Placement

Use event folders such as `gfx/event_pictures/085_ten_plagues_of_egypt/`, `gfx/super_events/085_ten_plagues_of_egypt/`, `gfx/interface/ideas/085_ten_plagues_of_egypt/` and `gfx/interface/decisions/085_ten_plagues_of_egypt/`.
Keep source PNGs, prompts, intermediates and contact sheets in `docs/assets/085_ten_plagues_of_egypt/`.

## Delegation and handoff

Route scenes to `chaosx_generated_event_art` and icons to `chaosx_icon_artist` with self-contained prompts per `chaos-redux-subagents`.
Workers do not edit `.gfx` files; they return a manifest and `gfx_handoff.md` with sprite names, textures, consumer conditions and open questions.
The parent wires the assets and reviews every family at native size.
No placeholder art, fabricated provenance or transform-only animation is accepted.
