# FALLOUT-565 catalog handoff

Updated `docs/spreadsheets/chaos_redux_events_catalog.xlsx` on the `Events` sheet at row 244 for `FALLOUT-565`, `The River Ration League`.

Changed cells: `A244:M244`.

- `A244`: `FALLOUT-565`.
- `B244`: `The River Ration League`.
- `C244`: mirrors the event detail for the Europe Danube corridor and records the ordinary dormant chain, candidate 565, transaction 710053, route 7153, and Event Log history 9158.
- `D244:G244`: four reviewed branches matching the in-game choices and 42-day result wording: joint barge law, upstream depot priority, armed customs bridges, and flood authority.
- `H244`: intentionally blank; no fifth evolution is implemented for this chain.
- `I244`: records the 180-day callback, event blocks 565 through 571, authenticated cleanup, no population loss in this tranche, dedicated report asset, and hidden AI parity.
- `J244:M244`: `Crisis`, blank cluster id, blank member severity, and `Needs Testing`, matching the existing `FALLOUT-554` row convention.

No `Clusters` row or manual `Scenarios` row was added because the workbook has no Fallout crisis cluster convention and the requested catalog entry is an ordinary regional event chain.

After saving the workbook, `python .tools/export_event_catalog_csv.py` completed successfully. It refreshed all three export-only snapshots: Events (244 rows, 13 columns, SHA-256 `d40509292d20d5ffb2f64cb4134162783e60b8687148eb2b349ef0920f275108`), Clusters (13 rows, 7 columns, SHA-256 `7cc6d9394240b3f69e39c4dd102a0c6b6b00978f26998a5bda7f96b696333a50`), and Scenarios (12 rows, 6 columns, SHA-256 `de802e37f03d55b242b693adb02c6a921d56729f31c671c26ef7bddc2ebe45b7`).

Remaining risks: `M244` remains `Needs Testing` by the existing catalog convention, and the dynamic state-name tokens in `C244` require the live event scopes to resolve in game.
