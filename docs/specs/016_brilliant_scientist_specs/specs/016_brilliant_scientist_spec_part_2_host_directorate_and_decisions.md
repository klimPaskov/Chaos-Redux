# 016 Brilliant Scientist spec, part 2: host directorate and decisions

## Binding reconciliation, 2026-07-14

The Directorate must show Mandate, Dependence, Exposure, and Project Capacity. Only Independent Capacity and Grievance remain hidden, with concrete incidents and warnings exposing their consequences. Temporal decisions use synchronization capacity and temporal debt. Each action has a bounded named target, a per-target use record, persistent scars where severe, and evidence-gated counterplay through authentication, observation, anchor discovery, ledger capture, and stabilization. Host takeover is never a territory-resolution action.

## Management purpose

The host-country system should let the player convert Kruger's impossible intellect into research, projects, weapons, institutions, or a new state. It should remain focused enough to understand without becoming a universal science simulator.

The central loop is:

1. Choose how much national capacity Kruger receives.
2. Choose which project families he pursues.
3. Manage Mandate, Dependence, and Security Exposure.
4. Respond to institutions, assistants, foreign powers, and accidents.
5. Decide whether to integrate, constrain, export, negotiate with, or confront him.

The system should use one main decision category with a richer scripted GUI when practical. Ordinary decisions remain the actual gameplay actions. The custom interface makes values, project slots, portrait stages, facility states, and warnings readable.

## Kruger Directorate interface

`Kruger Directorate` is a working interface label, not final localisation.

### Entry point

The interface becomes available after appointment and the primary laboratory site is selected. It should open from the Event 16 decision category. The category header still shows the essential values for players who do not open the custom window.

### Main layout

#### Profile panel

Shows:

- Current Kruger portrait stage.
- National role.
- Public or secret status.
- Current personal condition, such as active, injured, missing, duplicated, machine-linked, confined, or sovereign.
- Current laboratory site.
- Current dominant project family.
- Short status direction written from the visible campaign state.

#### National relationship panel

Shows:

- Scientific Mandate.
- Institutional Dependence.
- Security Exposure.
- Current oversight model.
- Current project capacity.
- Current facility network.
- A broad government-control status, such as secure, contested, brittle, compromised, or lost.

The control status should not expose the hidden Independent Capacity threshold. It should summarize visible evidence.

#### Project portfolio panel

Shows project-family cards with:

- Current stage.
- Next public requirement.
- Capacity occupied.
- Main resource burden.
- Known immediate benefit.
- Known risk class.
- Whether the project is public, classified, compartmentalized, suspended, destroyed, or under foreign investigation.

The panel should not display every project family at once from the beginning. Families appear through research, discoveries, cross-event links, evolution state, and prior projects.

#### Facilities panel

Shows:

- Primary laboratory.
- Secondary laboratories.
- Production sites.
- Test areas.
- Security level.
- Redundancy.
- Staff capacity.
- Power and logistics burden.
- Facility damage or infiltration.

#### Security and foreign contacts panel

Shows:

- Known foreign interest.
- Active protection missions.
- Exposed assistants or stolen archives.
- Invitation offers.
- Joint-laboratory agreements.
- Current security policy.

#### Sovereignty panel

Hidden until the confrontation phase. It later shows:

- Kruger's public demands.
- Negotiated concessions.
- Government red lines.
- Laboratory guard status.
- Known project units.
- Charter, confinement, dismissal, or military options.

It must not show the exact rebellion outcome before the player commits.

## Value presentation

### Color direction

| Value | Color direction | Readability purpose |
| --- | --- | --- |
| Scientific Mandate | Blue | Legal and administrative authority |
| Institutional Dependence | Purple | Reliance on Kruger's unique methods |
| Security Exposure | Red | Foreign and public risk |
| Project Capacity | Green | Productive laboratory bandwidth |
| Government Control status | Yellow to red state frames | Broad warning without revealing hidden arithmetic |

Dynamic values should use integer formatting unless a fraction directly changes decisions.

### Cause breakdown

Every main value tooltip should show named components. For example, Dependence can include:

- Centralized methods.
- Active Kruger-led projects.
- Independent replication teams.
- Public publication.
- Assistant loyalty.
- Emergency military use.

The player should understand why a value changed.

## Decision lifecycle

### Phase A: Appointment and institutional form

#### Select the primary laboratory site

Purpose:

Choose the physical center of the Kruger program.

Requirements:

- Valid controlled core state.
- Supply connection.
- No active enemy occupation.

Dynamic consequences:

- A capital or university city favors staff and public prestige.
- An industrial state favors prototype production.
- A remote state favors secrecy and testing.
- A fortified state favors security.
- A coastal state can support foreign access, shipping, or escape.

This action creates a persistent site target and must be cleaned up if the state changes owner or becomes invalid.

#### Establish a public scientific council

Purpose:

Place universities, civilian ministries, and professional societies around Kruger.

Costs and requirements:

- Civilian factory burden.
- Stable government.
- Available staff.
- Time for institutional setup.

Effects direction:

- Lower Mandate.
- Lower long-term Dependence.
- Higher early Exposure.
- More public research replication.
- Better conventional project safety.
- Slower access to forbidden project stages.

#### Establish a compartmentalized military office

Purpose:

Move Kruger under armed-forces and security control.

Costs and requirements:

- Command capacity.
- Military factory or facility burden.
- Security personnel.
- Higher intelligence exposure if foreign infiltration is already present.

Effects direction:

- Higher secrecy.
- Faster military and strategic projects.
- Higher Mandate.
- Faster Dependence.
- More severe consequences if the military chain becomes loyal to Kruger.

#### Grant a private industrial concession

Purpose:

Let a firm or cartel build around Kruger's work.

Costs and requirements:

- Civilian factories and industrial capacity.
- A suitable industrial state.
- Political willingness to grant patents or exclusive contracts.

Effects direction:

- Fast prototype production.
- Lower direct government cost.
- Corporate pressure and patent disputes.
- Greater risk of archives leaving the country through commercial channels.
- Possible industrial route after Kruger leaves.

#### Build an exile-scholar network

Purpose:

Recruit displaced academics and specialists around Kruger.

Costs and requirements:

- Political and diplomatic cost.
- Available refugee or foreign-scholar context.
- Housing and civilian capacity.

Effects direction:

- Faster assistant recruitment.
- Lower personal Dependence over time.
- Higher foreign political attention.
- Unique moral and ideological flavor.
- Better public-science outcome if Kruger is later removed.

### Phase B: Staff and facility growth

#### Recruit an interdisciplinary cohort

Purpose:

Create a group of assistants from several fields.

Dynamic cost:

- Civilian factories.
- Research capacity.
- Time.
- Possible officer, medical, industrial, or university staff commitment.

Outcome:

- Increase project capacity.
- Add named assistant roles without requiring a huge cast of fixed characters.
- Reduce the chance that one accident ends the program.
- Increase Exposure as more people know the work.

Assistant roles:

- Theoretical deputy.
- Chief engineer.
- Medical director.
- Security liaison.
- Production superintendent.
- Ethics chair.
- Foreign liaison.

These are working role labels, not final character names.

#### Build a secondary laboratory

Purpose:

Increase capacity and redundancy.

Requirements:

- A second valid state.
- Infrastructure, supply, and civilian construction burden.
- Sufficient staff.

Effects direction:

- More project capacity.
- Lower single-site vulnerability.
- Higher total Exposure.
- More possible breakaway territory if Kruger controls both sites.
- More difficult cleanup after accidents.

#### Build a prototype works

Purpose:

Move from theory into production.

Requirements:

- Military or civilian factory commitment based on project type.
- Trains, trucks, fuel, or convoys for logistics.
- A Deployment-stage project.

Effects direction:

- Allows project units and equipment.
- Raises Dependence and Independent Capacity.
- Creates production accidents, worker unrest, and foreign targeting.

#### Establish an isolated test range

Purpose:

Test rockets, weapons, monsters, portals, temporal devices, or biological systems away from the main population.

The Advanced Materials plus Rocketry qualification action is a distinct paid test-range consumer. After Materials Deployment, Rocketry Prototype, expanded prototype works, healthy ledgers, and two valid facilities, the host targets one owned, controlled, core, non-impassable state for a 180-day corridor. It consumes Air Experience, support and motorized equipment, fuel, manpower, Political Power, and three civilian factories. The resulting report chooses a host-local national qualification board or a portable Kruger proprietary flight envelope; invalid transfer, project damage, containment, or terminal cleanup cancels the unfinished corridor without refund.

Requirements:

- Suitable low-population state or controlled overseas site.
- Security and transport burden.
- Project-specific safety resources.

Effects direction:

- Reduces some civilian accident risks.
- Raises logistics cost.
- Creates a second strategic site.
- Makes foreign aerial or naval observation possible.
- Can become an independent Kruger enclave during rebellion.

#### Harden the laboratory network

Purpose:

Protect sites against raids, sabotage, occupation, and accidents.

Costs:

- Construction capacity.
- Anti-air, forts, radar, security equipment, or troops.
- Ongoing supply.

Tradeoff:

Hardening can protect the host. If Kruger later rebels, the same defenses protect him.

### Phase C: Scientific governance

#### Publish the Kruger Method

Purpose:

Spread reproducible parts of Kruger's approach through national institutions.

Requirements:

- Completed replication mission.
- Public or mixed governance.
- Kruger not openly hostile.

Effects direction:

- Lower Dependence.
- Preserve a permanent research remnant if he leaves.
- Increase foreign access and Exposure.
- Reduce exclusive project speed.
- Unlock international scientific prestige events.

#### Compartmentalize every project

Purpose:

Prevent one assistant or foreign agent from seeing the full portfolio.

Effects direction:

- Lower theft risk.
- Lower accident-chain spread.
- Slower cross-project synergies.
- Higher Kruger personal indispensability.
- Higher Dependence.

#### Create an independent safety board

Purpose:

Give scientists, military officers, physicians, and legal officials the power to delay dangerous work.

Effects direction:

- Lower accident risk.
- Lower Mandate.
- Slower Prototype and Weaponization stages.
- Better public legitimacy.
- Chance of confrontation when the board blocks a project Kruger considers essential.

#### Give Kruger final technical authority

Purpose:

Let him override ministries and safety boards.

Effects direction:

- Faster projects.
- Higher Mandate.
- Higher Independent Capacity.
- Fewer ordinary project delays.
- More severe hidden consequences if he prepares without oversight.

#### Train independent replication teams

Purpose:

Create teams that can reproduce one selected project's methods without Kruger.

Costs:

- Project capacity.
- Research delay.
- Equipment and facility time.

Effects direction:

- Lower Dependence in one project family.
- Preserve technology after defection or death.
- Create an assistant group that can oppose, imitate, or betray Kruger.

### Phase D: Security and intelligence

#### Assign ordinary state security

Purpose:

Protect Kruger while keeping the chain of command outside his laboratory.

Effects direction:

- Moderate protection.
- Lower Independent Capacity than a private guard.
- Risk that foreign services identify the program through normal bureaucracy.

#### Authorize a laboratory guard

Purpose:

Let Kruger recruit and command his own guards.

Effects direction:

- Strong protection and lower sabotage risk.
- Large increase to Mandate and Independent Capacity.
- Guard quality can inherit robotics, cloning, exotic weapons, or monster support.

#### Rotate security personnel

Purpose:

Prevent a permanent guard culture from forming.

Costs:

- Command disruption.
- Temporary project slowdown.
- Equipment and training burden.

Effects direction:

- Lower Independent Capacity.
- Higher risk of leaks from a wider personnel pool.

#### Conduct a loyalty review

Purpose:

Investigate assistants, guards, and contractors.

Outcomes:

- Discover foreign agents.
- Discover Kruger loyalists.
- Wrongful purge that raises Grievance.
- Reveal that some staff are clones, machines, or duplicates after relevant projects.

This should be a mission with uncertain findings shaped by intelligence capability, Exposure, and project history, not a repeatable certainty button.

#### Relocate Kruger

Purpose:

Move the primary site after a threat, invasion, or political crisis.

Requirements:

- Secure route.
- Trains, trucks, convoys, or aircraft appropriate to geography.
- Available destination facility.
- Time.

Risks:

- Foreign interception.
- Prototype loss.
- Staff refusal.
- Kruger using the move as an escape.
- Portal or temporal projects making ordinary relocation plans obsolete.

#### Create false project trails

Purpose:

Feed foreign intelligence plausible but wrong information.

Effects direction:

- Reduce effective Exposure.
- Create a chance that rivals waste resources or trigger accidents.
- Risk diplomatic scandal if exposed.
- Kruger may use the false network for his own foreign contacts.

### Phase E: Resource allocation

The player should not buy generic progress with political power. Each resource action represents a real national commitment.

#### Allocate civilian construction teams

Supports:

- Facilities.
- Public laboratories.
- Power systems.
- Medical infrastructure.
- Industrial synthesis.

Costs:

- Temporary civilian factory burden.
- Trains and trucks for large sites.
- Consumer and housing pressure at high scale.

#### Allocate military production

Supports:

- Rocketry.
- Exotic arms.
- Robots.
- Strategic weapons.
- Hardened facilities.

Costs:

- Military factory burden.
- Steel, tungsten, chromium, aluminum, or project-specific strategic resources.
- Equipment production loss.

#### Assign field units to trials

Supports:

- Military prototypes.
- Portal tactics.
- Robot command integration.
- Monster control.
- Protective equipment.

Costs and risks:

- Temporarily tied-down divisions.
- Equipment damage.
- Casualties.
- Lower unit experience or readiness.
- Condemnation if the trial violates accepted norms.

#### Assign medical and population programs

Supports:

- Biomedical acceleration.
- Cloning.
- Super-soldier work.
- Biological defense.

Costs and limits:

- Medical capacity.
- Manpower.
- Stability and public trust.
- Strong ethical gate.
- Any non-consensual route must create severe political, death, condemnation, and future-disaster consequences.

#### Grant strategic materials

Supports:

- Atomic and exotic energy work.
- Advanced electronics.
- Temporal devices.
- Alien arms.

Costs:

- Fuel.
- Rare resources.
- Convoys.
- Special equipment.
- Production disruption.

### Phase F: University and institutional conflict

#### Award the national chair

Purpose:

Give one university formal leadership of the public network.

Consequences:

- Faster public replication.
- Rival university resentment.
- Regional prestige and construction.
- One institution becomes a foreign intelligence target.

#### Rotate grants among institutions

Purpose:

Spread influence and prevent one monopoly.

Consequences:

- Lower Dependence.
- Slower concentrated progress.
- More resilient aftermath.
- Higher administrative burden.

#### Let Kruger select the institutions

Purpose:

Give him control of appointments and funding.

Consequences:

- Faster projects.
- Higher Mandate.
- Kruger loyalist network.
- Purged or excluded scholars may defect abroad.

#### Protect dissenting scientists

Purpose:

Keep internal critics inside the system.

Consequences:

- Better safety and public legitimacy.
- Slower dangerous projects.
- Lower Grievance among ordinary institutions.
- Kruger may demand their removal after a major accident or leak.

#### Dismiss the ethics chair

Purpose:

Remove a persistent obstacle to weaponization.

Consequences:

- Immediate project acceleration.
- Stability and legitimacy loss.
- Higher Grievance among assistants.
- Foreign asylum or leak event.
- More severe future accidents.

### Accepted finite country-specific institutional settlements (static implementation complete; targeted validation pending, 2026-08-03)

The accepted settlement addendum adds ten conditional choices inside the existing `chaosx.nr16.5` assistant-conflict event. Static source inspection confirms the named choices, resolvers, receipts, constants, selectors, AI factors, and localisation keys, and the bounded source implementation is complete in the working tree; targeted balance, transfer, cleanup, and live-acceptance evidence are still pending.

The generic `.5.a`, `.5.b`, and `.5.c` options remain unchanged. The national choices are available only to `ENG` and `FRA` in public-science or distributed-research context, `USA` and `CZE` in industrial-mobilization or distributed-research context, `SOV`, `JAP`, `GER`, `ITA`, and `CHI` in strategic-security or industrial-mobilization context, and `POL` in public-science, distributed-research, or strategic-security context. Each choice clears the pending assistant conflict, marks it resolved, calls its named bounded base resolver and settlement resolver, and schedules the impossible lecture once. Unnamed countries retain the complete generic choice set.

The accepted option and receipt contract is:

| Tag and option | Base resolver | Host-local receipt | Total vector `(Mandate, Dependence, Exposure, Project Capacity, Independent Capacity, Grievance)` |
| --- | --- | --- | --- |
| `ENG` `chaosx.nr16.5.d_eng` | `brilliant_scientist_context_recognize_assistant_school` | `brilliant_scientist_country_settlement_british_research_associations` | `(+5, -10, +15, +5, +20, -15)` |
| `USA` `chaosx.nr16.5.e_usa` | `brilliant_scientist_context_mediate_assistant_conflict` | `brilliant_scientist_country_settlement_american_federal_contracts` | `(+10, +5, +10, +15, +5, -5)` |
| `SOV` `chaosx.nr16.5.f_sov` | `brilliant_scientist_context_bind_assistant_service` | `brilliant_scientist_country_settlement_soviet_academy_plan` | `(+5, +20, -5, +15, -5, +20)` |
| `JAP` `chaosx.nr16.5.g_jap` | `brilliant_scientist_context_mediate_assistant_conflict` | `brilliant_scientist_country_settlement_japanese_riken_council` | `(+15, +5, +5, +10, +5, +5)` |
| `GER` `chaosx.nr16.5.h_ger` | `brilliant_scientist_context_bind_assistant_service` | `brilliant_scientist_country_settlement_german_research_board` | `(+10, +20, -10, +20, -15, +20)` |
| `FRA` `chaosx.nr16.5.i_fra` | `brilliant_scientist_context_recognize_assistant_school` | `brilliant_scientist_country_settlement_french_laboratories` | `(+10, -10, +15, +5, +25, -20)` |
| `ITA` `chaosx.nr16.5.j_ita` | `brilliant_scientist_context_mediate_assistant_conflict` | `brilliant_scientist_country_settlement_italian_procurement_compact` | `(+20, +10, +15, +15, +5, -5)` |
| `CHI` `chaosx.nr16.5.k_chi` | `brilliant_scientist_context_bind_assistant_service` | `brilliant_scientist_country_settlement_chinese_technical_bureau` | `(+5, +25, -10, +20, -20, +15)` |
| `POL` `chaosx.nr16.5.l_pol` | `brilliant_scientist_context_mediate_assistant_conflict` | `brilliant_scientist_country_settlement_polish_university_shelter` | `(+15, 0, +10, +5, +15, 0)` |
| `CZE` `chaosx.nr16.5.m_cze` | `brilliant_scientist_context_recognize_assistant_school` | `brilliant_scientist_country_settlement_czechoslovak_research_charter` | `(+5, -15, +15, +15, +20, -15)` |

The delta and AI values belong in `common/script_constants/016_brilliant_scientist_country_settlement_constants.txt`. The ten receipts are host-local institutional history and must not be added to the ordinary transfer-copy block or the Kruger State formation-copy block. They do not create, clone, rename, recruit, or re-scope Kruger. `.7` and `.8` receive only receipt-driven description clauses and AI modifiers; they do not receive new options or effects. Existing reaction outcomes, project custody, transfer ownership, terminal cleanup, and formation cancellation rules remain authoritative.

### Phase G: Confrontation and removal

The confrontation category becomes visible only after a public demand, a major security breach, a detected private army, or a government decision to end the appointment.

#### Negotiate binding limits

Purpose:

Create a settlement while Kruger still believes cooperation is useful.

Success factors:

- Low Grievance.
- Low or moderate Independent Capacity.
- Protected assistants.
- Prior agreements honored.
- Strong but non-hostile security.
- Public institutions able to continue without him.

Possible outcomes:

- Controlled secret compact.
- Public scientific settlement.
- Temporary truce.
- Kruger accepts limits publicly while preparing privately.

#### Offer a peaceful charter

Purpose:

Create a legally autonomous Kruger State before violence.

Requirements:

- Host controls a valid laboratory territory.
- Border and capital viability.
- Kruger accepts negotiated borders.
- Government can survive the transfer.

Tradeoffs:

- Lose territory and direct research bonus.
- Preserve a technology relationship, non-aggression agreement, research access, or joint projects.
- Avoid immediate civil war.
- Create foreign diplomatic reactions.
- High Grievance can still create later hostility.

#### Dismiss and escort him abroad

Purpose:

End the appointment without imprisonment.

Success factors:

- Low Dependence.
- Low Independent Capacity.
- Valid recipient or neutral destination.
- Secure transport.

Failure variants:

- Voluntary defection to a rival.
- Assistants follow him.
- Archive theft.
- Prototype escape.
- An apparent Kruger leaves while a clone or machine copy remains.

#### Confine Kruger

Purpose:

Seize him and preserve the archives.

The player should receive a severe warning that government control is uncertain. The exact result stays hidden.

Low-capacity outcome:

- Kruger is confined.
- The host chooses trial, continued coerced work, exile, or humane detention.
- Coerced work creates long-term risk and ethical consequences.

Medium-capacity outcome:

- He escapes, defects, or releases one prepared project force.
- A smaller crisis begins.

High-capacity outcome:

- Laboratory guards seize sites.
- Project-derived units activate.
- The Kruger State forms.

#### Kill Kruger

Purpose:

A final removal attempt.

This route must not be a safe universal reset.

Possible outcomes by portfolio:

- Ordinary death before replication or machine work ends the character and begins an archive aftermath.
- Clone research reveals that the target was one of several bodies.
- Machine research transfers part of him into a network.
- Temporal research causes contradictory death records or a later return.
- Alien biology makes identification uncertain.
- Monster or robot guards trigger immediate retaliation.
- Biological fail-deadly systems release contamination.

The player should understand that project history matters, but not receive a full outcome list in advance.

#### Military seizure of the laboratory network

Purpose:

Take facilities, prototypes, and project troops by force before a formal rebellion.

Requirements:

- Divisions assigned to named laboratory states.
- Supply and rail access.
- Command power kept within project limits.
- Equipment for containment.
- Air or naval control if the site requires it.

Outcomes:

- Complete seizure.
- Partial seizure with archive destruction.
- Multiple-site civil war.
- Portal evacuation.
- Project accident.
- Foreign intervention during the operation.

### Phase H: Post-Kruger recovery

#### Reconstruct independent research

Purpose:

Recover from defection, death, or rebellion.

Requirements:

- Civilian investment.
- Surviving assistants.
- Time.

Outcomes:

- Reduce scientific vacuum.
- Preserve selected conventional project benefits.
- Create counter-Kruger research capacity.

#### Secure abandoned archives

Purpose:

Recover project material after escape or rebellion.

Mission structure:

- Target a specific facility state.
- Hold it and maintain supply.
- Prevent sabotage for a set duration.
- Success yields project knowledge or countermeasures.
- Failure lets Kruger destroy, steal, or corrupt the archive.

#### Offer amnesty to assistants

Purpose:

Split staff loyalty after confrontation.

Tradeoff:

- Recover expertise.
- Accept infiltration risk.
- Lower the size of Kruger's country and army if used before the final split.

#### International inspection

Purpose:

Gain foreign help dismantling dangerous work.

Tradeoff:

- Lower domestic cleanup cost.
- Reveal technology to rivals.
- Improve legitimacy.
- Create treaty or tech-sharing consequences.

## Mission families

### Replication missions

Goal:

Prove that ordinary teams can reproduce one Kruger result without him.

Objective examples:

- Complete a selected conventional technology category while Kruger works elsewhere.
- Build and supply a secondary laboratory.
- Maintain two independent teams for a defined period.
- Complete a prototype without using Kruger as the assigned scientist.

Success:

- Lower Dependence.
- Preserve project knowledge.
- Unlock safer retirement or confinement outcomes.

Failure:

- Increase Dependence.
- Strengthen Kruger's argument for more authority.

### Facility security missions

Goal:

Protect a named site during a foreign-threat period.

Objectives:

- Hold the state.
- Keep rail or port supply open.
- Assign a required number of divisions or security resources.
- Maintain air defense or intelligence coverage.

Success:

- Reduce effective Exposure.
- Capture foreign agents.
- Improve government control.

Failure:

- Stolen project progress.
- Assistant loss.
- Sabotage.
- Kruger Grievance.

### Project containment missions

Goal:

Prevent an accident from spreading.

Objectives depend on project family:

- Quarantine biological sites.
- Shut down power to machine networks.
- Hold portal perimeter states.
- Recover escaped creatures.
- Prevent temporal duplicates from leaving a test area.

Success and failure must connect to deaths, contamination, condemnation, panic, state modifiers, project stage, and later rebellion assets where relevant.

### Sovereignty deadline missions

Goal:

Resolve Kruger's demand before he completes independent preparations.

Possible player paths during the timer:

- Negotiate a charter.
- Lower his capacity by securing facilities.
- Split assistants.
- Prepare military containment.
- Accept the demand.
- Seek foreign guarantees.

The mission timer should scale with Mandate, project portfolio, war state, and whether Kruger believes the host is acting in good faith.

## AI behavior for host decisions

AI hosts need route personalities rather than random clicks.

| Host profile | Preferred governance | Project preference | Confrontation behavior |
| --- | --- | --- | --- |
| Liberal institutional | Public council, independent teams, publication | Electronics, industry, medicine, defensive projects | Negotiates limits or peaceful charter |
| Wartime emergency | Secret office, concentrated facilities | Rockets, atomic, exotic arms, biomedical military work | Delays confrontation until war pressure falls |
| Authoritarian security | Military office, laboratory guard, compartmentalization | Weapons, AI, biological, surveillance | Grants Mandate, later attempts seizure if control falls |
| Small threatened state | Mixed governance, foreign protection | Industry, defensive weapons, cloning or robots if desperate | Bargains for security or grants charter |
| Technocratic opportunist | Private concession, concentrated network | Broad portfolio and synergies | Accepts high dependence and risks takeover |
| Morally restrictive | Safety board, public replication | Conventional science, medical, defensive work | Removes or confines early after forbidden demands |
| High-chaos extremist | Unrestricted laboratory | Monsters, temporal work, biological weapons, singularity | Supports sovereignty or joins world-conquest route |

AI must check resources before starting projects. It should prefer fewer completed project families over many stalled Theory stages.

## Category clutter control

- Show only current-phase decisions.
- Hide institutional-form choices after one is selected, while exposing later reform actions.
- Limit active projects by capacity.
- Show one selected foreign target at a time for player-facing foreign actions.
- Hide completed, destroyed, obsolete, or route-invalid project decisions.
- Replace early facility actions with upgraded variants rather than leaving both visible.
- Use emergency visibility for accidents, infiltration, invasion, and sovereignty deadlines.
- Close the host category after a final resolution, then replace it with a smaller aftermath category if needed.

## Exploit boundaries

- No repeatable button may create unlimited free research bonuses, project progress, divisions, facilities, or strategic materials.
- Moving Kruger between countries cannot duplicate the character or preserve full bonuses in both countries.
- Clones or machine copies are route mechanics, not duplicate advisor stacking.
- Dismissing and rehiring Kruger is impossible outside designed transfer events.
- A player cannot repeatedly trigger removal attempts to reroll a favorable hidden result.
- Facility construction has real capacity and map requirements.
- Research replication lowers Dependence through time and opportunity cost, not a cheap instant purchase.
- Peaceful charter territory cannot be used to strip allies or subjects of states without ownership and control safeguards.
