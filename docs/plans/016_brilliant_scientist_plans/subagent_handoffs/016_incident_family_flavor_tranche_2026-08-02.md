# Event 016 incident-family flavour tranche handoff

Date: 2026-08-02

Mode: parent-owned bounded content implementation. No 3D models, new events, new missions, new receipts, new resources, or new project effects were added.

## Scope

The existing `chaosx.nr16.13` project-incident report already selected a severity description, a family risk sentence, and a host-archetype clause. This tranche adds one additional family-specific presentation clause between the risk sentence and the existing recovery instructions.

The selector `GetBrilliantScientistIncidentFamilyClause` groups the fifteen mapped families into six readable surfaces:

| Selector group | Families | Localisation key |
| --- | --- | --- |
| Machine | computation, electronics, robotics | `brilliant_scientist_incident_family_machine` |
| Physical plant | materials, rocketry, high energy | `brilliant_scientist_incident_family_physical_plant` |
| Biological chain | biomedical, cloning, biological weapons | `brilliant_scientist_incident_family_biological_chain` |
| Living reserve | paleogenetics, xenobiological synthesis | `brilliant_scientist_incident_family_living_reserve` |
| Boundary | teleportation, temporal | `brilliant_scientist_incident_family_boundary` |
| Interface | alien arms, Strategic Singularity | `brilliant_scientist_incident_family_interface` |

Unknown or migrated family values use `brilliant_scientist_incident_family_unresolved` and keep the existing incident resolver safe.

## Changed files

- `common/scripted_localisation/016_brilliant_scientist_directorate_scripted_localisation.txt`
- `localisation/english/016_brilliant_scientist_directorate_outcomes_l_english.yml`
- `docs/events/016_brilliant_scientist/overview.md`
- `docs/events/016_brilliant_scientist/systems/projects.md`
- `docs/plans/016_brilliant_scientist_plans/016_core_runtime_handoff_map.md`
- `docs/specs/016_brilliant_scientist_specs/handoffs/016_completion_status.md`

## Invariants

- `chaosx.nr16.13` keeps its existing trigger, severity selection, family variable, mission deadline, option effects, receipts, and picture selector.
- The clause is presentation-only and does not alter Mandate, Dependence, Exposure, Capacity, Independent Capacity, Grievance, project stage, recovery outcome, AI weight, or event-log state.
- No new fallback was introduced: unresolved family values receive an explicit neutral sentence and retain the dossier picture through the existing selector.

## Validation

- Confirmed the localisation file retains its UTF-8 BOM.
- Confirmed all seven new localisation keys are referenced by the scripted selector.
- Focused Event Inspector for `chaosx.nr16.13` remains the relevant runtime inspection; no event source or option graph was changed beyond description text and the selector helper.

## Remaining boundary

Broader country-specific chains, quantitative balance evidence, live consumer acceptance, and the seven Event 016-specific 3D packages remain open. Models were intentionally not produced.
