# Event 19 Infantry Spawn Planning Package

This folder is the source planning package for Chaos Redux Event ID `19`, **Infantry Spawn**.

The request label `017# Infantry Spawn` is preserved in the package history, but the catalog and current repository identify the canonical event as ID `19`. All event, file, registry, achievement, scenario, and documentation identifiers in this package therefore use `019` or event ID `19`.

## Package purpose

The current event is a small repeatable global spawn loop. This package redesigns it as a scalable military disruption system whose identity changes through four evolutions:

1. uneven local musters
2. organized and increasingly advanced formations
3. deliberately requested armies with completely random composition and claimant generals
4. registered Chaos unit families whose reckless use can produce independent nonhuman revolt countries

The design keeps the event repeatable, prevents free equipment farming, separates ordinary lifecycle stages from true evolutions, provides AI behavior, maps the decision and scripted GUI layers, defines derivative country packages, and includes the requested immediate-mutiny triggerable scenario.

## Folder map

- `specs/` contains the sequential source specification.
- `matrices/` contains implementation-facing design maps for templates, decisions, generals, AI, countries, assets, and cleanup.
- `focus_graphs/` contains the route architecture for derivative nonhuman countries.
- `prompts/` contains bounded handoffs for asset production, achievements, decisions and missions, implementation, and the final implementation goal.
- `research/` records repository findings and historical design anchors.
- `review/` records full source reading, anti-bloat review, manual role-equivalent subagent reviews, uncertainty, and completion auditing.

## Reading order

1. `specs/019_infantry_spawn_spec_part_1_core.md`
2. `specs/019_infantry_spawn_spec_part_2_spawn_engine_and_baseline.md`
3. `specs/019_infantry_spawn_spec_part_3_evolutions_i_and_ii.md`
4. `specs/019_infantry_spawn_spec_part_4_evolution_iii.md`
5. `specs/019_infantry_spawn_spec_part_5_evolution_iv.md`
6. `specs/019_infantry_spawn_spec_part_6_derivative_countries.md`
7. `specs/019_infantry_spawn_spec_part_7_decisions_ui_ai_balance.md`
8. `specs/019_infantry_spawn_spec_part_8_scenario_interactions_acceptance.md`

The matrices and prompts should be read after the sequential specification.

## Deliberate boundaries

The event has no terminal world-end outcome. The derivative countries are dangerous regional actors, not substitutes for the Zombie Outbreak, Death, golem, or future parent event endgames. No super-event is planned because the normal event, its evolutions, and its requested triggerable scenario do not meet the project threshold for a campaign-defining presentation moment. A later globally dominant derivative revolt could justify a separate improvement proposal, but it is outside this source design.

The design does not prescribe final player-facing localisation. All names in the specification are working labels or internal design labels unless the text explicitly identifies a stable script-facing identifier. Implementation must write final in-world text from the supplied tone and information directions.

## Process disclosure

All 30 supplied project files were read in full before this package was drafted. Their hashes and line counts are recorded in `review/source_reading_manifest.md`.

The custom project subagent runtime was not available in this environment. The required specialist passes were therefore performed manually as role-equivalent reviews and recorded in `review/manual_subagent_role_reviews.md`. The mandatory near-completion improvement-loop review was also performed manually and recorded separately. This does not count as an actual `chaosx_improvement_loop_planner` spawn, so the implementation agent must run the real project subagent when that runtime is available before claiming implementation completion.

The public repository was inspected selectively for current Event 19 behavior and parent-system isolation risks. The full local Chaos Redux repository, offline Paradox wiki snapshot, and installed vanilla game documentation were not mounted here. Implementation must verify all engine syntax and current identifiers against those local sources.
