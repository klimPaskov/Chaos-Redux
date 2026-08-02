# Event 088 Mines Everywhere

Event 088 selects one curated sea strategic region and adds a large minefield there for every country through the event's existing meta effect.

## Runtime flow

1. `chaosx.nr88.1` calls `get_random_sea_region` from its hidden option effect.
2. The helper stores the selected strategic-region ID in `global.rand_sea_region`.
3. The event injects that numeric ID into `add_mines` through `meta_effect`.

## Event-owned helper

`get_random_sea_region` lives in `common/scripted_effects/088_mines_effects.txt` because Event 088 is its only caller.

Scope: any scope.

Inputs: none.

Output: `global.rand_sea_region`.

Defaults: none. Every random-list branch writes one curated sea-region ID.

Side effects: no state beyond replacing `global.rand_sea_region`. Repeated region entries retain the existing Event 088 weighting and were preserved during the ownership move.

Example:

```txt
hidden_effect = { get_random_sea_region = yes }
```

## Assets

The event continues to use `GFX_report_event_minelaying`. No new icons or sprites are required.

## Future plans

If the strategic-region map changes, audit the curated ID list against the installed game map before changing weights or adding regions.
