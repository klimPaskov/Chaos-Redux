# Event 078 planning handoff

## Scope and status

This package defines the proposed full rework of Border Conflict.
Its source specifications are in `docs/specs/078_border_conflict_specs/`.
The main design is `078_border_conflict_spec_part_1_core.md`.
The files in this plans folder record evidence, implementation acceptance requirements, and prepared specialist briefs.
They do not claim that the event has been implemented or engine-tested.

The entire supplied archive's 42 text files were read before specification drafting.
This includes every supplied skill, the mechanics and catalog exports, the configuration, and all 20 specialist definitions.
The separate MTTH skill retrieved from the repository was also read in full.
Some external dependencies required by those sources remain unread or only partly inspected, as recorded in the research manifest.

No project subagent was executed in this session.
The available connector for the outer Codex runtime requires a turn token that was not available.
The supplied role files describe specialists but do not themselves provide a launch facility.
The HOI4 MCP probability and live-game tools were also unavailable.
Prepared handoffs and parent review are explicitly distinguished from completed specialist work.

## Start here

Read the main specification and the frontier and evolution parts before implementing the allocator.
Then read the engine evidence and acceptance matrix before choosing how concurrent results will be identified.
The first implementation milestone is a small native concurrency prototype, because the worldwide design depends on it.
Do not spend the first milestone building presentation around a country-global opponent variable.

| File | Purpose |
| --- | --- |
| `integration/implementation_handoff.md` | Milestones, ownership boundaries, and shared-system integration |
| `research/engine_evidence.md` | Confirmed script surfaces, limited precedents, and open native questions |
| `research/reading_and_tooling_limits.md` | Full-reading claim boundaries and missing external dependencies |
| `research/source_manifest.json` | Per-file reading coverage, counts, and hashes |
| `validation/acceptance_matrix.md` | Required design, native, multiplayer, presentation, and migration cases |
| `validation/probability_scenarios.md` | Required random-allocation and evolution audit scenarios |
| `reviews/parent_review.md` | This session's design review and unresolved specialist gates |
| `subagent_handoffs/README.md` | Specialist roles, allowed work, and execution status |
| `prompts/078_border_conflict_coding_prompt.md` | Full implementation task |
| `prompts/078_border_conflict_goal_prompt.md` | Bounded `/goal` task |
| `prompts/078_border_conflict_asset_prompt.md` | Report, news, and category visual work |
| `prompts/078_border_conflict_achievement_prompt.md` | Achievement behavior and canonical icon work |
| `prompts/078_border_conflict_decision_mission_prompt.md` | Native informational category and hold presentation |

## Non-negotiable acceptance gates

Real native border wars must work simultaneously for one country against several neighbors and, when evolved, several independent fronts against the same neighbor.
Every result must identify the exact dispute and transfer at most its one declared target.
A normal war against somebody else must not exclude the participant.
The event must never start a normal war or silently serialize all participation into a country queue.

If the installed engine cannot meet one of these requirements, return an evidenced design blocker.
Do not mark a narrower implementation complete.
A temporary prototype is valid evidence work, but it is not a replacement accepted event.

The catalog status remains To Be Reworked until the actual implementation, mandatory specialist work, probability audit, assets, documentation, and runtime acceptance are complete.
A complete planning document does not authorize changing that status to finished.
