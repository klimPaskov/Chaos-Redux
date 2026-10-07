# Subagent Prompt: Event 021 Repository Explorer

Use this prompt only when paths, live APIs, precedents, or dependency order remain unclear under the [repo-explorer gate](../../../../.agents/skills/chaos-redux-subagents/SKILL.md#repo-explorer-use-gate).
For Codex, spawn `chaosx_repo_explorer` with `fork_turns="none"` and bounded parent questions.

Read:

- repository `AGENTS.md`
- `docs/specs/021_random_civil_war_specs/`
- Event 006 specs and implementation
- Event 004 and Event 007
- every specialized civil-war event named in `021_random_civil_war_overlap_and_catalog_reconciliation.md`

This is read-only exploration.

Map:

- current Event 021 implementation, registration, enable state, name mapping, Event Details, and event-log surfaces
- repeatable-event registration and no-target `N/A` precedent
- Wars cluster registry, member order, collision handling, skip reasons, and logging
- triggerable scenario registry and existing `SCN-018` ownership, resolved in the source-read ledger on 2026-09-25
- existing civil-war, dynamic-country, same-tag takeover, state allocation, unit allocation, stockpile, capital, faction, subject, and cleanup precedents
- Event 006 country collections, package registry, tag mapping, origin logic, initialization, forces, focus assignment, formables, decisions, AI, assets, and idempotence
- shared `is_actual_nonhuman_country` and `is_special_chaos_country` use
- event-owned decision, mission, idea, on-action, AI, and asset file patterns
- current script constants and reusable dynamic helper registries
- current authoritative XLSX path and exporter
- current HOI4 MCP tool schemas for event, probability, focus, GUI, and map surfaces

Inspect required offline wiki pages, installed vanilla documentation, vanilla files, and approved reference mods.

Return:

- source-of-truth map
- exact likely touched files
- reusable helpers already available
- helper gaps
- tag, character, focus, and country-package risks
- implementation order
- meaningful validation plan
- exact MCP blockers, if any
- exact unavailable sources, if any

Write:

`docs/plans/021_random_civil_war_plans/subagent_handoffs/repo_explorer_handoff.md`

Do not patch gameplay files.
