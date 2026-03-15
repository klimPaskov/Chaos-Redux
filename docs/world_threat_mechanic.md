# World Threat Mechanic

## Overview

`world_in_threat` is the shared global flag for Chaos Redux's existential-threat state.
It is not zombie-specific.

The purpose of the mechanic is to give other systems one clean hook for "the world is facing a large external threat right now, so normal geopolitical behavior should calm down and cooperation logic should be favored instead."

The framework is source-based:

- each major threat owns its own source flag
- the shared world-threat effect aggregates all active source flags
- if at least one source is active, the world is considered under threat

Current registered source flags:

- `world_threat_source_zombies`

Shared aggregate flag:

- `world_in_threat`

Shared bookkeeping variable:

- `global.world_threat_source_count`

## How it works

### 1. Threat sources

Each threat system decides for itself when it should count as a world threat.

For the zombie system, the source activates only when:

- the Anti-Zombie League exists
- the zombie outbreak system is still active
- the outbreak has not been disabled
- zombie pressure is already strong enough to justify global emergency behavior

Zombie strength is currently considered strong when either:

- total zombie divisions are at least `constant:anti_zombie_league.emergency_divisions`
- zombies have reached continent-scale control according to the existing Anti-Zombie League continent-pressure logic

If those conditions stop being true, the zombie source flag is cleared.

### 2. Aggregate refresh

`refresh_world_threat_state` in `common/scripted_effects/chaosx_dynamic_effects.txt` rebuilds the threat count from all registered source flags.

Current flow:

1. reset `global.world_threat_source_count` to `0`
2. add `1` for each active registered source flag
3. set `world_in_threat` if the count is above `0`
4. clear `world_in_threat` if the count is `0`

This keeps the high-level flag generic and future-proof.

### 3. Zombie integration

The zombie source uses `refresh_zombie_world_threat_source` in `common/scripted_effects/002_zombie_outbreak_effects.txt`.

That effect:

1. recalculates total zombie strength
2. recalculates continent presence
3. sets or clears `world_threat_source_zombies`
4. calls `refresh_world_threat_state`

The zombie source is refreshed from:

- the existing `ZZZ` daily outbreak runtime
- Anti-Zombie League formation
- Anti-Zombie League disband
- zombie-system shutdown

This means the flag stays live while the zombie campaign is active, and is also cleared immediately when the league or the outbreak system collapses.

## Script API

Shared effects:

- `refresh_world_threat_state`
- `refresh_zombie_world_threat_source`

Shared triggers:

- `is_world_in_threat`
- `has_world_threat_source_zombies`

## Adding future threats

When another existential threat is added later, the intended pattern is:

1. create a source flag such as `world_threat_source_aliens`
2. write a threat-specific refresh effect that decides when that source should be active
3. extend `refresh_world_threat_state` with one more source-flag count block
4. call the threat-specific refresh effect from that threat's own runtime hooks

Do not create a second independent global "world crisis" flag.
Everything should fold back into the same source-counted system.

## Limitations

- The current zombie source is refreshed from the existing zombie runtime rather than a dedicated global state-control hook. In practice that is good enough for the active zombie system, but it is still tied to zombie runtime execution rather than a universal threat bus.
- Only zombies are registered right now, so the framework is generic by structure but not yet by population.
- `world_in_threat` is intentionally just a state flag. It does not itself enforce diplomacy or AI behavior. Other systems must explicitly read it.

## Files

- `common/scripted_effects/chaosx_dynamic_effects.txt`
- `common/scripted_effects/chaosx_dynamic_effects.md`
- `common/scripted_effects/002_zombie_outbreak_effects.txt`
- `common/scripted_triggers/chaosx_world_threat_triggers.txt`
- `common/on_actions/chaosx_on_actions.txt`
- `common/decisions/chaosx_anti_zombie_league_decisions.txt`

## Icon Wiring

No new icons or audio are required for the current framework.

## Future Plans

- Add event-log or debug visibility for active world-threat sources if multi-threat overlap becomes common.
- Add a shared opinion or AI utility layer that threat-aware systems can reuse instead of each one re-implementing "cooperate more under threat".
- If multiple threat systems become very state-driven, move refresh calls onto a more centralized event-driven hook rather than per-threat runtime loops.
