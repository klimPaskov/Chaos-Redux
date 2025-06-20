# Chaos Redux Smart Event System

## Overview

The Smart Event System is a dynamic, weight-based event firing system that provides better gameplay flow and intelligent event progression.

## Features

### 1. Dynamic Weight-Based Event System

- **All events** Use variable weights from `global.event_weights` array for dynamic firing
- **Weight-based random selection**: Events with higher weights have higher chance of firing
- **Real-time weight adjustment**: Event probabilities change dynamically based on game state

### 2. Major Event Progression System

- **Major events** Start at weight 0 and increase by 100 per minor event fired
- **Unlimited scaling**: No caps on major event weights (they become increasingly likely)
- **Reset mechanism**: When a major event fires, all major event weights reset to 0

### 3. Minor Event Progression System

- **Fire-once events**: Start at weight 1000, become 0 permanently when fired
- **Repeatable events**: Start at weight 1000, drop to 0 when fired, recover +40/month until reaching new cap
