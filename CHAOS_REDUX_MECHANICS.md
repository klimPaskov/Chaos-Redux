# Chaos Redux: Complete Mechanics Guide

## Table of Contents

1. [Core Event System](#core-event-system)
2. [Smart Event Firing Logic](#smart-event-firing-logic)
3. [Event Categories](#event-categories)
4. [Chaos Meter (Danger Scaling)](#chaos-meter-danger-scaling)
5. [Event Evolution System](#event-evolution-system)
6. [Event Clusters & Party Nights](#event-clusters--party-nights)
7. [Multiplayer Compatibility](#multiplayer-compatibility)
8. [Event Chain Timers (Mini-Narratives)](#event-chain-timers-mini-narratives)
9. [Debug System](#debug-system)
10. [Configuration Options](#configuration-options)

---

## Core Event System

### Overview

Chaos Redux introduces an event system with a sophisticated, dynamic event firing mechanism that adapts to player actions, world state, and previous events.

### Key Features

- **Dynamic Event Weights**: Events become rarer after firing, recovering slowly over time
- **Intelligent Timing**: Major events fire based on minor event accumulation
- **Adaptive Difficulty**: System responds to world tension, stability, and chaos levels
- **Memory**: System tracks all fired events and adjusts future probabilities

---

## Smart Event Firing Logic

### Weight-Based System

Instead of pure randomness, events have **weight values** that determine firing probability:

- **Initial Weight**: 1000 (default for new events)
- **Weight Recovery**: +40 per month after firing
- **Weight Caps**: Individual caps per event, reduced by 25% each firing
- **Minimum Weight**: 1 (repeatable events can always fire, but become more rare)

### Event Selection Process

1. **Weight Calculation**: System calculates total weight of all eligible events
2. **Random Selection**: Weighted random selection picks an event
3. **Firing Logic**: Selected event fires and triggers appropriate handlers
4. **Weight Adjustment**: Fired event's weight drops, others remain unchanged

### Major vs Minor Event Logic

- **Minor Events**: Build up "pressure" in the system
- **Major Events**: Fire when enough minor events have occurred
- **Pressure Calculation**: Major event weight = (minor events since last major) × 100
- **Reset Mechanism**: Major event firing resets the minor event counter

---

## Event Categories

### 1. Fire-Once Events

- **Behavior**: Fire exactly once per game
- **Weight After Firing**: 0 (permanently disabled)

### 2. Repeatable Events

- **Behavior**: Can fire multiple times with decreasing frequency
- **Weight After Firing**: 1 (minimum), recovers to reduced cap
- **Cap Reduction**: 25% per firing

### 3. Major Events

- **Behavior**: Fire based on minor event accumulation
- **Initial Weight**: 0 (inactive until triggered)
- **Trigger Condition**: Sufficient minor events fired

---

## Chaos Meter (Danger Scaling)

### Concept

A global "Danger Meter" (0-1000+) that affects event firing patterns and enables special mechanics.

### Danger Level Tiers

#### 0-199: Calm World

- **Event Behavior**: Normal firing logic
- **Available Events**: Standard event pool
- **Special Mechanics**: None active
- **World State**: Usually peaceful, stable

#### 200-499: Rising Tension

- **Event Behavior**: Increased major event chances
- **Available Events**: More negative/challenging events
- **Special Mechanics**: Event probability modifiers active
- **World State**: Mounting pressure, political instability

#### 500-799: Instability

- **Event Behavior**: Weird/unexpected event spikes
- **Available Events**: Bizarre and dangerous events unlock
- **Special Mechanics**: Events evolve, cluster events
- **World State**: Reality becoming unstable

#### 800-1000: Chaos Tier

- **Event Behavior**: Event chains stack and compound
- **Available Events**: Major world-affecting events
- **Special Mechanics**: Full event evolution
- **World State**: World order collapsing

#### 1000+: World Collapse

- **Event Behavior**: Apocalyptic scenarios
- **Available Events**: 1984 scenario, alien invasions, supernatural events
- **Special Mechanics**: All systems active
- **World State**: Complete societal collapse. No turning back.

### Danger Meter Influences

**Increases Chaos:**

- High world tension
- Low national stability
- Active wars
- Previous major events
- Population suffering

**Decreases Chaos:**

- Diplomatic successes
- Peace agreements
- Economic prosperity
- High stability
- International cooperation

---

## Event Evolution System

Events can transform into more dangerous versions when the Chaos Meter is high enough.

### Evolution Triggers

Event must reach required danger level. Some evolutions require specific previous events

---

## Event Clusters & Party Nights

Instead of single events, multiple related events can fire in sequence during special "party nights." Events fire one after another. All events share common themes.

---

## Multiplayer Compatibility

### Shared Event System

Players can experience events together through two mechanisms:

#### Option 1: Ghost Events

- **Primary Receiver**: One player gets the full event with consequences
- **Ghost Recipients**: Other players see the event but choices do nothing
- **Visual Indicator**: Ghost events clearly marked as "observational"
- **Narrative Cohesion**: All players see the same world events

#### Option 2: Independent Events

- **Separate Pools**: Each player gets their own event system
- **Synchronized Chaos**: Chaos Meter affects all players equally
- **Cross-Player Effects**: Some events can affect other players' worlds

### Implementation

- **Host Configuration**: Game host chooses shared vs independent
- **Network Synchronization**: Event states synchronized across clients
- **Conflict Resolution**: System handles simultaneous event triggers
- **Save Game Compatibility**: Multiplayer event state preserved

---

## Event Chain Timers (Mini-Narratives)

### Concept

Events that create ongoing storylines with timed follow-ups based on player choices.

### Example Chain: "Mysterious Disappearance"

1. **Initial Event**: "General [Name] Disappears"

   - **Player Ignores**: Timer starts (30-90 days)
   - **Player Investigates**: Different chain path

2. **Follow-up Event**: "General Reappears with Rebel Army"
   - **Conditions**: If ignored + timer expired
   - **Consequences**: Civil war or uprising
   - **Severity**: Based on Chaos Meter level

### Chain Mechanics

- **Timer Systems**: Events schedule future events
- **Choice Memory**: System remembers player decisions
- **Branching Paths**: Different choices lead to different outcomes
- **Escalation**: Ignored problems become worse over time

### Common Chain Types

- **Political Intrigue**: Missing officials, corruption investigations
- **Military Affairs**: Desertion, rebellion, loyalty questions
- **Economic Issues**: Market manipulation, resource shortages
- **Supernatural**: Occult investigations, mysterious phenomena

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

...

====================================================
CHAOS REDUX EVENT SYSTEM DEBUG END NR [X]
====================================================
```

- **Weight Tracking**: Monitor all event weights and caps
- **Event History**: See all fired events and timing
- **Chaos Monitoring**: Track Chaos Meter changes
- **Chain Tracking**: Monitor active event chains

---

## Configuration Options

### Game Rules

Players can configure various aspects of the system:

#### Event System Settings

- **Event Frequency**: Adjust overall event firing rate
- **Major Event Threshold**: Change minor events required for major
- **Weight Recovery Rate**: Adjust how fast events recover
- **Chaos Sensitivity**: How much world events affect Chaos Meter

#### Multiplayer Settings

- **Event Sharing Mode**: Shared vs Independent events

### Difficulty Scaling

- **Chaos Accumulation Rate**: How fast Chaos Meter increases
- **Event Severity Scaling**: How much Chaos affects event intensity
- **Recovery Difficulty**: How hard it is to reduce Chaos
- **Apocalypse Threshold**: What Chaos level triggers end-game scenarios

---
