# Reusable alien infantry unit system

`alien_infantry` is a shared land-unit database entry rather than a Kruger-owned or D’Rhondan-owned duplicate. Event 016, Event 019 provider 508, D’Rhondan contact, and future event packages consume the same subunit, equipment, technology, tactic, counter, entity, and sound identifiers through the source-counted contact API.

## Unit and equipment contract

Each battalion has two combat width, zero human manpower, 40 HP, 90 organisation, 0.75 recovery, 10 reconnaissance, 0.50 initiative, five suppression, and 0.04 supply consumption. It requires exactly 200 `alien_laser_weapon_equipment` and no Infantry Equipment, Support Equipment, or other ordinary equipment. The subunit has `active = no`, so a technology unlock does not expose it as a freely selectable division-designer battalion.

`alien_laser_weapon_equipment_1` is the first and only buildable variant of the `alien_laser_weapon_equipment` archetype. It provides 0.98 reliability, 6.5 km/h speed, 60 defense, 40 breakthrough, 40 percent hardness, 30 armor, 30 soft attack, 20 hard attack, 80 piercing, 10 air attack, and a 0.75 IC cost. Licensing and lend lease are disabled. Production also requires a positive source-counted contact-access trigger; possessing the hidden unit technology without contact cannot open the production line.

The public API creates the only alien template: the locked ten-battalion, twenty-width `D’Rhondan Landing Cohort`. One complete cohort requires exactly 2,000 laser weapons. Project-force reconstruction does not create, unlock recruitment for, or raise a division cap on a second template.

## Technology and tactics

`brilliant_scientist_alien_infantry_tech` is a hidden grant-only bridge that enables the laser-equipment variant. The technology may exist before contact, but the equipment production gate still requires positive contact authorization. It deliberately does not use `enable_subunits`, preserving the battalion's inactive division-designer status while the public API can still construct the locked template. `brilliant_scientist_alien_predictive_warfare_tech` depends on it and unlocks the two alien-only tactics.

`tactic_alien_predictive_vector_assault` is an attacking standard-phase tactic with base factor four. It grants 35 percent attacker combat power, reduces the defender by 15 percent, increases attacker movement by 25 percent, and increases attacker organization damage by 30 percent.

`tactic_alien_probability_screen` is a defending standard-phase tactic with base factor four. It reduces the attacker by 35 percent, grants 30 percent defender combat power, and reduces attacker organization damage by 30 percent.

Both tactics are inactive until the predictive-warfare technology unlocks them, and each trigger requires `has_unit_type = alien_infantry`. Their values deliberately exceed vanilla basic and assault tactics, but their side and standard-phase gates prevent them from applying to ordinary formations or replacing phase-owned tactics.

## Runtime identifiers

- Subunit: `alien_infantry`
- Equipment archetype: `alien_laser_weapon_equipment`
- Equipment variant: `alien_laser_weapon_equipment_1`
- Operational technology: `brilliant_scientist_alien_infantry_tech`
- Predictive-warfare technology: `brilliant_scientist_alien_predictive_warfare_tech`
- Attacker tactic: `tactic_alien_predictive_vector_assault`
- Defender tactic: `tactic_alien_probability_screen`
- Runtime entity consumer: `alien_infantry_entity`
- Public contact API: `alien_infantry_grant_contact`, `alien_infantry_revoke_contact`, `alien_infantry_can_call_landing`, `alien_infantry_spawn_landing_cohort`, and `alien_infantry_reconcile_country`
- Event 019 provider 508 uses source receipt `constant:alien_infantry_contact_source.event019_provider_508` (receipt 3), routes every spawn surface through Event 019’s ordinary unit ledger transaction, and contributes no separate training or sustainment obligation. One Event 019 request or scenario actor may materialize exactly one cohort; automatic generation narrows its selected-state target to one, and anomalous scenarios use an actor-local target so the shared scenario intensity remains unchanged for other actors. The API creates the cohort with Event 019’s allocated engine deletion ID and debits exactly 2,000 laser weapons, but defers state markers, landing history, Alien Presence, Pact Strain, cooldown, and pact callbacks until the innermost or enclosing Event 019 transaction has passed its final ledger proof. Persistent transaction receipts survive a delayed same-tag rollback retry; a failed transaction deletes that exact cohort and refunds the one proven debit only after absence is proved and before Event 019 checks the restored stockpile and ledger snapshot. D’Rhondan’s one-time sovereignty bootstrap may pass temporary `alien_infantry_initial_force_mode = 1` only with batch mode and a positive sovereignty receipt; that exact branch preserves the 2,000-laser debit and cohort materialization while suppressing pact-host telemetry and the ordinary landing callback.
- Ordinary DHR landings keep the seven-day reservation and exact 2,000-laser debit. After a successful landing, the shared API applies the highest active recovery tier: 30 days by default, 24 with `dhrondan_landing_network_enabled`, 18 with `dhrondan_descent_windows_guarded`, or 12 with `dhrondan_near_space_secured`; the sovereignty bootstrap batch never sets this cooldown. The landing decision's AI base weight is modified by the network, reserve-priority, guarded-descent, and near-space flags through `constant:alien_infantry_landing_ai` factors.

## Visual, model, and sound contract

The source declarations use stable final paths while binary production remains owned by the dedicated asset and 3D packages.

- Large counter: `gfx/interface/counters/divisions_large/unit_alien_infantry_icon.dds`, registered as `GFX_group_alien_infantry_icon` and `GFX_unit_alien_infantry_icon_medium` in `interface/alien_infantry_system.gfx`.
- Map counter: `gfx/interface/counters/divisions_small/onmap_unit_alien_infantry_icon.dds`, registered as `GFX_unit_alien_infantry_icon_medium_white`.
- Equipment icon: `gfx/interface/technologies/shared_alien_infantry/alien_laser_weapon_equipment.dds`, registered as `GFX_alien_laser_weapon_equipment_medium`.
- Operational technology icon: `gfx/interface/technologies/016_brilliant_scientist/tech_016_brilliant_scientist_alien_infantry.dds`, registered as `GFX_brilliant_scientist_alien_infantry_tech_medium`.
- Predictive-warfare technology icon: `gfx/interface/technologies/016_brilliant_scientist/tech_016_brilliant_scientist_alien_predictive_warfare.dds`, registered as `GFX_brilliant_scientist_alien_predictive_warfare_tech_medium`.
- Tactic icons: `gfx/interface/landcombat/tactics/tactic_alien_predictive_vector_assault.dds` and `gfx/interface/landcombat/tactics/tactic_alien_probability_screen.dds`, registered under matching `GFX_` names.
- KRG laser-batch decision icon: `gfx/interface/decisions/016_brilliant_scientist/decisions/decision_alien_laser_batch.dds`, registered as `GFX_decision_brilliant_scientist_krg_alien_laser_batch` in `interface/016_brilliant_scientist_kruger_state_decisions.gfx`.
- Model, material, actions, entity, synchronized sourced audio, and acceptance evidence remain in the `alien_infantry_entity` 3D-package handoff and are not substituted by this database tranche.

## Future extensions

Future events can grant their own source receipt and call the same landing API without copying the unit or production line. Additional alien doctrines may unlock new tactics or country modifiers, but they should preserve the exact battalion equipment contract, contact-gated production, inactive designer status, and single locked-template ownership boundary.
