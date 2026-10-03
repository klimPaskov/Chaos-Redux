# Event 31 terminal owned-state trigger repair

## Report and disposition

Implemented bounded repair for the orchestrator's live load report from committed HEAD `aa9b16b58`, supplied on 2026-10-04.
The report identifies `Unknown trigger-type: num_of_owned_states` at both actor-validation branches in `random_terror_begin_false_revelation`.
The parent accepts this correction under the explicit live-QA fix request.
This does not close Event 31 implementation or establish a clean error log.

## Correction and semantics

Both invalid `num_of_owned_states > constant:random_terror_value.zero` checks are replaced by `any_owned_state = { always = yes }`.
This preserves the intended requirement that the selected actor owns at least one state.
Using only `num_of_controlled_states` would weaken that requirement for an actor occupying foreign territory without owning a state.
The existing `random_terror_is_viable_actor` guard independently retains its controlled-state and authority/control requirements.
The 1000+ Chaos and other terminal-readiness gates, dominant-actor scoring, branch selection, costs and AI weights are unchanged.

The commit owns only these two source-line replacements and this handoff.
The ongoing mission-ownership patch in the same effects file is excluded through the shared-tree isolated-index workflow.

## References and meaningful checks

Successful live `hoi4.reference_search` and revision-bound `hoi4.reference_read` identify `any_owned_state` as a country-scope existential state trigger in installed `documentation/triggers_documentation.md:1612-1620`.
Citation ID is `7cbd6de6bbed744f4c9ee3dbf152eddba33b1c2b05700fd912588abc18b72cd2`, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.
The offline `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md:387-392`, read directly during this repair and through the prior mission reference pass, describes the same owned-state iterator separately from controlled-state iteration.
Its SHA-256 is `18EF5249E4991F5427ECA9EC4A2F66DD47F51E26A491C730ADC622F1F5DB1B49`.
Installed `common/scripted_triggers/SWI_scripted_triggers.txt:485-489` supplies a vanilla existential owned-state precedent.

Source-bound truth-table cases cover an actor with no states, foreign occupation only, ownership without control, and both ownership and control.
The ownership predicate rejects the first two, accepts the ownership predicate in the third, and accepts the fourth.
The unchanged viability predicate still rejects the third case without controlled territory.
The corrected helper has two owned-state predicates and no unsupported owned-state count token.
No game was launched and no logs were requested.
Fresh live load acceptance is not claimed from source review.

## Simplifications, omissions, and blockers

No simplification or fallback was used in this bounded correction.
Unfinished mission, country, focus, asset, probability and terminal-transaction work remains outside this commit.
