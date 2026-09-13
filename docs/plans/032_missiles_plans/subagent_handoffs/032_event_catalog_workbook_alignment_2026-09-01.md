# Event 32 spreadsheet catalog handoff — 2026-09-01

Disposition: implemented and current. The authoritative workbook was updated and the repository exporter regenerated all three CSV exports; the recorded hashes remain the source-aligned evidence for the current Event 32 catalog state.

## Scope

Updated only the authoritative workbook at `docs/spreadsheets/chaos_redux_events_catalog.xlsx` and refreshed its three export-only CSV snapshots with `python .tools/export_event_catalog_csv.py`.

The catalog values were aligned to the Event 32 specifications, `docs/events/032_missiles/overview.md`, and the current player-facing localisation keys in `localisation/english/032_missile_crisis_l_english.yml`.

No gameplay, localisation, scripted localisation, or other source files were edited.

## Exact workbook changes

### Events sheet, Event ID 32, Excel row 33

| Cell | Exact value |
| --- | --- |
| `Events!A33` | `32` |
| `Events!B33` | `Missiles` |
| `Events!C33` | `Missile programmes have spread across the world. Countries can build and harden launch sites, stock operational missiles, improve guidance, and secure the officers and codes that control them. Heavier arsenals, guidance failures, special warheads, rogue commands, and automatic retaliation can transform the crisis.` |
| `Events!D33` | `Growing reserves and larger launch sites can support massed salvos. Saturation attacks can overwhelm defences, but they consume many missiles and strain readiness and command control.` |
| `Events!E33` | `Faulty guidance can send missiles away from their intended targets. Drift, false warnings, interception, and damage to launch sites force commanders to investigate failures and contain their consequences.` |
| `Events!F33` | `Countries that already possess chemical, biological, nuclear, or thermonuclear weapons can adapt them for missile delivery. Each launch still requires an authorised warhead held in secure custody.` |
| `Events!G33` | `A compromised launch site can break from lawful authority while its crews still hold missiles and warheads. The government must regain control through new codes, isolation, negotiation, loyal forces, or the destruction of the site.` |
| `Events!H33` | `Governments can delegate retaliation to officers or automatic warning systems. A disputed alert may be verified, delayed, or stopped by severing the network before missiles leave their sites.` |
| `Events!I33` | blank; Event 32 has no world-end branch. |
| `Events!J33` | `Minor Repeatable` |
| `Events!K33` | numeric `1`, the Calm World minimum chaos value. |
| `Events!L33` | blank; Event 32 has no cluster. |
| `Events!M33` | `Needs Testing`. |

Event 32’s existing cell styles were retained, including styles on the newly populated evolution cells.

### Clusters sheet

Event 32 was removed from the legacy aggregate lists while all unrelated members and severities were retained.

| Cell | Exact value |
| --- | --- |
| `Clusters!D16` | `19, 29, 37, 42, 56, 64` |
| `Clusters!E16` | `Medium, Medium, Medium, Low, Medium, Medium` |
| `Clusters!D19` | `22, 23, 42, 56, 64` |
| `Clusters!E19` | `High, Severe, Low, Medium, Medium` |

### Cluster Memberships sheet

The two Event 32 membership slots were cleared in place so the table shape and unrelated slot rows remain intact.

| Cells | Exact value |
| --- | --- |
| `Cluster Memberships!A68:G68` | all cells blank; former Sudden Abundance/Event 32 slot removed. |
| `Cluster Memberships!A80:G80` | all cells blank; former Military Preparation/Event 32 slot removed. |

Adjacent membership rows and their styles were preserved.

### Scenarios sheet

The missing implemented manual scenario was added as the sorted `SCN-015` row at `Scenarios!15`, shifting the existing `SCN-018` row to row 16 without changing its values.

| Cell | Exact value |
| --- | --- |
| `Scenarios!A15` | `SCN-015` |
| `Scenarios!B15` | `Missile Age` |
| `Scenarios!C15` | `Global Proliferation: Establishes or expands missile programmes across eligible countries. Higher intensity grants stronger technology, larger reserves, more launch capacity, and better readiness without choosing a future crisis.` followed by `Saturation War: Turns an existing war between missile powers into an arms race. The belligerents gain larger arsenals and the ability to prepare saturation attacks, while neutral countries retain ordinary programmes.` followed by `Command Breakdown: Exposes vulnerable missile powers to guidance failures and rogue launch commands. Control may weaken and launch sites may defect, but the crisis does not begin with an immediate strike.` followed by `Special Payload Crisis: Allows countries that already possess special warheads and stockpiles to adapt them for missile delivery. The scenario grants no chemical, biological, nuclear, or thermonuclear weapon by itself.` followed by `Retaliation Network: Builds retaliation networks with warning systems and national response postures. Lower intensities avoid an immediate launch, while higher intensities place more pressure on the warning chain.` Each profile paragraph is separated by one blank line. |
| `Scenarios!D15` | `Global Proliferation, Saturation War, Command Breakdown, Special Payload Crisis, Retaliation Network` |
| `Scenarios!E15` | `§RStarts the Missile Age immediately.§! A limited group receives early missile technology, modest reserves, one launch site, and secure command.` followed by `§RStarts the Missile Age immediately.§! More countries receive stronger reserves and secondary launch sites, and missile crises may begin to develop.` followed by `§RStarts the Missile Age immediately.§! Most eligible countries receive mature regional programmes, larger reserves, advanced sites, and a greater risk of crisis.` followed by `§RStarts the Missile Age immediately.§! Every eligible country receives the strongest supported programme and faces the full range of missile risks. The campaign continues.` Each intensity paragraph is separated by one blank line. |
| `Scenarios!F15` | `Needs Testing` |

The `Manual_Scenarios` table, Scenario status validation, and Scenario status conditional-formatting range were extended from row 15 to row 16 to cover the inserted row.

## Validation

The final workbook opens as a valid XLSX package with the original five sheets: `Events`, `Clusters`, `Cluster Memberships`, `Scenarios`, and `Legend`.

The final dimensions are `Events!A1:M1014`, `Clusters!A1:H20`, `Cluster Memberships!A1:G83`, `Scenarios!A1:F16`, and `Legend!A1:D24`.

The workbook contains no formulas, so no formula recalculation was required; both formula scans were empty.

The final table references are `Events!A1:M1014`, `Clusters!A1:H20`, `Cluster Memberships!A1:G83`, and `Scenarios!A1:F16`.

The final Scenario validation and conditional-formatting ranges are both `F2:F16`, and Event 32 has a blank world-end field, a blank cluster field, and no remaining Event 32 entry in the aggregate cluster member lists or membership rows.

The exporter completed with this result:

```json
{
  "status": "success",
  "workbook": "C:\\Users\\klimp\\OneDrive\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\chaos_redux\\docs\\spreadsheets\\chaos_redux_events_catalog.xlsx",
  "exports": [
    {
      "sheet": "Events",
      "path": "C:\\Users\\klimp\\OneDrive\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\chaos_redux\\docs\\spreadsheets\\chaos_redux_events_catalog.csv",
      "rows": 166,
      "columns": 14,
      "sha256": "1524940040a38b32176bebf797d2686c9e2ea6b49b7f2693ae7a3bbd177f3691"
    },
    {
      "sheet": "Clusters",
      "path": "C:\\Users\\klimp\\OneDrive\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\chaos_redux\\docs\\spreadsheets\\chaos_redux_clusters_catalog.csv",
      "rows": 20,
      "columns": 7,
      "sha256": "24a914fb257c99c8fc221c88828a229190de2555629dc751df05df1383be5e1e"
    },
    {
      "sheet": "Scenarios",
      "path": "C:\\Users\\klimp\\OneDrive\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\chaos_redux\\docs\\spreadsheets\\chaos_redux_scenarios_catalog.csv",
      "rows": 16,
      "columns": 6,
      "sha256": "8b944de19817b3887eac22e3d12437e62990273c8b0db1c6f27928f349d4b2e7"
    }
  ]
}
```

The three CSVs were refreshed by the exporter and were not edited directly.

On 2026-09-05, the current worktree workbook was reopened read-only with `openpyxl`. It still contains the five expected sheets, Event 32 at `Events!A33` with title `Missiles`, the blank world-end and cluster fields, and `SCN-015` at `Scenarios!A15`. The current workbook SHA-256 is `f70259334ec5e8ccefb40bfd71d21a4faa381924a25b106b60fb4fd8b68f7e05`; the three export hashes above remain unchanged.

## Blockers and needs_user_review

The shared event-log name mapping at `localisation/english/chaosx_event_names_l_english.yml` now defines `chaosx.event_name.32: "Missiles"`, matching the Event 32 root title, overview, and catalog.

Some older Event 32 specification prose also differs from the current localized detail, evolution, and SCN-015 descriptions. The workbook follows the current localization file as the player-facing source of truth; review the spec/localization divergence if the older prose is still intended.

No current runtime cluster registry entry for Event 32 was found in the cluster/event-log helper files reviewed after export; the blank catalog cluster field is therefore aligned with the current source state.

`Needs Testing` is intentional because the implementation wording is present but no HOI4 launch or live validation was performed in this spreadsheet-only task, and no explicit approval was supplied to mark the row `Playable`.

The workbook’s pre-existing `Events` table metadata still advertises 14 table columns including `Member Severity` while the visible Events sheet has 13 columns; it was preserved to avoid unrelated workbook-structure changes.

During the first attempted save, openpyxl stopped while rewriting the Scenario conditional-formatting collection and left a partial XLSX package. The target was recovered before the final update, reopened successfully, and passed the validations above.
