Implement Chaos Redux Event 62, Allies Backstab, from `docs/specs/062_allies_backstab_specs/`. Read the full pack, `AGENTS.md`, relevant skills, required offline wiki and vanilla references, and repo precedents. Inspect the repository first and preserve unrelated work.

Identity is fixed: `chaosx.nr62.1`, Minor Repeatable, Chaos level 1, Wars cluster High member. Each normal firing affects at least two valid factions. Use one bounded event-time scan and one idempotent transaction per selected faction.

Snapshot members, political units, subjects, wars, diplomacy, capitals, and player roles before mutation. Select victims through the accepted model for strength, manpower, equipment, industry, territory, losses, war strain, contribution, isolation, and strategic utility. Exclude the faction leader from the baseline pool. Protect strong core members. Treat an overlord and subjects as one unit unless the subject-release owner returns a valid independence receipt.

Reconcile expeditionary forces, withdrawal access, guarantees, subjects, and shared wars. Run a one-day legal recheck before war. Use immediate legal war, delayed separation war, armed expulsion pending war, or existing-hostility attachment according to proof. Never create contradictory war sides, duplicate wars, dead-country effects, or reload duplication.

Use one ordinary decision category, one static category picture, and one public value, working label `Crisis Cohesion`. Implement role actions for leaders, retained members, victims, pending defectors, neutral withdrawals, and two outside sponsors at most. Keep three to five actions per phase, six maximum, and one to three missions. Costs must be dynamic, meaningful, icon-correct, and capped at four spendable types. Implement the accepted missions, partial outcomes, idea lifecycle, settlements, successor compact, and cleanup. Do not add a scripted GUI, focus tree, country, unit, technology, portrait, flag, 3D model, counter, or animation.

Implement Evolution I at 200+ for expanded purges and co-victim coordination, Evolution II at 400+ for legal internal bloc wars and neutral withdrawals, and Evolution III at 600+ for bounded simultaneous large-faction collapse. Evolution state adds zero Chaos. Log realized behavior only. Respect each toggle. Cap Evolution III at three full fractures and eighteen political-unit mutations per generation.

Audit the shared faction-leave Chaos source. Forced hostile exits must not receive the ordinary negative Chaos result. Do not duplicate shared Chaos sources. Add distinct world-order-fracture and settlement-violation sources only after overlap review and with one-shot receipts.

Implement the bounded connections in the source pack. Each owner keeps its own transaction. The Offensive may change aggression, never legality, access, supply, viability, or rational settlement.

Use `chaosx_ai_probability_auditor` before weighted changes and again with `hoi4.probability_compare` after tuning. Use the named scenarios and required MCP event inspect, render, compare, and probability evidence. Invalid AI actions must have zero weight.

Produce every accepted final asset, four achievements, and the conditional fire-once Evolution III super-event with a verified quote, generated image, licensed musical WAV, settings-aware playback, and strict proof. Wire Event Logs, Event Details, Evolutions, Chaos History, registration, default enable state, cluster membership, localisation, documentation, achievements, and the catalog workbook. Regenerate CSV exports.

Run the decision, localisation, improvement-loop, probability, and completion audits. Review every handoff and dispose of every plan. Finish with a completion report covering files, evidence, acceptance results, assets, AI, Chaos deltas, workbook export, and every simplification, omitted validation, or blocker. Do not claim completion while an accepted surface remains missing.
