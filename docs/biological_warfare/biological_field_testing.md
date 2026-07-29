# Ordinary Biological Prototype Field Testing

## Purpose

Anthrax, Plague, Tularemia, and Smallpox prototype rewards use one exact-facility field-test resolver.

The resolver separates operational test reliability from agent potency.

Every ordinary agent has the same 25 percent containment-accident chance.

If an accident releases material, the ordinary lifecycle applies the accepted potency hierarchy `Tularemia < Anthrax < Plague < Smallpox`; only Smallpox is the severe weapon tier.

## Exact-state contract

The special-project `iteration_output` calls the field test from `facility_state_effects`.

That native block supplies the exact project facility state and exposes the active project through `FROM`.

The resolver accepts the test only when the project owner still controls that exact state.

It does not search for enemy territory, a non-capital state, a replacement facility, or any other fallback target.

If the special project has no native facility state, the engine skips `facility_state_effects` and no release is fabricated.

The lifecycle's `field_test_release` validator independently requires the exact actor and victim event targets, supplied actor and victim proofs, current control by the victim, and actor-victim identity before accepting the accident seed.

## Outcomes

A contained test grants the agent's configured project-progress reward and records the completed-test history.

A containment accident grants the same research progress, dispatches `field_test_release` with source `field_test` and result `accident`, and records an agent-specific accident history.

The lifecycle then owns incubation, detection, intensity, deaths, contamination, medical saturation, spread, evidence, and cleanup.

Field-test material belongs to the active prototype phase.

No national payload amount is invented or debited when the engine exposes no prototype-material stock value.

## Agent potency and political effects

Accident probability is identical for all four agents.

Domestic stability, war-support, and Political Power losses increase with the accepted weapon hierarchy because the consequences of the same containment failure are more serious for stronger agents.

Doctrine can increase the physical lifecycle consequences after release.

It does not change the field-test accident chance and cannot erase evidence, deaths, contamination, medical history, or the accident record.

## Events and assets

The stable field-test event ids remain notification-only:

- Anthrax: `chaosx_bioweapon.2` and `.3`
- Plague: `chaosx_bioweapon.7` and `.8`
- Tularemia: `chaosx_bioweapon.100` and `.101`
- Smallpox: `chaosx_bioweapon.201` and `.202`

The prototype rewards use the dedicated registered sprites:

- `GFX_sp_anthrax_reward_field_testing`
- `GFX_sp_plague_reward_field_testing`
- `GFX_sp_tularemia_reward_field_testing`
- `GFX_sp_smallpox_reward_field_testing`

Their final DDS files live under `gfx/interface/special_project/rewards/biowarfare/`.

No additional icon is required for this migration.

## Future extensions

A separate human-experimentation prototype choice can connect to the atrocity and camp-evidence systems after its exact facility, victims, deaths, evidence, responsibility, and discovery contract is implemented.

It must not reuse the controlled field-test result as a free research bonus or weaken camp-system records.
