# 016 Brilliant Scientist spec, part 1: core event

## Event identity

| Field | Design |
| --- | --- |
| Event ID | `16` |
| Event name | Brilliant Scientist |
| Type | Minor fire-once |
| Status target | Reworked |
| Cluster | None |
| Fixed scientist | Doctor Warren Kruger |
| Main host fantasy | One country receives a scientific advantage so great that national policy starts bending around a single person |
| Main danger fantasy | Every approved breakthrough gives Kruger more ways to survive, bargain, escape, rebel, or build a state of his own |
| Host implementation shape | Additive event chain, character, ideas, decisions, missions, special projects, and scripted GUI |
| Breakaway implementation shape | Full country package, dedicated focus tree, project-derived army, decisions, AI, diplomacy, and endgame routes |

The opening must remain clear and fast. A country discovers Doctor Warren Kruger, recruits him, and receives a dramatic scientific advantage. The first event should not explain the entire future system. It should establish three facts through visible behavior.

1. Kruger understands multiple scientific fields at a level that should not be possible.
2. He is willing to work for the selected country, but he expects unusual freedom.
3. His origin, training, and true objective cannot be verified.

The event becomes deep because the appointment persists. Kruger is a character with a changing portrait, a national role, special-project access, an institutional network, foreign attention, assistants, facilities, project history, and an evolving relationship with the host government.

## The playable promise

The host receives real power immediately. This is not a slow investment route where the player waits years before feeling the event. Accepting Kruger gives the requested `+100%` research speed anchor and access to an exceptional scientist across special-project fields.

That power creates a strategic problem rather than a flat punishment.

- A country at peace may build a public scientific renaissance and spread Kruger's methods through universities.
- A country at war may hide him in military laboratories and demand weapons.
- A weak country may use him to close a technological gap, then discover that its army and industry depend on his network.
- A major power may protect him from foreign intelligence, then find that its security state answers to him.
- A desperate government may approve cloning, robots, monsters, biological weapons, or temporal experiments because ordinary tools are failing.
- A cautious government may limit him early and keep the scientific gains without creating a sovereign rival.

Every route should create a recognizable campaign story. The player should be able to remember what kind of Kruger they created.

## Host selection

### Eligible country pool

The event should select a living, normal, sovereign country that can support both the appointment and a possible later territorial crisis.

Normal eligibility:

- Exists and controls its capital.
- Is not capitulated.
- Is not a subject unless the subject has enough internal autonomy and the implementation can guarantee a meaningful host response.
- Is not an actual nonhuman country.
- Is not another fixed-purpose special chaos country whose mechanics would make a human scientific appointment incoherent.
- Has at least three controlled core states or an approved territorial fallback that leaves both host and breakaway playable.
- Has at least one valid state that can become the primary laboratory site.
- Has not already hosted, expelled, killed, transferred, or lost Kruger through this campaign.
- Is not already in a terminal world-end state.

The selection pool should include AI and human countries. The current implementation's preference for majors or players should be removed. Every eligible country should retain a chance, with dynamic weighting rather than a hard major-only gate.

### Selection weighting

The event can be more interesting in countries that have enough institutional tension to use it. Weighting should consider:

- Existing research slots and research speed.
- Number of universities or equivalent national institutions represented through industry, urban states, and technology.
- Current technological gap relative to nearby rivals or faction leaders.
- War state and immediate military pressure.
- Availability of special-project facilities.
- Political ideology and willingness to centralize science.
- High chaos, which should make obscure and desperate hosts more likely.
- Existing science-related Chaos Redux events.

Do not make a major power overwhelmingly more likely. A small country receiving Kruger should be a viable and memorable outcome. The minimum-state gate exists to make later secession playable, not to reserve the event for great powers.

### Primary laboratory site

The host does not need a physical Kruger state at the first popup, but the system should select and remember a primary laboratory site before the directorate period begins.

Site score should consider:

- Infrastructure.
- Industrial capacity.
- Research facility presence.
- Urbanization or population.
- Distance from hostile borders.
- Air defense and fortification.
- Supply connection.
- Existing special-project facilities.
- Route-specific preference, such as an isolated rural site for secrecy or a major university city for public science.

The site becomes important later. It anchors the custom UI, facility decisions, sabotage, evacuation, foreign raids, project accidents, and any breakaway state. A distributed route can add secondary sites, while a concentrated route increases both research output and rebellion strength at the primary site.

## Opening event

### Information visible to the player

The first event should show:

- Kruger has solved or demonstrated several problems that local experts considered unresolved.
- His equipment or notation does not fit one known institution.
- He requests access to staff, laboratories, archives, and production resources.
- He offers immediate help rather than a vague future promise.
- His biography contains gaps.

The first event should not state that he is an alien. It can establish details that support several explanations, including an extraordinary polymath, a fraud with stolen work, a refugee, a foreign operative, a time traveler, a clone, or something nonhuman.

### Player options

#### Public appointment

Narrative meaning:

Kruger receives an official academic and government role. Universities, newspapers, industrial firms, and foreign embassies can see that the country has gained an unusual scientist.

Immediate direction:

- Apply the full research-speed anchor.
- Recruit the persistent Kruger character.
- Make him available across special-project fields.
- Start with higher fame and lower security secrecy.
- Open public-science and university-network decisions.
- Give foreign countries earlier observation opportunities.
- Reduce the initial grievance created by secrecy or coercion.

Tone direction:

The option should sound confident, curious, or opportunistic. A country-specific variant can use academic prestige, national revival, wartime necessity, or bureaucratic ceremony. It should not announce future rebellion.

#### Secret military appointment

Narrative meaning:

Kruger enters a compartmentalized program controlled by the armed forces or security services. His public identity remains obscure.

Immediate direction:

- Apply the full research-speed anchor.
- Recruit the persistent Kruger character.
- Make him available across special-project fields.
- Start with stronger security and lower public fame.
- Open military-laboratory and compartmentalization decisions.
- Increase initial mandate because the state has granted exceptional access without public oversight.
- Increase dependence faster when military projects are approved.

Tone direction:

The option should read as an urgent administrative decision made under pressure. It can be cold or wary, but not generic secret-file drama.

#### Send him away

Narrative meaning:

The government refuses the appointment, distrusts him, fears the cost, or decides that another country should bear the risk.

Immediate direction:

- Do not destroy or silently remove Kruger.
- Select another valid country through a weighted transfer pool.
- Give the rejecting country a temporary memory flag and a later news or intelligence reaction.
- Let the player identify or influence a recipient only when diplomacy, ideology, faction membership, or intelligence capacity makes that plausible.
- AI never takes this option.

Transfer priority:

1. Ally or faction member that openly welcomes scientific refugees.
2. Ideologically compatible rival seeking research advantage.
3. Neighbor with a technology gap.
4. Major power with active special-project facilities.
5. Any valid country.

The transfer must have loop protection. A country that already rejected Kruger cannot receive him again through the same transfer chain.

Tone direction:

The option can be distrustful, sardonic, cautious, or morally alarmed. It should not tell the player exactly which future disaster is avoided.

## AI appointment rule

AI always accepts Kruger. The AI may choose public or secret appointment based on context.

Public appointment is favored by:

- Democratic politics.
- High stability.
- Strong universities and civilian industry.
- Peace.
- Low immediate espionage threat.
- A desire for industrial, medical, or electronic research.

Secret military appointment is favored by:

- War.
- Authoritarian politics.
- Low stability.
- High intelligence threat.
- A nuclear, rocket, chemical, biological, or weapons program.
- A large technological gap against an enemy.

The AI should never reject Kruger merely because its economy is small. A weak AI can take a lower-capacity management path and delay expensive projects.

## Immediate appointment package

### Research advantage

The accepted appointment grants a deliberate `+100%` research speed anchor. This is the core event promise and must not be reduced to a small modifier during implementation.

The bonus can later be transformed by route:

- Public science spreads some of the benefit across institutions and makes it resilient if Kruger leaves.
- Secret concentration keeps the strongest immediate benefit but creates higher dependence.
- Security incidents may suppress a field temporarily rather than removing the entire event reward.
- Rebellion or defection can remove Kruger's direct bonus and leave an institutional remnant based on prior public investment.
- Successful early retirement can preserve a smaller permanent national-method bonus.

### Persistent character

Kruger must exist as one recognizable character identity.

Required visible roles:

- National advisor or equivalent appointment.
- Special-project scientist.
- Custom UI subject.
- Event actor.
- Possible breakaway leader.
- Possible later route-specific leader identity after cloning, machine integration, temporal duplication, or alien revelation.

The implementation should prefer one character object. If engine restrictions require multiple field-specific scientist entries, they must remain synchronized through shared name, portrait stage, project history, appointment state, injury state, capture state, defection state, and removal state.

### Special-project scientist

Kruger should be available in every special-project field under the same visible name. He should be unusually effective in all fields and absurdly effective in fields connected to approved projects.

General scientist direction:

- Highest practical base skill supported by the engine and current balance conventions.
- Genius and fast-learning behavior.
- Strong prototype and breakthrough support.
- Exceptional cross-specialization access.
- Project-specific traits gained through actual work rather than receiving every trait immediately.
- A unique trait family that scales with portfolio breadth and approved autonomy.

The design goal is not a balanced historical scientist. Kruger is the event's impossible advantage. The counterweight comes from institutional dependence and political consequences.

## Baseline progression

Baseline progression is the ordinary Kruger lifecycle. These stages are not logged evolutions.

### Stage 0: Arrival

The event selects the host and fires the appointment popup.

Player-facing state:

- Kruger is unknown.
- The government decides how to receive him.
- No custom category should appear before acceptance.

### Stage 1: Appointment

The research bonus, character, first portrait, and initial decision category become active.

Player actions:

- Choose a primary laboratory site.
- Assign a public or secret institutional form.
- Give him a first field priority.
- Decide how much staff and production capacity to commit.

### Stage 2: Laboratory consolidation

Kruger begins reorganizing existing research.

Player actions:

- Centralize laboratories or build a distributed network.
- Recruit assistants.
- Choose university, military, industrial, or private patronage.
- Establish security and oversight.

Consequences:

- Scientific Mandate, Institutional Dependence, and Security Exposure begin moving visibly.
- Project capacity becomes available.
- Early flavor events show institutional conflict and unexpected results.

### Stage 3: First impossible result

The first project result exceeds normal scientific explanation. The event can reach this stage through a conventional project that produces an impossible side effect or through direct investment in an impossible family after the required unlock.

Player-facing effect:

- The project portfolio expands.
- Kruger's portrait changes slightly.
- Foreign interest starts growing.
- The government must choose whether to publish, conceal, weaponize, or destroy the result.

### Stage 4: Directorate period

Kruger's network becomes a state within the state. This stage normally aligns with Evolution I or follows soon after it.

Player actions:

- Allocate project capacity.
- Manage universities and industrial contracts.
- Approve or deny project stages.
- Respond to foreign contact.
- Set security policy.
- Decide how much independent authority Kruger receives.

### Stage 5: Demands and confrontation

Kruger requests powers that affect sovereignty.

Possible demands:

- Independent procurement.
- Immunity from ordinary law.
- A protected territory around the main laboratory.
- Direct command over guards, assistants, and project units.
- Foreign negotiation rights.
- Access to prisoners, military units, strategic materials, or forbidden weapons.
- Control over the publication and ownership of all project results.

The player can grant, negotiate, delay, expose, confine, dismiss, arrest, or attempt to kill him. The outcome depends on the entire prior campaign, not one visible percentage roll.

### Stage 6: Resolution state

The baseline system ends in one of several persistent resolutions.

| Resolution | Conditions and meaning | Ongoing play |
| --- | --- | --- |
| Public scientific settlement | Kruger's methods are distributed, oversight remains strong, impossible weaponization is limited | Permanent institutional research benefit, periodic scientific events, low rebellion risk |
| Controlled secret compact | Kruger remains inside a secured program with negotiated limits | Strong specialist benefits, continuing security costs, occasional foreign incidents |
| Unrestricted laboratory state | Government grants near-total autonomy without formal secession | Maximum project output, high dependence, growing sovereignty crisis |
| Peaceful Kruger charter | Host grants territory and legal autonomy before violence | New Kruger State, technology relationship, negotiated border, no initial host war |
| Defection | Foreign extraction or voluntary departure succeeds | Recipient inherits part of the portfolio, former host suffers scientific vacuum and security scandal |
| Successful confinement or death | Host acts before Kruger has built sufficient independent capacity | Direct bonus ends, archives and assistants create a smaller aftermath system |
| Failed confinement | Kruger survives and escapes or seizes the laboratory network | Immediate rebellion or foreign defection, strength derived from project history |
| Violent Kruger rebellion | Host refuses sovereignty after Kruger has prepared forces and facilities | New country, civil conflict, project-derived army, focus tree |
| Host takeover | Extreme dependence and high infiltration allow Kruger to replace the government without territorial split | Host cosmetic and political transformation, rare route, same project tree overlay or country package transition |

## Core visible values

The host should manage three primary visible values and one visible portfolio state.

### Scientific Mandate

Meaning:

Kruger's legal, financial, and political authority over national science.

Increases from:

- Independent budgets.
- Emergency powers.
- Direct military command.
- Immunity from oversight.
- Approving forbidden project stages.
- Letting him appoint assistants and security personnel.
- Giving him control of multiple facilities.

Decreases from:

- Public review.
- Shared university governance.
- Independent safety boards.
- Dividing projects among institutions.
- Requiring ministerial or parliamentary approval.
- Successfully negotiating limits after a breakthrough.

Gameplay meaning:

High Mandate makes projects faster and cheaper in administrative friction. It also gives Kruger more control over guards, archives, facilities, and project results.

### Institutional Dependence

Meaning:

How much the host's research, production, military planning, and scientific personnel rely on Kruger personally.

Increases from:

- Using him in many special-project fields.
- Centralizing all research around one facility.
- Replacing ordinary institutions with his methods.
- Approving projects that require his unique calculations, biology, or machines.
- Accepting emergency solutions during war.
- Purging or sidelining scientists who disagree with him.

Decreases from:

- Training independent teams.
- Publishing methods.
- Building redundant laboratories.
- Rotating assistants through universities.
- Completing public replication missions.
- Maintaining ordinary research institutions.

Gameplay meaning:

High Dependence increases the immediate research advantage and project performance. It also makes removal, death, defection, or rebellion more damaging.

### Security Exposure

Meaning:

How visible, infiltrated, and internationally contested the Kruger program has become.

Increases from:

- Public fame.
- Foreign invitations.
- Multiple facilities.
- Failed security missions.
- Project accidents.
- Defecting assistants.
- Public demonstrations.
- Captured documents.
- Enemy occupation near a facility.

Decreases from:

- Compartmentalization.
- Counterintelligence.
- Relocation.
- False project trails.
- Secure transport.
- Successful foreign disinformation.

Gameplay meaning:

High Exposure increases foreign actions, assassination risk, theft, public pressure, and international opinion effects. It can also increase prestige, attract talent, and make public science more effective.

### Project Portfolio

The player sees which research families have reached Theory, Prototype, Deployment, and Weaponization or Autonomy. Project stages determine:

- Current bonuses and unlocked technologies.
- Available decisions and incidents.
- Kruger's portrait evolution.
- Foreign interest.
- Accident families.
- Breakaway army types.
- Kruger State focus priorities.
- World-end synergies.

## Hidden state

### Independent Capacity

Independent Capacity measures Kruger's practical ability to survive government action and operate without the host.

It is derived from:

- Mandate.
- Dependence.
- Number and quality of facilities.
- Loyal assistants.
- Private guards.
- Project stages.
- Control of autonomous machines, clones, monsters, portals, or temporal duplicates.
- Security access.
- Stored equipment and strategic materials.
- Foreign contacts.
- Time spent preparing after a confrontation begins.

The exact value and final threshold remain hidden. The player receives evidence through visible incidents:

- Guards who answer to laboratory officers.
- Procurement records that do not match declared projects.
- Assistants refusing government transfers.
- Duplicate signatures or biometric records.
- Unexplained troop movements near facilities.
- Machines operating after shutdown orders.
- Missing specimens.
- New tunnels, power demands, or transport schedules.

### Grievance

Grievance records Kruger's hostility toward the host.

Major increases:

- Public humiliation.
- Denial after repeated approval promises.
- Killing assistants.
- Foreign sabotage that the host fails to prevent.
- Attempted arrest or assassination.
- Seizing his archives.
- Using his discoveries while denying him credit or authority.

Major decreases:

- Fulfilling negotiated agreements.
- Protecting assistants.
- Allowing publication or credit.
- Granting a peaceful charter.
- Accepting safety demands that he considers technically necessary.

Grievance shapes whether a separation becomes negotiated, evasive, retaliatory, or exterminatory.

## Failure and counterplay philosophy

The event should never punish the player for accepting Kruger through an unavoidable hidden coin flip. Danger must follow accumulated choices and neglected warnings.

Counterplay includes:

- Limit Mandate before project weaponization.
- Spread methods to reduce Dependence.
- Protect facilities without giving Kruger direct control of all security.
- Invest in independent teams.
- Deny the most autonomy-producing project stages.
- Move dangerous prototypes away from the main laboratory.
- Negotiate a charter before confrontation becomes violent.
- Use foreign inspection or allied guarantees when domestic control is weak.
- Prepare military containment around project facilities.
- Remove Kruger early, accepting the loss of the research advantage.

The strongest rewards require accepting real risk. The safest route still provides a meaningful scientific story and a lasting benefit.

## Event Details direction

The Event Details entry should describe a gifted scientist appearing in one country and the uncertainty around his origin, methods, and ambitions. It should mention that his work can reshape the host's scientific institutions and attract foreign attention.

It must not list:

- The `+100%` research modifier.
- Hidden rebellion thresholds.
- Project-derived armies.
- Specific world-end weapons.
- Achievement paths.
- The guaranteed existence of a Kruger State.

## Catalog direction

The final catalog row should remain concise and player-facing.

- Event type: Minor Fire-Once.
- Details direction: one country receives Doctor Warren Kruger, whose impossible ability can transform its scientific institutions and draw escalating international attention.
- Evolution entries: four distinct evolution summaries, not baseline laboratory stages.
- World-end entry: conditional, describing a sovereign Kruger power and a final strategic weapon only at the level appropriate for the catalog.
- Cluster field: blank.
- Status: Reworked only after full implementation and audit.
