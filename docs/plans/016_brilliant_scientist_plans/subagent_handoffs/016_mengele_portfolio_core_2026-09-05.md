# Event 016 Mengele portfolio core handoff — 2026-09-05

## Scope and changed files

This tranche extends the private Mengele stage receipt API from Computation to all fifteen existing Event 016 families without editing parent gameplay surfaces. Changed files are:

- `common/scripted_effects/016_mengele_project_stage_effects.txt`
- `common/scripted_effects/016_mengele_project_stage_effects.md`
- `common/scripted_triggers/016_mengele_project_stage_triggers.txt`
- `common/script_constants/016_mengele_project_stage_constants.txt`
- `common/scripted_effects/016_mengele_project_bridge_effects.txt`
- `common/scripted_triggers/016_mengele_project_bridge_triggers.txt`

No files were staged or committed.

## Helper interfaces

- `brilliant_scientist_mengele_initialize_project_stage_receipts`: country scope; initializes the five aligned fifteen-slot arrays and provider-owned Singularity component flags.
- `brilliant_scientist_mengele_prepare_project_index`: country scope; derives family-ID-minus-one array index.
- `brilliant_scientist_mengele_load_project_stage_quote`: country scope; loads shared Theory/Deployment/Weaponization quotes, Computation Prototype quote, duration-only Prototype rows, and `mengele_event016_stage_quote_source_gap`.
- `brilliant_scientist_mengele_begin_project_stage`: country scope; strict provider/request/predecessor/payment/quote validation, direct PP/support/fuel debit, and one receipt write.
- `brilliant_scientist_mengele_cancel_project_stage`: country scope; exact receipt snapshot, clear, and one direct refund.
- `brilliant_scientist_mengele_finish_project_stage`: country scope; exact receipt settlement, provider revalidation, output dispatch, or direct refund.
- `brilliant_scientist_mengele_grant_conventional_stage_package`: country scope; six conventional families, cumulative weaponization package, fixed Mengele source, and selector cleanup.
- `brilliant_scientist_mengele_grant_custom_stage_package`: country scope; seven custom operational families, base-first weaponization, existing custom upgrade selectors, and cleanup.
- `brilliant_scientist_mengele_apply_family_stage_output`: country scope; four completion flags and family/stage output routing. Biological Weapons and Singularity late stages expose an explicit source gap.
- `brilliant_scientist_mengele_sync_native_project_prototypes`: country scope; exact native authentication for every ordinary family.
- `brilliant_scientist_mengele_record_native_project_prototype`: country scope; private or existing native family selector adapter.
- `brilliant_scientist_mengele_record_singularity_component`: country scope; exact component authentication, six provider component receipts, and idempotent full Singularity Prototype completion.
- `brilliant_scientist_mengele_reconcile_project_availability`: retains the existing Computation presentation reconciliation.
- `brilliant_scientist_mengele_cleanup_provider_receipts`: cancels active slots across all fifteen families and preserves durable history.
- `brilliant_scientist_record_mengele_project_prototype`: bridge entry point for ordinary native projects; custom families receive the existing neutral operational API.
- `brilliant_scientist_record_mengele_singularity_component`: bridge entry point for parent Singularity component output.

The strict active-owner predicate in `brilliant_scientist_mengele_project_stage_provider_is_valid` and the thin `brilliant_scientist_mengele_project_provider_is_valid` alias were preserved exactly from commit `b0093d361f`.

## Source-proven gaps and parent call sites

The shared Event 016 cost table has no Prototype quote for Electronics, Materials, Rocketry, High Energy, Biomedical, Teleportation, Cloning, Robotics, Paleogenetics, Xenobiological Synthesis, Biological Weapons, Alien Arms, Temporal, or Singularity. The loader records duration and a quote-source gap, and begin refuses these rows without inventing tuning.

Biological Weapons and Strategic Singularity Deployment/Weaponization remain explicit output gaps because no source-proven public/native adapter exists inside the owned helper surfaces. Parent work is required to route these stages through their existing public/native adapters while retaining native project ownership and avoiding fabricated Kruger history.

Parent native project output call sites still need to set the private family/component selectors and call `brilliant_scientist_record_mengele_project_prototype` or `brilliant_scientist_record_mengele_singularity_component`. Existing native callbacks currently call the public project/Kruger adapters; this tranche does not edit those out-of-scope definitions or callbacks.

Parent decisions still need to call the generic begin/cancel/finish helpers for non-Computation families. Localisation, events, decisions, special-project definitions, and any public presentation wiring remain parent-owned.

## Validation

Required offline wiki pages, vanilla documentation, the Event 016 completion contract, closure plan, active-owner repair handoff, and existing Computation lifecycle precedent were read before editing. Read-only Event MCP inspection was run for `chaosx.nr16.1` and `chaosx.nr16.901`; both returned zero blocking diagnostics with helper/lifecycle projections deferred. Evidence artifacts were `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/db070e845973698bb0a59a23b9042fc82172a26e54ab8e7e601f33ce46eb0d5f/66ee2040bc6b6fb89739f3bbf0d8e4d16516dbd2207c61885ef3f9472d65ce3d/event-trace-3871d10caa18.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1f0318bd860f4ccab1f539488a74e66428937178e0f0c35453bc5fa88de1066b/c5548ee71b4461bf1b0853b5e43a00c610708d4b8100fe856aa356c10b47a43b/event-trace-3871d10caa18.json`.

Task-specific static validation found balanced Clausewitz braces in all five changed script files, all fifteen family IDs in request/predecessor/receipt gates, all four completion flag stages per family in output logic, exact native authentication branches including both Rocketry projects and all six Biological Weapons projects, and no unsupported comparison operators in the changed gameplay files. The game was not launched.

## Completion claim

This is a bounded reusable scripted-system tranche, not full Event 016 portfolio completion. The parent must complete decision/native callback/localisation wiring and source-proven Biological Weapons/Singularity late-stage adapters before claiming the full portfolio.
