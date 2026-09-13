# Mengele native custom operational bridge

## Scope and ownership

`brilliant_scientist_mengele_grant_native_custom_operational_package` is a private country-scope adapter from authenticated Event 016 native Prototype history to the existing neutral seven-family operational technology API.
It serves the native callback bridge and the parent-owned post-Theory adoption helper.
It creates no project family, technology, payment, native completion, facility, incident, or public meter.

## Input, result, and defaults

Required input: temporary `mengele_event016_native_grant_family`, containing the literal Event 016 family ID from `brilliant_scientist_project_family`.
This is a separate private input, not the shared `brilliant_scientist_project_family` selector and not `mengele_event016_project_family`.
The caller must set it immediately before invocation.

Result: temporary `mengele_event016_native_operational_grant_applied`.
It starts at zero on every invocation and copies `chaosx_custom_technology_grant_applied` only after the neutral API is actually called.
An invalid provider, non-custom family, missing private Theory, missing private Prototype, or absent matching native completion produces zero and no grant.
If neutral grant eligibility rejects an otherwise authenticated call, the result remains zero.
The helper never removes existing learned technology or entitlement to report failure.

The helper requires `brilliant_scientist_mengele_project_stage_provider_is_valid = yes`.
Each selected family also requires both `mengele_event016_<family>_theory_completed` and `mengele_event016_<family>_prototype_completed`, plus the exact native completion below.
These checks read authentic history and do not create history.

## Exact mapping

| Private Event 016 family | Required native completion | Neutral operational family |
| --- | --- | --- |
| `teleportation` | `sp:sp_brilliant_scientist_quantum_transit` | `chaosx_custom_technology_family.portal` |
| `cloning` | `sp:sp_brilliant_scientist_cloning` | `chaosx_custom_technology_family.clone` |
| `robotics` | `sp:sp_brilliant_scientist_autonomous_cognition` | `chaosx_custom_technology_family.robot` |
| `paleogenetics` | `sp:sp_brilliant_scientist_paleogenetics` | `chaosx_custom_technology_family.paleogenetic` |
| `xenobiological_synthesis` | `sp:sp_brilliant_scientist_xenobiological_synthesis` | `chaosx_custom_technology_family.xenobiological` |
| `alien_arms` | `sp:sp_brilliant_scientist_alien_arms` | `chaosx_custom_technology_family.alien_infantry` |
| `temporal` | `sp:sp_brilliant_scientist_temporal_mechanics` | `chaosx_custom_technology_family.temporal` |

The mapping preserves the seven existing bridge mappings.
Conventional families, Biological Weapons, Singularity, zero, and unrelated family IDs are not custom operational grant candidates here.

## Side effects and cleanup

The chosen branch sets `chaosx_custom_technology_family`.
Immediately before its single neutral API call, it sets `chaosx_custom_technology_source = constant:mengele_event016_project_stage.provenance_mengele`.
The existing `chaosx_grant_custom_operational_technology` owns idempotent technology installation, neutral provenance, and runtime reconciliation.

The helper clears `chaosx_custom_technology_family`, `chaosx_custom_technology_source`, and its private input `mengele_event016_native_grant_family` on every exit path.
The neutral API's own result and working variables retain the neutral API's documented lifecycle.
The private result is authoritative for this invocation, including when no neutral call was made.
No stage selector, shared Kruger selector, Directorate value, provider history, native completion, event target, stockpile payment, or refund receipt is written by the extracted helper.

## Call sites and preserved bridge contract

`brilliant_scientist_record_mengele_project_prototype` first records the native private Prototype through `brilliant_scientist_mengele_record_native_project_prototype`.
Its existing public `brilliant_scientist_mengele_project_result_applied` remains copied from `mengele_event016_native_prototype_recorded`.
Only a successful private native record invokes the extracted helper with the original shared family value copied into the dedicated private input.
The neutral grant result does not overwrite the bridge's native-record result.
The bridge still clears `brilliant_scientist_project_family` and `chaosx_custom_technology_source` and refreshes dynamic modifiers at its established boundary.
The separate Singularity-component bridge is unchanged.

The parent-owned `brilliant_scientist_mengele_adopt_completed_native_after_theory` invokes the helper only after `mengele_event016_native_prototype_synced = 1`, using its saved `mengele_event016_adoption_outer_family`.
The extracted helper does not depend on private stage selectors that the native sync just cleared.
The parent preserves and restores the enclosing Theory callback's selectors and results.
This worker did not edit `016_mengele_project_stage_effects.txt`.

Example after successful native synchronization:

```txt
set_temp_variable = { mengele_event016_native_grant_family = mengele_event016_adoption_outer_family }
brilliant_scientist_mengele_grant_native_custom_operational_package = yes
```

## Tuning, assets, and migration

No tuning or AI weights changed in this extraction.
The existing family ID categories and Mengele provenance constant remain authoritative.
Seven duplicate grant bodies in the native bridge were replaced with one call site.
No new asset, localisation, category, event target, scheduler, or migration of permanent history is required.

## Reproducible source checks

Run from the repository root:

```powershell
node .tools/audit_mengele_project_adapter_contract.mjs
```

The maintained read-only check uses Node built-ins only and writes nothing.
It protects the shared provider adapter contract consumed by the Mengele programme and Event 016 neutral native project API.
Its authoritative inputs are the conventional decision triggers, project-stage effects, bridge effects, and four existing script-constant files.
It prints assertion counts and hashes to standard output, with no generated gameplay or report files.
It parses the actual bounded source blocks and fails on unsupported test syntax.

The recorded run passed 216 conventional adapter checks, five uninitialized-receipt checks, 36 five-family publication checks, and 259 seven-family grant checks.
The grant checks cover each exact mapping and provenance, missing owner/Theory/Prototype/native evidence, neutral grant failure, a non-custom family, input/custom-selector cleanup, private/shared-selector preservation, and unchanged history flags.
Neutral API success/failure and provider validity are explicit external stubs.
Actual technology grant effects, real special-project UI, runtime source-counted entitlements, native payment settlement, and engine lifecycle are not executed by this source check.

The MCP event inspection remains focused and partial with zero indexed helpers.
It cannot certify this helper's lifecycle and is not a substitute for the parent-owned full event audit.
Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cca75ebcdfaaffd7758f44e69620b7fbcecb694ae7325ab40f62e80321c45397/7fce52da95ac9a499fe73494bc4f591e2e8f85fc5752c43bfed6a4e11e505ba8/event-scan-4bccb6ec7fe1.json`.
No in-game execution or complete portfolio claim is made.

