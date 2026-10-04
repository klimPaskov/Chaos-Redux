# Event 027 queue correction and evidence

Disposition: implemented in source with model and runtime validation pending.
Acceptance basis: the user's goal requires separate country-owned queued batches, one-time receipts, and silent AI completion after each firing.

## Changed source

- `common/scripted_triggers/027_doctrine_research_triggers.txt`: restored `doctrine_research_receipt_ids^num = doctrine_research_receipt_batch_ids^num` in `doctrine_research_country_state_is_aligned`.
- `common/scripted_effects/027_doctrine_research_effects.txt`: removed the automatic corruption-flag clearing introduced by the erroneous cardinality diagnosis and added zero-choice completion to `doctrine_research_ai_resolve_active_batch`.
- `common/scripted_effects/027_doctrine_research_effects.txt`: guarded `doctrine_research_finalize_receipt` with effect-applied state, matching batch and choice identity, and positive remaining choices, then clears the selected action after recording the successful result.
- `docs/events/027_doctrine_research/overview.md`: recorded the correction and current acceptance limits.
- `docs/plans/027_doctrine_research_plans/receipt_finalize_once_scenario.json`: saved a source-backed mechanic-test fixture for repeated finalization.

The September parent diagnosis confused `doctrine_research_receipt_batch_ids` with `doctrine_research_batch_ids`.
The former is one parent ID per receipt and must align with all other receipt columns.
The batch ledger still checks its own columns independently.
The old diagnosis and any source-playability claim based on it are superseded by this correction.

The AI final closure branch previously required remaining choices to be greater than zero.
After its last successful choice, the country retained an active batch with zero choices.
The corrected branch checks the original active batch identity and completes it when choices are zero or the country has no valid action.
Completion uses `doctrine_research_complete_active_batch`, which closes the row and starts the next queued row.

Receipt finalization previously had no local replay guard.
The owner now checks the immutable receipt identity before decrementing a choice and clears only the selected action after preserving the result context.
The saved scenario invokes finalization twice and expects exactly one consumed choice, one recorded adoption, and a cleared action.
This fixture tests script state behavior and does not model the native doctrine engine.

## Reference evidence

The connected reference context and search routes responded on 2026-10-03.
An event context bundle returned omitted sources, so it is not recorded as complete topic coverage.
The pertinent array sections were read directly and through the reference route.

| Source | Lines | Revision | Rule used |
| --- | --- | --- | --- |
| `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` | 1069-1077 | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` | Arrays are scope-owned persistent collections, indexes start at zero, and `^num` returns element count. |
| Installed `documentation/effects_documentation.md` | 2278-2292 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` | `add_to_array` appends one element by default. |
| Installed `documentation/triggers_documentation.md` | 2110-2135 | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` | `check_variable` accepts another variable as its comparison value and supports explicit equality and ordering comparisons. |

The source lookup result at revision `20eaed78808f6daf60a5b4a4a760a523b48eba6d8f795ddc919b1b8d9fbdc79b` showed the pre-restoration trigger and was truncated within the returned block.
It is historical before evidence, not final helper coverage.

## Remaining validation

A source-backed MCP mechanic test was submitted for initialization with one batch and zero receipts.
The connected call returned `timed out awaiting tools/call after 600s`.
No test verdict or job identity was delivered, so its model outcome remains unresolved and no passing result is claimed.
A full Event 027 state-flow inspection and the repeated-finalization mechanic test also returned `timed out awaiting tools/call after 600s`.
No verdict or usable job identity was delivered by either call.
These tool failures establish no native mastery or persistence proof.

Current source hashes after these corrections are `DB2EBFAE400A4FC56ACB1988E9DEC548A8A9865FD31D190CF1A5C603AC2C8FA6` for the runtime effects and `CFBC55ECCD114D3C388CAD23D3CC87D8904152B032C325AF567BE1CE894B23A3` for the adapter triggers.
These hashes bind this handoff to the inspected source and must be refreshed if subsequent audits patch it.

The native transaction architect, probability auditor, completion auditor, and localisation auditor are assigned current scoped reviews with no inherited context.
The feature remains incomplete and no completion commit has been created.
