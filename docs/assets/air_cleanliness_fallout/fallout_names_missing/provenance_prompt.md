# Names for the Missing — generation provenance

Source mode: generated with the official built-in ImageGen workflow.

Generation output id: `019f8eff-7f79-7b42-92be-f45ee9e21de3`.

Generated source retained at `docs/assets/air_cleanliness_fallout/fallout_names_missing/source/fallout_names_missing_source.png`.

Prompt:

```text
Use case: historical-scene
Asset type: Hearts of Iron IV report event picture, intended for a 210x176 in-game report panel.
Primary request: a fictional period-authentic documentary photograph of a community census and memorial room inside a cold underground civil-defense shelter during a mid-20th-century global catastrophe. A volunteer archivist sits in profile at a rough wooden desk beneath a single low electric bulb, carefully adding a mark to a large wall ledger. The wall is covered with pinned paper sheets, small hand-drawn family marks, and rows of abstract handwritten strokes suggesting names, but every mark must be illegible at the image's final size and must not form readable words. The emotional tone is quiet, respectful remembrance and communal care rather than panic.
Scene/backdrop: bare poured-concrete shelter room, frost on the edges of a small high window, improvised coat hooks, stacked paper bundles, enamel mug, simple 1940s desk lamp and pencil; no modern infrastructure.
Subject: one non-identifiable volunteer archivist seen from a three-quarter rear angle, bundled in a plain wool coat, face mostly turned away and not recognizable; a wall ledger and family marks are the visual focus.
Style/medium: monochrome sepia archival press photograph from 1936-1945, authentic film grain, soft focus, imperfect exposure, documentary realism, restrained contrast, period darkroom print on off-white paper.
Composition/framing: wide horizontal report composition, archivist on the right third, ledger wall occupying the left and center, readable silhouette and strong focal light; leave no empty modern UI-like space; slightly rotated paper photograph presentation like vanilla HOI4 report art, with clean transparent outside border if possible.
Lighting/mood: cold blue-gray darkness outside, one dim warm electric bulb inside, subdued shadows, solemn but humane.
Color palette: desaturated charcoal, smoke gray, faded sepia, muted cream paper, a tiny warm amber bulb.
Materials/textures: rough concrete, frost, worn paper, pencil and ink strokes, wool coat, scratched wood, dust, period photographic grain.
Text (verbatim): none. Do not render any readable text, letters, numbers, names, signs, logos, watermarks, captions, or UI.
Constraints: fictional scene; no real identifiable person; no readable invented text; no flags; no military insignia; no gore; no bodies; no weapons; no modern props; preserve the memorial and census focus; match the vanilla report-art documentary print aesthetic.
Avoid: generic apocalypse collage, explosions, mushroom clouds, ruined skyline, maps, newspaper headline, propaganda poster, legible handwriting, modern clothing, smartphones, plastic, neon, cinematic color grading, glossy concept art, meme styling, watermark, border text, UI artifacts.
```

Processing note: the generated RGB source was copied unchanged into the package. The connected near-white surround was removed with a conservative flood-fill key, then the image was resized with Lanczos to 210×176 RGBA. Corners are transparent while the warm paper print is retained. The processed PNG was converted with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` to the runtime DDS path.

Vanilla fit: the matching `vanilla_reference/event_art/report` family uses 210×176 sepia documentary prints with a transparent surround. This package preserves that family while making the event-specific subject a fictional shelter census and memorial room.
