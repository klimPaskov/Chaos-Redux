# Major Event Weights

Major event weights use the configured gain in `global.major_event_weight_per_minor`.
The default is `constant:event_system_defaults.major_event_weight_per_minor`, and Advanced Settings can change the configured value.

## Accumulation and eligibility

`update_major_event_weights` adds the current pool-sensitive gain to the saved weight of every unfired major event.
Changing the configured gain or active pool affects subsequent increments and never recomputes previous progress.
Disabled or temporarily unavailable majors retain that progress and receive it when they become eligible.
Locked Event 91 remains the historical exception until `communism_spread_world_revolution_unlocked` is set.
Ordinary event eligibility still controls selection, so stored weight does not bypass a Chaos-level, target, disabled, fired, or world-state gate.
Fired and reset major entries retain the engine-safe inactive floor.

`calculate_dynamic_major_weight_gain` retains its name for existing status, settings, and welcome-screen callers.
It publishes the next increment in `global.current_dynamic_major_weight_gain` and refreshes active pool counts.
When both pools have eligible entries, the increment is the configured gain multiplied by `active_non_major / active_major` and `baseline_major / baseline_non_major`, rounded and clamped to the existing Advanced Settings gain bounds.
The tuning anchors live in `event_system_dynamic_major_gain`.
When either pool is empty, the configured gain remains available for accumulating minor-event progress toward later major eligibility.
Merely viewing settings or diagnostics never erases accumulated weight.
The global current-major-weight display accumulates the same increments and resets only through the major pacing lifecycle.
`apply_dynamic_major_weight_gain_after_minor` is a compatibility entry to the same accumulation helper.

## Cluster pacing

Each successful fixed-member cluster contributes one global event count and one repeatable recovery update.
Pacing follows the registered cluster type.
One-time and repeatable clusters apply one minor update even when their initial or delayed member is a major.
A registered major cluster applies one major reset.
Member dispatch records fired state and history without another batch pacing update.
Acid Rain reservation and delayed-queue cleanup remain independent of pacing.
Random Stuff remains a post-minor batch and contributes no second aggregate update.
Its actually dispatched major draws retain their own major reset as part of the later whole-pool mechanic.

## Tuning and scope

The country-scope helpers read the shared major-event registry, fired-event registry, minor count, configured gain, and Event 91 unlock flag.
Their outputs are the major weights and `global.current_major_event_weight`.
No persistent event target is required.
Major resets clear accumulated progress, and delayed queue cleanup removes any historical Acid Rain pacing receipt.

## Icons and future work

Existing settings, welcome-screen, and Event Logs assets are reused.
No new icon is required.
At the default gain of 150 and the 10-major/90-non-major anchors, three minor updates give 450 score per unfired major.
Five eligible majors with 90 non-majors give 300 per update, while 20 majors give 75.
These are selection scores, and actual selection probability depends on all selectable weights.
An unavailable major keeps the same increments but remains unselectable until its ordinary gates pass.
Future balance work can compare changing pool composition under declared scenarios.
