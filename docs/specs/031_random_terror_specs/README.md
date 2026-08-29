# Event 31 Random Terror planning package

## Purpose

This package is the source specification for Event 31, Random Terror.

It expands the supplied event brief into a complete event system with a compact national response loop, repeatable incidents, five evolutions, territorial extremist countries, a shared country focus framework, the Global Jihad manual scenario, the public world-end branch The False Revelation, cross-event behavior, AI requirements, asset inventories, achievement criteria, and implementation prompts.

The package plans design and implementation requirements. It does not contain Clausewitz code or final player-facing localisation.

## Core design decision

Event 31 begins as a global repeatable security crisis that can affect several countries in one firing.

Each affected country manages one primary visible value, Terror Pressure, and one supporting value, Response Legitimacy.

Active state modifiers show where cells are operating and how entrenched they are.

The ordinary response remains compact. The player normally sees three to five relevant actions and no more than three active missions.

Deeper content appears only when the crisis escalates. Territorial actors, focus trees, transnational coordination, foreign fighters, faction behavior, and world-end content do not crowd the early response surface.

## Representation rule

Every organization created by Event 31 is fictional.

The event does not associate terrorism with any religion, nationality, civilization, ethnicity, or ordinary political ideology.

Evolution IV introduces one fictional jihadist movement as a specific extremist branch.

Muslim communities, clerics, soldiers, and governments can become its main opponents.

The movement treats many Muslim governments as priority enemies because it calls them illegitimate.

The event never treats ordinary Muslims as members, sympathizers, recruits, or security risks by default.

The False Revelation never confirms that its entity is Allah.

No asset may depict Allah, use Quranic calligraphy as villain branding, use a real extremist symbol, or use sacred Islamic audio as an enemy cue.

## Package map

1. `031_random_terror_spec_part_1_event_identity_and_player_loop.md` defines event identity, pacing, values, stages, multiplayer behavior, and player experience.
2. `031_random_terror_spec_part_2_targeting_and_incident_engine.md` defines country selection, state selection, incident families, spread, cooldowns, deaths, damage, and cleanup.
3. `031_random_terror_spec_part_3_government_response_decisions_and_missions.md` defines the compact response category, decisions, missions, costs, outcomes, foreign help, and exploit controls.
4. `031_random_terror_spec_part_4_evolutions_and_escalation.md` defines the five evolution tracks, active-event pacing, evolved opening behavior, and log requirements.
5. `031_random_terror_spec_part_5_territorial_insurgency_and_country_packages.md` defines territorial seizure, country creation, force packages, technology, economy, leaders, flags, and defeat outcomes.
6. `031_random_terror_spec_part_6_focus_tree_and_political_routes.md` defines the shared extremist-country focus architecture, idea lifecycles, route interaction, AI, and branch payoffs.
7. `031_random_terror_spec_part_7_global_jihad_scenario.md` defines the proposed `SCN-014` manual scenario, deployment types, four intensities, setup isolation, and acceptance cases.
8. `031_random_terror_spec_part_8_false_revelation_world_end.md` defines the public terminal branch, readiness, unification, campaign phases, counterplay, presentation, and defeat aftermath.
9. `031_random_terror_spec_part_9_ai_balance_probability.md` defines government AI, extremist AI, target priorities, evolution pacing, probability scenarios, and balance constraints.
10. `031_random_terror_spec_part_10_cross_event_system_interactions.md` defines interactions with Cannibalism, Random Civil War, world threats, Deaths, Condemnation, disasters, disease, and country registries.
11. `031_random_terror_spec_part_11_assets_presentation_and_localisation.md` defines every visual family, portrait classification, flags, report and news art, super-event direction, animation, and writing direction.
12. `031_random_terror_spec_part_12_achievements.md` defines the event achievement package and disqualifiers.
13. `031_random_terror_spec_part_13_documentation_catalog_and_acceptance.md` defines event logs, Event Details, catalog updates, technical identifiers, documentation, validation, and completion evidence.
14. `031_random_terror_decision_mission_matrix.md` is the detailed action and mission matrix.
15. `031_random_terror_country_package_matrix.md` is the detailed country package matrix.
16. `031_random_terror_ai_scenario_matrix.md` is the detailed probability and AI scenario contract.
17. `031_random_terror_research_notes.md` records external research and the design conclusions drawn from it.
18. `031_random_terror_improvement_loop_review.md` records the manual near-completion improvement pass and its anti-bloat decisions.
19. `031_random_terror_source_audit_and_limitations.md` records supplied-source coverage and unavailable implementation evidence.
20. `031_random_terror_asset_prompt.md` is the context-complete visual production prompt.
21. `031_random_terror_super_event_prompt.md` is the context-complete super-event research prompt.
22. `031_random_terror_decision_mission_prompt.md` is the focused decision and mission implementation prompt.
23. `031_random_terror_achievement_prompt.md` is the focused achievement implementation prompt.
24. `031_random_terror_subagent_routing_prompts.md` contains bounded prompts for the project subagents.
25. `031_random_terror_coding_prompt.md` is the full implementation prompt.
26. `031_random_terror_goal_prompt.md` is the compact implementation goal prompt.
27. `031_random_terror_complete_spec.md` compiles the thirteen canonical specification parts into one reading copy.
28. `031_random_terror_manifest.json` lists final package files, statistics, and hashes.

## Stable accepted terms

The catalog event name remains `Random Terror`.

The event remains Event ID `31` and type `Minor Repeatable`.

The normal entry event remains `chaosx.nr31.1`.

The accepted evolution names are `Organized Cells`, `Transnational Terror Network`, `Territorial Insurgency`, `The Jihadist International`, and `The Final Jihad`.

The accepted manual scenario name is `Global Jihad`.

The accepted public world-end branch name is `The False Revelation`.

The proposed next manual scenario ID is `SCN-014`.

The proposed future cluster is Cluster `9`, working name `Internal Fracture`.

The scenario and cluster IDs require an authoritative workbook and live registry collision check before implementation.

## Scope boundaries

No custom combat battalion, equipment archetype, aircraft, ship, vehicle, building model, or 3D entity is required.

Spawned countries use existing land unit types with event-owned templates and equipment packages.

This decision avoids a new Event 19 provider, custom unit sound package, bespoke unit counter package, and 3D model pipeline without reducing the event's gameplay.

No permanent dedicated scripted GUI is required.

The national response uses an ordinary decision category, a static category picture, dynamic category text, targeted state decisions, and an event-owned state map mode.

The False Revelation may use one animated fictional leader portrait or portrait overlay because the leader is an impossible entity and the animation marks a world-end identity change.

No final quote, cultural remark, or audio track is selected in this planning package.

Those choices require the dedicated super-event research workflow, source verification, rights review, and final runtime inspection.
