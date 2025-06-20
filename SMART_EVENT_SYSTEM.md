# Chaos Redux Smart Event System

## Overview

The Smart Event System is a dynamic, weight-based event firing system with adaptive timing that provides better gameplay flow and intelligent event progression. The system features a daily timer that adapts based on event activity, creating a more responsive and engaging event experience.

## Features

### 1. Dynamic Timer System

- **Daily timer checks**: Events are evaluated every day instead of monthly intervals
- **Adaptive timing**: Timer intervals dynamically adjust based on recent event activity
- **Initialization**: First event timer is randomly set between 7-30 days at startup
- **Minor event acceleration**: Each minor event makes the next event fire 1 day sooner (cumulative)
- **Maximum acceleration**: Timer reduction is capped at 10 days maximum
- **Major event reset**: Major events reset all timer acceleration back to baseline

#### Timer Variables

- `global.event_timer_days`: Current countdown timer (decrements daily)
- `global.timer_day_decrement`: Current accumulated timer reduction from minor events
- `global.timer_max_cap_reduction`: Maximum allowed timer reduction (10 days)

### 2. Dynamic Weight-Based Event System

- **All events** Use variable weights from `global.event_weights` array for dynamic firing
- **Weight-based random selection**: Events with higher weights have higher chance of firing
- **Real-time weight adjustment**: Event probabilities change dynamically based on game state

### 3. Major Event Progression System

- **Major events** Start at weight 0 and increase by 100 per minor event fired
- **Unlimited scaling**: No caps on major event weights (they become increasingly likely)
- **Reset mechanism**: When a major event fires, all major event weights reset to 0

### 4. Minor Event Progression System

- **Fire-once events**: Start at weight 1000, become 0 permanently when fired
- **Repeatable events**: Start at weight 1000, drop to 0 when fired, recover +40/month until reaching new cap

### 5. System Initialization and Logging

During system startup, the following initialization steps occur:

1. **Variable Initialization**: All system variables are set to their default values
2. **Array Setup**: Event categorization arrays are populated with proper event IDs
3. **Weight Configuration**: Major events are set to weight 0, others to default weight 1000
4. **Timer Setup**: First event timer is randomly set between 7-30 days using `set_variable_to_random`
5. **Initialization Logging**: Three key log messages are written to the game log:
   - System initialization confirmation
   - Major event weight reset confirmation
   - First timer value announcement

#### Initialization Log Messages

```
CHAOS REDUX EVENT SYSTEM: System initialized successfully
CHAOS REDUX EVENT SYSTEM: Major event weights set to zero (inactive until triggered)
CHAOS REDUX EVENT SYSTEM: First event timer set to [X] days
```

### 6. Debug System

Comprehensive debug logging is available through the `log_event_system_debug` function, which provides:

- **Complete system state**: All variables and their current values
- **Timer information**: Current timer, accumulated reduction, and remaining time
- **Event statistics**: Total events fired, minor events since last major
- **Weight summaries**: Current weights for major, fire-once, and repeatable events
- **Array contents**: Current state of all tracking arrays

## Technical Implementation

### Files Involved

- `common/on_actions/chaosx_on_actions_events.txt`: Daily timer checks and event firing
- `common/scripted_effects/chaosx_effects_logic.txt`: Core system logic and timer calculations
- `events/chaosx_events.txt`: Individual event definitions and handlers

### Key Functions

- `initialize_event_system`: Complete system setup and initialization
- `check_event_timer`: Daily timer countdown and event triggering
- `calculate_next_timer_value`: Dynamic timer calculation based on event history
- `on_minor_event_timer_update`: Timer acceleration after minor events
- `on_major_event_timer_update`: Timer reset after major events
- `log_event_system_debug`: Comprehensive system state logging

## System Flow

1. **Initialization**: System starts up, sets random first timer (7-30 days)
2. **Daily Checks**: Timer decrements daily, events fire when timer reaches 0
3. **Event Selection**: Weighted random selection based on current event weights
4. **Timer Update**: After event fires, timer is recalculated based on event type:
   - Minor events: Reduce next timer by 1 day (cumulative, max 10 days)
   - Major events: Reset timer acceleration to baseline
5. **Weight Adjustment**: Event weights are updated based on firing results
6. **Repeat**: Process continues with new timer value

This creates a dynamic system where frequent minor events lead to faster event firing, while major events provide natural break points that reset the acceleration, maintaining balanced gameplay pacing.
