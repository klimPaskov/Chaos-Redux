# Event 015 Spreadsheet Final Audit

Status: **PASS — no workbook change required**

Audit date: 2026-07-18  
Workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`  
Workbook SHA-256: `729e48a3135094d210b70e74ce3694ff0b66dbd5d2bc448051db931a41f4bd80`

## Exact cells and fields audited

The authoritative `Events` row is `Events!A16:M16` (numeric ID 15). Every checked value matched the current player-facing source:

| Cell | Field | Result |
| --- | --- | --- |
| `A16` | ID | `15` |
| `B16` | Event Name | `Utopia Manifesto` |
| `C16` | Event Details | Exact `chaosx.events_log.window.event_details.utopia_manifesto` value |
| `D16` | Evo I | Exact evolution 1 title + two LF characters + body |
| `E16` | Evo II | Exact evolution 2 title + two LF characters + body |
| `F16` | Evo III | Exact evolution 3 title + two LF characters + body |
| `G16` | Evo IV | Exact evolution 4 title + two LF characters + body |
| `H16` | Evo V | Exact evolution 5 title + two LF characters + body |
| `I16` | World-End Scenario | Blank; no Event 15 world-end mapping |
| `J16` | Type | `Minor Fire-Once` |
| `K16` | Cluster ID | Blank; no Event 15 cluster mapping |
| `L16` | Member Severity | Blank |
| `M16` | Status | `Fully Functional` |

Exact UTF-8 value hashes for the populated player-facing cells:

| Cell | SHA-256 |
| --- | --- |
| `B16` | `ad41ee71047f14be7eb4c033e356d43120c0ff20cc67c052c242bf78a78c4983` |
| `C16` | `3b1063b91d076a60722212bff5925cf6db2184323296d2e4f375f658f46be51a` |
| `D16` | `c62381e7a169616993fc62127d7e720089dfb621aed36944fb6979cd1f021b9a` |
| `E16` | `4dcb2f732af67a2e4730e62d3a65f189c80f9d480612d9c4bd8c6dfb78a47da7` |
| `F16` | `c055f5f4025553464ee396e9a197298c1042a2938b1b1f5693b8f464b2a3bdd6` |
| `G16` | `a359ce4d6c882d7a513bebeca6d710a2d96592b6b0c850d00a2d3e35fd0719c5` |
| `H16` | `b14a3d96f6507efadd4490af9dd6737b05e5ab3b0e4c749320a8c1daa926c541` |

The populated row retains the existing formatting; `Events!A16` row height is `409.5` and the existing style IDs for the row were not rewritten.

## Mirror sources and hashes

The source values were read from the current English localisation files. `value_sha256_utf8` hashes the decoded player-facing value. `source_line_sha256_utf8` hashes the exact source line without its line ending.

| Key | Source file | value_sha256_utf8 | source_line_sha256_utf8 |
| --- | --- | --- | --- |
| `chaosx.event_name.15` | `localisation/english/chaosx_event_names_l_english.yml` | `ad41ee71047f14be7eb4c033e356d43120c0ff20cc67c052c242bf78a78c4983` | `19cef4b35ede10a3a30573fe46682b2d3a11c31702dc54fdfe699593f46bd1a5` |
| `chaosx.events_log.window.event_details.utopia_manifesto` | `localisation/english/chaosx_gui_l_english.yml` | `3b1063b91d076a60722212bff5925cf6db2184323296d2e4f375f658f46be51a` | `c1842ad7e7f633223ca57fc1962a59bb38ad9cf0c545b747cbefb43adfd9bbf5` |
| `utopia_manifesto.evolution.1.title` | `localisation/english/015_utopia_manifesto_evolutions_l_english.yml` | `14062b31fa8cf0c02a15b99b8682caf94ffbe3a16494d6f749491327be78200b` | `dc96c791f9083e367097f43763df1d401501299b2d6d1627887a2557df39667f` |
| `utopia_manifesto.evolution.1.body` | `localisation/english/015_utopia_manifesto_evolutions_l_english.yml` | `ec17815a331c1a2295cda423d020b7d80e0fd43d0279f88f2947d23bd1fa5104` | `86c02008d07acafc4a1f73e9b520ee41cf90eec140c196c137cd3b7302828c58` |
| `utopia_manifesto.evolution.2.title` | `localisation/english/015_utopia_manifesto_evolutions_l_english.yml` | `20cd79dfe26d37475e4feb5c2be2ef165284a112646fff5e85a3fb2f62439627` | `5d7e4223c0147c32fac4b63c37ff2623dfa1f0e620a839a8334d9730f68f3c26` |
| `utopia_manifesto.evolution.2.body` | `localisation/english/015_utopia_manifesto_evolutions_l_english.yml` | `a64a7864b7dc294083ccad72a85e08e00c086814aaeb0abc09c8e6b4c0ac6f2b` | `0c4f57739c09335e69066b0d391d0a1d81b634c1119dc62f296c26afe2af52fc` |
| `utopia_manifesto.evolution.3.title` | `localisation/english/015_utopia_manifesto_evolutions_l_english.yml` | `e7ba2787a556f1dca450034b4cfd02f7854577b7baabb889fd26bebaded28fef` | `e52123190f8da27249e2a4aa876a494988225503cc4fedb4e2b2900ec0713250` |
| `utopia_manifesto.evolution.3.body` | `localisation/english/015_utopia_manifesto_evolutions_l_english.yml` | `71173bd70b8eb436c85d3aa0dd1950b4c27bdd3c8564e28444b7ecfffff2af46` | `803447417403d2be51b586aa9019cc57eac97f76668a07bf28f389075dc8720f` |
| `utopia_manifesto.evolution.4.title` | `localisation/english/015_utopia_manifesto_evolutions_l_english.yml` | `a8c6289b6a94b84f1500c47625028d5df65010b70a92ea535d4a3f6ad218b8ca` | `8bcb5dd287c9aef7e648427e2f89394c8d46481624547224d01f159b58bf99a7` |
| `utopia_manifesto.evolution.4.body` | `localisation/english/015_utopia_manifesto_evolutions_l_english.yml` | `a1319c2d829b61c26ef1b943ca29c326474499d8e1dfc67b0046c680c6912947` | `da6d6eebdcccfbe724175ce8de29a616ed456a9bc5bab22e8992207be4abc611` |
| `utopia_manifesto.evolution.5.title` | `localisation/english/015_utopia_manifesto_evolutions_l_english.yml` | `838337e653e41c3879997ac4944a270ca4b685a986e284c061ab72355b0b5716` | `5469f9ae0288ba66d37678f88b47454f329c06f46de9b2e4ee8b8df146f4a1a5` |
| `utopia_manifesto.evolution.5.body` | `localisation/english/015_utopia_manifesto_evolutions_l_english.yml` | `e0e075856eb7f8e0d1f41ce31426415d17bf313946846e2357033d948cd5ad9c` | `7a3965e541b6e8aa8c1c29559ebad906d3ca243d7334d962c0d91cbff4a4eb5c` |

Current source-file SHA-256 values: `015_utopia_manifesto_evolutions_l_english.yml` = `508786fb2a6d8b0b1efa51dca67467a8241c25d9aa141528c9e44b590b1d1c01`; `chaosx_gui_l_english.yml` = `6810c1c888a171926e2841de0b4366773b9e6490ddc6e01a7faca90dc86b691f`; `chaosx_event_names_l_english.yml` = `ba57396a4e1b939f4e589ea38639694d6e9ab4c48f39df0b41c603be9d62421e`.

## Workbook-wide integrity evidence

- Formula counts are zero on `Events`, `Clusters`, `Scenarios`, `Info`, and `Legend`.
- Artifact-tool error scan for `#REF!|#DIV/0!|#VALUE!|#NAME?|#N/A` matched zero cells.
- `World Tension Subsides` matched zero workbook cells.
- The only exact numeric/string `15` cell is `Events!A16`; there is no stale ID 15 mapping elsewhere.
- `Clusters` and `Scenarios` contain no `Utopia` or `Manifesto` entries.
- Existing workbook ranges remain `Events!A1:M1015`, `Clusters!A1:G13`, `Scenarios!A1:F12`, `Info!A1`, and `Legend!A1:D24`.
- Existing table counts remain one each on `Events`, `Clusters`, and `Scenarios`; no tables exist on `Info` or `Legend`.
- Existing data-validation counts remain 3 (`Events`), 3 (`Clusters`), 1 (`Scenarios`), 0 (`Info`), and 0 (`Legend`).
- A visual render pass completed for all five sheets (`Events` A1:M20, `Clusters` A1:G13, `Scenarios` A1:F12, `Info` A1, `Legend` A1:D24).

## Export and limitations

The workbook was not changed, so `python .tools/export_event_catalog_csv.py` was intentionally **not run** and the export-only CSV snapshots were not churned. No blocked or `needs_user_review` cells were found. This bounded audit did not inspect or modify gameplay, event scripts, or unrelated localisation.

