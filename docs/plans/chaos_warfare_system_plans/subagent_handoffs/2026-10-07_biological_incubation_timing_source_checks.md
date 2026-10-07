# Biological incubation timing source checks

Disposition: implemented bounded independent source regression, pending parent review.
Acceptance basis: the parent approved the reviewed late queue helper and froze the source before final execution.
The architecture review was read, and the parent owns implementation, MCP evidence, integration, and the commit.

## Artifacts and final execution

Only these three assigned new files were written:

- `docs/testing/2026-10-07_biological_incubation_timing_source_tests.js`
- `docs/testing/2026-10-07_biological_incubation_timing_source_results.json`
- This handoff.

Run from the mod root:

```powershell
node docs/testing/2026-10-07_biological_incubation_timing_source_tests.js
```

The final run at `2026-10-07T17:07:51.375Z` exited 0 with 20 passing cases and `passed_bounded_incubation_timing_source_model`.
The original raid lifetime test suite and its 150-case archives were not edited or rerun.
The existing Event 026 parser and strict helper-frame VM are reused unchanged.
All native event requests are captured, and callback invocation is manual at a chosen fixture day.

The JSON records each delay sample, getter value, literal event request, due-day offset, baseline failure, source hashes, reference spans, and model limits.

## Exact source preservation

All three raw before archives match the baseline manifest.
All three raw after archives match the expected frozen source hashes, using the patch manifest for the changed lifecycle file and the original hashes for unchanged events/constants.
Current gameplay equals the raw after archive after CRLF-to-LF conversion only.
This permits checkout line-ending conversion without weakening substantive source comparisons.
The parent-owned local evidence attributes preserve both raw archive directories.

The complete lifecycle AST differs only by:

1. The new `bio_lifecycle_queue_incubation_event_internal` helper, containing one numeric meta-built state event and no draw, variable assignment, guard, or flag mutation.
2. Replacement of the scheduler's original premature `state_event` statement with that helper call.
3. Removal of the outer scheduler's premature `BIO_INCUBATION_DAYS` argument.

The original getter, scheduler guard/order, scheduled flag, due-day writes, activation body, tick scheduler, and all other existing definitions remain equal.
The new helper reads the existing caller-owned selector and computed incubation days, then builds literal integer ID/delay tokens.
No additional temporary return output is introduced.
The event entries and all tuning constants remain unchanged.

| Lifecycle source | SHA-256 |
| --- | --- |
| Before | `3d611e3424da6f221446810f6f4ad49e4065b1a8c066bcf7bec3989038a5d3cc` |
| After | `9bf1e04826fdde8c745e946af3230b6534707f457777637bda84e0c2f6105450` |

## Timing and guard evidence

Twelve cases execute every agent with deterministic random samples 0, 0.5, and 1.
The actual getter result, rounded/clamped oracle, queued literal event delay, and saved due-day offset agree in every revised case.
At fixture day 100, the tested delays are:

| Agent | Minimum sample | Midpoint sample | Upper sample |
| --- | ---: | ---: | ---: |
| Anthrax | 5 | 8 | 10 |
| Plague | 4 | 6 | 8 |
| Tularemia | 5 | 8 | 11 |
| Smallpox | 12 | 17 | 21 |

All event IDs match the selected agent's existing activation callback `.1` through `.4`.
The minimum clamp is executed from actual source, though none of these authored positive ranges requires a binding clamp.
No constants are altered to manufacture a clamp case.

Each sample reproduces the baseline event delay zero while its getter and saved due day are positive.
Invoking that baseline callback at the scheduling day fails the existing due guard and leaves both incubating and incubation-scheduled flags set, with no later activation request produced by the tested source path.
This reproduces the source-model timing failure without claiming observed engine execution.

For the revised source, repeated scheduling after changing fixture day and RNG input produces no second draw, no second request, and no due-date overwrite.
The callback immediately before due remains rejected with incubation state intact.
The exact-due callback changes the agent to active once, clears incubation scheduling state, and queues the unchanged weekly tick ID `.11` through `.14` at seven days.
A duplicate activation callback creates no second tick.
Four absent-incubating cases create neither draw nor event nor due field.

The shared-state case schedules Anthrax at day 45 and Smallpox at day 61 from fixture day 40.
Activating Anthrax does not overwrite or activate the later Smallpox record.
Both agents retain independent flags, due fields, activation IDs, and tick IDs in the same state.

## Reference and model limits

The local reads cover installed `effects_documentation.md:4833-4852` for meta-effect construction, `8096-8128` for numeric state-event delays, and offline `Effects:4617-4682` for substitution before built effect execution.
Their paths and source revisions are recorded in the JSON.
This model evaluates numeric meta arguments when each actual meta node executes, so the revised queue helper captures the delay after the getter rather than before it.

Deterministic samples exercise arithmetic boundaries and do not establish a native RNG distribution or whether the exact upper endpoint is reachable.
Positive half-up integer rounding is an explicit local convention, including midpoint cases.
Native RNG, rounding, callback timing/cardinality, and actual state-event queues remain unproved.

The actual getter, scheduler, queue helper, activation, tick scheduler, and activation event entries are evaluated from source.
Detection, state-modifier, and air-contribution hooks are explicit captured no-op boundaries.
Actual tick effects, protection, mortality, spread, and the broader outbreak transaction are outside scope.
The regular due fields and flags belong to one exact fixture state, and the two-agent case checks separate keyed records within that state.

The repair prevents newly queued zero-delay activation under the reviewed source model.
It introduces and validates no recovery for a previously stranded record.
No whole-biological-service or live-game completion is claimed.
No gameplay, shared VM, old test/evidence package, MCP/probability call, game launch, log search, staging, or commit was performed by this worker.
Skills used remain `chaos-redux-events`, `chaos-redux-native-raids`, and `chaos-redux-subagents`, with no skill changes.
No gameplay fallback or simplification was introduced.
