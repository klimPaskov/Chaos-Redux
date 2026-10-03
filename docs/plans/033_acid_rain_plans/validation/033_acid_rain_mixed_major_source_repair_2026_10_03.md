# Acid Rain mixed-Major launch pacing

Disposition: source repair implemented and reviewed; probability and executed acceptance remain unresolved.
Acceptance basis: the user's Event 033 goal and Part 7 require one Major launch commitment whenever the validated Natural Disasters queue contains Event 33.

The prepared-order getter reads the registered cluster type and selected rows without changing participation or drawing a new roll.
For the Natural Disasters cluster, selected Event 33 promotes the batch to effective Major pacing.
The caller declares both getter outputs before invoking it.
Successful launch calls the Major pacing owner once and, for delayed Acid Rain, writes a country-owned categorical receipt keyed to that batch ID.
The delayed Major handler skips only Acid Rain's second reset when its matching receipt exists.
Standalone Acid Rain, other delayed Major events, and a Natural Disasters queue without Acid Rain retain their normal paths.
Queue cancellation and batch finalization clear only the relevant targeted receipt; committed launch history is not rewound.
No numeric weight, random selection, roll range, or timer tuning value changed.

## Checks and limits

The parent reviewed the getter, caller, delayed guard, and cleanup hunks, and the source regression assertions pass in `033_acid_rain_population_first_checkpoint_2026_10_03.json`.
The fixture scenarios remain `natural_disasters_without_33`, `natural_disasters_optional_33_after_13`, and `natural_disasters_33_trigger`.
The original before sources and fixture remain immutable under `probability/baseline_2026_10_03/cluster_pacing/`.
The read-only probability auditor found the original optional-after-13 Minor launch and delayed Major reset mismatch and reviewed this owner repair.
Initial inspection, narrower helper-filtered inspection, mandatory matched comparison, and a refreshed comparison after caller-output declarations each timed out after 600 seconds without an artifact or MCP source revision.
The detailed route receipts and dependency limitations are in `033_acid_rain_probability_audit.md`.
The fixture does not yet have engine-validated batch/receipt bindings, and the complete global selection pool remains undeclared.
Numerical timer distributions, weight deltas, helper dependency isolation, engine temporary-output persistence, reload receipts, migration of already queued batches, and multiplayer launch behavior remain unresolved.
Source review and synthetic invariants are not substitutes for those gates.

Reference reading includes offline Data structures line 551 for `@var:` targeting, lines 437–442 for caller-owned temporary outputs, and installed effects documentation sections `clear_variable`, `for_each_loop`, `set_variable`, and `set_temp_variable`.
The auditor retains their exact spans and local source hashes.

## Scope

Changed gameplay surfaces are the three receipt/getter hunks in `chaosx_event_cluster_effects.txt` and the launch/delayed-handler hunks in `chaosx_logic_effects.txt`.
The validator's pacing assertions and the Acid Rain exception in both shared cluster documents follow the same contract.
Unrelated Event 027, Event 042, and other concurrent shared-file changes are excluded from this tranche.
The authoritative workbook/export already states once-only Major pacing for a sequence containing Acid Rain; final cross-surface wording alignment remains part of Event 033 acceptance.
This is not a full Event 033 completion or clean-error-log claim.
