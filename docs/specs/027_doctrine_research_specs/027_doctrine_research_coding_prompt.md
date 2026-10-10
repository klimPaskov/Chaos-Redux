# Coding prompt: Event 027 Doctrine Research continuation

Event 027 is implemented.
This prompt covers the remaining work: the 2026-10-10 audit revisions R1 to R7 once the user accepts them, and the open evidence items.
Do not start R1 to R7 before the README records their acceptance.

## Read first

- `CLAUDE.md` and `.claude/skills/chaos-redux-events/SKILL.md`
- `docs/events/027_doctrine_research/overview.md`, the reference for the implemented source
- `docs/plans/027_doctrine_research_plans/agent_decisions_2026-10-04.md`, the accepted decisions D1 to D25
- part 2 (R1 to R5) and part 4 (R6, R7) of this package
- `events/027_doctrine_research.txt`, `common/scripted_effects/027_doctrine_research_effects.txt`, `027_doctrine_research_ai_effects.txt`, `027_doctrine_research_achievement_effects.txt`, `common/scripted_triggers/027_doctrine_research_triggers.txt`, and `localisation/english/027_doctrine_research_l_english.yml`

Other sessions may hold uncommitted edits in these files; read the working tree and keep their hunks out of your commit.

## Flow revisions

1. **R1.** Give the `.2` opening the domain options of `.3` and keep `.3` for later choices.
2. **R2.** Let a `.5` track option whose track holds a subdoctrine set the selection and run the step transaction directly, then open the result; a failed step returns to the rebuilt `.5`.
   Keep `.60` to `.77` and `.7` for empty-track assignment, adoption, and the combined Special Forces entry.
3. **R3.** Merge `.9` and `.10` into `.8`: offer "advance the same branch again" when `doctrine_research_selected_choice_is_valid` still holds for the same selection, "choose another domain", and the general staff option; after the last choice show the summary and close the curriculum.
4. **R4.** Add the civilian-death cost sentence to the Chaos Warfare adoption confirmation, reusing `CBRN_BALANCED_CHAOS_WARFARE_DESC` for the programme gates.
5. **R5.** Add the general staff option as the first option on the domain menu and the result page.
   It runs `doctrine_research_ai_resolve_active_batch` for the active curriculum only; that effect has no controller gate of its own, but its closing path completes the curriculum the AI way, so the human summary must be captured before `doctrine_research_complete_active_batch` clears it, and queued curricula then open normally.
   Receipts and achievement evidence stay unchanged.
6. **R6.** Replace the summary counters with one line per recorded action and the Milestones reached, built from the curriculum's consumed receipts.
   Keep the internal counters the achievements read.
7. **R7.** Trim domain and track option labels and tooltips to part 4's Visible values table.

Every change keeps the receipt transaction, revalidation, navigation rules, and choice-consumption rules of parts 1 and 2 intact.

## Evidence still open

- Probability: bind a multi-choice timeline for group E, record the zero-reset subdoctrine comparison, and run group F only with the complete automatic-selection pool.
  Route through `chaosx_ai_probability_auditor`.
- Live checks listed in the overview's Validation limits belong to the user; do not launch the game.

## Close-out

- Update `docs/events/027_doctrine_research/overview.md`, the acceptance checklist in this package, and the README changelog with the implemented revisions.
- Run `chaosx_localisation_auditor` on changed text and `chaosx_event_completion_auditor` against this package before a completion claim.
- If Event Details or evolution wording changes, record the workbook cells in `docs/plans/027_doctrine_research_plans/catalog_changes_pending.md` for `chaosx_spreadsheet_doc_worker`.
- Commit only the Event 027 hunks.
