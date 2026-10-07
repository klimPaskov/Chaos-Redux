# Event 028 catalog changes pending

## Current text alignment, 2026-10-07

Disposition: implemented for `Events!C29`, `D29` and `E29`, with the exported Event 028 row matching the final localisation.
The [catalog handoff](subagent_handoffs/catalog_alignment_20261007.md) records exact before/after text, preserved cell styles, formula absence, full exporter parity and the original shared-workbook changes preserved by the worker.
Type and Status were not changed by this text-only tranche, and `Needs Testing` is not a full-feature or native acceptance claim.
The October 4 queued table below is retained as its accepted historical instruction and is superseded only for these three text updates.
The parent isolates those three cells and their generated export row from later unrelated shared-workbook edits for its scoped commit.

The event catalog workbook is edited only by its owner, and the CSV files are export-only.
These are the Event 028 row changes the catalog owner should apply to `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, then export with `python .tools/export_event_catalog_csv.py`.

## 2026-10-04: row 28 (sheet row 29)

Disposition: `accepted and queued` for the catalog owner.
Acceptance basis: the user granted the implementing agent full design authority for Event 028; the strings below are the committed in-game localisation.
This closes completion-audit finding F17 once applied: cell C29 still carries the older implementation-style description.

| Column | Cell | New value |
| --- | --- | --- |
| Details | C29 | Astronomers identify three possible impact sites and one near-miss course. A strike destroys its centre, damages three surrounding land rings, spreads atmospheric dust, and opens national recovery work. Global Fragmentation adds further impact sites, while Extraordinary Minerals makes control of those sites strategically valuable. The near miss causes no physical damage. |
| Evo I | D29 | Global Fragmentation — Chaos Tier, 600 Chaos, Stage 1: The altered trajectory breaks the asteroid apart. The main body still strikes the chosen state, while 3 to 6 smaller fragments, rising with Chaos, strike populated states elsewhere in the world. Each fragment leaves its own crater and two rings of damage, and adds to the atmospheric dust. |
| Evo II | E29 | Extraordinary Minerals — Totalen Chaos, 800 Chaos, Stage 1, requires Global Fragmentation: The impact sites hold extraordinary material. The country controlling the main crater gains 100% land-division armour, and each controlled fragment site adds 20%. Craters become military objectives with their own security, survey, fortification, and rival actions. |
| Type | J29 | Major (unchanged) |
| Status | M29 | Needs Testing (unchanged; the event is enabled in the default queue and awaits live-game verification) |

The Details value is the exact text of `asteroid_incoming.event_details.description` in `localisation/english/028_asteroid_impact_l_english.yml`.
The evolution values keep the catalog's "name — tier, threshold, stage:" prefix and then the in-game evolution body (`asteroid_incoming.evolution.fragmentation.body` and `asteroid_incoming.evolution.minerals.body`) with its colour codes removed and its constants rendered (3 and 6 fragment sites, 100% and 20% armour).

Exact localisation strings, for byte-for-byte comparison:

```text
asteroid_incoming.event_details.description: "Astronomers identify three possible impact sites and one near-miss course. A strike destroys its centre, damages three surrounding land rings, spreads atmospheric dust, and opens national recovery work. Global Fragmentation adds further impact sites, while Extraordinary Minerals makes control of those sites strategically valuable. The near miss causes no physical damage."
asteroid_incoming.evolution.fragmentation.title: "Global Fragmentation"
asteroid_incoming.evolution.fragmentation.body: "The altered trajectory breaks the asteroid apart. The main body still strikes the chosen state, while §Y[?constant:asteroid_incoming_runtime.fragment_site_goal_at_600|0]§! to §Y[?constant:asteroid_incoming_runtime.fragment_site_goal_at_900|0]§! smaller fragments, rising with Chaos, strike populated states elsewhere in the world. Each fragment leaves its own crater and two rings of damage, and adds to the atmospheric dust."
asteroid_incoming.evolution.fragmentation.summary: "The asteroid broke apart, and its fragments struck around the world."
asteroid_incoming.evolution.minerals.title: "Extraordinary Minerals"
asteroid_incoming.evolution.minerals.body: "The impact sites hold extraordinary material. The country controlling the main crater gains §G[?constant:asteroid_incoming_mineral.main_crater_armour_factor|%0]§! land-division armour, and each controlled fragment site adds §G[?constant:asteroid_incoming_mineral.fragment_site_armour_factor|%0]§!. Craters become military objectives with their own security, survey, fortification, and rival actions."
asteroid_incoming.evolution.minerals.summary: "The craters hold extraordinary material worth fighting over."
```
