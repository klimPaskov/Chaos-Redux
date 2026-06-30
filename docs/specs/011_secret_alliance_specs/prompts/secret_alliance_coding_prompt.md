# Coding Prompt: Event 011 Secret Alliance

Implement Event 011 according to the full source spec package in `docs/specs/011_secret_alliance_specs/`.

Primary files to read:

- `specs/011_secret_alliance_spec_part_1_core.md`
- `specs/011_secret_alliance_spec_part_2_evolutions_and_reveal.md`
- `specs/011_secret_alliance_spec_part_3_counter_pact_decisions.md`
- `specs/011_secret_alliance_spec_part_4_ai_assets_achievements.md`
- `matrices/011_secret_alliance_runtime_flow.md`
- `matrices/011_secret_alliance_decision_map.md`
- `matrices/011_secret_alliance_ai_matrix.md`
- `matrices/011_secret_alliance_tuning_matrix.md`
- `prompts/secret_alliance_asset_prompt.md`
- `prompts/secret_alliance_achievement_prompt.md`
- `prompts/secret_alliance_decision_mission_prompt.md`

Non-negotiables:

1. Event 011 is a Minor Fire-Once event that creates a hidden anti-target compact, not a public faction at start.
2. Initial baseline chooses three valid minor core members. They must not be at war with the target.
3. Prefer factionless minors, but use dynamic candidate scoring and strict disqualifiers.
4. If any core pact member goes to war with the target, immediately reveal the pact, form the public faction or coalition, and bring all valid core members into war against the target.
5. Evolution I adds more minor recruitment and stronger visible pressure while staying hidden.
6. Evolution II allows a major patron, opens the counter-pact decision category, and adds aggressive sabotage, threats, killings, and provocations.
7. If first firing occurs with Evolution II available, use a major founder opening plus minors.
8. Evolution III makes public confrontation likely, can add more members and a second major, and unlocks player war options.
9. If first firing occurs with Evolution III available, start from the Evolution II opening and progress later.
10. Implement counterplay with decisions and missions that use concrete costs, objectives, evidence, preparedness, diplomacy, border requirements, and AI equivalents.
11. Keep hidden member text hidden until exposure or reveal.
12. Implement all achievements, assets, docs, event details, evolution details, AI behavior, cleanup, and spreadsheet alignment.
13. Use project subagents or their prompt pack where appropriate. Do not claim completion until audits and meaningful validations support the claim.

Write final localisation during implementation from the direction in the spec. Do not paste working labels as final player-facing text unless an identifier requires it. Avoid fallbacks, simplifications, and placeholder content.
