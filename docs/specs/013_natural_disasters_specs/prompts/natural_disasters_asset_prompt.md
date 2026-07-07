# Asset prompt for Event 013 Natural Disasters

Use `chaos-redux-event-assets` and `chaos-redux-frame-animation` for every animated asset. Inspect the relevant reference folders before creating source art or processing files.

## Package scope

Create an asset package for Event 013 Natural Disasters. Use event-scoped final folders where the engine surface allows it. Do not edit gameplay files, localisation, GUI, GFX, or spreadsheets unless a parent prompt explicitly grants that scope.

## Source mode rules

Generated assets are appropriate for fictional, symbolic, abnormal, or impossible disaster scenes. Sourced archival images are appropriate for ordinary report or news images only when a suitable, licensed, era-fitting source is found. Do not use modern disaster photography for 1936 to 1945 style event art unless explicitly approved.

## Required static assets

| Asset group | Target size | Source mode | Direction |
| --- | ---: | --- | --- |
| Report event images | 210x176 | generated period-documentary or sourced archival | earthquake, flood, cyclone, wildfire, blizzard, heat, drought, dust, volcano, tsunami, meteor, regional aftermath. Use report-card treatment. |
| News event images | 397x153 | generated black-and-white news or sourced archival | first major family news and abnormal disaster news. |
| Super-event images | 457x328 | generated | abnormal disaster age, rupture wave, skyfall, massive eruption, moving storm corridor, delayed tsunami chain. |
| Decision category icon | repository category pattern | generated icon | Natural Disaster Aftermath category. |
| Decision icons | 32x32 | generated icon | rescue, evacuation, rail repair, port closure, medical corridor, food relief, firebreak, ash cleanup, winter fuel, water trains, observatory watch, reconstruction. |
| Idea and state modifier icons | 64x64 | generated icon | damaged transport, refugee pressure, ashfall, famine risk, disease risk, blocked ports, scorched state, frozen supply, cracked ground, crater aftermath. |
| Achievement icons | 64x64 | generated icon | one completed icon per achievement working id, plus grey and not-eligible variants when the achievement pipeline is ready. |
| GUI panel assets | target from implementation pattern | generated or UI art | disaster map panel, card backgrounds, selected state cards, warning frame, progress meter frames, family markers. |

## Animated assets

Each animated asset needs a frame plan, source frames, processed frames, sheet PNG, sheet DDS, static fallback DDS, preview GIF for review, manifest entry, and GFX handoff.

| Animated asset | Target surface | State logic | Direction |
| --- | --- | --- | --- |
| `013_storm_corridor_path` | abnormal disaster GUI | current path and next-hit segment | moving path pulse with readable storm marker. |
| `013_tsunami_wavefront` | abnormal disaster GUI | delayed wave approach | wavefront sweep across affected coast marker. |
| `013_meteor_marker` | abnormal disaster GUI | impact cluster and next possible strike | falling or blinking meteor marker frames. |
| `013_ash_plume_drift` | abnormal disaster GUI | ash spread and airfield risk | plume drift drawn per frame, not opacity filter. |
| `013_rupture_pulse` | abnormal disaster GUI | rupture wave and aftershock risk | seismic pulse marker frames. |
| `013_recovery_warning_border` | aftermath card | card near failure threshold | warning border loop with static fallback. |

## Manifest requirements

Record asset name, event id, asset type, source mode, prompt or source link, license or public domain notes if sourced, source PNG path, processed PNG path, final DDS path, target size, sprite name, target GFX file, status, and notes. For animation, also record frame count, FPS, loop behavior, static fallback, sheet size, and source mode for each frame.

## Reference folders to inspect

- `.agents/skills/chaos-redux-event-assets/assets/report_event_images`
- `.agents/skills/chaos-redux-event-assets/assets/news_event_images`
- `.agents/skills/chaos-redux-event-assets/assets/super_event_images`
- `.agents/skills/chaos-redux-event-assets/assets/decisions`
- `.agents/skills/chaos-redux-event-assets/assets/ideas`
- `.agents/skills/chaos-redux-event-assets/assets/achievements`

## Second-pass GUI and recovery asset additions

Use the abnormal scripted GUI map file as the source for UI asset names and states. The following asset families are required as planned assets, not placeholders:

- abnormal disaster map background, 580x410, generated UI panel art with static readable map silhouettes and no readable generated text.
- motion lane frame, 540x88, with normal, selected, warning, and completed variants.
- coming-next state card, 176x72, with normal, urgent, hit, and missed variants.
- impact pulse overlay, 64x64, frame-sheet animation with static fallback.
- tsunami path ribbon, 520x24, frame-sheet animation with static fallback.
- tornado track ribbon, 520x24, frame-sheet animation with static fallback.
- meteor rain overlay, 320x210, frame-sheet animation with static fallback.
- ash plume overlay, 300x190, frame-sheet animation with static fallback.
- rupture wave overlay, 560x130, frame-sheet animation with static fallback.
- state recovery card icons for rescue, stabilization, reconstruction, foreign relief, blocked logistics, and partial success.
- decision category icon for Event 013 recovery, designed as a disaster aftermath category icon rather than a generic authority seal.
- achievement icons for all Event 013 achievements, including the renamed no-global-announcer achievement key.

Every animated asset needs real source frames, a horizontal frame-sheet DDS, a static fallback DDS, a GIF preview for review only, a contact sheet, and a `gfx_handoff.md` entry. Do not create final animation by shifting, scaling, recoloring, blurring, or pulsing one still image. Use the frame-animation skill for frame plans.
