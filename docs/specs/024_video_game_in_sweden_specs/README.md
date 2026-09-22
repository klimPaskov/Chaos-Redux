# Event 24: Video Game in Sweden

The user's explicit 2026-09-20 instruction removes the Field-Validated Planner trait and its field-validation reward. This decision supersedes older passages and prompts that promise the trait or its icon; field-validation mission mechanics remain in scope.

This folder is the source specification package for Chaos Redux Event 24.

Intended repository location:

`docs/specs/024_video_game_in_sweden_specs/`

## Design decision

Event 24 is a Minor Fire-Once event at Chaos level 1, Calm World. Sweden develops an implausibly advanced grand-strategy war game and first treats it as a cheap staff-training instrument. The program can end after a useful but limited trial. Higher Chaos can turn it into an officer culture, a civilian obsession, and finally a reversible crisis in which the state mistakes the model for reality.

The event uses one visible country value, Simulation Reliance. It uses one staged idea lifecycle and one phase-based decision category. The event remains Swedish, bounded, reversible, and small enough to coexist with the rest of the campaign.

The event remains unclustered. The catalog's Scientific Research cluster is a poor fit because the event's main subject is institutional and cultural misuse of a simulation, not a shared research breakthrough.

## Files

| File | Purpose |
| --- | --- |
| `024_video_game_in_sweden_spec_part_1_core.md` | Core premise, targeting, baseline routes, reliance system, ordinary conclusion, and event identity |
| `024_video_game_in_sweden_spec_part_2_evolutions.md` | All three evolutions, pre-fire variants, reversal paths, incidents, and foreign reactions |
| `024_video_game_in_sweden_spec_part_3_decisions_ai_balance.md` | Decision system, AI strategy, balance targets, cleanup, exploit controls, and campaign-state behavior |
| `024_video_game_in_sweden_spec_part_4_presentation_achievements_acceptance.md` | Text direction, presentation choice, assets, achievements, Event Log behavior, and acceptance criteria |
| `024_video_game_in_sweden_decision_map.md` | Complete phase and action map for implementation |
| `024_video_game_in_sweden_ai_probability_scenarios.md` | Named scenarios for later MCP probability inspection and comparison |
| `024_video_game_in_sweden_research_notes.md` | Historical and design research with source links and explicit inferences |
| `024_video_game_in_sweden_catalog_alignment.md` | Current CSV row, proposed authoritative workbook content, and post-implementation status flow |
| `024_video_game_in_sweden_asset_prompt.md` | Context-complete prompt for generated report art, category art, icons, and asset packaging |
| `024_video_game_in_sweden_achievement_prompt.md` | Achievement implementation and asset brief |
| `024_video_game_in_sweden_decision_mission_prompt.md` | Context-complete decision and mission implementation brief |
| `024_video_game_in_sweden_coding_prompt.md` | Full implementation prompt for the parent coding agent |
| `024_video_game_in_sweden_goal_prompt.md` | Repository goal prompt, kept below 4,000 characters |
| `024_video_game_in_sweden_review_handoff.md` | Role-based subagent review, anti-bloat closure, capability limits, and unresolved implementation checks |
| `024_video_game_in_sweden_source_reading_audit.md` | Complete audit of the uploaded Markdown, skill, catalog, config, and subagent files read before planning |

## Main non-negotiables

1. Sweden is the only primary host. The event shows `N/A` when no valid principal Swedish state exists.
2. The event fires once and cannot create duplicate Swedish program instances after civil wars, annexation, release, or tag changes.
3. The baseline trial can conclude without any evolution.
4. Evolutions use Chaos tiers and delayed pacing. They do not all fire immediately because the campaign starts at high Chaos.
5. Simulation Reliance is the only player-managed value.
6. Every phase exposes three to five useful actions and at most one active mission.
7. The idea lifecycle replaces prior stages. It does not stack several near-identical spirits.
8. Evolution III always retains a credible recovery path. Even the maximum-risk route reaches a mandatory reassessment.
9. Foreign responses stay as bounded events and temporary effects. They do not create a global copy of the Swedish decision system.
10. The accepted surface list in this package is exhaustive and later implementation must preserve its bounded scope.
11. Final localisation must use dry period satire and concrete consequences. It must not use modern gamer slang as the main joke.
12. No final asset may remain a placeholder.

## Source authority

The user's Event 24 brief is the primary design source. The uploaded event catalog snapshot confirms ID 24 and its Minor Fire-Once classification, but its detail and evolution fields are stale. The implementation must update the authoritative workbook after in-game wording exists, then regenerate the CSV exports.
