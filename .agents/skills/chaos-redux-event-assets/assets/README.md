# Chaos Redux asset reference library

This directory contains reference material for the
`chaos-redux-event-assets` skill. It is not a destination for final mod art.
Final event assets belong in their documented `gfx/` location, with sources,
processed previews, manifests, and handoffs under `docs/assets/`.

## Start here

Use `vanilla_reference/` as the canonical style and engine-pipeline library.
Its `README.md` defines the review rules, and `CATALOG.md` maps every extracted
PNG to the exact local vanilla source and native dimensions.

The canonical library is organized by asset family:

- `vanilla_reference/portraits/leaders/` — 156x210 HOI4 leader portraits
- `vanilla_reference/portraits/advisors/` — independently composed 65x67
  advisor, theorist, high-command, and officer dossier icons
- `vanilla_reference/flags/` — flat normal, medium, and small flag ladders
- `vanilla_reference/icons/` — focus, idea, decision, mission, category,
  achievement, officer-corps, technology, special-project, and balance-of-power
  references
- `vanilla_reference/event_art/` — report and news event formats
- `vanilla_reference/units/equipment_icons_2d/` — equipment UI illustrations
- `vanilla_reference/units/unit_icons_2d/` — frame-aware division counters
- `vanilla_reference/units/model_material_refs_3d/` — model material and UV
  references, not 2D icons
- `vanilla_reference/contact_sheets/` — review sheets for the categories above

## Supplemental Chaos Redux examples

The category folders beside `vanilla_reference/` are retained supplemental
examples used by older specs and manifests. Their paths remain stable so those
records and reusable helpers do not break. They may show established Chaos
Redux treatment, overlays, or older project conventions, but they do not
override the canonical vanilla dimensions or pipeline evidence.

When a supplemental example conflicts with `vanilla_reference/CATALOG.md`,
follow the canonical catalog and inspect the original vanilla definition.

## Maintenance

Add a reference only when it documents a missing asset family, state, size, or
engine pipeline. Preserve source provenance, native dimensions, and a contact
sheet entry. Never bulk-copy vanilla art, wire a reference PNG into the mod,
or use a reference person or symbol as final Chaos Redux artwork.
