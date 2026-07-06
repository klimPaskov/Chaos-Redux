Implement Event 11, Secret Alliance, from `docs/specs/011_secret_alliance_specs/`. Use `prompts/secret_alliance_coding_prompt.md`, `prompts/secret_alliance_decision_mission_prompt.md`, `prompts/secret_alliance_asset_prompt.md`, `prompts/secret_alliance_super_event_prompt.md`, and `prompts/secret_alliance_achievement_prompt.md`.

Pass or fail requirements:
- Minor Fire-Once hidden pact against the current player.
- Three initial valid countries, not at war with the player, preferring minors outside factions.
- Hidden roles, membership rings, Evidence, Preparedness, player isolation, Pact Cohesion, Pact Readiness, and War Clock.
- Baseline subtle incidents, Evolution I minor expansion, Evolution II major patron and dossier decisions, Evolution III public faction and war pressure.
- If first fired at Evolution III conditions, open through Evolution II first.
- If a full pact country goes to war with the player, reveal the pact, form Anti-[player country] Pact, and call full signatories into war.
- Decision costs must use concrete resources and objectives, not mostly PP or CP.
- Implement AI motive logic, target safety, invitation logic, reveal behavior, war entry, and exit behavior.
- Complete super-event research and wiring. Unresearched title, quote, cultural remark, image, or audio is a blocker.
- Create all required icons, achievement icons, super-event image, and any animated assets with static fallbacks.
- Update event docs, Event Details, evolution log text, localisation, assets, and catalog wording after final in-game text exists.
- Spawn `chaosx_improvement_loop_planner` with `fork_context=false` near completion and resolve its addendum or closure handoff before any completion claim.
- Run relevant auditors and a completion audit. Do not claim completion until the implementation satisfies the spec with no undisclosed fallback or simplification.
