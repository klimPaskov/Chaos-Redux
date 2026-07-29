# Event 015 Spreadsheet Current Hash Follow-Up

Status: **PASS — Event 15 catalog parity confirmed; no workbook or CSV edits made**

Audit date: 2026-07-18  
Scope: read-only verification of Event 15 catalog authority after mixed workbook/export drift.  
Authority: `docs/spreadsheets/chaos_redux_events_catalog.xlsx` (the CSVs are read-only exports).

## Current artifact hashes

SHA-256 was computed over each current file's exact bytes:

| Artifact | Current SHA-256 |
| --- | --- |
| `docs/spreadsheets/chaos_redux_events_catalog.xlsx` | `ed52b1f3ee3f0e602b3cc6a4b5fd7bc0d340445a3c085c6c8531fbcd2c0430f4` |
| `docs/spreadsheets/chaos_redux_events_catalog.csv` | `7303641c56a4f5defe8827901ceda5717b1006ddd5936f76616733516fa999ce` |
| `docs/spreadsheets/chaos_redux_clusters_catalog.csv` | `f6f68b0bd3110ce63dc5a4c54303e9d85fb9ad859cb4b2d87897d067e1088c6f` |
| `docs/spreadsheets/chaos_redux_scenarios_catalog.csv` | `1b3a73517df6e97ad0237ef6c77f9d383a3e170eedf51a09f0f416448a70b5f8` |

The workbook hash differs from the prior final-audit snapshot (`729e48a3135094d210b70e74ce3694ff0b66dbd5d2bc448051db931a41f4bd80`), so this follow-up uses the files currently on disk rather than assuming the prior snapshot remains current.

## Exact `Events!A16:M16` evidence

The authoritative Event 15 row is `Events!A16:M16`. Workbook blanks are `None`; for parity comparison they normalize to the empty CSV field (`''`). Workbook ID `A16` is numeric `15`; the export represents it as CSV text `15`.

| Cell | Field | Current value / decoded shape | UTF-8 value SHA-256 | Source/parity result |
| --- | --- | --- | --- | --- |
| `A16` | ID | `15` (numeric XLSX cell) | `e629fa6598d732768f7c726b4b621285f9c3b85303900aa912017db7617d8bdb` | Matches Event ID 15; CSV-normalized parity PASS |
| `B16` | Event Name | `Utopia Manifesto` (16 chars) | `ad41ee71047f14be7eb4c033e356d43120c0ff20cc67c052c242bf78a78c4983` | Exact `chaosx.event_name.15`; source parity PASS |
| `C16` | Event Details | 664 chars, 2 LF characters | `3b1063b91d076a60722212bff5925cf6db2184323296d2e4f375f658f46be51a` | Exact `chaosx.events_log.window.event_details.utopia_manifesto`; source parity PASS |
| `D16` | Evo I | `Glosses in the Margin` + 2 LF + body (444 chars) | `c62381e7a169616993fc62127d7e720089dfb621aed36944fb6979cd1f021b9a` | Exact evolution 1 title/body; source parity PASS |
| `E16` | Evo II | `Necessary Shores` + 2 LF + body (423 chars) | `4dcb2f732af67a2e4730e62d3a65f189c80f9d480612d9c4bd8c6dfb78a47da7` | Exact evolution 2 title/body; source parity PASS |
| `F16` | Evo III | `Cities of One Measure` + 2 LF + body (430 chars) | `c055f5f4025553464ee396e9a197298c1042a2938b1b1f5693b8f464b2a3bdd6` | Exact evolution 3 title/body; source parity PASS |
| `G16` | Evo IV | `Nowhere Made Law` + 2 LF + body (445 chars) | `a359ce4d6c882d7a513bebeca6d710a2d96592b6b0c850d00a2d3e35fd0719c5` | Exact evolution 4 title/body; source parity PASS |
| `H16` | Evo V | `The Perfect Island` + 2 LF + body (501 chars) | `b14a3d96f6507efadd4490af9dd6737b05e5ab3b0e4c749320a8c1daa926c541` | Exact evolution 5 title/body; source parity PASS |
| `I16` | World-End Scenario | Blank (`None` in XLSX, empty CSV field) | — | No Event 15 world-end mapping; parity PASS |
| `J16` | Type | `Minor Fire-Once` (15 chars) | `07623ecfb458a2075245ab599d180142c88c5b801a5a9021efe35661f1b2dd3a` | Matches `chaosx.nr15.1` `fire_only_once = yes`; classification parity PASS |
| `K16` | Cluster ID | Blank (`None` in XLSX, empty CSV field) | — | No Event 15 cluster mapping; parity PASS |
| `L16` | Member Severity | Blank (`None` in XLSX, empty CSV field) | — | Correct for non-cluster member; parity PASS |
| `M16` | Status | `Fully Functional` (16 chars) | `e2d509fa92b05eff98410ba771ab4e8714731a22a96c34b4a32916e1b4b7e161` | Exact current status; parity PASS |

The normalized full-row SHA-256 for `A16:M16` (JSON array, UTF-8, compact separators, blanks normalized to `''`) is `e330489603bd739e64fc356b8bb79498c4a34d54433f28cda4c2ba459dadab1e`. All 13 cells compare equal to the expected decoded source row.

The localisation files store `\\n` as two-character escape sequences. For this audit those escapes were decoded to actual LF characters before comparison; each evolution field therefore contains exactly two LF characters between its title and body, matching the workbook cell representation.

## Export parity

The current Events CSV row with ID `15` is CSV row 16 and matches the normalized workbook row in all 13 columns (`A16:M16` ↔ CSV row 16: 13/13 equality). The three blank fields (`I`, `K`, `L`) are empty CSV fields, as expected. No `Utopia` or `Manifesto` entry exists in the current Clusters or Scenarios exports.

## Unrelated drift classification

Event 15 is unchanged relative to the prior spreadsheet final-audit evidence: its populated mirror-cell hashes (`B16:H16`) and exact decoded source values are identical, and the current Events export row remains equal to the workbook row. The current artifact hashes therefore represent mixed catalog/export drift outside this Event 15 row, not an Event 15 mismatch.

For a concrete working-tree comparison against the tracked baseline, the export-only diffs are on unrelated entries: Events IDs `6`, `11`, and `19`; Clusters row/ID `2`; and Scenarios `SCN-008` addition plus `SCN-009`, `SCN-010`, and `SCN-013` content changes. None touches Event ID `15`. Those files remain untouched in this follow-up.

## Files inspected

- `docs/spreadsheets/chaos_redux_events_catalog.xlsx` (`Events!A16:M16`; workbook structure read-only)
- `docs/spreadsheets/chaos_redux_events_catalog.csv`
- `docs/spreadsheets/chaos_redux_clusters_catalog.csv`
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv`
- `localisation/english/chaosx_event_names_l_english.yml` (`chaosx.event_name.15`)
- `localisation/english/chaosx_gui_l_english.yml` (`chaosx.events_log.window.event_details.utopia_manifesto`)
- `localisation/english/015_utopia_manifesto_evolutions_l_english.yml` (five title/body pairs)
- `events/015_utopia_manifesto.txt` (entry root `chaosx.nr15.1`, `fire_only_once = yes`)
- `docs/events/015_utopia_manifesto/overview.md` (current five-evolution inventory and Event Details mapping)
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/spreadsheet_final_audit_2026_07_18.md` (prior comparison evidence)
- `docs/specs/015_utopia_manifesto_specs/matrices/completion_coverage_matrix.md` (current completion matrix)

## No-edit confirmation

This was an audit-only follow-up. The workbook was not opened for save, no CSV was edited, and `python .tools/export_event_catalog_csv.py` was intentionally **not run** because no Event 15 catalog change was required and mixed unrelated rows already exist. No blocked or `needs_user_review` Event 15 cells were found.
