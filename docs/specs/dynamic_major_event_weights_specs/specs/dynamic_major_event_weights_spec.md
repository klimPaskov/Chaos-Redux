# Dynamic Major Event Weight Gain Spec

## Status

Implemented; the [event-system document](../../../systems/event_system/dynamic_major_event_weights.md) records the helpers, variables, UI and cluster behaviour.
No attributable acceptance record exists for this design, so acceptance remains unresolved; implementation evidence proves existence, not approval.
The 10 Oct 2026 spec audit reviewed the design and retained it unchanged (see the revision log).

## Purpose

After each minor pacing event, every active unfired major event gains weight.
The gain scales with the active pool so that the combined chance of a major event per roll stays stable as events fire, are disabled or are added.
The configured `Major Event Weight` setting is the baseline gain at the baseline ratio of 90 non-major to 10 major events.

## Formula

```text
dynamic_major_gain = baseline_major_gain * (current_non_major_count / current_major_count) / (baseline_non_major_count / baseline_major_count)
```

Baselines live in `common/script_constants/event_system_constants.txt` (`event_system_dynamic_major_gain`): 100 total, 10 major, 90 non-major.
The baseline gain is the player's setting (default 150), never a hard-coded value.

| Active major | Active non-major | Gain at baseline 150 |
| ---: | ---: | ---: |
| 10 | 90 | 150 |
| 10 | 91 | about 152 |
| 9 | 91 | about 169 |
| 11 | 90 | about 136 |

The total weight added across all majors per minor event is `gain × majors`, which equals `baseline × non-majors / 9`; fewer remaining majors each grow faster, so the last majors are not starved.

## Counting rules

Counts use the live random-pool registry: one entry per source event, regardless of its reports, helpers or follow-ups.
The pool owner decides participation; this feature consumes that decision and never creates a second eligibility registry.

- Major count: enabled, unfired majors that the pool owner still treats as available.
- Non-major count: enabled minor repeatables, unfired minor fire-once events and non-major cluster member sources that remain in the pool.
- Excluded: disabled events, fired majors, fired fire-once minors, events whose availability resolver reports a dynamic unavailability reason, and anything that is not a pool entry (hidden helpers, news, follow-ups, bootstrap events, scenario wrappers).
- A repeatable at low recovering weight still counts.
- A temporary owner-controlled suspension is not permanent removal; reenabling follows the owner.

## Safety

If either count is zero, the gain is zero and nothing divides by zero.
The result is rounded and clamped to the setting's bounds.

## Timing

The gain is calculated at the existing minor pacing receipt, after the firing's own membership changes, and applied once.
Status and settings displays recalculate for reading only: they never apply gain, change weights or activate pending events.
No daily recalculation is added.

## Clusters and delayed activation

A cluster firing is one pacing event and applies the gain once; member reports add none.
A Major trigger takes the major pacing path instead.
Random Stuff's bonus batch adds no second gain because its opening minor event already paid it.

[Event 026's reservation and lifecycle](../../026_black_friday_specs/026_black_friday_spec_part_2_friday_reservation_and_lifecycle.md#event-system-pacing) supplies the delayed-activation case.
Reservation removes Black Friday from live selection without a firing or a gain; another minor fired meanwhile pays its own gain from current membership.
Eligible Friday activation supplies one normal fire-once pacing receipt using the pool at activation; its hidden activation, report and expiry roles add none.
Cancellation or a below-threshold Friday adds none, and the helper never activates the sale or resets its timer.

## Player-facing values

The Advanced Settings field is the baseline major gain.
The Event Logs Status tab shows the current calculated gain beside the baseline and the accumulated major weight; nothing else about the formula is exposed.
Text never promises a fixed gain per minor event.

## Validation scenarios

| Case | Expected result |
| --- | --- |
| 90 non-major, 10 major | 150 at baseline 150 |
| 91 non-major, 10 major | About 152 |
| 90 non-major, 11 major | About 136 |
| 91 non-major, 9 major | About 169 |
| 0 active majors or 0 active non-majors | Gain 0, no division |
| Disabled, fired major and fired fire-once minor events | Excluded from counts |
| Repeatable at low recovering weight | Still counted |
| Cluster firing | One gain for the whole batch |
| `dmg_pool_membership` | Temporary exclusions and reenabling follow the pool owner without permanent removal |
| `dmg_black_friday_wait` | Reservation removes only Event 026, gives no gain, and does not block another minor's gain |
| `dmg_black_friday_activate` | Activation records one gain from the activation-time pool |
| `dmg_black_friday_cancel` | Cancellation and below-threshold Fridays give no gain |
| `dmg_readonly_status` | Opening status displays applies no gain and changes no weights |

These are validation scenarios, not executed probability evidence.
Any future change to the weighted source goes through `chaosx_ai_probability_auditor` with matching before and after scenarios.

## Revision log

### 2026-10-10 spec audit

- Rewrote the spec as a statement of the implemented design and linked the event-system document as the record of helpers, variables and UI.
- Removed the completed documentation-update list, completion standard and helper-naming instructions, and the obsolete root forwarder and goal prompt whose work is implemented.
- Pass 2 review: retained the formula, because it keeps the combined major chance per roll stable without adding a player-facing meter; the only visible values (baseline and current gain) already drive the setting the player controls.
