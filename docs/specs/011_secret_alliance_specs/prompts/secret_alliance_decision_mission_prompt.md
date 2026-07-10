# Decision and mission implementation prompt: Event 011 Secret Alliance

Implement the full decision, mission, and mechanic-window system described in the five event spec parts and `matrices/011_secret_alliance_decision_mission_matrix.md`. Follow the project decisions and missions skill, event skill, and frame-animation skill.

## Core category behavior

The dedicated category opens at Evolution II under a public foreign-interference identity. It must not reveal the pact name or confirmed membership until the player has evidence. The category changes presentation at Evolution III and after reveal.

Show:

- Evidence
- Preparedness
- recent incident
- broad coordination estimate
- up to three selected suspects with confidence bands
- active mission status
- Evolution III war pressure when applicable

Use a compact scripted GUI attached to the decision category only if the final layout is clearer than ordinary category text. Every button must call the same validated cost, effect, AI, logging, and cleanup logic as the decision system.

## Required decision families

Implement all families mapped in the matrix:

- investigation
- counterintelligence missions
- protection projects
- diplomatic probes
- deception and offensive counter-network actions
- border actions and limited conflicts
- public exposure
- Evolution III emergency preparation
- revealed-war fracture and exploitation

Do not reduce them to generic political-power exchanges. Use the mapped resource palette, including equipment, manpower, XP, fuel, trains, convoys, factory burden, unit placement, stability, diplomatic credibility, intelligence capacity, access, and time.

## Mission quality

- Use named states or named regions for border, depot, port, rail, and protection objectives.
- Auto-complete goal missions when the player has done the work.
- Use 90 to 180 day duration bands unless a true emergency justifies less.
- Give important missions full success, partial success, and failure.
- Record outcome memory so later pact behavior adapts.
- Do not create passive stockpile-check missions.
- Enforce active mission caps and selected-target presentation.

## Evidence and suspect rules

Suspect confidence must use bands and multiple evidence classes. Repeated clues from one class cannot by themselves produce a complete public case.

Country-targeted actions must show:

- current confidence band
- visible basis for suspicion
- risk of acting on weak proof
- blocked requirements

Repeated false accusation without new Evidence damages credibility, worsens relations, and can increase pact recruitment. Innocent suspects must remain mechanically meaningful.

## AI equivalence

AI targets must use the same action families without requiring human GUI clicks. Implement route-aware selection based on target government, Evidence, Preparedness, current wars, resources, geography, and recent operation type.

AI must not:

- target dead or invalid countries
- accuse without minimum confidence
- start suicidal border action
- spend critical equipment while losing an existential war
- repeat the same investigation or protection project without reason
- use a human-only selected-target state as a blocker

## Lifecycle and cleanup

Close or transform the category when:

- the pact collapses
- the target ceases to exist
- reveal occurs
- the target war ends
- a suspect becomes invalid
- a selected target leaves the pool
- a mission's named region is no longer meaningful

Clear event targets, flags, selected IDs, temporary modifiers, active missions, and obsolete decisions. Preserve only history and achievement state that still matters.

## Presentation and assets

Use the asset register for category icons, decision icons, meter frames, suspect cards, status icons, and the single Evolution III animation. The animated warning must use a real horizontal frame sheet with a static fallback. Do not animate every control.

Write final localisation from the spec direction. Costs should be icon-first and blocked requirements should be red. Long requirements belong in custom tooltips rather than raw trigger output.

## Audit and completion proof

After implementation, run the decision and mission auditor against:

- category lifecycle
- costs and dynamic scaling
- full, partial, and failure outcomes
- AI validity
- selected-target cleanup
- border-conflict safety
- false-accusation consequences
- duplicate mission risk
- active mission cap
- exploit loops
- localisation and icon coverage

Return a route and decision coverage table. Report every omitted, merged, renamed, simplified, or fallback action.
