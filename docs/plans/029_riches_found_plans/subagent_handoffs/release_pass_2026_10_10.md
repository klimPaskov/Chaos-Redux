# Event 029 release pass, 2026-10-10

Scope: Events 1-40 milestone release pass under the 2026-10-10 brief.

## Changes

- Committed the wartime denial tranche that was already in the tree: Deny the Mine is offered only while its controller is at war, a control change refreshes the registered mines beside the changed state, an occupier's revenue line reads as occupation receipts, and the foreign interest score is zeroed before each candidate.
- Fixed a malformed localisation line (`key:"text"`) for the patronage revenue route.
- Added readable requirement text for ten flags that were shown as raw identifiers in decision tooltips.
- Removed eighteen never-read entries from the `riches_found_ai_weight` constant table, leaving the policy weights the opening event reads.
- Moved the unloaded transport-cost helper module (28 helpers, no caller) from `common/` to `deferred_transport_cost/`, so shipped script contains only code that runs.

## Checked

- Every decision and mission has name and description keys; every `riches_found_*` and `rf_*` effect or trigger call resolves to a definition.
- Report and news keys carry no colour codes; the report slot queue already limits popups to one per mine at a time.
- Event 029 is Minor Repeatable with no cluster by the 2026-10-07 user instruction, so Sudden Abundance cluster 15 gets no member row.
- Not verified in game: the neighbor refresh in `on_state_control_changed` and Deny the Mine in a live war.
