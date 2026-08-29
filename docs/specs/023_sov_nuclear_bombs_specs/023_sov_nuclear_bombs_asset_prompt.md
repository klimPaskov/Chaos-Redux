# Event 023 asset-production prompt

Create the complete final visual asset package for Chaos Redux Event 23, `sov_nuclear_bombs`, using the accepted specification folder `docs/specs/023_sov_nuclear_bombs_specs/`.

## Required reading

Read before production:

- `AGENTS.md`.
- `chaos-redux-event-assets`.
- `chaos-redux-super-events` for the exchange image.
- `chaos-redux-frame-animation` to confirm that no animation is requested.
- `chaos-redux-subagents`.
- Event 23 Part 8 and Part 10.
- The current runtime sprite definitions and matching vanilla-reference contact sheets for every asset family.

Do not begin final generation until the parent locks every runtime basename, sprite name, target folder, and exact canvas from the live consumer.

## Scope

Create final source art, processed PNG previews, DDS files, contact sheets, manifests, and handoffs for the approved Event 23 assets.

This asset package has no portraits, flags, country tags, faction emblems, custom units, counters, equipment art, 3D models, skeletal animation, or frame-sheet animation.

Do not create an absent asset family.

## Subagent routing

Use `chaosx_generated_event_art` for:

- Decision-category picture.
- Opening event picture.
- Test report picture.
- Accident report picture.
- Public-test news picture.
- Nuclear-ultimatum news picture.
- First Soviet combat-use news picture.
- Breakaway-custody news picture.
- First multi-major exchange super-event image.

Use `chaosx_icon_artist` for:

- Decision category icon.
- National spirit progression icons.
- Decision icons.
- Mission icons.
- Seven achievement triplets.

Use `chaosx_asset_source_researcher` only when the parent deliberately selects a real archival image. Do not mix a sourced historical person or real event into a generated package without recording that source mode.

Every project subagent uses `fork_context=false` and receives exact files, names, dimensions, references, and handoff paths.

## Visual direction

Use period-authentic 1930s to 1940s Soviet industrial, laboratory, military, rail, civil-defense, and command imagery.

Generated event art should look like documentary photography or restrained period illustration. It must avoid modern computers, modern weapons, modern protective equipment, readable generated text, maps as the main subject, interface overlays, title cards, and cinematic science-fiction design.

Nuclear devices should appear as heavy controlled industrial objects. Do not use glowing fantasy cores.

Nuclear use and accidents must not be celebratory. Avoid gore and visible bodies.

## Required static picture assets

Lock final names with the parent. Working list:

1. `sov_nuclear_command_category_picture`.
2. `sov_nuclear_arsenal_opening`.
3. `sov_nuclear_test_report`.
4. `sov_nuclear_accident_report`.
5. `sov_nuclear_public_test_news`.
6. `sov_nuclear_ultimatum_news`.
7. `sov_nuclear_first_use_news`.
8. `sov_nuclear_breakaway_custody_news`.
9. `sov_nuclear_major_exchange_super_event`.

Follow Event 23 Part 8 for the subject and avoidance notes for each image.

## Required icon families

### Category icon

One dedicated Event 23 category icon.

### National spirit family

Create distinct icons for:

- Secret Soviet Arsenal.
- Demonstrated Arsenal.
- Coercive Arsenal.
- Retaliatory Command.
- Unrestrained Release.
- Broken Chain.
- Atomic Moratorium.

Keep the family coordinated while giving every stage its own asset-type-specific source art.

### Decision icons

Create separate icons or deliberate within-family reuse for:

- Accounting.
- Storage hardening.
- Reactor construction.
- Device assembly.
- Delivery preparation.
- Command exercise.
- Authentication.
- Test-site survey.
- Concealed test.
- Public test.
- Counterintelligence.
- Target selection.
- Private signal.
- Public ultimatum.
- Wartime demonstration.
- Strike preparation.
- Final authorization.
- Hold or abort.
- Hotline and stand-down.
- Dismantlement.
- Depot recall.
- Rail security.
- Joint custody.
- Recovery raid.
- Device disablement.

Do not satisfy mission or spirit assets by resizing these decision icons.

### Mission icons

Create dedicated mission art for:

- Test preparation.
- Ultimatum response.
- Strike preparation.
- Retaliation window.
- Rail corridor security.
- Breakaway technical access or operationalization.
- Joint-custody transfer.
- Dismantlement inspection.

### Achievement triplets

Create complete eligible, grey, and not-eligible DDS states for:

- `023_sov_nuclear_bombs_a_hundred_suns`.
- `023_sov_nuclear_bombs_the_bomb_never_fell`.
- `023_sov_nuclear_bombs_ultimatum_without_ash`.
- `023_sov_nuclear_bombs_scattered_arsenal`.
- `023_sov_nuclear_bombs_firebreak`.
- `023_sov_nuclear_bombs_first_and_last`.
- `023_sov_nuclear_bombs_the_last_telephone`.

Use the exact root achievement naming rule and matching vanilla achievement canvas.

## Processing and placement

Use the event-scoped working folder `docs/assets/023_sov_nuclear_bombs/` during active work.

Final runtime assets should use verified folders under:

- `gfx/event_pictures/023_sov_nuclear_bombs/`.
- `gfx/interface/ideas/023_sov_nuclear_bombs/`.
- `gfx/interface/decisions/023_sov_nuclear_bombs/`.
- `gfx/super_events/023_sov_nuclear_bombs/`.
- `gfx/achievements/` for achievement triplets.

The parent owns final non-portrait `.gfx`, `.gui`, gameplay, localisation, and spreadsheet wiring.

## Quality gates

- Inspect the exact reference family and contact sheet before every asset type.
- Preserve source PNGs and prompts.
- Produce true transparency where the verified family uses transparency.
- No checkerboard remnants, white halos, opaque square backgrounds, or chroma outlines.
- Icons remain readable at final size.
- Separate icon types use separate source art.
- DDS files use the repository conversion workflow and pass decoded review.
- Contact sheets show native-size alignment and transparency.
- Every final file has a manifest row.
- `gfx_handoff.md` names final paths, sprites, sizes, source mode, and consumer.
- The super-event image is distinct from Fallout and any Final Silence image.
- No placeholder or primitive locally drawn final art is accepted.

## Handoff

Write the asset handoff under:

`docs/plans/023_sov_nuclear_bombs_plans/subagent_handoffs/`

List every source file, final file, checksum, sprite proposal, consumer, reference inspected, review status, and blocker.

The parent must review and wire the package. Do not claim Event 23 implementation completion from asset production alone.
