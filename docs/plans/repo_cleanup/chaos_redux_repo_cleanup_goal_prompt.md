Read `docs/plans/repo_cleanup/chaos_redux_repo_cleanup_master_prompt.md` and carry out the Chaos Redux repository cleanup to its fullest safe extent.

This is a broad cleanup pass for shared Chaos Redux systems and Events 1-20. General systems remain fully in scope, including random events, settings, event logs, evolutions, clusters, triggerable scenarios, chaos meter, deaths, condemnation, air cleanliness, world threats, super-events, scripted GUI, shared helpers, constants, scripted localisation, localisation, docs, and shared infrastructure.

Do not audit or clean old event-specific implementations for Events 21 and higher. Those events are obsolete and will be reworked from scratch. Inspect or touch Events 21+ only when they appear inside shared infrastructure, such as registration arrays, event-log catalog entries, settings lists, triggerable scenario registries, shared localisation selectors, shared helper references, or docs for general systems.

Follow `AGENTS.md` and all relevant repo skills. Inspect the repo broadly for duplicated gameplay logic, overly complicated scripted logic that can be safely simplified, dead or unused code, stale references, scattered subsystem logic, inconsistent workflow patterns, stale docs, stale localisation, and helper or constant opportunities.

Preserve intended gameplay behavior unless cleanup reveals a clear bug. Before deleting anything, verify direct references, dynamic references, meta-effect use, scripted localisation, GUI, `.gfx`, event IDs, docs, and spreadsheet references. Leave uncertain dynamic or future-hook code in place and document the uncertainty.

Prefer existing helpers. Add new dynamic effects, scripted triggers, script constants, or dedicated subsystem files only when they improve reuse, ownership, and maintenance. Document every new or changed helper in the matching markdown file. Move logic only when ownership becomes clearer and all call sites can be safely updated. Where similar systems use different ad hoc flows for setup, validation, effects, logging, cleanup, docs, or localisation, normalize them to a clear existing pattern when it is safe. Do not leave random scattered code or tangled condition blocks in place when a simpler helper or subsystem-owned workflow preserves behavior.

Patch safe bounded improvements. For broad, risky, or design-changing migrations, write a plan and defer implementation. Do not use fallbacks, partial refactors, placeholder replacements, or undocumented helpers.

Update docs, localisation, scripted localisation, helper docs, and catalog references when cleanup affects them. Use project subagents where their scope helps, but review their output yourself.

Run meaningful validation that directly affects confidence. Re-scan changed systems for stale references, broken moved calls, missing helper docs, missing call sites, obsolete docs, and accidental Events 21+ event-specific cleanup.

Do not claim completion until the master prompt is satisfied. Final report must list systems inspected, event-specific surfaces inspected, Events 21+ shared-system references touched if any, files changed, helpers and triggers changed, constants changed, overcomplicated code simplified, workflow patterns normalized, code moved, new files created, duplication removed, dead code removed, dead code kept with reasons, docs and localisation updates, skills used or updated, validation performed, behavior changes, rejected candidates, deferred migrations, remaining risks, and simplifications or blockers.
