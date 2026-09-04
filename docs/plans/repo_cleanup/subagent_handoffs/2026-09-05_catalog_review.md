# Event catalog read-only review

Review date: 2026-09-05.

Scope: read-only review of docs/spreadsheets/chaos_redux_events_catalog.xlsx, docs/spreadsheets/README.md, .agents/skills/xlsx/SKILL.md, and .tools/export_event_catalog_csv.py.

The workbook was fully read by populated cell across Events, Clusters, Cluster Memberships, Scenarios, and Legend.

No workbook or CSV was edited.

The CSV exporter was not run because this task explicitly forbids workbook saves and exports.

The repository AGENTS.md contains a blanket requirement to read Paradox wiki and vanilla documentation before changes, while this bounded spreadsheet review explicitly forbids those broad sources and limits source reading to the assigned spreadsheet files and skill.

No gameplay, localization, runtime, or engine behavior claim was made.

## Workbook hash

The SHA256 before review was b6de395b4a77fb0f7cb9eaee274195a182b67626cbf5fcc4481ebe2db991acaa.

The workbook remained unchanged during review.

The SHA256 after review is b6de395b4a77fb0f7cb9eaee274195a182b67626cbf5fcc4481ebe2db991acaa.

## Sheet coverage

| Sheet | Populated coverage | Nonempty rows | Nonempty cells | Table ref | Workbook visible columns | Table metadata columns |
| --- | --- | ---: | ---: | --- | ---: | ---: |
| Events | A1:M166 | 166 | 1052 | A1:M1014 | 13 | 14 |
| Clusters | A1:H20 | 20 | 158 | A1:H20 | 8 | 8 |
| Cluster Memberships | A1:G76 with blank rows 61 and 73 | 74 | 479 | A1:G76 | 7 | 7 |
| Scenarios | A1:F16 | 16 | 96 | A1:F16 | 6 | 6 |
| Legend | A1:D24 with blank rows 7, 13, and 18 | 21 | 81 | none | 4 | none |

The Events table named Events has table id 1 and ref A1:M1014.

The Event_Clusters table has table id 2 and ref A1:H20.

The Cluster_Memberships table has table id 3 and ref A1:G76.

The Manual_Scenarios table has table id 4 and ref A1:F16.

The workbook has no defined names and contains no formula cells.

## README, schema, and exporter mismatches

The README says that Events has no member-severity column, but the Events table metadata declares a fourth field after Cluster ID named Member Severity.

The visible Events header is Events!A1:M1 with Status in M1 and no Member Severity header.

The Events table ref is A1:M1014, which is thirteen worksheet columns, while its table metadata contains fourteen columns.

The exporter sets SHEET_WIDTHS["Events"] to 14, so it reads one column beyond the visible Events sheet schema.

The Clusters sheet has eight visible columns through Status in H and table ref A1:H20, while the exporter sets SHEET_WIDTHS["Clusters"] to 7 and therefore omits the Status column from its declared export width.

The Scenarios sheet and exporter both use six columns, so no width mismatch was found there.

The README and Legend define the valid status values as Unavailable, Needs Testing, Playable, To Be Reworked, and Partially Available.

Events!M2:M1014 uses a stale validation list of Fully Functional, New, In progress, To Be Reworked, Buggy, and Needs Testing.

Scenarios!F2:F16 uses the same stale validation list and omits the README and Legend status values Unavailable, Playable, and Partially Available.

Events!M2:M1014 and Scenarios!F2:F16 also have conditional formatting rules for the stale value Fully Functional.

Cluster Memberships!F2:F83 has validation and conditional formatting coverage beyond the table and populated data ending at row 76.

The README requires complete player-facing descriptions in Evo I through Evo V, with titles kept separate from descriptions.

Event ID 39 at Events!A40:B40 is Murder Mystery, but Events!D40:H40 contain only the selector titles The Murder Cult, Cells Beyond the Border, The Hidden Hand Takes Territory, The Veiled Compact, and World Without Leaders.

The title-only evolution cells Events!D40:H40 are needs_user_review against the README description contract.

## Event ID and membership contradictions

The Events ID sequence contains 165 unique integer IDs and skips ID 163.

The sequence around the gap is Events!A163 = 162 and Events!A164 = 164.

The following Events Cluster ID declarations disagree with Cluster Memberships and the aligned Clusters aggregate list.

| Event ID | Events declaration | Membership evidence |
| ---: | --- | --- |
| 16 | Events!A17 = 16 and Events!L17 = "9" | No Cluster Memberships row with Event ID 16 and no ID 16 in Clusters!D10 |
| 60 | Events!A61 = 60 and Events!L61 = "9" | No Cluster Memberships row with Event ID 60 and no ID 60 in Clusters!D10 |
| 65 | Events!A66 = 65 and Events!L66 is blank | Cluster Memberships!A46:D46 has cluster 9 and Event ID 65, and Clusters!D10 includes 65 |
| 67 | Events!A68 = 67 and Events!L68 is blank | Cluster Memberships!A47:D47 has cluster 9 and Event ID 67, and Clusters!D10 includes 67 |
| 83 | Events!A84 = 83 and Events!L84 is blank | Cluster Memberships!A48:D48 has cluster 9 and Event ID 83, and Clusters!D10 includes 83 |
| 85 | Events!A86 = 85 and Events!L86 is blank | Cluster Memberships!A49:D49 has cluster 9 and Event ID 85, and Clusters!D10 includes 85 |
| 89 | Events!A90 = 89 and Events!L90 is blank | Cluster Memberships!A50:D50 has cluster 9 and Event ID 89, and Clusters!D10 includes 89 |

The following event names differ between Events and Cluster Memberships for the same Event ID.

| Event ID | Events cell and value | Membership cell and value |
| ---: | --- | --- |
| 20 | Events!B21 = "The Black Plague" | Cluster Memberships!E56 = "Black Plague" |
| 22 | Events!B23 = "Spain Antisemitism" | Cluster Memberships!E71 = "Concentration Camps" |
| 36 | Events!B37 = "Alien Spacecraft" | Cluster Memberships!E18 = "Chemical and Biological Weapons Convention" |
| 41 | Events!B42 = "Disease in divisions" | Cluster Memberships!E57 = "Disease in Divisions" |
| 42 | Events!B43 = "Equipment from heavens" | Cluster Memberships!E63 and E74 = "Equipment from Heavens" |
| 43 | Events!B44 = "Massive flood" | Cluster Memberships!E70 = "Monsters from the Deep" |
| 46 | Events!B47 = "Seismic Archive" | Cluster Memberships!E58 = "The Great Shuffle" |
| 54 | Events!B55 = "Gift from scientists" | Cluster Memberships!E45 = "Random Tech" |
| 57 | Events!B58 = "The Radar" | Cluster Memberships!E40 = "The Black Market" |
| 58 | Events!B59 = "The Industrial Complex" | Cluster Memberships!E41 = "Random Buildings" |
| 59 | Events!B60 = "AI focus aggressive" | Cluster Memberships!E19 = "The Offensive" |
| 61 | Events!B62 = "Half mils into civs" | Cluster Memberships!E24 = "Return to Peacetime" |
| 63 | Events!B64 = "End Subject Status" | Cluster Memberships!E15 and E69 = "Subjects Break Free" |
| 64 | Events!B65 = "Border fortifications" | Cluster Memberships!E65 and E76 = "Border Fortifications" |
| 83 | Events!B84 = "Agency upgrade" | Cluster Memberships!E48 = "Agency Upgrade" |
| 85 | Events!B86 = "XP" | Cluster Memberships!E49 = "Experience" |
| 89 | Events!B90 = "Tech sharing" | Cluster Memberships!E50 = "Tech Sharing Group" |

The exact text mismatches above are needs_user_review because the assigned read-only scope did not authorize source or engine reconciliation.

Cluster Memberships slot values are not sequential in four clusters.

| Cluster | Evidence | Gap |
| ---: | --- | --- |
| 7 | Cluster Memberships!C36:C41 = 1, 3, 4, 5, 6, 7 | Missing logical slot 2 |
| 15 | Cluster Memberships!C59:C65 excluding blank row 61 = 1, 2, 4, 5, 6, 7 | Missing logical slot 3 and blank row 61 |
| 16 | Cluster Memberships!C66:C69 = 1, 2, 4, 5 | Missing logical slot 3 |
| 18 | Cluster Memberships!C71:C76 excluding blank row 73 = 1, 2, 4, 5, 6 | Missing logical slot 3 and blank row 73 |

The Clusters aggregate member and severity list counts match the nonblank membership records for these four clusters, but the slot numbering still needs owner review.

Cluster 19 is a structural exception with Clusters!A20:H20 populated for Random Stuff, blank D20 and E20, and no Cluster Memberships rows.

The Random Stuff details say it draws from the entire currently fireable event pool, so the memberless shape may be intentional, but acceptance is not established by the catalog.

## Status contract review

The README requires Events 1 through 20 to remain Needs Testing until explicit playable approval.

Events 1 through 20 currently satisfy that status rule.

The README requires Events above 20 with an actual chaosx.nr<ID>.1 root definition to use To Be Reworked until replacement approval.

The current workbook has Needs Testing at the following above-20 cells.

| Cell | Event ID |
| --- | ---: |
| Events!M22 | 21 |
| Events!M25 | 24 |
| Events!M27 | 26 |
| Events!M28 | 27 |
| Events!M29 | 28 |
| Events!M30 | 29 |
| Events!M33 | 32 |
| Events!M36 | 35 |
| Events!M40 | 39 |

These cells are needs_user_review against the README rule, not a confirmed status error, because root-definition verification was outside this bounded catalog review.

The README also requires IDs without an actual root definition to use Unavailable.

Root-definition reconciliation was not performed and no status was inferred from the catalog alone.

## Other incomplete catalog cells

Events!K47 for Event ID 46 Seismic Archive is blank while Events!J47 is Minor Repeatable and Events!M47 is To Be Reworked.

Events!K100 for Event ID 99 Dust and Sandstorm Front is blank while Events!J100 is Minor Fire-Once and Events!M100 is To Be Reworked.

Events!J101 and Events!K101 for Event ID 100 Inflation are blank while Events!M101 is To Be Reworked.

The three metadata gaps above are needs_user_review because the source implementation was not opened under this assignment.

## Proposed next workbook-owner action

Use the owning spreadsheet workflow to decide whether the Events table should remain a thirteen-column sheet or migrate to a fourteen-column schema, then align the exporter width and table metadata together.

Reconcile the Events Cluster ID cells against Cluster Memberships and Clusters for Event IDs 16, 60, 65, 67, 83, 85, and 89 after the event owner confirms the intended memberships.

Reconcile the differing event names listed above after checking the authoritative player-facing source wording.

Resolve or explicitly accept the slot gaps in clusters 7, 15, 16, and 18, and document the memberless Random Stuff cluster as an accepted dynamic exception if that is intended.

Replace stale Events and Scenarios status validation and conditional-format rules with the Legend status set only after the workbook owner approves the schema cleanup.

Review the title-only Murder Mystery evolution cells and the three missing metadata cells before any workbook save.

After any accepted workbook save, run python .tools/export_event_catalog_csv.py from the mod root and verify all three export snapshots.
