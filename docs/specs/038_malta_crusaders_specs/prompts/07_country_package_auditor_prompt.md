# Prompt for `chaosx_country_package_auditor`

Work with no inherited conversation context. Audit and make only bounded local patches to Event 38 country packages.

Read `AGENTS.md`, `chaos-redux-events`, `chaos-redux-focus-trees`, `chaos-redux-event-assets`, `chaos-redux-subagents`, the full Event 38 pack, and especially `02_opening_release_and_map.md`, `03_malta_country_package.md`, `08_principalities_and_governance.md`, `10_hidden_teutonic_order.md`, `11_hidden_atlantis_betrayal.md`, `12_holy_world_terminal.md`, `21_multiplayer_dlc_performance_cleanup.md`, `23_acceptance_scenarios.md`, and `27_country_package_matrix.md`.

Audit every persistent package and transformation listed in the country matrix. Verify:

- collision-safe tag or cosmetic strategy and provenance
- reuse of valid existing identities and content
- no duplicate Pope, Hitler, Grand Master, or other leader ownership
- tag registration, country collections, color, flags, names, adjectives, parties, leaders, portraits, gender, and name pools
- capital, fallback capital, ownership, controller, cores, claims, compliance, resistance, and territory validity
- starting laws, ideas and lifecycles, technology, research, production, resources, manpower, fuel, convoys, trains, supply, ports, airbases, and building capacity
- starting army, navy, air force, templates, equipment, commanders, and reinforcement path
- custom-unit provider registration and concrete equipment coverage
- focus-tree loading, decisions, AI, faction behavior, and route origin
- annexation, defeat, expulsion, release, integration, independence, government change, and cleanup
- player switching, host ownership, and multiplayer behavior
- ordinary human civilian classification for Malta and principalities
- correct hidden Atlantis transformation on Germany without creating a duplicate Germany
- Holy World scenario creation only when no valid Papal actor exists

Use the map MCP route for state and capital facts and the technology route for country grants when in scope. Do not guess state IDs or technology tokens. Route weighted AI findings through the probability audit cycle.

Patch narrow package references and setup defects where safe. Do not invent a new country package or carrier without parent approval. Write the completed matrix from `templates/country_package_audit_template.md` and the handoff to `docs/plans/038_malta_crusaders_plans/subagent_handoffs/country_package_auditor.md`.
