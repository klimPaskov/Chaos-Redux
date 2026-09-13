# Event 47 BOOM asset prompt

Use `chaos-redux-event-assets` and route generated non-icon work to `chaosx_generated_event_art` with a complete context-free prompt.

## Required asset

Create one static report-event image for Event 47 BOOM.

- Working asset ID: `047_boom_report`
- Asset type: full-canvas report-event scene
- Expected review canvas: 210 by 176 pixels, subject to confirmation against the installed consumer
- Proposed final DDS path: `gfx/event_pictures/047_boom/047_boom_report.dds`
- Proposed sprite name: `GFX_report_event_047_boom`
- Background mode: consumer-opaque full scene
- Source mode: generated with native ImageGen
- Animation: none

## Scene direction

Show a huge mushroom cloud rising above a populated or industrial region during the 1936 to 1945 visual period. The camera should be far enough away to show the cloud's scale, the pressure front, darkened structures, and a broad damaged horizon. The image should read as period documentary photography or a period press photograph.

The event has no known attacker. Avoid every clue that would identify delivery or ownership.

Do not include:

- visible missile, bomb, aircraft, artillery piece, or launch site
- national flags, unit markings, or recognizable weapon-owner insignia
- radiation symbols
- modern vehicles, buildings, protective suits, cameras, or emergency equipment
- readable text, headlines, captions, watermarks, or signs
- a map, target marker, command table, or UI layout
- gore or visible bodies
- science-fiction energy beams or portals
- supernatural creatures or a confirmed cause

The cloud can resemble a thermonuclear detonation. The image must remain visually ambiguous about the cause.

## Reference and processing requirements

Inspect the canonical report-event reference family and its contact sheet before generation. Inspect the exact installed sprite and GUI consumer to confirm canvas, crop, and DDS requirements.

Preserve:

- the original generated source image
- the full prompt and source mode
- processed PNG preview
- final DDS
- contact sheet showing the source and final crop
- manifest with dimensions, paths, sprite proposal, status, and review notes
- `gfx_handoff.md` entry for the main agent

The final image must remain readable at the actual report-event size. The mushroom cloud, horizon, and destruction should still be clear after downscaling.

## Acceptance

The asset passes when it is period-consistent, has no attacker clue, has no modern object, has no generated text, fills the full canvas, uses the correct aspect ratio, survives final-size review, and has a complete runtime handoff.
