# Chaos Redux: Complete Mechanics Guide

Last reconciled with the repository source on 2026-07-29.

## Table of Contents

1. [Core Event System](#core-event-system)
2. [Dynamic Timer System](#dynamic-timer-system)
3. [Event Classification](#event-classification)
4. [Chaos Meter System](#chaos-meter-system)
5. [World End Scenario Mechanic](#world-end-scenario-mechanic)
6. [Event Evolution and Event Logs](#event-evolution-and-event-logs)
7. [Event Clusters](#event-clusters)
8. [Configuration and Settings](#configuration-and-settings)
9. [Triggerable Scenarios](#triggerable-scenarios)
10. [Multiplayer Compatibility](#multiplayer-compatibility)
11. [Debug and Monitoring](#debug-and-monitoring)
12. [Chemical and Biological Warfare](#chemical-and-biological-warfare)
13. [Camps and Genocide Mechanics](#camps-and-genocide-mechanics)
14. [Chaos Warfare](#chaos-warfare)
15. [CBRN Command, Protection, and Diplomacy](#cbrn-command-protection-and-diplomacy)
16. [Shared Country, UI, and Support Systems](#shared-country-ui-and-support-systems)

This guide is the top-level map of implemented gameplay. Live script remains authoritative for exact runtime behavior. Accepted specifications describe intended design, while dated plans and handoffs are evidence snapshots. The event catalog workbook at `docs/spreadsheets/chaos_redux_events_catalog.xlsx` remains the complete player-facing catalog for events, clusters, and manual scenarios.

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
- **Absolute Minimum**: 2 days

### Timer Acceleration

#### Minor Event Effects

Each minor event that fires:

- Reduces the next timer minimum by 1 day, up to a 15-day reduction
- Makes subsequent events fire sooner
- Effect accumulates across multiple minor events

#### Compression Mechanism

Every 3 minor events:

- Reduces the next timer maximum by 1 day, up to a 5-day reduction
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
- Maximum minimum-side reduction: -15 days
- Maximum maximum-side reduction: -5 days
- Effective pre-tier range: 30-40 days

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

### Country-Specific Target Gates

Events that require a specific country or small set of country tags must have a reusable valid-target trigger before they can be selected or manually fired. If no valid target exists, the event is treated as unavailable, shows `N/A` in the event list, and is not queued against a nonexistent country.

The Holy Realm uses this rule directly. Tibet is the normal host. If Tibet no longer exists, Bhutan or Nepal can host. If all three are gone or invalid, event ID `3` has no live weight.

### Event Chaos Levels

Every registered normal event has a minimum Chaos level from 1, Calm World, through 6, World Collapse.

The automatic picker requires the current global Chaos tier to meet or exceed the event's registered level before the event contributes weight.

A locked event keeps its stored weight, cap, fired history, and recovery state. Its weight is not overwritten with zero, and it becomes eligible as soon as the threshold is met.

Event Chaos levels are separate from evolution requirements and event-cluster unlock tiers. A clustered event must meet its own level before the cluster checks its unlock tier and member-specific minimum tiers.

Normal manual event firing respects the event level. Force Trigger Mode may bypass it, while manual cluster forcing and triggerable scenarios retain their separate behavior.

Event Details shows the numeric level and tier name. An Events-tab row that is locked by this requirement shows `N/A` instead of selectable weight.

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
- **Activation**: Weight increases by the current dynamic major gain after each minor pacing event. The configured baseline is 150 at 90 active non-major events and 10 active major events.
- **Firing Condition**: Compete with other events based on accumulated weight
- **Weight After Firing**: Permanently set to 0 for the fired event and all unfired major events reset to 0 weight
- **Purpose**: Events that have a major impact on the world right away
- **Super Events**: Major events are displayed as Super Events

| Event type | Default start weight | Repeat behavior | Recovery / growth | System effect after firing |
| --- | --- | --- | --- | --- |
| **Fire-Once** | `1000` | Fires once per campaign | None | Event is marked fired permanently and removed from future selection. It still adds minor-event timer pressure |
| **Repeatable** | `1000` | Can fire repeatedly | `+20` weight per month up to current cap | Weight cap is halved each firing. It still adds minor-event timer pressure |
| **Major** | `0` | Fires once per campaign | Current dynamic major gain per minor pacing event | Fired major resets major weights and resets timer acceleration state |

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
| Wildfire smoke and volcanic ash reservoir | up to `+4 bp` each month | up to `+0.04%` each month |

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
| `100%` | `10000 bp` | Contamination becomes irreversible and the normal Fallout request route becomes eligible |

<!-- IMAGE PLACEHOLDER: Air Cleanliness tab with thresholds and status line -->

### Condemnation System

Condemnation is the shared diplomatic consequence system for publicly known unconventional warfare, exposed atrocity sites, cover-ups, and repeated use.

What increases condemnation:

- Chemical combat, chemical raids, and chemical doomsday effects
- Biological strikes, outbreaks, biological doomsday effects, and hostile weaponized-zombie deployments
- Nuclear and thermonuclear strikes, with populated capitals and industrial targets causing heavier pressure
- Discovered camps, experiment sites, restricted chemical sites, destroyed records, blocked inspections, and exposed evasion
- Repeated public sources inside the recent-use window

Public condemnation is divided into chemical, biological, nuclear, atrocity, cover-up, and repeat-use sources. Hidden evidence remains outside the public total until inspections, observers, occupation, discovery, or another disclosure path reveals it.

The seven tiers are Normal below `25`, International Concern from `25`, Formal Censure from `50`, Arms Embargo from `100`, Strategic Embargo from `175`, Total Embargo from `300`, and Pariah State from `500`.

The **Condemnation** tab shows public country rows and opens a selected-country detail view with source breakdown, the three newest public sources, current and peak tier, next threshold or Pariah score cap, participant counts, practical penalties, decay, and compliance state. Hidden evidence is never shown before disclosure.

At International Concern, likely participants begin monitoring the target with light opinion and military-support pressure; Formal Censure strengthens those reactions. At Arms Embargo and higher, qualifying countries can impose scalable bilateral restrictions. The native diplomatic embargo is broad rather than resource-specific and requires **By Blood Alone**. Without that DLC, the bilateral enforcement record and its economic and diplomatic penalties still apply. The displayed trade dependency is an aggregate estimate because exact bilateral trade volume is not available to script.

Active volunteers and attachés can be recalled, new lend-lease agreements from sanction participants are blocked, and new volunteer or attaché violations are detected. Already active lend-lease, production licences, and research-sharing membership cannot be generically cancelled or revoked by this system.

Detailed implementation and tuning reference: `docs/systems/condemnation_sanctions.md`.

### Deaths System

Strategic bombing, chemical and biological attacks, outbreaks, nuclear strikes, genocide-crisis site processing, and military casualties all feed a shared global deaths tracker.

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

Reaching 1000 Chaos enters the **World Collapse** tier. It does not call a generic random world-end selector.

Every terminal route is owned by an exact event or consequence system. It must pass its own world-state, Chaos, enable, actor, target, and conflict gates before setting the shared `world_end` state.

Fallout is the contamination-driven terminal consequence. It can be requested at 100 percent Air Contamination, by an owning terminal event, or by its manual route. It uses a dedicated blackout presentation and does not create an ordinary random-event history entry or ordinary super-event popup.

<img width="480" height="80" alt="chaos_meter_max" src="https://github.com/klimPaskov/Chaos-Redux/blob/master/gfx/interface/chaos_meter/chaos_meter_max.png" />

### Key Rules

- **Final Chaos Tier**: Begins at 1000 Chaos.
- **Scenario Selection**: Event-owned and consequence-owned readiness replaces generic selection.
- **Per-Scenario Control**: Public event-owned endings can be enabled or disabled independently from their owner event in Event Details. A disabled ending is skipped by its automatic readiness path, while enabled sibling endings remain eligible.
- **Event Freeze**: Automatic event firing stops across the world.
- **Purpose**: Ensures campaigns reach a dramatic, conclusive end and prevents late-game slowdown.
- **Presentation**: Ordinary world ends use their custom super events. Fallout uses its dedicated full-screen blackout and dedicated dramatic audio while honoring the super-event audio preference.

The current public registry contains Zombie Apocalypse, Fallout, The World in Fury, Last Shores, The World Is the Larder, No Thaw Will Come, The World Opens Below, Laboratory World, and Strategic Singularity. The weaponized Wendigo terminal branch remains hidden from public Event Details.

The old save-facing Final Silence registry identity remains reserved. Its automatic public terminal registration has been replaced by Fallout. The explicit `SCN-004` Final Silence manual scenario remains available.

---

## Event Evolution and Event Logs

### Event Evolution

Events can transform into more dangerous versions when chaos levels are sufficient:

- **Chaos Requirements**: Different events evolve at different chaos thresholds
- **Progressive Escalation**: Higher chaos enables more severe event variants
- **Prerequisite Events**: Some evolutions require specific previous events

### Event Logs Window

The event logs window tracks what has happened and what can still happen.

- Tabs: **Status**, **History**, **Evolutions**, **Events**, **Clusters**
- **Events** tab lists all available events.
- **Clusters** tab lists cluster firings and member skip/fired reasons.
- You can filter events by enabled state, event type, or one of the six exact Chaos levels.
- You can sort by **Event ID**, **Fired count**, or **Weight** (ascending/descending).
- Each event row has a quick toggle button to enable/disable that event.

Any row in **History**, **Evolutions**, **Events**, or **Clusters** can be clicked to open a separate detail window.

Event Details places **World End Scenarios** below the evolution preview. Each public terminal branch owned by that event has its own clickable row, status, details view, and persistent checkbox. Events with several public endings show several independently controlled rows. Hidden easter-egg endings do not appear in this catalog or its controls.

Event Details also shows the selected event's numeric, tier-coloured Chaos level. A locked row shows `N/A` weight and identifies the named tier required for automatic or normal manual firing.

<!-- IMAGE PLACEHOLDER: Events tab with filter/sort/toggle controls -->
<!-- IMAGE PLACEHOLDER: Multiple event detail windows opened at once -->

---

## Event Clusters

Event clusters are linked groups of normal events. The random-event picker still selects one event first. If that event belongs to a cluster, the cluster can roll to fire the wider incident instead of only the selected event.

The selected event's Chaos level and the cluster unlock tier are independent. The event gate is checked first, then the cluster and member gates apply. White Peace therefore cannot enter automatically during Calm World even though the Peace cluster itself unlocks at Calm World.

Cluster firing counts as one global pacing event. Member events still apply their effects, log entries, repeatable cap changes, fire-once removal, fired history, and event details, but they do not each advance the event timer or apply the dynamic major-event gain.

The settings UI has an Event Clusters view for selecting a cluster ID, checking availability, and manually triggering a cluster. Fired clusters appear in the event log **Clusters** tab with the cluster actor, tier, fired/skipped counts, and member reasons.

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
- **Baseline Major Gain**: 0-10000 configured baseline gain (default: 150). At 90 active non-major events and 10 active major events, the current dynamic major gain equals this value.
- **Timer Modifiers**: 0.1x-2.0x chaos tier multipliers

<https://github.com/user-attachments/assets/cd4a3168-5f4f-47c8-96d0-e968a3007138>

---

## Triggerable Scenarios

The settings UI can open a separate movable Triggerable Scenarios window. This window uses generated log-style entries, and the list can be sorted by ID or name in either direction.

Each scenario has a type control and a four-stop intensity slider. The selected values are stored before launch and are read by the scenario effects when the player presses **Launch Scenario**.

All current entries can be found in the event catalog spreadsheet.

| ID | Scenario | Current role |
| --- | --- | --- |
| `SCN-001` | Zombie Apocalypse | Seeds standard or special zombie outbreaks with intensity-scaled coverage. |
| `SCN-002` | Army of Clones | Creates a hostile clone army with standard or Aryan configuration. |
| `SCN-003` | Soviet Collapse | Forces the Event 005 terminal collapse with ordinary or chaos republic settings. |
| `SCN-004` | Final Silence | Runs the explicit nuclear or thermonuclear Final Silence sequence. |
| `SCN-005` | The World in Fury | Seeds pact-based or hostile Fury actors. |
| `SCN-006` | Death | Starts Death with an intensity-scaled opening footprint without starting its terminal route. |
| `SCN-007` | Disaster Barrage | Starts one Event 013 disaster season by selected family and intensity. |
| `SCN-008` | Every Banner Rises | Launches the Event 006 frozen release transaction with selected political and war rules. |
| `SCN-009` | Coalition Unmasked | Builds and reveals an Event 011 coalition around the current player. |
| `SCN-010` | The Hunger Lines | Launches selected Event 014 crisis profiles. |
| `SCN-011` | Africa Is One | Reserved placeholder that launches a neutral placeholder event. |
| `SCN-012` | Black Plague Unbound | Seeds plague outbreaks, Rat Nations, and the Rat King without granting the terminal evolution. |
| `SCN-013` | The Unbidden Muster | Launches the Event 019 formation crisis with conventional, specialist, claimant, or nonhuman profiles. |

Manual scenarios bypass only the normal timing and source-event prerequisites that their setup is designed to replace. They retain their own host, target, conflict, setup-validity, and repeat-launch gates.

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

Debug and monitoring are split between live UI inspection and optional log output.

### Live Inspection

- **Event Logs window**: opened with the settings log button or keyboard shortcuts, and organized into **Status**, **History**, **Evolutions**, **Events**, and **Clusters** tabs.
- **Status tab**: shows current event-system counters and live tuning values, including current calculated major gain, baseline major gain, accumulated major weight, recovery rate, cap reduction, default event weight, and timer modifier.
- **History tab**: records fired automatic events with event ID, type, date, actor context when available, and a clickable detail window.
- **Evolutions tab**: records evolution milestones separately from normal event history, including tier, stage, type, and actor where the evolution belongs to a country.
- **Events tab**: shows the current event catalogue with live weight, fired count, event type, unique/repeatable state, and enable/disable controls.
- **Clusters tab**: shows cluster availability, roll chance, enabled state, fired count, and member status/danger. Cluster details can open member event details without closing the cluster window.
- **Chaos Meter window**: exposes current chaos value, chaos tier, history, air cleanliness, condemnation, and deaths tracking.
- **Timer window**: optionally shows the current event countdown.

### Manual Controls

The settings UI is also the main manual testing surface:

1. Select an event ID directly or use the random-event selector to pick a valid ID.
2. Use category filters to narrow event selection by event type.
3. Enable **Force Trigger Mode** when a manual test needs to bypass normal trigger restrictions.
4. Enable or disable individual events from the event list.
5. Enable or disable whole event clusters from the cluster list or cluster detail window.
6. Open triggerable scenarios for sandbox or challenge setups that are separate from the automatic event timer.

### Log Output

Event-fire log output is opt-in.

- The small log button in the settings window runs one manual event-system snapshot.
- The Trigger Events page has a checkbox for automatic logic log lines.
- Automatic logging is disabled by default.
- When enabled, event-fire summaries include the fired event ID, name, type, unique events left, minor events since the last major, total fired count, and remaining counts per category.
- Daily full debug dumps are gated behind the same setting so normal saves do not spam logs.

Supporting documentation:

- `docs/systems/events_log_window.md`
- `docs/systems/events_log_evolutions_and_clusters.md`
- `docs/systems/chaosx_event_logging_controls.md`
- `docs/systems/settings_miscellaneous_menu.md`
- `docs/systems/settings_numeric_manual_inputs.md`

---

## Chemical and Biological Warfare

Chaos Redux adds high-risk warfare tools that trade short-term battlefield power for long-term consequences. These systems reward preparation and timing, and they can backfire if used recklessly.

<!-- IMAGE PLACEHOLDER: Chemical and biological warfare overview (UI entry points) -->

### Chemical Warfare

Standard chemical weapons are unlocked through research, and more advanced and special chemical weapons are developed through special research projects.

### Chemical Cylinder Abilities

The older general-wide cylinder abilities are disabled. A commander ability cannot prove an exact selected state, current weather, terrain, and delivery receipt, so it cannot create a valid chemical release.

Current chemical attacks use selected-state chemical air raids, selected-state strategic rocket raids, chemical doomsday release, restricted chemical-site release, and other exact adapters that can prove their target and conditions.

Every accepted release must identify an exact target state, prove the selected agent and delivery method, pass the required policy and readiness gates, consume matching physical payload equipment, and record disruption, deaths, contamination, medical pressure, evidence, attribution, Condemnation, and confirmed-use history.

The timed state-targeted ground-operation family remains fail-closed. The current engine does not provide the verified selected-state weather and terrain receipt required by the design. Its decisions and assets remain hidden and unavailable instead of using a random state, capital proxy, or neutral-condition fallback.

<!-- IMAGE PLACEHOLDER: Example selected-state chemical raid tooltip showing payload, protection, and consequences -->

#### Weather

- Weather and terrain affect only routes that can supply a verified condition receipt.
- A delivery route remains unavailable if its required current conditions cannot be proven.

#### Frontline Contamination (Temporary State Effects)

An accepted exact-state chemical action can add contamination to the target state's persistent chemical ledger. The resulting state effects can disrupt all armies in the affected area, drive medical pressure, damage civilians over time, and add to global Air Cleanliness pressure.

<!-- IMAGE PLACEHOLDER: State modifier icon and a state view showing contamination effects -->

### Support Companies

#### Tanks

Chemical tank and armored-delivery support companies provide route eligibility, protection, and equipment-backed pressure. Adding the company to a template does not release an agent automatically.

Each chemical tank support company needs:

- normal tank chassis equipment by its class;
- matching protection and support equipment;
- matching chemical payload when an authorized delivery route commits.

#### Livens Projector

Each Livens chemical support company needs:

- Livens projector equipment;
- matching protection and support equipment;
- matching chemical payload when an authorized delivery route commits.

#### Contamination

Support companies never create contamination from mere presence or ordinary combat participation. They contribute only through an accepted payload-consuming delivery adapter.

#### Diplomacy and Condemnation

Verified chemical use adds to the public or hidden Chemical condemnation source according to evidence and attribution. Chemical raids, chemical doomsday effects, restricted-site releases, and supported exact-state adapters use the same shared consequence model with route-specific severity.

Heavy repeated use can add repeat-use pressure and cross the seven condemnation tiers, leading from concern and censure to arms, strategic, total, and pariah enforcement.

Condemnation is based on real use of unconventional weapons in combat, not on just being at war or owning stockpiles.

You can track who is responsible and inspect public source, sanctions, compliance, and penalty details in the Chaos Meter **Condemnation** tab.

### Chemical Planes

Chemical air modules can be installed on supported CAS and tactical-bomber designs. They authorize matching selected-state chemical raids and apply their native aircraft statistics only to designs carrying the exact rack.

Idle aircraft and ordinary air missions never create contamination. A chemical raid must reserve the exact agent payload, resolve the selected state through the shared exposure pipeline, and record its outcome.

### Raids

Chemical air and strategic rocket raids use the native raid system with exact agent-module, target-state, payload, protection, and consequence checks. Failed or aborted raids can still create an evidence record when the attempt becomes observable, but they cannot create confirmed-use history without a release.

### Gas Masks and Protection

Gas masks reduce how much your troops suffer from chemical attacks. Better protection means fewer losses and less disruption during chemical fighting.
Research gas mask improvements if you plan to use chemicals often, or if you expect the enemy to do so.
There's also dimercaprol, which reduces the effects of blister agents.

The wider protection system also uses filters, protective clothing, decontamination equipment, CBRN instruments, civilian distribution, warning coverage, shelters, medical capacity, and equipment-backed replacement. Protection changes exposure outcomes without erasing evidence, responsibility, historical deaths, or confirmed-use records.

<!-- IMAGE PLACEHOLDER: Gas mask research and its effect on chemical attacks -->

### Doomsday Protocols (Chemical Release)

When a fascist country is close to capitulation, it can unlock a desperate last-resort decision to release its entire chemical stockpile at once.

How it works in play:

- It harms armies in all states you control, including allies and friendly troops present.
- It leaves widespread contamination that can severely damage your ability to fight and supply your forces.
- It consumes your entire stockpile.

What the player does:

- Use it only when the military value is worth the permanent domestic, environmental, and diplomatic consequences.

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

- Balance a larger stockpile against higher accident and containment risk.
- Invest in containment safety through research if you want large reserves.

<!-- IMAGE PLACEHOLDER: Containment safety research and an example accident warning -->

### Doomsday Protocols (Biological Release)

Biological warfare has a last-resort full-stockpile release decision for desperate situations.

How it works in play:

- It consumes your entire bioweapon stockpile.
- It causes immediate harm across your controlled territory and can trigger widespread outbreaks.

What the player does:

- Use it only when the immediate military value is worth uncontrolled outbreaks, domestic losses, and international consequences.

<!-- IMAGE PLACEHOLDER: Bioweapon doomsday decision and the resulting news popup -->

---

## Camps and Genocide Mechanics

The camp and genocide crisis system models state repression, forced labor, extermination sites, gulag networks, experiment-linked atrocity sites, restricted chemical site escalation, evidence destruction, discovery, foreign response, and tribunal pressure.

The key rule is separation between hidden internal damage and public condemnation:

- Camp systems reduce real state population through the Chaos Meter Deaths system.
- Responsible countries accumulate hidden crisis variables such as `genocide_escalation`, `genocide_visibility`, `genocide_deaths`, `genocide_resistance_pressure`, `genocide_foreign_pressure`, `genocide_coverup_effort`, and `genocide_discovered_sites`.
- Camp operation, restricted-site operation, recorded deaths, and internal concealment also accumulate hidden atrocity or cover-up evidence in the shared condemnation system.
- Public condemnation does not rise passively while the responsible regime still controls the evidence.
- Discovery exposes the responsible country's hidden atrocity and cover-up evidence, then adds a public state-specific atrocity source. Experiment sites and restricted chemical sites add source-specific bonuses, while destroyed or failed cover-up evidence can add a separate public cover-up source.
- Enemy occupation or liberation can expose undiscovered camp, gulag, experiment, restricted-site, or destroyed-site evidence.

### Buildings and State Tracking

The system uses three state buildings:

- `concentration_camp`: detention, forced labor, deportation processing, and repression.
- `extermination_camp`: systematic killing and the highest discovery condemnation.
- `gulag_labor_camp_network`: Soviet forced labor and mass repression.

Concentration camps are available in the normal construction interface at a low construction cost. Historical Germany, Japan, and the Soviet Union can begin with quiet concentration camp infrastructure already present, but those sites do not enter the active death or discovery loop until later escalation. Extermination camps and gulag networks are created through decisions and effects. Scripted creation stores `genocide_responsible_country` on the state, so discovery targets the country that built or operated the site instead of the country that finds it.

### Crisis Decisions and AI

The generic crisis category covers upgrades from existing concentration camps into extermination camps. It is the lowest-priority decision category and appears only when a country has an eligible existing camp and an actual special decision available beyond the show/hide controls.

The generic category no longer builds concentration camps by decision. Most operational genocide behavior is AI-driven or handled by country-specific categories, while the player-facing generic category reveals or hides eligible extermination-camp, Germany, and restricted chemical site decisions.

Foreign-observer evidence pressure depends on context: occupied foreign territory, non-core target populations, diplomatic visibility, or discoveries. Domestic repression inside a closed authoritarian state does not automatically create foreign-observer pressure.

Country-specific categories handle:

- Germany: wartime camp administration, occupied Poland escalation, extermination camps, Mengele-linked experiment sites, deportation logistics, and retreat cover-ups.
- Japan: forced labor camps, anti-partisan reprisals, prisoner experimentation, occupation evidence destruction, and biological warfare links during the China war.
- Soviet Union: gulag expansion, deportations, famine pressure, camp-administrator purges, forced-labor quotas, evidence destruction, and a mechanical Soviet Collapse bridge.

Restricted chemical site escalation uses existing sarin/soman tech, special-project, stockpile, contamination, Deaths, and discovery systems. It creates hidden evidence and delayed atrocity or cover-up condemnation instead of firing public chemical-use condemnation immediately.

AI weights make fascist Germany, imperial Japan, and communist Soviet Union the primary users under historical or radicalized conditions. A separate AI strategy package adjusts broad behavior for active and exposed crisis regimes.

---

## Chaos Warfare

Chaos Warfare is a conditional CBRN grand doctrine. It turns protection, chemical and biological programs, headquarters, regimental support, payload logistics, readiness, and selected-state operations into one military institution.

Selecting the grand doctrine:

- costs 100 Army Experience;
- initializes Chemical Readiness and the CBRN institution;
- starts a 90-day establishment mission;
- opens four visible mastery tracks;
- grants only the technologies and operation gates whose exact requirements are met.

These options increase short-term military pressure, but they also raise long-term costs through condemnation, civilian harm, state contamination, and possible outbreak escalation.

<!-- IMAGE PLACEHOLDER: Chaos Warfare doctrine path and key effects -->

Establishment requires 500 gas masks, 50 decontamination equipment, 100 support equipment, a fielded CBRN Operations HQ Section, and a fielded Gas Mask and Decontamination Detachment. Failure leaves the doctrine active but closes offensive gates until the exact proof is repaired.

Four cross-track institutions raise readiness caps and unlock stronger command:

1. Protective Foundation
2. Delivery Integration
3. Theater Exploitation
4. Terminal CBRN Command

The use-policy ladder runs from Defensive Preparation through Retaliation Authority, Limited Battlefield Authority, Strategic Release Authority, and Unrestricted Chaos Warfare. Policy authorizes later adapters. It does not release a payload by itself.

### Infantry Track: Hazard Assault Formations

`extermination_columns` remains the compatibility ID for Hazard Assault Formations. The route covers mask discipline, contaminated-terrain movement, Hazard Pioneer qualification, Chaos Assault Battalion qualification, shock exploitation, and terminal hazard-operation eligibility.

Activation effects:

- adds a modest breakthrough bonus to mapped CBRN assault battalions;
- begins mastery from fielded gas-mask, reconnaissance, Hazard Pioneer, and Chaos Assault Battalion units.

#### Mastery 1: Contagion Assault Drills

- Improves reliability for mapped primary-protection equipment.
- Unlocks Mask Discipline.

#### Mastery 2: Sacrificial March Columns

- Reduces supply consumption for mapped CBRN engineer support.
- Unlocks contaminated-terrain movement.

#### Mastery 3: Chaos Assault Battalion

- Records the Chaos Assault Battalion qualification.
- The battalion still requires its exact doctrine, technology, formation, and equipment gates.
- Fielding the battalion never releases a chemical payload automatically.

#### Mastery 4: Ruinwave Battlecells

- Adds a modest breakthrough bonus to mapped CBRN assault battalions.
- Unlocks shock exploitation.

#### Mastery 5: Terminal Contagion Offensive

- Adds the track's final bounded breakthrough bonus to mapped CBRN assault battalions.
- Unlocks terminal hazard-operation eligibility.
- It does not create passive contamination, casualties, or Condemnation.

### Armor Track: Toxic Armored Warfare

`chemical_suppression` remains the compatibility ID for Toxic Armored Warfare. The route covers sealed crews, armored-agent delivery, equipment-backed suppression eligibility, protected breakthrough logistics, and synchronized shock preparation.

Activation effects:

- adds a modest breakthrough bonus to mapped chemical tank support companies;
- begins mastery from fielded light, medium, and heavy armored-delivery detachments and the nerve-suppression detachment.

#### Mastery 1: Adamsite Emission Cells

- Improves chemical tank support reliability.
- Unlocks sealed crew compartments.

#### Mastery 2: Armored Chemical Liaison Teams

- Unlocks armored-agent delivery operations.

#### Mastery 3: Zyklon B Saturation Drills

- Unlocks the mobile nerve-suppression operation gate.
- Does not create camps, extermination sites, experiment sites, genocide mechanics, or the retired Concentration occupation law.

#### Mastery 4: Sealed Pressure Logistics

- Reduces chemical tank support supply consumption.
- Unlocks protected breakthrough logistics.

#### Mastery 5: Catastrophic Shock Breakthrough

- Adds a small coordination bonus.
- Unlocks catastrophic shock-operation eligibility.

### Combat Support Track: Contaminant Fire Support

`contaminant_firebases` remains the compatibility ID for Contaminant Fire Support. It focuses on projector fire control, counterbattery coordination, chemical artillery shells, persistent-agent filling, and deep-contamination operation eligibility.

Activation effects:

- improves reliability for mapped CBRN artillery logistics;
- begins mastery from fielded chemical projector batteries and chemical ammunition trains.

#### Mastery 1: Livens Fire Control Cells

- Improves reliability for mapped offensive-delivery equipment.
- Unlocks projector fire control.

#### Mastery 2: Counterbattery Gas Synchronization

- Adds a small coordination bonus.
- Unlocks counterbattery chemical fire.

#### Mastery 3: Raid Targeting Teams

- Unlocks chemical-shell logistics.
- It does not release or reserve a payload by itself.

#### Mastery 4: Persistent Agent Distribution

- Improves reliability for mapped CBRN artillery logistics.
- Records the persistent-agent filling qualification.

#### Mastery 5: Deep Contamination Fireplans

- Records deep-contamination fire-plan eligibility.
- An actual attack still requires an exact payload-consuming adapter and the shared consequence pipeline.

### Operations Track: Integrated CBRN Command

`integrated_chemical_operations` remains the compatibility ID for Integrated CBRN Command. It supplies intelligence and weather cells, protective logistics, mobile decontamination, biological security, chemical-air eligibility, and Theater CBRN Headquarters.

Activation effects:

- begins mastery from the six fielded CBRN Army Headquarters companies;
- records the Integrated CBRN Command route for institutional and operation gates.

#### Mastery 1: Operational Recon Grids

- Improves reconnaissance.
- Records the first Integrated Command milestone and its Condemnation-only doctrine multiplier.

#### Mastery 2: Signal Intelligence Fusion

- Improves land reinforce rate.
- Records the second Integrated Command milestone for Headquarters and institution gates.

#### Mastery 3: Counter-Contamination Routing

- Reduces supply consumption for mapped CBRN Headquarters companies.
- Records the counter-contamination routing milestone.

#### Mastery 4: Air-Surface Chemical Link

- Adds a small coordination bonus.
- Records the Chemical Air Interdiction and Biological Security qualification milestone.
- It does not create a passive chemical-air effect.

#### Mastery 5: Theater Intelligence Overmatch

- Adds bounded army organization and coordination bonuses.
- Records Theater CBRN Headquarters and the final Integrated Command milestone.
- The final doctrine multiplier reduces Condemnation only. Evidence, attribution, payload use, deaths, contamination, medical pressure, and public-harm floors remain unchanged.

### Doctrine Visibility and AI

- All four Chaos Warfare subdoctrines remain visible in the doctrine interface.
- They are only selectable when the country has the `chaos_warfare` grand doctrine.
- AI weight is forced to `0` for countries without `chaos_warfare`.
- AI adoption and track preference use real program profiles, industry, war state, enemy chemical use, protection, stockpiles, and explicit route flags.
- AI receives no free payload, readiness, operation, or protection shortcut.
- Nonhuman countries receive zero weight for the institutional CBRN package.

The mastery subsections above preserve the established compatibility IDs and route ancestry. Exact current institutions, technology commissions, equipment requirements, readiness caps, operation gates, officer-corps effects, and balance values are maintained in `docs/systems/chaos_warfare_doctrine.md`.

Supporting documentation:

- `docs/chemical_warfare/chaos_warfare_grand_doctrine_update.md`
- `docs/chemical_warfare/chaos_warfare_extermination_columns.md`
- `docs/chemical_warfare/chaos_warfare_chemical_suppression.md`
- `docs/chemical_warfare/chaos_warfare_combat_support.md`
- `docs/chemical_warfare/chaos_warfare_integrated_chemical_operations.md`
- `docs/chemical_warfare/chaos_warfare_subdoctrine_visibility_and_ai.md`

---

## CBRN Command, Protection, and Diplomacy

The wider CBRN package connects Chaos Warfare to exact equipment, command, protection, delivery, evidence, diplomacy, AI, and historical records.

### Army Headquarters and Regimental Support

Six Army-HQ-only support companies prepare chemical planning, protection, decontamination, cordons, medical response, biological containment, and the doctrine capstone.

An HQ order checks the deployed headquarters and exact company composition, pays Command Power and real equipment, records the force band and operation identity, runs a bounded preparation period, and pays weekly sustainment while active.

HQ preparation never chooses a target or releases a payload by itself. Exact delivery remains owned by a selected-state raid, decision, camp adapter, occupation adapter, biological route, or other verified action.

Regimental CBRN companies form the division layer. They provide protection, reconnaissance, decontamination, medical support, and route eligibility with real reinforcement requirements.

Supporting documentation:

- `docs/systems/cbrn_hq_command.md`
- `docs/chemical_warfare/cbrn_regimental_support.md`

### Protection and Civil Defence

The protection package includes military and civilian gas masks, filters, protective clothing, decontamination equipment, CBRN instruments, medical capacity, warning coverage, shelters, national reserves, civilian distribution, issue, maintenance, and replacement.

Protection changes the resolved exposure of an accepted action. It never erases evidence, responsibility, historical deaths, Condemnation, or confirmed-use history.

### CBRN Military Industrial Organizations

The Military Industrial Organization layer includes chemical munitions, air delivery, protective equipment, decontamination, detection, and biological protection families.

Exact chemical-rack weight, range, and agility behavior uses grant-only module technologies because current MIO filters cannot prove that an aircraft variant carries one specific chemical rack. This prevents chemical-designer bonuses from applying to ordinary aircraft.

Supporting documentation: `docs/systems/cbrn_designers.md`.

### Unified Action Records

Every accepted deliberate chemical release and ordinary biological seed creates one durable action record.

Each record stores the attacker, affected country, exact target state, date, weapon class, agent, delivery method, severity, civilian deaths, available military casualty receipt, contamination or outbreak change, evidence, attribution, retaliation state, first-use state, and repeat-use pressure.

Each record also creates a dedicated Event Log history row. The action ledger remains separate from the Deaths, Air Cleanliness, outbreak, Condemnation, and diplomacy ledgers.

Supporting documentation: `docs/systems/cbrn_action_records.md`.

### International Response

The CBRN diplomacy layer includes inspection demands, exact-state forensic publication, foreign decontamination aid, sanctions participation, retaliation, compliance, refusal, and stockpile destruction.

Every action uses a stored country or state target and consumes real equipment, factory capacity, or political resources. Forensic publication advances the exact stored action row and never assigns hidden responsibility to a guessed incident.

Supporting documentation:

- `docs/systems/cbrn_diplomacy_actions.md`
- `docs/systems/condemnation_sanctions.md`

### Occupation Policies

Two supported occupation policies are active:

- **CBRN Coercive Security**
- **Protected Occupation Administration**

The legacy `concentration` occupation-law ID remains hidden and modifier-free for save migration.

The Nerve Agent Suppression Detachment and exact-state suppression transaction remain fail-closed. The engine does not expose the verified state-condition and target-loss receipts required by the accepted design. Its commissioning and operation controls remain hidden, and no estimator or fallback is used.

Supporting documentation: `docs/systems/cbrn_occupation_and_nerve_suppression.md`.

---

## Shared Country, UI, and Support Systems

### Liberation Release Coordinator

The release coordinator synchronizes country-release systems that can collide, especially Soviet Collapse and Independence Wave. It protects host survival, state reservations, transaction ownership, rollback, and joint presentation.

Supporting documentation: `docs/systems/liberation_release_coordinator.md`.

### Country and Formable Registries

Event-created countries use shared carrier collections, provenance, package identity, active-generation state, and collision-safe formable contracts.

Event 006 adds a dedicated country registry, formable registry, package admission rules, regional overlays, rival blocs, and fail-closed formable readiness.

Supporting documentation:

- `docs/events/006_independence_wave/systems/country_registry.md`
- `docs/events/006_independence_wave/systems/formable_registry.md`
- `docs/systems/chaos_unit_family_registry.md`

### Startup History Compatibility

Additive technologies, equipment, facilities, and character grants for existing countries are applied through the startup compatibility layer rather than copied vanilla history files.

Supporting documentation: `docs/systems/startup_history_compatibility.md`.

### Custom Achievements

The shared achievement registry and event-owned achievement packages track real routes, survival, origin, scenario state, and forced-run disqualifiers. Event-owned documents remain authoritative for exact conditions.

Supporting documentation:

- `docs/systems/custom_achievements.md`
- `docs/achievements/006_independence_wave/achievements.md`
- `docs/achievements/016_brilliant_scientist/achievements.md`

### State Map Modes

Custom map modes expose state-level disease, contamination, repression, and event-owned data. Rebuilds occur after committed transactions rather than during every intermediate mutation.

Supporting documentation: `docs/systems/state_map_modes.md`.

### Main Menu, Help, and Settings Export

The mod includes a custom main menu, welcome surface, settings interface, Event Log, Chaos Meter, super-event presentation, scenario window, help window, and settings export.

Supporting documentation:

- `docs/systems/main_menu_redesign.md`
- `docs/systems/chaosx_help_window.md`
- `docs/systems/chaosx_settings_export.md`
- `docs/systems/gfx_icon_flag_mapmode_cleanup.md`

### 3D Runtime Assets

The 3D unit and facility pipeline uses explicit model, material, animation, scale, entity, and runtime-consumer contracts. A model package is not a gameplay mechanic until its unit, building, entity, action, and map consumer are wired.

Supporting documentation:

- `docs/systems/chaos_warfare_facility_models.md`
- `docs/specs/chaos_redux_3d_model_workflow_planning_package/`
- `docs/assets/chaos_redux_3d_model_pilots/`
