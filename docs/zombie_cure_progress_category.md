# Zombie Cure Progress Category

## Overview

The base zombie cure decision category now shows cure progress directly in the category itself.

It uses a bottle-fill icon set with eleven states:

- `0%`
- `10%`
- `20%`
- `30%`
- `40%`
- `50%`
- `60%`
- `70%`
- `80%`
- `90%`
- `100%`

The category reads the same cure values already used by the cure decisions:

- if the country is in `cure_sharing`, it reads `global.zzz_cure`
- otherwise it reads the country's local `zzz_cure`

This means the bottle always reflects the actual cure progress relevant to the current country.

The category also shows a live text panel beside the bottle, covering:

- current cure progress
- whether research is national or shared
- the activation threshold
- the cure duration after activation
- a reminder that evolved zombie outbreaks require more research effort

## Wiring

### Category UI selection

The category is assigned in:

- `common/decisions/categories/chaosx_decisions_categories.txt`

The category uses a decision-category scripted GUI instead of unsupported triggered icon syntax:

- `common/scripted_guis/chaosx_scripted_guis.txt`
- `interface/chaosx_decisions.gui`
- `common/scripted_localisation/chaosx_scripted_localisation.txt`

The scripted GUI:

- draws the bottle on the left side of the category
- swaps the bottle sprite at each ten-percent threshold
- shows live cure-status text on the right

### Sprite definitions

The sprite definitions are registered in:

- `interface/chaosx_decisions.gfx`

Sprite names used by the category:

- `GFX_decision_category_zombies_cure_0`
- `GFX_decision_category_zombies_cure_10`
- `GFX_decision_category_zombies_cure_20`
- `GFX_decision_category_zombies_cure_30`
- `GFX_decision_category_zombies_cure_40`
- `GFX_decision_category_zombies_cure_50`
- `GFX_decision_category_zombies_cure_60`
- `GFX_decision_category_zombies_cure_70`
- `GFX_decision_category_zombies_cure_80`
- `GFX_decision_category_zombies_cure_90`
- `GFX_decision_category_zombies_cure_100`

### Art files

The category currently expects these files:

- `gfx/interface/decisions/zombie_cure/zombie_cure_0.dds`
- `gfx/interface/decisions/zombie_cure/zombie_cure_10.dds`
- `gfx/interface/decisions/zombie_cure/zombie_cure_20.dds`
- `gfx/interface/decisions/zombie_cure/zombie_cure_30.dds`
- `gfx/interface/decisions/zombie_cure/zombie_cure_40.dds`
- `gfx/interface/decisions/zombie_cure/zombie_cure_50.dds`
- `gfx/interface/decisions/zombie_cure/zombie_cure_60.dds`
- `gfx/interface/decisions/zombie_cure/zombie_cure_70.dds`
- `gfx/interface/decisions/zombie_cure/zombie_cure_80.dds`
- `gfx/interface/decisions/zombie_cure/zombie_cure_90.dds`
- `gfx/interface/decisions/zombie_cure/zombie_cure_100.dds`

## First Activation Achievement

The first country to activate the zombie cure now receives a one-time achievement flag.

This is centralized in:

- `common/scripted_effects/002_zombie_outbreak_effects.txt`

The shared activation logic:

- marks the first cure activation globally
- grants the achievement flag only to the country that actually triggered that first activation
- preserves the existing cure durations:
  - `120` days for cure-sharing activation
  - `360` days for solo activation

## Files

- `common/decisions/categories/chaosx_decisions_categories.txt`
- `common/decisions/chaosx_zzz_cure_decisions.txt`
- `common/scripted_guis/chaosx_scripted_guis.txt`
- `common/scripted_localisation/chaosx_scripted_localisation.txt`
- `common/scripted_effects/002_zombie_outbreak_effects.txt`
- `common/achievements/chaos_redux_achievements.txt`
- `interface/chaosx_decisions.gui`
- `interface/chaosx_decisions.gfx`
- `localisation/english/chaosx_decisions_l_english.yml`
- `localisation/english/chaosx_achievements_l_english.yml`

## Future Work

- Add custom achievement art for the first-activation cure achievement instead of using a placeholder DDS set.
