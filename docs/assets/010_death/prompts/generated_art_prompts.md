## Event 010 Death generated-art prompt record

Tool: official `image_gen`

### Core prompts used

- `leader_zol`: fictional nonhuman HOI4 leader portrait, bust framing, matte-black hooded figure, face-like absence, white eye glow only, subdued 1930s-1940s painterly mood, no gore or ornate fantasy styling.
- `DTH` flag set: full rectangular near-black cloth flag, straight-on view, worn matte fabric, restrained pale broken-ring/void emblem centered, readable at `82x52` and `10x7`, no text or bright colors.
- `report_event_death_mail_boat`: 1936-1945 period-documentary empty island pier and unattended mail boat, no people, black-and-white source for later report-card treatment.
- `report_event_death_lighthouse`: 1936-1945 period-documentary lighthouse over empty island settlement, bleak coast, no people.
- `report_event_death_census`: 1936-1945 period-documentary abandoned census office, blank papers and ledgers, no readable text.
- `news_event_death_mainland_reveal`: 1936-1945 black-and-white press image of emptied mainland coastal town/road, black horizon, no people.
- `news_event_death_defeated`: 1936-1945 black-and-white press image of soldiers and surveyors entering empty dead settlement, no cheering or restoration.
- `super_event_death_reveal`: period-documentary mainland reveal scene, observers dwarfed by empty coastal settlement and black shoreline.
- `super_event_death_world_end`: period-documentary black tide crossing a desolate shore, terminal oceanic mood, no fantasy creature styling.
- `super_event_death_defeat_aftermath`: period-documentary aftermath scene, soldiers and surveyors in dead land, victory without restoration.
- `super_event_death_world_consumed`: period-documentary ruined coastal capital overtaken by a vast black tide, tiny foreground witnesses for scale, no office, no map table, no readable text.
- `super_event_death_black_oath`: 1936-1945 government chamber oath tableau, officials around a sealed black document, looming void witness behind them, no readable text, restrained supernatural presence.

### Local processing notes

- Report images were passed through `.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py`.
- News and super-event images were cover-cropped to target size and normalized to stark grayscale documentary contrast.
- The repository DDS helper `.tools/convert_to_dds.py` was attempted first and failed in this environment on its FFmpeg fallback path with a `struct.pack` header error. Final DDS files were exported with `convert -define dds:compression=none` so the package still contains final in-game files.
