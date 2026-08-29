# Achievements

## Achievement design goals

The achievement set rewards distinct ways of playing the expedition race.

It covers:

- ordinary victory
- difficult access
- restraint
- recovery from failure
- cooperation
- intelligence play
- fragment play
- evolution mastery
- Event 036 interaction

Achievements must use full tracking, disqualifiers, localisation, icons, and save persistence. They must not unlock from a force-triggered test unless the project achievement rules explicitly allow debug testing.

## 1. Antarctic Vanguard

Working achievement ID:

`025_alien_technology_antarctic_vanguard`

Objective:

Win the primary recovery core as a participant.

Tracking:

- Event 025 winner flag belongs to current country
- main technology reward successfully applied

Disqualifiers:

- no reward application because of invalid state
- debug-only launch when achievements are disabled by project policy

Icon direction:

A period expedition pennant planted beside a dark metallic fragment.

Purpose:

Baseline completion achievement.

## 2. The Long Way South

Working achievement ID:

`025_alien_technology_long_way_south`

Objective:

Win while using the improvised or chartered-access route from a country without direct coastal access at entry.

Tracking:

- country lacked direct coastal route when it entered
- route remained improvised, chartered, or sponsored through the departure phase
- country won the main core

Disqualifiers:

- direct route became available before departure and was selected
- country received a special free route bypass

Icon direction:

A long dotted route crossing a globe toward an Antarctic compass point, with a small crate and convoy silhouette.

Purpose:

Rewards human minors and landlocked starts.

## 3. White Science

Working achievement ID:

`025_alien_technology_white_science`

Objective:

Win without carrying out a hostile expedition action.

Allowed actions:

- defense
- counterintelligence
- rescue
- data exchange
- ordinary escort

Disqualifying actions:

- theft
- false coordinates
- route sabotage
- outpost sabotage
- blockade
- seizure
- unprovoked armed attack

A country does not lose eligibility merely because another participant attacked it.

Icon direction:

A clean white field notebook, radio antenna, and microscope over snow.

Purpose:

Makes peaceful competition a real route.

## 4. Nobody Gets Left on the Ice

Working achievement ID:

`025_alien_technology_nobody_left_on_ice`

Objective:

Rescue a rival expedition facing a valid personnel-loss crisis, then win the main core.

Tracking:

- rescue action completed
- target was another active participant
- rescue prevented or reduced a real loss
- rescuer later won

Disqualifiers:

- staged or self-created invalid target
- target already withdrawn

Icon direction:

Two expedition figures pulling a third from a crevasse under a radio mast.

Purpose:

Rewards cooperation under pressure.

## 5. The False Map

Working achievement ID:

`025_alien_technology_false_map`

Objective:

Suffer a successful false-coordinate operation, identify the deception, recover the lost search time, and still win.

Tracking:

- false-coordinate effect applied
- deception later exposed
- survey certainty restored to or above the previous verified level
- country won

Disqualifiers:

- deception removed through debug effect

Icon direction:

A torn Antarctic chart with two crossed coordinate marks and one corrected route.

Purpose:

Rewards recovery from intelligence failure.

## 6. Without an Escort

Working achievement ID:

`025_alien_technology_without_escort`

Objective:

Win after Something Survived or Militarised Antarctica becomes active without committing a military escort.

Tracking:

- Evolution II or III recorded while country is active
- no military escort action used at any point
- country won

Civilian guards, weather teams, and ordinary expedition security do not count as a military escort.

Disqualifiers:

- armed escort, warship patrol, military aircraft cover, or fortified security package used

Icon direction:

A lone tracked expedition vehicle approaching a huge dark shadow in the snow.

Purpose:

High-risk scientific route.

## 7. Reclaim the Station

Working achievement ID:

`025_alien_technology_reclaim_the_station`

Objective:

Lose control of the Antarctic outpost through a valid hostile or survivor incident, restore it, and win.

Tracking:

- outpost became seized, overrun, or abandoned through crisis
- same country restored a functioning outpost
- same country won

Disqualifiers:

- voluntary dismantlement followed by ordinary rebuilding

Icon direction:

A damaged polar hut with a restored flag and repaired radio mast.

Purpose:

Rewards recovery from a major operational setback.

## 8. Fragments of a Losing Cause

Working achievement ID:

`025_alien_technology_fragments_of_a_losing_cause`

Objective:

Lose the main race but finish with the highest non-winner fragment tier.

Tracking:

- another country won
- current country received the major fragment-cache outcome
- current country remained active until resolution or completed a valid fragment evacuation

Disqualifiers:

- fragment tier obtained by transfer after the winner announcement

Icon direction:

Several broken alien components arranged in a field crate while a distant rival ship departs.

Purpose:

Recognizes a meaningful non-winner strategy.

## 9. Six Fields of Debris

Working achievement ID:

`025_alien_technology_six_fields_of_debris`

Objective:

Recover all six authorized fragment categories during Wreck Breaking Apart in one campaign.

Tracking:

- country owns each distinct fragment category at least once
- categories are recorded through physical recovery or valid exchange

Disqualifiers:

- duplicated category counted more than once
- ownership created without transfer proof

Icon direction:

Six distinct alien fragments arranged around an Antarctic sector map.

Purpose:

Evolution IV mastery.

## 10. Listen Without Answering

Working achievement ID:

`025_alien_technology_listen_without_answering`

Objective:

Win after Active Signal by using passive remote analysis while never jamming, broadcasting toward, or deliberately amplifying the signal.

Tracking:

- Evolution I active
- remote passive analysis completed
- no active-signal provocation action used
- country won

Disqualifiers:

- signal jamming
- directed transmission
- reckless amplification

Icon direction:

A period radio receiver with headphones and a thin luminous trace above it.

Purpose:

Rewards disciplined signal play.

## 11. Human Factors

Working achievement ID:

`025_alien_technology_human_factors`

Objective:

Contain Alien Dependence while retaining the recovered technology, then pass one full year without a dependence accident.

Tracking:

- Evolution V active for current country
- containment route completed
- technology retained
- Dependence below the controlled threshold
- 365 continuous days without an alien-system accident

Disqualifiers:

- artifact destroyed before the containment result
- custody transferred away
- accident timer reset

Icon direction:

A gloved human hand placing a transparent shield over an alien circuit.

Purpose:

Evolution V safe-management achievement.

## 12. The System Prefers Us

Working achievement ID:

`025_alien_technology_system_prefers_us`

Objective:

Choose aggressive integration, reach a high but stable Dependence band, and remain in control for two years.

Tracking:

- integration route selected
- high Dependence threshold reached
- country retains government control
- no forced transfer or emergency destruction
- 730 days survive after threshold

Disqualifiers:

- Dependence collapsed through debug action
- country lost the alien program

Icon direction:

An alien control surface bending around a human command chair, with the human silhouette still upright.

Purpose:

Difficult high-risk Evolution V route.

## 13. Two Crashes, One Answer

Working achievement ID:

`025_alien_technology_two_crashes_one_answer`

Objective:

Receive a valid upgraded reward through the Event 025 and Event 036 arbitration system.

Valid orders:

- win Event 025, then receive an upgraded Event 036 aircraft result
- receive Event 036 first, then win Event 025 and receive a non-duplicate upgrade or integration result

Tracking:

- both event identities recorded for current country
- shared alien-recovery ledger confirms overlap conversion
- upgraded result applied successfully

Disqualifiers:

- two unrelated non-overlapping rewards with no arbitration
- duplicate base reward applied through a bug

Icon direction:

Two different falling objects converging into one upgraded aircraft or propulsion symbol.

Purpose:

Cross-event mastery.

## 14. First Among Equals

Working achievement ID:

`025_alien_technology_first_among_equals`

Objective:

Win a race with at least five active participants after sharing data with two different rivals.

Tracking:

- five or more valid participants reached the outpost phase
- current country completed two separate valid data-sharing actions with different countries
- current country won

Disqualifiers:

- repeated exchange with the same country counted twice
- data sharing after the main core was already secured

Icon direction:

Five expedition pennants around a central instrument case, with one pennant holding the recovered core.

Purpose:

Rewards cooperative play in a genuinely competitive field.

## Tracking architecture

Achievement tracking should use stable flags and bounded counters.

Suggested surfaces:

- participant route identity at entry and departure
- hostile action ledger
- rescue ledger
- false-coordinate incident flag and recovery proof
- escort commitment flag
- outpost loss and restoration flags
- fragment-category bitset or flags
- signal-policy action flags
- Dependence route and accident-free day counter
- Event 036 overlap conversion flag
- unique data-sharing target set or bounded count with country proof

Tracking must survive save and reload.

## Achievement timing

Achievements should unlock when the full condition is proven.

- winner achievements unlock after reward application and cleanup
- fragment achievements unlock after ownership is stable
- Evolution V timed achievements unlock after their full duration
- cross-event achievement unlocks after the upgraded reward is applied

Do not unlock winner achievements at the start of the final mission.

## Achievement asset contract

Each achievement requires:

- final working ID promoted to stable ID
- name and description localisation
- unlock trigger
- disqualifiers
- normal DDS
- grey DDS
- not-eligible DDS
- documentation row
- asset manifest row
- test case

The three DDS files must follow the root achievement folder naming convention and use independent achievement art, not resized decision or idea icons.

## Achievement balance and exploit review

Required checks:

- hostile actions are recorded before cleanup
- withdrawal cannot preserve winner eligibility
- fragment transfer cannot duplicate ownership
- one data-sharing target cannot satisfy two-target requirements
- toggling an evolution off cannot leave impossible achievement tracking active
- Event 036 overlap must prove an actual converted reward
- Dependence survival timers reset on qualifying accidents
- annexation and tag changes preserve or invalidate tracking according to country continuity rules
