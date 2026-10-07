# Event016 Rocketry native AI source evidence

Disposition: immutable-source comparison and bounded scenario review implemented, with full native-state and campaign acceptance incomplete.
Acceptance basis: the existing D27 source-selection policy and the user's direction to finish the accepted Event016 plan without simplifications.
This tranche changes no gameplay weights, decisions, costs, model files or runtime state.

## Result

The four Rocketry selection and withdrawal actions were inspected and compared using the exact decision file before D27 and its current unchanged post-D27 version.
Fifteen different declared source states replace the earlier nine repeated fixture labels.
No candidate eligibility override is used.
The immutable files, requests and reviewed outcomes are under [the evidence fixture](../../testing/event016_native_selection_ai_20261007/README.md).

The MCP comparison identifies five withdrawal score increases from zero to ten.
Four are stale selections where the opposite Rocketry project is being researched or completed.
The fifth is the same state with a closed programme, where the separate decision inspection confirms that the category and action are hidden.
The paid Prototype case excludes all four actions in the probability availability model and makes the withdrawal both invisible and unavailable in the decision inspection.
The current war/factory points return 20 for war with four spare factories, 10 for war with three, and 5 for peace with three.
No selection-candidate score changes in these declared cases, so they do not establish the new suppressors' behavior when both technology paths are simultaneously researchable.

The parent independently verified the recovered comparison and evaluation bytes against their returned SHA-256 hashes.
It then checked the fifteen scenario IDs and scenario hash, all five deltas, rank and unresolved deltas, the three war/factory values and the paid-case exclusion.
The auditor's [handoff](subagent_handoffs/016_rocketry_native_snapshot_comparison_2026-10-07.md) and [parent review](../../testing/event016_native_selection_ai_20261007/comparison_review.json) retain the source identities and limits.

## Source and artifact preservation

The before file is the exact Git source from `a4b0c089ab8ad406551ec361db5f8d2c02e52b88`, the parent of `dd10a3f3e36aa63d50a9cfd5294b75a23126bc46`.
The current decision Git blob still equals the D27 decision blob, `840c851298496663807de6658a34a3b178b8ddb3`.
The live MCP accepted `path`, `snapshotPath` and `expectedSourceHash`, letting both frozen copies retain the original logical gameplay path without replacing live files.
Shared helpers and constants remain current, so this is a decision-file comparison under current dependencies.
It is not a full historical workspace reconstruction.

The exact current evaluation is saved as `after_analysis.json`, 1,879,534 bytes, SHA-256 `fdc724afd8fd3608ff3dd54d29db5d32a4f459c577fcb7de7832f8c71543cb13`.
The exact comparison is saved as `compare_analysis.json`, 1,893,939 bytes, SHA-256 `8676e8d30ea64a01f2ef58c7e41098f6f1ab4c497799b9d8e580a1435469b40c`.
The parent's direct retrieval of those aggregate artifacts failed, and the auditor recovered the already-produced bytes without rerunning.
The parent verified the copies independently.
An additional parent comparison returned the same scenario hash, five changes, fourteen available candidate rows, forty-six excluded rows and eight unresolved items.
Its compact response and its separate artifact-delivery limit are retained in `parent_repeat_evidence.json`.

## Availability, visibility and remaining limits

The probability adapter reads `available` and AI scoring, and returns willingness scores rather than normalized selection probabilities.
The parent separately inspected the withdrawal's category and decision visibility with valid, closed-provider and paid-receipt states.
At explicitly declared political power zero, all three zero-cost actions are affordable.
Only the valid-provider case is visible and available.
The full decision report remains partial because numeric state 88 is unbound in historical German-programme branches.
Those warnings are preserved in [the visibility evidence](../../testing/event016_native_selection_ai_20261007/decision_visibility_evidence.json).

The installed scalar predicate model cannot represent both Rocketry projects completed or researched, both prerequisite technology paths, or simultaneous Gotterdammerung and By Blood Alone states through the fields used here.
Those joint states remain open and were not replaced with an eligibility override or fabricated gameplay flag.
The fixtures are expression-level checks and do not prove campaign reachability of every combination, native AI cadence, repeated execution or native cancellation/reselection behavior.
The comparison's empty regression list is limited to the declared analyzer comparison and is not whole-event balance acceptance.
The comparison produced render artifacts, while a later standalone render rejected a changed workspace revision.
No fresh standalone visual acceptance is inferred from that stale result.

## Documentation and reusable guidance

The source reports, resume checkpoint and accepted portfolio plan point to this stronger bounded comparison while retaining the unresolved requirements.
The earlier partial audit remains historical evidence, including its rejected repeated-state fixtures.
The `chaos-redux-subagents` skill now explains verified immutable source selectors, complete byte-range artifact recovery and why an empty discovered input list does not prove complete scenario state.
The [skill review](subagent_handoffs/016_probability_evidence_skill_review_2026-10-07.md) records the parent-owned paragraphs and the preserved unrelated working changes.
No event-specific context was added to the skill.

No implementation simplification or acceptance waiver was introduced.
No models were created, inspected or changed, and HOI4 was not launched.
Native lifecycle proof, unsupported joint-state coverage, remaining domain/UI/catalog requirements and clean live error.log evidence remain open under the full Event016 goal.
