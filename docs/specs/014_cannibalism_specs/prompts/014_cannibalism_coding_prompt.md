# Coding prompt for Event 014 Cannibalism

Implement Event 014 Cannibalism according to the full source spec package.

Source files:

- docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_1_core.md
- docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_2_evolutions_decisions.md
- docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_3_country_packages_focus_tree.md
- docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_4_world_end_super_events_assets.md
- docs/specs/014_cannibalism_specs/matrices/014_cannibalism_decision_matrix.md
- docs/specs/014_cannibalism_specs/matrices/014_cannibalism_ai_strategy_matrix.md
- docs/specs/014_cannibalism_specs/matrices/014_cannibalism_achievement_matrix.md
- docs/specs/014_cannibalism_specs/prompts/014_cannibalism_asset_prompt.md
- docs/specs/014_cannibalism_specs/prompts/014_cannibalism_super_event_prompt.md
- docs/specs/014_cannibalism_specs/prompts/014_cannibalism_decision_mission_prompt.md
- docs/specs/014_cannibalism_specs/prompts/014_cannibalism_achievement_prompt.md

Follow AGENTS.md and all relevant Chaos Redux skills. Use chaos-redux-events for event implementation, hoi4-decisions-missions for decisions and missions, hoi4-focus-trees if the cannibal country focus tree is implemented, chaos-redux-event-assets and chaos-redux-frame-animation for assets and animation, chaos-redux-super-events for super-event research and wiring, and chaos-redux-subagents for audits and handoffs.

Top requirements:

- Event 014 uses the user prompt classification, Minor Fire-Once.
- The baseline starts as war horror and discipline collapse in a random country at war.
- Early containment can fully defeat the system for that country.
- If the event did not spread, early containment can deactivate the global system.
- If the event spread, every affected country must contain it separately.
- Evolutions are mutation tracks, not baseline stages.
- Evolution I adds ritual and ideology.
- Evolution II adds organized cults, severe state modifiers, and possible cannibal islands or communes.
- Evolution III adds a global cult network, world-threat integration, and future Hannibal hooks.
- Hannibal integration must be future-proof and must not require the Hannibal event to exist yet.
- World-end route requires chaos above world-end threshold plus Hannibal or a later accepted replacement unifier.
- Decisions and missions use concrete costs and map objectives.
- Exploitation path is dangerous and cannot be a safe power route.
- Cannibal country creation includes a full country package, starting forces, reinforcement pathways, AI, focus tree, flags, portraits, ideas, decisions, and cleanup.
- Assets require gore, generated fictional gore, animated states, static fallbacks, manifests, and gfx handoffs.
- Super-event titles, quotes, button remarks, and audio require research before final localisation.
- Achievements must be difficult and tracked, not automatic.
- Event Details and spreadsheet text must describe the premise, not raw effects.

Do not use fallbacks, placeholders, or simplified versions without explicit approval. Keep iterating until the implementation satisfies the spec to its fullest extent. Do not claim completion until audits, docs, assets, localisation, spreadsheet alignment, AI behavior, cleanup, and meaningful validations are complete.
