# Dynamic Major Event Weights

## Overview

Major events gain weight after minor global pacing events, but the per-minor gain is calculated from the current active random-event pool instead of using a fixed value. The configured setting remains the baseline gain. With the default baseline of `150`, 90 active non-major events and 10 active major events produce a current gain of `150`.

## Formula

```text
dynamic_major_gain = baseline_major_gain * (current_non_major_count / current_major_count) / (baseline_non_major_count / baseline_major_count)
```

The script uses the equivalent order:

```text
dynamic_major_gain = baseline_major_gain * current_non_major_count / current_major_count * baseline_major_count / baseline_non_major_count
```

Baseline constants live in `common/script_constants/event_system_constants.txt` under `event_system_dynamic_major_gain`:

- `baseline_total_events = 100`
- `baseline_major_events = 10`
- `baseline_non_major_events = 90`

The baseline gain is `global.major_event_weight_per_minor`, which is staged by the Advanced Settings value `global.settings_major_weight_per_minor` and defaults to `event_system_defaults.major_event_weight_per_minor`.

## Active Pool Counts

The active pool count only includes entries that can still participate in automatic random selection, before current weight is considered.

Excluded entries:

- disabled events in `global.disabled_events`
- fired non-repeatable events
- fired major events
- events whose shared automatic-pool availability resolver returns a dynamic unavailability reason, including locked Event 91, Holy Realm without a refuge host, Fury without a selectable country, unavailable Tensions Rising or White Peace, and unavailable Utopia, Brilliant Scientist, Secret Alliance, Cannibalism, Random Faction, Resources Found, Independence Wave, Africa Is One, or Black Plague states
- hidden helper, news, follow-up, bootstrap, scenario wrapper, or permanent-unavailable entries because they are not registered in the random-pool arrays

Repeatable events remain in the non-major count after firing while they remain active.

## Script Helpers

The event-system helpers live in `common/scripted_effects/chaosx_logic_effects.txt`. Their behavior and ownership are documented in this system file because they are private to random-event selection and major-weight pacing.

- `evaluate_random_event_active_pool_candidate`
- `evaluate_event_pool_candidate_unavailability`
- `count_dynamic_major_weight_pool_events`
- `calculate_dynamic_major_weight_gain`
- `apply_dynamic_major_weight_gain_after_minor`

`calculate_dynamic_major_weight_gain` stores the live result in `global.current_dynamic_major_weight_gain` and stores the counts in `global.current_dynamic_major_active_major_count` and `global.current_dynamic_major_active_non_major_count`. If either count is zero, the gain is set to `0`, so the script never divides by zero. The result is rounded with `round_temp_variable` and clamped to `settings_advanced_bounds.major_weight_per_minor`.

`update_major_event_weights` calls `apply_dynamic_major_weight_gain_after_minor`, which adds the calculated gain to active, unfired major events after one minor global pacing event. Major weights reset to `1` for engine safety, so the helper treats values below `2` as `0` before adding the gain.

## Cluster Pacing

Clusters still apply global pacing once. One-time and repeatable clusters count as one minor global pacing event, so `apply_dynamic_major_weight_gain_after_minor` runs once for the whole cluster. Member events fire in `event_cluster_member_fire_context`, which suppresses additional timer or major-gain updates.

Major clusters use the major pacing path and reset major weights once for the cluster.

## UI And Localisation

The Advanced Settings field is labelled as the baseline major gain. The Event Logs Status tab shows current calculated major gain and baseline major gain as separate lines, followed by accumulated major weight. Welcome-screen text describes both the configured baseline and the live calculated gain.

UI variables:

- `global.current_dynamic_major_weight_gain`
- `global.current_dynamic_major_active_major_count`
- `global.current_dynamic_major_active_non_major_count`
- `global.current_major_event_weight`
- `global.major_event_weight_per_minor`

## Icons And Assets

No new icons or sprites are required. Existing settings and event-log controls are reused.

## Future Plans

- Add a compact tooltip showing the active major and non-major counts directly in the Event Logs Status tab if the layout receives more space.
- Consider exposing the dynamic formula in a debug-only detail line for balancing sessions.
