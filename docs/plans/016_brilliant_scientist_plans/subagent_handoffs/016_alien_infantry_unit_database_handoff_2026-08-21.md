# Alien infantry unit database handoff — 2026-08-21

## Scope and status

This tranche establishes the reusable provider-neutral `alien_infantry` unit, laser-equipment, hidden-technology, and combat-tactic contract from `016_alien_infantry_and_dhronda_addendum.md`. It does not define the locked landing template, contact decisions, Event 019 provider behavior, D’Rhondan country or focus content, the runtime entity, or binary artwork.

The source implementation is complete within the granted unit-database ownership. Mandatory HOI4 technology MCP evidence remains blocked by tool timeouts and a stale cached workspace, so this tranche must not be treated as engine-validated technology evidence.

## Public identifiers

- Subunit: `alien_infantry`
- Equipment archetype: `alien_laser_weapon_equipment`
- Equipment variant: `alien_laser_weapon_equipment_1`
- Operational technology: `brilliant_scientist_alien_infantry_tech`
- Predictive-warfare technology: `brilliant_scientist_alien_predictive_warfare_tech`
- Attacker tactic: `tactic_alien_predictive_vector_assault`
- Defender tactic: `tactic_alien_probability_screen`
- Runtime entity consumer: `alien_infantry_entity`

## Implemented contract

`alien_infantry` is inactive in the normal division designer and is not enabled through `enable_subunits`. It has two combat width, zero manpower, 40 HP, 90 organisation, 0.75 recovery, 10 reconnaissance, 0.50 initiative, five suppression, 0.04 supply consumption, and an exact need of 200 `alien_laser_weapon_equipment` per battalion with no ordinary equipment need.

`alien_laser_weapon_equipment_1` is the only buildable variant. The archetype supplies 0.98 reliability, 6.5 km/h speed, 60 defense, 40 breakthrough, 0.40 hardness, 30 armor, 30 soft attack, 20 hard attack, 80 piercing, 10 air attack, and 0.75 IC cost. Licensing and lend lease are disabled. Its `can_be_produced` block calls the provider-neutral COUNTRY trigger `alien_infantry_has_contact`, so an early hidden-technology grant cannot open a no-contact production line.

`brilliant_scientist_alien_infantry_tech` enables the laser-equipment variant without activating the battalion in the division designer. `brilliant_scientist_alien_predictive_warfare_tech` depends on it and owns both tactic unlocks through `enable_tactic`.

Both combat tactics are defined in the root `common/combat_tactics.txt`, matching the confirmed HOI4 load surface. Both have `active = no`, base factor four, `phase = no`, the correct attacker-side gate, and `has_unit_type = alien_infantry`. Predictive Vector Assault applies attacker `+0.35`, defender `-0.15`, attacker movement `+0.25`, and attacker organisation-damage modifier `+0.30`. Probability Screen applies attacker `-0.35`, defender `+0.30`, and attacker organisation-damage modifier `-0.30`.

The retired Event 016 five-battalion alien-interface template, its recruitment switch, division cap, and locking logic were removed from the project-force runtime. `brilliant_scientist_spawn_alien_arms_project_force` delegates to `alien_infantry_reconcile_country`; the public API remains the sole owner of the locked ten-battalion `D’Rhondan Landing Cohort` and its 2,000-weapon requirement.

The owned runtime consumers now use the public unit, equipment, and technology IDs: Alien Arms project completion, project-force rebuild and cleanup, achievement family recognition, KRG batch stockpile output, synchronized equipment tokens, the equipment bonus enum, technology/equipment/unit/tactic sprite declarations, and player-facing unit database localisation.

The project-force cleanup readers and public custom-technology API writers use `chaosx_custom_technology_alien_infantry_granted`, `chaosx_custom_technology_alien_predictive_warfare_granted`, and `chaosx_custom_technology_alien_infantry_operational` consistently.

## Files changed

- `common/units/016_brilliant_scientist_project_forces.txt`
- `common/units/equipment/016_brilliant_scientist_project_force_equipment.txt`
- `common/technologies/016_brilliant_scientist_project_technologies.txt`
- `common/technologies/016_brilliant_scientist_project_force_technologies.txt`
- `common/combat_tactics.txt`
- `common/script_constants/016_brilliant_scientist_project_force_constants.txt`
- `common/script_enums.txt`
- `common/synchronized_dynamic_tokens/chaosx_tokens.txt`
- `common/decisions/016_brilliant_scientist_kruger_state_canonical_and_exotic_decisions.txt`
- `common/script_constants/016_brilliant_scientist_kruger_state_decision_constants.txt`
- `common/scripted_effects/016_brilliant_scientist_project_force_effects.txt`
- `common/scripted_effects/016_brilliant_scientist_project_effects.txt`
- `common/scripted_effects/016_brilliant_scientist_kruger_state_decision_effects.txt`
- `common/scripted_effects/016_brilliant_scientist_achievement_effects.txt`
- `interface/016_brilliant_scientist_hidden_technologies.gfx`
- `interface/016_brilliant_scientist_kruger_state_decisions.gfx`
- `interface/alien_infantry_system.gfx`
- `localisation/english/016_brilliant_scientist_country_l_english.yml`
- `localisation/english/016_brilliant_scientist_projects_l_english.yml`
- `localisation/english/016_brilliant_scientist_kruger_state_decisions_l_english.yml`
- `docs/events/016_brilliant_scientist/systems/alien_infantry.md`
- `docs/events/016_brilliant_scientist/systems/projects.md`
- This handoff.

## Stable sprite and asset handoff

- `gfx/interface/counters/divisions_large/unit_alien_infantry_icon.dds` — `GFX_group_alien_infantry_icon`, `GFX_unit_alien_infantry_icon_medium`
- `gfx/interface/counters/divisions_small/onmap_unit_alien_infantry_icon.dds` — `GFX_unit_alien_infantry_icon_medium_white`
- `gfx/interface/technologies/shared_alien_infantry/alien_laser_weapon_equipment.dds` — `GFX_alien_laser_weapon_equipment_medium`
- `gfx/interface/technologies/016_brilliant_scientist/tech_016_brilliant_scientist_alien_infantry.dds` — `GFX_brilliant_scientist_alien_infantry_tech_medium`
- `gfx/interface/technologies/016_brilliant_scientist/tech_016_brilliant_scientist_alien_predictive_warfare.dds` — `GFX_brilliant_scientist_alien_predictive_warfare_tech_medium`
- `gfx/interface/landcombat/tactics/tactic_alien_predictive_vector_assault.dds` — `GFX_tactic_alien_predictive_vector_assault`
- `gfx/interface/landcombat/tactics/tactic_alien_probability_screen.dds` — `GFX_tactic_alien_probability_screen`
- `gfx/interface/decisions/016_brilliant_scientist/decisions/decision_alien_laser_batch.dds` — `GFX_decision_brilliant_scientist_krg_alien_laser_batch`

These declarations deliberately point to stable final paths without creating substitute artwork. None of the eight DDS consumers existed during this database handoff. Counter and icon production belongs to the asset package, while `alien_infantry_entity`, actions, materials, and synchronized sourced audio belong to the 3D package.

## Mandatory HOI4 MCP evidence blocker

- A refreshed `hoi4.tech_inspect` baseline call timed out at the MCP server’s 180-second limit.
- A non-refreshed inspection of `brilliant_scientist_alien_infantry_tech` returned `TECHNOLOGY_NOT_FOUND` in cached workspace `mod_chaos_redux_ea3b2d67c2c0`, demonstrating that the cache did not include the new source.
- A non-refreshed render of the new technology returned the same missing-technology result.
- A render-enabled `hoi4.tech_compare` using proposed sources timed out at 180 seconds.
- A non-refreshed render attempt against the legacy technology also timed out at 180 seconds.

Source inspection, balanced-brace checks, unique database-definition checks, localisation encoding checks, and direct contract checks were performed, but they are not substitutes for the unavailable MCP inspection, render, and comparison evidence.

## References and skills used

The implementation used the full `chaos-redux-events`, `chaos-redux-event-assets`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents` skills. Source review covered the offline wiki’s core data, trigger, effect, modifier, localisation, scope, event, decision, idea, AI, equipment, unit, division, technology, tactics, interface, and file-loading references; official vanilla script/effect/trigger/modifier/equipment documentation; and vanilla unit, equipment, technology-unlock, combat-tactic, and sprite precedents.

## Cross-owner convergence and remaining references

### KRG focus and decision convergence

The parent-owned focus pass migrated the focus, AI plan, completion-trigger, focus-sprite, and focus-localisation surfaces to `KRG_arm_the_alien_cohorts`, `GFX_goal_KRG_arm_the_alien_cohorts`, and `brilliant_scientist_focus_unlock_bounded_alien_laser_production`.

The non-focus decision path uses `brilliant_scientist_krg_fabricate_alien_laser_batch`, `brilliant_scientist_krg_alien_laser_batches`, `brilliant_scientist_krg_complete_alien_laser_batch`, `constant:brilliant_scientist_krg_capacity.alien_laser_batch_maximum`, `constant:brilliant_scientist_krg_output.alien_laser_equipment_batch`, and `GFX_decision_brilliant_scientist_krg_alien_laser_batch`. The decision requires `alien_infantry_has_contact = yes` and cancels if all contact receipts are revoked. No KRG-owned unit name remains.

### Public custom-technology API

The runtime owner migrated the grant, random-candidate, reconciliation, and companion documentation paths to `brilliant_scientist_alien_infantry_tech`, `brilliant_scientist_alien_predictive_warfare_tech`, `chaosx_custom_technology_alien_infantry_operational`, `chaosx_custom_technology_alien_infantry_granted`, and `chaosx_custom_technology_alien_predictive_warfare_granted`. The source readers, writers, and active API documentation therefore agree.

### Event 019 dependency owned by the public-API runtime owner

The provider registry, exact-equipment accounting, family-name lookups, and active registry documentation were migrated to the alien IDs while this tranche was in progress. The shared provider constant now defines `alien_laser_weapon_equipment_per_battalion = 200`, matching its migrated reader.

The last source audit found that provider 508 still created its own three-battalion alien template and retained legacy manpower, Infantry Equipment, and Support Equipment manifest charges around that template. This conflicts with the accepted single API-owned ten-battalion template and laser-only battalion contract even though it no longer exposes an old identifier. The parent assigned the full provider-508 template, payment, materialization, and cleanup migration to the public-API runtime owner; that owner’s final review remains a dependency outside this unit-database tranche.

### Documentation follow-up

Active planning, architecture, acceptance, and historical handoff documents use the current `KRG_arm_the_alien_cohorts`, `alien_infantry`, and `alien_laser_weapon_equipment` identities. Migration assertions describe the retired family without preserving obsolete runtime identifiers.

## Simplifications, omissions, and blockers

No gameplay-value simplification was made in the unit database. The required template remains with the public API, binary assets remain with the asset and 3D packages, and the KRG focus rename was completed by the parent under the focus skill and mandatory focus MCP workflow. The unavailable mandatory technology MCP evidence remains this tranche’s validation blocker. Event 019 provider 508 remains an explicit cross-owner integration dependency until the public-API runtime owner confirms the single-template, laser-only rewire. No commit was created.
