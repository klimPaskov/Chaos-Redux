# CBRN commander progression effects

`cbrn_commander_record_completed_hq_operation` runs in the exact CBRN HQ commander's character scope after the final successful, paid upkeep tick of a bounded active order.
It requires `cbrn_hq_upkeep_ticks_remaining = 0`, the matching persistent `cbrn_hq_operation_code` and active status trait, an assigned corps commander, and no `cbrn_hq_command_completion_recorded` flag.
The shared HQ starter must clear that flag when a new operation is validly committed.
The effect sets the flag before crediting service, so an accidental duplicate callback cannot credit the same operation twice.

Decontamination Corridor credits `cbrn_chemical_operations_completed`.
Mass Antidote Response and Seal Infection Corridor credit `cbrn_biological_operations_completed`.
Decontamination Corridor, Seal Operational Area, and Seal Infection Corridor credit `cbrn_containment_operations_completed`.
Failed upkeep, cancellation, and preparation completion grant no service credit.
The thresholds live in `common/script_constants/cbrn_commander_progression_constants.txt` and counts stop at those thresholds.

`cbrn_commander_record_protected_combat_victory` runs in the winning army leader's character scope from `on_army_leader_won_combat`.
It requires an assigned corps commander who commands at least one `cbrn_gas_mask_decon_detachment` when the combat is won.
It increments the capped `cbrn_protected_combat_victories` counter; it does not assert that a particular protected division fought in the battle.

`cbrn_commander_refresh_earned_traits` runs in character scope after a completed HQ receipt.
It grants Chemical Operations Commander at the chemical threshold, Biological Operations Veteran at the biological threshold, and Hazard Warfare Veteran when that commander has both.
Protected Assault Expert and Theatre Containment Organizer use vanilla general and field marshal assignable slots, respectively, with service prerequisites checked in `common/scripted_triggers/cbrn_commander_progression_triggers.txt`.

Example final-upkeep call in `cbrn_hq.2`, inside `event_target:cbrn_hq_commander` after a successful debit and `cbrn_hq_complete_upkeep_tick`:

```text
cbrn_commander_record_completed_hq_operation = yes
```

The native raid outcome context identifies its actor country and target state but exposes no documented participating army leader.
Its completed results therefore cannot be assigned to a random leader as personal service credit.

## Trait icons

`interface/chaosx_traits.gfx` registers `GFX_trait_chemical_operations_commander` and the four new CBRN trait sprites.
The new DDS files belong under `gfx/interface/traits/cbrn/` with basename `trait_<trait id>.dds`.
The native High Command role uses the existing commander's portrait and adds no new card or portrait asset.

## Future plans

If the raid engine later exposes a documented participating army leader, credit that exact character from completed land raid outcomes and retain the HQ and combat receipts as distinct service sources.
An explicit CBRN HQ to raid binding could also provide a verifiable commander link, but it must not infer one from country ownership alone.
