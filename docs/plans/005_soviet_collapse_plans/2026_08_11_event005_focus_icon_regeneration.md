# Event 005 Focus Icon Overlay Removal

Date: 2026-08-11

## Requirement

Every non-specialist Event 005 focus icon must be free of the rejected shared-base-plus-overlay construction.

Duplicate genuine artwork is allowed. A tree that intentionally uses one icon can reuse that icon throughout. A suitable existing base or vanilla-style icon may replace an overlay-derived texture, and native ImageGen is used only where no suitable existing artwork fits.

## Audit finding

The previous 1,730 non-specialist variants were derived from shared country focus textures and semantic medallions.

That construction is rejected because the added accents and medallions are not real icon artwork.

The 30 UWR/KMB specialist focus icons were visually reviewed as a separate bespoke package and remain outside this regeneration batch unless an individual review finds a source or quality defect.

## Locked runtime contract

- Focus count in the assignment manifest: 1,760.
- Regeneration scope: 1,730 derived non-specialist focus textures.
- Native runtime focus canvas: 100x88, matching the active consumer and installed vanilla focus reference family.
- Runtime folder: `gfx/interface/goals/005_soviet_collapse/`.
- Existing sprite names, focus ids, focus files, localisation, and tree positions remain stable.
- The active per-focus registry is `interface/005_soviet_collapse_focus_icons.gfx`.
- Duplicate legacy definitions for the regenerated sprite names are removed from `interface/005_soviet_collapse.gfx`.

## Production evidence

Each newly generated focus requires its own native ImageGen source PNG, processed transparent PNG, final DDS, prompt/source-mode record, native-size contact-sheet entry, decoded DDS round-trip evidence, and manifest row. Each existing-art reuse records the exact source texture and final runtime hash instead of inventing a duplicate generation package.

The active evidence workspace is `docs/assets/005_soviet_collapse/focus_icon_regeneration/`.

The source prompt uses the focus id and its route meaning as the semantic brief and forbids generated text, UI controls, watermarks, and reuse of existing runtime art as an ImageGen input.

## Validation gate

The parent agent will reconcile every batch against `docs/assets/005_soviet_collapse/focus_icon_assignments/manifest.json`, verify source and processed coverage, inspect representative contact sheets, validate DDS headers and dimensions, confirm sprite-to-texture coverage, and rerun MCP focus inspection and raster evidence without changing the authored layout.

Completion requires all 1,730 replacement rows to resolve to either a documented existing-art reuse or a complete generated package, with no rejected overlay-derived runtime texture remaining. That asset gate is satisfied. The 30 UWR/KMB specialist rows remain preserved bespoke art.

## Final resolution

The clarified reuse policy is applied in `docs/assets/005_soviet_collapse/focus_icon_regeneration/final_focus_icon_manifest.json`.

- 1,408 former overlay rows now use the documented genuine existing tree/base texture.
- 322 rows retain individually generated ImageGen source and processed artwork with decoded DDS round-trip evidence.
- 30 UWR/KMB specialist rows remain preserved bespoke artwork.
- All 1,760 runtime textures are present, and all 1,760 focus sprite names resolve through the active registries.
- The focus source files and authored tree layout were not changed.

The old duplicate focus sprite definitions were removed from `interface/005_soviet_collapse.gfx`; the active focus registry is `interface/005_soviet_collapse_focus_icons.gfx` plus the specialist registry.

The current local asset audit reports zero missing runtime textures, zero reuse mismatches, zero generated round-trip mismatches, and zero unregistered focus sprites.
