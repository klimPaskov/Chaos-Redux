# Event 012 Formables cluster catalog alignment

Date: 2026-08-01.

Status: implemented source-and-catalog alignment; live campaign acceptance remains open.

## Scope

This tranche aligns the existing Formables cluster registration with the accepted Event 012 contract. It does not add a cluster, event, tag, country, or duplicate member store.

The stable cluster ID remains `6`. The repeatable cluster unlocks at Chaos Tier 3, while Event 12 remains its required Severe Fire-Once member at Chaos Tier 4.

## Changes

- `common/script_constants/event_cluster_constants.txt` now sets `event_cluster_formables.unlock_tier = 3`.
- `docs/systems/event_system/event_clusters.md` describes Africa Is One as the required Severe member and records the tier-3 cluster / tier-4 member split.
- `localisation/english/chaosx_gui_l_english.yml` replaces the stale “no playable formable escalation” cluster description with the protection-first, consent-based Formables wording.
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx` updates only the cluster-6 description, member list (`12`), and status (`In progress`) on the `Clusters` sheet. All unrelated workbook cell values were checked unchanged.
- The required exporter regenerated the three read-only catalog CSV snapshots.
- `docs/events/012_africa/overview.md` now records the catalog/runtime alignment.

## Validation

- The runtime cluster source already maps Event 12 to `constant:event_cluster_id.formables`, queues it as a required member, and assigns Severe danger with a tier-4 member minimum; this tranche changes only the shared cluster unlock constant and presentation/catalog surfaces.
- The workbook round-trip assertion found no non-target cell-value changes.
- The exporter completed successfully for Events, Clusters, and Scenarios.
- The generated Formables row reads `6 | Formables | ... | 12 | Minor Repeatable | 3 | In progress`.
- No new tag, cosmetic identity, model, fallback, recurring world scan, or terminal readiness flag was introduced.

## Remaining boundary

The Event 12 member and the Formables cluster still require live consumer testing. This alignment does not certify the blocked W5 continent packages, terminal super-event, model/audio/native-review dependencies, or the broader Event 12 completion ledger.
