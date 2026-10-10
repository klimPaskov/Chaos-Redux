# Event 032 catalog changes pending

These changes belong in `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, sheet `Events`, row 33 (ID `32`, Missiles).
The two wording changes were applied by the catalog worker on 2026-10-07 and verified against the in-game localisation.
The handoff is `subagent_handoffs/032_catalog_alignment_2026-10-07.md`; the retained status below supersedes the prior promotion proposal.
After applying them to the workbook, run `python .tools/export_event_catalog_csv.py` from the mod root.

| Cell | Column | Previous value | Applied value | Reason |
| --- | --- | --- | --- | --- |
| `M33` | Status | `To Be Reworked` | `To Be Reworked` (retain) | The full accepted gameplay and validation contract remains incomplete; default enablement does not authorize a status promotion. |
| `D33` | Evo I | Growing reserves and larger launch sites can support massed salvos. Saturation attacks can overwhelm defences, but they consume many missiles and strain readiness and command control. | Countries with working launch sites and enough industry can adopt a saturation doctrine for massed salvos. Saturation attacks can overwhelm defences, but they consume many missiles and strain readiness and command control. | Saturation Arsenals is now an explicit country doctrine; matches `missiles.evolution.saturation.body`. |
| `H33` | Evo V | Governments can delegate retaliation to officers or automatic warning systems. A disputed alert may be verified, delayed, or stopped by severing the network before missiles leave their sites. | Governments can choose to delegate retaliation to officers or automatic warning systems. A disputed alert may be verified, delayed, or stopped by severing the network before missiles leave their sites. | Retaliation posture is now an explicit country choice that starts Off; matches `missiles.evolution.automatic_retaliation.body`. |

The `Details`, `Evo II`, `Evo III`, and `Evo IV` cells already match `missiles.event_log.detail`, `missiles.evolution.unreliable_guidance.body`, `missiles.evolution.special_warheads.body`, and `missiles.evolution.rogue_commands.body` and need no change.

Disposition: the exact `D33` and `H33` wording is `implemented` under the user's catalog/localisation alignment goal, with repository-generated CSV exports and a two-cell HEAD projection for the shared-tree commit.
The former `M33 = Needs Testing` proposal is `superseded` by the retained status above following the current contract reconciliation at `subagent_handoffs/032_current_contract_reconciliation_2026-10-07.md`.
This distinction preserves the post-20 existing-root status rule and does not treat incomplete gameplay or source-only validation as completion.

2026-10-10: the Details, Evo I and Evo III cells (`C33`, `D33`, `F33`) were respelled to US English (programs, defenses, authorized) to match the in-game text; status stays `To Be Reworked`.
