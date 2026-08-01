# Event 016 cross-domain synthesis decision audit

## Scope

Audited the cross-domain review decision, its synthesis triggers and effects, event `chaosx.nr16.14`, related constants and dynamic modifier, and the bounded transfer and Kruger State formation handoff paths.

## Changed files

- `common/script_constants/016_brilliant_scientist_directorate_constants.txt`
  - Added `brilliant_scientist_cross_domain_review.political_power_gate`.
- `common/scripted_triggers/016_brilliant_scientist_synthesis_triggers.txt`
  - Updated `brilliant_scientist_can_pay_cross_domain_review`.
- `localisation/english/016_brilliant_scientist_directorate_outcomes_l_english.yml`
  - Added `brilliant_scientist_convene_cross_domain_review_desc`.

## Issue list, sorted by severity

1. Resolved, high confidence: the availability gate used `num_of_available_civilian_factories`, which does not specifically reserve capacity for a new decision project.
   It now uses `num_of_civilian_factories_available_for_projects` against the same centralized two-factory requirement, matching the `civilian_factory_use` burden.
2. Resolved, high confidence: the custom gate required `political_power > 70` for a visible 70 PP decision cost.
   It now requires `political_power > political_power_gate`, where the centralized gate is 69, so exactly 70 PP is sufficient.
3. Resolved, low severity: the visible decision lacked its standard `_desc` localisation key.

No remaining correctness defect was found in the bounded decision, event, transfer, formation, dynamic-modifier, or cleanup paths.
The custom-cost string is clear, but it is not yet the decision skill's preferred fully icon-first presentation.

## Lifecycle and mission notes

The decision is visible only to the current host when ready or already pending or in progress, is clickable only when both prototypes, the valid project board, and all resource gates are present, and stays as a timed 120-day factory-burdened review after selection.

Cancellation clears the transient review flags when the host, prototype prerequisites, or world state invalidates the review.

Ordinary transfer records a paid pending review before mutating the old host, clears the old host state, restores it to the recipient, and fires `chaosx.nr16.14` there without taking costs a second time.

Sovereignty formation restores the same receipt set through `brilliant_scientist_inherit_exact_host_directorate_state`, restores the validated synthesis modifier through `brilliant_scientist_restore_exact_directorate_modifiers`, and queues the resolution event if the review was pending.

This tranche has no mission, so there is no mission owner, region, success, failure, duration, or duplicate-mission risk to record.

## Costs, AI, localisation, and cleanup

The review has a one-time 70 PP payment, 300 support equipment, 150 motorized equipment, 1,500 fuel, 1,500 manpower, and two civilian factories for 120 days.

The event is self-targeted and its resolution trigger revalidates the host, primary facility, prototype receipts, pending receipt, completion state, and terminal-state gate.

Decision AI has a nonzero base only while the full availability gate is true, then adjusts for security, exposure, and independent capacity.

Event option AI uses valid root-only conditions and has no target, route, or dead-country reference risk.

All referenced Event 016 title, option, cost, and tooltip keys exist after the description addition, and the localisation file retains a UTF-8 BOM.

## Validation evidence

- Compared the cost and factory pattern with vanilla decision precedents, including `common/decisions/GER.txt`, and checked the corresponding official trigger documentation.
- Verified the project-board gate requires a valid primary facility, so the decision and resolution use the same facility validity contract.
- Traced the current transfer and formation call sites and confirmed outcome receipts are carried once, the authorise modifier is restored, and pending reviews are re-fired only on the successor host.
- Ran `hoi4.event_inspect` lint on `chaosx.nr16.14` after the patch.
  Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/469cc9cfc4f2fc04ca74dc4a6149b374db7473832cff2f991c9f2d0494372f02/f45b433770c94a09f59d0870aec73148f2778ced2a06c505aa03dcf226f2fa0d/event-lint-5bf41c8ac88f.json`.
  The tool returned a focused partial workspace graph with no blocker but deferred workspace-wide helper projections, so it is supporting evidence rather than full-chain proof.

## Skipped validation and remaining risks

No live-game run was performed because in-game validation belongs to the user.

I did not run a probability sweep because the three event-option weights require a declared campaign-state scenario set to make a balance conclusion meaningful.

The cost localisation was left as the existing readable mixed-text string because converting its non-PP resource labels to text icons would be a presentation-only follow-up outside this narrow correctness patch.

No GUI surface is owned by this tranche, so no GUI inspection or render was needed.

No plan handoff was written because the remaining AI-weight calibration is a balance choice, not a defect requiring a broader mechanic change.
