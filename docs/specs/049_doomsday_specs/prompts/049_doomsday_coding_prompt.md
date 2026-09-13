# Event 049 Doomsday Coding Prompt

Implement Event 049, **Doomsday**, to the full specification under `docs/specs/049_doomsday_specs/`.

Read every specification, prompt, diagram, research note, quality matrix, and blocker note in the package before editing. Follow `AGENTS.md`, the required offline Paradox wiki pages, current vanilla documentation, vanilla precedents, existing Chaos Redux precedents, and all relevant project skills.

## Event identity

- Event ID: `49`
- Entry namespace: preserve the project `chaosx.nr49.1` contract.
- Type: Major.
- Chaos level: 4.
- Cluster: none.
- Replaces the old Mass Panic identity.
- Evolutions: The Last Calendar at 800 or more Chaos, and Nothing After Tomorrow at 1000 or more Chaos.
- Public world end: The Final Vigil at 1000 or more Chaos with event-owned readiness.

## Core non-negotiables

- Generate one persistent public predicted date roughly two to four years after firing.
- Expose only two persistent public values, Doomsday Conviction and Time Until the End.
- Keep local conviction, society organization and currents, suppression backlash, institutional continuity, peace pressure, and terminal readiness hidden or qualitative.
- Use one phased decision category with static stage pictures, no full scripted mechanic window.
- Show no more than six primary actions and three active missions in one phase.
- Use real costs with a maximum of four spendable cost types per action.
- Do not create mass country tags for Doomsday administrations.
- Doomsday administrations remain human transformations of existing countries.
- Do not add Doomsday administrations to special or nonhuman classifiers.
- Do not automatically white-peace every war.
- Keep asset production within the listed two-dimensional event, interface, focus, idea, decision, achievement, and super-event families.
- Evolution activation gives zero Chaos.
- Do not double count generic war, peace, deaths, contamination, famine, migration, annexation, puppeting, or nuclear Chaos.
- The predicted date can pass without a physical apocalypse.
- The failed-date aftermath is a full reconstruction phase.

## Full implementation scope

Implement and align:

- Entry event, country response events, report events, news events, final-week chain, failed-date chain, evolution events, government-transfer events, Final Assembly events, and terminal sequence.
- Random-event registration, type mapping, level gating, default enable state, actor mapping, history, Event Details, evolution catalog, evolution history, public world-end row, branch toggle, and status text.
- Persistent date generation and scripted localisation.
- Global and local Conviction simulation with bounded country weights.
- Hidden society organization and current composition.
- Six posture packages and one bounded emergency realignment.
- Full phased decision and mission system from the decision prompt.
- Contextual peace pressure, armistice, defensive-only service, prisoner policy, arms conversion, and Nothing Left to Lose military window.
- Construction, research, education, recruitment, finance, labor, transport, shelter, reserve, and institutional effects.
- Famine, Migration, Deaths, Condemnation, Air Cleanliness, disaster, and other event integrations through owner-safe bounded contracts.
- Both evolutions, including pre-fire evolved openings, pacing, enable behavior, logging, and gated content.
- National Doomsday administration transformations and leadership handling.
- The complete shared 18 to 24 focus emergency branch from the focus prompt.
- Preparatory Final Assembly, full membership, observer state, holdout state, five Assembly currents, and current influence.
- All five Final Vigil readiness paths and valid mixed-path proof.
- World-end commitment, unique super-event, 30 to 90 day consolidation, contextual war handling, and terminal state.
- Final-day sequence, Conviction collapse, movement splits, government outcomes, reconstruction, and one bounded revised-date branch.
- All ten achievements.
- All required static visual assets, institutional portraits where used, and both complete super-event packages.
- Event docs, super-event docs, music catalog, Event Details, final localisation, and the authoritative event catalog workbook.

## Shared system safety

Use `uses_normal_civilian_systems` for ordinary country eligibility and fail closed on invalid state.

Reuse documented dynamic helpers when they fit. Event-owned orchestration belongs in Event 049 files and documentation. Add a shared dynamic helper only when it has genuine cross-system use and document its full contract in the registry.

Avoid new daily whole-world iteration. Use bounded registered sets, event-owned scheduled pulses, existing on-actions, or country-local processing.

Real deaths must use the shared population and Deaths transaction. Real population movement must use Migration. Famine, Condemnation, and Air Cleanliness keep their own ledgers.

## AI and probability

Every AI weight, MTTH, random list, target weight, option chance, incident pool, date distribution, evolution timing, peace acceptance, takeover route, focus plan, terminal path, and failed-date response must use the named scenarios in `quality/049_doomsday_probability_scenarios.md`.

Spawn `chaosx_ai_probability_auditor` before a weighted patch. Establish baseline evidence with `hoi4.probability_inspect` and the proper evaluation tools. Apply the owner patch. Run `hoi4.probability_compare` with the same scenarios.

Use mandatory MCP event and focus inspection, rendering, and comparison. Record exact blockers if a required route is unavailable.

## Assets and super-events

Follow the asset and super-event prompts.

Do not implement unresearched final quotes, cultural remarks, titles, or audio. Treat missing source, license, final WAV, sprite, or settings-aware playback as a blocker.

Every required visual asset must be final, processed, placed, wired, documented, and reviewed. No primitive or copied placeholder is acceptable.

## Localisation and writing

Write finished player-facing text from the specification direction. Do not paste planning labels or process notes.

Keep event, decision, focus, achievement, GUI, Event Details, docs, and workbook wording aligned. Follow the project prose rules, including the ban on em dashes, semicolons, staccato dramatic filler, and generic contrast formulas.

## Catalog

Edit only `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, then run `python .tools/export_event_catalog_csv.py`.

Update Event 49 to Doomsday, Major, Chaos level 4, no cluster, two evolutions, and The Final Vigil. Keep status at To Be Reworked until the implementation is complete and audited.

## Required subagents and audits

Use the correct bounded subagents with isolated self-contained prompts.

At minimum, use:

- `chaosx_decision_mission_auditor`
- `chaosx_focus_tree_auditor`
- `chaosx_localisation_auditor`
- `chaosx_ai_probability_auditor`
- `chaosx_event_completion_auditor`
- `chaosx_spreadsheet_doc_worker`
- narrow asset and super-event workers as required

Before treating the goal as near complete, spawn `chaosx_improvement_loop_planner`. Resolve its addendum by implementation, spec promotion, explicit queue with reason, or rejection with reason. A closure handoff still requires parent review.

## Completion

Keep iterating until every accepted requirement is implemented to its fullest extent.

Do not claim completion because the entry popup, decision category, or terminal super-event works in isolation.

The final report must list files changed, event surfaces, decisions and missions, focus route coverage, government transformations, AI and probability evidence, Chaos and shared-system transactions, assets, super-events, achievements, docs, workbook alignment, meaningful validation, and every remaining blocker or simplification.
