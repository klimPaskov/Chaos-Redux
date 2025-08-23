# Chaos Redux: Complete Mechanics Guide

## Table of Contents

1. [Core Event System](#core-event-system)
2. [Dynamic Timer System](#dynamic-timer-system)
3. [Event Classification](#event-classification)
4. [Chaos Meter System](#chaos-meter-system)
5. [World End Scenario Mechanic](#world-end-scenario-mechanic)
6. [Event Evolution and Clusters](#event-evolution-and-clusters)
7. [Configuration and Settings](#configuration-and-settings)
8. [Multiplayer Compatibility](#multiplayer-compatibility)
9. [Debug and Monitoring](#debug-and-monitoring)

---

## Core Event System

### Overview

Chaos Redux implements an adaptive event system that responds to player actions, world state, and previous events. The system uses weight-based probability, dynamic timing, and chaos-driven escalation to create an unpredictable and challenging experience.

Complete event documentation: https://docs.google.com/spreadsheets/d/1A-N5TvU9Ed_xDW4YFG75RvzTIhdA5Hc0f5YyO3qi0Ik/edit?usp=sharing

### Core Principles

- **Dynamic Adaptation**: Event frequency and selection adapt to current world state
- **Historical Memory**: System tracks all fired events and adjusts future probabilities
- **Escalating Difficulty**: Higher chaos levels increase event frequency and severity
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

---

## Event Classification

### Fire-Once Events

- **Frequency**: Trigger exactly once per campaign
- **Weight After Firing**: Permanently set to 0
- **Purpose**: Events that have a minor impact on the world at first, usually regional, but can become global.

### Repeatable Events

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

### Super Event Example

<img width="910" height="595" alt="super_event_preview" src="https://github.com/user-attachments/assets/ac4d2961-ee6b-4ea3-8d06-1e668bbf0fe0" />

---

## Chaos Meter System

### Chaos Meter Overview

A global meter (0-1000+) that tracks world instability and drives system behavior.

<img width="480" height="80" alt="chaos_meter_0" src="https://github.com/user-attachments/assets/315ecf14-8e84-4e42-9f85-1cfccbf78a9f" />

### Chaos Tiers

- **Calm World** (0-199): Normal event frequency, stable conditions
- **Gathering Storm** (200-399): Slightly increased event frequency, some evolutions available
- **Rising Chaos** (400-599): Moderately increased frequency, more evolutions available
- **Chaos Tier** (600-799): High frequency, a lot event evolutions
- **Totalen Chaos** (800-999): Very high frequency, most evolutions available
- **World Collapse** (1000+): Maximum chaos, system prepares end-game scenarios

### Chaos Sources

#### Major Increases

- Major power wars: +5 chaos
- Major annexations: +10 chaos
- Major power ideology changes to non-democratic: +5 chaos

#### Moderate Increases

- Minor power wars: +1 chaos
- Minor annexations: +2 chaos
- Puppeting: +1 to +3 chaos
- Faction joining: +1 to +3 chaos
- Nuke: +1 chaos (so it's not abused)
- World tension increases: +1 per percentage point
- Military buildup: +1 per 50 military factories or 100 divisions
- Casualties: +1 per 250,000 casualties

#### Decreases

- Peace agreements: -2 to -5 chaos
- Liberation by democratic powers: -5 chaos
- Freeing countries: -2 to -5 chaos
- Faction leaving: -1 to -3 chaos
- High world stability: variable reduction
- Increased global democracy: variable reduction
- Monthly Decay: -1

Chaos changes can also happen from events.

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

![Chaos Meter 1000+](gfx\interface\chaos_meter\chaos_meter_max.png)

### Key Rules

- **Trigger Condition**: Chaos > 1000  
- **Scenario Selection**: Based on world state (e.g., zombie apocalypse if outbreak dominates, or other endgame disasters depending on conditions).  
- **Event Freeze**: Automatic event firing stops for all countries.  
- **Purpose**: Ensures campaigns reach a dramatic, conclusive end and prevents late-game slowdown.

---

## Event Evolution and Clusters

### Event Evolution

Events can transform into more dangerous versions when chaos levels are sufficient:

- **Chaos Requirements**: Different events evolve at different chaos thresholds
- **Progressive Escalation**: Higher chaos enables more severe event variants
- **Prerequisite Events**: Some evolutions require specific previous events

### Event Clusters

Related events can fire in sequence:

- **Cluster Probability**: Increases with higher chaos levels
- **Thematic Connections**: Events within clusters share themes or consequences
- **Escalating Sequences**: Later events in clusters tend to be more severe

---

## Configuration and Settings

### Event Trigger Settings

- **Event System Toggle**: Enable/disable per country
- **Force Trigger Mode**: Bypass normal restrictions
- **Event Filtering**: View by type (All/Major/Repeatable/Fire-Once)
- **Manual Triggering**: Direct event selection and firing
- **Random Event**: Random selection with filters

https://github.com/user-attachments/assets/c60e12a0-5fee-424d-8768-2b89a261ccfe

### Timer System and Tag Management Settings

- **Timer**: Adjust the timer range
- **Timer Window**: Optional display of countdown
- **Bulk Operations**: Enable/disable for selected countries
- **Country Filtering**: All/Enabled Only/Disabled Only
- **Continent Sorting**: All countries or by continent
- **Auto-Enable on Switch**: Automatically enable for new player countries
- **Disable for the previous country**: Automatically disables the event system for the previous country on tag switch.

https://github.com/user-attachments/assets/d23b0a7b-de94-4f8e-aedb-99ad13a3d887

### Chaos Meter Configuration

- **Value Adjustment**: Direct manipulation of chaos level
- **Tier Selection**: Jump to specific chaos tiers
- **System Toggle**: Enable/disable chaos meter effects

https://github.com/user-attachments/assets/83ccc354-9396-4341-bfe2-dc9a066ad1ab

### Advanced Settings

- **Recovery Rate**: 0-10000 weight recovery per month (default: 20)
- **Cap Reduction Factor**: 0-100% weight cap reduction per firing (default: 50%)
- **Major Event Weight**: 0-10000 weight per minor event (default: 150)
- **Timer Modifiers**: 0.1x-2.0x chaos tier multipliers

https://github.com/user-attachments/assets/cd4a3168-5f4f-47c8-96d0-e968a3007138

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

### Debug Output

Comprehensive logging system tracks:

- **Event Statistics**: Total fired, by type
- **Timer Information**: Current values, modifiers, progression
- **Weight Tracking**: Current weights, caps, recovery status
- **Chaos Monitoring**: Current level, recent changes, tier effects

### Debug Commands

Available through the settings interface:

- **System Reset**: Return all settings to defaults
- **Manual Event Firing**: Direct event triggering with bypass options
- **Timer Testing**: Immediate timer recalculation and adjustment

### Diagnostic Information

```
  ======================================================
  CHAOS REDUX EVENT SYSTEM DEBUG START NR [X]
  DATE:  [X]
  ======================================================

  EVENTS FIRED:
  Total events fired: [X]
  Major events fired: [X]
  Minor events fired: [X]
    - Minor repeatable events fired: [X]
    - Minor fire-once events fired: [X]
  ------------------------------------------------------
  UNIQUE EVENTS:
  Total events in system: [X]
  Total unique events yet to be fired: [X]
    - Major events unfired: [X] / [X]
    - Minor fire-once events unfired: [X] / [X]
    - Minor repeatable events unfired: [X] / [X]
  ------------------------------------------------------
  MAJOR EVENT WEIGHTS:
  Minor events fired since last major: [X]
  Current major event weight: [X]
  ------------------------------------------------------
  SYSTEM INFO:
  Minor event weight: [X]
  Minor event recovery rate: [X]
  Minor repeatable event cap reduction: [X]
  Major event weight per minor: [X]
  ------------------------------------------------------
  DYNAMIC TIMER SYSTEM:
  Timer range: [X] - [X] days
  Timer day decrement: [X] / [X] days
  Max cap reduction: [X] / [X] days
  Current timer range after decrements: [X] - [X] days
  Current chaos tier: [X]
  Current chaos timer modifier: [X]x
  Current timer: [X] days
  ------------------------------------------------------
  Last fired event: ID: [X]
  Name: [X], Type: [X]
  ------------------------------------------------------
  MAJOR EVENTS DETAIL:
  ID: [X], Name: [X], Weight: [X]
  …
  ------------------------------------------------------
  FIRE-ONCE EVENTS DETAIL:
  ID: [X], Name: [X], Weight: [X]
  …
  ------------------------------------------------------
  REPEATABLE EVENTS DETAIL:
  ID: [X], Name: [X], Weight: [X], Cap: [X]
  …

  ======================================================
  CHAOS REDUX EVENT SYSTEM DEBUG END NR [X]
  ======================================================

```
