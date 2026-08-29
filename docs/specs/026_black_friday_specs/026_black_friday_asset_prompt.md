# Event 26 asset production prompt

Create the complete visual asset package for Chaos Redux Event 26, Black Friday. Read `AGENTS.md`, the Event 26 specification package, `chaos-redux-event-assets`, and the matching canonical Vanilla reference families before producing files.

Use separate source art for each asset family. Do not satisfy one family by resizing another.

## Asset 1: report event image

- Runtime basename: `black_friday_report`
- Proposed sprite: `GFX_report_event_026_black_friday`
- Final folder: `gfx/event_pictures/026_black_friday/`
- Source mode: generated period documentary art
- Target: use the current report-event processor and exact current report-event runtime dimensions

Show a crowded late-1930s or early-1940s purchasing scene. Civilians, civil servants, clerks, and uniformed quartermasters rush to secure goods and supply crates. Use invoices, counters, boxes, and period shop fittings to show that civilian shopping and state procurement have merged for one day. Keep one clear focal area and strong readability at report-event size.

Avoid readable generated text, current brands, modern shopping carts, digital displays, modern clothing, modern packaging, cinematic color grading, war-room maps, and violent crowd scenes.

## Asset 2: active-sale idea icon

- Runtime basename: `black_friday_sale`
- Proposed sprite: `GFX_idea_026_black_friday_sale`
- Final folder: `gfx/interface/ideas/026_black_friday/`
- Target: 64 by 64, subject to exact active idea-icon precedent
- Background: real transparency

Create a compact HOI4 idea icon centered on a paper price tag tied to a small gear or supply crate. Use a strong downward graphic mark without readable text. Keep a dark outline, restrained shadow, transparent unused canvas, and one readable silhouette.

## Asset 3: achievement triplet

- Achievement working ID: `026_black_friday_five_departments`
- Final folder: `gfx/achievements/`
- Required files: normal, `_grey`, and `_not_eligible` variants using the full achievement ID
- Target: inspect and match the current installed Vanilla and Chaos Redux achievement family

Create original achievement art showing an overloaded government purchasing desk or ledger with a supply crate, military file, fuel can, and price tag. Use one dominant subject and strong contrast. Do not derive this art from the idea icon.

## Production rules

Use the official image generation route. Preserve prompts and source outputs. Process transparency correctly. Convert through the repository-standard DDS workflow. Review every result at native size and in a contact sheet.

Return:

- generated source PNGs
- processed PNG previews
- final DDS files
- achievement triplet
- exact dimensions and alpha evidence
- contact sheets
- manifest entries
- prompt records
- `gfx_handoff.md` with final paths, proposed sprite names, target `.gfx` file, and use notes
- completed, blocked, and `needs_user_review` status for each asset

Do not edit gameplay, localisation, event, GUI, achievement registry, spreadsheet, or non-portrait `.gfx` files. The parent implementation agent owns final wiring.
