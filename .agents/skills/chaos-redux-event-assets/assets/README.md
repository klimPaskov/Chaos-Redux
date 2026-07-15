# Chaos Redux asset reference library

This directory contains the visual reference material owned by the
`chaos-redux-event-assets` skill. It is not a destination for final mod art.
Final assets belong in their documented `gfx/` locations; sources, processed
previews, manifests, and handoffs belong under `docs/assets/`.

## Canonical library

All canonical references live under `vanilla_reference/` inside this skill.
Do not create a second canonical library at the project root or in another
skill. Start every review with:

- `vanilla_reference/README.md` for library and contact-sheet rules
- `vanilla_reference/CATALOG.md` for exact vanilla provenance, native canvas,
  frame count, and owning definition

Reference PNGs teach framing, scale, transparency, style, and engine pipeline.
They are not templates or final assets and must never be copied, recolored,
traced, wired, or shipped.

### Portrait identity and dossier families

- `vanilla_reference/portraits/leaders/` — country-leader portraits
- `vanilla_reference/portraits/commanders/` — full `156x210` army and navy
  commander portraits; do not misclassify them as native 50x67 textures
- `vanilla_reference/portraits/operatives/` — operative portraits
- `vanilla_reference/portraits/advisors/` — independently composed `65x67`
  advisor, theorist, high-command, and officer dossier cards

For a real person, begin with an attributed real source photograph and an
explicit head-and-shoulders crop. Preserve identity, expression, age, hair,
clothing, and pose while applying a restrained HOI4 painted finish and quiet
period background. A raw photo, generic oil-paint filter, reconstructed face,
or weak likeness is not a finished portrait. Advisor cards may share an
approved portrait master, but their crop, subject scale, background, frame,
corners, and paper overlay must be composed independently at `65x67`; never
shrink a leader, commander, or operative portrait into a dossier card.

Reusable generated dossier components live under
`advisor_dossier_overlays/`. Read
`advisor_dossier_overlays/advisor_dossier_overlay_manifest.json` before use.
The frame and paper/seal are original ImageGen outputs with transparent
derivatives; they are compositing inputs, not permission to recreate visible
card art with rectangles, polygons, lines, ellipses, procedural patina, or
other primitive drawing.

### Flags and event art

- `vanilla_reference/flags/normal/`, `flags/medium/`, and `flags/small/` — flat
  flag ladders
- `vanilla_reference/event_art/report/` — report-event presentation
- `vanilla_reference/event_art/news/` — news-event presentation

Every final flag remains an ImageGen-created flat graphic design, including a
historically attested flag after research locks its geometry, colours, and
symbols. References do not authorize painterly flag artwork: reject fabric,
folds, flagpoles, scenery, perspective, lighting, gradients, and invented
heraldry.

### Gameplay icon families

Use only the folder matching the owning UI surface:

- core progression: `icons/national_focus/`, `icons/ideas/`,
  `icons/technologies/`, `icons/special_projects/`, and
  `icons/balance_of_power/`
- decisions and goals: `icons/decisions/`, `icons/missions/`,
  `icons/decision_categories/`, and `icons/achievements/`
- military leadership: `icons/officer_corps_spirits/`,
  `icons/commander_traits/`, and `icons/medals/`
- intelligence: `icons/intelligence_agency/` and
  `icons/intelligence_operations/`
- operations and world state: `icons/military_raids/` and
  `icons/state_modifiers/`
- organizations and economy: `icons/military_industrial_organizations/`,
  `icons/factions/`, `icons/buildings/`, and `icons/modifiers/`

These families are not interchangeable. Follow the cataloged native canvas,
transparency, frame order, and owning `.gfx`, `.gui`, or database definition.
Do not force every family to 32x32 or 64x64, and do not treat a strip or indexed
sprite as one standalone icon.

### Unit visual pipelines

- `vanilla_reference/units/equipment/technology_art/` — flat 2D equipment and
  technology illustrations with source-specific canvases
- `vanilla_reference/units/land/counters_large/` — frame-aware large land-unit
  counter strips
- `vanilla_reference/units/land/map_counters/` — land map counters
- `vanilla_reference/units/land/division_template_emblems/` — division-template
  identity emblems
- `vanilla_reference/units/air/map_counters/` — air map counters
- `vanilla_reference/units/naval/map_counters/` — naval map counters
- `vanilla_reference/units/models_3d/land_materials/` — land-model materials
- `vanilla_reference/units/models_3d/air_materials/` — air-model materials
- `vanilla_reference/units/models_3d/naval_materials/` — naval-model materials

Classify unit work by domain and UI/model surface before creating it. Equipment
art, large counters, map counters, template emblems, and 3D materials require
separate briefs, source art, native canvases or UV layouts, frame metadata,
final paths, and handoffs. Model materials are UV references paired with
cataloged mesh, asset, and entity definitions; they are not 2D icons, finished
renders, or concept sheets.

## Legacy compatibility and supplemental paths

The category folders beside `vanilla_reference/` remain stable because older
manifests, prompts, and processing scripts may depend on them. Classify them as:

- legacy icon and workflow examples: `achievements/`, `bop/`, `decisions/`,
  `focuses/`, `ideas/`, `special_projects/`, and `tech_icons/`
- legacy flat-flag examples: `flags/`
- legacy event-art examples: `news_event_images/`, `report_event_images/`, and
  `super_event_images/`

Do not rename, move, delete, or repurpose these paths without first migrating
every dependency. Do not add new canonical references to them. They may teach
an established Chaos Redux treatment or provide a retained workflow input, but
they never override `vanilla_reference/CATALOG.md` or the current source rules.

## Maintenance

Add a canonical reference only when it documents a missing family, state,
size, or engine pipeline. Record exact vanilla provenance and native
dimensions, update the relevant contact sheet, and keep the selection small
and representative. Never bulk-copy vanilla art or wire reference PNGs into
the mod.
