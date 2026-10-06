# Fallout report-scene ImageGen prompts

All five sources below were generated or edited with the built-in ImageGen tool. Source scenes are opaque because the photographed interior fills the report image; the shared tilted transparent print frame is applied downstream. The door-list and open-city scenes required by the fix plan were generated as new 1940s-looking sources. Health Without Borders was a targeted edit of its existing scene.

## R01 — `open_the_sealed_city`

Reference: canonical `report_event_soldiers_marching.png`, period-photo style anchor only.

```text
Use case: historical-scene. Asset type: opaque source scene for a Hearts of Iron IV Fallout report image, 210x176 landscape crop. Primary request: an original documentary-style archival photograph showing a sealed city opening after years of isolation. Depict a 1940s industrial city street seen from street level as a heavy cordon gate is pulled open; a few distant civilians in period wool coats move toward the entrance, ruined masonry and old tram wires recede into a hazy skyline. Make it feel like an authentic mid-20th-century press photograph: natural overcast light, silver-gelatin grain, gentle contrast, no modern styling. Composition is broad and readable in a small report window with important people and the gate near the center. No modern glass towers, modern cars, LED signs, logos, flags, readable signs, text, poster lettering, watermark, or close-up faces. Image 1 is a canonical HOI4 report-photo style reference only; borrow its period-documentary tone and print softness, never its subjects or exact composition. Keep a complete opaque scene across the canvas; sepia framing is applied after generation.
```

## R02 — `door_list`

Reference: canonical `report_event_airplane_crash.png`, period-photo style anchor only.

```text
Use case: historical-scene. Asset type: opaque source scene for a Hearts of Iron IV Fallout report image, 210x176 landscape crop. Primary request: an original 1940s-style documentary photograph of a bomb-shelter door and a posted resident list. Show a heavy riveted steel shelter door in a worn underground corridor, a small cream sheet fixed at eye level with only a few vague handwritten tally-like strokes that are not letters, numbers, or readable writing, and faint chalk marks on the adjacent concrete. The image should feel like a genuine mid-20th-century archival press photograph: monochrome silver-gelatin, subtle film grain, natural hard lamp light, plain industrial materials. Composition: the door dominates but fits entirely in frame; sheet and hardware are visible without legible text. No modern hospital equipment, digital screens, modern construction, logos, flags, signage, legible text, watermark, close-up human faces. Image 1 is a canonical HOI4 report-photo style reference only; borrow its period-documentary tone and print softness, never its exact subject or composition. Keep a complete opaque scene across the canvas; sepia framing is applied after generation.
```

## R03 — `dead_city_permit` after review

Reference: canonical `report_event_airplane_crash.png`, period-photo style anchor only. This new upright scene replaced a parent-rejected upside-down, blurred crop.

```text
Use case: historical-scene. Asset type: opaque replacement source for the Hearts of Iron IV Fallout event report "Dead City Permit", intended for a 210x176 tilted-print composition. Generate a sharp, upright mid-20th-century documentary press photograph. Subject: a municipal clerk's hands stamping a completely blank permit sheet on a scarred wooden desk, with a deserted, damaged city street visible through a cracked office window behind it; a plain stamp and a small brass key suggest controlled entry. Compose the foreground paper and stamp clearly while keeping the ruined city legible in the background. Authentic 1940s film texture and lens, natural overcast daylight, crisp enough to remain readable at 210x176. No upside-down scene, no tilt within the photo, no blur, no watercolor or painting, no readable text, no letters, no numbers, no signage, no logos, no flags, no watermark, no close-up faces. Image 1 is a canonical report-photo style reference only; borrow archival silver-gelatin texture and print contrast, never its subject or exact composition. Keep a complete opaque scene; the shared sepia tilted frame is applied after generation.
```

## R04 — `orchard_flowers` after review

Reference: canonical `report_event_african_soldiers.png`, period-photo style anchor only. This new documentary photograph replaced a parent-rejected soft, undersized framed crop.

```text
Use case: historical-scene. Asset type: opaque replacement source for the Hearts of Iron IV Fallout event report "Orchard Flowers", intended for a 210x176 tilted-print composition. Generate an original upright 1940s documentary photograph of a survivor orchard in spring. Clear foreground branches carry many small apple blossoms, and a gardener in plain period work clothes inspects a young graft among rows of full-size fruit trees; a low ruined farm wall and distant hills add context. The image should look like a real silver-gelatin press photograph, not a painting or miniature: strong photographic detail, natural cloudy light, moderate depth, balanced tonal range, subjects sized to fill the frame. Do not show close-up faces. No modern tools or buildings, no text, labels, logos, flags, signage, watermark, fake paper border, or blur. Image 1 is a canonical report-photo style reference only; borrow archival grain and documentary contrast, never its subject or exact composition. Keep the full scene opaque; the shared sepia tilted frame is applied after generation.
```

## R05 — `health_without_borders` sign edit

Image 1 is the exact existing source target `report_event_fallout_health_without_borders_source.png`.

```text
Use case: precise-object-edit. Asset type: edited opaque source photograph for the Hearts of Iron IV Fallout report "Health Without Borders". Input Image 1 is the exact edit target. Preserve its 1940s post-apocalyptic relief-clinic street scene, people, composition, perspective, lighting, atmosphere, and all scene content. Edit only the sign on the right-side storefront: remove every readable word, letter, number, and logo; replace the text area with a blank weathered plaster panel and a few faint non-letter brush marks. Keep the original sign board in place. Do not add text anywhere else or alter the people. Maintain the same full-opaque photo canvas. The shared sepia tilted frame is applied later.
```

## Existing-source report processing

No ImageGen prompt was used for the other 25 report images. The original runtime DDS files were archived and decoded to source PNGs. The sepia grade was sampled from the interior of `report_event_fallout_school_vent_room.dds`. The frame-edge layer was derived from `report_event_air_winter_phase_1.dds`; the final alpha mask matches that source exactly. Every report output is 210x176.
