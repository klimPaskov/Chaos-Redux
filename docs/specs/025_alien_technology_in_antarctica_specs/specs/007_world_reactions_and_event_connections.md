# World reactions and event connections

## Reaction model

The world reacts to what it can observe.

A secret failed sabotage attempt, an unexplained missing convoy, an armed clash witnessed by several countries, and a public winner announcement should not use the same diplomatic result.

Event 025 tracks three evidence states for hostile incidents:

1. hidden
2. suspected
3. attributed

Only attributed incidents identify a responsible country publicly. Suspected incidents may create targeted opinion pressure and intelligence activity without declaring guilt as fact.

## Baseline public reactions

All valid country scopes that receive global event presentation receive the opening super-event and the winner announcement.

Participant countries receive additional reports for:

- first departure
- first functioning outpost
- first verified fragment
- first public hostile incident
- final recovery attempt
- winner resolution

Observer countries should not receive every expedition setback. Public report frequency must remain bounded.

## Opinion and tension

Baseline participation does not create world tension.

Public actions may create small and scaled tension changes:

- publicly arming an expedition
- blockading a rival route
- seizing an outpost
- firing on a rival ship or aircraft
- capturing foreign personnel
- refusing a negotiated evacuation after a clash

Research, surveying, rescue, signal study, fragment recovery, and ordinary defensive escorts do not add tension by default.

Opinion modifiers should distinguish:

- scientific cooperation
- expedition rescue
- data sharing
- suspected interference
- exposed sabotage
- seizure of material
- armed Antarctic incident
- transfer of alien custody

Modifiers need clear durations and cleanup. Avoid permanent opinion penalties for one small covert action.

## Diplomatic incident ladder

### Level 0: Competition

Ordinary rivalry, false information, defensive security, and private accusations.

Consequences stay inside expedition values and small bilateral opinion changes.

### Level 1: Public accusation

A participant presents evidence of theft, sabotage, or route interference.

Possible responses:

- deny involvement
- offer inspection
- compensate the target
- counter-accuse
- admit a limited operation

### Level 2: Detention or seizure

Personnel, fragments, or an outpost have been captured.

Possible responses:

- exchange prisoners
- return fragments
- accept arbitration
- reinforce the expedition
- impose a bilateral response

### Level 3: Armed clash

Ships, aircraft, or outposts exchange fire.

Consequences:

- world tension increase scaled to losses and publicity
- larger opinion penalties
- military access and convoy-route effects when supported
- pressure to demilitarise or withdraw
- Evolution III progress when enabled

An armed clash does not automatically create a war. War remains possible only through ordinary diplomacy or a later explicit escalation event with valid actors and strong gates.

## Rescue and cooperation

Cooperative actions provide real counterplay to pure sabotage.

A country may:

- rescue a stranded rival crew
- share weather observations
- permit emergency staging
- exchange survey data
- coordinate a temporary search sector
- establish a neutral medical station
- negotiate a fragment exchange

Cooperation should help without erasing competition. Shared data raises both countries' progress by a bounded amount, while the main recovery remains exclusive.

A rescue can create a debt marker used by later negotiations, reduce attribution pressure, or unlock an achievement.

## Antarctica and sovereignty

Baseline text should reflect competing access and claims without treating the later Antarctic Treaty as existing law.

The expedition occurs in a 1936-era campaign where national claims, naval access, weather stations, and wartime strategic concerns can matter. A late campaign may use language about negotiated scientific access, but it should not state that the 1959 treaty is already in force.

The event does not change state ownership or create Antarctic map states by itself.

## Shared Chaos Meter integration

Event 025 can affect shared systems through actual consequences.

### Chaos

The major event itself does not need a large direct Chaos grant merely for firing.

Chaos changes should come from concrete escalation:

- public armed clashes
- expedition deaths at meaningful scale
- alien-system accidents
- high Dependence failures
- transfer crises

Peaceful cooperation, safe containment, and negotiated withdrawal may reduce a small amount of event-created pressure when the shared system supports a matching history entry.

### Deaths

Actual casualties use the shared Deaths API.

### Air Cleanliness

Baseline expedition activity does not change Air Cleanliness.

A later alien-system accident changes Air Cleanliness only when the accident creates verified atmospheric contamination and can use a shared contamination adapter. Do not invent generic pollution values for every wreck incident.

### Condemnation

Ordinary sabotage and armed competition use opinion and tension, not the unconventional-warfare Condemnation ledger.

Condemnation is appropriate only when an Event 025 branch produces a source already covered by that system, such as an exposed atrocity, prohibited unconventional weapon use, or a serious cover-up. The current event spec does not add such a source by default.

### World threat

Event 025 does not set `world_in_threat` or register a world-threat source.

Evolution V dependence remains a national risk unless a later accepted event creates an existential actor or terminal route.

## Event 016 Brilliant Scientist

Event 016 owns the custom technology system.

Event 025 integration rules:

- call Event 016 external-grant helpers
- never create Kruger ownership
- never add Warren Kruger as a scientist, advisor, leader, or event target
- never create Event 016 project history
- never add Event 016 evolution records
- never increase Event 016 host Mandate, Dependence, Exposure, or Project Capacity
- never create the Kruger State
- never fire Strategic Singularity
- never grant free custom formations or equipment outside the Event 016 helper's normal consumer rebuild

A country that already hosts Kruger can still enter the race. Its scientists may interpret recovered systems faster, which can affect Logistics Readiness, signal analysis, or reward selection. The public event still attributes the result to the craft.

A Kruger State participant uses its own scientific identity and AI behavior. It receives no guaranteed win.

## Event 036 Alien Spacecraft

Event 036 is the closest direct connection.

The two events share a country-level and global alien-recovery ledger.

Event 025 represents a difficult international search for a crashed object in Antarctica. Event 036 represents a separate spacecraft recovery that grants aircraft and production capability.

Connections:

- Event 025 winner status changes Event 036 report wording
- Event 036 ownership changes Event 025 reward arbitration
- an overlapping result becomes an upgraded outcome
- a country that has both incidents can unlock a combined achievement
- global repeated-recovery reports increase foreign suspicion and scientific competition
- neither event silently fires the other

Event 036 remains repeatable according to its own future rework. Event 025 remains one major race.

## Event 044 Space Race

Event 044 is currently unreworked. Event 025 should expose a narrow future hook without depending on it.

Possible hook after Event 044 implementation:

- recovered propulsion or materials provide bounded Space Race progress
- Event 044 participation changes foreign interest in the Antarctic winner
- a winner with advanced alien systems may unlock a different spaceflight route

Event 025 must remain complete when Event 044 is unavailable or disabled.

## Event 028 Asteroid Incoming

Event 028 is currently unreworked. The shared connection should be informational.

Possible future hook:

- alien sensors improve impact prediction
- asteroid fragments can be compared with Antarctic material
- false assumptions about extraterrestrial origin change report wording

Event 025 must not call Event 028 or grant its reward before Event 028 has an accepted rework.

## Event 052 Intel Leaked

Event 052 is currently unreworked.

A future leak can expose:

- participant coordinates
- sabotage records
- fragment ownership
- hidden alien research
- Evolution V concealment

Event 025 should centralize its hidden evidence and selected-target ledgers so a future leak adapter can read them. It should not create Event 052 state itself.

## Event 024 Video Game in Sweden

The Swedish war-game event may later provide a small planning advantage for military escort or logistics simulation.

This connection is optional and should remain flavor-scale. Event 024 cannot determine the Event 025 winner.

## Event 027 Doctrine Research

Alien Dependence can distort doctrine choices after Evolution V.

A future Event 027 rework may read that state and offer a strange doctrine breakthrough or a corrective path. Event 025 does not grant a complete ordinary doctrine.

## Event 011 Secret Alliance

Secret Alliance may affect sabotage coordination only after a future accepted integration pass.

Coalition members could share coordinates or coordinate interference. Event 025 must not expose coalition membership or duplicate Event 011 history.

## Natural Disasters

Ordinary Antarctic weather is part of Event 025's bounded expedition model.

Do not call Event 013 Natural Disasters for routine blizzards, sea ice, whiteouts, or crevasses. Event 013 remains owner of large disaster sequences.

A severe externally triggered Antarctic disaster can later call Event 013 through its public API if the caller supplies a valid target and all required proofs. Event 025 does not need that route for baseline completion.

## Multiplayer behavior

Each human country receives its own entry choice and Expedition Board.

Shared global facts:

- participant roster
- crash sectors
- evolution state
- fragment ownership
- winner
- public incidents

Country-specific facts:

- private survey certainty
- hidden coordinates
- selected rival
- sabotage authorship
- counterintelligence
- private signal interpretation
- Exposure Risk or Dependence

A human player should not see another participant's exact progress unless intelligence has exposed it. Rival cards use broad status bands and confidence markers.

Pause-sensitive popups should remain limited. The board, missions, and reports carry most participant updates.

## AI-only wars and annexations

When a participant is annexed, capitulates, or loses its expedition institutions:

- its active missions cancel
- its selected targets clear
- physical fragments may be abandoned, transferred to the occupier only through a valid recovery rule, or returned to the unclaimed pool
- its outpost becomes abandoned
- its temporary industrial commitments end

The occupier does not automatically inherit survey certainty or the right to win.

## Public history and Event Details

The History row records the global opening once.

Event Details should show:

- event premise
- current phase or resolved state
- active participant count
- winner when resolved
- broad public evolution milestones
- whether the main wreck remains unclaimed
- the current public severity of Antarctic competition

It should not show:

- exact secret coordinates
- hidden sabotage authors
- private progress values
- future evolution surprises
- internal Event 016 technology keys
- internal Event 036 arbitration flags

## Global news frequency

The event should normally create global presentation at these thresholds:

1. opening super-event
2. first confirmed wreck fragment or first functioning Antarctic outpost, one report only
3. first attributed armed clash, only if it happens
4. winner announcement
5. major Evolution V public exposure, only if it becomes public

Minor setbacks remain participant reports.

