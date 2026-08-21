# Per-Event Chaos Levels Completion Report

## Implementation status

The requested source implementation is present across the normal-event registry, automatic selection, recovery, major-event growth, cluster-member availability, normal manual triggering, shared Events and Event Details presentation, documentation, and the authoritative event catalog.

The implementation remains validation-blocked because the mandatory HOI4 MCP event, GUI, and post-change probability routes did not return artifacts.

## Runtime contract

- `initialize_event_chaos_level_registry` creates one aligned `global.event_chaos_level_entries` value for every `global.all_events` entry.
- Every registered normal event defaults to internal tier 0, displayed as Chaos level 1.
- White Peace, Event 9, is the only current override and stores internal tier 1, displayed as Chaos level 2, Gathering Storm.
- `get_event_required_chaos_level`, `event_required_chaos_level_is_met`, and `evaluate_event_required_chaos_level` provide the shared lookup and gate.
- The active-pool evaluator rejects locked events before the weighted selector reads their weight.
- Repeatable recovery and major-event growth skip locked events without mutating stored weight, cap, fired history, or timer state.
- Cluster member availability reaches the same active-pool evaluator after its independent cluster and member-tier checks.
- Normal Settings, Event Details, and bulk event triggering apply the gate. Force Trigger Mode may bypass the gate while the existing special manual readiness rules remain intact outside the Settings force path.
- Triggerable scenarios and manual cluster forcing retain their existing independent behavior.

## Presentation and catalog

- The Events tab has six exact Chaos-level filters.
- A locked row displays `N/A` weight and a named `Requires` message.
- Event Details displays the exact tier-coloured numeric `Chaos lvl:` value.
- The workbook Events table contains a numeric `Chaos level` column with 98 registered normal-event rows populated.
- Events 1-8 and 10-20 are level 1, Event 9 is level 2, and registered Event 163 is level 1.
- The catalog exporter now emits 14 Event columns, including `Chaos level`, and regenerated all three CSV snapshots from the workbook.

## Meaningful source validation

Targeted assertions confirmed the registry, Event 9 override, active-pool rejection, frozen repeatable recovery, Settings/Event Details/bulk manual gates, cluster-member path through the active-pool evaluator, Events 1-20 catalog assignments, and Event 163 catalog assignment.

The localisation audit found no missing or duplicate feature keys, confirmed selector and parallel-array indices, confirmed the UTF-8 BOM, and retained the user-specified `Totalen Chaos` terminology after parent review.

The completion audit found no missing requested runtime, UI, documentation, catalog, asset, scenario, or cluster surface in source.

## MCP evidence blockers

- `hoi4.event_inspect` accepted both focused and lint requests but timed out after 180 seconds without an artifact.
- `hoi4.gui_inspect` for `events_log_popup_window` and scenario `event_chaos_level_event9_gathering_storm` timed out after 180 seconds without an artifact.
- `hoi4.gui_render` for the same window and scenario timed out after 180 seconds without an artifact.
- The probability adapter's baseline capability artifact reported `completePoolRequired = true`, `candidateCount = 0`, and `poolComplete = false` for this dynamically assembled pool.
- A bounded post-change `hoi4.probability_inspect` and `hoi4.probability_compare` using the unchanged 98-candidate scenario contract each timed out after 180 seconds, so no comparison ID, scenario hash, normalized probability, dominance, starvation, rank-reversal, or repetition evidence exists.

Source-level scenario comparison shows Event 9 excluded at Calm World with stored weight preserved, Event 9 eligible at Gathering Storm under identical White Peace conditions, Event 8 unaffected at Calm World, and the Peace cluster and member minimum tiers unchanged at internal tier 0.

## Simplifications and omissions

No implementation simplifications, fallback mechanics, placeholder assets, skipped assignments, or omitted player-facing surfaces were used.

Mandatory MCP event, GUI, and probability evidence is missing because the service timed out. This report does not treat source inspection as equivalent engine evidence and does not make an unqualified completion claim.
