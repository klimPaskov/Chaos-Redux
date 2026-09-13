# Event 066 Catalog Crosswalk

## Source snapshot used

The planning pass read the supplied export-only catalogs in full:

- `chaos_redux_events_catalog(4).csv`, 165 event rows
- `chaos_redux_clusters_catalog(4).csv`, 13 cluster rows
- `chaos_redux_scenarios_catalog(4).csv`, 13 scenario rows

The authoritative XLSX workbook was not supplied.
No CSV file was edited.

## Current Event 66 export row

| Field | Supplied value |
| --- | --- |
| ID | 66 |
| Event Name | CIC |
| Details | International market funding expands for a random major country. |
| Evolution I | blank |
| Evolution II | blank |
| Evolution III | blank |
| Type | Minor Repeatable |
| Chaos level | 1 |
| Cluster ID | blank |
| Member Severity | blank |
| Status | To Be Reworked |

This row describes an earlier and much narrower concept.
The accepted Event 66 brief replaces it.

## Required Event 66 workbook alignment

| Field | Required direction |
| --- | --- |
| ID | Keep `66` |
| Event Name | `Abundance` |
| Details | Match the final Event Details wording about four country-specific dynamic choices and one selected abundance result |
| Evolution I | `Strange Abundance` with final in-game detail wording |
| Evolution II | `Abundance Comes in Pairs` with final in-game detail wording |
| Evolution III | `Everything in Excess` with final in-game detail wording |
| Evolution IV | blank |
| Evolution V | blank |
| Type | `Minor Repeatable` |
| Chaos level | `1` |
| Cluster ID | Final verified ID for `Sudden Abundance` |
| Member Severity | Preserve all three roles, `Low`, `Medium`, and `High` |
| Status | Keep `To Be Reworked` until implementation evidence supports a status change |

The Member Severity field must not collapse three accepted logical slots into one label.
If the workbook uses one event row per event, the cell should carry all three values in the established multi-value format and the Clusters sheet should repeat Event 66 three times in ordered membership.

## Sudden Abundance cluster gap

The supplied cluster export has numeric IDs `1` through `8`, then `10`.
There is no Sudden Abundance row.
Numeric ID `9` is therefore the provisional planning choice, but it is not locked until the authoritative workbook and runtime constants are inspected.

The cluster row needs:

| Field | Required direction |
| --- | --- |
| Cluster ID | Provisional `9`, verify before implementation |
| Cluster Name | `Sudden Abundance` |
| Details | Explain that abundance incidents create excess across military, economic, political, resource, construction, and mechanic values, with member severity controlling breadth or persistence |
| Members | Include Event 66 three times in Low, Medium, High order, plus every other accepted member from the shared cluster plan |
| Type | `Minor Repeatable` unless the shared cluster spec establishes another accepted type |
| Chaos level | `1` unless the shared cluster spec establishes a higher unlock |
| Status | Follow actual implementation coverage |

Event 64 Border Fortifications has already been accepted in project context as a Medium Sudden Abundance member.
The cluster workbook pass must reconcile that row and any other approved members before export.

## Overlap audit

The event catalog contains several fixed abundance, resource, capacity, or value ideas.
Event 66 should coexist with them.

| ID | Event | Potential overlap | Distinct role retained |
| --- | --- | --- | --- |
| 18 | Resources Found | resource deposits | persistent discovery chain and state development |
| 29 | Riches Found | wealth and Political Power | country-focused riches crisis with follow-up systems |
| 34 | Industrial Boom | industry | boom, overheating, and depression lifecycle |
| 42 | Equipment from heavens | stockpiles | fixed equipment abundance event |
| 54 | Gift from scientists | technology | direct random technology grant |
| 55 | The Great Infrastructure Project | construction | map-based infrastructure program |
| 56 | The Navy | naval capacity | dedicated naval expansion |
| 57 | The Radar | radar construction | dedicated radar expansion |
| 58 | The Industrial Complex | factories | dedicated factory expansion |
| 64 | Border fortifications | forts | dedicated global defensive construction and cluster member |
| 82 | Law upgrade | laws | direct law progression |
| 83 | Agency upgrade | intelligence agency | dedicated agency progression |
| 84 | PP | Political Power | one fixed scalar grant |
| 85 | XP | military experience | fixed experience grant |
| 89 | Tech sharing | research cooperation | diplomatic research network |
| 98 | New Ore | state resources | dedicated new-deposit event |
| 103 | Conscription | manpower law | conscription movement |
| 104 | Stability or War support | bounded gauges | fixed tradeoff between two values |
| 114 | Fuel crisis | fuel | worldwide fuel removal and crisis identity |
| 132 | Investment | investment value | dedicated investment concept |
| 135 | Equipment choice | stockpile choice | dedicated equipment selection concept |
| 137 | Research Investment | research value | dedicated research investment concept |

Event 66 remains distinct because it affects every valid country, builds four country-local choices from a live provider registry, permits harmful values, combines unrelated values at later evolutions, and discards the three unchosen cards.

## Status transition

The workbook status should advance only after the matching evidence exists.
A reasonable sequence is:

1. `To Be Reworked` while the accepted spec is not implemented.
2. `Needs Testing` after complete implementation, assets, localisation, AI, logs, achievements, cluster wiring, and docs exist.
3. `Implemented` only after the project's required validation and catalog policy support that label.

## Export rule

After the authoritative workbook is updated, run the repository exporter so the Events, Clusters, and Scenarios CSV snapshots are regenerated together.
Do not patch the supplied CSV snapshots directly.
