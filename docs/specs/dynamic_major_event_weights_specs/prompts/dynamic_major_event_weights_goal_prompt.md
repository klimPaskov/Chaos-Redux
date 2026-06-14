/goal Implement dynamic major event weight gain for Chaos Redux.

Read and follow AGENTS.md, chaos-redux-events, chaos-redux-subagents, and chaosx_scripted_system_architect guidance. Use the spec at docs/specs/dynamic_major_event_weights_specs/dynamic_major_event_weights_spec.md as the source design.

Replace the fixed major-event weight gain with a dynamic formula:

```text
dynamic_major_gain = base_major_gain * (current_non_major_count / current_major_count) / (baseline_non_major_count / baseline_major_count)
```

Baseline is 100 active events, 10 major events, 90 non-major events, and default baseline gain 150. This means 90 non-major and 10 major must still produce 150. If there are 91 non-major and 10 major, the gain should be about 152. Use the player-configured major event weight setting as the baseline gain, not a hardcoded 150.

Count only current active random-pool entries. Do not count disabled events, fired fire-once events, fired major events, hidden helper events, news/follow-up/bootstrap events, triggerable scenario wrappers, or permanently unavailable events. Repeatable events still count if they remain in the pool.

If current_major_count is 0, skip major gain and do not divide by zero. If current_non_major_count is 0, skip gain or set it to 0. Clamp the calculated value to the current safe setting range.

Create reusable scripted helper logic instead of duplicating the math. Prefer helper names like calculate_dynamic_major_weight_gain and apply_dynamic_major_weight_gain_after_minor unless repo naming suggests better names. Store the current calculated gain in a variable that status/debug UI can display.

Event clusters must still count as one global pacing event. A cluster with multiple members applies the dynamic major gain only once.

Update relevant localisation and UI so the old fixed +150 wording is gone. The settings value should be described as the configured baseline major gain. Where the UI shows the value, show the current calculated gain or clearly distinguish baseline from current calculation.

Update relevant docs now, including CHAOS_REDUX_MECHANICS.md and every docs/systems file that describes major event weight gain, settings numeric inputs, debug/status displays, or cluster pacing. If new dynamic helpers are added, update the matching helper documentation.

Validate the mechanic with these cases: 90 non-major and 10 major gives 150, 91 non-major and 10 major gives about 152, 90 non-major and 11 major gives about 136, 91 non-major and 9 major gives about 169, 0 major does not divide by zero, disabled events do not affect the count, fired majors and fired fire-once minors do not affect the count, repeatables still count when active, and cluster firing applies gain once.

Keep iterating until the implementation, UI, localisation, docs, and validation satisfy the spec. Do not claim completion while any fixed +150 application remains active except as the baseline setting. Report files changed, helper names, UI/docs changed, validation results, rounding choice, and any simplifications or blockers.
