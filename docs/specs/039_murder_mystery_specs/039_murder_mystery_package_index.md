# Event 039 Murder Mystery Specification Package

## Source of truth

This package is the accepted planning source for Event 039 Murder Mystery. It supersedes the current catalog snapshot where Event 39 is still described as a Minor Repeatable leader murder. The authoritative catalog workbook must be updated during implementation so the event is recorded as Minor Fire-Once, Chaos level 1, Intelligence cluster, Medium member, with five evolutions, the Assassin Network triggerable scenario, and the public World of Anarchy terminal branch.

The package is intended to be extracted directly into `docs/specs/039_murder_mystery_specs/`.

## Event identity

| Field | Accepted value |
| --- | --- |
| Event ID | `39` |
| Event name | Murder Mystery |
| Event type | Minor Fire-Once |
| Status before implementation | To Be Reworked |
| Chaos level | `1` |
| Cluster | Intelligence |
| Cluster role | Medium member |
| Normal host | One valid random major country or one valid player-controlled ordinary country |
| Baseline conclusion | Permanent resolution when the original killer and core network are captured before international survival routes remain |
| Country escalation | Dynamic Assassin State at Evolution III |
| Manual scenario | Assassin Network |
| Public terminal branch | World of Anarchy |

## Design promise

Murder Mystery begins as a national security crisis that a capable government can solve. Neglect, weak institutions, repeated deaths, and higher Chaos can turn one murderer into a cult, an international cell network, a territorial revolutionary state, and a terminal campaign against ordinary government leadership.

The event supports two connected games. Ordinary governments investigate murders, protect vulnerable offices, share intelligence, raid cells, and prevent territorial collapse. An Assassin State player manages a movement whose doctrine attacks hierarchy while its war effort depends on command, logistics, production, and disciplined military organization.

The opening remains intentionally ambiguous. The event never confirms a historical order, religion, nation, or real political doctrine as the source. The word assassin describes the event's fictional murder movement. It must not borrow the Nizari Ismailis, the hostile medieval legends attached to them, or generic depictions of anarchism as its identity.

## Locked design decisions

1. The event uses a normal decision category with a strong static or animated category picture and compact status text. It does not require a dedicated scripted GUI.
2. Ordinary governments see two persistent public values, Case Progress and Network Reach. The Assassin State sees Network Reach and Brotherhood Cohesion. No actor manages more than two persistent Event 39 values at once.
3. The opening leader murder is allowed only when safe succession can be proven. The event must never remove an unregistered character that another system needs.
4. Named character deaths use a curated safe target registry. An unsafe or unregistered role uses a generic office casualty instead of deleting a character.
5. The Assassin State split transfers a validated connected cluster of states and leaves a viable original government. It does not use the ordinary civil war command.
6. Foreign revolts are bounded. They use smaller validated state clusters, a capped country pool, and one central movement hierarchy.
7. Assassin units win through mobility, organization, reconnaissance, night operations, terrain use, raids, and short attacks. Low hit points, weak armor interaction, air vulnerability, attrition, supply demands, and formation caps stop them from replacing normal infantry.
8. World of Anarchy uses bounded activation, war, capitulation, and cleanup hooks. It does not run a daily whole-world country scan.
9. Evolution state gives no Chaos. Chaos changes only follow concrete murders, failed containment, territorial revolts, movement growth, government dismantling, or successful reversal.
10. The manual scenario reuses the normal event system and clears every scenario bypass after setup.

## Package map

| File | Role |
| --- | --- |
| `039_murder_mystery_spec_part_1_core.md` | Event contract, eligibility, public values, lifecycle, baseline outcomes |
| `039_murder_mystery_spec_part_2_investigation.md` | Investigation loop, intelligence scaling, player actions, missions, capture outcomes |
| `039_murder_mystery_spec_part_3_character_safety.md` | Safe succession, character target registry, protected ownership, death handling |
| `039_murder_mystery_spec_part_4_evolutions.md` | Evolution I through V, pacing, pre-fire handling, Chaos consequences |
| `039_murder_mystery_spec_part_5_international_network.md` | Foreign cells, intelligence cooperation, territorial revolt, movement succession |
| `039_murder_mystery_spec_part_6_assassin_state.md` | Dynamic country split, country package, economy, politics, subjects, defeat |
| `039_murder_mystery_spec_part_7_focus_tree.md` | Assassin State focus route architecture and branch interaction |
| `039_murder_mystery_spec_part_8_decisions_missions.md` | Decision categories, active mission budget, costs, visibility, AI actions |
| `039_murder_mystery_spec_part_9_units_3d.md` | Custom unit family, balance, equipment, Event 19 integration, 3D, audio, counters |
| `039_murder_mystery_spec_part_10_world_end.md` | World of Anarchy activation, conquest handling, victory, defeat, aftermath |
| `039_murder_mystery_spec_part_11_scenario_cluster_integrations.md` | Manual scenario, Intelligence cluster, external event connections |
| `039_murder_mystery_spec_part_12_system_architecture.md` | State ownership, registries, helper boundaries, performance, save and multiplayer |
| `039_murder_mystery_spec_part_13_ai_probability.md` | AI plans, named probability scenarios, balance expectations, exploit controls |
| `039_murder_mystery_spec_part_14_assets_presentation.md` | Complete visual package, source modes, paths, animation states, manifest rules |
| `039_murder_mystery_spec_part_15_super_events_news.md` | Presentation hierarchy, super-event roles, report and news direction, audio gates |
| `039_murder_mystery_spec_part_16_achievements.md` | Achievement set, tracking, disqualifiers, icon directions |
| `039_murder_mystery_spec_part_17_research_safety.md` | Historical design anchors, cultural safety, terminology, bibliography |
| `039_murder_mystery_spec_part_18_acceptance.md` | Completion contract, scenario matrix, audits, blocked conditions |
| `039_murder_mystery_asset_prompt.md` | Context-complete prompt for visual asset production |
| `039_murder_mystery_super_event_prompt.md` | Context-complete super-event research and production prompt |
| `039_murder_mystery_achievement_prompt.md` | Context-complete achievement implementation and art prompt |
| `039_murder_mystery_decision_mission_prompt.md` | Context-complete decision and mission implementation prompt |
| `039_murder_mystery_focus_tree_prompt.md` | Context-complete focus tree implementation and audit prompt |
| `039_murder_mystery_3d_prompt.md` | Context-complete Meshy 7, Blender, audio, and counter handoff prompt |
| `039_murder_mystery_coding_prompt.md` | Main coding handoff after all accepted specs are read |
| `039_murder_mystery_goal_prompt.md` | Final goal prompt, kept within the required character limit |
| `039_murder_mystery_improvement_audit.md` | Manual improvement-loop and specialist-role review of the finished design |
| `039_murder_mystery_source_manifest.md` | Complete source-reading record, subagent status, and known source conflicts |
| `039_murder_mystery_research_bibliography.md` | Web research sources used for design and safety decisions |
| `manifest.json` | Machine-readable package inventory and status |
| `039_murder_mystery_package_checksums.sha256` | SHA-256 integrity ledger for the packaged files |

## Implementation order

The implementation should first lock the tag, character, country, state, and super-event registries. The scripted-system layer should then establish the safe succession, character protection, investigation, cell, split, and cleanup APIs. Baseline and Evolutions I and II should be completed before country creation begins. The Assassin State package, focus tree, decisions, units, models, faction, and foreign derivatives should follow. World of Anarchy, manual scenario wiring, asset completion, catalog alignment, and final audits should be the closing tranche.

The event must remain testable after every tranche. A later evolution may be unavailable while unfinished, but baseline systems must never depend on placeholder country, unit, asset, or terminal logic.

## Completion position

This is a complete planning package. No requested event branch, evolution, country route, custom unit family, manual scenario, cluster role, terminal branch, asset family, super-event role, achievement family, AI surface, or cleanup path has been intentionally removed from the accepted rough design.
