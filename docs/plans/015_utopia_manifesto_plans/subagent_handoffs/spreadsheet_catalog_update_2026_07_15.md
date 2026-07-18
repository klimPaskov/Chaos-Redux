# Event 15 Spreadsheet Catalog Update Handoff

Date: 2026-07-15

Subagent role: `chaosx_spreadsheet_doc_worker`

## Scope and result

Updated only the Event 15 catalog row in `docs/spreadsheets/chaos_redux_events_catalog.xlsx`. The row with numeric ID `15` is `Events` row 16. Its disabled placeholder text now mirrors the current English Event Details and evolution localisation.

No gameplay, localisation, specification, event documentation, asset, or other spreadsheet row was edited by this pass. No commit was created.

## Source localisation copied

Event name source:

- Key: `chaosx.event_name.15`
- Value: `Utopia Manifesto`

Event Details source:

- Key: `chaosx.events_log.window.event_details.utopia_manifesto`
- Value copied to `Events!C16`:

```text
A translated manifesto passes from reading rooms into the ministries of a small country. It proposes that public need should govern common stores, useful work, settlements, and the obligations of citizenship. Its readers disagree over whether freedom is secured by consent, shared councils, expert measure, disciplined separation, or the right to revise the book itself.

As the experiment takes hold, shortages, public works, local charters, and agreements with neighboring states test every interpretation. Promises are judged through visible provision and conduct, while each territorial case asks whether necessity can cross a border without becoming appetite.
```

Evolution cells follow the nearest implemented event-row convention. Each cell contains the current title, two newline characters, and the current body.

### Evo I

- Keys: `utopia_manifesto.evolution.1.title` and `utopia_manifesto.evolution.1.body`
- Value copied to `Events!D16`:

```text
Glosses in the Margin

The recovered manuscript no longer speaks with one voice. Rival translations, household annotations, and public commentaries have become organized schools of interpretation. Delegates arrive carrying copies marked by workshops, parishes, councils, and exiles. The argument over the book has become an institution of its own, and the eventual commonwealth will be shaped by whoever keeps the right to write in its margins.
```

### Evo II

- Keys: `utopia_manifesto.evolution.2.title` and `utopia_manifesto.evolution.2.body`
- Value copied to `Events!E16`:

```text
Necessary Shores

Migration, blockade, crowded housing, and uncertain supply have pushed the common store against the limits of the map. Surveyors now distinguish want from ambition before they mark a harbor, corridor, settlement, or lease as necessary ground. Domestic works remain possible, and every foreign offer leaves a record. The experiment must decide whether need can cross a border without turning into appetite.
```

### Evo III

- Keys: `utopia_manifesto.evolution.3.title` and `utopia_manifesto.evolution.3.body`
- Value copied to `Events!F16`:

```text
Cities of One Measure

The settlement plan has escaped the capital. Cooperative municipalities, associated towns, and rebuilt districts repeat its gardens, clinics, workshops, stores, and transport links in different soil. Each place adapts the design to local votes and local shortages. Their growing network makes the manifesto visible in ordinary streets, while disputes over assignment reveal who is allowed to alter the plan.
```

### Evo IV

- Keys: `utopia_manifesto.evolution.4.title` and `utopia_manifesto.evolution.4.body`
- Value copied to `Events!G16`:

```text
Nowhere Made Law

The manifesto has become a regional legal identity. Governments and movements invoke it when they negotiate association, refuse an ultimatum, request aid, or defend local charters. Sponsors offer protection with conditions, rivals describe every storehouse as a disguised frontier, and small states judge whether the commonwealth is refuge, partner, or threat. An imagined country has become a claim that diplomacy must answer.
```

### Evo V

- Keys: `utopia_manifesto.evolution.5.title` and `utopia_manifesto.evolution.5.body`
- Value copied to `Events!H16`:

```text
The Perfect Island

Ordinary regional order is breaking around a society trying to make one bounded place endure. Reserve trains, guarded harbors, refugee districts, fortification works, and member councils all pull against one another. A closed regime can harden the boundary into compulsory service. A voluntary commonwealth can distribute refuge among willing towns. Neither answer escapes the cost of keeping stores open while the roads beyond them fail.
```

## Exact workbook changes

Sheet: `Events`

| Cell | Before | After |
|---|---|---|
| `B16` | `Event 015 Placeholder` | `Utopia Manifesto` |
| `C16` | Disabled placeholder details | Exact Event Details value recorded above |
| `D16` | blank | Evo I title and body recorded above |
| `E16` | blank | Evo II title and body recorded above |
| `F16` | blank | Evo III title and body recorded above |
| `G16` | blank | Evo IV title and body recorded above |
| `H16` | blank | Evo V title and body recorded above |
| `J16` | `Reserved Disabled` | `Minor Fire-Once` |
| `M16` | `Placeholder` | `Fully Functional` |

Verified without changing:

- `A16` remains numeric `15`.
- `I16` remains blank because Event 15 has no catalog world-end scenario.
- `K16` remains blank because Event 15 has no cluster mapping.
- `L16` remains blank because there is no member severity without a cluster mapping.
- Row 16 height changed from `22.5` to `409.5`, matching the nearest fully populated implemented row and the workbook's maximum-height convention for long wrapped text.
- Every Event 15 cell retained its original style, number format, alignment, border, and fill.

## Validation evidence

- The workbook loaded before the edit and after the final save with `openpyxl 3.1.5` under `C:\Program Files\Python39\python.exe`.
- A pre-edit to post-edit cell-state comparison found exactly nine changed cells: `Events!B16:H16`, `Events!J16`, and `Events!M16`. The only non-cell change was the intended `Events` row 16 height adjustment.
- All sheet names, dimensions, table references, merge ranges, column dimensions, data validations, conditional-formatting counts, defined names, and sheet visibility states remained identical.
- Sheet dimensions remain `Events A1:M1015`, `Clusters A1:G13`, `Scenarios A1:F11`, `Info A1:A1`, and `Legend A1:D24`. All five sheets retain zero merged ranges.
- The workbook package retained the same 19 ZIP parts. Every XML and relationship part parsed successfully, and the ZIP integrity scan found no corrupt member.
- Formula count was zero before and zero after. Formula and cached-value error scans found zero `#REF!`, `#DIV/0!`, `#VALUE!`, `#N/A`, `#NAME?`, `#NUM!`, or `#NULL!` cells.
- Cell style count remained 85 and named style count remained 1.
- Pre-edit workbook SHA-256: `00e4f5fd91b75937777c87fcef20d694ab0eb8a2b9e193da7438b3fc94518790`.
- Post-edit workbook SHA-256: `6aa758d699d814599a1011d5f9acc1089bbf42baf053be7a4dbabadd525091a2`.

The workbook already contained unrelated uncommitted Event 19 and Scenarios edits before this pass. A comparison against `HEAD` identified 12 such pre-existing changed cells plus the pre-existing `Scenarios` row 11 height of `280.0`. Their values, styles, and row formatting were preserved and were not counted as changes made by this pass.

## Simplifications, omissions, fallbacks, and blockers

None. The requested Event 15 catalog fields were populated from the frozen in-game English localisation without substituted wording, and no fallback source was used.

## Skills used

- `xlsx`
- `chaos-redux-events`

No skill was created or updated.
