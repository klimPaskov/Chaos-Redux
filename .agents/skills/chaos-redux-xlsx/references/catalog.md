# Event catalog contract

Read `docs/spreadsheets/README.md` as the current authority before editing.
The schema below describes the established workbook, not permission to restructure it.
Discover the current headers and table ranges on each run and report discrepancies before guessing.

## Sheets and identifiers

| Sheet | Established headers | Identity and purpose |
| --- | --- | --- |
| Events | ID, Event Name, Details, Evo I, Evo II, Evo III, Evo IV, Evo V, World-End Scenario, Type, Chaos level, Cluster ID, Status | One row per event ID, including unavailable catalog entries. |
| Clusters | Cluster ID, Cluster Name, Details, Members (ID), Member Severities, Type, Chaos level, Status | One row per cluster with aligned aggregate member and severity lists. |
| Cluster Memberships | Cluster ID, Cluster Name, Slot, Event ID, Event Name, Severity, Membership Notes | Exact membership slots, including repeated event IDs. |
| Scenarios | Scenario ID, Scenario Name, Details, Type Options, Intensity Scaling, Status | Manual scenario records with their own identifiers. |
| Legend | Category, Value, Color Meaning, Applies To | Allowed labels and their presentation. Its header may be below a title row. |

The data sheets use Excel tables, so inspect both table ranges and worksheet dimensions.
Do not truncate legitimate unavailable rows or infer the intended table extent from only populated descriptions.
Worksheet filters can be carried by the table rather than `ws.auto_filter`.

## Player-facing text

Use the exact current localisation wording for Event Details, evolution details, and cluster details supplied by the parent or located in its named sources.
Follow the prose rules in `chaos-redux-events` when writing new wording, without loading unrelated implementation instructions for a transcription task.
Descriptions explain the premise and situation, preserve paragraphs, and do not become effect lists or implementation notes.
Keep titles and descriptions distinct.

- `Details` matches the Event Details description.
- `Evo I` through `Evo V` contain complete descriptions of actual implemented evolutions, not selector titles or ordinary baseline stages.
- More than five distinct evolution descriptions remain complete in `Evo V`, with titles as separators for overflow entries, until an explicit schema migration is approved.
- `World-End Scenario` retains every public terminal branch owned by the event, each with its full description and a title separator where several branches share the cell.
  A cross-event terminal link must retain the meaning of the source wording.
- `Scenarios` describes the separate manual scenario setup.
  Do not conflate it with an event's terminal branch cell.

Do not strip all formatting tokens from localisation blindly.
Resolve known display markup while preserving text, paragraphs, and dynamic meaning, and report a missing dynamic-text input instead of inventing its value.

## Status and Legend

Valid statuses are exactly `Playable`, `Partially Available`, `To Be Reworked`, `Unavailable`, and `Needs Testing`.
`Playable` requires explicit approval, with its basis recorded in the handoff.
Implementation or a passing source check alone is not that approval.
Use the README's classification rules:

- Events 1 through 20 awaiting playable approval use `Needs Testing`.
- Events above 20 with an actual `chaosx.nr<ID>.1` root definition use `To Be Reworked` until their replacement implementation is approved.
- IDs without that root definition use `Unavailable`.
- `Partially Available` represents a usable surface with materially blocked, incomplete, or unavailable content, and is not a playable approval.

Use accepted parent facts about root definitions rather than changing status from a guessed category membership.
Do not automatically reclassify unrelated rows during a bounded prose update.
An explicit user-approved classification takes precedence over a default classification.
Catalog status does not alter runtime registration or enablement.

`Legend` defines Type, Status, Severity, evolution, and World-End appearance.
Read its actual cell fills as well as its color descriptions.
Keep dropdown labels/ranges, conditional-formatting rules, and static populated-cell fills synchronized with it when updating the relevant field.
Do not substitute financial-model colors or generic status palettes.

## Cluster alignment

`Events.Cluster ID` is a comma-separated list of every distinct cluster ID containing that event.
It has no membership-severity column.
The `Cluster Memberships` identity is the cluster plus slot, not Event ID alone.
An event can occur more than once in one cluster with different or repeated severity values.
Never deduplicate membership slots or severity entries during cleanup.

For each touched cluster:

1. Read its membership rows in slot order and verify slot identity and event names against the supplied sources.
2. Compare the ordered Event ID sequence to `Clusters.Members (ID)` and the corresponding severity sequence to `Clusters.Member Severities`.
   Their lengths, order, and duplicates must match.
3. Compare the distinct cluster memberships of each touched event with `Events.Cluster ID`.
4. Keep severity labels aligned with `Legend`, using the exact established vocabulary.

Name-only changes may require corresponding membership display-name changes.
Membership changes can affect all three representations and require their joint validation.

## Export and external copies

`.tools/export_event_catalog_csv.py` exports `Events`, `Clusters`, and `Scenarios` only.
Its established widths are 13, 8, and 6 columns respectively.
It keeps headers, trims empty trailing records, and writes UTF-8 BOM CSV with multiline fields quoted by the CSV writer.
Use a CSV parser for comparison rather than splitting physical lines.
`Cluster Memberships` and `Legend` remain workbook-only.
A schema change must account for the exporter as well as workbook consumers and requires explicit scope.

The exporter reads cached formula results and checks for missing caches, but cannot establish freshness or detect every formula error.
Inspect relevant cached values separately if formulas are introduced.
Run it after the accepted authoritative save, even for a formatting-only update.
For disposable validation, its `--workbook` and `--output-dir` options allow isolated copies and outputs.

A public Google Sheet or another published copy is a separate surface.
It must not replace the authoritative local workbook with stale data or be synchronized/published without authorization.
Existing local task authorization does not imply publication authorization.
