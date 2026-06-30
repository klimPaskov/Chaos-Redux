/goal Implement Chaos Redux Event 011 Secret Alliance to its fullest extent.

Use the source package at `docs/specs/011_secret_alliance_specs/`:
- `specs/011_secret_alliance_spec_part_1_core.md`
- `specs/011_secret_alliance_spec_part_2_evolutions_and_reveal.md`
- `specs/011_secret_alliance_spec_part_3_counter_pact_decisions.md`
- `specs/011_secret_alliance_spec_part_4_ai_assets_achievements.md`
- `matrices/011_secret_alliance_runtime_flow.md`
- `matrices/011_secret_alliance_decision_map.md`
- `matrices/011_secret_alliance_ai_matrix.md`
- `matrices/011_secret_alliance_tuning_matrix.md`
- `prompts/secret_alliance_coding_prompt.md`
- `prompts/secret_alliance_asset_prompt.md`
- `prompts/secret_alliance_achievement_prompt.md`
- `prompts/secret_alliance_decision_mission_prompt.md`

Follow AGENTS.md, chaos-redux-events, hoi4-decisions-missions, chaos-redux-event-assets, chaos-redux-frame-animation, chaos-redux-improvement-loop, and chaos-redux-subagents.

Pass or fail requirements:
1. Hidden Anti-[target] compact starts with three valid minor members and no public faction at start.
2. Core members are not at war with the target at hidden formation. If any core member goes to war with the target, reveal the pact, form the public faction or coalition, and join all valid core members against the target immediately.
3. Evolution I, II, and III match the spec, including active-event changes and pre-fire evolved openings.
4. Evolution II opens the counter-pact decision system with evidence, preparedness, dynamic costs, missions, diplomacy, border options, and AI equivalents.
5. Evolution III unlocks public confrontation, war options, possible second major, and a final crisis window.
6. Implement all mapped operations, ideas, AI behavior, assets, animated fallbacks, achievements, event logs, event details, docs, and spreadsheet alignment.
7. Do not expose hidden members or future mechanics through localisation.
8. Avoid fallbacks, placeholder assets, generic AI weights, store-like PP buttons, and unreported simplifications.
9. Run focused audits, including decision, localisation, asset, AI, reveal, cleanup, and completion checks.

Keep iterating until the implementation satisfies the spec. Do not claim completion until the files, assets, docs, spreadsheet, audits, and meaningful validation prove it.
