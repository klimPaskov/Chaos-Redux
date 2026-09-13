# Event 41 AI, achievements, and replay specification

## AI design purpose

AI countries should treat Disease in Divisions as an operational problem. The AI must compare the expected military cost of medical restraint with the expected cost of allowing disease to grow.

Generic decision weights are insufficient. The AI should react to pressure, front importance, supply, enemy threat, medical capacity, transport, manpower, evolution state, and the current hidden disease profile.

## AI state model

The AI should derive one response posture from the current episode.

### Containment posture

The AI chooses containment when the front can tolerate temporary weakness, pressure is rising, or medical capacity is adequate to turn a short sacrifice into a fast recovery.

Typical actions:

- sanitation
- quarantine
- field hospitals
- rotation
- restricted offensives

### Balanced posture

The AI preserves part of the front while using one medical action and one spread-control action.

Typical actions:

- field hospitals plus sanitation
- evacuation without full offensive restriction
- corridor repair followed by rotation

### Emergency posture

The AI accepts major production and military costs because disease is threatening the front more than the enemy is.

Typical actions:

- emergency medical mobilization
- isolate military district
- large evacuation
- abandon contaminated sector when the front can be redrawn

### Desperate operations posture

The AI fights through the outbreak for a short strategic reason.

Valid reasons include:

- the capital is under immediate threat
- a major encirclement must be broken
- a short offensive can end the war
- no safe withdrawal or rear area exists

The AI should almost never use this posture for routine border fighting or while pressure is already at the army-crisis ceiling.

## AI country profiles

### Medical and logistics-rich major

This AI should respond early. It can afford hospitals, evacuation, and transport commitments. It should usually contain a baseline outbreak before army-crisis pressure.

### Undersupplied minor

This AI has fewer material options. It should prioritize sanitation, quarantine, local rest, and one corridor action. It should avoid spending all transport or support equipment when doing so would collapse the rest of the army.

### Aggressive major during an offensive

This AI can delay restraint at low pressure, but it should change course when pressure rises or the offensive loses momentum. It can use fight-through only for a bounded window.

### Defensive country near defeat

This AI should preserve critical fronts while using in-place hospitals, sanitation, and quarantine. It can accept higher pressure when withdrawal would expose the capital. It should seek emergency mobilization earlier.

### Country with several active fronts

This AI should isolate the infected sector from the rest of the army. It should avoid rotating sick formations through another active front.

### Overseas expeditionary power

This AI should assess ports, convoys, transport, and safe rear areas. It can choose local treatment when strategic evacuation would consume excessive sea capacity.

## AI decision scoring factors

### Rotation score rises with

- pressure above the localized stage
- several active formations in one node
- a valid supplied rear area
- strong replacement coverage
- camp-borne or tropical profile indicators
- a stable or secondary front

### Rotation score falls with

- capital or major victory point under immediate threat
- no safe route
- severe encirclement risk
- lack of replacement formations
- active mission already running

### Quarantine score rises with

- rapid same-node spread
- crowding
- reserve or allied formations entering the node
- camp-borne profile indicators
- sufficient support equipment and manpower

### Field-hospital score rises with

- medical overload
- high fatality risk
- large active sick pool
- long convalescent tail
- adequate civilian and support resources

### Sanitation score rises with

- enteric or camp-borne indicators
- damaged camp and water conditions
- good enough route access to deliver supplies
- high exposure with moderate medical burden

### Evacuation score rises with

- high active sick burden
- low local hospital capacity
- a valid transport route
- a safe rear area
- high mortality risk

### Offensive restriction score rises with

- pressure driven by combat
- stable defensive position
- enough reserve forces
- no immediate strategic deadline

### Fight-through score rises with

- immediate strategic danger
- chance to end the war quickly
- low or moderate pressure
- high manpower and medical reserves

### Fight-through score falls to near zero with

- army-crisis pressure
- high fatality trend
- civilian spillover risk
- no medical capacity
- no short strategic objective

## AI behavior under Evolution I

The source country should warn allies when relations and intelligence permit. It should separate expeditionary forces and common camps when the cost is lower than a second national outbreak.

Receiving allied countries should:

- inspect exposed formations
- establish early quarantine
- avoid moving exposed expeditionary units to another theater
- accept shared medical reports when relations are adequate

Enemy countries should receive weaker warning unless intelligence is strong or the outbreak is public. They should still respond when their own national episode begins.

AI should not exploit the disease by intentionally sending infected formations into allied territory. Military spread is a consequence, not a player-controlled biological weapon.

## AI behavior under Evolution II

AI countries should protect civilian hubs when spillover risk is high.

They should consider:

- closing military ports
- controlled demobilization
- separating troop and civilian transport
- restricting allied access
- isolating military districts
- international medical coordination

The AI should avoid closing its only viable supply port unless the disease threat clearly exceeds the military cost or a replacement route exists.

## Foreign AI response

Countries without a national outbreak can react when they have a valid exposure route.

### Allies

Allies should usually accept medical reports and screening. They can refuse costly restrictions when their front is collapsing or relations are poor.

### Enemies

Enemies can exploit a weakened infected front through ordinary military strategy. Event 41 should not grant a special attack bonus against diseased countries. The existing combat penalties create the opportunity.

### Neutral transit countries

Neutral countries can restrict military transit or port access when War Plague threatens their territory. Their response should depend on relations, faction pressure, trade dependence, and civilian vulnerability.

## AI safety rules

The AI must not:

- spend unavailable equipment or transport
- start a rotation mission without a valid destination
- abandon a sector with no fallback line
- close the only supply port without a severe reason
- isolate its capital district through an ordinary choice
- keep fight-through active after the strategic reason ends
- create repeated quarantine or hospital actions while the previous commitment remains active
- use a decision whose target country, state, route, or outbreak generation is invalid

## Achievement design

The achievements use working keys and working labels. Final player-facing titles and descriptions should be written during implementation from the directions below.

### Achievement 1: The Line Holds

- Working key: `chaosx_41_the_line_holds`
- Visibility: visible
- Difficulty: hard
- Eligible country: any ordinary player-controlled country that becomes the primary Event 41 target
- Required episode: baseline or Evolution I without civilian spillover
- Unlock conditions:
  - contain the outbreak while the country remains at war
  - keep maximum Army Infection Pressure below the operational epidemic band
  - lose no state in the originally infected sector from outbreak start to resolution
  - create no secondary national outbreak from the player's military
  - keep military disease deaths below a population-scaled ceiling
  - complete at least one rotation mission and one sanitation or quarantine action
- Disqualifiers:
  - use Fight Through the Outbreak
  - civilian spillover from the player's episode
  - annexation or capitulation during the episode
- Why it is not trivial: the player must weaken the active front, manage the sector, and contain the outbreak without giving the enemy the targeted ground
- Title direction: disciplined defense and medical control
- Description direction: hold the infected line while containing disease before it becomes an operational epidemic
- Icon direction: a field medic's armband or medical satchel in front of an intact trench line, with no national symbol

### Achievement 2: Every Soldier Accounted For

- Working key: `chaosx_41_every_soldier_accounted_for`
- Visibility: visible
- Difficulty: very hard
- Eligible country: any ordinary player-controlled country
- Required episode: pressure must reach the operational epidemic band
- Unlock conditions:
  - resolve the episode after pressure reaches a high threshold
  - return a very high share of all recorded sick and convalescent soldiers to duty
  - keep fatal cases below a strict fraction of total recorded cases
  - use field-hospital expansion and medical evacuation
  - finish with no unresolved ledger discrepancy
- Disqualifiers:
  - emergency cleanup that writes off an unknown sick remainder
  - capitulation
  - player-triggered cancellation of the event through force settings
- Why it is not trivial: the player must recover from a serious epidemic while preserving lives and proving the manpower ledger closes cleanly
- Title direction: careful medical accounting and return to duty
- Description direction: bring almost every recoverable soldier home from a severe field epidemic
- Icon direction: a returning column of soldiers passing a field hospital ledger or medical tag, using a simple readable silhouette

### Achievement 3: Quarantine the Coalition

- Working key: `chaosx_41_quarantine_the_coalition`
- Visibility: visible
- Difficulty: very hard
- Eligible country: a player-controlled faction member with an active Evolution I outbreak
- Required episode: at least one allied military exposure route must exist
- Unlock conditions:
  - prevent every exposed allied country from becoming a full secondary national outbreak
  - use coalition camp separation and medical report exchange
  - keep military access or faction membership intact through resolution
  - contain the player's outbreak without using a total military district abandonment
- Disqualifiers:
  - expel or leave the faction to remove the exposure route
  - civilian spillover
  - intentional access closure lasting beyond the accepted emergency window
- Why it is not trivial: the player must protect allies while preserving coalition function and absorbing the material cost of coordinated control
- Title direction: coalition discipline under infection pressure
- Description direction: contain an evolved military epidemic without letting shared camps infect another member
- Icon direction: three military tents separated by medical barriers beneath a shared faction-style emblem that does not copy a real flag

### Achievement 4: War Without Plague

- Working key: `chaosx_41_war_without_plague`
- Visibility: hidden until Evolution II has appeared in the campaign
- Difficulty: extreme
- Eligible country: a player-controlled primary source country under War Plague
- Required episode: Evolution II active and at least one valid civilian spillover route present
- Unlock conditions:
  - continue the war for a substantial period after War Plague becomes active
  - prevent every civilian spillover request from the player's military nodes from becoming a civilian outbreak
  - prevent distant military transmission from the player's ports and demobilization routes
  - resolve the military episode
  - keep pressure below the army-crisis ceiling after Evolution II activates
- Required actions:
  - protect civilian transport hubs
  - use controlled demobilization if the war ends during the episode
  - close or screen an infected military port when one is involved
- Disqualifiers:
  - any accepted civilian spillover receipt sourced from the player's episode
  - use of force settings to cancel the episode
  - becoming a special Chaos country
- Why it is not trivial: the player must keep fighting while managing the most dangerous evolution and protecting civilian systems
- Title direction: separation of military necessity from civilian catastrophe
- Description direction: contain War Plague inside the armed forces despite active routes into society
- Icon direction: a military train stopped before a guarded civilian station, with a medical inspection symbol and clear period styling

## Achievement tracking principles

Achievement tracking should use episode generation and one-shot flags. It should not infer success from a final state when the achievement depends on maximum pressure, actions taken, source relationships, casualties, or a disqualifying event that occurred earlier.

The implementation should track:

- primary target status
- maximum pressure reached
- original infected sector
- sector state losses
- outbreak generation
- linked secondary outbreaks
- civilian spillover receipts by source
- actions and missions completed
- fight-through use
- military disease cases, recoveries, and deaths
- faction and access continuity where required
- cancellation or force-trigger disqualifiers

## Replay variation

The event should feel different across campaigns through combinations of:

- hidden disease profile
- climate and terrain
- front importance
- supply and infrastructure
- army size and concentration
- medical technology
- transport access
- war stage
- evolution state
- faction and expeditionary relationships
- contamination, famine, displacement, bombing, and disasters

A repeated firing should not reuse the exact same sector and profile automatically. Recent local resistance, current world state, and previous failures should alter the next incident.

## Rare but grounded combinations

### Winter trench epidemic

A camp-borne profile strikes a static cold front. Rotation and sanitation are powerful, while crowding and shared shelters drive spread.

### Tropical campaign collapse

A tropical profile strikes an undersupplied jungle front. Recovery is slow, prophylaxis and transport matter, and the army can lose tempo without large early deaths.

### Bombed rail epidemic

An enteric profile strikes after bombardment destroys water and evacuation routes. Corridor repair becomes the key action.

### Coalition hospital chain

Evolution I spreads through shared hospitals and expeditionary forces. Early intelligence and separation can stop a second country from developing a full outbreak.

### Demobilization crisis

Evolution II activates near the end of a war. Returning soldiers and transport hubs create the main civilian spillover risk.

These combinations should emerge from world state. They do not require separate random-event identities.

## Balance review questions

Before implementation is accepted, the AI and balance review should answer:

- Can a prepared country contain a baseline episode with two complementary actions?
- Can an unprepared country survive without permanent ruin if it accepts a major operational sacrifice?
- Does the worst baseline failure affect one front more strongly than the whole army?
- Does field-hospital strength reduce mortality without solving transmission alone?
- Does evacuation reduce deaths while creating a visible logistics cost?
- Can the AI distinguish a threatened capital from an ordinary front?
- Can Evolution I spread internationally without infecting every country on the front?
- Can Evolution II create civilian risk without duplicating civilian outbreak deaths or Air Cleanliness?
- Are all achievements difficult through gameplay without depending on random AI failure?
