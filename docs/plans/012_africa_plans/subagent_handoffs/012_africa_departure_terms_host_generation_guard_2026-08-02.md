# Event 012 departure-terms host-generation guard

## Scope

The priority-member departure surface now fails closed during host succession or explicit transfer windows without adding tags, stores, or new relationship states.

## Change

`africa_priority_member_can_open_departure_terms` now requires a live committed `event_target:africa_host` and `africa_member_host_generation_is_current`. The decision and event both consume this shared trigger, so stale UI exposure and stale event dispatch are blocked together.

## Validation

The trigger matches the existing registration, politics, League, and post-settlement gates. The downstream departure transition remains unchanged and still handles consent, autonomy, rivalry, and cleanup. Static source review found no new references or duplicate identifiers; live host-transfer and withdrawal scenarios remain required for campaign acceptance.
