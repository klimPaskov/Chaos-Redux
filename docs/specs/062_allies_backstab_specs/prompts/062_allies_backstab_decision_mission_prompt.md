# Event 062 decision and mission implementation prompt

Implement and audit the temporary crisis decision system for Chaos Redux Event 62, Allies Backstab.

Read every Event 62 spec and quality file, with special attention to:

- `specs/062_allies_backstab_spec_part_4_decisions_and_missions.md`
- `specs/062_allies_backstab_spec_part_3_transaction_and_war.md`
- `quality/062_allies_backstab_probability_scenarios.md`
- `quality/062_allies_backstab_acceptance_scenarios.md`

Also read `AGENTS.md`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, and `chaos-redux-subagents`.

## Presentation

Use one ordinary Event 62 decision category with role-specific text and a static category picture. Do not add a dedicated scripted GUI.

Expose one public value, working label `Crisis Cohesion`. Show the exact value, stage, next threshold, principal recent cause, side leader, opponent, and active mission in a compact header.

Keep hidden target, side-choice, war-viability, sponsor, and settlement calculations internal.

## Role variants

Implement role-aware actions for:

- original faction leader
- retained loyalist member
- expelled government
- expelled-group leader
- pending Evolution II member
- neutral withdrawal member
- selected outside sponsor or mediator

A country sees only actions for its current role and phase.

## Visibility and clutter

- three to five primary actions per role and phase
- six hard maximum
- one to three active missions
- hidden queue for lower-priority missions
- selected-target pattern for human multi-target actions
- AI sees valid targets without depending on human selection state
- obsolete actions disappear immediately after role, war, target, or settlement changes

## Costs

Centralize cost floors, scaling steps, and caps. Use meaningful equipment, fuel, XP, manpower, stability, war support, factory burden, transport, or command costs.

No action may contain more than four spendable cost types. Every displayed cost needs the correct texticon. Conditions such as capital control, divisions in a region, or route access are requirements and remain separate.

Do not use small political power purchases as the main effect.

## Required action families

Original leader:

- secure the war council
- demand renewed commitments
- coordinate punitive operations
- offer conditional readmission
- recognize separation

Retained member:

- reaffirm the faction
- demand a mutual security charter
- withhold forces
- join the expelled governments at Evolution II or III
- withdraw neutrally when legal

Expelled government:

- emergency mobilization
- secure the capital and supply spine
- open the expelled-governments liaison
- request a foreign lifeline
- pool emergency reserves
- seek recognized separation
- form a successor compact

Outside sponsor:

- guarantee the expelled governments
- back the original faction
- convene an armistice conference
- threaten direct intervention only when high-Evolution or treaty proof allows it

The full behavior, costs, risks, and AI direction are in the source spec.

## Required missions

- Hold the Government Together
- Break the Expelled Resistance
- Keep the Expelled Governments Connected
- Prevent a Second Defection
- Decide the Bloc
- Secure an Armistice

Use varied durations from the accepted ranges. Goal-style missions auto-complete. Success, partial success, and failure need distinct effects.

Dynamic tooltips must name the exact capital, state group, route, side leader, opponent, required divisions, and deadline. Do not expose raw state IDs.

## AI and probability

Run `chaosx_ai_probability_auditor` before patching weighted decision or mission logic. Use `hoi4.probability_inspect` and the named `AB-DEC`, `AB-SPN`, and `AB-SET` scenarios.

After implementation and balance changes, run the same auditor with `hoi4.probability_compare` against the same scenarios.

Unpayable or invalid actions must have zero AI probability.

## Cleanup

Clear decisions, missions, selected targets, target flags, stored IDs, category state, temporary access, pending offers, and active registry membership after:

- settlement
- war end
- target death or annexation
- faction dissolution
- role change
- wider-war handoff
- successor compact formation

Durable betrayal, guarantee, settlement, cooldown, and achievement receipts remain.

## Audit

After parent implementation, spawn `chaosx_decision_mission_auditor` with no inherited context. Permit only bounded fixes inside Event 62 and direct dependencies.

The handoff must list changed files, decision and mission IDs, costs, AI changes, cleanup hooks, task-specific validation, skipped evidence, and remaining gaps.
