# Event 24: Video Game in Sweden

The user's explicit 2026-09-20 instruction removes the Field-Validated Planner trait and its field-validation reward. This decision supersedes older passages and prompts that promise the trait or its icon; field-validation mission mechanics remain in scope.

This folder is the source specification package for Chaos Redux Event 24.
The event is implemented; the current implementation state and remaining acceptance gaps are recorded in [acceptance_status_2026-10-07.md](../../plans/024_video_game_in_sweden_plans/acceptance_status_2026-10-07.md) and [takeover_status_2026-10-06.md](../../plans/024_video_game_in_sweden_plans/takeover_status_2026-10-06.md).

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
| `024_video_game_in_sweden_asset_prompt.md` | Historical build contract for report art, category art, icons, and asset packaging |
| `024_video_game_in_sweden_achievement_prompt.md` | Historical build contract for achievements and their assets |
| `024_video_game_in_sweden_decision_mission_prompt.md` | Historical build contract for decisions and missions |
| `024_video_game_in_sweden_coding_prompt.md` | Historical build contract for the parent coding agent |
| `024_video_game_in_sweden_goal_prompt.md` | Historical repository goal prompt |
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

## Open questions

1. Supplied-division requirement (unresolved, awaiting the user).
   The field-validation objective and the Reality Audit require supplied divisions in Swedish training regions, but the installed documentation exposes no supply getter (`unit_organization` measures organisation and `supply_units` only grants supply).
   Source implements the D16 proxy: organisation, control, railway and national-reserve checks.
   Proposed (spec audit 2026-10-10): approve D16 as the final requirement and reword the objective as "divisions at operational strength in a controlled, rail-connected training state", because no engine-checkable exact form exists and the proxy is the only blocker on this acceptance item.
2. No further design change is proposed.
   The 8 October review retained the three openings, the single Simulation Reliance value, phased action budgets, four finite Evolution III responses and the mandatory reassessment, and this audit found no redundant meter, repeated decision or inert value to remove.
   The event is deliberately tied to campaign state (war, tension, supply, defeats) rather than to other events or shared crisis systems, which suits a Calm World fire-once satire.

## Changelog

- 2026-10-10 spec audit, pass 1:
  - Removed the planning-era "intended repository location" scaffold and pointed the README at the current acceptance and takeover status.
  - Marked the coding, goal, decision-mission, achievement and asset prompts as historical build contracts, noting that an unavailable MCP check is no longer a blocker under `CLAUDE.md`.
  - Repointed asset reference paths from the ignored `.agents/skills/` mirror to `.claude/skills/`.
- 2026-10-10 spec audit, pass 2:
  - Reviewed mechanics, values and decisions against the anti-bloat rules and retained them; added the D16 resolution proposal as the one open design question.
