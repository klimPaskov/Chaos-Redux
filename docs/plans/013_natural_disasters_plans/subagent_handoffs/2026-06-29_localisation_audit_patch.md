# Event 013 localisation audit patch handoff

## Scope

Audited Event 013 Natural Disasters localisation and scripted localisation surfaces named by the parent prompt.

## Files changed

- `localisation/english/013_natural_disasters_l_english.yml`
- `localisation/english/chaosx_achievements_l_english.yml`
- `docs/events/013_natural_disasters.md`

## Keys changed

- `chaosx.nr13.21.tt`
- `nd_cost_evacuation_text`
- `nd_cost_engineers_text`
- `nd_cost_relief_text`
- `nd_cost_shelter_text`
- `nd_famine_displacement_open_food_columns_tt`
- `nd_famine_displacement_shelter_refugee_columns_mission_failure_tt`
- all `nd_*_tt` warning preparation keys that used the repeated final dynamic loss-rate sentence
- all `nd_*_mission_failure_tt` keys that used the repeated current-state-population aftermath sentence
- `achievement_nd_prepared_capital_tooltip`
- `achievement_nd_global_relief_tooltip`

## Behavior before and after

Before, several decision and event tooltips described the internal loss-rate model, fixed casualty avoidance, or hidden thresholds directly. Cost labels also used prose `Requires...` phrasing.

After, those strings describe public disaster effects, preparedness, civilian danger, relief movement, and compact resource categories without exposing formulas or hidden cutoffs. The gameplay triggers and costs were not changed.

## Dynamic localisation

No new scripted localisation was added. The existing Event 13 scripted localisation references resolved against the scoped English keys during the audit.

## Validation

- Checked scoped English localisation files for duplicate keys. Result: none found.
- Checked Event 13 relevant script references against English localisation keys. Result: no missing Event 13 keys found.
- Checked scoped English localisation files for forbidden `:0` keys. Result: none found.
- Checked touched localisation files for UTF-8 BOM after patching. Result: BOM remains present.
- Checked scoped scripted localisation files for raw `§` or `£` format symbols. Result: none found.
- Checked Event 13 scoped prose for em dashes and semicolons. One semicolon remains in shared Chaos Meter prose, `chaos_meter.window.status.mechanics_body`, outside the Event 13 introduced text and left unchanged.

## Remaining risks

- Event 13 cost labels still summarize resource families rather than printing exact dynamic quantities. A fuller cost display would need a small scripted localisation pass or cost-display variables owned by the decision or scripted-system agent.
- Shared Chaos Meter prose has an unrelated semicolon outside the Event 13 surface. It was not patched because the parent prompt asked not to rewrite unrelated shared Chaos Meter prose.
