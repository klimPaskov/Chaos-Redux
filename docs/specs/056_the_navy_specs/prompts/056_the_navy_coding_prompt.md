# Coding Prompt: Event 056 The Navy

Implement the complete Chaos Redux Event 56 specification under `docs/specs/056_the_navy_specs/`.

Read every specification part in order, then read:

- `prompts/056_the_navy_commissioning_prompt.md`
- `prompts/056_the_navy_asset_prompt.md`
- `prompts/056_the_navy_achievement_prompt.md`
- `quality/ai_probability_scenario_matrix.md`
- `quality/catalog_alignment_brief.md`
- `quality/spec_coverage_matrix.md`

Follow `AGENTS.md`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-subagents`, and `chaos-redux-improvement-loop`. Consult the required offline wiki pages, vanilla documentation, current vanilla naval implementation, and existing Chaos Redux precedents before editing. Use the HOI4 MCP event and probability routes where required.

## Required event result

Register Event 56 as a Chaos level 1 Minor Repeatable event. One firing must process every valid country with direct usable coastline, give each one independently rolled coherent naval package, handle human and AI commissioning, record one global event history row with no actor, and clean up all temporary work.

Implement all baseline package identities, their legal compatibility branches, compact through heavy bands, global hull-equivalent allocation, direct entity limits, one-to-three-port commissioning, emergency coast-without-port handling, package support, task-force organization, repeat scaling, bounded cohort memory, and exploit guards.

Package identity must remain random. Do not tailor it to doctrine, ideology, production, enemy composition, or current strategy. Safety scaling may alter size but cannot erase the defining identity.

## Commissioning

Implement Full Commissioning, Phased Commissioning, and conditional Break Up outcomes exactly as specified. Human recipients receive one personal report. AI recipients use the same result set through scenario-aware handling. Do not add a permanent decision category, persistent public custom value, or dedicated scripted GUI.

Delayed tranches and emergency ports must resolve once, survive save and reload, reselect a lost port at most once, and cancel cleanly when no valid recipient remains.

## Evolutions and repeats

Implement all three evolution stages at 200, 400, and 600 Chaos through normal evolution pacing and enable controls. Evolution activation changes future rolls and gives zero Chaos. It never grants ships retroactively.

Evolution II and III content must use explicit owner registration and fail closed. Event 56 grants no research.

Implement first through fourth-or-later recipient scaling and the Evolution I late-repeat floor. Preserve recipient history through cosmetic and ideology changes.

## Chaos impact

Implement the complete one-time map:

- +5 for first manifestation
- +5 for the first firing with at least 25 successful recipients
- +10 for the first actual experimental delivery
- +15 for the first actual impossible package
- +3 for the first previously landlocked country later receiving a package after gaining direct usable coast

Use repeat guards. Do not double count shared war, tension, death, famine, blockade, nuclear, or other generic sources. Do not add Event 56 Chaos per ship, recipient, convoy, aircraft, battle, blockade, or evolution activation. Do not invent a negative reversal.

## Clusters

Implement Event 56 as a Medium member of Sudden Abundance and Military Preparation. Add the full proposed memberships and per-membership severities only after inspecting the current cluster registry and authoritative workbook structure.

One selected Event 56 can enter at most one cluster. One cluster transaction can apply Event 56 once. Preserve shared pacing and member history rules. Run probability inspection and comparison for dual-cluster entry and optional member participation.

## Connections

Implement bounded integration with Event 54 technology state, Event 55 port and logistics state, Event 42 support adapters, Event 32 owner-registered naval assets, and Famine's real blockade requirements. Do not call these events, count them as fired, grant their owned content without permission, or apply famine directly.

## AI

Implement the full AI strategy and task-force handling from the spec. Spawn `chaosx_ai_probability_auditor` before weighted changes, apply the owner patch, then run `hoi4.probability_compare` with the same scenarios. Do not claim exact probabilities from an incomplete pool.

## Assets and achievements

Create and wire all four report images and all three achievement icon triplets through the proper asset workers. Implement all three achievements with bounded cohort tracking, disqualifiers, deadlines, combat proof, save persistence, localisation, docs, and icons.

Do not add custom ship models, custom counters, portraits, flags, focus trees, super-events, animation, or audio. Ordinary package ships must use supported implemented assets.

## Text and UI

Write final player-facing localisation from the directions in Part 7. Keep the source unresolved. Remove developer-facing, debug, update-history, raw-variable, and formula wording. Keep the global report, personal report, Event Details, History, Evolutions, cluster details, achievements, and catalog wording aligned.

## Documentation and catalog

Update event docs, event registration, logs, evolution previews, cluster surfaces, assets, achievements, and the authoritative `docs/spreadsheets/chaos_redux_events_catalog.xlsx` workbook. Correct the stale Event 56 row and add the two cluster definitions with unused IDs after registry inspection. Never edit the three CSV exports directly. Run the catalog exporter after the workbook save.

## Completion route

Use `chaosx_scripted_system_architect` for reusable allocation and registration logic, the asset workers for final files, `chaosx_localisation_auditor` for visible text, `chaosx_spreadsheet_doc_worker` for the workbook, and `chaosx_event_completion_auditor` before completion.

Near completion, spawn `chaosx_improvement_loop_planner` with a complete context-free prompt. Resolve its addendum, queue or reject it with a reason, or receive a closure handoff. Re-run final event, probability, localisation, asset, documentation, and catalog checks afterward.

Do not use unapproved fallbacks or reduce the event to a few static ship grants. Report every blocker or simplification. Do not claim completion until every acceptance criterion in Part 8 is satisfied.
