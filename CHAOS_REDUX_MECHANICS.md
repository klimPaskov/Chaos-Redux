# Chaos Redux: Complete Mechanics Guide

## Table of Contents

1. [Core Event System](#core-event-system)
2. [Smart Event Firing Logic](#smart-event-firing-logic)
3. [Dynamic Timer System](#dynamic-timer-system)
4. [Event Categories](#event-categories)
5. [Chaos Meter](#chaos-meter-danger-scaling)
6. [Event Evolution System](#event-evolution-system)
7. [Event Clusters](#event-clusters)
8. [Multiplayer Compatibility](#multiplayer-compatibility)
9. [Event Chain Timers (Mini-Narratives)](#event-chain-timers-mini-narratives)
10. [Debug System](#debug-system)
11. [Configuration Options](#configuration-options)

---

## Core Event System

### Overview

Chaos Redux introduces an event system with a sophisticated, dynamic event firing mechanism that adapts to player actions, world state, and previous events.
List of all the existing and upcoming events can be found here: https://docs.google.com/spreadsheets/d/1A-N5TvU9Ed_xDW4YFG75RvzTIhdA5Hc0f5YyO3qi0Ik/edit?usp=sharing

### Key Features

- **Dynamic Event Weights**: Events become rarer after firing, recovering slowly over time
- **Intelligent Timing**: Major events fire based on minor event accumulation
- **Adaptive Difficulty**: System responds to chaos levels (Chaos Meter)
- **Memory**: System tracks all fired events and adjusts future probabilities

---

## Smart Event Firing Logic

### Weight-Based System

Instead of pure randomness, events have **weight values** that determine firing probability:

- **Initial Weight**: 1000 (default for minor events)
- **Weight Recovery**: +20 per month after firing
- **Weight Caps**: Individual caps per event, reduced by 50% each firing. 1000 → 500 → 250 → 125 → 63 → 32 → 16 → 8 → 4 → 2 → 1

### Major vs Minor Event Logic

- **Minor Events**: Build up "pressure" in the system
- **Major Events**: Fire when enough minor events have occurred
- **Pressure Calculation**: Major event weight = (minor events since last major) × 200
- **Reset Mechanism**: Major event firing resets the minor event counter

---

## Dynamic Timer System

### Overview

The Dynamic Timer System replaces fixed monthly event timers with a daily, adaptive timer that responds to the types of events that have recently fired.

### Core Timer Mechanics

#### Initial Timer

- **Startup Range**: 7-30 days (random on game initialization)
- **Daily Check**: Timer decrements by 1 each day
- **Event Firing**: When timer reaches 0, the event selection process triggers

#### Base Timer Range

- **Minimum Days**: 20 (configurable via `timer_min_days`)
- **Maximum Days**: 30 (configurable via `timer_max_days`)
- **Default Range**: Events fire every 20-30 days under normal conditions

### Timer Modifiers

#### Minor Event Acceleration

When a minor event fires:

1. **Day Decrement Increase**: Adds +1 to decrement value (max: 15)
2. **Faster Next Event**: Subsequent timer will be reduced by current decrement
3. **Cumulative Effect**: Each minor event makes the next event fire sooner

#### Max Cap Reduction

Every 3 minor events that fire:

1. **Max Cap Reduction**: Reduces timer maximum by 1 day (max reduction: 5 days)
2. **Range Compression**: Timer range becomes more compressed over time
3. **Minimum Protection**: Range never goes below realistic values

#### Major Event Reset

When a major event fires:

1. **Full Reset**: Both day decrement and max cap reduction reset to 0
2. **Normal Timing**: Next event returns to standard 20-30 day range

### Example Timer Progression

#### Normal Progression

1. **Game Start**: Timer = 7-30 days (random)
2. **First Event**: Timer = 20-30 days (normal range)
3. **After Minor Event**: Timer = 19-29 days (decrement = 1)
4. **After 2nd Minor**: Timer = 18-28 days (decrement = 2)
5. **After 3rd Minor**: Timer = 17-26 days (decrement = 3, max reduced by 1)

#### Maximum Acceleration

After 15 minor events and max reductions:

- **Timer Range**: 20-25 days (base range with -5 max reduction)
- **Day Decrement**: -15 days
- **Effective Range**: 5-10 days between events

### Timer Variables

All timer behavior is controlled by global variables that can be modified:

- `timer_min_days`: Minimum timer range (default: 20)
- `timer_max_days`: Maximum timer range (default: 30)
- `timer_day_decrement`: Current day reduction (max: 15)
- `timer_max_cap_reduction`: Max range reduction (max: 5)
- `event_timer_days`: Current countdown timer

### Debug Information

The debug system tracks all timer-related information:

- Current timer countdown
- Timer range settings
- Current modifiers
- Timer calculation details

## Event Categories

### 1. Fire-Once Events

- **Behavior**: Fire exactly once per game
- **Weight After Firing**: 0 (permanently disabled)

### 2. Repeatable Events

- **Behavior**: Can fire multiple times with decreasing frequency
- **Weight After Firing**: 1 (minimum), recovers by 20 to reduced cap
- **Cap Reduction**: 50% per firing

### 3. Major Events

- **Initial Weight**: 0 (inactive until triggered)
- **Behavior**: Fire based on minor event accumulation. For each minor event, weight is increased by 200.
- **Weight After Firing**: 0, permanently for the fired event

---

## Chaos Meter

### Concept

A global "Chaos Meter" (0-1000+) that affects event firing patterns and enables special mechanics.

### Chaos Meter Effects

The chaos meter value directly influences:

- **Event Frequency**: Higher chaos reduces event timer through configurable global multipliers
- **Event Selection**: Chaos affects which events can trigger
- **Event Evolution**: Events evolve into more dangerous versions
- **Special Mechanics**: Various mechanics activate based on chaos thresholds
- **Tiers**:
  - 0-199 - Calm World
  - 200-399 - Gathering Storm
  - 400-599 - Rising Chaos
  - 600-799 - Chaos Tier
  - 800-1000 - Totalen Chaos
  - 1000+ - World Collapse
- **Max Value**: When chaos exceeds 1000, the system disables itself and displays "1000+". A world ending scenario will be triggered.

### Chaos Timer Modifier System

The chaos meter now uses a sophisticated global variable system to control timer reduction:

#### Global Timer Modifier Variables

- `global.chaos_timer_modifier_calm`: Timer multiplier for Calm World tier (default: 1.0)
- `global.chaos_timer_modifier_gathering_storm`: Timer multiplier for Gathering Storm tier (default: 0.9)
- `global.chaos_timer_modifier_rising_chaos`: Timer multiplier for Rising Chaos tier (default: 0.8)
- `global.chaos_timer_modifier_chaos_tier`: Timer multiplier for Chaos Tier (default: 0.7)
- `global.chaos_timer_modifier_totalen_chaos`: Timer multiplier for Totalen Chaos tier (default: 0.6)
- `global.chaos_timer_modifier`: Current active timer modifier based on chaos tier

#### Timer Calculation

1. **Base Timer**: Random value between min and max days
2. **Chaos Modifier**: Multiplied by current chaos tier modifier
3. **Rounding**: Always rounded up to ensure integer timer values
4. **Application**: Timer is reduced daily and triggers events when reaching 0

### Chaos Meter Influences

**Increases Chaos:**

- High world tension (integer percentage changes only)
- Wars, Annexations, Puppeting, etc
- Previous major events
- Population suffering

**Decreases Chaos:**

- Diplomatic successes (democracy)
- Peace agreements
- Free nations
- High stability
- International cooperation

---

## Event Evolution System

Events can transform into more dangerous versions when the Chaos Meter is high enough.

### Evolution Triggers

Event must reach required chaos level. Some evolutions require specific previous events

---

## Event Clusters

Instead of single events, multiple related events can fire in sequence. They are based on chance. The higher the danger level, more likely these event clusters will happen.

---

## Multiplayer Compatibility

- **Shared Pools**: Every player shares one event system
- **Synchronized Chaos**: Chaos Meter affects all players

---

## Event Chain Timers (Mini-Narratives)

### Concept

Events that create ongoing storylines with timed follow-ups based on player choices.

### Chain Mechanics

- **Timer Systems**: Events schedule future events
- **Choice Memory**: System remembers player decisions
- **Branching Paths**: Different choices lead to different outcomes
- **Escalation**: Ignored problems or wrong decisions make things worse over time

---

## Debug System

### Debug Logging

Comprehensive system for monitoring event mechanics:

```
====================================================
CHAOS REDUX EVENT SYSTEM DEBUG START NR [X]
====================================================

EVENTS FIRED:
Total events fired: [X]
Major events fired: [X]
Minor events fired: [X]
  - Minor repeatable events fired: [X]
  - Minor fire-once events fired: [X]

UNIQUE EVENTS:
Total events in system: [X]
Total unique events yet to be fired: [X]
  - Major events unfired: [X] / [X]
  - Minor fire-once events unfired: [X] / [X]
  - Minor repeatable events unfired: [X] / [X]

MAJOR EVENT WEIGHTS:
Minor events fired since last major: [X]
Current major event weight: [X]

REPEATABLE EVENTS DETAIL:
ID: [X], Name: [Event Name], Weight: [X], Cap: [X]
[... for each repeatable event]

DYNAMIC TIMER SYSTEM:
Timer range: [X] - [X] days
Day decrement: [X]
Max cap reduction: [X]
Current chaos tier: [X]
Current timer modifier: [X]

...

====================================================
CHAOS REDUX EVENT SYSTEM DEBUG END NR [X]
====================================================
```

### Debug Information Details

- **Weight Tracking**: Monitor all event weights and caps
- **Event History**: See all fired events and timing
- **Chaos Monitoring**: Track Chaos Meter changes and tier transitions
- **Timer System**: Monitor current chaos tier, active modifier, and all configured values
- **Chain Tracking**: Monitor active event chains

---

## Configuration Options

### Game Rules

Players can configure various aspects of the system:

#### Event System Settings

### Advanced Configuration

---
