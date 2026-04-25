# Chaos Redux: Complete Mechanics Guide

## Table of Contents

1. [Core Event System](#core-event-system)
2. [Dynamic Timer System](#dynamic-timer-system)
3. [Event Classification](#event-classification)
4. [Chaos Meter System](#chaos-meter-system)
5. [World End Scenario Mechanic](#world-end-scenario-mechanic)
6. [Event Evolution and Event Logs](#event-evolution-and-event-logs)
7. [Configuration and Settings](#configuration-and-settings)
8. [Multiplayer Compatibility](#multiplayer-compatibility)
9. [Debug and Monitoring](#debug-and-monitoring)
10. [Chemical and Biological Warfare](#chemical-and-biological-warfare)
11. [Chaos Warfare](#chaos-warfare)

---

## Core Event System

### Overview

Chaos Redux implements an adaptive event system that responds to player actions, world state, and previous events. The system uses weight-based probability, dynamic timing, and chaos-driven escalation to create an unpredictable and challenging experience.

Complete event documentation: <https://docs.google.com/spreadsheets/d/1A-N5TvU9Ed_xDW4YFG75RvzTIhdA5Hc0f5YyO3qi0Ik/edit?usp=sharing>

### Core Principles

- **Dynamic Adaptation**: Event frequency and selection adapt to current world state
- **Historical Memory**: System tracks all fired events and adjusts future probabilities
- **Escalating Difficulty**: Higher chaos levels increase event frequency and severity (evolution)
- **Player Agency**: Settings allow customization of system behavior

---

## Dynamic Timer System

### Timer Mechanics

The system uses a dynamic timer that replaces traditional fixed monthly intervals:

- **Daily Updates**: Timer decreases by 1 each day
- **Event Trigger**: When timer reaches 0, event selection begins
- **Base Range**: 45-60 days between events (configurable)
- **Initial Timer**: 7-30 days on game start

### Timer Acceleration

#### Minor Event Effects

Each minor event that fires:

- Increases daily decrement by +1 (maximum: 35)
- Makes subsequent events fire sooner
- Effect accumulates across multiple minor events

#### Compression Mechanism

Every 3 minor events:

- Reduces maximum timer by 1 day (maximum reduction: 13 days)
- Compresses the overall timer range
- Creates faster event cycles during active periods

| Minor events since last major | Daily decrement | Max timer reduction before roll | Possible next timer at `1.0x` |
| --- | --- | --- | --- |
| `0` | `0` | `0` | `45-60` days |
| `1` | `1` | `0` | `44-59` days |
| `2` | `2` | `0` | `43-58` days |
| `3` | `3` | `1` | `42-56` days |
| `6` | `6` | `2` | `39-52` days |
| `9` | `9` | `3` | `36-48` days |
| `12` | `12` | `4` | `33-44` days |
| `15+` | `15` | `5` | `30-40` days |

#### Major Event Reset

When a major event fires:

- Resets both decrement and compression to 0
- Returns timer to standard 45-60 day range
- Provides breathing room after significant events

### Timer Examples

**Standard Progression:**

- Event 1: 45-60 days
- After minor event: 44-59 days (decrement +1)
- After 2nd minor: 43-58 days (decrement +2)
- After 3rd minor: 42-56 days (decrement +3, max -1)

**Maximum Acceleration:**

- Base range: 45-60 days
- Maximum decrement: -35 days
- Maximum compression: -13 days
- Effective range: 10-12 days

| Chaos tier | Timer multiplier | Speed vs calm | Max-acceleration range with current defaults |
| --- | --- | --- | --- |
| **Calm World** | `1.0x` | baseline | `30-40` days |
| **Gathering Storm** | `0.8x` | `20%` faster | `24-32` days |
| **Rising Chaos** | `0.7x` | `30%` faster | `21-28` days |
| **Chaos Tier** | `0.6x` | `40%` faster | `18-24` days |
| **Totalen Chaos** | `0.5x` | `50%` faster | `15-20` days |
| **World Collapse** | `0.5x` | `50%` faster | `15-20` days |

---

## Event Classification

### Fire-Once Events

- **Initial State**: Weight starts at 1000
- **Frequency**: Trigger exactly once per campaign
- **Weight After Firing**: Permanently set to 0
- **Purpose**: Events that have a minor impact on the world at first, usually regional, but can become global.

### Repeatable Events

- **Initial State**: Weight starts at 1000
- **Frequency**: Can fire multiple times with diminishing returns
- **Weight Recovery**: +20 per month after firing
- **Cap Reduction**: Maximum weight reduced by 50% each firing
- **Weight Progression**: 1000 → 500 → 250 → 125 → 63 → 32 → 16 → 8 → 4 → 2 → 1
- **Purpose**: Events that have a minor impact on the world and can be fired multiple times during a game.

### Major Events

- **Initial State**: Weight starts at 0 (inactive)
- **Activation**: Weight increases by 150 per minor event fired
- **Firing Condition**: Compete with other events based on accumulated weight
- **Weight After Firing**: Permanently set to 0 for the fired event and all unfired major events reset to 0 weight
- **Purpose**: Events that have a major impact on the world right away
- **Super Events**: Major events are displayed as Super Events

| Event type | Default start weight | Repeat behavior | Recovery / growth | System effect after firing |
| --- | --- | --- | --- | --- |
| **Fire-Once** | `1000` | Fires once per campaign | None | Event is marked fired permanently and removed from future selection; still adds minor-event timer pressure |
| **Repeatable** | `1000` | Can fire repeatedly | `+20` weight per month up to current cap | Weight cap is halved each firing; still adds minor-event timer pressure |
| **Major** | `0` | Fires once per campaign | `+150` weight per minor event fired | Fired major resets major weights and resets timer acceleration state |

### Super Event Example

<img width="910" height="595" alt="super_event_preview" src="https://github.com/user-attachments/assets/ac4d2961-ee6b-4ea3-8d06-1e668bbf0fe0" />

---

## Chaos Meter System

### Chaos Meter Overview

A global meter (0-1000+) that tracks world instability and drives system behavior.

<img width="480" height="80" alt="chaos_meter_0" src="https://github.com/user-attachments/assets/315ecf14-8e84-4e42-9f85-1cfccbf78a9f" />

### Chaos Meter Window

The Chaos Meter details window has five tabs:

1. **Status**: Current chaos value, current tier, and a short mechanics explanation.
2. **History**: Scrollable chaos change log with filters and sorting.
3. **Air Cleanliness**: Global air quality, contamination pressure, and threshold status.
4. **Condemnation**: Country-by-country responsibility for unconventional warfare use.
5. **Deaths**: Total deaths, civilian/military split, and a recent death log.

<!-- IMAGE PLACEHOLDER: Chaos Meter window with all five tabs visible -->

### Chaos Tiers

- **Calm World** (0-199): Normal event frequency, stable conditions
- **Gathering Storm** (200-399): Slightly increased event frequency, some evolutions available
- **Rising Chaos** (400-599): Moderately increased frequency, more evolutions available
- **Chaos Tier** (600-799): High frequency, a lot event evolutions
- **Totalen Chaos** (800-999): Very high frequency, most evolutions available
- **World Collapse** (1000+): Maximum chaos, system prepares end-game scenarios

| Tier | Chaos range | Timer multiplier | Relative event speed |
| --- | --- | --- | --- |
| **Calm World** | `0-199` | `1.0x` | baseline |
| **Gathering Storm** | `200-399` | `0.8x` | `20%` faster |
| **Rising Chaos** | `400-599` | `0.7x` | `30%` faster |
| **Chaos Tier** | `600-799` | `0.6x` | `40%` faster |
| **Totalen Chaos** | `800-999` | `0.5x` | `50%` faster |
| **World Collapse** | `1000+` | `0.5x` | `50%` faster |

### Chaos Sources

| System | Lower / minor change | Higher / major change |
| --- | --- | --- |
| War | `+1` | `+5` |
| Peace | `-1` | `-3` |
| Annexation | `+2` | `+10` |
| Puppeting | `+1` | `+3` |
| Liberation | `-2` | `-5` democratic liberation |
| Freeing countries | `-3` | n/a |
| Faction joining | `+1` | `+3` |
| Faction leaving | `-1` | `-3` |
| Ideology change | `+1` minor non-democratic / `-2` minor democratic | `+5` major non-democratic / `-5` major democratic |
| Nuclear or thermonuclear use | shared ladder: `+10`, `+5`, `+3`, `+2`, then `+1` | thermonuclear uses stronger fallout/condemnation effects, but shares the same direct chaos ladder |
| Monthly world decay | `-1` | n/a |

| Scaling rule | Exact threshold |
| --- | --- |
| World tension rise | `+1` chaos per percentage-point rise |
| Military buildup | `+1` chaos per `100` military factories |
| Division buildup | `+1` chaos per `100` divisions |
| Deaths | `+1` chaos per `1,000,000` tracked deaths |
| Air contamination | `+1` chaos per net `+1%` contamination, `-1` chaos per net `-1%` recovery |

Chaos changes can also happen from events.

### Air Cleanliness (Contamination) System

Air cleanliness is a global pressure system shown in the Chaos Meter window.

- Chemical contamination in one state adds **+0.01%**.
- One outbreak state adds about **+0.02%** (lower/higher by outbreak intensity).
- A normal nuke adds **+0.2%**.
- A thermonuclear strike adds **+1.5%**.
- Natural recovery scales by contamination level while still reversible:
  - below **25%**: **-0.03%** monthly
  - **25%+**: **-0.02%** monthly
  - **50%+**: **-0.01%** monthly
  - **75%+**: **-0.005%** monthly

Threshold behavior:

- **25%**: contamination and outbreak spread becomes easier.
- **50%**: mild nuclear-winter periods can begin.
- **75%**: stronger nuclear-winter periods can begin, with harsher global penalties.
- **100%**: contamination becomes irreversible and states begin a long decline toward wasteland.

For chaos synchronization:

- Every **+1%** contamination change adds **+1 chaos**.
- Every **-1%** contamination recovery removes **1 chaos**.

The tab uses a single current status line for stage/state, plus a short mechanics overview on the side.
The tab also includes an enable/disable checkbox for the air cleanliness system.

| Source | Basis points | Percent |
| --- | --- | --- |
| Chemical contamination in one state | `+1 bp` | `+0.01%` |
| One outbreak state, low intensity | `+1 bp` | `+0.01%` |
| One outbreak state, base intensity | `+2 bp` | `+0.02%` |
| One outbreak state, high intensity | `+3 bp` | `+0.03%` |
| Normal nuke | `+20 bp` | `+0.20%` |
| Thermonuclear strike | `+150 bp` | `+1.50%` |

| Monthly recovery band | Basis points | Percent |
| --- | --- | --- |
| Below `25%` | `-3 bp` | `-0.03%` |
| `25%+` | `-2 bp` | `-0.02%` |
| `50%+` | `-1 bp` | `-0.01%` |
| `75%+` | `-0.5 bp` | `-0.005%` |

| Threshold | Basis points | Result |
| --- | --- | --- |
| `25%` | `2500 bp` | Spread becomes easier |
| `50%` | `5000 bp` | Mild nuclear-winter periods can begin |
| `75%` | `7500 bp` | Stronger nuclear-winter periods can begin |
| `100%` | `10000 bp` | Contamination becomes irreversible |
| `1000%` | `100000 bp` | Fallout world-end scenario can trigger |

<!-- IMAGE PLACEHOLDER: Air Cleanliness tab with thresholds and status line -->

### Condemnation System

Condemnation is diplomatic blame for unconventional weapon use.

What increases condemnation:

- Chemical units actively used in combat
- Chemical and biological attack use
- Nuclear strike use, with larger strikes on more populated states causing heavier condemnation
- Some decisions as well

The **Condemnation** tab shows your value and a sortable country list.  
The list updates instantly when condemnation changes.

<!-- IMAGE PLACEHOLDER: Condemnation tab with sortable country list -->

### Deaths System

Strategic bombing, chemical and biological attacks, outbreaks, nuclear strikes, and military casualties all feed a shared global deaths tracker.

- Death sources reduce real state population, not only recruitable manpower.
- Population losses are scaled by state population, local conditions, and the kind of attack, so dense and poorly protected areas suffer more heavily.
- Outbreak and contamination deaths happen gradually over time for as long as the state remains affected.
- Nuclear strikes cause a heavy immediate death spike and can leave behind radioactive fallout that keeps killing civilians over time.
- The **Deaths** tab shows total deaths, civilian deaths, military deaths, latest change, and a scrollable death log.
- Death log entries show the affected country, death type as **Civilian** or **Military**, and can be filtered by type.
- The tab includes an enable/disable checkbox for the deaths system.
- Every **1,000,000** total deaths adds **+1 chaos**.

<!-- IMAGE PLACEHOLDER: Deaths tab with totals and recent log -->

### Chaos Effects on Timing

Each chaos tier applies a multiplier to event timers:

- **Calm World**: 1.0x (no change)
- **Gathering Storm**: 0.8x (20% faster)
- **Rising Chaos**: 0.7x (30% faster)
- **Chaos Tier**: 0.6x (40% faster)
- **Totalen Chaos**: 0.5x (50% faster)
- **World Collapse**: 0.5x (events prepare for end-game)

---

## World End Scenario Mechanic

When the **Chaos Meter** exceeds 1000, the system triggers a **World End Scenario**.  
This represents the logical conclusion of the campaign and prevents indefinite gameplay.

<img width="480" height="80" alt="chaos_meter_max" src="https://github.com/klimPaskov/Chaos-Redux/blob/master/gfx/interface/chaos_meter/chaos_meter_max.png" />

### Key Rules

- **Trigger Condition**: Chaos > 1000  
- **Scenario Selection**: Based on world state (e.g., zombie apocalypse if outbreak dominates, or other endgame disasters depending on conditions).  
- **Event Freeze**: Automatic event firing stops across the world.
- **Purpose**: Ensures campaigns reach a dramatic, conclusive end and prevents late-game slowdown.
- **Super Event**: Each world end scenario has a custom super event.

---

## Event Evolution and Event Logs

### Event Evolution

Events can transform into more dangerous versions when chaos levels are sufficient:

- **Chaos Requirements**: Different events evolve at different chaos thresholds
- **Progressive Escalation**: Higher chaos enables more severe event variants
- **Prerequisite Events**: Some evolutions require specific previous events

### Event Logs Window

The event logs window tracks what has happened and what can still happen.

- Tabs: **Status**, **History**, **Evolutions**, **Events**
- **Events** tab lists all available events.
- You can filter events by **All / Enabled / Disabled**.
- You can sort by **Event ID**, **Fired count**, or **Weight** (ascending/descending).
- Each event row has a quick toggle button to enable/disable that event.

Any row in **History**, **Evolutions**, or **Events** can be clicked to open a separate detail window.

<!-- IMAGE PLACEHOLDER: Events tab with filter/sort/toggle controls -->
<!-- IMAGE PLACEHOLDER: Multiple event detail windows opened at once -->

---

## Configuration and Settings

### Event Trigger Settings

- **Event System Toggle**: Enable/disable per country
- **Force Trigger Mode**: Bypass normal restrictions
- **Event Filtering**: View by type (All/Major/Repeatable/Fire-Once)
- **Manual Triggering**: Direct event selection and firing
- **Random Event**: Random selection with filters

<https://github.com/user-attachments/assets/c60e12a0-5fee-424d-8768-2b89a261ccfe>

### Timer System and Tag Management Settings

- **Timer**: Adjust the timer range
- **Timer Window**: Optional display of countdown
- **Bulk Operations**: Enable/disable for selected countries
- **Country Filtering**: All/Enabled Only/Disabled Only
- **Continent Sorting**: All countries or by continent
- **Auto-Enable on Switch**: Automatically enable for new player countries
- **Disable for the previous country**: Automatically disables the event system for the previous country on tag switch.

<https://github.com/user-attachments/assets/d23b0a7b-de94-4f8e-aedb-99ad13a3d887>

### Chaos Meter Configuration

- **Value Adjustment**: Direct manipulation of chaos level
- **Tier Selection**: Jump to specific chaos tiers
- **System Toggle**: Enable/disable chaos meter effects

<https://github.com/user-attachments/assets/83ccc354-9396-4341-bfe2-dc9a066ad1ab>

### Advanced Settings

- **Recovery Rate**: 0-10000 weight recovery per month (default: 20)
- **Cap Reduction Factor**: 0-100% weight cap reduction per firing (default: 50%)
- **Major Event Weight**: 0-10000 weight per minor event (default: 150)
- **Timer Modifiers**: 0.1x-2.0x chaos tier multipliers

<https://github.com/user-attachments/assets/cd4a3168-5f4f-47c8-96d0-e968a3007138>

---

## Multiplayer Compatibility

### Shared Systems

- **Event Pool**: All players share the same global event system
- **Chaos Meter**: Single global chaos value affects all players

### Individual Systems

- **Timers**: Each player has their own event timer
- **Settings**: Players can configure their own local settings
- **Event Targeting**: Events can target specific players or be global

---

## Debug and Monitoring

TODO

---

## Chemical and Biological Warfare

Chaos Redux adds high-risk warfare tools that trade short-term battlefield power for long-term consequences. These systems reward preparation and timing, and they can backfire if used recklessly.

<!-- IMAGE PLACEHOLDER: Chemical and biological warfare overview (UI entry points) -->

### Chemical Warfare

Standard chemical weapons are unlocked through research, and more advanced and special chemical weapons are developed through special research projects.

### Chemical Cylinder Abilities

Chemical attacks appear as special abilities on your generals once you research them. Each chemical type has its own ability.

What it is:

- A short, controlled chemical release that boosts your army for a limited time.
- Powered by command power and your stored chemical cylinders.

How it works in play:

- You activate the ability on a general.
- It affects every division under that general for a set duration.
- The ability’s power depends on how many cylinders you have available compared to how many your army needs.
- While active, your troops become slower overall, but they fight better when attacking in cities for example.
- Weather, terrain, and wind can change the result. Bad conditions can greatly reduce the value of the attack. You can research special wind techs to get more favorable wind forecasts.
- You cannot chain different chemical abilities on the same general at the same time.

What the player does:

1. Research a chemical type.
2. Produce and stockpile cylinders for that chemical.
3. Choose the right general and timing, then activate the ability.
4. Watch the forecast and battlefield conditions before committing.

What changes in outcomes:

- With good preparation and good conditions, chemical abilities can create breakthroughs.
- With low stockpiles or bad conditions, the attack is much weaker and may cause heavy self-inflicted disruption.

<!-- IMAGE PLACEHOLDER: Example chemical ability tooltip showing stockpile, forecast, and final effects -->

#### Wind Forecast (Weekly)

Chemical attacks are heavily affected by wind. The game provides a wind forecast that updates each week.

How it works in play:

- Most of the time the wind is neutral and changes nothing.
- Sometimes the wind is favorable and your chemical attack becomes stronger.
- Sometimes the wind is against you and the attack becomes weaker and more harmful to your own troops.
- There is also a small chance the forecast is wrong, causing an unpleasant surprise after you commit.

What the player does:

- Use wind detection research to improve the odds of favorable wind and reduce forecast mistakes.
- Prefer using chemical attacks when the forecast is favorable and the terrain is suitable.

<!-- IMAGE PLACEHOLDER: Wind forecast bar (Against / Neutral / Favorable / Strong) -->

#### Weather

- Colder conditions preserve effects longer.
- Hotter conditions shorten persistence.

#### Frontline Contamination (Temporary State Effects)

While a chemical ability is active, chemical contamination can build up in areas where your affected divisions are operating near the enemy.

How it works in play:

- Contamination builds gradually over the duration.
- The longer you keep pressure up in the same region, the worse the contamination becomes.
- Contamination affects everyone in the area, not just one side.

What the player does:

- Decide whether the short-term gains are worth making a region harder to fight in for everyone.

<!-- IMAGE PLACEHOLDER: State modifier icon and a state view showing contamination effects -->

### Support Companies

#### Tanks

Chemical tank support companies and provide chemical battlefield pressure through tank-supported delivery.

Each chemical tank support company needs:

- normal tank chassis equipment (by its class),
- matching chemical payload stock.

#### Livens Projector

Each Livens chemical support company needs:

- Livens projector equipment,
- matching chemical payload stock.

#### Contamination

Support companies can contribute to contamination when they are actively participating in combat. They are also weather-sensitive.

#### Diplomacy and Condemnation

Using chemical supports in combat increases international condemnation.

Heavy repeated use can trigger escalating diplomatic fallout.

Condemnation is based on real use of unconventional weapons in combat, not on just being at war or owning stockpiles.

You can track who is responsible in the Chaos Meter **Condemnation** tab.

<!-- IMAGE PLACEHOLDER: Condemnation tab showing countries and updated totals -->

### Chemical Planes

You can apply chemical air bomb modules to your planes. The planes behave as CAS, but cause more damage and add contamination to states.
This feature is part of the chemical warfare system and expands high-impact air operations.

### Raids

You can create raids with chemical weapons, similar to nuke raids.

### Gas Masks and Protection

Gas masks reduce how much your troops suffer from chemical attacks. Better protection means fewer losses and less disruption during chemical fighting.
Research gas mask improvements if you plan to use chemicals often, or if you expect the enemy to do so.
There's also dimercaprol, which reduces the effects of blister agents.

<!-- IMAGE PLACEHOLDER: Gas mask research and its effect on chemical attacks -->

### Doomsday Protocols (Chemical Release)

When a fascist country is close to capitulation, it can unlock a desperate last-resort decision to release its entire chemical stockpile at once.

How it works in play:

- It harms armies in all states you control, including allies and friendly troops present.
- It leaves widespread contamination that can severely damage your ability to fight and supply your forces.
- It consumes your entire stockpile.

What the player does:

- Use only as a last resort when collapse is imminent, and you want to trade long-term damage for one final chance. (or you are just a madman)

<!-- IMAGE PLACEHOLDER: Doomsday Protocol decision and its warning tooltip -->

### Biological Warfare

Bioweapons are developed through special research projects.

- Completing a bioweapon project unlocks new bioweapon stockpiles you can build up.
- Some development choices are safer but slower.
- Riskier choices can speed things up, but can also cause serious accidents at home.

<!-- IMAGE PLACEHOLDER: Biowarfare special projects screen -->

### Bioweapon Strikes (Raids)

Once unlocked, bioweapons can be delivered through special strike missions.

How it works in play:

- You select a target and launch a strike if you have the required aircraft and bioweapon stockpiles.
- A strike can fail, partially succeed, or succeed.
- Successful strikes contaminate the target area and can trigger international backlash.

What the player does:

- Use strikes to cripple key enemy regions and war effort (or mostly just kill population), but plan for consequences and retaliation.

<!-- IMAGE PLACEHOLDER: Bioweapon raid selection and target map -->

### Outbreaks and Spread

Contamination is not always contained to one place.

How it works in play:

- Some bioweapons can spread from one area to neighboring areas over time.
- Spread is more likely when conditions are chaotic and containment is weak.
- The most dangerous diseases can escalate into large outbreaks if not contained.

What the player does:

- Treat bioweapons as more than a one-time strike: a successful hit can become an ongoing crisis.

<!-- IMAGE PLACEHOLDER: Multiple neighboring states showing a spreading outbreak -->

#### Countermeasures (Hospitals, Quarantine, Medicine, Vaccination)

Biowarfare has dedicated defensive tools.

How it works in play:

- You can deploy emergency measures to reduce the damage of contamination.
- Medical programs can reduce long-term harm and slow the spread.
- Some threats require long-term national programs to fully remove.

What the player does:

- Use containment decisions quickly when an outbreak begins.
- Maintain defensive programs if you expect repeated attacks.

<!-- IMAGE PLACEHOLDER: Containment decisions (field hospitals, quarantine) and active effects -->

#### Stockpile Accidents and Containment Safety

Holding large bioweapon stockpiles is dangerous.

How it works in play:

- The more bioweapons you store, the higher the risk of accidents.
- Accidents can cause outbreaks in your own territory.
- Containment safety research reduces this risk, and the highest level can prevent stockpile accidents entirely.

What the player does:

- Balance “more stockpile” against “more risk”.
- Invest in containment safety through research if you want large reserves.

<!-- IMAGE PLACEHOLDER: Containment safety research and an example accident warning -->

### Doomsday Protocols (Biological Release)

Like chemical warfare, biological warfare also has a last-resort “unleash everything” decision for desperate situations.

How it works in play:

- It consumes your entire bioweapon stockpile.
- It causes immediate harm across your controlled territory and can trigger widespread outbreaks.

What the player does:

- Use only in extreme desperation when conventional defense is collapsing. (or you are a complete madman)

<!-- IMAGE PLACEHOLDER: Bioweapon doomsday decision and the resulting news popup -->

---

## Chaos Warfare

Chaos Warfare focuses on the most extreme battlefield doctrine paths.

These options increase short-term military pressure, but they also raise long-term costs such as condemnation, civilian harm, and contamination. TODO

<!-- IMAGE PLACEHOLDER: Chaos Warfare doctrine path and key effects -->

### Subdoctrine 1

#### Mastery 1

#### Mastery 2

#### Mastery 3

#### Mastery 4

#### Mastery 5

### Subdoctrine 2

#### Mastery 1

#### Mastery 2

#### Mastery 3

#### Mastery 4

#### Mastery 5

### Subdoctrine 3

#### Mastery 1

#### Mastery 2

#### Mastery 3

#### Mastery 4

#### Mastery 5

### Subdoctrine 4

#### Mastery 1

#### Mastery 2

#### Mastery 3

#### Mastery 4

#### Mastery 5
