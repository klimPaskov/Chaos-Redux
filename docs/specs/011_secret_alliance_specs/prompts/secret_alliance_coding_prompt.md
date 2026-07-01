# Coding Prompt for Event 011 Secret Alliance

Implement Event 011 Secret Alliance according to the full spec package under `docs/specs/011_secret_alliance_specs/`.

Required source files from this package:

- `specs/011_secret_alliance_spec_part_1_core.md`
- `specs/011_secret_alliance_spec_part_2_evolutions_and_reveal.md`
- `specs/011_secret_alliance_spec_part_3_decisions_missions_ui.md`
- `specs/011_secret_alliance_spec_part_4_systems_ai_assets_achievements.md`
- matrices and prompts in this package

Follow `AGENTS.md`, `chaos-redux-events`, `hoi4-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-frame-animation`, `chaos-redux-super-events`, `chaos-redux-subagents`, and `chaos-redux-improvement-loop`.

Before editing, inspect the actual repo, offline Paradox wiki, and vanilla HOI4 docs and examples required by the touched systems. This planning environment did not include those files, so implementation must do that inspection.

Core implementation requirements:

- keep Event 011 as Minor Fire-Once
- select three valid founders or mark unavailable
- prefer factionless minors and exclude countries at war with the target
- track founder roles, members, patron, secrecy, cohesion, readiness, suspicion, evidence, counter-readiness, and member confidence
- implement baseline, Evolution I, Evolution II, and Evolution III
- implement active-event evolution and pre-fire evolved openings
- open target counterplay at Evolution II
- implement member invitations and cleanup
- implement war reveal when any member and target become enemies
- create formal Anti-[target country] Pact on reveal and pull valid members into war
- implement public exposure, settlement, fracture, war, victory, defeat, and cleanup routes
- implement decision category and optional Dossier Board GUI
- wire super-event reveal with researched final text, image, and audio
- create and wire required assets and achievements
- update event log, event details, docs, and spreadsheet handoff after final localisation exists

Do not use fallbacks or smaller substitutes without explicit approval. Do not paste planning direction into localisation. Treat mapped content as acceptance criteria.

Run the required subagent audits before claiming completion, especially scripted-system, decision, localisation, asset, super-event, spreadsheet, and completion checks. Report any simplification, blocked asset, missing source, skipped validation, or unresolved plan.
