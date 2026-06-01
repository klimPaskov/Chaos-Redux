# Event 006 News Image Source Tranche Handoff

Scope:
- bounded sourced Event 006 Independence Wave news image asset package
- created only the two requested news sprites
- no `.gfx`, gameplay, localisation, GUI, decisions, focuses, scripted files, spreadsheet, or flag edits

## Files created

- `docs/assets/006_independence_wave/news_event_images/manifest.md`
- `docs/assets/006_independence_wave/news_event_images/gfx_handoff.md`
- `docs/assets/006_independence_wave/news_event_images/source/news_event_independence_wave_partition_week_source_changing_face_of_europe_1945.jpg`
- `docs/assets/006_independence_wave/news_event_images/source/news_event_independence_wave_league_source_bundesarchiv_league_chamber_1930.jpg`
- `docs/assets/006_independence_wave/news_event_images/processed_png/news_event_independence_wave_partition_week.png`
- `docs/assets/006_independence_wave/news_event_images/processed_png/news_event_independence_wave_league.png`
- `gfx/event_pictures/news_event_independence_wave_partition_week.dds`
- `gfx/event_pictures/news_event_independence_wave_league.dds`

## Sources selected

### `GFX_news_event_independence_wave_partition_week`
- source page: `https://www.loc.gov/item/81690522/`
- source download used: `https://upload.wikimedia.org/wikipedia/commons/5/50/Changing_face_of_Europe_and_colonial_tension%2C_late_1945._LOC_81690522.jpg`
- archive / author: United States. Central Intelligence Agency; Library of Congress host record
- rights: public domain U.S. government work / LOC free-to-reuse note
- date: `1945`
- reason chosen: strongest bounded sourced fit for the "many new borders, maps" direction at the requested news-event aspect ratio

### `GFX_news_event_independence_wave_league`
- source page: `https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_102-09042,_Genf,_V%C3%B6lkerbund,_Sitzungssaal.jpg`
- source download used: `https://upload.wikimedia.org/wikipedia/commons/6/60/Bundesarchiv_Bild_102-09042%2C_Genf%2C_V%C3%B6lkerbund%2C_Sitzungssaal.jpg`
- archive / author: unknown photographer; German Federal Archives
- rights: `CC BY-SA 3.0 DE`
- date: `1930`
- reason chosen: exact League of Nations chamber imagery read better at `397x153` than later candidate conference photographs

## Processing and conversion

- Reference news images inspected before processing:
  - `.agents/skills/chaos-redux-event-assets/assets/news_event_images/news_event_001.png`
  - `.agents/skills/chaos-redux-event-assets/assets/news_event_images/news_event_002.png`
- Processing used local ImageMagick only:
  - exact crop to `397x153`
  - grayscale conversion
  - contrast shaping toward period-news readability
  - explicit opaque alpha added before DDS export so final DDS writes as `ARGB8888`
- DDS conversion command family:
  - `convert -define dds:compression=none`

## Validation run

- `file docs/assets/006_independence_wave/news_event_images/processed_png/news_event_independence_wave_partition_week.png`
- `file docs/assets/006_independence_wave/news_event_images/processed_png/news_event_independence_wave_league.png`
- `file gfx/event_pictures/news_event_independence_wave_partition_week.dds`
- `file gfx/event_pictures/news_event_independence_wave_league.dds`
- visual inspection against reference folder completed
- no-flag-scope check: no flag files created or modified in this tranche

Validation result:
- processed PNG previews: both `397x153`
- final DDS files: both `397x153`, `32-bit color, ARGB8888`

## Remaining risks and uncertainty

- `GFX_news_event_independence_wave_partition_week` is a period map rather than a photographed newsroom or telegraph office. It matches the allowed "many new borders, maps" branch of the brief, but if the parent wants a more human or office-centered composition, a new source pass would be needed.
- `GFX_news_event_independence_wave_league` uses a 1930 League chamber image. It is institutionally exact, but earlier than the preferred 1936-1945 band. This is documented in the manifest instead of hidden.
- Parent still owns all `.gfx` wiring and gameplay/event references.
