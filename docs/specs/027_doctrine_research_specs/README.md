# Event 027: Doctrine Research specification package

This folder is the source specification package for Event 027, Doctrine Research. It is intended to be copied to `docs/specs/027_doctrine_research_specs/` in the Chaos Redux repository.

The package replaces the stale catalog concept in the supplied CSV snapshot. That row describes one major country receiving a complete doctrine through a fire-once event. The accepted design in this package is a global Minor Repeatable event. Every valid country receives a doctrine-development batch, and the size of that batch rises from one choice at baseline to five choices at Evolution IV.

## Reading order

| File | Purpose |
| --- | --- |
| `027_doctrine_research_spec_part_1_core.md` | Event identity, baseline rules, doctrine terminology, global scope, batch behavior, persistence, and system connections. |
| `027_doctrine_research_spec_part_2_choice_flow.md` | Complete human and AI choice flow, event-page structure, invalidation rules, DLC handling, custom doctrine handling, and edge cases. |
| `027_doctrine_research_spec_part_3_evolutions_balance_ai.md` | Evolution entry paths, recommended chaos thresholds, AI strategy, balance intent, exploit controls, and cluster behavior. |
| `027_doctrine_research_spec_part_4_presentation_assets_achievements.md` | Player-facing writing direction, report-event presentation, asset inventory, dynamic text requirements, and achievements. |
| `027_doctrine_research_research_notes.md` | Source-grounded doctrine findings, terminology reconciliation, design inferences, and engine questions that must be verified during implementation. |
| `027_doctrine_research_doctrine_registry_matrix.md` | Required doctrine-domain adapter contract for vanilla, DLC, Chaos Warfare, and future custom doctrine families. |
| `027_doctrine_research_probability_scenarios.md` | Named AI and weighted-selection scenarios for the mandatory probability audit. |
| `027_doctrine_research_catalog_cluster_handoff.md` | Proposed event row, proposed National Breakthroughs cluster row, member treatment, and authoritative workbook update instructions. |
| `027_doctrine_research_acceptance_criteria.md` | Feature-level completion criteria and concrete validation scenarios. |
| `027_doctrine_research_review_and_closure.md` | Manual application of the project subagent roles, improvement-loop closure finding, and tooling blockers. |
| `027_doctrine_research_source_review.md` | Full uploaded-source inventory, archive inventory, read status, and unavailable external sources. |
| `027_doctrine_research_asset_prompt.md` | Bounded asset-production prompt for the report image and achievement icons. |
| `027_doctrine_research_achievement_prompt.md` | Bounded achievement implementation and tracking prompt. |
| `027_doctrine_research_coding_prompt.md` | Full implementation prompt for the coding agent. |
| `027_doctrine_research_goal_prompt.md` | Compact goal prompt for a Codex implementation thread. |

## Accepted design in one page

Event 027 is a global positive breakthrough. One random-event firing creates one doctrine-development batch for every country that exists at the firing snapshot and has at least one valid registered doctrine option.

A batch contains one choice at baseline, two at Evolution I, three at Evolution II, four at Evolution III, and five at Evolution IV. Each choice is resolved independently. A country may direct every choice into one branch or distribute choices across several branches and service domains.

Each choice begins by selecting a doctrine domain. If that domain lacks an active Grand Doctrine, the country may adopt one eligible Grand Doctrine. Adoption consumes the choice and grants no event mastery step. If the domain already has an active Grand Doctrine, the country selects an eligible track and advances one mastery level in its current subdoctrine. An empty track may select one eligible subdoctrine and receive the first event mastery step in the same choice. Existing banked mastery remains intact and resolves through the native doctrine system.

The package uses the phrase `mastery step` for the event reward. The official doctrine interface uses `Milestone` for the Grand Doctrine reward earned by completing a full track. Keeping these terms separate prevents player-facing and implementation confusion.

The doctrine pool is adapter-driven. Army, Navy, Air, supported Special Forces content, Chaos Warfare, and future custom doctrine families can participate when their local graph, DLC gate, availability rules, track list, and mastery operations have been verified. Unsupported or invalid families fail closed. The event never substitutes military experience, research bonuses, political power, or a different doctrine family.

Human countries resolve a chained country-event flow. AI countries use the same valid option pool and resolve silently. The AI scores domains, Grand Doctrines, tracks, and subdoctrines from force composition, production, current wars, terrain, strategic plans, doctrine completion value, and custom adapter factors. It recalculates after every choice so it can stack a strong branch, finish a near-complete branch, or diversify when several tracks have similar value.

A country can hold one active batch and a queue of later batches. Each batch snapshots its size and evolution stage when Event 027 fires. Evolution unlocks do not enlarge a batch already in progress. Annexed countries lose unused choices, released countries receive no retroactive choices, and later normal firings include every country that exists at the new firing snapshot.

The event records one global history entry per random-event firing. Country choice pages do not create extra random-event history rows. Evolution records have no country actor. Cluster participation remains one global pacing event and does not multiply the Event 027 fanout.

## Scope decision

The accepted design uses ordinary country events, doctrine adapters, dynamic text, AI logic, event-log integration, one report image, and three achievements. The event already has a complete playable loop through the chained choices. A separate decision category or custom mechanic window would duplicate the same interaction and add avoidable maintenance.

## Tooling status

Every uploaded Markdown, CSV, TOML, configuration file, and every TOML contained in `subagents.zip` was read in full for this package. The actual Chaos Redux repository, its offline Paradox wiki snapshot, the installed vanilla game files, the authoritative catalog XLSX, the configured Codex subagent runner, and the HOI4 MCP server were not present in this runtime. Their required inspections are carried as explicit implementation gates in the research notes, prompts, review file, and acceptance criteria.

The design was not shortened into a fallback version. Engine-specific doctrine operations, exact file paths, current vanilla graph identities, current DLC gates, and numeric AI weights remain deliberately unresolved until the required repository, vanilla, wiki, and MCP evidence is available.
