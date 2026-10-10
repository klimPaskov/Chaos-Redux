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
Each hook names its owner and its disposition; only implemented hooks describe current behaviour.

### Current consumers of Event 011 state (implemented)

- Individual crisis targeting counts `secret_alliance_target_country` and `secret_alliance_active_member` toward a country's crisis load, and Event 011 founder, recruit, and sponsor selection applies the same bounded ticket adjustment (`docs/systems/event_system/individual_crisis_targeting.md`).
- Utopia Manifesto excludes hosts carrying `secret_alliance_active_member` or `secret_alliance_founder` (`utopia_manifesto_candidate_has_active_event_package`).
- The shared event pool reports Secret Alliance target, active-run, and postwar-bloc unavailability reasons instead of firing an impossible run (`chaosx_logic_effects.txt`).
- Black Friday (Event 026) applies its sale ratio to Event 011's cached costs, so the shown, required, and paid amounts stay equal.

### Tensions Rising, Event 008

Disposition: accepted by the parent on 2026-10-08 and queued; neither event reads the other in source yet.

Read the existing timed diplomatic context when an [Event 008 shock](../../008_tensions_rising_specs/specs/008_tensions_rising_spec.md) involves the fixed target and a candidate or active member.
The pair flags `tensions_rising_active_<shock>_with_<TAG>` and the border actor flag `tensions_rising_recent_border_war_actor` already exist in `common/scripted_effects/008_tensions_rising_effects.txt`.
The context can make a fear, grievance, or opportunist motive more plausible within the existing recruitment evaluation.
The global pulse alone cannot recruit a country, waive strategic access, create readiness, or apply another world-tension packet.
Recruitment retains its normal capacity, consent, and validity requirements.

Event 008 owns its shock, duration, and pressure accounting.
Event 011 owns its operation dossier and corroboration.
A circulating accusation supplies no Evidence or suspect confidence unless an independent Event 011 operation creates a valid source-aware clue.
The same rumour cannot become a second evidence class merely because two events described it.
Pact absence leaves Event 008 ordinary behaviour intact, and shock expiry removes only that diplomatic context.

An Event 008 non-transfer border conflict does not meet the hostile normal-war reveal rule.
A later normal war between an active member and the fixed target immediately uses the existing all-valid-members reveal contract.
Future checks distinguish panic alone, a genuine separately corroborated operation during panic, an unresolved border clash, and a normal hostile war.
No numeric recruitment or operation-weight claim is accepted without the probability owner's matching scenarios.

### Africa's Scramble response, Event 012

Disposition: accepted by the parent on 2026-10-08.
The reveal half is already satisfied because `secret_alliance_handle_war_relation_added` reveals the pact for any normal hostile war with the fixed target; the Event 012 side of the no-displacement rule is queued and unverified.

When the player-controlled African unifier is also the fixed Event 011 target, use the [Scramble coalition ownership rule](../../012_africa_specs/specs/012_africa_spec_part_5_high_chaos_world_order.md#coalition-war).
Event 012 owns its colonial-interest terms and treaty obligations.
Event 011 owns concealed membership, evidence, reveal, faction identity, and Resolve.
An actual member entering a normal Scramble war against the target still causes immediate pact reveal.
Crisis diplomacy supplies no member list or pact clue.
A surviving public faction is not renamed or displaced to create another copy of the same coalition.
The two systems close their own obligations from the actual war outcome.

### Intel Leaked, Event 052

Disposition: accepted and queued in the Event 052 package, whose catalogue row is still To Be Reworked.
The [Event 052 interaction matrix](../../052_intel_leaked_specs/matrices/052_intel_leaked_cluster_and_interaction_matrix.md) owns one bounded Evidence or Pact Readiness change per leak sequence.
A leak involving a pact member adds Evidence only through Event 011's source-aware clue path, so it cannot repeat a class the dossier already holds.
A leak involving the target can raise Pact Readiness once.
The adapter shape is open question 5 in the package README.

### Counterintelligence, Event 147, and Secret Society Influence, Event 150

Disposition: unresolved; both catalogue rows are Unavailable and neither event has a mechanic to read.
If Event 147 is built, Event 011 should read its shared counterintelligence effect as a Preparedness or operation-success input rather than copy it.
If Event 150 is built, a domestic network could increase false clues or official compromise, and that hook must stay optional.

### World threat framework

Disposition: unresolved; source has no Event 011 world-threat hook.
The original direction let a revealed pact set the shared world-threat state above a future threshold such as two majors, a near-global member count, and an offensive war of sufficient scope.
The [world-threat framework](../../../systems/world_threat_mechanic.md) reserves `world_in_threat` for existential threats and asks other systems to calm ordinary geopolitics while it is set, so open question 1 in the package README proposes the reverse direction: Event 011 reads `world_in_threat` and slows, rather than feeds, the threat.

### Shared systems Event 011 deliberately does not feed

- Chaos Meter and Deaths: the coalition war already counts through war-declaration counting and global casualty aggregation (Part 4), so a bespoke packet would double count.
- Condemnation: its buckets are chemical, biological, nuclear, atrocity, and cover-up; covert operations, false accusations, and preemption use Event 011's own credibility and diplomatic consequences.
- Famine and Migration: no Event 011 rule reads population movement, and coalition-war displacement belongs to Migration's ordinary front and control-change handling; the options listed for Event 011 in the Migration package are open question 3 in the package README.
- Camps and repression, CBRN, and air cleanliness: the pact has no route that builds camps or uses special weapons, and the ideology-flavoured target responses in this part stay tone and weight variants.
- Event clusters: Event 011 belongs to no runtime cluster; the catalogue's one-member Pacts row is open question 2 in the package README.

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

### Make preparation state-capacity limited

Counter-preparation must be a strategic mobilization, not a cheap meter purchase.
Dynamic costs scale from real command power, Army Experience, equipment, transport, fuel, manpower, Political Power, Stability, and War Support commitments, with at most four of them on any one action (Part 3, Cost palette). Countries below the small-industry, field-army, or territorial-capacity thresholds pay additional multiplicative surcharges. Large countries retain their existing upward scale, so neither a microstate nor a major can buy the complete response matrix trivially.

Only one protection project and one emergency commitment may be active at a time. Their long lock periods force the target to choose which preparedness layer matters most. The Mobilized band begins at 85, and reaching it requires several independently funded layers such as protection, emergency mobilization, known plans, allied consultation, or a secured frontier. A one-state minor can still defend itself, but cannot reach full Preparedness through cheap project cycling.

Higher costs must buy consequential results. Evidence and confidence gains remain sufficient to reach the public-case gates through independent corroboration. Defensive projects, false plans, defections, war objectives, and settlements have larger visible consequences. Hostile operations, false accusations, failed public actions, coalition opening bonuses, wartime Resolve facts, and persistent ideas increase in parallel so the event remains dangerous rather than becoming a resource sink with negligible outcomes.

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

The parent's final completion audit records these criteria as implemented at the July 2026 static freeze; the evidence still open after the October release repairs is listed in `docs/plans/011_secret_alliance_plans/agent_decisions_2026-10-05.md`.

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
