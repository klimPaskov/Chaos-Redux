# Event 097 Collaboration: Part 3, Occupation, Capitulation, and Governments

This part defines how Event 097 networks change the moments when wars are decided: the capture of a state, the slide toward defeat, the capitulation itself, and the government that follows it.

All pair reads in this part happen in occupation contexts, where the capturing or occupying country controls territory of the host. The design relies on the native collaboration value only in those contexts, because the engine documents the value as tied to occupied cores. Each behavior also checks that Event 097 has added networks inside the host, so collaboration from vanilla operations alone never starts an Event 097 behavior.

The wiki wording ties the read to the host's cores that the reader occupies. Event 097 follows the same rule by design: seats, Open Gates, and prepared cadres consider only states that are cores of the host, because the prepared collaborators are the host's own people in its own lands. A captured colony or other non-core state receives no Event 097 behavior. The implementation must still verify how the native read behaves when the reader occupies some host cores and the captured state is one of them, and record the result.

## Network bands

Several behaviors read the native collaboration of one occupier inside one host and place it in a band.

| Band | Collaboration of the occupier inside the host | Meaning in play |
| --- | --- | --- |
| Thin | below 15 | No Event 097 behavior |
| Ordinary | 15 to 39 | One baseline layer or more is in place |
| Strong | 40 to 69 | Several layers, or Deep Networks layers |
| Total | 70 and above | The occupier's network runs through the whole host administration |

The band edges are tuning anchors in one constant group and are shared by every behavior in this part.

## Baseline: capitulation through the engine

Without any evolution, Event 097 changes wars only through the engine rules for collaboration.

- A host with foreign networks inside it capitulates earlier to every enemy that holds them.
- When the host capitulates, every occupier converts its collaboration into starting compliance in the host territory it holds.
- When several enemies can receive the capitulation, the engine favors the one with more collaboration. Because the base layer is uniform, stance choices decide this in practice. A country that chose Cultivate in earlier firings is more likely to be the one its enemies surrender to.

The event adds nothing here. The player should feel the change through faster wars and quieter occupations, and the decision categories and reports in later evolutions explain why.

## Evolution I: prepared cadres at capitulation

When a participant host capitulates and Deep Networks is active, every participant enemy that occupies host states and holds at least a Strong network inside the host receives a lasting occupation bonus in each host core state it controls.

| Occupier band | Compliance growth in those states | Resistance target in those states | Duration |
| --- | --- | --- | --- |
| Strong | +25 percent | -10 | 365 days |
| Total | +50 percent | -20 | 365 days |

The bonus is a state-level modifier tied to the occupier. It is removed early when the occupier loses control of the state. It applies once per capitulation per occupier and host. It stacks with the engine's own compliance at capitulation because the two represent different things: the engine turns collaborators into starting compliance, and the prepared cadres keep that compliance growing.

The host's government, if it survives in exile, receives a short report from its own point of view: the people who kept the provinces running under the enemy were the same people who ran them before.

## Evolution II: seated administrations

### Trigger

A seat is considered when a state changes controller and all of the following are true:

- the new controller and the state's owner are both participants
- the state is a core of the owner
- the new controller is at war with the owner
- Event 097 has added networks inside the owner
- the new controller holds at least an Ordinary network inside the owner
- the state has not been seated for this controller in the last 180 days
- Administrations in Waiting is active and enabled

The previous controller can be the owner or one of the owner's allies. The seat depends on the owner, because the prepared administration belongs to the owner's country.

### Effect

The state receives:

- an immediate compliance gain equal to half the new controller's collaboration inside the owner, capped at 40
- a lowered resistance target for this controller, equal to a quarter of that collaboration and capped at 25, with a removable identifier
- a seat marker recording the controller and the date

While the Fifth Column is active in the owner, the compliance gain grows by half and its cap rises to 50.

An Open Gates state is seated at once when it changes hands.

### Recapture

When the state changes controller again, the seat ends. The resistance-target identifier is removed and the seat marker is cleared. If the owner or one of its allies retakes the state, the owner's government may learn who served the enemy. This creates the Collaborators Unmasked choice, defined in Part 4, at most once per war for each owner and enemy pair.

### Open ministries

When the capture takes the owner's capital state and the new controller holds at least a Strong network inside the owner, the new controller receives an immediate additional compliance gain of 15 in every other owner core state it controls, and the owner loses 10 percent war support. This happens once per war for each owner and controller pair.

### Reports

The new controller receives a short report the first time a seat happens in a given owner during a war. The direction is concrete and visual: officials waiting at the town hall with keys, ledgers, and lists, and police who already know the new routes. The owner receives a report when its capital is seated under Open ministries.

### Cycling guard

A state that changes hands repeatedly can be seated for the same controller at most once in 180 days. Recapture by a different enemy is a new seat for that enemy. The guard prevents farming compliance and Chaos milestones through repeated capture.

## Evolution III: The Fifth Column

### Condition

A participant host has the Fifth Column when all of the following are true:

- the host is at war with at least one participant enemy
- Event 097 has added networks inside the host
- the host's surrender progress is above 20 percent
- at least one participant enemy controls a core state of the host and holds at least an Ordinary network inside it
- The Fifth Column evolution is active and enabled

The strongest enemy network is the highest band among enemies that satisfy the last condition.

### Bands

| Band | Host surrender progress | Character |
| --- | --- | --- |
| Wavering | 20 to 39 percent | Officials delay orders and keep their options open |
| Defecting | 40 to 59 percent | Departments stop cooperating and local authorities contact the enemy |
| Collapsing | 60 percent and above | The state apparatus prepares to serve the victor |

A band drops only when surrender progress falls 5 points below its floor. This prevents the spirit from flickering every time a single state changes hands.

### Effects

The host receives one national spirit, working label Fifth Column, implemented as one dynamic modifier whose values come from the band and from a network factor.

| Strongest enemy network | Network factor |
| --- | --- |
| Ordinary | 0.5 |
| Strong | 1.0 |
| Total | 1.5 |

Values at network factor 1.0:

| Effect | Wavering | Defecting | Collapsing |
| --- | --- | --- | --- |
| Surrender limit | -5 percent | -10 percent | -15 percent |
| War support | -10 percent | -15 percent | -20 percent |
| Stability | none | -10 percent | -15 percent |
| Factory output | none | -10 percent | -20 percent |
| Recruitable population | none | none | -25 percent |
| Enemy compliance growth in our occupied states | +25 percent | +50 percent | +75 percent |
| Resistance target in our occupied states | -10 | -20 | -30 |

These values are tuning anchors kept in one constant group. The modifier names must be verified against the installed modifier documentation. The table expresses the intent: officials stop cooperating with the war effort (factory output and recruitment), political resistance to capitulation weakens (surrender limit, war support, stability), and local authorities prepare for the victor (compliance and resistance in occupied territory).

The spirit's tooltip names the band and the country with the strongest network inside the host. It does not show the network factor or the formula.

### Open Gates

At the Defecting and Collapsing bands, a frontline state can hand itself to the enemy without a battle.

An Open Gates incident is considered for a host on a timer with an ordinary MTTH anchor of about 60 days at Defecting and about 30 days at Collapsing. Responses in Part 4 can slow it. The incident chooses one state that meets all of these conditions:

- a core of the host, owned and controlled by the host
- not the host's capital
- adjacent to a state controlled by the enemy with the strongest network
- without any division of the host or its allies present
- not seated or opened in the last 180 days

If no state qualifies, the incident does nothing and its timer restarts. If several qualify, the state with the lowest victory-point value is preferred, so the incident favors provincial districts over major cities.

The chosen state changes controller to the enemy with the strongest network, without changing ownership, and receives a seated administration if Administrations in Waiting is active. The host receives a report from the point of view of a government that learns one of its districts has simply opened its doors. The enemy receives a report that one of its columns marched in without firing a shot.

Caps: one incident per host every 90 days, and at most three per host per war. The incident needs a state-scope effect that changes control without ownership and a reliable trigger for friendly divisions present in a state. Both must be verified in the installed documentation. If either is missing, the implementation reports a blocker.

### Cleanup

The spirit is removed when the condition fails with hysteresis, when the host makes peace with every participant enemy, when the host capitulates (after Evolution IV processing reads it), or when the host is annexed. Pending evaluation and Open Gates timers end with it.

The host records the highest band it reached in each war. Evolution IV and achievements read that record. It clears when the war ends.

## Evolution IV: prepared governments

### Qualification threshold

The installation threshold is the minimum collaboration an occupier needs inside a host to install a prepared government.

| Situation | Threshold |
| --- | --- |
| Ordinary | 40 |
| The host reached the Collapsing band in this war | 30 |
| The host chartered a government in exile before capitulating (Part 4) | +10 to the threshold |
| The host lies inside a registered external sphere for the occupier (Part 5) | -10 to the threshold |

The threshold never falls below 25 and never rises above 60.

### The capitulation offer

When a participant host capitulates while Collaboration Governments is active, Event 097 looks for one installer among the host's participant enemies.

An enemy qualifies when it controls at least one core state of the host, holds collaboration inside the host at or above the threshold, and there is no living government installed through this route for the host's original tag.

When several enemies qualify, the installer is the one with the highest network band, then the most host core states controlled, then the country that received the capitulation.

The installer receives the Prepared Government event. It has two options:

- Install the prepared government over the host cores the installer occupies.
- Keep direct occupation. The networks stay in place, and the Seat the Prepared Government decision remains available later.

AI weights for this choice belong to Part 6 and the probability matrix.

The capitulation offer can happen once per capitulation of a host.

### Installation

Installation uses the vanilla collaboration-government creation path, with the installer as overlord and the host as the country to initiate, as the precedent and engine route. The implementation must inspect the vanilla route and reuse it instead of writing a parallel country-creation system.

After the vanilla route creates the government, Event 097 adds its own layer:

- a provenance marker that identifies the government as installed through Event 097
- a registry row with the government, the original tag, the installer, the installation date, and the route used (offer, decision, or external sphere)
- the Installed Administration spirit at its first stage
- local auxiliary forces (below)
- the Chaos change from the impact map
- a check for the competing-orders milestone

A democratic installer uses the same route. Text calls the result a provisional administration instead of a collaboration government. If the engine route refuses a democratic overlord, the implementation stops and reports the blocker. It must not quietly exclude democracies.

Repository evidence makes this blocker likely rather than hypothetical. The mod's own copy of the ideology definitions sets `can_create_collaboration_government = no` for the democratic group, gives `can_collaborate = yes` only to communism and fascism, and gives the non-aligned group neither. Whether the scripted creation effect honors these rules could not be confirmed, because vanilla documentation and the HOI4 MCP tools were unavailable. The implementation must establish this before writing the installation helper. If the effect honors the rules, the user chooses between three directions, and the implementation must not pick one alone:

- keep the vanilla route and accept that democratic and non-aligned installers cannot install, which narrows the brief's ideology-blind promise
- change the ideology rules globally, which also changes vanilla intelligence operations for every democracy and non-aligned country
- build the installed government through a puppet release with the collaboration-government autonomy state, if that route proves to ignore the ideology rule

The installation Chaos row in the impact map assumes that no generic puppet Chaos source fires for a scripted collaboration government. The wiki documents the puppet on-action only for peace conferences. If live testing shows that the generic source fires for this route, the event-owned installation amount drops to zero for that installation and only the first-government and milestone rows remain.

### Installed government package

The installed government is a dynamic country created by the vanilla route from the host's identity. Event 097 creates no new tag, no new flag, and no new characters.

| Surface | Design |
| --- | --- |
| Name and flag | Vanilla collaboration-government naming and flag behavior for the original tag and overlord |
| Ruling ideology | The vanilla route's result, which follows the installer |
| Leader | Whatever character the vanilla route assigns. Event 097 does not create or name leaders. Because these are grounded polities, the event must never invent a substitute person or generate a portrait. The implementation must document which character leads in tested cases. |
| Territory | The host cores the installer occupied at installation |
| Subject status | Collaboration-government autonomy under the installer |
| Starting spirit | Installed Administration, Imposed stage |
| Starting forces | Local auxiliaries |
| Focus tree | The original tag's existing tree, unchanged. Event 097 loads no tree. |
| AI | Follows its overlord in war, uses the arming decision through its overlord (Part 4), and never seeks a new overlord except through Turned Regime |

### Local auxiliaries

The installed government receives local auxiliary divisions raised from the police, gendarmerie, and militia that the network prepared. They are ordinary infantry formations with light equipment, suited to garrison and rear-area duty.

- Count: one division for every two states of the new government, at least one and at most six
- Template: a light infantry auxiliary template using ordinary infantry battalions, without artillery or support companies, with a working template name of Auxiliary Police
- Equipment: drawn from the installer's infantry equipment stockpile at installation, as part of the installation cost
- Experience: low, representing police and militia rather than soldiers

These troops do not need a new unit type. They fight as ordinary light infantry and their role is to hold territory so the installer can move its own garrisons elsewhere. Their identity is carried by the template name, the report text, and the fact that they appear only through this route. Reinforcement happens through the installer's Arm the Installed Administration decision in Part 4.

### Installed Administration lifecycle

The installed government carries one Event 097 spirit at a time. It never holds more than one.

| Stage | Entered when | Main effects | Leaves when |
| --- | --- | --- | --- |
| Imposed Administration | Installation | Stability -15 percent, war support -20 percent, faster auxiliary recruitment from local police cadres | 365 days pass without entering Contested, or Contested begins |
| Entrenched Administration | 365 days in Imposed without being Contested | Stability -5 percent, war support -10 percent, consumer goods demand reduced because local elites manage supply | Contested begins |
| Contested Administration | The installer is at war and past 40 percent surrender progress, or a rival participant at war with the installer occupies part of the government's territory and holds at least a Strong network inside the government's country | Stability -25 percent, war support -25 percent, Turned Regime becomes possible | The condition ends, returning to the previous stage |
| Abandoned Administration | The installer capitulates, is annexed, or stops being the government's overlord for any reason other than Turned Regime | Stability -30 percent, political power gain -50 percent, the strongest restoration pressure for Event 095 | The original country is restored, or two years pass, after which the spirit is removed and the government continues as an ordinary country with a former-collaboration marker |

The values are tuning anchors. Every stage must matter in play, because the spirit is the regime's whole political problem.

### Ties to the installer

The government stays bound to its installer. While the spirit is in the Imposed, Entrenched, or Contested stage:

- the government joins its installer's wars through the normal subject rules
- Event 097 never offers it a way to raise its autonomy
- the only way it changes masters is Turned Regime

### Turned Regime

A government installed through this route can defect to a rival during a war. The variant is considered when all of these are true:

- the government is in the Contested stage
- a rival participant is at war with the installer and with the government
- the rival occupies at least one core state of the government and holds at least a Strong network inside the government's country
- the installer is past 40 percent surrender progress, or the Fifth Column is active in the installer at the Defecting band or higher

The installed government is itself a participant, so later firings build networks inside it like any other country. The variant reads the rival's network only where the rival occupies the government's territory, which keeps every pair read in an occupation context. A rival that chose Cultivate in recent firings is the most likely beneficiary, because its networks inside every country are deeper than those of an ordinary power.

The variant has an ordinary MTTH anchor of about 120 days while the conditions hold. When it fires, the government changes its overlord to the rival as a collaboration government, leaves the installer's war, and is placed on the rival's side. The registry row records the new installer and the route Turned Regime. The spirit resets to Imposed.

Each government can turn at most once per war. The engine route for changing a subject's overlord during a war must be verified. If the engine cannot perform the transfer cleanly, the implementation reports a blocker and leaves the variant unimplemented with that reason recorded.

### Competing orders

The competing-orders milestone is reached the first time two or more different powers each hold at least two living governments installed through this route at the same time. It is checked whenever a government is installed, turns, or stops existing. It fires the Event 097 super-event (Part 6) and its largest single Chaos increase once per campaign.

### Registry cleanup

A registry row is retired when its government stops existing, when the government becomes independent, or when the original country is restored over its territory. Retirement keeps a small history record for achievements and Event 095 but removes the row from every live count.

## Collaborators and the returning owner

When a host survives, the networks inside it remain a problem. Part 4 defines the responses available to the host, and Part 5 defines how Event 095 and other events read the state left behind.
