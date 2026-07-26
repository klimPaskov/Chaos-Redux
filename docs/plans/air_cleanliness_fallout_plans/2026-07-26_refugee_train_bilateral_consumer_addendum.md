# Refugee Train bilateral consumer addendum

Status: implemented as a dormant authored consumer on 2026-07-26.

This tranche consumes the existing Refugee Train reciprocal reservation without enabling the Fallout scheduler.

The reservation keeps two reviewed candidate registries paired through the existing bilateral arrays.

The initiator row stores an opening token pair at event ids `1019` and `1020`.

The responder row stores a response token pair at event ids `1021` and `1022`.

The existing bilateral dispatch source remains `bilateral_response` because the source already authenticates country-to-country delivery and cleanup.

The reconciler publishes an opening envelope only for a current initiator row with a current reciprocal, a reserved status, and a due date that has arrived.

The opening event authenticates the issued ticket, generation, role, token, status, and Refugee Train transaction key before moving both rows atomically from `reserved` to `response_pending`.

Human and hidden AI opening paths share the same terminalizer and use branch-specific Food, Recognition, and Cohesion costs.

The responder envelope is published only for the reciprocal responder row after the opening transition.

Human response choices resolve success, partial, or failure outcomes with distinct costs and resource effects.

Hidden AI response chooses an outcome from the initiator branch through a deterministic government-independent rule and uses the same issued resolver.

Both countries apply durable refugee memory, resource, stability, war-support, Air Winter, Supply Access, reclamation, exposure, state-flag, and dynamic-modifier effects after the pair commits.

The state target is recovered from each participant's current reviewed candidate row rather than a temporary last-selection pointer.

Resolved rows remain visible to the existing bilateral cleanup reconciler.

No new tag, diplomacy relation, province sweep, asset, sprite, audio path, or scheduler activation flag is introduced.

## Owned files

- `common/script_constants/fallout_world_end_event_constants.txt`
- `common/scripted_effects/fallout_world_end_event_effects.txt`
- `common/scripted_effects/fallout_world_end_refugee_train_event_effects.txt`
- `common/scripted_triggers/fallout_world_end_event_triggers.txt`
- `common/scripted_triggers/fallout_world_end_refugee_train_event_triggers.txt`
- `events/fallout_world_end_events.txt`
- `localisation/english/fallout_world_end_refugee_train_l_english.yml`

## Boundaries

This is a dormant authored consumer and not a release-floor credit claim.

The scheduler activation flags remain unset.

The exact engine behavior of dynamic array scope selection, native country-event issuance, save recovery, multiplayer host authority, and bilateral cleanup remains unobserved because HOI4 was not launched.

The four event blocks are outside the fifty-four reviewed ordinary candidate rows and do not increase the `0 of 660` countable release-floor total.

Separate Event Log payloads for this bilateral pilot are not claimed because the consumer remains dormant and the existing candidate identity remains the ordinary Refugee Train row.
