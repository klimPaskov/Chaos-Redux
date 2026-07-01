/goal Implement Event 015 as `utopia_manifesto`, replacing `World Tension Subsides` completely. Use the source spec package at `docs/specs/015_utopia_manifesto_specs/`, especially the coding prompt, asset prompt, decision prompt, achievement prompt, and super-event prompt.

Required skills and docs: `AGENTS.md`, `chaos-redux-events`, `hoi4-focus-trees`, `hoi4-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-frame-animation`, `chaos-redux-super-events`, `chaos-redux-subagents`, and `chaos-redux-improvement-loop`.

Pass or fail requirements: Event ID 15 is Minor Fire-Once. It targets only eligible minors and eligible player countries, blocks majors and strong industry, shows `N/A` when no valid target exists, gives AI forced acceptance, and gives humans accept or reject. Acceptance replaces the focus tree only for the accepting country and opens the Utopian Ledger. Rejection cleanly closes the route.

Implement the full Utopian Manifesto tree with opening trunk, Living Humanism, Common Store State, Guild Commonwealth, Island Discipline, hidden Marked Bounds, economy, vocation, military, diplomacy, needful land, integration, geography adaptation, and late proclamation branches. Keep it non-linear, route-aware, localized, iconed, AI-weighted, and free of filler rewards.

Implement Ledger values: Need, Consent, Surplus, Overreach, Vocation Balance, and Foreign Suspicion. Values must be visible and must drive decisions, focuses, AI, claims, integration, League behavior, and late outcomes. Decisions and missions must use concrete costs and objectives such as equipment, trains, convoys, manpower, factories, supply, state control, compliance, XP, stability, war support, and timed missions. Do not make political power stores.

Implement Needful Land claims with Need proof, arbitration, AI safety, and postwar integration. No instant free cores. Implement occupation and integration projects with local stores, councils, supply, compliance, resistance, and route-specific risks. Implement dynamic unit families and reinforcement paths. Implement achievements, required assets, animated GUI pieces with static fallbacks, docs, event log, and spreadsheet alignment after final localisation exists.

Late super-events need researched final titles, quotes, button remarks, images, unique licensed audio, documentation, and settings-aware wiring before completion. Treat unresearched super-event wording or audio as blockers.

Use subagents as required. Keep iterating until the implementation satisfies the spec to the fullest extent. Do not claim completion with fallbacks, placeholders, missing AI, missing assets, missing localisation, missing audits, missing docs, or unresolved simplifications. Produce a concrete completion report.
