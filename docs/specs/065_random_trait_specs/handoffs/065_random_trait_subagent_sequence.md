# Event 065 Subagent and Validation Sequence

## Purpose

This sequence keeps read-only review, gameplay ownership, asset work, probability validation, text work, documentation, and final acceptance separate.

Every prompt is self-contained because project subagents should run with `fork_context=false` when required.

## Sequence

### 1. Repo explorer

Prompt:

`prompts/065_random_trait_repo_explorer_prompt.md`

Output target:

`docs/plans/065_random_trait_plans/subagent_handoffs/065_random_trait_repo_explorer_report.md`

Purpose:

Map current source, shared integrations, trait roots, consumers, and stale assumptions.

### 2. Scripted-system architect

Prompt:

`prompts/065_random_trait_scripted_system_architect_prompt.md`

Output target:

`docs/plans/065_random_trait_plans/subagent_handoffs/065_random_trait_scripted_system_architecture.md`

Purpose:

Resolve the generator, registry, ledger scope, exact roll method, report storage, and cluster entry path before code changes.

### 3. Main implementation agent

Prompt:

`prompts/065_random_trait_coding_prompt.md`

Purpose:

Own every gameplay and shared-file change.

The main agent also owns the generator and final integration.

### 4. Asset worker

Prompt:

`prompts/065_random_trait_asset_prompt.md`

Output target:

Event 65 asset workspace and final handoff.

Purpose:

Validate or replace the report-event image.

This can run in parallel after the image direction and consumer are confirmed.

### 5. Probability auditor

Prompt:

`prompts/065_random_trait_probability_audit_prompt.md`

Output target:

`docs/plans/065_random_trait_plans/subagent_handoffs/065_random_trait_probability_audit.md`

Purpose:

Inspect and evaluate the actual generated weighted pool under every named scenario.

The main agent applies any approved correction.

The auditor then runs the required comparison again.

### 6. Localisation auditor

Prompt:

`prompts/065_random_trait_localisation_audit_prompt.md`

Output target:

Patch and audit report within the Event 65 plan handoff area.

Purpose:

Fix missing keys, raw IDs, clipping, vague prose, count grammar, and cross-surface wording.

### 7. Documentation curator

Prompt:

`prompts/065_random_trait_documentation_prompt.md`

Output target:

Permanent `docs/events/065_random_trait/` content and a plan handoff.

Purpose:

Record implemented facts and remove temporary planning language from permanent docs.

### 8. Spreadsheet alignment worker

Prompt:

`prompts/065_random_trait_spreadsheet_alignment_prompt.md`

Output target:

Workbook update, CSV exports, and alignment report.

Purpose:

Update the Event 65 row and Randomizations cluster row through the authoritative workbook.

### 9. Improvement-loop planner

Prompt:

`prompts/065_random_trait_improvement_loop_prompt.md`

Output target:

Either an Event 65 improvement addendum or a closure handoff.

Purpose:

Test design depth, integration, presentation, and bloat near completion.

Any accepted addition returns to the relevant owner and re-enters validation.

### 10. Completion auditor

Prompt:

`prompts/065_random_trait_completion_audit_prompt.md`

Output target:

`docs/plans/065_random_trait_plans/subagent_handoffs/065_random_trait_completion_audit.md`

Purpose:

Issue a final read-only pass, fail, blocked, or needs user review result against the acceptance matrix.

### 11. User acceptance

The user performs the in-game campaign and multiplayer checks.

Only the user acceptance step can support the final `Available` status.

## Ownership rule

Read-only auditors do not edit gameplay source.

The main implementation agent owns corrections to event logic, shared event-system files, cluster logic, registry generation, and runtime integration.

The asset worker owns Event 65 visual files.

The localisation auditor can patch assigned Event 65 text.

The documentation and spreadsheet worker owns permanent docs and workbook alignment after implemented facts are stable.

## Current planning-session limitation

The project subagent tool registry failed during this planning session.

The prompts above were created for later execution.

No output path listed here should be treated as already produced.
