# Event 020 remaining report art handoff

The five final non-model report-card packages are wired into the existing Event 020 report chain.

## Runtime files

- `gfx/event_pictures/020_black_plague/report_event_020_black_plague_severe.dds`
- `gfx/event_pictures/020_black_plague/report_event_020_rat_king_crisis.dds`
- `gfx/event_pictures/020_black_plague/report_event_020_crown_strike.dds`
- `gfx/event_pictures/020_black_plague/report_event_020_rat_king_aftermath.dds`

All five are validated 210x176, one-level, uncompressed BGRA DDS report cards with transparent corners.

## Wiring

- `interface/020_black_plague_event_pictures.gfx` registers stable sprite names for all five textures.
- `events/020_black_death.txt` assigns severe, Rat King crisis, Crown Strike, and aftermath cards to their existing Event 020 consumers.

Source and processed evidence, prompts, contact sheet, and the detailed manifest remain under `docs/assets/020_black_plague/`; that folder is ignored by the repository and is not a gameplay dependency.

No 3D models were created or referenced. The Rat Nation and Rat King continue to use the existing valid non-human entity consumers until a future model package is explicitly commissioned.
