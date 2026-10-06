# Holy Mandala Animation Repair Brief

Status: source generation in progress; parent review is required before runtime DDS replacement.

Consumer: `holy_realm_mandala_core` in `interface/chaosx_decisions.gui`; seven state sprites are selected by `GetHolyRealmMandalaSprite` and registered in `interface/003_holy_realm.gfx`.

Each state keeps its existing name, static fallback path, animated path, 420x420 frame canvas, 16-frame horizontal sheet, 8 fps, two-second loop, `looping = yes`, and `play_on_show = yes`. The consumer scales the art to 0.52, or 218.4 pixels on screen.

Each new family begins with one generated 4x4 frame-source atlas made expressly as animation source art. Its 16 cells are distinct individually drawn motion poses, ordered left-to-right and top-to-bottom. The fixed medallion body, camera, scale, silhouette, and center anchor remain stable within a family. State motion comes from visible smoke, cloth, petals, flames, sparks, or ash as named in the frame plan; no glow-only loop or transformed still is accepted.

ImageGen receives a native transparent-background request for every atlas. Each frame is cropped from its own atlas cell, then aligned on a 420x420 transparent canvas. The subject is a centered cutout with painted cold-ink surfaces inside the medallion and transparent unused canvas outside it. No opaque square, checkerboard, text, border, or watermark is permitted.

The previous runtime static and first animation frames are preserved in `source_references/` and `previous_rejected_dds/`. They guide Mandala geometry, material, and stage palette only; the old glow-derived cells are not accepted as source frames. The image-generation tool exposes no model selector, so the record names only the built-in execution route and does not claim an unreported backend model.

The canonical decision-category contact sheet and `decision_category_generic.png` were inspected. The visual-component catalog and `national_spirit_backgrounds/contact_sheet.png` were also inspected. The listed `decision_category_background_blue_roundel.png` is a 52x40 mini-icon background and does not fit this 420x420 standalone GUI medallion; no component layer is used.

The native and 4x contact sheets plus loop previews are review artifacts. Do not copy candidate DDS files over runtime paths until the parent accepts the previews.
