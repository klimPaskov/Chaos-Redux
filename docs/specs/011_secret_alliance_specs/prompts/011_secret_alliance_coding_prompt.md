# Event 011 Secret Alliance Coding Prompt

Implement Event 011 Secret Alliance according to the source spec pack under `docs/specs/011_secret_alliance_specs/`.

Read and follow AGENTS.md, chaos-redux-events, hoi4-decisions-missions, chaos-redux-event-assets, chaos-redux-frame-animation for animated UI pieces, chaos-redux-super-events for the public reveal super-event, chaos-redux-improvement-loop, and chaos-redux-subagents.

Implement the full hidden compact system:

- Fire-once root event `chaosx.nr11.1` for the current player target.
- Select three valid founding countries that are not at war with the target, preferring factionless minors.
- Store convenor, purse holder, and knife hand roles.
- Track dynamic secrecy, cohesion, aggression, war readiness, suspicion, evidence, preparedness, identified members, and member commitment.
- Add baseline incidents, Evolution I minor recruitment, Evolution II dossier and sabotage, and Evolution III public compact behavior.
- Keep ordinary baseline progress separate from evolution log entries.
- Add the dossier decision category with selected-target flow, dynamic costs, timed missions, target cleanup, and AI equivalents.
- Implement player routes for counterintelligence, hardening, exposure, splitter diplomacy, border handling, and war preparation.
- Implement the instant reveal rule when any pact member goes to war with the target. Create the Anti-[target] Pact, add all valid members, and call them into war.
- Implement public compact war timer, ultimatums, member splitting, defection, border war isolation, pact defeat, pact collapse, and pact victory outcomes.
- Implement achievement tracking from the achievement prompt.
- Implement super-event research and wiring for the public compact reveal when its trigger conditions are met. Treat unresearched title, button remark, quote, cultural reference, and audio as blockers.
- Create and wire required assets from the asset prompt, including static fallbacks and frame-sheet animations.
- Update event log, event details, evolution details, docs, and spreadsheet-facing wording from final localisation.
- Do not paste working labels as final localisation.
- Do not use fallback trees, placeholder assets, or hardcoded scattered values.
- Keep the event outside cluster registration unless a later accepted spec changes that.

Use patch-capable subagents from the subagent prompt file when their surfaces are implemented. Every subagent patch needs a handoff under `docs/plans/011_secret_alliance_plans/subagent_handoffs/`.

Do not claim completion until the implemented files satisfy the spec, assets are real and documented, localisation exists, AI behavior works, and meaningful target-specific validation has been performed. Report any simplification, omission, or blocker clearly.
