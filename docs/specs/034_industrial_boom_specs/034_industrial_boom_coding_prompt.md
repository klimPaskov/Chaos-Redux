# Event 34 Industrial Boom coding-agent prompt

## Goal

Implement Event 34 Industrial Boom as the complete Minor Repeatable economic system defined by the accepted specification pack under `docs/specs/034_industrial_boom_specs/`. Preserve every mapped gameplay surface, cross-event contract, AI rule, asset need, achievement, documentation requirement, and acceptance scenario. Do not reduce the event to a popup, one dynamic modifier, or a small set of political power purchases.

## Source of truth

Read the full package before editing:

- `034_industrial_boom_spec_index.md`
- specification parts 1 through 10
- decision map
- AI probability matrix
- research notes
- asset prompt
- achievement prompt
- decision and mission prompt
- source-reading ledger and subagent review

Then read `AGENTS.md`, all current owner skills, the relevant offline Paradox wiki pages, installed vanilla documentation, vanilla precedents, current Event 34 and Event 35 files, shared event systems, dynamic effects and triggers, and the authoritative event catalog workbook.

The working labels in the specification are structural identifiers and writing directions. Write final in-world localisation during implementation. Do not paste planning prose into the game.

## Non-negotiable event identity

- Entry event remains `chaosx.nr34.1`.
- Classification remains Minor Repeatable.
- Chaos level remains 1.
- The event targets one valid random major country or one player-controlled country, including a non-major player country.
- A country with an active Industrial Boom is excluded.
- Special Chaos actors, actual nonhuman economies, and countries without normal civilian systems are excluded.
- Costs, effects, project capacity, and lasting rewards scale to the target's real economy.
- Event 34 remains unclustered unless the user separately accepts a cluster change after the event exists.

## Live repository migration

The current repository contains legacy Event 34 and Event 35 stubs. Preserve stable identifiers unless every reference is migrated together:

- Event 34 namespace `chaosx.nr34`, entry `chaosx.nr34.1`, visible event `chaosx.nr34.2`, idea `industrial_boom`, and opening news slot `chaosx.news.39`.
- Event 35 namespace `chaosx.nr35`, entry `chaosx.nr35.1`, visible event `chaosx.nr35.2`, idea `great_depression`, and news slot `chaosx.news.40`.
- Both events remain registered in the repeatable-event array.

The existing 180-day Industrial Boom idea and 365-day Great Depression idea are legacy stub behavior. Replace their fixed-duration resolution with the accepted dynamic lifecycles. Do not stack the old static modifier package under the new Overheating system. The existing Industrial Boom idea grants research speed and broad resource growth, but those effects are not mandatory baseline promises. Civil-war behavior must use the explicit lifecycle and state-project contract instead of relying only on the current idea inheritance block.

## Core player loop

Apply an immediate, intentionally extreme economic shock that changes production and construction planning. Open one compact decision category and manage one public value, `Overheating`, on a 0 to 100 scale.

The category shows current Overheating, trend, next threshold, current phase, reserve status, and state target when relevant. Hidden contributors include labor, material, logistics, maintenance, speculation, structural progress, and exposure. Do not expose those as additional persistent public counters.

Implement the baseline phases and their real transitions:

1. Ignition
2. Expansion
3. Strain
4. Landing or collapse

The baseline must support controlled landing, rough landing, forced landing, and terminal crash without any evolution enabled.

## Overheating

Use the accepted threshold bands and central tuning constants. Overheating changes through an event-owned active-country schedule and immediate actions or exact external shocks. Do not create an unauthorized recurring whole-world country scan.

The drift model must react to output intensity, construction expansion, project load, supply, fuel, trains, convoys, trade access, infrastructure, state loss, bombing, blockade, disasters, stability, war state, reserve capacity, protection, previous decisions, evolution, and repeat memory. The public tooltip summarizes actionable causes without exposing a full internal ledger.

At 100, resolve the crash immediately through the Event 35 handoff. Prevent duplicate resolution.

## Decisions, missions, and state projects

Implement every action and objective from the decision prompt. Keep normal visible actions within the accepted budget. Costs use no more than four spendable types per action and favor civilian capacity, equipment, logistics, fuel, stability, output sacrifice, and time.

Create a sparse owner-side project registry for Industrial Regions. Projects need stable identities, phase state, completion receipts, interruption and transfer rules, landing conversion, Event 35 inheritance, and cleanup. Do not infer project history from current buildings.

Permanent development comes from completed projects and landing quality. Apply country and state legacy budgets, repeat diminishing returns, and anti-transfer protections. Event 34 must not become an uncapped factory, building-slot, infrastructure, or resource farm.

## Evolutions

Implement three true evolution stages:

- Evolution I, Speculative Mania, available at Rising Chaos
- Evolution II, The Industrial Miracle, available at Chaos Tier
- Evolution III, Runaway Industrialization, available at Totalen Chaos

Each evolution supports active-event entry and pre-fire evolved opening. Use dynamic pacing, shared evolution logging, actor mapping, enable and disable controls, and stage-specific Event Details text. The event does not need to fire again for an active boom to receive an enabled evolution.

Evolution activation gives zero Chaos. Add Event 34 Chaos only after concrete abnormal outcomes such as a first impossible expansion, a completed Miracle network, material runaway spread, or catastrophic Event 35 handoff. Guard repeat sources with one-shot thresholds, distinct-region receipts, or diminishing returns. Do not duplicate generic Chaos from deaths, war, annexation, contamination, or world tension.

## Event 35 handoff

Event 35 owns one reusable depression-start and deepening API. Event 34 calls it for the same target country after freezing the boom snapshot and removing boom-only modifiers.

Carry:

- source is Industrial Boom collapse
- firing identity
- highest active evolution
- direct evolution floor
- peak and final Overheating
- boom intensity
- reserve condition
- landing failure state
- completed, protected, unfinished, and speculative region receipts
- relevant external shocks
- repeat history

Inheritance is direct:

- baseline crash starts baseline Event 35
- Evolution I crash starts Event 35 at Evolution I
- Evolution II crash starts Event 35 with Evolutions I and II
- Evolution III crash starts Event 35 with Evolutions I, II, and III plus very high starting Depression Severity

If Event 35 is already active, raise and deepen the existing crisis. Never create duplicate categories or modifiers. The chained handoff is a consequence of Event 34 and does not count as a second global pacing event.

The shared call must fail closed. A failed handoff must not leave active boom bonuses, a half-cleared category, or duplicate history.

## Cross-system integration

Implement exact, bounded adapters for the systems mapped in part 7. Important connections include:

- shared event history and Event Details
- Chaos Meter and Chaos History
- Event 35
- economic event conflict rules
- natural disasters
- bombing and nuclear or thermonuclear damage
- blockade, convoy, port, rail, fuel, and trade disruption
- Resources Found when an exact state or country connection exists
- humanitarian and migration pressure where boom concentration or collapse creates a valid context
- air cleanliness and environmental pressure only when an actual registered source exists
- state ownership and control changes

Use existing dynamic effects, triggers, and transaction contracts before adding new helpers. New reusable APIs require full registry documentation in the same change.

## AI and probability

Implement the five AI profiles and every named scenario ordering from the AI matrix. AI actions must depend on war urgency, usable demand, logistics, state exposure, stability, reserve condition, Overheating, evolution, project value, repeat history, and expected landing quality.

For every AI weight, random incident pool, target selection, evolution pacing surface, and weighted outcome:

1. run `chaosx_ai_probability_auditor` for named baseline scenarios
2. apply the owner patch
3. rerun the same scenarios with `hoi4.probability_compare`

Do not claim an exact probability from an incomplete candidate pool.

## Presentation, assets, and writing

Follow the full asset prompt. Produce the report image, category picture phases, category icon, decision and mission icons, project and state icons, idea lifecycle icons, Overheating and trend visuals, landing visuals, and achievement triplets. Route generated non-icon art to `chaosx_generated_event_art` and icons to `chaosx_icon_artist`. Use the exact vanilla reference family for each consumer. Final runtime assets must be processed, placed, wired, documented, and free of temporary workspace references.

Use the ordinary decision category presentation unless a formal design exception proves it insufficient. A new event-owned scripted GUI requires `chaosx_event_ui_worker` and full MCP before-and-after evidence.

Write final localisation from the viewpoint and tone directions in part 9. Keep it concrete and in-world. Explain visible costs, thresholds, and consequences. Preserve uncertainty around hidden incidents. Do not use process history, tuning notes, or future spoilers in player-facing text.

## Achievements

Implement all six achievements from the achievement prompt with bounded history receipts, exploit disqualifiers, final localisation, icon triplets, documentation, and route-specific checks. Do not reduce them to generic completion checks.

## Documentation and catalog

Update:

- permanent Event 34 documentation
- reusable API documentation
- Event 35 documentation for the shared handoff
- Event Details and evolution catalog surfaces
- event history actor and consequence mapping
- asset and audio documentation where applicable
- authoritative `docs/spreadsheets/chaos_redux_events_catalog.xlsx`

After the workbook update, run the repository exporter. Never edit the three catalog CSV exports directly.

## Required subagent and MCP workflow

Use context-complete, isolated prompts for the project subagents. At minimum the final implementation requires:

- `chaosx_scripted_system_architect` for the Overheating, project, and Event 35 APIs
- `chaosx_decision_mission_auditor`
- `chaosx_ai_probability_auditor` before and after weighted changes
- `chaosx_generated_event_art`
- `chaosx_icon_artist`
- `chaosx_localisation_auditor`
- `chaosx_documentation_curator` when implementation handoffs become difficult to reconcile
- `chaosx_improvement_loop_planner` after a meaningful implementation tranche
- `chaosx_event_completion_auditor` before completion
- `chaosx_spreadsheet_doc_worker` after final player-facing implementation facts exist

Use the HOI4 MCP event, probability, decision, GUI, and map routes for every supported in-scope surface. Missing required evidence is a blocker for the corresponding completion claim.

## Final acceptance

Run every acceptance scenario in part 10, including baseline success, rough landing, collapse, all evolved openings, active evolution, existing depression, repeat firing, state transfer, annexation, civil war, invalid target pool, external shocks, AI profiles, achievement positive and negative cases, save continuity, and exploit controls.

Return:

- files changed
- identifiers and APIs added
- full requirement coverage matrix
- event and decision flow evidence
- probability comparison evidence
- AI scenario results
- asset coverage and final paths
- achievement coverage
- documentation and workbook alignment
- accepted improvement addendum disposition
- task-specific validation findings
- every simplification, omission, fallback, substitution, blocker, or unimplemented requirement

Do not claim completion while a mapped mechanic, evolution, decision, state project, inheritance field, AI path, asset, achievement, localisation surface, document, workbook row, or acceptance scenario is missing.
