# Event 059 design decisions

## Accepted decisions

| Question | Decision | Reason |
| --- | --- | --- |
| What does the event change? | AI strategic choices and priorities | The supplied brief explicitly excludes direct combat bonuses |
| How persistent is it? | Permanent global state after one Fire-Once activation | The event is a campaign-wide doctrine shift |
| How does player control work? | Current human control suspends all Event 059 AI layers | Fire-time ownership would fail takeover, hotjoin, and AI handback cases |
| How are later countries covered? | Declarative global plan if supported, otherwise bounded registration on creation and release | A recurring global scan conflicts with project performance rules |
| Does the event apply hidden modifiers to human countries? | No | The player must remain fully in control and free of direct stat effects |
| Does baseline create arbitrary wars? | No | Baseline improves current wars and existing objectives. Predatory war entry belongs to Evolution II |
| How is encirclement treated? | Intended outcome through concentration and exploitation | Exact direct encirclement control cannot be assumed without verified engine support |
| What is Evolution I for? | Persistence, reinforcement, resupply, and follow-up | This separates operational pressure from diplomatic predation |
| What is Evolution II for? | Claims, war goals, intervention, and valid opportunity wars | This creates a clear strategic escalation at 400 Chaos |
| What is Evolution III for? | Scale, theater ambition, and accepted risk | It can deepen active lower channels without recreating disabled ones |
| Can a higher evolution substitute for a disabled lower stage? | No | Shared evolution controls must remain meaningful |
| How do high-Chaos first firings work? | Pre-fire catch-up activates each enabled eligible layer with one report and ordered logs | A late Fire-Once event should reflect current world state without popup spam |
| Do evolution activations add Chaos? | No | Evolution state changes capability, not a concrete consequence |
| Does initial activation add Chaos? | Yes, one bounded 15 to 25 gain | A simultaneous worldwide strategic shift is a concrete destabilising manifestation |
| Do later wars receive Event 059 Chaos premiums? | No | Shared war, death, annexation, faction, and tension systems already measure those outcomes |
| Which cluster owns the event? | Diplomacy | The accepted cluster update explicitly assigns Event 059 to Diplomacy with High severity and merges the old Diplomatic Panic identity into that cluster |
| How severe is cluster membership? | High | The global permanent effect materially changes the campaign |
| What member role and chance apply? | Use the authoritative Diplomacy defaults | The accepted cluster update fixes membership and severity but directs new members to current role, chance, and minimum-tier defaults instead of a new event-specific subsystem |
| Does it need a custom GUI? | No | The player has no event-owned controls or values to manage |
| Does it need decisions or missions? | No | Player responses already exist through ordinary military, diplomatic, production, and intelligence play |
| Does it need a focus tree or country package? | No | The event changes global AI behavior and creates no polity or player route |
| Does it need a super-event? | No | A normal global report fits a Minor Fire-Once event and avoids presentation inflation |
| Does it need animation or 3D assets? | No | Motion and 3D do not clarify the hidden AI mechanic |
| What visible art is needed? | One report image plus one achievement icon family | This covers the real player-facing surfaces without asset bloat |
| Is an achievement justified? | Yes, one very hard defensive challenge | It creates a meaningful player objective tied to Total Offensive and cannot unlock by passive participation |

## Rejected expansions

### Global aggression meter

Rejected because it would expose internal AI weighting as a player-managed value. The event has no action that would let the player control such a meter.

### Country decision category

Rejected because the event does not grant players a special response system. Fortification, diplomacy, intelligence, production, alliance choices, and military planning already provide the response.

### Defensive emergency bonuses for players

Rejected because they would weaken the event's challenge and violate the rule that the event changes AI behavior rather than country statistics.

### Automatic random war creation at baseline

Rejected because it would duplicate Random War and erase the intended distinction between baseline, Predatory Powers, and Total Offensive.

### Direct attack or breakthrough modifiers

Rejected because they would conceal difficulty in stat bonuses and could persist on human-controlled countries.

### National focus priority override

Rejected because it could erase country route identity. Event 059 should influence action inside valid content, not force one political or expansion route.

### Separate art for every evolution

Rejected because the evolutions develop one doctrine and can share one report image. Extra images would add production cost without improving recognition.

## Unresolved implementation choices

These choices require inspection of current installed HOI4 and the actual mod repository:

- exact generic AI strategy plan database and supported trigger fields
- whether native plan reevaluation alone covers player takeover and handback
- whether new countries inherit a generic plan automatically
- exact available front, production, air, naval, war-target, and intervention strategy types
- exact owner-plan precedence behavior
- safe legacy Event 059 migration identifiers
- authoritative Diplomacy member role, chance, and minimum tier, with complete-pool probability evidence for any weighted value
- final achievement strength-comparison fields

The implementation agent must resolve these from authoritative local references and tool evidence. The spec intentionally avoids inventing unsupported script keys.
