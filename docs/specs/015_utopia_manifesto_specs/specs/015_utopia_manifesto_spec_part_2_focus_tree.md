# Event 015, `utopia_manifesto`, focus tree specification

## Tree purpose

The Utopian Manifesto tree is a full replacement tree for the accepting country. It must make a small country play like an ideological experiment with a living civic economy, a contested interpretation of need, and a path from local reform to regional order.

The final in-game layout belongs to the implementation agent. This spec defines route families, branch logic, anchor focus groups, route locks, rewards, idea lifecycles, and AI behavior. Working focus labels are not final localisation.

## Expected tree size and shape

Target range: 85 to 115 focuses.

The tree should use non-linear branch architecture:

- opening trunk and first institutions
- interpretation fork with four normal routes
- hidden coercive route
- common stores and useful arts branch
- vocation and learning branch
- military and just-war branch
- diplomacy, neighbors, and league branch
- needful land and integration branch
- geography branch that adapts to island, coastal, landlocked, subject, and tiny countries
- late proclamation branch

The support branches should interact with political choices. The player should not simply finish one vertical path and then collect generic bonuses.

## Lane map

| Lane | Placement direction | Main role | Interacts with |
| --- | --- | --- | --- |
| Opening trunk | center top | discovery, translation, census, ledger reveal | all branches |
| Interpretation routes | center and upper left/right split | political identity and route locks | decisions, ideas, diplomacy, expansion |
| Common stores and useful arts | left support lane | economy, infrastructure, warehouses, production, surplus | Vocation, diplomacy, integration |
| Vocation and learning | left-center support lane | job choice, research, public education, shortages | industry, politics, military |
| Military and just war | right support lane | defense, citizen drills, indirect war, mercenaries | expansion, diplomacy, suspicion |
| Diplomacy and neighbors | far left or lower-left | foreign aid, magistrates, friends, League | surplus, consent, suspicion |
| Needful land and integration | far right or lower-right | claims, arbitration, occupation, coring | need, overreach, military |
| Geography branch | lower center with conditional entries | island, coastal, inland ring, subject autonomy | industry, military, diplomacy |
| Late proclamation | bottom center | New Utopia, League, or Marked Bounds outcome | all major routes |

## Opening trunk

The opening trunk should take roughly 8 to 12 focuses. It introduces the manifesto and the first institutions without locking the country too early.

### Opening focus groups

| Focus group | Role | Reward direction | Notes |
| --- | --- | --- | --- |
| Found Manuscript | acknowledges discovery and enables public translation | removes initial curiosity flag, small stability or political capital, event detail update | event title direction should stay grounded |
| Translate the Old Hand | creates the first readers and translators | unlocks scripted localisation for the Ledger, starts Common Stores category | do not use final source quote |
| First Household Census | measures people, homes, work, and shortages | sets baseline Need, Consent, Surplus, and Vocation Balance | can scale by states, population, stability, and subject status |
| The Public Reading | opens national debate | route unlock, small party popularity movement based on ideology | player sees interpretation fork soon after |
| Storehouse Trial | creates first common store in capital or most suitable state | state modifier, civilian factory burden, Surplus movement | should use construction and infrastructure hooks |
| The Useful Arts Register | collects craft petitions | unlocks Vocation Accord decisions | can produce early shortages if ignored |
| The Question of Boundaries | introduces land-by-need issue | unlocks Needful Land branch preview, not the full coercive route | should imply controversy without spoiling late route |
| A Country That Can Be Read | commits to the new tree identity | converts Found Manifesto into route-selectable spirit | enables first route lock focus group |

### Early choices

The early tree should ask the player to choose between institutional style before ideology fully changes.

- Readers' Assembly gives high Consent and slower decisions.
- Storekeeper Commission gives better Surplus and bureaucracy cost.
- Civic Wardens gives defense and lower foreign trust.
- Guild Congress gives Vocation Balance tools and labor politics.

These are soft openers. They lead toward the four normal interpretation routes.

## Normal interpretation routes

### Route A, Living Humanism

This is the consent and council route. It adapts the manifesto through public deliberation, education, and religious or philosophical tolerance where fitting.

| Element | Direction |
| --- | --- |
| Political role | democratic or liberal-humanist route when compatible with country ideology |
| Mechanical role | high Consent, better peaceful integration, better diplomacy, weaker forced claims |
| Unlocks | local councils, public debates, observer missions, consent integration projects, peaceful League path |
| Tradeoff | slow expansion, fewer emergency compulsion tools, more vulnerability to crisis when Need is high |
| AI | democracies, high-stability minors, and player-adjacent peaceful AI prefer it |

Anchor focus groups:

- Councils of the Households: changes government or ruling party direction toward democratic, council, or public commonwealth identity.
- Laws in Plain Speech: improves compliance gain, reduces resistance in integrated states, raises Consent.
- Tolerance in the Temples: improves stability and reduces ideology conflict, unlocks religious or cultural accommodation decisions where relevant.
- The Three-Day Debate: decisions and focus bypasses become slower but safer, raises Consent after public missions.
- Consent Before Settlement: integration projects require local consent but grant stronger long-term cores.
- A League of Willing Neighbors: opens the peaceful Utopian League route.

Avoid making this route only stability and democracy drift. It must change integration rules and diplomacy.

### Route B, The Common Store State

This is the planning and distribution route. It treats the manifesto as a manual for measuring production, stores, and useful labor.

| Element | Direction |
| --- | --- |
| Political role | technocratic neutral, democratic planning, or socialist planning depending on ideology context |
| Mechanical role | high Surplus, strong industry projects, better shortage response, stronger Vocation management |
| Unlocks | warehouse network, ration missions, production shifts, foreign surplus aid, emergency allocation orders |
| Tradeoff | higher bureaucracy burden, risk of lowering Consent through assignments |
| AI | subjects, low-industry minors, and states under economic pressure prefer it |

Anchor focus groups:

- The Capital Storehouse: builds first warehouse chain and improves supply.
- The Ledger of Need: improves Need calculation and unlocks dynamic cost reductions when Need is real.
- Warehouses Without Locks: reduces consumer goods after successful storehouse missions.
- Iron Before Ornament: production and resource branch that favors steel, tools, trains, trucks, and support equipment over luxury abstractions.
- The Public Granary Model: state infrastructure and supply hub construction decisions.
- Emergency Allocation Articles: strong decisions that solve shortages but risk Consent loss.
- Surplus Sent Abroad: diplomacy actions using excess production and convoys.

This route can remain humane or slide into compulsion depending on choices. It should not automatically become the hidden coercive route.

### Route C, Guild Commonwealth

This is the labor-choice route. It treats the manifesto's chosen trades as the constitution of the state.

| Element | Direction |
| --- | --- |
| Political role | cooperative, socialist, syndical, guild, or labor republican depending on country context |
| Mechanical role | strongest Vocation Balance tools, research and production specialization, worker militias |
| Unlocks | craft guild decisions, apprenticeship missions, learning branch, labor councils, volunteer cadres |
| Tradeoff | production shortages when a popular trade is overchosen, internal faction disputes |
| AI | communist, socialist, high-union, or high-worker-pressure countries prefer it |

Anchor focus groups:

- Petition of Trades: lets citizens request vocations and raises Consent if honored.
- Useful Arts Congress: unlocks trade guild cards in the Ledger.
- Apprentices by Inclination: production efficiency and research bonuses if Vocation Balance stays healthy.
- The Six-Hour Ambition: reduces economic strain through efficiency and learning, but only after storehouses can support it.
- The Scholar Lots: special research or advisor unlocks tied to high Learning vocation share.
- Factory Households: converts industrial states into common production cells.
- Craft Militias: creates unit families from guilds, with equipment and training requirements.

The route should not be a simple communism path. Its identity is labor choice constrained by public need.

### Route D, Island Discipline

This is the civic defense and ordered service route. It imagines the country as an island even if geography says otherwise.

| Element | Direction |
| --- | --- |
| Political role | neutral, paternal, constitutional authoritarian, or disciplined civic route |
| Mechanical role | defense, resilience, lower invasion risk, military readiness, stable authority |
| Unlocks | border and port missions, citizen drills, household guard units, inland ring branch, strict service laws |
| Tradeoff | lower Consent growth, higher Foreign Suspicion, limited peaceful diplomacy if overused |
| AI | small threatened states, island minors, and countries near aggressive neighbors prefer it |

Anchor focus groups:

- The Island in the Mind: unlocks geography branch and defensive state selection.
- Citizen Exercises: trains men and women in defense, with manpower and equipment costs.
- The Harbor Watch or Inland Ring: conditional branch based on coastal access.
- No Rash Wars: war support, defensive bonuses, and offensive war penalties unless justified by the Ledger.
- Wardens of the Common Peace: internal security and resistance suppression through local support.
- Sacred Interposers: peacekeeping and battlefield restraint concepts from Utopian priests, represented through decisions that reduce casualties or speed peace talks.
- The Closed Shore: late defensive fortification and coastal denial.

This route should make the country hard to conquer. It should not be the best route for global expansion.

## Hidden interpretation, Marked Bounds

Marked Bounds is the dangerous route. It opens when the state decides that its own measured need justifies taking uncultivated, weakly defended, or poorly administered land.

### Unlock conditions

Open this route if one or more of these is true:

- Need is very high for a sustained period
- Overreach is already high
- arbitration missions repeatedly fail
- the country has lost core territory or is blockaded
- chaos tier is high and the relevant evolution is enabled
- the player takes repeated emergency allocation or forced assignment decisions
- the country follows Common Store State or Island Discipline and then chooses hardline boundary focuses

AI should not choose this route under ordinary conditions. It can choose it at high chaos, under severe threat, or if authoritarian and surrounded by weak targets.

### Route content

| Focus group | Role | Reward direction | Risk |
| --- | --- | --- | --- |
| The Clause of Waste Soil | public doctrinal break | unlocks stronger claims and harsh arbitration | large Foreign Suspicion |
| Surveyors of Idleness | target selection | identifies states considered underused | diplomatic incidents |
| Mark the Bounds | expansion opener | claims or war goals under strict need rules | Overreach spike |
| Settlement Without Invitation | forced integration | faster occupation projects | resistance, Consent loss |
| The Necessary War | military doctrine | attack bonuses against marked targets | chaos and coalition risk |
| The Quiet Expulsion Crisis | internal crisis | local unrest, condemnation risk if abusive | can close peaceful routes |
| The Perfect Country Problem | late crisis | choose reform, double down, or face backlash | possible civil split or foreign coalition |

The route must remain playable, but it should be morally and mechanically costly. It should not produce free cores. It should grant claims first, then contested integration only after projects, compliance, infrastructure, and suppression or consent work.

### Reform exit

A player who opened Marked Bounds should have a difficult reform exit:

- renounce forced settlement
- pay reparations through factories, convoys, or equipment
- lose claims on some targets
- lower Overreach slowly
- regain peaceful diplomacy
- keep some defensive or administrative lessons

This route should support a hidden achievement for recovering from the coercive path without collapsing.

## Common stores and useful arts branch

This branch should be compatible with every normal interpretation. It changes costs and bonuses based on route.

### Branch groups

| Group | Route interaction | Reward types |
| --- | --- | --- |
| Capital Warehouse | all routes | supply hub or capital state modifier, consumer goods changes, first storehouse decisions |
| Monthly Storehouse Audits | Common Store State stronger | dynamic Surplus gain, corruption risk if bureaucracy high |
| Farms by Rotation | Living Humanism and Guild gain Consent, Island Discipline gains readiness | infrastructure, supply, attrition reduction, rural training |
| Necessary Crafts | Guild strongest | production efficiency, equipment conversion, tech bonuses, factory output |
| Iron, Linen, Glass | Common Store and Guild | steel import reductions, trucks, trains, support equipment, civilian factory projects |
| Public Repair Days | all routes | timed missions to repair infrastructure, rail, ports, forts, or airbases |
| No Luxury Schedule | Common Store and Island Discipline | consumer goods reduction, stability risk for elites, foreign trade effects |
| Surplus Beyond the Town | diplomacy hook | aid decisions, relations, League preparation |

Rewards should include buildings, production lines, construction decisions, state modifiers, stockpile conversions, research bonuses, and national spirit upgrades. Avoid repeated generic factory focuses.

## Vocation and learning branch

This branch manages chosen labor and public learning.

### Vocation tracks

| Vocation | Main effects | Shortage risk | Route synergy |
| --- | --- | --- | --- |
| Agriculture | supply, attrition reduction, infrastructure repair, population resilience | low production and research if too high | Living Humanism, Island Discipline |
| Useful Arts | factory output, production efficiency, repair, equipment conversion | Consent and research stagnation if too high | Common Store, Guild |
| Learning | research, advisor quality, codebreaking or intelligence | low manpower and industry if too high | Guild, Living Humanism |
| Civic Service | compliance, stability, resistance reduction, integration speed | lower military and production if too high | Living Humanism, Common Store |
| Defense | recruitable population, training, militia, forts | Consent and economy strain if too high | Island Discipline, Marked Bounds |

### Focus groups

- Petition Days: citizens choose vocations.
- Second Trade Permission: unlocks switching without heavy penalties.
- Scholars Before Dawn: research and advisors.
- Useful Games and Public Lectures: stability, learning, and entertainment without luxury effects.
- Idleness Audits: prevents free-riding, but can become coercive.
- Assignment by Need: emergency action. It should be powerful and risky.
- The Six-Hour Ambition: late route that reduces consumer burden and improves stability if Surplus and Balance are high.

The branch should create choices. If the player pushes Defense and Useful Arts too hard, Learning and Consent should suffer. If the player honors every popular petition, Need may rise because necessary roles are empty.

## Military and just-war branch

The Utopian country should not be pacifist by default. It dislikes glory, but it trains, defends, and fights under defined causes.

### Branch philosophy

- war for conquest without Need damages Consent and raises Overreach
- defensive war improves Consent and can lower Foreign Suspicion
- aid to oppressed or friendly minors is legitimate if the target asked for help or was attacked
- indirect methods can reduce casualties but create suspicion and ethical risk
- mercenary decisions cost Treasury Abroad, equipment, convoys, or political credibility

### Focus groups

| Group | Reward direction | Cost or risk |
| --- | --- | --- |
| Daily Exercises | training time, army XP, militia templates | infantry equipment and manpower |
| Women and Men in Drill | wider recruitable base, support units, stability if Consent high | conservative backlash in some ideologies |
| The Household Guard | defensive divisions scaled by states and manpower | equipment cost and Vocation Defense share |
| The Harbor Watch | coastal defense, naval mine or port protection where supported | coastal only or alternate inland version |
| No Rash War | offensive war penalties without justification, defensive bonuses | blocks some aggressive choices |
| The Bloodless Victory | intelligence, sabotage, surrender pressure, leader-targeting abstraction | Foreign Suspicion and Overreach |
| Treasury Abroad | builds variable used for hired forces and influence | requires surplus exports and civilian burden |
| Hired Companies | limited mercenary units or temporary modifiers | Treasury, convoys, foreign suspicion |
| Peace by Interposition | war de-escalation missions, truce or white peace pressure | requires high Consent and low Overreach |

Unit rewards must be specific:

- Household Guard infantry with lower attack and stronger defense
- Storehouse Engineers with support equipment and construction or entrenchment flavor
- Harbor Watch detachments for coastal states
- Surveyor Light Columns for marked border regions
- Foreign Hired Companies that are temporary, costly, and limited
- League Volunteer Cadres after diplomacy route matures

## Diplomacy, friends, and neighbors branch

This branch creates the Utopian external order without making a faction too early.

### Relationship statuses

Use state or country flags to track target relationships:

| Status | Meaning | Unlock source | Benefit |
| --- | --- | --- | --- |
| Observed | target has allowed readers, observers, or aid | early diplomacy decisions | relations and visibility |
| Neighbor | target accepts magistrate or storehouse assistance | diplomacy missions | lower suspicion and aid access |
| Friend | target has received aid, recognition, or defensive support | mid-branch diplomacy | mutual defense or volunteer options |
| League Member | target joins formal Utopian League | late branch, minimum membership | faction or coalition mechanics |

### Focus groups

- Open the Storehouse to Strangers: aid and observer missions.
- Magistrates for Neighbors: send officials or advisors to friendly minors.
- The Friend Without Treaty: improves relations without formal alliances.
- Grain Before Guarantees: aid to minors in crisis, with Surplus and convoys as costs.
- Anti-Tyranny Clause: support oppressed neighbors or subjects, can create foreign tension.
- The League Question: create formal League only after minimum support.
- Common Reserves: shared reserves or volunteers for League members.
- Arbitration Halls: settlement decisions that avoid war if Need is legitimate.
- A Region That Can Be Fed: late peaceful regional order payoff.

The branch should avoid forming a faction just because the country exists. Require minimum members, high Consent or Surplus, and low enough Overreach unless Marked Bounds creates a fear-based rival version.

## Needful land and integration branch

This is the expansion branch. It must be distinct from politics and industry.

### Expansion standards

The player should never get all claims for free. Land action goes through:

1. measure Need
2. identify a plausible target state or region
3. try arbitration or settlement first unless on Marked Bounds
4. face acceptance, refusal, or delay
5. if war follows, apply Just War Ledger rules
6. after control, run integration projects before cores

### Focus groups

| Group | Role | Reward direction |
| --- | --- | --- |
| The Boundary Census | measures homeland shortages and border regions | unlocks targetable Need claims |
| Waste Is a Dangerous Word | public debate over land doctrine | raises Consent if restrained, unlocks choices |
| Arbitration Before Claim | peaceful pressure | target missions and relation tests |
| Settlement Charter | negotiated land or subject arrangement | claims, demilitarized settlement, autonomy options |
| The Needed Port | coastal outlet route for landlocked countries | claim or port charter under strict conditions |
| Common Administration | occupation law and integration projects | compliance, resistance reduction, local support |
| Houses for the New District | local construction project | infrastructure, civ factory burden, compliance |
| The Local Voice | consent integration route | slower cores, higher stability |
| Marked Bounds | hardline route if unlocked | faster claims, high Overreach |
| No Dominion Without Bread | final peaceful expansion discipline | cores only after local supply and consent |

### State integration requirements

A state should become a core or deep integration only after several proof steps. Use a named scripted trigger or state group tooltips.

Required direction:

- owned and controlled
- not in active rebellion
- compliance or local support above a threshold
- resistance under threshold
- infrastructure or supply project completed
- common store established
- local council or household register completed unless on Marked Bounds
- no unresolved forced-removal crisis if peaceful route
- cost paid in civilian burden, support equipment, trains, manpower, or time

Marked Bounds can bypass some consent requirements, but should add resistance, Overreach, and diplomatic penalties. It should not grant instant free cores on large conquered regions.

## Geography branch

The geography branch should adapt to the target country.

### Island or coastal path

Focus groups:

- Harbors of the Common Store
- The Fortified Shore
- Fishing and Convoy Stores
- The Closed Channel
- Civic Signal Ports
- The Island Proclamation

Rewards:

- ports, coastal forts, dockyards, convoys, naval support, supply
- coastal decisions to protect ports and distribute surplus
- stronger New Utopia proclamation if the country controls enough island or coastal states

### Landlocked path

Focus groups:

- The Inland Island
- Rail as Shoreline
- River and Pass Registers
- Supply Hub Ring
- Port by Charter
- The Cut Through Need

Rewards:

- infrastructure, rail, supply hubs, forts
- decisions to secure a port through trade, federation, or need claim
- alternate New Utopia route based on a completed inland ring

### Subject path

Focus groups:

- Stores Under Inspection
- Useful Autonomy
- Overlord Readers
- The Account That Proves Capacity
- A Free Household Among Nations

Rewards:

- autonomy, relations, independence missions, subject-specific decisions
- peaceful independence if high Consent and Surplus
- crisis independence if Need and Overreach are high

## Late proclamation branch

The late branch turns the experiment into a public identity. It can be peaceful, disciplined, guild-led, or coercive.

### Proclamation paths

| Path | Requirements | Result direction | Super-event eligibility |
| --- | --- | --- | --- |
| New Utopia | high Consent, high Surplus, stable Vocation Balance, low Overreach, completed geography path | cosmetic country identity, strong integration, peaceful diplomacy | yes |
| Utopian League | several Friends or League Members, high Surplus, low Foreign Suspicion | faction or coalition with cohesion mechanic | yes |
| The Necessary Commonwealth | high Need solved through integration and defense, moderate Overreach | regional state with strict just-war doctrine | possible news or super-event if region changes |
| Marked Bounds State | high Overreach, several forced integrations, hardline route complete | feared expansion state with backlash | yes, dark route if it becomes regional threat |
| The Paper Utopia | low Consent, low Surplus, high bureaucracy, failed missions | crisis branch, reform or collapse | no super-event unless it starts a large civil conflict |

### Cosmetic identity

Use cosmetic tags or dynamic country names where appropriate. Public map names should be direct country names, such as:

- New Utopia
- Utopian Republic
- Utopian Commonwealth
- Utopian Union
- Utopian League leader name based on original country when needed

Do not use internal office names as public country names.

### Leader and council changes

Late routes may replace or modify leaders:

- Living Humanism: Council of Households or elected reformer
- Common Store State: Storekeeper Directorate or named planner if country context supports one
- Guild Commonwealth: Guild Congress or labor council
- Island Discipline: Civic Wardens or disciplined constitutional leader
- Marked Bounds: Boundary Surveyorate or hardline Warden council

Generated council portraits are allowed for fictional collective leaders. Real leader replacements should use sourced portraits only if using real people.

## Idea lifecycle table

| Idea | Start or unlock | Starting role | Mitigation path | Upgrade path | Failure path | Final forms |
| --- | --- | --- | --- | --- | --- | --- |
| Found Manifesto | event acceptance | temporary curiosity and route seed | opening trunk | Manifesto Mandate | rejection removes route | none after trunk |
| Unproven Common Stores | event acceptance | economic strain and relief promise | Capital Warehouse | Common Store Network | Storehouse Corruption | Common Stores, Emergency Stores, Empty Stores |
| Vocation Confusion | event acceptance | labor uncertainty | Useful Arts Register | Vocation Accord | Compulsory Assignments | Chosen Trades, Assigned Trades, Guild Constitution |
| Foreign Laughter | event acceptance | diplomatic weakness | Observers and aid | Friends Without Treaty | Foreign Suspicion | Respected Experiment, Feared Doctrine |
| Household Councils | Living Humanism | Consent institution | local councils | Plain Law Commonwealth | factional deadlock | Council Commonwealth |
| Storekeeper Commission | Common Store | planning institution | audits | Ledger State | bureaucracy burden | Common Store State |
| Guild Congress | Guild | labor institution | petition balancing | Useful Arts Republic | guild faction dispute | Guild Commonwealth |
| Civic Wardens | Island Discipline | defense institution | defensive missions | Island Discipline | compulsion drift | Warden Commonwealth |
| Marked Bounds Doctrine | hidden route | forced land doctrine | hard reform exit | Necessary War State | coalition backlash | Marked Bounds State or Renounced Bounds |
| Utopian League | late diplomacy | regional coalition | member aid | Common Reserves | member exits | League of Friends |

## Focus reward diversity guide

The implementation should use a varied reward palette:

- state infrastructure and rail projects
- capital or regional supply hubs
- civilian and military factory construction tied to state projects
- dockyards, convoys, ports, coastal forts for coastal routes
- support equipment, trains, trucks, and infantry equipment costs and rewards
- dynamic national spirit upgrades
- decision and mission unlocks
- advisors, council leaders, and route-specific high command
- laws and occupation law changes
- claims and war goals through decisions, not raw focus dumps
- state integration projects
- defensive unit templates and limited unit spawns
- research bonuses for industry, construction, logistics, doctrine, and encryption or intelligence
- foreign aid and recognition actions
- faction or League mechanics
- super-event triggers only for late regional outcomes

Avoid:

- repeated political power rewards
- repeated small stability rewards
- one new idea for every focus
- war goals directly granted without Need logic
- cores directly granted on large conquered regions
- generic `two infantry divisions` rewards without story and costs

## Focus AI route behavior

| AI context | Preferred route | Avoids | Notes |
| --- | --- | --- | --- |
| Democratic minor, stable | Living Humanism | Marked Bounds | prioritizes Consent and diplomacy |
| Communist or worker-heavy minor | Guild Commonwealth | Island Discipline if not threatened | prioritizes labor and solidarity |
| Subject minor | Common Store State or Living Humanism | early Marked Bounds | seeks autonomy through proof |
| Island minor | Island Discipline plus Common Stores | landlocked outlet branch | builds ports and coastal defenses |
| Landlocked minor | Common Store State plus Inland Island | naval content | seeks rail ring and port charter |
| Threatened by stronger neighbor | Island Discipline | slow diplomacy-only path | builds defense and household guard |
| High chaos authoritarian | Common Store State into Marked Bounds possible | peaceful League | only if Need high and targets are weak |
| Low stability | Common Store or Island Discipline | Guild if it worsens disputes | tries to stabilize first |
| AI near player major | Living Humanism or defense | claims against player | avoid suicidal player-facing wars |

AI should prefer survival and internal functioning before expansion. It should not take Need claims unless it can defend itself, has a plausible target, and Overreach is not already catastrophic.

