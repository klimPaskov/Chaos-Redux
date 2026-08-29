# Decision and Mission Prompt: Event 24 Video Game in Sweden

Implement the Event 24 decision category, decisions, missions, dynamic text, AI behavior, cleanup, and balance according to the complete source specification package at:

`docs/specs/024_video_game_in_sweden_specs/`

Read and follow `AGENTS.md`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-subagents`, the offline Decision Modding, Triggers, Effects, Scopes, Localisation, Modifiers, and Data Structures pages, vanilla documentation, and relevant vanilla decision precedents.

Use `fork_context=false` for project subagents. Spawn `chaosx_decision_mission_auditor` after the implementation pass. Route every weighted AI or probability surface through `chaosx_ai_probability_auditor` before and after changes.

## Category contract

Create one Event 24 category owned by the principal Swedish host.

Working category id:

`video_game_in_sweden_program`

The category shows:

- Simulation Reliance as the only player-managed value.
- Current named stage and next threshold.
- Current program phase.
- Current review or mission state.
- One static category picture from the Event 24 asset handoff.

Use the normal category as the complete player-facing surface. Keep internal score components, hidden chance values, and incident weights out of the visible presentation, and keep the text concise.

Normal phase budget:

- Three to five primary visible actions.
- Six is forbidden.
- Zero or one active mission.
- One concise category header.
- Tooltips normally use two to four short lines for one action or value, plus precise requirements where needed.

Obsolete actions must hide or be replaced when the phase changes.

## Core value

Implement Simulation Reliance on a 0 to 100 scale with these public states:

- Instrument, 0 to 24.
- Habit, 25 to 49.
- Doctrine, 50 to 74.
- Worldview, 75 to 100.

Centralize thresholds, gains, losses, cooldowns, mission durations, and AI weights. Every action that changes Reliance must display the change. Clamp the value. No hidden fifth player-facing value is authorized.

## Baseline actions

Implement the full mapped behavior from `024_video_game_in_sweden_decision_map.md`:

- Controlled staff exercise.
- Commission a logistics module.
- Expand access according to the chosen release route.
- Conclude the trial.

The baseline can end without any evolution. AI must conclude a low-value program after the review period instead of maintaining it forever.

## Evolution I actions

Implement:

- Publish a rules revision.
- Field-validation exercise.
- Independent red team.
- Formalize or limit the officer league.

Rules Revision needs cooldown and escalating staff cost. It may improve the staged idea, but it must also move Reliance or incident risk.

Field Validation starts a real 90 to 120 day objective. It commits fuel, support equipment, trains, and army experience. These are four spendable cost types and the hard limit. Division placement, control of regions, Stockholm, and supply are requirements. The mission auto-completes. Implement full success, partial success, and failure with distinct effects.

## Evolution II actions

Implement:

- Hold a national league season.
- Protect essential shifts.
- Direct clubs toward preparedness.
- License foreign editions.
- Separate play from policy.

Use phased visibility and cooldowns. National League must create a meaningful public benefit and productivity risk. Protect Essential Shifts must materially address that risk. Foreign Licensing uses a bounded target flow and never displays one decision per possible country. Stop after three meaningful foreign responses.

## Evolution III actions

The initial Evolution III phase shows only:

- Begin Reality Audit.
- Establish Dual-Track Staff System.
- Restrict Official and Public Use.
- Trust the Model.

Selecting one hides the other initial choices and opens only that route's follow-up actions.

### Reality Audit

Create the main 120 to 180 day mission. Require supplied divisions across southern, central, and northern Swedish conditions or equivalent active fronts, continued control of Stockholm, committed resources, one logistics review, and one red-team result.

Implement full success, partial success, and failure. Failure must retain a cheaper restriction route and a narrower re-audit. It must never dead-end the event.

### Dual-Track Staff System

Create one verification mission. Cap Reliance below Worldview, retain moderate benefits, and close the severe incident pool after success. Failure returns the player to audit or restriction.

### Restriction

Create a short enforcement period. Remove Event 24 benefits, lower Reliance quickly, apply the defined finite backlash, then close the category.

### Trust the Model

Create a finite maximum-reliance surge. Apply strong temporary planning and army-experience benefits together with serious supply, adaptability, recovery, stability, or political-attention risks. Start mandatory reassessment. End or accelerate reassessment after war resolution, core loss, capital threat, severe supply failure, major mismatch, or the maximum duration. The surge cannot restart.

## Cost and requirement rules

- No action may use more than four spendable cost types.
- Use the correct texticon for every displayed spendable cost.
- Do not spell out resource names in cost strings when a valid texticon exists.
- Keep requirements separate from costs.
- Use custom trigger tooltips for named Swedish regions, division counts, supply, partner validity, autonomy, and opponent qualification.
- Use political power and command power only where they fit the action. Do not make them the whole cost model.
- Costs, durations, cooldowns, and effects should respond to war state, supply, industry, prior failures, route, Reliance, and Chaos where mapped.

## Mission and incident integration

Implement the incident families defined in the decision map:

- Terrain mismatch.
- Supply mismatch.
- Enemy adaptation.
- Over-standardized template.
- Diplomatic category error.
- Workplace distraction.
- Party appropriation.

Incidents must be campaign-valid, cooldown-controlled, and less likely after relevant validation. Prefer a new valid family before immediate repetition. Do not create an incident that lacks its required target or campaign condition.

## AI

Implement the AI matrix and named scenarios in:

`024_video_game_in_sweden_ai_probability_scenarios.md`

AI must check material ability before starting missions. Trust the Model is invalid or near zero when Sweden is near capitulation, lacks supply resources, recently lost a core, or suffered a severe mismatch. Audit and restriction become strong after supply failure and territorial loss.

Run the complete probability audit cycle:

1. Baseline `hoi4.probability_inspect` and named scenarios.
2. Owner-applied weights.
3. `hoi4.probability_compare` with the same scenarios.
4. Record exact, bounded, sampled, score-only, or unresolved status accurately.

## Cleanup and persistence

Persist route, Reliance, phase, mission progress, incident memory, foreign partners, commander target, and reassessment deadline through save and reload.

Clean all Event 24 decisions, missions, temporary targets, obsolete ideas, and scheduling state after conclusion, annexation, invalid actor, civil-war host change, or event disable. Preserve fire-once history, recorded evolutions, valid achievement proof, and surviving commander trait results.

Do not use a recurring whole-world scan. Keep runtime work scoped to the active Swedish host, event timers, bounded on-actions, and decision evaluation.

## Localisation and assets

Write final category, decision, mission, cost, requirement, success, failure, and tooltip text from the specification's direction. Do not copy working labels blindly. Follow the Event 24 writing rules.

Wire the static category picture and decision icons from `024_video_game_in_sweden_asset_prompt.md`. No placeholder, wrong icon type, or fake UI artwork is acceptable.

## Required audit and handoff

Spawn `chaosx_decision_mission_auditor` with `fork_context=false` after implementation. The audit must cover:

- Visible action count and category clarity.
- Cost count and texticon coverage.
- Mission quality and duration.
- Full, partial, and failure behavior.
- AI validity and probability evidence.
- Cleanup and save persistence.
- Exploit loops and repeated rewards.
- Focus integration marked not applicable.
- Event Log and evolution integration.

Write a handoff under:

`docs/plans/024_video_game_in_sweden_plans/subagent_handoffs/`

Do not claim completion while any mapped decision, mission, AI route, tooltip, asset, cleanup state, or probability scenario is missing. No simplification is authorized without explicit user approval.
