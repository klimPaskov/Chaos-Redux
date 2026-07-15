# Event 014 Cannibalism, Part 11: Achievements, Triggerable Scenario, and Aftermath

## Achievement philosophy

Achievements should reward mastery, dangerous route completion, rare campaign states, clean containment, recovery, warlord play, Hannibal play, and the Wendigo crossover. None should unlock merely because Event 14 fired.

All titles below are internal working directions. Final titles and descriptions are written during implementation.

## Achievement set

### `cannibalism_01_clean_first_country`

Route:

- play the first host country
- achieve clean local containment
- never use exploitation
- prevent foreign spread

Disqualifiers:

- any second country infected
- terror feeding policy
- commune or warlord state formed

Difficulty:

- medium

Visibility:

- visible

Icon direction:

- clean military ration tin beside sealed evidence bag, with dried blood kept outside the seal

### `cannibalism_02_no_second_table`

Route:

- contain Event 14 worldwide before a second country develops an active cell
- the first host can be AI or player, but the player must contribute decisive aid or control the host

Difficulty:

- hard

Visibility:

- visible

Icon direction:

- broken rail and convoy routes surrounding one extinguished red mark

### `cannibalism_03_three_front_containment`

Route:

- remove active cells in three countries
- no warlord country forms
- complete at least one joint suppression mission

Difficulty:

- hard

Visibility:

- visible

Icon direction:

- three military insignia closing around a shattered ritual token

### `cannibalism_04_silent_islands_reclaimed`

Route:

- liberate and fully recover three island or isolated coastal nodes
- maintain supply to each during recovery

Difficulty:

- hard

Visibility:

- visible

Icon direction:

- relief ship approaching a blood-stained island with restored signal light

### `cannibalism_05_cured_then_returned`

Route:

- achieve local victory
- later face an external cannibal invasion or foreign seeding action
- defeat it without reopening domestic exploitation

Difficulty:

- hard

Visibility:

- visible

Icon direction:

- restored army line confronting a Host banner across the border

### `cannibalism_06_repentant_weapon`

Route:

- use the terror exploitation policy
- end the policy
- expose or dismantle the responsible command
- achieve local victory before a commune forms

Disqualifiers:

- later return to exploitation

Difficulty:

- very hard

Visibility:

- hidden until exploitation is selected

Icon direction:

- bloodied bayonet broken over a tribunal file

### `cannibalism_07_break_the_island_host`

Route:

- defeat an Island Host through blockade and landing
- rescue surviving population
- prevent the Host from forming another island node

Difficulty:

- hard

Visibility:

- visible after first Island Host appears

Icon direction:

- shattered jaw emblem above a landing craft and broken chains

### `cannibalism_08_warlord_without_master`

Route:

- play a cannibal warlord country
- choose the defiant route
- survive Hannibal's reveal
- remain independent for a long stabilization period or defeat the unified state

Difficulty:

- extreme

Visibility:

- hidden until Hannibal reveal

Icon direction:

- lone bloody warlord severing a dark command cord

### `cannibalism_09_host_of_unification`

Route:

- play a warlord country
- become the selected unification host
- retain at least three named warlords as commanders or governors
- complete a major unified branch

Difficulty:

- extreme

Visibility:

- hidden until reveal

Icon direction:

- central throne or command seat surrounded by four distinct warlord blades

### `cannibalism_10_all_mouths_one_command`

Route:

- as unified Hannibal, absorb every surviving cannibal country and commune
- no resistant warlord country remains
- preserve a functioning global Larder network

Difficulty:

- extreme

Visibility:

- hidden until reveal

Icon direction:

- many jaw and tooth emblems converging on one blood-covered hand

### `cannibalism_11_continental_larder`

Route:

- as unified Hannibal, maintain active controlled feeding states on three continents
- reach a major cumulative population-consumption threshold
- do not trigger terminal world-end yet

Difficulty:

- extreme

Visibility:

- hidden until reveal

Icon direction:

- three landmasses connected by blood-red shipping and rail routes

### `cannibalism_12_stop_the_reveal`

Route:

- win the convergence warning mission
- destroy the likely host
- reduce Network Reach below reveal readiness
- achieve global victory before the reveal occurs

Difficulty:

- extreme

Visibility:

- hidden until convergence begins

Icon direction:

- unseen portrait frame cracked before it opens

This icon must avoid showing Hannibal's face.

### `cannibalism_13_defeat_hannibal`

Route:

- defeat the revealed unified country before ordinary terminal lock
- eliminate every remaining cell, commune, and warlord
- complete global stabilization

Difficulty:

- extreme

Visibility:

- hidden until reveal

Icon direction:

- fallen command mantle and broken Host standards during recovery

### `cannibalism_14_break_the_winter_hunger`

Route:

- allow the Wendigo Hannibal merge to occur
- capture or destroy every transformation anchor before lock
- defeat the merged state or force it out of terminal progression

Difficulty:

- extreme

Visibility:

- secret until alternate merge

Icon direction:

- frozen transformed claw split by a heated rail spike or relief torch

### `cannibalism_15_ordinary_world_end`

Route:

- complete the ordinary Hannibal world-end

Difficulty:

- extreme

Visibility:

- hidden until Hannibal reveal

Icon direction:

- Hannibal command silhouette over a world consumed by red routes

### `cannibalism_16_wendigo_world_end`

Route:

- complete the Wendigo Hannibal terminal transformation

Difficulty:

- maximum

Visibility:

- secret until alternate merge

Icon direction:

- transformed Hannibal above a frozen and blood-covered globe

### `cannibalism_17_global_burial_detail`

Route:

- defeat a globally significant Hannibal threat
- complete reconstruction in every former feeding state
- maintain the international memory and inspection system for a long period

Difficulty:

- extreme

Visibility:

- hidden until defeat aftermath is eligible

Icon direction:

- identification tags, burial tools, and extinguished Host emblem

### `cannibalism_18_no_empty_state`

Route:

- defeat Event 14 after at least one warlord country forms
- prevent any state from reaching the Silent Larder stage

Difficulty:

- very hard

Visibility:

- visible after Evolution II

Icon direction:

- populated village protected behind a broken jaw-shaped border

## Achievement tracking rules

- hidden routes stay hidden until the appropriate public reveal
- exploitation disqualifiers set immediately and do not clear through cosmetic policy changes
- population and state thresholds use real tracked values
- global-victory achievements require all cells and countries cleared
- player tag transfers during unification preserve achievement eligibility
- manual triggerable scenario launches can be excluded from achievements if project policy requires it
- terminal achievements cannot fire below the world-end chaos threshold

## Triggerable scenario

### Registry direction

Stable catalog ID: `SCN-010`.

Current catalog status: `Fully Functional`.

Working public direction:

- a neutral scenario name about a wartime hunger network
- no Hannibal name
- no Wendigo name
- no terminal-branch spoiler

The scenario remains Event 14 and uses the shared four-stop intensity slider.

## Scenario types

### Discipline Collapse

Purpose:

- begin with one country, one compromised theater, and baseline containment
- no ritual cult at launch unless intensity creates it later

Low:

- one formation, manageable supply problem

Medium:

- several formations and one high-risk state

High:

- severe Field Hunger, low Command Integrity, and foreign spread risk

Maximum:

- several countries or theaters, but still no direct identity reveal

### Ritual Cells

Purpose:

- launch with Evolution I active
- cells exist in selected countries
- Cult Cohesion visible

Intensity controls:

- number of countries
- cell strength
- officer involvement
- exploitation history

### Silent Islands

Purpose:

- create remote island or coastal commune sequences
- emphasize convoy, port, reconnaissance, evacuation, and blockade play

Intensity controls:

- number of islands
- starting isolation
- garrison strength
- probability of immediate Island Host formation

### Warlord States

Purpose:

- create event-owned cannibal countries immediately
- test country packages, focus trees, military setup, and counterwar

Intensity controls:

- number of warlord states
- origin archetypes
- starting territory
- Larder
- units
- Network Reach

### Convergence

Purpose:

- create several mature warlord states and a visible convergence phase
- stage the identity reveal in-world after launch

The scenario UI still does not name Hannibal. The reveal event fires after setup and can become a super-event if scale supports it.

If a valid Wendigo country already exists, the later unification can enter the alternate branch. The scenario type list does not reveal that possibility.

## Scenario launch gates

Block only impossible or conflicting setup:

- world-end already active
- no valid ordinary country or state for the selected type
- no valid island for Silent Islands
- no conflict-free tag capacity for Warlord States or Convergence
- no valid map package

Do not block because:

- chaos is low
- Event 14 has not fired
- evolutions have not naturally occurred
- date is early
- ordinary prerequisites are missing

The manual scenario uses tightly scoped bypass state and clears it after setup.

## Scenario launch behavior

The launch effect reads selected type and intensity at confirmation time.

Setup responsibilities:

- create valid actors and targets
- initialize values
- apply event-owned flags
- set player-facing category state
- preserve player control
- create units and equipment without duplication
- open relevant decisions and focus trees
- record scenario history according to shared scenario rules
- clear bypass flags

## Implemented atomic scenario preflight

Manual launch first builds a mutation-free temporary plan for the exact selected type and intensity. The plan freezes every ordinary actor, each actor's required opening-state capacity, the external Island, Siege, and March state arrays, the required origin distribution, and the deterministic reusable CBA-CBH slot array. Planned destructive states exclude every planned actor country.

Commit begins only after every planned count exactly matches its required count. The launch then consumes the frozen actor, state, and slot arrays rather than reselecting them. A failed preflight changes only the launcher's setup-failure marker and clears temporary planning state. It does not initialize Event 014 runtime, actors, nodes, evolutions, warlords, achievements, scheduling, or launch history. Automatic Evolution III prefire keeps its separate dynamic selection path.

## Implemented staged achievement tracker

All 18 real achievements remain in the root Chaos Redux achievement registry. Achievements 01 through 05 are visible there from the baseline. Achievements 06 through 18 remain statically hidden in the Career Profile because the achievement schema provides only a static hidden field.

A dedicated read-only decision category supplies the required campaign-stage discovery surface. It contains 18 permanently unavailable entries, uses the real completed achievement icons, and calls the exact real achievement completion trigger for each status. The tracker has no cost, effect, cooldown, completion hook, disqualifier, or AI behavior and cannot grant an achievement.

Tracker discovery stages are:

- 01 through 05 at Event 014 system start
- 06 at first exploitation
- 07 at first successful Island Host formation
- 18 at Evolution II
- 12 at convergence
- 08 through 11, 13, and 15 after public reveal
- 14 and 16 after the Wendigo merge
- 17 when global-defeat aftermath becomes eligible.

The category has its own generated 32x32 icon and 114x101 panel. The 18 entries intentionally use the matching real achievement icons because they are the same objectives.

## Defeat aftermath detail

### State recovery stages

#### Emergency liberation

- stop active population consumption
- secure prisoners and evidence
- clear immediate warlord control
- restore supply and medical access

#### Identification and burial

- identify civilian and military victims
- restore records
- support families
- prosecute grave and body theft

#### Institutional recovery

- rebuild local administration
- restore rail, ports, hospitals, prisons, and food distribution
- screen surviving security forces

#### Long-term trauma

- persistent population and production loss
- migration and trust effects
- memorial or vigilance decisions

Dead population is not restored.

### Captured warlords

Possible outcomes:

- public trial
- international tribunal
- local prosecution
- prisoner exchange for captives
- intelligence cooperation
- execution
- escape attempt

Each named warlord should receive an outcome. Do not silently delete the character.

### Captured Hannibal

Only possible before terminal lock.

Potential directions:

- international trial
- disappearance during collapse
- execution by rival warlord or ordinary government
- death in battle

The final player-facing wording requires careful tone and cannot become cheap triumph.

### Reconstruction ideas

Affected countries can gain staged ideas:

- Liberated Feeding States
- Identification and Burial Emergency
- Broken Military Trust
- Rebuilt Supply Discipline
- Permanent Vigilance

Each idea has a clear removal or upgrade path.

### International compact

Available only after global-scale defeat.

Functions:

- prisoner-transfer standards
- burial and casualty-record protection
- military food and supply inspection
- cult intelligence exchange
- rapid island and prison response

The compact can use decisions and opinion modifiers without forcing a permanent faction.
