# Event 31 Random Terror specification

## Part 12: Achievement package

## Achievement design rules

Event 31 achievements should reward mastery of pressure, legitimacy, territorial war, cross-border networks, the manual scenario, actor play, and the world-end branch.

An achievement must require deliberate play.

It should not unlock from the first event popup, a passive threshold, a debug trigger, or a scenario setup before the player acts.

Each achievement needs:

- a stable internal ID
- public title direction or working label
- public description direction
- eligible countries
- exact unlock conditions
- disqualifiers
- persistent tracking
- difficulty rating
- visible or hidden status
- completed, grey, and not-eligible icon variants
- documentation and catalog coverage where relevant

The working labels below are not final localisation.

## 1. No Second Blast

- Proposed ID: `031_no_second_blast`
- Working label: No Second Blast
- Eligibility: any ordinary government affected by Event 31
- Difficulty: hard
- Visibility: visible

### Unlock

Begin with at least `60` Terror Pressure and at least three active states.

Clear every active state and reduce Terror Pressure to zero within `180` days.

During the run:

- no new state becomes active
- no territorial actor forms
- no government-caused civilian death is recorded
- no abusive failure occurs

### Disqualifiers

- force-trigger or debug bypass
- Global Jihad scenario setup
- changing away from the tracked country
- a new Event 31 firing that replaces the tracked crisis conditions

### Why it is difficult

The player must combine protection, intelligence, precise operations, and recovery under a deadline.

### Icon direction

A guarded city skyline behind one extinguished fuse or shattered detonator symbol, with no real device detail.

## 2. The Long Watch

- Proposed ID: `031_the_long_watch`
- Working label: The Long Watch
- Eligibility: any ordinary government
- Difficulty: hard
- Visibility: visible

### Unlock

Experience five separate automatic Event 31 firings in the same country.

Clear every crisis without:

- losing a state to an Event 31 actor
- suffering a successful coup
- dropping Response Legitimacy below `50`

The country must end the fifth crisis at zero Terror Pressure.

### Disqualifiers

- manual scenario launch
- force-triggered Event 31 firing
- tag switch away from the country

### Why it is difficult

The player must manage recurrence over a long campaign and cannot rely on one extreme coercive response.

### Icon direction

A period watchtower or guarded station with five marked lamps and a calm city below.

## 3. The City Still Stands

- Proposed ID: `031_the_city_still_stands`
- Working label: The City Still Stands
- Eligibility: any government with an active capital-seizure mission
- Difficulty: medium to hard
- Visibility: visible

### Unlock

Prevent Capital Seizure while:

- Terror Pressure is at least `80`
- the country is already at war
- at least one non-capital state is Armed Insurgency or worse

Hold the capital through the mission and lower pressure below `60` within the following recovery window.

### Disqualifiers

- moving the capital through a debug or unrelated forced effect during the mission
- scenario setup that begins after the capital mission already counts as complete

### Icon direction

A fortified government building with intact lights behind damaged streets.

## 4. Cut Every Route

- Proposed ID: `031_cut_every_route`
- Working label: Cut Every Route
- Eligibility: any ordinary government or coalition leader
- Difficulty: hard
- Visibility: visible

### Unlock

During one connected transnational crisis:

- break at least three distinct cross-border corridors
- expose or neutralize one sponsor
- eliminate one safe haven
- reduce Network Reach by at least one major stage
- clear every domestic Event 31 state

### Disqualifiers

- corridors created and destroyed through repeated launch exploitation
- the network disappearing because every actor was removed by an unrelated terminal event before the player completes the objectives

### Icon direction

Three broken transport lines converging on a sealed border gate.

## 5. The False Claim Rejected

- Proposed ID: `031_the_false_claim_rejected`
- Working label: The False Claim Rejected
- Eligibility: an ordinary Muslim-majority government identified through the event-local reaction registry
- Difficulty: hard
- Visibility: visible

### Unlock

After Evolution IV:

- publicly reject the fictional jihadist movement through the eligible opposition chain
- maintain Response Legitimacy at `70` or above
- protect all threatened community and worship-site objectives
- defeat or force the surrender of the current Jihadist International faction leader
- remain independent

### Disqualifiers

- joining or materially sponsoring the jihadist faction
- using collective punishment
- losing the tracked government through takeover

### Why it is difficult

The player must combine military victory, civilian protection, and political resistance against an actor that prioritizes the country.

### Icon direction

A fictional council seal and protected city gate facing a broken false crown, with no sacred calligraphy.

## 6. No Collective Punishment

- Proposed ID: `031_no_collective_punishment`
- Working label: No Collective Punishment
- Eligibility: any ordinary government fighting an Event 31 territorial actor
- Difficulty: very hard
- Visibility: visible

### Unlock

Defeat or secure the full surrender of a territorial Event 31 actor while:

- Response Legitimacy never falls below `70` after the war begins
- no movement restriction exceeds its ordinary duration
- no abusive failure occurs
- no government atrocity or cover-up Condemnation source is recorded
- every recaptured state completes Restore Civil Authority

### Disqualifiers

- annexing the actor through an unrelated console or debug path
- tag switching

### Icon direction

A restrained sword beside an open relief gate and restored civic building.

## 7. The Enemy of My Enemy Is Still My Enemy

- Proposed ID: `031_enemy_of_my_enemy`
- Working label: The Enemy of My Enemy Is Still My Enemy
- Eligibility: any ordinary government or Event 31 actor
- Difficulty: hard
- Visibility: visible

### Unlock

Defeat both:

- one Event 31 territorial actor
- one Event 14 cannibal actor

The two hostile actors must have shared a border or contested the same state during the campaign.

The tracked country must never ally, join a faction with, send volunteers to, or sponsor either actor.

### Disqualifiers

- any formal cooperation with either actor
- one target disappearing through an unrelated cleanup before the player contributes materially to defeat

### Icon direction

Two broken hostile emblems separated by one defended civilian settlement.

## 8. Fracture from Within

- Proposed ID: `031_fracture_from_within`
- Working label: Fracture from Within
- Eligibility: a player-controlled Event 31 territorial actor
- Difficulty: very hard
- Visibility: hidden until the player controls an eligible actor

### Unlock

Enter the jihadist route after Evolution IV, then reject the dominant international leader and cause one of these outcomes:

- win the resulting leadership war
- split at least three member actors from the faction
- reduce International Unity below its lowest active stage

The player must remain independent at completion.

### Disqualifiers

- accepting subordination to the final command
- winning only because an unrelated world-end branch deletes the faction

### Icon direction

A fictional faction seal split through its center with three diverging banners.

## 9. Maximum Survivor

- Proposed ID: `031_maximum_survivor`
- Working label: Maximum Survivor
- Eligibility: the player country selected when Global Jihad launches at Maximum intensity
- Difficulty: extreme
- Visibility: visible

### Unlock

Launch Global Jihad at Maximum intensity, then:

- survive without changing player country
- preserve or restore the original capital
- clear domestic Terror Pressure
- defeat every Event 31 territorial actor or end them through valid surrender and cleanup
- prevent The False Revelation or defeat it if it fires

### Disqualifiers

- launch through debug bypass outside the scenario UI
- lower the selected intensity after confirmation
- tag switching
- an incomplete scenario ledger

### Icon direction

A battered national capital surrounded by cleared crisis markers and broken faction emblems.

## 10. The False Revelation Denied

- Proposed ID: `031_false_revelation_denied`
- Working label: The False Revelation Denied
- Eligibility: any country fighting the final state
- Difficulty: extreme
- Visibility: hidden until the world-end branch begins

### Unlock

After The False Revelation:

- contribute materially to recapturing at least one command capital
- help sever at least one strategic corridor
- restore at least one high-pressure country or defeat one major uprising
- participate in the final defeat or disappearance of the entity state
- survive the terminal campaign

### Disqualifiers

- joining or submitting to the final state
- changing player country
- final defeat occurring without the tracked contribution thresholds

### Icon direction

An ambiguous dark figure fading above a recaptured command hall at dawn, without sacred imagery.

## 11. Victims Before Victory

- Proposed ID: `031_victims_before_victory`
- Working label: Victims Before Victory
- Eligibility: any ordinary government with major Event 31 civilian losses
- Difficulty: hard
- Visibility: visible

### Unlock

Before completing the final defeat of the connected organization:

- run victim support in every affected state with major civilian losses
- restore every destroyed critical transport link
- maintain protected relief access during the territorial phase
- finish with Response Legitimacy at `80` or above

The player must then defeat or secure the surrender of the organization.

### Disqualifiers

- an affected state remains without completed recovery
- an abusive failure occurs after the support chain begins

### Icon direction

Relief workers opening a restored railway station while soldiers remain outside the civilian area.

## 12. War Without a Capital

- Proposed ID: `031_war_without_a_capital`
- Working label: War Without a Capital
- Eligibility: any ordinary government
- Difficulty: extreme
- Visibility: hidden until the capital is lost to Event 31

### Unlock

Lose the original capital to an Event 31 actor without capitulating.

Establish a valid backup capital, continue the war, retake the original capital, and restore civil authority there within one year.

The original government must survive and Terror Pressure must fall below `40` at completion.

### Disqualifiers

- losing the country through takeover
- retaking the capital through an unrelated scripted transfer
- changing player country

### Icon direction

A government seal carried from a dark temporary headquarters back to a restored capital skyline.

## Tracking requirements

The achievement system needs persistent tracking for:

- automatic versus manual firing
- player country at start
- tag-switch disqualification
- active crisis start date
- highest and lowest Response Legitimacy during the run
- government-caused civilian deaths
- abusive failures
- lost states and capital history
- corridor, sponsor, and safe-haven objectives
- Event 31 and Event 14 actor hostility and defeat contribution
- scenario type and intensity
- evolution and world-end state
- command-capital and corridor contribution
- recovery completion in each affected state
- force-trigger and debug disqualification

Tracking should use flags for boolean state and variables only for actual counts or thresholds.

Achievements must survive save and reload.

## Icon production

Every achievement needs one original completed icon designed for the achievement surface.

The grey and not-eligible variants follow the project achievement pipeline.

Achievement images cannot be resized focus or decision icons.

The icons should avoid real extremist symbols, graphic gore, sacred hostile branding, and readable generated text.

## Completion standard

The achievement package is complete only when:

- all `12` achievements have stable IDs
- unlock conditions and disqualifiers are implemented exactly
- manual and debug paths cannot grant automatic-play achievements
- tag switching is handled
- contribution achievements require real contribution
- hidden achievements reveal at the intended stage
- localisation and icon triplets exist
- tracking survives save and reload
- achievement docs and coverage tables match implementation
