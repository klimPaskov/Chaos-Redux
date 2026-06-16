# Event 012 Africa Dynamic Cross-Continent Union Art Handoff

Date: `2026-06-16`
Role: `africa_dynamic_cross_continent_union`
Scope: generated still-package only; no gameplay, localisation, `.gfx`, sound, GUI, or event-file edits.

## Inputs used

- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-16_super_event_missing_roles_text_handoff.md`
- `docs/specs/012_africa_specs/prompts/012_africa_super_event_prompt.md`
- `docs/assets/012_africa/generated_art/manifest.md`
- `docs/assets/012_africa/implementation_asset_manifest.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-super-events/SKILL.md`
- `/mnt/c/Users/klimp/.codex/skills/.system/imagegen/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/assets/super_event_images/`

## Files created

- `docs/assets/012_africa/generated_art/source_png/super_event_012_dynamic_cross_continent_union_source.png`
- `docs/assets/012_africa/generated_art/processed_png/super_event_012_dynamic_cross_continent_union_processed.png`
- `docs/assets/012_africa/generated_art/dds/super_event_012_dynamic_cross_continent_union_processed.dds`
- `docs/assets/012_africa/generated_art/contact_sheets/super_event_012_dynamic_cross_continent_union_variants.png`

## Dimensions

- Source PNG: `1480x1063`
- Processed PNG: `457x328`
- DDS: `457x328`
- Contact sheet: `1371x376`

## Generation and selection notes

- Source mode: generated with built-in `image_gen`.
- Three bounded variants were generated and reviewed against the super-event reference folder.
- Selected final still: the harbor-backed treaty chamber scene where African and non-African delegates seal separate continental charters into one legal instrument.
- Why this variant won: it reads immediately as a transcontinental legal merger, keeps African Charter symbolism present, includes port and convoy context without collapsing into a map, and stays clearly short of the terminal world-union register.

## Visual direction delivered

- Treaty chamber and continental delegates as the main subject.
- African Charter and cross-continental standards/seals in frame.
- Harbor, steamship, and convoy-port context visible through the chamber arches.
- 1936-1945 period clothing and architecture, no modern props, no readable titles, no terminal world-state iconography.

## Documentation updates made

- Added the asset row to `docs/assets/012_africa/generated_art/manifest.md`.
- Added the sprite proposal note to `docs/assets/012_africa/generated_art/gfx_handoff.md`.

## Wiring recommendation for parent

- Current package DDS: `docs/assets/012_africa/generated_art/dds/super_event_012_dynamic_cross_continent_union_processed.dds`
- Proposed final in-mod DDS: `gfx/event_pictures/super_events/super_event_012_dynamic_cross_continent_union.dds`
- Proposed sprite: `GFX_super_event_012_dynamic_cross_continent_union`
- Suggested target `.gfx` file: `interface/012_africa.gfx`, alongside the existing Event 012 super-event still sprites

## Use notes

- Keep the super-event title dynamic by actual formed union name. Do not hardcode one static title onto this still.
- Recommended dynamic title examples from the text handoff remain:
  - `African-Middle Eastern Union`
  - `Afro-Asian Union`
  - `Afro-Eurasian Union`
- Use this still for the federative or congress-scale merger role only. Do not reuse it for the terminal `World Is One` branch.

## Validation

- Verified processed PNG dimensions at `457x328`.
- Verified DDS dimensions at `457x328`.
- Visually reviewed the final processed still and the variant contact sheet.

## Non-actions

- No gameplay, localisation, `.gfx`, sound, GUI, event, focus, decision, history, or spreadsheet files were edited.
