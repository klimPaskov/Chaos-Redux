# Event 018 Stage and Registry Fixer Handoff

Date: 2026-07-12

## Scope completed

This patch repairs the mutually exclusive field-output presentation, exact scripted-localisation band boundaries, and the later cave-breach registry lifecycle. It also includes the parent-requested achievement evidence refresh calls and persistent settlement disruption latches.

## Files changed

- `common/scripted_effects/018_resources_found_effects.txt`
- `common/scripted_effects/018_resources_found_decision_effects.txt`
- `common/scripted_effects/018_resources_found_cave_effects.txt`
- `common/scripted_localisation/018_resources_found_scripted_localisation.txt`
- `docs/plans/018_resources_found_plans/subagent_handoffs/stage_registry_fixer_handoff.md`

## Gameplay surfaces and identifiers

### Field-output lifecycle

Added STATE-scope helpers:

- `resources_found_clear_field_output_stage_modifiers`
- `resources_found_normalize_field_output_stage`

`resources_found_normalize_field_output_stage` removes all six mutually exclusive output modifiers, synchronizes `resources_found_field_stage` from durable field facts, and adds exactly one presentation to an active field. Visible modifier priority is suspended, maximum shifts, local processing, primary works, completed geological appraisal, then dormant. A suspended field retains its underlying development stage so resumption restores the correct non-suspended presentation.

The normalized modifier family is:

- `resources_found_field_dormant`
- `resources_found_field_surveyed`
- `resources_found_field_operating`
- `resources_found_field_industrial`
- `resources_found_field_maximum_extraction`
- `resources_found_field_suspended`

`resources_found_refresh_field_record` now calls the normalizer after value clamping. `resources_found_suspend_field` now uses the common refresh, matching the existing resume and partial-closure paths. Exact full sealing and cave conversion reuse the stage-family clear helper, so inactive records receive no replacement field-output modifier.

Removed direct stage-modifier manipulation from these project completions because the common finalizer now owns the result:

- geological appraisal
- open primary works
- build local processing
- regulated output
- maximum shifts

### Common achievement evidence refresh

`resources_found_refresh_field_record` calls these existing STATE-scope effects after clamping and stage normalization:

- `resources_found_refresh_contract_century_qualification`
- `resources_found_refresh_dispute_achievement_evidence`

Ownership transfer latches `resources_found_dispute_owner_changed` before the former registry is removed and the new owner is bound. Control loss latches `resources_found_dispute_control_disrupted` while a dispute settlement qualification is active. Recovery does not clear either historical failure flag. No achievement file was edited.

### Later cave-breach registry conversion

`resources_found_reinforce_existing_cave_host_from_field` now:

1. saves the converting state as `resources_found_unbinding_state`
2. removes it from the recorded former owner's `resources_found_owned_fields`
3. clears the same state from `resources_found_selected_field` before active and suspended status are cleared
4. validates the former owner's remaining selection after the field becomes inactive
5. removes ordinary field-output and diplomacy state
6. transfers the state to DHO
7. records both `resources_found_recorded_owner` and `resources_found_recorded_controller` as DHO

The first-origin path still clears active status before removing the former owner registry entry. The full-seal path still clears ordinary field modifiers, makes the field inactive before selection rebuild, removes the registry entry, and only then marks permanent closure.

### Scripted-localisation boundaries

The six selected-field band helpers now use long-form `check_variable` comparisons with `compare = greater_than_or_equals` for every `band_2`, `band_3`, `band_4`, and `band_5` threshold. Exact values 20, 40, 60, and 80 therefore enter the higher band for yield, depth, safety, foreign pressure, disturbance, and breach pressure.

Changed scripted-localisation helpers:

- `GetResourcesFoundSelectedYieldBand`
- `GetResourcesFoundSelectedDepthBand`
- `GetResourcesFoundSelectedSafetyBand`
- `GetResourcesFoundSelectedPressureBand`
- `GetResourcesFoundSelectedDisturbanceBand`
- `GetResourcesFoundSelectedBreachBand`

## Before and after behavior

Before this patch, survey, operating, industrial, and maximum-extraction modifiers could remain together on one state. Suspension did not install its own output presentation through the shared lifecycle. Later cave breaches cleared active flags without removing the field from the former owner's registry and selected pointer. Exact band thresholds remained in the lower scripted-localisation band.

After this patch, every active field refresh converges on one output modifier, inactive closure and conversion paths clear the family, exact threshold values use the higher band, and later cave breaches leave no former-owner registry or selection entry.

## Focused validation

- A stage-family scan found exactly six centralized removals and six centralized additions, with zero direct field-stage modifier calls left in the project completion file.
- A boundary scan found 24 inclusive long-form comparisons and zero remaining exclusive shorthand comparisons across the six selected-field band helpers.
- A lifecycle ordering trace confirmed later-breach registry removal, selection removal, active-status clearing, DHO transfer, and DHO owner/controller recording in that order.
- The same trace confirmed that first-origin and full-seal registry ordering remains unchanged and safe.
- Refresh ordering is clamp, stage normalization, contract qualification refresh, dispute evidence refresh, maxima, scaling, and AI weights.
- The four touched script files retained balanced block depth after the combined shared-worktree edits.

## Skipped validation and risks

No live HOI4 session was run. This task requested focused static checks, and the parent remains responsible for final integration review and completion claims.

The later-breach unbind relies on the active-field invariant that `resources_found_recorded_owner` exists and points to the registry owner. That invariant is established by field initialization and ownership transfer. No fallback was added.

## Simplifications, omissions, and blockers

No simplification or fallback was used. No known blocker remains inside this patch scope.

## Skills used

- `chaos-redux-events`
- `chaos-redux-subagents`
