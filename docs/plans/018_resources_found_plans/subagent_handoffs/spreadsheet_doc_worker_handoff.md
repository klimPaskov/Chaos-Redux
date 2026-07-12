# Event 018 spreadsheet documentation handoff

## Disposition

Event 018 spreadsheet alignment is complete within the existing workbook schema. The `Events` record and its `Economy (pos)` cluster record now use the finalized player-facing localisation wherever the workbook has a corresponding field.

This worker edited only `docs/spreadsheets/chaos_redux_events_catalog.xlsx` and this handoff. It did not edit gameplay, localisation, assets, manifests, specifications, or other documentation. No commit was created.

The workbook was already modified in the working tree when this worker began. The only workbook values changed by this worker were `Events!D19` and `Events!E19`.

## Sources reviewed

The following sources were read before deriving workbook facts:

- the full `chaos-redux-events` skill
- the full `xlsx` skill
- repository `AGENTS.md`
- the complete 26-file Event 018 specification package under `docs/specs/018_resources_found_specs/`
- `docs/events/018_resources_found.md`
- `docs/events/018_resources_found_cave_country.md`
- finalized Event 018 event, system, decision, shared event-name, shared GUI, achievement, and music localisation
- Event 018 implementation handoffs, acceptance report, country audit, asset manifests, super-event text research, and super-event audio research
- the required offline Paradox wiki pages and relevant vanilla localisation documentation

The final workbook strings come directly from finalized localisation when a dedicated localisation key exists. Type, severity, repeatability, cluster membership, status, and the intentional four-evolution limit were cross-checked against the specification package and implementation handoffs.

## Canonical Events row

The complete Event 018 record is `Events!A19:M19`.

| Cell | Header | Final value | Primary source |
| --- | --- | --- | --- |
| `A19` | ID | `18` | Event identity and entry root `chaosx.nr18.1` |
| `B19` | Event Name | `Resources Found` | `chaosx.event_name.18` |
| `C19` | Details | `Surveyors in an owned state discover a major strategic resource deposit. Repeated discoveries can deepen the same field, turning local prospecting into a long-lived question of development, labor, trade, and control.` | `resources_found.event_details.description` |
| `D19` | Evo I | `Veins Without End: One field reveals several large deposits at once. Repeated finds of the same resource deepen its discovery ledger, while foreign buyers, claimants, and a negotiated demilitarized commission compete for access to the concentrated wealth.` | `resources_found.evolution.stage_1.title` and `resources_found.evolution.stage_1.body` |
| `E19` | Evo II | `The Workings Turn Sick: Sickness, corrosion, disappearances, and underground attacks spread through the lower workings. Investigation, containment, concealment, suspension, and permanent closure determine whether the field remains an economy or becomes a grave.` | `resources_found.evolution.stage_2.title` and `resources_found.evolution.stage_2.body` |
| `F19` | Evo III | `The Breach Takes Shape: A vast deposit of every standard resource draws the field far below safe workings. Public attacks, hunts, evacuation, partial closure, and a full sealing operation decide whether every registered discovery deposit is surrendered before the breach opens.` | `resources_found.evolution.stage_3.title` and `resources_found.evolution.stage_3.body` |
| `G19` | Evo IV | `The Oth-Kesh Emerge: The field becomes the origin chamber of the playable Oth-Kesh Host. Its armored broods draw strength from exploitation and captured resource anchors, attack every adjacent land neighbor, and prepare to carry the connected depths beyond their first continent.` | `resources_found.evolution.stage_4.title` and `resources_found.evolution.stage_4.body` |
| `H19` | Evo V | blank | Intentional. Event 018 has four distinct evolutions. |
| `I19` | World-End Scenario | `The World Opens Below: The first continent is no longer a contained theater. Stronger formations will emerge through resource-weighted footholds on distant continents at once.` | `DHO_the_world_opens_below` and `DHO_the_world_opens_below_desc` |
| `J19` | Type | `Minor Repeatable` | Event 018 catalog reconciliation and specification manifest |
| `K19` | Cluster ID | `7` | `Economy (pos)` cluster registration |
| `L19` | Member Severity | `Medium` | Event 018 catalog reconciliation and cluster specification |
| `M19` | Status | `Implemented` | Implemented Event 018 package and acceptance evidence |

## Canonical cluster row

The corresponding cluster record is `Clusters!A10:G10`.

| Cell | Header | Final value | Primary source |
| --- | --- | --- | --- |
| `A10` | Cluster ID | `7` | Event 018 catalog reconciliation |
| `B10` | Cluster Name | `Economy (pos)` | `chaosx.event_cluster.economy_positive.name` |
| `C10` | Details | `Economy (pos) delivers beneficial economic shocks with persistent development choices. Resources Found is its medium-severity repeatable member: one discovery can mature into trade, investment, foreign pressure, or a cleanly closed field.` | `chaosx.events_log.window.cluster_details.description.economy_positive` |
| `D10` | Members (ID) | `18` | Event 018 membership |
| `E10` | Type | `Minor Repeatable` | Event classification |
| `F10` | Chaos level | `1` | Event 018 catalog reconciliation |
| `G10` | Status | `Implemented` | Implemented cluster member |

## Workbook changes made by this worker

Only two cell values required correction. All other canonical Event 018 and cluster values were already aligned before this worker's write.

### `Events!D19`

Previous wording:

> Veins Without End: One field reveals several large deposits at once. Duplicate resource rolls remain valid and stack, while foreign buyers, claimants, and a negotiated demilitarized commission compete for access to the concentrated wealth.

Final wording:

> Veins Without End: One field reveals several large deposits at once. Repeated finds of the same resource deepen its discovery ledger, while foreign buyers, claimants, and a negotiated demilitarized commission compete for access to the concentrated wealth.

### `Events!E19`

Previous wording:

> The Workings Turn Sick: Sickness, corrosion, disappearances, and underground attacks accumulate through a gradual incident chain. Investigation, containment, concealment, suspension, and permanent closure determine whether the field remains an economy or becomes a grave.

Final wording:

> The Workings Turn Sick: Sickness, corrosion, disappearances, and underground attacks spread through the lower workings. Investigation, containment, concealment, suspension, and permanent closure determine whether the field remains an economy or becomes a grave.

## Verified facts without workbook columns

The existing workbook has no country tag, country package, leader, asset, audio, super-event quote, or super-event slot columns. The schema was not expanded and unrelated event rows were not disturbed. The following facts were still verified against their finalized implementation surfaces so that the absence of a workbook write was deliberate:

- country package: `DHO`, the Oth-Kesh Host, with the World Below identity and Vhorruk as leader
- super-event slots and audio IDs: `82/54`, `83/55`, and conditional `84/56`
- super-event titles: `THE OTH-KESH HOST RISES`, `THE DEEP WAR CROSSES THE SEAS`, and `THE LAST DEPTH IS SEALED`
- quote sources: Job 28:5, Aeschylus in *Prometheus Bound*, and Croesus in Herodotus
- audio selections: Mussorgsky's *Bydło*, Brahms's Symphony No. 1 first movement, and Chopin's Prelude in E minor, Op. 28 No. 4
- asset package: finalized Event 018 source, processed, DDS, sprite, and manifest surfaces are documented and wired in the implementation handoffs

These facts do not correspond to any field in the current `Events`, `Clusters`, `Scenarios`, `Info`, or `Legend` sheets. No placeholder or compressed substitute was placed in another column.

## Verification evidence

- Pre-write workbook SHA-256: `D88653845CFCCC29284DD802B13073AC6CC411C933AB8CB54C47AC370C54E73A`
- Post-write workbook SHA-256: `BECBF6834DC354BC9A4161D30A45641FF660B9278218DB30D30F1228BE4EF3D9`
- A guarded before-and-after comparison found exactly two changed cell values, `Events!D19` and `Events!E19`.
- Workbook sheet names, dimensions, merged ranges, and style IDs were preserved.
- The XLSX ZIP container passes integrity testing.
- The workbook opens through `openpyxl` with five expected sheets.
- The workbook contains zero formulas and zero stored Excel error values. Formula recalculation was therefore not applicable.
- LibreOffice exported the workbook to a 39-page PDF without an error.
- Rendered PDF pages were visually inspected for Event 018 identity, details, evolutions, world-end scenario, classification, severity, status, and cluster membership.
- The evolution render shows four distinct populated evolution cells and an intentionally blank Evo V cell.
- The classification render shows `Minor Repeatable`, cluster ID `7`, `Medium`, and `Implemented`.
- The cluster render shows `Economy (pos)`, member `18`, `Minor Repeatable`, chaos level `1`, and `Implemented`.

## Simplifications, omissions, and blockers

No simplification was made within the workbook's defined Event 018 surface. Evo V remains blank because the finalized design has four evolutions. Country package, asset, audio, and quote data were not omitted from an existing field because no such workbook fields exist.

There are no spreadsheet blockers. This handoff claims completion only for Event 018 workbook alignment, not for the broader Event 018 implementation goal.

## Skill usage

- Used `chaos-redux-events` to preserve Event 018 naming, detail, evolution, cluster, and player-facing wording contracts.
- Used `xlsx` for schema inspection, guarded cell editing, structural comparison, integrity checks, PDF rendering, and visual verification.
- No skill was created or modified.
