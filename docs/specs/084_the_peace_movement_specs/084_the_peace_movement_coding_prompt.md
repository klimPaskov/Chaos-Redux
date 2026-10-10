# Implement Event 84 · The Peace Movement

Work in the Chaos Redux repository.
The source package is `docs/specs/084_the_peace_movement_specs/`; plans, handoffs, audit evidence, and unresolved findings belong in `docs/plans/084_the_peace_movement_plans/`.
Use this prompt only under an implementation assignment that accepts the relevant design.
Preserve unrelated worktree changes.

## Read first

Read `CLAUDE.md` and the current `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-focus-trees`, `chaos-redux-super-events`, `chaos-redux-event-assets`, `chaos-redux-3d-model-pipeline`, `chaos-redux-mtth`, `chaos-redux-improvement-loop`, and `chaos-redux-subagents` skills, plus the generic HOI4 skills for the systems you touch.
Read all 13 spec parts, the modifier precedence, the decision and mission matrix, the AI matrix, the achievement matrix, the asset register, the 3D briefs, the super-event research, and the acceptance scenarios.
Consult installed documentation, the offline wiki, vanilla precedents, and the current shared implementations through the reference workflow in `CLAUDE.md`.
Working labels are not finished localisation, and numeric tuning remains subject to evidenced balancing.

## Fixed design contract

- Event 84 is a Major, Chaos level 1, Peace High and Domestic Unrest High, fired once as an episode origin from one deduplicated major or player country.
  It replaces the legacy `events/084_pp.txt` +100 Political Power content; the catalog row is corrected through the workbook owner and export.
- Exactly two public country values, Influence and Reaction, independent of each other.
  At most three Event 84 national spirits, composed by the modifier precedence file.
  Orientation is never a mechanical penalty; only an explicit population policy changes future positive growth.
- Five response families, evidence-based adult character cases, peaceful and coercive transfers, three movement constitutions, three traditionalist programs, the negotiated settlement, and their aftermath.
  Existing countries keep meaningful national content; new authorities get complete country packages.
  High Influence and Reaction alone never start a civil war.
- Evolutions at 200/400/600 Chaos; Armed Peace also requires actual distinct repression.
  The four special formations train with real manpower and equipment after Armed Peace, except in the explicit manual setup; earlier emergencies use existing regular forces.
- Both Internationals form through lawful congresses and sovereign commitments, with commitments and votes instead of a third meter.
- The Gay World needs strictly more than 1000 Chaos, strictly more than 50% of authoritative living world population counted once per controlling state, the Rainbow International, meaningful organized territorial opposition, the enabled branch, and valid terminal ownership.
  Activation starts a campaign; victory requires the 180-day settlement.
- War for the Soul uses the reservation `SCN-031`, raw ID `31`; do not allocate a replacement.
  Four intensities with additive Chaos, conserved setup forces, and no mutation from previewing.
- No new all-country periodic loop without the user's permission.
  Shared wars, deaths, migration, famine, camps, condemnation, and Chaos each keep one owner (Part 12).

## Delegation

Route specialist work through `chaos-redux-subagents` with self-contained prompts carrying the event, slug, goal, constraints, source paths, allowed writes, known blockers, and the acceptance question.
Use `chaosx_repo_explorer` only where locations or ownership are unclear, `chaosx_scripted_system_architect` for the lifecycle, population, and shared-system seams, and the decision, focus, country-package, localisation, AI-probability, and event-completion auditors before completion claims.
Asset, portrait, 3D, super-event text and audio, and spreadsheet work go to their owners through the asset, super-event, and achievement prompts.
`chaosx_event_ui_worker` applies only if a later accepted change adds an event-owned window; the core design uses ordinary decision categories.
Use the improvement-loop planner after substantial implementation stages, not repeatedly while an addendum is unresolved.

## Checks

Follow the MCP retry limits and completion rules in `CLAUDE.md`.
For weighted logic, use `hoi4.probability_*` where it supports the script, otherwise calculate representative named cases from the actual script and state the assumptions.
Check technology and unit unlocks, equipment, and new-country inheritance against the installed and repository sources.
Register the four new subunits through the CXT idempotent setup contract in `docs/testing/chaosx_test_country.md`.
The acceptance scenarios are the behavior to implement and review against source; live-game validation belongs to the user, and agents do not launch the game.

## Finish

Report what was implemented, every simplification or fallback, and every remaining blocker, including portraits awaiting the user's finals and unresolved licensed audio or references.
