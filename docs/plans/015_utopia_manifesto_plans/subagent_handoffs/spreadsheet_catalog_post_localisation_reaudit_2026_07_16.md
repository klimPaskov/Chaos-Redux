# Event 015 Spreadsheet Catalog Post-Localisation Reaudit

Status: **PASS**

Date: 2026-07-16  
Workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`  
Catalog target: `Events!A16:M16`, Event ID 15

## Result

Event 15 has exact parity with the current in-game Event Details name, description, and all five frozen evolution title and body pairs.

Only `Events!H16` changed. Its stale fifth-evolution body used the `A closed regime can`, `A voluntary commonwealth can`, and `Neither answer` frame. The replacement is the exact `utopia_manifesto.evolution.5.title` value, followed by two LF characters, followed by the exact `utopia_manifesto.evolution.5.body` value.

The final catalog classification is:

- `I16` is blank, so Event 15 has no world-end catalog mapping.
- `J16` is `Minor Fire-Once`.
- `K16` and `L16` are blank, so Event 15 has no cluster mapping or member severity.
- `M16` is `Fully Functional`.

A workbook-wide search found no Event 15, Utopia, or Manifesto entry on the `Clusters` or `Scenarios` sheets. A narrow source check found no Utopia Manifesto mapping in `common/scripted_effects/chaosx_event_cluster_effects.txt` or `common/scripted_triggers/chaosx_world_end_scenario_triggers.txt`.

## Exact Event 15 cells before

The JSON strings below use `\n\n` to represent the two LF characters stored between each evolution title and body. `null` represents a genuinely blank cell.

```json
{
  "A16": 15,
  "B16": "Utopia Manifesto",
  "C16": "A translated manifesto passes from reading rooms into the ministries of a small country. It proposes that public need should govern common stores, useful work, settlements, and the obligations of citizenship. Its readers disagree over whether freedom is secured by consent, shared councils, expert measure, disciplined separation, or the right to revise the book itself.\n\nAs the experiment takes hold, shortages, public works, local charters, and agreements with neighboring states test every interpretation. Promises are judged through visible provision and conduct, while each territorial case asks whether necessity can cross a border without becoming appetite.",
  "D16": "Glosses in the Margin\n\nThe recovered manuscript no longer speaks with one voice. Rival translations, household annotations, and public commentaries have become organized schools of interpretation. Delegates arrive carrying copies marked by workshops, parishes, councils, and exiles. The argument over the book has become an institution of its own, and the eventual commonwealth will be shaped by whoever keeps the right to write in its margins.",
  "E16": "Necessary Shores\n\nMigration, blockade, crowded housing, and uncertain supply have pushed the common store against the limits of the map. Surveyors now distinguish want from ambition before they mark a harbor, corridor, settlement, or lease as necessary ground. Domestic works remain possible, and every foreign offer leaves a record. The experiment must decide whether need can cross a border without turning into appetite.",
  "F16": "Cities of One Measure\n\nThe settlement plan has escaped the capital. Cooperative municipalities, associated towns, and rebuilt districts repeat its gardens, clinics, workshops, stores, and transport links in different soil. Each place adapts the design to local votes and local shortages. Their growing network makes the manifesto visible in ordinary streets, while disputes over assignment reveal who is allowed to alter the plan.",
  "G16": "Nowhere Made Law\n\nThe manifesto has become a regional legal identity. Governments and movements invoke it when they negotiate association, refuse an ultimatum, request aid, or defend local charters. Sponsors offer protection with conditions, rivals describe every storehouse as a disguised frontier, and small states judge whether the commonwealth is refuge, partner, or threat. An imagined country has become a claim that diplomacy must answer.",
  "H16": "The Perfect Island\n\nOrdinary regional order is breaking around a society trying to make one bounded place endure. Reserve trains, guarded harbors, refugee districts, fortification works, and member councils all pull against one another. A closed regime can harden the boundary into compulsory service. A voluntary commonwealth can distribute refuge among willing towns. Neither answer escapes the cost of keeping stores open while the roads beyond them fail.",
  "I16": null,
  "J16": "Minor Fire-Once",
  "K16": null,
  "L16": null,
  "M16": "Fully Functional"
}
```

## Exact Event 15 cells after

```json
{
  "A16": 15,
  "B16": "Utopia Manifesto",
  "C16": "A translated manifesto passes from reading rooms into the ministries of a small country. It proposes that public need should govern common stores, useful work, settlements, and the obligations of citizenship. Its readers disagree over whether freedom is secured by consent, shared councils, expert measure, disciplined separation, or the right to revise the book itself.\n\nAs the experiment takes hold, shortages, public works, local charters, and agreements with neighboring states test every interpretation. Promises are judged through visible provision and conduct, while each territorial case asks whether necessity can cross a border without becoming appetite.",
  "D16": "Glosses in the Margin\n\nThe recovered manuscript no longer speaks with one voice. Rival translations, household annotations, and public commentaries have become organized schools of interpretation. Delegates arrive carrying copies marked by workshops, parishes, councils, and exiles. The argument over the book has become an institution of its own, and the eventual commonwealth will be shaped by whoever keeps the right to write in its margins.",
  "E16": "Necessary Shores\n\nMigration, blockade, crowded housing, and uncertain supply have pushed the common store against the limits of the map. Surveyors now distinguish want from ambition before they mark a harbor, corridor, settlement, or lease as necessary ground. Domestic works remain possible, and every foreign offer leaves a record. The experiment must decide whether need can cross a border without turning into appetite.",
  "F16": "Cities of One Measure\n\nThe settlement plan has escaped the capital. Cooperative municipalities, associated towns, and rebuilt districts repeat its gardens, clinics, workshops, stores, and transport links in different soil. Each place adapts the design to local votes and local shortages. Their growing network makes the manifesto visible in ordinary streets, while disputes over assignment reveal who is allowed to alter the plan.",
  "G16": "Nowhere Made Law\n\nThe manifesto has become a regional legal identity. Governments and movements invoke it when they negotiate association, refuse an ultimatum, request aid, or defend local charters. Sponsors offer protection with conditions, rivals describe every storehouse as a disguised frontier, and small states judge whether the commonwealth is refuge, partner, or threat. An imagined country has become a claim that diplomacy must answer.",
  "H16": "The Perfect Island\n\nOrdinary regional order is breaking around a society trying to make one bounded place endure. Reserve trains, guarded harbors, refugee districts, fortification works, and member councils all pull against one another. The closed route hardens the boundary through compulsory service and carries the cost inside its gates. The voluntary route distributes refuge among willing towns and spreads the obligation across its members. Stores must remain open as the roads beyond them fail.",
  "I16": null,
  "J16": "Minor Fire-Once",
  "K16": null,
  "L16": null,
  "M16": "Fully Functional"
}
```

## Localisation source hashes

All hashes use SHA-256 and lowercase hexadecimal output.

- `value_sha256_utf8` hashes the exact decoded localisation value encoded as UTF-8.
- `source_line_sha256_utf8` hashes the exact UTF-8 source line without its line ending or file BOM.

| Localisation key | `value_sha256_utf8` | `source_line_sha256_utf8` |
| --- | --- | --- |
| `chaosx.event_name.15` | `ad41ee71047f14be7eb4c033e356d43120c0ff20cc67c052c242bf78a78c4983` | `19cef4b35ede10a3a30573fe46682b2d3a11c31702dc54fdfe699593f46bd1a5` |
| `chaosx.events_log.window.event_details.utopia_manifesto` | `3b1063b91d076a60722212bff5925cf6db2184323296d2e4f375f658f46be51a` | `c1842ad7e7f633223ca57fc1962a59bb38ad9cf0c545b747cbefb43adfd9bbf5` |
| `utopia_manifesto.evolution.1.title` | `14062b31fa8cf0c02a15b99b8682caf94ffbe3a16494d6f749491327be78200b` | `dc96c791f9083e367097f43763df1d401501299b2d6d1627887a2557df39667f` |
| `utopia_manifesto.evolution.1.body` | `ec17815a331c1a2295cda423d020b7d80e0fd43d0279f88f2947d23bd1fa5104` | `86c02008d07acafc4a1f73e9b520ee41cf90eec140c196c137cd3b7302828c58` |
| `utopia_manifesto.evolution.2.title` | `20cd79dfe26d37475e4feb5c2be2ef165284a112646fff5e85a3fb2f62439627` | `5d7e4223c0147c32fac4b63c37ff2623dfa1f0e620a839a8334d9730f68f3c26` |
| `utopia_manifesto.evolution.2.body` | `a64a7864b7dc294083ccad72a85e08e00c086814aaeb0abc09c8e6b4c0ac6f2b` | `0c4f57739c09335e69066b0d391d0a1d81b634c1119dc62f296c26afe2af52fc` |
| `utopia_manifesto.evolution.3.title` | `e7ba2787a556f1dca450034b4cfd02f7854577b7baabb889fd26bebaded28fef` | `e52123190f8da27249e2a4aa876a494988225503cc4fedb4e2b2900ec0713250` |
| `utopia_manifesto.evolution.3.body` | `71173bd70b8eb436c85d3aa0dd1950b4c27bdd3c8564e28444b7ecfffff2af46` | `803447417403d2be51b586aa9019cc57eac97f76668a07bf28f389075dc8720f` |
| `utopia_manifesto.evolution.4.title` | `a8c6289b6a94b84f1500c47625028d5df65010b70a92ea535d4a3f6ad218b8ca` | `8bcb5dd287c9aef7e648427e2f89394c8d46481624547224d01f159b58bf99a7` |
| `utopia_manifesto.evolution.4.body` | `a1319c2d829b61c26ef1b943ca29c326474499d8e1dfc67b0046c680c6912947` | `da6d6eebdcccfbe724175ce8de29a616ed456a9bc5bab22e8992207be4abc611` |
| `utopia_manifesto.evolution.5.title` | `838337e653e41c3879997ac4944a270ca4b685a986e284c061ab72355b0b5716` | `5469f9ae0288ba66d37678f88b47454f329c06f46de9b2e4ee8b8df146f4a1a5` |
| `utopia_manifesto.evolution.5.body` | `e0e075856eb7f8e0d1f41ce31426415d17bf313946846e2357033d948cd5ad9c` | `7a3965e541b6e8aa8c1c29559ebad906d3ca243d7334d962c0d91cbff4a4eb5c` |

Source file hashes at reconciliation time:

| Source file | SHA-256 |
| --- | --- |
| `localisation/english/015_utopia_manifesto_evolutions_l_english.yml` | `508786fb2a6d8b0b1efa51dca67467a8241c25d9aa141528c9e44b590b1d1c01` |
| `localisation/english/chaosx_gui_l_english.yml` | `451862430b424bf603626fac24aa66dad17120c3517c0447b41edb435e83ac1b` |
| `localisation/english/chaosx_event_names_l_english.yml` | `2e1c78a86e307b8cc19ebc735d02b52fb82d470eecea20133d2874c0c6a2796e` |

Final player-facing cell hashes:

| Cell | SHA-256 of exact UTF-8 value |
| --- | --- |
| `B16` | `ad41ee71047f14be7eb4c033e356d43120c0ff20cc67c052c242bf78a78c4983` |
| `C16` | `3b1063b91d076a60722212bff5925cf6db2184323296d2e4f375f658f46be51a` |
| `D16` | `c62381e7a169616993fc62127d7e720089dfb621aed36944fb6979cd1f021b9a` |
| `E16` | `4dcb2f732af67a2e4730e62d3a65f189c80f9d480612d9c4bd8c6dfb78a47da7` |
| `F16` | `c055f5f4025553464ee396e9a197298c1042a2938b1b1f5693b8f464b2a3bdd6` |
| `G16` | `a359ce4d6c882d7a513bebeca6d710a2d96592b6b0c850d00a2d3e35fd0719c5` |
| `H16` | `b14a3d96f6507efadd4490af9dd6737b05e5ab3b0e4c749320a8c1daa926c541` |

## Workbook preservation proof

The edit used `C:\Program Files\Python39\python.exe`, Python 3.9.12, and `openpyxl 3.1.5`. The validated package was written to a temporary file, reopened, compared against the exact pre-edit workbook, and only then atomically replaced the catalog. The writer path retained the workbook core properties instead of changing the internal modified timestamp.

Workbook SHA-256:

- Before: `1e787d3fb88d11e5e01ea0a6c2a92bb690c434e620c8e0262ade6002ced8ac7f`
- After: `3c324b75c26f9e17eb9e73761abc5aedfa9bb642f2108a1397fb240679614031`

Logical comparison results:

| Evidence | Before | After | Result |
| --- | --- | --- | --- |
| Workbook structure digest | `3c5bcab2476b0ef71e49d4b070dd67175f91ea8f948c7b8af8fedb3f40995518` | `3c5bcab2476b0ef71e49d4b070dd67175f91ea8f948c7b8af8fedb3f40995518` | Equal |
| Workbook style bundle digest | `361d38028c2f9d924922d76369ed1958b5360bd42654cf573913977aa1b22fd3` | `361d38028c2f9d924922d76369ed1958b5360bd42654cf573913977aa1b22fd3` | Equal |
| Every instantiated cell except `Events!H16` | `b5d9d6e80721e4aa5a091ec0e99aa00159d2a131c70f5124514c064d8bbd5b8d` | `b5d9d6e80721e4aa5a091ec0e99aa00159d2a131c70f5124514c064d8bbd5b8d` | Equal |
| Event 19 `Events!A20:M20` values and styles | `5671a5070e0118fa2f1ce3ab365ed76bb3764873500ef7357b4d72069d1ca836` | `5671a5070e0118fa2f1ce3ab365ed76bb3764873500ef7357b4d72069d1ca836` | Equal |
| `Scenarios!A11:F11` values and styles | `8685451d0d70aa533628a2af4feb6a26c84fa18df89ef67b7a8766a8ceece9f7` | `8685451d0d70aa533628a2af4feb6a26c84fa18df89ef67b7a8766a8ceece9f7` | Equal |

The full cell comparison produced:

- Changed values: `Events!H16` only.
- Changed cell styles: none.
- Changed comments, hyperlinks, quote-prefix flags, or pivot-button flags: none.
- Event 15 style IDs before and after: `A16:M16 = [49, 43, 43, 50, 51, 52, 53, 54, 55, 60, 57, 57, 64]`.
- Event 15 row height before and after: `409.5`.

The structure digest covers sheet order and states, dimensions, row and column dimensions, filters, freeze panes, validation definitions and ranges, merged ranges, workbook and sheet properties, views, page settings, tables, conditional formatting, named ranges, named styles, images, charts, calculation properties, and external links.

The reopened workbook retained these sheet dimensions and validation counts:

| Sheet | Dimensions | Data validations | Freeze panes | Auto-filter | Merged ranges |
| --- | --- | ---: | --- | --- | ---: |
| `Events` | 1015 rows by 13 columns | 3 | none | none | 0 |
| `Clusters` | 13 rows by 7 columns | 3 | none | none | 0 |
| `Scenarios` | 11 rows by 6 columns | 1 | none | none | 0 |
| `Info` | 1 row by 1 column | 0 | none | none | 0 |
| `Legend` | 24 rows by 4 columns | 0 | none | none | 0 |

The workbook contains zero formulas and zero error-valued cells, so formula recalculation was not applicable.

## Parity checklist

- `B16` equals `chaosx.event_name.15`.
- `C16` equals `chaosx.events_log.window.event_details.utopia_manifesto`.
- `D16:H16` each equal the matching title, two LF characters, and body from `utopia_manifesto.evolution.1` through `.5`.
- `I16` is blank.
- `J16` is `Minor Fire-Once`.
- `K16` and `L16` are blank.
- `M16` is `Fully Functional`.
- The forbidden fifth-evolution frame is absent from the final workbook.
- Event 19 and `Scenarios!11` remain logically identical to the pre-edit working file.

## Files changed

- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/spreadsheet_catalog_post_localisation_reaudit_2026_07_16.md`

## Limitations, omissions, fallbacks, and blockers

There are no limitations, omissions, fallbacks, simplifications, or blockers. No gameplay, localisation, specs, assets, Event 19 cells, Scenarios row 11 cells, or unrelated workbook content were edited. No commit was created, as required by the parent task.
