# Decision startup repair handoff

Status: implemented for the authorized decision and category-registration tranche after the Cycle 02 process stopped at the main menu. No commit was created.

## Scope and authority

This tranche repairs parser-invalid decision fields, invalid Event 021 equipment database identifiers, the Event 023 doctrine constant selector, and the missing Event 025 category registry.

The existing decision costs, custom payment gates, receipts, factory reservations, timers, effects, cleanup, visibility helpers, mission callers, and AI weights were preserved.

The required immediate backups are under docs/testing/live_qa/20260913_main_menu_startup/baseline/decisions/ using the source-relative paths.

The new common/decisions/categories/025_alien_technology_in_antarctica_categories.txt had no prior source file to archive.

## Issue list by severity

1. Critical startup parser errors: ai_hint_pp_cost = constant:... was rejected in Event 012 and Event 016 decision fields, so the affected decisions were skipped or degraded during loading.

2. Critical startup parser errors: Event 016 fallback prototype and singularity-component civilian_factory_use = constant:... fields were rejected in the native modifier surface.

3. Critical category-registration errors: all seven Event 025 category IDs were absent from common/decisions/categories, causing the phase decisions, evolution decisions, aftermath decisions, and Event 025 missions to be skipped as unknown-category children.

4. High database-reference errors: Event 021 used the invalid database objects trains, trucks, and convoys in equipment gates and stockpile effects.

5. High constant-reference error: Event 023 selected constant:sov_nuclear_bombs_doctrine.dispersed, but the authoritative key is dispersed_commands.

## Changed source and identifiers

- common/decisions/012_africa_elephant_operations_decisions.txt: africa_elephant_open_logistics_contract now uses the static alias @CR_SC_AFRICA_ELEPHANT_LOGISTICS_COMMAND_POWER_COST = 12 for its native AI hint field.

- common/decisions/016_brilliant_scientist_directorate_project_board.txt: all 15 fallback prototype rows and all 6 singularity-component rows now use file-scoped aliases for their native AI hint and civilian-factory fields.

- The Event 016 fallback aliases mirror the central prototype values 68/2, 68/2, 68/2, 75/3, 90/3, 90/2, 90/3, 98/2, 83/3, 98/2, 105/2, 120/2, 105/3, 113/3, and 150/4 in source order for computation, electronics, materials, rocketry, high-energy, biomedical, teleportation, cloning, robotics, paleogenetics, xenobiological synthesis, biological weapons, alien arms, temporal, and singularity.

- The Event 016 singularity-component aliases mirror 75/3, 80/3, 80/3, 90/3, 100/4, and 110/4 for command core, power link, containment lattice, temporal authenticator, delivery architecture, and fail-deadly governor.

- common/decisions/016_brilliant_scientist_kruger_state_clone_machine_decisions.txt: brilliant_scientist_krg_run_bounded_clone_growth_cycle now uses @CR_SC_CLONE_MATURATION_POLITICAL_POWER = 65 for its native AI hint field.

- common/decisions/016_mengele_computation_incident_decisions.txt: mengele_event016_computation_incident_recovery now uses @CR_SC_MENGELE_COMPUTATION_INCIDENT_RECOVERY_POLITICAL_POWER = 35.

- common/decisions/016_mengele_computation_stage_decisions.txt: the four computation stage decisions now use static aliases retaining the central PP values 45, 68, 90, and 135 for theory, prototype, deployment, and weaponization.

- common/decisions/016_mengele_conventional_incident_decisions.txt: the five incident recovery decisions now use static aliases retaining technical 35, industrial 50, industrial 50, exotic 75, and biological 60.

- common/decisions/016_mengele_conventional_stage_decisions.txt: the 15 conventional stage decisions now use static aliases retaining the central PP ladders for electronics 45/90/135, materials 45/90/135, rocketry 50/100/150, high energy 60/120/180, and biomedical 60/120/180.

- common/decisions/021_random_civil_war_decisions.txt: every exact plural equipment token in the gates and stockpile effects was replaced with the requested archetype train_equipment, motorized_equipment, or convoy, while all existing gate and spend constants remain unchanged.

- common/decisions/023_sov_nuclear_bombs_decisions.txt: sov_nuclear_bombs_custody_dispersed_commands now selects constant:sov_nuclear_bombs_doctrine.dispersed_commands.

- common/decisions/categories/025_alien_technology_in_antarctica_categories.txt: registered chaosx_nr25_expedition_category, chaosx_nr25_evolution_category, chaosx_nr25_outpost_emphasis_category, chaosx_nr25_cooperation_category, chaosx_nr25_countermeasure_category, chaosx_nr25_utility_category, and chaosx_nr25_analysis_category.

## Before and after behavior

Before the repair, the engine rejected the named static constant placements and invalid Event 021 database objects during startup and reported every Event 025 child as an unknown category.

After the repair, native static fields receive same-value file aliases, Event 021 gates and effects use valid equipment archetypes, Event 023 resolves the existing doctrine constant, and Event 025 child definitions have registered category owners.

The Event 016 regular cost = constant:... fields remain constant-backed where the engine accepted them.

The Event 016 custom cost triggers, custom cost text, private receipts, equipment and fuel payment paths, factory reservations, timers, completion effects, cancellation paths, and cleanup remain unchanged.

## Decision-category lifecycle notes

The Expedition Board category is visible for a participant while Event 025 is active or final recovery is resolved, remains visible when empty so its existing board entry point can render, and retains chaosx_nr25_expedition_board_scripted_gui.

The evolution category requires a participant and one of the five existing evolution global flags, matching the evolution decision visibility wrappers.

The outpost emphasis category requires the existing participant and outpost-emphasis flags.

The cooperation category requires the existing participant flag so its child phase visibility controls continue to decide which actions appear.

The countermeasure category requires the existing participant and sabotage flags.

The utility category requires the existing participant, active race, and absence of the existing terminal flag.

The analysis category requires final recovery resolution, a winner or loser settlement flag, and the existing analysis-sealed and closure exclusions.

The secondary category visibility predicates intentionally retain the child decision lifecycle instead of adding a new phase or cooldown rule.

## Cognitive-load notes

The Event 025 primary tray remains the existing six phase surface, and category registration does not add a decision or duplicate an action.

The existing Event 025 mission lane remains one phase mission at a time through its existing phase-mission flag, with nine phase mission definitions and five final-recovery mission definitions retained in their source category.

No player-facing meter, threshold, cost text, icon, tooltip, or value display was changed in this parser tranche.

The category registry restores the intended bounded trays without introducing another visible value or an extra tab.

## Mission quality notes

Event 025 owns chaosx_nr25_organize_southern_expedition_mission, chaosx_nr25_reach_gateway_mission, chaosx_nr25_establish_antarctic_outpost_mission, chaosx_nr25_triangulate_crash_zone_mission, chaosx_nr25_protect_supply_route_mission, chaosx_nr25_confirm_primary_site_mission, chaosx_nr25_evacuate_expedition_mission, chaosx_nr25_stabilize_wreck_mission, and chaosx_nr25_contain_alien_systems_mission under chaosx_nr25_expedition_category.

Its final-recovery missions are chaosx_nr25_secure_recovery_core_mission, chaosx_nr25_rapid_extraction_mission, chaosx_nr25_remote_recovery_mission, chaosx_nr25_armed_retrieval_mission, and chaosx_nr25_distributed_salvage_mission under that same registered category.

The existing mission owner, category, region and phase requirements, constant-backed durations, success effects, timeout effects, cancellation rules, and cleanup helpers were not edited.

The previously reported invalid mission IDs were downstream of the missing category registration, so their callers remain unchanged.

## Cost, requirement, and AI notes

No spendable amount was changed, and no decision gained an additional spendable cost type.

Event 016 fallback AI hint aliases and factory aliases retain the authoritative central values, while regular costs and custom payment contracts remain as authored.

Event 021 equipment gates and stockpile additions retain every existing *_gate and *_spend constant; only the database archetype token changed.

Event 025 category definitions add no cost or requirement surface.

No ai_will_do factor, probability, target pool, MTTH value, or route weight was changed, so no probability target was introduced and no probability compare was required for this syntax and registration repair.

## Localisation, cleanup, and exploit notes

No localisation file was edited.

The existing Event 025 localisation contains keys for expedition, evolution, countermeasure, and analysis, but does not currently contain category keys for outpost emphasis, cooperation, or utility; this is an unresolved parent-owned localisation gap.

No effects, triggers, timers, payment debits, cancellation paths, cooldowns, or cleanup hooks were changed.

No new free-resource path, duplicate mission lane, exploit loop, or balance shortcut was introduced.

## References consulted

The offline paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md, Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Idea modding, and AI modding pages were consulted before editing.

The installed vanilla documentation C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md, common/script_constants/documentation.md, and vanilla common/decisions/_documentation.md were consulted for constant expansion, static field support, and decision cost behavior.

Vanilla interface/decisions.gfx was consulted for the generic industry, foreign-policy, and crisis category sprites used by the new Event 025 registry.

Event 025 architecture and decision-cost specifications were consulted at docs/specs/025_alien_technology_in_antarctica_specs/specs/013_implementation_architecture.md and docs/specs/025_alien_technology_in_antarctica_specs/specs/005_decisions_missions_and_costs.md.

## Backups and validation

Pre-edit copies exist for the eight Event 012, Event 016, Event 021, and Event 023 source files at docs/testing/live_qa/20260913_main_menu_startup/baseline/decisions/common/decisions/.

Targeted post-edit scans report zero rejected ai_hint_pp_cost = constant: fields and zero rejected civilian_factory_use = constant: fields in the repaired Event 012 and Event 016 files.

Targeted post-edit scans report zero exact plural database IDs trains, trucks, or convoys in Event 021, zero stale Event 023 constant:sov_nuclear_bombs_doctrine.dispersed, and all seven Event 025 category IDs in the new registry.

Brace counts are balanced in every touched decision and category file, and field-count comparisons against the immediate backups preserve the existing cost, custom-cost, AI, completion, timer, modifier, and stockpile-effect structure.

git diff --check reported no whitespace errors for the touched source set.

No post-edit game launch was run by this subagent; the parent must generate the next fresh startup log to confirm engine loading after these repairs.

The required hoi4.gui_inspect and hoi4.gui_render evidence was not run here because this tranche registers an existing decision-owned GUI entry point without changing its layout or assets; the parent-owned GUI handoff records unresolved references, missing fonts/localisation, and a prior render timeout.

## Remaining issues and routing

The Cycle 02 log is a pre-edit baseline for this tranche, so its old malformed-field and unknown-category lines must be checked against a new post-edit launch rather than treated as current source errors.

Parent-owned errors remain in other decision, effect, trigger, database-object, localisation, and GUI surfaces reported by the fresh log.

The three missing Event 025 category localisation keys remain unresolved and need the parent localisation owner.

No simplifications, placeholders, generic branches, disabled content, balance substitutions, or unapproved fallbacks were used.
