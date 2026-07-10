# Event 011 Secret Alliance

## Part 5: AI, presentation, system connections, balance, and acceptance

## AI strategy

The pact needs route-specific AI behavior. Generic willingness weights would make the system either passive or suicidal.

### Founder AI

Founder AI evaluates its motive, the target's power, distance, current wars, faction commitments, stability, equipment, and expected sponsor support.

A fearful founder prefers intelligence, guarantees, and defensive preparation. A grievance founder prefers border pressure and punitive operations. An ideological founder prefers propaganda and regime pressure. An opportunist delays costly commitments until victory looks likely.

Founder AI should almost never start open war in the calm-world baseline. It can create the hostile-war reveal when a normal strategic conflict makes war rational, when a border incident escalates, or when late readiness and doctrine support the action.

### Recruit AI

Recruit AI compares the pact's credibility with the cost of joining.

It prefers acceptance when the target is strong, nearby, aggressive, ideologically hostile, or threatening its claims. It prefers refusal when the target is friendly, distant, weak, or already protected by a strong faction relationship.

A candidate can leak the invitation when it has good relations with the target, distrusts the sponsor, or believes the pact will lose.

### Major sponsor AI

A major sponsor joins only when it has a strategic reason. It should not enter because the evolution unlocked a slot.

The sponsor considers rivalry, access, target expansion, faction commitments, global fronts, naval reach, industrial balance, and whether minor members provide useful geography.

A sponsor should avoid joining when it is already losing a major war, cannot reach the target, or would abandon a stronger strategic obligation. High chaos and desperation can relax these limits without removing them.

### Operation AI

Operation selection reacts to target vulnerabilities.

- weak counterintelligence favors penetration
- exposed industry favors sabotage
- diplomatic isolation favors recruitment and public pressure
- a long border favors military preparation
- high player Evidence favors false clues and network cleanup
- high player Preparedness favors diplomacy, recruitment, and indirect pressure over another failed attack

AI should avoid repeating the same operation family until the player has seen nothing else.

### Reveal AI

The pact chooses public reveal when readiness and cohesion support it, when exposure is becoming dangerous, or when an external war makes secrecy impossible.

A defensive pact can delay war after reveal. A punitive coalition pushes the offensive countdown. A fractured pact seeks a public justification that may keep doubtful members inside.

### War AI

Coalition AI should coordinate fronts around access and capability. A naval member should not be forced into a useless land plan. A distant member can provide air, naval, expeditionary, equipment, or strategic pressure.

The faction leader prioritizes the target. Members still defend their own territory and avoid abandoning active existential fronts.

Low coalition resolve reduces offensive willingness and increases separate negotiation behavior. High resolve increases coordinated planning.

## Target ideology variants

The core mechanics stay consistent. Player-facing reaction direction and some decision costs can vary by government.

| Target government | Response flavor | Favored tools | Typical risk |
| --- | --- | --- | --- |
| Democratic | legislative scrutiny, public evidence, allied consultation | dossiers, legal investigation, defensive consultation | slow action and public credibility loss |
| Fascist | security police, coercive interrogation, rapid military pressure | raids, border action, counter-propaganda | overreach recruits neutral states |
| Communist | party security, cell analysis, ideological counter-subversion | network penetration, controlled information, cadre protection | purges and false accusations damage stability |
| Non-aligned | court, cabinet, military, or diplomatic intelligence | envoys, guarantees, staff protection, selective mobilization | elite rivalry and inconsistent policy |

These are tone and weight variants. They should not create four unrelated decision systems.

## Regional variation

Geography should change operation selection.

- landlocked targets face rail, border, and overland courier pressure
- maritime targets face ports, convoys, naval access, and coastal infiltration
- island targets require naval and air reach before a strong war plan is credible
- colonial or dispersed targets face pressure on routes, subjects, and distant garrisons
- very large targets encourage a wider coalition and regional division of responsibilities

The pact should not select an island-only minor with no access as a core military founder unless it has a meaningful naval, intelligence, or sponsor role.

## Connections with other Chaos Redux events

These are optional integration hooks. Event 011 must work without them.

### Tensions Rising, Event 008

Active diplomatic panic can improve recruitment and make coordinated complaints easier. Secret Alliance should not duplicate Event 008's world-tension role.

### Intel Leaked, Event 052

A leak involving a pact member can sharply increase Evidence. A leak involving the target can raise pact readiness. The exact hook should be added only when Event 052 has a stable implementation.

### Counterintelligence, Event 147

A global or country counterintelligence improvement can raise Preparedness or reduce operation success. Event 011 should read the shared effect rather than copy it.

### Secret Society Influence, Event 150

A shadowy domestic network can increase false clues, make official compromise more likely, or create a target-side vulnerability. This must remain an optional hook until Event 150 has a defined mechanic.

### World threat framework

The revealed pact is a hostile coalition, but it is not automatically an existential world threat. It should set the shared world-threat state only if the implementation later defines a threshold such as two majors, a near-global member count, and an offensive war of sufficient scope.

## Player-facing text direction

### Entry and early reports

Use concrete anomalies and consequences. Show missing people, repeated methods, unusual foreign money, altered schedules, damaged equipment, and similar incidents appearing in distant places.

Do not name a pact, alliance, coalition, member count, future war, or secret variable.

Avoid staged contrast between frightened witnesses and official denial. Write the observed pattern directly.

### Evolution I

Show that methods, timings, and routes are repeating. The player should suspect coordination without receiving a formal explanation.

### Evolution II

Text can refer to organized foreign interference and credible coordination. It should still distinguish confirmed facts from suspicions.

Decision descriptions must explain visible action, cost, risk, and broad result. They must not reveal hidden success rolls or future members.

### Evolution III and reveal

Public text can name the pact and its members. It should explain the immediate military and diplomatic situation without turning into an effects list.

### Options

Early options can be dismissive, cautious, privately alarmed, or dryly sarcastic. Evolution II options should represent investigation doctrine, protection, diplomacy, and limited force. Reveal options should be serious, strategic, and route-specific.

Cultural allusions require research before final wording. No working label in this package should be pasted into localisation.

### Event Details and spreadsheet direction

Before reveal, describe recurring foreign contacts and unexplained interference around the target. After reveal, describe the public anti-target coalition and its path to war.

Do not list modifiers, Evidence gains, Preparedness effects, member caps, or decision rewards.

## Asset direction

The event needs a coordinated visual family based on intersecting routes, closed circles, broken seals, marked dossiers, linked hands, courier cases, and inward-pointing military symbols.

The visual family should avoid readable generated text, generic map-table scenes, modern spy imagery, and cinematic color grading.

Required families include:

- report event images for early meetings, courier interception, sabotage, assassination aftermath, border caches, and captured planning material
- one reveal news image
- one generated reveal super-event image
- decision category and decision icons
- a small number of staged idea icons
- a faction emblem or coalition seal
- suspect-card and confidence-state UI elements
- one Evolution III warning animation with a static fallback
- achievement icons and required variants

No country flags or leader portraits are required because existing countries retain their identity.

## Achievement direction

The achievement set should reward prevention, investigation accuracy, coalition fracture, survival, and difficult scenario play. It should not reward the event merely firing.

The detailed matrix defines six achievements:

- break the pact before reveal without starting a war
- identify most members without a false accusation
- turn a member and use it to disrupt the opening war
- cause at least half the coalition to enter reveal in a compromised state
- survive the Maximum triggerable scenario under strict conditions
- defeat a two-major coalition while keeping the target capital and independence

Final titles and descriptions are implementation-localisation work.

## Balance principles

### Scale with the target

Coalition size, sponsor interest, operation intensity, and readiness should react to target strength, aggression, geography, and diplomacy.

A small peaceful country should face a slower, narrower conspiracy. A dominant expansionist country can attract more members and a stronger sponsor.

### Give the player time to learn

The baseline should use low-impact incidents and spacing. Evolution II provides active tools before Evolution III makes open war likely.

### Make counterplay carry forward

Evidence and Preparedness must affect reveal and war. Turning a member, protecting a rail corridor, or feeding false plans should change the opening conflict.

### Preserve risk

Investigation can alert the pact. Public accusations can be wrong. Border action can cause war. Protection costs real resources and opportunity.

### Avoid unavoidable collapse

The pact can be strong, but the player must have credible ways to fracture, delay, expose, deter, or prepare against it.

### Avoid reward dust

Important actions should change membership, evidence quality, preparedness, operation access, reveal timing, or war readiness. Tiny modifiers should support these outcomes rather than replace them.

## Anti-exploit rules

- suspects cannot be farmed for repeated Evidence
- the same member cannot be turned more than once
- withdrawal settlements require motive compatibility and real concessions
- public disclosure has a one-time major resolution effect
- border raids use cooldowns, costs, and escalation risk
- preemptive war cannot be made consequence-free through one cheap decision
- scenario launch cannot create duplicate faction membership or duplicate war calls
- invalid and dead members are cleaned before every major operation and reveal
- membership cannot be used to force a human country without consent
- equipment transfers and wartime bonuses cannot repeat through save or event refresh loops

## Acceptance criteria

The event design is satisfied only when implementation includes:

- three valid minor founders in the normal opening
- a hidden non-faction pact state before reveal
- dynamic recruitment of additional countries
- member motives and meaningful acceptance or refusal behavior
- slow and subtle calm-world operations
- Evolution I minor expansion
- Evolution II major participation, aggressive operations, and player counterplay
- Evolution III public faction formation, direct war options, and high war probability
- active-event and pre-fire entry paths for every evolution
- immediate reveal and war entry when an active member enters hostile war with the target
- a real dynamic Anti-[target] faction at reveal
- a reveal super-event with complete research and asset wiring
- Evidence and Preparedness that carry into reveal and war
- false clues and meaningful wrong-accusation consequences
- a compact suspect and response UI with spoiler-safe information
- AI behavior for founders, recruits, sponsors, operations, reveal, and war
- safe handling of faction membership, subjects, civil wars, dead countries, and human countries
- a direct triggerable coalition-war scenario with type and intensity controls
- complete assets, localisation, event logs, docs, achievements, and spreadsheet alignment
- task-specific validation of selection, recruitment, reveal, call-to-war, scenario launch, and cleanup

## Anti-bloat boundary

The event should not create new country tags, bespoke focus trees, formables, leader packages, or a second custom diplomacy game. Those additions would pull attention away from the hidden-coalition loop.

A future implementation can add country-specific flavor events when a famous rivalry makes them worthwhile. The core system should remain tag-agnostic and reusable without requiring country packages.
