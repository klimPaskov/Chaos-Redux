# Event 016 Generic Unit Identifier Migration Handoff

Date: 2026-09-01

Owner: `event016_generic_ids_retry`

Status: Complete within the bounded tranche 2 identifier-migration scope.

## Result

The Event 016 paleogenetic, xenobiological, and temporal unit families now use generic gameplay identifiers across their definitions and all consumers discovered by the repository-wide exact-token inventory.

| Retired identifier | Generic identifier |
|---|---|
| Event-specific paleogenetic battalion ID | `paleogenetic_creature` |
| Event-specific paleogenetic equipment archetype | `paleogenetic_creature_equipment` |
| Event-specific xenobiological battalion ID | `xenobiological_assault_organism` |
| Event-specific xenobiological equipment archetype | `xenobiological_assault_organism_equipment` |
| Event-specific temporal battalion ID | `temporal_guard` |
| Event-specific temporal equipment archetype | `temporal_guard_equipment` |

Concrete equipment identifiers inherited the same migration, including `paleogenetic_creature_equipment_1`, `xenobiological_assault_organism_equipment_1`, and `temporal_guard_equipment_1`.

## Files changed

### Gameplay definitions and consumers

- `common/decisions/016_brilliant_scientist_kruger_state_paleo_xeno_decisions.txt`
- `common/ideas/016_brilliant_scientist_project_force_ideas.txt`
- `common/on_actions/016_brilliant_scientist_achievement_on_actions.txt`
- `common/script_constants/016_brilliant_scientist_project_force_constants.txt`
- `common/script_enums.txt`
- `common/scripted_effects/016_brilliant_scientist_achievement_effects.txt`
- `common/scripted_effects/016_brilliant_scientist_kruger_state_decision_effects.txt`
- `common/scripted_effects/016_brilliant_scientist_project_force_effects.txt`
- `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt`
- `common/scripted_effects/chaosx_test_country_stockpile_effects.txt`
- `common/scripted_effects/chaosx_test_country_unit_effects.txt`
- `common/synchronized_dynamic_tokens/chaosx_tokens.txt`
- `common/technologies/016_brilliant_scientist_project_force_technologies.txt`
- `common/technologies/016_brilliant_scientist_project_technologies.txt`
- `common/units/016_brilliant_scientist_project_forces.txt`
- `common/units/equipment/016_brilliant_scientist_project_force_equipment.txt`
- `localisation/english/016_brilliant_scientist_country_l_english.yml`
- `localisation/english/019_infrantry_spawn_l_english.yml`

### Documentation, integration records, and manifests

- `docs/events/019_infantry_spawn/systems/unit_family_coverage.md`
- `docs/plans/016_brilliant_scientist_plans/016_core_runtime_handoff_map.md`
- `docs/plans/016_brilliant_scientist_plans/016_event19_generic_unit_family_3d_model_backlog.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_event19_portal_temporal_provider_extension_2026-08-03.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_event19_provider_isolation_audit_2026-08-03.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_event19_provider_localisation_audit_2026-08-03.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_project_force_equipment_loader_and_causality_2026-08-02.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_project_reuse_identifier_map.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_unit_model_backlog_reconciliation_2026-08-01.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/paleogenetic_creature_meshy7_handoff_2026-08-27.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/temporal_guard_meshy7_handoff_2026-08-27.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/xenobiological_assault_meshy7_handoff_2026-08-27.md`
- `docs/specs/042_equipment_from_heavens_specs/research/042_equipment_from_heavens_repository_findings.md`
- `docs/specs/042_equipment_from_heavens_specs/research/042_equipment_from_heavens_special_equipment_audit_matrix.md`
- `docs/specs/042_equipment_from_heavens_specs/specs/042_equipment_from_heavens_spec_part_3_evolutions_and_integrations.md`
- `docs/systems/cbrn_warfare/chaos_unit_family_registry.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_final_generic_unit_identifier_migration_2026-09-01.md`

## Consumer coverage

- Unit and equipment definitions, technology unlocks, sub-unit modifiers, ideas, decisions, achievement accounting, stockpile effects, equipment variables, dynamic tokens, script enums, and player-facing localisation keys use the generic identifiers.
- The CXT setup package unlocks and instantiates the generic sub-units and stocks the generic concrete equipment types.
- The Event 019 adapter uses the generic sub-units in templates, the generic concrete equipment in affordability and payment effects, the generic synchronized tokens in provider publication, and generic family localisation references.
- Project-force script constant field names were migrated where the retired equipment identifiers formed part of a constant key, and all in-scope callers were updated with them.
- No GFX source edit was required because the inspected sprite identifiers were already generic or belonged to the broader Brilliant Scientist and Kruger Directorate display families. Exact scans of `.gfx`, `.asset`, and `.gui` files found no retired identifiers before or after the migration.
- No model geometry, animation, material, entity, or binary asset was modified.

## Validation evidence

- A repository-wide exact-token scan, including hidden non-Git files, found zero occurrences of all six retired identifiers after the edit.
- A repository-wide filename scan found zero paths containing any retired identifier.
- Each of the three generic sub-unit identifiers has exactly one definition in `common/units/016_brilliant_scientist_project_forces.txt`.
- Each of the three generic equipment archetypes and each matching `_1` concrete equipment identifier has exactly one definition in `common/units/equipment/016_brilliant_scientist_project_force_equipment.txt`.
- Each generic equipment archetype and concrete equipment identifier has exactly one `script_enum_equipment_bonus_type` entry, and each concrete equipment identifier has exactly one synchronized dynamic token entry.
- Each generic sub-unit, equipment archetype, and concrete equipment identifier has exactly one base English localisation key.
- The two edited localisation files retain UTF-8 BOM encoding and decode as strict UTF-8.
- CXT inspection confirmed generic sub-unit unlocks and division-template rows plus generic concrete-equipment stockpile entries.
- Event 019 inspection confirmed generic template rows, equipment variables, synchronized token publication, stockpile costs and refunds, and family display-key references.
- HOI4 MCP pre-change unlock inspection accepted all six retired targets with `TECH_INSPECTED` in workspace `mod_chaos_redux_ea3b2d67c2c0`.
- HOI4 MCP post-change unlock inspection accepted all six generic targets with `TECH_INSPECTED` at technology graph revision `1ebacb793e4e33f39c0732a2411e7ae2e6a0474ae10a717183e132b5fcee06f7` and graph hash `6ebd7b4fcdb0e2ffd0c29fb1b49604b5155f5336e1c805d20970ccc50d5bec50`.
- HOI4 MCP post-change tracing of `chaosx.nr016.1` returned `EVENT_INSPECTED_PARTIAL` without a tool blocker at event graph revision `3d4d1503eea170d5726ebd4bc8d78f7284ec53439d7e518957fff586d3ed1741` and graph hash `1cd2e09ea7a0edb7ac45e4be12d05844197d1df3f9467c8975a75fdb821e4a7e`.
- Explicit technology and event comparison calls were attempted after the edit. The MCP rejected both because no explicit cached revision or graph artifact was supplied, returning `TECH_COMPARISON_BASELINE_REQUIRED` and `EVENT_COMPARISON_BASELINE_REQUIRED`. The successful before and after target inspections and the repository-wide exact-token inventory provide the migration evidence instead.

## Intentional remnants

- No exact retired identifier remains in gameplay, localisation, documentation, manifests, or historical handoffs.
- Event-owned display names such as Paleogenetic Shock Pack, Xenobiological Assault Organisms, Temporal Continuity Guard, and their existing abbreviations remain because they are player-facing names rather than gameplay identifiers.
- Doctor Kruger, the Kruger Directorate, `KRG`, `brilliant_scientist_paleogenetics`, related project identifiers, file names, flags, scripted effects, and GFX identifiers remain because they identify the character, country, event route, or project family rather than one of the six migrated gameplay identifiers.
- Existing generic 3D package, entity, and animation identifiers remain unchanged. The migration did not rename or regenerate any model asset.

## Concurrent ownership and conflicts

- The working tree contained extensive concurrent edits, including work in Event 016 API surfaces. This tranche made only exact identifier replacements in the files listed above and preserved all surrounding content.
- `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt`, `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.md`, the API architect's trigger file, and `common/script_constants/016_brilliant_scientist_custom_technology_constants.txt` were not edited by this tranche.
- The final repository scan observed generic identifiers in the protected API files and no retired identifiers there. Those lines belong to the parallel API architect and are not included in this handoff's changed-file inventory.
- No conflicting old-to-new mapping was discovered.

## Risks and parent follow-up

- The parent should repeat the six-token repository scan after every parallel Event 016 worker has stopped because the protected API surfaces were still under concurrent ownership during this pass.
- The MCP comparison commands could not construct an implicit before-and-after baseline. If artifact-level visual comparison is required, the parent must supply an explicit cached revision or graph artifact to the comparison tools.
- No balance value, AI weight, route condition, model geometry, asset registration, or player-facing display name was changed.

## Simplifications, omissions, and blockers

No gameplay, localisation, documentation, CXT, Event 019, enum, token, or GFX consumer carrying an exact retired identifier was omitted.

The only validation limitation was the MCP comparison baseline requirement documented above.
