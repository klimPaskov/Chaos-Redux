# Coding prompt: Event 027 Doctrine Research continuation

Event 027 is implemented, including the flow revisions of the 2026-10-10 audit (direct track advance, the result page with the next step, the general staff option, the Chaos Warfare cost line, the outcome summary, and trimmed option labels).
This prompt covers the open evidence items.

## Read first

- `CLAUDE.md` and `.claude/skills/chaos-redux-events/SKILL.md`
- `docs/events/027_doctrine_research/overview.md`, the reference for the implemented source
- `docs/plans/027_doctrine_research_plans/agent_decisions_2026-10-04.md`, the accepted decisions D1 to D25
- `events/027_doctrine_research.txt`, `common/scripted_effects/027_doctrine_research_effects.txt`, and `localisation/english/027_doctrine_research_l_english.yml`

Other sessions may hold uncommitted edits in these files; read the working tree and keep their hunks out of your commit.

## Evidence still open

- Probability: bind a multi-choice timeline for group E, record the zero-reset subdoctrine comparison, and run group F only with the complete automatic-selection pool.
  Route through `chaosx_ai_probability_auditor`.
- Live checks listed in the overview's Validation limits belong to the user; do not launch the game.

## Close-out

- Keep the overview, the acceptance checklist, and the README changelog aligned.
- If Event Details or evolution wording changes, update the workbook row through `chaosx_spreadsheet_doc_worker`.
- Commit only the Event 027 hunks.
