# Catalog Alignment Brief

## Current export finding

The supplied event CSV contains a stale or shifted description sequence around Event 56.

The current exported rows include:

| ID | Event name | Current exported details |
| ---: | --- | --- |
| 54 | Gift from scientists | A country enters a sudden infrastructure boom. |
| 55 | The Great Infrastructure Project | A naval renaissance gives every country a functioning fleet. |
| 56 | The Navy | Radar coverage expands across the world. |
| 57 | The Radar | Industry expands in every country as factories spread with the territory under control. |
| 58 | The Industrial Complex | Every country expands its civilian industry in proportion to the territory it controls. |

Event 56 therefore cannot use its current exported Details field as source design. The user-provided brief and this specification are the Event 56 authority.

The adjacent rows should be audited separately against their own accepted specifications. This Event 56 handoff must not silently rewrite Events 54, 55, 57, or 58 from inference.

## Authoritative edit rule

Edit only:

```text
docs/spreadsheets/chaos_redux_events_catalog.xlsx
```

After a successful workbook update, run:

```text
python .tools/export_event_catalog_csv.py
```

Do not edit the three CSV snapshots directly.

## Event 56 workbook content

### Identity fields

- ID: `56`
- Event Name: The Navy
- Type: Minor Repeatable
- Chaos level: `1`
- Status before implementation completion: To Be Reworked

### Details direction

Use a concise player-facing summary stating that every country with usable coastline receives one independently rolled naval package. Packages can be balanced, submarine-heavy, destroyer-heavy, convoy-focused, cruiser-focused, capital-focused, carrier-focused, coastal-defense, invasion-support, or another legal specialized fleet. Landlocked countries are skipped until a later firing finds that they have gained direct usable coast.

Do not list global budgets, exact weights, internal eligibility predicates, or implementation notes.

### Evolution fields

#### Evo I

At 200 Chaos, future packages can become larger and more sharply specialized, including extreme submarine, destroyer, convoy, carrier, or capital concentrations.

#### Evo II

At 400 Chaos, future packages can include explicitly owner-approved experimental naval assets. The event does not grant their technology.

#### Evo III

At 600 Chaos, future packages can become coherent impossible hybrids that mix heavy fleets, advanced submarines, carriers, and registered unusual assets while remaining bounded.

### Cluster fields

Event 56 has two memberships:

- Sudden Abundance, Medium
- Military Preparation, Medium

The supplied export has only one `Cluster ID` and one `Member Severity` field per event row. Before editing, inspect the authoritative workbook and current cluster implementation to determine the supported multi-membership representation. Do not flatten the event to one cluster or place comma-separated IDs into a field that the runtime does not parse.

## New cluster rows

The supplied cluster export does not contain Sudden Abundance or Military Preparation.

Do not assume that numeric ID `9` or any other apparent gap is free. Inspect the live cluster registry, workbook, Event Log selectors, scripted localisation, and settings surfaces before assigning unused stable IDs.

### Sudden Abundance

- Type: Minor Repeatable
- Chaos level proposal: 1
- Status before implementation: Unavailable or the workbook's equivalent planning state
- Members: 19, 29, 32, 37, 42, 56, 64
- Per-membership severities: Medium, Medium, Medium, Medium, Low, Medium, Medium

Details direction: sudden supplies of people, equipment, money, strategic weapons, fleets, and fortifications give countries power they did not prepare to absorb.

### Military Preparation

- Type: Minor Repeatable
- Chaos level proposal: 2
- Status before implementation: Unavailable or the workbook's equivalent planning state
- Members: 32, 42, 56, 64
- Per-membership severities: Medium, Low, Medium, Medium

Details direction: military arsenals, missile forces, fleets, and border defenses expand across the world without directly starting wars.

## Status transition

Keep Event 56 and both proposed clusters in their planning or unavailable states until the implementation, assets, AI behavior, Event Log integration, cluster behavior, workbook export, and required validation are complete.
