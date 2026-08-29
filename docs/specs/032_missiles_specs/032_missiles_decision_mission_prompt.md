# Event 32 decision and mission implementation prompt

## Role

Implement and audit the Event 32 decision category, missions, target selection, emergency actions, and `SCN-015` scenario wrapper.

Read these source files first:

- `docs/specs/032_missiles_specs/032_missiles_spec_part_2_program_and_launch_sites.md`
- `docs/specs/032_missiles_specs/032_missiles_spec_part_3_operations_and_consequences.md`
- `docs/specs/032_missiles_specs/032_missiles_spec_part_4_evolutions.md`
- `docs/specs/032_missiles_specs/032_missiles_spec_part_5_decisions_missions_and_scenario.md`
- `docs/specs/032_missiles_specs/032_missiles_spec_part_6_ai_and_probability.md`
- `docs/specs/032_missiles_specs/032_missiles_probability_scenario_matrix.md`
- `docs/specs/032_missiles_specs/032_missiles_asset_prompt.md`
- `AGENTS.md`
- `chaos-redux-events`
- `chaos-redux-decisions-missions`
- `chaos-redux-event-assets`
- the offline Decision Modding, Triggers, Effects, Scopes, Localisation, and Modifiers wiki pages
- installed vanilla decision and raid precedents

## Presentation contract

Use one ordinary Event 32 decision category with a static category picture and concise dynamic header.

The header exposes only:

- Operational Reserve
- Launch Readiness
- Command Control
- a compact guidance status
- current retaliation posture when Automatic Retaliation is active
- selected target and prepared-operation status when relevant

Do not add a dedicated scripted GUI, separate mechanic window, focus inlay, fake control panel, or decorative meter board.

A normal phase should expose three to five primary decisions. Six is the hard maximum. Keep active missions between one and three. Replace obsolete actions by phase and hide invalid actions.

## Category lifecycle

Implement the six phases mapped in part 5:

1. program establishment
2. maintenance and expansion
3. war operations
4. prepared operation
5. incident response
6. retaliation emergency

Only the current phase and relevant emergency actions should remain visible. Cleanup must remove stale targets, operations, missions, site incidents, and emergency actions when their country, state, war, evolution, or incident becomes invalid.

## Establishment and maintenance families

Implement the mapped actions and their dynamic costs, requirements, cooldowns, AI, failure states, and tooltips:

- survey for a launch state
- establish command authority
- resolve a captured site
- replenish operational reserve
- restore launch readiness
- improve guidance and maintenance
- secure launch authority
- harden a launch state
- expand site capacity
- establish a secondary launch state

Use concrete costs such as civilian factory burden, fuel, trains, trucks, support equipment, manpower, stability, war support, army or air experience, and site capacity where the spec assigns them.

An action may consume at most four spendable cost types. Non-consumed state control, technology, war, site, route, and threshold conditions are requirements. Every displayed custom cost needs the correct texticon.

Do not convert the system into political power purchases. Political or command power can support an action when the action is genuinely political or command-based, but they cannot replace the mapped physical costs.

## Human target selection

Use the selected-target category pattern from `chaos-redux-decisions-missions` when the native raid UI does not own the complete target flow.

The human player selects one valid target country, sees only that target's relevant preparation and launch actions, and can clear the selection. Store and clean the selected target safely. AI evaluates all valid targets without using the human selector.

Target eligibility and the visible selected-target state must use the same helpers as operation launch validation.

## Operation families

Implement:

- prepare precision strike
- prepare strategic barrage
- prepare saturation barrage after its evolution
- prepare counterforce strike
- select or clear a special payload after its evolution
- launch the prepared operation
- cancel or stand down before commitment when permitted

Preparation creates a timed mission with an exact target, origin site, reserve reservation, capacity reservation, selected profile, payload, and commitment state.

The launch action must not charge the player twice. Reserve and payload accounting must remain exact across preparation, cancellation, launch, failure, drift, site capture, country removal, and save reload.

The operation effects must call the normalized Event 32 strike contract from part 3. Special payload actions consume real stockpiles and call the existing chemical, biological, nuclear, thermonuclear, Deaths, Air Cleanliness, evidence, and Condemnation systems.

## Missions

Implement distinct goal-style or timed missions for:

- launch-state survey
- secondary-site construction
- site repair
- strike preparation
- site recovery
- warning verification
- retaliation-network restoration

A mission should auto-complete when the mapped objective is satisfied. Do not require a second payment click after the player has done the work.

Use varied durations based on task scale. Preserve the public duration and consequence. Failure must call a distinct failure path and can create readiness loss, reserve loss, higher command pressure, site compromise, harder follow-up work, or incident escalation where mapped.

## Incident and aftermath actions

Implement the mapped bounded responses:

- inspect the incident
- accelerate recovery
- compensate an accidental neutral victim
- deny responsibility
- suspend a damaged site
- emergency guidance recalibration
- investigate debris

Evidence, attribution, apology, denial, compensation, and diplomatic effects must use the same incident record as the strike outcome. A country cannot compensate or deny an incident that does not belong to it.

## Rogue Launch Commands actions

Implement:

- rotate emergency codes
- isolate the site
- send loyal forces
- negotiate with the command
- scuttle the site
- retake the site

Each action needs exact site ownership, control, reserve, security, and prepared-operation proof. Scuttling destroys the mapped capacity and reserve. Recovery cannot duplicate missiles or restore destroyed payloads.

## Automatic Retaliation actions

Implement retaliation-posture selection and the emergency actions:

- verify warning
- delay retaliation
- sever the network
- isolate one site
- change target only when the accepted spec and engine proof permit it
- accept the response
- restore the retaliation network

The warning window reads one incident root. Actions must be idempotent. No option can create direct recursive launches. Every accepted response enters the bounded incident queue.

## AI and weighted behavior

Give AI an equivalent path for every action family.

Use the doctrine profiles and reserve floors in part 6. AI must understand maintenance, site security, restraint, target value, civilian risk, neutral adjacency, payload stockpile, enemy first use, attribution confidence, imminent defeat, and retaliation posture.

Before changing any weight, route the surface through `chaosx_ai_probability_auditor`. Start with `hoi4.probability_inspect`, use the named scenarios in the probability matrix, apply the bounded patch through the owning agent, then run `hoi4.probability_compare` against the same scenarios.

Do not accept score-only evidence as exact probability when the pool or external state is incomplete.

## SCN-015

Implement the planned collision-free scenario identity only after repeating the current scenario-registry audit.

Working public name: Missile Age.

Profiles:

- Global Proliferation
- Saturation War
- Command Breakdown
- Special Payload Crisis
- Retaliation Network

Wire all four shared intensities. The scenario must use one atomic preflight and commit transaction, respect impossible and terminal-state blockers, clean its bypass flags, and never award Event 32 achievements.

The scenario reuses the shared scenario window. Do not add dedicated scenario art or a new scenario GUI.

## Localisation, assets, docs, and audit

Write final decision, mission, cost, requirement, target, incident, and scenario localisation from the spec direction. Keep costs icon-first and concise. Use custom trigger tooltips for long requirements.

Wire only final icons created by the Event 32 asset package. Do not use unrelated generic icons as completion fallbacks.

Update Event 32 docs, scenario docs, Event Details, test coverage, and the authoritative catalog workbook. Regenerate the CSV exports through the repository exporter.

After implementation, run `chaosx_decision_mission_auditor`. Resolve every local patch or carry every broad design gap into a reported plan. Do not claim completion with stale actions, duplicate missions, missing AI, unproved costs, missing icons, unresolved target cleanup, or an untested scenario transaction.
