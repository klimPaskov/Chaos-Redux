# Canonical asset-reference library

This directory is the single canonical review library for the asset workflows
used by Chaos Redux, Slop Redux, and agentic HOI4 Modding:

`C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-event-assets\assets\vanilla_reference`

It is organized by the owning visual surface so an agent can compare the right
canvas, transparency treatment, frame layout, or event-art presentation before
creating an original asset. The other two mod repositories must reference this
directory directly; their local copies are legacy review copies and are not
workflow inputs.

Reference PNGs are never runtime mod assets. Do not wire, ship, trace, recolor,
or copy the depicted people and symbols into final art. For implementation,
inspect the cataloged source and its `.gfx`, `.gui`, `.asset`, or `.mesh`
precedent, then create an original or properly sourced Chaos Redux asset.

## Provenance and coverage

- Vanilla source root: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`
- Installed build at extraction: `Operation Postern v1.19.2.0.a729 (d245)`
- Extraction date: `2026-07-16`
- Review format: lossless RGBA PNG decoded from source DDS, TGA, or PNG
- Pixel policy: preserve the source texture canvas exactly; do not crop,
  stretch, repaint, or normalize transparent bounds during extraction
- Inventory: 287 allowlisted reference PNGs across 37 semantic folders
- Rebuild and validation tool: `.tools/extract_hoi4_asset_references.py`

The generated [CATALOG.md](CATALOG.md) records the exact source, source kind,
native dimensions, related definition, and local contact sheet for every
reference. Vanilla HOI4 entries are distinguished from explicitly marked Chaos
Redux source and migrated legacy review copies.

Common icon families — national focus, ideas, decisions, decision categories,
technologies, and achievement states — contain at least 15 references. Every
other tracked icon family contains at least 5. Counts exclude contact sheets.
The reusable achievement not-eligible overlay is stored beside these examples
at `icons/achievements/overlay.png`, but is a workflow input and is excluded
from the contact sheet and inventory count.

## Contact sheets

Every semantic folder owns one labeled `contact_sheet.png` beside its reference
PNGs. There is deliberately no broad `contact_sheets/` directory. Sheets use a
checkerboard review background for transparency, show the filename and native
dimensions, and preserve the source family’s aspect ratio. The checkerboard is
not part of any extracted image.

Examples:

- `icons/national_focus/contact_sheet.png`
- `icons/ideas/contact_sheet.png`
- `icons/decisions/contact_sheet.png`
- `icons/technologies/contact_sheet.png`
- `event_art/report/contact_sheet.png`
- `event_art/news/contact_sheet.png`
- `event_art/super_event/contact_sheet.png`
- `flags/contact_sheet.png`

## Reference families

Portrait references:

- `portraits/leaders/`
- `portraits/commanders/`
- `portraits/operatives/`
- `portraits/advisors/` (native `65x67` advisor and high-command dossier cards)

Flags and event art:

- `flags/normal/`, `flags/medium/`, and `flags/small/`
- `event_art/report/`, `event_art/news/`, and `event_art/super_event/`

Gameplay icons:

- `icons/national_focus/`, `icons/ideas/`, `icons/technologies/`
- `icons/decisions/`, `icons/missions/`, and `icons/decision_categories/`
- `icons/achievements/`, `icons/officer_corps_spirits/`, and
  `icons/special_projects/`
- `icons/balance_of_power/`, `icons/intelligence_agency/`, and
  `icons/intelligence_operations/`
- `icons/commander_traits/`, `icons/medals/`, and `icons/military_raids/`
- `icons/state_modifiers/`, `icons/military_industrial_organizations/`,
  `icons/factions/`, `icons/buildings/`, and `icons/modifiers/`

Unit visual pipelines:

- `units/equipment/technology_art/`
- `units/land/counters_large/`, `units/land/map_counters/`, and
  `units/land/division_template_emblems/`
- `units/air/map_counters/` and `units/naval/map_counters/`
- `units/models_3d/land_materials/`, `air_materials/`, and `naval_materials/`

These families are not interchangeable. Follow the cataloged native canvas,
transparency, frame order, and owning definition. Model materials are UV
references paired with mesh/entity definitions; they are not 2D icons, renders,
or concept sheets.

## Maintenance

The allowlist is maintained by `.tools/extract_hoi4_asset_references.py`.
When adding a reference, record its exact provenance, choose the correct
semantic folder, keep the coverage floor, regenerate that folder’s contact
sheet, and update the catalog. Do not recreate the old shared contact-sheet
directory or add new reference images beside this tree.
