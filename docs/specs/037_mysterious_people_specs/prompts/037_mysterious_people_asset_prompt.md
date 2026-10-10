# Prompt: Event 037 visual assets

Produce the asset inventory in [Part 7](../specs/037_mysterious_people_spec_part_7_assets_achievements_and_catalog.md#asset-inventory) under `.claude/skills/chaos-redux-event-assets/SKILL.md`.
Part 7 owns the inventory, the visual identity, and the forbidden imagery.
The asset skill owns the image-generation route, reference inspection, transparency, processing, DDS conversion, temporary workspace rules, and handoff format.

## Routing

- `chaosx_generated_event_art`: the manifestation report image, the category picture, and the news picture if the review in Part 7 finds the existing one unusable.
- `chaosx_icon_artist`: the category icon, two stance icons, five action icons, the mission icon, the Newcomers modifier icon, and the three achievement triplets.

Each subagent receives a self-contained prompt with this inventory, the exact consumer for each asset, the paths below, and the forbidden imagery.
The parent owns `.gfx` registration and runtime wiring.

## Paths

| Asset family | Final folder |
| --- | --- |
| Report and news images | `gfx/event_pictures/037_mysterious_population/` |
| Category picture, category icon, stance, action, mission, and modifier icons | `gfx/interface/decisions/037_mysterious_population/` |
| Achievement triplets | `gfx/achievements/`, named after the achievement IDs in Part 7 |
| Sprite registration | `interface/037_mysterious_population.gfx` |
| Temporary workspace | `docs/assets/037_mysterious_people/` |

Inspect each live consumer before choosing a canvas.
The vanilla report-event family is the starting reference for the report image, and the existing Chaos Redux decision-category pictures are the reference for the category picture.

## Subjects

Use the subject column in Part 7.
Full-canvas images keep the opaque treatment of their consumer, and icons are transparent.
No readable lettering in any asset.
