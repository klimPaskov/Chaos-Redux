# Event 021 cluster alignment handoff

Date: 2026-09-01.

## Scope

The event catalog workbook was corrected so Event 021 is no longer listed as a Domestic Unrest member, matching the current Event 021 design and gameplay cluster constants.

## Workbook changes

- `Clusters` Excel row 17, CSV row 16, `Cluster ID = 16`, `Domestic Unrest`: `Members (ID)` changed from `1, 6, 21, 31, 63` to `1, 6, 31, 63`.
- `Clusters` Excel row 17, CSV row 16, `Domestic Unrest`: `Member Severities` changed from `Medium, High, Low, Medium, Medium` to `Medium, High, Medium, Medium`.
- `Events` row 22, `ID = 21`: `Cluster ID` changed from `1, 16` to `1`, while the Event 021 player-facing text, type, chaos level, and status were retained.
- `Cluster Memberships` row 75, the Domestic Unrest slot for Event 021 at Low severity, was removed.
- The `Cluster_Memberships` table range changed from `A1:G84` to `A1:G83` to remove that exact membership slot without leaving a blank table row.
- The stale Event 021 Wars membership note in `Cluster Memberships!G8` was cleared; the Wars membership itself remains Event 021 at Medium severity.
- Event 021 remains in the Wars cluster at its aligned seventh member position with `Medium` severity.
- `Scenarios` row 15, `SCN-018`, `The Fracture Cascade`, was retained unchanged.

## Verification evidence

- The workbook reopened successfully with the original five sheets and zero formulas.
- The retained table ranges are `Events!A1:M1014`, `Clusters!A1:H20`, and `Scenarios!A1:F15`; the intentionally reduced membership range is `Cluster Memberships!A1:G83`.
- Domestic Unrest now exports `Members (ID) = 1, 6, 31, 63` and `Member Severities = Medium, High, Medium, Medium`; Event 021 is absent.
- Wars still exports Event 021 at one-based position 7 with `Medium` severity.
- The Event 021 export row remains present with `Cluster ID = 1`.
- `SCN-018` remains present as `The Fracture Cascade`.

## Export evidence

The required exporter completed successfully as `python -B .tools/export_event_catalog_csv.py` after the workbook save.

- `chaos_redux_events_catalog.csv`: 166 rows including the header, 13 columns, SHA256 `7290945be502cd3df6b2c92e11cc53826d232a6c416558e13abf2d6f43042a65`.
- `chaos_redux_clusters_catalog.csv`: 20 rows including the header, 8 columns, SHA256 `46754e9e90f1554c8adfae7b3853664042c06bde47233b9bd6b4e0d6d3e7daea`.
- `chaos_redux_scenarios_catalog.csv`: 15 rows including the header, 6 columns, SHA256 `3936d057dacc7efdeab94e29790b88a446890030bf4b5d5c244bbf7299873145`.
- Final workbook SHA256: `ac7ffbf32b5a143b54486e7539757098d5c7990c4b53e9574552ffe45700f287`.

No gameplay, localisation, or unrelated files were edited, and no commit was made.
