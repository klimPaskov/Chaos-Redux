# Murder Mystery Specification Part 8: Decisions and Missions

## Presentation choice

Event 39 uses ordinary decision categories with strong category pictures and concise scripted status text. A separate scripted GUI is not accepted for the current design because the investigation and movement can remain clear with phased decisions, named missions, two public values, and dynamic tooltips.

A custom window may be reconsidered only if implementation proves that ordinary decisions cannot present target selection or state clearly. Such a change would require a new accepted plan and the event UI worker. It is not part of this source spec.

## Category set

### Murder Mystery Investigation

Owned by the original host. It begins after the opening murder and transforms through national cult, international network, and counterinsurgency phases.

Public header:

- Case Progress stage and progress bar or compact value
- Network Reach stage and compact value
- current investigation phase
- current protected office group
- next public threshold or blocked requirement
- one short warning when an active mission or imminent incident matters

### Foreign Cell Investigation

Owned by each secondary affected country. It shows Local Case Progress, shared Network Reach stage, local cell stage, current protected office group, and current evidence-sharing state.

### Brotherhood Operations

Owned by the central Assassin State. It shows Network Reach, Brotherhood Cohesion, current foreign-cell support target, current subject or faction pressure, and one active campaign objective.

### Cell Administration

Owned by foreign Assassin derivatives. It shows local survival, Cohesion relation, central support, parent-war objective, and a compact set of local decisions.

### World Without Leaders

Visible only after Evolution V and terminal preparation. It manages terminal activation, campaign sectors, synchronized uprisings, conquered-government settlement, and victory progress. It should not show every ordinary government as a permanent decision row.

## Visible action budget

Each phase normally shows three to five primary decisions and no more than six. Each country normally has one to three active Event 39 missions. Target-selection decisions replace the visible target family. They do not expose every country, cell, office group, or subject at once.

Obsolete actions disappear. A decision category that retains completed opening actions, unavailable cell routes, defeated targets, or old phase missions has failed the clutter gate.

## Government investigation decisions

### Opening decisions

#### Establish the case command

Chooses the rule-bound, integrated security, or emergency repression response profile. The choice affects starting public state and future costs. It is a one-time opening decision or event option.

#### Secure the government quarter

Commits security forces, equipment, and transport to the capital and key institutions. It raises protection and succession stability. The action may start a mission to hold named states or keep supply connected.

#### Preserve the first evidence

Commits civilian capacity, investigators, and secure transport. It protects evidence integrity and opens the first investigative method.

#### Choose a protection priority

Selects one office group. The visible selected target uses a compact selector. Changing priority has a cooldown and real cost.

### Baseline and cult decisions

#### Commit an operative or case team

With La Résistance, commit a suitable operative for a fixed period. Without the DLC, commit an institutional case team through civilian and political capacity. The commitment raises progress and unlocks operations while creating exposure.

#### Audit communications

Consumes intelligence capacity, radio or encryption support, and time. It can reveal routes, safe houses, or compromised offices. Repeated use raises adaptation.

#### Trace movement logistics

Targets equipment, money, vehicles, rail, port, or border movement. It requires named route evidence and may start a map objective.

#### Protect witnesses

Commits manpower, support equipment, and transport. It improves witness safety and can start a transfer mission.

#### Raid an identified cell

Available only after public evidence threshold. The player chooses a quiet raid, coordinated raid, or fast strike. Costs, evidence result, and risk differ.

#### Replace a compromised office

Temporarily removes an infiltration penalty and resets part of the protection system. It costs institutional capacity and may lower Case Progress if done without proof.

#### Prepare the final operation

Locks one capture plan and starts its final mission. It is unavailable below the public threshold or when required evidence is missing.

## Foreign investigation decisions

### Join the evidence exchange

Makes the country an active cooperation member. It grants inherited knowledge and exposes the country to shared compromise risks.

### Request the original case file

Uses relations, intelligence access, and transport or liaison capacity. It raises Local Case Progress when the original host has usable evidence.

### Harden a target group

Applies temporary protection to one office group. Strong agencies pay lower institutional cost. Repeating the same pattern increases movement adaptation.

### Interdict a known route

Targets a named border, port, rail, or sea corridor. It requires evidence and starts an objective.

### Dismantle the local cell

Final local operation. Success grants immunity. Partial success reduces stage. Failure can move the cell or accelerate revolt readiness.

### Support a threatened partner

Sends equipment, investigators, operatives, or transport to another affected country. Aid requires route access and can be intercepted.

## Assassin State decisions

### Reconcile a command dispute

Raises Cohesion through a route-specific action. Centralized command imposes a decision, decentralized cells hold a council, and the pragmatic route uses a temporary administrative settlement. Each has costs and ideological consequences.

### Select a foreign cell target

Uses a compact target selector over eligible active cells. Human players see one selected target's actions. AI evaluates all valid targets through its own path.

### Supply the selected cell

Sends equipment, operatives, transport, or funds. The action raises local maturity and revolt readiness while costing real resources and exposure.

### Order a high-value operation

Attempts a protected assassination, archive raid, prison break, or intelligence theft. It requires a mature cell and a specific target profile. The outcome affects Network Reach, local investigation, evidence, and international reaction.

### Prepare a territorial revolt

Starts a timed preparation mission in one eligible country. It requires a validated state cluster, high cell maturity, route access, and derivative tag capacity. The target government receives counterplay.

### Dispatch a Shadow Company

Temporarily commits an elite unit or equipment package to a foreign operation. The unit is unavailable or weakened at home during the mission.

### Reinforce a derivative

Transfers equipment, manpower cadres, intelligence, or supply to a foreign Assassin subject. The cost scales with distance and route access.

### Discipline an unauthorized cell

Reduces rogue murder risk or foreign backlash. It can lower Network Reach or Cohesion depending on route and local response.

## Derivative decisions

Foreign Assassin derivatives need a compact survival package:

- secure the revolt capital
- raise local Assassin Cadres
- seize a depot or rail route
- request central support
- integrate local cells into government
- choose obedience, autonomy, or local campaign priority
- manage captured officials
- negotiate or reject a local settlement

A derivative should not receive a copy of every central operation.

## World of Anarchy decisions

### Complete the terminal command settlement

Required before activation. It resolves who can authorize worldwide operations under the chosen political route.

### Activate World of Anarchy

Deliberate terminal action. It checks Chaos, evolution, branch toggle, movement viability, Cohesion, war readiness, and incompatible world-end state. It opens confirmation and triggers the super-event only after setup succeeds.

### Select a campaign sector

The player chooses a bounded region or strategic group, not every country at once. The sector creates military, cell, and intelligence objectives.

### Synchronize uprisings

Starts a bounded wave among mature eligible cells in the selected sector. It respects derivative caps and map safety.

### Break the command spine

Targets a government already under severe Event 39 pressure. It can disrupt leadership and command through safe character and office handling. It cannot delete arbitrary protected characters.

### Establish a successor administration

After conquest, chooses a subject administration, decentralized cell territory, staged integration, or route-specific settlement. It uses the conquest transaction from Part 10.

### Reconstitute the campaign council

Repairs Cohesion after major expansion or leader loss. It creates a period of vulnerability and resource commitment.

## Mission families

### Investigation missions

- protect a witness transfer between named states
- hold a government quarter during a public event
- secure an evidence train or convoy
- guard a named port or border route
- place supplied divisions in a threatened region
- keep the capital connected to supply
- complete an agency operation before a cell moves
- capture an identified safe-house chain
- preserve a target through an expected attack window

### Counterinsurgency missions

- prevent a stage 4 cell from completing revolt preparation
- secure selected depots, rail hubs, and urban states
- dismantle local recruitment before a deadline
- protect local government leadership during a regional crisis
- prevent an Assassin support shipment from reaching the cell
- hold the parent capital and revolt border during mobilization

### Assassin State missions

- survive the opening war period
- control or contest named supply routes
- capture a host archive or command center
- keep a foreign cell supplied for a defined period
- raise local maturity without exposing the parent route
- prepare one validated revolt cluster
- prevent a subject from leaving during low Cohesion
- complete a synchronized operation before foreign investigations adapt

### Terminal missions

- dismantle one selected regional command network
- force a government capitulation before the campaign mandate expires
- hold a sector's capitals or strategic nodes
- protect the central command while authority is temporarily delegated
- prevent a coalition from destroying a foreign derivative
- reduce the number of eligible ordinary independent governments in a sector

## Mission durations

Ordinary investigation missions should normally last 90 to 180 days. Emergency protection windows can be shorter when an attack date is already known. Revolt preparation and counterinsurgency missions should normally last 120 to 240 days. Terminal sector missions can last 180 to 365 days according to scale.

The same duration should not be copied across every mission. Distance, agency strength, war state, supply, cell maturity, route access, and country size should change the time.

## Cost model

No decision or GUI-equivalent action may use more than four spendable cost types.

### Government costs

- civilian factory commitment
- command power, kept below the project maximum and used only for real command actions
- army, navy, or air experience when a service develops protection doctrine
- support equipment, infantry equipment, trucks, trains, convoys, or fuel
- manpower commitment
- operative commitment or agency capacity
- stability or war support when the action creates public strain
- political power only for genuinely political or legal action

### Assassin costs

- Assassin equipment and ordinary equipment
- manpower cadres
- trucks, trains, convoys, fuel, and support equipment
- civilian or military factory burden
- intelligence capacity or operative commitment
- Cohesion loss or subject autonomy as a consequence
- Network Reach exposure as a risk
- unavailable unit commitment for dispatched formations

Cost strings must use matching texticons. Nonconsumed requirements are shown separately.

## Success, partial success, and failure

Every mission has distinct success and failure effects. Major missions should support partial success when the player achieved part of the objective.

Examples:

- a witness arrives but records are lost
- a cell is disrupted but its leader escapes
- a revolt is prevented but the government loses legitimacy
- an Assassin supply route succeeds but exposes the parent state
- a subject survives but gains autonomy
- a terminal sector falls but the central campaign council loses Cohesion

Failure should create new pressure, not merely remove a reward.

## Target management

Large target families use the reusable selected-target pattern. Human players select one country, cell, subject, office group, or sector and see only relevant actions. A hide or close action clears the selected presentation state. AI uses all valid targets without the human selector.

Cleanup clears target flags, stored IDs, active decisions, invalid event targets, and selected state when a target dies, annexes, changes package, leaves the movement, or becomes protected.

## Dynamic localisation

Category text and tooltips should communicate:

- current public value stages
- current protected role
- current selected target
- main causes of progress or pressure
- next threshold
- exact named state or route requirements
- blocked cost or missing capability
- mission deadline and visible consequence

They should not expose hidden character registry rows, exact random weights, future surprise branches, or internal implementation identifiers.

## AI behavior

AI decision logic must use route, cost, capability, target validity, war state, supply, unit availability, agency strength, stability, current mission load, and expected consequence.

AI should not:

- start more missions than it can support
- repeatedly use an adapted method
- expose an unprotected leader to a bait operation without desperation
- support a foreign revolt while its capital is collapsing
- spend all custom equipment on covert actions while front-line units cannot reinforce
- create derivatives beyond the cap
- activate World of Anarchy without terminal readiness

Every complex or balance-sensitive weight needs the probability audit cycle in Part 13.

## Cleanup and persistence

Decision categories, active missions, selected targets, commitments, costs, flags, and visible values must survive save and reload. They must clear after capture, local dismantling, country defeat, movement inheritance, terminal resolution, or invalid target state.

A completed or obsolete decision cannot return because an old flag remained on an annexed country or recycled dynamic tag.

## Acceptance standard

The decision system is accepted only when each phase shows a compact action set, every action changes play, costs use no more than four spendable types, missions require real objectives, target selection remains current, AI uses equivalent paths, no stale decisions survive lifecycle changes, and the normal decision interface communicates the mechanic without a custom GUI.
