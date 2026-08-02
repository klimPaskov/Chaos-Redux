# Event 016 news art asset production handoff

Date: 2026-08-02

## Scope

The bounded generated-event-art package produced six Event 016 news-event scenes. It did not produce models, animations, gameplay, localisation, `.gfx`, GUI, events, focuses, decisions, country setup, or spreadsheet edits. The parent owns the gameplay wiring and final validation.

## Files and identifiers

- Active asset workspace: `docs/assets/016_brilliant_scientist/report_news_expansion/`.
- Runtime folder: `gfx/event_pictures/016_brilliant_scientist/`.
- Parent sprite registration: `interface/016_brilliant_scientist.gfx`.
- Six stable sprite names and corresponding event ids are documented in `manifest.md` and `gfx_handoff.md`.
- Presentation events are `chaosx.nr16.304` through `.309`.

## Evidence

- Six source masters under `source_masters/news/`.
- Six generated prompts under `prompts/news/`.
- Six processed `397x153` black-and-white PNG previews under `processed/news/`.
- Six runtime DDS files and six evidence DDS copies under `dds/news/`.
- Contact sheet: `contact_sheets/news_event_016_brilliant_scientist_news_contact_sheet.png`.

The parent independently checked the six runtime files: each is `397x153`, has a 124-byte DDS header, a 32-byte RGB+alpha pixel format with 32 bits per pixel, and exact length `128 + 397 * 153 * 4 = 243092` bytes. Four processed scenes were visually reviewed at native size; they read as period black-and-white documentary compositions without modern UI or generated text.

## Remaining parent work

The parent must review the handoff, retain the active workspace while Event 016 remains incomplete, update the durable Event 016 asset manifest and content map, run focused event/GFX/localisation checks after the six news hooks are wired, and commit the scoped gameplay plus asset changes. No defeat/remnant image was substituted by this package; the qualifying defeat remains in the separate aftermath pipeline. The seven deferred Event 016 3D unit packages remain untouched.
