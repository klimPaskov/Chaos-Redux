# Event 40 Improvement Loop Review

## Review status

This is a parent-authored improvement review based on the supplied improvement-loop skill. The dedicated improvement-loop subagent could not be invoked in the available tool environment. No subagent output is represented here.

## Playable promise

The event promises a contest over foreign influence, local sovereignty, arms, political promises, intelligence, and regional state formation. It should feel different depending on whether the player is Britain, the active Arabian target, an earlier client, a resistant neighbor, or a federation core.

The final specification supports that promise through:

- one clear public value
- material British commitments
- compact target and sponsor action sets
- character state for Lawrence
- internal regional progression after one Fire-Once entry
- armed escalation only after Evolution I
- a client system only after Evolution II
- three federation outcomes only after Evolution III
- permanent consequences that other events can read

## Gaps found in the original brief

### Lawrence's death before 1936

The brief treated Lawrence as readily available. That would conflict with the standard start date.

Accepted improvement:

- concealed survival is part of the entry premise
- later death is permanent
- existing-character ownership is audited

### Risk of a lone-savior narrative

The brief could be implemented as one British character overpowering passive governments.

Accepted improvement:

- local leaders, officers, governments, and institutions control outcomes
- British resources and promises matter
- Lawrence is a liaison and catalyst
- the federation normally uses a legitimate local core

### Regional chain versus Fire-Once classification

The brief correctly asked for a Fire-Once event with repeated regional stages, while the catalog still said Minor Repeatable.

Accepted improvement:

- only the entry uses the random event system
- later interventions are internal stages
- catalog correction is mandatory

### Influence could become too abstract

A single value can become a disguised progress bar when it has no concrete actions.

Accepted improvement:

- Influence responds to arms, gold, officers, routes, intelligence, promises, missions, wars, and institutions
- every major movement has a visible cause
- hidden components stay internal

### Evolution I could cause random civil wars

The revolt-network premise could produce repeated arbitrary country splits.

Accepted improvement:

- cells use real routes and political conditions
- coups require a valid coalition
- civil wars require viable territory, forces, supply, and rollback
- strong intelligence can stop escalation

### Evolution II could become a generic faction

A British regional system could be reduced to one faction button and flat bonuses.

Accepted improvement:

- clients contribute ports, rail, air routes, equipment, officers, intelligence, and diplomacy
- clients can refuse and seek autonomy
- existing faction structures are reused where valid
- regional institutions require real participants

### Evolution III could create free annexation and cores

A broad federation can easily become an instant reward dump.

Accepted improvement:

- formation requires a congress and ratification
- one validated transaction handles transfer
- founding states and disputed territories receive different treatment
- cores are staged
- the new country begins with administrative, command, and political problems

### Lawrence's Kingdom could dominate the event

The rare route could overshadow stronger British and independent outcomes.

Accepted improvement:

- strict hidden conditions
- at least three governments or equivalent base
- no stronger uncontested claimant
- extremely low AI preference
- succession and institutionalization are mandatory

## Design additions accepted

### One public value

Keeping only Lawrence's Influence at baseline gives the player a clear state without stripping depth from the simulation.

### Qualitative hidden facts

Regional reach, cells, trust, credibility, and federation readiness remain available to script and AI without becoming player homework.

### Target-owned national custody route

This creates a meaningful middle path between rejection and puppeting.

### Evidence and double-game route

This makes strong intelligence useful and allows a target to exploit British aid without a guaranteed result.

### Client autonomy politics

This keeps British clients playable and supports later federation transitions.

### Federal Authority after formation

The federation receives one relevant new value after Lawrence's Influence has ended. The two values are not active together as permanent player burdens.

### Outcome-specific super-events

British Arabia, Independent Arab Federation, and Lawrence's Kingdom change regional order enough to justify super-events.

## Additions rejected

### Dedicated scripted GUI

Rejected because one value, a small action set, and selected-target logic fit the ordinary decision system. A custom window would add layout and maintenance without improving decisions.

### Triggerable scenario

Rejected because Event 40 has no separate sandbox premise that needs manual type and intensity controls. Normal force-trigger testing is enough.

### Custom 3D units

Rejected because the event uses officers, irregulars, local armies, and transport forces that existing HOI4 unit families can represent.

### Baseline animated portrait

Rejected because motion does not clarify Lawrence's state and increases portrait risk for a real historical person.

### A separate public British Reach meter

Rejected because the player can infer current British access from category state, route actions, and tooltips. The value remains internal.

### A separate public Cell Strength meter

Rejected because cells matter only after Evolution I and can be shown as incident states, missions, and warnings.

### Full focus trees for every target

Rejected because ordinary targets retain their country identity. The dedicated tree belongs to the durable federation.

### Automatic federation at 600 Chaos

Rejected because the evolution threshold unlocks content. It does not create participants, legitimacy, or a valid state.

### A world-end branch

Rejected because even a large Arabian federation remains a regional order change. It does not resolve or end the global campaign.

## Complexity review

### Player-facing values

- Active intervention: Lawrence's Influence
- Post-formation federation: Federal Authority

The values do not normally coexist as two active event meters. The design is inside the project budget.

### Visible decisions

- normal phase: three to five
- hard maximum: six
- active missions: one or two

### Country-package count

- ordinary targets: no new full package
- temporary revolts: bounded crisis package only when needed
- permanent federation: one full package with origin variants

### Super-events

- three possible formation super-events
- one fires in a campaign unless separate federations are explicitly allowed by future design

## Remaining implementation risks

- exact Arabian target registry must be reconciled with current map tags and state data
- Lawrence character ownership may conflict with vanilla or another mod package
- federation tag or transformation carrier requires collision review
- unit and stockpile transfer needs transactional validation
- focus tree needs MCP render and first-glance audit
- weighted target, AI, incident, and rare-route logic needs probability evidence
- real-person portrait sourcing needs independent review
- super-event quotes and audio need separate source research
- exact no-DLC intelligence fallback needs balance work

These are implementation tasks. They do not require broad new event design.

## Closure recommendation

Broad expansion is no longer recommended before implementation. The event has a complete playable loop, escalation, regional system, federation package, AI plan, asset boundary, achievements, cross-event connections, cleanup, and acceptance scenarios.

A later improvement pass is justified only after implementation creates a new design problem that this specification did not resolve. The next work should focus on implementation, evidence, balance, assets, localisation, documentation, and audit.
