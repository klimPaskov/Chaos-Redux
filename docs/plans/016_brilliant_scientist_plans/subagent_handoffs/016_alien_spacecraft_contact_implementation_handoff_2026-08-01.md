# Event 016 alien spacecraft contact implementation handoff

## Scope

This tranche closes the accepted Event 036 spacecraft evidence bridge without adding a new project reward, route, evolution, event-log entry, asset, or 3D model.

## Changed files and identifiers

- `events/036_alien_spacecraft.txt` now writes `brilliant_scientist_alien_spacecraft_recovered` in the authenticated `chaosx.nr36.2` outcome and asks the Event 016 scheduler to inspect the recipient.
- `common/scripted_effects/016_brilliant_scientist_context_effects.txt` adds `brilliant_scientist_try_schedule_alien_spacecraft_contact`, clears its pending obligation during normal context cleanup, and removes the impossible opening-only guard from the analogous Antarctic scheduler so Event 025 can resolve after appointment.
- `common/scripted_effects/016_brilliant_scientist_effects.txt` calls the scheduler after host initialization, covering spacecraft recovery before appointment.
- `events/016_brilliant_scientist.txt` adds the one-time report `chaosx.nr16.18` with `GFX_report_event_alien_spacecraft`.
- `localisation/english/016_brilliant_scientist_l_english.yml` adds the report text and bounded effect tooltip.
- `common/script_constants/016_brilliant_scientist_directorate_constants.txt` adds `alien_spacecraft_contact_report_days`.
- The Event 016 overview, project table, specification parts 3 and 7, and the project identifier map now describe the live bridge.

## Runtime contract

Event 036 sets the physical evidence flag on the country that recovered the spacecraft. If that country is the active Kruger host, the scheduler sets `brilliant_scientist_alien_spacecraft_contact_pending` and queues `chaosx.nr16.18` after the shared one-day report delay. Host initialization performs the same check so recovery before appointment is order-independent.

The report requires the current host, the physical recovery flag, the pending receipt, and no prior report receipt. Its single option clears the pending receipt and sets `brilliant_scientist_alien_spacecraft_contact_report_seen`. It does not advance Alien Arms, grant resources or units, make an origin conclusion, create a claim, write the Event Log, or enable an evolution.

The physical recovery flag remains on the recovering country and is intentionally not copied by Kruger transfer or Kruger State formation. Transfer cleanup clears only a delayed Event 016 presentation obligation, so stale reports cannot appear after Kruger leaves.

## Validation evidence

- Direct source inspection found one authenticated Event 036 outcome and one existing Alien Arms consumer before the patch, with zero gameplay writers for the recovery flag.
- The new `chaosx.nr16.18` namespace and localisation keys were free before implementation.
- The report reuses the registered `GFX_report_event_alien_spacecraft` sprite and its existing DDS, so no new asset or model dependency was introduced.
- The previous Antarctic scheduler guard was corrected because `brilliant_scientist_initialize_host_state` sets `brilliant_scientist_event_resolved` before invoking cross-event schedulers; `brilliant_scientist_is_current_host` remains the active-host gate.

## Remaining risks

The Event 036 report is intentionally limited to the authenticated spacecraft outcome. Foreign expeditions, broader alien recognition, bespoke report art, quantitative balance, and live in-game acceptance remain outside this tranche.
