# Welcome Screen Description

## Overview

The welcome screen description now reads from live variables and constant-backed values instead of hardcoded copy.

It shows:

- current event-pool totals,
- the player country's opening timer roll and active timer window,
- live event-system tuning values,
- live chaos-tier ranges and timer multipliers,
- script-backed examples of chaos gains and reductions.

## Data Flow

1. `common/on_actions/chaosx_on_actions_system.txt` calls `initialize_welcome_screen_values` during `on_startup` after the event system, chaos meter, and global settings are initialized.
2. `common/scripted_effects/chaosx_welcome_effects.txt` copies the required script constants and initialized live values into `global.welcome_*` variables.
3. `localisation/english/chaosx_events_l_english.yml` reads those values directly in the welcome-screen description text.
4. Country-scoped timer values such as `event_timer_days`, `timer_min_days`, `timer_max_days`, `timer_min_decrement_cap`, and `timer_max_decrement_cap` are still read from the active player country.

## Shared Tuning

Welcome text values come from:

- `common/script_constants/event_system_constants.txt`
- `common/script_constants/chaos_meter_constants.txt`
- initialized live globals from `common/scripted_effects/chaosx_logic_effects.txt`
- initialized live globals from `common/scripted_effects/chaos_meter_effects.txt`

New welcome-specific display variables are only mirrors for localisation. They do not define gameplay logic themselves.

## Existing UI Assets

No new sprites are required for this update.

Existing welcome-screen assets remain:

- Background sprite file: `gfx/interface/chaosx_welcome_bg.dds`
- Title sprite file: `gfx/interface/chaosx_welcome_title.dds`
- Button sprite files:
  - `gfx/interface/discord_button.dds`
  - `gfx/interface/donation_button.dds`
  - `gfx/interface/homepage_button.dds`
  - `gfx/interface/github_button.dds`
  - `gfx/interface/documentation_button.dds`

These are registered in:

- `interface/chaosx.gfx`

The screen layout remains in:

- `interface/chaosx_welcome.gui`

## Future Plans

- Move any additional welcome-screen numeric copy to script constants before it is surfaced in localisation.
- If the welcome screen later gets tabbed content, keep all overview numbers sourced from the same `global.welcome_*` mirror variables or direct live state.
