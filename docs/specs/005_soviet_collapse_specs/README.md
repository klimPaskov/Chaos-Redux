# Event 005 Soviet Collapse specifications

The seven `005_soviet_union_collapse_final_clean_merged_part_*` files form the merged design package. The Kuznetsk Mining Board and Unconventional Warfare Republic documents are bounded companion sources.

The folder uses `soviet_collapse` while the merged files retain the older `soviet_union_collapse` wording. Treat those as aliases for Event 005 and do not create a second event package.

Acceptance is determined per design claim from recorded user direction or parent acceptance within that scope.
The merged package's title and earlier correction labels do not independently approve every requirement.
The companion UWR and KMB documents retain bounded implementation descriptions whose dates and current limitations must be checked against the working ledger.
The asset manifest is `docs/assets/005_soviet_collapse/manifest.md`, matching the existing asset directory; it is absent in the current checkout, which leaves asset provenance unresolved.

Current implementation documentation is in [`docs/events/005_soviet_collapse/overview.md`](../../events/005_soviet_collapse/overview.md). Working status and historical audit routing are in [`docs/plans/005_soviet_collapse_plans/source_of_truth_map.md`](../../plans/005_soviet_collapse_plans/source_of_truth_map.md).

## Open questions

These are proposals from the 2026-10-10 spec audit, not accepted design, and they are not implementation requirements until the user or a parent accepts them.

- Visible-value budget (Part 2): at most three crisis values on any category header or crisis tooltip, with the rest shown in the effect tooltip of the action that moves them, and no ninth meter without a decision that the existing eight cannot express.
- Chaos Meter contribution (Part 3): one bounded terminal contribution sized from the realized rupture, with ordinary stage progress silent.
- Gulag feedback (Part 3): live camp sites raise a republic's Armed Breakaway Momentum and an accepted dismantlement route lowers it, using the existing camp markers.
- Famine inheritance (Part 3): a republic released into a state already under famine pressure inherits that pressure as an opening problem.

## Changelog

### 2026-10-10 spec audit

Consistency pass: Part 1's seven required ledger and audit files were reduced to the one current implementation audit plus the asset manifest, with the superseded files recorded as such; the required-reading list no longer restates the repository rules; the Part 7 completion report and acceptance list no longer duplicate Part 1 and the repository completion rules; the asset manifest path now matches the existing `docs/assets/005_soviet_collapse/` directory; the validation scenarios state that they are documented from source review because live confirmation is the user's; and the skill links point at the canonical `.claude/skills` path.

Design pass: Part 2 now carries one canonical crisis-value table with the real source variables, the unimplemented Local Support meter was dropped, the event-detail window became four in-world lines instead of an eleven-item status dump, Part 3 refers to that single table instead of its own twelve-value list, and a new Part 3 section records the camp and repression bridge and the automatic humanitarian and casualty connections that already exist, so the event does not pay for the same displacement, food strain or deaths twice.

