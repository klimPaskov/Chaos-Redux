# Prompt for `chaosx_scripted_system_architect`

Spawn with `fork_context=false`.

Event ID: `53`.
Event slug: `mysterious_man`.
Source specification: `docs/specs/053_mysterious_man_specs/`.
Handoff path: `docs/plans/053_mysterious_man_plans/subagent_handoffs/scripted_system_architect_handoff.md`.

Read `AGENTS.md`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-subagents`, the complete Event 53 specification, the repo explorer handoff, relevant offline wiki pages, installed vanilla script documentation, and the exact existing Event 53 and helper files.

Own only the Event 53 scripted-system layer. Inspect first, then implement bounded owner-side logic where safe:

- `common/script_constants/053_mysterious_man_constants.txt`
- `common/scripted_triggers/053_mysterious_man_triggers.txt`
- `common/scripted_effects/053_mysterious_man_effects.txt`
- direct Event 53 helper call sites explicitly named by the parent or repo explorer

Implement or fully map:

- uniform valid-player target pool
- persistent target proof and legal-successor transfer
- exclusive lifecycle states and sequence IDs
- dynamic interval calculation and one-visit scheduling
- player-control pause and resume
- valid demand-type pool and uniform selection
- locked dynamic demand amounts and affordability
- exact payment transactions
- 57-entry registry constants and live registration gates
- fresh valid consequence pool with each package once
- uniform random member or ordinal selection
- package dispatch, receipts, idempotence, one bounded redraw, and government-paralysis safety package
- evolution activation state and target-local checks
- startup reconciliation
- direct package helpers that fit existing neutral primitives

Keep Event 53 orchestration out of `chaosx_dynamic_effects`. Reuse documented neutral helpers. Add a shared helper only when unrelated callers genuinely need it, then document its public contract in the matching registry file.

Do not create fake adapter stubs that report success. A missing owner adapter must keep its package out of the live pool and appear as a blocker in the handoff. Do not edit localisation, assets, workbook, focus, country, decision, GUI, or unrelated files.

Use `hoi4.event_inspect` for linked Event 53 call sites. Any probability-bearing helper requires `hoi4.probability_inspect` and the read-only probability auditor before and after the parent applies balance changes.

Report files changed, helper names, constants, call sites, live and reserved package IDs, owner dependencies, receipts, cleanup, meaningful validation, skipped checks, and every blocker.
