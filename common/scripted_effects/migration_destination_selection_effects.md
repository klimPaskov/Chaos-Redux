# Migration Destination Selection Helpers

This helper set owns adjacent-state destination selection and the bounded closed-border rejection prepass. It does not mutate population, create deaths, scan distant geometry, or add a mapmode. The normal selector remains the only weighted destination consumer.

## Helper map

| Helper | Scope | Inputs | Outputs | Side effects | Call sites |
| --- | --- | --- | --- | --- | --- |
| `migration_destination_selection_bind_actor` | State | Explicit override proof or ROOT | Regular chain-local actor target | Refreshes the actor target for ordinary callers | Every selector and the rejection prepass |
| `migration_destination_selection_border_admissible` | State trigger | Candidate owner reception policy and pending forced-return flag | Admission boolean | None | Foreign candidate trigger |
| `migration_destination_selection_reception_policy_blocks_admission` | State trigger | Candidate owner authoritative reception policy | Exact closed, violent, or forced-return blocker boolean | None | Rejection candidate and receipt revalidation |
| `migration_destination_selection_foreign_policy_rejection_candidate_is_valid` | State trigger | Adjacent candidate, origin target, safety facts, capacity, owner/controller, route, and policy blocker | Otherwise-valid foreign policy-rejection boolean | None | Closed-border prepass |
| `migration_destination_selection_preflight_closed_border_rejection` | State | Origin state and actor target | Temporary exact candidate count/result plus chain-local destination and actor targets when count is one | One adjacent-neighbor proof pass | Spontaneous movement owner before the normal selector |
| `migration_destination_selection_run_weighted_pool` | State | Pool identifier and actor target | Temporary result plus normal route or donor target | Existing two-pass weighted selection and normal proof writes | Destination wrappers |

## Policy contract

Foreign admission consumes `migration_reception_policy` through the decision-owner `migration_decision_reception_policy_allows_admission` trigger. The derived `migration_border_policy` remains presentation compatibility only. A missing or malformed reception policy fails closed in the consumer. The decision-owner initialization/backfill contract remains responsible for migrating legacy policy state.

The prepass recognizes only valid reception values `closed`, `violent`, and `forced_return` as exact policy blockers. It does not infer a cause from an unset policy, a malformed value, the presentation policy, a forced-return pending flag, or any candidate that fails a separate safety, capacity, controller, owner, war, or route gate.

## Weighted selector preservation

`migration_destination_selection_calculate_candidate_weight` retains its existing numeric terms and tuning constants. Its foreign policy preference reads the authoritative reception variable for valid candidates. The added prepass performs no random draw and contributes no weight. The weighted surfaces affected by the policy-consumer patch are `prob_destination_selection_internal`, `prob_destination_selection_persecution`, `prob_destination_selection_donor`, and `prob_cleanup` through the existing candidate gates. Independent baseline/post-change probability auditing remains required.

## Proof and lifecycle

The prepass iterates only `every_neighbor_state` from the registered origin. It counts candidates that pass the normal foreign safety and capacity contract while the destination policy blocker is true. It saves the exact destination state and its owner only when the count equals `constant:migration_destination_selection_runtime.one`. These are regular event targets and clear with the current effect chain.

The spontaneous owner calls the normal selector after the prepass. A successful normal selection makes the prepass irrelevant. A failed normal selection calls the spontaneous trap helper without touching population and then records a rejection only when the exact prepass result and chain-local targets still validate. The destination-selection helpers never call a Condemnation adapter.

## Validation notes and limitations

The trigger is intentionally duplicated at the safety-contract boundary so the policy proof cannot accidentally admit a destination excluded by the normal selector. It uses no `every_state`, `every_country`, distant path inference, mapmode, or balance constant. The current Condemnation adapter has no exact actor, blocker, generation, and transaction input contract, so durable receipt fields are emitted for the owning integration handoff rather than passed to an incompatible wrapper.

The installed `hoi4_probability_inspect` route was attempted before this weighted-surface review. No callable `chaosx_ai_probability_auditor` route is exposed in the current tool registry, so independent scenario evaluation and `hoi4.probability_compare` evidence remain blocked. No live game was launched by this helper owner.
