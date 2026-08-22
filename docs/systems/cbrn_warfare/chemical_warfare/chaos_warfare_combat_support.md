# Chaos Warfare: Contaminant Fire Support

## Purpose

`contaminant_firebases` is the Combat Support track of Chaos Warfare. It rewards divisions built around chemical projectors, ammunition trains, and artillery, while its later masteries make paid chemical releases substantially more destructive. It never manufactures payload, selects a target, or writes consequences outside the shared exposure pipeline.

## Adoption reward

The track grants 25% soft attack, breakthrough, and defense to chemical support companies; 20% soft attack to line artillery; 25% soft attack and 30% breakthrough to support artillery; and 15% reliability to CBRN artillery logistics. Its mastery multiplier is 16, so units built around the mapped projector and ammunition-train sub-units advance the track rapidly enough to feel like a deliberate force-design route.

## Mastery ladder

1. `livens_fire_control_cells` adds 20% offensive-delivery reliability, 25% chemical-support soft attack, 20 organization, and 25% support-artillery soft attack.
2. `counterbattery_gas_synchronization` adds 15% coordination, 30% line-artillery soft attack and breakthrough, 25% support-artillery soft attack, and 25% chemical-support defense.
3. `raid_targeting_teams` adds 15% coordination and multiplies shared-pipeline chemical operational effect by 1.35.
4. `persistent_agent_distribution` adds 20% artillery-logistics reliability, 30% line-artillery soft attack, and multiplies contamination output by 1.40.
5. `deep_contamination_fireplans` adds 30% chemical-support soft attack and breakthrough, 40% support-artillery soft attack, multiplies shared-pipeline chemical operational effect by 1.65, and multiplies contamination output by 1.80.

The operational multipliers increase disruption and downstream exposure potency only after a route has supplied its exact target, real payload debit, protection, conditions, and accepted action record. They do not lower evidence, attribution, deaths, contamination, medical load, or history.

## Implementation map

- Doctrine and mastery stats: `common/doctrines/subdoctrines/land/chaos_warfare_combat_support_subdoctrines.txt`
- Central tuning: `common/script_constants/chemical_warfare_constants.txt` and `common/script_constants/cbrn_doctrine_constants.txt`
- Shared chemical application: `common/scripted_effects/cbrn_exposure_effects.txt`
- Milestone receipts: `common/scripted_effects/cbrn_doctrine_effects.txt`
- Localisation: `localisation/english/chaosx_doctrines_l_english.yml`

## Icon

The dedicated doctrine-family asset is `gfx/interface/doctrines/icons/chaos_warfare_doctrine_style/doctrine_contaminant_fire_support.dds`, registered as `GFX_doctrine_contaminant_firebases_medium` in `interface/chaosx_doctrines.gfx`. It is not a generic or cross-type substitute.

## Engine boundary

Ordinary combat tactics do not expose the exact selected-state, payload-debit, and condition receipt required for a chemical release. The chemical tactics therefore remain fail-closed unless a future verified current-version combat receipt can satisfy the same shared contract; the doctrine's unit and paid-route rewards remain fully active.
