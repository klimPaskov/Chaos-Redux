# Event 016 Directorate background refresh handoff

## Scope

This bounded handoff replaces only the two Event 016 Kruger Directorate scripted-GUI wallpaper textures. It does not edit `.gui`, `.gfx`, gameplay, localisation, spreadsheets, or focus files.

## Delivered assets

- `gfx/interface/016_brilliant_scientist/directorate/directorate_background.dds` — exact `500x620` one-level uncompressed BGRA DDS, sprite `GFX_kruger_directorate_background`.
- `gfx/interface/016_brilliant_scientist/directorate/directorate_compact_header.dds` — exact `500x58` one-level uncompressed BGRA DDS, sprite `GFX_kruger_directorate_compact_header`.
- Source, processed PNGs, decoded DDS previews, contact sheet, prompt, manifest, crosswalk, and validation live under `docs/assets/016_brilliant_scientist/directorate_ui/background_refresh/`.

## Visual direction and layout fit

The new art is native built-in ImageGen output for fictional Kruger Directorate UI art, not a resize or crop of the previous `700x500` wallpaper. It uses a blue-black enamel and oxidized-brass wartime laboratory dossier language. Functional bays are dark, matte, quiet, and free of generated text, maps, focal diagrams, portraits, or bright ornament. Laboratory/alchemical detail is restricted to frame hardware, edge tubing, pinlights, rivets, and subtle separators. The compact header is an exact crop of the new full panel top strip.

The fixed parent zones reviewed against the final `500x620` candidate are header `x0-499 y0-67`, profile dossier `x14-181 y74-309`, telemetry/control `x192-485 y74-205`, navigation `x14-485 y316-345`, tab content `x14-485 y352-573`, and footer `x14-485 y584-609`.

## Evidence

Source master: `docs/assets/016_brilliant_scientist/directorate_ui/background_refresh/source_png/directorate_background_master_v2.png`, `1127x1396` RGB, SHA-256 `2EA81E0CCF78C7C8A33B72360AC82601F06A56C098A00FC7841BCA3AC0900D7F`.

Full panel processed PNG SHA-256: `74C7861A03C816A4CAD9320B53D78DD3CCD6B5F42811A491FAFD612024C1BE3A`.

Full panel DDS SHA-256: `E743D0DC392B83718823D2CA66884D8CBEECEBF9FA9B3679C23FF23ED941A90E`; exact length `1,240,128` bytes; decoded dimensions `500x620`; alpha `255..255`.

Compact-header processed PNG SHA-256: `14D121DCD68AB37AA68845180F3A8763824C96ABCD008C98072176BBE3BE6642`.

Compact-header DDS SHA-256: `CE5E4B184B75488FDBABA0981CAB71E913D3A246CD7886CF03867D58B8CB73E2`; exact length `116,128` bytes; decoded dimensions `500x58`; alpha `255..255`.

`validation.json` confirms legacy `DDS ` header, `DDS_HEADER` size `124`, `DDS_PIXELFORMAT` size `32`, flags `65`, 32-bit BGRA masks, `DDSCAPS_TEXTURE`, expected file lengths, declared dimensions, and decoded pixel equality for both files.

## Parent-owned follow-up

Parent should review the contact sheet and decoded DDS, keep the stable sprite names and paths, and wire the new `500x620`/`500x58` surfaces into the revised 502px decision-grid GUI. Final in-game click-region, clipping, and visual acceptance remain parent-owned.

## Parent review disposition

Accepted on 2026-08-05 after native-size review of the decoded full panel, compact header, and contact sheet. The shell provides quiet functional bays at the parent-authored coordinates, restricts bright detail to the frame and separators, contains no generated text or focal artwork beneath controls, and matches the existing blue-black enamel and oxidized-brass Directorate assets. The two stable runtime sprites are wired by `interface/016_brilliant_scientist_directorate.gfx` and consumed by the 500-pixel layout in `interface/016_brilliant_scientist_directorate.gui`.

Status: accepted for static runtime use. Live in-game consumer acceptance remains user-owned.
