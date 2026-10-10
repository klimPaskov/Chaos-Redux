# Event 029 catalog and Event Details alignment

The authoritative catalog is `docs/spreadsheets/chaos_redux_events_catalog.xlsx`; the CSV files in `docs/spreadsheets/` are exports refreshed only by `python .tools/export_event_catalog_csv.py` and are never edited by hand.

## Current row (verified 2026-10-10 against the exported CSV)

| Field | Value |
| --- | --- |
| ID | `29` |
| Event Name | Riches Found |
| Type | Minor Repeatable |
| Chaos level | 1 |
| Cluster ID | Blank |
| Evo IV, Evo V, World-End Scenario | Blank |
| Status | Needs Testing |

Details and Evo I to Evo III match the in-game `riches_found.event_details.description` and `riches_found.evolution.stage_1.body` to `stage_3.body` exactly.

The blank cluster follows the user's 2026-10-07 instruction applied in [the catalog correction handoff](../../plans/029_riches_found_plans/subagent_handoffs/catalog_alignment_2026_10_07.md); it supersedes agent decision D2 and the request in `catalog_changes_pending.md`, whose N/A sentence is no longer in the row.

## Status transition

Needs Testing stays until the user's live testing and the acceptance criteria are complete.

The row moves to the workbook's playable status only then, through `chaosx_spreadsheet_doc_worker` and the exporter.

## Event Details premise direction

Event Details explains the public premise without exact reward values beyond the defining 1,000 political power, hidden formulas, future supernatural outcomes, or implementation structure.

It communicates that one country finds exceptional wealth in one state, a rush of labour, capital, criminals, guards, officials, and foreign interests follows, the mine stays tied to the state and enriches whoever controls it, and development, revenue, security, concessions, and extraction policy decide what it becomes.

It does not name Gold Disease, demons, bargains, late outcomes, thresholds, Event 018 separation rules, or aggregate formulas, and it does not read as a reward list or a warning.

## Evolution fields

Only three evolution fields are populated: The Resource Curse (600+), Gold Disease (800+), and Demons Beneath the Mine (1,000+).

Each describes the new public situation and the core choices without exact values, without calling Gold Disease a pathogen, and without naming The Gilded Sovereignty, The Bottomless Account's terms, or any existing Chaos Redux underground actor.

The Gilded Sovereignty and The Bottomless Account are late outcomes inside existing tracks and never get evolution fields or log rows.

## Event Details evolution catalog and history

The Event Details evolution catalog shows three independently toggled entries, each with the event link, evolution type, stage, tier, premise, and enabled state, and never fake dates, sequence numbers, or actors before logging.

A normal firing creates one history row with the recipient as actor; ordinary phases, decisions, missions, contracts, raids, and closures never create evolution rows.

An evolution row records the controller at the time it entered, and that actor stays historical after a transfer.

## Event list availability

The Events tab shows a live weight while at least one valid country and state pair exists and `N/A` otherwise (no eligible ordinary country, no eligible state, every suitable state already a mine or another persistent site, or only special and nonhuman actors left).

A shortage of ideal states never causes `N/A` while a lower-weight valid state exists.

## Event 018 separation in catalog text

Event 029 wording never reuses Event 018's language about deposits beneath deposits, caves, fossils, underground attackers, Oth-Kesh, or The World Opens Below.

A player reading both rows should see two different campaign systems: resource deposits and an underground breach for Event 018, wealth governance, ownership, corruption, obsession, and a fictional bargain for Event 029.

## Workbook update checklist

When player-facing wording changes:

1. Read the workbook row and the current localisation.
2. Update Details and Evo I to Evo III to match the in-game text exactly.
3. Keep Type, Cluster ID, Evo IV, Evo V, and World-End Scenario as above.
4. Set Status from verified implementation and testing state only.
5. Preserve workbook structure, validation, and formatting, then run the exporter from the mod root.
6. Report any discrepancy instead of editing a CSV.
