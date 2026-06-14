# Subagent Prompt — chaosx_scripted_system_architect — Event 009 White Peace

Spawn with `fork_context=false`.

Read:

- `AGENTS.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- relevant HOI4 wiki/vanilla docs for triggers/effects/scopes/event targets/script constants
- `docs/specs/009_white_peace_specs/specs/009_white_peace_spec.md`
- `docs/specs/009_white_peace_specs/specs/009_white_peace_dynamic_weight_model.md`
- `docs/specs/009_white_peace_specs/matrices/009_white_peace_safety_ai_acceptance_matrix.md`

Task:

Design and, if parent scope permits implementation, add narrow reusable helpers for Event 009:

- `prepare_white_peace_runtime_context`
- `calculate_white_peace_dynamic_cap`
- `can_country_be_white_peace_target`
- `can_pair_receive_white_peace`
- `score_white_peace_pair`
- `apply_white_peace_pair`
- `mark_recent_white_peace_pair`
- `record_white_peace_evolution_if_needed`
- compact skip-reason support for event list and Peace cluster detail.

Preserve the normal repeatable recovery system. The environment cap must never exceed `1500`; higher evolution stages must reduce event likelihood; no new daily/weekly all-country loops should be added solely for this event.

Deliver:

- helper map with scopes, inputs, outputs, side effects, and call sites;
- constants/tuning table plan;
- event target and cleanup plan;
- risks around unsupported fields and timed flags;
- validation checks for no-war, one-war, many-war, protected-war, stage-II major, stage-III broad, and repeat-fired states;
- handoff under `docs/plans/009_white_peace_plans/subagent_handoffs/` if files are patched.
