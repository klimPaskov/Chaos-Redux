# Prompt for `chaosx_localisation_auditor`

Use `fork_context=false`.

Repository: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux`

Read the source specs, final Event 15 implementation, scripted localisation, event log text, GUI text, focus text, decision text, achievement text, super-event research, docs, and catalog handoff.

Audit:

- missing and duplicate keys
- UTF-8 BOM
- namespaces
- dynamic actor, target, state, route, cost, timer, and value text
- integer formatting
- raw trigger exposure
- tree-replacement warning
- Need, Plenty, Concord, and balance breakdowns
- hidden-route spoilers
- route tone
- Event Details and catalog alignment
- super-event source fidelity

Patch bounded key, tooltip, dynamic text, grammar, and consistency defects. Do not invent new mechanics or final quotes.

Write key-level handoff under:

`docs/plans/015_utopia_manifesto_plans/subagent_handoffs/`
