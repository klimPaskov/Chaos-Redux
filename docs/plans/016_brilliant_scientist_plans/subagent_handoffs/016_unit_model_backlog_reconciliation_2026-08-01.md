# Event 016 unit-model backlog reconciliation handoff

## Scope

This handoff records the deferred visual package inventory requested for Event 016. It is documentation-only. No model, texture, `.asset`, `.mesh`, `.anim`, entity binding, or gameplay reference was created or changed.

## Evidence reviewed

- `common/units/016_brilliant_scientist_project_forces.txt` defines seven Event 016 project-force consumers: `kruger_portal_raider`, `kruger_clone_infantry`, `kruger_robot_frame`, `kruger_paleogenetic_beast`, `kruger_xenobiological_assault`, `kruger_exotic_guard`, and `kruger_temporal_guard`.
- `common/units/equipment/016_brilliant_scientist_project_force_equipment.txt` supplies the corresponding portal, clone, robot, paleogenetic, xenobiological, alien-arms, and temporal equipment archetypes.
- `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt` exposes Event 019 provider identities 504-508 for clone, robot, paleogenetic, xenobiological, and alien-interface families only.
- Portal-raider and temporal-guard units remain native Event 016 consumers. Their future infantry-spawn provider contracts are documented as targets, not runtime references.

## Result

`016_event19_generic_unit_family_3d_model_backlog.md` now contains seven generic packages, each with a consumer crosswalk, static fallback, future entity key, skeleton/action requirements, variants, map/runtime surfaces, and reuse boundary.

The seven deferred packages are:

1. Portal Raider — `chaosx_portal_raider_entity`.
2. Clone Infantry — `chaosx_clone_infantry_entity`.
3. Autonomous Robot — `chaosx_autonomous_robot_entity`.
4. Paleogenetic Creature — `chaosx_paleogenetic_creature_entity`.
5. Xenobiological Organism — `chaosx_xenobiological_assault_entity`.
6. Alien Interface Infantry — `chaosx_alien_interface_infantry_entity`.
7. Temporal Guard — `chaosx_temporal_guard_entity`.

Clone, robot, and alien-interface packages retain generic naming so another event can reuse them without inheriting Event 016 country identity. Creature, portal, and temporal packages use the same provider-neutral boundary. All packages retain vanilla sprite/map-icon fallbacks until the 3D workflow is explicitly commissioned.

## Validation and remaining work

- Exact consumer and equipment identifiers were checked against the current unit and Event 019 provider files.
- No gameplay surface was edited in this tranche, so no runtime wiring was introduced or left dangling.
- Future production must still follow the Meshy one-image gate, vanilla scale crosswalk, real authored animation requirement, `.mesh`/`.anim` reimport proof, static fallback, and parent-owned runtime wiring rules.
- No 3D package was produced because the current goal explicitly defers model creation.
