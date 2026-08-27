# Decisions and Missions Skill Formatting Handoff

## Files changed

- `.agents/skills/chaos-redux-decisions-missions/SKILL.md`
- `docs/plans/repression_ledger_plans/subagent_handoffs/decision_category_text_formatting_skill_2026-08-27.md`

## Reusable rule added

The skill now forbids repeated pipes or vertical bars, divider-character runs, ASCII or Unicode table rows, and other text separators in player-facing decision category descriptions, status summaries, scripted localisation, and compact attached displays when they simulate columns, meters, ledgers, buttons, or panel layout.

The skill also forbids debug-style telemetry dumps, generic developer-state labels, raw variable names, and country-agnostic fallback prose that can leak another country's wording.

The guidance requires short natural-language lines, properly wired icons or texticons, real meters or panels, concise tooltips, and explicit country- or route-specific localisation branches with a neutral safe default fallback.

Category pictures and attached displays must not paint or textually simulate fake buttons, meters, ledger columns, or controls, and a real scripted GUI is warranted only when its layout is justified and functional.

Internal Markdown audit tables remain allowed as documentation and must not be copied into runtime localisation.

## Validation

- Read the repository `AGENTS.md`, the complete existing decisions/missions skill, and the official `skill-creator` guidance before editing.
- Ran the official `quick_validate.py` validator against `.agents/skills/chaos-redux-decisions-missions` with `python -X utf8`; it returned `Skill is valid!` after the default Windows code-page invocation could not decode an existing Unicode character.
- Reviewed the focused diff and confirmed that no gameplay, localisation, or GUI files were edited.

## Remaining risks

- Existing runtime decision text was not audited in this skill-maintenance pass; future decision and UI audits should apply the new formatting gate.
- No MCP surface was changed, so no live GUI inspection was required for this documentation-only update.
