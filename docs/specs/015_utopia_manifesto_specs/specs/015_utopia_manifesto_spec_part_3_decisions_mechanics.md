# Event 015, `utopia_manifesto`, decisions, missions, GUI, and mechanics

## Design rule

The decision layer must make the country act. The player should not buy utopia with political power. Decisions and missions should ask the player to build stores, place divisions, hold ports, repair railways, send aid, manage labor petitions, arbitrate claims, and integrate occupied districts.

Every major decision family should use concrete resources, map objectives, or time pressure.

## Utopian Ledger decision category

Working category id: `utopia_manifesto_ledger_category`.

The category appears after the country accepts the manifesto. It stays visible while the Utopian tree is active. It should hide obsolete decisions by phase, route, geography, and target validity.

### Header content

The header should show:

- Need value and trend
- Consent value and trend
- Surplus value and trend
- Overreach value and trend
- Vocation Balance value and most severe shortage
- Foreign Suspicion value and warning status
- current interpretation route
- current geography mode
- current active project count

Long explanations should go in tooltips and scripted localisation. The visible header should be readable.

### Phase structure

| Phase | Unlock | Visible decisions |
| --- | --- | --- |
| Opening | event accepted | census, first storehouse, public reading, craft petitions, first observers |
| Stabilization | opening trunk complete | vocation balancing, storehouse projects, rural rotation, defensive drill |
| Interpretation | first route opener taken | route-specific decisions, focused storehouse upgrades, councils, assignments, guilds, wardens |
| External | diplomacy or needful land branch open | aid, observers, arbitration, claims, neighbor statuses |
| Integration | owns or occupies target states | common administration, local councils, supply projects, resistance handling |
| Late | route finisher or proclamation branch | League, New Utopia, Marked Bounds crisis, final reforms |

Decision visibility should keep the category curated. Human players should not see every possible target at once.

## Ledger values and dynamic movement

### Need

Need is the state pressure that justifies action. It should not be a simple timer.

Rises from:

- low civilian factories relative to owned states or population
- low infrastructure, rail, or supply in core states
- lack of port for landlocked countries after the island branch opens
- war, blockade, lost states, strategic bombing, occupied core land
- high Vocation imbalance in agriculture or useful arts
- refugees or population pressure from other event systems if available
- failed storehouse missions

Falls from:

- storehouse projects
- infrastructure, rail, ports, and supply hubs
- successful rural rotation
- surplus imports or aid
- peace
- stable vocation distribution
- integration projects that actually feed and administer new states

Need thresholds:

| Band | Gameplay meaning |
| --- | --- |
| 0 to 24 | experiment has room to be generous |
| 25 to 49 | ordinary reforms and mild claims become plausible |
| 50 to 74 | emergency decisions and border arbitration become available |
| 75 to 89 | strong claims and strict allocation unlock |
| 90 to 100 | crisis state, Marked Bounds pressure, shortage events |

### Consent

Consent measures public willingness to live under the experiment.

Rises from:

- public councils
- voluntary vocation choices
- successful relief
- low Overreach
- defensive victories
- peaceful integration
- elections or public votes where the route supports them

Falls from:

- forced vocation assignments
- repeated emergency allocation
- offensive wars without Need justification
- failed storehouse missions
- high casualties
- forced settlement
- suppression of councils

Consent thresholds should gate:

- peaceful League membership
- consent-based integration
- route elections
- reform exit from Marked Bounds
- stability of the six-hour ambition

### Surplus

Surplus is the ability to maintain stores and help others.

Rises from:

- civilian factories
- infrastructure and rail
- storehouse network
- stable useful arts and agriculture vocations
- convoys and ports for coastal states
- peace and trade

Falls from:

- war
- blockades
- aid shipments
- storehouse corruption
- overmilitarization
- low Vocation Balance

Surplus gates:

- foreign aid
- common reserves
- peaceful diplomacy
- New Utopia proclamation
- storehouse upgrades

### Overreach

Overreach is the cost of turning need into domination.

Rises from:

- forced settlement
- claims without proper Need
- war goals against weak neighbors
- mercenary or assassination-style indirect war decisions
- bypassing local councils
- harsh occupation
- ignoring failed arbitration and taking land anyway

Falls from:

- reparations
- renouncing claims
- local councils
- slow integration
- peace settlements
- aid to affected states
- public accountability focuses

Overreach gates:

- Marked Bounds route
- backlash events
- coalition reaction
- super-event tone
- achievement disqualifiers

### Vocation Balance

Vocation Balance is computed from the five vocation shares. It should reward matching citizen preference with public need.

The player should be able to nudge distribution, not command it freely without cost.

Main actions:

- honor petitions, raises Consent and may worsen shortages
- request urgent service, solves shortages and lowers Consent
- fund apprenticeship, costs civilian burden and time
- draft defense service, raises Defense share and war readiness, lowers useful arts and Consent if overused
- sponsor scholars, raises Learning and research, costs production or consumer goods

### Foreign Suspicion

Foreign Suspicion measures external reaction.

Rises from:

- claims
- Marked Bounds focuses
- large League growth
- indirect war methods
- mercenary hiring
- ideology export
- high Overreach

Falls from:

- observers
- aid
- defensive behavior
- diplomacy focuses
- low Overreach
- honoring arbitration outcomes

High Suspicion creates:

- foreign guarantees against targets
- hostile propaganda events
- sanctions or trade friction
- rival aid to neighbors
- anti-Utopian conference missions

## Decision family, household census and public reading

### Conduct the Household Census

Purpose: establish baseline values and name the country's first shortages.

Requirements:

- capital controlled
- not already completed
- small civilian factory burden or temporary consumer goods cost

Success:

- sets reliable Need and Surplus values
- reduces random early swings
- unlocks targeted storehouse projects

Failure or delay:

- if ignored for too long, Need estimates become unreliable and early decisions cost more

### Invite Public Readers

Purpose: build Consent and make the manifesto public.

Costs:

- stability risk if country is authoritarian or at war
- political capital can be a small part, but not the only cost
- time

Outcomes:

- raises Consent
- unlocks route opener focuses faster
- can create route-specific party shifts

AI:

- usually takes it unless at war and low stability

## Decision family, common stores

### Establish a Common Storehouse

Target: controlled core or integrated state.

Requirements:

- civilian factory burden
- infrastructure threshold or repair mission
- trains or trucks for inland states
- convoys for island or overseas states
- support equipment for administration

Effects:

- raises Surplus if completed
- lowers Need in the state region
- unlocks local integration or aid decisions
- can add a state modifier for supply and compliance

Failure:

- if state is occupied, bombed, or cut off during project, storehouse becomes delayed or damaged
- raises Need and lowers Consent

### Storehouse Audit

Purpose: prevent the Common Store route from being a free economy engine.

Requirements:

- storehouse network exists
- not on cooldown

Outcomes:

- successful audit reduces corruption and raises Surplus
- harsh audit raises bureaucracy burden and can lower Consent
- failed audit creates Storehouse Corruption spirit or modifier

### Open the Stores in a Crisis

Purpose: emergency relief.

Costs:

- Surplus
- civilian factory burden
- convoys or trains if state is not adjacent to capital

Effects:

- lowers Need sharply
- raises Consent if peaceful
- can hurt production or create temporary consumer goods burden

AI:

- use when Need high and Surplus adequate
- avoid if war emergency needs production unless Consent is near collapse

## Decision family, vocation accord

### Collect Craft Petitions

Purpose: learn what people want to do.

Outcomes:

- reveals preferred vocation distribution
- raises Consent slightly
- can reveal a shortage if preferences mismatch public need

### Fund Apprenticeships

Purpose: move workers gradually into needed trades.

Costs:

- civilian factory burden
- small equipment or industrial stockpile cost depending on vocation
- time

Effects:

- improves Vocation Balance
- raises relevant production, research, compliance, or defense outcomes

### Request Urgent Service

Purpose: solve a shortage quickly.

Costs and risks:

- Consent loss
- possible stability loss
- route-specific ideology friction

Effects:

- raises target vocation share quickly
- raises Overreach if repeated or used during peacetime

### Recognize a Second Trade

Purpose: allow flexible labor without coercion.

Requirements:

- focus unlock
- Consent threshold
- enough Surplus to support training time

Effects:

- lowers future assignment costs
- improves Vocation Balance recovery
- unlocks achievement path for balanced vocations

## Decision family, rural rotation and inland stores

### Begin Rural Rotation

Purpose: shared agriculture and supply resilience.

Requirements:

- owned core state with infrastructure below cap or rural state group
- manpower and trains or trucks
- no active occupation crisis in target

Effects:

- improves infrastructure or supply
- raises Agriculture share
- raises Consent if voluntary
- lowers production temporarily if overused

### Complete the Harvest Mission

Timed mission, 90 to 140 days.

Objective examples:

- keep target state supplied
- avoid enemy occupation
- maintain rail connection to capital
- hold enough manpower and trains

Success:

- Need decreases
- Surplus rises
- state receives temporary supply or compliance benefit

Failure:

- Need rises
- Consent falls
- storehouse costs increase

## Decision family, just war and defense

### Muster Household Guards

Requirements:

- infantry equipment
- manpower
- Defense vocation share or military focus unlock
- not on cooldown

Effects:

- creates limited defensive units scaled by states, population, equipment, and chaos tier
- increases Defense share
- raises Consent if at defensive war
- lowers Consent if used during peace with low Need

Template direction:

- small infantry or militia units
- low attack, better defense or entrenchment
- no free artillery unless paid

### Guard the Shore or Inland Ring

Timed mission, 120 to 180 days.

Objective examples:

- place supplied divisions in named coastal, port, river, pass, or capital states
- keep ports or supply hubs controlled
- maintain convoy or train stock

Success:

- defensive bonuses or state fortification
- lowers Foreign Suspicion if purely defensive

Failure:

- raises Need and Suspicion
- can unlock emergency defense decisions

### Declare a Just Cause Review

Purpose: before claims or war, the state reviews whether Need justifies escalation.

Requirements:

- target is valid and not stronger by a large margin
- Need threshold met
- no recent failed review unless chaos high

Outcomes:

- valid cause lowers Overreach cost of later pressure
- invalid cause blocks or penalizes war goals
- Marked Bounds can bypass, but gains Overreach

## Decision family, needful land and arbitration

### Open Boundary Arbitration

Target: neighboring minor or state owner.

Requirements:

- Need threshold
- target not a major or far stronger country unless the player is defending a lost core
- relation or diplomatic access path
- no active truce conflict with target

Costs:

- political capital can appear here, but include diplomatic credibility, civilian burden, and time
- Surplus can be spent to offer compensation

Timed mission, 120 to 180 days:

- maintain relations above a threshold
- keep Overreach below a threshold
- keep border demilitarized or avoid just-war violations
- optionally send aid or compensation

Outcomes:

- target accepts limited transfer or lease if friendly and weak
- target grants access, demilitarized zone, or port charter instead of land
- target refuses, opening claim escalation
- target calls for outside guarantees if Suspicion high

### Mark a Needed District

Target: neighboring state after arbitration failure or Marked Bounds unlock.

Requirements:

- Need high
- target state has low strategic value or matches implemented state-group logic
- target owner is valid
- not already marked

Effects:

- creates claim or mission chain
- raises Foreign Suspicion
- raises Overreach if Need proof is weak

### Settlement Charter

Purpose: peaceful incorporation or autonomy arrangement.

Requirements:

- successful arbitration or target occupied after war
- Surplus and Consent thresholds
- local compliance or support

Effects:

- creates claim, local autonomy, demilitarized arrangement, or integration project
- avoids instant cores

## Decision family, occupation and integration

### Establish Common Administration

Target: occupied or owned non-core state.

Requirements:

- controlled state
- resistance below a safe threshold or enough garrison strength
- support equipment, manpower, and civilian factory burden
- rail or port access

Effects:

- compliance gain or local support
- lowers resistance over time
- unlocks storehouse project

### Build the Local Store

Target: state under common administration.

Requirements:

- infrastructure or supply route
- civilian factories
- trains, trucks, or convoys
- Surplus

Success:

- local Need reduction
- compliance or local support
- progress toward integration

Failure:

- state modifier for shortages
- resistance increase
- Consent loss

### Convene Local Households

Peaceful route integration project.

Requirements:

- Consent high
- Overreach low
- local store exists
- resistance low
- timed mission complete

Effects:

- local support and integration progress
- eventual core after several projects
- no force if local rejection event triggers unless player chooses coercion

### Assign Boundary Wardens

Hardline integration project.

Requirements:

- Marked Bounds route or high Need emergency
- garrison strength and equipment

Effects:

- faster integration progress
- resistance and Overreach rise
- possible condemnation or foreign backlash if combined with destructive event systems

## Decision family, friends and neighbors

### Send Storehouse Aid

Target: minor country or League candidate.

Requirements:

- Surplus threshold
- convoys or trains depending on geography
- not target at war with the sender unless route supports aid corridor

Costs:

- equipment, support equipment, civilian burden, convoys, or trains

Effects:

- relation gain
- target Observed or Neighbor status
- lowers Foreign Suspicion if no claims are active
- can lower chaos slightly when stabilizing a crisis minor

### Send Magistrates

Target: Observed or Neighbor country.

Requirements:

- high Consent or Common Store route
- advisor capacity or bureaucracy value
- target accepts foreign civic help

Effects:

- influence and status upgrade
- target can gain small administrative spirit
- sender gains diplomatic legitimacy

Risks:

- ideology rivals accuse the Utopian country of exporting a state model
- high Overreach turns it into subversion and raises Suspicion

### Recognize a Friend

Purpose: formal friendly relationship without faction creation.

Requirements:

- two previous positive interactions
- low Overreach or shared ideology

Effects:

- Friend status
- mutual aid decisions
- future League eligibility

## Decision family, Utopian League

The League should be a late mechanic.

### Minimum requirements

- at least three Friends or two Friends plus one subject or puppet with high autonomy
- high Consent or high Surplus
- Foreign Suspicion under dangerous threshold unless route is hardline
- no ongoing Marked Bounds crisis unless forming the fear-based variant

### League values

If implemented, the League uses:

- Cohesion
- Shared Stores
- Member Confidence
- Sponsor Pressure or Foreign Suspicion

### League actions

- common reserves
- defensive aid missions
- arbitration congress
- member storehouse project
- emergency convoy
- expulsion or suspension for members at war against League principles
- League proclamation focus

AI must have equivalent actions without needing a human-only GUI.

## Decision family, Marked Bounds crisis

Marked Bounds should create a living crisis, not only give claims.

### Crisis values

Use Overreach, Consent, Foreign Suspicion, and local resistance. A separate `bounds_backlash` value can exist if useful.

### Decisions

- mark district by need
- enforce settlement register
- suppress local refusal
- invite observers to reduce suspicion
- pay reparations after abuses
- renounce an excessive claim
- redirect settlers to underused home states
- call boundary congress

### Crisis missions

| Mission | Duration | Objective | Success | Failure |
| --- | --- | --- | --- | --- |
| Boundary Congress | 120 days | keep Overreach under threshold and relations with target stable | claim becomes settlement charter | target gains guarantees or rejects publicly |
| Store the New District | 180 days | build or repair local infrastructure and supply | lowers resistance and unlocks integration | raises Need and resistance |
| Prevent the Empty Houses | 150 days | keep garrisons disciplined and local support above threshold | Overreach lowers | backlash event and Consent loss |
| Renunciation Vote | 120 days | high Consent and no active offensive war | closes some hardline content and lowers Overreach | hardliners gain route pressure |

## Scripted GUI design

The Utopian Ledger deserves a compact scripted GUI because the player manages multiple values, vocation shares, target statuses, and integration projects.

### Window role

Working GUI label: `utopia_ledger_window`, not final localisation.

Entry point:

- button in Utopian Ledger decision category
- optional focus completion opens it automatically once

The GUI should not replace decisions. It should make decisions readable and call the same scripted effects and triggers that decision buttons use.

### Layout

| Area | Content | Notes |
| --- | --- | --- |
| Header | country name, interpretation route, geography mode | dynamic localisation |
| Main meters | Need, Consent, Surplus, Overreach, Suspicion | coloured values and trend arrows |
| Vocation wheel or row | five vocation shares and shortage warning | no exact pie needed if GUI limits make bars easier |
| Project cards | active storehouse, integration, arbitration, defense missions | show timer and target state or country |
| Neighbor list | Observed, Neighbor, Friend, League Member targets | show only selected or top priority targets |
| Action buttons | open matching decisions or perform GUI action equivalent | all buttons need costs and blocked tooltips |
| Warning panel | high Need, high Overreach, foreign backlash, vocation shortage | animated warning if assets exist |

### GUI button families

- open census detail
- focus a vocation shortage
- open selected target decisions
- pin or unpin target country
- open integration project for selected state
- call arbitration congress
- open League board after unlock

Every GUI action needs AI equivalent through decisions or periodic scripted effects. The AI should not depend on the GUI.

### Cleanup

The GUI must close or hide invalid cards when:

- target country dies
- state is lost
- route changes
- country stops using Utopian tree
- country is annexed
- subject status changes invalid branch
- League member leaves or dies
- event is disabled before acceptance in testing

## Animated presentation plan

Animation should clarify state changes and warnings. It should not decorate every button.

### Planned animated sprites

| Working sprite | Surface | Size direction | State logic | Loop | Static fallback |
| --- | --- | --- | --- | --- | --- |
| `GFX_utopia_ledger_seal_animated` | Ledger header or category seal | 64x64 or existing category seal size | glows softly when category has an available important action | 8 frames, slow loop | `GFX_utopia_ledger_seal` |
| `GFX_utopia_overreach_warning_animated` | warning panel | 64x64 or panel icon size | pulses when Overreach is high | 8 frames, warning loop | `GFX_utopia_overreach_warning` |
| `GFX_utopia_storehouse_fill_animated` | storehouse project card | small horizontal strip or 64x16 | shimmer while a storehouse mission is active | 6 to 8 frames | `GFX_utopia_storehouse_fill` |
| `GFX_utopia_new_utopia_seal_animated` | late proclamation focus or decision | 94x86 focus icon companion or 96x96 GUI seal | appears when proclamation is available | 10 frames | `GFX_utopia_new_utopia_seal` |
| `GFX_utopia_marked_bounds_seal_animated` | hidden route warning | 94x86 or 96x96 | appears only on Marked Bounds route | 10 frames | `GFX_utopia_marked_bounds_seal` |

All animated assets must follow frame-sheet rules, real source frames, static fallbacks, contact sheets, preview GIFs for review only, and `.gfx` handoff notes.

### Static presentation cases

Do not animate every focus icon. Ordinary focus icons, idea icons, and decision icons should be static unless the asset prompt explicitly routes a special late-route seal or GUI warning.

## Mission quality table

| Mission family | Owner | Category | Region or target | Requirement | Duration band | Success | Failure | Duplicate risk control |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Harvest Rotation | Utopian country | Ledger | rural or supply-poor core state | keep rail or supply connection, pay trains or manpower | 90 to 140 days | Need falls, Surplus rises | Need rises, Consent falls | only one per region at a time |
| Storehouse Build | Utopian country | Ledger | core, owned, or occupied state | factories, support equipment, access | 120 to 180 days | local store, integration progress | damaged store, higher cost | active cap of 2 early, 4 late |
| Household Guard | Utopian country | Ledger or defense | capital and border states | supplied divisions placed or equipment paid | 90 to 120 days | defensive unit or modifier | Need and Suspicion rise | one active defensive region |
| Boundary Arbitration | Utopian country and target | Needful Land | neighboring country or state | relations, Need proof, compensation | 120 to 180 days | settlement or status | claim escalation or target guarantee | one target at a time for humans |
| Local Households | Utopian country | Integration | occupied state | compliance, storehouse, low resistance | 150 to 220 days | core progress | resistance and overreach | state flag blocks repeats |
| League Aid Corridor | Utopian country | Diplomacy | Friend or League target | convoys, equipment, access | 120 to 180 days | Friend confidence, Surplus use | lost aid and suspicion | target cooldown |
| Renunciation Vote | Utopian country | Marked Bounds | home politics | high Consent, low war pressure | 120 days | Overreach reduction | hardliner pressure | one-time or long cooldown |

## Cost model

Use a varied cost palette. Recommended cost families:

| Action | Primary costs | Secondary risks |
| --- | --- | --- |
| Census | civilian burden, time | stability if authoritarian crackdowns occur |
| Storehouse | civilian factories, support equipment, trains or convoys | production delay |
| Vocation training | civilian burden, industrial output, time | shortage in another vocation |
| Urgent assignment | Consent and stability | Overreach if repeated |
| Rural rotation | manpower, trains or trucks | production slowdown |
| Household guard | infantry equipment, manpower, army XP | economy strain |
| Mercenaries | Treasury Abroad, convoys, equipment, diplomatic credibility | Foreign Suspicion |
| Aid shipments | Surplus, convoys, support equipment, trucks | domestic Need if overused |
| Arbitration | Surplus, diplomatic credibility, time | failure opens backlash |
| Integration | support equipment, manpower, factories, compliance, supply | resistance and Overreach |
| Marked Bounds | army readiness, garrisons, stability, Overreach | coalitions and unrest |

Command power should be conservative and never above 60 for a decision.

## Localisation handoff for decision text

Decision text should describe public actions, not hidden mechanics. Use dynamic placeholders for:

- target state name
- target country name
- current Need band
- current shortage vocation
- current Overreach warning
- cost summary
- project timer
- relationship status

Avoid long raw triggers. Use custom trigger tooltips for:

- state requirements
- project caps
- relationship status
- Need threshold
- route lock
- missing convoys, trains, support equipment, or divisions

Blocked cost localisation should be icon-first where possible.

## AI decision behavior

AI should act by current values:

| Situation | AI behavior |
| --- | --- |
| Need high, Surplus high | build stores, open stores, send fewer external aid shipments |
| Need high, Surplus low | prioritize storehouse and rural rotation, avoid League aid |
| Consent low | avoid forced assignments unless at war, take public reading and councils |
| Overreach high | stop claims, pursue reparations or renunciation if not hardline |
| Foreign Suspicion high | invite observers, pause claims, strengthen defense |
| Vocation shortage | fund apprenticeships first, urgent service only during war or severe Need |
| At defensive war | muster guards, guard ports, prioritize Island Discipline focuses |
| At offensive war without Need | seek peace or avoid escalation if AI not Marked Bounds |
| Target country stronger | avoid Need claim unless target is already at war, weak, or allied support exists |
| League member threatened | send aid if Surplus and convoys permit |

AI invalidity blockers:

- do not target dead countries
- do not target majors for Need claims under ordinary logic
- do not target states impossible to reach or integrate
- do not form League with dead or puppet-invalid members
- do not keep integration missions active after state loss
- do not keep subject autonomy focuses after independence unless branch adapts

## Route-specific decision upgrades

| Route | Decision upgrades |
| --- | --- |
| Living Humanism | cheaper consent integration, better observer missions, stronger arbitration, no forced settlement bonuses |
| Common Store State | stronger storehouse and emergency allocation, higher bureaucracy risk, better Surplus aid |
| Guild Commonwealth | stronger apprenticeship, scholar, and craft militia decisions, more labor faction events |
| Island Discipline | stronger defensive missions, household guard, port and rail ring actions, slower peaceful diplomacy |
| Marked Bounds | stronger claims and hard integration, much higher Overreach and resistance |

## Event follow-ups from decisions

Use follow-up popups sparingly. Good follow-up moments:

- first successful storehouse
- first arbitration success or failure
- first forced assignment backlash
- first local household integration
- League foundation
- first Marked Bounds backlash
- New Utopia proclamation
- reform exit from Marked Bounds

These follow-ups should avoid listing modifiers. They should describe public consequences and route meaning.

