# Event 023 decision and mission implementation prompt

Implement and audit the complete Event 23 decision and mission system from:

- `023_sov_nuclear_bombs_spec_part_1_core.md` through Part 10.
- `023_sov_nuclear_bombs_decision_map.md`.
- `023_sov_nuclear_bombs_probability_scenarios.md`.

This prompt is for the decision and mission owner after the parent has verified or implemented the required shared nuclear, ledger, Event 5, and event-log helpers.

## Required reading

Read:

- `AGENTS.md`.
- `chaos-redux-events`.
- `chaos-redux-decisions-missions`.
- `chaos-redux-subagents`.
- `chaos-redux-event-assets` for icon consumers.
- Relevant offline wiki pages and current vanilla documentation.
- Current Event 23 and Event 5 source.
- Current shared nuclear consequence and delivery source.

Inspect current decision precedents before editing.

## Surface

Implement:

- Event 23 decision category.
- Optional linked collapse-custody category only if verified engine constraints require it.
- Dynamic header for bomb count, Readiness, Integrity, posture, and public knowledge.
- All opening, storage, production, delivery, testing, targeting, coercion, authorization, exchange, collapse, dismantlement, and moratorium actions mapped in the decision map.
- Target response missions and events required by decisions.
- AI-equivalent actions.
- Cleanup, persistence, costs, tooltips, and dynamic localisation.

Do not create a full scripted GUI. Use ordinary decisions, missions, selected-target management, selected-site management, category text, tooltips, and static art.

## Clarity and clutter

- Show three to five primary actions in a normal phase.
- Six visible primary actions is the hard maximum.
- Keep active missions between one and three.
- Hide obsolete and invalid actions.
- Use phase replacement and target selection.
- Expose no more than the four header items defined by the spec.
- Use concise tooltips and named targets.

## Costs

- Use no more than four spendable cost types per action.
- Use costs that fit the action, including equipment, fuel, trains, experience, manpower commitment, civilian capacity, and conservative command power.
- Do not default every action to political power.
- Cost localisation is icon-first.
- Nonconsumed state, route, force, war, and diplomacy conditions remain requirements.

## Bomb and custody accounting

- Every test or strike reserves one exact bomb.
- Cancel, failure, release, transfer, dismantlement, destruction, and recovery reconcile once.
- No mission may duplicate a bomb on cancel or reload.
- Reactor entitlements reconcile once.
- State transfer uses the Event 23 custody ledger.
- Breakaway physical custody does not grant operational use.

## Targeting

- Use the selected-target pattern.
- AI evaluates the complete target pool without the human selector.
- Demands are specific and route-valid.
- Target response is timed and includes acceptance, partial settlement, delay, refusal, foreign support, exposure, evacuation, and route-specific choices.
- Exact strike state is selected and rechecked.
- Invalid states do not redirect automatically.
- Final authorization is separate and deliberate.

## Shared consequences

The decision system supplies validated context to the shared nuclear adapter. It does not apply duplicate deaths, population loss, building damage, contamination, Air Cleanliness, condemnation, direct nuclear-use Chaos, or Fallout progression.

## AI and probability

Before patching complex weights, use `chaosx_ai_probability_auditor` with `fork_context=false` and the named scenarios.

After the owner applies the accepted balance change, rerun the same scenarios through `hoi4.probability_compare`.

AI major first use is impossible below Evolution IV. At Evolution IV it remains gated and rare.

## Localisation

Write final in-world text from the direction in Part 8.

Do not paste working labels automatically.

Add custom trigger tooltips for long conditions. Show exact selected countries, states, regions, counts, costs, and deadlines. Do not expose hidden AI scores, future incidents, or achievement conditions.

## Assets

Use locked sprite names and final icons from the Event 23 asset handoff. Do not substitute generic, resized, or placeholder art.

## Audit and handoff

Run `chaosx_decision_mission_auditor` after the implementation tranche. It may make bounded fixes inside this surface.

Write the handoff to:

`docs/plans/023_sov_nuclear_bombs_plans/subagent_handoffs/`

Include:

- Files changed.
- Category and decision IDs.
- Mission IDs.
- Helper calls.
- Costs and dynamic factors.
- AI surfaces and probability evidence.
- Cleanup and persistence behavior.
- Asset consumers.
- Meaningful validation scenarios.
- Remaining gaps or simplifications.

Do not claim completion while any accepted decision family, target response, AI route, localisation, icon, cleanup, or accounting rule is missing.
