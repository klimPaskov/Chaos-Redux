# Achievement specification

## Achievement policy

Achievements reward mastery, unusual settlements, recovery, humane governance, difficult formables, and hidden routes. They must include complete tracking, disqualifiers, icons, localisation, and route hooks.

Hidden-route achievements must not spoil Teutonic Order or Atlantis before reveal. Their public names and descriptions can remain hidden or use non-spoiling conditions according to the current achievement framework.

## Achievement set

### 038_01 Deus Vult, Logistically

**Goal:** hold Malta, Jerusalem, Cyprus, and the selected main supply port for a sustained period while every active Event 38 front remains supplied.

**Difficulty:** medium.

**Disqualifiers:** Force Trigger Mode or scenario setup if the project achievement rules disallow them.

**Purpose:** rewards solving the event's real logistics problem instead of only winning battles.

### 038_02 A Hospital with an Army

**Goal:** complete the Hospitaller capstone, field a minimum number of formations with Hospitaller support, keep Order Cohesion above the high threshold, and complete major relief actions without an exposed Event 38 atrocity site.

**Difficulty:** medium to hard.

### 038_03 The Eleventh Time Is the Charm

**Goal:** lose the original Holy Land expedition, activate the Eleventh Crusade, retake Jerusalem, and hold it through the recovery mission.

**Difficulty:** hard.

**Anti-cheese:** the failure state must be genuine and sustained. Voluntary one-day state transfer does not count.

### 038_04 Outremer Reborn

**Goal:** create and maintain the Kingdom of Jerusalem, Principality of Antioch, County of Tripoli, and Crusader Cyprus at the same time, with fulfilled obligations and no active succession crisis.

**Difficulty:** hard.

### 038_05 All Roads Lead to Rome

**Goal:** form the Holy See, install the Pope as supreme ruler, make Rome the political capital, and retain Jerusalem as sacred military center.

**Difficulty:** medium to hard.

### 038_06 Neither Sword nor Hunger

**Goal:** complete a major Malta or Papal campaign using humane governance, prevent catastrophic famine in Event 38 territories, avoid forced-displacement deaths caused by Event 38 policy, and finish with low public atrocity condemnation.

**Difficulty:** hard.

**Purpose:** rewards a route that protects populations rather than extracting them.

### 038_07 The Orders Stand Together

**Goal:** form the Confederation of the Military Orders with all six order families active, Order Cohesion at or above 80, and no dominant order.

**Difficulty:** medium.

### 038_08 The Temple Pays Its Debts

**Goal:** finish the Templar finance route, clear or stabilize every route-specific debt obligation, and win a major regional war without defaulting on sponsor commitments.

**Difficulty:** hard.

### 038_09 No False Relics

**Goal:** reach Sacred Legitimacy at or above 80 and form the Kingdom of God without using a relic later exposed as false.

**Difficulty:** hard.

**Hidden proof:** relic authenticity or controversy remains hidden from the player until normal exposure. Achievement tracking reads the final public state and internal proof without revealing it early.

### 038_10 A Continent Under the Keys

**Goal:** complete the full-continent Holy World readiness mission before Chaos reaches 1000.

**Difficulty:** very hard.

**Purpose:** rewards terminal preparation without automatically requiring world conquest.

### 038_11 The Last Pilgrimage

**Goal:** activate The Holy World through the normal Event 38 route and secure a defined first terminal campaign objective.

**Difficulty:** very hard.

**Scenario exclusion:** the manual Believers vs Nonbelievers scenario does not count.

### 038_12 The Cross and the Wheel

**Goal:** hidden. Form the Teutonic Order and begin Operation The Final Crusade with all three founding members intact.

**Difficulty:** very hard.

**Spoiler rule:** name, icon, and description remain hidden until the route is revealed or completed.

### 038_13 Twenty Spears of Atlantus

**Goal:** hidden. Activate Atlantis and keep all 20 initial Supreme formations alive through a defined major campaign milestone.

**Difficulty:** very hard.

**Tone:** description should frame the route's military feat without celebrating the extermination policy.

### 038_14 The Myth Breaks

**Goal:** defeat Atlantis as Malta, the Holy See, the Holy Realm, or an accepted coalition leader, dismantle its extermination system, and liberate Atlantus.

**Difficulty:** very hard.

### 038_15 Malta Stands Alone

**Goal:** survive and win the original regional campaign without any formal foreign sponsor, Papal military aid, or created principality.

**Difficulty:** hard.

**Purpose:** supports a compact Malta-centered replay route.

## Tracking rules

Every achievement needs:

- stable ID
- visibility rule
- availability rule
- disqualifiers
- progress flags or variables
- exact completion trigger
- no accidental completion from manual setup
- save and reload persistence
- icon triplet
- localisation
- documentation

## Scenario and force-trigger rules

The implementation must follow current project achievement policy. Recommended defaults:

- normal manual event firing can count only when Force Trigger Mode is off and ordinary eligibility is respected
- triggerable scenarios do not count for normal-route achievements unless the achievement explicitly says so
- debug or CXT setup does not count
- tag switching can disqualify country-specific achievements when the current framework supports that proof

## Multiplayer

Country-specific achievements should attach to the human player or current player actor according to the existing achievement system. A coalition achievement must define which player receives it.

## Icon direction

Every achievement gets unique achievement art and the full triplet. Visual directions:

- logistics uses ports, convoys, and a cross-shaped route
- Hospitaller uses hospital and order symbolism
- Eleventh Crusade uses a damaged then restored banner
- principalities uses several crowns or seals
- Holy See uses keys, Rome, and Jerusalem
- humane route uses relief and protected civilians
- confederation uses six order emblems
- relic route uses a guarded reliquary without proving authenticity
- Holy World uses a Papal globe or continental seal
- hidden routes use non-spoiling locked art until reveal

Do not resize focus or idea icons into achievement art.

## Achievement acceptance tests

- normal campaign completion
- manual scenario exclusion
- Force Trigger Mode exclusion
- save and reload
- state transfer exploit
- principality annex and recreate exploit
- hidden achievement spoiler behavior
- multiplayer actor ownership
- route transformation from Malta to Holy See or Kingdom of God
- Atlantis defeat by several accepted actors
- icon triplet and localisation coverage
