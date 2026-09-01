# Event 016 final custom technology API handoff

Date: 2026-09-01.

This bounded tranche covers the neutral hidden-technology API, its query and runtime-reconciliation contract, the API documentation, the Event 016 API trigger surface, and safe tuning constants. No technology definitions, equipment or unit definitions, decisions, localisation, project-family gameplay, Event 019 files, or focus trees were edited by this tranche. No commit was created.

## Files and identifiers

Changed files are `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt`, `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.md`, `common/script_constants/016_brilliant_scientist_custom_technology_constants.txt`, and the new `common/scripted_triggers/016_brilliant_scientist_custom_technology_api_triggers.txt`.

The retained public grant effects are `chaosx_grant_custom_operational_technology_core`, `chaosx_grant_custom_operational_technology`, `chaosx_grant_custom_technology_upgrade`, and `chaosx_grant_random_custom_operational_technology`.

The new API effects are `chaosx_record_custom_operational_technology_provenance`, `chaosx_record_custom_technology_upgrade_provenance`, `chaosx_reconcile_custom_xeno_control_grants`, and `chaosx_reconcile_custom_technology_runtime`.

The new query triggers are `chaosx_custom_technology_family_is_valid`, `chaosx_custom_technology_upgrade_is_valid`, `chaosx_custom_technology_xeno_chemical_control_is_current`, `chaosx_custom_technology_xeno_neural_control_is_current`, `chaosx_custom_technology_xeno_machine_control_is_current`, `chaosx_custom_technology_xeno_researched_control_is_current`, `chaosx_custom_technology_has_xeno_control`, `chaosx_custom_operational_technology_is_unowned`, `chaosx_can_grant_custom_operational_technology`, `chaosx_can_grant_custom_technology_upgrade`, and `chaosx_custom_technology_upgrade_is_eligible`.

The constants remain under `chaosx_custom_technology_family`, `chaosx_custom_technology_upgrade`, and `chaosx_custom_technology_control`; tuning adds `random_candidate_weight`, `provenance_minimum_source`, and `provenance_stride` alongside the protected integration reinforcement value.

## Runtime contract

Operational grants accept a valid family selector, are idempotent, install the full generic package immediately, preserve the Mengele clone-program branch, and call the existing Event 016 runtime rebuild without creating Kruger project history.

Upgrade grants accept a valid upgrade selector, grant its prerequisite operational family first, and then grant the selected upgrade without orphaning the static technology dependency.

The four xenobiological controls are mutually exclusive at the public boundary; an occupied alternate makes a new control grant a no-op, while repeating the selected control remains idempotent.

`chaosx_reconcile_custom_xeno_control_grants` deterministically keeps one control in `chemical`, `neural`, `machine`, `researched` order, preferring existing Event 016 control flags and then neutral or external receipts and learned control technology. It removes stale alternate control flags, hidden control technologies, and control ideas, while retaining the chosen learned path and never touching project history, Directorate variables, facilities, or achievements.

`chaosx_reconcile_custom_technology_runtime` is the caller-facing rebuild boundary and runs the control repair before the existing full runtime package rebuild. Learned technology is not revoked when an external source disappears because the external grant ledger remains independent of project history.

The random operational pool uses equal `constant:chaosx_custom_technology_tuning.random_candidate_weight` values only for unowned families and does nothing when all seven families are owned.

`chaosx_custom_technology_upgrade_is_eligible` is the strict weighted-pool query: it requires the base to be owned or externally received, the selected upgrade to be unowned, and any control selector to pass the mutual-exclusion checks. The Event 025/Event 036 external alien-recovery upgrade pool now assigns weight only after this query, so alternate controls receive zero weight instead of being selected and falling through to Integration.

## Provenance contract

The optional numeric input is `chaosx_custom_technology_source`; omitted, zero, or negative values intentionally produce no receipt and do not block a grant.

Operational receipts append idempotently to country array `chaosx_custom_technology_operational_provenance`, and upgrade receipts append idempotently to country array `chaosx_custom_technology_upgrade_provenance`.

Each receipt is `selector * constant:chaosx_custom_technology_tuning.provenance_stride + source`, with the current stride set to `1000000` and positive source IDs expected to remain below that stride. The operational effect records the family receipt; the upgrade effect records both its prerequisite family receipt and its selected upgrade receipt. Reconciliation and runtime rebuild never clear either array.

The external alien-recovery helper maps its existing positive Event 025 or Event 036 source-event value into `chaosx_custom_technology_source` when a direct generic source input is absent. It continues to record only provenance and generic knowledge; it does not fabricate Kruger history, Directorate state, facilities, achievements, or other project state.

## Concurrent Event 025/036 preservation

The existing `chaosx_mark_external_alien_recovery_reward_consumed`, `chaosx_grant_external_alien_recovery_reward`, duplicate guards, overlap handling, integration capstone, source-event consumption flags, and protected reinforcement addition were retained. The only concurrent-extension behavior adjusted was candidate weight construction, which now calls `chaosx_custom_technology_upgrade_is_eligible` for all eleven upgrade candidates.

After this tranche, the parent replaced Event 025 constant dependencies with Event 016-owned `chaosx_custom_technology_recovery` constants. That parent follow-up is the current ownership boundary; recheck the final source for the renamed recovery constants before merge and retain the replacement.

## Validation and evidence

Required offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, and technology modding were consulted.

Vanilla `effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, `dynamic_variables_documentation.md`, `script_math_functions.md`, and `common/script_constants/documentation.md` were consulted for `set_technology`, scripted triggers and effects, arrays, random-list weights, variables, and global constants.

The required initial probability inspection completed with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c53ae24878c7abd7c69784649ce6b712cd03fc9a3c7c41dc64c2dfb15be054ef/be9f0e47e8ac8863bbd4ef0b0087b7e66c5ede856a46592240e64a06d9ebc170/probability-inspect-055e2e4f696d.json`. The adapter found eighteen candidates but reported an incomplete pool with one unresolved input, so it is source evidence rather than acceptance evidence.

The targeted technology scan completed with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6a20780d6d6d8da23002eababb6d7a2f3cbf57e45da6b660b408959504c86c74/59117efe1756ec6f76cc1adaa4db63d0bcf29f0c26f2084076f231f81664fafb/technology-scan-58a394bed282.json`. It reported the combined graph and inherited diagnostics, including 679 technologies, 18 folders, 1427 blocking diagnostics, and three unresolved items; it is not a clean Event 016 acceptance artifact.

Targeted technology explain/lint retries returned `Transport closed` after the broad scan, so no post-change targeted MCP comparison was available. The `chaosx_ai_probability_auditor` route did not produce a usable evidence artifact in this bounded turn, and no in-game launch or live consumer validation was performed.

## Risks and follow-up

The final parent-owned recovery-constant substitution must be checked for complete identifier migration before review.

The MCP technology graph diagnostics and unresolved probability adapter input remain engine-evidence limitations, not source-level proof of failure or success.

The zero-total `random_list` behavior and runtime semantics of country-scoped provenance arrays still require parent/user live validation. The arrays deliberately have no revocation path; any future revocation design must explicitly own and clear its receipts before a rebuild.
