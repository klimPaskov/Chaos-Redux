# Major Event Weights

Major event weights use the configured gain in `global.major_event_weight_per_minor`.
The default is `constant:event_system_defaults.major_event_weight_per_minor`, and Advanced Settings can change the configured value.

## Accumulation and eligibility

`update_major_event_weights` assigns `global.minor_events_since_major × global.major_event_weight_per_minor` to every unfired major event.
Disabled or temporarily unavailable majors retain that progress and receive it when they become eligible.
Locked Event 91 remains the historical exception until `communism_spread_world_revolution_unlocked` is set.
Ordinary event eligibility still controls selection, so stored weight does not bypass a Chaos-level, target, disabled, fired, or world-state gate.
Fired and reset major entries retain the engine-safe inactive floor.

`calculate_dynamic_major_weight_gain` retains its name for existing status, settings, and welcome-screen callers.
It publishes the configured gain in `global.current_dynamic_major_weight_gain` and refreshes active pool counts for diagnostics.
The counts do not change the gain or accumulated weight.
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
Future balance work can compare the current weighted pool under declared scenarios without changing these accumulation rules.
