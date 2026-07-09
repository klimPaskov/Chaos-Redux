# Temporary continuation prompt, not part of the spec

Continue Event 019 Infantry Spawn from the completed planning handoff in `docs/specs/019_infantry_spawn_specs/`.

Stopping point: the planning package has been written. Completed files are all spec parts in `specs/`, prompt files in `prompts/`, matrices in `matrices/`, the reading manifest in `research/`, and subagent work orders in `handoff/`. No gameplay implementation, localisation implementation, asset generation, GFX wiring, GUI wiring, spreadsheet workbook edit, or subagent execution has been performed in this chat.

Next step: implement the event using `prompts/infantry_spawn_goal_prompt.md` and `prompts/infantry_spawn_coding_prompt.md`. Read every spec file and matrix first. Then inspect the real repository, offline Paradox wiki snapshot, vanilla HOI4 documentation, existing Chaos Redux event, decision, unit, scenario, chaos unit, country package, focus tree, achievement, asset, and super-event patterns.

Constraints to preserve: Event 019 is Minor Repeatable. Baseline spawns weak or basic units across most eligible controlled states with diminishing per-state density for large countries and no hard cap. Evolution I improves organization. Evolution II adds serious and strange units plus decisions. Evolution III stops clean default spawns and uses crisis decisions, random battalion composition, possessed generals, and revolts. Evolution IV uses a dynamic chaos unit registry. Zombies are limited to the base trainable unit. Ghosts and golems are spawn-only. Parent Zombie Outbreak, Death, and future golem mechanics must not be called by this event's lesser splinters. Triggerable scenario creates instant crisis and revolt setup without normal event prerequisites. No terminal world-end flags are set by this event.

Continue with full-depth implementation. Do not summarize missing implementation. Do not use fallbacks. Do not claim completion until all required mechanics, AI, assets, localisation, event logs, docs, spreadsheet alignment, triggerable scenario, achievements, audits, and accepted improvement-loop disposition are complete.
