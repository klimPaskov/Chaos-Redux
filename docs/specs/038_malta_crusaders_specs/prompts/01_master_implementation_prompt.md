# Master implementation prompt

You are the parent implementation agent for Chaos Redux Event 38, **Malta Crusaders**.

## Repository and source design

Work in the active Chaos Redux mod repository. Read these sources before editing:

- `AGENTS.md`
- every file under `docs/specs/038_malta_crusaders_specs/`
- relevant current files under `docs/plans/038_malta_crusaders_plans/`
- `chaos-redux-events`
- `chaos-redux-event-planning`
- `chaos-redux-improvement-loop`
- `chaos-redux-subagents`
- `chaos-redux-focus-trees`
- `chaos-redux-decisions-missions`
- `chaos-redux-event-assets`
- `chaos-redux-3d-model-pipeline`
- `chaos-redux-frame-animation`
- `chaos-redux-super-events`
- project portrait-production guidance
- relevant shared systems for Chaos, Deaths, Condemnation, famine, migration, camps, CBRN, event logs, clusters, scenarios, and world ends

Consult every required offline Paradox wiki page and current installed-vanilla documentation and precedent for each touched system. Keep vanilla read-only.

## Objective

Implement the entire accepted Event 38 specification without silent reduction. Preserve its classification, regional opening, three evolutions, custom unit families, Malta campaign, government routes, principalities, comeback route, hidden Teutonic and Atlantis routes, public Holy World ending, and manual Believers vs Nonbelievers scenario.

## Mandatory first pass

1. Inspect repository status and preserve unrelated work.
2. Use `chaosx_repo_explorer` with `prompts/02_repo_explorer_prompt.md` when touched files, carriers, precedents, or edit order are not already certain.
3. Use `hoi4.event_inspect` and event render or compare tools to map existing Event 38 and adjacent event ownership.
4. Use `hoi4.map_inspect` for every state registry and capital rule in `02_opening_release_and_map.md`.
5. Audit the Malta identity and every candidate carrier against vanilla, Chaos Redux, installed Workshop mods, and sibling local mods.
6. Inspect Event 3 Holy Realm, Event 40 Lawrence of Arabia, Event 126 Heroic Crusade, event clusters, triggerable scenarios, world-end registry, current Pope and Germany ownership, and the unit-provider registry.
7. Write an implementation ledger that maps every spec file and acceptance scenario to planned files and evidence.

## Architecture

Keep Event 38 ownership in event-scoped files unless an existing shared contract requires a neutral shared helper. Centralize tuning through script constants. Use one authoritative exact-state registry. Keep one idempotent release transaction, one principality transaction family, one terminal Holy World runtime, and explicit cleanup.

The player sees only Crusade Authority, Order Cohesion, and Sacred Legitimacy as persistent Event 38 values. Supporting scores remain hidden or qualitative. Do not expose debug ledgers.

Malta and its ordinary derivatives are human and use normal civilian systems. Add narrow event-routing markers when another event needs to exclude them. Do not mark them as actual nonhuman actors.

## Weighted logic

Before changing any weighted surface, dispatch `chaosx_ai_probability_auditor` with `prompts/09_ai_probability_auditor_baseline_prompt.md`. After the owner patches source, dispatch it again with `prompts/10_ai_probability_auditor_compare_prompt.md` and the same scenarios. This applies to AI route weights, event options, MTTH, random lists, demand selection, relic outcomes, principality behavior, Holy World alignment, Atlantis choice, and target selection.

## Event-owned GUI

The dedicated Crusade Council window is owned by Event 38. Lock exact GUI identifiers, files, entry point, states, resolutions, assets, and gameplay helpers before dispatching `chaosx_event_ui_worker` with `prompts/04_event_ui_worker_prompt.md`. The worker owns layout and visual evidence. The parent owns values, effects, costs, AI, and final integration.

## Focuses, decisions, and countries

Implement the route and country matrices completely. Use HOI4 MCP focus tools before and after source changes. Use technology tools for every custom technology and doctrine surface. Use the full decision register, varied concrete costs, readable mission objectives, active caps, dynamic targets, cleanup, and AI equivalents. Every fighting country needs a viable setup and reinforcement path.

Dispatch the focus, decision, and country auditors after meaningful implementation. Review and integrate every bounded patch and handoff.

## Assets

Lock consumers and identifiers before production. Split work by asset family using prompts 11 to 17. Do not let one agent create mixed asset packages. Every grounded portrait needs attributed source evidence. Every generated flag must be a flat design. Every custom unit needs distinct counters, source-only licensed sound roles, and the required 3D package. Every animated UI family needs genuine source frames and a static fallback.

Final runtime assets must leave the temporary Event 38 asset workspace before completion. Promote durable evidence, then delete the complete temporary workspace only after every runtime consumer and reference is verified.

## Hidden routes and terminal state

Keep Teutonic and Atlantis content absent from public Event Details, workbook fields, public evolution descriptions, and scenario controls. Apply exact route gates and exclusive leader ownership.

The Holy World public branch has its own stable registry row and toggle. Normal activation requires the approved continent proof, Papal ruler, 1000 Chaos, no active world end, and enabled branch. The manual scenario uses the same terminal runtime after a tightly scoped setup bypass raises Chaos into World Collapse.

## Finalization

Run localisation, probability, map, event, focus, technology, GUI, decision, country, asset, documentation, spreadsheet, and completion passes. Update only `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, then run `python .tools/export_event_catalog_csv.py`. Do not edit CSV exports directly.

Use the improvement loop after a meaningful tranche. Implement, promote, queue, or reject its addendum with a reason before another pass.

Do not claim completion while any accepted route, actor, unit, asset, super-event, audio cue, AI path, cleanup rule, workbook row, or required MCP evidence is missing. Produce the completion report described in `validation/completion_report_template.md`.
