# Event 016 Portal Raid beachhead and factory extraction handoff

> Historical contract superseded by the 2026-08-09 documentation reconciliation: the native Portal Facility Raid is the current architecture and uses seven-day preparation, ten Command Power, sixty Teleportation Equipment, hostile-province seizure, fully supplied unit spawn, and eligible building transfer. The separate KRG biological stockpile and delivery ledger remains queued behind the optional native CBRN callback; no parallel ledger is authorized. Portal Raider counters are complete and wired, while the runtime model/entity, actions, and sounds remain rejected and unwired pending user-approved paid recovery. See `docs/events/016_brilliant_scientist/systems/portal_raider_api.md` and `docs/plans/016_brilliant_scientist_plans/016_portal_plague_documentation_reconciliation_2026-08-09.md`.

Date: 2026-08-03

## Scope

This reviewed tranche makes Kruger's Portal Facility Raid quick to use and gives a successful operation a concrete strategic result. It keeps the native raid engine as the owner of preparation, equipment reservation, cancellation, expiry, outcome selection, and raid history.

## Changed files

- `common/raids/016_brilliant_scientist_portal_raids.txt`
- `common/raids/categories/chaosx_raid_categories.txt`
- `common/scripted_triggers/016_brilliant_scientist_raid_triggers.txt`
- `common/scripted_effects/016_brilliant_scientist_raid_effects.txt`
- `common/scripted_triggers/016_brilliant_scientist_kruger_state_decision_triggers.txt`
- `common/scripted_triggers/biological_raid_triggers.txt`
- `common/units/equipment/016_brilliant_scientist_project_force_equipment.txt`
- `common/decisions/016_brilliant_scientist_kruger_state_clone_machine_decisions.txt`
- `common/decisions/016_brilliant_scientist_kruger_state_paleo_xeno_decisions.txt`
- `common/decisions/016_brilliant_scientist_kruger_state_canonical_and_exotic_decisions.txt`
- `common/decisions/016_brilliant_scientist_kruger_state_portal_temporal_decisions.txt`
- `localisation/english/chaosx_raids_l_english.yml`
- `docs/events/016_brilliant_scientist/systems/kruger_state_decisions.md`
- `docs/specs/016_brilliant_scientist_specs/README.md`
- `docs/specs/016_brilliant_scientist_specs/package_manifest.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_native_raid_integration_2026-08-03.md`

## Runtime contract

1. The Portal Facility Raid is visible after `brilliant_scientist_portal_warfare_weaponization_tech` and available to any country with an active Kruger, the existing locked `Quantum Transit Raiders` template, and the native raid equipment/unit requirements.
2. Preparation is seven days, costs ten command power, reserves one portal apparatus, and has a thirty-day target cooldown.
3. A limited success remains a facility-damage result.
4. A normal success calls `brilliant_scientist_portal_raid_establish_beachhead`, which controls `var:target_province` for the actor and creates one understrength `Portal Breach Cadre` in that province using the existing `Quantum Transit Raiders` template. The target state receives `brilliant_scientist_portal_beachhead_active` and `brilliant_scientist_portal_raid_breach_recorded` state flags for later spread and containment decisions.
5. The normal success also calls `brilliant_scientist_portal_raid_steal_factory` once. When the selected state has a factory level, the effect removes one level in priority order `arms_factory`, `industrial_complex`, then `dockyard`, and grants the same factory type to the actor as portable off-map industry. Critical success calls the effect twice, allowing up to two extracted levels without creating factories from nothing; strategic-facility-only targets still receive the landing and damage outcome without an invented factory.
6. Active Kruger hosts and the Kruger State bypass the separate Event 016 biological authority board. Native biological policy, target, staging, aircraft or formation, payload, and lifecycle checks remain the release contract; native payload ledgers are not duplicated.
7. The six bespoke Event 016 equipment archetypes accept the living-Kruger shortcut once their existing project stage is present. Suspended, damaged, and dismantled project-family locks still stop production, but separate terminal, facility, and transport-pen checks no longer block an active Kruger from opening the production line. The seven project-force batch decisions follow the same shortcut while retaining their concrete material, factory, command-power, temporal, capacity, and time costs; batch caps and one-shot commitment flags remain to prevent free-unit loops. Temporal anchor discovery also accepts an active Kruger at its target-root gate, so the temporal batch is not stranded behind a second action-board activation.

## Assets and models

No models or new art were created. The raid reuses the existing Portal Raider unit template/entity, map icon, and equipment icon. Future approved 3D work still needs generic reusable models for Portal Raiders, cloned infantry, autonomous robots, paleogenetic beasts, xenobiological assault organisms, exotic interface guards, and temporal guards; those packages remain outside this no-model tranche.

## Validation and open evidence

- Offline Effects/wiki and vanilla effects documentation were consulted for `create_unit`, `set_province_controller`, `remove_building`, and `add_offsite_building`.
- Static brace/operator/localisation-reference checks are required before commit.
- Live game parser, province landing, factory extraction, and AI-frequency evidence remain user-owned; Hearts of Iron IV was not launched by the agent.
- The separate Event 016 KRG biological stockpile ledger remains blocked on a stable native reservation/outcome/cancellation/expiry callback and was not replaced with a fallback ledger.
