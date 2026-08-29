# Event 31 Random Terror achievement implementation prompt

## Task

Implement the complete Event 31 achievement package from:

`docs/specs/031_random_terror_specs/031_random_terror_spec_part_12_achievements.md`

Read the full Event 31 specification, especially the government response, territorial country, Global Jihad, False Revelation, AI, asset, and acceptance parts.

Follow:

- `AGENTS.md`
- `chaos-redux-events`
- `chaos-redux-event-assets`
- `chaos-redux-subagents`
- current Chaos Redux achievement registry and documentation
- installed vanilla achievement definitions and assets

Use the single root Chaos Redux achievement registry under `common/achievements/`.

Do not create a separate achievement database or new `unique_id` file.

Use the full achievement IDs below as the runtime identity unless a verified collision requires a reported change.

## 1. `031_no_second_blast`

Working label: No Second Blast.

Eligible country:

Any ordinary government affected by Event 31.

Unlock conditions:

- tracked crisis begins with Terror Pressure at least `60`
- at least three active states exist
- every active state clears within `180` days
- Terror Pressure reaches zero
- no new state becomes active during the run
- no territorial actor forms
- no government-caused civilian death is recorded
- no abusive failure occurs

Disqualifiers:

- force-trigger or debug bypass
- Global Jihad setup
- tag switch
- tracked crisis invalidated by a replacement setup

Difficulty: hard.

Visibility: visible.

Icon direction:

A guarded city skyline behind one extinguished fuse or broken detonator symbol. Avoid device detail and real extremist imagery.

## 2. `031_the_long_watch`

Working label: The Long Watch.

Eligible country:

Any ordinary government.

Unlock conditions:

- experience five separate automatic Event 31 firings in the same country
- clear all five crises
- never lose a state to an Event 31 actor
- never suffer a successful coup
- Response Legitimacy never falls below `50`
- end the fifth crisis at zero Terror Pressure

Disqualifiers:

- manual scenario launch
- force-triggered firing
- tag switch

Difficulty: hard.

Visibility: visible.

Icon direction:

A period watchtower or guarded station with five marked lamps and a calm city below.

## 3. `031_the_city_still_stands`

Working label: The City Still Stands.

Eligible country:

Any government with an active capital-seizure mission.

Unlock conditions:

- Terror Pressure is at least `80`
- the country is already at war
- at least one non-capital state is Armed Insurgency or worse
- Prevent Capital Seizure succeeds
- pressure falls below `60` during the following recovery window

Disqualifiers:

- unrelated forced capital movement
- scenario setup that begins after the mission is already counted complete

Difficulty: medium to hard.

Visibility: visible.

Icon direction:

A fortified government building with intact lights behind damaged streets.

## 4. `031_cut_every_route`

Working label: Cut Every Route.

Eligible country:

Any ordinary government or recognized coalition leader.

Unlock conditions during one connected transnational crisis:

- break at least three distinct corridors
- expose or neutralize one sponsor
- eliminate one safe haven
- reduce Network Reach by at least one major stage
- clear every domestic Event 31 state

Disqualifiers:

- repeated scenario or launch exploitation
- all targets removed by an unrelated terminal cleanup before material player action

Difficulty: hard.

Visibility: visible.

Icon direction:

Three broken transport lines converging on a sealed border gate.

## 5. `031_the_false_claim_rejected`

Working label: The False Claim Rejected.

Eligible country:

An ordinary Muslim-majority government identified through the Event 31 reaction registry.

Unlock conditions after Evolution IV:

- complete the public rejection and opposition chain
- maintain Response Legitimacy at `70` or above
- protect every threatened community and worship-site objective
- defeat or force the surrender of the current Jihadist International faction leader
- remain independent

Disqualifiers:

- join or materially sponsor the jihadist faction
- use collective punishment
- lose the government through takeover

Difficulty: hard.

Visibility: visible.

Icon direction:

A fictional council seal and protected city gate facing a broken false crown. No sacred calligraphy.

## 6. `031_no_collective_punishment`

Working label: No Collective Punishment.

Eligible country:

Any ordinary government fighting an Event 31 territorial actor.

Unlock conditions:

- defeat or secure full surrender of the actor
- Response Legitimacy never falls below `70` after the war begins
- no movement restriction exceeds its ordinary duration
- no abusive failure occurs
- no government atrocity or cover-up Condemnation source is recorded
- every recaptured state completes Restore Civil Authority

Disqualifiers:

- unrelated forced annexation
- tag switch

Difficulty: very hard.

Visibility: visible.

Icon direction:

A restrained sword beside an open relief gate and restored civic building.

## 7. `031_enemy_of_my_enemy`

Working label: The Enemy of My Enemy Is Still My Enemy.

Eligible country:

Any ordinary government or Event 31 actor.

Unlock conditions:

- materially contribute to the defeat of one Event 31 territorial actor
- materially contribute to the defeat of one Event 14 cannibal actor
- the two targets shared a border or contested the same state
- the tracked country never allied, joined a faction with, sent volunteers to, or sponsored either actor

Disqualifiers:

- formal cooperation with either target
- target removed by unrelated cleanup before material contribution

Difficulty: hard.

Visibility: visible.

Icon direction:

Two broken hostile fictional emblems separated by one defended civilian settlement.

## 8. `031_fracture_from_within`

Working label: Fracture from Within.

Eligible country:

A player-controlled Event 31 territorial actor.

Unlock conditions:

- enter the jihadist route after Evolution IV
- reject the dominant international leader
- win the resulting leadership war, or split at least three members from the faction, or reduce International Unity below its lowest active stage
- remain independent

Disqualifiers:

- accept subordination to the final command
- faction disappears through an unrelated world-end cleanup

Difficulty: very hard.

Visibility: hidden until the player controls an eligible actor.

Icon direction:

A fictional faction seal split through its center with three diverging banners.

## 9. `031_maximum_survivor`

Working label: Maximum Survivor.

Eligible country:

The player country selected when Global Jihad launches at Maximum intensity.

Unlock conditions:

- launch through the scenario UI at Maximum
- survive without changing player country
- preserve or restore the original capital
- clear domestic Terror Pressure
- defeat every Event 31 territorial actor or end them through valid surrender and cleanup
- prevent The False Revelation or defeat it if it fires

Disqualifiers:

- debug launch outside the scenario UI
- intensity mismatch
- tag switch
- incomplete scenario ledger

Difficulty: extreme.

Visibility: visible.

Icon direction:

A battered national capital surrounded by cleared crisis markers and broken fictional faction emblems.

## 10. `031_false_revelation_denied`

Working label: The False Revelation Denied.

Eligible country:

Any country fighting the final state.

Unlock conditions:

- materially help recapture at least one command capital
- materially help sever at least one strategic corridor
- restore at least one high-pressure country or defeat one major uprising
- participate in the final defeat or disappearance of the entity state
- survive the terminal campaign

Disqualifiers:

- join or submit to the final state
- tag switch
- no material contribution to final defeat

Difficulty: extreme.

Visibility: hidden until the world-end branch begins.

Icon direction:

An ambiguous dark figure fading above a recaptured command hall at dawn. No sacred imagery.

## 11. `031_victims_before_victory`

Working label: Victims Before Victory.

Eligible country:

Any ordinary government with major Event 31 civilian losses.

Unlock conditions before final defeat of the connected organization:

- complete victim support in every state with major losses
- restore every destroyed critical transport link
- maintain protected relief access during the territorial phase
- finish with Response Legitimacy at `80` or above
- defeat or secure the surrender of the organization

Disqualifiers:

- any affected state remains without completed recovery
- an abusive failure occurs after the support chain begins

Difficulty: hard.

Visibility: visible.

Icon direction:

Relief workers opening a restored railway station while soldiers remain outside the civilian area.

## 12. `031_war_without_a_capital`

Working label: War Without a Capital.

Eligible country:

Any ordinary government.

Unlock conditions:

- lose the original capital to an Event 31 actor without capitulating
- establish a valid backup capital
- continue the war
- retake the original capital
- complete Restore Civil Authority in that state within one year
- preserve the original government
- reduce Terror Pressure below `40`

Disqualifiers:

- government takeover
- unrelated scripted state transfer
- tag switch

Difficulty: extreme.

Visibility: hidden until the original capital is lost.

Icon direction:

A government seal carried from a dark temporary headquarters back to a restored capital skyline.

## Tracking architecture

Implement persistent tracking for:

- automatic Event 31 firing count
- manual and force-trigger disqualification
- tracked player country
- tag-switch disqualification
- crisis start date and deadline
- starting and current Terror Pressure
- active-state count
- new-state creation during an achievement run
- territorial actor formation
- successful coups
- minimum Response Legitimacy
- government-caused civilian deaths
- abusive failures
- movement-restriction duration
- atrocity and cover-up Condemnation
- state loss and restoration
- original and backup capital
- corridor IDs broken
- sponsor exposed or neutralized
- safe haven eliminated
- Network Reach stage change
- community and worship-site objective completion
- Event 31 and Event 14 rival identity and shared-border proof
- material defeat contribution
- jihadist faction membership and leadership contest
- International Unity stage
- Global Jihad type and intensity
- scenario launch source and ledger
- False Revelation state
- command-capital contribution
- strategic-corridor contribution
- restored high-pressure country contribution
- victim-support and transport-repair completion by state
- final actor cleanup

Use flags for true or false state and variables for actual counts, dates, IDs, and threshold history.

Clean temporary trackers when an achievement run succeeds, fails permanently, or the campaign state makes it invalid.

Do not clear global one-campaign history needed by The Long Watch.

All tracking must survive save and reload.

## Eligibility and anti-cheese rules

Achievements intended for automatic play must not unlock from:

- Force Trigger Mode
- console or debug setup
- manual scenario unless the achievement explicitly requires Global Jihad
- precompleted mission state
- unrelated scripted annexation or state transfer
- tag switching
- duplicated actors or scenario launch

Contribution achievements need clear material thresholds.

A country that enters a war on the final day and performs no objective should not unlock a defeat achievement.

A scenario achievement must read the stored intensity and type at confirmation time.

## Localisation

Write final achievement names and descriptions from the working direction.

Descriptions should clearly state the difficult public objective without exposing hidden formulas or internal variable names.

Hidden achievements can conceal surprise conditions until revealed, but their eligible-state tooltip should remain coherent.

Do not paste this prompt, working labels, or implementation notes into localisation.

## Icons

Route all achievement art to `chaosx_icon_artist` through the Event 31 asset prompt.

Each achievement needs:

- original completed `64x64` source and DDS
- grey variant
- not-eligible variant
- exact full-ID filename triplet
- contact-sheet review
- manifest row
- final consumer

Do not resize focus, idea, decision, report, or flag art.

No icon may use a real extremist symbol, sacred hostile branding, graphic gore, or readable generated text.

## Documentation

Document:

- ID
- final name
- public description
- eligibility
- unlock conditions
- disqualifiers
- difficulty
- hidden state
- tracking flags and variables
- icon paths
- test cases
- known blockers

Add a route and achievement coverage table to the Event 31 documentation.

Update the authoritative workbook only when it contains an achievement-facing field. Never edit the export CSVs directly.

## Validation

For every achievement test:

- one valid unlock path
- one near-miss
- every major disqualifier
- save and reload during tracking
- tag switch
- debug or force-trigger path
- manual scenario path where relevant
- actor merge, annexation, or cleanup when relevant
- asset and localisation visibility

Use a clean campaign checkpoint for each mutually exclusive or long-running case.

## Completion gate

Do not claim the achievement package complete until all `12` achievements are registered, tracked, localized, documented, given final icon triplets, tested against valid and invalid cases, and included in the final Event 31 completion audit.
