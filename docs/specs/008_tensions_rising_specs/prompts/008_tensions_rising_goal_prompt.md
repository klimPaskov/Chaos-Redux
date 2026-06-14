/goal Implement Chaos Redux Event 008 “Tensions Rising” to the fullest extent, using the source spec pack at `docs/specs/008_tensions_rising_specs/`.

Read first: `AGENTS.md`, `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-event-assets`, and the relevant offline HOI4 wiki/vanilla docs for touched systems.

Spec files:
- `specs/008_tensions_rising_spec.md`
- `specs/008_tensions_rising_evolutions_and_hidden_effects.md`
- `specs/008_tensions_rising_event_log_and_localisation.md`
- `matrices/008_tensions_rising_constants_and_helpers.md`
- `matrices/008_tensions_rising_ai_matrix.md`
- `matrices/008_tensions_rising_cluster_and_achievements.md`

Prompts:
- `prompts/008_tensions_rising_coding_prompt.md`
- `prompts/008_tensions_rising_asset_prompt.md`
- `prompts/008_tensions_rising_achievement_prompt.md`
- `prompts/008_tensions_rising_scripted_system_prompt.md`
- `prompts/008_tensions_rising_localisation_audit_prompt.md`

Non-negotiables: Event 8 stays Minor Repeatable. Baseline Calm World firing is +100 world tension and only fires below 100% WT. Stage I: +10 chaos/+100 WT and can fire at 100% WT. Stage II: +15 chaos/+200 WT. Stage III: +25 chaos/+500 WT. Stage IV: +50 chaos/+1000 WT. No super-event or world-end scenario. Add capped temporary timer pressure, timed relation shocks, delayed reports, event-log/evolution detail wiring, AI posture hooks, assets, achievements, and docs as specified. No direct war goals, countries, focus trees, cores, or formables.

Keep iterating until the implementation satisfies the spec. Do not claim completion with fallbacks, placeholder assets, missing localisation, missing event-log/evolution surfaces, skipped achievements, uncapped pulse stacking, or unreported queued cluster work. Finish with a concrete completion report and validation evidence.
