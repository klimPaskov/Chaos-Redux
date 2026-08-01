# Chaos Redux asset reference library

This directory documents visual references for the `chaos-redux-event-assets`
skill. It is not a destination for final mod art. Final assets belong in their
documented `gfx/` locations; sources, processed previews, manifests, and
handoffs belong under `docs/assets/`.

## Skill-local reference roots

Every active Chaos Redux skill and asset-routing agent must use this exact
skill-local root:

`C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-event-assets\assets`

The organized canonical library is `vanilla_reference/`. The user-requested `leader_portraits/` directory is a curated male-only, directly browsable country-leader and commander review pack. Its `leaders/` and `commanders/` subfolders contain byte-identical copies whose mappings and hashes are documented in `REFERENCE_MANIFEST.md`; it is a deliberate review aid, not a second provenance authority or runtime source.

Start every review with:

- `vanilla_reference/README.md` for library and contact-sheet rules
- `vanilla_reference/CATALOG.md` for exact source provenance, native canvas, frame count, and owning definition
- `leader_portraits/README.md` and `leader_portraits/REFERENCE_MANIFEST.md` for the curated male-only portrait review pack and its `leaders/` and `commanders/` contact sheets

Reference PNGs teach framing, scale, transparency, style, and engine pipeline. They are review material only: never recolor, trace, wire, or ship them as runtime assets.

## Reference families

Portraits and character references:

- `portraits/leaders/`
- `portraits/commanders/`
- `portraits/operatives/`
- `portraits/advisors/` (native `65x67` dossier-card references)

Flags and event art:

- `flags/normal/`, `flags/medium/`, and `flags/small/`
- `event_art/report/`
- `event_art/news/`
- `event_art/super_event/`

Gameplay icons:

- `icons/national_focus/`, `icons/ideas/`, `icons/technologies/`, and
  `icons/special_projects/`
- `icons/decisions/`, `icons/missions/`, `icons/decision_categories/`, and
  `icons/achievements/`
- `icons/officer_corps_spirits/`, `icons/balance_of_power/`,
  `icons/intelligence_agency/`, and `icons/intelligence_operations/`
- the separate `commander_traits`, `medals`, `military_raids`,
  `state_modifiers`, `military_industrial_organizations`, `factions`,
  `buildings`, and `modifiers` folders under `icons/`

Unit visual pipelines:

- `units/equipment/technology_art/`
- `units/land/counters_large/`, `map_counters/`, and
  `division_template_emblems/`
- `units/air/map_counters/` and `units/naval/map_counters/`
- `units/models_3d/land_materials/`, `air_materials/`, and
  `naval_materials/`

Every semantic reference directory owns a labeled `contact_sheet.png`. There
is no shared `contact_sheets/` directory. Contact sheets are
review aids, not final assets. Follow the cataloged native canvas, transparency,
frame order, and owning `.gfx`, `.gui`, `.asset`, or `.mesh` definition for the
selected family.

## Portrait source discipline

For a real person, begin with an attributed real source photograph and an
explicit head-and-shoulders crop. Preserve identity, expression, age, hair,
clothing, and pose while applying a restrained HOI4 painted finish and quiet
period background. A raw photo, generic oil-paint filter, reconstructed face,
or weak likeness is not a finished portrait.

Grounded, historical, restored, separatist, regional, indigenous, dynastic, and
otherwise plausibly historical identities use sourced real people; generated
one-person portraits are limited to truly fictional high-chaos or
impossible/supernatural entities. Allowed fictional faces should be extraordinary
and culturally coherent for their invented setting without stereotypes, gore,
mockery, memes, or borrowed sacred motifs. Missing or ambiguous classification
fails closed.

Fictional councils, committees, juntas, boards, offices, and symbolic bodies
must use people-free institutional portraits: one readable institutional
symbol, empty chamber, desk, machine, seal, or document arrangement with no
human figure, face, silhouette, or crowd. Use institutional names rather than
personal random-name pools.

## Advisor and high-command dossier portraits

Advisor, theorist, military-high-command, officer-corps, and army-small dossier
portraits are a separate, explicitly authorized asset family. The canonical style
references live under `vanilla_reference/portraits/advisors/`; they are native
`65x67` review inputs and are not runtime art. Never infer this family from a
character or small-portrait consumer when the accepted requirement does not request
it.

There is no bundled dossier compositor or reusable card-art package. Prepare each
native `65x67` candidate with a deterministic, task-specific/manual image workflow.
Retain source and processed PNGs, exact dimensions, crop/composition notes, hashes,
provenance, comparison sheet, stable sprite name, and runtime path in distinct
repo-contained artifacts. Grounded real people must complete the sourced identity
gate through an independently approved `156x210` candidate first; fictional
high-chaos or impossible/supernatural subjects may use an approved generated master.
Never directly resize a full portrait into the card or draw replacement card art
from primitive geometry.

Review every candidate against the canonical advisor/high-command references at
native size and at `4x` nearest-neighbour size. Check face readability, frame
silhouette and palette, paper geometry and opacity where present, transparent
corners, texture continuity, and holes or fringe. The producer may not approve the
candidate. Convert only an independently approved PNG to DDS with the repository
converter, then wire the stable sprite in the appropriate `.gfx` file.

## Flags and event art

Every final flag is a clean flat graphic design. Historical research may lock
the geometry, colours, and symbols, but the final design must not be a waving
fabric scene, painterly illustration, perspective view, or invented heraldry.
Report, news, and super-event references use their matching event-art family
and owning UI definition.

## Maintenance

Add a canonical reference only when it documents a missing family, state, size, or engine pipeline. Record exact provenance and native dimensions, update that family's local `contact_sheet.png`, and preserve the coverage floor. The extractor and catalog distinguish Vanilla HOI4 examples from explicitly marked Chaos Redux source or migrated review copies. Add male leader/commander copies to `leader_portraits/leaders/` or `leader_portraits/commanders/` only when the manifest and both family contact sheets are updated in the same change. Never add another reference root outside this skill-local `assets/` directory or wire reference PNGs into the mod.
