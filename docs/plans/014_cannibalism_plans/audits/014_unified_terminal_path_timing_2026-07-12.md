# Event 014 unified terminal-path timing audit

## Result

The post-reveal unified tree uses the following focus-cost cadence:

- short: 3 focus-cost units, or 21 days
- normal: 5 focus-cost units, or 35 days
- terminal: 8 focus-cost units, or 56 days

A graph walk of `common/national_focus/014_cannibalism_unified_focus.txt` treated separate `prerequisite` blocks as cumulative requirements and multiple `focus` entries inside one block as alternatives. It also rejected combinations that contained mutually exclusive route focuses.

The least-time valid route to `CBL_final_global_mobilization` contains 54 distinct focuses and takes 1,505 days, or 4.12 years. Completing `CBL_dismantle_the_ordinary_world` raises that to 55 focuses and 1,561 days, or 4.28 years.

The focus clock is not the terminal gate by itself. The same route still requires:

- five successful Larder operations
- five Cannibal Legions, one Bone Guard, and five army operations
- five prepared campaigns, three postwar integrations, and five cell operations
- five counterwar operations
- all global territory, population-consumption, Network Reach, Larder, and strict Chaos-greater-than-1000 conditions
- a completed final population levy before the terminal focus can fire the world-end transaction

This keeps the terminal route deliberately long and resource-intensive while allowing it to resolve within a late-game campaign rather than consuming almost the entire remaining scenario through focus time alone.

## Additional path samples

- `CBL_host_theaters_without_borders`: 27 focuses, 672 days
- `CBL_consume_the_counterwar`: 31 focuses, 819 days
- `CBL_final_global_mobilization`: 54 focuses, 1,505 days
- `CBL_dismantle_the_ordinary_world`: 55 focuses, 1,561 days

## Remaining audit dependency

The final focus-tree re-audit must be run after the unified focus-contract consumers and player-facing terminal requirement text are complete.
