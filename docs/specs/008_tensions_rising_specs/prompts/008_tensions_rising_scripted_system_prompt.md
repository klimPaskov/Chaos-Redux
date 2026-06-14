# Scripted System Architect Prompt: Event 008 Tensions Rising

Design or implement the reusable scripted helper layer for Event 008 `Tensions Rising`.

Read:

- `AGENTS.md`
- `chaos-redux-events`
- `chaos-redux-subagents`
- Event 008 specs under `docs/specs/008_tensions_rising_specs/`
- `matrices/008_tensions_rising_constants_and_helpers.md`
- existing dynamic helper files, especially `common/scripted_effects/chaosx_dynamic_effects.txt` and docs if working in the repo

Own this scope:

- script constants for Event 8 tuning
- staged world tension/chaos values
- Tension Pulse helper and cap/replacement behavior
- relation-pair helper design or small implementation if local and safe
- delayed follow-up scheduler helper design
- event-log/evolution context helper design
- cleanup plan for variables, flags, and event targets

Non-negotiables:

- No new global daily/weekly/monthly loop for Event 8.
- No hardcoded magic numbers when script constants can own tuning.
- No unsupported duration-token shortcuts, mirror file-scoped constants if needed.
- Stage IV does not trigger a super-event and remains non-terminal.
- Relation damage is timed and capped by pair cooldowns.
- Timer pulse uses replacement/extension caps, never additive infinite stacking.
- No direct war goals, countries, focus trees, cores, or formables.

Output required:

- proposed helper map with scopes, inputs, outputs, side effects, and call sites
- constants and tuning table plan
- event target and cleanup plan
- migration plan if existing Event 8 logic exists
- validation notes
- if patching, a handoff under `docs/plans/008_tensions_rising_plans/subagent_handoffs/`
