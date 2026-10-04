# Event 032 catalog changes pending

These changes belong in `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, sheet `Events`, row 33 (ID `32`, Missiles).
They are staged here because the workbook and its CSV exports are owned by the catalog worker in the shared tree.
After applying them to the workbook, run `python .tools/export_event_catalog_csv.py` from the mod root.

| Cell | Column | Current value | New value | Reason |
| --- | --- | --- | --- | --- |
| `M33` | Status | `To Be Reworked` | `Needs Testing` | Event 32 is back in the default-enable allowlist after the 2026-10-04 gameplay round; live validation is still required. |
| `D33` | Evo I | Growing reserves and larger launch sites can support massed salvos. Saturation attacks can overwhelm defences, but they consume many missiles and strain readiness and command control. | Countries with working launch sites and enough industry can adopt a saturation doctrine for massed salvos. Saturation attacks can overwhelm defences, but they consume many missiles and strain readiness and command control. | Saturation Arsenals is now an explicit country doctrine; matches `missiles.evolution.saturation.body`. |
| `H33` | Evo V | Governments can delegate retaliation to officers or automatic warning systems. A disputed alert may be verified, delayed, or stopped by severing the network before missiles leave their sites. | Governments can choose to delegate retaliation to officers or automatic warning systems. A disputed alert may be verified, delayed, or stopped by severing the network before missiles leave their sites. | Retaliation posture is now an explicit country choice that starts Off; matches `missiles.evolution.automatic_retaliation.body`. |

The `Details`, `Evo II`, `Evo III`, and `Evo IV` cells already match `missiles.event_log.detail`, `missiles.evolution.unreliable_guidance.body`, `missiles.evolution.special_warheads.body`, and `missiles.evolution.rogue_commands.body` and need no change.

Disposition: `accepted and queued` — accepted under the user's grant of full implementation authority (lead decision 8); queued because the workbook is outside this owner's write scope.
