# Event 006 Congress Volunteer Cadre Tranche Handoff

## Scope

Implemented a targeted New States Congress volunteer-cadre decision for Event 006 without touching flag assets, country definitions, or Event 005 Soviet Collapse systems.

## Files Changed

- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/decisions/006_independence_wave_decisions.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `docs/events/006_independence_wave.md`

## Identifiers

- Decision: `independence_wave_send_congress_volunteer_cadre`
- Trigger: `can_independence_wave_send_congress_volunteer_cadre`
- Effect: `independence_wave_send_congress_volunteer_cadre_effect`
- Script constants: `independence_wave_decision.congress_volunteer_cadre_*`
- State flags: `independence_wave_sent_congress_volunteer_cadre`, `independence_wave_received_congress_volunteers`
- Tracking variable: `global.chaosx_iw_congress_volunteer_cadre_count`

## Behavior

- Any independent Event 006 release that opened the New States Congress and sent delegates can target another delegate state from `global.independence_wave_released_countries`.
- The sending government spends command power, available manpower, and infantry equipment.
- The target receives manpower, infantry equipment, militia strength, coalition cohesion, and foreign attention.
- The target must be a different Event 006 release that has sent delegates, has not already received Congress volunteers, and is either at war or below the starting militia-strength threshold.
- AI weighting favors revolutionary and compact-member governments, active-war targets, and reduces patron-cabinet senders.

## Validation Notes

- Static brace-balance validation passed for Event 006 constants, scripted triggers, scripted effects, decisions, and decision categories.
- Checked the bounded Event 006 tranche files for unsupported `<=` / `>=`; none found.
- Localisation remains UTF-8 with BOM and has no `:0` keys.
- `git status --short -- gfx/flags common/countries history/countries` returned no changes.
- `chaosx_decision_mission_auditor` reviewed the tranche and patched the sender/target independence gates; see `2026_05_30_event006_congress_volunteer_cadre_decision_audit.md`.
- No flag asset or country-history paths are part of this change.

## Remaining Risks

- This is a bounded Congress cooperation tranche. It does not claim completion for the full Event 006 spec pack.
