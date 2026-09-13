# Event 049 Doomsday Decision and Mission Implementation Prompt

## Role

Implement the complete Event 049 country response, mission, countdown, authority-transfer, terminal-support, and failed-date reconstruction decision system.

Read:

- `specs/049_doomsday_spec_part_1_core.md`
- `specs/049_doomsday_spec_part_2_simulation.md`
- `specs/049_doomsday_spec_part_3_societies_and_responses.md`
- `specs/049_doomsday_spec_part_4_decisions_and_missions.md`
- `specs/049_doomsday_spec_part_5_war_economy_and_institutions.md`
- `specs/049_doomsday_spec_part_6_evolutions.md`
- `specs/049_doomsday_spec_part_8_final_vigil.md`
- `specs/049_doomsday_spec_part_9_last_day_and_aftermath.md`
- `quality/049_doomsday_probability_scenarios.md`
- `quality/049_doomsday_acceptance_matrix.md`

Follow `AGENTS.md`, `chaos-redux-decisions-missions`, `chaos-redux-events`, `chaos-redux-event-assets`, and `chaos-redux-subagents`.

## Core presentation contract

Use one normal event-owned decision category with a strong stage-specific static category picture and compact dynamic header.

Do not create a full scripted mechanic window.

The only persistent public event values are:

- Doomsday Conviction.
- Time Until the End.

The header may show a qualitative posture and institutional status. It must not expose additional persistent numeric counters.

Use five stage pictures from the asset prompt. Do not paint fake controls into them.

## Visibility and capacity

- Show three to five primary decisions in a normal phase.
- Never show more than six primary decisions in one phase.
- Keep active missions between one and three.
- Replace obsolete decisions as the countdown advances.
- Hide invalid war, country, institution, state, and target actions.
- Use selected-target handling only where a large dynamic target family requires it.
- Keep AI access valid without forcing the player to inspect every possible target.

## Cost rules

- A decision or gameplay-changing action can use at most four spendable cost types.
- Use icon-first compact cost localisation.
- Use political power only for genuinely political or bureaucratic work.
- Use equipment, manpower, fuel, trains, convoys, XP, Command Power, stability, War Support, civilian capacity, military capacity, unit commitment, route access, and time pressure where they fit.
- Command Power cannot exceed the project cap.
- Do not use repeated tiny modifiers or reward dust as the main result.
- Every important action must alter institutions, map work, military behavior, movement state, diplomacy, war, recovery, or another visible choice.

## Phase implementation

### Phase 1: First response

Implement the six posture commitments:

- Civic Continuity.
- Concordat of Vigil.
- Emergency Order.
- National Preparation.
- Peace Before the End when at war.
- Nothing Left to Lose when the late militarist conditions exist.

Each posture needs a real package, AI logic, commitment lock, and one bounded emergency realignment route.

### Phase 2: Institutional continuity

Implement the mission pool for:

- Schools and universities.
- Technical institutes.
- Rail and food network.
- Military rolls and depots.
- Archives and registers.
- Hospitals and public health.

Use named states, rail hubs, ports, capitals, institutions, or regions where possible.

Typical mission durations range from 90 to 210 days according to difficulty. Shorter emergency missions require clear countdown justification.

Each mission needs success, partial success where useful, failure, AI, and cleanup.

### Phase 3: War and peace

Implement contextual actions for:

- Exploratory armistice talks.
- Humanitarian agreements.
- Time-limited Last Day truces.
- Full armistice frameworks.
- Conscientious service.
- Prisoner and objector release.
- Defensive-only military command.
- Arms-line conversion.
- One defined final offensive for Nothing Left to Lose.

Do not white-peace every war. Use war context, enemy willingness, casualties, war direction, War Support, Conviction, organization, and remaining time.

### Phase 3 for peace countries

Implement relevant alternatives for:

- Public evidence.
- Movement cooperation.
- Fraud exposure.
- Shelter and reserve work.
- Transport and labor continuity.
- Hoarding and public-order control.

### Phase 4: Last Calendar policies

When Evolution I is active, implement rotating posture-relevant policies for:

- Military program wind-down.
- Project cancellation or preservation.
- Prisoner policy.
- Border opening and family reunion.
- Debt settlement.
- Reserve distribution.
- Shelters and continuity sites.
- Public observance.
- Movement representation.

Do not show every policy simultaneously.

### Phase 5: Parallel government

When Evolution II is active, implement:

- Voluntary custodial transfer.
- Constitutional or national assembly transfer.
- Municipal service transfer.
- Defensive-only military transfer.
- Existing-government continuity defense.
- High-risk action against parallel government.
- Final Assembly observer and membership petitions.

Player countries require explicit player-facing choices where the design calls for voluntary transfer. Do not use AI-only silent surrender.

### Phase 6: Final month

Replace ordinary actions with a limited priority set covering:

- Food and water.
- Hospitals and burial services.
- Archives and seed.
- Communications.
- Public vigils.
- Prisoners.
- Military standing orders.
- Family transport.
- Reopening plans.

The player cannot complete every priority at maximum strength.

### Phase 7: Failed-date reconstruction

Implement staged actions for:

- Reopening education and research.
- Recalling skilled personnel.
- Restoring transport and essential production.
- Settling debt, property, wages, and emergency currencies.
- Reconstituting or reforming the military.
- Converting shelters.
- Reintegrating settlements.
- Investigating suppression.
- Resolving or integrating society institutions.
- Closing the Last Calendar.

No single political power purchase can restore the country.

## Shared-system contracts

- Famine owns Food Security, Food Reserves, Relief Access, relief missions, and mortality.
- Migration owns population transfer, border policy, trapped people, settlement, and route deaths.
- Deaths owns real population loss records.
- Condemnation owns proven public atrocity and cover-up consequences.
- Air Cleanliness owns atmospheric state.
- Event 049 can submit and receive bounded proof. It cannot create duplicate values or transactions.

Use `uses_normal_civilian_systems` for ordinary eligibility. Doomsday administrations remain ordinary human countries and should not be added to nonhuman classifiers.

## Dynamic design

Centralize thresholds, durations, caps, costs, cooldowns, gains, losses, and AI tuning through script constants or the established tuning pattern.

Keep hidden:

- Local conviction.
- Society organization and current shares.
- Backlash.
- Institutional continuity.
- Peace pressure.
- Terminal readiness.

Turn them into concise qualitative text and action availability where the player needs information.

## AI and probability

Before changing any AI weight, MTTH, random selection, target score, or option chance:

1. Spawn `chaosx_ai_probability_auditor` with the named scenarios from `quality/049_doomsday_probability_scenarios.md`.
2. Establish baseline evidence through `hoi4.probability_inspect` and the correct evaluate, sweep, simulate, sequence, or render route.
3. Apply the bounded owner patch.
4. Run `hoi4.probability_compare` against the same scenarios.

The auditor is read-only. The parent or decision owner chooses the intended balance.

## Cleanup and exploits

Prevent:

- Posture switching rewards.
- Suppression cycling.
- Armistice spam.
- Shelter and reserve farming.
- Arms-conversion duplication.
- Government-transfer reversal farming.
- Assembly membership cycling.
- Revised-date repetition.
- Stale war, country, and state targets.

Cleanup must cover war end, annexation, country invalidation, evolution disable, government transfer, Final Vigil commitment, date failure, tag switch, and system closure.

## Localisation and assets

Write final player-facing text from the specification direction. Do not copy working labels without review.

Every cost, blocked requirement, named region, mission objective, success, partial success, failure, and posture consequence needs clear localisation.

Use the final category pictures, category icon, and decision icons from `prompts/049_doomsday_asset_prompt.md`.

## Audit and handoff

After implementation, spawn `chaosx_decision_mission_auditor` for a full pass over:

- Category lifecycle.
- Visibility cap.
- Mission quality.
- Cost budget.
- Tooltips.
- AI validity.
- Cleanup.
- Duplicate actions.
- Exploit risk.
- Shared-system transactions.
- Localisation.

Return a handoff with changed files, category and decision IDs, mission IDs, dynamic helper names, AI and probability evidence, meaningful validation, unresolved risks, and parent follow-up.

Do not claim completion while any required phase is missing, passive, cluttered, unlocalized, exploitable, or disconnected from the two-value mechanic.
