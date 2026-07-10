# Event 011 Secret Alliance

## Part 4: Reveal, faction formation, coalition war, and triggerable scenario

## Reveal paths

The pact can be revealed through several routes. Every route must converge on one clean faction-formation and cleanup contract.

### Hostile war reveal

When any active pact member enters a normal hostile war against the target, the pact is revealed immediately.

The triggering country may have declared the war, joined an existing war, answered a guarantee, or been pulled into a hostile side through another valid mechanism. A limited border conflict does not count until it becomes a normal war.

The reveal effect forms the faction, assigns a leader, invites every valid active member, and brings every valid member into the target war immediately.

This is the hard user rule. It cannot wait for a later event, a separate invitation cycle, or an AI decision.

### Pact-controlled reveal

At Evolution III, a cohesive and ready pact can reveal itself publicly before war. The faction appears, the members join it, and a short offensive countdown begins.

This route gives the player a final deterrence, fracture, or preemption window. It also lets the coalition present a public justification instead of appearing only through an accidental war.

### Player-forced reveal

High Evidence, a successful public dossier, a turned member, or a captured planning conference can force the pact into the open.

A forced reveal should weaken cohesion, expose compromised members, and reduce the coalition's opening coordination. It can still produce war.

### Fractured reveal

Low cohesion can produce a partial reveal. A sponsor and committed members form the faction, while doubtful members withdraw, delay, or become exposed sympathizers.

Only current valid active members count as pact members for the automatic war contract. Countries removed through prior validity cleanup are not silently treated as members.

## Faction identity

The public faction name follows the dynamic pattern **Anti-[target country adjective] Pact**. The final localisation must handle countries whose adjective reads poorly and must have a name-based alternative.

The faction is an actual Hearts of Iron IV faction. It should not be simulated only through opinion modifiers or parallel wars.

The faction leader is chosen in this order:

1. the active major sponsor designated as leader
2. the strongest active major member
3. the strongest founder by military and industrial capacity
4. the hostile-war trigger country when no stronger valid founder exists

A second major sponsor does not automatically replace the first leader. Leadership conflict becomes a coalition weakness.

## Faction goals and rules

The faction exists to contain, defeat, or coerce the target. Its exact public aim depends on the hidden doctrine and the circumstances of reveal.

The faction should have:

- a shared target and war plan
- member call-to-arms rules
- a visible coalition resolve estimate after reveal
- shared emergency decisions or AI effects for coordination
- member confidence and withdrawal behavior
- consequences for failed offensives and conflicting war aims
- a clear end condition after the target war

The faction should not become a permanent generic alliance by default. After the target war ends, it evaluates whether to dissolve, remain as a regional bloc, or split through a leadership dispute. This outcome depends on doctrine, victory, cohesion, sponsor survival, and member relations.

## Conversion of hidden values

At reveal:

- Pact cohesion becomes visible coalition resolve
- Pact readiness determines opening coordination and mobilization bonuses
- Evidence determines how much the player knows about plans and member weaknesses
- Preparedness determines the target's opening defense and the number of pact disadvantages carried into war
- turned members and compromised networks convert into delayed calls, weaker planning, exposed depots, or refusal events

The conversion should make pre-war decisions matter. Preparedness cannot be a cosmetic score that disappears when war begins.

## Member call behavior

The reveal effect should process all valid active members immediately.

A member can have one of four reveal states based on pre-war counterplay:

| State | Reveal behavior |
| --- | --- |
| Committed | joins faction and war immediately |
| Delayed | joins faction immediately, enters war after a short disruption event unless the hard hostile-war reveal requires immediate entry |
| Compromised | joins, but receives weaker planning, logistics, or intelligence state |
| Turned or withdrawn | is removed from active membership before reveal and does not count against the all-members rule |

For the hostile-war reveal, every remaining active member enters war immediately. Pre-war disruption is expressed through penalties and missing preparation rather than a delayed call.

## Opening war behavior

A strong pact opening should feel coordinated without creating units from nowhere.

Possible opening advantages include:

- temporary planning and coordination
- prepared supply routes
- better intelligence against the target
- limited equipment transfers from the sponsor
- synchronized offensive AI priorities
- reduced call-to-arms delay
- defensive guarantees on exposed fronts

Possible player-earned counters include:

- protected supply and industry
- prebuilt border entrenchment
- false coalition plans
- delayed sponsor logistics
- compromised member communication
- exposed depots
- neutral opinion support

The design should avoid flat global combat bonuses as the only expression of preparation. Operations and countermeasures should affect logistics, planning, intelligence, access, and timing.

## Direct player choices after reveal

### Fight the coalition

The default route continues the war or prepares for the offensive countdown. Preparedness and known member weaknesses shape the opening.

### Seek a fracture

The player can target doubtful members with separate peace, withdrawal, guarantees, or exposure of conflicting promises. This route uses coalition resolve and member motives.

### Challenge the leader

Evidence against the sponsor or leader can create a leadership crisis. A second major may contest control. The faction remains dangerous while coordination falls.

### Accept a limited settlement

A containment or grievance coalition may offer terms before war or during a failed offensive. The settlement must reflect member motives and should not force an arbitrary surrender of the whole country.

### Escalate preemption

When the faction has revealed before war, the player can strike first. The legitimacy cost depends on Evidence and the coalition's public actions.

## Coalition resolve after reveal

Coalition resolve is a visible banded value. It changes through:

- battlefield success and failure
- member casualties
- capture of member capitals
- conflicting war aims
- sponsor aid
- target concessions
- public exposure of lies
- separate negotiations
- the survival or defeat of the coalition leader
- whether the target appears stronger or weaker than expected

Low resolve can trigger withdrawals, faction leadership contests, refusal of offensives, and a negotiated end. High resolve improves shared planning and makes separate talks harder.

## War outcomes

### Target victory

The pact is defeated when the coalition war ends in the target's favor, the faction collapses, or every committed member leaves the war.

The aftermath should acknowledge the revealed network, remove event-owned ideas and decisions, close suspect state, and preserve only justified diplomatic memories.

A major coalition that caused a long global war can receive a stronger aftermath report. This minor event does not require a second super-event by default.

### Pact victory

The pact achieves its purpose when the target capitulates or accepts a settlement that satisfies the coalition's stated objective.

The faction then evaluates whether it dissolves or survives. A spoils compact is likely to fracture over peace terms. A containment front is likely to dissolve after guarantees or restrictions. A major-led regime-pressure coalition may remain as a bloc.

The event should not override the normal peace conference with a large bespoke partition system unless a later accepted implementation plan expands that scope.

### Pre-war fracture

If the player removes enough members or collapses cohesion before public reveal, the pact dissolves.

The target receives a short aftermath window with options to expose the surviving evidence, keep the matter secret, repair relations with innocent suspects, or retain a limited counterintelligence benefit.

### Objective overtaken

If the target is annexed, absorbed, or otherwise ceases to be a valid independent actor before reveal, the pact ends. Member governments may claim that events solved the problem, but the system does not retarget.

## Super-event trigger

The reveal super-event fires when the faction becomes public, whether through hostile war, pact-controlled reveal, or player-forced reveal.

The super-event role is **public revelation and faction formation**.

It should communicate that previously separate incidents were connected, that governments have accepted common obligations, and that the target now faces an organized bloc.

The description direction varies by reveal route:

- hostile-war reveal emphasizes synchronized entry into an existing war
- pact-controlled reveal emphasizes public declaration and completed preparations
- player-forced reveal emphasizes exposed documents, hurried denials, and a coalition compelled to act in daylight

The final title, button wording, and cultural remark require dedicated research. The main quote recommendation is documented in the separate super-event research note.

## Triggerable scenario

### Working scenario identity

The manual scenario working label is **Coalition Unmasked**. This is an internal label and not final localisation.

The scenario creates the instant anti-target coalition and war requested in the source idea. It is separate from the normal random-event timer, chaos thresholds, baseline stages, and evolution pacing.

### Launch behavior

The selected player country becomes the target. The scenario builds a safe candidate pool, chooses members according to the selected type and intensity, forms the public faction, fires the reveal super-event, and starts war immediately.

The launch bypasses ordinary chaos, evolution, date, prior-event, and event-history gates. It blocks only impossible launches, insufficient valid countries, human-country consent issues, and active terminal-state conflicts.

The launch uses the same member validity, faction formation, war entry, AI strategy, super-event, and cleanup helpers as the normal chain.

### Scenario type options

| Type | Selection direction | Play identity |
| --- | --- | --- |
| Regional ring | nearby countries and states with strategic access to the target | encirclement and border pressure |
| Ideological front | countries with compatible hostility to the target government | propaganda, regime pressure, aligned war aims |
| Great-power sponsor | one eligible major leads a wider minor coalition | stronger logistics, intelligence, and command |
| Unlikely coalition | mixed ideologies united by fear or grievance | high material reach, lower cohesion |
| Random coalition | safe weighted selection from all valid candidates | unpredictable challenge |

### Intensity scaling

| Intensity | Default composition | Opening condition |
| --- | --- | --- |
| Low | 3 minor countries | limited readiness, no preloaded severe sabotage |
| Medium | 4 to 6 countries, major participation uncommon | moderate readiness and one prepared operation effect |
| High | 1 major plus 5 to 7 other members when valid | high readiness, coordinated logistics, stronger opening plan |
| Maximum | up to 2 majors plus 8 to 12 total members, capped by safe candidates | maximum safe readiness, multiple fronts, strong coalition AI, no impossible member forcing |

Intensity should also scale equipment transfers, planning, intelligence, and coalition resolve. It should not scale only through flat combat modifiers.

### Scenario confirmation and controls

The scenario uses the existing data-driven registry, sortable list, detail panel, four-stop intensity slider, type cycle control, and launch confirmation.

Confirmation reads the currently selected type and intensity at launch time. The scenario does not hardcode them on the first click.

### Scenario failure handling

If the selected composition cannot be built, the launch is blocked with a clear reason. Maximum intensity can use every safe valid candidate when fewer than the target band exist, but it must state the achieved composition. It cannot substitute invalid countries.
