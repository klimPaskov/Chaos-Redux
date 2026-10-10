# Event 027 catalog changes pending

Disposition: the `M28` Status change to `Needs Testing` is `implemented` in the workbook on 2026-10-10 with regenerated CSV exports. The Cluster Memberships notes stay `accepted and queued`.

Basis: the Event 027 rework is implemented in commits `b55edd969`, `317e43684`, and `2a8be6e32` and awaits live acceptance (see `agent_decisions_2026-10-04.md`).

## Changes

| Sheet | Cell | Current value | New value |
| --- | --- | --- | --- |
| Events | M28 (Status, ID 27 Doctrine Research) | `To Be Reworked` | `Needs Testing` |
| Cluster Memberships | G45 (cluster 9, slot 2, event 54) | empty | `Catalogued member; it joins the runtime cluster when its own rework is implemented.` |
| Cluster Memberships | G46 (cluster 9, slot 3, event 65) | empty | `Catalogued member; it joins the runtime cluster when its own rework is implemented.` |
| Cluster Memberships | G47 (cluster 9, slot 4, event 67) | empty | `Catalogued member; it joins the runtime cluster when its own rework is implemented.` |
| Cluster Memberships | G48 (cluster 9, slot 5, event 83) | empty | `Catalogued member; it joins the runtime cluster when its own rework is implemented.` |
| Cluster Memberships | G49 (cluster 9, slot 6, event 85) | empty | `Catalogued member; it joins the runtime cluster when its own rework is implemented.` |
| Cluster Memberships | G50 (cluster 9, slot 7, event 89) | empty | `Catalogued member; it joins the runtime cluster when its own rework is implemented.` |

## Values to keep

- Clusters H10 (National Breakthroughs status) stays `Partially Available`: only Event 027, runtime member row 9001, is implemented.
- Cluster Memberships G44 (Event 27) stays `Optional member of the National Breakthroughs cluster.`
- Events C28 to G28 already match the in-game Event Details and evolution localisation (`chaosx.events_log.window.event_details.doctrine_research` and `chaosx.events_log.window.evolution_details.doctrine_research.body.stage_1` to `stage_4`).

## Export

After applying the workbook changes, run `python .tools/export_event_catalog_csv.py` from the mod root to regenerate `chaos_redux_events_catalog.csv`, `chaos_redux_clusters_catalog.csv`, and `chaos_redux_scenarios_catalog.csv`.
