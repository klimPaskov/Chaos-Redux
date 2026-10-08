# Dynamic Major Event Weight Gain Spec

## Purpose

Major event weight gain should no longer be a fixed `+150` per minor pacing event. The system should keep the old behaviour as the baseline, but calculate the actual major weight gain from the current event pool composition.

The old baseline remains:

- 100 total active events.
- 10 active major events.
- 90 active non-major events.
- 150 major weight gain per minor pacing event.

The new behaviour should preserve that baseline exactly, then adjust when the event pool ratio changes.

## Core formula

Use the ratio of active non-major events to active major events.

```text
dynamic_major_gain = base_major_gain * (current_non_major_count / current_major_count) / (baseline_non_major_count / baseline_major_count)
```

Baseline constants:

```text
base_major_gain = configured major event gain, default 150
baseline_total_events = 100
baseline_major_events = 10
baseline_non_major_events = 90
baseline_ratio = 90 / 10 = 9
```

Default simplified formula:

```text
dynamic_major_gain = 150 * (current_non_major_count / current_major_count) / 9
```

If the player changes the configured major event gain from 150 to another value, the formula must scale from that configured value instead of hardcoding 150.

## Behaviour examples

| Active total events | Active major events | Active non-major events | Dynamic gain | Meaning |
| --- | ---: | ---: | ---: | --- |
| 100 | 10 | 90 | 150 | Baseline unchanged. |
| 101 | 10 | 91 | 151.67, round to about 152 | More non-major events per major means majors need slightly faster growth. |
| 100 | 9 | 91 | 168.52, round to about 169 | Fewer available majors means each remaining major should build faster. |
| 101 | 11 | 90 | 136.36, round to about 136 | More available majors means each major should build slower. |

## Counting rules

The calculation must use the current active random event pool, not a static event catalog count.
One counted entry is one source event in the existing random-pool registry, regardless of how many reports, helpers, countries, or follow-ups that source can produce.
The pool owner determines whether an entry is currently participating; this feature consumes that result rather than creating a second eligibility or reservation registry.
Record whether an exclusion is permanent retirement or a temporary owner-controlled suspension, and preserve the owner's reenabling behavior.
Low recovering weight alone is not removal, and a status refresh cannot add a pacing receipt, alter a weight, retire an entry, or activate a pending event.

Count as current major events:

- Major events that are still valid pool entries.
- Major events that are enabled.
- Major events that have not already fired or been permanently removed.

Do not count as current major events:

- Disabled major events.
- Fired major events.
- Major events unavailable because their required target or permanent condition is impossible.

Count as current non-major events:

- Enabled minor repeatable events that remain valid pool entries.
- Enabled minor fire-once events that have not fired yet and remain valid pool entries.
- Enabled non-major cluster member source events if they remain in the normal random event pool.

Do not count as current non-major events:

- Disabled minor events.
- Fired fire-once events.
- Events that are permanently unavailable.
- Events that exist only as hidden helpers, follow-ups, news popups, bootstrap events, triggerable scenario wrappers, or internal subevents.

Repeatable events should still count if they remain part of the pool, even if their current weight is low after firing.

## Safety rules

If `current_major_count` is 0, skip major weight gain entirely. Do not divide by zero.

If `current_non_major_count` is 0, skip major weight gain or set the dynamic gain to 0.

Clamp the final dynamic gain to the same safe range as the current major event gain setting, normally 0 to 10000 unless the current implementation uses a different range.

Round or floor the final value consistently with the existing weight system. Prefer rounding to the nearest whole number if the existing script can support it cleanly. If the engine path makes integer truncation safer, document that choice and make the examples in docs match the actual behaviour.

## Timing of recalculation

The dynamic gain should be recalculated only when needed.

Required timing:

- Recalculate immediately before major event weights increase after a minor pacing event, using the pool state at that existing accounting point after the firing's owner-controlled membership changes.
- Use that one calculated gain for the one pacing receipt; follow-up reports and status refreshes do not recalculate and apply an additional gain.
- Recalculate when the status or debug UI displays the current major gain.
- Recalculate when settings or event list views need to show the current value.

Avoid daily recalculation unless the existing system already rebuilds a matching status cache daily. This feature should not add a new daily all-country or all-event performance cost.

## Event clusters

A fired cluster still counts as one global pacing event.

If a cluster contains several member events, apply the dynamic major weight gain only once for the cluster firing.
Member events may still apply their own effects, fire-once removal, repeatable cap changes, logs, and details, but they must not each add major weight.
A member remains a counted source only if the normal pool owner still includes it; a cluster wrapper is not an extra source entry.

[Event 026's reservation and lifecycle](../../026_black_friday_specs/026_black_friday_spec_part_2_friday_reservation_and_lifecycle.md#event-system-pacing) supplies the delayed-activation case.
Reservation removes Black Friday from live selection without recording a firing or adding major gain.
A different minor event that fires while it is reserved uses the pool's current membership at its own pacing receipt.
Eligible Friday activation supplies one normal fire-once pacing receipt using the pool state at activation, while its hidden activation, report, and expiry roles add none.
Cancellation or a below-threshold Friday adds none; it follows Event 026's existing reservation and reenabling rules.
The weight helper must neither activate the sale nor reset its selecting timer.
When Event 026 is absent or disabled, the same ordinary pool and pacing contract applies without a reservation adapter.

## Settings behaviour

The existing `Major Event Weight` setting should become the baseline gain setting.

Player-facing meaning:

```text
Major Event Weight controls the baseline major gain used when the active pool ratio is 90 non-major events to 10 major events.
```

The current calculated dynamic value should be shown somewhere useful in the status or debug UI if the old fixed value is currently shown.

The UI should not imply that every minor always adds exactly the configured value. It should distinguish the configured baseline from the current calculated gain.

## Helper design

Do not duplicate this math inline.

Create reusable scripted logic, with names close to these unless the existing repo naming pattern suggests better names:

```text
calculate_dynamic_major_weight_gain
apply_dynamic_major_weight_gain_after_minor
```

Expected helper responsibilities:

- Count active major events.
- Count active non-major events.
- Read the configured baseline gain.
- Apply the ratio formula.
- Clamp the result.
- Store the current calculated gain in a readable global variable for status and debug surfaces.
- Apply the calculated gain to eligible major events after a minor pacing event.

If the existing event pool already has helper arrays or count variables, reuse them instead of creating a second registry.

If a new dynamic helper is added, document it in the matching dynamic effects documentation file.

## Constants and tuning

Use script constants for baseline tuning values where the repo pattern supports them.

Recommended constants:

```text
baseline_total_events = 100
baseline_major_events = 10
baseline_non_major_events = 90
baseline_non_major_major_ratio = 9
minimum_dynamic_major_gain = 0
maximum_dynamic_major_gain = 10000
```

The implementation should avoid scattering these values across logic, localisation, UI, docs, and tests.

## Documentation updates required

Update every relevant repo doc that still describes major event weight gain as a fixed `+150` per minor event.

At minimum, update:

- `CHAOS_REDUX_MECHANICS.md`, especially Event Classification, Advanced Settings, and Debug and Monitoring references.
- Any event-system docs under `docs/systems/` that describe major event weight gain.
- Any settings docs that describe the `Major Event Weight` numeric input.
- Any event log, status tab, or debug docs that show major gain as a fixed value.
- `docs/systems/event_system/event_clusters.md` or equivalent cluster docs if they mention that clusters affect major weights.
- `common/scripted_effects/chaosx_dynamic_effects.md` if new dynamic helper effects are added there.

The docs should explain that 150 is the baseline gain at the baseline pool ratio, not an always-fixed gain.

## Localisation and UI wording

Update localisation where the old wording implies a fixed value.

Preferred wording direction:

```text
Configured baseline major gain: [?global.major_event_weight_baseline]
Current calculated major gain: [?global.current_dynamic_major_weight_gain]
```

The exact variable names should follow the implementation.

Avoid player-facing update-history wording such as `new dynamic system`, `recently changed`, or `fixed from old +150`.

## Validation requirements

The completion report must show meaningful validation for this mechanic.

Required cases:

| Case | Expected result |
| --- | --- |
| 90 active non-major, 10 active major | Dynamic gain is 150 when baseline gain is 150. |
| 91 active non-major, 10 active major | Dynamic gain is about 152. |
| 90 active non-major, 11 active major | Dynamic gain is about 136. |
| 91 active non-major, 9 active major | Dynamic gain is about 169. |
| 0 active major | No divide by zero. Gain is skipped. |
| 0 active non-major | Gain is skipped or 0. |
| Disabled events | Disabled events do not affect the count. |
| Fired major events | Fired major events do not affect the current major count. |
| Fired fire-once minor events | Fired fire-once minor events do not affect the current non-major count. |
| Repeatable event at low recovering weight | Still counts if it remains in the active pool. |
| Cluster firing | Dynamic gain applies once after owner-controlled member accounting; the wrapper and member reports add no extra gain. |
| `dmg_pool_membership` | Low recovering weight remains counted; temporary exclusions and reenabling match the existing pool owner's decisions without becoming permanent removal. |
| `dmg_black_friday_wait` | Reservation removes only Event 026 from participating sources, gives no gain, and does not prevent another minor from supplying its own one gain. |
| `dmg_black_friday_activate` | Eligible Friday activation records one gain from the activation-time pool; same-day activation, hidden reports, and expiry cannot add another. |
| `dmg_black_friday_cancel` | Disable/cancellation and below-threshold Fridays give no gain; reenabling follows Event 026 without restoring an old reservation. |
| `dmg_readonly_status` | Opening or refreshing existing status displays shows the current calculation without applying gain, changing weights, or activating pending events. |

These named cases are future validation scenarios, not executed probability evidence.
Before any weighted-source patch, the parent routes the actual candidate pool, owner eligibility inputs, and immutable source baseline through `chaosx_ai_probability_auditor` for inspection and evaluation, then uses matching scenarios for the mandatory post-patch comparison.
Unknown eligibility or native timing remains unresolved rather than inferred from these formula examples.

Validation should inspect real script paths and variables. Do not claim this is complete with only a calculator note.

## Completion standard

This task is complete only when:

- Fixed major gain application has been replaced by dynamic gain application.
- The configured major gain setting remains the baseline value.
- Dynamic gain uses the active non-major to active major ratio.
- Cluster pacing applies the gain only once.
- Disabled, fired, hidden helper, and permanently unavailable events are not counted incorrectly.
- Status or debug surfaces show the calculated value where relevant.
- Localisation no longer promises a fixed `+150` gain.
- Relevant docs are updated to describe the new behaviour.
- Meaningful validation covers the required cases.
- Any simplification, rounding choice, unsupported dynamic field, or fallback is reported clearly.
