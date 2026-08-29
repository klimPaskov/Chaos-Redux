# Event 32 asset-production prompt

## Role

Use `chaos-redux-event-assets` and the appropriate bounded asset workers to create the complete visual package for Event 32, Missiles.

Read these files first:

- `docs/specs/032_missiles_specs/032_missiles_spec_part_7_assets_text_and_achievements.md`
- `docs/specs/032_missiles_specs/032_missiles_achievement_prompt.md`
- `docs/specs/032_missiles_specs/032_missiles_decision_mission_prompt.md`
- `AGENTS.md`
- `chaos-redux-event-assets`
- `chaos-redux-frame-animation`

Inspect the exact installed-vanilla and Chaos Redux consumer for every asset before production. Do not infer dimensions or sprite types from the labels below when the active consumer proves a different contract.

## Hard scope boundary

This package contains no character portrait, flag, focus icon, faction emblem, custom country art, super-event art, custom 3D model, skeletal animation, or frame-sheet animation.

Do not create those asset families. Event 32 reuses existing rocket-site, missile, raid, explosion, and CBRN runtime entities. A missing suitable runtime entity is an implementation blocker that requires a separate accepted brief.

All planned Event 32 art is static.

## Reference gates

Inspect the matching canonical reference folders and their contact sheets:

- report art: `assets/vanilla_reference/event_art/report/`
- news art: `assets/vanilla_reference/event_art/news/`
- decision category icons: `assets/vanilla_reference/icons/decision_categories/`
- decision category pictures: `assets/vanilla_reference/icons/decision_categories/pictures/`
- idea icons: `assets/vanilla_reference/icons/ideas/`
- decision icons: `assets/vanilla_reference/icons/decisions/`
- mission icons: `assets/vanilla_reference/icons/missions/`
- achievement icons: `assets/vanilla_reference/icons/achievements/`
- state modifier icons: `assets/vanilla_reference/icons/state_modifiers/`
- military raid icons: `assets/vanilla_reference/icons/military_raids/`
- modifier and texticon precedents: the exact installed consumer and the closest canonical modifier family

If the decision-category picture contact sheet is missing, create it first, label filenames and native dimensions, and update the reference README and catalog before making the Event 32 picture.

## Main event images

### Country report image

Create generated period-authentic documentary art for a report-event canvas, normally `210x176`.

Show guarded military engineers around a heavy missile canister or newly completed buried launch entrance. The location should look usable in a 1936 campaign without copying one modern national system. Keep national insignia absent, labels unreadable, and the machinery practical. Do not show an explosion, mushroom cloud, satellite view, or modern digital control room.

Suggested runtime basename: `032_missiles_country_report`.
Suggested sprite: `GFX_report_event_032_missiles_country_report`.

### First global news image

Create generated black-and-white press-photo art for a news canvas, normally `397x153`.

Show several launch columns or transport silhouettes across a broad military landscape with distant launch smoke. Suggest worldwide proliferation without using a world map. Do not add readable headlines or country flags.

Suggested runtime basename: `032_missiles_global_proliferation_news`.
Suggested sprite: `GFX_news_event_032_missiles_global_proliferation`.

### Decision category picture

Create a static category picture after inspecting the exact category consumer, with `114x101` used only when the active precedent confirms it.

Show a hardened launch entrance or underground command console as one clear focal subject. Do not paint fake buttons, meters, dynamic values, or text into the image.

Suggested basename: `032_missiles_program_category`.
Suggested sprite: `GFX_decision_category_032_missiles_program`.

## Decision category icon

Create a separate category-button icon after inspecting its exact consumer. Use a compact missile canister and command-key motif that remains readable at native size. Do not resize a decision, idea, or category-picture asset.

Suggested basename: `032_missiles_program_category_icon`.
Suggested sprite: `GFX_decision_category_icon_032_missiles_program`.

## Program and state icons

Create separate source art for each exposed variant. Do not recolor or resize another icon family as a substitute.

Idea or national-spirit family:

- initial missile program
- mature strategic command
- compromised command

State-modifier family, limited to states that the implementation exposes:

- active launch site
- hardened launch site
- damaged launch site
- compromised launch site
- rogue launch site

Create three custom texticons with exact consumer-compatible definitions:

- operational missile reserve
- launch readiness
- command control

Each texticon needs a compact shape that remains readable beside a number. Use the same visual identity in category text, costs, tooltips, and status localisation.

## Decision icons

Create one decision-surface icon for each visible action that survives the final implementation review:

1. survey launch state
2. establish command authority
3. replenish reserve
4. restore readiness
5. improve guidance
6. secure launch codes
7. harden site
8. expand capacity
9. establish secondary site
10. select missile target
11. precision strike
12. strategic barrage
13. saturation barrage
14. counterforce strike
15. integrate special payload
16. inspect incident
17. compensate neutral victim
18. suspend damaged site
19. rotate emergency codes
20. isolate site
21. send loyal forces
22. negotiate with command
23. scuttle site
24. verify warning
25. delay retaliation
26. sever network
27. restore retaliation network

Use separate source art designed for the decision canvas. Merge assets only when the coding agent has merged the underlying actions and the resulting icon remains accurate.

## Mission icons

Create distinct mission-surface art for:

- launch-state survey
- secondary-site construction
- site repair
- strike preparation
- site recovery
- warning verification
- retaliation-network restoration

Do not satisfy these by renaming or resizing the decision icons.

## Raid and payload icons

Inspect the exact native raid adapter and existing CBRN raid assets before adding anything.

Create new Event 32 operation icons only when no matching installed or Chaos Redux icon already represents the same delivery and payload surface:

- conventional missile raid
- saturation missile raid
- chemical missile delivery
- biological missile delivery
- nuclear missile delivery
- thermonuclear missile delivery

Reuse must be exact and documented. Do not duplicate a chemical, biological, nuclear, or thermonuclear icon under a new filename only for Event 32.

## Achievement icons

Create the full completed, grey, and not-eligible triplet for all eight achievements in `032_missiles_achievement_prompt.md`.

Use the working icon directions in that file. Achievement art must be original 64x64 achievement-surface art and cannot be a resized decision, idea, or focus icon.

Achievement files remain directly under `gfx/achievements/` and must match the final achievement IDs exactly.

## Source and processing rules

Use generated source art for the fictional worldwide proliferation scenes and symbolic icons. Preserve the prompt and original source output for every generated asset.

For transparent icons, require real transparency, centered composition, a dark outline, a subtle shadow, no white halo, no fake checkerboard, and no opaque square background.

For every accepted asset, produce:

- original source PNG
- processed PNG at exact target dimensions
- final DDS in the engine-facing folder
- native-size contact sheet
- decoded DDS review evidence where the workflow supports it
- manifest entry with source mode, prompt, dimensions, hashes, final path, sprite proposal, and status
- `gfx_handoff.md` entry for every sprite or texticon

Use the temporary workspace `docs/assets/032_missiles/` while production or review is active. Before the event is complete, move durable provenance and coverage facts into permanent Event 32 documentation, verify that no runtime consumer points into `docs/assets/`, and delete the event-scoped temporary workspace.

## Completion boundary

The asset worker does not edit event logic, decisions, ideas, state modifiers, raids, scripted effects, localisation, GUI, achievements, or the catalog workbook unless the parent grants a narrow exception.

Report every blocked, rejected, merged, reused, or omitted asset. Do not use placeholders, primitive local drawings, resized unrelated icons, or unapproved substitutes.
