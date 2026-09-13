# Event 41 decisions, missions, and resolution specification

## Temporary decision category

The affected country receives one temporary category for the duration of the episode. The category should appear only while the country has an active Event 41 outbreak or a short unresolved recovery tail that still requires player action.

The category uses the least complex presentation that can communicate the crisis:

- one static category picture
- one Army Infection Pressure meter or staged bar
- one trend indicator
- one current operational posture line
- one short line naming the most important current driver
- map highlighting for the active military disease nodes
- three to five visible primary actions in the current phase
- no more than one active sector-rotation mission at a time

The category should not behave like a store. Each action should commit transport, medical stores, civilian capacity, formations, operational freedom, or time.

## Action phases

The category changes its visible actions by pressure and evolution state. Obsolete or irrelevant actions disappear.

### Localized response phase

The opening phase normally exposes:

- Rotate the Sickest Formations
- Establish Quarantine Camps
- Expand Field Hospitals
- Sanitize Camps and Supply
- Set Operational Posture

### Operational epidemic phase

When pressure rises or several nodes become active, the category normally exposes:

- the active rotation mission or a new rotation target
- Assign Medical Evacuation Priority
- Expand Field Hospitals
- Repair the Medical Corridor when needed
- Set Operational Posture

### Army crisis phase

At very high pressure, the category normally exposes:

- Isolate the Military District
- Emergency Medical Mobilization
- Abandon the Contaminated Sector when valid
- Repair or Secure the Medical Corridor
- Set Operational Posture

Under Evolution I and Evolution II, international or civilian-protection actions can replace one of these slots when they become relevant. The category should never show every possible response at once.

## Decision family: Rotate the Sickest Formations

### Purpose

This is the main operational containment action. The country pulls the most affected formations away from active combat, disperses them into supplied rear areas, and replaces them with fresh units when possible.

### Availability

The action becomes available when the event can prove:

- at least one active infected sector
- affected formations that can be withdrawn or rested
- a valid rear-area destination or an in-place rest alternative
- no existing rotation mission

### Costs and requirements

The action should use a dynamic combination of up to four cost types:

- temporary commitment of affected formations
- command attention or a conservative command power amount
- trains or motorized equipment when movement is required
- short-term loss of front coverage or planning

The formation commitment and front weakness are the main price. Political power should not be the primary cost.

### Mission structure

Starting the action creates one timed goal mission tied to a named infected sector and a named safe rear area or in-place recovery zone.

The player must hold the required condition for a sustained period, normally around thirty to forty-five days inside a wider mission window:

- the selected affected formations or their event proxy are out of active combat
- the formations remain supplied
- the medical corridor remains open when one is required
- the sector does not receive a new major concentration of infected troops

The mission should auto-complete when the conditions are maintained. It should not ask for another payment click.

### Success

Success should:

- move a meaningful share of active sick manpower into recovery
- lower spread inside the selected node
- reduce pressure over more than one pulse
- improve the effectiveness of field hospitals and sanitation in that node
- give the rested formations temporary reinfection resistance

### Failure

Failure should follow a concrete operational breakdown such as returning the formations to combat too early, losing the corridor, or allowing the recovery area to become unsupplied.

Failure should:

- create a moderate pressure rise
- delay recovery
- increase medical overload
- prevent immediate reuse of the same mission

The failure should not create deaths by itself. Deaths arise from the worsened medical conditions during later processing.

### Profile response

Camp-borne fever should respond very strongly to rotation and dispersal. Tropical disease should respond strongly but recover slowly. Enteric disease should respond only partly unless clean supply and sanitation also improve.

## Decision family: Establish Quarantine Camps

### Purpose

The army separates sick and exposed soldiers, restricts movement through the infected node, and creates guarded treatment areas.

### Costs

The action should use a dynamic package drawn from:

- support equipment
- temporary manpower assigned to guards and camp staff
- civilian factory commitment or consumer burden
- temporary movement and organization penalties in the node

The action may use three or four costs when the scale demands it. It must never hide an extra spendable cost in the effect.

### Effects

Quarantine should:

- reduce same-node transmission
- reduce exposure of newly arriving formations
- improve medical triage
- slow movement and reinforcement through the node
- slightly worsen organization in the short term

Quarantine should be less effective when the node is under active enemy attack, cut off, or already overwhelmed. It should be more effective when combined with rotation or sanitation.

### Risks

An overcrowded quarantine system can become another transmission center. At high pressure, using quarantine without field hospitals or supply should have diminishing returns and a small chance of a report that the camps are failing.

## Decision family: Expand Field Hospitals

### Purpose

The country increases the capacity to treat active cases, separates fatal cases from recoverable illness, and shortens the convalescent tail.

### Costs

The action should use a dynamic package drawn from:

- support equipment
- manpower committed to medical service
- civilian factory capacity
- army experience when the expansion represents rapid reorganization and training

The country should receive lower cost or stronger effect from existing field-hospital companies and medical technologies. It should not receive a free response merely because one division uses a field hospital.

### Effects

Field-hospital expansion should:

- reduce the fatal share of active cases
- speed movement from active sick to convalescent
- improve return-to-duty speed
- reduce medical overload
- make medical evacuation more effective

It should not sharply reduce transmission by itself. The country still needs sanitation, quarantine, supply, or rotation.

### Duration

The expansion should provide a temporary capacity state for several months. It can be renewed at higher cost if the episode persists. It should not become a permanent national bonus from repeated clicks.

## Decision family: Sanitize Camps and Supply

### Purpose

The army cleans water and food systems, launders and replaces bedding, controls lice and insects, inspects kitchens, separates hospital wards, and replaces contaminated camp stocks.

### Costs

The action should use a dynamic package drawn from:

- support equipment
- infantry equipment only when clothing and camp stores are represented through the shared stockpile and the cost remains sensible
- motorized equipment or fuel for distribution
- civilian factory commitment

The action should normally use two or three spendable costs.

### Effects

Sanitation should:

- reduce new exposure
- lower same-node spread
- reduce the environmental component of pressure
- improve quarantine effectiveness
- reduce civilian spillover risk under Evolution II

Its effect should depend on profile and supply access. Enteric and camp-borne profiles respond quickly. Tropical disease responds when the action includes vector control and medicine distribution.

### Blocked state

The action should show a clear blocked reason when the army cannot deliver clean supplies to the selected node. The player should be directed toward corridor repair, local quarantine, or rotation instead.

## Decision family: Assign Medical Evacuation Priority

### Purpose

The army diverts trains, trucks, fuel, and route capacity to move sick soldiers from the front to treatment areas.

### Availability

The action appears when active sick manpower, pressure, or medical overload reaches a meaningful level and a valid route exists.

### Costs

The action should use up to four spendable costs:

- trains
- motorized equipment
- fuel
- temporary logistics or supply penalty for military operations

Convoys may replace one transport cost for an overseas theater. The action must not require trains, trucks, fuel, and convoys together unless the route genuinely uses all of them and one cost is converted into a condition or consequence to keep the hard cost limit.

### Effects

Evacuation should:

- reduce the active sick population in the front node
- increase the convalescent pool in safer areas
- reduce mortality
- improve the effect of field hospitals
- reduce pressure after a short transport delay

The action should create an immediate logistical sacrifice. The front receives less transport capacity while the evacuation priority remains active.

### Failure conditions

A cut railway, lost port, encircled sector, or severe enemy air pressure can interrupt the route. The action should pause, downgrade, or fail with a clear report. It should not silently consume transport while giving no effect.

## Decision family: Repair the Medical Corridor

### Purpose

The country repairs or secures the specific route linking the infected sector to the treatment area.

This action appears only when a route problem is materially limiting rotation or evacuation.

### Requirements and costs

The action can require:

- control of named states or route nodes
- civilian factory commitment
- trains or motorized equipment
- temporary construction or repair capacity
- sufficient military presence when the route is threatened

State control and unit presence are requirements, not spendable costs.

### Effects

Successful repair should:

- restore evacuation and supply effectiveness
- reduce pressure indirectly
- improve sanitation delivery
- unlock or strengthen the rotation mission

The action should change real route or building conditions where the engine and owning systems support it. It should avoid a generic country modifier when a named damaged railway, infrastructure link, supply hub, or port can be used.

## Decision family: Emergency Medical Mobilization

### Purpose

This is a high-pressure measure that expands the response across the army and civilian economy for a limited period.

### Availability

It should appear only when pressure is very high, medical overload is severe, or several nodes are active.

### Costs

The action should combine up to four meaningful burdens:

- civilian factory capacity
- support equipment
- manpower committed to medical service
- stability or war support loss when the diversion is politically damaging

### Effects

Emergency mobilization should:

- raise medical and evacuation capacity sharply
- lower fatality risk
- shorten high-pressure recovery
- improve the next rotation or sanitation action

It should also create a real temporary national cost. The country gives up production or public confidence to keep the army alive.

### Limits

The action should be usable once per episode or carry a long cooldown. It must not become a repeatable conversion of factories into free manpower.

## Decision family: Isolate the Military District

### Purpose

At army-crisis pressure, the country can seal a large infected military area, restrict movement, and stop reinforcements from passing through it.

### Effects

The action should:

- sharply reduce transmission out of the district
- reduce reinforcement and movement through the district
- lower supply flexibility
- weaken the front if the district is strategically important
- create a strong pressure reduction after a delay when the isolation holds

### Validity

The action should require a coherent district and should not isolate the national capital or last viable supply route unless the situation has no safer option. AI should avoid it when isolation would cause immediate military collapse.

## Decision family: Abandon the Contaminated Sector

### Purpose

This is a desperate action for high pressure, a lost medical corridor, or Evolution II conditions. The army withdraws from an infected sector and leaves prepared positions, stores, and local access behind.

### Availability

The action appears only when:

- the selected sector is severely infected
- a viable withdrawal route exists
- the front can be redrawn
- the country controls a valid fallback area

### Effects

The action should:

- remove most active formations from the node
- sharply reduce military transmission in that sector
- reduce pressure after evacuation
- impose a large local military and political loss
- risk state loss, entrenchment loss, supply disruption, or enemy exploitation

This action should never be the routine optimal choice. It exists because War Plague can make one sector strategically toxic.

## Operational posture controls

The category should present one compact control for the current posture.

### Restrict offensive operations

The country commits to a defined restraint period. Affected formations receive stronger recovery and lower exposure. The front loses offensive capacity, planning, movement flexibility, or attack efficiency.

The posture should be most effective when pressure is rising from combat. It should matter less when the main cause is unsafe water or a collapsed rear hospital network.

### Preserve ordinary operations

This neutral posture removes the special restraint and special risk. It should be available after the current commitment period ends.

### Fight through the outbreak

The country refuses medical restrictions and keeps the sector active. This stance is available only after acknowledging the risk through a confirmation or report.

It should:

- remove or avoid the restrictions attached to medical restraint
- increase exposure, medical overload, and fatality risk
- make rotation and quarantine less effective
- create an event report when pressure crosses a severe threshold during the stance

It should never create free combat power. It preserves operations at the cost of disease.

## Decision combinations

The system should reward complementary responses.

Useful combinations include:

- rotation plus field hospitals for rapid recovery
- quarantine plus sanitation for spread control
- evacuation plus field hospitals for mortality reduction
- corridor repair plus evacuation for isolated sectors
- offensive restriction plus rotation for a major pressure reversal
- sanitation plus Evolution II border controls for civilian protection

Repeated use of the same action should have diminishing returns. An army cannot solve a severe epidemic by clicking quarantine repeatedly while continuing full offensives and leaving supply ruined.

## AI use of decisions

AI behavior should be driven by the same visible crisis logic.

### Early pressure

The AI should prefer low-disruption containment such as sanitation, quarantine, and field-hospital expansion. It should use rotation when affected formations can leave the line without exposing a capital, major victory point, or collapsing front.

### Moderate pressure

The AI should combine one spread-control action with one recovery action. It should begin evacuation when medical overload is high and transport is available.

### High pressure

The AI should accept larger production and operational costs. It should isolate a district or restrict offensives when the expected military loss from disease exceeds the expected loss from temporary restraint.

### Desperate defense

An AI can fight through the outbreak when all of the following are broadly true:

- an enemy threatens the capital, a major encirclement, or immediate strategic defeat
- pressure is below the absolute crisis ceiling or no safe withdrawal exists
- the expected operational window is short
- the AI has enough manpower and medical capacity to survive the risk

The AI should stop the stance when the immediate danger passes or pressure reaches a hard danger threshold.

## Resolution conditions

An episode enters resolution when all of the following remain true for a sustained confirmation window:

- Army Infection Pressure is in the controlled band
- the active sick share is below the meaningful infection threshold
- no new formation or node has become infected recently
- the country has no unresolved rotation or evacuation failure
- active cross-border transmission checks are quiet when Evolution I is active
- civilian handoff risk is resolved or transferred cleanly when Evolution II is active

The confirmation window should normally last several weeks. This prevents one favorable pulse from ending the event while the army still carries a major burden.

## Gradual cleanup

Resolution removes penalties in stages.

1. New transmission stops.
2. Active infection modifiers downgrade to recovery modifiers.
3. Convalescent soldiers return in installments.
4. Temporary transport and production commitments end.
5. The category closes after the player no longer has meaningful actions.
6. The recent-survivor resistance state begins.

Formations should not jump from severe disease to full readiness in one day.

## Outcome tiers

### Exemplary field containment

This outcome requires low maximum pressure, limited military deaths, no foreign military spread, no civilian spillover, and a relatively short episode.

It should grant a temporary preparedness benefit that improves:

- future Event 41 opening resistance
- field sanitation
- medical response speed
- early warning for secondary outbreaks

The benefit should be useful but modest and temporary.

### Controlled at cost

This is the ordinary successful outcome. The country ends transmission but carries a convalescent tail and short medical strain. No special reward beyond recent-survivor resistance is required.

### Exhausted medical service

This outcome follows high pressure, prolonged overload, or substantial military deaths.

It should apply a longer temporary penalty to:

- manpower recovery
- reinforcement
- field-hospital efficiency
- support equipment demand

The penalty should fade or be shortened by completing recovery actions.

### Shattered infected front

This outcome follows the worst baseline failure, where the selected front approaches the intended half-strength danger band.

It should produce:

- a severe but temporary aftermath penalty
- a report marking the operational collapse
- a high convalescent burden
- long recent-survivor resistance after recovery
- a stronger foreign warning under Evolution I

The event remains recoverable. The outcome should not permanently cripple the country.

## Post-resolution follow-up

A country that contained the episode can receive one short follow-up report about field medicine, sanitation, lessons learned, or soldiers returning to duty. This report should not add another permanent system.

A country that suffered a severe outcome can receive a later report when medical services recover. This closes the aftermath and confirms that the penalties have ended.
