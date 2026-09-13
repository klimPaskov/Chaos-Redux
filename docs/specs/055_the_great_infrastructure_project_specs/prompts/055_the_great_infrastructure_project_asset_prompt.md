# Asset Production Prompt for Event 55

Create the complete visual asset package for Chaos Redux Event 55, The Great Infrastructure Project.

Read `AGENTS.md`, `chaos-redux-event-assets`, `chaos-redux-frame-animation` only if a later accepted change adds animation, the Event 55 source specs, and the matching installed vanilla reference families before creating any file.

Use the narrow asset subagents with context-complete prompts. Use `chaosx_generated_event_art` for report, news, and category picture art. Use `chaosx_icon_artist` for category, decision, mission, idea, state modifier, and achievement icons. No portrait work is required.

## Required assets

### Opening report event image

- Event-owned report image
- Verify the current report-event consumer and reference canvas, expected `210x176`
- Generated period-authentic documentary scene
- Show a large public works mobilization with workers, surveyors, cranes, earthworks, rail grade, viaduct, or a major road cut
- The scale should feel unusual but physically grounded
- Avoid a map as the main subject, modern machinery, modern safety clothing, readable generated text, conference rooms, and generic staff tables

### First major multinational network news image

- News image for the first fully operational network with at least three sovereign participants
- Verify the current news-event consumer and reference canvas, expected `397x153`
- Generated period press photograph
- Show freight movement through a new international bridge, border interchange, port, or railway junction
- Keep national identity dynamic by avoiding prominent fixed flags or readable signs

### Decision category icon

- Inspect the exact category icon reference family and consumer
- Native transparent ImageGen source
- One strong silhouette combining rail, bridge, and road convergence
- Readable at final size

### Static decision category picture

- Inspect `icons/decision_categories/pictures` and its contact sheet
- Verify final consumer size, with `114x101` as the current reference-family expectation
- Full-canvas scene or montage with a viaduct, highway cut, port crane, and freight movement
- No fake buttons, meters, route lines, labels, values, or other simulated controls

### National works institution idea icons

Create a coordinated staged family for the national works institution and its overextended condition.

- Verify the idea or national spirit consumer, expected `64x64`
- Native transparent ImageGen source
- Use survey instruments, blueprint rolls, rail wheel, bridge geometry, and civic engineering symbols
- Each stage must be separately designed for its target role
- Do not resize a focus-style or category image into an idea icon

### Project family decision icons

Create one distinct decision-specific icon for each primary family:

- continental railway
- continental highway
- international trade corridor
- underwater tunnel
- great bridge
- grand port
- resource corridor
- continental network

Verify the exact decision consumer, expected `32x32`. Use native transparency, strong silhouettes, dark edge definition, and minimal interior detail. These may share a coordinated palette and motif, but every icon needs its own source art.

### Mission icons

Create mission-specific icons for:

- survey and charter
- partner negotiation
- procurement
- main construction
- repair
- rerouting
- commissioning

Inspect the mission reference family. Do not satisfy these roles by resizing decision icons.

### State and status icons

Create only icons that have a real visible consumer after implementation confirms the need:

- major fixed-link or port state modifier
- route disruption or maintenance status when the selected UI surface uses an icon

Do not create art for hidden markers.

### Achievement icons

Create completed `64x64` icons and the required grey and not-eligible variants for all five achievements in the achievement prompt:

- From Sea to Sea, working label
- No Mountain Is High Enough, working label
- Steel Thread of Nations, working label
- Master Builder, working label
- The Relief Artery, working label

Follow the achievement reference family and overlay rules. Keep each icon readable without text.

## Source and processing rules

- Use native transparency for all alpha-backed icon families.
- Preserve source PNGs, processed PNGs, final DDS files, prompts, hashes, and source-mode notes.
- Validate transparent corners, edge quality, internal opacity, alignment, and final-size readability.
- Do not use primitive local drawings, resized unrelated icons, contact sheets, or placeholder geometry as final art.
- Keep each asset type separate. Category, idea, decision, mission, state modifier, and achievement art are not interchangeable.
- Place final runtime files under event-scoped engine folders using `055_the_great_infrastructure_project`.
- Register stable proposed sprite names in the handoff. The parent implementation agent owns final non-portrait GFX wiring.
- Create a contact sheet for every generated family.
- Write a full manifest and `gfx_handoff.md` in the temporary event asset workspace.
- Keep the temporary workspace while implementation is active or blocked. Before final event completion, promote durable provenance and coverage facts, verify no runtime reference points into `docs/assets/`, then delete the temporary Event 55 workspace.

## Review gate

Reject and regenerate any asset with modern objects, unreadable generated text, white matte, opaque square background where alpha is required, bad crop, bleeding, clipping, weak silhouette, inconsistent framing, or art derived by resizing another asset type.

Do not add animation, portraits, flags, 3D models, or super-event art unless a later accepted source specification explicitly adds that surface.
