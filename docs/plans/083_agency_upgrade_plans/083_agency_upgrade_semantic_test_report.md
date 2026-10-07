# Event 83 abstract semantic test report

Executed on 22 September 2026 with the included standalone Python reference model.

**Result: 30 tests run, 0 failures, 0 errors.**

## What was tested

The model checks package thresholds, independent evolution controls, creation-before-award counting, sequential synthetic upgrade eligibility, one-for-one exhaustion, cumulative abstract recruit entitlements, duplicate redemption protection, once-per-firing Chaos, independent percentage-contribution lifetimes, other-owner preservation, conditional family eligibility, feature preflight, synthetic registry coverage, and a JSON round trip of the model's own data.

The fixed probability calculation is exact arithmetic for the authored family rule. It is not a sampled campaign result or a finding from the game's picker.

## What was not tested

This model does not execute HOI4, use the actual upgrade database, recruit an operative through the native UI, validate engine modifier names, prove correct percentage adapters, inspect actual operation callbacks, validate native save formats, compare multiplayer clients, process runtime assets, or replace an independent subagent or HOI4 probability audit.

The test named `native_candidate_entitlements_are_distinct` tests abstract entitlement identity only. It does not establish that the native recruitment interface can redeem those entitlements. Similarly, the JSON round trip proves persistence in this reference model rather than native HOI4 save compatibility.

## Reproduce

From the companion plans folder, run:

```bash
python 083_agency_upgrade_semantic_checks.py --report 083_agency_upgrade_semantic_results.json
```

Python 3.10 or newer and the standard library are sufficient. The model uses synthetic upgrade names and integer percentage contributions. It is not drop-in Clausewitz implementation code.

## Actual check results

| Check | Result |
| --- | --- |
| `test_01_thresholds` | Pass |
| `test_02_independent_enable_controls` | Pass |
| `test_03_new_agency_does_not_consume_roll` | Pass |
| `test_04_replacement_package_not_twelve` | Pass |
| `test_05_no_owned_or_same_firing_duplicate` | Pass |
| `test_06_prerequisite_recomputed_per_draw` | Pass |
| `test_07_two_remaining_three_conversions` | Pass |
| `test_08_exhaustion_every_package` | Pass |
| `test_09_native_candidate_entitlements_are_distinct` | Pass |
| `test_10_claim_cannot_be_redeemed_twice` | Pass |
| `test_11_duplicate_recipient_is_idempotent` | Pass |
| `test_12_world_chaos_once_not_per_country` | Pass |
| `test_13_tier_snapshot_before_own_chaos` | Pass |
| `test_14_fixed_suite_exact` | Pass |
| `test_15_duplicate_network_conversions_add` | Pass |
| `test_16_staggered_expiration_no_refresh` | Pass |
| `test_17_capacity_survives_expiration` | Pass |
| `test_18_other_owner_preserved` | Pass |
| `test_19_restricted_families` | Pass |
| `test_20_cryptology_with_one_usable_branch` | Pass |
| `test_21_specialty_is_one_eligible_bonus` | Pass |
| `test_22_no_usable_specialty_exception` | Pass |
| `test_23_country_restriction` | Pass |
| `test_24_dormant_country_excluded` | Pass |
| `test_25_capability_failure_no_mutation` | Pass |
| `test_26_registry_coverage_failure` | Pass |
| `test_27_json_roundtrip_claims_and_expirations` | Pass |
| `test_28_exact_design_probability_arithmetic` | Pass |
| `test_29_later_weaker_package_does_not_revoke` | Pass |
| `test_30_same_day_separate_firings` | Pass |

The complete console output is retained in `083_agency_upgrade_semantic_run.txt`, and the machine-readable result is retained in `083_agency_upgrade_semantic_results.json`.
