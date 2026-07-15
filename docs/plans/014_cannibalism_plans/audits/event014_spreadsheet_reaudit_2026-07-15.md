# Event 014 Spreadsheet Re-audit

> Superseded for current authority by `event014_spreadsheet_consolidation_reaudit_2026-07-15.md`. This same-day checkpoint remains historical evidence only.

Date: 2026-07-15

Workbook: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`

SHA-256: `6aa758d699d814599a1011d5f9acc1089bbf42baf053be7a4dbabadd525091a2`

## Result

No Event 014 workbook edit was required. The Event 014 and SCN-010 rows contain no reference to the removed origin package, no fixed slot-to-origin mapping, and no obsolete local-tree or asset count. Concurrent workbook changes outside this event add `SCN-013`; the Event 014 audit preserves that row and does not stage the workbook.

## Cell reconciliation

- `Events!A15:B15` identifies Event 14 as Cannibalism.
- `Events!D15:F15` matches the in-game evolution titles `cannibalism.evolution.stage_1.title`, `cannibalism.evolution.stage_2.title`, and `cannibalism.evolution.stage_3.title`: Ritualized Ranks, The Organized Network, and Hannibal Lecter Commands.
- `Events!J15` remains Minor Fire-Once, and Event 014 remains outside every cluster row.
- `Events!M15` records `Fully Functional`.
- `Scenarios!A10:B10` identifies `SCN-010` as The Hunger Lines.
- `Scenarios!D10` matches the five in-game scenario types: Discipline Collapse, Ritual Cells, Silent Islands, Warlord States, and Convergence.
- `Scenarios!C10` describes warlord states generically through regional command and origin doctrine. It does not reserve any tag or advertise a removed origin.
- `Scenarios!F10` records `Fully Functional`.

The workbook contains no formulas and no Excel error values. Reading and verification did not alter workbook formatting, values, metadata, or cached state.
