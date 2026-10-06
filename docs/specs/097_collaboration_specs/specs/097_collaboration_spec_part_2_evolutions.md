# Event 097 Collaboration: Part 2, Evolutions

## Evolution structure

Event 097 has four evolutions on one mutation track. Each sits at its own Chaos tier and each can be enabled or disabled independently through Event Details.

| Evolution | Working name | Chaos requirement | What changes |
| --- | --- | --- | --- |
| I | Deep Networks | 200 | Layers grow larger, existing networks deepen once, and occupiers hold defeated countries more easily after capitulation. |
| II | Administrations in Waiting | 400 | A captured core state receives a prepared local administration the moment it changes hands. |
| III | The Fifth Column | 600 | Networks turn openly against a host that is losing a war, and frontline districts can change sides without a battle. |
| IV | Collaboration Governments | 800 | A defeated host can be replaced by a prepared government tied to the power that built the network. |

The track has no ordinary baseline stages. Every firing is the same baseline incident at a size chosen by the current evolution state. The evolutions are true mutations: each one adds a new rule that ordinary firings do not have.

Evolution activation never changes Chaos. A Chaos change appears only when an evolution causes a concrete world consequence, as mapped in `matrices/097_collaboration_chaos_impact_map.md`.

## Shared pacing and logging

Each evolution becomes eligible when Chaos reaches its requirement and the evolution is enabled. It then activates through the shared MTTH-based evolution pacing used by other Chaos Redux events, not instantly at the threshold. Each evolution records one entry in the shared evolution log with no actor, because the event is global. The shared evolution context variables are set before the enable check, and a disabled evolution never sets a recorded flag that later content reads.

### Timing model

Every timed surface in Event 097 uses the same model: the evolution clocks here, and the Open Gates and Turned Regime timers in Part 3.

1. When a countdown starts, the MTTH entry is evaluated once with the current world state.
2. The result is clamped between the surface's minimum and maximum.
3. One check is scheduled at that delay, spread evenly by up to a third of the delay in either direction, so countdowns started in the same situation do not land on the same day.
4. The countdown is not recomputed when the world changes during it.
5. When the check runs, it tests the surface's conditions again. If they still hold, the surface activates. If they no longer hold, nothing happens and the countdown can start again at the next opportunity.

War activity in every MTTH factor is measured as the number of participants at war with another participant, which the event keeps current through its own war hooks, because the engine offers no count of wars.

An evolution countdown can start whenever the Chaos value changes, when Event 097 fires, and when a war between participants begins, provided the evolution is eligible and no countdown for it is already running. These are event-driven moments. No periodic pulse is involved.

For an evolution, the conditions at the check are that the evolution is still enabled, still inactive, and that Chaos still meets its requirement. Chaos falling below the requirement or the evolution being disabled during a countdown therefore cancels that activation without leaving any flag behind.

Each evolution has two MTTH entries, one for the pre-fire path before Event 097 has applied layers and one for the active path afterward. The pre-fire entry is slower, with an ordinary anchor of one and a half times the active base. A pre-fire countdown that is running when the first firing completes continues unchanged.

| Evolution | Active base | Minimum | Maximum |
| --- | --- | --- | --- |
| I | 90 days | 30 days | 240 days |
| II | 90 days | 30 days | 240 days |
| III | 90 days | 30 days | 240 days |
| IV | 120 days | 45 days | 300 days |

Factor magnitudes are tuning anchors that live with the MTTH entries and must pass the timing scenarios in the probability matrix. The minimum clamp guarantees that stacked fast factors never activate an evolution in under 30 days.

### Independence and entry paths

Evolutions do not require one another. Evolution II can activate while Evolution I is disabled. Each later evolution reads the state of earlier ones only as an accelerating or strengthening factor, never as a hard prerequisite, so disabling one evolution never strands another.

Evolution content acts only on networks that Event 097 has actually created. Behaviors check that the host has a non-zero incoming network depth from Event 097 before reading the native collaboration value. Collaboration from vanilla intelligence operations alone never triggers an Event 097 behavior.

Each evolution has two entry paths where the design supports both.

- Active-event entry: Event 097 has already applied layers and the evolution activates. The world changes immediately as described for that evolution.
- Pre-fire evolved opening: the evolution activates before Event 097 has ever applied layers. The first firing then opens in the evolved form.

Pre-fire activation creates no extra Chaos. Its first firing generates Chaos through the same concrete outcomes as any other firing.

When Chaos later falls below a requirement, an active evolution stays active. Evolutions in Chaos Redux record a world that has changed, and these networks do not unlearn what they know.

## Evolution I: Deep Networks

### Promise

Networks are no longer a few sympathizers in a café. They reach the middle of the state: local government, ministry departments, the police, industrial management, party organizations, and the military bureaucracy. Defeated countries become noticeably easier to occupy and hold.

### Pacing

- Chaos requirement: 200
- MTTH anchor: about 90 days once eligible
- Faster when Event 097 has already fired once, and faster again after two firings
- Faster when at least six participants are at war with another participant
- The pre-fire entry applies before the first firing

The ordinary expected range on the active path is roughly 60 to 120 days.

### Changes

1. Every later firing uses the Deep Networks layer of 25 points instead of 15.
2. Prepared cadres: when a participant host capitulates, every enemy that occupies its core states and holds at least a Widespread network inside it, which means 40 percent collaboration or more, receives a lasting occupation bonus in those states. Part 3 defines the bands.
3. Opening reports and evolution reports use the deep sector vocabulary: ministries, prefectures, police, plant management, party offices, and military staffs.

### Active-event entry

When Deep Networks activates after Event 097 has applied layers at least once, the existing networks deepen once. Every ordered pair of current participants receives a deepening tranche of 10 points, with no stance multipliers. The tranche uses the same batched application pass as a firing.

The tranche is a concrete change to every network in the world and creates its own small Chaos increase. A short report reaches human players. It describes recruitment reaching higher offices, without numbers.

### Pre-fire evolved opening

When Deep Networks activates before any firing, there is no tranche. The first firing applies 25 points and uses an opening report variant in which the networks already sit inside ministries and police headquarters. The player learns that this is not the first contact between foreign services and their officials, only the first time it has become visible everywhere.

### Disabled

Layers stay at 15 points, no tranche happens, and capitulations receive no prepared-cadre bonus.

### Evolution log title direction

A short title about recruitment reaching the offices that matter. It should not use the word warning or describe the change as a threat.

## Evolution II: Administrations in Waiting

### Promise

Networks prepare complete local administrations before conquest. When a state falls, the prefect, the police chief, and the district council are already waiting to serve the new controller. Compliance becomes much stronger where networks run deep.

### Pacing

- Chaos requirement: 400
- MTTH anchor: about 90 days once eligible
- Faster when Deep Networks is active
- Faster when a participant has capitulated since Event 097 first fired, or since the countdown started on the pre-fire path
- Slower when no war between participants is active

### Changes

1. Seated administrations: when a participant captures a core state of a participant enemy, and the capturing country holds at least 15 percent collaboration inside the owner, the state receives an immediate compliance gain and a lowered resistance target while the capturer holds it. Part 3 defines the formula, guards, and recapture behavior.
2. Open ministries: when such a capture takes the owner's capital and the capturer holds at least 40 percent collaboration inside the owner, every core state of that owner the capturer already holds receives an additional one-time compliance gain, and the owner loses war support.
3. Collaborators unmasked: when the owner retakes a seated state, it learns who served the enemy and receives a one-time choice per war and enemy between purging the exposed network and granting amnesty. Part 4 defines the choice.

### Active-event entry

When Administrations in Waiting activates after Event 097 has applied layers, every core state currently occupied by a participant enemy of its participant owner is checked once. Qualifying states receive their seated administration immediately. This is a single bounded pass at activation.

### Pre-fire evolved opening

When the evolution is already active before the first firing, the same single pass runs immediately after the first application pass completes. The first opening report gains a line of direction about administrations that seem to know in advance which flag they will serve under.

### Disabled

Captured states start at the ordinary compliance of zero. Collaboration still converts to compliance at capitulation through the engine.

### Evolution log title direction

A title about offices that were ready before the soldiers arrived.

## Evolution III: The Fifth Column

### Promise

When a host begins losing a war, the networks inside it stop waiting. Officials stop cooperating with the war effort, local authorities prepare for the victor, and political and military resistance to capitulation weakens. The effect is strongest in countries that are already close to defeat.

### Pacing

- Chaos requirement: 600
- MTTH anchor: about 90 days once eligible
- Faster when Administrations in Waiting is active
- Faster when any participant at war has passed 40 percent surrender progress
- Slower when no war between participants is active

### Changes

1. The Fifth Column condition: a participant host at war, past 20 percent surrender progress, with at least one participant enemy that holds part of its territory and at least 15 percent collaboration inside it, gains the Fifth Column national spirit. The spirit has three bands, Wavering, Defecting, and Collapsing, selected by surrender progress and scaled by the strongest enemy network. Part 3 defines the bands and values.
2. Open Gates: at the Defecting and Collapsing bands, a frontline state can hand itself to the enemy without a battle. This is the evolution's uncommon incident. Part 3 defines the selection, guards, and caps.
3. Stronger seats: while the Fifth Column is active in a host, seated administrations in that host receive a larger compliance gain.
4. Weaker exile: a host that reaches the Collapsing band in a war lowers the installation threshold for Evolution IV against it in the same war.

### Evaluation without a world scan

The Fifth Column is evaluated only when something that changes it happens: a state owned or controlled by a participant changes controller, a war between participants starts or ends, or a host capitulates. Each such event schedules one delayed evaluation for the affected host. If an evaluation is already pending, no second one is scheduled. There is no daily or weekly loop over all countries.

### Active-event entry

When the evolution activates, every participant currently at war with another participant is evaluated once.

### Pre-fire evolved opening

When the evolution is active before the first firing, the same single evaluation runs after the first application pass completes.

### Disabled

Hosts receive no Fifth Column spirit, no Open Gates incidents happen, and installation thresholds ignore the Collapsing reduction.

### Evolution log title direction

A title about the column inside the walls. The phrase fifth column itself may appear in the title because it is a common noun in English. A quotation attributed to a specific historical person needs the super-event research workflow and is not part of this log title.

## Evolution IV: Collaboration Governments

### Promise

The networks can now form governments. When a host is defeated by an enemy with a strong network inside it, the victor can install a collaboration government quickly and cheaply instead of holding the country by direct occupation. These governments stay tied to the power that installed them. Because every country holds networks everywhere, several powers can build competing systems of collaboration governments across the world.

### Pacing

- Chaos requirement: 800
- MTTH anchor: about 120 days once eligible
- Faster when Administrations in Waiting and The Fifth Column are both active
- Faster when a participant capitulated during the last year
- Slower when no war between participants is active

### Changes

1. Prepared governments at capitulation: when a participant host capitulates, the strongest qualifying enemy network receives an event offering to install a collaboration government over the host cores it occupies. Part 3 defines the qualification threshold, the choice of installer, and the installation.
2. Seat the Prepared Government decision: an occupier that did not receive the capitulation offer, declined it, or later deepened its network can install a government through a targeted decision once compliance and collaboration meet a reduced threshold. Part 4 defines the decision.
3. Every ideology can install: the event does not care about ideology. Democracies can install governments through this route, framed as provisional administrations in text. If the engine refuses a democratic overlord on this route, the implementation stops and reports the blocker instead of excluding democracies quietly.
4. Installed administrations: every government created through this route receives the Installed Administration spirit and its lifecycle, local auxiliary forces, and a registry row that other events can read. Part 3 defines the package.
5. Turned regimes: a government installed by one power can defect to a rival that holds a stronger network inside its country while the original installer is losing a war. This is the evolution's rare variant. Part 3 defines it.
6. Competing orders: when at least two different powers each hold at least two governments installed through this route at the same time, the world reaches the competing-orders milestone. It triggers the event's super-event and its largest single Chaos increase.

### Active-event entry

When the evolution activates, participants that have already capitulated and are still occupied by a qualifying enemy become valid targets for the Seat the Prepared Government decision. No offer event fires for those earlier capitulations, because the offer belongs to the capitulation moment itself.

### Pre-fire evolved opening

Evolution IV needs capitulations to act on. A pre-fire activation changes nothing visible until the first capitulation of a host with Event 097 networks inside it. The first opening report gains a line of direction about exile communities abroad already discussing who would run their country under foreign protection.

### Disabled

No offer event, no decision, no installed-administration package, no turned regimes, and no competing-orders milestone. The vanilla collaboration-government route remains whatever vanilla provides.

### Evolution log title direction

A title about governments that were formed before the countries they would govern had fallen.

## Rare variants

Rare variants belong to the evolutions, because the baseline event is deliberately uniform. The evolutions own two of them, both defined in Part 3.

| Variant | Evolution | Conditions in short | What it adds |
| --- | --- | --- | --- |
| Open Gates | III | Host at the Defecting or Collapsing band, the enemy with the strongest network controlling an adjacent state, an undefended non-capital core state | A state changes controller without a battle and receives a seated administration. |
| Turned Regime | IV | An installed government whose installer is losing a war against a rival holding a much stronger network inside the government's country | The government changes masters during the war. |

Both variants are uncommon by design. Their timing, caps, and AI behavior belong to the probability audit.

## Evolution interaction summary

| Active evolutions | Resulting behavior |
| --- | --- |
| I | Bigger layers, one deepening tranche, prepared cadres at capitulation |
| II | Seated administrations on capture, open ministries on capital capture |
| I and II | Larger networks make seats both more common and larger |
| III | Fifth Column bands on losing hosts, Open Gates incidents |
| II and III | Seats in a host with an active Fifth Column grow by half, and Open Gates states are seated at once |
| IV | Prepared governments at capitulation and by decision, installed-administration package, turned regimes, competing orders |
| III and IV | A Collapsing host faces a lower installation threshold, and a losing installer can lose its regimes to a rival |
| All four | The complete loop: deep networks, ready administrations, internal collapse, and a replacement government |
