# 076 · USA Tests Weapons

A repeatable American weapons-testing program that leaves foreign minor countries with damaged towns, lost people, and another request arriving before reconstruction is finished.

**Extract this folder into `docs/specs/`.** The resulting source location is `docs/specs/076_usa_tests_weapons_specs/`. Implementation work and actual specialist handoffs belong in `docs/plans/076_usa_tests_weapons_plans/`.

The supplied brief fixes the event identity, coercive choice, wave structure, real damage, delayed rewards, three evolutions, and Military Preparation / Low membership. This package expands those requirements into a proposed implementation design. Its numerical calibration, recovery actions, achievements, and presentation choices are new design decisions within the requested expansion. They have not been playtested or separately approved by the user.

## Read the design

| File | What it settles |
| --- | --- |
| [01 · The testing program](gameplay/01_testing_program.md) | Identity, campaign rhythm, American and victim roles |
| [02 · Targets and ultimatums](gameplay/02_targets_and_ultimatums.md) | Dynamic minors, player priority, repeat victims, real refusal wars |
| [03 · Independent test schedules](gameplay/03_test_schedules.md) | Wave size, preparation, impact, analysis, cancellation |
| [04 · Evolutions](gameplay/04_evolutions.md) | High-chaos openings, delayed activation, frozen assignments |
| [05 · Dynamic arsenal](weapons/05_dynamic_arsenal.md) | Extensible providers, equipment and technology eligibility |
| [06 · Conventional trials](weapons/06_conventional_trials.md) | Distinct weapon families, destruction, military effects |
| [07 · Nuclear and unconventional trials](weapons/07_unconventional_trials.md) | Testing-only prototypes, owner-controlled contamination and disease |
| [08 · Physical damage and casualties](integration/08_damage_and_deaths.md) | Real mutations, exact receipts, military and civilian accounting |
| [09 · American development](gameplay/09_american_development.md) | Delayed typed rewards, research priorities, production benefits |
| [10 · Repeated victims and recovery](gameplay/10_victims_and_recovery.md) | Domestic Hostility, repair objectives, relief and protection |
| [11 · Decisions and missions](gameplay/11_decisions_and_missions.md) | Actions, costs, requirements, deadlines and AI equivalents |
| [12 · International consequences](gameplay/12_international_consequences.md) | Condemnation, guarantees, sanctions, conferences and connections |
| [13 · AI and tuning](integration/13_ai_and_tuning.md) | Complete intended selection model, balancing fixtures |
| [14 · Persistence and owner contracts](integration/14_persistence_and_owners.md) | Job identity, retries, migration, missing owner capabilities |
| [15 · Event integration](integration/15_event_integration.md) | Namespace, shared picker, cluster, history, workbook and touchpoints |
| [16 · Presentation and assets](presentation/16_presentation_and_assets.md) | Narrative direction, report families, native decision surfaces |
| [17 · First foreign nuclear trial](presentation/17_nuclear_super_event.md) | One earned super-event, researched text and audio handoff |
| [18 · Achievements](gameplay/18_achievements.md) | Difficult, persistent conditions with exact proof requirements |
| [19 · Acceptance scenarios](integration/19_acceptance_scenarios.md) | What must be demonstrated before implementation can pass |
| [20 · Research and source limits](reference/20_research_and_source_limits.md) | Supplied sources, repository evidence, conflicts and unavailable checks |
| [21 · Requirement coverage](reference/21_requirement_coverage.md) | Every part of the rough brief mapped to its design owner |
| [22 · Source reading inventory](reference/22_source_reading_inventory.md) | Supplied text files, lengths, hashes and reading coverage |
| [23 · Package checks](reference/23_package_checks.md) | Checks performed on this document package, distinct from game validation |

## Implementation prompts

Start with the [coding prompt](prompts/076_usa_tests_weapons_coding_prompt.md) and use the [goal prompt](prompts/076_usa_tests_weapons_goal_prompt.md) as the completion contract. Separate briefs cover [decisions and missions](prompts/076_usa_tests_weapons_decision_mission_prompt.md), [assets](prompts/076_usa_tests_weapons_asset_prompt.md), [achievements](prompts/076_usa_tests_weapons_achievement_prompt.md), and the [super-event](prompts/076_usa_tests_weapons_super_event_prompt.md).

All player-facing wording remains direction-only. The supplied event and evolution names are retained as source labels. Working mechanic labels, asset labels and achievement IDs are not finished localisation.

## Evidence boundary

Every text file supplied in the archive, including all 20 subagent definitions, was read. The original event brief was also read. A bounded read-only inspection of the repository used commit `879b3007d3b6bf75c726c11635473fccda45c569`. The full live repository, all linked reference files, installed vanilla files and offline wiki set were not read. The source-limit document identifies the actual inspected material and remaining requirements.

No supplied subagent was executed. No HOI4 MCP analysis, game run, asset production, audio licensing approval, workbook edit or repository change was performed. This is a full design handoff with explicit implementation gates, not a claim that Event 076 has been implemented.
