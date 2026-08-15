# Event 12 Manual Trigger Repair Handoff

## Superseded host gate

The later African-capital eligibility decision supersedes this handoff's three-contact and dedicated-SAF entry requirements. Manual and automatic launch now share the same host rule: an existing country whose current capital is in Africa. Frozen contacts remain opening content, may contain zero to five governments, and never determine host eligibility. The stale-context cleanup and shared manual-dispatch boundary described below remain authoritative.

## Outcome

Event 12 can be launched from Event Details or the Settings manual trigger without weakening its normal opening contract.

## Root Cause

The visible availability check admitted a country with one opening contact, while the real prefire selector requires a frozen roster of three valid contacts. A failed attempt could also leave stale frozen-roster state that poisoned later manual retries.

## Implementation

`africa_prepare_manual_event_fire` marks a bounded manual prefire context, clears stale selected-host roster state, selects an eligible African-capital host, and rebuilds the host's frozen contact roster. Dispatch proceeds when `africa_prefire_ready` is true and the selected country still has its capital in Africa. Contact count and the specialised South African exile-patron proof do not control dispatch. Event Details and Settings manual triggers both set the shared manual-dispatch marker before calling `fire_event_by_temp_id_no_cluster`; automatic firing still uses `africa_prepare_random_event_fire`.

The repair is implemented in `common/scripted_effects/012_africa_effects.txt`, `common/scripted_triggers/012_africa_triggers.txt`, `common/scripted_triggers/012_africa_rsa_triggers.txt`, `common/scripted_effects/chaosx_settings_effects.txt`, and `common/scripted_guis/chaosx_scripted_gui_events_log.txt`.

## Validation

The Event 12 MCP inspection and render completed with no blocking target diagnostics. Workspace-wide helper projection was partial because of the installed adapter's large-workspace limit. Source validation confirms that failed selection closes dispatch before `chaosx.nr12.1`, while valid manual selection reaches the same initialization contract as automatic firing.

No alternate event root was introduced. The later eligibility decision deliberately accepts a reduced or empty contact roster and supplies unmapped African-capital countries with the defined compact capital-only package.
