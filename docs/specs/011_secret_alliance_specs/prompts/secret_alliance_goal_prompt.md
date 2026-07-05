/goal Implement Event 011 Secret Alliance to the fullest extent using the planning package at docs/specs/011_secret_alliance_specs/ or the imported package contents:
- specs/011_secret_alliance_spec_part_1_core.md
- specs/011_secret_alliance_spec_part_2_evolutions_and_reveal.md
- specs/011_secret_alliance_spec_part_3_decisions_missions_ui.md
- specs/011_secret_alliance_spec_part_4_systems_ai_assets_achievements.md
- prompts/secret_alliance_coding_prompt.md
- prompts/secret_alliance_asset_prompt.md
- prompts/secret_alliance_super_event_prompt.md
- prompts/secret_alliance_achievement_prompt.md
- prompts/secret_alliance_decision_mission_prompt.md
- matrices/*

Follow AGENTS.md plus chaos-redux-events, hoi4-decisions-missions, chaos-redux-event-assets, chaos-redux-frame-animation, chaos-redux-super-events, chaos-redux-subagents, and chaos-redux-improvement-loop. Inspect the actual repo, offline Paradox wiki, vanilla HOI4 docs, and existing Chaos Redux patterns before editing.

Pass or fail requirements: keep Event 011 as Minor Fire-Once, select exactly three valid non-war founders or mark unavailable, prefer factionless minors, track roles and values, support member invitations, implement Baseline, Evo I, Evo II, Evo III, active evolutions and pre-fire openings, open counterplay at Evo II, create public pact crisis at Evo III, trigger reveal when any member wars the target, form Anti-[target] Pact and join all live members to war, implement evidence, counter-readiness, secrecy, cohesion, readiness, member confidence, decisions, missions, AI, cleanup, event logs, event details, docs, achievements, assets, animated UI assets with fallbacks, and reveal super-event with researched text and licensed audio.

Use subagents from the routing handoff. Do not use fallbacks, placeholders, or smaller substitutes without explicit approval. Do not paste planning text into localisation. Do not claim completion until the implementation satisfies the spec and final audits report no unresolved blockers. Provide a concrete completion report with files changed, validation, subagent handoffs, simplifications, and remaining risks.
