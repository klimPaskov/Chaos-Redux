# Event 015 Spreadsheet Catalog Completion Audit

Date: 2026-07-15

Auditor role: independent read-only spreadsheet completion audit

Workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`

Audited row: `Events!16`, numeric event ID `15`

## Verdict

**PASS**

`Events!A16:M16` matches the frozen Event 015 source and English localisation. The row identifies `Utopia Manifesto`, reproduces the Event Details text exactly, carries the five canonical evolutions in order, leaves the world-end and cluster fields blank, classifies the event as `Minor Fire-Once`, and marks it `Fully Functional`.

No P0, P1, or P2 finding was identified.

The workbook was not modified by this audit.

## Frozen evidence snapshot

| File | SHA-256 |
|---|---|
| `docs/spreadsheets/chaos_redux_events_catalog.xlsx` | `6aa758d699d814599a1011d5f9acc1089bbf42baf053be7a4dbabadd525091a2` |
| `localisation/english/chaosx_event_names_l_english.yml` | `2e1c78a86e307b8cc19ebc735d02b52fb82d470eecea20133d2874c0c6a2796e` |
| `localisation/english/chaosx_gui_l_english.yml` | `451862430b424bf603626fac24aa66dad17120c3517c0447b41edb435e83ac1b` |
| `localisation/english/015_utopia_manifesto_evolutions_l_english.yml` | `bbf1d8af6246fbf892f4a9d7b4b41e9fc94e8ff5a810588d74180d00cde85cf7` |
| `common/script_constants/015_utopia_manifesto_constants.txt` | `a426f72ee144e8bbf940ffb46460777b8b69f6f2fbf8b1989c020a663cf901e1` |
| `common/script_constants/event_system_constants.txt` | `bf5491471a6154bd33e2177fdd8a08bbb059a05b6bc3762d5ff5e02613b3f5f6` |
| `common/scripted_effects/chaosx_logic_effects.txt` | `e8cd143721269fcbb6326e77dc607a12c27c7178872b5f2cc82b1024efb0c88d` |
| `common/scripted_effects/chaosx_event_cluster_effects.txt` | `e20d44ae1772b6460f6809fd86d414b3ef61fa8eb3056188bb946d1ac9bc770f` |
| `common/scripted_effects/chaosx_events_log_effects.txt` | `04ffe7ce7f84152690ddde5354dbeeedcc197c1fc14dd7cf66e97a59aca0bef6` |
| `common/scripted_triggers/chaosx_settings_triggers.txt` | `67a9f65759eaa267734a3c00f09b46249aecfb52bf8535d4e45bbea8eacea7a6` |

The workbook hash exactly matches the post-edit SHA-256 recorded in `spreadsheet_catalog_update_2026_07_15.md`.

## Live registry and mapping evidence

### Event identity and classification

- `common/script_constants/015_utopia_manifesto_constants.txt:10-18` defines `utopia_manifesto_event.id = 15`, `event_type = 3`, and `evolution_type = 15`.
- `common/script_constants/event_system_constants.txt:70-79` defines event type `3` as `fire_once`.
- `common/scripted_effects/chaosx_logic_effects.txt:180` registers `constant:utopia_manifesto_event.id` exactly once in `global.fire_once_events`.
- The Event 015 constant has no entry in `global.major_events` or `global.repeatable_events`.
- `common/scripted_triggers/chaosx_settings_triggers.txt:25` includes Event 015 in `event_log_event_is_reworked_default_enabled`. The live registry therefore does not retain the reserved-disabled state.

This supports `Events!J16 = Minor Fire-Once` and `Events!M16 = Fully Functional`.

### No cluster membership

- `common/scripted_effects/chaosx_event_cluster_effects.txt:302-396` contains the complete `event_belongs_to_cluster` mapping. It has no Event 015 branch and no `constant:utopia_manifesto_event.id` branch.
- `load_event_cluster_members` contains no Event 015 member entry.
- The Event 015 constant has zero membership occurrences in the event cluster registry sources.

This supports blank `Events!K16` and `Events!L16`.

### No world-end catalog branch

- No world-end registry or world-end gate maps event ID `15` or `constant:utopia_manifesto_event.id` to a terminal scenario.
- Event 015 has route presentation super events, but those are not world-end scenarios.

This supports blank `Events!I16`.

### Current name and Event Details mapping

- `localisation/english/chaosx_event_names_l_english.yml:17` defines `chaosx.event_name.15` as `Utopia Manifesto`.
- `common/scripted_localisation/chaosx_scripted_localisation_debug.txt:81-82` maps Event 015 to `chaosx.event_name.15`.
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:4701-4702` maps Event 015 to `chaosx.events_log.window.event_details.utopia_manifesto`.
- `localisation/english/chaosx_gui_l_english.yml:551` defines the exact Event Details text copied into `Events!C16`.

### Canonical evolution order

`common/script_constants/015_utopia_manifesto_constants.txt:46-57` assigns the public evolution order:

1. `glosses_in_the_margin = 1`
2. `necessary_shores = 2`
3. `cities_of_one_measure = 3`
4. `nowhere_made_law = 4`
5. `perfect_island = 5`

`common/scripted_effects/chaosx_events_log_effects.txt:2170-2192` adds the Event Details evolution preview entries in that same order. The title and body selectors map those stages to `utopia_manifesto.evolution.1..5.title` and `utopia_manifesto.evolution.1..5.body`.

## Exact `Events!16` cell audit

| Cell | Header | Expected and actual value | Result |
|---|---|---|---|
| `A16` | ID | numeric `15` | PASS |
| `B16` | Event Name | `Utopia Manifesto` | PASS |
| `C16` | Details | exact expanded value of `chaosx.events_log.window.event_details.utopia_manifesto` | PASS |
| `D16` | Evo I | title, two newline characters, body for evolution 1 | PASS |
| `E16` | Evo II | title, two newline characters, body for evolution 2 | PASS |
| `F16` | Evo III | title, two newline characters, body for evolution 3 | PASS |
| `G16` | Evo IV | title, two newline characters, body for evolution 4 | PASS |
| `H16` | Evo V | title, two newline characters, body for evolution 5 | PASS |
| `I16` | World-End Scenario | blank | PASS |
| `J16` | Type | `Minor Fire-Once` | PASS |
| `K16` | Cluster ID | blank | PASS |
| `L16` | Member Severity | blank | PASS |
| `M16` | Status | `Fully Functional` | PASS |

Event ID `15` occurs exactly once in the `Events` table, at row 16.

### Exact Event Details value in `C16`

```text
A translated manifesto passes from reading rooms into the ministries of a small country. It proposes that public need should govern common stores, useful work, settlements, and the obligations of citizenship. Its readers disagree over whether freedom is secured by consent, shared councils, expert measure, disciplined separation, or the right to revise the book itself.

As the experiment takes hold, shortages, public works, local charters, and agreements with neighboring states test every interpretation. Promises are judged through visible provision and conduct, while each territorial case asks whether necessity can cross a border without becoming appetite.
```

The expanded localisation and workbook value are both 664 characters and have SHA-256 `3b1063b91d076a60722212bff5925cf6db2184323296d2e4f375f658f46be51a`.

### Exact Evo I value in `D16`

```text
Glosses in the Margin

The recovered manuscript no longer speaks with one voice. Rival translations, household annotations, and public commentaries have become organized schools of interpretation. Delegates arrive carrying copies marked by workshops, parishes, councils, and exiles. The argument over the book has become an institution of its own, and the eventual commonwealth will be shaped by whoever keeps the right to write in its margins.
```

The expanded localisation and workbook value are both 444 characters and have SHA-256 `c62381e7a169616993fc62127d7e720089dfb621aed36944fb6979cd1f021b9a`.

### Exact Evo II value in `E16`

```text
Necessary Shores

Migration, blockade, crowded housing, and uncertain supply have pushed the common store against the limits of the map. Surveyors now distinguish want from ambition before they mark a harbor, corridor, settlement, or lease as necessary ground. Domestic works remain possible, and every foreign offer leaves a record. The experiment must decide whether need can cross a border without turning into appetite.
```

The expanded localisation and workbook value are both 423 characters and have SHA-256 `4dcb2f732af67a2e4730e62d3a65f189c80f9d480612d9c4bd8c6dfb78a47da7`.

### Exact Evo III value in `F16`

```text
Cities of One Measure

The settlement plan has escaped the capital. Cooperative municipalities, associated towns, and rebuilt districts repeat its gardens, clinics, workshops, stores, and transport links in different soil. Each place adapts the design to local votes and local shortages. Their growing network makes the manifesto visible in ordinary streets, while disputes over assignment reveal who is allowed to alter the plan.
```

The expanded localisation and workbook value are both 430 characters and have SHA-256 `c055f5f4025553464ee396e9a197298c1042a2938b1b1f5693b8f464b2a3bdd6`.

### Exact Evo IV value in `G16`

```text
Nowhere Made Law

The manifesto has become a regional legal identity. Governments and movements invoke it when they negotiate association, refuse an ultimatum, request aid, or defend local charters. Sponsors offer protection with conditions, rivals describe every storehouse as a disguised frontier, and small states judge whether the commonwealth is refuge, partner, or threat. An imagined country has become a claim that diplomacy must answer.
```

The expanded localisation and workbook value are both 445 characters and have SHA-256 `a359ce4d6c882d7a513bebeca6d710a2d96592b6b0c850d00a2d3e35fd0719c5`.

### Exact Evo V value in `H16`

```text
The Perfect Island

Ordinary regional order is breaking around a society trying to make one bounded place endure. Reserve trains, guarded harbors, refugee districts, fortification works, and member councils all pull against one another. A closed regime can harden the boundary into compulsory service. A voluntary commonwealth can distribute refuge among willing towns. Neither answer escapes the cost of keeping stores open while the roads beyond them fail.
```

The expanded localisation and workbook value are both 458 characters and have SHA-256 `7208731291621ea2abfcf34903e854a337689ee8693b713e20b72d90b9c41234`.

## Stale and placeholder scan

The following values have zero occurrences in `Events!A16:M16`:

- `World Tension Subsides`
- `Event 015 Placeholder`
- `Reserved Disabled`
- `reserved-disabled`
- `mechanical placeholder`
- the former mechanical placeholder sentence that listed missing dispatch, focus, decision, ledger, achievement, and super-event systems

The exact stale identity strings also have zero occurrences in live `events/`, `common/`, and `localisation/` sources. Historical specs, plans, and handoffs retain some of those phrases as provenance. They are not live Event 015 mappings and are outside the catalog row.

## Workbook style and structure

- Row 16 retained the established column styles. Style IDs across `A16:M16` are `49, 43, 43, 50, 51, 52, 53, 54, 55, 60, 57, 57, 64`.
- A semantic comparison with `HEAD` found no Event 015 font, fill, border, alignment, number format, protection, hyperlink, or comment change.
- All long text fields in `B16:H16` retain wrapped, top-aligned formatting where the column convention uses it.
- Row 16 height is `409.5`, up from `22.5` in `HEAD`. It matches row 15 and is the maximum established height in the `Events` sheet.
- Row 16 belongs to table `Events`, reference `A1:M1015`.
- The workbook has five sheets with dimensions `Events A1:M1015`, `Clusters A1:G13`, `Scenarios A1:F11`, `Info A1:A1`, and `Legend A1:D24`.
- Every sheet has zero merged ranges.
- The workbook contains 85 cell styles and one named style. The three styles added relative to `HEAD` belong to the unrelated pre-existing Scenarios row, not Event 015.
- Formula count is zero. Formula error token count is zero.

## Package integrity and reload validation

- The workbook reloaded successfully from its byte stream with `openpyxl 3.1.5` in normal mode.
- The workbook reloaded successfully in read-only mode.
- Both reloads returned the expected sheets in order: `Events`, `Clusters`, `Scenarios`, `Info`, `Legend`.
- The XLSX ZIP package contains 19 parts.
- The ZIP integrity scan returned no corrupt member.
- Every XML and relationship part parsed successfully.
- No `#REF!`, `#DIV/0!`, `#VALUE!`, `#N/A`, `#NAME?`, `#NUM!`, or `#NULL!` token was present in any workbook cell.

The audit did not save or recalculate the workbook. Recalculation was unnecessary because the workbook contains no formulas.

## Independent change attribution against `HEAD`

The current workbook and the `HEAD` workbook were loaded from memory and compared at cell, row-dimension, column-dimension, table, merge, and workbook-structure levels.

There are exactly 21 changed cells against `HEAD`:

- Nine Event 015 cells: `Events!B16:H16`, `Events!J16`, and `Events!M16`.
- Six unrelated pre-existing Event 019 cells: `Events!C20:G20` and `Events!M20`.
- Six unrelated pre-existing Scenarios cells: `Scenarios!A11:F11`.

There are exactly two changed row heights against `HEAD`:

- `Events!16`, from `22.5` to `409.5`, which belongs to the Event 015 worker pass.
- `Scenarios!11`, from the default height to `280.0`, which predates the Event 015 worker pass.

The unrelated Scenarios work also expands `Manual_Scenarios` from `A1:F10` in `HEAD` to `A1:F11` in the current workbook and changes the Scenarios used dimension from `A1:F10` to `A1:F11`. Those are preserved pre-existing changes. They are not attributed to Event 015.

No other Event 015 cell, row, column, table, merge, or workbook structure differs from `HEAD`. This independently corroborates the handoff claim that the Event 015 pass changed only `B16:H16`, `J16`, `M16`, and row 16 height while preserving the unrelated Event 019 and Scenarios work.

The handoff's pre-edit SHA-256 cannot be independently recomputed because the pre-edit binary was not retained. This is a non-blocking evidence limitation. The exact current hash, the complete semantic diff against `HEAD`, the unchanged Event 015 styles, and the isolated unrelated deltas provide independent cell-level attribution.

## Findings by priority

### P0

None.

### P1

None.

### P2

None.

## Simplifications, omissions, fallbacks, and blockers

- Simplifications: none.
- Functional omissions: none.
- Fallbacks: none.
- Blockers: none.
- Evidence limitation: the worker's pre-edit binary is not present, so its recorded pre-edit SHA-256 was not independently rehashed. The claimed edit scope was independently verified semantically as described above.

## Audit output

This report is the only file created by the audit. No gameplay file, localisation file, workbook, or pre-existing document was edited.

## Skills used

- `xlsx`
- `chaos-redux-events`
- `chaos-redux-subagents`

No skill was created or updated.
