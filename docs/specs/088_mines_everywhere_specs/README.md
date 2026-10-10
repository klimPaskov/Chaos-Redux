# Event 088: Mines everywhere

This is the source specification for the once-only global mine incident.
The [companion plans](../../plans/088_mines_everywhere_plans/) hold source receipts, engine questions, staged handoffs, acceptance tests and subagent briefs.

## Reading order

1. [Part 1](088_mines_everywhere_spec_part_1_core.md): the world change and the player's experience.
2. [Part 2](088_mines_everywhere_spec_part_2_ownership_and_coverage.md): ownership, the additive cap rule and current-map coverage.
3. [Part 3](088_mines_everywhere_spec_part_3_play_and_integration.md): naval play, AI, cluster membership and the Chaos impact map.
4. [Part 4](088_mines_everywhere_spec_part_4_presentation_and_assets.md): writing direction and the seven-image asset plan.
5. [Part 5](088_mines_everywhere_spec_part_5_achievements.md): two naval achievements and their observation requirements.

The goal, coding, asset and achievement prompts are implementation handoffs; none of their work has been done.
[`package_metadata/`](package_metadata/README_PACKAGE.md) keeps the original archive receipt as provenance only.

## Authority

The user's Event 088 brief overrides the stale catalog description and the old random-region event.
User decisions: the fixed 1,000-mine addition, global coverage, separate ownership, fire-once type, the normal cap, ordinary clearance, and Sudden Abundance membership at Medium severity.
Authored proposals awaiting acceptance: the +20 once-only Chaos award, the two achievement routes, the presentation approach, and the compatibility and duplicate-dispatch boundaries.
Event status remains To Be Reworked; no gameplay, art, workbook or in-game validation exists.

## Revision log

### 2026-10-10 spec audit

- Rewrote this README as a reading order and authority summary, removing repeated delivery and reading-coverage narration that the companion plans already record.
- Replaced Codex-specific subagent instructions (`fork_turns`, goal field) in the goal, coding and asset prompts with the repository's current subagent routing.
- Pass 2 review retained the design: the event's identity is one clear physical change resolved through native naval play, and adding response decisions or an event currency would be busywork on top of ordinary minesweeping.
