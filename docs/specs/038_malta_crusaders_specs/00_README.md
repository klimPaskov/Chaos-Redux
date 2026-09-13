# Event 038: Malta Crusaders

## Full specification pack

This folder is the source design for Event 38, **Malta Crusaders**.

The event remains a **Minor Fire-Once** event at **Chaos level 1** because its opening is a regional Mediterranean war. It belongs to the **Formables** cluster as a **High** member. The opening release is followed by a complete Malta Crusader campaign, three Chaos evolutions, several formable and principality routes, one hidden Teutonic alliance route, one hidden Atlantis betrayal, one public world-end route, and one manual triggerable scenario.

The pack is planning only. It does not claim that gameplay script, localisation, assets, models, audio, workbook rows, or MCP evidence have been implemented.

## Binding design decisions

1. Malta is released immediately. The crusade is already active when the event fires.
2. The opening remains regional. High-Chaos pre-fire scaling increases strength and footprint without turning the first day into a global war.
3. The medieval formations are real custom unit families with their own equipment, sustainment, counters, models, animation roles, and AI use. They cannot be ordinary infantry templates with renamed battalions.
4. Malta remains a human society and uses normal civilian systems. Event-specific routing markers must not accidentally classify Malta, the Holy See, the Kingdom of God, or ordinary crusader principalities as nonhuman.
5. The public campaign exposes three persistent mechanic values: **Crusade Authority**, **Order Cohesion**, and **Sacred Legitimacy**. Supporting calculations stay hidden or qualitative.
6. The Holy See and Kingdom of God are normal focus-tree outcomes. They are not evolutions.
7. Evolution activation gives no Chaos. Only concrete outcomes use the shared Chaos pipeline.
8. The Teutonic Order and Atlantis routes are hidden. They do not appear in public Event Details, public workbook fields, or public world-end toggles.
9. Nazi racial claims and Atlantean ancestry are presented as ideology, fabrication, or propaganda. The game never treats them as scientific fact.
10. The Holy World is Event 38's public terminal route. Preparation begins at 800 or more Chaos. Terminal activation still requires 1000 or more Chaos and the event-owned world-state gates.
11. The manual **Believers vs Nonbelievers** scenario raises Chaos into World Collapse during setup, then calls the same Holy World terminal runtime as the normal route.
12. The implementation must keep one authoritative exact-state registry for all Event 38 state groups. Provisional IDs in this pack require local map inspection before use.
13. The opening, evolutions, principalities, terminal paths, and manual scenario must remain safe when tags, owners, borders, factions, and capitals differ from 1936 history.
14. The supplied event idea is the binding premise. This pack expands and corrects engine conflicts without removing its core routes.

## File map

| File | Purpose |
| --- | --- |
| `01_event_contract.md` | Classification, playable promise, lifecycle, and system boundaries |
| `02_opening_release_and_map.md` | Release transaction, provisional state groups, wars, and map validation |
| `03_malta_country_package.md` | Complete Malta political, economic, military, and AI setup |
| `04_crusade_council_mechanic.md` | Three-value management loop, order politics, relics, and UI |
| `05_custom_military_families.md` | Custom battalions, equipment, upgrades, sustainment, and provider contracts |
| `06_focus_tree_architecture.md` | Full route map, branch interaction, visibility, and focus AI direction |
| `07_decisions_missions_and_failure.md` | Decision families, objectives, Eleventh Crusade, costs, and cleanup |
| `08_principalities_and_governance.md` | Crusader states, local rule, staged integration, and country packages |
| `09_evolutions_and_prefire_scaling.md` | Evolutions I to III, MTTH, pre-fire scaling, and logging |
| `10_hidden_teutonic_order.md` | Hidden Malta, Germany, and Holy Realm alliance route |
| `11_hidden_atlantis_betrayal.md` | Atlantis betrayal, claim program, tank formations, and atrocity integration |
| `12_holy_world_terminal.md` | Public terminal preparation, continent proof, final war, and aftermath |
| `13_triggerable_scenario.md` | Manual Believers vs Nonbelievers launch contract and intensity packages |
| `14_event_chain_reactions_cross_events.md` | Popup families, regional reactions, and cross-event ownership |
| `15_ai_probability_and_balance.md` | AI plans, named probability scenarios, and balance acceptance |
| `16_chaos_deaths_condemnation_migration.md` | Shared system integrations and double-counting prevention |
| `17_assets_3d_audio_animation.md` | Full visual, sound, model, counter, and animation inventory |
| `18_super_events.md` | Super-event roles and research requirements |
| `19_achievements.md` | Achievement set, hidden achievement rules, and anti-cheese gates |
| `20_event_logs_details_catalog_localisation.md` | Event log, Event Details, workbook, cluster, scenario, and prose direction |
| `21_multiplayer_dlc_performance_cleanup.md` | Multiplayer, DLC, performance, save safety, and cleanup contracts |
| `22_scripted_architecture_and_file_map.md` | Intended script ownership, APIs, constants, targets, and file layout |
| `23_acceptance_scenarios.md` | Implementation acceptance matrix and completion evidence |
| `24_research_and_source_notes.md` | Source reading record, historical anchors, uncertainties, and bibliography |
| `25_decision_register.md` | Detailed decision and mission register |
| `26_focus_route_matrix.md` | Route-by-route focus implementation matrix |
| `27_country_package_matrix.md` | Malta, principalities, Holy See, Kingdom of God, and hidden country matrices |
| `28_balance_tuning_tables.md` | Central tuning groups and initial balance bands |
| `29_asset_requirement_matrix.md` | Requirement-to-runtime asset crosswalk |
| `30_subagent_dispatch_plan.md` | Subagent order, ownership, handoffs, and runtime limitations |
| `prompts/` | Context-complete prompts for the main coding agent and project subagents |
| `templates/` | Handoff and manifest templates |
| `validation/` | Source manifest, unresolved gates, and package checks |

## Source priority

Use this order when implementation sources disagree:

1. Explicit user corrections and the attached Event 38 brief
2. This specification pack
3. Current accepted Chaos Redux system specifications
4. Current repository implementation where it does not conflict with accepted design
5. Current installed vanilla documentation and local vanilla precedents
6. Offline Paradox wiki snapshot
7. Approved reference mods when vanilla is insufficient
8. Historical research for names, institutions, and visual grounding

## Required implementation sequence

1. Run repository and tag collision discovery.
2. Inspect the local vanilla state registry and build the exact Event 38 state collections.
3. Lock the Malta tag and country identity strategy.
4. Implement shared Event 38 constants, triggers, effects, ledgers, and setup transactions.
5. Implement the baseline event and country package.
6. Implement custom unit families and their owner-side provider contracts.
7. Implement the Crusade Council values and decisions.
8. Implement focus tree routes and principalities.
9. Implement evolutions and pre-fire scaling.
10. Implement hidden Teutonic and Atlantis routes.
11. Implement the public Holy World route and manual scenario through one terminal runtime.
12. Produce all required assets, audio, counters, portraits, and 3D packages.
13. Complete event logs, Event Details, cluster data, workbook data, and documentation.
14. Run focus, decision, country, localisation, probability, UI, technology, map, and completion audits.
15. Resolve every audit gap before changing the event status from `To Be Reworked`.

## Planning status

The planning pack contains no approved fallback. Exact state IDs, exact country carrier decisions, final numerical values, final player-facing wording, final quotes, final music, final images, and final model sources remain implementation-time evidence gates. Those gates are defined precisely so they cannot be filled by guesswork.
