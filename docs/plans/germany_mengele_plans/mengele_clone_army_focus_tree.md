# Army of Clones Focus Tree

## Overview

The Army of Clones scenario country receives its own focus tree when the triggerable scenario creates the dynamic country. The tree is not assigned through a normal history tag, because the country is created at runtime from Germany. `triggerable_scenario_setup_clone_country` loads `mengele_clone_army_focus_tree` immediately after the scenario flag and cosmetic tag are assigned.

The tree is split into four connected branches:

- Biowarfare facilities and projects: builds biowarfare facilities in the clone army's controlled German/Polish core corridor, grants biowarfare breakthrough progress, and uses the Directorate special-project registry to make hidden special projects available for research.
- Clone army expansion: expands growth vats, lowers clone deployment command-power costs, unlocks assault and guard clone deployment decisions, strengthens manpower replacement, infantry equipment, officer cadres, conditioning, and selected genius cohorts.
- Directorate state policy: builds the logistics grid, unlocks biowarfare trial decisions, strengthens the Aryan variant route, and leads into the final numbered-state capstone.
- Heartland and world-dominance path: after `MCL_the_numbered_future`, gives the Directorate a German-Polish reclamation branch. Once all German and Polish core states are owned, controlled, and cored by the Directorate, a separate expansion branch opens for western, eastern, and southern continental campaigns.
- Clone world-order path: after the Directorate becomes a major and chaos is high, builds a hidden foreign cloning network through deniable aid offers and culminates in the world-end focus `MCL_the_numbered_world`.

## Runtime Flow

1. The triggerable scenario creates a dynamic country from Germany.
2. `triggerable_scenario_setup_clone_country` sets `mengele_clone_army_scenario_country`, applies the Army of Clones cosmetic tag, and loads `mengele_clone_army_focus_tree`.
3. The focus tree unlocks national spirits and decision flags as it progresses.
4. The same tree remains available to the victorious Angelic Directorate after the Mengele chain consolidates Germany.
5. The `mengele_clone_army_category` decision category appears for clone Directorate countries with unlocked clone or hidden-network decisions.
6. Focus-unlocked decisions provide repeatable clone-vat expansion, clone infantry waves, assault-pattern clone waves, guard-pattern clone waves, temporary conditioning, genius selection, biowarfare trial work, clone immunity hardening, heartland integration, continental assault preparation, borderland command integration, hidden foreign aid missions, deeper foreign tank networks, and activation-ledger refreshes.
7. The final world-order focus activates foreign facilities, creates clone client regimes, spawns clone divisions, and triggers the Angelic Directorate world-end scenario when all rank, chaos, and network conditions are met.

## Late World-Order Branch

The late branch begins after `MCL_the_numbered_future`:

- `MCL_foreign_aid_fronts` unlocks deniable foreign aid missions.
- `MCL_embassy_science_cells` adds the foreign science-front idea.
- `MCL_hidden_tank_consortia` unlocks deeper hidden-tank network expansion.
- `MCL_directorate_project_registry` calls the Directorate special-project availability registry.
- `MCL_global_replacement_maps` unlocks the activation ledger and refreshes the final ranking check.
- `MCL_the_numbered_world` launches the world-end activation if the Directorate is a major, chaos is above the world-end threshold, the hidden network is large enough, and the Directorate is top three industrially or militarily.

Foreign host acceptance is event-driven and weighted toward countries under pressure. Accepted countries receive hidden markers but are not puppeted until the final launch.

`make_random_directorate_special_project_researchable` and `make_all_directorate_special_projects_researchable` are the update points for future Directorate special-project access. Add future clone, replication, biomedical, or biowarfare projects to those effects and to the matching project `visible` or `available` gates when new special projects enter the mod.

## Clone Deployment Branch

The clone deployment branch now has separate focus gates for deployment cost control and formation variety:

- `MCL_batch_accounting_offices` reduces the command-power cost of clone deployment decisions from `25` to `20`.
- `MCL_assault_clone_series` unlocks `raise_clone_assault_wave`, which deploys larger assault-pattern infantry-only clone divisions.
- `MCL_guard_clone_series` unlocks `raise_clone_guard_wave`, which deploys elite guard-pattern infantry-only clone divisions.
- `MCL_deployment_ledger_automation` reduces clone deployment decisions to `15` command power and is required before `MCL_numbered_legions`.

The visible decision cost is produced through `mengele_clone_deployment_command_power_cost` and `[This.GetMengeleCloneDeploymentCommandPowerCost]`; the actual spend is centralized in `mengele_clone_army_spend_clone_deployment_command_power`, so future clone deployment decisions can share the same discount path.

## Heartland And Expansion Branch

The conventional expansion branch begins after `MCL_the_numbered_future`:

- `MCL_reclamation_war_cabinet` unlocks heartland integration decisions, claims German and Polish core states, and creates war goals against countries holding those core states.
- `MCL_number_the_old_heartland` requires the Directorate to own and control all German and Polish core states. It cores those states for the Directorate and fortifies the reclaimed industrial corridor.
- `MCL_continental_dominance_protocol` requires the German-Polish heartland to be both controlled and cored. It unlocks continental assault and borderland command decisions.
- `MCL_rhine_specimen_corridor` and `MCL_channel_replacement_ports` target western command states and core reclaimed western holdings.
- `MCL_eastern_laboratory_march` and `MCL_moscow_numbering_office` target eastern command states and core reclaimed eastern holdings.
- `MCL_danubian_replacement_zone` and `MCL_mediterranean_growth_axis` target southern command states and core reclaimed southern holdings.
- `MCL_continental_command_spine` merges the three continental commands, cores eligible owned borderland states, and strengthens the clone army command structure.
- `MCL_assert_world_dominance` requires the Directorate to be a major with the German-Polish heartland still controlled and cored. It grants the final conventional dominance idea, allows same-ideology declarations, and creates war goals against remaining major powers that can be targeted.

The heartland gate is implemented through `mengele_clone_army_controls_german_polish_heartland` and `mengele_clone_army_controls_and_cores_german_polish_heartland`. Those triggers use the live German and Polish core-state sets rather than a duplicated state list, so future state file changes are automatically respected.

## Key Files

- `common/national_focus/germany_mengele_clone_army.txt`
- `common/decisions/categories/germany_mengele_categories.txt`
- `common/decisions/germany_mengele_decisions.txt`
- `common/ideas/germany_mengele_ideas.txt`
- `common/scripted_effects/germany_mengele_effects.txt`
- `common/scripted_triggers/germany_mengele_triggers.txt`
- `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt`
- `common/special_projects/projects/zombie_weaponized_projects.txt`
- `common/special_projects/projects/mengele_cloning_projects.txt`
- `localisation/english/germany_mengele_l_english.yml`

## Tuning

Focus and decision values are centralized in:

- `mengele_clone_focus_int`
- `mengele_clone_focus_value`
- `mengele_clone_decision`
- `mengele_clone_decision_value`
- `mengele_clone_decision_ai`

The focus tree keeps local `@mcl_focus_cost_*` values for focus duration because national focus cost is a static layout field and the values are only used inside the focus tree file.

## Assets

Most focus-tree nodes use vanilla focus icons directly, and standard clone army decisions use existing vanilla or Chaos Redux decision sprites:

- `GFX_goal_generic_secret_weapon`
- `GFX_goal_generic_scientific_exchange`
- `GFX_goal_generic_construct_mil_factory`
- `GFX_goal_generic_construct_civ_factory`
- `GFX_goal_generic_army_doctrines`
- `GFX_goal_generic_major_war`
- `GFX_focus_generic_population_growth`
- `GFX_focus_generic_military_academy`
- `GFX_focus_generic_cryptologic_bomb`
- `GFX_decision_generic_construction`
- `GFX_decision_generic_industry`
- `GFX_decision_generic_research`
- `GFX_decision_deploy_field_hospitals`
- `GFX_decision_generic_military`
- `GFX_decision_generic_political_discourse`
- `GFX_decision_category_chaos_doom`

The clone world-order branch adds dedicated final assets:

- `GFX_focus_mengele_numbered_world` -> `gfx/interface/goals/focus_mengele_numbered_world.dds`
- `GFX_decision_mengele_hidden_clone_network` -> `gfx/interface/decisions/decision_mengele_hidden_clone_network.dds`
- `GFX_idea_mengele_clone_world_order` -> `gfx/interface/ideas/idea_mengele_clone_world_order.dds`
- `GFX_idea_mengele_clone_client_state` -> `gfx/interface/ideas/idea_mengele_clone_client_state.dds`
- `GFX_idea_mengele_artificial_army_crisis` -> `gfx/interface/ideas/idea_mengele_artificial_army_crisis.dds`
- `GFX_sp_mengele_cloning` -> `gfx/interface/special_project/project_icons/sp_mengele_cloning.dds`
- `GFX_super_event_angelic_world_order` -> `gfx/super_events/super_event_angelic_world_order.dds`

The world-order package is documented in `docs/assets/mengele_clone_world_order/manifest.md`; the artificial army crisis icon is documented in `docs/assets/mengele_artificial_army_crisis/manifest.md`; the cloning special-project icon is documented in `docs/assets/mengele_cloning_special_project/manifest.md`.

## Future Plans

- Add bespoke focus icons for clone vats and genius cohorts if a later art pass wants stronger visual identity.
- Add focus-branch events for clone laboratory breakthroughs once the scenario country has more bespoke narrative content.
- Add AI strategy tuning if long live-session tests show the scenario country choosing too much research before stabilizing its frontline.
