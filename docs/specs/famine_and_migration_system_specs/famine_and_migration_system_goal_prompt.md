# /goal: Implement the Famine and Migration Mechanics

> **Current design clarification (2026-08-25):** The user clarification and accepted split implementation supersede any shared mechanic, category, or runtime-namespace wording retained below as historical design context. The current implementation uses independent `famine_*` and `migration_*` mechanics, `famine_decision_category` and `migration_decision_category`, and `famine_state_map_mode` and `migration_state_map_mode`; no combined mechanic, category, runtime namespace, or mapmode is current. Use [source_of_truth_map.md](../../plans/famine_and_migration_system_plans/source_of_truth_map.md) and [completion_report.md](../../plans/famine_and_migration_system_plans/completion_report.md) for current status, including the incomplete blockers.

Implement the separate famine and migration mechanics from `docs/specs/famine_and_migration_system_specs/`. These are systems, not random events. Connect them only through explicit causal adapters and neutral conservation primitives. Do not assign an event ID, create an event object, register either mechanic in the event pool, or count their state/accounting pulses as event pacing. The separate register helpers are presentation seams only.

Read the eight spec parts and every supporting matrix, prompt, routing file, bibliography, and closure review. Treat the implementation prompts as binding guidance.

Before editing, read `AGENTS.md`, relevant Chaos Redux skills, offline wiki pages, vanilla documentation and precedents, and current code. Use mandatory HOI4 MCP routes for supported event, probability, GUI, and map surfaces. Record exact blockers for unavailable sources or tools.

Completion requires:

- Dynamic state food security with supply strain, acute shortage, famine, and catastrophic famine.
- Significant population-scaled civilian deaths from unmanaged severe famine through the exact state-population API, recorded as `From famine`.
- Related occupation, forced movement, transit, and trapped-population reasons with clear ownership and no double counting.
- Exact state-to-state civilian transfer. Movement is not death. Add only the population removed from the origin and surviving the route.
- Internal displacement, cross-border flight, evacuation, deportation, reception, integration, resettlement, voluntary return, and forced return.
- Island blockade famine only when war, isolation, maritime dependence, route or port disruption, convoy or escort shortage, inadequate local supply, and no relief corridor are proven.
- Shared adapters for Air Cleanliness, occupation laws, camps, gulags, genocide, forced labor, bombing, nuclear damage, fallout, outbreaks, natural disasters, war, peace, condemnation, relevant events, clusters, and scenarios.
- Ideology as one bounded factor. Persecution, bombing, camps, famine, occupation conduct, and route safety can override ideological affinity.
- Closed borders that create trapped populations and real humanitarian, diplomatic, security, political, and mortality consequences.
- Separate famine and migration categories hidden until their own mechanic has a genuine problem. Reveal migration only after repeated or large displacement evidence creates a sustained issue. Use exactly three canonical player-facing values per mechanic, phased actions, and no shared full scripted GUI.
- AI access to the same valid responses. Complete named probability scenarios through baseline audit, owner patch, and comparison.
- Active registries, scoped hooks, and scheduled jobs. Do not add a whole-world daily, weekly, or monthly scan.
- Absorption, retirement, disabling, or conversion of Event 149 `Immigrations` so no competing flat population drain remains.
- All eight achievements, required static assets, final DDS files, sprite consumers, localisation, permanent documentation, and catalog workbook alignment.

Spawn project subagents with `fork_context=false` using the prepared prompts. Required routes cover repo exploration, system architecture, pre-change and post-change probability audits, decisions, localisation, assets, documentation, improvement review, completion audit, and spreadsheet alignment. Use conditional routes only when their gate is met. Review every handoff and record its disposition.

Keep iterating until the accepted design is implemented. Do not use fixed historical death totals, placeholder art, duplicated population, fake route logic, shallow flat modifiers, undocumented hardcoded values, or unapproved simplifications. Do not claim completion while any accepted mechanic, adapter, AI path, asset, achievement, localisation, audit, cleanup, documentation, or catalog requirement is missing.

The completion report must cover changed files, formulas, transfer proof, Deaths reasons, decisions, AI evidence, adapters, historical profiles, assets, achievements, localisation, documentation, workbook export, validation, and all blockers. Report every remaining simplification or fallback with audit evidence.
