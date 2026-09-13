# Event 60 asset production prompt

Create the authorized static visual package for Event 60 Research Failure.
Read `AGENTS.md`, `chaos-redux-event-assets`, the complete Event 60 specification pack, and the matching skill-local vanilla reference catalogs before producing files.
Use the correct narrow asset subagent for generated scene art and the icon artist for icon families.
Do not edit gameplay, localisation, GUI, decisions, events, achievements, or the catalog workbook.

## Event identity

Event 60 depicts the collapse and reconstruction of a national scientific establishment during the 1936 to 1945 visual period.
Its visual subjects are damaged laboratories, scattered technical records, silent measuring instruments, guarded archives, evacuated specialists, improvised institutes, restored standards, and the return of repeatable scientific work.
Avoid modern computers, modern laboratories, futuristic holograms, readable generated text, generic glowing atoms, comedy, gore, maps as the main subject, or a contemporary corporate office.

## Required scene art

### Opening report event picture

Create one full-canvas period documentary scene for the opening incident.
Show a recognizable institutional collapse inside a research facility or technical institute.
Strong subjects include abandoned benches, smashed precision instruments, archive boxes in disorder, empty staff spaces, guarded corridors, and evidence that working knowledge has disappeared.
The composition needs one clear focal area and enough human presence or recent human absence to communicate loss.
Use generated period-authentic documentary art unless implementation research identifies a specific real archive image that the accepted event text requires.

### Decision category picture

Create one static decision category picture based on the inspected vanilla category-picture family and actual runtime consumer.
Show reconstruction work, such as technicians cataloguing recovered records, calibrating instruments, reopening a damaged laboratory, or connecting several institutions.
The picture is presentation only.
Do not paint buttons, meters, labels, fake controls, ledger rows, or readable documents into it.

## Required icon families

Create separate source art for every UI family.
Do not resize a focus-style image to satisfy another family.
No focus icons are authorized.

1. One decision category icon for national scientific reconstruction.
2. About twelve to sixteen decision icons, with final count taken from implemented actions.
3. About three to four mission icons, with final count taken from implemented missions.
4. About seven idea or national-spirit icons for the active collapse, institutional settlements, and Kruger mandate states that actually exist in implementation.
5. Two achievement source icons and their required achievement triplets.

Suggested icon subjects include a broken microscope, recovered archive case, guarded laboratory door, returning scientist, calibration weight or gauge, university workshop, reopened institute, foreign archive exchange, central scientific authority, academy council, international consortium, and sealed Directorate laboratory.
Use one strong silhouette per small icon.

## Transparency and processing

Request genuine native transparency for every alpha-backed icon source.
Preserve alpha through crop, alignment, resizing, contact sheets, and DDS conversion.
Reject white mattes, opaque squares, checkerboard pixels, clipped edges, transparent holes, and weak silhouettes.
Use full-canvas opaque treatment only for the report picture, category picture, and achievement family where the inspected consumer requires it.

Store active source evidence under `docs/assets/060_research_failure/` and final runtime assets under event-scoped folders for their exact asset categories.
Follow root-only achievement naming rules.
Create processed PNGs, final DDS files, contact sheets, a manifest, and `gfx_handoff.md` with stable proposed sprite names and exact runtime paths.

## Authorization boundary

Do not create portraits, advisors, flags, faction emblems, focus icons, technology icons, special-project icons, animation frames, super-event art, 3D models, sound, or unit counters for this event unless a later accepted implementation change explicitly adds a real consumer.
Do not create placeholders for those absent families.

## Review standard

Inspect every final asset at native size and at enlarged nearest-neighbor scale.
The report and category images must read clearly without generated text.
Every icon must remain recognizable at its actual consumer size.
The handoff must list generated prompts, source mode, background mode, reference files inspected, final dimensions, paths, sprites, checksums, review result, and any blocked asset.
