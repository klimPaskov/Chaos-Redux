# Parent coding prompt: implement Event 043 Monsters from the Deep

Implement Chaos Redux Event 043 from the complete specification package at:

```text
docs/specs/043_monsters_from_the_deep_specs/
```

This is a full implementation task. Do not replace the event with a smaller prototype.

## Required source reading

Before editing, read in full:

- `AGENTS.md`
- every file under `docs/specs/043_monsters_from_the_deep_specs/`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-event-planning/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `.agents/skills/chaos-redux-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-frame-animation/SKILL.md`
- `.agents/skills/chaos-redux-super-events/SKILL.md`
- `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/references/portrait-production.md`
- current Event 043 source and every call site
- current event, scenario, world-end, country, unit, threat, Deaths, Migration, Famine, Event Logs, and Event Details registries
- required offline Paradox wiki pages
- installed vanilla documentation
- direct vanilla precedents
- direct current Chaos Redux precedents

Use the HOI4 MCP for event chains, focus trees, weighted logic, GUI surfaces in scope, technology if unexpectedly touched, and map work. Do not treat source-only review as equivalent.

## Fixed design

- Event ID `43`
- name Monsters from the Deep
- replaces Massive Flood
- Major event
- Chaos level 3
- no cluster
- sixteen full monster countries
- one unique irreplaceable apex division per monster
- six shared support families
- no ordinary recruitment, manpower, equipment production, or conventional monster army loop
- two public monster values, Hunger and Sea Bond
- physical inland-depth system
- Jiaolong river exception
- Cipactli marsh and lowland exception
- one monster decision category
- one ordinary-country response category
- no dedicated Event 043 scripted GUI
- two evolutions
- one public Cthulhu terminal row
- five alternate terminal readiness paths
- Cthulhu as leader only
- one manual scenario with Warring Titans and Pact of the Deep types
- four scenario intensities
- three super-event roles
- ten achievements
- full asset, AI, documentation, log, and catalog coverage

Do not add a seventeenth monster, another world end, a custom GUI, a technology tree, a conventional navy, or apex resurrection without a separately accepted design addendum.

## Preflight blockers

Before implementation work, prove:

1. seventeen collision-free stable tags against vanilla, Chaos Redux, installed Workshop mods, and sibling local mods
2. exact state and spawn-province pools for all sixteen identities
3. a generated saltwater-coast and inland-depth registry
4. current free append-only IDs for the manual scenario and public world-end row
5. an enforceable way to block apex training, duplication, template conversion, splitting, voluntary deletion, and recreation
6. one reliable apex-death and terminal-transfer identity system
7. complete package-readiness gating so unfinished identities never enter selection

If one gate fails, record the exact blocker. Do not improvise a silent fallback.

## Legacy replacement

Search every reference to:

- `chaosx.nr43`
- `043_massive_flood`
- `Massive Flood`
- `Massive flood`
- Event ID `43` in event arrays, logs, clusters, scenarios, and world-end registries

Move Event 43 from the repeatable registry to the Major registry. Replace old localisation and documentation. Resolve direct Event 70 calls to the old flood entry through the disposition in the legacy replacement map.

## Architecture

Keep Event 043 orchestration in event-owned files. Add neutral shared helpers only when several unrelated systems need them.

Use:

- owner-specific script constants
- stable markers
- sparse active monster arrays
- bounded event-owned pulses
- exact population transactions
- lair, receipt, pact, apex, and terminal ledgers
- idempotent setup and cleanup
- save-repair logic that fails closed

Do not add unrestricted daily, weekly, or monthly every-country or every-state iteration.

Extend the shared special-country and actual-nonhuman classifiers with owner-set Event 043 markers. Add and document the Event 043 world-threat source.

## Country and unit implementation

Create all sixteen full monster tags and one terminal tag. Each full package needs country identity, leader, static and animated portrait, flag triplet, focus tree, apex unit, support permissions, ideas, decisions, AI, surrender, remnant, and terminal transfer.

Create all six support families as owner-side registered nonhuman unit families. Add CXT setup for every new subunit and concrete equipment definition, if any.

Apex and support units use zero ordinary manpower and no normal equipment. Prove unit behavior and caps.

## Focus trees

Implement sixteen unique trees, one Cthulhu tree, and one remnant tree.

Use the route matrix and lane diagram. Add Focus Navigation, accurate filters, clean geometry, varied rewards, route-specific AI, decision integration, idea lifecycles, crisis content, and terminal reveals.

Run MCP inspect, render, rewrite where needed, and compare. Spawn `chaosx_focus_tree_auditor` after each meaningful batch. Route every focus weight through the probability audit cycle.

## Decisions and missions

Implement the decision and mission map with strict visible-action and active-mission limits.

Use real costs, exact targets, concise tooltips, AI equivalents, and complete cleanup. Feeding must debit real state population through the shared Deaths transaction. Evacuation uses Migration. Event 043 must not debit the same people twice.

Spawn `chaosx_decision_mission_auditor` and `chaosx_ai_probability_auditor`.

## Pacts, evolutions, and terminal route

Implement proposal, truce, compact, abyssal faction, betrayal, and cleanup.

Implement both evolutions in pre-fire and post-fire modes. Evolution state adds zero Chaos.

Implement one Cthulhu public world-end row. The five readiness paths are alternate proofs for that one row. Use confirmation receipts and fail-closed terminal preflight.

Cthulhu transfer must snapshot and dispose of every full monster country, living apex, support unit, state, lair, subject, war, and receipt exactly once. Dead apexes stay dead. Old tags retire. Individual terminal apex death weakens the union. Last-apex death collapses it.

## Manual scenario

Register the next verified free scenario ID. Add Warring Titans and Pact of the Deep types.

Low creates 2, Medium 5, High 10, Maximum 16. A requested count must be exact or the launch reports a blocker. Clear every scenario bypass after setup.

Maximum Pact reaches terminal state only after World Collapse and according to the documented public-toggle behavior.

## Assets

Route portraits to `chaosx_portrait_creator`, generated scenes to `chaosx_generated_event_art`, icons and counters to `chaosx_icon_artist`, archival research to `chaosx_asset_source_researcher`, and all 3D packages to `chaosx_3d_model_pipeline`.

Every custom unit needs its own model package, substantive actions, sourced sound package, and bespoke counter. Use Meshy 7 and the 3D hard gates. Do not accept static models or reused counters.

Use real source frames for animation. A GIF is review-only.

## Super-events

Produce:

- global Event 043 opening
- Cthulhu's Dominion
- eligible global defeat aftermath

Use text and audio research specialists. Every final cue is a unique licensed musical recording with full sound wiring and canonical catalog entry.

## AI and probability

Use the named scenarios in `matrices/043_probability_scenario_matrix.md`.

Run baseline inspection and evaluation. Apply tuning through the owning surface. Run compare with identical scenario IDs. Distinguish exact, bounded, sampled, score-only, and unresolved evidence.

## Documentation and catalog

Keep specs, implementation docs, event logs, Event Details, localisation, assets, audio docs, and the authoritative workbook aligned.

Edit only `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, then run the exporter. Never edit the CSV exports directly.

Use `chaosx_documentation_curator` before final audit and `chaosx_spreadsheet_doc_worker` after final player-facing text exists.

## Completion

Run every scenario in `matrices/043_acceptance_scenarios.md` that can be proven in the current environment. Preserve honest blocked and needs-user-review states.

Before claiming completion, run:

- country audit
- focus audit
- decision audit
- localisation audit
- probability compare
- event completion audit

Write a concrete completion report listing files changed, runtime systems, models, assets, sounds, balance evidence, MCP evidence, scenario results, docs, workbook updates, and every remaining blocker.

Do not claim completion while any required monster, route, unit family, model, animation, counter, sound, portrait, flag, decision, mission, evolution, terminal path, scenario intensity, achievement, localisation, doc, or catalog row is missing.
