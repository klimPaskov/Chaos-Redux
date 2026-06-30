# Event 011 Secret Alliance Decision and Mission Implementation Prompt

Implement the dossier decision system from the Secret Alliance spec.

Read AGENTS.md, chaos-redux-events, hoi4-decisions-missions, chaos-redux-event-assets, chaos-redux-frame-animation if animated UI assets are used, and chaos-redux-subagents before editing.

Core requirements:

- Create a staged dossier category that appears at Evolution II.
- Use selected-target flow for human player target actions.
- Keep AI decisions available through direct validity checks without requiring human selector state.
- Use dynamic values for suspicion, evidence, preparedness, pact cohesion, and war readiness.
- Use costs beyond political power and command power. Include support equipment, infantry equipment, trains, convoys, civilian factory burden, army XP, stability, war support, local unit placement, and timed objectives where appropriate.
- Keep command power costs below 60.
- Use named state groups and clear custom tooltips for border, rail, port, factory, and capital defense missions.
- Add mission success, failure, partial success, and cleanup outcomes.
- Hide obsolete decisions after reveal, war, pact collapse, member death, target invalidation, or selected target cleanup.
- Add AI weights that respect target validity, strength, war state, evidence quality, and route risk.
- Ensure the instant reveal war helper is called whenever a member enters war with the target.
- Write final localisation from direction only. Do not paste working labels as final text.
- Write a decision subagent handoff under docs/plans/011_secret_alliance_plans/subagent_handoffs/ if a patch-capable decision subagent edits files.

Run meaningful validation focused on target validity, duplicate active missions, hidden decision clutter, selected-target cleanup, and AI invalid target prevention.
