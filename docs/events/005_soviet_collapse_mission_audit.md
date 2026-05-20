# Event 005 Soviet Collapse Mission Audit

Audit date: 2026-05-20

## Mission Catalogue

The active Soviet crisis board contains 118 manually activated missions. The full 118-row mission table is maintained in `docs/events/005_soviet_union_collapse_mission_audit.md`; this file is the required current-path audit for the serious completion pass.

Verifier evidence:

- `soviet_objective_board_surface`: 118 missions, 118 activation refs, 118 completion payloads, 118 timeout payloads, 118 done-flag refs, 10 active mission cap.
- `mission_quality_surface`: 118 unique available blocks, zero weak available blocks, zero identical success/failure outcomes, zero raw division-state available blocks, zero long inline availability blocks, 117 map or state requirements.
- `mission_requirement_surface`: 118 scripted requirement refs, zero thin requirements, zero meter-only requirements, zero passive-only requirements, zero forbidden trivial literal thresholds, four division-position tooltips with localisation.
- `decision_tooltip_surface`: 118 mission-specific requirement tooltips; no direct raw trigger blocks exposed in mission UI.
- `terminal_mission_cleanup`: all 118 missions removed on terminal collapse.

## Family Coverage

| Category | Mission count |
| --- | ---: |
| Authority | 9 |
| Cleanup | 7 |
| Command | 21 |
| Depot | 10 |
| Foreign | 22 |
| League | 8 |
| Legal | 3 |
| Old Movement | 17 |
| Rail | 11 |
| Settlement | 10 |

## Clarity Requirements

Mission localisation uses named mission requirement keys such as `<mission_id>_req_tt`, with actual scripted triggers hidden behind `custom_trigger_tooltip`/`hidden_trigger`. Division-state missions name concrete state groups in localisation, for example:

- Moscow, Arkhangelsk, Leningrad, and Pskov for the Northern Signal Offices.
- Moscow and Arkhangelsk for the Capital Ministry Belt.
- Moscow, Smolensk, and Minsk for the Western Courier Belt.
- Moscow, Smolensk, Minsk, and Azerbaijan for loyal military districts.

The audit rejects generic text such as `required states` as proof of completion unless a named region or state list is present in the mission tooltip.

## Duplicate Cleanup Result

Passive stockpile, stability-only, war-support-only, manpower-only, and generic waiting missions are absent from the active mission surface after recursive scripted-trigger expansion. Stockpiles and meters can still appear as costs, scaling values, or supporting conditions, but no mission completes from those alone.

## Verification Command

```text
python3 .tools/verify_event005_completion_gate.py --allow-missing-continuation-spec
```

Result: exit 0.
