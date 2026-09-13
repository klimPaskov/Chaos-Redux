# Asset production prompt

Create the complete authorized visual package for Chaos Redux Event 036, Chemical and Biological Weapons Convention.

Before producing anything, read:

- `AGENTS.md`
- `chaos-redux-event-assets`
- `chaos-redux-frame-animation` only to confirm that the accepted package is static
- `14_asset_requirements.md`
- `13_achievements.md`
- the matching vanilla reference README, catalog, and contact sheets
- the active runtime consumers and existing Chaos Redux precedents

Use `chaosx_generated_event_art` for the report image and static category picture.

Use `chaosx_icon_artist` for the category icon, decision icons, visible idea icons that have real consumers, and achievement triplets.

Spawn every project subagent with a complete context-free prompt and no inherited conversation context.

## Required package

Produce:

- one Event 036 report image
- one static decision-category picture
- one decision-category icon
- thirteen separate decision icons listed in the asset spec
- up to four separate idea or doctrine icons only when the final implementation has a visible consumer
- seven separate achievement masters and their normal, grey, and not-eligible states

Do not satisfy one asset type by resizing or lightly editing another asset type.

## Visual direction

Use a period-authentic 1930s or 1940s diplomatic and military visual family.

The main subjects are delegates, treaty papers, gas masks, sealed cylinders, laboratory equipment, protective equipment, inspection tools, delivery-system silhouettes, industrial work, and research facilities.

The report image should show an international conference that treats forbidden weapons as ordinary policy subjects.

The category picture should establish the treaty system’s identity without painting fake controls.

Icons need a strong centered silhouette, limited interior detail, a dark outline, and a subtle shadow where the consumer uses transparent unused canvas.

Avoid readable generated text, modern conference technology, modern tactical gear, science-fiction UI, generic map tables, gore, fake checkerboards, white halos, and opaque icon squares.

## Source and processing rules

Use native ImageGen for generated art.

Request genuine transparency in the initial call for every alpha-backed icon family and preserve it through processing and DDS conversion.

Keep the source PNG, processed preview, final DDS, prompt, source mode, dimensions, alpha mode, and review evidence.

Use background removal only as a recorded fallback after native transparency fails.

Inspect the exact current consumer before fixing final dimensions.

Use `210x176` for the report image only when the active report-event consumer confirms it.

Use the decision-category picture reference family’s `114x101` canvas only when the active consumer confirms it.

## Placement and handoff

Place final event-owned runtime assets in event-scoped folders under the correct GFX categories.

Keep achievement DDS files directly under `gfx/achievements/` with filenames matching the full achievement IDs.

Use `docs/assets/036_chemical_biological_weapons_convention/` as the temporary source and evidence workspace.

Write a manifest and `gfx_handoff.md` that list source files, final files, checksums, sprite names, consumers, dimensions, alpha treatment, prompts, review status, and blockers.

Do not edit gameplay, localisation, events, decisions, GUI, or the workbook unless the parent explicitly grants a narrow exception.

Before the event can be marked complete, the parent must wire every accepted asset, promote durable provenance and runtime crosswalk facts into permanent documentation, confirm that no runtime path points into `docs/assets/`, and delete the complete temporary event workspace.

Do not create placeholders or unrequested asset families.
