# Event 016 Time-Traveler Reachability Handoff

## Scope

This tranche closes the two valid ordering paths for the Event 030 time-traveler bridge without creating a new project, evolution, log entry, or model dependency.

## Gameplay changes

- `common/scripted_effects/016_brilliant_scientist_context_effects.txt` adds `brilliant_scientist_try_schedule_time_traveler_contact`, guarded by the active host, the temporary `time_traveler` idea, world-end exclusion, and the existing contact/report receipts.
- `common/scripted_effects/016_brilliant_scientist_effects.txt` calls the helper during Kruger appointment initialization, so a traveler discovered before recruitment is not lost.
- `events/030_time_traveler.txt` uses the same helper for a traveler discovered after appointment and no longer rejects the bridge solely because the global Event 016 resolution flag is already set.

## Runtime contract

The helper is idempotent. It writes `brilliant_scientist_time_traveler_contact` and the pending receipt before scheduling `chaosx.nr16.16`; later calls see the receipt and do nothing. Event 030 keeps its ordinary idea, news, and country-specific hidden follow-ups.

## Validation evidence

- Source braces are balanced for the three gameplay files.
- The old global-resolution guard is absent only from the Event 030 bridge limit; appointment and report guards remain intact.
- Exact helper, event, and receipt IDs were checked after the edit.

## Remaining risks

Live timing before/after appointment remains user-owned validation. This tranche intentionally does not migrate physical artifacts, add a project reward, produce assets, or create 3D models.
