# Famine and Migration Decision-Category Picture Prompts

## `fm_pic_displacement`

Source mode: native built-in ImageGen generation with no reference image and no sourced or archival input.

Generation record: the source artifact was generated at `C:\Users\klimp\.codex\generated_images\01a0295b-d43a-73c3-a244-097a71ae8231\exec-368ef70e-8164-4ae8-adc7-8b1bb9ee91b6.png` and preserved in the repository as `docs/assets/famine_and_migration_system/category_picture/source_png/fm_pic_displacement_source.png`.

Prompt:

> Create a single original HOI4 decision-category picture for a serious 1936–1945 famine and displacement system. Depict a wartime railway platform being used as a civilian reception and relief station: a steam locomotive and covered platform in the middle distance, civilians with modest luggage and bundled belongings moving through the station, two period relief staff checking a paper manifest without any readable writing, handcarts and stacked crates, a railway signal and distant smoke. Documentary-style historical painted photograph, restrained sepia and charcoal palette with muted rust accents, dignified human scale, clear central silhouette and strong value separation so it remains legible when reduced to a tiny 114×101 category-picture canvas. Opaque full-canvas background from edge to edge. Period-accurate 1930s–1940s clothing, rail infrastructure, luggage and vehicles only. No flags, no national insignia, no portraits, no graphic injury, no bodies, no modern objects, no modern clothing, no plastic, no contemporary barriers, no map, no interface, no buttons, no meters, no labels, no logos, no watermarks, no readable text, no fake signage. Wide composition with the most important people, luggage and relief activity inside the central safe area; do not use a portrait crop or a transparent background.

## Processing record

The generated RGB source was cover-cropped with Pillow to the 114×101 consumer aspect ratio using Lanczos resampling and a 0.51 horizontal composition center, then received a restrained 1.04 contrast and 1.08 sharpness adjustment for tiny-canvas legibility.

The processed PNG is RGBA only because the repository pipeline stores four-channel PNG previews; its alpha channel is forced to 255 for every pixel so the runtime category picture remains fully opaque.
