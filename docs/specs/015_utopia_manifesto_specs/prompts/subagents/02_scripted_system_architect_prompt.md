# Prompt for `chaosx_scripted_system_architect`

Use `fork_context=false`.

Repository: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux`

Read:

- `AGENTS.md`
- `docs/specs/015_utopia_manifesto_specs/`
- repo explorer handoff
- relevant current helpers and documentation

Task:

Design reusable architecture for Event 15's safe target gate, weak-country score, Need, Plenty, Concord, Choice versus Assignment, reserve bands, calling shortages, Need-case integrity, selected-target lifecycle, stewardship cleanup, league state, route state, formation proof, and evolution context.

Identify existing helpers first. Propose names, scopes, inputs, outputs, defaults, side effects, call sites, constants, tuning bands, event targets, flags, variables, and cleanup. Patch only narrow reusable helpers and a few direct call sites when safe. Write helper documentation for every new helper.

Do not redesign the source spec or create a large system silently. Broad architecture stays in a plan.

Write a handoff under:

`docs/plans/015_utopia_manifesto_plans/subagent_handoffs/`
