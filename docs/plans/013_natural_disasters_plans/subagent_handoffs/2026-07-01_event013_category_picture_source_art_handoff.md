# Event 013 Category Picture Source Art Handoff

Scope: Natural Disasters cosmetic left-side decision category pictures only.

## Completed

- Generated distinct source art for:
  - `decision_cat_picture_nd_firefront`
  - `decision_cat_picture_nd_drought`
  - `decision_cat_picture_nd_heat`
  - `decision_cat_picture_nd_winter`
  - `decision_cat_picture_nd_dust`
  - `decision_cat_picture_nd_landslide`
  - `decision_cat_picture_nd_slope`
  - `decision_cat_picture_nd_skyfall`
  - `decision_cat_picture_nd_meteor_storm`
  - `decision_cat_picture_nd_famine`
- Reviewed the existing generated category-picture sources for `recovery_overview`, `flood`, `cyclone`, `severe_storm`, `hail`, `wind`, `corridor`, `earthquake`, `rupture`, `tsunami`, `volcano`, and `massive_eruption`; kept them because the contact sheet showed no visible breakage.
- Reprocessed all 22 `decision_cat_picture_nd_*` sources into 114x101 PNGs.
- Exported all 22 package DDS files to `docs/assets/013_natural_disasters/dds/`.
- Exported all 22 live DDS files to `gfx/interface/decisions/013_natural_disasters/`.
- Rebuilt `docs/assets/013_natural_disasters/contact_sheets/natural_disaster_category_pictures_contact.png`.

## Source Mode

The 10 replacement sources are generated bitmap art from Codex `image_gen`. Generation is appropriate here because these are fictional/event-generic Natural Disasters category scenes, not real documentary depictions of a specific photographed historical incident. Prompts requested period 1936-1945 disaster reportage / painted miniature styling, no readable text, no logos, no baked UI frame, no modern props.

## Sprite Handoff

The parent already wired the GUI and sprites. This pass did not edit `.gfx` or GUI files.

Use the already registered sprite naming pattern:

- `GFX_decision_cat_picture_nd_<slug>`
- Texture path: `gfx/interface/decisions/013_natural_disasters/decision_cat_picture_nd_<slug>.dds`

## Validation

- Count validation passed:
  - `docs/assets/013_natural_disasters/processed_png/`: 22 matching `decision_cat_picture_nd_*.png`
  - `docs/assets/013_natural_disasters/dds/`: 22 matching package DDS
  - `gfx/interface/decisions/013_natural_disasters/`: 22 matching live DDS
- Dimension validation passed: all checked processed PNG, package DDS, and live DDS files are `114x101`.
- Alpha validation passed: all checked category pictures are opaque with valid alpha.
- Chroma validation passed: no chroma-green-like pixels detected with `g > 220`, `r < 45`, `b < 45`.
- DDS header validation passed: all 22 package DDS files are `114x101` 32-bit BGRA-mask DDS.
- Visual contact-sheet review passed for target-size readability and distinct disaster identity.
- DDS export used `.tools/convert_to_dds.py`; `texconv` was not available in this shell, so the helper used its BGRA fallback path.

## Intentionally Untouched

- No category button icons (`nd_cat_*`) were edited by this pass.
- No decision icons, idea icons, animations, gameplay, localisation, `.gfx`, GUI, spreadsheet, event docs, `docs/assets/013_natural_disasters/manifest.md`, or `docs/assets/013_natural_disasters/gfx_handoff.md` edits were made by this pass.

## Remaining Risks

- The generated sources are final-source art, but they have only been visually reviewed through the rebuilt contact sheet, not in a live HOI4 session.
- Manifest and main `gfx_handoff.md` source-mode notes were not updated because the parent task explicitly restricted this pass from touching those files.
