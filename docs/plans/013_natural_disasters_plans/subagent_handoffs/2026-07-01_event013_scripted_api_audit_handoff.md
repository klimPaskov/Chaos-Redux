# Event 013 Scripted API Audit Handoff

## Files Changed

- `common/scripted_effects/013_natural_disasters_effects.txt`
- `docs/events/013_natural_disasters.md`

## Surface Audited

- Immediate no-log helpers:
  - `natural_disasters_call_immediate_family`
  - `natural_disasters_call_immediate_targeted_state_family`
  - `natural_disasters_call_immediate_targeted_country_family`
  - `natural_disasters_call_immediate_regional_family`
  - `natural_disasters_call_immediate_world_family`
- Delayed direct helpers:
  - `natural_disasters_call_direct_family`
  - `natural_disasters_call_targeted_state_family`
  - `natural_disasters_call_targeted_country_family`
  - `natural_disasters_call_regional_family`
  - `natural_disasters_call_world_family`
- Shared target loading, report scheduling, follow-up scheduling, and SCN-007/cluster entry paths.

## Behavior Before

Immediate no-log calls used `natural_disaster_sequence_slot = 9` and avoided delayed slot cleanup and follow-up scheduling. They still scheduled direct reports through the single global event target `natural_disaster_direct_report_state`.

If two immediate no-log calls scheduled direct reports before the first report event fired, the later call could overwrite `natural_disaster_direct_report_state`. That could make the first report show the wrong state or leave a later scheduled report with no target after the target was cleared.

## Behavior After

`natural_disasters_should_schedule_report` suppresses a slot 9 report when `natural_disaster_direct_report_state` is already pending. The immediate disaster still applies target validation, damage, deaths, recovery, news checks, and `natural_disaster_direct_call_success`, but it does not overwrite the pending direct report target.

The event documentation now records that immediate direct reports have one pending target and are suppressed while that target is waiting.

## Why This Is Bounded

The change only reads the existing slot 9 marker and existing direct report event target. It does not alter delayed sequence slot allocation, delayed report targets, family selection, target validation, follow-up assignment, SCN-007 barrage setup, event cluster firing, or Event Log recording.

## Validation

- Traced immediate helpers into `natural_disasters_select_target`, `natural_disasters_apply_family_to_target`, `natural_disasters_schedule_report`, and `natural_disasters_schedule_followups`.
- Verified SCN-007 still enters through `natural_disasters_start_disaster_barrage` and delayed slot allocation.
- Verified event clusters queue Event 013 member seasons through the normal event firing path, not the slot 9 helpers.
- Checked touched Event 013 scripts for unsupported `<=` or `>=` operators.

## Remaining Risks

- `natural_disaster_news_state` is still a single global news target shared by all Event 013 news events. Existing cooldown logic throttles news heavily, but the target is not cleared by news options in `events/013_natural_disasters.txt`. That file was outside this audit's write scope.
- The direct report API intentionally supports one pending direct report at a time. A future broader patch could add multiple direct report slots if callers need several simultaneous immediate reports.
