# Event 53 Implementation Prompt

Implement Chaos Redux Event 53 from every file under `docs/specs/053_mysterious_man_specs/`. Treat the package as accepted source design.

## Required preparation

Read `AGENTS.md`, the complete Event 53 spec pack, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-subagents`, and the relevant parts of `chaos-redux-improvement-loop`. Read the required offline Paradox wiki pages and installed vanilla documentation before editing engine-facing files. Inspect at least one existing Chaos Redux Fire-Once event with recurring country follow-ups, the current Event 53 namespace, event registration, Event Details, evolution logging, and actor mapping.

Use the HOI4 MCP event tools before editing. Use the probability tools for every target, demand, and consequence selection surface. Preserve unrelated worktree changes.

## Core implementation

Retain `chaosx.nr53.1` as the canonical parent identity unless the existing namespace proves a conflict. Register Event 53 as Minor Fire-Once, Chaos level 1, with no cluster.

Select one valid human-controlled ordinary country uniformly. Use the shared special-country and nonhuman classifiers. Require at least one owned state. Store one persistent target and one recovery marker. Recurring visits are country-scoped delayed follow-ups. Do not add a daily, weekly, or monthly whole-world scan.

The chain survives save and reload, ideology changes, cosmetic tags, subject changes, faction changes, and capital movement. Pause visits when the target is not human-controlled. Resume one visit when human control returns. End cleanly on country extinction or incompatible nonhuman transformation. Transfer only through an explicit legal-successor adapter supplied by the owner that created the successor. Never infer or randomly choose a replacement.
An unrelated `world_end` flag does not cancel the recurring chain while the target remains valid. Let owner adapters exclude packages that conflict with the active terminal scenario.

Implement exclusive lifecycle states for scheduled, paused, present, resolving, and transferring behavior. Use sequence IDs and idempotent receipts so a visit, payment, refusal, release, stockpile debit, or state strike cannot apply twice.

## Visits and demands

Use centralized script constants for interval bands, the 45-day floor, refusal compression, progression, demand minimums, proportions, caps, protected floors, industrial-burden durations, package IDs, demand IDs, and transaction results.

Baseline asks for Political Power. Evolution I at 400+ selects one valid demand type uniformly from the accepted list. Evolution II at 800+ raises scale. Evolution III at 1000+ permits extreme amounts. A demand type can be valid while unaffordable. Calculate and lock the exact amount before opening the popup.

Use structural floors so dumping a stockpile cannot reduce future demands to a token value. Cap Command Power at 60. Debit free manpower, not state population. Represent civilian and military capacity as timed burdens, not factory deletion. Protect Stability and War Support payment floors. Display exact costs and blocked reasons.

Payment debits the displayed amount once, records a receipt, increases compliance progression, clears the refusal streak, and schedules one later visit. It gives zero Chaos and prevents punishment for that visit only.

Refusal, including inability to pay, increments refusal history and calls the Event 53 selector once.

## Consequence registry

Implement every accepted package row in `quality/consequence_registry_manifest.md` that has a completed safe owner path. Reserve stable IDs for blocked rows but keep them out of the live pool.

Event 53 owns `mysterious_man_apply_random_consequence` and the registry build. Keep this logic in Event 53 owner files. Do not move it to `chaosx_dynamic_effects`.

Every refusal builds a fresh candidate pool. Add each valid registered package exactly once. Choose one uniform random member or ordinal. Do not use strategic, severity, recent-history, anti-repeat, source-event, or hidden weights. A previously selected package remains valid next time. Target, severity, flavour, disaster-family, movement-candidate, and character-candidate variants do not create extra ballots.

A selected adapter should not reject after prevalidation. Support one bounded fresh rebuild that excludes the rejected package for the current transaction. If a second adapter rejects, apply the always-valid government-paralysis package once and record an implementation-error receipt.

Compound packages receive one ballot. Prevalidate and reserve every component before the first irreversible mutation. Once mutation begins, the owner must finish the sequence and return a combined receipt.

## Owner adapters

Use `quality/adapter_contract_matrix.md` as the integration contract. Connected systems own their real targets, effects, follow-up processing, AI, and cleanup. Event 53 supplies target, transaction ID, package ID, tier, severity request, origin, and source-firing suppression.

Borrowed consequences must not change the source event fired count, type state, weight, repeatable cap, random-event timer, pacing, ordinary History, cluster record, evolution state, opening super-event, world-end route, or source achievement. Owner operational ledgers can change when required for real gameplay and cleanup, with Event 53 origin recorded.

Use documented public helpers where valid. These include `call_natural_disaster`, supported stockpile debit helpers, building damage, exact state population loss, and the indexed Independence Wave, famine, and migration owner APIs.

Do not claim Event 52 Intel Leaked, Event 50 Great Embargo, or Event 021 Random Civil War adapters are complete until their To Be Reworked source systems expose safe bounded adapters and pass the isolation scenarios.

## Evolutions

Implement three Event 53 evolution milestones at 400+, 800+, and 1000+ Chaos. Active-chain milestones use target-local paced activation and the shared evolution log. If the event first fires above a threshold, enabled behavior can apply on the first visit and enabled milestones are recorded in order without redundant popups.

Evolution activation gives zero Chaos. Disabled milestones do not log or set recorded flags. A later enabled evolution independently provides the demand behavior needed by its tier and activates only its own registry additions. Disabled lower-tier package additions remain inactive.

## Nationwide nuclear annihilation

Implement the Evolution III catastrophe without an attacker country. Build a unique ledger of every valid owned or controlled state and process each once. Use real nuclear-scale building damage, exact civilian population loss, Deaths registration, military casualty paths, fallout intensity, and Air Cleanliness contribution. Do not fabricate Condemnation, war responsibility, or a dummy attacker.

The package does not directly set `world_end`. Ordinary fallout can later satisfy the Air Cleanliness owner's normal Fallout request when enabled and valid. Use bounded batches for large countries without reducing state coverage.

## Presentation and assets

Use normal event popups. Implement the initial appearance, recurring appearances, payment resolution, refusal transition, direct consequence reports where needed, target-loss closure, and evolution reporting. Keep hidden scheduler, selector, receipt, and cleanup events hidden.

Follow the writing direction in `specs/09_presentation_event_logs_and_assets.md`. Do not explain the man. Do not expose formulas, pool contents, package IDs, or future surprises.

Produce and wire the five generated report-event scenes from `prompts/asset_prompt.md`. Keep the same fictional ordinary man across office, archive, bunker, intelligence, and cabinet settings. No supernatural markers, modern props, generated text, or portrait-only framing.

Do not add a custom GUI, decision category, focus branch, new country, character portrait, animation, 3D model, achievement, triggerable scenario, super-event, Event 53 world-end branch, or countermeasure system.

## Event system and documentation

Wire Event 53 registration, event type resolution, Chaos level, default enabled allowlist after rework completion, event name mapping, actor mapping, one parent History row, Event Details, evolution catalog, evolution history, and documentation.

Recurring visits do not create new Event 53 firing or History entries. Borrowed source events do not create source History entries.

Write final player-facing localisation during implementation. Use no prompt fragments, update-history wording, hidden mechanics, raw implementation labels, em dashes, semicolons, staccato chains, dialectical hedging, or generic dramatic filler. Run the localisation auditor.

After final in-game Event Details and evolution wording exists, use the spreadsheet worker to update only `docs/spreadsheets/chaos_redux_events_catalog.xlsx`. Set status to Needs Testing when source implementation is complete. Run `python .tools/export_event_catalog_csv.py`. Never edit the CSV exports directly.

## Required evidence

Run the complete named scenarios in `quality/probability_scenarios.md` and `quality/validation_scenarios.md`.

Use:

- `hoi4.event_inspect`
- `hoi4.event_render`
- `hoi4.event_compare`
- `hoi4.probability_inspect`
- `hoi4.probability_evaluate`
- `hoi4.probability_sweep`
- `hoi4.probability_compare`
- `hoi4.probability_render` where useful

For probability changes, use the read-only probability auditor before a patch and again after the owner applies the patch, with the same scenarios.

Run the completion auditor before claiming completion.

## Completion report

List files changed, package rows activated, package rows blocked, owner adapters, source-event isolation evidence, evolution behavior, target and lifecycle behavior, demand tuning, probability artifacts, assets, localisation, docs, workbook update, and remaining risks.

Report every simplification, omission, placeholder, missing adapter, skipped meaningful validation, or fallback. Do not mark the event complete while an accepted active package, required asset, log surface, localisation surface, document, or catalog field is silently missing.
