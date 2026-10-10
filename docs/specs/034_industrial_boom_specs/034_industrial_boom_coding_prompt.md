# Event 34 Industrial Boom coding-agent prompt

## Goal

Replace the interim Event 34 stub with the Industrial Boom design in this package, keeping the implemented Event 35 handoff, supplier adapter and stable identifiers working throughout.
Disposition `implemented` (2026-10-10): the work order below was carried out, and [docs/events/034_industrial_boom.md](../../events/034_industrial_boom.md) describes the result.
Parts 1 to 10 of the [package README](034_industrial_boom_spec_index.md) are the requirements.
Do not reduce the event to a popup, one modifier or a political power shop.

## Read first

- The README, parts 1 to 10, the [decision map](034_industrial_boom_decision_map.md) and the [AI matrix](034_industrial_boom_ai_probability_matrix.md).
- `CLAUDE.md` and the skills it routes this work to: `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-mtth`, `chaos-redux-event-assets`, `hoi4-ideas-modifiers`, `hoi4-ai-strategies`.
- Current source: `events/034_industrial_boom.txt`, `common/ideas/034_industrial_boom_ideas.txt`, the two `034_` script-constant files, `common/scripted_effects/034_industrial_boom_collapse_handoff_effects.txt`, `common/scripted_effects/034_industrial_boom_adapter_effects.txt`, `common/scripted_triggers/034_industrial_boom_adapter_triggers.txt`, both `034_` localisation files.
- Event 35's side of the contract: `docs/events/035_great_depression.md`, `common/scripted_effects/035_great_depression_effects.md`, `common/scripted_effects/035_great_depression_region_effects.md` and `common/script_constants/035_great_depression_region_constants.txt`.

## Keep stable

- Namespace `chaosx.nr34`, entry `chaosx.nr34.1`, visible `chaosx.nr34.2`, landing `chaosx.nr34.3`, retry `chaosx.nr34.4`, news `chaosx.news.39`, idea id `industrial_boom` while it remains the package carrier.
- Repeatable registration in `chaosx_logic_effects.txt` and the catalog identity in the README.
- Every variable, flag and trigger Event 35 and Event 39 read: `industrial_boom_active`, `industrial_boom_overheating`, `industrial_boom_peak_overheating`, `industrial_boom_episode_id`, the `industrial_boom_snapshot_*` fields, the supplier flags and `industrial_boom_supplier_adapter_*` triggers.
- The Event 35 call contract in `industrial_boom_prepare_collapse_request` and the bounded retry.
- `chaos_redux_034_the_long_fall` and its Event 35 proof flag.

## Work order

1. Replace the opening: weighted target pool (part 1), starting Overheating from part 2, ranked Industrial Regions (part 4), and a staged package that replaces the static idea without stacking on it.
2. Replace the fixed 180-day landing with the lifecycle, bands, drift evaluation for active booms only, shocks and incidents (parts 1 and 2). No whole-world on-action.
3. Add the decision category, actions, missions and Emergency Production Halt (part 3), with dynamic costs and full AI equivalents.
4. Add projects, protection, outcomes, legacy budgets, exhaustion and repeat memory (part 4).
5. Fill every snapshot field from live state and deliver every region and spread state through the region contract (part 6).
6. Add the supplier-side output opportunity and the landing upgrade (part 7), and the famine, migration and contamination reads once their owners expose triggers.
7. Add the three evolutions with both entry paths, logs and Event Details rows (part 5), and the guarded Chaos sources (part 7).
8. Add the four remaining achievements (part 10), assets (part 9 and the asset prompt) and final localisation.

## Constraints

- All tuning values in `common/script_constants/034_industrial_boom_constants.txt`; durations that reject constants go through a variable first.
- No `<=` or `>=`; flags for true or false state; reusable logic in scripted effects and triggers, documented in the dynamic-effects docs when shared.
- Player-facing text follows part 9 and never mentions tuning or update history.
- Weighted surfaces follow the probability workflow in part 8 with before and after scenarios from the AI matrix.

## Reviews

Use the project subagents named in `CLAUDE.md` and the `chaos-redux-subagents` skill: the scripted-system architect for the drift, project and region-delivery helpers, the decision and AI probability auditors, the art and icon workers, the localisation auditor, the event completion auditor before any completion claim, and the spreadsheet worker once player-facing facts are final.
Afterwards create `docs/events/034_industrial_boom.md` (it does not exist yet) as the permanent event document, update the Event 35 event doc where the contract changed, the catalog workbook row (evolution names and details), and regenerate the CSV exports with `python .tools/export_event_catalog_csv.py`.

## Report

Return changed files and identifiers, requirement coverage against parts 1 to 10, probability evidence, AI and exploit results, asset and achievement coverage, documentation and workbook alignment, and every simplification, omission or blocker.
