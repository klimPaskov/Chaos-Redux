# Baseline prompt for `chaosx_ai_probability_auditor`

Work read-only with no inherited conversation context. Establish the named probability baseline for Event 38 before any weighted patch.

Read `AGENTS.md`, `chaos-redux-events`, `chaos-redux-focus-trees`, `chaos-redux-decisions-missions`, `chaos-redux-subagents`, and the complete Event 38 specs, especially `15_ai_probability_and_balance.md`, `23_acceptance_scenarios.md`, `25_decision_register.md`, `26_focus_route_matrix.md`, and `28_balance_tuning_tables.md`.

Start with `hoi4.probability_inspect` for every implemented weighted surface in scope. Then use the correct MCP tools based on the evidence contract. Do not patch source and do not choose balance targets.

Audit at minimum:

- Malta government and dominant-order route selection
- regional campaign targets
- focus selection for survival, logistics, military, settlement, Papal, failure, and hidden routes
- council demand pool and order-specific demand selection
- event option `ai_chance`
- evolution MTTH modifiers
- principality charter, levy, loyalty response, succession, autonomy, integration, and rebellion choices
- relic expedition target and outcome pools
- foreign Catholic support choices
- Eleventh Crusade refuge, landing, and recovery choices
- Teutonic negotiation and member assent
- Atlantis AI Germany `90%` choice inside the complete eligible pool
- Holy World believer alignment and side assignment
- regional terminal war target order
- triggerable scenario AI side assignment by intensity
- unit-family production, recruitment, and template selection where weighted

Use the named scenarios in `validation/probability_scenario_manifest.md` and add only scenarios needed to cover an observed surface. State whether each candidate pool and external factor set is complete. Label evidence as exact, bounded, sampled, score-only, or unresolved.

Use `hoi4.probability_evaluate` and `hoi4.probability_sweep` for score and sensitivity. Use seeded simulation only when the complete pool and state contract permit it. Use sequence analysis only when cadence, recovery, caps, cooldowns, removals, resets, and terminal states are fully declared. Render evidence when it improves review.

Return observed ordering, dominance, starvation, invalid candidates, timing, sensitivity, unresolved external state, and scenario hashes. Save the baseline report under `docs/plans/038_malta_crusaders_plans/probability_baseline.md`. The owner will apply any accepted patch.
