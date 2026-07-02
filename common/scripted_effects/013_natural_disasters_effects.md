# Event 013 Natural Disasters Scripted Effect API

This file documents the reusable Natural Disasters helpers in `common/scripted_effects/013_natural_disasters_effects.txt`. They let other events launch a delayed disaster season or apply one specific disaster family without copying Event 013 damage, deaths, aftermath, recovery, news, or targeting logic.

## Scope

Call these helpers from a country or event effect chain. Targeted calls use regular event targets saved in the same chain:

- `natural_disasters_direct_target_state`
- `natural_disasters_direct_target_country`

## Common Inputs

- `natural_disasters_start_family`: family constant from `natural_disaster_family`.
- `natural_disasters_start_target_mode`: target mode constant from `natural_disaster_target_mode`.
- `natural_disasters_start_report_policy`: policy constant from `natural_disaster_report_policy`.
- `natural_disasters_start_recovery_allowed`: `1` opens recovery hooks, `0` suppresses them.
- `natural_disasters_start_deaths_allowed`: `1` routes deaths through the Deaths system, `0` suppresses them.
- `natural_disasters_start_super_event_allowed`: `1` allows abnormal super-events, `0` suppresses them.
- `natural_disasters_start_total`: optional delayed sequence pulse count.
- `natural_disasters_start_delay_min` and `natural_disasters_start_delay_max`: optional delayed cadence bounds.

## Delayed Season Helpers

- `natural_disasters_start_sequence = yes`: starts a normal delayed season from the current context.
- `natural_disasters_call_direct_family = yes`: starts a delayed one-pulse no-log Event 013 disaster season.
- `natural_disasters_call_targeted_state_family = yes`: uses `natural_disasters_direct_target_state`.
- `natural_disasters_call_targeted_country_family = yes`: uses `natural_disasters_direct_target_country`.
- `natural_disasters_call_regional_family = yes`: uses `natural_disasters_direct_target_state` as a regional seed.
- `natural_disasters_call_world_family = yes`: selects a valid world target.
- `natural_disasters_call_direct_sandstorm = yes`: compatibility wrapper for old sandstorm call sites.
- `natural_disasters_start_disaster_barrage = yes`: launches SCN-007 through the same controller.

Delayed helpers allocate sequence slots and schedule hidden follow-up events. They do not create separate Event Log entries for individual disaster pulses.

## Immediate No-Log Helpers

- `natural_disasters_call_immediate_family = yes`
- `natural_disasters_call_immediate_targeted_state_family = yes`
- `natural_disasters_call_immediate_targeted_country_family = yes`
- `natural_disasters_call_immediate_regional_family = yes`
- `natural_disasters_call_immediate_world_family = yes`

Immediate helpers apply one family pulse immediately through slot `9`, which is reserved outside the delayed season slots. They set `natural_disaster_direct_call_success` to `1` when a valid target is found and `0` when no valid target exists.

## Side Effects

Successful calls can damage buildings, register civilian deaths through the Deaths system, apply state dynamic modifiers, open recovery decisions, update country disaster-pressure ideas, schedule reports, and send throttled specific-disaster news. Use `natural_disasters_start_report_policy = constant:natural_disaster_report_policy.quiet` when the caller owns its own visible follow-up.

## Examples

Delayed targeted tsunami:

```txt
random_controlled_state = {
	limit = { natural_disaster_target_tsunami = yes }
	save_event_target_as = natural_disasters_direct_target_state
}
set_temp_variable = { natural_disasters_start_family = constant:natural_disaster_family.tsunami }
set_temp_variable = { natural_disasters_start_report_policy = constant:natural_disaster_report_policy.important }
natural_disasters_call_targeted_state_family = yes
```

Immediate no-log flood:

```txt
random_controlled_state = {
	limit = { natural_disaster_target_flood = yes }
	save_event_target_as = natural_disasters_direct_target_state
}
set_temp_variable = { natural_disasters_start_family = constant:natural_disaster_family.flood }
set_temp_variable = { natural_disasters_start_report_policy = constant:natural_disaster_report_policy.quiet }
natural_disasters_call_immediate_targeted_state_family = yes
```

Scenario barrage:

```txt
set_temp_variable = { natural_disasters_start_scenario_intensity = constant:triggerable_scenario_intensity.maximum }
set_temp_variable = { natural_disasters_start_family = constant:natural_disaster_family.meteor_shower }
natural_disasters_start_disaster_barrage = yes
```
