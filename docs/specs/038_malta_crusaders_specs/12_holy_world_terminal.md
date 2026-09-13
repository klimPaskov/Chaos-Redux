# Public world-end route: The Holy World

## Route status

The Holy World is Event 38's public terminal route. It appears in Event Details as one independently controlled world-end row owned by Event 38.

It does not require the hidden Teutonic Order. It can absorb aligned survivors from that route, but the ordinary Papal campaign must reach The Holy World on its own.

## Public branch control

The Event Details row needs:

- stable scenario registry identity
- owning event ID 38
- public title
- public premise and terminal-state details
- persistent default-enabled toggle
- current availability status
- selection and detail behavior

Disabling The Holy World skips this branch during automatic readiness and activation. It does not disable Event 38, the Holy See, Kingdom of God, hidden routes, or manual scenarios.

## Preparation eligibility

The preparation lane becomes available when all required checks pass:

- global Chaos is at least 800
- Event 38 has fired or an accepted Event 38 successor exists
- the Pope is the supreme ruler of Malta, the Holy See, or the Kingdom of God
- no incompatible terminal state is active
- The Holy World branch is enabled
- the Papal actor has a valid capital, government, and alliance system
- at least one durable crusader territory or principality exists

Preparation does not set `world_end`.

## Papal supremacy

The Pope must hold supreme political and spiritual authority over the crusader actor. A ceremonial Pope under a dominant secular council does not qualify.

Accepted proofs can include:

- Holy See identity under the Pope
- Kingdom of God under the Pope
- an Event 38 Papal government flag with valid leader ownership
- a constitutional arrangement that grants the Pope final war and foreign policy authority

The implementation must handle the current real or modded Pope without character duplication. A Papal institutional actor is acceptable only when the current repository system already supports one coherently.

## Preparation campaign

The Pope builds a world religious bloc through:

- believer alliances
- leagues
- protectorates
- crusader subjects
- aligned governments
- foreign religious movements
- military orders
- aid and equipment networks
- pilgrimage and sacred-site diplomacy
- coercive submission where the route permits it

The world does not divide into two final sides during preparation. Countries can support, oppose, remain undecided, or bargain.

## Believer relationship before terminal war

A pre-terminal believer can be:

- a formal alliance member
- a Papal subject
- a crusader principality
- a government that recognizes Papal supremacy
- a country with a binding military-order compact
- a foreign movement with political power but no state control

These statuses have different obligations. Preparation should not flatten every supporter into one subject type.

## Continental requirement

### Design goal

The Pope must prove the ability to govern a continental system before proclaiming a final world crusade. Tiny island occupations, one-day conquests, and irrelevant offshore holdings cannot satisfy the proof.

### Continent contracts

Implementation creates one exact Event 38 state collection for each eligible continent. Each collection is built from the current local map and reviewed through the map workflow.

A continent contract contains:

- qualifying mainland states
- strategically significant islands that belong to the continent's normal political space
- explicitly excluded remote islands and map anomalies
- excluded wastelands or unusable states
- total qualifying state count
- ownership and subject-control proof rules

The exact set is fixed for a campaign generation. Map changes between mod versions require regeneration and review.

### Complete control

The requirement is exact over the curated contract. Every qualifying state must be controlled through one of these accepted forms:

- direct ownership by the Papal actor
- ownership by an approved Papal subject

Temporary military occupation does not count. An ally that has not accepted Papal supremacy does not count.

### Approved Papal subject

A subject counts only when:

- it is in the Papal alliance
- its charter or subject type grants Papal war leadership and foreign-policy control
- it has remained in that relationship for the stabilization period
- it is not in active rebellion
- it owns and controls the state
- it is not merely an occupied collaboration government created for one day

A nominal faction member does not count.

### Stabilization period

The full continent must remain valid for a recommended 90 days before readiness is recorded. Losing a qualifying state pauses or resets the proof according to the final mission design.

The public mission names the selected continent and shows qualitative progress with a concise state-group tooltip. It does not print a developer ledger of every state ID.

### Selecting a continent

The Papal actor can pursue one continent at a time for the public proof. AI chooses from current control, subject network, distance, enemy strength, supply, and existing wars.

The implementation may allow any complete continent supported by the local map. It should not hardcode Europe as the only valid route.

### Anti-exploit checks

- transfer to a one-day subject does not count
- ownership without control does not count
- an occupied enemy puppet does not count
- tiny offshore territory does not substitute for the mainland
- state ownership changes are revalidated before readiness
- annexing and immediately releasing a state does not bypass the stabilization period
- a map update cannot silently drop missing states and make the proof easier

## Holy World Ready state

Once one continent contract passes:

- set the event-owned ready flag
- record the selected continent
- retain the proof as long as the Papal system remains valid
- open final preparation focuses and decisions
- show a public status in Event Details and the Holy World category

If Chaos is below 1000, the route waits. It cannot set the shared terminal state early.

If the continent later becomes invalid before activation, readiness is suspended or revoked. The exact policy should be public and consistent. A recommended design is a 30-day grace period before revocation so one transient battle does not erase months of preparation.

## Final activation

Activation requires:

- Holy World Ready
- Chaos at least 1000
- The Holy World branch enabled
- no existing `world_end`
- valid Pope and Papal actor
- valid selected continent proof or grace state
- no scenario setup conflict

The activation transaction:

1. freezes the Papal actor and readiness proof
2. revalidates every terminal gate
3. sets `world_end`
4. sets the Event 38 Holy World scenario flag
5. sets the matching super-event visibility
6. sets the unique audio ID and calls the settings-aware sound helper
7. stops normal automatic event firing under the shared contract
8. transforms the Papal alliance into the terminal believer structure
9. queues final submission choices
10. stages regional war pulses
11. opens terminal decisions and logistics
12. clears preparation-only targets and bypass facts

A partial terminal activation is unacceptable. If the transaction fails before the shared world-end state is committed, it must cleanly reject.

## Final world division

### Human countries

Every human country receives a direct choice unless already controlling the Holy World actor or already bound by an accepted irreversible Papal subject agreement.

The choice explains visible consequences:

- submit to Papal war leadership
- resist and join a counter-coalition
- attempt a narrow neutrality only when the terminal design allows it

No human country should be silently assigned by AI weight.

### AI countries

AI chooses from:

- current religion and ideology where the game's political model can express them
- prior Papal alignment
- existing believer status
- relations
- fear and military balance
- existing wars
- territorial exposure
- faction membership
- government autonomy
- condemnation of Malta or the Pope
- local religious movements
- hostility to Papal supremacy

The AI result should create a real world war. Even a strong Holy World needs major nonbeliever resistance.

### Believers

Believer governments:

- accept Papal war leadership
- join the Holy World alliance or approved subject structure
- contribute troops, equipment, convoys, industry, or bases
- retain varying local administration
- receive shared defence and terminal support

Believers are not automatically annexed.

### Nonbelievers

Nonbelievers:

- reject Papal authority
- join one or more coordinated resistance blocs where possible
- receive emergency mobilization and coalition support
- share intelligence or logistics according to their coalition
- become terminal conquest targets

The system can maintain more than one counter-bloc when forcing every hostile country into one faction would break existing wars or diplomacy.

## Staged regional war

The terminal war uses rapid regional pulses rather than one world effect.

Suggested order:

1. borders and immediate continental holdouts
2. Mediterranean and neighbouring regions
3. adjacent continents
4. major overseas powers
5. remaining islands and remote governments

Each pulse:

- reads a frozen valid target array
- skips countries already at war
- handles faction leaders before members where needed
- creates war or submission outcomes
- records skipped invalid targets
- clears its working array

Pulses should begin immediately and complete quickly enough to feel like one terminal proclamation.

## Terminal military

The Holy World receives deliberately extreme terminal support:

- recruitable population
- organization
- recovery
- attack and defence
- breakthrough
- planning
- logistics
- reinforcement
- naval invasion capacity
- convoy protection
- construction support
- rail, port, supply hub, fort, and military industry projects

Support must be centralised in terminal ideas and systems with clear cleanup. It should not scatter permanent magic numbers across dozens of files.

## Terminal unit families

Available families include:

- Supreme Papal Knights
- Blessed Heavy Cavalry
- Holy Siege Hosts
- mechanized crusader formations
- Papal armored divisions
- elite multinational believer armies
- ordinary infantry and armour from believer states

The medieval identity remains visible through formations, names, counters, models, and order command. The army still uses late-game industrial equipment.

## Terminal economy and logistics

### Believer contributions

Believers can contribute:

- equipment
- manpower or expeditionary units
- convoys and escorts
- factories through national burdens
- ports and bases
- fuel and resources
- air and naval support

Contributions must respect country survival floors and avoid deleting an ally's entire stockpile.

### Papal construction authority

The Holy World can rapidly build or repair:

- supply hubs
- railways
- ports
- airbases
- forts
- anti-air
- military factories
- dockyards

Projects should target active fronts and selected regions. They cannot be free unlimited repeatable factory buttons.

## Conquest outcomes

Conquered countries can be:

- annexed
- reorganized as Papal subjects
- converted into crusader administrations
- restored under believer governments
- assigned to existing principalities

The outcome depends on route, local administration, strategic value, Authority, and Papal policy.

Terminal conquest does not automatically give actual cores everywhere. The terminal state can use extreme compliance, subject, and administration tools without erasing all population and resistance logic.

## Holy capitals

- Rome is the primary political and holy capital.
- Jerusalem is the secondary sacred and military center.
- Malta remains the original fortress and major naval center.

Losing Rome or Jerusalem creates terminal emergency missions. It does not instantly delete the world-end state.

## Terminal victory and defeat

### Holy World victory

A victory condition should require the defeat or submission of every major organized nonbeliever bloc and control of defined world strategic regions. It should not require chasing one tiny inaccessible exile forever.

Victory can lead to:

- continued sandbox under the Holy World
- final victory presentation
- global administration decisions
- a stable terminal state with normal event firing still frozen

### Holy World defeat

Defeat can occur through:

- fall of the Papal actor and all valid successors
- loss of Rome, Jerusalem, and Malta combined with coalition collapse
- destruction of the believer alliance
- an accepted anti-Papal settlement

Defeat aftermath can include:

- dissolution of Papal supremacy
- restored governments
- refugee return and reconstruction
- war-crime and atrocity consequences where relevant
- surviving military orders
- a defeat super-event if the terminal war was genuinely global and costly

The campaign does not need to end at a static game-over screen.

## Interaction with Teutonic Order and Atlantis

### Teutonic Order

Surviving aligned Teutonic members can enter the believer bloc when:

- they accept Papal supremacy
- the alliance has not broken through Atlantis
- their current route is compatible

The Holy World does not require them.

### Atlantis

If Atlantis activates first, it becomes a hostile separate route and cannot be automatically assigned as a believer. Atlantis and Holy World can fight when both reach their valid campaign states, but only one shared world-end state can be active. The implementation must define which route owns terminal activation when both are ready.

Recommended rule:

- Atlantis betrayal can occur before any terminal state
- once Holy World activates, new Atlantis activation is blocked
- existing Atlantis remains a major nonbeliever enemy during Holy World setup if the route has already formed

## Event-owned Chaos effects

Terminal activation does not add arbitrary Chaos after the 1000 gate. World Collapse already exists. Preparatory concrete outcomes can change Chaos only through the approved one-shot milestones and shared sources.

## Performance

The terminal runtime uses:

- registered country arrays
- regional queues
- sparse active projects
- actor-local decision processing
- no new global daily or weekly scan
- bounded submission receipts
- idempotent war creation
- cleanup of processed targets

## AI and probability evidence

Required named scenarios include:

- weak Pope with one continent
- strong Pope with one continent
- Europe controlled through subjects
- Africa controlled directly
- several human countries
- existing global factions
- active Atlantis
- active unrelated world-end blocker
- Low, Medium, High, and Maximum manual scenario setup

AI side choice, regional target order, settlement, contribution, and Papal project weights all need probability inspection and comparison.

## Public Event Details direction

Event Details should explain:

- a Papal crusader state can build a worldwide believer bloc at extreme Chaos
- complete control of one continent is required before final readiness
- the final proclamation divides governments between submission and resistance
- the terminal war replaces normal automatic events

It should not list exact AI formulas, hidden state arrays, Atlantis interactions, or implementation variables.

## Acceptance scenarios

1. preparation appears at 799 and 800 Chaos
2. branch toggle disabled and enabled
3. Pope is ceremonial only
4. Rome controlled but not owned
5. continent controlled directly
6. continent controlled through valid subjects
7. one subject enters rebellion
8. one tiny excluded island remains hostile
9. one qualifying state is occupied but not owned
10. full proof held for 89 and 90 days
11. readiness achieved at 900 Chaos
12. readiness lost before 1000
13. readiness and 1000 occur on same day
14. another world-end route activates first
15. multiple human countries choose sides
16. wars already exist across several regions
17. believer coalition too strong at Maximum scenario intensity
18. Papal actor capitulates during regional pulses
19. save and reload during proof, readiness, activation, and terminal war
