# Leader portrait compatibility index

This directory is a compatibility surface for agents that look for a
top-level `assets/leader_portraits/` path. It contains a small, male-only pack
of reference PNG copies under `leaders/` and `commanders/`, plus role-specific
contact sheets. The canonical reference PNGs remain under
`../vanilla_reference/`; the copies are review material, not runtime assets or
a competing source of truth. Exact source mapping and SHA-256 values are in
[`REFERENCE_MANIFEST.md`](REFERENCE_MANIFEST.md).

## Route by HOI4 role

Use the exact canonical directory for the character's runtime role before
generating, sourcing, processing, or wiring a portrait.

| HOI4 role | Canonical reference path | Native reference canvas | Contact sheet |
| --- | --- | ---: | --- |
| Country leader | `../vanilla_reference/portraits/leaders/` | `156x210` | `leaders/contact_sheet.png` (curated pack) or `../vanilla_reference/portraits/leaders/contact_sheet.png` (full library) |
| Army or navy commander (`army.large` / `navy.large`) | `../vanilla_reference/portraits/commanders/` | `156x210` | `commanders/contact_sheet.png` (curated pack) or `../vanilla_reference/portraits/commanders/contact_sheet.png` (full library) |
| Operative | `../vanilla_reference/portraits/operatives/` | `156x210` | `../vanilla_reference/portraits/operatives/contact_sheet.png` |
| Political advisor, theorist, high command, or officer-corps dossier icon (`army.small`) | `../vanilla_reference/portraits/advisors/` | `65x67` | `../vanilla_reference/portraits/advisors/contact_sheet.png` |

The repository-relative paths to these same folders are:

```text
.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/
.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/
.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/operatives/
.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors/
```

## Curated male reference pack

The directly browsable compatibility copies are deliberately limited to
male-presenting examples and are grouped by runtime role:

- `leaders/` — four country-leader portrait copies, each `156x210`, with
  `leaders/contact_sheet.png`
- `commanders/` — two land and two naval commander portrait copies, each
  `156x210`, with `commanders/contact_sheet.png`

The pack excludes the canonical female leader and advisor examples. It does
not authorize generated or sourced portraits for any particular character;
use the full canonical family and the task's accepted asset requirements when
producing a final portrait.

### Do not mix portrait families

- Country leaders, commanders, and operatives use full `156x210` portrait
  textures. A commander remains a full portrait even when a UI view displays
  it at a smaller apparent size; never manufacture a `50x67` commander source.
- Advisors, theorists, high-command, and officer-corps characters use an
  independently composed `65x67` dossier card when their `army.small` or
  equivalent dossier slot is explicitly required. Do not shrink or directly
  wire a leader, commander, or operative portrait into that card.
- The advisor folder's `army_small_*` examples are dossier-card references,
  not commander portrait masters. Use the commander folder for `army.large` or
  `navy.large` textures.

Read the canonical [library rules](../vanilla_reference/README.md) and
[provenance catalog](../vanilla_reference/CATALOG.md) before using any
reference. Reference PNGs are review material only; do not copy, recolour,
trace, wire, or ship them as final mod assets.

## Related visual-reference routes

The same canonical library contains the other visual surfaces. Keep these
families separate from portraits and use their owning contact sheet and
catalog entry:

- units: `../vanilla_reference/units/` (equipment art, land/air/naval
  counters, division-template emblems, and 3D model materials)
- gameplay icons: `../vanilla_reference/icons/` (focus, ideas, decisions,
  missions, decision categories, technologies, achievements, officer corps,
  intelligence, commander traits, medals, raids, state modifiers, MIOs,
  factions, buildings, and modifiers)
- event art: `../vanilla_reference/event_art/`
- flags: `../vanilla_reference/flags/`

The PNG copies and contact sheets in this compatibility directory are
reference-only. If an agent needs a visual reference, open the curated file or
the canonical file/contact sheet at the path above and follow its cataloged
native canvas, transparency, frame order, and owning `.gfx`, `.gui`, `.asset`,
or `.mesh` definition. Never wire these copies into the mod or treat them as
final art.
