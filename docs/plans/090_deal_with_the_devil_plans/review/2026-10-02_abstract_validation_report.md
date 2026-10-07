# Abstract validation report

Status: PASS.

The result below comes from executing `090_abstract_model_checks.py`. It checks selected route, explicit-acceptance, duplicate-delivery, evidence, history and cure-preservation invariants in a small Python model. It does not execute game scripts, validate owner APIs, test the UI, produce assets, evaluate AI probabilities, or resolve territory and engine gates.

```text
test_early_refusals_do_not_consume_acceptances (__main__.DesignInvariantTests.test_early_refusals_do_not_consume_acceptances) ... ok
test_early_settlement_preserves_delivered_cure (__main__.DesignInvariantTests.test_early_settlement_preserves_delivered_cure) ... ok
test_failed_or_duplicate_delivery_cannot_count (__main__.DesignInvariantTests.test_failed_or_duplicate_delivery_cannot_count) ... ok
test_final_offer_requires_evidence_and_time (__main__.DesignInvariantTests.test_final_offer_requires_evidence_and_time) ... ok
test_five_acceptances_are_peaceful (__main__.DesignInvariantTests.test_five_acceptances_are_peaceful) ... ok
test_leader_change_does_not_reset_history_or_rewards (__main__.DesignInvariantTests.test_leader_change_does_not_reset_history_or_rewards) ... ok
test_partial_refusals_retain_distinct_routes (__main__.DesignInvariantTests.test_partial_refusals_retain_distinct_routes) ... ok
test_resolved_side_favors_never_advance_main_count (__main__.DesignInvariantTests.test_resolved_side_favors_never_advance_main_count) ... ok
test_total_clean_refusal_has_no_infiltrated_institutions (__main__.DesignInvariantTests.test_total_clean_refusal_has_no_infiltrated_institutions) ... ok
test_unsigned_receipt_requires_explicit_adoption (__main__.DesignInvariantTests.test_unsigned_receipt_requires_explicit_adoption) ... ok

----------------------------------------------------------------------
Ran 10 tests in 0.002s

OK

```

All live acceptance scenarios remain required. A passing model does not certify the specification against every original source instruction.
