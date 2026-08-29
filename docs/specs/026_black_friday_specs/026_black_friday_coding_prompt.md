# Event 26 implementation prompt

Implement the complete Chaos Redux Event 26 Black Friday specification at `docs/specs/026_black_friday_specs/`. Treat every mapped behavior, cost family, asset, log surface, evolution, achievement, audit, and documentation requirement as acceptance criteria.

Read `AGENTS.md`, all Event 26 spec files, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`, the relevant localisation and achievement rules, the required offline wiki pages, installed Vanilla documentation, and current Vanilla and Chaos Redux precedents. Use the mandatory HOI4 MCP event and probability workflows. If a required route is unavailable, record the exact blocker.

## Replace the old Event 26

Replace the current desert-industry Event 26 while preserving `chaosx.nr26.1` as the canonical entry. Remove or replace every stale desert script, localisation key, news reference, sprite reference, event-name mapping, debug mapping, comment, doc, and catalog entry. Keep ID 26 classified as Minor Fire-Once.

## Implement the lifecycle

Event 26 is unavailable below 200 chaos. Automatic selection reserves it globally and resolves the current timer without recording a fire. It waits for the first Friday at 200 chaos or higher. Selection on an eligible Friday may activate the same day. Friday activation records one event, adds minor pacing and major gain once, broadcasts one report to each human player, snapshots 50 percent off below 600 chaos or 75 percent off at 600 chaos when Evolution I is enabled, and starts a one-day expiry. Later chaos changes do not change the snapshot.

Use the existing bounded global daily event pulse. Do not add a new daily all-country iteration. Preserve reservation, snapshot, expiry, achievement progress, and refundable payment records across save and reload. Implement disable, force-trigger, multiplayer, tag-switch, and terminal cleanup exactly as specified.

## Build the reusable cost framework

Use `chaosx_scripted_system_architect` with `fork_context=false` for the universal source, quotation, rounding, affordability, payment, refund, display, and cleanup contracts. Black Friday multiplies the ordinary current payable cost. Apply deterministic upward rounding and keep every positive cost at one quantum or more. Zero stays zero. Rewards and penalties are not discounted.

Build the complete cost surface registry against the final implementation commit. Cover every reachable Vanilla and Chaos Redux purchase surface through native composition, shared scripted payment, or complete normal, 50 percent, and 75 percent static variants. Record exact evidence for every engine-inaccessible surface. A sample list is not accepted.

Displayed and paid costs must agree. Refunds return the amount paid. Discount and record each component of a multi-resource transaction separately, while committing the logical action once. Assign one primary achievement family per logical transaction. Static variants share lifecycle state and expose one player and AI candidate. Existing requirements, cooldowns, reserve floors, targets, laws, routes, project rules, and action limits remain active.

## AI and audits

The sale changes affordability, not strategic validity. Preserve reserve floors and invalid-target zero weights. Run `chaosx_ai_probability_auditor` for every changed weighted surface, using the named Event 26 scenarios and before-to-after comparisons. Run the decision and mission auditor for costs, variants, cleanup, and exploits. Run the localisation auditor across every visible Event 26 and cost-source string.

## Presentation, assets, and achievement

Implement the actorless Event 26 history row, Event Details premise, truthful availability and reserved status, Evolution I preview and log, temporary human-player active status, cost-source text, and debug mappings. Use the Event 26 asset prompt and wire the report image, status icon, and achievement triplet. Implement the `Five Departments` working achievement contract using the final family registry.

## Documentation and catalog

Update `docs/events/026_black_friday.md`, the universal cost system documentation, public helper documentation, asset crosswalks, and completion evidence. Edit only `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, replace the old ID 26 row, resolve the duplicate no-ID Black Friday row, save the workbook, and run `python .tools/export_event_catalog_csv.py`. Mark the implemented row `Needs Testing` until live acceptance passes.

## Completion

Run the full acceptance scenarios in Part 8. Use `chaosx_event_completion_auditor` before claiming completion. Keep Event 26 disabled by default during implementation and remove it from the rework-disabled list only in the completed change. Report every file changed, registry disposition, MCP result, probability result, live scenario, asset, catalog update, blocker, and simplification. No fallback or partial cost sample may be hidden as completion.
