# Event 016 Mengele active-program owner repair

Status: owner correction after the independent source re-audit on 2026-09-04.

## Finding

The initial Computation lifecycle gate accepted the broad scenario, victory, or faction identity flags as sufficient program ownership.

Those flags identify a country family but did not prove that the country still represented the current active Mengele program owner.

The older native-project bridge alias used an even broader identity trigger, so non-Computation prototypes did not share the stricter lifecycle contract.

## Correction

`brilliant_scientist_mengele_project_stage_provider_is_valid` now requires the Directorate project registry plus one exact live owner form:

- the active full German program and its full-program idea;
- the active restricted German program and its restricted-program idea;
- the Mengele civil-war laboratory state and its laboratory-state idea, before Aryan replacement;
- the victorious Mengele state and its victory-state idea, before Aryan replacement; or
- the triggerable Mengele scenario country and its scenario-state idea, provided the scenario did not select the Aryan replacement variant.

Identity flags without their corresponding active state no longer authorize paid project stages, incidents, recovery, or native prototype dispatch.

`brilliant_scientist_mengele_project_provider_is_valid` is now a thin alias of that same strict predicate, so every existing bridge family uses one owner contract.

## Files

- `common/scripted_triggers/016_mengele_project_stage_triggers.txt`
- `common/scripted_triggers/016_mengele_project_bridge_triggers.txt`
- `common/scripted_effects/016_mengele_project_stage_effects.md`

## Evidence boundary

The re-audit confirmed this source defect after the foundation commit.

The installed probability adapter still leaves the compound eligibility helper unresolved and supplies no normalized engine-selection probability; this correction therefore resolves the source authorization defect without claiming engine-complete probability evidence.
