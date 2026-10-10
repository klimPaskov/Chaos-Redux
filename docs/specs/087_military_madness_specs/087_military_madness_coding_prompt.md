# Implement Military Madness

Implement Chaos Redux Event 087, Military Madness, from `docs/specs/087_military_madness_specs/`.
Read the README (authority, gates, open question), Parts 1–6, the acceptance scenarios, the research notes and the asset and achievement prompts before editing.
The user-locked rules in the README are not negotiable; proposed tuning is recorded in the plans folder with its acceptance when it changes.
This is not permission to ship a short whitelist or a fixed entrenchment substitute.

Follow the repository rules (`CLAUDE.md`) and the `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-subagents`, `chaos-redux-event-assets`, `chaos-redux-ideas-modifiers`, `chaos-redux-ai-strategies` and `chaos-redux-improvement-loop` skills.

## Start from current source

- Read the relevant offline wiki and installed documentation sections for dynamic modifiers, ideas, timed decisions, scopes, on actions and AI strategies.
- Search `chaosx.nr87.1`, `chaosx.nr87.2`, `entrenchment_bonus`, event selection, cluster registration and localisation consumers; keep the `chaosx.nr87.1` entry and retire the legacy report option and idea.

## Behavior

- Every valid country draws independently at the frozen stage: one roll at baseline, three with one broad at 200 Chaos, six with two broad at 400, ten with three broad at 600, and no further stage (Part 1).
- The stage is the highest enabled eligible one, frozen before distribution and the Chaos impulse; older packages never change.
- Packages last exactly 365 days, stack with duplicates and expire independently; rewards never depend on popup acknowledgement.
- Guaranteed broad slots sample broad entries with replacement; the other slots sample the deduplicated stage union with replacement; every entry and every magnitude step has equal weight (Parts 2 and 3).
- No usefulness, force composition, prior luck or human control filters the pool.

## The registry

- Audit the installed modifier documentation, enabled DLC content, country systems and Chaos Redux military systems, and write a coverage document in the plans folder giving every candidate's admission or technical exclusion.
- Each admitted entry needs a stable ID, binding, value type, beneficial sign, real military consumer, minimum stage, magnitude profile, reversible application and localisation.
- Entries are append-only; resolve Boolean candidates per the README open question.
- Do not put idea-only `equipment_bonus` or `research_bonus` attributes in a dynamic-modifier block, and do not turn a leader or state effect into a national one through unsupported scopes.

## Stacking and safety

Keep raw per-package contributions and derive the applied totals; clamp only at proved technical limits, never at a balance cap; rebuild from surviving contributions at expiry; prove reductions stay valid with external modifiers and the dynamic-modifier update order (Parts 3 and 4).
Follow Part 4 for country lifetimes, civil wars, annexation, exile and same-day firings.
Add no recurring world scan.

## Presentation, AI and integration

- One combined dynamic-modifier spirit and one decision-category row per active package with its rolls and native remaining days (Part 5); no scripted GUI.
- The AI strategy responses in Part 5, ending with their contribution.
- Military Preparation Low member, Minor Repeatable, Chaos level 1, one history record and one +5 Chaos impulse per natural occurrence, no double cluster accounting, no Chaos or achievement progress from debug paths.
- Event Details holds the premise only; final localisation follows the Part 5 tone with correct units and expiry meaning.
- The package-owned idempotent CXT setup registration required by the repository rules.

## Delegation and checks

Route bounded work through `chaos-redux-subagents` with self-contained prompts: the registry, adapters and aggregation to `chaosx_scripted_system_architect`; the draw and AI strategy weights to `chaosx_ai_probability_auditor`; the decision rows to `chaosx_decision_mission_auditor`; player text to `chaosx_localisation_auditor`; art to the asset prompt's roles; achievements through the achievement prompt.
Use HOI4 MCP checks where they answer a concrete question, within the repository retry limits; when a tool or specialist is unavailable, do the review directly and record the limit.
Cover the acceptance scenarios with evidence or an explicit blocker.
Near completion, run `chaosx_improvement_loop_planner` and resolve its handoff, then `chaosx_event_completion_auditor`.
Do not launch the game; live validation belongs to the user.

## Documentation and catalog

Write `docs/events/087_military_madness/overview.md` and keep working evidence and the coverage document under `docs/plans/087_military_madness_plans/`.
After final wording exists, the spreadsheet worker updates Event 087 and the Military Preparation row in `docs/spreadsheets/chaos_redux_events_catalog.xlsx` and runs `python .tools/export_event_catalog_csv.py`; never edit the CSV exports or set Playable without approval.

Report implemented surfaces, changed files, evidence, unverified candidates, missing assets and blockers, and never replace a requirement with a silent fallback.
