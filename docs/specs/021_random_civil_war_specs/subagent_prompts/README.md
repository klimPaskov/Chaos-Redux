# Event 021 Subagent Prompts

These prompts are implementation handoffs for the project custom subagents.

Spawn every project subagent with a complete, self-contained prompt and no inherited parent context; the `fork_turns="none"` wording in these templates means exactly that.
Use the current [subagent skill](../../../../.claude/skills/chaos-redux-subagents/SKILL.md) for ownership boundaries.
Before dispatch, add exact allowed files, current source and handoff paths, accepted decisions, and unresolved blockers to each template.
These templates need bounded parent context and are not standalone authorizations.

The parent must use the prompt text as the complete context for the subagent. Do not assume inherited conversation state.

Shared source-spec folder:

`docs/specs/021_random_civil_war_specs/`

Shared handoff folder:

`docs/plans/021_random_civil_war_plans/subagent_handoffs/`

The prompts route only work justified by the accepted Event 021 design.

No prompt is provided for:

- `chaosx_event_ui_worker`
- `chaosx_3d_model_pipeline`
- `chaosx_super_event_text_researcher`
- `chaosx_super_event_audio_researcher`

The accepted design has no event-owned custom GUI, custom 3D asset, or super-event.

Conditional prompts must be used only when their stated gate is met.
