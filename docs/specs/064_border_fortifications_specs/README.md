# Event 064 Border Fortifications Planning Package

This package is the accepted design handoff for Chaos Redux Event 064, Border Fortifications.

All project-facing event-scoped folders, filenames, prompts, asset identifiers, achievement identifiers, and test scenario labels use the zero-padded form `064`. The established runtime namespace remains `chaosx.nr64.*`.

Event 064 remains a Chaos Level 1 Minor Repeatable event. Its primary cluster is Sudden Abundance at Medium member severity. Its additional cluster is Military Preparation at Medium member severity. The event creates one synchronized global wave of physical defenses along current foreign land frontiers, then lets each country decide how to use, supply, or overcome the new lines.

The package keeps the idea proportional to a global minor event. It provides a complete event transaction, three evolution packages, a compact response system, AI behavior, cluster coordination, Chaos feedback, achievements, assets, text direction, catalog reconciliation, and acceptance criteria. Its player surface uses the normal report event and a compact decision category.

All names marked as working labels are internal design handles. They are not final localisation. Border Fortifications, Defense in Depth, Fortress States, and Fortress World are accepted event and evolution names from the user brief.

## Package map

### Specifications

- `specs/064_border_fortifications_spec_part_1_core_and_baseline.md`
- `specs/064_border_fortifications_spec_part_2_evolutions_and_targeting.md`
- `specs/064_border_fortifications_spec_part_3_responses_decisions_and_ai.md`
- `specs/064_border_fortifications_spec_part_4_chaos_clusters_and_connections.md`
- `specs/064_border_fortifications_spec_part_5_text_assets_achievements_and_acceptance.md`

### Matrices

- `matrices/event_chain_and_state_map.md`
- `matrices/decision_mission_matrix.md`
- `matrices/ai_probability_scenario_matrix.md`
- `matrices/tuning_and_balance_framework.md`
- `matrices/acceptance_criteria.md`

### Diagram

- `diagrams/064_border_fortifications_flow.md`

### Research and review

- `research/design_precedents.md`
- `research/catalog_and_repo_reconciliation.md`
- `research/source_corpus_read_log.md`
- `research/improvement_loop_review.md`

### Implementation prompts

- `prompts/064_border_fortifications_asset_prompt.md`
- `prompts/064_border_fortifications_achievement_prompt.md`
- `prompts/064_border_fortifications_decision_mission_prompt.md`
- `prompts/064_border_fortifications_coding_prompt.md`
- `prompts/064_border_fortifications_goal_prompt.md`

### Required blocked handoff

- `../../plans/064_border_fortifications_plans/subagent_handoffs/064_border_fortifications_improvement_loop_tooling_blocker.md`

### Manifest

- `manifest.md`

## Design non-negotiables

1. The canonical entry event remains `chaosx.nr64.1`.
2. One global root resolves the complete construction wave. Country report options never own the automatic fort grant.
3. Every qualifying province on a current foreign land frontier receives one land-fort level per ordinary wave, subject to the active tier cap.
4. A qualifying frontier is based on current control and passable direct land adjacency. Strait links, sea links, impassable map edges, lakes, and invalid building slots do not qualify.
5. Relations do not protect a frontier from the event. Allies, faction partners, subjects, overlords, enemies, civil-war countries, and neutral states can receive lines along their shared controlled boundary.
6. The wave uses a firing-time snapshot. Later conquests, releases, occupations, and border changes wait for a later firing.
7. A province is processed once per incident even when it touches several foreign countries or satisfies several strategic roles.
8. Existing forts are preserved. The event never lowers a building level and never uses blanket replacement.
9. Repeated waves strengthen defenses gradually. Tier caps stay below level ten and ordinary frontiers remain weaker than selected anchors.
10. Evolution I adds a bounded second line and stronger strategic frontier anchors.
11. Evolution II creates a bounded set of Fortress States with stronger line sectors, anti-air, radar, logistics work, and selective coastal defenses.
12. Evolution III creates bounded internal redoubts around capitals, major victory points, supply hubs, and critical approaches. It also gives island countries a valid local result when suitable positions exist.
13. Evolutions alter future waves. They do not retrofit every prior fort immediately and they add no Chaos merely for becoming enabled.
14. Disabled evolution stages are skipped cleanly. Later enabled stages remain functional without hidden dependence on disabled earlier stages.
15. The response category shows a qualitative posture, the remaining response window, valid projects, and clear costs.
16. Each affected country chooses one temporary response posture after a wave. The postures support defense, logistics, or offensive breach preparation and never stack with their older versions.
17. The offensive posture provides real counterplay against the worldwide defenses.
18. Decision costs use concrete industry, equipment, transport, fuel, experience, manpower, and time commitments. Political power is not the default price.
19. AI behavior reacts to threat, supply, country size, stockpiles, planned offensives, coast exposure, and capital danger.
20. Automatic Event 064 firing can enter one cluster context per incident. Multi-cluster membership never duplicates the event effect.
21. Event 064 remains valid as a standalone event when neither cluster fires.
22. Event-owned Chaos changes are tied to concrete construction outcomes and use one-time milestones, cooldowns, minimum footprint checks, and shared-source overlap rules.
23. The first impossible global construction wave has an event-specific abnormality premium. Generic military buildup, wars, casualties, and later combat are not counted twice.
24. The asset package is restrained and event-specific. It includes the report image, category presentation, posture icons, decision icons, and achievement icons.
25. The existing report sprite identity should be preserved unless source inspection proves a clean migration is safer.
26. Event Details, History, Evolutions, cluster views, debug names, documents, and the authoritative catalog must agree.
27. The stale exported Event 064 catalog row must be corrected in the authoritative workbook, then all CSV exports must be regenerated by the repository export tool.
28. The implementation must stay bounded. No broad recurring world scan may be added to maintain the fort network.
29. Every mapped achievement needs full tracking, disqualifiers, localisation, icons, documentation, and test coverage.
30. No fallback, silent reduction, temporary substitute, or unreported omission counts as completion.

## Reading and review statement

All 21 standalone project source files and all 20 subagent definition files supplied with this task were read through their complete end markers. The three current CSV catalogs were included in that full read. The connected repository was also inspected for the current Event 064 event file, localisation, report sprite, event registry conventions, cluster system, and an accepted planning-package precedent.

The available tool registry did not expose a subagent execution function. The mandatory independent `chaosx_improvement_loop_planner` run could not be performed in this environment. A parent-led review using the full planner definition was completed and folded into the package. The unresolved execution requirement is recorded as a tooling blocker and remains a required implementation-stage action.

## Package status

The specification is complete as a planning handoff. It has not implemented or live-tested Event 064. The event catalog status therefore remains To Be Reworked until the repository implementation and acceptance work are completed.
