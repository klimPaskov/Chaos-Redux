# Event 006 Independence Wave News Event Image Manifest

Package scope: bounded sourced news image package for Event 006 Independence Wave only.

Current status: wired. `interface/006_independence_wave_news_event_images.gfx` exists and the current Event 006 news-event DDS texture references resolve. This package is not a current playable-wrap-up blocker; later severe-patron, border-war, or high-chaos news variants are optional future polish.

Reference inspection completed:
- `.agents/skills/chaos-redux-event-assets/assets/news_event_images/news_event_001.png`
- `.agents/skills/chaos-redux-event-assets/assets/news_event_images/news_event_002.png`

DDS conversion note:
- Local conversion used `convert -define dds:compression=none`.
- Processed PNG previews were exported as `397x153` RGBA files with an explicit opaque alpha channel so the final DDS files would export as `32-bit color, ARGB8888`.
- `file` reports both final DDS files as `Microsoft DirectDraw Surface (DDS): 397 x 153, 32-bit color, ARGB8888`.

Processing note:
- This tranche used sourced archival or official historical imagery only.
- News images were cropped to exact `397x153`, converted to black and white, and contrast-shaped toward the existing Chaos Redux news-event reference look.

No-flag note:
- No country flag files were created or modified in this tranche.

## Assets

### `GFX_news_event_independence_wave_partition_week`
- Asset type: news event image
- Intended in-game use: Event 006 global release-wave / border-shock / partition-week beat
- Related event id: `006`
- Related event slug: `independence_wave`
- Source mode: sourced archival image
- Source URL: `https://www.loc.gov/item/81690522/`
- Source download: `https://upload.wikimedia.org/wikipedia/commons/5/50/Changing_face_of_Europe_and_colonial_tension%2C_late_1945._LOC_81690522.jpg`
- Author / archive: United States. Central Intelligence Agency; Library of Congress Geography and Map Division host record
- License / public-domain status: public domain U.S. government work; LOC rights note says Geography and Map Division digitized content is free to use and reuse unless stated otherwise
- Source date: `1945`
- Why it fits Event006: the world map foregrounds shifting borders, colonial tension, and a sudden multiplication of state lines, which reads directly as a large-scale independence-wave news image rather than a local battlefield or one-country ceremony
- Event006-origin specificity: specifically supports the Event 006 global-fragmentation presentation and does not imply Event 005 Soviet-collapse origin
- Era-fit note: exact late-1945 geopolitical map, period-correct for the mod's documentary-news treatment
- Source file: `docs/assets/006_independence_wave/news_event_images/source/news_event_independence_wave_partition_week_source_changing_face_of_europe_1945.jpg`
- Processed PNG: `docs/assets/006_independence_wave/news_event_images/processed_png/news_event_independence_wave_partition_week.png`
- Final DDS: `gfx/event_pictures/news_event_independence_wave_partition_week.dds`
- Target size: `397x153`
- Sprite name: `GFX_news_event_independence_wave_partition_week`
- Asset status: `complete`
- Uncertainty / needs_user_review: the selected source is a period map rather than a newsroom or telegraph-office photograph; this still matches the brief's allowed "many new borders, maps" direction and reads clearly at HOI4 news size

### `GFX_news_event_independence_wave_league`
- Asset type: news event image
- Intended in-game use: Event 006 league / congress / diplomatic-chamber beat
- Related event id: `006`
- Related event slug: `independence_wave`
- Source mode: sourced archival image
- Source URL: `https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_102-09042,_Genf,_V%C3%B6lkerbund,_Sitzungssaal.jpg`
- Source download: `https://upload.wikimedia.org/wikipedia/commons/6/60/Bundesarchiv_Bild_102-09042%2C_Genf%2C_V%C3%B6lkerbund%2C_Sitzungssaal.jpg`
- Author / archive: unknown photographer; German Federal Archives (`Bundesarchiv`)
- License / public-domain status: `CC BY-SA 3.0 DE` with Commons attribution line `Bundesarchiv, Bild 102-09042 / CC-BY-SA 3.0`
- Source date: `1930`
- Why it fits Event006: the League of Nations chamber is an exact institutional match for a small-state congress or league-formation news beat, with delegates, benches, galleries, and a central dais that still read clearly after a wide crop
- Event006-origin specificity: specifically frames the Event 006 coalition or league route as a diplomatic assembly, not a Soviet-collapse republic congress or unrelated wartime summit
- Era-fit note: pre-war but period-authentic interwar diplomatic imagery; institutionally exact for the brief's League of Nations option
- Source file: `docs/assets/006_independence_wave/news_event_images/source/news_event_independence_wave_league_source_bundesarchiv_league_chamber_1930.jpg`
- Processed PNG: `docs/assets/006_independence_wave/news_event_images/processed_png/news_event_independence_wave_league.png`
- Final DDS: `gfx/event_pictures/news_event_independence_wave_league.dds`
- Target size: `397x153`
- Sprite name: `GFX_news_event_independence_wave_league`
- Asset status: `complete`
- Uncertainty / needs_user_review: the image is from 1930 rather than 1936-1945, but it is the exact League chamber requested by the brief and avoided the weaker readability of later candidate conference photos
