# Migration priority triggers

This file validates the player-selected class attached to an exact organized-evacuation cohort. It performs no mutation and no country, state, or province scan.

## `migration_cohort_priority_is_valid`

Scope: any scope holding the temporary `migration_cohort_record_priority` input.

Inputs: `migration_cohort_record_priority` must equal one of the four identifiers in `migration_cohort_priority`.

Output: true only for `general`, `vulnerable`, `industrial`, or `administrative`.

Call site: `migration_cohort_record_request_is_valid` in `common/scripted_triggers/migration_core_triggers.txt`.

Tuning and identifiers: `common/script_constants/migration_cohort_priority_constants.txt`.

## General evacuation availability and payment triggers

`migration_evacuate_civilians_cost_is_affordable` checks the shared standard train/fuel/convoy profile and rejects a second paid receipt for the selected state.

`migration_evacuate_civilians_can_start` uses the same existing-state pressure, prepared-route, current-controller, and national reception-capacity gates as the specialized evacuation lanes. It adds no preparation step or support-equipment requirement.

`migration_evacuate_civilians_cost_receipt_is_valid` binds refunds and cleanup to the paid actor who still controls the selected origin state.

All three are called by `migration_evacuate_civilians` in `common/decisions/migration_decisions.txt`; the selected cohort receives `general` priority.

## Administrative evacuation availability and payment triggers

`migration_evacuate_administration_cost_is_affordable` checks the shared standard train/fuel/convoy profile, rejects a second paid receipt for the selected state, and checks the separate train requirement.

`migration_evacuate_administration_can_start` uses the same existing-state pressure, prepared-route, current-controller, and national reception-capacity gates as the other organized evacuation lanes. It adds no preparation step or support-equipment requirement.

`migration_evacuate_administration_cost_receipt_is_valid` binds refunds and cleanup to the paid actor who still controls the selected origin state.

All three are called by `migration_evacuate_administration` in `common/decisions/migration_decisions.txt`. Their fee tuning is in `common/script_constants/migration_transport_cost_constants.txt` and `humanitarian_legacy_cost_constants.txt`.

## Explicit action context

Scope-sensitive bodies have one `_in_context` implementation reading the mandatory unscoped temporary COUNTRY pointer `humanitarian_action_actor` and STATE pointer `humanitarian_action_target`.
The original helper name is a compatibility wrapper initializing those inputs from ROOT and FROM before a bare `= yes` call when no explicit context is proven.
A caller that supplies an explicit envelope also initializes temporary `humanitarian_action_context_proven = 1`, so nested legacy wrappers retain that exact actor and target.
Panel gates initialize the actor from their country context and the target from the exact selected state, and an immediate country event establishes the actor as ROOT for deep owner helpers.
These helpers accept no named arguments, have no implicit scope defaults, and publish no additional gameplay output beyond their documented owner body.
These adapters do not change tuning or create independent transaction owners.
See [the shared action lifecycle](../scripted_effects/humanitarian_gui_action_effects.md) for caller, pending, and cleanup contracts.
