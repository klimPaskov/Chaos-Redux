# Event 006 catalog current alignment — 2026-08-25

## Result

This was a read-only workbook alignment pass. No workbook cell was stale, so `docs/spreadsheets/chaos_redux_events_catalog.xlsx` was not saved or structurally rewritten.

No gameplay, localisation, scripted-localisation, CSV, or other catalog source was edited.

## Verified workbook rows and current wording

- `Events!A7:N7` is Event ID `6`, `Independence Wave`; `Events!B7` exactly matches `chaosx.event_name.6` (`Independence Wave`).
- `Events!C7` exactly matches `chaosx.events_log.window.event_details.independence_wave`: `New governments have taken control of capitals, ministries, and borders across several regions. They must secure recognition, administration, defense, and settlements with former hosts and foreign patrons. Former hosts retain part of their territory. A surviving country that loses at least [?constant:independence_wave_join.reduction_percent|0]% of its former states and at least [?constant:independence_wave_join.minimum_states_lost|0] states may join the wave if every retained state belongs to one prepared homeland.\n\n[GetIndependenceWaveRivalBlocEventDetails]\n[GetIndependenceWaveRivalBlocEventDetailsMember]`.
- `Events!D7` exactly matches `The Manuals Cross the Border`: `Founding charters, civil-service manuals, recognition protocols, and trusted couriers now pass from one young state to the next. New governments enter the world with stronger institutions, earlier diplomatic contacts, and a network prepared to sponsor their survival.`
- `Events!E7` exactly matches `Old Nations Wake`: `Dormant national projects and half-remembered unions return to political life. Regional and signature independence movements can surface sooner, while the states already born from the wave gain the confidence and institutions needed to rediscover larger identities.`
- `Events!F7` exactly matches `Flags Rise Behind the Barracks`: `The next declarations arrive with officers, guarded depots, and plans for immediate defense. Breakaway governments gain stronger military budgets and better prepared forces, but every rifle issued sharpens instability, former-host hostility, and the fear of reconquest.`
- `Events!G7` exactly matches `The Sovereigns Take Their Seats`: `The informal network becomes a congress of delegates, observers, and rejected clients. Recognition missions, arbitration, rescue commitments, and a shared reserve draw the independent states toward collective leadership without deciding the charter they must ultimately choose.`
- `Events!H7` exactly matches `No Border Is Final`: `World collapse strips old borders of their final authority. New sovereignty projects enter the struggle for independence, while existing breakaways gain the freedom and pressure to pursue dangerous routes.`
- `Events!I7` remains empty because Event 006 has no terminal world-end scenario catalog field.
- `Clusters!A3:G3` is Cluster ID `2`, `Liberations`, with exact current name and detail wording: `Liberation shocks create new countries, break old chains of command, and turn subject or republic disputes into broader independence crises.` Members remain `5, 6`.
- `Scenarios!A8:F8` is `SCN-008`, `Every Banner Rises`; its exact current scenario name, Sovereign Scatter detail, eight type labels, and Low/Medium/High/Maximum intensity text match `006_independence_wave_scenario_l_english.yml`.

## Current status boundary

`Events!N7` remains `Needs Testing`, and the current authority continues to treat Event 006 as partially available under the 32 attested-package boundary.

`Clusters!G3` remains `Partially Available` for the mixed Liberations cluster.

`Scenarios!F8` remains `Needs Testing`; the current authority still treats SCN-008 as unavailable for completion/runtime claims. The workbook has one status field and does not represent a separate availability column, so no guessed status replacement was made.

The automatic ladder remains the exact `3/4/5/7/10` sequence with World Collapse also at `10`; it is not inserted into `Events!C7` because that field mirrors the current in-game Event Details localisation. No pre-event crisis surface or hidden package/formable IDs are present in the verified Event 006 catalog fields.

## Validation and exports

- Workbook sheets remain `Events`, `Clusters`, `Scenarios`, and `Legend`; the existing tables and data-validation rules remain present, with zero formulas and zero Excel error cells.
- Workbook-to-localisation checks passed for Event 006 name/details, all five evolution bodies, Liberations name/details, and SCN-008 scenario fields.
- Ran `python .tools/export_event_catalog_csv.py` from the mod root for export validation; it completed with `status: success`.
- Export snapshots remained row-for-row equal to the workbook for the verified Event 006, Liberations, and SCN-008 rows. Current SHA-256 values are `8d7b5506a219a92c6c14fa54811eba533f7a1a12765383203b62f4fe206d7c16` for `chaos_redux_events_catalog.csv`, `647c9206de61a70d7a0d7adf0740dc97c81c8e63d01fefac6549b430b666425b` for `chaos_redux_clusters_catalog.csv`, and `52a80f59912841d0b046f889a40bdec66b452d5cc92c3f486245de56f08559cd` for `chaos_redux_scenarios_catalog.csv`.

## Changed cells and remaining gaps

Changed workbook sheets, rows, columns, and Event IDs: none.

Changed export rows: none; the exporter only revalidated the current snapshots in this read-only pass.

Blocked or `needs_user_review` cells introduced: none.

Remaining catalog gap: SCN-008 remains a `Needs Testing` workbook row under an unavailable runtime/completion authority, while the workbook schema has no separate availability field.
