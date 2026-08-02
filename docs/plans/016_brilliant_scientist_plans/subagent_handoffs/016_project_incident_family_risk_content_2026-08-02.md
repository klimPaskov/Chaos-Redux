# Event 016 project-incident family risk content handoff

Date: 2026-08-02

## Scope

This tranche deepens the existing `chaosx.nr16.13` report with one readable risk signature for every project family. It does not add a project, incident fire path, governance option, reward, asset, unit, model, or catalog row.

## Changed files

- `common/scripted_localisation/016_brilliant_scientist_directorate_scripted_localisation.txt`
  - Added `GetBrilliantScientistIncidentRiskClause`, mapping all fifteen family values plus an unresolved guard to visible localisation keys.
- `localisation/english/016_brilliant_scientist_directorate_outcomes_l_english.yml`
  - Added fifteen family-specific risk clauses and the unresolved fallback.
  - Inserted the clause into standard, major, and severe incident descriptions.
- `docs/events/016_brilliant_scientist/systems/projects.md`
  - Records that the incident report now names each family's failure signature while preserving shared governance resolution.

## Behavior

When an active family incident opens `chaosx.nr16.13`, the report still uses the existing dynamic family name, pressure band, deadline, recovery mission, and three governance postures. The new sentence explains the specific hazard for the current family. The family mission remains responsible for concrete equipment, fuel, manpower, factory time, damage, repair, deadline, and AI recovery. If the family value is absent or outside the mapped fifteen, the report uses a conservative unresolved sentence.

## Validation

- Confirmed all fifteen project-family constants are mapped exactly once and the unresolved branch is present.
- Confirmed the new scripted-localisation name is referenced only by the three existing incident descriptions.
- Confirmed the localisation file retains UTF-8 BOM encoding and has matching definitions for all new keys.
- No new event, decision, project, asset, unit, model, or recurring world iteration was introduced.

## Remaining risks

Dedicated accident, security, black-and-white news, and defeat/remnant art remain queued. Event 016-specific 3D production remains deferred as requested. Live consumer validation remains user-owned.
