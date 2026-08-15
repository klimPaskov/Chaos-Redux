# Event 12 Manual Trigger Repair Handoff

## Outcome

Event 12 can be launched from Event Details or the Settings manual trigger without weakening its normal opening contract.

## Root Cause

The visible availability check admitted a country with one opening contact, while the real prefire selector requires a frozen roster of three valid contacts. A failed attempt could also leave stale frozen-roster state that poisoned later manual retries.

## Implementation

`africa_prepare_manual_event_fire` marks a bounded manual prefire context, clears stale selected-host roster state, selects an eligible host, and rebuilds the host's frozen contact roster. Dispatch proceeds only when `africa_prefire_ready` is true, the selected host remains valid, and the normal three-contact contract is satisfied. Event Details and Settings manual triggers both set the shared manual-dispatch marker before calling `fire_event_by_temp_id_no_cluster`; automatic firing still uses `africa_prepare_random_event_fire`.

The repair is implemented in `common/scripted_effects/012_africa_effects.txt`, `common/scripted_triggers/012_africa_triggers.txt`, `common/scripted_effects/chaosx_settings_effects.txt`, and `common/scripted_guis/chaosx_scripted_gui_events_log.txt`.

## Validation

The Event 12 MCP inspection and render completed with no blocking target diagnostics. Workspace-wide helper projection was partial because of the installed adapter's large-workspace limit. Source validation confirms that failed selection closes dispatch before `chaosx.nr12.1`, while valid manual selection reaches the same initialization contract as automatic firing.

No fallback, reduced contact count, or alternate event root was introduced.
