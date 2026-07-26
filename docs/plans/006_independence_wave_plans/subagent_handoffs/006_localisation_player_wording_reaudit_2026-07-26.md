# Event 006 player-facing wording re-audit

Audit date: 2026-07-26.

This bounded re-audit follows the player-facing wording patch in `c3ee88096` and the catalog mirror update in `2b0a04afe`. It changes no gameplay or asset files.

## Result

The SCN-008 descriptions, launch status, outcome summary, unavailable-movement record, and rejection reasons now describe visible political, territorial, diplomatic, and safety outcomes without exposing planner, registry, frozen-plan, or transaction terminology. Evolution II and Evolution V describe political emergence and the struggle for independence rather than internal package or pool mechanics. Formable readiness tooltips describe homeland, identity, symbols, consent, and credible settlement requirements in player-facing language.

The catalog mirrors now match the changed SCN-008 Sovereign Scatter premise and Maximum intensity wording, and Event 006 Evolution II and Evolution V bodies. Event 6 and Cluster 2 remain `In progress`; SCN-008 remains `Needs Testing`.

## Static checks

- The three changed English localisation files retain UTF-8 BOM and decode as UTF-8.
- The changed files contain 203 keys in total with no duplicate key IDs.
- No semicolon or em-dash punctuation was introduced.
- The existing scoped localisation audit remains authoritative for complete key-reference coverage; this handoff only closes the wording subset it identified.

## Boundary

The dynamic count opportunity in the scenario ready text was removed by describing the selectable surface without literal registry counts. Internal key and variable names such as `blocked_package_ids` remain implementation identifiers and are not rendered as player-facing prose. Whole-event completion remains **HOLD** under the v10 audit because DM-58 witness commitment, zero-blocker focus geometry, ten compatible admitted groups, runtime matrices, and other package and asset gates remain unresolved.
