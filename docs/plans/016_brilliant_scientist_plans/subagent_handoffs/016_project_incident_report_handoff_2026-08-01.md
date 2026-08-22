# Event 016 project incident report handoff

Date: 2026-08-01

## Scope

This bounded content tranche adds one ordinary report for the existing family-specific project accident system. It does not add an evolution, a project family, a second project reward, a super-event, a catalog row, a new asset, or a 3D model.

## Changed files

- `common/script_constants/016_brilliant_scientist_directorate_constants.txt`
- `common/script_constants/016_brilliant_scientist_containment_constants.txt`
- `common/scripted_effects/016_brilliant_scientist_project_effects.txt`
- `common/scripted_effects/016_brilliant_scientist_containment_effects.txt`
- `common/scripted_effects/016_brilliant_scientist_effects.txt`
- `common/scripted_localisation/016_brilliant_scientist_directorate_scripted_localisation.txt`
- `events/016_brilliant_scientist_project_incident_events.txt`
- `localisation/english/016_brilliant_scientist_directorate_outcomes_l_english.yml`
- `docs/events/016_brilliant_scientist/overview.md`
- `docs/events/016_brilliant_scientist/systems/projects.md`

## Runtime contract

`brilliant_scientist_begin_family_project_incident` persists the active family and stage, clears the previous incident posture, sets a one-shot pending report flag, and schedules `chaosx.nr16.13` after `constant:brilliant_scientist_directorate_timing.incident_report_days`. The event requires a live incident, pending report, valid Event 016 carrier, and no world-end state.

The event uses the existing `GFX_report_event_016_brilliant_scientist_directorate_dossier` image. Its dynamic project name comes from `GetBrilliantScientistIncidentProjectName`, which maps all fifteen family values and has an unresolved fallback. Standard, major, and severe descriptions are selected from accident pressure bands.

The three options resolve only the report gate and causal posture. Public notice changes Mandate, Exposure, Capacity, Independent Capacity, and Grievance. State security changes Mandate, Dependence, Exposure, Capacity, and Grievance. A Kruger-led cordon changes Dependence, Exposure, Independent Capacity, and Grievance. The family mission remains responsible for concrete equipment, fuel, manpower, factory time, deadline, damage, repair, and AI recovery.

The selected report posture feeds the existing containment score. Public notice and state security add government-side containment evidence. A Kruger-led cordon adds Kruger-side containment evidence. The active mission remains the sole dangerous-project incident flag, so the report cannot be replayed or create a second incident.

Transfer reconciliation clears an unshown pending report on the former host. Resolution and timeout also clear the pending gate, preventing an orphaned event after the incident is no longer actionable.

## Validation evidence

- The new event ID `chaosx.nr16.13` is unique across Event 016 event files.
- Every new event title, description, option, tooltip, scripted-localisation, and constant key has a matching definition.
- All touched Clausewitz files have balanced braces and no unsupported `<=` or `>=` operators.
- Localisation remains UTF-8 with BOM and contains no duplicate keys.
- The existing dossier image is reused, so no asset production or unwired sprite registration was introduced.
- No HOI4 game launch or live-save validation was performed. The user owns live acceptance.

## Deferred boundaries

Dedicated accident, security, black-and-white news, and defeat/remnant art remain queued. The unit-model backlog covers portal raiders, clone infantry, autonomous robots, paleogenetic beasts, xenobiological assault organisms, generic alien infantry, and temporal guards; installed packages and current blockers are tracked in their model handoffs.
