# Event Chaos Levels

## Purpose

Every registered normal Chaos Redux event has a minimum global Chaos tier for automatic selection.

The requirement is an event property and does not replace its enabled state, normal availability trigger, fire-once or repeatable state, weight, cap, recovery state, or cluster membership.

## Levels

The player-facing levels use the existing six Chaos tiers:

| Chaos level | Existing tier ID | Tier name |
| --- | --- | --- |
| 1 | `constant:chaos_meter_tier_id.tier_0` | Calm World |
| 2 | `constant:chaos_meter_tier_id.tier_1` | Gathering Storm |
| 3 | `constant:chaos_meter_tier_id.tier_2` | Rising Chaos |
| 4 | `constant:chaos_meter_tier_id.tier_3` | Chaos Tier |
| 5 | `constant:chaos_meter_tier_id.tier_4` | Totalen Chaos |
| 6 | `constant:chaos_meter_tier_id.tier_final` | World Collapse |

The registry stores the existing zero-based tier IDs and presents them as one-based Chaos levels.

## Registry And Lookup

`initialize_event_chaos_level_registry` rebuilds `global.event_chaos_level_entries` in the same order as `global.all_events`.

Every registered event receives an aligned entry.

An event without a specific assignment receives Calm World through `constant:chaos_meter_tier_id.tier_0`.

`get_event_required_chaos_level` resolves the registered tier for the current temporary `event_id`, and `event_required_chaos_level_is_met` compares it with the existing global `chaos_tier` state.

## Automatic Selection

The shared active-pool evaluator resolves the event requirement before a candidate contributes selectable weight.

An automatic candidate remains eligible only when its event toggle, normal event trigger and target requirements, fire history, weight state, event Chaos level, and every other existing selection rule all permit firing.

When the current tier is below the requirement, the event contributes no selectable weight without writing zero into `global.event_weights`.

Repeatable recovery also skips the locked event, so its stored weight, maximum cap, and recovery position remain unchanged until the required tier returns.

Major-event growth skips a locked major through the same active-pool eligibility helper.

The lock does not mark the event fired, change its cap, advance the event timer, or add major-event weight.

Crossing the threshold makes the event eligible on the next normal evaluation, and falling below it restores the temporary lock without erasing persistent event state.

## Event And Cluster Requirements

Event Chaos levels and cluster unlock tiers remain independent gates.

The normal picker must first select an event that meets its own requirement.

If that selected event belongs to a cluster, the cluster system then checks its own unlock tier, member-specific minimum tiers, cooldown, participation, runtime context, and other availability rules.

The effective automatic threshold is therefore the strictest requirement reached by the event, cluster, and participating member.

Event 9, White Peace, requires Gathering Storm even though the Peace cluster unlocks at Calm World.

The Peace cluster cannot enter automatically through White Peace during Calm World.

## Manual Triggering

Normal manual event firing from Settings, the Event Details trigger button, and the Events-tab bulk trigger respects the event Chaos level in addition to the existing manual readiness checks.

Force Trigger Mode may bypass the event Chaos-level requirement together with the other restrictions it already bypasses.

Manual cluster forcing keeps its existing separate bypass behavior.

Triggerable scenarios remain separate from normal event eligibility and do not read the event Chaos-level gate.

## Event Details And Events Tab

Event Details shows the exact numeric Chaos level with its existing tier colour, while an Events-tab row shows `Chaos lvl: <number>` beside Weight on its top line.

The Events tab keeps the enabled checkbox independent from Chaos availability.

When the current tier is too low, the row shows `N/A` instead of selectable weight and its hover tooltip reports the required tier name in red. Other automatic-pool gates use the same hover line to report their first unmet requirement.

The existing Events-tab filter cycles through the original event filters and six exact Chaos-level filters.

The rebuilt Events view carries the event Chaos tier in an aligned array, so filtering and sorting cannot associate one event with another event's requirement.

## Event 1-20 Assignments

| Event ID | Event | Chaos level |
| --- | --- | --- |
| 1 | Communist Insurgency | 1, Calm World |
| 2 | Zombie Outbreak | 1, Calm World |
| 3 | The Holy Realm | 1, Calm World |
| 4 | Random War | 1, Calm World |
| 5 | Soviet Union Collapse | 1, Calm World |
| 6 | Independence Wave | 1, Calm World |
| 7 | Fury | 1, Calm World |
| 8 | Tensions Rising | 1, Calm World |
| 9 | White Peace | 2, Gathering Storm |
| 10 | Death | 1, Calm World |
| 11 | Secret Alliance | 1, Calm World |
| 12 | Africa | 1, Calm World |
| 13 | Natural Disasters | 1, Calm World |
| 14 | Cannibalism | 1, Calm World |
| 15 | Utopia Manifesto | 1, Calm World |
| 16 | Brilliant Scientist | 1, Calm World |
| 17 | Random Faction | 1, Calm World |
| 18 | Resources Found | 1, Calm World |
| 19 | Infantry Spawn | 1, Calm World |
| 20 | Black Plague | 1, Calm World |

## Icons And Assets

No new icon or bitmap asset is required.

The feature reuses the existing Event Details window, Events-tab rows, checkboxes, buttons, fonts, and Chaos tier colours.

No new sprite registration or `.gfx` entry is required.

## Files

- `common/scripted_effects/chaosx_logic_effects.txt`
- `common/scripted_effects/chaosx_settings_effects.txt`
- `common/scripted_effects/chaosx_events_log_effects.txt`
- `common/scripted_triggers/chaosx_settings_triggers.txt`
- `common/scripted_guis/chaosx_scripted_gui_settings.txt`
- `common/scripted_guis/chaosx_scripted_gui_events_log.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_settings.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `localisation/english/chaosx_gui_l_english.yml`
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
- `docs/spreadsheets/chaos_redux_events_catalog.csv`
- `.tools/export_event_catalog_csv.py`

## Future Plans

- Assign higher event Chaos levels as more registered events receive completed balance and progression reviews.
- Add Chaos level as an optional Events-tab sort mode if the catalogue grows enough for that ordering to become useful.
- Add a compact locked-reason icon only if future Event Details metadata can no longer present the tier status clearly.
