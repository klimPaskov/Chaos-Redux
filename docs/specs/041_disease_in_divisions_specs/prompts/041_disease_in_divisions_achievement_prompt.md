# Achievement implementation prompt for Event 41

Read the full Event 41 specification, the asset prompt, `AGENTS.md`, `chaos-redux-events`, and `chaos-redux-event-assets` before implementation.

Implement every achievement below with stable tracking, final localisation written from the direction, completed icon art, required variants, documentation, and cleanup. Inspect the repository's existing achievement definitions and runtime pattern first.

Do not unlock an achievement from the event firing alone. Use episode generation, historical maximums, completed actions, casualty accounting, spillover receipts, and disqualifier flags where the final state cannot prove the route.

## The Line Holds

- Key: `chaosx_41_the_line_holds`
- Visibility: visible
- Difficulty: hard
- Eligible country: any ordinary player-controlled primary target
- Required route:
  - contain the episode while still at war
  - maximum pressure remains below the operational epidemic band
  - no state in the original infected sector is lost during the episode
  - no secondary national outbreak is sourced from the player
  - military disease deaths remain below a population-scaled ceiling
  - complete a rotation mission
  - complete sanitation or quarantine
- Disqualifiers:
  - Fight Through the Outbreak used
  - civilian spillover from the player episode
  - capitulation or annexation
  - force-setting cancellation
- Title direction: disciplined defense under medical pressure
- Description direction: hold the infected sector and contain disease before it becomes an operational epidemic
- Icon direction: field medic symbol or satchel before an intact trench line

## Every Soldier Accounted For

- Key: `chaosx_41_every_soldier_accounted_for`
- Visibility: visible
- Difficulty: very hard
- Eligible country: any ordinary player-controlled country
- Required route:
  - pressure reaches the operational epidemic band
  - episode resolves
  - a very high share of recorded sick and convalescent manpower returns to duty
  - fatalities remain below a strict fraction of recorded cases
  - field-hospital expansion and medical evacuation are used
  - the manpower ledger closes without an unexplained remainder
- Disqualifiers:
  - emergency write-off of sick manpower
  - capitulation
  - force-setting cancellation
- Title direction: careful recovery and medical accountability
- Description direction: return almost every recoverable soldier after a severe epidemic
- Icon direction: returning soldiers passing a field hospital ledger or medical tag

## Quarantine the Coalition

- Key: `chaosx_41_quarantine_the_coalition`
- Visibility: visible
- Difficulty: very hard
- Eligible country: player-controlled faction member with an Evolution I outbreak
- Required route:
  - at least one valid allied exposure route exists
  - every exposed ally avoids a full secondary national outbreak
  - coalition camp separation and medical report exchange are used
  - the faction and ordinary military access relationship survive resolution
  - the source outbreak resolves
- Disqualifiers:
  - leaving or dissolving the faction to remove the route
  - civilian spillover
  - prolonged punitive access closure beyond the emergency window
  - force-setting cancellation
- Title direction: coalition discipline and shared containment
- Description direction: keep shared camps from carrying an evolved military epidemic into another member
- Icon direction: three military tents separated by medical barriers beneath a shared coalition motif

## War Without Plague

- Key: `chaosx_41_war_without_plague`
- Visibility: hidden until Evolution II has appeared in the campaign
- Difficulty: extreme
- Eligible country: player-controlled primary source under War Plague
- Required route:
  - at least one valid civilian spillover route exists
  - the war continues for a substantial period after Evolution II activates
  - no civilian spillover request sourced from the player's military nodes becomes a civilian outbreak
  - no distant military outbreak is sourced from the player's ports or demobilization route
  - protect civilian transport hubs
  - use controlled demobilization when the war ends during the episode
  - screen or close an infected port when one is involved
  - resolve the military episode
  - keep pressure below the army-crisis ceiling after Evolution II activation
- Disqualifiers:
  - any accepted civilian spillover receipt sourced from the player episode
  - becoming a special Chaos country
  - force-setting cancellation
- Title direction: preserve civilian society while fighting through the War Plague era
- Description direction: contain the evolved epidemic inside the armed forces despite real routes into society
- Icon direction: military train stopped before a guarded civilian station for medical inspection

## Tracking contract

Track at least:

- episode and generation IDs
- primary target status
- maximum pressure
- original infected sector
- relevant state losses
- actions and missions completed
- posture use
- military disease cases
- convalescent returns
- military disease deaths
- linked secondary national outbreaks
- exposed allies
- civilian spillover requests and accepted receipts by source
- distant military transmissions by source
- faction and access continuity
- capitulation, annexation, special-country, and force-setting disqualifiers

Clear temporary tracking when an episode ends. Preserve only the permanent achievement completion state and any campaign-level reveal state required by the achievement UI.

Use the asset prompt for all icons. Match final achievement wording to the implemented rules. Do not expose hidden future evolution conditions in visible descriptions before the content is eligible.
