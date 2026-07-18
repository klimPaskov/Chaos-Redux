# IW-043 / IW-058 catalog alignment verification

Date: 2026-07-18
Owner: parent Event 006 implementation thread
Scope: bounded IW-043 `CHU` / IW-058 `ASY` closeout against the shared Event 006 Event Details, evolution, Liberations-cluster, SCN-008, and catalog surfaces.

## Verdict

**PASS for the bounded catalog-alignment surface.**

The player-facing workbook mirror fields already match their in-game localisation sources exactly. No workbook cell required a content change, so the workbook was not rewritten and the export-only CSV files were not regenerated. This is deliberate: the export tool is required after a successful workbook update, and there was no update to export.

## Exact comparisons

The editable source `docs/spreadsheets/chaos_redux_events_catalog.xlsx` was read directly and compared with the current localisation values:

- `Events!C7` exactly matches `chaosx.events_log.window.event_details.independence_wave`.
- `Events!D7:H7` exactly match the five `independence_wave.evolution.<stage>.title` plus body pairs, separated by two line breaks.
- `Scenarios!B9` exactly matches `chaosx.scenarios.independence_wave.name`.
- `Scenarios!C9` exactly matches the shared SCN-008 premise in `chaosx.scenarios.independence_wave.desc.sovereign_scatter`.
- `Scenarios!D9` exactly joins the eight registered SCN-008 type names in UI order.
- `Scenarios!E9` exactly joins the four registered intensity descriptions in UI order.
- `Clusters!B3:C3` exactly match `chaosx.event_cluster.liberations.name` and `chaosx.events_log.window.cluster_details.description.liberations`.

The Event 6 workbook row remains `In progress`, and SCN-008 remains `Needs Testing`. Those statuses correctly preserve the open parent-wide package, runtime-scenario, audio, animation, and completion-audit work.

## Package-detail disposition

The generic Event 6 Event Details and workbook mirror intentionally do not enumerate `IW-043`, `IW-058`, `FORM-12`, `FORM-13`, or `FORM-18`. The accepted catalog handoff explicitly directs this surface to describe the synchronized incident without candidate IDs, hidden route labels, internal rarity layers, exact modifiers, or other implementation detail. Package-specific treaty, formable, route, and achievement wording remains in the country package localisation, decisions, events, focuses, tooltips, manifests, and system documentation where the player can encounter it in context.

## Asset boundary

No asset files or sprite definitions were created or changed. In particular, this verification adds no Independence Wave advisor icon, portrait, sprite, dossier, or manifest entry.
