# Coding-agent implementation prompt for Event 045

Implement Event 045, Third Balkan War, from the complete accepted package under `docs/specs/045_third_balkan_war_specs/`. Treat every mapped requirement as acceptance criteria. Do not replace dynamic camp construction, linked wars, claims, intervention, Evolutions, AI, achievements, assets, or settlement logic with smaller substitutes.

## Mandatory preparation

Read `AGENTS.md`, all event-package files, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-super-events`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`, the relevant offline wiki pages, current vanilla documentation, and at least one current vanilla precedent for each engine surface touched. Use the HOI4 MCP event and probability tools for the supported event-chain and weighted surfaces. Record exact blockers when a mandatory route is unavailable.

## Required gameplay implementation

- Keep Event ID `45`, type Minor Fire-Once, Chaos level `1`, and entry `chaosx.nr45.1`.
- Register Event 045 in the Wars cluster with High member severity.
- Keep it disabled by default until the complete rework is ready.
- Add a reusable validity trigger that requires enough ordinary, viable regional governments to form a real multi-country war.
- Dynamically assemble two opening camps, or a justified three-sided linked war graph, from current borders, claims, factions, guarantees, ideology, geography, and campaign state.
- Never place same-faction countries in opposing opening camps.
- Make opening setup transactional and rollback-safe.
- Expose exactly one persistent custom value, Balkan War Escalation, with the five accepted stages and proof gates.
- React to regional entry, support tiers, volunteers, guarantees, faction calls, direct major intervention, hostile major pairs, theater spread, armistice compliance, and settlements without passive upward drift.
- Implement the maintained regional-interest and claim registry through map-inspected state groups.
- Implement role-aware decisions and missions with selected targets, varied real costs, clear tooltips, AI equivalents, and complete cleanup.
- Implement regional victory, negotiated settlement, imposed ceasefire, frozen armistice, wider-war continuation, and Another World War handoff.
- Implement all three Evolutions through separate enable state, dynamic pacing, log entries, content gates, and cleanup. Evolution activation itself adds zero Chaos.
- Reuse Independence Wave and Random Civil War provider packages for valid Evolution II actors instead of creating empty tags.
- Implement the six achievements and complete asset, super-event, event-log, Event Details, documentation, and catalog alignment.

## Chaos and origin rules

Do not duplicate generic Chaos from wars, peace, deaths, annexations, puppeting, or faction changes. Add event-owned Chaos only for a separately defined Event 045 consequence that shared systems do not already represent. The final Another World War stage is not a world-end scenario. Set the origin memory only when Event 045 proves that its linked conflict created the first qualifying wider war. A pre-existing global war must not receive false Event 045 origin credit.

## Technical architecture

Centralize thresholds, stage bands, support tiers, durations, cooldowns, AI factors, and settlement tuning in script constants. Use event targets for short-lived scope pointers and stable generation identifiers for persistent ledgers. Use registered participants, claims, sponsors, missions, and bounded pulses. Do not add a broad daily, weekly, or monthly all-country loop without explicit user authorization.

Reuse shared classifiers for special and nonhuman countries and shared stockpile or population helpers when applicable. Event-specific lifecycle and validation remain in Event 045 owner files. Document any genuinely cross-system helper added to the dynamic registry in the same change.

## Required specialist passes

Use the correct bounded subagents with explicit context and no inherited thread state:

- scripted-system architect for reusable helpers
- decision and mission auditor for the category and missions
- AI probability auditor before and after weighted changes
- generated art, source research, and icon workers for accepted assets
- super-event text and audio researchers for the two accepted super-event moments
- localisation auditor for visible text
- event completion auditor before the final claim
- spreadsheet worker only after final in-game wording and implementation facts exist

Do not invoke the event UI worker because the accepted design has no dedicated scripted GUI.

## Validation and completion

Use `hoi4.event_inspect`, event render or compare routes, and the probability scenarios in the quality folder. Test opening validity, two-camp and three-sided setup, rollback, same-faction rejection, fragmented Yugoslavia, support tier anti-farming, stage proof caps, settlement families, each Evolution enabled and disabled, wider-war origin, pre-existing world-war rejection, achievements, save and reload, invalid-target cleanup, cluster integration, and Event Log displays.

Produce a concrete completion report with changed files, identifiers, scenario evidence, assets, audio and source records, docs, workbook export, unresolved plans, and simplifications. If any accepted surface is missing, fallback, unwired, unaudited, or unverified, mark the implementation incomplete. No simplification or fallback is authorized by this prompt.
