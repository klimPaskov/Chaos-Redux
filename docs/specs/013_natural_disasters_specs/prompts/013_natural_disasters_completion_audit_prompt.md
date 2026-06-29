
# Completion audit prompt for Event 013 Natural Disasters

Use `chaosx_event_completion_auditor` after the implementation agent believes Event 13 is complete. This is a read-only audit.

## Inputs

Read the Event 13 source spec package under:

`docs/specs/013_natural_disasters_specs/`

Read the implementation files that the main agent changed for Event 13, including events, scripted effects, scripted triggers, constants, decisions, scripted GUI, interface, GFX, localisation, docs, scenario registry, event log, cluster logic, assets manifests, and spreadsheet if updated.

## Audit questions

- Does Event 13 remain Minor Repeatable.
- Does one Event 13 sequence create exactly one random-event history row.
- Do delayed subevents avoid extra random-event log rows.
- Are disasters delayed from one another.
- Are disaster families target-specific and not flat random damage.
- Are there no fixed casualty amounts, fixed per-state death totals, or absolute death caps that block multi-million outcomes in dense states.
- Does building damage vary by family.
- Does real state population loss feed civilian deaths through per-state dynamic percentage calculations.
- Is condemnation untouched by natural disasters.
- Does Baseline, Evolution I, Evolution II, and Evolution III behavior exist as specified.
- Does Event 13 avoid a world-end branch.
- Is Sandstorm active gameplay routed through Event 13 or safely disabled as a placeholder.
- Is Earth Earthquake or Event 46 inactive, unknown, and routed back to Event 13 for seismic content.
- Does the Natural Disasters cluster contain repeated Event 13 member slots with proper delayed sequence behavior.
- Does the Disaster Barrage scenario launch directly with type and intensity controls.
- Do recovery decisions and missions use physical resources, logistics, objectives, and dynamic factors rather than a political power store.
- Does AI use recovery decisions and missions safely.
- Does the scripted GUI or category presentation show active warnings, impacts, aftermaths, and recovery state.
- Do animated assets have real source frames, sheet DDS, static fallbacks, manifests, and no transform-only final motion.
- Are event details, evolution details, cluster details, scenario details, docs, and spreadsheet aligned.
- Are assets complete or explicitly blocked.
- Are any simplifications hidden.

## Output

Write a completion audit report under:

`docs/plans/013_natural_disasters_plans/subagent_handoffs/`

Include surface status, missing or simplified requirements, validation evidence, remaining blockers, and recommended next actions. Do not patch gameplay files.
