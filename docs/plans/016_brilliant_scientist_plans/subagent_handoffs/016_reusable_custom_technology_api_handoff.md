# Event 016 reusable custom-technology API handoff

## Status

Implemented the neutral, country-scope API for all eighteen existing Event 016 custom technologies. The API is restricted to the `brilliant_scientist_*_tech` IDs already defined by Event 016 and does not grant vanilla research, project history, project stages, facilities, opening units, stockpiles, or Kruger ownership.

No Antarctic future event was added. No visual assets, models, event-localisation surfaces, or unrelated systems were changed.

## Helper map

| Helper | Scope | Inputs | Outputs | Side effects | Call sites |
| --- | --- | --- | --- | --- | --- |
| `chaosx_grant_custom_operational_technology_core` | Country | Temporary `chaosx_custom_technology_family` selector | Temporary `chaosx_custom_technology_grant_applied` | Grants one of seven base IDs and sets the matching external operational and per-tech ledger flags; no rebuild | Public operational/upgrade helpers and runtime reapply only |
| `chaosx_grant_custom_operational_technology` | Country | `chaosx_custom_technology_family = constant:chaosx_custom_technology_family.*` | Temporary applied flag | Idempotently grants one base ID, then calls the existing project-force runtime rebuild so the matching capped locked template, custom equipment gate, and provider package become usable | Intended consumer API for events, decisions, focuses, and scripted systems |
| `chaosx_grant_custom_technology_upgrade` | Country | `chaosx_custom_technology_upgrade = constant:chaosx_custom_technology_upgrade.*` | Temporary `chaosx_custom_technology_upgrade_applied` | Grants the matching base first, then one of seven weaponization IDs or four xenobiological control IDs; sets the external grant ledger and rebuilds once | Intended consumer API for dependency-safe upgrade awards |
| `chaosx_grant_random_custom_operational_technology` | Country | None | Temporary `chaosx_custom_technology_random_grant_applied` | Randomly chooses one unresearched operational family from the seven-family pool; no-op when all seven are held | Intended consumer API for generic random breakthroughs |
| `chaosx_reapply_custom_technology_grants` | Country | Durable external grant ledger flags | None | Replays only external custom technology grants after Event 016's clear; does not set project-history or Kruger flags and does not rebuild | Called by `brilliant_scientist_rebuild_project_force_runtime_package` before template/provider reconstruction |

## Eighteen-ID surface

Operational IDs: `brilliant_scientist_portal_warfare_tech`, `brilliant_scientist_clone_formations_tech`, `brilliant_scientist_robot_formations_tech`, `brilliant_scientist_paleogenetic_formations_tech`, `brilliant_scientist_xenobiological_formations_tech`, `brilliant_scientist_exotic_guard_tech`, and `brilliant_scientist_temporal_guard_tech`.

Weaponization IDs: `brilliant_scientist_portal_warfare_weaponization_tech`, `brilliant_scientist_clone_formations_weaponization_tech`, `brilliant_scientist_robot_formations_weaponization_tech`, `brilliant_scientist_paleogenetic_formations_weaponization_tech`, `brilliant_scientist_xenobiological_formations_weaponization_tech`, `brilliant_scientist_exotic_guard_weaponization_tech`, and `brilliant_scientist_temporal_guard_weaponization_tech`.

Xenobiological control IDs: `brilliant_scientist_xeno_chemical_control_tech`, `brilliant_scientist_xeno_neural_control_tech`, `brilliant_scientist_xeno_machine_control_tech`, and `brilliant_scientist_xeno_researched_control_tech`.

The seven weaponization technologies now have static dependencies on their matching operational base. The four control technologies now depend on `brilliant_scientist_xenobiological_formations_tech`. The upgrade helper grants the base before the dependent ID, so runtime awards never orphan a dependency.

## Constants and tuning

`common/script_constants/016_brilliant_scientist_custom_technology_constants.txt` owns selector values for the seven families, eleven upgrade selectors, and the random candidate weight. The selector values are not technology IDs and cannot be passed directly to `set_technology`; the API uses static branches because HOI4 requires static technology tokens in that effect.

Existing `brilliant_scientist_project_force_cap` values remain the single source for external template ceilings: portal 4, clone 8, robot 8, paleogenetic 6, xenobiological 6, exotic 4, and temporal 3. External grants do not use prototype caps or project-stage variables.

## Runtime, flags, and cleanup

External ledger flags use the neutral `chaosx_custom_technology_*` namespace. Each operational family has an `*_operational` flag and a matching `*_granted` flag; each upgrade has its own `*_granted` flag. The four control upgrades also set neutral `chaosx_custom_technology_xeno_control_*` flags. None of these flags are project-history receipts.

`brilliant_scientist_clear_project_force_runtime_package` now removes each custom technology only when its per-tech external grant flag is absent. The flags therefore survive an Event 016 clear/rebuild. Existing runtime revocation still zeroes caps and disables recruiting before reconstruction. There is intentionally no automatic external-revocation helper; a future design must clear its own ledger flags and call the normal rebuild.

No event targets are required. The grant ledger is country-scoped and persistent, while the existing runtime rebuild is the single reconstruction boundary. This avoids global event-target cleanup and keeps project history separate from external knowledge.

External operational flags extend the existing seven template creation/cap branches, six custom-equipment `can_be_produced` gates, Event 019 provider registration, and Event 019 provider-unlocked triggers. Suspended, damaged, and dismantled-family locks remain active. External grants bypass only project-stage, facility, and Kruger-owner gates, so the matching package is immediately usable by a recipient country.

## Migration plan

1. Future event/decision/focus callers set one documented selector and call the public operational or upgrade helper.
2. Future generic breakthrough callers call the random helper; no caller should duplicate the seven-family pool or call `set_technology` directly.
3. Existing Event 016 history grants remain in `brilliant_scientist_rebuild_project_force_runtime_package` and `016_brilliant_scientist_project_effects.txt`; they continue to set internal history flags and ideas exactly as before.
4. If future code needs to inspect external knowledge, use the neutral `chaosx_custom_technology_*_operational` or per-tech `*_granted` flags. Do not infer project ownership from them.

## Files changed

- `common/script_constants/016_brilliant_scientist_custom_technology_constants.txt`
- `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt`
- `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.md`
- `common/scripted_effects/016_brilliant_scientist_project_force_effects.txt`
- `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt`
- `common/scripted_triggers/016_brilliant_scientist_project_force_event19_triggers.txt`
- `common/technologies/016_brilliant_scientist_project_force_technologies.txt`
- `common/technologies/016_brilliant_scientist_project_technologies.txt`
- `common/units/equipment/016_brilliant_scientist_project_force_equipment.txt`

## Evidence and validation

- Offline Paradox wiki pages consulted: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Technology modding, Equipment modding, Division modding, and Unit modding.
- Vanilla documentation consulted: `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, `documentation/script_concept_documentation.md`, `documentation/dynamic_variables_documentation.md`, and `common/script_constants/documentation.md`.
- Read-only `hoi4.tech_inspect` scan evidence: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0c1c9b8f.../78bb4a56.../technology-scan-733bcf69c1ea.json`.
- Post-change read-only `hoi4.tech_inspect` lint artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4357e8e47e8386e791e6b6ebfed9c522f710787413c74e01e8ae9255909b2fc1/fb555d3d37b9499946a1ef20db55759a5bd10e2c23d7620d4ed6be2b73cdd2a6/technology-lint-de7a9975dae6.json`.
- Post-change dependency explain artifact for portal weaponization: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/da8934f9ec478c4fba02595a578af7afd35b7c92a645548870a447f4789f0d56/957dbf54d118923152de572d47a0aaf02fef7f479971dca477f5af35d815b594/technology-explain-de7a9975dae6.json`.
- Local structural check: brace deltas are zero for all eight touched script/technology/constant files; the API contains exactly eighteen distinct technology IDs and no non-Event-016 `set_technology` target.

The MCP technology reports are partial because helper projections were deferred for this large workspace; they provide linked graph evidence but not a clean helper-level pass/fail. In-game execution remains parent/user validation and was not launched by this subagent.

## Risks and limitations

- Provider rows retain their existing Event 016 generic registry identity and Event 019 source metadata; only unlock/registration eligibility is externalized. This preserves provider idempotence and neutral naming but should be reviewed if a future provider needs a distinct provenance record.
- External xeno operational knowledge bypasses the existing internal exact-control-mode gate for custom equipment production. Control upgrades still grant their own hidden modifiers and neutral flags, but an operational grant alone is deliberately immediately usable per the Event 016 API requirement.
- The existing generic registry may still impose its own downstream capacity, sustainment, or scenario restrictions; those are outside this narrow API and should be audited if a new consumer reports a provider mismatch.
